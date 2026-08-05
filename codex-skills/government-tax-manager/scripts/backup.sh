#!/bin/bash

BASE_PATH="/Users/moll/Library/Mobile Documents/com~apple~CloudDocs/Documents/Personal /Government"
BACKUP_PATH="$BASE_PATH/backups"

if [ ! -d "$BASE_PATH" ]; then
  echo "Error: Base government folder not found"
  exit 1
fi

mkdir -p "$BACKUP_PATH"

TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_NAME="government_backup_$TIMESTAMP.tar.gz"
BACKUP_FILE="$BACKUP_PATH/$BACKUP_NAME"

echo "Creating backup: $BACKUP_NAME"
tar -czf "$BACKUP_FILE" -C "$BASE_PATH" .. 2>/dev/null || tar -czf "$BACKUP_FILE" "$BASE_PATH" 2>/dev/null

if [ -f "$BACKUP_FILE" ]; then
  SIZE=$(du -h "$BACKUP_FILE" | cut -f1)
  echo "Backup created: $SIZE"
  echo "Location: $BACKUP_FILE"
  
  echo ""
  echo "Recent backups:"
  ls -lh "$BACKUP_PATH" | tail -5
else
  echo "Backup failed"
  exit 1
fi