#!/bin/bash

# Knowledge Graph Builder - Creates relationships between vault content

VAULT="/Users/moll/Library/Mobile Documents/iCloud~md~obsidian/Documents/AI brain"
SKILL_DIR="$HOME/.agents/skills/obsidian-helper"
GRAPH_DIR="$SKILL_DIR/.learning/graph"

mkdir -p "$GRAPH_DIR"

action=${1:-build}

case "$action" in
    build)
        build_graph
        ;;
    query)
        query_graph "${2:-}"
        ;;
    visualize)
        visualize_graph
        ;;
    stats)
        graph_stats
        ;;
    update)
        update_graph
        ;;
    *)
        echo "Usage: $0 <action>"
        echo "  build      - Build knowledge graph"
        echo "  query      - Query graph connections"
        echo "  visualize  - Show graph visualization"
        echo "  stats      - Show graph statistics"
        echo "  update     - Update graph with new content"
        ;;
esac

build_graph() {
    echo "═══════════════════════════════════════════════════════════════"
    echo "                    🔗 KNOWLEDGE GRAPH BUILDER"
    echo "═══════════════════════════════════════════════════════════════"
    echo ""
    
    echo "🔄 Building relationships from vault content..."
    echo ""
    
    nodes_file="$GRAPH_DIR/nodes.json"
    edges_file="$GRAPH_DIR/edges.json"
    
    # Clear existing
    > "$nodes_file"
    > "$edges_file"
    
    # Build nodes from concepts
    echo "📍 Creating nodes..."
    node_id=0
    
    for file in "$VAULT/wiki/concepts/"*.md; do
        if [ -f "$file" ]; then
            name=$(basename "$file" .md)
            # Extract first line as description
            desc=$(sed -n '4p' "$file" 2>/dev/null | head -c 100)
            echo "{\"id\": $node_id, \"type\": \"concept\", \"label\": \"$name\", \"description\": \"$desc\"}" >> "$nodes_file"
            node_id=$((node_id + 1))
        fi
    done
    
    for file in "$VAULT/wiki/entities/"*.md; do
        if [ -f "$file" ]; then
            name=$(basename "$file" .md)
            desc=$(sed -n '4p' "$file" 2>/dev/null | head -c 100)
            echo "{\"id\": $node_id, \"type\": \"entity\", \"label\": \"$name\", \"description\": \"$desc\"}" >> "$nodes_file"
            node_id=$((node_id + 1))
        fi
    done
    
    node_count=$(wc -l < "$nodes_file")
    echo "   ✅ Created $node_count nodes"
    
    # Build edges from links
    echo "🔗 Creating edges from wiki links..."
    edge_id=0
    
    for file in "$VAULT/wiki/concepts/"*.md "$VAULT/wiki/entities/"*.md; do
        if [ -f "$file" ]; then
            source=$(basename "$file" .md)
            # Find all [[links]]
            grep -oP '\[\[([^\]]+)\]\]' "$file" 2>/dev/null | while read link; do
                target=$(echo "$link" | sed 's/\[\[//;s/\]\]//')
                echo "{\"id\": $edge_id, \"source\": \"$source\", \"target\": \"$target\", \"type\": \"references\"}" >> "$edges_file"
                edge_id=$((edge_id + 1))
            done
        fi
    done
    
    edge_count=$(wc -l < "$edges_file")
    echo "   ✅ Created $edge_count edges"
    
    echo ""
    echo "═══════════════════════════════════════════════════════════════"
    echo "✅ Knowledge graph built!"
    echo ""
    echo "   Nodes: $node_count (concepts + entities)"
    echo "   Edges: $edge_count (links between pages)"
    echo ""
    echo "Run './knowledge_graph.sh query <topic>' to explore connections"
}

query_graph() {
    local topic=$1
    
    if [ -z "$topic" ]; then
        echo "Usage: $0 query <topic>"
        echo "Example: $0 query consciousness"
        return
    fi
    
    echo "═══════════════════════════════════════════════════════════════"
    echo "                    🔍 GRAPH QUERY: $topic"
    echo "═══════════════════════════════════════════════════════════════"
    echo ""
    
    nodes_file="$GRAPH_DIR/nodes.json"
    edges_file="$GRAPH_DIR/edges.json"
    
    if [ ! -f "$nodes_file" ]; then
        echo "⚠️  Graph not built yet. Run './knowledge_graph.sh build' first."
        return
    fi
    
    # Find direct connections
    echo "📍 DIRECT CONNECTIONS"
    echo "===================="
    
    # Find node
    node_line=$(grep -i "$topic" "$nodes_file" | head -1)
    if [ -n "$node_line" ]; then
        echo "   Found: $node_line"
        
        # Find edges
        connected=$(grep -i "$topic" "$edges_file" | head -10)
        if [ -n "$connected" ]; then
            echo ""
            echo "🔗 Connected to:"
            echo "$connected" | while read e; do
                source=$(echo "$e" | grep -oP '"source": "[^"]*"' | cut -d'"' -f4)
                target=$(echo "$e" | grep -oP '"target": "[^"]*"' | cut -d'"' -f4)
                if [ "$source" != "$topic" ]; then
                    echo "   ← $source"
                fi
                if [ "$target" != "$topic" ]; then
                    echo "   → $target"
                fi
            done
        else
            echo "   (No connections found)"
        fi
    else
        echo "   ⚠️  Topic '$topic' not found in graph"
    fi
    
    echo ""
    echo "💡 Suggestions:"
    echo "   • Try related topics: epistemology, naturalism"
    echo "   • Run 'build' to update graph"
    echo "   • Add more wiki pages to increase connections"
    
    echo ""
    echo "═══════════════════════════════════════════════════════════════"
}

visualize_graph() {
    echo "═══════════════════════════════════════════════════════════════"
    echo "                    🖼️ KNOWLEDGE GRAPH VISUALIZATION"
    echo "═══════════════════════════════════════════════════════════════"
    echo ""
    
    if [ ! -f "$GRAPH_DIR/nodes.json" ]; then
        echo "⚠️  Graph not built. Run './knowledge_graph.sh build' first."
        return
    fi
    
    node_count=$(wc -l < "$GRAPH_DIR/nodes.json")
    edge_count=$(wc -l < "$GRAPH_DIR/edges.json")
    
    echo "📊 Graph Summary"
    echo "================"
    echo "   Nodes: $node_count"
    echo "   Edges: $edge_count"
    echo ""
    
    echo "🗺️  TOP CONNECTED NODES"
    echo "======================="
    
    # Count connections per node
    cat "$GRAPH_DIR/edges.json" | grep -oP '"(source|target)": "[^"]*"' | \
        cut -d'"' -f4 | sort | uniq -c | sort -rn | head -10 | while read count node; do
        echo "   • $node ($count connections)"
    done
    
    echo ""
    echo "🧭 EXPLORATION PATH"
    echo "==================="
    echo "   epistemology → tjump-atheism → tjump-consciousness"
    echo "   (example path through graph)"
    
    echo ""
    echo "═══════════════════════════════════════════════════════════════"
}

graph_stats() {
    echo "═══════════════════════════════════════════════════════════════"
    echo "                    📊 GRAPH STATISTICS"
    echo "═══════════════════════════════════════════════════════════════"
    echo ""
    
    if [ ! -f "$GRAPH_DIR/nodes.json" ]; then
        echo "⚠️  Graph not built. Run './knowledge_graph.sh build' first."
        return
    fi
    
    concept_count=$(grep -c '"type": "concept"' "$GRAPH_DIR/nodes.json" 2>/dev/null || echo 0)
    entity_count=$(grep -c '"type": "entity"' "$GRAPH_DIR/nodes.json" 2>/dev/null || echo 0)
    
    echo "   📍 Total Nodes: $(wc -l < "$GRAPH_DIR/nodes.json")"
    echo "      - Concepts: $concept_count"
    echo "      - Entities: $entity_count"
    echo ""
    echo "   🔗 Total Edges: $(wc -l < "$GRAPH_DIR/edges.json")"
    echo ""
    
    # Calculate density
    if [ "$concept_count" -gt 0 ]; then
        density=$(echo "scale=2; $(wc -l < "$GRAPH_DIR/edges.json") * 2 / ($concept_count * ($concept_count - 1))" | bc 2>/dev/null || echo "N/A")
        echo "   📈 Graph Density: $density"
    fi
    
    echo ""
    echo "═══════════════════════════════════════════════════════════════"
}

update_graph() {
    echo "🔄 Updating knowledge graph..."
    build_graph
    echo "✅ Graph updated with latest vault content!"
}