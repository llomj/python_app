#!/bin/bash

echo "=== OpenCode Configuration Checker ==="
echo ""

check_file() {
    local file=$1
    if [ -f "$file" ]; then
        echo "✓ Found: $file"
        if [[ "$file" == *.json ]]; then
            if python3 -m json.tool "$file" > /dev/null 2>&1; then
                echo "  ✓ Valid JSON"
            else
                echo "  ✗ Invalid JSON"
            fi
        elif [[ "$file" == *.jsonc ]]; then
            if node -e "JSON.parse(require('fs').readFileSync('$file', 'utf8'))" > /dev/null 2>&1; then
                echo "  ✓ Valid JSONC"
            else
                echo "  ✗ Invalid JSONC (may contain comments)"
            fi
        fi
    else
        echo "✗ Not found: $file"
    fi
}

echo "Checking configurations..."
check_file "opencode.json"
check_file "opencode.jsonc"
check_file "$HOME/.config/opencode/opencode.json"
check_file "$HOME/.config/opencode/opencode.jsonc"

echo ""
echo "=== Available Skills ==="
if [ -d "$HOME/.agents/skills" ]; then
    ls -1 "$HOME/.agents/skills/" 2>/dev/null | while read skill; do
        echo "  - $skill"
    done
fi

echo ""
echo "=== Agent Files ==="
if [ -f "AGENTS.md" ]; then
    echo "  ✓ AGENTS.md exists"
else
    echo "  ✗ AGENTS.md not found"
fi

echo ""
echo "=== Memory ==="
if [ -f "MEMORY.md" ]; then
    echo "  ✓ MEMORY.md exists"
else
    echo "  ✗ MEMORY.md not found"
fi