#!/bin/bash

# Ingest new transcript into the AI Brain vault

VAULT="/Users/moll/Library/Mobile Documents/iCloud~md~obsidian/Documents/AI brain"
SOURCE=$1

if [ -z "$SOURCE" ]; then
    echo "Usage: ingest.sh <transcript-file>"
    echo "Example: ingest.sh raw/20241001_new_debate.md"
    echo ""
    echo "This script helps process a new transcript following the workflow:"
    echo "1. Read source"
    echo "2. Create summary in wiki/sources/"
    echo "3. Update index.md"
    echo "4. Update relevant entity/concept pages"
    echo "5. Update synthesis.md if needed"
    echo "6. Append to log.md"
    exit 1
fi

# Resolve full path
if [[ "$SOURCE" != "$VAULT"* ]]; then
    SOURCE="$VAULT/$SOURCE"
fi

if [ ! -f "$SOURCE" ]; then
    echo "❌ Error: File not found: $SOURCE"
    exit 1
fi

echo "═══════════════════════════════════════════════════════════════"
echo "                    📥 INGEST WORKFLOW"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "📄 Source: $(basename "$SOURCE")"
echo ""

echo "Step 1: Reading source file..."
echo "================================"
echo ""
head -50 "$SOURCE"
echo ""
echo "... (truncated)"

echo ""
echo "Step 2: Key takeaways discussion"
echo "================================="
echo "💬 Please discuss the key arguments/points from this transcript."
echo "   - What is the main topic?"
echo "   - What are the key arguments?"
echo "   - Any new concepts or entities?"

echo ""
echo "Step 3: Create source summary"
echo "=============================="
echo "To create a summary, create a file in wiki/sources/ like:"
echo "   $VAULT/wiki/sources/$(basename "$SOURCE" .md | head -50).md"
echo ""
echo "Frontmatter format:"
echo "---"
echo "tags: [topic, category]"
echo "created: $(date +%Y-%m-%d)"
echo "updated: $(date +%Y-%m-%d)"
echo "sources: [$(basename "$SOURCE")]"
echo "---"

echo ""
echo "Step 4: Update index.md"
echo "======================"
echo "Add to index.md under Concepts or Sources section"

echo ""
echo "Step 5: Update entities/concepts"
echo "================================"
echo "Update relevant pages in wiki/entities/ or wiki/concepts/"

echo ""
echo "Step 6: Update synthesis.md"
echo "==========================="
echo "If this changes the overall worldview, update wiki/synthesis.md"

echo ""
echo "Step 7: Append to log.md"
echo "========================"
echo "Add entry: ## [$(date +%Y-%m-%d)] ingest | $(basename "$SOURCE" .md)"

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "                    📋 INGEST CHECKLIST"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "After creating the summary, verify:"
echo ""
echo "   [ ] Read complete source in raw/"
echo "   [ ] Created summary in wiki/sources/"
echo "   [ ] Added to index.md under correct category"
echo "   [ ] Updated relevant entity pages"
echo "   [ ] Updated relevant concept pages"
echo "   [ ] Updated synthesis.md if worldview changed"
echo "   [ ] Appended entry to log.md"
echo ""
echo "Use 'lint.sh' to check for issues after ingest"