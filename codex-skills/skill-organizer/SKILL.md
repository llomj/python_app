---
name: skill-organizer
description: |
  Skill management, organization, automatic GitHub backups, sync, GitHub commits,
  and cross-tool skill sharing.
  Use for: managing skills, syncing across tools, organizing folders, version control,
  skill organization, automation.
---

# Skill Organizer

Manage skills across Codex, OpenCode, Cursor, and Antigravity.

## Central Location

Codex runtime source:
`/Users/moll/.codex/skills/`

GitHub automation checkout:
`/Users/moll/.codex/github-sync/python_app/codex-skills/`

Desktop working checkout:
`/Users/moll/Desktop/python_app/codex-skills/`

Repository:
`https://github.com/llomj/python_app.git`

The repository's GitHub folder is a non-destructive backup of user-authored Codex skills.
The background job uses its private checkout because macOS blocks LaunchAgents
from Desktop. Exclude Codex-managed `.system/` content and the recursive
`user-codex-skills` symlink.

Cross-tool base path:
`/Users/moll/Library/Mobile Documents/iCloud~md~obsidian/Documents/AI brain/AI skills/`

Structure:
```
AI skills/
├── codex-skills/      # canonical user-authored cross-tool skills
├── opencode-skills/   # OpenCode runtime mirror
└── cursor-skills/     # Cursor reusable skills, never extension installs
```

## Tasks

1. **Sync Skills**: Align canonical user-authored skills to local runtimes
2. **Organize**: Place new skills in correct tool folder based on source
3. **Cross-reference**: Ensure skills work across all tools (scripts work everywhere)
4. **Commit**: Automatically mirror, commit, and push Codex skill changes to GitHub
5. **Align**: Keep skills consistent across tools

## Workflow

When new skill created in any tool:
1. Create or update the skill under `~/.codex/skills/`.
2. The `com.user.skill-sync` LaunchAgent mirrors it to the GitHub repository.
3. Run the cross-tool synchronizer when the skill must also be aligned to other runtimes.
4. Verify GitHub automation logs if the repository copy is not current.

## Auto-Sync Behavior

The synchronizer is non-destructive: it updates matching skill directories but
does not delete extra runtime skills.

## Commands

- "sync skills" - Run dry-run, then apply safe alignment
- "organize skill [name]" - Move skill to correct folder, then sync
- "commit skills" - Just commit to GitHub
- "check alignment" - Verify skills work across tools

## GitHub

The `com.user.skill-sync` LaunchAgent watches `~/.codex/skills` and also runs every
five minutes. It uses `scripts/sync_to_github.py` to add or update meaningful
skill files, scan for common secret formats, verify `origin/main`, commit only
`codex-skills/`, and push. It never deletes older GitHub content when a local
source disappears. It stops rather than pushing unrelated commits or branch
divergence.

## Cross-Tool Compatibility

Scripts (Python/Bash) work everywhere - prioritize these over tool-specific formats.
Keep skill definitions in Markdown for portability.

## Commands

```bash
python3 ~/.codex/skills/skill-organizer/scripts/sync_to_github.py --dry-run
python3 ~/.codex/skills/skill-organizer/scripts/sync_to_github.py
python3 "AI skills/codex-skills/skill-organizer/scripts/sync_skills.py"
python3 "AI skills/codex-skills/skill-organizer/scripts/sync_skills.py" --apply
```
