# OpenCode Configuration Explanations

## Complete Config Breakdown

### $schema
**What:** JSON schema validation
**Why:** Ensures config follows correct format
**Example:** `"$schema": "https://opencode.ai/config.json"`

---

### agents.enabled
**What:** List of AI agents to enable
**Why:** Different agents excel at different tasks

| Agent | Best For |
|-------|----------|
| `general` | Default tasks, general assistance |
| `explore` | Finding files, understanding codebases |
| `code-reviewer` | Reviewing code, finding issues |
| `researcher` | Documentation, research tasks |

**Example:**
```json
{
  "agents": {
    "enabled": ["explore", "code-reviewer"],
    "default": "general"
  }
}
```

---

### tools.enabled
**What:** Which tools the AI can use
**Why:** Control capabilities and security

| Tool | Purpose |
|------|---------|
| `read` | Read files |
| `write` | Create files |
| `edit` | Modify files |
| `glob` | Find files by pattern |
| `grep` | Search file contents |
| `bash` | Run shell commands |
| `task` | Use subagents |
| `websearch` | Search the web |
| `webfetch` | Get web page content |

**Example:**
```json
{
  "tools": {
    "enabled": ["read", "write", "edit", "glob", "grep", "bash"]
  }
}
```

---

### permissions.skills
**What:** Enable/disable specific skills
**Why:** Add specialized capabilities

| Skill | Purpose |
|-------|---------|
| `opencode-configure` | Configure OpenCode settings |
| `terminal-helper` | Terminal operations & help |
| Custom skills | Your own created skills |

**Example:**
```json
{
  "permissions": {
    "skills": {
      "opencode-configure": true,
      "terminal-helper": true
    }
  }
}
```

---

### permissions.tools.bash.allowed_commands
**What:** Whitelist of allowed shell commands
**Why:** Security - prevent dangerous commands

**Example:**
```json
{
  "permissions": {
    "tools": {
      "bash": {
        "allowed_commands": ["ls", "cat", "git status", "git diff"]
      }
    }
  }
}
```

---

### theme
**What:** UI appearance
**Why:** Personalize your workspace

**Options:** "default", "dark", "light", custom themes

---

### keybinds
**What:** Custom keyboard shortcuts
**Why:** Faster workflow

**Example:**
```json
{
  "keybinds": {
    "ctrl+p": "quick-pick",
    "ctrl+shift+c": "copy-output"
  }
}
```

---

### provider
**What:** AI model configuration
**Why:** Choose your preferred AI

**Example:**
```json
{
  "provider": {
    "type": "anthropic",
    "model": "claude-sonnet-4-20250514"
  }
}
```

---

## Minimal Config

```json
{
  "$schema": "https://opencode.ai/config.json",
  "agents": {
    "enabled": [],
    "default": "general"
  },
  "tools": {
    "enabled": ["read", "write", "edit", "glob", "grep", "bash"]
  }
}
```

## Full Config

See `opencode-config-schema.json` for complete example with all options.