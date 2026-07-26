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

Resume in a task with Let Him Grill installed:

```text
Use $let-him-grill in compact mode. Resume
docs/examples/software-architecture/decisions.json and continue to the next Human-Gate.
```
