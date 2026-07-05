#!/usr/bin/env python3
"""
Fix solutions in exercises.ts:
1. Remove fn() placeholder garbage lines
2. Add function approach where missing
"""
import json, os, re, time, urllib.request

EXERCISES_FILE = '/Users/moll/Desktop/python_app/exercises.ts'
PROGRESS_FILE = '/Users/moll/Desktop/python_app/scripts/.solution_fix_progress.json'
OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen2.5-coder:1.5b"
MAX_RETRIES = 2
DELAY_BETWEEN = 0.2

SYSTEM_MSG = "You are a Python tutor. Write correct, runnable Python code. Only output code, no explanations."
FEW_SHOT = """Example function approach for 'Use all() to check if numbers are in range':
# Using function approach
def is_within_range(numbers, min_val, max_val):
    return all(min_val <= x <= max_val for x in numbers)

nums = [5, 6, 7]
print(is_within_range(nums, 1, 10))

Example function approach for 'Find longest key in kwargs':
# Using function approach
def find_longest_key(**kwargs):
    return max(kwargs, key=len)

print(find_longest_key(apple=5, banana=3, cherry=8))"""


def gen_function_approach(desc, icode, eid):
    """Generate a function approach for an exercise."""
    prompt = f"""{FEW_SHOT}

Write ONLY the function approach for this problem. Include:
- A proper function definition with good parameter names
- A call to the function with example input
- A print() of the result

Format exactly like the examples above, starting with "# Using function approach".

Problem #{eid}: {desc[:400]}
Starter code: {icode[:200]}"""

    payload = json.dumps({"model": MODEL, "messages": [
        {"role": "system", "content": SYSTEM_MSG},
        {"role": "user", "content": prompt}
    ], "stream": False, "options": {"temperature": 0.1, "num_predict": 512}}).encode()
    
    req = urllib.request.Request(OLLAMA_URL, data=payload,
                                 headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=120) as resp:
        r = json.loads(resp.read())
        return r["message"]["content"].strip()


def fix_solution(sol_text, desc, icode, eid):
    """Remove fn() garbage and add function approach if missing."""
    lines = sol_text.split('\n')
    
    # Remove lines with fn() placeholders
    cleaned = [l for l in lines if 'fn(' not in l]
    
    # Check if function approach exists
    has_func = any('function approach' in l.lower() for l in cleaned)
    
    # If missing function approach, generate one
    if not has_func:
        try:
            new_code = gen_function_approach(desc, icode, eid)
            # Strip markdown fences if present
            new_code = re.sub(r'```\w*\n?', '', new_code).strip()
            # Insert at the beginning
            result = new_code + '\n\n' + '\n'.join(cleaned)
            print(f'  +Added function approach')
            return result
        except Exception as ex:
            print(f'  +GEN FAILED: {ex}')
            return '\n'.join(cleaned)
    
    return '\n'.join(cleaned)


def read_blocks(content):
    """Parse exercises from TypeScript file content."""
    lines = content.split('\n')
    start_idx = 0
    for i, line in enumerate(lines):
        if 'Exercise[] = [' in line or ('EXERCISES:' in line and '[' in line):
            start_idx = i + 1
            break
    blocks = []
    in_ex = False
    depth = 0
    cur = []
    for i in range(start_idx, len(lines)):
        ob = lines[i].count('{')
        cb = lines[i].count('}')
        if '{' in lines[i] and not in_ex:
            in_ex = True
            depth = ob - cb
            cur = [(lines[i], i)]
        elif in_ex:
            cur.append((lines[i], i))
            depth += ob - cb
            if depth <= 0:
                blocks.append(cur)
                cur = []
                in_ex = False
    return blocks


def get_field(block, field):
    full = ''.join(l for l, _ in block)
    m = re.search(r'"' + field + r'":\s*"(?:\\.|[^"\\])*"', full)
    if m:
        raw = m.group(0)
        val = re.search(r'":\s*"(.*)"$', raw)
        if val:
            return val.group(1)
    return ''


def get_field_raw(block, field):
    """Get the raw matched text including the full key:value pair."""
    full = ''.join(l for l, _ in block)
    m = re.search(r'"' + field + r'":\s*"(?:\\.|[^"\\])*"', full)
    return m.group(0) if m else ''


def get_id(block):
    full = ''.join(l for l, _ in block)
    m = re.search(r'"id":\s*(\d+)', full)
    return int(m.group(1)) if m else 0


def main():
    with open(EXERCISES_FILE, 'r') as f:
        content = f.read()
    
    blocks = read_blocks(content)
    print(f'Read {len(blocks)} blocks.')
    
    # Count stats
    fn_count = 0
    no_func_count = 0
    
    for block in blocks:
        sol = get_field(block, 'solution')
        if not sol:
            continue
        unescaped = sol.replace('\\n', '\n').replace('\\"', '"').replace('\\\\', '\\')
        if 'fn(' in unescaped:
            fn_count += 1
        if 'function approach' not in unescaped.lower():
            no_func_count += 1
    
    print(f'Exercises with fn() placeholders: {fn_count}')
    print(f'Exercises without function approach: {no_func_count}')
    
    # Process: strip fn() first (safe, no AI needed)
    lines = content.split('\n')
    edits = []  # (lineno, removal_of_old, insertion_of_new)
    
    for block in blocks:
        eid = get_id(block)
        desc = get_field(block, 'description').replace('\\n', ' ').replace('"', "'")
        icode = get_field(block, 'initialCode').replace('\\n', ' ').replace('"', "'")
        
        # Find solution field position
        sol_lineno = None
        for bl, lineno in block:
            if '"solution":' in bl:
                sol_lineno = lineno
                break
        
        if sol_lineno is None:
            continue
        
        old_sol_raw = get_field(block, 'solution')
        if not old_sol_raw:
            continue
        
        unescaped = old_sol_raw.replace('\\n', '\n').replace('\\"', '"').replace('\\\\', '\\')
        
        # Check if anything needs fixing
        has_fn = 'fn(' in unescaped
        has_func = 'function approach' in unescaped.lower()
        
        if not has_fn and has_func:
            continue  # Nothing to fix
        
        print(f'[{eid}] fn={has_fn} func={has_func}... ', end='', flush=True)
        
        new_content = fix_solution(unescaped, desc, icode, eid)
        
        # Re-escape for JSON
        escaped = new_content.replace('\\', '\\\\').replace('\n', '\\n').replace('"', '\\"')
        new_sol_line = lines[sol_lineno]
        new_sol_line = re.sub(r'"solution":\s*"(?:\\.|[^"\\])*"', f'"solution": "{escaped}"', new_sol_line)
        edits.append((sol_lineno, new_sol_line))
        print('done')
        time.sleep(DELAY_BETWEEN)
    
    # Apply edits bottom-to-top
    edits.sort(key=lambda x: x[0], reverse=True)
    for lineno, new_line in edits:
        lines[lineno] = new_line
    
    with open(EXERCISES_FILE, 'w') as f:
        f.write('\n'.join(lines))
    
    print(f'\nFixed {len(edits)} solutions.')


if __name__ == '__main__':
    main()
