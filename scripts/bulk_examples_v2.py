"""
Second pass: fix the 558 problems that still lack examples.
Handles: no-function scripts, OOP, multi-param, solve()-style.
"""
import re, json, io, contextlib, threading, traceback

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

def extract_fn_from_code_or_sol(init, sol):
    m = re.search(r'def\s+(\w+)\s*\(', init)
    if m: return m.group(1)
    for fn in re.findall(r'def\s+(\w+)\s*\(', sol):
        if not fn.startswith('_') and fn != 'print_square':
            return fn
    m = re.search(r'def\s+(\w+)\s*\(', sol)
    if m: return m.group(1)
    return None

def extract_func_block(sol, fn_name):
    for try_name in [fn_name, fn_name.rstrip('s'), fn_name + 's']:
        idx = sol.find(f'def {try_name}(')
        if idx != -1: break
    else:
        for m in re.finditer(r'def\s+\w+\s*\(', sol):
            base = m.group(0).replace('def ', '').replace('(', '').strip()
            if base in fn_name or fn_name in base:
                idx = m.start()
                break
        else:
            return None
    block = sol[idx:]
    end = re.search(r'\n(?=def\s|class\s|#\s*(?:Using|Direct|Script|Approach)\s)', block)
    if end: block = block[:end.start()]
    lines = block.strip().split('\n')
    if not lines: return None
    result = [lines[0]]
    for line in lines[1:]:
        if line.startswith(' ') or line.startswith('\t') or line.strip() == '':
            result.append(line)
        else:
            break
    return '\n'.join(result)

def maybe_exists(desc):
    return any(p in desc.lower() for p in ['example', 'input:', '→', '->', 'for example'])

def guess_type(p, desc):
    p = p.split(':')[0].strip()
    if p in ('self','cls','*args','**kwargs'): return None
    if p in ('str','string','name','text','word','sentence','char','character','filename','file','path','msg','message'): return 'str'
    if p in ('num','int','count','n','index','idx','number','size','length','value','val'): return 'int'
    if any(w in desc.lower() for w in ['list of','array of','collection','multiple']): return 'list'
    if p.endswith('s') and p not in ('class','this','status','process','address','success','radius'): return 'list'
    return 'int'

def generate_args(fn_name, func_block, desc):
    m = re.search(r'def\s+' + re.escape(fn_name) + r'\s*\(([^)]*)\)', func_block)
    if not m:
        for m2 in re.finditer(r'def\s+(\w+)\s*\(([^)]*)\)', func_block):
            if m2.group(1) == fn_name:
                m = m2; break
    if not m: return None, None
    params_str = m.group(1) if m.lastindex == 1 else m.group(2)
    if not params_str: return None, None
    params = [p.strip() for p in params_str.split(',') if p.strip()]
    types = []
    for p in params:
        t = guess_type(p, desc)
        if t: types.append(t)
    if not types: return None, None
    samples = [
        {'str': "'hello'", 'int': '5', 'list': '[1, 2, 3]'},
        {'str': "'world'", 'int': '3', 'list': '[5, 8, 2]'},
        {'str': "'python'", 'int': '10', 'list': '[3, 1, 4]'},
    ]
    args_list = [', '.join(samples[i][t] for t in types) for i in range(3)]
    return fn_name, args_list

def oop_examples(sol, desc):
    cls_m = re.search(r'class\s+(\w+)', sol)
    if not cls_m: return None
    cls_name = cls_m.group(1)
    methods = [m for m in re.findall(r'def\s+(\w+)\s*\(', sol) if not m.startswith('_')]
    if not methods: return None
    method = methods[0]
    
    init_m = re.search(r'def\s+__init__\s*\(([^)]*)\)', sol)
    init_samples = []
    if init_m:
        params = [p.strip() for p in init_m.group(1).split(',') if p.strip()]
        params = [p for p in params if p not in ('self',)]
        if params:
            types = [guess_type(p, desc) for p in params]
            samples = [
                {'str': "'hello'", 'int': '5', 'list': '[1, 2, 3]'},
                {'str': "'world'", 'int': '3', 'list': '[5, 8, 2]'},
                {'str': "'python'", 'int': '10', 'list': '[3, 1, 4]'},
            ]
            init_samples = [', '.join(samples[i][t] for t in types) for i in range(3)]
    
    mparams_m = re.search(r'def\s+' + re.escape(method) + r'\s*\(([^)]*)\)', sol)
    method_samples = ['', '', '']
    if mparams_m:
        params = [p.strip() for p in mparams_m.group(1).split(',') if p.strip()]
        params = [p for p in params if p not in ('self',)]
        if params:
            types = [guess_type(p, desc) for p in params]
            samples = [
                {'str': "'hello'", 'int': '5', 'list': '[1, 2, 3]'},
                {'str': "'world'", 'int': '3', 'list': '[5, 8, 2]'},
                {'str': "'python'", 'int': '10', 'list': '[3, 1, 4]'},
            ]
            method_samples = [', '.join(samples[i][t] for t in types) for i in range(3)]
    
    test_lines = []
    for i in range(3):
        if i < len(init_samples) and init_samples[i]:
            test_lines.append(f"obj = {cls_name}({init_samples[i]})")
        else:
            test_lines.append(f"obj = {cls_name}()")
        if method_samples[i]:
            test_lines.append(f"print(obj.{method}({method_samples[i]}))")
        else:
            test_lines.append(f"print(obj.{method}())")
    
    idx = sol.find(f'class {cls_name}')
    if idx == -1: return None
    class_block = sol[idx:]
    end = re.search(r'\n(?=class\s|def\s|#\s*(?:Using|Direct|Script|Approach)\s)', class_block)
    if end: class_block = class_block[:end.start()]
    return class_block.strip(), '\n'.join(test_lines)

count_updated = 0

for i, ex in enumerate(exercises):
    if maybe_exists(ex['description']): continue
    
    desc = ex['description']
    sol = ex['solution']
    init = ex['initialCode']
    
    # Strategy 1: extract function
    fn = extract_fn_from_code_or_sol(init, sol)
    if fn:
        try:
            func_block = extract_func_block(sol, fn)
            if func_block:
                real_fn, args_list = generate_args(fn, func_block, desc)
                if real_fn and args_list:
                    test_calls = '\n'.join(f'print({real_fn}({args}))' for args in args_list)
                    runnable = func_block + '\n\n' + test_calls
                    stdout = safe_exec(runnable, timeout=3)
                    
                    ex_lines = ['', 'Examples:']
                    for j, args in enumerate(args_list):
                        out = stdout.split('\n')[j].strip() if stdout else '?'
                        ex_lines.append(f'  {real_fn}({args}) → {out}')
                    ex['description'] = desc + '\n'.join(ex_lines)
                    count_updated += 1
                    continue
        except Exception as e:
            pass
    
    # Strategy 2: OOP
    try:
        oop = oop_examples(sol, desc)
        if oop:
            class_block, test_code = oop
            runnable = class_block + '\n\n' + test_code
            stdout = safe_exec(runnable, timeout=3)
            ex_lines = ['', 'Examples:']
            out_lines = stdout.split('\n') if stdout else ['?', '?', '?']
            for j in range(3):
                out = out_lines[j].strip() if j < len(out_lines) else '?'
                ex_lines.append(f'  → {out}')
            if '?' not in ex_lines[-1]:
                ex['description'] = desc + '\n'.join(ex_lines)
                count_updated += 1
                continue
    except Exception as e:
        pass
    
    if (i+1) % 300 == 0:
        print(f"  progress: {i+1}/{len(exercises)}, updated: {count_updated}")

print(f"\nSecond pass complete! Updated {count_updated} more.")

# Final write
lines = []
for ex in exercises:
    obj_str = json.dumps(ex, indent=4, ensure_ascii=False)
    obj_lines = obj_str.split('\n')
    fixed = ['    ' + l if l.startswith('{') or l.startswith('}') else '        ' + l for l in obj_lines]
    lines.append('\n'.join(fixed))

with open(EXERCISES_FILE, 'w') as f:
    f.write(prefix + '[\n' + ',\n'.join(lines) + '\n]' + suffix)

print("File written.")
