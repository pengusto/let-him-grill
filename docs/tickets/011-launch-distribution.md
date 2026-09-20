# Launch through focused distribution

Status: Ready

Depends on: ticket 009

Feeds evidence into: ticket 010

## Goal

Put Let Him Grill in front of relevant users with one consistent message, then
turn repeated feedback into focused issues without adding speculative features.

## Scope

- Prepare one short problem → demo → install post using only verified claims.
- Prepare one concise note to Matt Pocock that credits Grill with Docs, explains
  the resumable decision artifact, and does not imply endorsement.
- Select no more than three relevant Codex or agent-skill communities and adapt
  the same core post to each community's current format and rules.
- Record publication links, dates, qualitative responses, and repeated failure
  themes in a small versioned launch log.
- Create at most three follow-up issues, and only when evidence repeats across
  users or blocks installation, invocation, artifact completion, or resume.

## Deliverables

- `docs/launch/launch-post.md`: copy-ready primary post and shorter variants.
- `docs/launch/matt-pocock-note.md`: attribution-first outreach draft.
- `docs/validation/launch-feedback/README.md`: publication log, consent-safe
  feedback categories, and links to any resulting issues.

## Human gates

The repository owner must approve and send external messages. The agent may
prepare copy and verify links, but must not publish posts, contact people, or
join communities without explicit action-time approval.

## Acceptance criteria

- Every public claim links to the benchmark, release, or a reference artifact.
- Install command is `npx skills add pengusto/let-him-grill -g -a codex -y`.
- Primary post contains problem, visible artifact or demo, install command, and
  one link to the live Pages site.
- Matt Pocock note includes the existing inspiration link and explicitly frames
  Let Him Grill as an independent extension.
- At least one primary post and one relevant community post are published by the
  owner, with their URLs recorded.
- Feedback log contains no secrets, private conversations, email addresses, or
  user identifiers without explicit consent.
- Follow-up issues are evidence-backed and limited to the three highest-impact
  repeated problems.

## Out of scope

- paid promotion
- automated direct messages or cross-posting bots
- passive analytics, cookies, or tracking pixels
- feature work before launch feedback exists
- optimizing stars as the primary outcome
