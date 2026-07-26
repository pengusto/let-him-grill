# Define the portable decision artifact

Status: Done

Depends on: tickets 001, 004, and 005

## Goal

A completed Let Him Grill run should leave one portable artifact that another
supported coding agent or a later session can inspect and resume without the
original conversation.

## Scope

- Define the supported artifact as `.grill/decisions.json` plus an optional
  rendered HTML view and Markdown handoff.
- Document which file is the source of truth and which files are derived views.
- Add a concise resume contract covering confirmed choices, provisional choices,
  unresolved human gates, invalidated descendants, and the next action.
- Add an export command or extend the existing export only when the current
  output cannot express that contract.
- Keep version 2 state and the Python standard-library implementation.

## Measurement

Test three independent local resumptions from fixtures with no conversation
history:

1. continue from the next unresolved human gate
2. change an earlier confirmed choice and invalidate only its descendants
3. report a completed state and verify the same ordered procedure is specified
   for the native backend

Record the prompt, artifact fixture, expected result, and observed result under
`docs/validation/portable-artifact/`.

## Acceptance criteria

- One document defines the artifact and resume contract without relying on
  Codex-specific UI behavior.
- All three local resumptions succeed from repository files alone.
- No confirmed human choice is silently overwritten.
- Python and native paths identify the same next gate and invalidated nodes.
- `python3 scripts/test_decision_state.py` passes.

Clean Codex and Claude Code task resumptions are covered separately by ticket
007 so this contract ticket stays deterministic and locally reproducible.

## Out of scope

- cloud synchronization
- multi-user editing
- a new state version unless a concrete missing field requires it
- support for every agent harness
