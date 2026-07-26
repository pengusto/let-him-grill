# Software architecture: event intake service

## What initial system boundary fits the observed load?

- Type: `review`
- Status: `recommended`
- Choice: Modular monolith
- Context: The team owns one product and has no independent scaling evidence yet.
- Reason: Current evidence supports one deployable with explicit modules.

## Where should accepted events be stored first?

- Type: `auto`
- Status: `recommended`
- Choice: PostgreSQL
- Context: The initial system needs transactions and ordinary operational queries.
- Reason: One relational store satisfies the current operational contract.

## How should the architecture choice be recorded?

- Type: `auto`
- Status: `recommended`
- Choice: One ADR with extraction triggers
- Context: Future maintainers need the evidence and extraction trigger.
- Reason: The trade-off meets the repository ADR threshold.

## Should the team accept a distributed-service operational boundary now?

- Type: `human`
- Status: `pending`
- Choice: No selection yet
- Context: Separate services create lasting deployment, failure, and on-call obligations.
- Reason: Open
