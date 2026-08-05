#!/bin/bash

TARGET=$1

if [ -z "$TARGET" ]; then
    echo "Usage: backup_files.sh <file-or-directory>"
    echo "Creates timestamped backup before making changes"
    exit 1
fi

if [ ! -e "$TARGET" ]; then
    echo "Error: '$TARGET' does not exist"
    exit 1
fi

BACKUP_DIR="$HOME/.terminal-helper-backups"
timestamp=$(date +%Y%m%d_%H%M%S)
mkdir -p "$BACKUP_DIR"

backup_name=$(basename "$TARGET")_$timestamp

if [ -d "$TARGET" ]; then
    backup_path="$BACKUP_DIR/${backup_name}.tar.gz"
    tar -czf "$backup_path" "$TARGET" 2>/dev/null
    echo "✓ Backup created: $backup_path"
    echo "  Compressed directory: $TARGET"
elif [ -f "$TARGET" ]; then
    backup_path="$BACKUP_DIR/${backup_name}"
    cp "$TARGET" "$backup_path"
    echo "✓ Backup created: $backup_path"
    echo "  Original file: $TARGET"
fi

echo ""
echo "Backup location: $BACKUP_DIR"
ls -lh "$BACKUP_DIR" | tail -5