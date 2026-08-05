#!/bin/bash

echo "=== OpenCode Debug & Log Analysis ==="
echo ""

LOG_DIRS=(
    "$HOME/Library/Logs/opencode"
    "$HOME/.config/opencode/logs"
    "$HOME/.codex/logs"
)

echo "=== Recent Log Files ==="
for dir in "${LOG_DIRS[@]}"; do
    if [ -d "$dir" ]; then
        echo "Directory: $dir"
        find "$dir" -type f -name "*.log" -mtime -7 2>/dev/null | head -5 | while read log; do
            echo "  - $(basename "$log") ($(wc -l < "$log") lines)"
        done
    fi
done

echo ""
echo "=== Recent Errors (last 48 hours) ==="
for dir in "${LOG_DIRS[@]}"; do
    if [ -d "$dir" ]; then
        find "$dir" -type f -name "*.log" -mtime -2 2>/dev/null | xargs grep -i -E "(error|fatal|exception|crash)" 2>/dev/null | tail -10
    fi
done

echo ""
echo "=== Configuration Status ==="
~/.agents/skills/opencode-configure/scripts/check_config.sh

echo ""
echo "=== Tool Diagnostics ==="
echo "Checking enabled tools..."
for tool in read write edit glob grep bash task websearch webfetch; do
    if command -v "$tool" >/dev/null 2>&1; then
        echo "  ✓ $tool available"
    else
        echo "  ✗ $tool not found"
    fi
done

echo ""
echo "=== Suggestions ==="
echo "1. Check MEMORY.md for past issues"
echo "2. Review AGENTS.md for agent behavior"
echo "3. Try: kill -HUP \$(pgrep opencode) to restart"
echo "4. Check ~/.codex/ for Codex-specific logs"