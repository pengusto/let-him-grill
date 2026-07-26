# Reassessment: split the system boundary

Copy `decisions.json`, then change `boundary` from `modular-monolith` to
`services`:

```bash
python3 scripts/decision_state.py choose \
  /path/to/copied-decisions.json boundary services --actor human
```

Expected invalidation:

- `storage`: invalidated because storage topology depends on system boundary
- `operations-gate`: invalidated transitively through boundary and storage
- `decision-record`: unchanged because an ADR is required for either boundary

Resume must reassess `storage` before `operations-gate` and preserve
`decision-record=adr`.
