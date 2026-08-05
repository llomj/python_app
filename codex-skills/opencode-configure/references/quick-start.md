# OpenCode Configuration Quick Reference

## Common Tasks

### Enable a Skill
```json
{
  "permissions": {
    "skills": {
      "skill-name": true
    }
  }
}
```

### Add Custom Agent
```json
{
  "agents": {
    "custom": {
      "my-agent": {
        "type": "general",
        "instructions": "Custom instructions"
      }
    }
  }
}
```

### Configure Tools
```json
{
  "tools": {
    "enabled": ["read", "write", "edit", "glob", "grep", "bash"],
    "disabled": ["webfetch"]
  }
}
```

### Restrict Bash Commands
```json
{
  "permissions": {
    "tools": {
      "bash": {
        "allowed_commands": ["ls", "cat", "git status"]
      }
    }
  }
}
```

## File Locations

| Scope | Path |
|-------|------|
| Project | `./opencode.json` or `./opencode.jsonc` |
| Global | `~/.config/opencode/opencode.json` |
| Skills | `~/.agents/skills/` |
| Memory | `./MEMORY.md` |

## Useful Commands

- Check config: `~/.agents/skills/opencode-configure/scripts/check_config.sh`
- Backup config: `~/.agents/skills/opencode-configure/scripts/backup_config.sh`
- Init project: `~/.agents/skills/opencode-configure/scripts/init_project.sh`
- Create agent: `~/.agents/skills/opencode-configure/scripts/create_agent.sh <name>`