---
name: terminal-helper
description: |
  Use when user needs help with terminal commands, understanding flags, or navigating the terminal.
  Use when user wants to execute shell commands or check system status.
  Use for security audits and permission checks.
  CRITICAL: Never delete files without explicit user approval.
---

You are a terminal operations assistant.

## Available Commands

- ls, cd, pwd - Navigation
- chmod, chown - Permissions
- ps, top - Process monitoring
- grep, find - File search

## Safety Rules

- Always explain commands before execution
- Never run destructive commands without approval
- Backup before risky operations

## Scripts

Available in scripts/ folder:
- explain_command.sh - Explain any terminal command
- safe_delete.sh - Safe file deletion with backup
- system_info.sh - System information
- security_audit.sh - Security checks

## GitHub Repository

**Repo:** https://github.com/llomj/Terminal.git

**To commit changes:**
1. Use github-helper skill
2. Say "commit terminal-helper" or "push terminal changes"

## Related Skills

- **github-helper** - For committing terminal-helper changes to GitHub
  - Use for: commit, push, open Terminal repo
  - Trigger: "commit terminal", "push to Terminal"

- **moll-helper** - For home folder organization and cleanup
  - Use for: analyzing home folder, cleaning up files, organizing projects
  - Trigger: "organize home", "clean home", "analyze home"

- **icloud-helper** - For iCloud sync and folder backup
  - Use for: sync folders to iCloud, check sync status, backup to cloud
  - Trigger: "sync to icloud", "check icloud status", "backup folder"
  - **Note**: Uses COPY (keeps local + cloud duplicate), not MOVE

- **github-helper** - For opening GitHub in browser
  - Trigger: "open github"

- **government-tax-manager** - For tax/financial management
  - Trigger: "tax", "expenses", "invoices"

- **skill-organizer** - For syncing skills to GitHub
  - Trigger: "sync skills", "commit skills"

## Codex Personal Skills Troubleshooting

**Known Issue**: New personal skills sometimes don't appear in Codex UI skill list even when properly configured.

**Symptoms**:
- Skill folder exists in ~/.codex/skills/ with SKILL.md
- agents/openai.yaml created with interface fields
- Skill still doesn't show in Codex personal skills list

**Debugging Steps**:
1. Verify folder structure: ls -la ~/.codex/skills/[skill-name]/
2. Check SKILL.md has valid YAML frontmatter with name and description
3. Clear cache: rm -rf ~/.codex/cache/codex_app_directory/*.json
4. Restart Codex completely (quit and reopen)
5. Force trigger by typing the skill name in conversation

**Root Cause**: Codex caches skill list. New skills may not appear until cache rebuilds.

**Workaround**: Skills still work via keyword triggering even if not visible in UI list.

## Creating New Skills

When creating new Codex personal skills:
1. Create folder: ~/.codex/skills/[skill-name]/
2. Add SKILL.md with YAML frontmatter (name, description)
3. Optional: Add agents/openai.yaml for UI visibility
4. Clear cache: rm -rf ~/.codex/cache/codex_app_directory/*.json
5. Restart Codex

## Obsidian Vault Sync Policy

- For AI brain vault operations, target repository is `https://github.com/llomj/Obsidian.git`.
- Coordinate with `obsidian-helper` and `github-helper` so commit scope and push behavior are consistent.
- Before any push for AI brain: run `git fetch`, inspect `git status -sb`, and verify staged scope.
- For deletion/cleanup tasks: record deleted path categories and estimated sizes in vault tracking notes (`track.md` and/or `log.md`).
- If there is uncertainty about deleting/moving/restructuring files, stop and consult Jono before proceeding.

## Obsidian iCloud Provider Path Note (Updated 2026-05-31)

When Obsidian appears empty on iPhone while Mac has data, first verify both apps are using the same Obsidian provider container:

- Canonical filesystem path:
  - `/Users/moll/Library/Mobile Documents/iCloud~md~obsidian/Documents/AI brain`
- Finder/iPhone display:
  - `iCloud Drive/Obsidian/AI brain` with the Obsidian icon

Recovery pattern:
1. Verify Mac Obsidian config points to the canonical filesystem path.
2. Verify File Provider upload state for `wiki`, `raw`, `schema`, `templates`, and `scripts`.
3. Force-close/reopen iPhone Obsidian and recheck counts/search.
4. Never run concurrent rsync mirrors; avoid renames during active iCloud sync.

## Obsidian Blank Screen Recovery

Use this command when Obsidian opens to a blank window after relaunch:

```bash
~/.agents/skills/obsidian-helper/scripts/obsidian_recover_open.sh --safe
```

This command force-quits Obsidian, points startup to the canonical iCloud vault, disables hardware acceleration, resets workspace/plugins in safe mode, and relaunches.
