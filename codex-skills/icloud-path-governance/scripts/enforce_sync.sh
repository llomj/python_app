#!/usr/bin/env bash
set -euo pipefail

CANON="/Users/moll/Library/Mobile Documents/iCloud~md~obsidian/Documents/AI brain"
CFG="$HOME/Library/Application Support/obsidian/obsidian.json"
TRACK="$CANON/track.md"
LOCK="/tmp/icloud-path-governance.lock"
TS="$(date '+%Y-%m-%d %H:%M:%S')"

if [ -e "$LOCK" ]; then
  echo "Lock exists: $LOCK" >&2
  exit 1
fi
trap 'rm -f "$LOCK"' EXIT
touch "$LOCK"

if [ ! -d "$CANON" ]; then
  echo "canonical vault missing: $CANON" >&2
  exit 2
fi

mac_before=$(cat "$CFG" 2>/dev/null | sed -n 's/.*"path":"\([^"]*\)".*/\1/p' | head -n1)

cat > "$CFG" <<JSON
{"vaults":{"aibrain":{"path":"$CANON","ts":1780180000000,"open":true}},"cli":true}
JSON

wiki_count="$(find "$CANON/wiki" -type f 2>/dev/null | wc -l | tr -d ' ')"
raw_count="$(find "$CANON/raw" -type f 2>/dev/null | wc -l | tr -d ' ')"
mac_after=$(cat "$CFG" 2>/dev/null | sed -n 's/.*"path":"\([^"]*\)".*/\1/p' | head -n1)
dupes="$(find "$CANON" -path '*/Obsidian AI/AI brain' -o -path '*/AI brain/AI brain' -o -name 'AI 2' -o -name 'Obsidian 2' 2>/dev/null || true)"

{
  echo
  echo "## Path Governance Update ($TS)"
  echo "- Enforced Mac Obsidian path lock."
  echo "- mac_path_before: $mac_before"
  echo "- mac_path_after: $mac_after"
  echo "- canonical_vault: $CANON"
  echo "- wiki_files: $wiki_count"
  echo "- raw_files: $raw_count"
  echo "- duplicate_active_roots: ${dupes:-none}"
  echo "- note: Mac and iPhone use the same Obsidian provider container; no mirror operation was run."
} >> "$TRACK"

echo "path lock enforced"
