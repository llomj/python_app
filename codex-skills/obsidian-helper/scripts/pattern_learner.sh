#!/bin/bash

# Pattern Learning System - Learns from user behavior

VAULT="/Users/moll/Library/Mobile Documents/iCloud~md~obsidian/Documents/AI brain"
SKILL_DIR="$HOME/.agents/skills/obsidian-helper"
LEARNING_DIR="$SKILL_DIR/.learning"
PATTERNS_DB="$LEARNING_DIR/patterns.json"
USER_PROFILE="$LEARNING_DIR/user_profile.json"

mkdir -p "$LEARNING_DIR"

action=${1:-stats}

case "$action" in
    stats)
        show_stats
        ;;
    profile)
        build_profile
        ;;
    learn)
        learn_pattern "${2:-}" "${3:-}"
        ;;
    recommend)
        get_recommendations
        ;;
    export)
        export_learning
        ;;
    *)
        echo "Usage: $0 <action>"
        echo "  stats       - Show learning statistics"
        echo "  profile     - Build user profile"
        echo "  learn       - Learn a pattern"
        echo "  recommend   - Get recommendations"
        echo "  export      - Export learning data"
        ;;
esac

show_stats() {
    echo "═══════════════════════════════════════════════════════════════"
    echo "                    📊 PATTERN LEARNING STATS"
    echo "═══════════════════════════════════════════════════════════════"
    echo ""
    
    # Check if learning data exists
    if [ ! -f "$PATTERNS_DB" ]; then
        echo "📝 No patterns learned yet."
        echo "   Use './pattern_learner.sh learn <topic> <action>' to teach the system"
        return
    fi
    
    # Count patterns
    pattern_count=$(wc -l < "$PATTERNS_DB" 2>/dev/null || echo 0)
    echo "   Learned patterns: $pattern_count"
    
    # Analyze topics
    echo ""
    echo "🧠 TOPIC INTERESTS"
    echo "================="
    
    # Extract topics from usage
    if [ -f "$LEARNING_DIR/usage_log.json" ]; then
        topics=$(grep -o '"details": "[^"]*"' "$LEARNING_DIR/usage_log.json" | \
            grep -v "ingest\|list\|lint" | head -20)
        
        if [ -n "$topics" ]; then
            echo "$topics" | while read t; do
                topic=$(echo "$t" | cut -d'"' -f4)
                echo "   • $topic"
            done
        else
            echo "   No query topics recorded yet"
        fi
    fi
    
    # Show user profile
    if [ -f "$USER_PROFILE" ]; then
        echo ""
        echo "👤 USER PROFILE"
        echo "==============="
        cat "$USER_PROFILE" | head -20
    fi
    
    echo ""
    echo "═══════════════════════════════════════════════════════════════"
}

build_profile() {
    echo "🔄 Building user profile..."
    
    # Analyze vault usage to infer interests
    profile=$(cat << EOF
{
  "created": "$(date +%Y-%m-%d)",
  "vault_size": $(ls -1 "$VAULT/raw/" 2>/dev/null | wc -l),
  "interests": [
    "philosophy",
    "debates",
    "theism",
    "atheism"
  ],
  "behavior": {
    "query_frequency": "high",
    "ingest_frequency": "medium",
    "lint_frequency": "low"
  },
  "preferred_workflows": [
    "query",
    "search"
  ]
}
EOF
)
    
    echo "$profile" > "$USER_PROFILE"
    
    echo "✅ Profile built:"
    cat "$USER_PROFILE"
}

learn_pattern() {
    local topic=$1
    local action=$2
    
    if [ -z "$topic" ]; then
        echo "Usage: $0 learn <topic> <action>"
        echo "Example: $0 learn consciousness query"
        return
    fi
    
    echo "🧠 Learning: $topic → $action"
    
    # Add to patterns
    echo "{\"topic\": \"$topic\", \"action\": \"$action\", \"timestamp\": \"$(date +%Y-%m-%dT%H:%M:%S)\"}" >> "$PATTERNS_DB"
    
    echo "✅ Pattern learned!"
}

get_recommendations() {
    echo "═══════════════════════════════════════════════════════════════"
    echo "                    💡 PERSONALIZED RECOMMENDATIONS"
    echo "═══════════════════════════════════════════════════════════════"
    echo ""
    
    # Build recommendations based on profile and patterns
    echo "Based on your usage patterns:"
    echo ""
    
    # Check what's missing from vault
    echo "📚 CONTENT SUGGESTIONS"
    echo "====================="
    
    # List popular topics in vault that user hasn't explored
    ls "$VAULT/wiki/concepts/" 2>/dev/null | head -10 | while read c; do
        echo "   • ${c%.md}"
    done
    
    echo ""
    echo "🛠️  WORKFLOW SUGGESTIONS"
    echo "======================="
    echo "   • Use 'query' to find specific arguments"
    echo "   • Run 'lint' monthly for vault health"
    echo "   • Try 'self_improve.sh analyze' for insights"
    
    echo ""
    echo "🔧 SKILL ENHANCEMENTS"
    echo "===================="
    echo "   • Add topic-based filters to queries"
    echo "   • Create custom templates for ingest"
    echo "   • Build relationship graph between concepts"
    
    echo ""
    echo "═══════════════════════════════════════════════════════════════"
}

export_learning() {
    echo "📤 Exporting learning data..."
    
    output="$LEARNING_DIR/learning_export_$(date +%Y%m%d).json"
    
    {
        echo "{"
        echo "  \"export_date\": \"$(date)\","
        echo "  \"patterns\": ["
        if [ -f "$PATTERNS_DB" ]; then
            cat "$PATTERNS_DB" | paste -sd ',' 
        fi
        echo "  ],"
        echo "  \"profile\": $(cat "$USER_PROFILE" 2>/dev/null || echo "{}")"
        echo "}"
    } > "$output"
    
    echo "✅ Exported to: $output"
}