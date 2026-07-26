# Release readiness: account export

## How should account export reach users?

- Type: `review`
- Status: `recommended`
- Choice: Staged rollout
- Context: The feature handles personal data and needs observable production evidence.
- Reason: A controlled cohort provides evidence with bounded exposure.

## What rollback control is required?

- Type: `auto`
- Status: `recommended`
- Choice: Server-side feature flag
- Context: Export failures must be stopped without redeploying unrelated changes.
- Reason: A targeted kill switch matches the staged rollout.

## How should the user-facing change be documented?

- Type: `auto`
- Status: `recommended`
- Choice: Release note plus export guide
- Context: Users need to understand export contents and delivery timing.
- Reason: Documentation is required regardless of rollout size.

## Is the current privacy and operational evidence sufficient for public rollout?

- Type: `human`
- Status: `pending`
- Choice: No selection yet
- Context: Public availability accepts residual data-exposure and support risk.
- Reason: Open
