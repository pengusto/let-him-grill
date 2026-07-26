# Viral agent skills, May–July 2026

Research snapshot: 26 July 2026. Scope: reusable skills and skill packs for Claude Code, Codex and other Agent Skills-compatible harnesses.

## Executive finding

The strongest recent breakouts did not win as broad prompt libraries. They led with one behavior that can be understood and demonstrated in a sentence, made installation nearly frictionless, and only then expanded into a workflow or ecosystem.

The closest analogue is Matt Pocock's `grill-me` / `grill-with-docs`: the same core promise as Let Him Grill already has enormous distribution. Competing as another generic “agent asks hard questions” skill is therefore a weak position. Let Him Grill's defensible direction is the part Matt's version does not own: a **visible, resumable decision-state artifact** that can be inspected, shared, edited and handed back to any coding agent.

## What the numbers mean

- skills.sh says its leaderboard is powered by anonymous CLI installation telemetry; its API defines `installs` as a “total deduplicated install count”. It is stronger evidence than stars, but still measures installation, not retention or successful use. ([FAQ](https://www.skills.sh/docs/faq), [API reference](https://www.skills.sh/docs/api))
- “Trending” is recent growth; “Hot” compares the current hour with the same hour yesterday. These are live snapshots, not a downloadable historical series. ([API reference](https://www.skills.sh/docs/api))
- GitHub stars measure attention. They are not active users or installations.
- “First seen” means first indexed by skills.sh, not necessarily the skill's first commit.
- Approximate rates below divide today's count by days since “first seen”. They describe cumulative pace, not a true daily time series.

## Strongest cases

### 1. `grill-me` and `grill-with-docs`: a memorable trick became a workflow

**What they do.** `grill-me` interviews the user branch by branch until a plan is understood. `grill-with-docs` grounds the interview in the codebase and domain language and can update `CONTEXT.md` and architectural decisions. The publisher describes them as the repository's most popular skills. ([repository and product explanation](https://github.com/mattpocock/skills), [grill-me](https://www.skills.sh/mattpocock/skills/grill-me), [grill-with-docs](https://www.skills.sh/mattpocock/skills/grill-with-docs))

**Verified snapshot and trajectory.**

- `grill-me`: first seen 13 March; 665,000+ installs on 26 July; roughly 4,900 cumulative installs/day since indexing.
- `grill-with-docs`: first seen 28 April; 563,000+ installs in about 89 days; roughly 6,300/day.
- On 26 July they still ranked around 6,700 and 5,800 installs in the 24-hour Trending view, plus 262 and 226 installs in the current Hot hour. This is sustained distribution, not merely an old launch spike. ([live leaderboard](https://www.skills.sh/trending), [live hot view](https://www.skills.sh/hot))
- The parent repository showed about 189,000 stars and 16,200 forks. Its README also points to a newsletter audience of about 60,000 developers. ([GitHub repository](https://github.com/mattpocock/skills))

**How it evolved.** The June 1.0 release changed the collection from loose commands into reusable user-invoked and model-invoked components, introduced an `ask-matt` router and made `grilling` the shared primitive behind both front doors. The 8 July 1.1 release sharpened the human decision gate and connected the flow from idea to spec, tickets, implementation and review. ([release history](https://github.com/mattpocock/skills/releases))

**Likely viral mechanism — inference.**

1. The name is provocative, easy to repeat and describes the experience.
2. The result is visible during the first run: the agent behaves differently immediately.
3. One-line installation works across agents; Claude users can also subscribe through a managed plugin.
4. A trusted educator shipped his real workflow, then amplified it through an existing audience.
5. The atomic hero skill became the entry point to a larger, coherent suite.

### 2. `gstack`: sell the whole personal operating system

**What it does.** Garry Tan's pack turns Claude Code into named roles spanning CEO review, design, engineering planning, QA, shipping, security and post-deploy monitoring. The product is a complete software lifecycle, not one prompt. ([primary repository](https://github.com/garrytan/gstack), [changelog](https://github.com/garrytan/gstack/blob/main/CHANGELOG.md))

**Verified snapshot.** GitHub's API reports the repository was created 11 March 2026 and had about 124,500 stars and 18,600 forks on 26 July. ([GitHub API](https://api.github.com/repos/garrytan/gstack))

**Reconstructed trajectory.** Public GitHub-data analyses recorded about 50,400 stars by 27 March; later public snapshots place it around 82,700 in early May and 106,000 near late June before reaching 124,500 in late July. These intermediate figures are secondary reconstructions, not official gstack analytics, so they establish direction rather than exact daily growth. ([OSSInsight analysis](https://ossinsight.io/blog/personal-ai-stacks-2026), [current primary snapshot](https://api.github.com/repos/garrytan/gstack))

**Likely viral mechanism — inference.** A well-known founder packaged his own operating style; role names make an abstract workflow tangible; one install promises an entire “team”; and frequent, visible releases continually supplied new stories to share.

### 3. `caveman`: a meme with a measurable before/after

**What it does.** Caveman forces terse output while preserving technical content. The promise is immediate and quantifiable rather than architectural. ([skill page](https://www.skills.sh/juliusbrussee/caveman/caveman), [repository](https://github.com/JuliusBrussee/caveman))

**Verified snapshot and trajectory.** It was first seen on 4 April and showed about 383,000 installs by 26 July, roughly 3,400 cumulative installs/day. The current repository presents a ten-prompt benchmark rather than relying only on a slogan. May releases added multi-agent installer detection, terse subagents, MCP description compression and first-class OpenClaw/OpenCode support; follow-up patches quickly repaired one-line installation failures. ([releases](https://github.com/JuliusBrussee/caveman/releases))

**Likely viral mechanism — inference.** Meme-quality naming makes the value shareable; users can see token reduction in any response; benchmark receipts make the claim concrete; and broad harness support increases the reachable market. The repair releases also show the post-viral burden: installation reliability and defensible claims become product features.

### 4. `superpowers`: methodology as executable guardrails

**What it does.** Superpowers turns practices such as brainstorming, worktree isolation, planning, TDD, subagent execution, review and verification into enforced agent behavior. Its `brainstorming` skill alone showed about 296,000 skills.sh installs on 26 July. ([repository](https://github.com/obra/superpowers), [brainstorming skill](https://www.skills.sh/obra/superpowers/brainstorming))

**Verified snapshot.** GitHub's API showed about 261,000 stars and 23,000 forks. ([GitHub API](https://api.github.com/repos/obra/superpowers))

**Growth-period product moves.** Releases expanded support across Claude, Codex, Cursor, Gemini and OpenCode, added plugin distribution and tested actual agent triggering and behavior rather than treating Markdown existence as success. ([release history](https://github.com/obra/superpowers/releases))

**Likely viral mechanism — inference.** It promises repeatable engineering discipline, not model magic. Plain-text rules are inspectable and adaptable, while tests and hard gates build trust with serious developers.

### 5. `paperclip`: the skill as an acquisition surface for a larger product

**What it does.** Paperclip's skills expose an agent control plane: heartbeat work windows, budgets, reporting chains, governance-aware agent creation and API contracts. The skill is an interface into the Paperclip product, not the whole product itself. ([core skill](https://github.com/paperclipai/paperclip/blob/master/skills/paperclip/SKILL.md), [create-agent companion](https://github.com/paperclipai/paperclip/blob/master/skills/paperclip-create-agent/SKILL.md))

**Verified breakout signal.** The canonical skill was first seen on 2 July and reached roughly 158,000 installs within the month; its six-skill publisher family approached one million aggregate installs in the late-July skills.sh snapshot. Treat this as an early breakout, not proof of retention. ([skill page](https://www.skills.sh/getpaperclipai/paperclip/paperclip), [product releases](https://github.com/paperclipai/paperclip/releases))

**Likely viral mechanism — inference.** A free portable skill removes onboarding friction for a larger tool. Companion skills cross-promote one another, while governance and orchestration address a timely pain point that a static prompt cannot solve.

## Pattern across the winners

1. **One sentence first.** “Grill my plan,” “cut agent verbosity,” or “give Claude a full engineering team” is easier to transmit than a feature list.
2. **The behavior is observable.** Users can screenshot the interrogation, token reduction, design result or workflow immediately.
3. **Install is one command.** Cross-agent portability multiplies the addressable audience.
4. **The source is inspectable.** Markdown lowers perceived commitment and invites adaptation.
5. **Credibility precedes breadth.** A known creator, official vendor or measurable benchmark supplies trust.
6. **Expansion follows the hero.** Winners add routers, complementary skills, plugins or a product after the entry behavior has traction.
7. **Trust becomes operational.** Security audits, pinned content, reliable installers and honest benchmarks matter once distribution grows.

## Implications for Let Him Grill

### Positioning decision

Do **not** position it primarily as another grilling prompt. That category is already owned by a creator with more than half a million installs per relevant skill.

Recommended category:

> **The visual decision-state companion for coding agents.** It turns an ambiguous conversation into a resumable tree of resolved choices, open branches and a clean handoff.

The product proof should be the artifact, not the questioning style.

### Product moves, in order

1. **Make the artifact unmistakable.** A completed run should leave one portable decision file plus the interactive tree. It must survive session changes and work across Claude Code, Codex and GitHub Copilot.
2. **Lead with a 20-second before/after.** Before: a vague request and hidden assumptions. After: a visible tree with decisions, unresolved branches and one handoff action. Show this in the README GIF and Pages demo.
3. **Publish through the existing ecosystem.** Ensure `npx skills add <owner>/<repo>` installs cleanly into supported harnesses and that the skills.sh page has a precise, searchable description. Avoid a custom installer until the portable path proves insufficient.
4. **Measure the claim.** Track questions asked, branches resolved, decisions changed after inspection, handoff completeness and implementation rework in the existing benchmark. Avoid claiming “better decisions” without a reproducible comparison.
5. **Keep one hero skill.** Do not launch a suite yet. A router and satellite skills only pay off after users repeatedly ask for adjacent workflows.
6. **Use Molebyte as recognition, not the value proposition.** The mascot can make demos and release posts recognizable; the decision artifact must remain the reason to install.
7. **Add trust early.** Pin remote references, document what the skill may write, keep legal/privacy claims accurate, and submit the published skill to the available ecosystem audits.

### A practical 30-day validation plan

- **Week 1:** make a clean install from an empty test repository the acceptance test; record Claude Code and Codex runs.
- **Week 2:** create three short, real scenarios—feature planning, architecture choice and release decision—with downloadable final artifacts.
- **Week 3:** publish the 20-second demo and the exact one-line install; submit/list it on skills.sh and relevant Claude/Codex directories.
- **Week 4:** compare install-to-first-completed-tree, completed-tree-to-handoff and repeat-run rates. Interview users who started but did not finish.

The go/no-go signal is not GitHub stars. It is whether strangers complete a tree, hand it to an agent and return for a second decision.

## Research limits

There is no authoritative public daily-install history for most skills. skills.sh provides live deduplicated totals plus short-window Trending/Hot views; GitHub exposes current repository metadata but not a native historical star series. Historical checkpoints above are therefore labeled as reconstructions. Counts can also change between cached pages, so rounded values are more honest than single-install precision.
