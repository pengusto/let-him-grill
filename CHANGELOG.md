# Changelog

All notable user-facing changes to Let Him Grill are recorded here.

## [Unreleased]

### Added

- Added Molebyte as the project mascot across the GitHub Pages builder section,
  final call to action, and both README language versions, including a compact
  pixel-art workflow animation.
- Added a read-only `resume` command and matching native-backend contract for
  deterministically continuing portable decision state in a later agent task.
- Added repository-relative state references for public rendered decision-tree
  examples.
- Added three downloadable reference-artifact bundles for feature planning,
  software architecture, and release readiness, each with portable state,
  interactive tree, handoff, and reassessment guidance.

### Fixed

- Reject cyclic decision dependencies before rendering, exporting, resuming, or
  changing state.
- Send all pending answers from the interactive tree in one dependency-aware
  Codex follow-up, show option summaries without expanding details, and explain
  excluded or stale options as unavailable.
- Seed `Own answer` from the selected or recommended option so users can refine
  an existing answer instead of rewriting it from scratch.
- Prevent duplicate Codex follow-ups while a send is pending, and hide the
  custom-answer editor until invalidated decisions are reassessed.
- Add monotonic state revisions so historical trees cannot silently apply
  choices to a newer decision state.

## [0.2.1] - 2026-07-26

### Added

- Added English-language imprint and privacy pages and linked them from the
  GitHub Pages footer.

## [0.2.0] - 2026-07-26

### Added

- Added a responsive GitHub Pages landing page with the benchmark, workflow,
  installation command, and repository link.
- Added six copy-ready examples for finance, software architecture, AI
  training, game development, language training, and infrastructure security,
  each with its own decision-tree screenshot.
- Added a complete German README and language links between both versions.
- Added an Excalidraw-style overview of decision triage, human gates, and visual
  rendering in Codex.

### Changed

- Added the GitHub mark to the landing-page repository link, with a compact
  icon-only treatment on narrow screens.
- Replaced the ambiguous `66 → 1` landing-page claim with the seven material
  human gates surfaced in the benchmark, and clarified that its question count
  measures prompt-dependent conversational interruptions rather than gates
  removed.
- Updated GitHub repository and installation references for the new `pengusto`
  account name.
- Decision questions now use the same disclosure arrow as option details, and
  each question accepts a custom answer that the bottom action sends to Codex
  for refinement and application. Opening a custom answer selects it; choosing
  a predefined option closes that question's custom field.
- Option details now show color-coded confidence bands, risk, effort, and
  reversibility as separate tags for faster comparison.
- Expanded questions now separate decision context from the current assessment.
- Pending selections now identify their question and answer, use a visible
  `Pending change` tag, and send through the single bottom action. Long answers
  use a two-column desktop and one-column narrow layout, confidence ranges have
  a compact legend, and failed Codex delivery offers `Copy prompt`.
- Stabilized the bottom selection bar and pending tag during text entry, and
  kept the two-column answer layout at Codex's desktop inline width.
- Reordered option colors by recommendation strength: green recommended, blue
  solid alternative, orange situational, red not recommended, and gray excluded.
- Made positive, informational, and warning colors stable instead of inheriting
  host series colors that could render high confidence as red.
- Increased the red emphasis specifically for confidence below 70%.
- Refreshed the before and reassessed screenshots for the current two-column
  decision interface.
- Clarified the primary installation requirements and replaced obsolete open
  product questions with the decisions implemented in `v0.1.0`.
- Added a confirmed handoff before implementation, including a concise decision
  summary and reuse of existing canonical project documentation.
- Cropped and lightly rounded the demo animation and poster to remove the
  captured white browser background on GitHub and the project landing page.

## [0.1.0] - 2026-07-24

### Added

- One canonical decision-tree template shared by the Python renderer, native
  Codex fallback, and recorded demo.
- An 18-second workflow demo and accessible poster frame showing autonomous
  progress, a human gate, branch invalidation, and reassessment.
- Reproducible five-scenario workflow benchmark with ten raw transcripts and an
  evidence-backed before-and-after result.
- Invalidated decision paths now offer a direct Codex reassessment action while
  preventing stale options from being selected.
- Decision triage for `auto`, `review`, `human`, `derived`, and `blocked` paths.
- Option triage for recommended, alternative, situational, discouraged, and
  excluded choices.
- Per-option rationale, confidence, reversibility, effort, risk, downstream
  impact, and preferred conditions.
- Deterministic auto-selection when exactly one recommendation is low-risk and
  reversible.
- Subtle option status accents and expandable assessment details in the visual
  decision tree.
- Protection against selecting excluded or invalidated options.
- Transitive invalidation of dependent decisions and their option assessments.
- Explicit Python and runtime-free native Codex backends for visual mode, with
  visible backend selection and matching state rules.

### Changed

- The interactive tree now confirms successful Codex follow-up delivery and
  preserves the complete prompt when the host bridge is unavailable or rejects
  the request.
- Added the verified one-line `skills` CLI installation as the primary setup
  path, while retaining Git installation as a fallback.
- State format moved to version 2; version 1 state is intentionally unsupported
  before the first public release.
- The project and skill were renamed from Grill with Docs Interactive to Let Him
  Grill.
- The public example and generated interface now use English labels.

### Fixed

- State validation now rejects native-backend schema synonyms instead of
  accepting unsupported status and actor values.
- Confirmed human decisions now display as confirmed instead of continuing to
  appear as decision-required nodes.
- Native visual rendering now targets and verifies the exact current Codex task
  directory instead of reusing another task's visualization directory.

## [0.0.1] - 2026-07-22

Initial pre-release baseline:

- Compact and visual Grill with Docs workflows.
- Persistent workspace JSON and Markdown export.
- Interactive Codex decision tree with selectable and expandable options.
- Transitive invalidation after changing an earlier decision.
- Python standard-library state engine with no package installation or virtual
  environment requirement.
- README, MIT license, product notes, screenshot, examples, and initial tests.
