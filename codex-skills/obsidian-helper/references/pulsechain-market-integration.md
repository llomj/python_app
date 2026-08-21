# PulseChain Market Analyst integration

## Skill link

- Display name: PulseChain Market Analyst
- Invocation: `$analyze-pulsechain-markets`
- Codex path: `/Users/moll/.codex/skills/analyze-pulsechain-markets`
- Canonical iCloud path: `/Users/moll/Library/Mobile Documents/com~apple~CloudDocs/AI/Pulsechain/analyze-pulsechain-markets`

Use the market skill for live collection and quantitative analysis. Use Obsidian Helper to find prior research, synthesize multiple dated observations, and publish human-readable knowledge notes.

## Routing rules

- Treat unqualified `HEX` as HEX on PulseChain.
- Treat `HEX on Ethereum`, `Ethereum HEX`, or `eHEX` as HEX on Ethereum.
- Refresh live data before answering current-market questions.
- Preserve the UTC observation time, source health, and coverage limitations.
- Never present a stored Obsidian note as live market data.
- Never store wallet addresses, seed phrases, private keys, authentication secrets, or browser-local wallet data in the vault.

## Vault publication

Write only when the user explicitly asks to save, remember, publish, or update research.

- Put dated market reports in `wiki/sources/`.
- Put durable token definitions, terminology, and methodologies in `wiki/concepts/`.
- Link related pages with Obsidian wikilinks.
- Follow the vault frontmatter format.
- Update `index.md` and append the action to `log.md`.
- Cite the skill snapshot path and external market sources used.
- Never modify `raw/`.

Keep machine snapshots in the PulseChain skill. Store concise conclusions and source links in Obsidian rather than duplicating complete JSON snapshots.
