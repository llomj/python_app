#!/bin/bash

echo "=== OpenCode Security Audit ==="
echo ""

AUDIT_PASSED=true

check_secrets() {
    local file=$1
    if [ -f "$file" ]; then
        echo "Checking: $file"
        
        if grep -i -E "(password|secret|api_key|token|key|credential|auth)" "$file" 2>/dev/null | grep -v "^\s*//" | grep -v "^\s*#" | grep -v "\${.*}" > /dev/null; then
            echo "  ⚠️  WARNING: Potential secrets found - review manually"
            AUDIT_PASSED=false
        else
            echo "  ✓ No obvious secrets"
        fi
    fi
}

echo "Scanning configuration files..."
check_secrets "$HOME/.config/opencode/opencode.json"
check_secrets "$HOME/.config/opencode/opencode.jsonc"
check_secrets "opencode.json"
check_secrets "opencode.jsonc"

echo ""
echo "Checking file permissions..."
for f in "$HOME/.config/opencode/opencode.json" "$HOME/.config/opencode/opencode.jsonc" "opencode.json" "opencode.jsonc"; do
    if [ -f "$f" ]; then
        perms=$(stat -f "%OLp" "$f" 2>/dev/null || stat -c "%a" "$f" 2>/dev/null)
        if [ "$perms" = "600" ] || [ "$perms" = "400" ] || [ "$perms" = "644" ]; then
            echo "  ✓ $f: $perms"
        else
            echo "  ⚠️  $f: $perms (recommend 600)"
        fi
    fi
done

echo ""
echo "Checking for environment variables usage..."
for f in "$HOME/.config/opencode/opencode.json" "opencode.json"; do
    if [ -f "$f" ]; then
        if grep -q '\${' "$f"; then
            echo "  ✓ $f uses environment variables"
        else
            echo "  ℹ️  $f: No environment variables detected"
        fi
    fi
done

echo ""
if [ "$AUDIT_PASSED" = true ]; then
    echo "✅ Audit passed - no obvious security issues"
else
    echo "⚠️  Review warnings above and fix any exposed secrets"
fi