# Software architecture: event intake service

This bundle chooses the smallest initial architecture supported by current load
and ownership evidence, then stops before accepting distributed operations.

- [Starting prompt](prompt.md)
- [Portable decision state](decisions.json)
- [Interactive tree](tree.html)
- [Markdown handoff](handoff.md)
- [Earlier-choice reassessment](reassessment.md)

Expected path: modular monolith → PostgreSQL → ADR → Human-Gate on separate
service operations.

After downloading `decisions.json` into your project as `.grill/decisions.json`,
resume it in a task with Let Him Grill installed:

```text
Use $let-him-grill in compact mode. Resume .grill/decisions.json and continue
to the next Human-Gate.
```
