# Script Templates

## Bash Script Template

```bash
#!/bin/bash
# Script: script-name.sh
# Description: What this script does
# Author: Your Name
# Date: $(date +%Y-%m-%d)

set -euo pipefail

# Variables
VAR_NAME="value"

# Functions
function main() {
    echo "Starting script..."
    # Your code here
}

function helper() {
    # Helper function
    echo "Helper function"
}

# Main execution
main "$@"
```

## PowerShell Script Template

```powershell
<#
.SYNOPSIS
    Script description
.DESCRIPTION
    Detailed description
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory=$false)]
    [string]$Name = "default"
)

# Variables
$ErrorActionPreference = "Stop"

# Functions
function Main {
    Write-Host "Starting script..."
    # Your code here
}

function Helper-Function {
    param([string]$Input)
    Write-Output "Helper: $Input"
}

# Execution
Main
```

## Backup Script Template

```bash
#!/bin/bash
# Backup script template
# Usage: ./backup.sh <source> <destination>

set -euo pipefail

SOURCE=$1
DESTINATION=$2
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

echo "📦 Starting backup..."
echo "  Source: $SOURCE"
echo "  Destination: $DESTINATION"

if [ ! -d "$SOURCE" ]; then
    echo "❌ Error: Source directory does not exist"
    exit 1
fi

mkdir -p "$DESTINATION"

backup_name=$(basename "$SOURCE")_$TIMESTAMP.tar.gz
tar -czf "$DESTINATION/$backup_name" "$SOURCE"

echo "✅ Backup complete: $backup_name"
echo "📁 Size: $(du -h "$DESTINATION/$backup_name" | cut -f1)"
```

## Cron Job Script Template

```bash
#!/bin/bash
# Cron job script
# Set as: crontab -e
# Example: 0 * * * * /path/to/script.sh

LOG_FILE="/var/log/script.log"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

log "Script started"

# Your cron job logic here

log "Script completed successfully"
```

## Docker Cleanup Script

```bash
#!/bin/bash
# Docker cleanup script
# ⚠️ WARNING: This removes containers and images!

echo "🐳 Docker Cleanup Script"
echo "========================"

# Show current usage
echo "Current usage:"
docker system df

read -p "Remove stopped containers? (yes/no): " confirm
if [ "$confirm" = "yes" ]; then
    docker container prune -f
    echo "✅ Removed stopped containers"
fi

read -p "Remove unused images? (yes/no): " confirm
if [ "$confirm" = "yes" ]; then
    docker image prune -a -f
    echo "✅ Removed unused images"
fi

read -p "Remove unused volumes? (yes/no): " confirm
if [ "$confirm" = "yes" ]; then
    docker volume prune -f
    echo "✅ Removed unused volumes"
fi

echo "📊 After cleanup:"
docker system df
```

## System Health Check Script

```bash
#!/bin/bash
# System health check

echo "╔═══════════════════════════════════════════════╗"
echo "║         SYSTEM HEALTH CHECK                 ║"
echo "╚═══════════════════════════════════════════════╝"
echo ""

# CPU
echo "📊 CPU Usage:"
top -bn1 | grep "Cpu(s)" | awk '{print "  Usage: " $2}'

# Memory
echo "📊 Memory Usage:"
free -h | awk '/^Mem:/ {print "  Used: " $3 " / " $2}'

# Disk
echo "📊 Disk Usage:"
df -h | awk '/\/$/ {print "  Used: " $3 " / " $2 " (" $5 ")"}'

# Top processes
echo "📊 Top 5 Processes:"
ps aux --sort=-%cpu | head -6 | tail -5 | awk '{print "  " $11 " - " $3"%"}'

echo ""
echo "✅ Health check complete"
```

## Interactive Menu Script

```bash
#!/bin/bash
# Interactive menu

while true; do
    echo "╔═══════════════════╗"
    echo "║   SELECT OPTION   ║"
    echo "╠═══════════════════╣"
    echo "║ 1. Option One     ║"
    echo "║ 2. Option Two    ║"
    echo "║ 3. Option Three  ║"
    echo "║ 4. Exit           ║"
    echo "╚═══════════════════╝"
    
    read -p "Enter choice: " choice
    
    case $choice in
        1) echo "You chose Option 1" ;;
        2) echo "You chose Option 2" ;;
        3) echo "You chose Option 3" ;;
        4) echo "Goodbye!"; break ;;
        *) echo "Invalid option" ;;
    esac
    echo ""
done
```

## Error Handling Template

```bash
#!/bin/bash
# Script with error handling

set -euo pipefail

trap 'error_handler $? $LINENO' ERR

error_handler() {
    echo "❌ Error occurred at line $2 with exit code $1"
    # Cleanup if needed
    exit 1
}

function risky_operation() {
    # Your potentially failing operation
    false || return $?
}

# Main
main() {
    risky_operation
    echo "✅ Success"
}

main "$@"
```