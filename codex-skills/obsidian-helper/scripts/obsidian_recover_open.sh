#!/bin/zsh
set -euo pipefail

VAULT_PATH="/Users/moll/Library/Mobile Documents/iCloud~md~obsidian/Documents/AI brain"
APP_SUPPORT="$HOME/Library/Application Support/obsidian"
SAFE_MODE="${1:-}"

if [[ ! -d "$VAULT_PATH" ]]; then
  echo "ERROR: Vault path not found: $VAULT_PATH" >&2
  exit 1
fi

# Repair known startup blockers before relaunching Obsidian.
HEALTH_GUARD="$HOME/.local/bin/obsidian_health_guard.sh"
if [[ -x "$HEALTH_GUARD" ]]; then
  "$HEALTH_GUARD"
fi

# Stop Obsidian completely
osascript -e 'tell application "Obsidian" to quit' >/dev/null 2>&1 || true
sleep 1
pkill -f "/Applications/Obsidian.app/Contents/MacOS/Obsidian" >/dev/null 2>&1 || true
pkill -f "Obsidian Helper" >/dev/null 2>&1 || true
sleep 1

mkdir -p "$APP_SUPPORT"

# Force Obsidian to point to canonical iCloud vault
cat > "$APP_SUPPORT/obsidian.json" << JSON
{"vaults":{"aibrain":{"path":"$VAULT_PATH","ts":$(date +%s),"open":true}}}
JSON

# Keep GPU acceleration off in vault config (prevents blank renderer loops)
mkdir -p "$VAULT_PATH/.obsidian"
cat > "$VAULT_PATH/.obsidian/app.json" << 'JSON'
{
  "hardwareAcceleration": false,
  "alwaysUpdateLinks": true
}
JSON

# Repair truncated core-plugin state before Obsidian tries to parse it.
CORE_PLUGINS="$VAULT_PATH/.obsidian/core-plugins.json"
if [[ ! -s "$CORE_PLUGINS" ]] || ! node -e 'JSON.parse(require("fs").readFileSync(process.argv[1], "utf8"))' "$CORE_PLUGINS" >/dev/null 2>&1; then
  [[ -e "$CORE_PLUGINS" ]] && cp "$CORE_PLUGINS" "$CORE_PLUGINS.bak.recovery-$(date +%Y%m%d-%H%M%S)"
  cat > "$CORE_PLUGINS" << 'JSON'
{
  "file-explorer": true,
  "global-search": true,
  "switcher": true,
  "graph": true,
  "backlink": true,
  "canvas": true,
  "outgoing-link": true,
  "tag-pane": true,
  "properties": true,
  "page-preview": true,
  "daily-notes": true,
  "templates": true,
  "note-composer": true,
  "command-palette": true,
  "slash-command": true,
  "editor-status": true,
  "bookmarks": true,
  "outline": true,
  "word-count": true,
  "file-recovery": true,
  "workspaces": false,
  "publish": false,
  "sync": false
}
JSON
fi

# Optional safe mode: disable community plugins and reset workspace state
if [[ "$SAFE_MODE" == "--safe" ]]; then
  cat > "$VAULT_PATH/.obsidian/community-plugins.json" << 'JSON'
[]
JSON
  cat > "$VAULT_PATH/.obsidian/workspace.json" << 'JSON'
{
  "main": {
    "id": "main",
    "type": "split",
    "children": [{"id": "tabs", "type": "tabs", "children": [{"id": "leaf", "type": "leaf", "state": {"type": "empty", "state": {}, "title": "New tab"}}]}],
    "direction": "vertical"
  },
  "left": {
    "id": "left",
    "type": "split",
    "children": [{"id": "left-tabs", "type": "tabs", "children": [{"id": "files", "type": "leaf", "state": {"type": "file-explorer", "state": {}}}], "currentTab": 0}],
    "direction": "horizontal",
    "width": 300
  },
  "right": {"id": "right", "type": "split", "children": [], "direction": "horizontal", "width": 300},
  "active": "leaf",
  "lastOpenFiles": []
}
JSON
fi

# Launch with GPU disabled at process level too
open -a Obsidian --args --disable-gpu
sleep 2

if pgrep -fl "Obsidian" >/dev/null 2>&1; then
  echo "Obsidian launched (vault: $VAULT_PATH)"
  [[ "$SAFE_MODE" == "--safe" ]] && echo "Mode: SAFE (plugins disabled)" || echo "Mode: NORMAL"
else
  echo "ERROR: Obsidian did not launch" >&2
  exit 1
fi
