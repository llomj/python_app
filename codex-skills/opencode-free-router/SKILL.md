---
name: opencode-free-router
description: |
  Use when user says "use opencode", asks to save credits, or wants a cheaper external-model path.
  Route Obsidian work through OpenCode without breaking the canonical iCloud vault rules.
---

You are an OpenCode routing skill focused on cost-aware execution.

## Canonical Vault Guard

- Active vault path: `/Users/moll/Library/Mobile Documents/iCloud~md~obsidian/Documents/AI brain`
- Finder/iPhone path: `iCloud Drive/Obsidian/AI brain`
- Never use `/Users/moll/Library/Mobile Documents/com~apple~CloudDocs/Obsidian/AI brain`
- Never modify `raw/` or `raw/Sources/`; treat them as read-only evidence
- Search before writing and update canonical notes instead of creating duplicates

## Provider Order

Choose based on the user's goal:

1. `OpenCode Go` for paid-but-working default use on this machine
2. Free OpenCode models when the user explicitly asks to save credits
3. Codex-native flow when reliability matters more than cost

Known good paid defaults:
- `opencode-go/kimi-k2.6`
- `opencode-go/deepseek-v4-flash`

Free-model priority chain:
1. Big Pickle
2. DeepSeek V4 Flash Free
3. MiniMax M2 Free
4. Nemotron 3 Super Free
5. Qwen3.6 Plus Free

## Preflight

Before routing:

1. `which opencode`
2. `opencode --version`
3. `opencode auth list`
4. confirm task path is inside the canonical vault
5. prefer the canonical Obsidian launcher when starting a fresh terminal OpenCode session:
   - `/Users/moll/Library/Mobile Documents/iCloud~md~obsidian/Documents/AI brain/scripts/opencode_obsidian.sh`

If `auth list` shows `OpenAI` with an `sk-or-v1` key, stop and repair auth first.

## Run Contract

When using OpenCode for vault work:

- State provider name in context
- State exact model name in context
- Use the external-model scaffold/run-note flow from `AGENTS.md`
- After the run, record:
  - prompt/input tokens
  - completion/output tokens
  - total tokens
  - estimated cost
- If OpenCode does not return usage metrics, record:
  - `token_usage: unavailable`
  - `reason: provider did not return usage metrics`

## Suggested Task Classes

Good fit:
- thin note expansion drafts
- note cleanup
- cross-link suggestion passes
- low-risk source summarization

Do not use as first choice for:
- destructive cleanup
- broad regex rewrites over the vault
- security-sensitive tasks
- path/sync repair
