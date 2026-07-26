# Portable decision artifact contract

## Supported artifact

`.grill/decisions.json` is the portable source of truth. A later task may resume
it when Let Him Grill is installed in the target agent harness. The original
conversation is not required.

Rendered HTML and exported Markdown are derived views. They may contain an
absolute path from the workspace that created them and must not be used as
mutable state. Regenerate them after moving the JSON artifact.

## Resume behavior

Resume is read-only until the agent has inspected current repository evidence.
It reports confirmed human choices and provisional AI choices, then selects one
next action:

1. `reassess`: first invalidated node without an invalidated dependency
2. `unblock`: first remaining blocked node
3. `human-gate`: first pending human node
4. `assess`: first other pending node
5. `complete`: no unresolved node remains

Node-array order breaks ties. An invalidated descendant cannot be selected
before its invalidated ancestor.

After inspection, the agent keeps provisional AI choices supported by current
project evidence. When evidence contradicts one, the agent invalidates that
choice and only its transitive descendants, reassesses them, and continues
autonomously until the next Human-Gate.

## Safety invariants

- Never overwrite a confirmed human choice during inspection or reassessment.
- Never select an excluded or invalidated option.
- Never treat confidence alone as permission to cross a Human-Gate.
- Keep state version 2 until a missing capability requires a schema change.
- The target harness must have Let Him Grill installed; workflow and safety
  rules are not duplicated in each artifact.

## Commands

Inspect the next action without modifying state:

```bash
python3 scripts/decision_state.py resume .grill/decisions.json
```

Create human-readable and visual derived views after resuming:

```bash
python3 scripts/decision_state.py export \
  .grill/decisions.json docs/decision-path.md
python3 scripts/decision_state.py render \
  .grill/decisions.json /absolute/current-task/decision-tree.html
```

For a versioned public example, provide a repository-relative reference so the
generated HTML does not embed a private machine path:

```bash
python3 scripts/decision_state.py render \
  docs/examples/example/decisions.json docs/examples/example/tree.html \
  --state-reference docs/examples/example/decisions.json
```

The native backend applies the same priority and reporting rules directly to
the validated JSON without invoking Python.
