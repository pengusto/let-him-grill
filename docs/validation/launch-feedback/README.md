# Launch feedback log

This is a versioned, consent-safe log template. No external messages have been
sent from this repository by Codex.

## Publication log

Record one row per manually published item:

| Date (UTC) | Channel | Draft | URL | Asset | Owner action | Notes |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

Do not record private messages, email addresses, usernames, raw repository
content, access tokens, or personal identifiers without explicit consent.

## Feedback categories

Use categories instead of copying private conversations:

- `install`: command, agent detection, or target path failed
- `discovery`: skill was not found or did not activate
- `invocation`: skill activated but the workflow diverged
- `decision-boundary`: it stopped too early or continued too far
- `artifact`: state, render, or export was confusing or wrong
- `resume`: a later task could not continue the artifact
- `compatibility`: host or companion-skill behavior differed
- `documentation`: user could not find or understand an instruction

For each repeated issue, record only:

```text
Date:
Category:
Environment:
Reproducible: yes/no/unknown
Observed failure:
Expected behavior:
Evidence link or issue:
Consent-safe summary:
```

Open at most three follow-up issues, and only when the same problem repeats or
blocks installation, invocation, artifact completion, or resume. Stars and
upvotes are discovery signals, not feedback quality.
