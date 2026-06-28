"""
Fourth pass: extract expected output from '# Expected output:' comments in solutions.
No code execution needed — works for file ops, missing imports, etc.
"""
import re, json

EXERCISES_FILE = '/Users/moll/Desktop/python_app/exercises.ts'

def load():
    with open(EXERCISES_FILE, 'r') as f:
        c = f.read()
    s = c.find('[\n')
    e = c.rfind('];') + 1
    json_str = c[s:e]
    json_str = re.sub(r',\s*}', '}', json_str)
    json_str = re.sub(r',\s*]', ']', json_str)
    return json.loads(json_str), c[:s], c[e:]

exercises, prefix, suffix = load()
print(f"Loaded {len(exercises)} exercises")

def maybe_exists(desc):
    return any(p in desc.lower() for p in ['example', 'input:', '\u2192', '->', 'for example'])

count_updated = 0

for ex in exercises:
    if maybe_exists(ex['description']): continue
    
    sol = ex['solution']
    desc = ex['description']
    
    # Find all Expected output comments
    expected_matches = re.findall(r'# [Ee]xpected output:?\s*(.*?)$', sol, re.MULTILINE)
    if not expected_matches:
        # Also check for "# Output:" comments
        expected_matches = re.findall(r'# Output:\s*(.*?)$', sol, re.MULTILINE)
    if not expected_matches:
        continue
    
    expected = expected_matches[0].strip()
    # Skip random-output descriptions
    if expected.lower().startswith('a random'):
        continue
    
    # Look for a function call in the solution context to use as the example call
    fn_call = None
    # Find print() calls that show inputs
    print_matches = re.findall(r'print\((\w+\([^)]*\))\)', sol)
    if print_matches:
        fn_call = print_matches[0]
    
    # Look for direct function calls without print
    if not fn_call:
        call_matches = re.findall(r'\b(\w+\([^)]*\))\s*#', sol)
        for cm in call_matches:
            if cm.startswith('print('): continue
            fn_call = cm
            break
    
    # Build examples section
    ex_lines = ['', 'Examples:']
    if fn_call:
        ex_lines.append(f'  {fn_call}  →  {expected}')
    else:
        ex_lines.append(f'  →  {expected}')
    
    ex['description'] = desc + '\n'.join(ex_lines)
    count_updated += 1
    
    if count_updated % 30 == 0:
        print(f"  updated: {count_updated}")

# Write back
lines = []
for ex in exercises:
    obj_str = json.dumps(ex, indent=4, ensure_ascii=False)
    obj_lines = obj_str.split('\n')
    fixed = ['    ' + l if l.startswith('{') or l.startswith('}') else '        ' + l for l in obj_lines]
    lines.append('\n'.join(fixed))

with open(EXERCISES_FILE, 'w') as f:
    f.write(prefix + '[\n' + ',\n'.join(lines) + '\n]' + suffix)

# Final count
loaded = json.loads(re.sub(r',\s*}', '}', re.sub(r',\s*]', ']', open(EXERCISES_FILE).read())))
has = sum(1 for ex in loaded if any(p in ex['description'].lower() for p in ['example', 'input:', '\u2192', '->', 'for example']))
print(f"\nDone! Updated {count_updated} descriptions this pass.")
print(f"Final: {has}/{len(loaded)} have examples ({(100*has/len(loaded)):.0f}%)")
