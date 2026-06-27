#!/usr/bin/env python3
"""Generate 2 script-style alternatives per problem in exercises.ts.

Script-style alts show how to USE/CALL the function directly with example data,
as opposed to function-style alts which show different implementations.
"""

import re
import sys
import ast
from pathlib import Path

TS_FILE = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('/Users/moll/Desktop/python_app/exercises.ts')
BATCH_START = int(sys.argv[2]) if len(sys.argv) > 2 else 1
BATCH_END = int(sys.argv[3]) if len(sys.argv) > 3 else 1981
DRY_RUN = '--dry-run' in sys.argv

EXISTING_SCRIPT_HEADINGS = (
    '# Script approach', '# Direct approach', '# Script-style',
)

PARAM_VALUES = {
    # Name -> (type, value1, value2)
    'a': ('num', 10, 20),
    'b': ('num', 20, 30),
    'x': ('num', 7, 3),
    'y': ('num', 3, 14),
    'n': ('num', 6, 15),
    'm': ('num', 4, 12),
    'numbers': ('list', '[3, 7, 2, 9, 1]', '[4, 1, 8, 6, 3]'),
    'nums': ('list', '[3, 7, 2, 9, 1]', '[4, 1, 8, 6, 3]'),
    'lst': ('list', '[2, 4, 6, 8]', '[1, 3, 5, 7]'),
    'list': ('list', '[5, 10, 15]', '[2, 8, 3]'),
    'arr': ('list', '[8, 3, 6, 1]', '[5, 9, 2, 7]'),
    'items': ('list', '[5, 10, 15]', '[2, 8, 3]'),
    'values': ('list', '[3, 7, 2, 9, 1]', '[4, 1, 8, 6, 3]'),
    'elements': ('list', '[2, 7, 1, 9]', '[5, 3, 8, 4]'),
    'collection': ('list', '[3, 1, 4, 1, 5]', '[2, 7, 1, 8]'),
    'string': ('str', "'hello'", "'world'"),
    'text': ('str', "'hello'", "'world'"),
    'word': ('str', "'python'", "'coding'"),
    'name': ('str', "'Alice'", "'Bob'"),
    'sentence': ('str', "'Hello, World!'", "'Python is fun'"),
    'char': ('str', "'a'", "'z'"),
    'msg': ('str', "'hi'", "'hello'"),
    'message': ('str', "'Good morning'", "'Hello there'"),
    'prefix': ('str', "'Hello, '", "'Hi, '"),
    'suffix': ('str', "'!'", "'?'"),
    'base': ('num', 5, 10),
    'height': ('num', 10, 20),
    'width': ('num', 15, 25),
    'radius': ('num', 7, 14),
    'count': ('num', 5, 10),
    'index': ('num', 2, 4),
    'start': ('num', 1, 3),
    'end': ('num', 10, 20),
    'step': ('num', 1, 2),
    'key': ('str', "'key'", "'value'"),
    'target': ('str', "'target'", "'goal'"),
    'default': ('num', 0, 1),
    'flag': ('bool', 'True', 'False'),
    'verbose': ('bool', 'True', 'False'),
    'num1': ('num', 10, 20),
    'num2': ('num', 20, 30),
    'str1': ('str', "'hello'", "'world'"),
    'str2': ('str', "'world'", "'python'"),
    'string1': ('str', "'hello'", "'world'"),
    'string2': ('str', "'world'", "'python'"),
    'lst1': ('list', '[1, 3, 5]', '[2, 4, 6]'),
    'lst2': ('list', '[2, 4, 6]', '[1, 3, 5]'),
    'tuple': ('list', '(1, 2, 3)', '(4, 5, 6)'),
    'set': ('list', '{1, 2, 3}', '{4, 5, 6}'),
    'dict': ('dict', '{"a": 1, "b": 2}', '{"x": 10, "y": 20}'),
    'dictionary': ('dict', '{"a": 1, "b": 2}', '{"x": 10, "y": 20}'),
    'mapping': ('dict', '{"a": 1, "b": 2}', '{"x": 10, "y": 20}'),
}


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


def extract_first_func(code):
    """Find the first function that has at least one parameter."""
    lines = code.split('\n')
    for start_idx, l in enumerate(lines):
        if l.startswith('def ') or l.startswith('class '):
            # Check if this function has parameters
            m = re.match(r'def\s+\w+\s*\((.*?)\)\s*(?:->\s*[^:]+)?\s*:', l, re.DOTALL)
            if m:
                params = m.group(1).strip()
                if params and params != 'self':  # Has at least one param
                    block = [lines[start_idx]]
                    for l2 in lines[start_idx + 1:]:
                        stripped = l2.strip()
                        if not stripped:
                            block.append(l2)
                        elif l2.startswith(' ') or l2.startswith('\t') or stripped.startswith('#'):
                            block.append(l2)
                        else:
                            break
                    while block and not block[-1].strip():
                        block.pop()
                    return '\n'.join(block)
    return None


def get_signature(func_code):
    m = re.match(r'def\s+(\w+)\s*\((.*?)\)\s*(?:->\s*[^:]+)?\s*:', func_code, re.DOTALL)
    if m:
        return m.group(1), m.group(2)
    return None, None


def get_param_names(params_str):
    parts = []
    depth = 0
    cur = ''
    for ch in params_str:
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


def get_value_for_param(name, func_code):
    """Get (type_str, value1, value2) for a parameter name."""
    # Check exact name match first
    if name in PARAM_VALUES:
        return PARAM_VALUES[name]

    # Check for prefixes/suffixes
    name_lower = name.lower().strip('_')

    # Infer type from function body
    body = func_code.split('\n', 1)[1] if '\n' in func_code else ''

    # String indicators
    if re.search(r'\b' + re.escape(name) + r'\.(lower|upper|startswith|endswith|find|split|strip|join|format|replace|capitalize|title)', body):
        return ('str', "'hello'", "'world'")

    # List indicators
    if re.search(r'for\s+\w+\s+in\s+' + re.escape(name) + r'\b', body):
        return ('list', '[3, 7, 2, 9, 1]', '[4, 1, 8, 6, 3]')
    if re.search(r'\b' + re.escape(name) + r'\.append\(', body):
        return ('list', '[3, 7, 2, 9, 1]', '[4, 1, 8, 6, 3]')
    if re.search(r'\b' + re.escape(name) + r'\s*\[', body):
        return ('list', '[3, 7, 2, 9, 1]', '[4, 1, 8, 6, 3]')

    # Built-ins that take iterables
    if re.search(r'(max|min|sum|sorted|reversed)\s*\([^)]*' + re.escape(name) + r'[^)]*\)', body):
        return ('list', '[3, 7, 2, 9, 1]', '[4, 1, 8, 6, 3]')

    # Arithmetic on param
    if re.search(r'\b' + re.escape(name) + r'\s*[+\-*/%]', body):
        return ('num', 15, 25)

    # Number-like name patterns
    if any(kw in name_lower for kw in ('num', 'int', 'value', 'count', 'total',
                                         'sum', 'max', 'min', 'idx', 'index',
                                         'size', 'len', 'amt', 'amount')):
        return ('num', 15, 25)
    if any(kw in name_lower for kw in ('string', 'str', 'text', 'word', 'char',
                                         'msg', 'name', 'sentence')):
        return ('str', "'hello'", "'world'")
    if any(kw in name_lower for kw in ('list', 'arr', 'items', 'values',
                                         'elements', 'lst', 'collection',
                                         'nums', 'ints')):
        return ('list', '[3, 7, 2, 9, 1]', '[4, 1, 8, 6, 3]')
    if any(kw in name_lower for kw in ('dict', 'map', 'hash')):
        return ('dict', '{"a": 1, "b": 2}', '{"x": 10, "y": 20}')

    # Single letter defaults
    if len(name) == 1:
        return ('num', 5, 10)

    return ('num', 15, 25)


def has_script_already(code):
    for h in EXISTING_SCRIPT_HEADINGS:
        if h in code:
            return True
    return False


def infer_input_value(prompt_text):
    """Infer a sensible hardcoded value from an input() prompt."""
    p = (prompt_text or '').lower()
    if 'number' in p or 'num' in p or 'int' in p or 'digit' in p \
       or 'value' in p or 'amount' in p or 'count' in p \
       or 'age' in p or 'year' in p or 'limit' in p:
        return '5'
    if 'float' in p or 'decimal' in p or 'real' in p or 'double' in p:
        return '3.5'
    if 'string' in p or 'text' in p or 'str' in p or 'word' in p \
       or 'name' in p or 'char' in p or 'sentence' in p \
       or 'msg' in p or 'message' in p or 'letter' in p:
        return "'hello'"
    if 'list' in p or 'arr' in p or 'item' in p:
        return "'1 2 3'"
    return '5'


def replace_input_line(line, seen_vars):
    """Replace input() call with a hardcoded value assignment. Returns (new_line, replaced_var) or None."""
    m = re.match(r'^(\s*)(\w+)\s*=\s*.*?input\s*\(([^)]*)\)', line)
    if m:
        indent, var, prompt = m.groups()
        val = infer_input_value(prompt)
        return f'{indent}{var} = {val}', var
    return None, None


def gen_script_alts(code):
    # First try: find a function with params
    func = extract_first_func(code)
    if func:
        fname, params_str = get_signature(func)
        if fname:
            param_names = get_param_names(params_str)
            if param_names:
                values1 = {}
                values2 = {}
                for p in param_names:
                    typ, v1, v2 = get_value_for_param(p, func)
                    values1[p] = v1
                    values2[p] = v2

                def format_val(v):
                    return str(v)

                alt1_lines = []
                for p in param_names:
                    alt1_lines.append(f'{p} = {format_val(values1[p])}')
                alt1_args = ', '.join(param_names)
                alt1_lines.append(f'result = {fname}({alt1_args})')
                alt1_lines.append('print(result)')

                lit_args = ', '.join(format_val(values2[p]) for p in param_names)
                alt2_lines = [f'print({fname}({lit_args}))']

                alt1_code = '\n'.join(alt1_lines)
                alt2_code = '\n'.join(alt2_lines)

                if alt1_code and alt2_code:
                    try:
                        ast.parse(alt1_code)
                        ast.parse(alt2_code)
                        result = f'\n\n# Script approach\n{alt1_code}\n\n# Direct approach\n{alt2_code}'
                        return [result]
                    except SyntaxError:
                        pass

    # Fallback: extract ANY function and replace input() calls with hardcoded values
    # Find the first function (even no-param)
    lines = code.split('\n')
    func_start = None
    for i, l in enumerate(lines):
        if l.startswith('def ') or l.startswith('class '):
            func_start = i
            break
    if func_start is None:
        return []

    # Check if it's a class (not a def)
    if lines[func_start].startswith('class '):
        cm = re.match(r'class\s+(\w+)', lines[func_start])
        if cm:
            cls_name = cm.group(1)
            found_init = False
            for j in range(func_start + 1, min(func_start + 40, len(lines))):
                im = re.match(r'\s+def\s+__init__\s*\((.*?)\)\s*(?:->\s*[^:]+)?\s*:', lines[j])
                if im:
                    found_init = True
                    init_params = im.group(1).strip()
                    init_param_names = get_param_names(init_params)
                    init_param_names = [p for p in init_param_names if p != 'self']
                    if not init_param_names:
                        a1 = f'obj = {cls_name}()'
                        a2 = f'print({cls_name}())'
                        alt1_code = f'{a1}\nprint(obj)'
                        alt2_code = a2
                    else:
                        vals1 = {}
                        vals2 = {}
                        for p in init_param_names:
                            typ, v1, v2 = get_value_for_param(p, f'class {cls_name}')
                            vals1[p] = v1
                            vals2[p] = v2
                        args1 = ', '.join(str(vals1[p]) for p in init_param_names)
                        args2 = ', '.join(str(vals2[p]) for p in init_param_names)
                        alt1_code = f'obj = {cls_name}({args1})\nprint(obj)'
                        alt2_code = f'print({cls_name}({args2}))'
                    try:
                        ast.parse(alt1_code)
                        ast.parse(alt2_code)
                        result = f'\n\n# Script approach\n{alt1_code}\n\n# Direct approach\n{alt2_code}'
                        return [result]
                    except SyntaxError:
                        pass
            if not found_init:
                # No __init__ found — use default no-arg constructor
                alt1_code = f'obj = {cls_name}()\nprint(obj)'
                alt2_code = f'print({cls_name}())'
                try:
                    ast.parse(alt1_code)
                    ast.parse(alt2_code)
                    result = f'\n\n# Script approach\n{alt1_code}\n\n# Direct approach\n{alt2_code}'
                    return [result]
                except SyntaxError:
                    pass
        return []

    # Extract the function name
    fm = re.match(r'def\s+(\w+)\s*\(', lines[func_start])
    if not fm:
        return []
    fname = fm.group(1)

    # Extract function body
    body = []
    for ll in lines[func_start + 1:]:
        stripped = ll.strip()
        if not stripped:
            body.append(ll)
        elif ll.startswith(' ') or ll.startswith('\t') or stripped.startswith('#'):
            body.append(ll)
        else:
            break
    while body and not body[-1].strip():
        body.pop()

    # Build variant 1: replace input() calls with values, keep rest of logic
    seen_vars = set()
    alt1_lines = []
    for bl in body:
        new_line, replaced_var = replace_input_line(bl, seen_vars)
        if replaced_var:
            alt1_lines.append(new_line)
            seen_vars.add(replaced_var)
            continue
        stripped = bl.strip()
        if not stripped or stripped == 'pass' or stripped.startswith('#'):
            continue
        if stripped.startswith('return '):
            expr = stripped[7:].split('#')[0].strip()
            alt1_lines.append(f'    result = {expr}')
            alt1_lines.append('    print(result)')
        elif re.search(r'print\s*\(', stripped):
            alt1_lines.append(bl)
        else:
            alt1_lines.append(bl)

    # Dedent
    dedented = []
    min_indent = None
    for l in alt1_lines:
        leading = len(l) - len(l.lstrip())
        if leading > 0:
            if min_indent is None or leading < min_indent:
                min_indent = leading
    if min_indent and min_indent > 0:
        for l in alt1_lines:
            if len(l) >= min_indent:
                dedented.append(l[min_indent:])
            else:
                dedented.append(l)
    else:
        dedented = alt1_lines

    alt1_code = '\n'.join(dedented).strip()

    # Variant 2: inline version with different values
    # Same approach but with different numbers
    seen_vars2 = set()
    alt2_lines = []
    for bl in body:
        new_line, replaced_var = replace_input_line(bl, seen_vars2)
        if replaced_var:
            # Use different values for variant 2
            m = re.match(r'^(\s*)(\w+)\s*=\s*(.*)', new_line)
            if m:
                var = m.group(2)
                val = m.group(3)
                # Shift to different value
                if val == '5':
                    val2 = '10'
                elif val == "'hello'":
                    val2 = "'world'"
                elif val == '3.5':
                    val2 = '7.0'
                else:
                    val2 = val
                alt2_lines.append(f'{m.group(1)}{var} = {val2}')
                seen_vars2.add(replaced_var)
            continue
        stripped = bl.strip()
        if not stripped or stripped == 'pass' or stripped.startswith('#'):
            continue
        if stripped.startswith('return '):
            expr = stripped[7:].split('#')[0].strip()
            alt2_lines.append(f'    result = {expr}')
            alt2_lines.append('    print(result)')
        elif re.search(r'print\s*\(', stripped):
            alt2_lines.append(bl)
        else:
            alt2_lines.append(bl)

    dedented2 = []
    min_indent2 = None
    for l in alt2_lines:
        leading = len(l) - len(l.lstrip())
        if leading > 0:
            if min_indent2 is None or leading < min_indent2:
                min_indent2 = leading
    if min_indent2 and min_indent2 > 0:
        for l in alt2_lines:
            if len(l) >= min_indent2:
                dedented2.append(l[min_indent2:])
            else:
                dedented2.append(l)
    else:
        dedented2 = alt2_lines

    alt2_code = '\n'.join(dedented2).strip()

    if not alt1_code or not alt2_code:
        return []

    try:
        ast.parse(alt1_code)
    except SyntaxError:
        return []
    try:
        ast.parse(alt2_code)
    except SyntaxError:
        return []

    result = f'\n\n# Script approach\n{alt1_code}\n\n# Direct approach\n{alt2_code}'
    return [result]


def main():
    with open(TS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    id_matches = list(re.finditer(r'"id": (\d+),', content))
    in_range = [(idx, m) for idx, m in enumerate(id_matches) if BATCH_START <= int(m.group(1)) <= BATCH_END]

    inserted = 0
    skipped_existing = 0
    failed_gen = 0
    offset = 0

    for idx, idm in in_range:
        pid = int(idm.group(1))
        prob_pos = idm.start() + offset
        next_pos = (id_matches[idx + 1].start() if idx + 1 < len(id_matches) else len(content)) + offset
        chunk = content[prob_pos:next_pos]

        sol_field = '"solution": "'
        sol_pos = chunk.find(sol_field)
        if sol_pos == -1:
            failed_gen += 1
            continue

        val_start = prob_pos + sol_pos + len(sol_field)
        close_quote = find_solution_end(content, val_start)
        if close_quote == -1:
            failed_gen += 1
            continue

        sol_raw = content[val_start:close_quote]
        code = unescape_ts(sol_raw)

        if has_script_already(code):
            skipped_existing += 1
            continue

        alts_list = gen_script_alts(code)
        if not alts_list:
            failed_gen += 1
            continue

        alt_text = alts_list[0]
        alt_text_escaped = escape_ts(alt_text)

        if '"' in alt_text_escaped:
            failed_gen += 1
            continue

        if not DRY_RUN:
            content = content[:close_quote] + alt_text_escaped + content[close_quote:]
            offset += len(alt_text_escaped)
        inserted += 2

    if not DRY_RUN:
        with open(TS_FILE, 'w', encoding='utf-8') as f:
            f.write(content)

    total = len(in_range)
    print(f'Range: P{BATCH_START}-{BATCH_END} ({total} problems)')
    print(f'Script alts inserted: {inserted} ({inserted // 2} problems)')
    print(f'Skipped (already had script alts): {skipped_existing}')
    print(f'Failed (no func / gen error): {failed_gen}')
    print(f'Mode: {"DRY RUN" if DRY_RUN else "APPLIED"}')


if __name__ == '__main__':
    main()
