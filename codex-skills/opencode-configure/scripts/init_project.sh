#!/bin/bash

echo "=== Initialize OpenCode in Current Project ==="
echo ""

if [ -f "opencode.json" ] || [ -f "opencode.jsonc" ]; then
    echo "OpenCode config already exists!"
    echo "Run check_config.sh to verify"
    exit 0
fi

echo "Creating opencode.json..."
cat > opencode.json << 'EOF'
{
  "$schema": "https://opencode.ai/config.json",
  "agents": {
    "enabled": [],
    "default": "general"
  },
  "tools": {
    "enabled": ["read", "write", "edit", "glob", "grep", "bash"],
    "disabled": []
  },
  "permissions": {
    "skills": {
      "opencode-configure": true
    }
  },
  "keybinds": {},
  "theme": "default"
}
EOF

echo "✓ Created opencode.json"

if [ -f "AGENTS.md" ]; then
    echo "✓ AGENTS.md already exists"
else
    echo "Creating AGENTS.md..."
    cat > AGENTS.md << 'EOF'
# Project Agents

## Overview

This project uses OpenCode for terminal operations and AI-assisted tasks.

## Agent Behavior

- Follow security best practices
- Prefer safe diagnostics first
- Explain commands before execution
- Document findings in MEMORY.md

## Available Agents

- general: Default agent for general tasks
- explore: For codebase exploration
- code-reviewer: For code review tasks
- researcher: For research and documentation
EOF
    echo "✓ Created AGENTS.md"
fi

if [ -f "MEMORY.md" ]; then
    echo "✓ MEMORY.md already exists"
else
    echo "Creating MEMORY.md..."
    cat > MEMORY.md << 'EOF'
# Memory & Diagnostics History

## System Overview

| Metric | Value |
|--------|-------|
| Total RAM | |
| Used | |
| Available | |
| Swap Used | |

## Completed Tasks

| Date | Task | Command | Result |
|------|------|---------|--------|
| | | | |

## Pending Tasks

| Priority | Task | Notes |
|----------|------|-------|
| | | |

## Recommendations

### High Priority

- 

### Medium Priority

- 

### Low Priority

- 

## Commands Log

| Date | Command | Output |
|------|---------|--------|
EOF
    echo "✓ Created MEMORY.md"
fi

echo ""
echo "Project initialized with OpenCode!"