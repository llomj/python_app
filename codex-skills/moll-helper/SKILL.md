---
name: moll-helper
description: |
  Home folder organization, file management, cleanup, system maintenance,
  dotfiles management, project organization, storage analysis.
  Use when user wants to clean, organize, or understand their home folder (~).
---

# Moll Helper

Manage and organize the user's home folder (~).

## Home Folder Structure

Current home folder contains:
- **Hidden config folders** (.codex, .cursor, .openclaw, .config, etc.)
- **AI/ML tools** (.ollama, .lmstudio, .antigravity, .aitk)
- **Dev tools** (.npm, .bun, .gem, .opencode, .claude)
- **Project files** (loose files in root: package.json, node_modules, etc.)
- **Media/Backup** (.Trash, .dropbox)
- **Shell configs** (.bashrc, .myaliases, .zshrc)

## Organization Strategy

**Recommended structure:**
```
~/Clean/           # Move loose project files here
├── projects/      # Development projects
├── scripts/      # Personal scripts
└── archives/     # Old projects to archive

~/Documents/       # Standard Documents folder
~/Downloads/      # Standard Downloads folder
```

## Cleanup Tasks

1. **Identify loose files** - Files in ~ root that should be in subfolders
2. **Find large files** - Use disk analysis to find space hogs
3. **Organize config files** - Group similar dotfiles
4. **Archive old projects** - Move inactive projects to archive

**NEVER delete files without explicit user approval.**
- Only MOVE files, never DELETE
- Always ask before removing anything
- Use safe_move with backup option
- .Trash cleanup requires explicit permission

## Scripts

- `analyze_home.py` - Analyze home folder, show size breakdown
- `organize_home.py` - Suggest/move files to organized structure
- `find_large_files.py` - Find largest files taking space

## Commands

- "analyze home" - Show folder analysis
- "clean home" - Suggest cleanup items
- "organize home" - Move files to proper locations
- "find large files" - Show largest files

## Integration

This skill works with terminal-helper for executing commands.
Reference terminal-helper for terminal operations.

## Related Skills

- **icloud-helper** - After organizing, sync important folders to iCloud
  - Use for: backup folders to iCloud, create local + cloud duplicates
  - Trigger: "sync to icloud", "backup folder to cloud"