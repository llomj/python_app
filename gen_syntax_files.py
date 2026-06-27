#!/usr/bin/env python3
# Generate syntax docs using real Python code snippets + minimal # headers.
# CodeMirror will syntax-highlight the code naturally.
#
# Output: level1_{500,1000,1500,2000}_syntax.py
# Format:  """ Problem N: """ markers (same as requirements files)

import ast
import re
from pathlib import Path

TS_FILE = Path('/Users/moll/Desktop/python_app/exercises.ts')
OUT_DIR = Path('/Users/moll/Desktop/python_app')


def unescape_ts(s: str) -> str:
    return (s.replace('\\\\', '\\')
             .replace('\\"', '"')
             .replace("\\'", "'")
             .replace('\\n', '\n'))


def find_solution_end(text: str, start_pos: int) -> int:
    i = start_pos
    while i < len(text):
        if text[i] == '\\' and i + 1 < len(text):
            i += 2
        elif text[i] == '"' and i + 1 < len(text) and text[i + 1] == ',':
            return i
        else:
            i += 1
    return -1


# ── AST helpers ─────────────────────────────────────────────────────

def _op_name(op: ast.operator) -> str:
    m = {ast.Add: '+', ast.Sub: '-', ast.Mult: '*', ast.Div: '/',
         ast.FloorDiv: '//', ast.Mod: '%', ast.Pow: '**',
         ast.LShift: '<<', ast.RShift: '>>', ast.BitOr: '|',
         ast.BitXor: '^', ast.BitAnd: '&'}
    for cls, n in m.items():
        if isinstance(op, cls):
            return n
    return '?'


def _name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return f"{_name(node.value)}.{node.attr}"
    if isinstance(node, ast.Call):
        return f"{_name(node.func)}(...)"
    if isinstance(node, ast.Constant):
        return repr(node.value)
    if isinstance(node, ast.List):
        return f"[{', '.join(_name(e) for e in node.elts)}]"
    if isinstance(node, ast.Tuple):
        return f"({', '.join(_name(e) for e in node.elts)})"
    return '?'


def first_code_section(code: str) -> str:
    """Extract the first main approach from a multi-alternative solution."""
    markers = ['# Using built-in approach', '# Using manual approach',
               '# Script approach', '# Direct approach',
               '# Using function approach']
    pos = None
    for m in markers:
        p = code.find(m)
        if p != -1 and (pos is None or p < pos):
            pos = p
    if pos and pos > 0:
        return code[:pos].strip()
    return code.strip()


def _func_sig(f: ast.FunctionDef) -> str:
    params = [a.arg for a in f.args.args]
    return f"def {f.name}({', '.join(params)}):"


def _code_line(node: ast.AST) -> str:
    """Return a compact source-code representation of a top-level statement."""
    if isinstance(node, ast.FunctionDef):
        return _func_sig(node)
    if isinstance(node, ast.ClassDef):
        bases = [b.id if isinstance(b, ast.Name) else '' for b in node.bases]
        return f"class {node.name}({', '.join(bases)})" if bases else f"class {node.name}"
    if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
        return _call_str(node.value)
    if isinstance(node, ast.Assign):
        ts = ', '.join(t.id if isinstance(t, ast.Name) else '?' for t in node.targets)
        return f"{ts} = ..."
    if isinstance(node, ast.For):
        target = ast.unparse(node.target)
        return f"for {target} in {_name(node.iter)}:"
    if isinstance(node, ast.While):
        return "while ...:"
    if isinstance(node, ast.If):
        return "if ...:"
    if isinstance(node, ast.Import):
        return f"import {', '.join(a.name for a in node.names)}"
    if isinstance(node, ast.ImportFrom):
        return f"from {node.module} import {', '.join(a.name for a in node.names)}"
    return ''


def _call_str(node: ast.Call) -> str:
    args = []
    for a in node.args:
        if isinstance(a, ast.Name):
            args.append(a.id)
        elif isinstance(a, ast.Constant):
            args.append(repr(a.value))
        elif isinstance(a, ast.Call):
            args.append(_name(a))
        elif isinstance(a, ast.BinOp):
            args.append(f"{_name(a.left)} {_op_name(a.op)} {_name(a.right)}")
        else:
            args.append('?')
    return f"{_name(node.func)}({', '.join(args)})"


# ── Section generators (return real Python code) ────────────────────

def gen_syntax(tree: ast.Module) -> str:
    lines = []
    lines.append("# Syntax")
    lines.append("")

    funcs = [n for n in tree.body if isinstance(n, ast.FunctionDef)]
    classes = [n for n in tree.body if isinstance(n, ast.ClassDef)]

    if classes:
        for c in classes:
            bases = [b.id if isinstance(b, ast.Name) else '' for b in c.bases]
            if bases:
                lines.append(f"class {c.name}({', '.join(bases)}):")
            else:
                lines.append(f"class {c.name}:")
            for m in c.body:
                if isinstance(m, ast.FunctionDef):
                    lines.append(f"    {_func_sig(m)}")
                    for stmt in m.body:
                        body_code = ast.unparse(stmt)
                        for line in body_code.split('\n'):
                            lines.append(f"        {line}")
            lines.append("")

    if funcs:
        f = funcs[0]
        lines.append(_func_sig(f))
        for stmt in f.body:
            body_code = ast.unparse(stmt)
            for line in body_code.split('\n'):
                lines.append(f"    {line}")
        lines.append("")

    # Keywords and operators as comments
    kw_parts = []
    for n in ast.walk(tree):
        if isinstance(n, ast.For): kw_parts.append('for'); break
    for n in ast.walk(tree):
        if isinstance(n, ast.While): kw_parts.append('while'); break
    for n in ast.walk(tree):
        if isinstance(n, ast.If): kw_parts.append('if/else'); break
    for n in ast.walk(tree):
        if isinstance(n, ast.Try): kw_parts.append('try/except'); break
    if kw_parts:
        lines.append(f"# keywords: {' | '.join(kw_parts)}")

    # Operators
    ops = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.BinOp): ops.add(_op_name(n.op))
        elif isinstance(n, ast.Compare):
            for op in n.ops:
                for cls, s in {ast.Eq: '==', ast.NotEq: '!=', ast.Lt: '<', ast.LtE: '<=',
                               ast.Gt: '>', ast.GtE: '>=', ast.In: 'in', ast.NotIn: 'not in',
                               ast.Is: 'is', ast.IsNot: 'is not'}.items():
                    if isinstance(op, cls): ops.add(s)
        elif isinstance(n, ast.BoolOp):
            ops.add('and' if isinstance(n.op, ast.And) else 'or')
    if ops:
        lines.append(f"# operators: {' '.join(sorted(ops, key=lambda x: (len(x), x)))}")

    # Built-in calls (excluding user-defined functions and print)
    user_funcs = {f.name for f in tree.body if isinstance(f, (ast.FunctionDef, ast.AsyncFunctionDef))}
    calls = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id not in ('print',) and n.func.id not in user_funcs:
            calls.add(n.func.id)
    if calls:
        lines.append(f"# builtins: {', '.join(sorted(calls))}()")

    return '\n'.join(lines)


def gen_evaluation_order(tree: ast.Module) -> str:
    lines = []
    lines.append("# Evaluation Order")
    lines.append("")

    func_names = {f.name for f in tree.body if isinstance(f, ast.FunctionDef)}
    shown = set()

    # Show key expressions from the code
    for n in ast.walk(tree):
        if isinstance(n, ast.BinOp):
            code = ast.unparse(n)
            if code not in shown:
                shown.add(code)
                lines.append(f"{code}  # {_name(n.left)} → {_name(n.right)} → {_op_name(n.op)}")
        elif isinstance(n, ast.Call) and isinstance(n.func, ast.Name):
            if n.func.id in func_names:
                code = ast.unparse(n)
                if code not in shown:
                    shown.add(code)
                    lines.append(f"{code}  # evaluate args first, then run body")
            elif n.func.id == 'print' and n.args:
                inner = n.args[0]
                if isinstance(inner, ast.Call):
                    code = ast.unparse(n)
                    if code not in shown:
                        shown.add(code)
                        inner_name = _name(inner.func)
                        lines.append(f"{code}  # {inner_name}() runs first, then print()")
        elif isinstance(n, ast.Compare):
            code = ast.unparse(n)
            if code not in shown:
                shown.add(code)
                lines.append(f"{code}  # evaluates to True or False")

    if not shown:
        lines.append("# (simple expressions — evaluated left to right)")

    return '\n'.join(lines)


def gen_execution_order(tree: ast.Module) -> str:
    lines = []
    lines.append("# Execution Order")
    lines.append("")

    func_map = {f.name: f for f in tree.body if isinstance(f, ast.FunctionDef)}

    for i, stmt in enumerate(tree.body, 1):
        code = _code_line(stmt)
        if not code:
            continue

        if isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Call):
            call = stmt.value
            name = _name(call.func)
            inner = call.args[0] if call.args and isinstance(call.args[0], ast.Call) else None
            target = func_map.get(name) or (func_map.get(_name(inner.func)) if inner and _name(inner.func) in func_map else None)

            lines.append(f"# {i}. {code}")
            if target:
                params = [a.arg for a in target.args.args]
                the_call = inner if name not in func_map else call
                if params and the_call.args:
                    binds = ', '.join(f"{p}={_name(a)}" for p, a in zip(params, the_call.args))
                    lines.append(f"#    → calls with {binds}")
                for j, bs in enumerate(target.body, 1):
                    body = ast.unparse(bs)
                    for bline in body.split('\n'):
                        lines.append(f"#    → {i}.{j} {bline}")
        elif isinstance(stmt, ast.FunctionDef):
            lines.append(f"# {i}. {code}  # stored, not run yet")
        elif isinstance(stmt, ast.For):
            lines.append(f"# {i}. for ... in {_name(stmt.iter)}:  # loops over each item")
            for j, bs in enumerate(stmt.body, 1):
                body = _code_line(bs)
                if body:
                    lines.append(f"#    {i}.{j} {body}")
        else:
            lines.append(f"# {i}. {code}")

    return '\n'.join(lines)


def gen_execution_flow(tree: ast.Module) -> str:
    lines = []
    lines.append("# Execution Flow")
    lines.append("")

    func_names = {f.name for f in tree.body if isinstance(f, ast.FunctionDef)}
    class_names = {c.name for c in tree.body if isinstance(c, ast.ClassDef)}
    top_code = [n for n in tree.body
                if not isinstance(n, (ast.FunctionDef, ast.ClassDef, ast.Import, ast.ImportFrom))]

    has_loop = any(isinstance(n, (ast.For, ast.While)) for n in ast.walk(tree))
    has_if = any(isinstance(n, ast.If) for n in ast.walk(tree))

    if class_names:
        lines.append(f"# Classes {', '.join(class_names)} are defined (methods stored)")
        lines.append("")

    if func_names:
        lines.append(f"# def lines are skipped — {', '.join(func_names)} are just stored in memory")
        lines.append("")

    if not top_code:
        lines.append("# No top-level execution (functions must be called externally)")
    else:
        lines.append("# Runtime starts here (top-level code runs top to bottom):")
        lines.append("")
        for stmt in top_code:
            code = _code_line(stmt)
            if not code:
                continue

            if isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Call):
                call = stmt.value
                name = _name(call.func)
                inner = call.args[0] if call.args and isinstance(call.args[0], ast.Call) else None
                if name in func_names:
                    lines.append(f"{ast.unparse(call)}  # jumps into {name}(), runs body, returns")
                elif inner and _name(inner.func) in func_names:
                    iname = _name(inner.func)
                    lines.append(f"{ast.unparse(call)}  # {iname}() runs first, then print() outputs")
                else:
                    lines.append(ast.unparse(call))
            elif isinstance(stmt, ast.For):
                lines.append(f"for ... in {_name(stmt.iter)}:  # repeats N times")
            elif isinstance(stmt, ast.While):
                lines.append(f"while ...:  # loops until condition is False")
            elif isinstance(stmt, ast.If):
                lines.append(f"if ...:  # only one branch executes")
            else:
                lines.append(code)

    if has_loop:
        lines.append("")
        for n in ast.walk(tree):
            if isinstance(n, ast.For):
                lines.append(f"# Loop: one item from {_name(n.iter)} each iteration")
                break
            elif isinstance(n, ast.While):
                lines.append(f"# Loop: check condition → run body → check again")
                break

    if has_if:
        lines.append("# Branch: condition determines which block runs")

    return '\n'.join(lines)


# ── Main ────────────────────────────────────────────────────────────

def main():
    with open(TS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    id_matches = list(re.finditer(r'"id": (\d+),', content))
    tiers = {500: [], 1000: [], 1500: [], 2000: []}

    for idx, m in enumerate(id_matches):
        pid = int(m.group(1))
        pos = m.start()
        next_pos = id_matches[idx + 1].start() if idx + 1 < len(id_matches) else len(content)
        chunk = content[pos:next_pos]

        sol_field = '"solution": "'
        sol_pos = chunk.find(sol_field)
        if sol_pos == -1:
            continue
        val_start = pos + sol_pos + len(sol_field)
        close_quote = find_solution_end(content, val_start)
        if close_quote == -1:
            continue

        code = unescape_ts(content[val_start:close_quote])

        if pid <= 500:
            tier = 500
        elif pid <= 1000:
            tier = 1000
        elif pid <= 1500:
            tier = 1500
        else:
            tier = 2000

        try:
            tree = ast.parse(code)
        except SyntaxError:
            section = first_code_section(code)
            try:
                tree = ast.parse(section)
            except SyntaxError:
                print(f"  Skipping P{pid}")
                continue

        parts = [
            "#" + "=" * 50,
            gen_syntax(tree),
            "",
            "#" + "=" * 50,
            gen_evaluation_order(tree),
            "",
            "#" + "=" * 50,
            gen_execution_order(tree),
            "",
            "#" + "=" * 50,
            gen_execution_flow(tree),
        ]

        full = '\n'.join(parts)
        tiers[tier].append((pid, full))

        if pid % 200 == 0:
            print(f"  Processed P{pid}...")

    for tier, entries in sorted(tiers.items()):
        if not entries:
            continue
        outfile = OUT_DIR / f'level1_{tier}_syntax.py'
        with open(outfile, 'w', encoding='utf-8') as f:
            f.write(f'# Syntax documentation for level 1 (problems 1-{tier})\n')
            f.write(f'# Auto-generated by gen_syntax_files.py\n\n')
            for pid, content in entries:
                f.write(f'"""\nProblem {pid}:\n{content}\n\n"""\n\n')
        print(f"Wrote {outfile} ({len(entries)} problems)")

    print("\nDone!")


if __name__ == '__main__':
    main()
