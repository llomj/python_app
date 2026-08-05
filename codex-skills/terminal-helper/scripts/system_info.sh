#!/bin/bash

echo "=== System Information ==="
echo ""

echo "=== Basic Info ==="
echo "Hostname: $(hostname)"
echo "Kernel: $(uname -r)"
echo "OS: $(uname -s)"
echo "Architecture: $(uname -m)"
echo "Uptime: $(uptime -p 2>/dev/null || uptime)"

echo ""
echo "=== CPU ==="
if command -v sysctl >/dev/null 2>&1; then
    sysctl -n machdep.cpu.brand_string 2>/dev/null || sysctl -n hw.model
else
    cat /proc/cpuinfo | grep "model name" | head -1 | cut -d: -f2
fi
echo "Cores: $(nproc 2>/dev/null || sysctl -n hw.ncpu 2>/dev/null)"

echo ""
echo "=== Memory ==="
if command -v free >/dev/null 2>&1; then
    free -h
else
    vm_stat | head -10
fi

echo ""
echo "=== Disk Usage ==="
df -h | grep -v "tmpfs\|devtmpfs\|snap"

echo ""
echo "=== Top Processes ==="
if command -v top >/dev/null 2>&1; then
    ps aux --sort=-%cpu | head -6
else
    ps -eo pcpu,pid,comm | head -6
fi

echo ""
echo "=== Network ==="
echo "IP Addresses:"
if command -v ip >/dev/null 2>&1; then
    ip addr show | grep "inet " | awk '{print "  " $2}'
elif command -v ifconfig >/dev/null 2>&1; then
    ifconfig | grep "inet " | awk '{print "  " $2}'
fi

echo ""
echo "=== Current User ==="
echo "User: $(whoami)"
echo "Groups: $(groups)"
echo "Home: $HOME"

echo ""
echo "=== Recent Logs (errors) ==="
if [ -d "/var/log" ]; then
    sudo tail -5 /var/log/syslog 2>/dev/null || tail -5 /var/log/messages 2>/dev/null || echo "No log access"
fi