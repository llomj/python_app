#!/bin/bash

echo "=== Security Audit ==="
echo ""

echo "=== File Permissions ==="
echo "Sensitive directories:"
for dir in ~/.ssh ~/.config ~/.git-credentials; do
    if [ -d "$dir" ]; then
        perms=$(stat -f "%OLp" "$dir" 2>/dev/null || stat -c "%a" "$dir" 2>/dev/null)
        echo "  $dir: $perms"
    fi
done

echo ""
echo "=== World-Writable Files ==="
find ~ -type f -perm -002 2>/dev/null | head -10

echo ""
echo "=== SUID Files (Potential Risks) ==="
find / -type f -perm /4000 2>/dev/null | head -10

echo ""
echo "=== Open Ports ==="
if command -v netstat >/dev/null 2>&1; then
    netstat -tuln 2>/dev/null | grep LISTEN | head -10
elif command -v ss >/dev/null 2>&1; then
    ss -tuln 2>/dev/null | head -10
fi

echo ""
echo "=== Running Services ==="
if command -v systemctl >/dev/null 2>&1; then
    systemctl list-units --type=service --state=running | head -10
fi

echo ""
echo "=== Recent Failed Logins ==="
if command -v lastb >/dev/null 2>&1; then
    lastb -n 5 2>/dev/null || echo "No failed login data"
fi

echo ""
echo "=== Recommendations ==="
echo "1. Review world-writable files - these can be security risks"
echo "2. Check open ports - close unnecessary services"
echo "3. Verify SSH keys are secure (600 permissions)"
echo "4. Review running services - disable unused ones"
echo "5. Check failed login attempts for suspicious activity"