"""
Fifth pass: catch remaining with '# Expected:' (without 'output') comments,
and fix missing 'import re' in first script blocks.
"""
import re, json, tempfile, os, io, contextlib, threading

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
            outdir = tempfile.mkdtemp()
            old_cwd = os.getcwd()
            os.chdir(outdir)
            ns = {'__builtins__': __builtins__}
            with contextlib.redirect_stdout(stdout):
                exec(code, ns)
            os.chdir(old_cwd)
        except:
            try: os.chdir(old_cwd)
            except: pass
    t = threading.Thread(target=run)
    t.daemon = True; t.start(); t.join(timeout)
    return stdout.getvalue().strip()

def maybe_exists(desc):
    return any(p in desc.lower() for p in ['example', 'input:', '\u2192', '->', 'for example'])

def extract_first_script(sol):
    sections = re.split(r'\n# (?:Alternative|Using|Direct|Script|Approach|Built-in|Wrapped)\s', sol)
    first = sections[0].strip()
    if not first: return None
    lines = [l for l in first.split('\n') if l.strip() and not l.strip().startswith('#')]
    if not lines and len(sections) > 1:
        first = sections[1].strip()
    # Ensure import re is present if not already
    if 're.' in first and 'import re' not in first:
        if not first.startswith('import re'):
            first = 'import re\n' + first
    return first

def extract_solve_call(sol):
    for name in ['solve', 'main']:
        m = re.search(r'def\s+' + re.escape(name) + r'\s*\(\s*\)', sol)
        if m:
            idx = m.start()
            block = sol[idx:]
            end = re.search(r'\n(?=def\s|class\s|#\s*(?:Alternative|Using|Direct|Script|Approach|Wrapped)\s)', block)
            if end: block = block[:end.start()]
            lines = block.split('\n')
            result = [lines[0]]
            for line in lines[1:]:
                if line.startswith(' ') or line.startswith('\t') or line.strip() == '':
                    result.append(line)
                else:
                    break
            return '\n'.join(result) + f'\n\n{name}()'
    return None

count_updated = 0

for i, ex in enumerate(exercises):
    if maybe_exists(ex['description']): continue
    
    sol = ex['solution']
    desc = ex['description']
    output = None
    
    # Strategy 1: first script (with import re fix and temp dir)
    script = extract_first_script(sol)
    if script and 'input(' not in script and 'import random' not in script and 'from random' not in script:
        output = safe_exec(script, timeout=3)
    
    # Strategy 2: solve() call
    if not output:
        solve_code = extract_solve_call(sol)
        if solve_code and 'input(' not in solve_code and 'import random' not in solve_code and 'from random' not in solve_code:
            # Ensure import re
            if 're.' in solve_code and 'import re' not in solve_code:
                solve_code = 'import re\n' + solve_code
            output = safe_exec(solve_code, timeout=3)
    
    # Strategy 3: extract from # Expected: comments (without "output")
    if not output:
        expected = re.findall(r'# [Ee]xpected:?\s*(.*?)$', sol, re.MULTILINE)
        if expected:
            exp = expected[0].strip()
            if not exp.lower().startswith('a random'):
                # Find a print() call with function call as context
                fn_call = None
                prints = re.findall(r'print\((\w+\([^)]*\))\)', sol)
                if prints: fn_call = prints[0]
                if fn_call:
                    output = f"{fn_call}  →  {exp}"
                else:
                    output = exp
    
    if output and len(output.strip()) > 0:
        ex_lines = ['', 'Examples:']
        ex_lines.append(f'  {output}')
        ex['description'] = desc + '\n'.join(ex_lines)
        count_updated += 1
    
    if (i+1) % 300 == 0:
        pass

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
with open(EXERCISES_FILE, 'r') as f:
    c = f.read()
s = c.find('[\n'); e = c.rfind('];') + 1
js = c[s:e]
js = re.sub(r',\s*}', '}', js)
js = re.sub(r',\s*]', ']', js)
loaded = json.loads(js)
has = sum(1 for ex in loaded if any(p in ex['description'].lower() for p in ['example', 'input:', '\u2192', '->', 'for example']))
print(f"\nUpdated {count_updated} this pass.")
print(f"Final: {has}/{len(loaded)} have examples ({(100*has/len(loaded)):.0f}%)")
print(f"Missing: {[ex['id'] for ex in loaded if not any(p in ex['description'].lower() for p in ['example', 'input:', '\u2192', '->', 'for example'])]}")
