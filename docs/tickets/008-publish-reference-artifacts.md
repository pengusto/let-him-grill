# Publish three reference decision artifacts

Status: Done

Depends on: tickets 006 and 007

## Goal

Visitors should be able to inspect and reuse complete Let Him Grill outcomes,
not only screenshots of the interface.

## Scenarios

1. feature planning with scope and delivery trade-offs
2. software architecture with a material long-term choice
3. release readiness with security or operational gates

## Deliverable per scenario

- exact starting prompt
- portable decision JSON
- rendered interactive HTML tree
- Markdown handoff
- short expected-path explanation
- one documented earlier-choice change and reassessment

Store each self-contained bundle below `docs/examples/<scenario>/`.

## Measurement

- all three bundles validate with the state engine
- every bundle contains at least two autonomous or review decisions and one
  genuine human gate
- a fresh task can identify the next action from each bundle without reading the
  original transcript
- every internal link works from GitHub Pages and the repository

## Acceptance criteria

- Three complete bundles exist and use the same artifact contract.
- None contains invented benchmark results, secrets, private paths, or machine-
  specific identifiers.
- Each reassessment invalidates only dependent decisions.
- README and GitHub Pages link to all three downloadable artifacts.
- `python3 scripts/test_decision_state.py` passes.

## Out of scope

- additional industries before these three scenarios receive real usage
- a generic example generator
- hosted artifact storage
