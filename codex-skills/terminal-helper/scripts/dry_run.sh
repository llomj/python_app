#!/bin/bash

# Dry-run mode - Preview what a command would do without executing

COMMAND=$1

if [ -z "$COMMAND" ]; then
    echo "Usage: dry_run.sh <command>"
    echo "Example: dry_run.sh 'rm -rf /tmp/test'"
    echo ""
    echo "🔍 This script previews potentially dangerous commands"
    exit 1
fi

echo "═══════════════════════════════════════════════════════════════"
echo "                    🔍 DRY-RUN MODE 🔍"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "Command to preview: $COMMAND"
echo ""

# Analyze command for safety
case "$COMMAND" in
    *rm\ -rf*)
        echo "⚠️  ⚠️  ⚠️  DESTRUCTIVE COMMAND DETECTED  ⚠️  ⚠️  ⚠️"
        echo ""
        echo "This command would DELETE files!"
        echo ""
        
        # Extract the target
        target=$(echo "$COMMAND" | sed 's/.*rm -rf //')
        
        if [ "$target" = "/" ]; then
            echo "🔴 🔴 🔴  CRITICAL: THIS WOULD DELETE YOUR ENTIRE SYSTEM!  🔴 🔴 🔴"
            echo ""
            echo "This command is BLOCKED and should NEVER be executed!"
            exit 1
        elif [ "$target" = "*" ]; then
            echo "🔴 WARNING: This would delete ALL files in current directory!"
            ls -la
        else
            echo "📁 Would affect: $target"
            if [ -e "$target" ]; then
                echo "📊 Files that would be affected:"
                if [ -d "$target" ]; then
                    ls -la "$target" | head -20
                else
                    ls -la "$target"
                fi
            else
                echo "⚠️  Target does not exist"
            fi
        fi
        ;;
    *chmod\ -R\ 777*)
        echo "⚠️  WARNING: OVERLY PERMISSIVE CHMOD DETECTED"
        echo ""
        echo "This makes files WORLD-WRITABLE - security risk!"
        ;;
    *dd\ of=*)
        echo "⚠️  ⚠️  ⚠️  DISK WRITE COMMAND DETECTED  ⚠️  ⚠️  ⚠️"
        echo ""
        echo "This could DESTROY data on a disk!"
        ;;
    *chown\ -R*)
        echo "⚠️  WARNING: RECURSIVE OWNERSHIP CHANGE"
        echo ""
        echo "This changes ownership recursively!"
        ;;
    *sudo\ rm*)
        echo "⚠️  ⚠️  ⚠️  SUDO DELETE COMMAND  ⚠️  ⚠️  ⚠️"
        echo ""
        echo "This uses ROOT privileges to DELETE files!"
        ;;
    *)
        echo "📋 Command analysis:"
        echo "  Type: Standard operation"
        echo "  Risk level: Low to Medium"
        ;;
esac

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "                    🛡️  SAFETY SUMMARY 🛡️"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "To actually execute this command:"
echo "  1. Make sure you understand what it does"
echo "  2. Backup important files first"
echo "  3. Type 'yes' to confirm you want to proceed:"
echo ""

read -p "Execute command? (yes/no): " confirm

if [ "$confirm" = "yes" ]; then
    echo ""
    echo "⚠️  Executing: $COMMAND"
    eval "$COMMAND"
else
    echo ""
    echo "✅ Command cancelled - no changes made"
fi