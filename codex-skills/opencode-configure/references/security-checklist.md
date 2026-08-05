# OpenCode Security Checklist

## Before Sharing or Committing Configs

- [ ] No plain-text passwords
- [ ] No API keys or tokens
- [ ] No authentication credentials
- [ ] No private keys
- [ ] No database connection strings with credentials
- [ ] No hardcoded secrets in comments

## File Permissions

| File Type | Recommended Permission |
|-----------|----------------------|
| Config files | 600 (owner read/write only) |
| Skills directory | 755 (read/execute) |
| Scripts | 700 (owner execute) |
| Memory files | 600 |

## Safe Configuration Patterns

### Environment Variables (Recommended)
```json
{
  "provider": {
    "api_key": "${OPENCODE_API_KEY}"
  }
}
```

### External Secrets File
```json
{
  "secrets": "./secrets.json"
}
```

### .gitignore for Secrets
```
opencode.json
opencode.jsonc
.secrets/
*.key
```

## Audit Commands

```bash
# Run security audit
~/.agents/skills/opencode-configure/scripts/audit_secrets.sh

# Check permissions
ls -la opencode.json ~/.config/opencode/

# Verify no secrets in git
git diff --cached --word-diff | grep -i secret
```

## If You Find Exposed Secrets

1. **Immediately** rotate the exposed credentials
2. **Remove** the secret from config
3. **Update** to use environment variables
4. **Check** if already compromised
5. **Audit** other configs for same issue