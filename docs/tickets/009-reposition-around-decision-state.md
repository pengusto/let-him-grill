# Reposition the project around resumable decision state

Status: Ready

Depends on: ticket 008

## Goal

The README and GitHub Pages should explain Let Him Grill's distinct value in one
sentence and prove it with the portable artifact rather than presenting it as
another generic grilling prompt.

## Positioning

Working promise:

> Turn an ambiguous plan into a decision tree your coding agent can resume.

The final wording may change, but it must communicate ambiguity, visible
decisions, and resumability.

## Scope

- Lead README and Pages with the artifact promise.
- Show a 15–25 second sequence: ambiguous request, autonomous decisions, human
  gate, changed branch, resumable handoff.
- Link directly to one complete reference artifact above the long-form feature
  explanation.
- Preserve attribution to Grill with Docs and avoid comparative claims that the
  benchmark does not support.
- Keep Molebyte as recognition, not the primary value proposition.

## Measurement

Run a five-person comprehension check. After viewing the first screen for no
more than 30 seconds, ask each person:

1. What does this project leave behind?
2. What makes it different from an agent that only asks planning questions?
3. What command would you run to try it?

Target: at least four of five mention a resumable decision tree or persistent
decision artifact, and at least four find the install command without help.

## Acceptance criteria

- README and Pages use one consistent primary promise.
- The first viewport contains promise, proof artifact, and install action.
- The demo shows a branch change and later-session handoff, not only questioning.
- Comprehension-check responses and result summary are stored under
  `docs/validation/positioning/`.
- Desktop and narrow layouts pass visual inspection.

## Out of scope

- redesigning the complete visual system
- paid marketing
- additional mascot characters or a skill suite
