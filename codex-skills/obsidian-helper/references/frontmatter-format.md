# Frontmatter Format

## Required Format

Every wiki page MUST have YAML frontmatter:

```yaml
---
tags: [comma, separated, tags]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [list of source filenames that informed this page]
---
```

## Example

```yaml
---
tags: [consciousness, philosophy, debate]
created: 2024-01-15
updated: 2025-05-10
sources: [20230805_TJump_Dr._Bernardo_Kastrup.md, 20231001_TJump_Consciousness_Matters.md]
---

# Consciousness

## Overview

This page synthesizes TJump's views on consciousness...

## Key Arguments

1. Materialist position
2. Epistemological skepticism
3. Comparison to Kastrup's idealism

## Related Concepts

- [[tjumps-metaphysics]]
- [[tjumps-epistemology]]

## Sources

See sources listed in frontmatter above.
```

## Field Details

### tags
- Comma-separated list
- Use lowercase, hyphens for spaces
- Include topic, category, debate type

**Examples:**
```yaml
tags: [consciousness, philosophy, materialism]
tags: [debate, theism, kalam-argument]
tags: [entities, person, opponent]
```

### created
- Date page first created
- Format: YYYY-MM-DD
- ISO 8601 format

### updated
- Date page last modified
- Update on every edit
- Format: YYYY-MM-DD

### sources
- List of raw/ filenames that informed this page
- Use exact filenames
- Comma-separated or list format

**Examples:**
```yaml
sources: [20230805_TJump_Dr._Bernardo_Kastrup.md]
sources: [source1.md, source2.md, source3.md]
```

## Common Mistakes

❌ Wrong:
```yaml
tags: "consciousness, philosophy"
created: "January 15, 2024"
sources: [source.md, Another source]
```

✅ Correct:
```yaml
tags: [consciousness, philosophy]
created: 2024-01-15
sources: [source.md]
```

## Tools Check

The lint script checks for:
- Missing frontmatter
- Incorrect date format
- Empty tags field
- Unlinked sources