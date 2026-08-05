#!/bin/bash

# Environment setup for terminal-helper

echo "═══════════════════════════════════════════════════════"
echo "           🖥️  ENVIRONMENT SETUP 🖥️"
echo "═══════════════════════════════════════════════════════"
echo ""

# Detect OS
if [[ "$OSTYPE" == "darwin"* ]]; then
    OS="macOS"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS="Linux"
else
    OS="Unknown"
fi

echo "📍 Detected OS: $OS"
echo "📍 Shell: $SHELL"
echo ""

# Create directories
echo "📁 Creating directories..."
DIRS=(
    "$HOME/.terminal-helper-backups"
    "$HOME/.config/opencode/backups"
    "$HOME/logs"
)

for dir in "${DIRS[@]}"; do
    mkdir -p "$dir" 2>/dev/null
    if [ -d "$dir" ]; then
        echo "   ✅ $dir"
    else
        echo "   ❌ $dir (failed)"
    fi
done

# Setup aliases
echo ""
echo "📝 Setting up aliases..."
SHELL_RC=~/.zshrc
[ -f ~/.bashrc ] && [ -z "$ZSH_VERSION" ] && SHELL_RC=~/.bashrc

# Check if aliases already exist
if grep -q "terminal-helper" "$SHELL_RC" 2>/dev/null; then
    echo "   ⚠️  Aliases already exist in $SHELL_RC"
else
    cat >> "$SHELL_RC" << 'EOF'

# Terminal helper aliases
alias th-backup='~/.agents/skills/terminal-helper/scripts/backup_files.sh'
alias th-sysinfo='~/.agents/skills/terminal-helper/scripts/system_info.sh'
alias th-security='~/.agents/skills/terminal-helper/scripts/security_audit.sh'
alias th-dryrun='~/.agents/skills/terminal-helper/scripts/dry_run.sh'
alias th-explain='~/.agents/skills/terminal-helper/scripts/explain_command.sh'
alias th-logs='~/.agents/skills/opencode-configure/scripts/debug_logs.sh'
alias th-check='~/.agents/skills/opencode-configure/scripts/check_config.sh'
EOF
    echo "   ✅ Aliases added to $SHELL_RC"
fi

# Check for required tools
echo ""
echo "🔧 Checking required tools..."
TOOLS=("bash" "grep" "sed" "awk" "tar")
for tool in "${TOOLS[@]}"; do
    if command -v "$tool" >/dev/null 2>&1; then
        echo "   ✅ $tool"
    else
        echo "   ❌ $tool (missing)"
    fi
done

# Optional tools
echo ""
echo "🔧 Optional tools:"
OPTIONAL=("python3" "node" "docker" "git")
for tool in "${OPTIONAL[@]}"; do
    if command -v "$tool" >/dev/null 2>&1; then
        echo "   ✅ $tool"
    else
        echo "   ⚠️  $tool (not installed)"
    fi
done

# Update shell
echo ""
echo "📜 Reloading shell..."
source "$SHELL_RC" 2>/dev/null

echo ""
echo "═══════════════════════════════════════════════════════"
echo "              ✅ SETUP COMPLETE ✅"
echo "═══════════════════════════════════════════════════════"
echo ""
echo "To use terminal-helper aliases, run:"
echo "   source $SHELL_RC"
echo ""
echo "Available shortcuts:"
echo "   th-backup    - Backup files"
echo "   th-sysinfo   - System info"
echo "   th-security  - Security audit"
echo "   th-dryrun    - Preview commands"
echo "   th-explain   - Explain commands"
echo "   th-logs      - Debug logs"
echo "   th-check     - Config check"
echo ""
echo "📚 Reference files:"
echo "   ~/.agents/skills/terminal-helper/references/"
echo ""
echo "📝 Log commands to MEMORY.md:"
echo "   ~/.agents/skills/terminal-helper/scripts/track_commands.sh"