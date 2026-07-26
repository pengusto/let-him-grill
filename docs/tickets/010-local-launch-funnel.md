# Measure the local launch funnel

Status: Ready

Depends on: tickets 007, 008, and 009

## Goal

Evaluate whether users complete and reuse the decision artifact without adding
telemetry, accounts, or a backend.

## Scope

- Create a local, versioned measurement template for assisted user tests.
- Record only aggregate or explicitly consented data.
- Run at least five external-user sessions from install through first human gate.
- Invite each participant to resume the artifact in a second task.
- Capture failure reasons as short categories that can become focused issues.

## Funnel

1. saw project page
2. ran install command
3. invoked skill successfully
4. reached first human gate
5. completed a portable artifact
6. resumed it in a new task
7. voluntarily used it for a second decision within 14 days

## Measurement

Record counts and conversion between every adjacent step. Also record median
time from installation to first human gate and the three most common drop-off
reasons.

Initial validation thresholds for five or more participants:

- at least 80% of installers invoke the skill successfully
- at least 60% of starters complete one artifact
- at least 50% of completers resume it in a new task
- at least two participants return for a second real decision within 14 days

These are learning thresholds, not public product claims.

## Acceptance criteria

- Measurement template and anonymized aggregate report live under
  `docs/validation/launch-funnel/`.
- Denominators and drop-offs remain visible; failed sessions are not discarded.
- No analytics SDK, cookie, unique device identifier, or network service is
  added.
- Findings produce no more than three evidence-backed follow-up issues.
- Public claims distinguish installs, completed artifacts, resumed artifacts,
  and repeat use.

## Out of scope

- passive production telemetry
- growth dashboards
- paid acquisition
- optimizing GitHub stars as the primary success metric
