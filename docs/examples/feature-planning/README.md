# Feature planning: saved filters

This bundle shows Let Him Grill narrowing a feature to a reversible vertical
slice before stopping at the public collaboration scope.

- [Starting prompt](prompt.md)
- [Portable decision state](decisions.json)
- [Interactive tree](tree.html)
- [Markdown handoff](handoff.md)
- [Earlier-choice reassessment](reassessment.md)

Expected path: existing dashboard users → private save/rename/delete → inline
help → Human-Gate on team sharing.

After downloading `decisions.json` into your project as `.grill/decisions.json`,
resume it in a task with Let Him Grill installed:

```text
Use $let-him-grill in compact mode. Resume .grill/decisions.json and continue
to the next Human-Gate.
```
