#!/bin/bash

# Export summary of AI Brain vault

VAULT="/Users/moll/Library/Mobile Documents/iCloud~md~obsidian/Documents/AI brain"
OUTPUT=${1:-}

echo "═══════════════════════════════════════════════════════════════"
echo "                    📤 VAULT EXPORT"
echo "═══════════════════════════════════════════════════════════════"
echo ""

# Statistics
raw_count=$(ls -1 "$VAULT/raw/" 2>/dev/null | wc -l)
concepts_count=$(ls -1 "$VAULT/wiki/concepts/" 2>/dev/null | wc -l)
entities_count=$(ls -1 "$VAULT/wiki/entities/" 2>/dev/null | wc -l)
sources_count=$(ls -1 "$VAULT/wiki/sources/" 2>/dev/null | wc -l)

echo "📊 VAULT STATISTICS"
echo "==================="
echo "   📜 Raw transcripts:     $raw_count"
echo "   💡 Concepts:            $concepts_count"
echo "   👤 Entities:            $entities_count"
echo "   📖 Source summaries:    $sources_count"

echo ""
echo "📚 CONCEPTS (Top 10)"
echo "===================="
ls -1 "$VAULT/wiki/concepts/" 2>/dev/null | head -10 | while read c; do
    echo "   • ${c%.md}"
done

echo ""
echo "👤 ENTITIES"
echo "=========="
ls -1 "$VAULT/wiki/entities/" 2>/dev/null | while read e; do
    echo "   • ${e%.md}"
done

echo ""
echo "📜 RECENT RAW FILES (Top 10)"
echo "============================="
ls -1t "$VAULT/raw/" | head -10 | while read f; do
    echo "   • $f"
done

echo ""
echo "📝 RECENT LOG ENTRIES"
echo "===================="
if [ -f "$VAULT/log.md" ]; then
    tail -10 "$VAULT/log.md" | while read line; do
        echo "   $line"
    done
fi

if [ -n "$OUTPUT" ]; then
    echo ""
    echo "💾 Saving to: $OUTPUT"
    {
        echo "# AI Brain Vault Export"
        echo ""
        echo "Generated: $(date)"
        echo ""
        echo "## Statistics"
        echo "- Raw transcripts: $raw_count"
        echo "- Concepts: $concepts_count"
        echo "- Entities: $entities_count"
        echo "- Sources: $sources_count"
    } > "$OUTPUT"
    echo "✅ Export saved!"
fi

echo ""
echo "═══════════════════════════════════════════════════════════════"