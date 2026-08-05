---
name: icloud-helper
description: |
  iCloud Drive management, folder sync, cloud storage, folder organization,
  local vs cloud toggle, iCloud backup, file sync management.
  Use when user wants to sync folders to iCloud, manage iCloud storage,
  move folders to/from iCloud, or check sync status.
---

# iCloud Helper

Manage iCloud Drive sync and folder synchronization.

## iCloud Location

iCloud Drive path: ~/Library/Mobile Documents/

## Core Functions

1. **Sync to iCloud** - COPY folder to iCloud (keeps local + cloud copy)
2. **Check sync status** - See which folders are in iCloud
3. **Verify sync** - Check if folder exists in both places
4. **Two-way sync** - Keep both local and iCloud identical

**Important**: All operations COPY (not move) - original stays local, iCloud gets duplicate.

## Folder Status

On macOS, folders can have these states:
- **Cloud with local cache** (downloaded)
- **Cloud only** (not downloaded, icon in Finder)
- **Local only** (not in iCloud)

Use `chflags nocloudstorage` to remove from iCloud
Use `chflags icloudstorage` to add to iCloud

## Important Folders to Sync

User may request these folders:
- ~/Library/Mobile Documents/com~apple~CloudDocs/AI/ → iCloud (AI projects and tasks)
- ~/Library/Mobile Documents/com~apple~CloudDocs/AI/AI apps/ → canonical working clones for application repositories
- ~/Documents/ → iCloud (personal docs)
- Custom folders as requested

## GitHub Application Clones

New application repositories belong directly under:
`/Users/moll/Library/Mobile Documents/com~apple~CloudDocs/AI/AI apps/`

Use `github-helper` for clone checks and GitHub operations. The existing folder
is spelled `AI apps` with uppercase `AI` and lowercase `apps`; do not silently
create a second casing variant.

## Commands

- "sync folder to icloud [path]" - Move folder to iCloud
- "make local [path]" - Remove from iCloud, keep local
- "check icloud status" - Show iCloud sync status
- "list icloud folders" - Show folders in iCloud Drive
- "download from icloud [path]" - Download cloud-only folder

## Scripts

- `sync_to_icloud.py` - Move folder to iCloud Drive
- `make_local.py` - Remove from iCloud, keep local
- `check_status.py` - Show iCloud sync status
- `list_icloud.py` - List folders in iCloud Drive
- `download_folder.py` - Download cloud folder locally

## Safety Rules

- ALWAYS confirm before moving folders to iCloud
- Explain what will happen before execution
- Provide rollback option (move back to local)
- NEVER delete - only MOVE or COPY

## Integration

This skill works with terminal-helper for executing commands.
Reference terminal-helper for terminal operations.

Related skills:
- **moll-helper** - For home folder organization
- **terminal-helper** - For terminal commands
