# Verify clean Codex and Claude Code installation

Status: Ready

Depends on: ticket 006

## Goal

A stranger should be able to install the same repository and complete one
portable decision-tree run in Codex or Claude Code without editing files by hand.

## Scope

- Test the published one-line `skills` installation in two empty temporary
  repositories: one with Codex and one with Claude Code.
- Invoke the installed skill by its documented name.
- Run one fixed three-decision scenario through an autonomous choice and a human
  gate.
- Resume the resulting artifact in a new task for each harness.
- Correct only installation, discovery, or documentation defects found by the
  smoke tests.

## Measurement

For each harness record:

- commands entered before the first successful invocation
- manual file edits required
- time from install command to first rendered or textual human gate
- whether a new task resumes from the saved artifact
- exact failure and recovery when the first attempt does not work

Target: one install command, zero manual edits, successful invocation and resume
in both harnesses.

## Acceptance criteria

- Codex passes the complete install, invoke, gate, and resume flow.
- Claude Code passes the complete install, invoke, gate, and resume flow.
- Evidence is stored under `docs/validation/cross-agent-install/`.
- README instructions match the commands that actually passed.
- No custom installer is introduced unless the standard installer demonstrably
  cannot satisfy the test.

## Out of scope

- automatic testing of every supported agent
- operating-system matrix testing
- managed accounts or remote services
