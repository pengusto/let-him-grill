# Cross-agent installation validation

Validation date: 26 July 2026

Both tests used new temporary Git repositories and project-local copied skills.
No global Let Him Grill installation was changed.

## Fixed scenario

The repository contained only the `next-human-gate.json` fixture at
`.grill/decisions.json`. Expected behavior:

- keep provisional `storage=json`
- select `release` as the next node
- stop at `human-gate`
- modify no file

## Codex

Environment: Codex CLI `0.142.2`, authenticated through ChatGPT.

Installation:

```bash
npx -y skills@latest add pengusto/let-him-grill -a codex -y --copy
```

Observed installation target:

```text
.agents/skills/let-him-grill
```

The installation completed in one command with no manual file edits. The
installed Python command returned:

```text
Resume status: human-gate
Confirmed human decisions: none
Provisional AI decisions: storage=json
Next node: release
Question: Should this become the public release baseline?
```

A fresh ephemeral read-only `codex exec` task discovered the installed skill,
ran that command, reported the same values, stopped at the Human-Gate, and
reported `Files modified: None`. The fixture remained byte-identical afterward.

Approximate observed time: under 10 seconds for installation and about 25
seconds from invocation to the reported Human-Gate on this machine. This is a
single smoke-test observation, not a performance claim.

Result: **Pass**.

## Claude Code

Environment: official temporary npm package, Claude Code `2.1.220`.

Installation:

```bash
npx -y skills@latest add pengusto/let-him-grill -a claude-code -y --copy
```

Observed installation target:

```text
.claude/skills/let-him-grill
```

The installation completed in one command with no manual file edits. Running
the installed Python `resume` command produced the same expected Human-Gate
result as Codex, proving that the published package contains the required files.

Live Claude invocation stopped before skill discovery with:

```text
Not logged in · Please run /login
```

Result: **Package validation passed; live invocation not verified**. No product
or installation defect was observed. Live use requires a Claude subscription,
prepaid Console API credits, or a supported cloud provider. The project owner
accepted this limitation rather than adding a paid test dependency.

## Acceptance status

| Check | Codex | Claude Code |
| --- | --- | --- |
| One-command project installation | Pass | Pass |
| No manual skill-file edits | Pass | Pass |
| Installed `resume` command | Pass | Pass |
| Fresh harness discovers skill | Pass | Blocked by auth |
| Stops at expected Human-Gate | Pass | Blocked by auth |
| State remains unchanged | Pass | Not reached |

Ticket 007 is complete with the live-Claude limitation shown above. Future
authenticated users may add evidence or file a focused compatibility issue.
