"""
Third pass: handle script-style problems (no function args).
Run the first solution block as a script and capture full output as example.
"""
import re, json, io, contextlib, threading, textwrap

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

def safe_exec(code, timeout=3):
    stdout = io.StringIO()
    def run():
        try:
            with contextlib.redirect_stdout(stdout):
                exec(code, {'__builtins__': __builtins__})
        except: pass
    t = threading.Thread(target=run)
    t.daemon = True; t.start(); t.join(timeout)
    return stdout.getvalue().strip()

def maybe_exists(desc):
    return any(p in desc.lower() for p in ['example', 'input:', '\u2192', '->', 'for example'])

def extract_first_script(sol):
    """Get the first solution block (before any # Alternative or # Using section)."""
    # Remove section headers, keep first script block
    sections = re.split(r'\n# (?:Alternative|Using|Direct|Script|Approach|Built-in)\s', sol)
    first = sections[0].strip()
    if not first:
        return None
    # If first section is just comments, try next
    lines = [l for l in first.split('\n') if l.strip() and not l.strip().startswith('#')]
    if not lines and len(sections) > 1:
        first = sections[1].strip()
    return first

def extract_solve_call(sol):
    """Find a def solve(): or def main(): and extract it + call it."""
    for name in ['solve', 'main']:
        m = re.search(r'def\s+' + re.escape(name) + r'\s*\(\s*\)', sol)
        if m:
            # Extract the function block
            idx = m.start()
            block = sol[idx:]
            end = re.search(r'\n(?=def\s|class\s|#\s*(?:Alternative|Using|Direct|Script|Approach)\s)', block)
            if end: block = block[:end.start()]
            # Trim to just the def block
            lines = block.split('\n')
            result = [lines[0]]
            for line in lines[1:]:
                if line.startswith(' ') or line.startswith('\t') or line.strip() == '':
                    result.append(line)
                else:
                    break
            func_block = '\n'.join(result)
            return func_block + f'\n\n{name}()'
    return None

count_updated = 0

for i, ex in enumerate(exercises):
    if maybe_exists(ex['description']): continue
    
    sol = ex['solution']
    desc = ex['description']
    output = None
    
    # Strategy 1: run as standalone script (first block)
    script = extract_first_script(sol)
    if script:
        # Check if script has input() or random - skip those
        if 'input(' not in script and 'import random' not in script and 'from random' not in script:
            output = safe_exec(script, timeout=3)
    
    # Strategy 2: call solve()/main()
    if not output:
        solve_code = extract_solve_call(sol)
        if solve_code:
            if 'input(' not in solve_code and 'import random' not in solve_code and 'from random' not in solve_code:
                output = safe_exec(solve_code, timeout=3)
    
    if output and len(output.strip()) > 0:  # Must have real output
        # Truncate very long output
        if len(output) > 200:
            output = output[:197] + '...'
        ex['description'] = desc + f'\n\nExample output:\n{output}'
        count_updated += 1
    
    if (i+1) % 300 == 0:
        print(f"  progress: {i+1}/{len(exercises)}, updated: {count_updated}")

print(f"\nThird pass: updated {count_updated} script-style problems.")

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
final_ex = lambda d: any(p in d.lower() for p in ['example', 'input:', '\u2192', '->', 'for example'])
loaded = json.loads(re.sub(r',\s*}', '}', re.sub(r',\s*]', ']', open(EXERCISES_FILE).read()[open(EXERCISES_FILE).read().find('[\n'):open(EXERCISES_FILE).read().rfind('];')+1])))
has = sum(1 for ex in loaded if final_ex(ex['description']))
print(f"\nFinal: {has}/{len(loaded)} have examples ({(100*has/len(loaded)):.0f}%)")
