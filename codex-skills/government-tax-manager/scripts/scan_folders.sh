#!/bin/bash

BASE_PATH="/Users/moll/Library/Mobile Documents/com~apple~CloudDocs/Documents/Personal /Government"

if [ ! -d "$BASE_PATH" ]; then
  echo "Error: Base government folder not found at $BASE_PATH"
  exit 1
fi

echo "=== Government Tax Manager - Folder Scan ==="
echo "Base path: $BASE_PATH"
echo ""

echo "=== Folder Structure ==="
find "$BASE_PATH" -maxdepth 2 -type d 2>/dev/null | sort

echo ""
echo "=== File Counts by Folder ==="
for folder in "$BASE_PATH"/*/; do
  if [ -d "$folder" ]; then
    name=$(basename "$folder")
    count=$(find "$folder" -type f 2>/dev/null | wc -l)
    echo "$name: $count files"
  fi
done

echo ""
echo "=== Recent Files (last 10) ==="
find "$BASE_PATH" -type f -exec ls -lt {} + 2>/dev/null | head -10 | awk '{print $9, $6, $7, $8}'

echo ""
echo "=== File Types ==="
find "$BASE_PATH" -type f 2>/dev/null | sed 's/.*\.//' | sort | uniq -c | sort -rn

echo ""
echo "Scan complete."