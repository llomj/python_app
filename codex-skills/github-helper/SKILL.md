---
name: github-helper
description: |
  GitHub management, repository operations, issues, PRs, commits, GitHub Actions,
  browser automation, URL opening. Use when user mentions GitHub, wants to open
  GitHub, check repos, manage issues.
---

# GitHub Skill

Open and manage GitHub in default browser. Uses GitHub CLI (gh) for authentication.

## Behaviors

When user asks to "open GitHub" or similar:
- Use `open` command to launch GitHub in default browser
- User logs in manually in browser (browser remembers session)

Default URL: https://github.com
Can open specific repos: https://github.com/llomj/[repo]

## Commands

- "open github" → opens github.com
- "open my github" → opens github.com/llomj
- "open repo [name]" → opens github.com/llomj/[name]
- "github status" → check GitHub auth status
- "open terminal repo" → opens github.com/llomj/Terminal
- "commit terminal" → commit and push Terminal folder changes

## Scripts

- `open_github.py` - Opens GitHub URLs in browser
- `github_status.py` - Check GitHub status

## GitHub Username

llomj
## Obsidian Vault Sync Policy

- For AI brain vault operations, repository is `https://github.com/llomj/Obsidian.git`.
- Sync behavior must match `AGENTS.md` in the vault (safe scope by default, explicit approval for raw/large deletions).
- Before push: run `git fetch` and inspect `git status -sb` to avoid divergence.
- If uncertainty exists around destructive changes, consult Jono before proceeding.
