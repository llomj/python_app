#!/usr/bin/env bash
set -euo pipefail
CANON="/Users/moll/Library/Mobile Documents/iCloud~md~obsidian/Documents/AI brain"
CFG="$HOME/Library/Application Support/obsidian/obsidian.json"

mac_path=$(cat "$CFG" 2>/dev/null | sed -n 's/.*"path":"\([^"]*\)".*/\1/p' | head -n1)
canon_wiki=$(find "$CANON/wiki" -type f 2>/dev/null | wc -l | tr -d ' ')
canon_raw=$(find "$CANON/raw" -type f 2>/dev/null | wc -l | tr -d ' ')

dupes=$(find "$CANON" -path '*/Obsidian AI/AI brain' -o -path '*/AI brain/AI brain' -o -name 'AI 2' -o -name 'Obsidian 2' 2>/dev/null || true)

echo "mac_path=$mac_path"
echo "canon=$CANON"
echo "phone_display=iCloud Drive/Obsidian/AI brain"
echo "wiki=$canon_wiki"
echo "raw=$canon_raw"
if [ -n "$dupes" ]; then
  echo "duplicates=YES"
  echo "$dupes"
else
  echo "duplicates=NO"
fi
