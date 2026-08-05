#!/bin/bash

# List contents of AI Brain vault

VAULT="/Users/moll/Library/Mobile Documents/iCloud~md~obsidian/Documents/AI brain"
TYPE=${1:-all}

echo "═══════════════════════════════════════════════════════════════"
echo "                    📚 VAULT CONTENTS"
echo "═══════════════════════════════════════════════════════════════"
echo ""

case "$TYPE" in
    entities)
        echo "👤 ENTITIES (wiki/entities/):"
        echo "-----------------------------------"
        if [ -d "$VAULT/wiki/entities" ]; then
            ls -1 "$VAULT/wiki/entities/" | sed 's/\.md$//' | while read e; do
                echo "   • $e"
            done
        else
            echo "   (No entities folder)"
        fi
        ;;
    concepts)
        echo "💡 CONCEPTS (wiki/concepts/):"
        echo "-----------------------------------"
        if [ -d "$VAULT/wiki/concepts" ]; then
            ls -1 "$VAULT/wiki/concepts/" | sed 's/\.md$//' | while read c; do
                echo "   • $c"
            done
        else
            echo "   (No concepts folder)"
        fi
        ;;
    sources)
        echo "📖 SOURCES (wiki/sources/):"
        echo "-----------------------------------"
        if [ -d "$VAULT/wiki/sources" ]; then
            ls -1 "$VAULT/wiki/sources/ | head -20" | sed 's/\.md$//' | while read s; do
                echo "   • $s"
            done
            total=$(ls -1 "$VAULT/wiki/sources/" 2>/dev/null | wc -l)
            if [ "$total" -gt 20 ]; then
                echo "   ... and $((total - 20)) more"
            fi
        else
            echo "   (No sources folder)"
        fi
        ;;
    raw)
        echo "📜 RAW TRANSCRIPTS (raw/):"
        echo "-----------------------------------"
        count=$(ls -1 "$VAULT/raw/" 2>/dev/null | wc -l)
        echo "   Total transcripts: $count"
        echo ""
        echo "   Recent files:"
        ls -1t "$VAULT/raw/" | head -10 | while read f; do
            echo "   • $f"
        done
        ;;
    all|*)
        echo "📊 VAULT STATISTICS:"
        echo "-----------------------------------"
        raw_count=$(ls -1 "$VAULT/raw/" 2>/dev/null | wc -l)
        concepts_count=$(ls -1 "$VAULT/wiki/concepts/" 2>/dev/null | wc -l)
        entities_count=$(ls -1 "$VAULT/wiki/entities/" 2>/dev/null | wc -l)
        sources_count=$(ls -1 "$VAULT/wiki/sources/" 2>/dev/null | wc -l)
        
        echo "   📜 Raw transcripts:     $raw_count"
        echo "   💡 Concepts:            $concepts_count"
        echo "   👤 Entities:            $entities_count"
        echo "   📖 Source summaries:    $sources_count"
        
        echo ""
        echo "📁 FOLDERS:"
        echo "-----------------------------------"
        echo "   • raw/              - Immutable sources"
        echo "   • wiki/concepts/   - Synthesized concepts"
        echo "   • wiki/entities/    - People & organizations"
        echo "   • wiki/sources/    - Source summaries"
        echo "   • index.md         - Content catalog"
        echo "   • log.md           - Activity log"
        echo "   • synthesis.md     - Worldview synthesis"
        ;;
esac

echo ""
echo "═══════════════════════════════════════════════════════════════"