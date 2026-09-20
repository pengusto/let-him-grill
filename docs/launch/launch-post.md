# Copy-ready launch posts

These drafts are prepared, not published. Replace no claims with guesses and
do not cross-post them verbatim.

## r/codex — primary Showcase post

Suggested title:

> Showcase: I built a Codex skill that handles reversible decisions for me

Suggested flair: `Showcase`

```text
Codex kept stopping to ask me about decisions it could safely make itself:
local JSON or Markdown, one CI trigger or another, which low-risk default to
use. “Continue autonomously” helped it keep moving, but it did not tell me
where the line was.

I built Let Him Grill to make that line explicit.

It researches the repository first, classifies decisions, resolves low-risk
reversible options, and stops at product, architecture, security, cost, and
other choices where human judgment changes the outcome. In visual mode it
keeps a portable `.grill/decisions.json`; changing an earlier choice invalidates
only the dependent branch, which can then be reassessed.

Demo: https://pengusto.github.io/let-him-grill/
Repo: https://github.com/pengusto/let-him-grill
Install:
npx skills add pengusto/let-him-grill -g -a codex -y

The repo contains five paired planning runs with raw transcripts and explicit
limitations, plus clean-install/resume validation. The benchmark timing
includes Codex/controller latency; it is not a controlled model benchmark.

I would especially like feedback on false positives: where should a decision
have stopped for you, but the skill continued? Please include the prompt and
the decision boundary, not private repository content.
```

## Reddit — discussion/value-first alternative

Suggested title:

> Where do you draw the line between Codex autonomy and a human decision?

```text
I am trying to reduce a specific kind of Codex interruption: the agent asks me
to choose between two reversible implementation defaults even though the repo
already contains enough evidence to recommend one.

My current rule is:

- resolve it automatically when the choice is low-risk, reversible, and
  supported by repository evidence;
- stop when it changes product intent, architecture, security, cost, or another
  hard-to-reverse outcome;
- if an earlier choice changes, reassess the dependent decisions instead of
  silently continuing with stale assumptions.

I packaged that rule as an open-source Codex skill called Let Him Grill. It has
compact text mode and a portable visual decision tree:
https://github.com/pengusto/let-him-grill

For people using Codex regularly: which “small” decisions do you still want to
answer yourself, even when they look reversible? I am looking for counterexamples
and boundary cases more than promotion feedback.
```

## X — launch thread

Post 1:

> Codex should not stop for every decision.
>
> I built Let Him Grill: a skill that resolves low-risk, reversible planning
> choices and interrupts you when your judgment actually changes the outcome.
>
> Demo + install ↓

Post 2:

> “Continue autonomously” is not a decision policy.
>
> Let Him Grill classifies the choice, records the path, and stops before
> product, architecture, security, cost, or other material trade-offs.

Post 3:

> The useful part is what happens after a change: choose a different earlier
> option and only its dependent branch becomes invalid and gets reassessed.
>
> No stale downstream assumptions quietly survive.

Post 4:

> Proof in the repo: five paired planning runs, raw transcripts, 16 state-engine
> tests, and Codex install/resume validation.
>
> The timing claim includes Codex/controller latency and is explicitly not a
> controlled model-performance benchmark.

Post 5:

> Install:
> `npx skills add pengusto/let-him-grill -g -a codex -y`
>
> https://github.com/pengusto/let-him-grill
>
> If you use Codex, where should an autonomous run stop for you?

Attach `docs/demo-poster.png` to Post 1. Write replies manually; do not use
bulk mentions, identical replies, or engagement groups.

## Hacker News — conditional Show HN candidate

Use only after the current Show HN restriction is lifted and the owner can
answer technical questions in the thread.

Suggested title:

> Show HN: Let Him Grill — a Codex skill that stops at consequential decisions

Suggested body:

```text
Hi HN — I built Let Him Grill because my coding agent kept interrupting me for
low-risk decisions that the repository already gave it enough evidence to make.

It is a local, open-source Agent Skill for Codex. It researches the codebase,
resolves reversible choices, and stops at material human gates. In visual mode,
it stores the decision state as portable JSON. If an earlier decision changes,
the dependent branch is invalidated and reassessed instead of being reused.

There is no hosted service or signup. Install it with:
npx skills add pengusto/let-him-grill -g -a codex -y

The demo, raw benchmark runs, limitations, and reference artifacts are in the
repo: https://github.com/pengusto/let-him-grill

I am most interested in whether the stop rules match how experienced developers
want Codex to behave, and where the skill should have stopped earlier or kept
going.
```

Attach `docs/demo-poster.png` and be explicit that the benchmark is product
evidence under one protocol, not a controlled model comparison.

## Directory summary — skillsdir.dev, if approved

Unique ID: `let-him-grill`

Summary (under 180 characters):

> Codex skill that resolves reversible planning decisions, records a portable path, and stops at material human gates.

Suggested verticals: `Developer Tools`, `AI`, `Productivity`.

Repository: <https://github.com/pengusto/let-him-grill>

Submit through the directory's GitHub issue template only after reviewing its
current requirements and getting owner approval.
