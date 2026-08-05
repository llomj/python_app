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

## Protected Content: No Deletion

- Never delete Jono's GitHub repositories or folders within them.
- Never run or approve `git rm`, destructive `git clean`, folder-removing sync,
  force-push deletion, or GitHub repository/content deletion APIs.
- A missing local folder is not authorization to remove its GitHub copy.
- On an initial deletion request, do not execute. Show
  `🛑 ⚠️ DELETION WARNING`, identify every exact repository/path, explain the
  impact, and ask for explicit confirmation.
- After first confirmation, still do not execute. Show
  `🛑 ⚠️ SECOND DELETION WARNING` and require a second explicit confirmation.
- Even after second confirmation, preserve the GitHub content and offer an
  in-repository archive or backup. Jono must perform permanent deletion manually.

## Application Repository Clone Policy

Canonical application clone root:
`/Users/moll/Library/Mobile Documents/com~apple~CloudDocs/AI/AI apps/`

Finder location:
`iCloud Drive/AI/AI apps/`

- Clone every new application repository directly to
  `AI apps/<repository-name>/` unless Jono explicitly chooses another location.
- Before cloning, verify the canonical root exists and search for an existing
  clone of the same GitHub remote to avoid duplicate working copies.
- Do not use Desktop, Documents, or the home folder as the default location for
  application repositories.
- The repository directory in `AI apps/` is the normal working clone; commits
  and pushes continue to use its GitHub `origin` remote.
- Infrastructure mirrors may use dedicated hidden locations. For example, the
  automated Codex-skill publisher uses `~/.codex/github-sync/` and is not an app
  development checkout.
- The existing folder is spelled `AI apps` with uppercase `AI` and lowercase
  `apps`. Do not perform a case-only rename without checking dependent paths.

Example:

```bash
git clone https://github.com/llomj/example-app.git \
  "/Users/moll/Library/Mobile Documents/com~apple~CloudDocs/AI/AI apps/example-app"
```

## Obsidian Vault Sync Policy

- For AI brain vault operations, repository is `https://github.com/llomj/Obsidian.git`.
- Sync behavior must match `AGENTS.md` in the vault (safe scope by default, explicit approval for raw/large deletions).
- Before push: run `git fetch` and inspect `git status -sb` to avoid divergence.
- If uncertainty exists around destructive changes, consult Jono before proceeding.
