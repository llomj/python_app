#!/bin/bash

# Auto-Suggestion Engine - Context-aware recommendations

VAULT="/Users/moll/Library/Mobile Documents/iCloud~md~obsidian/Documents/AI brain"
SKILL_DIR="$HOME/.agents/skills/obsidian-helper"
SUGGEST_DIR="$SKILL_DIR/.learning/suggestions"

mkdir -p "$SUGGEST_DIR"

action=${1:-generate}
context=${2:-}

case "$action" in
    generate)
        generate_suggestions "$context"
        ;;
    add)
        add_suggestion "${2:-}" "${3:-}"
        ;;
    accept)
        accept_suggestion "${2:-}"
        ;;
    dismiss)
        dismiss_suggestion "${2:-}"
        ;;
    list)
        list_suggestions
        ;;
    *)
        echo "Usage: $0 <action> [args]"
        echo "  generate [context]  - Generate suggestions"
        echo "  add <type> <desc>   - Add manual suggestion"
        echo "  accept <id>         - Accept suggestion"
        echo "  dismiss <id>         - Dismiss suggestion"
        echo "  list                - List all suggestions"
        ;;
esac

generate_suggestions() {
    local context=$1
    
    echo "═══════════════════════════════════════════════════════════════"
    echo "                    💡 AUTO-SUGGESTIONS"
    echo "═══════════════════════════════════════════════════════════════"
    echo ""
    
    # Analyze vault state and generate relevant suggestions
    suggestions=()
    
    # Check vault health
    concept_count=$(ls -1 "$VAULT/wiki/concepts/" 2>/dev/null | wc -l)
    entity_count=$(ls -1 "$VAULT/wiki/entities/" 2>/dev/null | wc -l)
    raw_count=$(ls -1 "$VAULT/raw/" 2>/dev/null | wc -l)
    
    # Suggest based on gaps
    if [ "$concept_count" -lt 15 ]; then
        echo "   📝 [1] Low concept count ($concept_count) - synthesize more topics"
        suggestions+=("1")
    fi
    
    if [ "$raw_count" -gt "$((concept_count * 10))" ]; then
        ratio=$((raw_count / concept_count))
        echo "   📝 [2] High ratio (~$ratio raw per concept) - add more summaries"
        suggestions+=("2")
    fi
    
    # Check for unprocessed raw files
    unprocessed=0
    for raw in "$VAULT/raw/"*.md; do
        name=$(basename "$raw" .md)
        if ! grep -q "$name" "$VAULT/wiki/sources/"* 2>/dev/null; then
            unprocessed=$((unprocessed + 1))
        fi
    done
    
    if [ "$unprocessed" -gt 5 ]; then
        echo "   📝 [3] $unprocessed unprocessed transcripts - consider ingesting"
        suggestions+=("3")
    fi
    
    # Context-specific suggestions
    case "$context" in
        query)
            echo "   📝 [4] Add search filters (by date, topic, source)"
            suggestions+=("4")
            echo "   📝 [5] Add query history and favorites"
            suggestions+=("5")
            ;;
        ingest)
            echo "   📝 [6] Add batch import capability"
            suggestions+=("6")
            echo "   📝 [7] Auto-detect topics from transcript"
            suggestions+=("7")
            ;;
        lint)
            echo "   📝 [8] Add AI-powered contradiction detection"
            suggestions+=("8")
            echo "   📝 [9] Schedule automatic linting"
            suggestions+=("9")
            ;;
    esac
    
    # Learning-based suggestions
    echo ""
    echo "🧠 LEARNED RECOMMENDATIONS"
    echo "========================="
    
    # Look for patterns
    if [ -f "$SKILL_DIR/.learning/usage_log.json" ]; then
        last_queries=$(tail -5 "$SKILL_DIR/.learning/usage_log.json" | grep "query" | wc -l)
        
        if [ "$last_queries" -gt 3 ]; then
            echo "   • You're query-focused - try advanced search filters"
        fi
    fi
    
    # Default suggestions
    echo "   • Run 'knowledge_graph.sh build' to see connections"
    echo "   • Run 'self_improve.sh analyze' for detailed insights"
    echo "   • Use 'pattern_learner.sh profile' to build your profile"
    
    echo ""
    echo "═══════════════════════════════════════════════════════════════"
    echo "To accept: $0 accept <id>"
    echo "To dismiss: $0 dismiss <id>"
    echo "═══════════════════════════════════════════════════════════════"
}

add_suggestion() {
    local type=$1
    local desc=$2
    
    if [ -z "$type" ] || [ -z "$desc" ]; then
        echo "Usage: $0 add <type> <description>"
        return
    fi
    
    local id=$(date +%s)
    echo "{\"id\": $id, \"type\": \"$type\", \"description\": \"$desc\", \"status\": \"pending\", \"created\": \"$(date +%Y-%m-%d)\"}" >> "$SUGGEST_DIR/suggestions.json"
    
    echo "✅ Added suggestion: $desc"
}

accept_suggestion() {
    local id=$1
    
    if [ -z "$id" ]; then
        echo "Usage: $0 accept <id>"
        return
    fi
    
    echo "✅ Accepted suggestion $id"
    echo "   (This would trigger an action in production)"
    
    # Log acceptance for learning
    echo "{\"suggestion_id\": $id, \"action\": \"accept\", \"timestamp\": \"$(date +%Y-%m-%dT%H:%M:%S)\"}" >> "$SUGGEST_DIR/feedback.json"
}

dismiss_suggestion() {
    local id=$1
    
    if [ -z "$id" ]; then
        echo "Usage: $0 dismiss <id>"
        return
    fi
    
    echo "✅ Dismissed suggestion $id"
}

list_suggestions() {
    echo "📋 ALL SUGGESTIONS"
    echo "================="
    
    if [ ! -f "$SUGGEST_DIR/suggestions.json" ]; then
        echo "   No suggestions yet. Run 'generate' first."
        return
    fi
    
    cat "$SUGGEST_DIR/suggestions.json" | while read line; do
        echo "   $line"
    done
}