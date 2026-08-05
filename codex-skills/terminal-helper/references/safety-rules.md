# Safety Rules for Terminal Operations

## Critical Warnings

### NEVER execute without approval:
1. **Delete commands** (`rm -rf`, `del`, etc.)
2. **Format commands** (`mkfs`, `format`)
3. **Disk write commands** (`dd` to device)
4. **System shutdown/restart** (unless critical)
5. **Permission changes** on system directories

### ALWAYS warn about:
- `rm -rf *` - Deletes all files in directory
- `rm -rf /` - DELETES EVERYTHING ON SYSTEM
- `chmod -R 777` - Makes everything writable
- `dd if=/dev/zero of=/dev/sda` - WIPES DRIVE
- `chown -R` - Changes ownership recursively

## Before Any Command

1. **Explain what it does**
2. **Show what will be affected**
3. **Wait for explicit approval**
4. **Backup if destructive**

## Safe Alternatives

Instead of `rm -rf *`, use:
```bash
# Show what would be deleted first
ls -la
# Then delete specific files with confirmation
rm -ri *.txt
```

Instead of `chmod -R 777`, use:
```bash
# Check current permissions
ls -la
# Set specific needed permissions
chmod 755 directory
```

## Approval Keywords

User MUST explicitly type one of:
- "yes" - Approve the operation
- "delete" - Confirm deletion
- "proceed" - Continue with command
- "do it" - Execute dangerous command

## When Unsure

1. Ask for clarification
2. Suggest safer alternative
3. Offer to explain more
4. Suggest backup first

## Logging

Always log dangerous commands in MEMORY.md:
| Date | Command | Reason | Approved |
|------|---------|--------|----------|
| 2025-05-15 | rm -rf old/ | Remove old files | yes |