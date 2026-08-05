# iCloud Path Governance v2

Use when Obsidian/Codex path drift, duplicate iCloud roots, or Mac/iPhone sync mismatch occurs.

## Canonical Contract

- Canonical vault (source of truth):
  - `/Users/moll/Library/Mobile Documents/iCloud~md~obsidian/Documents/AI brain`
- iPhone/Files visible location for the same provider container:
  - `/Users/moll/Library/Mobile Documents/iCloud~md~obsidian/Documents/AI brain`
  - `iCloud Drive/Obsidian/AI brain` with the Obsidian icon

## Guarantees

1. Mac Obsidian path remains pinned to canonical vault.
2. Mac and iPhone read the same Obsidian provider container; lower phone counts usually mean iCloud/Obsidian mobile indexing lag unless a second real vault root is found.
3. Duplicate roots are detected and quarantined/archived.
4. Every run is logged to:
   - `track.md` and/or `log.md`

## Run Modes

- Drift check only:
  - `scripts/check_drift.sh`
- Enforce sync + path lock:
  - `scripts/enforce_sync.sh`

## Required Preflight

- Verify current Mac Obsidian path.
- Verify provider upload state for `wiki`, `raw`, `schema`, `templates`, and `scripts`.
- Detect duplicate roots (`AI 2`, `Obsidian 2`, archive variants).

## Safety Rules

- Use single-process lock (no concurrent rsync loops).
- Archive before delete.
- No destructive cleanup unless explicitly approved.

## Post-Run

- Append short summary to `ps.md`, `track.md`, and/or `log.md`.
