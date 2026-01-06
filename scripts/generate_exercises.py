import os
import re
import json

# Configuration
SOURCE_FILES = [
    "level1_500.py",
    "level1_1000-1.py",
    "level1_1500.py",
    "level1_2000.py"
]
OUTPUT_FILE = "exercises.ts"

def parse_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to split by the docstring blocks
    # Looking for """ ... """ blocks.
    # We assume the file starts with a docstring or code, but the pattern is mainly:
    # """ Problem ... """
    # Code
    
    # We'll use a regex that finds the docstring, captures it, and then allows capturing the code following it until the next docstring.
    pattern = re.compile(r'"""(.*?)"""(.*?)(?="""|$)', re.DOTALL)
    
    matches = pattern.findall(content)
    exercises = []
    
    for docstring, code_block in matches:
        docstring = docstring.strip()
        code_block = code_block.strip()
        
        # Parse docstring for ID and Description
        # Formats seen: 
        # "Problem: 1501\nDescription..."
        # "Problem 1:\nDescription..."
        
        lines = docstring.split('\n')
        # Filter out empty lines
        lines = [l.strip() for l in lines if l.strip()]
        
        if not lines:
            continue
            
        header = lines[0]
        description = "\n".join(lines[1:]) if len(lines) > 1 else header
        
        # Extract ID
        problem_id = 0
        id_match = re.search(r'Problem\s*:?\s*(\d+)', header, re.IGNORECASE)
        if id_match:
            problem_id = int(id_match.group(1))
        
        if problem_id == 0:
            print(f"Skipping block, no ID found in: {header}")
            continue

        # Generate Initial Code
        # We want to preserve function definitions but remove bodies.
        # Simple heuristic:
        # If line starts with 'def ', keep it and add '    pass'.
        # Keep imports.
        # Keep comments? Maybe not.
        
        initial_code_lines = []
        in_def = False
        
        code_lines = code_block.split('\n')
        for line in code_lines:
            stripped = line.strip()
            if line.startswith('import ') or line.startswith('from '):
                initial_code_lines.append(line)
            elif line.startswith('def '):
                initial_code_lines.append(line)
                initial_code_lines.append("    pass") # valid indent assuming 4 spaces
                initial_code_lines.append("")
            elif line.startswith('class '):
                initial_code_lines.append(line)
                initial_code_lines.append("    pass")
                initial_code_lines.append("")
            # If it's a simple top-level print or assignment, we might skip it for the "initial" code 
            # so the user has to write it.
            # But for "fix this" type problems, maybe we want the wrong code?
            # The prompt descriptions says "Write a function...", so blank slate or signature is best.
            # However, looking at the code, some are "Debug this" (though most seem to be "Write a function").
            # Let's stick to signatures if present, else just a comment.
            
        if not any(l.startswith('def ') or l.startswith('class ') for l in initial_code_lines):
            # If no function/class structure detected, maybe just provide a comment
            initial_code_lines.append("# Write your solution here")
            initial_code_lines.append("")
            
        initial_code = "\n".join(initial_code_lines).strip()
        
        # Clean up solution
        solution = code_block.strip()
        
        exercise = {
            "id": problem_id,
            "title": f"Problem {problem_id}",
            "description": description,
            "initialCode": initial_code,
            "solution": solution,
            "hint": "Check the description for requirements.",
            "category": "Level 1"
        }
        exercises.append(exercise)
        
    return exercises

def main():
    all_exercises = []
    seen_ids = set()
    
    for fname in SOURCE_FILES:
        if not os.path.exists(fname):
            print(f"File not found: {fname}")
            continue
            
        print(f"Parsing {fname}...")
        file_exercises = parse_file(fname)
        
        for ex in file_exercises:
            if ex['id'] in seen_ids:
                print(f"Duplicate ID found: {ex['id']}, skipping.")
                continue
            seen_ids.add(ex['id'])
            all_exercises.append(ex)
            
    # Sort by ID
    all_exercises.sort(key=lambda x: x['id'])
    
    # Generate TypeScript file
    ts_content = """import { Exercise } from './types';

export const EXERCISES: Exercise[] = %s;
""" % json.dumps(all_exercises, indent=4)

    # Allow for some TS specific formatting adjustments if needed (like regex replacement for keys if they weren't quoted, but JSON is valid TS)
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(ts_content)
        
    print(f"Successfully generated {OUTPUT_FILE} with {len(all_exercises)} exercises.")

if __name__ == "__main__":
    main()
