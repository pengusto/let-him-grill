import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("decision_state.py")
ROOT = SCRIPT.parent.parent
TEMPLATE = ROOT / "assets" / "decision-tree.html"
SKILL = ROOT / "SKILL.md"
REFERENCE_EXAMPLES = ROOT / "docs" / "examples"


class DecisionStateTest(unittest.TestCase):
    def run_cli(self, *args: str) -> None:
        subprocess.run([sys.executable, str(SCRIPT), *args], check=True)

    def assessment(
        self,
        option: str,
        triage: str = "recommended",
        risk: str = "low",
        reversible: bool = True,
    ) -> str:
        value = {
            "triage": triage,
            "reason": "Best fit for the stated constraints.",
            "confidence": 0.9,
            "reversible": reversible,
            "effort": "low",
            "risk": risk,
            "impact": "Keeps downstream work small.",
            "preferredWhen": "Prefer when simplicity matters most.",
        }
        return f"{option}={json.dumps(value)}"

    def test_auto_selects_only_a_safe_recommended_option(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory) / "state.json"
            self.run_cli("init", str(state), "--title", "Test")
            self.run_cli(
                "add", str(state), "--id", "storage", "--question", "Storage?",
                "--context", "State must remain inspectable across Codex tasks.",
                "--type", "auto", "--option", "json=JSON", "--option", "cloud=Cloud",
                "--assessment", self.assessment("json"),
                "--assessment", self.assessment("cloud", "situational", "medium", False),
            )
            self.run_cli(
                "add", str(state), "--id", "provider", "--question", "Provider?",
                "--type", "human", "--option", "one=One", "--option", "two=Two",
                "--assessment", self.assessment("one"),
                "--assessment", self.assessment("two", "solid-alternative"),
            )
            self.run_cli(
                "add", str(state), "--id", "region", "--question", "Region?",
                "--type", "blocked", "--option", "eu=EU", "--option", "us=US",
                "--assessment", self.assessment("eu", "situational"),
                "--assessment", self.assessment("us", "situational"),
            )

            nodes = {node["id"]: node for node in json.loads(state.read_text())["nodes"]}
            self.assertEqual(nodes["storage"]["choice"], "json")
            self.assertEqual(nodes["storage"]["context"], "State must remain inspectable across Codex tasks.")
            self.assertEqual(nodes["storage"]["actor"], "ai")
            self.assertIsNone(nodes["provider"]["choice"])
            self.assertEqual(nodes["provider"]["status"], "pending")
            self.assertIsNone(nodes["region"]["choice"])

            rendered = Path(directory) / "tree.html"
            self.run_cli("render", str(state), str(rendered))
            fragment = rendered.read_text()
            self.assertIn("Blocked", fragment)
            self.assertIn("State must remain inspectable across Codex tasks.", fragment)
            self.assertIn('"Context"', fragment)

            ambiguous = subprocess.run(
                [
                    sys.executable, str(SCRIPT), "add", str(state),
                    "--id", "ambiguous", "--question", "Ambiguous?", "--type", "auto",
                    "--option", "one=One", "--option", "two=Two",
                    "--assessment", self.assessment("one"),
                    "--assessment", self.assessment("two"),
                ],
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(ambiguous.returncode, 0)
            self.assertIn("exactly one", ambiguous.stderr)

    def test_excluded_option_cannot_be_selected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory) / "state.json"
            self.run_cli("init", str(state), "--title", "Test")
            self.run_cli(
                "add", str(state), "--id", "unsafe", "--question", "Unsafe?", "--type", "review",
                "--option", "safe=Safe", "--option", "unsafe=Unsafe",
                "--assessment", self.assessment("safe"),
                "--assessment", self.assessment("unsafe", "excluded", "high", False),
                "--choice", "safe",
            )
            result = subprocess.run(
                [
                    sys.executable, str(SCRIPT), "choose", str(state), "unsafe", "unsafe",
                ],
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("excluded", result.stderr)

    def test_revision_guard_rejects_a_stale_tree(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory) / "state.json"
            self.run_cli("init", str(state), "--title", "Revision")
            self.run_cli(
                "add", str(state), "--id", "storage", "--question", "Storage?",
                "--type", "review", "--option", "json=JSON", "--option", "sqlite=SQLite",
                "--assessment", self.assessment("json"),
                "--assessment", self.assessment("sqlite", "solid-alternative"),
                "--choice", "json",
            )
            self.assertEqual(json.loads(state.read_text())["revision"], 1)

            rendered = Path(directory) / "tree.html"
            self.run_cli("render", str(state), str(rendered))
            self.assertIn('"revision": 1', rendered.read_text())
            self.assertIn("const expectedRevision = state.revision ?? 0", rendered.read_text())

            self.run_cli(
                "add", str(state), "--id", "release", "--question", "Release?",
                "--type", "human", "--option", "now=Now", "--option", "later=Later",
                "--assessment", self.assessment("now"),
                "--assessment", self.assessment("later", "solid-alternative"),
            )
            self.assertEqual(json.loads(state.read_text())["revision"], 2)
            result = subprocess.run(
                [
                    sys.executable, str(SCRIPT), "choose", str(state), "storage", "sqlite",
                    "--expected-revision", "1",
                ],
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Stale state revision", result.stderr)
            self.assertEqual(json.loads(state.read_text())["nodes"][0]["choice"], "json")

    def test_rejects_native_schema_synonyms(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory) / "state.json"
            self.run_cli("init", str(state), "--title", "Test")
            self.run_cli(
                "add", str(state), "--id", "release", "--question", "Release?",
                "--type", "auto", "--option", "tag=Tag",
                "--assessment", self.assessment("tag"),
            )
            valid = json.loads(state.read_text())
            invalid_values = (
                ("status", "resolved", "Invalid type or status"),
                ("actor", "agent", "Invalid actor"),
                ("assessment-status", "current", "Invalid assessment status"),
            )
            for field, value, message in invalid_values:
                with self.subTest(field=field):
                    candidate = json.loads(json.dumps(valid))
                    if field == "assessment-status":
                        candidate["nodes"][0]["options"][0]["assessment"]["status"] = value
                    else:
                        candidate["nodes"][0][field] = value
                    state.write_text(json.dumps(candidate))
                    result = subprocess.run(
                        [sys.executable, str(SCRIPT), "render", str(state), str(Path(directory) / "tree.html")],
                        capture_output=True,
                        text=True,
                    )
                    self.assertNotEqual(result.returncode, 0)
                    self.assertIn(message, result.stderr)

    def test_rejects_cyclic_decision_dependencies(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory) / "state.json"
            assessment = json.loads(self.assessment("one").partition("=")[2])
            node = {
                "question": "Cycle?",
                "type": "review",
                "options": [{"id": "one", "label": "One", "assessment": assessment}],
                "choice": "one",
                "reason": "Test",
                "confidence": 0.9,
                "reversible": True,
                "status": "recommended",
                "actor": "ai",
            }
            state.write_text(json.dumps({
                "version": 2,
                "title": "Cycle",
                "nodes": [
                    node | {"id": "one", "dependsOn": ["two"]},
                    node | {"id": "two", "dependsOn": ["one"]},
                ],
            }))

            result = subprocess.run(
                [sys.executable, str(SCRIPT), "resume", str(state)],
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("must not contain a cycle", result.stderr)

    def test_change_invalidates_only_transitive_descendants(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory) / "state.json"
            self.run_cli("init", str(state), "--title", "Test")
            self.run_cli("add", str(state), "--id", "audience", "--question", "Audience?", "--type", "review", "--option", "dev=Developers", "--option", "team=Teams", "--assessment", self.assessment("dev"), "--assessment", self.assessment("team", "solid-alternative"), "--choice", "dev")
            self.run_cli("add", str(state), "--id", "storage", "--question", "Storage?", "--type", "review", "--option", "json=JSON", "--option", "sqlite=SQLite", "--assessment", self.assessment("json"), "--assessment", self.assessment("sqlite", "solid-alternative"), "--choice", "json", "--depends-on", "audience")
            self.run_cli("add", str(state), "--id", "architecture", "--question", "Architecture?", "--type", "human", "--option", "skill=Skill::Thin workflow wrapper", "--option", "plugin=Plugin::Installable bundle", "--assessment", self.assessment("skill"), "--assessment", self.assessment("plugin", "solid-alternative"), "--depends-on", "storage")
            self.run_cli("add", str(state), "--id", "unrelated", "--question", "Unrelated?", "--type", "auto", "--option", "yes=Yes", "--assessment", self.assessment("yes"))
            self.run_cli("choose", str(state), "audience", "team")

            nodes = {node["id"]: node for node in json.loads(state.read_text())["nodes"]}
            self.assertEqual(nodes["audience"]["status"], "confirmed")
            self.assertEqual(nodes["storage"]["status"], "invalidated")
            self.assertEqual(nodes["architecture"]["status"], "invalidated")
            self.assertEqual(nodes["unrelated"]["choice"], "yes")
            self.assertEqual(nodes["storage"]["options"][0]["assessment"]["status"], "invalidated")

            stale = subprocess.run(
                [sys.executable, str(SCRIPT), "choose", str(state), "storage", "sqlite"],
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(stale.returncode, 0)
            self.assertIn("reassess", stale.stderr)

            rendered = Path(directory) / "tree.html"
            self.run_cli("render", str(state), str(rendered))
            fragment = rendered.read_text()
            self.assertIn("sendFollowUpMessage", fragment)
            self.assertIn("Architecture?", fragment)
            self.assertIn("Thin workflow wrapper", fragment)
            self.assertIn("data-expand-all", fragment)
            self.assertIn("data-option-toggle", fragment)
            self.assertIn("Recommended", fragment)
            self.assertIn('input.disabled = excluded || invalidated', fragment)
            self.assertIn('const firstInvalidated = state.nodes.find', fragment)
            self.assertEqual(fragment.count('"status": "invalidated"'), 6)
            self.assertIn("Reassess path", fragment)
            self.assertIn("Reassess invalidated decision", fragment)

    def test_rendered_action_uses_codex_follow_up_bridge_with_safe_fallback(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory) / "state.json"
            self.run_cli("init", str(state), "--title", "Test")
            self.run_cli(
                "add", str(state), "--id", "release", "--question", "Release?",
                "--type", "review", "--option", "tag=Tag only", "--option", "page=Release page",
                "--assessment", self.assessment("tag"),
                "--assessment", self.assessment("page", "solid-alternative"),
                "--choice", "tag",
            )

            rendered = Path(directory) / "tree.html"
            self.run_cli("render", str(state), str(rendered))
            fragment = rendered.read_text()

            self.assertIn(f"const statePath = {json.dumps(str(state.resolve()))}", fragment)
            self.assertIn("await window.openai.sendFollowUpMessage({ prompt, title })", fragment)
            self.assertIn('sendToCodex(prompt, `Apply ${decisionCount}`, `${decisionCount} sent to Codex.`)', fragment)
            self.assertIn('customChoice.type = "radio"', fragment)
            self.assertIn('customChoice.checked = true', fragment)
            self.assertIn('querySelector("[data-custom-answer]")?.removeAttribute("open")', fragment)
            self.assertIn('const selections = new Map()', fragment)
            self.assertIn('let sending = false', fragment)
            self.assertIn('if (sending) return false', fragment)
            self.assertIn('apply.disabled = sending || count === 0', fragment)
            self.assertIn('selections.clear()', fragment)
            self.assertIn('selections.set(node.id, selection)', fragment)
            self.assertIn('const selectedItems = state.nodes.flatMap', fragment)
            self.assertIn('function formatDecisions(decisions)', fragment)
            self.assertIn('const decisionSummary = formatDecisions(decisions)', fragment)
            self.assertIn('Menschliche Entscheidungen:', fragment)
            self.assertIn('Arbeitsregeln:', fragment)
            self.assertIn('Formuliere eigene Antworten als kurze, klare Entscheidungsstatements um', fragment)
            self.assertIn('customInput.setAttribute("aria-label", `Own answer for: ${node.question}`)', fragment)
            self.assertIn('function editableAnswerSeed(node)', fragment)
            self.assertIn('querySelector("[data-option]:checked")', fragment)
            self.assertIn('option.assessment.triage === "recommended"', fragment)
            self.assertIn('if (!customInput.value.trim()) customInput.value = editableAnswerSeed(node)', fragment)
            self.assertIn('Edit the selected or recommended answer…', fragment)
            self.assertIn('data-apply disabled>Send all decisions to Codex</button>', fragment)
            self.assertIn('apply.textContent = "Send all decisions to Codex"', fragment)
            self.assertIn('.gwd-disclosure:hover .gwd-chevron', fragment)
            self.assertNotIn('.gwd-disclosure:hover {', fragment)
            self.assertIn('High confidence: 90–100%', fragment)
            self.assertIn('Medium confidence: 70–89%', fragment)
            self.assertIn('Low confidence: below 70%', fragment)
            self.assertIn('gwd-metric gwd-confidence-low', fragment)
            self.assertIn('var(--destructive, #ff6868) 34%', fragment)
            self.assertIn('metric(`Risk ${assessment.risk}`', fragment)
            self.assertIn('recommended:"var(--gwd-positive-color)"', fragment)
            self.assertIn('"solid-alternative":"var(--gwd-info-color)"', fragment)
            self.assertIn('situational:"var(--gwd-warning-color)"', fragment)
            self.assertIn('--gwd-positive-color:#54d18b', fragment)
            self.assertIn('`${count} decision${count === 1 ? "" : "s"} ready`', fragment)
            self.assertNotIn('let selected = null', fragment)
            self.assertNotIn('keepOnlyOnePendingDecision', fragment)
            self.assertIn('optionMain.append(label, summary, triage, pending)', fragment)
            self.assertIn('option.description || assessment.reason', fragment)
            self.assertIn('excluded:"Excluded · unavailable"', fragment)
            self.assertIn('"Needs reassessment · unavailable"', fragment)
            self.assertIn('Reassess path before editing this answer.', fragment)
            self.assertIn('const expectedRevision = state.revision ?? 0', fragment)
            self.assertIn('Expected state revision: ${expectedRevision}', fragment)
            self.assertIn('If the current revision differs, do not apply these decisions', fragment)
            self.assertIn('item.hidden = item !== target', fragment)
            self.assertIn('grid-template-columns:repeat(2, minmax(0, 1fr))', fragment)
            self.assertNotIn('@media (max-width:760px)', fragment)
            self.assertIn('text-overflow:ellipsis', fragment)
            self.assertIn('"Pending change"', fragment)
            self.assertIn('High 90–100%', fragment)
            self.assertIn('data-copy-prompt hidden>Copy prompt</button>', fragment)
            self.assertEqual(fragment.count('feedback.textContent = "Codex connection failed."'), 2)
            self.assertIn('await navigator.clipboard.writeText(fallbackPrompt)', fragment)
            self.assertNotIn('Copy this prompt: ${prompt}', fragment)
            self.assertNotIn("data-reassess=", fragment)

    def test_render_uses_the_canonical_template_contract(self) -> None:
        self.assertTrue(TEMPLATE.is_file())
        template = TEMPLATE.read_text()
        self.assertEqual(template.count("__LET_HIM_GRILL_STATE_JSON__"), 1)
        self.assertEqual(template.count("__LET_HIM_GRILL_STATE_PATH_JSON__"), 1)

        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory) / "state.json"
            self.run_cli("init", str(state), "--title", "Canonical <template>")
            self.run_cli(
                "add", str(state), "--id", "surface", "--question", "Surface?",
                "--type", "auto", "--option", "native=Native Codex",
                "--assessment", self.assessment("native"),
            )

            rendered = Path(directory) / "tree.html"
            self.run_cli("render", str(state), str(rendered))
            fragment = rendered.read_text()

            self.assertIn('data-template="let-him-grill-v1"', fragment)
            self.assertIn('${autonomous} autonomous', fragment)
            self.assertIn('if (node.status === "confirmed") return "Confirmed"', fragment)
            self.assertIn(r"Canonical \u003ctemplate>", fragment)
            self.assertNotIn("Canonical <template>", fragment)
            self.assertIn(json.dumps(str(state.resolve())), fragment)
            self.assertNotIn("__LET_HIM_GRILL_", fragment)

            portable = Path(directory) / "portable.html"
            self.run_cli(
                "render", str(state), str(portable),
                "--state-reference", "docs/examples/example/decisions.json",
            )
            portable_fragment = portable.read_text()
            self.assertIn(
                'const statePath = "docs/examples/example/decisions.json"',
                portable_fragment,
            )
            self.assertNotIn(str(state.resolve()), portable_fragment)

        skill = SKILL.read_text()
        self.assertIn("assets/decision-tree.html", skill)
        self.assertIn("__LET_HIM_GRILL_STATE_JSON__", skill)
        self.assertIn("__LET_HIM_GRILL_STATE_PATH_JSON__", skill)
        self.assertIn("never invent synonyms", skill)
        self.assertNotIn("sendFollowUpMessage", SCRIPT.read_text())

    def test_skill_requires_a_confirmed_handoff_before_implementation(self) -> None:
        skill = SKILL.read_text()
        self.assertIn("summarize confirmed human decisions", skill)
        self.assertIn("Ask the user to confirm that summary", skill)
        self.assertIn("Do not implement the discussed plan", skill)
        self.assertIn("creating a duplicate", skill)
        self.assertIn("decision_state.py resume", skill)
        self.assertIn("expectedRevision", skill)
        self.assertIn("missing `revision` means `0`", skill)
        self.assertRegex(skill, r"increment\s+`revision` exactly once")
        self.assertIn("one or more persisted options", skill)
        self.assertRegex(skill, r"Apply batched human choices in node-array\s+order")
        self.assertIn("the first invalidated node that has no invalidated dependency", skill)
        self.assertIn("otherwise the first non-invalidated `blocked` node", skill)
        self.assertIn("otherwise the first `pending` node", skill)

    def test_resume_prioritizes_the_first_valid_invalidated_root(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory) / "state.json"
            self.run_cli("init", str(state), "--title", "Resume")
            self.run_cli("add", str(state), "--id", "audience", "--question", "Audience?", "--type", "review", "--option", "dev=Developers", "--option", "team=Teams", "--assessment", self.assessment("dev"), "--assessment", self.assessment("team", "solid-alternative"), "--choice", "dev")
            self.run_cli("choose", str(state), "audience", "dev")
            self.run_cli("add", str(state), "--id", "storage", "--question", "Storage?", "--type", "review", "--option", "json=JSON", "--option", "sqlite=SQLite", "--assessment", self.assessment("json"), "--assessment", self.assessment("sqlite", "solid-alternative"), "--choice", "json", "--depends-on", "audience")
            self.run_cli("add", str(state), "--id", "architecture", "--question", "Architecture?", "--type", "human", "--option", "skill=Skill", "--option", "plugin=Plugin", "--assessment", self.assessment("skill"), "--assessment", self.assessment("plugin", "solid-alternative"), "--depends-on", "storage")
            self.run_cli("add", str(state), "--id", "release", "--question", "Release?", "--type", "human", "--option", "now=Now", "--option", "later=Later", "--assessment", self.assessment("now"), "--assessment", self.assessment("later", "solid-alternative"))
            self.run_cli("choose", str(state), "audience", "team")

            before = state.read_text()
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "resume", str(state)],
                check=True,
                capture_output=True,
                text=True,
            )

            self.assertEqual(state.read_text(), before)
            self.assertIn("Resume status: reassess", result.stdout)
            self.assertIn("Confirmed human decisions: audience", result.stdout)
            self.assertIn("Next node: storage", result.stdout)
            self.assertNotIn("Next node: architecture", result.stdout)

    def test_resume_reports_blocked_then_pending_human_gate(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory) / "state.json"
            self.run_cli("init", str(state), "--title", "Resume")
            self.run_cli("add", str(state), "--id", "storage", "--question", "Storage?", "--type", "auto", "--option", "json=JSON", "--assessment", self.assessment("json"))
            self.run_cli("add", str(state), "--id", "release", "--question", "Release?", "--type", "human", "--option", "now=Now", "--option", "later=Later", "--assessment", self.assessment("now"), "--assessment", self.assessment("later", "solid-alternative"))
            self.run_cli("add", str(state), "--id", "budget", "--question", "Budget?", "--type", "blocked", "--option", "known=Known", "--assessment", self.assessment("known", "situational"))

            blocked = subprocess.run(
                [sys.executable, str(SCRIPT), "resume", str(state)],
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertIn("Resume status: unblock", blocked.stdout)
            self.assertIn("Next node: budget", blocked.stdout)
            self.assertIn("Provisional AI decisions: storage", blocked.stdout)

            data = json.loads(state.read_text())
            data["nodes"] = [node for node in data["nodes"] if node["id"] != "budget"]
            state.write_text(json.dumps(data))
            pending = subprocess.run(
                [sys.executable, str(SCRIPT), "resume", str(state)],
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertIn("Resume status: human-gate", pending.stdout)
            self.assertIn("Next node: release", pending.stdout)

    def test_resume_reports_complete_state(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory) / "state.json"
            self.run_cli("init", str(state), "--title", "Resume")
            self.run_cli("add", str(state), "--id", "storage", "--question", "Storage?", "--type", "auto", "--option", "json=JSON", "--assessment", self.assessment("json"))

            result = subprocess.run(
                [sys.executable, str(SCRIPT), "resume", str(state)],
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertIn("Resume status: complete", result.stdout)
            self.assertIn("Next node: none", result.stdout)

    def test_render_finds_template_in_an_installed_skill_layout(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            skill = Path(directory) / "let-him-grill"
            (skill / "scripts").mkdir(parents=True)
            (skill / "assets").mkdir()
            shutil.copy2(SCRIPT, skill / "scripts" / SCRIPT.name)
            shutil.copy2(TEMPLATE, skill / "assets" / TEMPLATE.name)
            output = Path(directory) / "tree.html"

            subprocess.run(
                [
                    sys.executable,
                    str(skill / "scripts" / SCRIPT.name),
                    "render",
                    str(ROOT / "examples" / "decisions.json"),
                    str(output),
                ],
                check=True,
            )

            self.assertIn('data-template="let-him-grill-v1"', output.read_text())

    def test_reference_example_bundles_are_portable_and_reassess_only_descendants(self) -> None:
        cases = {
            "feature-planning": ("audience", "new-users", {"delivery", "scope-gate"}, "documentation", "inline-help"),
            "software-architecture": ("boundary", "services", {"storage", "operations-gate"}, "decision-record", "adr"),
            "release-readiness": ("rollout", "direct", {"rollback", "go-live-gate"}, "release-notes", "guide"),
        }
        for scenario, (node_id, option_id, invalidated, preserved_id, preserved_choice) in cases.items():
            with self.subTest(scenario=scenario), tempfile.TemporaryDirectory() as directory:
                bundle = REFERENCE_EXAMPLES / scenario
                state = json.loads((bundle / "decisions.json").read_text())
                self.assertGreaterEqual(
                    sum(node["type"] in {"auto", "review"} for node in state["nodes"]),
                    2,
                )
                self.assertTrue(any(
                    node["type"] == "human" and node["status"] == "pending"
                    for node in state["nodes"]
                ))
                for artifact in ("README.md", "prompt.md", "handoff.md", "reassessment.md", "tree.html"):
                    self.assertTrue((bundle / artifact).is_file())
                tree = (bundle / "tree.html").read_text()
                reference = f"docs/examples/{scenario}/decisions.json"
                self.assertIn(f"const statePath = {json.dumps(reference)}", tree)
                self.assertNotIn(str(ROOT), tree)

                copy = Path(directory) / "decisions.json"
                shutil.copy2(bundle / "decisions.json", copy)
                self.run_cli("choose", str(copy), node_id, option_id, "--actor", "human")
                changed = {node["id"]: node for node in json.loads(copy.read_text())["nodes"]}
                self.assertEqual(
                    {node_id for node_id, node in changed.items() if node["status"] == "invalidated"},
                    invalidated,
                )
                self.assertEqual(changed[preserved_id]["choice"], preserved_choice)


if __name__ == "__main__":
    unittest.main()
