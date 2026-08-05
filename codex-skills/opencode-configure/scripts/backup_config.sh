#!/bin/bash

BACKUP_DIR="$HOME/.config/opencode/backups"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

mkdir -p "$BACKUP_DIR"

backup_file() {
    local file=$1
    local name=$(basename "$file")
    if [ -f "$file" ]; then
        cp "$file" "$BACKUP_DIR/${name}.${TIMESTAMP}"
        echo "Backed up: $file -> $BACKUP_DIR/${name}.${TIMESTAMP}"
    fi
}

echo "=== OpenCode Configuration Backup ==="
echo "Timestamp: $TIMESTAMP"
echo ""

echo "Backing up configs..."
backup_file "$HOME/.config/opencode/opencode.json"
backup_file "$HOME/.config/opencode/opencode.jsonc"

if [ -f "opencode.json" ]; then
    backup_file "opencode.json"
fi
if [ -f "opencode.jsonc" ]; then
    backup_file "opencode.jsonc"
fi

echo ""
echo "Backup complete. Backups stored in: $BACKUP_DIR"

ls -1t "$BACKUP_DIR" | head -5