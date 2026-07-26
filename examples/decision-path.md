# Let Him Grill

## Where should the decision tree live?

- Type: `human`
- Status: `confirmed`
- Choice: Native Codex visualization
- Context: Users need to inspect and revise earlier decisions without losing the flow of the current planning conversation.
- Reason: It stays in the conversation without a server or separate frontend.

## Where should persistent state live?

- Type: `review`
- Status: `recommended`
- Choice: Workspace JSON
- Context: The decision history must survive later Codex tasks, support deterministic updates, and remain easy for humans to inspect.
- Reason: The visualization remains a replaceable view.

## How should Grill with Docs be extended?

- Type: `review`
- Status: `recommended`
- Choice: Dedicated orchestrator skill
- Context: The new workflow must add autonomous decision triage while preserving the original evidence-first skill and its update path.
- Reason: The original skill remains unchanged and independently updateable.

## When should the workflow stop?

- Type: `derived`
- Status: `derived`
- Choice: Only for material decisions
- Context: Autonomy should reduce routine interruptions without allowing the agent to cross consequential product, security, cost, or architecture boundaries.
- Reason: This follows directly from the product goal.
