# Reassessment: change the initial audience

Copy `decisions.json`, then change `audience` from `existing-users` to
`new-users`:

```bash
python3 scripts/decision_state.py choose \
  /path/to/copied-decisions.json audience new-users --actor human
```

Expected invalidation:

- `delivery`: invalidated because its smallest useful slice depends on audience
- `scope-gate`: invalidated transitively through audience and delivery
- `documentation`: unchanged because its explanation requirement is independent

Resume must reassess `delivery` before `scope-gate` and preserve
`documentation=inline-help`.
