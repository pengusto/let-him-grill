# Portable artifact validation

These fixtures exercise the read-only resume contract in a new Python process,
without conversation history or mutable external state.

Run:

```bash
python3 scripts/decision_state.py resume \
  docs/validation/portable-artifact/fixtures/next-human-gate.json
python3 scripts/decision_state.py resume \
  docs/validation/portable-artifact/fixtures/invalidated-branch.json
python3 scripts/decision_state.py resume \
  docs/validation/portable-artifact/fixtures/complete.json
```

Expected next actions:

| Fixture | Status | Next node | Why |
| --- | --- | --- | --- |
| `next-human-gate.json` | `human-gate` | `release` | Earlier AI choice remains provisional and the material choice needs a person. |
| `invalidated-branch.json` | `reassess` | `storage` | `surface` cannot be reassessed before its invalidated dependency. |
| `complete.json` | `complete` | none | No invalidated, blocked, or pending node remains. |

The unit suite additionally verifies that running `resume` does not change the
state file, blocked nodes precede pending gates, confirmed human decisions are
reported, and provisional AI choices remain visible.

Native parity is defined by the identical ordered procedure in `SKILL.md` and
checked against this table during a native-backend smoke test. Actual clean
Codex and Claude Code task resumptions remain the scope of ticket 007.
