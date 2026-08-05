# OpenCode Troubleshooting Guide

## Fast Diagnostic Order

Run these in order:

```bash
which opencode
opencode --version
opencode auth list
sed -n '1,160p' ~/.config/opencode/opencode.jsonc
```

For this machine, the expected healthy state is:

- `which opencode` => `/Users/moll/.npm-global/bin/opencode`
- `opencode --version` => `1.15.13` or newer
- `opencode auth list` => shows `OpenCode Go`
- default model config => `opencode-go/kimi-k2.6`

## Known Working Paths

- CLI: `/Users/moll/.npm-global/bin/opencode`
- Config: `/Users/moll/.config/opencode/opencode.jsonc`
- Auth: `/Users/moll/.local/share/opencode/auth.json`
- Vault for Obsidian work: `/Users/moll/Library/Mobile Documents/iCloud~md~obsidian/Documents/AI brain`

## Common Failures

### Wrong CLI Version

Symptoms:
- terminal behavior differs from the app
- commands/features missing

Cause:
- shell resolves `/opt/homebrew/bin/opencode` instead of npm-global install

Fix:
- check `which opencode`
- fix PATH order so `~/.npm-global/bin` comes before Homebrew
- open a fresh login shell and recheck version

### `Incorrect API key provided: sk-or-v1...`

Symptoms:
- OpenCode reports an OpenAI auth failure
- saved key starts with `sk-or-v1`

Cause:
- an OpenRouter key was saved under the `OpenAI` provider slot

Fix:
1. Back up `~/.local/share/opencode/auth.json`
2. Remove the bad `OpenAI` credential entry only
3. Keep `OpenCode Go`
4. Re-test:

```bash
opencode auth list
opencode models opencode-go
opencode run "Reply with exactly: OK"
```

### OpenCode App Works But Terminal Does Not

Cause:
- desktop app and terminal CLI are using different installs or provider state

Fix:
- compare app version and terminal CLI version
- align terminal CLI first
- recheck auth/config after version alignment

### OpenCode Uses the Wrong Vault

Cause:
- task launched from the wrong folder
- stale instructions still mention the old CloudDocs path

Fix:
- use only:
  `/Users/moll/Library/Mobile Documents/iCloud~md~obsidian/Documents/AI brain`
- never use:
  `/Users/moll/Library/Mobile Documents/com~apple~CloudDocs/Obsidian/AI brain`

## Minimal Verification

```bash
opencode models opencode-go
opencode run "Reply with exactly: DEFAULT_GO_OK"
```

If that works, OpenCode is basically healthy again.
