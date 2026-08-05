#!/bin/zsh
set -euo pipefail

VAULT_BASE="/Users/moll/Library/Mobile Documents/iCloud~md~obsidian/Documents/AI brain"
CODEX_SKILL="/Users/moll/.codex/skills/obsidian-helper"
AGENTS_SKILL="/Users/moll/.agents/skills/obsidian-helper"

mkdir -p "$VAULT_BASE"

# Ensure key policy files exist in vault
for f in AGENTS.md USER.md ps.md; do
  touch "$VAULT_BASE/$f"
done

# Mirror recovery/open scripts across codex + agents skills
if [[ -f "$CODEX_SKILL/scripts/obsidian_recover_open.sh" ]]; then
  cp "$CODEX_SKILL/scripts/obsidian_recover_open.sh" "$AGENTS_SKILL/scripts/obsidian_recover_open.sh"
fi

echo "Synced agent contract targets:"
echo "- $VAULT_BASE/AGENTS.md"
echo "- $VAULT_BASE/USER.md"
echo "- $VAULT_BASE/ps.md"
echo "- $AGENTS_SKILL/scripts/obsidian_recover_open.sh"
