---
name: memory-governance
description: Manage persistent memory rules, cross-project skill indexing, and publish-state tracking for Codex skills. Use when updating memory policies, tracking skill changes, deciding when to commit and push, and enforcing security guardrails.
---

# Memory Governance

Maintain memory policies and track skill update lifecycle across projects.

## Track States

For every skill, track:
- `update_state`: `unchanged|modified`
- `commit_state`: `not_committed|committed`
- `push_state`: `not_pushed|pushed`
- `last_commit`
- `last_push_date_utc`

## Workflow

1. Detect skill changes.
2. Update tracking row in [references/projects-index.md](references/projects-index.md).
3. If modified, set `update_state=modified` and `push_state=not_pushed`.
4. Commit skill files and set `commit_state=committed` plus `last_commit`.
5. Push to `https://github.com/llomj/Skills.git` and set `push_state=pushed` plus `last_push_date_utc`.
6. Log high-risk actions in [references/audit-log.md](references/audit-log.md).

## Guardrails

- Never reveal secrets or credentials.
- Before destructive actions, require explicit confirmation with `⚠️` and exact path.
- Never publish skills to non-canonical repositories.
