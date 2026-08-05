# AI Brain Vault Structure

## Overview

This vault follows Karpathy's LLM Wiki pattern - a content-oriented knowledge base optimized for AI interactions.

## Directory Structure

```
AI brain/
├── raw/                    # Immutable source documents
│   ├── llm-wiki.md         # Seed file (Karpathy)
│   └── *.md               # 950+ video transcripts
│
├── wiki/                   # Synthesized content (your domain)
│   ├── entities/           # People, places, organizations
│   │   ├── tjump.md       # Main entity
│   │   └── tjump-opponents.md
│   │
│   ├── concepts/          # Ideas, arguments, methodologies
│   │   ├── tjump-atheism.md
│   │   ├── tjump-consciousness.md
│   │   └── ...
│   │
│   ├── sources/           # Summaries of ingested sources
│   │   └── <filename>.md
│   │
│   └── synthesis.md       # Evolving worldview synthesis
│
├── index.md               # Content catalog (updated on ingest)
├── log.md                # Chronological activity log
├── AGENTS.md             # Vault rules & workflows
└── templates/            # Page templates
```

## File Purposes

### raw/
- **Immutable** - Never modify after adding
- Contains source transcripts (videos, articles)
- AI can read but should not edit
- References via citations, not direct linking

### wiki/
- **Mutable** - Your synthesized content
- Where AI creates/edits pages
- Follows frontmatter format
- Uses [[wiki/page]] for internal links

### index.md
- Content-oriented catalog
- Updated on every ingest
- Lists all concepts, entities, sources

### log.md
- Append-only chronological record
- Format: `## [YYYY-MM-DD] operation | Title`
- Never modify past entries

## Content Flow

```
raw/ (source) → read → synthesize → wiki/ (output)
                                      ↓
                                   index.md
                                      ↓
                                   synthesis.md
```

## Key Rules

1. **raw/ is immutable** - Read, cite, but never edit
2. **wiki/ is mutable** - Create, update, maintain
3. **Cite sources** - Link to raw/ files in frontmatter
4. **Frontmatter required** - Every wiki page needs it
5. **Cross-link** - Use [[wiki/page]] links