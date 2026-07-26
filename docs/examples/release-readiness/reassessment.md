# Reassessment: replace staged rollout with direct rollout

Copy `decisions.json`, then change `rollout` from `staged` to `direct`:

```bash
python3 scripts/decision_state.py choose \
  /path/to/copied-decisions.json rollout direct --actor human
```

Expected invalidation:

- `rollback`: invalidated because its control assumes a staged cohort
- `go-live-gate`: invalidated transitively through rollout and rollback
- `release-notes`: unchanged because user documentation is always required

Resume must reassess `rollback` before `go-live-gate` and preserve
`release-notes=guide`.
