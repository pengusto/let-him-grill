# Verify clean Codex and Claude Code installation

Status: Done — Claude live invocation not verified

Depends on: ticket 006

## Goal

A stranger should be able to install the same repository and complete one
portable decision-tree run in Codex or Claude Code without editing files by hand.

## Scope

- Test the published one-line `skills` installation in two empty temporary
  repositories: one with Codex and one with Claude Code.
- Invoke the installed skill by its documented name in Codex.
- Run one fixed scenario through a provisional choice and a human gate in Codex.
- Verify that Claude Code receives the same packaged skill and deterministic
  resume command without requiring paid live inference.
- Correct only installation, discovery, or documentation defects found by the
  smoke tests.

## Measurement

For each harness record:

- commands entered before the first successful invocation
- manual file edits required
- time from install command to first rendered or textual human gate
- whether a new task resumes from the saved artifact
- exact failure and recovery when the first attempt does not work

Target: one install command and zero manual skill-file edits in both harnesses;
successful live invocation and resume in Codex; matching packaged resume output
for Claude Code.

## Acceptance criteria

- Codex passes the complete install, invoke, gate, and resume flow.
- Claude Code passes project-local installation and the packaged deterministic
  resume command. Live agent invocation remains optional because it requires a
  paid subscription, prepaid API credits, or a supported cloud provider.
- Evidence is stored under `docs/validation/cross-agent-install/`.
- README instructions match the commands that actually passed.
- No custom installer is introduced unless the standard installer demonstrably
  cannot satisfy the test.

## Out of scope

- automatic testing of every supported agent
- operating-system matrix testing
- managed accounts or remote services

## Current result

- Codex: passed project-local install, discovery, read-only resume, and Human-Gate stop.
- Claude Code: passed project-local install and packaged resume command; live
  invocation is blocked before skill discovery because the local Claude CLI is
  not authenticated (`Not logged in · Please run /login`).
- The project owner accepted this limitation on 26 July 2026. Users with Claude
  access can report and fix harness-specific discovery issues if they occur.
- Evidence and reproduction commands are stored in
  [the cross-agent validation report](../validation/cross-agent-install/README.md).
