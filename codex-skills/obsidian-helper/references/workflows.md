# Obsidian Workflows

## 1. Query Workflow

When user asks about a topic:

### Step 1: Search Index
```bash
# Read index.md to find relevant sections
cat index.md | grep -i "topic"
```

### Step 2: Find Relevant Wiki Pages
```bash
# List relevant concepts
ls wiki/concepts/ | grep -i "topic"

# Search wiki content
grep -r "topic" wiki/
```

### Step 3: Read Synthesized Pages
```bash
# Read the relevant wiki page
cat wiki/concepts/tjump-topic.md
```

### Step 4: Check Raw Sources (if needed)
```bash
# Find source transcripts
grep -l "topic" raw/*.md
```

### Step 5: Synthesize Answer
- Combine info from wiki pages
- Cite sources using frontmatter
- Link to related wiki pages

## 2. Ingest Workflow

When adding new transcript:

### Step 1: Read Source
```bash
# Read the new transcript
cat raw/new-video.md
```

### Step 2: Discuss with User
- Key takeaways
- Important arguments
- New concepts/entities

### Step 3: Create Source Summary
```bash
# Create wiki/sources/summary.md
cat > wiki/sources/new-video-summary.md << 'EOF'
---
tags: [topic, category]
created: 2025-01-15
updated: 2025-01-15
sources: [new-video.md]
---

# Summary Title

## Key Points

1. First point
2. Second point

## Arguments

- Pro argument
- Con argument
EOF
```

### Step 4: Update index.md
```markdown
- [[wiki/sources/new-video-summary|Summary Title]]
```

### Step 5: Update Entities/Concepts
- Add new info to relevant wiki pages
- Create new pages if needed

### Step 6: Update synthesis.md
- If worldview changed significantly

### Step 7: Append to log.md
```markdown
## [2025-01-15] ingest | Video Title
```

## 3. Lint Workflow

Periodic health check:

### Orphan Check
```bash
# Find pages with no inbound links
grep -r "[[page]]" wiki/ | grep -v "page"
```

### Frontmatter Check
```bash
# Verify all pages have frontmatter
for f in wiki/*.md wiki/*/*.md; do
    head -5 "$f" | grep -q "---" || echo "Missing: $f"
done
```

### Link Check
```bash
# Find broken wiki links
grep -r "\[\[" wiki/ | grep -v "html"
```

### Contradiction Check
- Compare similar topics across pages
- Flag conflicts for user review

## 4. Update Workflow

When content needs updating:

1. Read current wiki page
2. Read relevant raw sources
3. Discuss changes with user
4. Update page with new info
5. Update `updated` date in frontmatter
6. Append to log.md

## 5. Export Workflow

```bash
# Generate summary
./scripts/export.sh

# Export specific category
grep "## Concepts" -A 100 index.md
```