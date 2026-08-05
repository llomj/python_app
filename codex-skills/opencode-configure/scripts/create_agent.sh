#!/bin/bash

AGENT_NAME=$1
AGENT_TYPE=${2:-general}

if [ -z "$AGENT_NAME" ]; then
    echo "Usage: create_agent.sh <agent-name> [type]"
    echo "Types: general, explore, code-reviewer, researcher"
    exit 1
fi

AGENT_DIR=".opencode/agents"
mkdir -p "$AGENT_DIR"

cat > "$AGENT_DIR/${AGENT_NAME}.yaml" << EOF
name: $AGENT_NAME
type: $AGENT_TYPE
description: |
  Custom agent for $AGENT_TYPE tasks

instructions: |
  - Be thorough and precise
  - Follow project conventions in AGENTS.md
  - Use MEMORY.md for context

tools:
  - read
  - write
  - edit
  - glob
  - grep
  - bash
EOF

echo "Created agent: $AGENT_DIR/${AGENT_NAME}.yaml"