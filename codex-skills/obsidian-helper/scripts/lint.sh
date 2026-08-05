#!/bin/bash

# Lint the AI Brain vault for issues

VAULT="/Users/moll/Library/Mobile Documents/iCloud~md~obsidian/Documents/AI brain"

echo "═══════════════════════════════════════════════════════════════"
echo "                    🔧 VAULT LINT"
echo "═══════════════════════════════════════════════════════════════"
echo ""

echo "1️⃣  Checking for pages without frontmatter..."
frontmatter_issues=0
for file in "$VAULT/wiki"/*.md "$VAULT/wiki"/*/*.md; do
    if [ -f "$file" ]; then
        if ! head -5 "$file" | grep -q -- "---"; then
            echo "   ⚠️  Missing frontmatter: $(basename "$file")"
            frontmatter_issues=$((frontmatter_issues + 1))
        fi
    fi
done
if [ "$frontmatter_issues" -eq 0 ]; then
    echo "   ✅ All pages have frontmatter"
fi

echo ""
echo "2️⃣  Checking for orphan pages (no inbound links)..."
orphan_count=0
for wiki_file in "$VAULT/wiki"/*.md "$VAULT/wiki"/*/*.md; do
    if [ -f "$wiki_file" ]; then
        filename=$(basename "$wiki_file" .md)
        if ! grep -r "\[\[$filename\]\]" "$VAULT/wiki/" "$VAULT"/*.md >/dev/null 2>&1; then
            if ! grep -r "\[\[wiki/.*$filename" "$VAULT/wiki/" "$VAULT"/*.md >/dev/null 2>&1; then
                echo "   ⚠️  Potentially orphan: $filename"
                orphan_count=$((orphan_count + 1))
            fi
        fi
    fi
done
if [ "$orphan_count" -eq 0 ]; then
    echo "   ✅ No orphan pages found"
fi

echo ""
echo "3️⃣  Checking for broken wiki links..."
broken_links=0
for file in "$VAULT/wiki"/*.md "$VAULT/wiki"/*/*.md; do
    if [ -f "$file" ]; then
        while IFS= read -r line; do
            if [[ $line =~ \[\[([^]]+)\]\] ]]; then
                raw_link="${BASH_REMATCH[1]}"
                link="${raw_link%%|*}"
                link="${link%%#*}"
                if [[ "$link" =~ ^http ]] || [[ -z "$link" ]]; then
                    continue
                fi

                if [[ "$link" == wiki/* ]]; then
                    target="$VAULT/$link.md"
                elif [[ -f "$VAULT/$link.md" ]]; then
                    target="$VAULT/$link.md"
                else
                    target="$VAULT/wiki/$link.md"
                fi

                if [[ ! -f "$target" ]]; then
                    echo "   ⚠️  Broken link in $(basename "$file"): $raw_link"
                    broken_links=$((broken_links + 1))
                fi
            fi
        done < "$file"
    fi
done
if [ "$broken_links" -eq 0 ]; then
    echo "   ✅ No broken links found"
fi

echo ""
echo "4️⃣  Checking for unlinked raw files..."
unlinked_raw=0
for raw_file in "$VAULT/raw"/*.md; do
    if [ -f "$raw_file" ]; then
        filename=$(basename "$raw_file" .md)
        if ! grep -q "$filename" "$VAULT/wiki/"*/*.md "$VAULT/wiki/sources"/*.md 2>/dev/null; then
            echo "   ⚠️  Unlinked raw file: $filename"
            unlinked_raw=$((unlinked_raw + 1))
        fi
    fi
done
if [ "$unlinked_raw" -eq 0 ]; then
    echo "   ✅ All raw files are referenced"
fi

echo ""
echo "5️⃣  Checking index.md completeness..."
if [ -f "$VAULT/index.md" ]; then
    concept_count=$(grep -c "^\- \[\[" "$VAULT/index.md" 2>/dev/null || echo 0)
    wiki_concepts=$(ls -1 "$VAULT/wiki/concepts/" 2>/dev/null | wc -l)
    if [ "$concept_count" -lt "$wiki_concepts" ]; then
        echo "   ⚠️  index.md may be outdated (concepts: $concept_count vs wiki: $wiki_concepts)"
    else
        echo "   ✅ index.md appears current"
    fi
fi

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "                    ✅ LINT COMPLETE"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "💡 Run 'query.sh <topic>' to search the vault"
echo "💡 Run 'list.sh' to see vault contents"
echo "💡 Run 'ingest.sh <file>' to add new content"
