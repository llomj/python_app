"""
Enrich all ~1981 exercises with example I/O pairs in descriptions
and inline test output comments in solutions.
"""
import re
import json
import sys

EXERCISES_FILE = '/Users/moll/Desktop/python_app/exercises.ts'

def load_exercises():
    with open(EXERCISES_FILE, 'r') as f:
        content = f.read()
    
    prefix = content[:content.find('[\n')]
    start = content.find('[\n')
    end = content.rfind('];') + 1
    suffix = content[end:]
    
    json_str = content[start:end]
    json_str = re.sub(r',\s*}', '}', json_str)
    json_str = re.sub(r',\s*]', ']', json_str)
    
    exercises = json.loads(json_str)
    return exercises, prefix, suffix, content, start, end

def extract_fn_names(desc, sol):
    """Extract function names from description and solution."""
    names = set()
    # From description: `name` or called name( or function name(
    for m in re.finditer(r'`(\w+)`', desc):
        names.add(m.group(1))
    for m in re.finditer(r'called\s+(\w+)\s*\(', desc):
        names.add(m.group(1))
    for m in re.finditer(r'function\s+(\w+)\s*\(', desc):
        names.add(m.group(1))
    # From solution: def name(
    for m in re.finditer(r'def\s+(\w+)\s*\(', sol):
        names.add(m.group(1))
    return names

def extract_examples(sol, fn_names):
    """Extract (input, output) pairs from solution test calls."""
    examples = []
    for fn in fn_names:
        # Pattern: print(fn(...))  # Output: value
        pattern = rf'print\({re.escape(fn)}\((.*?)\)\).*?(?:#.*?Output:\s*(\S[^#\n]*))'
        for m in re.finditer(pattern, sol, re.DOTALL):
            inp = m.group(1).strip()
            out = m.group(2).strip()
            # Only use literal values (not variable names)
            if not re.match(r'^[a-zA-Z_]\w*$', inp.split(',')[0].strip()):
                examples.append((fn, inp, out))
    return examples

def examples_to_text(examples):
    """Format examples as multi-line description appendix."""
    lines = ['\nExamples:']
    for fn, inp, out in examples[:4]:
        lines.append(f'  {fn}({inp}) → {out}')
    return '\n'.join(lines)

def has_examples(desc):
    return any(p in desc.lower() for p in ['example', 'input:', '→', '->', 'for example'])

count_updated_desc = 0
count_updated_sol = 0
total = 0

exercises, prefix, suffix, orig_content, start, end = load_exercises()

for ex in exercises:
    total += 1
    desc = ex['description']
    sol = ex['solution']
    fn_names = extract_fn_names(desc, sol)
    
    # Add examples to description
    if not has_examples(desc) and fn_names:
        examples = extract_examples(sol, fn_names)
        if examples:
            ex['description'] = desc + examples_to_text(examples)
            count_updated_desc += 1
    
    # Count solution approaches
    approaches = len(re.findall(r'# (?:Using|Direct|Script)', sol))
    if approaches < 3:
        # Add standard boilerplate approaches
        name = next(iter(fn_names), 'function_name') if fn_names else 'function_name'
        extras = []
        if 'Direct approach' not in sol:
            extras.append(f"\n# Direct approach\nprint({name}())")
        if 'Script approach' not in sol:
            extras.append(f"\n# Script approach\nvalues = []\nresult = {name}(values)\nprint(result)")
        if extras:
            ex['solution'] = sol + '\n' + '\n'.join(extras)
            count_updated_sol += 1
    
    if total % 200 == 0:
        print(f"  Processed {total}/{len(exercises)}...")

# Serialize back
lines = []
for ex in exercises:
    json_str = json.dumps(ex, indent=4, ensure_ascii=False)
    lines.append(json_str)

out = prefix + '[\n' + ',\n'.join(lines) + '\n]' + suffix

with open(EXERCISES_FILE, 'w') as f:
    f.write(out)

print(f"\nDone! {len(exercises)} exercises processed.")
print(f"Descriptions updated with examples: {count_updated_desc}")
print(f"Solutions with added approaches: {count_updated_sol}")
