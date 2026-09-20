# Launch kit

Status: prepared for review; nothing in this directory has been published.

Prepared: 14 August 2026

## Positioning

Primary statement:

> Let Him Grill is a Codex skill that resolves low-risk, reversible planning
> decisions and stops at the choices where human judgment changes the outcome.

Primary hook:

> Stop babysitting Codex. Let it resolve reversible decisions and interrupt you
> when your judgment matters.

Ranked alternatives:

1. **Your agent can make the reversible calls. Let it.**
2. **Codex should not stop for every decision.**
3. **Keep Codex moving. Keep the consequential calls human.**
4. **A decision boundary for autonomous coding-agent planning.**

Short explanation:

Coding agents often interrupt for low-risk choices, while a blanket “continue
autonomously” instruction does not define a safe stopping point. Let Him Grill
researches the repository, classifies decisions, resolves reversible options,
records a portable decision state, and stops at genuine Human-Gates. If an
earlier choice changes, only its dependent branch is reassessed.

## Differentiators

- Explicit stop rules for product intent, architecture, security, privacy,
  cost, operations, and hard-to-reverse choices.
- Compact text mode and a persistent visual tree with the same decision rules.
- Portable `.grill/decisions.json` that can be inspected and resumed in a later
  agent task.
- Transitive invalidation instead of silently reusing stale downstream choices.
- No server, database, virtual environment, or new package for the core state
  engine.
- Evidence exists, but is scoped honestly: 16 local state tests, five paired
  benchmark runs, and Codex install/resume validation. A live Claude invocation
  is not verified.

## Likely objections

- **“Is this just `continue autonomously`?”** No. The skill defines the
  decision boundary, records the state, stops at material gates, and rebuilds
  dependent decisions after a changed choice.
- **“Will it make product or security decisions for me?”** It is instructed to
  stop before those material choices; the final human decision remains yours.
- **“Does it need a service?”** No. The core workflow is local and uses the
  standard library for deterministic state changes in visual mode.
- **“Does this prove faster coding?”** No. The benchmark measures time to a
  usable plan under one five-run protocol, includes Codex/controller latency,
  and is not a controlled model-performance study.
- **“Does it work in Claude Code?”** The package installation and deterministic
  resume path were checked; a live Claude task was blocked by authentication.
- **“What does it modify?”** Compact mode can stay text-only. Visual mode may
  create `.grill/decisions.json` and derived views in the current task's
  visualization directory. The skill does not publish or deploy anything.

## Repository metadata to review

The current GitHub description is:

> Let Him Grill: autonomous Codex decision workflow with compact and
> interactive visual modes

Suggested description:

> Codex skill that resolves reversible planning decisions, records the path, and stops at material human gates.

Suggested topics:

`agent-skills` · `ai-agents` · `ai-coding` · `coding-agent` · `codex` ·
`codex-skill` · `decision-making` · `developer-tools` · `human-in-the-loop` ·
`workflow-automation`

The repository already has a 1280×640 social preview image and a live Pages
homepage. Changing the GitHub description or topics requires the owner's
authenticated GitHub account, so those changes remain a human gate.

## Channel targets and rules

### Primary: r/codex

Use the `Showcase` flair and publish the technical, evidence-first version in
[`launch-post.md`](launch-post.md). The current rules require direct relevance
to Codex and prioritize high-information posts with setup details, prompts,
screenshots, before/afters, reasoning, and output. Do not use bots, duplicate
the post, or ask for votes. Reply personally and disclose that this is the
author's project.

Rules checked 14 August 2026:
<https://www.reddit.com/r/codex/> (rules are visible in the community page).

### Secondary: X

Publish one original thread with the demo poster and repository link. Do not
copy the Reddit text, mass-reply, use engagement groups, or send link-only DMs.
The thread should ask one concrete question about interruption boundaries so it
starts a conversation rather than acting as a link drop.

Rules checked 14 August 2026:
<https://help.x.com/en/rules-and-policies/authenticity>

### Conditional: Hacker News / Show HN

The project is a plausible Show HN candidate because it is personally built,
non-trivial, locally runnable, and has no signup or hosted-service dependency.
Use the prepared title and body only after the current Show HN restriction is
lifted and the owner can stay in the thread to answer technical questions.
Do not ask friends for votes. If the restriction remains, wait instead of
submitting a landing-page announcement.

Rules checked 14 August 2026:
<https://news.ycombinator.com/showhn.html> and
<https://news.ycombinator.com/showlim>.

### Discovery: skills.sh

This is the primary directory for the existing install path. Skills appear in
its leaderboard through anonymous `skills` CLI telemetry; there is no manual
listing pitch to send. A real user install may be counted, while
`DISABLE_TELEMETRY=1` opts out. Never run proof installs to inflate a ranking or
describe installs as active users.

Rules and mechanics checked 14 August 2026:
<https://www.skills.sh/docs>, <https://www.skills.sh/docs/cli>, and
<https://www.skills.sh/docs/faq>.

### Optional directory: skillsdir.dev

Submit only after the owner approves a separate external submission. Its
current requirements are a valid `SKILL.md`, at least one public link, up to
three verticals, a concise summary of 180 characters or fewer, and a unique
kebab-case ID. It uses a GitHub issue template and maintainer review.

Requirements checked 14 August 2026:
<https://skillsdir.dev/add>.

## Asset map

- r/codex: `docs/demo-poster.png` plus the repository link.
- X: `docs/demo-poster.png`; use the static image, not the mascot animation.
- Show HN: `docs/demo-poster.png`, the one-line install, and the raw benchmark
  link.
- GitHub/Pages: keep the poster near the README opening and link the three
  portable reference artifacts.

## Launch sequence

### Preparation

1. Review this kit, the proposed metadata, and the final diff.
2. Run the local test and exact install smoke check from the repository root.
3. Confirm the live Pages URL and GitHub links resolve.
4. Make one real, clean install if the owner wants a skills.sh discovery signal;
   do not repeat it for ranking.
5. Decide whether to update GitHub description/topics and whether the current
   Show HN restriction permits a submission.

### Seed audience

Send the attribution-first note in
[`matt-pocock-note.md`](matt-pocock-note.md) privately only if the owner
chooses to contact him. Share the finished repository with a small number of
people who already use Codex and can try the install; ask for failure reports,
not stars.

### Launch day

Publish the r/codex Showcase post first. Stay available for replies and record
installation, invocation, and resume feedback in
[`docs/validation/launch-feedback/README.md`](../validation/launch-feedback/README.md).
Publish the X thread later the same day with its own wording. Publish Show HN
only if its readiness and account/community gates are clear.

### First 24 hours

Answer questions with links to source, benchmark limitations, and the exact
current behavior. Fix only a concrete install, invocation, artifact, or resume
failure. Do not add speculative features during the launch window.

### Next 48 hours

Summarize repeated friction, separate one-off confusion from reproducible
failures, and open no more than three focused issues. Update the feedback log
with links and consent-safe categories.

### One-week follow-up

Publish a short evidence update: what people tried, where they stopped, which
fixes landed, and what remains intentionally out of scope. Compare discovery
sources by qualified installs and completed/resumed artifacts, not stars alone.

## Measurement

Record a dated weekly snapshot with:

- GitHub stars, forks, issues, repository views, and unique visitors.
- Clones and unique cloners.
- GitHub referrers and the top content pages.
- External mentions, directory appearances, and skills.sh discovery signals.
- Qualified funnel events: install attempted, skill invoked, first Human-Gate,
  artifact completed, artifact resumed, and failure reason.

Do not add cookies, tracking pixels, or a hosted analytics service for this
launch. GitHub traffic history is short-lived, so the smallest useful later
automation is a weekly GitHub Action using its built-in `GITHUB_TOKEN` to call
the public repository traffic endpoints and commit one dated JSON snapshot of
views, clones, and referrers. Keep that as a separate follow-up after the first
launch; a hand-captured `gh api` snapshot is enough for the first week.

Suggested endpoints:

```text
repos/pengusto/let-him-grill/traffic/views
repos/pengusto/let-him-grill/traffic/clones
repos/pengusto/let-him-grill/traffic/popular/referrers
```

Traffic endpoints require repository access and may not be available to every
contributor. Never store tokens, private conversations, or user identifiers in
the repository.
