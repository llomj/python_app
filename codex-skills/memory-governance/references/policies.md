# Policies

## Security
- Never output passwords, secrets, tokens, or private keys.
- Redact sensitive values from logs before sharing.

## Destructive Actions
- Never permanently delete content from iCloud Drive or folders/repositories from Jono's GitHub.
- Initial request: do not execute; show `🛑 ⚠️ DELETION WARNING`, exact targets, impact, and recovery risk.
- First confirmation: still do not execute; show `🛑 ⚠️ SECOND DELETION WARNING` and require a second confirmation.
- Second confirmation: offer only a recoverable archive or backup. Permanent deletion must be performed manually by Jono.
- Never use `rsync --delete`, `git rm`, `git clean`, destructive GitHub APIs, or equivalent commands on protected content.

## Publishing
- Canonical repo: `https://github.com/llomj/python_app.git`
- Required path: `codex-skills/<skill-name>/`
