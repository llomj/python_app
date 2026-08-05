#!/bin/bash

COMMAND=$1
PURPOSE=$2

if [ -z "$COMMAND" ]; then
    echo "Usage: track_commands.sh <command> <purpose>"
    echo "Logs command to MEMORY.md in terminal folder"
    exit 1
fi

MEMORY_FILE="/Users/moll/Library/Mobile Documents/com~apple~CloudDocs/AI/termimal/MEMORY.md"
TIMESTAMP=$(date +%Y-%m-%d)

if [ ! -f "$MEMORY_FILE" ]; then
    echo "Error: MEMORY.md not found at $MEMORY_FILE"
    exit 1
fi

TEMP_FILE=$(mktemp)

awk -v cmd="grep -n '## Commands Log' $MEMORY_FILE" '/## Commands Log/{getline; while($0 !~ /^##/ && $0 !~ /^$/) {print; getline}}' "$MEMORY_FILE" > /dev/null

sed -i '' "/| Date | Command | Output |/a\\
| $TIMESTAMP | $COMMAND | $PURPOSE |" "$MEMORY_FILE"

echo "Logged to MEMORY.md:"
echo "  Date: $TIMESTAMP"
echo "  Command: $COMMAND"
echo "  Purpose: $PURPOSE"

echo ""
echo "Recent entries:"
tail -5 "$MEMORY_FILE" | grep "^[0-9]"