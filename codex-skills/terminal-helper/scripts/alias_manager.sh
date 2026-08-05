#!/bin/bash

# Alias manager for terminal-helper

ACTION=${1:-list}

case "$ACTION" in
    list)
        echo "═══════════════════════════════════════════════════════"
        echo "                    📝 ALIAS LIST 📝"
        echo "═══════════════════════════════════════════════════════"
        echo ""
        
        if [ -f ~/.bashrc ]; then
            echo "📄 ~/.bashrc aliases:"
            grep "^alias " ~/.bashrc 2>/dev/null | sed 's/^/   /'
        fi
        
        if [ -f ~/.zshrc ]; then
            echo ""
            echo "📄 ~/.zshrc aliases:"
            grep "^alias " ~/.zshrc 2>/dev/null | sed 's/^/   /'
        fi
        
        echo ""
        echo "📄 Built-in helper aliases:"
        echo "   th-backup      - Backup files before changes"
        echo "   th-sysinfo     - System information"
        echo "   th-security    - Run security audit"
        echo "   th-dryrun      - Preview dangerous commands"
        echo "   th-explain     - Explain a command"
        ;;
    add)
        ALIAS_NAME=$2
        ALIAS_CMD=$3
        
        if [ -z "$ALIAS_NAME" ] || [ -z "$ALIAS_CMD" ]; then
            echo "Usage: alias_manager.sh add <alias-name> <command>"
            echo "Example: alias_manager.sh add ll 'ls -la'"
            exit 1
        fi
        
        SHELL_RC=~/.zshrc
        if [ -f ~/.bashrc ] && [ -z "$ZSH_VERSION" ]; then
            SHELL_RC=~/.bashrc
        fi
        
        echo "alias $ALIAS_NAME='$ALIAS_CMD'" >> "$SHELL_RC"
        echo "✅ Added alias: $ALIAS_NAME='$ALIAS_CMD'"
        echo "   To use: source ~/$SHELL_RC"
        ;;
    remove)
        ALIAS_NAME=$2
        
        if [ -z "$ALIAS_NAME" ]; then
            echo "Usage: alias_manager.sh remove <alias-name>"
            exit 1
        fi
        
        for rc in ~/.bashrc ~/.zshrc; do
            if [ -f "$rc" ]; then
                sed -i.bak "/^alias $ALIAS_NAME=/d" "$rc"
                echo "✅ Removed alias from $rc"
            fi
        done
        ;;
    create)
        echo "═══════════════════════════════════════════════════════"
        echo "              📝 CREATE HELPER ALIASES 📝"
        echo "═══════════════════════════════════════════════════════"
        echo ""
        
        SCRIPT_DIR="$HOME/.agents/skills/terminal-helper/scripts"
        
        SHELL_RC=~/.zshrc
        [ -f ~/.bashrc ] && [ -z "$ZSH_VERSION" ] && SHELL_RC=~/.bashrc
        
        # Add helper aliases
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
        
        echo "✅ Created terminal-helper aliases!"
        echo ""
        echo "Available aliases:"
        echo "   th-backup    - Backup files"
        echo "   th-sysinfo   - System info"
        echo "   th-security  - Security audit"
        echo "   th-dryrun    - Preview commands"
        echo "   th-explain   - Explain commands"
        echo "   th-logs      - Debug logs"
        echo "   th-check     - Config check"
        echo ""
        echo "Run: source $SHELL_RC"
        ;;
    *)
        echo "Usage: $0 <action>"
        echo ""
        echo "Actions:"
        echo "  list              - Show all aliases"
        echo "  add <name> <cmd>  - Add new alias"
        echo "  remove <name>    - Remove alias"
        echo "  create            - Create helper aliases"
        ;;
esac