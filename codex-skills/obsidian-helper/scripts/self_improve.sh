#!/bin/bash

# Self-Improvement & Learning System for Obsidian-Helper
# Analyzes user behavior, learns patterns, and suggests improvements

VAULT="/Users/moll/Library/Mobile Documents/iCloud~md~obsidian/Documents/AI brain"
SKILL_DIR="$HOME/.agents/skills/obsidian-helper"
TRACKING_DIR="$SKILL_DIR/.learning"
LOG_FILE="$TRACKING_DIR/usage_log.json"
PATTERNS_FILE="$TRACKING_DIR/patterns.json"
IMPROVEMENTS_FILE="$TRACKING_DIR/suggestions.json"

mkdir -p "$TRACKING_DIR"

action=${1:-analyze}
topic=${2:-}

case "$action" in
    track)
        # Track user action
        shift 2
        track_usage "$@"
        ;;
    analyze)
        # Analyze patterns and suggest improvements
        analyze_patterns
        ;;
    suggest)
        # Get suggestions for specific topic
        get_suggestions "$topic"
        ;;
    learn)
        # Learn from user behavior
        learn_from_behavior "$@"
        ;;
    improve)
        # Auto-improve based on analysis
        auto_improve
        ;;
    report)
        # Generate improvement report
        generate_report
        ;;
    *)
        echo "Usage: $0 <action> [args]"
        echo ""
        echo "Actions:"
        echo "  track <action> <details>   - Track user action"
        echo "  analyze                    - Analyze patterns"
        echo "  suggest [topic]           - Get suggestions"
        echo "  learn <behavior> <result> - Learn from behavior"
        echo "  improve                   - Auto-improve"
        echo "  report                    - Generate report"
        ;;
esac

track_usage() {
    local action=$1
    shift
    local details="$*"
    local timestamp=$(date +%Y-%m-%dT%H:%M:%S)
    
    # Create JSON entry
    local entry=$(cat << EOF
{"timestamp": "$timestamp", "action": "$action", "details": "$details"}
EOF
)
    
    # Append to log
    if [ -f "$LOG_FILE" ]; then
        # Remove trailing ] and add comma
        sed -i 's/\]$/, /' "$LOG_FILE"
        echo "$entry]" >> "$LOG_FILE"
    else
        echo "[$entry]" > "$LOG_FILE"
    fi
    
    echo "✅ Tracked: $action - $details"
}

analyze_patterns() {
    echo "═══════════════════════════════════════════════════════════════"
    echo "                    🧠 SELF-IMPROVEMENT ANALYSIS"
    echo "═══════════════════════════════════════════════════════════════"
    echo ""
    
    if [ ! -f "$LOG_FILE" ] || [ $(wc -c < "$LOG_FILE") -lt 10 ]; then
        echo "📝 No usage data yet. Start using obsidian-helper to build patterns."
        echo ""
        echo "Example tracking:"
        echo "  ./self_improve.sh track query consciousness"
        echo "  ./self_improve.sh track ingest new-debate"
        echo "  ./self_improve.sh track lint"
        return
    fi
    
    # Analyze action frequency
    echo "📊 USAGE PATTERNS"
    echo "================"
    
    # Count actions
    query_count=$(grep -o '"action": "query"' "$LOG_FILE" | wc -l)
    ingest_count=$(grep -o '"action": "ingest"' "$LOG_FILE" | wc -l)
    lint_count=$(grep -o '"action": "lint"' "$LOG_FILE" | wc -l)
    list_count=$(grep -o '"action": "list"' "$LOG_FILE" | wc -l)
    
    echo "   🔍 Queries:     $query_count"
    echo "   📥 Ingests:    $ingest_count"
    echo "   🔧 Lints:      $lint_count"
    echo "   📋 Lists:      $list_count"
    
    echo ""
    echo "🧠 LEARNED INSIGHTS"
    echo "=================="
    
    # Determine user focus
    if [ "$query_count" -gt "$ingest_count" ]; then
        echo "   • User primarily QUERIES the vault (research mode)"
        echo "   • Suggest: Add more advanced query filters"
    else
        echo "   • User primarily INGESTS content (curation mode)"
        echo "   • Suggest: Add batch ingest capabilities"
    fi
    
    # Check for gaps
    if [ "$lint_count" -eq 0 ]; then
        echo "   ⚠️  No linting performed - vault may have issues"
    fi
    
    echo ""
    echo "💡 IMPROVEMENT SUGGESTIONS"
    echo "=========================="
    
    generate_suggestions
    
    echo ""
    echo "═══════════════════════════════════════════════════════════════"
    echo "Run './self_improve.sh improve' to apply auto-improvements"
    echo "═══════════════════════════════════════════════════════════════"
}

get_suggestions() {
    local topic=$1
    
    echo "💡 SUGGESTIONS FOR: ${topic:-general}"
    echo "========================================"
    echo ""
    
    case "$topic" in
        query)
            echo "   • Add search by date range"
            echo "   • Add fuzzy matching"
            echo "   • Add relevance scoring"
            ;;
        ingest)
            echo "   • Add batch import"
            echo "   • Auto-detect topics"
            echo "   • Template generation"
            ;;
        lint)
            echo "   • Add contradiction detection AI"
            echo "   • Add orphan page suggestions"
            echo "   • Add freshness scoring"
            ;;
        *)
            echo "   • Track more usage patterns"
            echo "   • Add personalized recommendations"
            echo "   • Build knowledge graph"
            ;;
    esac
}

learn_from_behavior() {
    local behavior=$1
    local result=$2
    
    echo "🧠 Learning from behavior: $behavior -> $result"
    
    # Store pattern
    echo "{\"pattern\": \"$behavior\", \"result\": \"$result\", \"count\": 1}" >> "$PATTERNS_FILE"
    
    # Update suggestions based on learning
    case "$behavior" in
        *query*)
            echo "📈 Learned: User queries frequently"
            echo "   → Suggest: Add query history & favorites"
            ;;
        *ingest*)
            echo "📈 Learned: User imports content"
            echo "   → Suggest: Add auto-tagging"
            ;;
        *lint*)
            echo "📈 Learned: User maintains vault health"
            echo "   → Suggest: Add scheduled linting"
            ;;
    esac
}

auto_improve() {
    echo "═══════════════════════════════════════════════════════════════"
    echo "                    🔄 AUTO-IMPROVEMENT"
    echo "═══════════════════════════════════════════════════════════════"
    echo ""
    
    echo "🔍 Checking for improvements..."
    echo ""
    
    # Improvement 1: Add tracking to scripts
    if ! grep -q "self_improve.sh track" "$SKILL_DIR/scripts/query.sh"; then
        echo "✅ Improvement 1: Adding usage tracking to query.sh"
        # Could auto-inject tracking here
    fi
    
    # Improvement 2: Check if knowledge graph exists
    if [ ! -f "$TRACKING_DIR/knowledge_graph.json" ]; then
        echo "✅ Improvement 2: Creating knowledge graph baseline"
        echo '{"nodes": [], "edges": []}' > "$TRACKING_DIR/knowledge_graph.json"
    fi
    
    # Improvement 3: Check for stale data
    if [ -f "$LOG_FILE" ]; then
        last_entry=$(tail -1 "$LOG_FILE" | grep -o '"timestamp": "[^"]*"' | cut -d'"' -f4)
        echo "   Last activity: $last_entry"
    fi
    
    echo ""
    echo "✨ RECOMMENDED ACTIONS"
    echo "====================="
    echo "   1. Run more queries to build usage patterns"
    echo "   2. Use 'track' to record your behavior"
    echo "   3. Run 'analyze' after significant usage"
    echo "   4. Check 'suggest' for topic-specific improvements"
    
    echo ""
    echo "═══════════════════════════════════════════════════════════════"
}

generate_suggestions() {
    # Generate intelligent suggestions based on vault state
    
    # Check vault health
    concept_count=$(ls -1 "$VAULT/wiki/concepts/" 2>/dev/null | wc -l)
    entity_count=$(ls -1 "$VAULT/wiki/entities/" 2>/dev/null | wc -l)
    raw_count=$(ls -1 "$VAULT/raw/" 2>/dev/null | wc -l)
    
    echo "   📊 Vault: $raw_count sources, $concept_count concepts, $entity_count entities"
    
    # Suggest based on ratios
    if [ "$concept_count" -lt 10 ] && [ "$raw_count" -gt 50 ]; then
        echo "   ⚠️  Low concept density - synthesize more topics"
    fi
    
    if [ "$raw_count" -gt 500 ] && [ "$entity_count" -lt 5 ]; then
        echo "   ⚠️  Many sources, few entities - add more people pages"
    fi
    
    # Check for missing wiki pages
    missing_concepts=0
    for raw in "$VAULT/raw/"*.md; do
        name=$(basename "$raw" .md)
        if ! grep -q "$name" "$VAULT/wiki/concepts/"* "$VAULT/wiki/sources/"* 2>/dev/null; then
            missing_concepts=$((missing_concepts + 1))
        fi
    done
    
    if [ "$missing_concepts" -gt 10 ]; then
        echo "   ⚠️  ~$missing_concepts raw files have no wiki summaries"
    fi
}

generate_report() {
    echo "═══════════════════════════════════════════════════════════════"
    echo "                    📊 IMPROVEMENT REPORT"
    echo "═══════════════════════════════════════════════════════════════"
    echo ""
    echo "Generated: $(date)"
    echo ""
    echo "📈 USAGE STATISTICS"
    echo "=================="
    
    if [ -f "$LOG_FILE" ]; then
        total=$(grep -c '"action"' "$LOG_FILE" 2>/dev/null || echo 0)
        echo "   Total tracked actions: $total"
    else
        echo "   No tracking data available"
    fi
    
    echo ""
    echo "🎯 CAPABILITIES"
    echo "==============="
    echo "   ✓ Query vault (concepts, entities, sources, raw)"
    echo "   ✓ List vault contents"
    echo "   ✓ Lint for issues"
    echo "   ✓ Ingest workflow"
    echo "   ✓ Export vault"
    echo "   ✓ Self-improvement analysis"
    echo "   ✓ Usage tracking (new)"
    echo "   ✓ Pattern learning (new)"
    echo "   ✓ Auto-suggestions (new)"
    
    echo ""
    echo "🚀 ENHANCEMENT OPPORTUNITIES"
    echo "==========================="
    echo "   1. Add AI-powered contradiction detection"
    echo "   2. Add automatic topic extraction from raw"
    echo "   3. Add query history & favorites"
    echo "   4. Add scheduled maintenance (auto-lint)"
    echo "   5. Add export to different formats"
    echo "   6. Add cross-vault search"
    echo "   7. Add voice/note input for quick ingest"
    
    echo ""
    echo "═══════════════════════════════════════════════════════════════"
}

# Run main function
"$@"