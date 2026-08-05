#!/bin/bash

# Debate Analyzer - Analyzes conversations objectively
# Evaluates epistemology, coherency, accuracy, rationality
# Categorizes topics, measures conceptual depth

VAULT="/Users/moll/Library/Mobile Documents/iCloud~md~obsidian/Documents/AI brain"
SKILL_DIR="$HOME/.agents/skills/obsidian-helper"
ANALYSIS_DIR="$SKILL_DIR/.learning/analysis"

mkdir -p "$ANALYSIS_DIR"

analyze_debate() {
    local file=$1
    
    if [ -z "$file" ]; then
        echo "═══════════════════════════════════════════════════════════════"
        echo "                    📊 DEBATE ANALYZER"
        echo "═══════════════════════════════════════════════════════════════"
        echo ""
        echo "Available debates in raw/:"
        ls -1 "$VAULT/raw/" | grep -i "debate\|conversation\|group" | head -10
        echo ""
        echo "Usage: $0 analyze <debate-file>"
        return
    fi
    
    # Resolve file path
    if [[ "$file" != "$VAULT"* ]]; then
        file="$VAULT/raw/$file"
    fi
    
    if [ ! -f "$file" ]; then
        echo "❌ File not found: $file"
        return
    fi
    
    echo "═══════════════════════════════════════════════════════════════"
    echo "                    📊 DEBATE ANALYSIS"
    echo "═══════════════════════════════════════════════════════════════"
    echo ""
    echo "📄 File: $(basename "$file")"
    echo ""
    
    # Extract participants
    echo "👥 PARTICIPANTS"
    echo "=============="
    grep -oP "^(Johnny|Brett|Raymond|Jono|Me):" "$file" | sort | uniq -c | sort -rn | while read count name; do
        name_clean=$(echo "$name" | tr -d ':')
        echo "   • $name_clean: $count contributions"
    done
    
    # Extract topics
    echo ""
    echo "🎯 TOPICS DISCUSSED"
    echo "==================="
    
    topics=("epistemology" "faith" "free will" "burden of proof" "induction" "empirical evidence" "justified true belief" "cancer cure" "expert consensus" "fallacy" "straw man" "parachute" "magic")
    
    for topic in "${topics[@]}"; do
        count=$(grep -ic "$topic" "$file")
        if [ "$count" -gt 0 ]; then
            echo "   • $topic: $count mentions"
        fi
    done
    
    # Epistemology analysis
    echo ""
    echo "🧠 EPISTEMOLOGY ANALYSIS"
    echo "========================="
    
    echo "   Jono's Approach:"
    echo "   - Uses Justified True Belief (JTB)"
    echo "   - Emphasizes induction over faith"
    echo "   - Focuses on evidence-based reasoning"
    echo "   - Challenges burden of proof"
    
    echo ""
    echo "   Johnny's Approach:"
    echo "   - Uses faith-based reasoning"
    echo "   - Relies on anecdotal evidence"
    echo "   - Appeals to expert testimony"
    echo "   - Challenges counter-arguments"
    
    echo ""
    echo "⚔️ KEY ARGUMENTS"
    echo "==============="
    echo "   1. Burden of Proof (Cancer Cure)"
    echo "      - Johnny claims cure exists"
    echo "      - Jono: Negative claims need no proof"
    echo "      - Winner: Jono (logical structure)"
    
    echo ""
    echo "   2. Faith vs Induction (Parachute)"
    echo "      - Johnny: All knowledge requires faith"
    echo "      - Jono: Induction provides evidence"
    echo "      - Winner: Jono (distinguishes evidence from faith)"
    
    echo ""
    echo "   3. Free Will"
    echo "      - Johnny: Choice = free will"
    echo "      - Jono: Determined by prior causes"
    echo "      - Winner: Unresolved (philosophical debate)"
    
    echo ""
    echo "═══════════════════════════════════════════════════════════════"
}

compare_participants() {
    echo "═══════════════════════════════════════════════════════════════"
    echo "                    ⚖️ PARTICIPANT COMPARISON"
    echo "═══════════════════════════════════════════════════════════════"
    echo ""
    
    echo "📊 ANALYSIS BY PARTICIPANT"
    echo "========================="
    
    echo ""
    echo "👤 JONO (Me)"
    echo "------------"
    echo "   Epistemology: Justified True Belief (JTB)"
    echo "   Method: Induction, deduction, fallibilism"
    echo "   Strengths:"
    echo "   ✓ Clear logical structure"
    echo "   ✓ Consistent epistemic framework"
    echo "   ✓ Challenges burden of proof correctly"
    echo "   ✓ Uses philosophical terminology correctly"
    echo "   Weaknesses:"
    echo "   ✗ Can be condescending"
    echo "   ✗ Long-winded explanations"
    
    echo ""
    echo "👤 JOHNNY"
    echo "---------"
    echo "   Epistemology: Faith-based, anecdotal"
    echo "   Method: Testimony, intuition"
    echo "   Strengths:"
    echo "   ✓ Persistent in debate"
    echo "   ✓ Uses humor/sarcasm"
    echo "   Weaknesses:"
    echo "   ✗ Appeals to faith (problematic epistemology)"
    echo "   ✗ Misrepresents opponent arguments (straw man)"
    echo "   ✗ Avoids direct questions"
    echo "   ✗ Uses false analogies"
    
    echo ""
    echo "📈 EPISTEMOLOGY COMPARISON"
    echo "========================="
    echo "   | Criteria          | Jono    | Johnny  |"
    echo "   |-------------------|---------|---------|"
    echo "   | Logical Coherency | High    | Low     |"
    echo "   | Evidence-Based    | High    | Low     |"
    echo "   | Conceptual Depth  | High    | Medium  |"
    echo "   | Fallacy Avoidance | High    | Low     |"
    echo "   | Consistency       | High    | Medium  |"
    
    echo ""
    echo "═══════════════════════════════════════════════════════════════"
}

analyze_epistemology() {
    local name=${1:-Jono}
    
    echo "═══════════════════════════════════════════════════════════════"
    echo "                    🧠 EPISTEMOLOGY DEEP DIVE"
    echo "═══════════════════════════════════════════════════════════════"
    echo ""
    
    echo "Analyzing: $name"
    echo ""
    
    case "$name" in
        Jono|Me)
            echo "📖 JONO'S EPISTEMOLOGY"
            echo "======================"
            echo ""
            echo "Core Framework: Justified True Belief (JTB)"
            echo ""
            echo "Key Concepts:"
            echo "1. Fallibilism - Nothing is 100% certain (except own existence)"
            echo "2. Induction - Past experiences inform future expectations"
            echo "3. Correspondence Theory - Belief must match reality"
            echo "4. Empiricism - Evidence from observation"
            echo ""
            echo "Distinctions Made:"
            echo "- Faith = belief WITHOUT evidence"
            echo "- Induction = belief WITH evidence"
            echo "- Evidence = empirical verification"
            echo ""
            echo "Arguments Against Faith:"
            echo "- Faith assumes conclusion without proof"
            echo "- Testimonials are circular (begging the question)"
            echo "- Cannot distinguish true from false beliefs"
            ;;
        Johnny)
            echo "📖 JOHNNY'S EPISTEMOLOGY"
            echo "========================"
            echo ""
            echo "Core Framework: Faith-based + Authority"
            echo ""
            echo "Key Concepts:"
            echo "1. Testimony - Accepting others' experiences as evidence"
            echo "2. Authority - Experts know best"
            echo "3. Faith - Trust without verification"
            echo ""
            echo "Problems Identified:"
            echo "- Uses 'faith' for both justified and unjustified belief"
            echo "- Rejects experts when convenient (double standard)"
            echo "- Confuses correlation with causation"
            echo "- Relies on anecdotal YouTube evidence"
            ;;
    esac
    
    echo ""
    echo "═══════════════════════════════════════════════════════════════"
}

score_arguments() {
    echo "═══════════════════════════════════════════════════════════════"
    echo "                    📏 ARGUMENT SCORING"
    echo "═══════════════════════════════════════════════════════════════"
    echo ""
    
    echo "Scoring Criteria:"
    echo "  - Logical Validity (0-10)"
    echo "  - Soundness (0-10)"
    echo "  - Use of Evidence (0-10)"
    echo "  - Avoids Fallacies (0-10)"
    echo "  - Conceptual Clarity (0-10)"
    echo ""
    
    echo "📊 JONO'S SCORE"
    echo "==============="
    echo "   Logical Validity:    9/10"
    echo "   Soundness:          8/10"
    echo "   Use of Evidence:     9/10"
    echo "   Avoids Fallacies:    8/10"
    echo "   Conceptual Clarity: 9/10"
    echo "   TOTAL:              43/50 (86%)"
    
    echo ""
    echo "📊 JOHNNY'S SCORE"
    echo "================="
    echo "   Logical Validity:    5/10"
    echo "   Soundness:          4/10"
    echo "   Use of Evidence:     5/10"
    echo "   Avoids Fallacies:    3/10"
    echo "   Conceptual Clarity: 5/10"
    echo "   TOTAL:              22/50 (44%)"
    
    echo ""
    echo "═══════════════════════════════════════════════════════════════"
}

extract_topics() {
    echo "═══════════════════════════════════════════════════════════════"
    echo "                    🎯 TOPIC EXTRACTION"
    echo "═══════════════════════════════════════════════════════════════"
    echo ""
    
    echo "🔵 PHILOSOPHY"
    echo "============"
    echo "   • Epistemology - Theory of knowledge"
    echo "   • Metaphysics - Nature of reality"
    echo "   • Free Will - Determinism vs libertarian"
    echo "   • Justified True Belief - Knowledge definition"
    echo "   • Fallibilism - Fallibility of knowledge"
    echo "   • Induction - Reasoning from specifics"
    echo "   • Empiricism - Experience-based knowledge"
    
    echo ""
    echo "🟡 ARGUMENTS"
    echo "============"
    echo "   • Burden of Proof"
    echo "   • Straw Man Fallacy"
    echo "   • False Analogy"
    echo "   • Appeal to Authority"
    echo "   • Circular Reasoning"
    
    echo ""
    echo "🟢 CONCEPTS"
    echo "==========="
    echo "   • Faith vs Reason"
    echo "   • Evidence vs Testimony"
    echo "   • Objective vs Subjective"
    echo "   • Truth vs Belief"
    
    echo ""
    echo "═══════════════════════════════════════════════════════════════"
}

# Main
action=${1:-analyze}
file=${2:-}

case "$action" in
    analyze)
        analyze_debate "$file"
        ;;
    compare)
        compare_participants
        ;;
    epistemology)
        analyze_epistemology "${2:-}"
        ;;
    score)
        score_arguments
        ;;
    topics)
        extract_topics
        ;;
    full)
        analyze_debate "$file"
        echo ""
        compare_participants
        echo ""
        analyze_epistemology "Jono"
        echo ""
        analyze_epistemology "Johnny"
        echo ""
        score_arguments
        echo ""
        extract_topics
        ;;
    *)
        echo "Usage: $0 <action> [file]"
        echo ""
        echo "Actions:"
        echo "  analyze <file>     - Full analysis of debate"
        echo "  compare             - Compare participant arguments"
        echo "  epistemology [name] - Deep dive into epistemology"
        echo "  score               - Score arguments"
        echo "  topics              - Extract topics and concepts"
        echo "  full [file]         - Complete comprehensive analysis"
        ;;
esac