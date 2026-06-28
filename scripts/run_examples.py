"""
Extract test calls from solutions and compute actual outputs by running the code.
Updates problem descriptions with verified examples.
"""
import re
import json
import subprocess
import sys

EXERCISES_FILE = '/Users/moll/Desktop/python_app/exercises.ts'

def load_exercises():
    with open(EXERCISES_FILE, 'r') as f:
        content = f.read()
    start = content.find('[\n')
    end = content.rfind('];') + 1
    prefix = content[:start]
    suffix = content[end:]
    json_str = content[start:end]
    json_str = re.sub(r',\s*}', '}', json_str)
    json_str = re.sub(r',\s*]', ']', json_str)
    exercises = json.loads(json_str)
    return exercises, prefix, suffix, json_str

def run_py(code, timeout=5):
    try:
        r = subprocess.run(['python3', '-c', code], capture_output=True, text=True, timeout=timeout)
        return r.stdout.strip(), r.stderr.strip()
    except:
        return None, 'ERROR'

def extract_fn_name(desc, code):
    m = re.search(r'def\s+(\w+)\s*\(', code)
    if m: return m.group(1)
    m = re.search(r'`(\w+)`', desc)
    if m: return m.group(1)
    return None

exercises, prefix, suffix, orig_json = load_exercises()
print(f"Loaded {len(exercises)} exercises")

count = 0
error_count = 0
for i, ex in enumerate(exercises):
    desc = ex['description']
    sol = ex['solution']
    
    if any(p in desc.lower() for p in ['example', 'input:', '→', '->', 'for example']):
        continue
    
    fn = extract_fn_name(desc, ex['initialCode'])
    if not fn:
        continue
    
    # Find print(fn(...)) calls in solution
    calls = []
    for m in re.finditer(rf'print\(\s*{re.escape(fn)}\s*\((.*?)\)\s*\)', sol, re.DOTALL):
        calls.append(m.group(1).strip())
    
    if not calls:
        # Try with print(result) patterns
        for m in re.finditer(r'print\((\w+)\)\s*#.*?Output:\s*(\S+)', sol):
            var_name = m.group(1)
            out_val = m.group(2)
            # Find the var definition
            var_def = re.search(rf'\b{re.escape(var_name)}\s*=\s*(.*)', sol)
            if var_def:
                calls.append((var_def.group(1).strip(), out_val))
    
    # If we have direct calls, build and run code
    if isinstance(calls, list) and calls and not isinstance(calls[0], tuple):
        # Build code: all function defs + test calls
        code_lines = []
        for match in re.finditer(r'def\s+\w+\(.*?\):\s*(?:\n\s+.*)*', sol):
            code_lines.append(match.group())
        
        func_blocks = list(re.finditer(r'(?:#.*\n)?def\s+\w+\(.*?\):\s*(?:\n\s+.*)*', sol))
        if not func_blocks:
            continue
        
        runnable = '\n\n'.join(m.group() for m in func_blocks)
        test_lines = [f'print({fn}({args}))' for args in calls[:4]]
        if not test_lines:
            continue
        
        full_code = runnable + '\n\n' + '\n'.join(test_lines)
        
        stdout, stderr = run_py(full_code)
        if stdout and not stderr:
            outputs = stdout.strip().split('\n')
            ex_lines = ['', 'Examples:']
            for j, args in enumerate(calls[:4]):
                out = outputs[j] if j < len(outputs) else '?'
                ex_lines.append(f'  {fn}({args}) → {out}')
            ex['description'] = desc + '\n'.join(ex_lines)
            count += 1
    
    if (i+1) % 200 == 0:
        print(f"  {i+1}/{len(exercises)} - updated: {count}")

# Write back
lines = []
for ex in exercises:
    obj_str = json.dumps(ex, indent=4, ensure_ascii=False)
    obj_lines = obj_str.split('\n')
    fixed = ['    ' + l if l.startswith('{') or l.startswith('}') else '        ' + l for l in obj_lines]
    lines.append('\n'.join(fixed))

with open(EXERCISES_FILE, 'w') as f:
    f.write(prefix + '[\n' + ',\n'.join(lines) + '\n]' + suffix)

print(f"\nDone! Updated: {count}")
