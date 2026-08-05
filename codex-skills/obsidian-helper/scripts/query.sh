#!/bin/bash

# Query the AI Brain vault for topics, concepts, or entities

VAULT="/Users/moll/Library/Mobile Documents/iCloud~md~obsidian/Documents/AI brain"
QUERY=$1

if [ -z "$QUERY" ]; then
    echo "Usage: query.sh <search-term>"
    echo "Example: query.sh consciousness"
    echo ""
    echo "Search options:"
    echo "  - Concepts in wiki/concepts/"
    echo "  - Entities in wiki/entities/"
    echo "  - Sources in wiki/sources/"
    echo "  - Raw transcripts in raw/"
    exit 1
fi

echo "═══════════════════════════════════════════════════════════════"
echo "                    🔍 VAULT QUERY: $QUERY"
echo "═══════════════════════════════════════════════════════════════"
echo ""

echo "📚 Searching wiki/concepts/..."
find "$VAULT/wiki/concepts/" -name "*.md" -exec grep -l -i "$QUERY" {} \; 2>/dev/null | while read f; do
    echo "   📄 $(basename "$f")"
done

echo ""
echo "👤 Searching wiki/entities/..."
find "$VAULT/wiki/entities/" -name "*.md" -exec grep -l -i "$QUERY" {} \; 2>/dev/null | while read f; do
    echo "   📄 $(basename "$f")"
done

echo ""
echo "📖 Searching wiki/sources/..."
find "$VAULT/wiki/sources/" -name "*.md" -exec grep -l -i "$QUERY" {} \; 2>/dev/null | while read f; do
    echo "   📄 $(basename "$f")"
done

echo ""
echo "📜 Searching raw transcripts..."
count=$(grep -r -l -i "$QUERY" "$VAULT/raw/" 2>/dev/null | wc -l)
echo "   Found $count transcripts mentioning '$QUERY'"

if [ "$count" -gt 0 ] && [ "$count" -lt 10 ]; then
    echo "   Files:"
    grep -r -l -i "$QUERY" "$VAULT/raw/" 2>/dev/null | while read f; do
        echo "   - $(basename "$f")"
    done
elif [ "$count" -ge 10 ]; then
    echo "   (Too many to list - showing first 10)"
    grep -r -l -i "$QUERY" "$VAULT/raw/" 2>/dev/null | head -10 | while read f; do
        echo "   - $(basename "$f")"
    done
fi

echo ""
echo "🔗 Checking index.md..."
if grep -i "$QUERY" "$VAULT/index.md" >/dev/null 2>&1; then
    echo "   Found in index.md!"
    grep -i "$QUERY" "$VAULT/index.md" | head -3
fi

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "💡 Tip: Read relevant wiki pages for synthesized information"
echo "   Use [[wiki/page]] links to navigate between pages"
echo "═══════════════════════════════════════════════════════════════"