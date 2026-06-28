"""
Add example I/O pairs to ALL problem descriptions by executing function code directly.
"""
import re
import json
import sys
import signal

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
    """Execute Python code with timeout and capture stdout."""
    import io, contextlib
    stdout = io.StringIO()
    result = []
    
    def run():
        try:
            with contextlib.redirect_stdout(stdout):
                exec(code, {'__builtins__': __builtins__})
        except:
            pass
    
    import threading
    t = threading.Thread(target=run)
    t.daemon = True
    t.start()
    t.join(timeout)
    return stdout.getvalue().strip()

def extract_fn(code, desc):
    m = re.search(r'def\s+(\w+)\s*\(', code)
    if m: return m.group(1)
    m = re.search(r'`(\w+)`', desc)
    if m: return m.group(1)
    return None

def extract_pure_func(sol, fn_name):
    idx = sol.find(f'def {fn_name}(')
    if idx == -1: return None
    block = sol[idx:]
    end = re.search(r'\n(?=def\s+|#\s*(?:Using|Direct|Script)\s|\n)', block)
    if end: block = block[:end.start()]
    lines = block.split('\n')
    result = [lines[0]]
    for line in lines[1:]:
        if line.startswith(' ') or line.startswith('\t') or line.strip() == '':
            result.append(line)
        else:
            break
    return '\n'.join(result)

def guess_type(param_name, desc):
    p = param_name.split(':')[0].strip()
    if p in ('self','cls','*args','**kwargs'): return None
    if p in ('str','string','name','text','word','sentence','char','character','filename','file','path','msg','message'): return 'str'
    if p in ('num','int','count','n','index','idx','number','size','length','value','val'): return 'int'
    if p in ('lst','list','arr','array','items','numbers','elements','collection','number'): return 'list'
    d = desc.lower()
    if any(w in d for w in ['string','text','word','character','sentence','name','greeting']): return 'str'
    if any(w in d for w in ['list of','array of','collection','multiple']): return 'list'
    if any(w in d for w in ['number','integer','numeric','digit','count']): return 'int'
    if p.endswith('s') and p not in ('class','this','status','process','address','success'): return 'list'
    return 'int'

def infer_args(fn_name, func_block, desc):
    m = re.search(r'def\s+' + re.escape(fn_name) + r'\s*\(([^)]*)\)', func_block)
    if not m: return []
    params = [p.strip() for p in m.group(1).split(',') if p.strip()]
    types = [t for p in params if (t := guess_type(p, desc))]
    samples = [
        {'str': "'hello'", 'int': '5', 'list': '[1, 2, 3]'},
        {'str': "'world'", 'int': '3', 'list': '[5, 8, 2]'},
        {'str': "'python'", 'int': '10', 'list': '[3, 1, 4]'},
    ]
    return [', '.join(samples[i][t] for t in types) for i in range(3)]

count_updated = 0

for i, ex in enumerate(exercises):
    desc = ex['description']
    sol = ex['solution']
    code = ex['initialCode']
    
    if any(p in desc.lower() for p in ['example', 'input:', '→', '->', 'for example']):
        continue
    
    fn = extract_fn(code, desc)
    if not fn: continue
    
    func_block = extract_pure_func(sol, fn)
    if not func_block: continue
    
    args_list = infer_args(fn, func_block, desc)
    if not args_list: continue
    
    test_calls = '\n'.join(f'print({fn}({args}))' for args in args_list)
    runnable = func_block + '\n\n' + test_calls
    stdout = safe_exec(runnable, timeout=3)
    
    ex_lines = ['', 'Examples:']
    for j, args in enumerate(args_list):
        if stdout:
            outputs = stdout.split('\n')
            out = outputs[j].strip() if j < len(outputs) else '?'
        else:
            out = '?'
        ex_lines.append(f'  {fn}({args}) → {out}')
    
    ex['description'] = desc + '\n'.join(ex_lines)
    count_updated += 1
    
    if (i+1) % 200 == 0:
        print(f"  {i+1}/{len(exercises)} - updated: {count_updated}")

# Write back
lines = []
for ex in exercises:
    obj_str = json.dumps(ex, indent=4, ensure_ascii=False)
    obj_lines = obj_str.split('\n')
    fixed = ['    ' + l if l.startswith('{') or l.startswith('}') else '        ' + l for l in obj_lines]
    lines.append('\n'.join(fixed))

with open(EXERCISES_FILE, 'w') as f:
    f.write(prefix + '[\n' + ',\n'.join(lines) + '\n]' + suffix)

print(f"\nDone! Updated {count_updated} descriptions with computed examples.")
