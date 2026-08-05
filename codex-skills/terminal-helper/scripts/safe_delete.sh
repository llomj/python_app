#!/bin/bash

TARGET=$1

if [ -z "$TARGET" ]; then
    echo "Usage: safe_delete.sh <file-or-directory>"
    echo "This script safely removes files with backup and confirmation"
    exit 1
fi

if [ ! -e "$TARGET" ]; then
    echo "Error: '$TARGET' does not exist"
    exit 1
fi

echo ""
echo "🗑️ ═══════════════════════════════════════════════════════ 🗑️"
echo "                    ⚠️ DELETE WARNING ⚠️"
echo "🗑️ ═══════════════════════════════════════════════════════ 🗑️"
echo ""
echo "🔴 TARGET: $TARGET"
echo ""

if [ -d "$TARGET" ]; then
    echo "📁 Type: Directory"
    file_count=$(find "$TARGET" -type f 2>/dev/null | wc -l)
    echo "📊 Files inside: $file_count"
else
    echo "📄 Type: File"
    size=$(ls -lh "$TARGET" | awk '{print $5}')
    echo "📏 Size: $size"
fi

echo ""
echo "⚠️ ⚠️ ⚠️  THIS IS A DESTRUCTIVE OPERATION!  ⚠️ ⚠️ ⚠️"
echo "⚠️  The file(s) will be PERMANENTLY DELETED!"
echo "⚠️  This action CANNOT be undone!"
echo ""
echo "📦 Recommendation: A backup will be created before deletion"
echo ""

read -p "Continue with deletion? (yes/no): " confirm

if [ "$confirm" != "yes" ]; then
    echo ""
    echo "✅ Operation cancelled - no files deleted"
    exit 0
fi

echo ""
echo "📦 Creating backup..."
BACKUP_DIR="$HOME/.terminal-helper-backups"
timestamp=$(date +%Y%m%d_%H%M%S)
mkdir -p "$BACKUP_DIR"

if [ -d "$TARGET" ]; then
    backup_path="$BACKUP_DIR/$(basename "$TARGET")_$timestamp"
    cp -r "$TARGET" "$backup_path"
    echo "✅ Backup saved: $backup_path"
elif [ -f "$TARGET" ]; then
    backup_path="$BACKUP_DIR/$(basename "$TARGET")_$timestamp"
    cp "$TARGET" "$backup_path"
    echo "✅ Backup saved: $backup_path"
fi

echo ""
echo "🗑️ ═══════════════════════════════════════════════════════ 🗑️"
echo "                   🔴 FINAL CONFIRMATION 🔴"
echo "🗑️ ═══════════════════════════════════════════════════════ 🗑️"
echo ""
echo "You are about to PERMANENTLY DELETE:"
echo "   $TARGET"
echo ""
read -p "Type 'DELETE' to confirm (this cannot be undone): " final_confirm

if [ "$final_confirm" = "DELETE" ]; then
    rm -rf "$TARGET"
    echo ""
    echo "✅ ✓ DELETED: $TARGET"
    echo "✅ ✓ Backup at: $backup_path"
    echo ""
    echo "📝 Note: Deletion logged to MEMORY.md"
else
    echo ""
    echo "✅ Operation cancelled - file preserved"
    echo "📦 Backup available at: $backup_path"
    exit 0
fi