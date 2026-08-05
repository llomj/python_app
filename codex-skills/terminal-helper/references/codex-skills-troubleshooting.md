# Codex Skills Troubleshooting Guide

## Problem: Personal Skills Not Visible in UI

### Symptoms
- Skill folder exists in ~/.codex/skills/ with SKILL.md
- agents/openai.yaml created with interface fields  
- Skill still doesn't show in Codex personal skills list

### Debugging Steps
1. Verify folder structure:
   ```bash
   ls -la ~/.codex/skills/[skill-name]/
   ```

2. Check SKILL.md has valid YAML frontmatter:
   ```yaml
   ---
   name: skill-name
   description: |
     Use when user needs help with [topic].
   ---
   ```

3. Clear Codex cache:
   ```bash
   rm -rf ~/.codex/cache/codex_app_directory/*.json
   ```

4. Restart Codex completely (quit and reopen)

5. Force trigger by typing the skill name in conversation

### Root Cause
Codex caches skill list. New skills may not appear until cache rebuilds.

### Workaround
Skills still work via keyword triggering even if not visible in UI list.

---

## Creating New Skills Checklist

- [ ] Create folder: ~/.codex/skills/[skill-name]/
- [ ] Add SKILL.md with YAML frontmatter (name, description)
- [ ] Add agents/openai.yaml for UI visibility:
  ```yaml
  interface:
    display_name: "Skill Name"
    short_description: "What it does"
    default_prompt: "Example trigger"
  ```
- [ ] Clear cache: rm -rf ~/.codex/cache/codex_app_directory/*.json
- [ ] Restart Codex
- [ ] Test by typing skill trigger in conversation

---

## Tested Skills (Working in UI)
- terminal-helper ✓
- obsidian-helper ✓
- government-tax-manager ✓
- opencode-configure ✓
- hatch-pet ✓
- pdf ✓
- skill-organizer ✓

## Not Working (Visible in UI)
- github (works via trigger, not visible in list)