"""
Big Pickle Handler for Cursor - Efficient Large Dataset Processing
Optimized for free model limitations and memory management
"""

import pickle
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Union
import gzip
import json

class BigPickleHandler:
    """
    Efficient handler for large pickle files in Cursor/Free model environments.
    Provides chunked reading, memory management, and selective loading.
    """
    
    def __init__(self, file_path: str, chunk_size: int = 1000):
        self.file_path = Path(file_path)
        self.chunk_size = chunk_size
        self.file_size = self.file_path.stat().st_size if self.file_path.exists() else 0
        
    def get_file_info(self) -> Dict[str, Any]:
        """Get comprehensive file information"""
        if not self.file_path.exists():
            return {"error": "File not found", "path": str(self.file_path)}
        
        # Quick peek at pickle structure
        try:
            with open(self.file_path, 'rb') as f:
                # Read just the first few bytes to determine structure
                header = f.read(100)
                f.seek(0, 2)  # Seek to end
                
            return {
                "file_path": str(self.file_path),
                "size_mb": round(self.file_size / (1024 * 1024), 2),
                "size_gb": round(self.file_size / (1024 * 1024 * 1024), 3),
                "exists": True,
                "readable": True
            }
        except Exception as e:
            return {"error": str(e), "path": str(self.file_path)}
    
    def peek_structure(self, max_items: int = 5) -> Dict[str, Any]:
        """Quickly peek at data structure without loading everything"""
        try:
            with open(self.file_path, 'rb') as f:
                data = pickle.load(f)
                
            structure_info = {
                "type": type(data).__name__,
                "length": len(data) if hasattr(data, '__len__') else None,
            }
            
            # Handle different data types
            if isinstance(data, dict):
                structure_info.update({
                    "keys_count": len(data),
                    "sample_keys": list(data.keys())[:max_items],
                    "sample_items": {k: str(v)[:100] for k, v in list(data.items())[:max_items]}
                })
            elif isinstance(data, (list, tuple)):
                structure_info.update({
                    "sample_items": [str(item)[:100] for item in data[:max_items]],
                    "item_types": list(set(type(item).__name__ for item in data[:max_items]))
                })
            else:
                structure_info["sample"] = str(data)[:200]
                
            return structure_info
        except Exception as e:
            return {"error": str(e)}
    
    def load_selective(self, keys: Optional[List[str]] = None, 
                    indices: Optional[List[int]] = None,
                    max_items: Optional[int] = None) -> Any:
        """Load only specific parts of the data"""
        try:
            with open(self.file_path, 'rb') as f:
                data = pickle.load(f)
            
            # Selective loading based on data type
            if isinstance(data, dict) and keys:
                return {k: data[k] for k in keys if k in data}
            elif isinstance(data, (list, tuple)) and indices:
                return [data[i] for i in indices if i < len(data)]
            elif max_items and hasattr(data, '__len__'):
                return data[:max_items]
            else:
                return data
        except Exception as e:
            return {"error": str(e)}
    
    def save_compressed(self, output_path: str, data: Any) -> bool:
        """Save data as compressed pickle to save space"""
        try:
            with gzip.open(output_path, 'wb') as f:
                pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)
            return True
        except Exception as e:
            print(f"Error saving compressed: {e}")
            return False
    
    def convert_to_json(self, output_path: str, max_items: Optional[int] = None) -> bool:
        """Convert pickle to JSON for better compatibility"""
        try:
            with open(self.file_path, 'rb') as f:
                data = pickle.load(f)
            
            # Limit data if specified
            if max_items and hasattr(data, '__len__'):
                if isinstance(data, dict):
                    data = dict(list(data.items())[:max_items])
                else:
                    data = data[:max_items]
            
            # Convert to JSON
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, default=str, ensure_ascii=False)
            
            return True
        except Exception as e:
            print(f"Error converting to JSON: {e}")
            return False
    
    def chunked_iterator(self):
        """Iterate over data in chunks (for lists/tuples)"""
        try:
            with open(self.file_path, 'rb') as f:
                data = pickle.load(f)
            
            if not hasattr(data, '__len__'):
                yield data
                return
            
            for i in range(0, len(data), self.chunk_size):
                yield data[i:i + self.chunk_size]
                
        except Exception as e:
            yield {"error": str(e)}
    
    def analyze_memory_usage(self) -> Dict[str, Any]:
        """Analyze memory usage patterns"""
        try:
            with open(self.file_path, 'rb') as f:
                data = pickle.load(f)
            
            # Sample memory usage
            import sys
            data_size = sys.getsizeof(data)
            
            analysis = {
                "data_type": type(data).__name__,
                "estimated_size_mb": round(data_size / (1024 * 1024), 2),
                "item_count": len(data) if hasattr(data, '__len__') else None,
                "recommendations": []
            }
            
            # Memory recommendations
            if data_size > 100 * 1024 * 1024:  # > 100MB
                analysis["recommendations"].append("Use selective loading with specific keys/indices")
            if data_size > 500 * 1024 * 1024:  # > 500MB
                analysis["recommendations"].append("Convert to compressed format")
            if analysis["item_count"] and analysis["item_count"] > 10000:
                analysis["recommendations"].append("Use chunked processing")
            
            return analysis
        except Exception as e:
            return {"error": str(e)}

def create_pickle_analysis_tool(file_path: str):
    """Create a ready-to-use analysis tool for a specific pickle file"""
    handler = BigPickleHandler(file_path)
    
    print(f"📁 Analyzing: {file_path}")
    print("=" * 50)
    
    # File info
    info = handler.get_file_info()
    if "error" in info:
        print(f"❌ Error: {info['error']}")
        return None
    
    print(f"📊 File Size: {info['size_mb']} MB ({info['size_gb']} GB)")
    print(f"✅ Status: Accessible")
    
    # Structure peek
    print("\n🔍 Data Structure:")
    structure = handler.peek_structure()
    if "error" in structure:
        print(f"❌ Error reading structure: {structure['error']}")
    else:
        print(f"   Type: {structure['type']}")
        if structure['length'] is not None:
            print(f"   Length: {structure['length']}")
        
        if 'sample_keys' in structure:
            print(f"   Sample Keys: {structure['sample_keys']}")
        if 'sample_items' in structure:
            print(f"   Sample Items: {list(structure['sample_items'].values())[:3]}...")
    
    # Memory analysis
    print("\n🧠 Memory Analysis:")
    memory = handler.analyze_memory_usage()
    if "error" in memory:
        print(f"❌ Error: {memory['error']}")
    else:
        print(f"   Estimated Size: {memory['estimated_size_mb']} MB")
        if memory['recommendations']:
            print("   Recommendations:")
            for rec in memory['recommendations']:
                print(f"     • {rec}")
    
    return handler

# Usage Examples for Cursor Environment
def cursor_examples():
    """Examples optimized for Cursor/free model usage"""
    
    print("""
🚀 BIG PICKLE HANDLER - CURSOR EXAMPLES
=====================================

# 1. Quick Analysis (Recommended first step)
handler = create_pickle_analysis_tool("your_data.pickle")

# 2. Load Only What You Need
data = handler.load_selective(keys=["important_key1", "important_key2"])
small_sample = handler.load_selective(max_items=100)  # First 100 items only

# 3. Chunked Processing (Great for large datasets)
for chunk in handler.chunked_iterator():
    process_chunk(chunk)  # Your processing function
    break  # Remove this to process all chunks

# 4. Convert to JSON (Better compatibility)
handler.convert_to_json("data.json", max_items=1000)

# 5. Save Compressed Version
handler.save_compressed("data_compressed.pkl.gz", data)

💡 PRO TIPS FOR CURSOR:
• Always start with create_pickle_analysis_tool() - gives you file info
• Use load_selective() to avoid memory limits
• Convert to JSON for easier inspection
• Use chunked processing for very large files
• Compress files to save space
""")

if __name__ == "__main__":
    # Run example analysis
    cursor_examples()
    
    # Test with current directory pickle files
    current_dir = Path(".")
    pickle_files = list(current_dir.glob("*.pkl")) + list(current_dir.glob("*.pickle"))
    
    if pickle_files:
        print(f"\n🔍 Found {len(pickle_files)} pickle files:")
        for file in pickle_files:
            print(f"   • {file}")
        
        # Analyze the first one as example
        print(f"\n📊 Analyzing {pickle_files[0]}:")
        create_pickle_analysis_tool(str(pickle_files[0]))