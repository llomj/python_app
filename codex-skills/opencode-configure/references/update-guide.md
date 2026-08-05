# OpenCode Update Guide

## Repair Target

For this environment, aim for:

- CLI path: `/Users/moll/.npm-global/bin/opencode`
- CLI version: `1.15.13` or newer
- provider: `OpenCode Go`
- config file:

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "model": "opencode-go/kimi-k2.6",
  "small_model": "opencode-go/deepseek-v4-flash",
  "autoupdate": true
}
```

## Before Updating

1. Back up:
   - `~/.local/share/opencode/auth.json`
   - `~/.config/opencode/opencode.jsonc`
2. Check current binary:

```bash
which opencode
opencode --version
```

3. Check current providers:

```bash
opencode auth list
```

## Preferred Update Flow

Use the install source that matches the working CLI.

For this machine, the active good CLI is npm-global:

```bash
npm install -g opencode@latest
```

Then re-open a fresh login shell and verify:

```bash
which opencode
opencode --version
```

If Homebrew still wins path resolution, fix PATH order instead of assuming the update failed.

## Post-Update Verification

```bash
opencode auth list
opencode models opencode-go
opencode run "Reply with exactly: OK"
```

## Do Not Do This

- Do not store an OpenRouter key under `OpenAI`
- Do not assume desktop app version means terminal CLI is current
- Do not point OpenCode at the old CloudDocs vault path
- Do not add duplicate auth entries without understanding which provider they belong to
