#!/usr/bin/env python3
"""Conservative batch alternative generator for exercises.ts."""

import re
import sys
import ast
from pathlib import Path

TS_FILE = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('/Users/moll/Desktop/python_app/exercises.ts')
BATCH_START = int(sys.argv[2]) if len(sys.argv) > 2 else 1
BATCH_END = int(sys.argv[3]) if len(sys.argv) > 3 else 50
REPORT_FILE = Path(sys.argv[4]) if len(sys.argv) > 4 else Path('/tmp/batch_report.md')
DRY_RUN = '--dry-run' in sys.argv

HEADING_PREFIXES = (
    '# Alternative', '# Using ', '# Try ', '# Modify ', '# Consider ',
    '# Equivalent ', '# Convert ', '# Another ',
)


def unescape_ts(s):
    return (s.replace('\\\\', '\\')
             .replace('\\"', '"')
             .replace("\\'", "'")
             .replace('\\n', '\n'))


def escape_ts(s):
    s = s.replace('\\', '\\\\')
    s = s.replace('\n', '\\n')
    s = s.replace('"', "'")
    return s


def find_solution_end(text, start_pos):
    i = start_pos
    while i < len(text):
        if text[i] == '\\' and i + 1 < len(text):
            i += 2
        elif text[i] == '"' and i + 1 < len(text) and text[i + 1] == ',':
            return i
        else:
            i += 1
    return -1


def is_heading(line):
    if line.startswith(' ') or line.startswith('\t'):
        return False
    s = line.strip()
    if not s.startswith('#'):
        return False
    # Aggressive heading detection for alternative/placeholder sections
    heading_keywords = [
        'alternative', 'adding', 'wrapped', 'example usage', 'expected output',
        'expected:', 'note:', 'warning:', 'same logic', 'inline version',
        'check condition', 'manual ', 'using ', 'modify ', 'try ',
        'different variable names', 'rewrite with', 'implement as',
        'return instead of print', 'return value instead of printing',
        'intermediate variable', 'alternative approach', 'another approach',
    ]
    s_lower = s.lower()
    return any(kw in s_lower for kw in heading_keywords)


def next_non_blank(lines, start):
    for i in range(start + 1, len(lines)):
        if lines[i].strip():
            return i, lines[i]
    return None, ''


def strip_broken_tail(code):
    lines = code.split('\n')
    cutoff = len(lines)
    for i, l in enumerate(lines):
        if is_heading(l):
            idx, nxt = next_non_blank(lines, i)
            if idx is None:
                cutoff = i
                break
            if nxt.startswith('def ') or nxt.startswith('class '):
                continue
            if nxt.startswith(' ') or nxt.startswith('\t'):
                stripped = nxt.strip()
                if not (stripped.startswith('#') or stripped.startswith('"""') or stripped.startswith("''")):
                    cutoff = i
                    break
    while cutoff > 0 and not lines[cutoff - 1].strip():
        cutoff -= 1
    return '\n'.join(lines[:cutoff])


def strip_inline_comment(expr):
    in_str = None
    i = 0
    while i < len(expr):
        ch = expr[i]
        if in_str:
            if ch == '\\' and i + 1 < len(expr):
                i += 2
                continue
            if ch == in_str:
                in_str = None
        elif ch in ('"', "'"):
            in_str = ch
        elif ch == '#':
            return expr[:i].rstrip()
        i += 1
    return expr.rstrip()


def extract_first_func(code):
    lines = code.split('\n')
    start_idx = None
    for i, l in enumerate(lines):
        if l.startswith('def ') or l.startswith('class '):
            start_idx = i
            break
    if start_idx is None:
        return None
    block = [lines[start_idx]]
    for l in lines[start_idx + 1:]:
        stripped = l.strip()
        if not stripped:
            block.append(l)
        elif l.startswith(' ') or l.startswith('\t') or stripped.startswith('#'):
            block.append(l)
        else:
            break
    while block and not block[-1].strip():
        block.pop()
    return '\n'.join(block)


def get_signature(func_code):
    m = re.match(r'def\s+(\w+)\s*\((.*?)\)\s*(?:->\s*[^:]+)?\s*:', func_code, re.DOTALL)
    if m:
        return m.group(1), m.group(2)
    return None, None


def get_param_names(params):
    parts = []
    depth = 0
    cur = ''
    for ch in params:
        if ch in '([{':
            depth += 1
            cur += ch
        elif ch in ')]}':
            depth -= 1
            cur += ch
        elif ch == ',' and depth == 0:
            parts.append(cur.strip())
            cur = ''
        else:
            cur += ch
    if cur.strip():
        parts.append(cur.strip())
    names = []
    for p in parts:
        p = p.split('=')[0].split(':')[0].strip()
        if p and p != 'self':
            names.append(p)
    return names


def compile_check(code):
    try:
        ast.parse(code)
        return True
    except SyntaxError:
        return False


# ---------------------------------------------------------------------------
# Pattern generators
# ---------------------------------------------------------------------------

def gen_arithmetic_alts(fname, params, left, op, right):
    if op == '+':
        return [
            f'def {fname}({params}):\n    return sum([{left}, {right}])',
            f'def {fname}({params}):\n    import operator\n    return operator.add({left}, {right})',
        ]
    if op == '-':
        return [
            f'def {fname}({params}):\n    return {left} + (-{right})',
            f'def {fname}({params}):\n    import operator\n    return operator.sub({left}, {right})',
        ]
    if op == '*':
        return [
            f'def {fname}({params}):\n    result = 0\n    for _ in range({right}):\n        result += {left}\n    return result',
            f'def {fname}({params}):\n    return pow({left}, {right})',
        ]
    if op == '/':
        return [
            f'def {fname}({params}):\n    return {left} * (1 / {right})',
            f'def {fname}({params}):\n    from fractions import Fraction\n    return float(Fraction({left}, {right}))',
        ]
    if op == '%':
        return [
            f'def {fname}({params}):\n    return {left} - ({right} * ({left} // {right}))',
            f'def {fname}({params}):\n    return divmod({left}, {right})[1]',
        ]
    return []


def gen_from_return(fname, params, ret_expr, param_names):
    alts = []

    # String concatenation heuristic
    m = re.match(r'^(\w+)\s*\+\s*(\w+)$', ret_expr)
    if m and not alts:
        left, right = m.groups()
        stringy = ('string', 'str', 'text', 'word', 'char', 'name', 'prefix', 'suffix')
        if any(s in left.lower() or s in right.lower() or s in fname.lower() for s in stringy):
            alts = [
                f'def {fname}({params}):\n    return "".join([{left}, {right}])',
                f'def {fname}({params}):\n    return "%s%s" % ({left}, {right})',
            ]

    # Arithmetic
    m = re.match(r'^(\w+)\s*([+\-*/%])\s*(\w+)$', ret_expr)
    if m and not alts:
        alts = gen_arithmetic_alts(fname, params, *m.groups())

    # Power
    m = re.match(r'^(\w+)\s*\*\*\s*(\w+)$', ret_expr)
    if m and not alts:
        left, right = m.groups()
        alts = [
            f'def {fname}({params}):\n    return pow({left}, {right})',
            f'def {fname}({params}):\n    import math\n    return math.pow({left}, {right})',
        ]

    # Comparison
    m = re.match(r'^(\w+)\s*(==|!=|>|<|>=|<=)\s*(\w+)$', ret_expr)
    if m and not alts:
        left, op, right = m.groups()
        inverse = {'>': '<=', '<': '>=', '>=': '<', '<=': '>', '!=': '=='}.get(op)
        alt1 = f'def {fname}({params}):\n    if {left} {op} {right}:\n        return True\n    return False'
        alt2 = f'def {fname}({params}):\n    return not ({left} {inverse} {right})' if inverse else f'def {fname}({params}):\n    return ({left} {op} {right})'
        alts = [alt1, alt2]

    # len
    m = re.match(r'^len\s*\((\w+)\)$', ret_expr)
    if m and not alts:
        var = m.group(1)
        alts = [
            f'def {fname}({params}):\n    count = 0\n    for _ in {var}:\n        count += 1\n    return count',
            f'def {fname}({params}):\n    return sum(1 for _ in {var})',
        ]

    # max/min
    m = re.match(r'^(max|min)\s*\((\w+)\)$', ret_expr)
    if m and not alts:
        func, var = m.groups()
        if func == 'max':
            alts = [
                f'def {fname}({params}):\n    return sorted({var})[-1]',
                f'def {fname}({params}):\n    result = {var}[0]\n    for item in {var}:\n        if item > result:\n            result = item\n    return result',
            ]
        else:
            alts = [
                f'def {fname}({params}):\n    return sorted({var})[0]',
                f'def {fname}({params}):\n    result = {var}[0]\n    for item in {var}:\n        if item < result:\n            result = item\n    return result',
            ]

    # sum
    m = re.match(r'^sum\s*\((\w+)\)$', ret_expr)
    if m and not alts:
        var = m.group(1)
        alts = [
            f'def {fname}({params}):\n    total = 0\n    for item in {var}:\n        total += item\n    return total',
            f'def {fname}({params}):\n    from functools import reduce\n    import operator\n    return reduce(operator.add, {var}, 0)',
        ]

    # sorted
    m = re.match(r'^sorted\s*\((\w+)\)$', ret_expr)
    if m and not alts:
        var = m.group(1)
        alts = [
            f'def {fname}({params}):\n    copy = {var}.copy()\n    copy.sort()\n    return copy',
            f'def {fname}({params}):\n    return sorted({var}, reverse=False)',
        ]

    # average: sum(x) / len(x)
    m = re.match(r'^sum\s*\((\w+)\)\s*/\s*len\s*\((\w+)\)$', ret_expr)
    if m and not alts and m.group(1) == m.group(2):
        var = m.group(1)
        alts = [
            f'def {fname}({params}):\n    return sum({var}) / len({var})',
            f'def {fname}({params}):\n    total = 0\n    count = 0\n    for item in {var}:\n        total += item\n        count += 1\n    return total / count if count else 0',
        ]

    # reverse string
    m = re.match(r'^(\w+)\[::-1\]$', ret_expr)
    if m and not alts:
        var = m.group(1)
        alts = [
            f'def {fname}({params}):\n    return "".join(reversed({var}))',
            f'def {fname}({params}):\n    result = ""\n    for char in {var}:\n        result = char + result\n    return result',
        ]

    # string upper/lower
    m = re.match(r'^(\w+)\.(upper|lower|title|capitalize|swapcase)\s*\(\s*\)$', ret_expr)
    if m and not alts:
        var, method = m.groups()
        if method == 'upper':
            alts = [
                f"def {fname}({params}):\n    return ''.join(chr(ord(c) - 32) if 'a' <= c <= 'z' else c for c in {var})",
                f'def {fname}({params}):\n    return str({var}).upper()',
            ]
        elif method == 'lower':
            alts = [
                f"def {fname}({params}):\n    return ''.join(chr(ord(c) + 32) if 'A' <= c <= 'Z' else c for c in {var})",
                f'def {fname}({params}):\n    return str({var}).lower()',
            ]
        else:
            alts = [
                f'def {fname}({params}):\n    return {var}.{method}()',
                f'def {fname}({params}):\n    return str({var}).{method}()',
            ]

    # split
    m = re.match(r'^(\w+)\.split\s*\(\s*\)$', ret_expr)
    if m and not alts:
        var = m.group(1)
        alts = [
            f'def {fname}({params}):\n    import re\n    return re.split(r"\\s+", {var}.strip())',
            f'def {fname}({params}):\n    return {var}.split(" ")',
        ]

    # count
    m = re.match(r'^(\w+)\.count\s*\((.+?)\)$', ret_expr)
    if m and not alts:
        var, elem = m.groups()
        alts = [
            f'def {fname}({params}):\n    return sum(1 for c in {var} if c == {elem})',
            f'def {fname}({params}):\n    count = 0\n    for c in {var}:\n        if c == {elem}:\n            count += 1\n    return count',
        ]

    # membership
    m = re.match(r'^(\w+)\s+in\s+(\w+)$', ret_expr)
    if m and not alts:
        item, container = m.groups()
        alts = [
            f'def {fname}({params}):\n    for element in {container}:\n        if element == {item}:\n            return True\n    return False',
            f'def {fname}({params}):\n    return any(element == {item} for element in {container})',
        ]

    # f-string -> .format() and % formatting
    if not alts and (ret_expr.startswith('f"') or ret_expr.startswith("f'")):
        quote = ret_expr[1]
        inner = ret_expr[2:-1]
        parts = []
        cur = ''
        i = 0
        while i < len(inner):
            if inner[i] == '{':
                if cur:
                    parts.append(('str', cur))
                    cur = ''
                j = inner.find('}', i)
                if j == -1:
                    break
                expr = inner[i + 1:j].strip() or None
                parts.append(('expr', expr))
                i = j + 1
            elif inner[i] == '}' and inner[i:i+2] == '}}':
                cur += '}'
                i += 2
            elif inner[i] == '{' and inner[i:i+2] == '{{':
                cur += '{'
                i += 2
            else:
                cur += inner[i]
                i += 1
        if cur:
            parts.append(('str', cur))
        exprs = [p[1] for p in parts if p[0] == 'expr' and p[1]]
        if exprs and all(re.match(r'^[A-Za-z_]\w*$', e) for e in exprs):
            format_template = ''.join(['{}' if p[0] == 'expr' else p[1] for p in parts])
            percent_template = ''.join(['%s' if p[0] == 'expr' else p[1] for p in parts])
            alt1 = 'def ' + fname + '(' + params + '):\n    return ' + repr(format_template) + '.format(' + ', '.join(exprs) + ')'
            alt2 = 'def ' + fname + '(' + params + '):\n    return ' + repr(percent_template) + ' % (' + ', '.join(exprs) + ')'
            alts = [alt1, alt2]

    return alts[:2]


# ---------------------------------------------------------------------------
# Body-pattern detection
# ---------------------------------------------------------------------------

def extract_body_assignment(func_code, var_name):
    body_lines = func_code.split('\n')[1:]
    for l in body_lines:
        stripped = l.strip()
        if stripped.startswith(var_name + ' ='):
            return strip_inline_comment(stripped[len(var_name) + 1:].lstrip('=').strip())
        if stripped.startswith(var_name + '='):
            return strip_inline_comment(stripped[len(var_name):].lstrip('=').strip())
    return None


def detect_list_append_loop(func_code):
    text = func_code
    m = re.search(r'(\w+)\s*=\s*\[\]', text)
    if not m:
        return None
    result_var = m.group(1)
    append_m = re.search(rf'for\s+(\w+)\s+in\s+(\w+):.*?{re.escape(result_var)}\.append\((.+?)\)', text, re.DOTALL)
    if not append_m:
        return None
    loop_var, iterable, expr = append_m.groups()
    expr = strip_inline_comment(expr)
    return result_var, iterable, loop_var, expr


def detect_counting_loop(func_code):
    text = func_code
    m = re.search(r'(\w+)\s*=\s*0', text)
    if not m:
        return None
    count_var = m.group(1)
    loop_m = re.search(r'for\s+(\w+)\s+in\s+(\w+):', text, re.DOTALL)
    if not loop_m:
        return None
    loop_var, iterable = loop_m.groups()
    cond_m = re.search(r'if\s+(.+?):\s*' + re.escape(count_var) + r'\s*\+=\s*1', text, re.DOTALL)
    if not cond_m:
        return None
    cond = strip_inline_comment(cond_m.group(1))
    return count_var, iterable, loop_var, cond


def gen_from_body_patterns(fname, params, func_code, param_names):
    ret_lines = [l for l in func_code.split('\n') if l.strip().startswith('return ')]
    if not ret_lines:
        return []
    ret_expr = strip_inline_comment(ret_lines[0].strip()[7:])

    # List append loop -> list comprehension and map
    append_info = detect_list_append_loop(func_code)
    if append_info:
        result_var, iterable, loop_var, expr = append_info
        return [
            f'def {fname}({params}):\n    return [{expr} for {loop_var} in {iterable}]',
            f'def {fname}({params}):\n    return list(map(lambda {loop_var}: {expr}, {iterable}))',
        ]

    # Counting loop -> sum and len(filter)
    count_info = detect_counting_loop(func_code)
    if count_info:
        count_var, iterable, loop_var, cond = count_info
        return [
            f'def {fname}({params}):\n    return sum(1 for {loop_var} in {iterable} if {cond})',
            f'def {fname}({params}):\n    return len([{loop_var} for {loop_var} in {iterable} if {cond}])',
        ]

    # If return is a variable assigned to a non-trivial expression, use that expression
    if re.match(r'^[A-Za-z_]\w*$', ret_expr):
        assigned = extract_body_assignment(func_code, ret_expr)
        if assigned and assigned not in ('0', '[]', '{}', '', 'None', 'True', 'False'):
            return gen_from_return(fname, params, assigned, param_names)

    return []


# ---------------------------------------------------------------------------
# Script wrapping
# ---------------------------------------------------------------------------

def infer_param_from_prompt(prompt):
    p = prompt.strip().lower()
    if 'number' in p or 'num' in p or 'integer' in p or 'int' in p or 'value' in p:
        return 'number'
    if 'string' in p or 'text' in p or 'word' in p or 'sentence' in p:
        return 'text'
    if 'list' in p or 'array' in p:
        return 'items'
    words = re.findall(r'[a-zA-Z_]+', prompt)
    if words:
        return words[0].lower()
    return 'value'


def rename_vars_in_script(script_body):
    """Produce a trivial variant by renaming top-level assignment variables."""
    lines = script_body.split('\n')
    mapping = {}
    new_lines = []
    for l in lines:
        stripped = l.strip()
        if not stripped or stripped.startswith('#'):
            new_lines.append(l)
            continue
        m = re.match(r'^(\w+)\s*=\s*(.+)$', stripped)
        if m and not m.group(1).startswith('_') and m.group(1) not in mapping:
            mapping[m.group(1)] = m.group(1) + '_2'
        for old, new in mapping.items():
            # Simple whole-word replacement
            l = re.sub(r'\b' + re.escape(old) + r'\b', new, l)
        new_lines.append(l)
    return '\n'.join(new_lines)


def wrap_script_in_function(code, variant=1):
    # Use only the first contiguous script block (before any heading)
    lines = code.split('\n')
    end_idx = len(lines)
    for i, l in enumerate(lines):
        if is_heading(l):
            end_idx = i
            break
    body_lines = lines[:end_idx]

    param_names = []
    seen = set()

    for l in body_lines:
        if 'input(' in l:
            m = re.search(r'input\(([^)]*)\)', l)
            prompt = m.group(1) if m else ''
            pname = infer_param_from_prompt(prompt)
            base = pname
            suffix = 1
            while pname in seen:
                pname = f'{base}{suffix}'
                suffix += 1
            seen.add(pname)
            param_names.append(pname)

    new_lines = []
    input_idx = 0
    for l in body_lines:
        if 'input(' in l and input_idx < len(param_names):
            var = l.split('=')[0].strip()
            new_lines.append(f'    {var} = {param_names[input_idx]}')
            input_idx += 1
        elif l.strip().startswith('#'):
            continue
        elif l.strip():
            new_lines.append('    ' + l)

    if not new_lines:
        return None

    if variant == 2:
        # Try to produce a return variant if there is a single trailing print
        print_lines = [i for i, l in enumerate(new_lines) if re.search(r'print\s*\(', l.strip())]
        if len(print_lines) == 1:
            pl = print_lines[0]
            pm = re.search(r'print\s*\((.+?)\)', new_lines[pl])
            if pm:
                indent_match = re.match(r'^(\s*)', new_lines[pl])
                indent = indent_match.group(1) if indent_match else '    '
                new_lines[pl] = indent + 'return ' + pm.group(1)
                params = ', '.join(param_names)
                return f'def solve({params}):\n' + '\n'.join(new_lines), param_names
        # Otherwise rename variables
        body = '\n'.join(l[4:] if l.startswith('    ') else l for l in new_lines)
        body = rename_vars_in_script(body)
        new_lines = ['    ' + l if l.strip() else l for l in body.split('\n')]

    params = ', '.join(param_names)
    wrapped = f'def solve({params}):\n' + '\n'.join(new_lines)
    return wrapped, param_names


def convert_for_to_while(code):
    lines = code.split('\n')
    new_lines = []
    i = 0
    changed = False
    while i < len(lines):
        l = lines[i]
        m = re.match(r'^(\s*)for\s+(\w+)\s+in\s+range\(([^)]+)\):\s*$', l)
        if m:
            indent_s, var, range_args = m.groups()
            args = [a.strip() for a in range_args.split(',')]
            if len(args) == 1:
                start, end, step = '0', args[0], '1'
            elif len(args) == 2:
                start, end, step = args[0], args[1], '1'
            elif len(args) == 3:
                start, end, step = args
            else:
                new_lines.append(l)
                i += 1
                continue
            new_lines.append(f'{indent_s}{var} = {start}')
            new_lines.append(f'{indent_s}while {var} < {end}:')
            i += 1
            body_indent = indent_s + '    '
            while i < len(lines) and (lines[i].startswith(body_indent) or not lines[i].strip()):
                if lines[i].strip():
                    new_lines.append(lines[i])
                i += 1
            new_lines.append(body_indent + f'{var} += {step}')
            changed = True
        else:
            new_lines.append(l)
            i += 1
    if not changed:
        return None
    return '\n'.join(new_lines)


def gen_function_alts(code):
    func = extract_first_func(code)
    if func:
        fname, params = get_signature(func)
        if fname:
            param_names = get_param_names(params)
            ret_lines = [l for l in func.split('\n') if l.strip().startswith('return ')]
            ret_expr = strip_inline_comment(ret_lines[0].strip()[7:]) if ret_lines else None

            if ret_expr:
                alts = gen_from_return(fname, params, ret_expr, param_names)
                if alts and all(compile_check(a) for a in alts):
                    return alts, None

            alts = gen_from_body_patterns(fname, params, func, param_names)
            if alts and all(compile_check(a) for a in alts):
                return alts, None

            # Final generic fallback
            if ret_expr:
                alts = [
                    f'def {fname}({params}):\n    result = {ret_expr}\n    return result',
                    f'def {fname}({params}):\n    return {ret_expr}',
                ]
                if all(compile_check(a) for a in alts):
                    return alts, None

    # Print-based function fallback: turn the printed expression into a return
    if func:
        fname, params = get_signature(func)
        if fname:
            param_names = get_param_names(params)
            prints = [l for l in func.split('\n') if re.search(r'print\s*\(', l.strip())]
            if prints and not any(l.strip().startswith('return ') for l in func.split('\n')):
                pm = re.search(r'print\s*\((.+?)\)\s*$', strip_inline_comment(prints[-1].strip()))
                if pm:
                    expr = pm.group(1)
                    # Build a return version of the function
                    body_lines = []
                    for l in func.split('\n')[1:]:
                        stripped = l.strip()
                        if stripped.startswith('print') and re.search(r'print\s*\((.+?)\)\s*$', strip_inline_comment(stripped)):
                            body_lines.append('    return ' + expr)
                        elif stripped:
                            body_lines.append(l)
                    return_version = f'def {fname}({params}):\n' + '\n'.join(body_lines)
                    intermediate_version = f'def {fname}({params}):\n' + '\n'.join(body_lines[:-1] + ['    result = ' + expr, '    return result'])
                    alts = [return_version, intermediate_version]
                    if all(compile_check(a) for a in alts):
                        return alts, None

    w1 = wrap_script_in_function(code, variant=1)
    w2 = wrap_script_in_function(code, variant=2)
    if w1 and w2 and compile_check(w1[0]) and compile_check(w2[0]):
        return [w1[0], w2[0]], None

    return [], 'could not generate reliable alternatives'


def format_alts(alts):
    titles = ['Using built-in approach', 'Using manual approach']
    return ''.join([f'\n\n# {titles[i] if i < len(titles) else "Alternative approach"}\n{alt}' for i, alt in enumerate(alts)])


def main():
    with open(TS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    id_matches = list(re.finditer(r'"id": (\d+),', content))
    in_range = [(idx, m) for idx, m in enumerate(id_matches) if BATCH_START <= int(m.group(1)) <= BATCH_END]

    inserted = 0
    manual_review = []
    offset = 0

    for idx, idm in in_range:
        pid = int(idm.group(1))
        prob_pos = idm.start() + offset
        next_pos = (id_matches[idx + 1].start() if idx + 1 < len(id_matches) else len(content)) + offset
        chunk = content[prob_pos:next_pos]

        sol_field = '"solution": "'
        sol_pos = chunk.find(sol_field)
        if sol_pos == -1:
            manual_review.append((pid, 'no solution field'))
            continue

        val_start = prob_pos + sol_pos + len(sol_field)
        close_quote = find_solution_end(content, val_start)
        if close_quote == -1:
            manual_review.append((pid, 'unterminated solution string'))
            continue

        sol_raw = content[val_start:close_quote]
        code = unescape_ts(sol_raw)
        code = strip_broken_tail(code)
        stripped_raw = escape_ts(code)

        # Always write the cleaned (stripped) solution back
        if not DRY_RUN:
            content = content[:val_start] + stripped_raw + content[close_quote:]
            offset -= close_quote - val_start - len(stripped_raw)

        alts, reason = gen_function_alts(code)
        if not alts or len(alts) < 2:
            manual_review.append((pid, reason or 'insufficient alternatives generated'))
            continue

        if not all(compile_check(a) for a in alts):
            manual_review.append((pid, 'generated code failed compile check'))
            continue

        alt_text = format_alts(alts)
        alt_text = escape_ts(alt_text)

        if '"' in alt_text:
            manual_review.append((pid, 'double quote remains after escaping'))
            continue

        if not DRY_RUN:
            # Append alts right after the now-stripped solution string
            content = content[:val_start + len(stripped_raw)] + alt_text + content[val_start + len(stripped_raw):]
            offset += len(alt_text)
        inserted += 2

    if not DRY_RUN:
        with open(TS_FILE, 'w', encoding='utf-8') as f:
            f.write(content)

    report = []
    report.append(f'# Batch {BATCH_START}-{BATCH_END} Report')
    report.append(f'')
    report.append(f'- Mode: {"DRY RUN" if DRY_RUN else "APPLIED"}')
    report.append(f'- Problems in range: {len(in_range)}')
    report.append(f'- Alternatives inserted: {inserted}')
    report.append(f'- Manual review needed: {len(manual_review)}')
    report.append(f'')
    if manual_review:
        report.append('## Manual review needed')
        for pid, reason in manual_review:
            report.append(f'- P{pid}: {reason}')
        report.append('')

    REPORT_FILE.write_text('\n'.join(report), encoding='utf-8')
    print('\n'.join(report))


if __name__ == '__main__':
    main()
