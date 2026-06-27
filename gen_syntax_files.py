#!/usr/bin/env python3
# Generate syntax docs in comment format (like the Logic tab).
# All lines start with # so CodeMirror renders them as gray comments.
#
# Output: level1_{500,1000,1500,2000}_syntax.py

import ast
import re
from pathlib import Path

TS_FILE = Path('/Users/moll/Desktop/python_app/exercises.ts')
OUT_DIR = Path('/Users/moll/Desktop/python_app')


def unescape_ts(s: str) -> str:
    return (s.replace('\\\\', '\\').replace('\\"', '"').replace("\\'", "'").replace('\\n', '\n'))


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


def first_code_section(code: str) -> str:
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


def _name(node: ast.AST) -> str:
    if isinstance(node, ast.Name): return node.id
    if isinstance(node, ast.Attribute): return f"{_name(node.value)}.{node.attr}"
    if isinstance(node, ast.Call): return f"{_name(node.func)}(...)"
    if isinstance(node, ast.Constant): return repr(node.value)
    if isinstance(node, ast.List): return f"[{', '.join(_name(e) for e in node.elts)}]"
    return '?'


def _op_name(op: ast.operator) -> str:
    m = {ast.Add: '+', ast.Sub: '-', ast.Mult: '*', ast.Div: '/',
         ast.FloorDiv: '//', ast.Mod: '%', ast.Pow: '**',
         ast.LShift: '<<', ast.RShift: '>>', ast.BitOr: '|',
         ast.BitXor: '^', ast.BitAnd: '&'}
    for cls, n in m.items():
        if isinstance(op, cls): return n
    return '?'


def _call_str(node: ast.Call) -> str:
    args = []
    for a in node.args:
        if isinstance(a, ast.Name): args.append(a.id)
        elif isinstance(a, ast.Constant): args.append(repr(a.value))
        elif isinstance(a, ast.Call): args.append(_name(a))
        elif isinstance(a, ast.BinOp): args.append(f"{_name(a.left)} {_op_name(a.op)} {_name(a.right)}")
        else: args.append('?')
    return f"{_name(node.func)}({', '.join(args)})"


# ── Generators ─────────────────────────────────────────────────────

def gen_syntax(tree: ast.Module) -> list:
    lines = []
    lines.append("# ------")
    lines.append("# SYNTAX:")
    lines.append("# Syntax shows the Python keywords, operators, and structures used in")
    lines.append("# this solution.")
    lines.append("#")

    funcs = [n for n in tree.body if isinstance(n, ast.FunctionDef)]
    classes = [n for n in tree.body if isinstance(n, ast.ClassDef)]

    if classes:
        lines.append("# Classes:")
        for c in classes:
            bases = [b.id if isinstance(b, ast.Name) else '' for b in c.bases]
            if bases:
                lines.append(f"#   class {c.name}({', '.join(bases)}) → inherits from parent class")
            else:
                lines.append(f"#   class {c.name} → defines a new type")
            for m in c.body:
                if isinstance(m, ast.FunctionDef):
                    lines.append(f"#     def {m.name}(...) → method of {c.name}")
        lines.append("#")

    if funcs:
        f = funcs[0]
        params = ', '.join(a.arg for a in f.args.args)
        lines.append(f"#   def {f.name}({params}) → defines a reusable function")
        has_return = any(isinstance(n, ast.Return) for n in ast.walk(f))
        if has_return:
            lines.append(f"#   return → sends a value back to the caller")
        else:
            lines.append(f"#   (no return statement — the function prints output directly)")
        lines.append("#")

    # Keywords
    ks = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.For): ks.add('for')
        elif isinstance(n, ast.While): ks.add('while')
        elif isinstance(n, ast.If): ks.add('if/else')
        elif isinstance(n, ast.Try): ks.add('try/except')
    if ks:
        lines.append(f"# Keywords: {' | '.join(sorted(ks))}")

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
        lines.append(f"# Operators: {' '.join(sorted(ops, key=lambda x: (len(x), x)))}")

    # Built-in functions used
    user_funcs = {f.name for f in tree.body if isinstance(f, (ast.FunctionDef, ast.AsyncFunctionDef))}
    builtins_used = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id not in ('print',) and n.func.id not in user_funcs:
            builtins_used.add(n.func.id)
    if builtins_used:
        lines.append(f"# Built-in functions: {', '.join(sorted(builtins_used))}()")

    return lines


def gen_evaluation_order(tree: ast.Module) -> list:
    lines = []
    lines.append("#")
    lines.append("# ------")
    lines.append("# EVALUATION ORDER:")
    lines.append("# Evaluation Order shows how Python reads and processes expressions")
    lines.append("# step by step. Inner expressions are evaluated first, then outer ones.")
    lines.append("#")

    func_names = {f.name for f in tree.body if isinstance(f, ast.FunctionDef)}
    shown = set()

    for n in ast.walk(tree):
        if isinstance(n, ast.BinOp):
            code = f"{_name(n.left)} {_op_name(n.op)} {_name(n.right)}"
            if code not in shown:
                shown.add(code)
                lines.append(f"#   {code} → Python looks up {_name(n.left)}, then {_name(n.right)}, then applies {_op_name(n.op)}")
        elif isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in func_names:
            code = _call_str(n)
            if code not in shown:
                shown.add(code)
                lines.append(f"#   {code} → each argument is evaluated first, then the function body runs")
        elif isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == 'print':
            for a in n.args:
                if isinstance(a, ast.Call) and _name(a.func) in func_names:
                    code = f"print({_call_str(a)})"
                    if code not in shown:
                        shown.add(code)
                        lines.append(f"#   {_call_str(a)} runs first → then print() outputs the result")
        elif isinstance(n, ast.Compare):
            for i, op in enumerate(n.ops):
                cls_map = {ast.Eq: '==', ast.NotEq: '!=', ast.Lt: '<', ast.LtE: '<=',
                           ast.Gt: '>', ast.GtE: '>=', ast.In: 'in', ast.NotIn: 'not in'}
                op_s = ''
                for cls, s in cls_map.items():
                    if isinstance(op, cls): op_s = s
                if i < len(n.comparators):
                    compare = f"{_name(n.left)} {op_s} {_name(n.comparators[i])}"
                    if compare not in shown:
                        shown.add(compare)
                        lines.append(f"#   {compare} → evaluated as True or False (determines which branch runs)")

    if not shown:
        lines.append("#   (expressions are evaluated left to right, inner calls first)")

    return lines


def gen_execution_order(tree: ast.Module) -> list:
    lines = []
    lines.append("#")
    lines.append("# ------")
    lines.append("# EXECUTION ORDER:")
    lines.append("# Execution Order lists every statement in the sequence Python runs them.")
    lines.append("# 'def' and 'class' blocks are only stored, not executed yet.")
    lines.append("#")

    func_map = {f.name: f for f in tree.body if isinstance(f, ast.FunctionDef)}

    for i, stmt in enumerate(tree.body, 1):
        if isinstance(stmt, ast.FunctionDef):
            params = ', '.join(a.arg for a in stmt.args.args)
            lines.append(f"#   {i}. def {stmt.name}({params}) → stored in memory, not executed")
        elif isinstance(stmt, ast.ClassDef):
            bases = [b.id if isinstance(b, ast.Name) else '' for b in stmt.bases]
            cls = f"class {stmt.name}({', '.join(bases)})" if bases else f"class {stmt.name}"
            lines.append(f"#   {i}. {cls} → class definition stored")
        elif isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Call):
            call = stmt.value
            name = _name(call.func)
            inner = call.args[0] if call.args and isinstance(call.args[0], ast.Call) else None
            target = func_map.get(name) or (func_map.get(_name(inner.func)) if inner and _name(inner.func) in func_map else None)

            if name in func_map:
                params_str = ', '.join(a.arg for a in target.args.args)
                binds = ', '.join(f"{a.arg}={_name(b)}" for a, b in zip(target.args.args, call.args))
                lines.append(f"#   {i}. {_call_str(call)} → calls {name}({params_str}) with {binds}")
                for j, bs in enumerate(target.body, 1):
                    body = ast.unparse(bs)
                    for bl in body.split('\n'):
                        lines.append(f"#      → {i}.{j} {bl}")
            elif inner and _name(inner.func) in func_map:
                itarget = func_map[_name(inner.func)]
                iparams_str = ', '.join(a.arg for a in itarget.args.args)
                ibinds = ', '.join(f"{a.arg}={_name(b)}" for a, b in zip(itarget.args.args, inner.args))
                lines.append(f"#   {i}. {_call_str(call)}")
                lines.append(f"#      → calls {_name(inner.func)}({iparams_str}) with {ibinds}")
                for j, bs in enumerate(itarget.body, 1):
                    body = ast.unparse(bs)
                    for bl in body.split('\n'):
                        lines.append(f"#      → {i}.{j} {bl}")
            else:
                lines.append(f"#   {i}. {_call_str(call)}")
        elif isinstance(stmt, ast.Assign):
            targets = ', '.join(t.id if isinstance(t, ast.Name) else '?' for t in stmt.targets)
            lines.append(f"#   {i}. {targets} = ... → assigns value to variable")
        elif isinstance(stmt, ast.For):
            target = ast.unparse(stmt.target)
            lines.append(f"#   {i}. for {target} in {_name(stmt.iter)} → loops over each item")
            for j, bs in enumerate(stmt.body, 1):
                bcode = _code_line(bs)
                if bcode:
                    lines.append(f"#      → {i}.{j} {bcode}")
        elif isinstance(stmt, ast.While):
            lines.append(f"#   {i}. while ... → repeats as long as condition is true")
        elif isinstance(stmt, ast.If):
            lines.append(f"#   {i}. if ... → only one branch executes")
        elif isinstance(stmt, ast.Import):
            names = ', '.join(a.name for a in stmt.names)
            lines.append(f"#   {i}. import {names}")
        elif isinstance(stmt, ast.ImportFrom):
            names = ', '.join(a.name for a in stmt.names)
            lines.append(f"#   {i}. from {stmt.module} import {names}")
        elif isinstance(stmt, ast.Expr):
            lines.append(f"#   {i}. evaluates expression")
        else:
            lines.append(f"#   {i}. statement")

    return lines


def _code_line(node: ast.AST) -> str:
    if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
        return _call_str(node.value)
    if isinstance(node, ast.Assign):
        ts = ', '.join(t.id if isinstance(t, ast.Name) else '?' for t in node.targets)
        return f"{ts} = ..."
    return ''


def gen_execution_flow(tree: ast.Module) -> list:
    lines = []
    lines.append("#")
    lines.append("# ------")
    lines.append("# EXECUTION FLOW:")
    lines.append("# Execution Flow tracks how Python jumps between different parts of the")
    lines.append("# code — which blocks are skipped and where execution actually starts.")
    lines.append("#")

    func_names = {f.name for f in tree.body if isinstance(f, ast.FunctionDef)}
    class_names = {c.name for c in tree.body if isinstance(c, ast.ClassDef)}
    top_code = [n for n in tree.body
                if not isinstance(n, (ast.FunctionDef, ast.ClassDef, ast.Import, ast.ImportFrom))]
    has_loop = any(isinstance(n, (ast.For, ast.While)) for n in ast.walk(tree))
    has_if = any(isinstance(n, ast.If) for n in ast.walk(tree))

    if class_names:
        lines.append(f"#   Classes ({', '.join(class_names)}) are defined — methods are stored, not called")
    if func_names:
        lines.append(f"#   Functions ({', '.join(func_names)}) are defined — skipped at runtime, stored in memory")

    if not top_code:
        lines.append("#   No code runs at the top level — functions must be called externally")
    else:
        lines.append("#")
        lines.append("#   Execution begins at the top-level code (outside def/class blocks):")
        for stmt in top_code:
            if isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Call):
                call = stmt.value
                name = _name(call.func)
                inner = call.args[0] if call.args and isinstance(call.args[0], ast.Call) else None
                if name in func_names:
                    lines.append(f"#     {_call_str(call)} → jumps into {name}(), runs body, returns")
                elif inner and _name(inner.func) in func_names:
                    iname = _name(inner.func)
                    lines.append(f"#     {_call_str(call)} → {iname}() runs first → value passed to print()")
                else:
                    lines.append(f"#     {_call_str(call)}")
            elif isinstance(stmt, ast.For):
                target = ast.unparse(stmt.target)
                lines.append(f"#     for {target} in {_name(stmt.iter)} → runs body once per item")
            elif isinstance(stmt, ast.While):
                lines.append(f"#     while → checks condition before each iteration")
            elif isinstance(stmt, ast.If):
                lines.append(f"#     if → evaluates condition, runs matching branch")
            elif isinstance(stmt, ast.Assign):
                targets = ', '.join(t.id if isinstance(t, ast.Name) else '?' for t in stmt.targets)
                lines.append(f"#     {targets} = ... → stored in memory")
            else:
                lines.append(f"#     (statement runs)")

    if has_loop:
        lines.append("#")
        for n in ast.walk(tree):
            if isinstance(n, ast.For):
                lines.append(f"#   Loop: takes one item from {_name(n.iter)} each round, runs body, repeats until done")
                break
            elif isinstance(n, ast.While):
                lines.append(f"#   Loop: check condition → if True, run body → check again")
                break
    if has_if:
        lines.append(f"#   Branch: condition picks one path — other branches are skipped")

    return lines


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

        if pid <= 500: tier = 500
        elif pid <= 1000: tier = 1000
        elif pid <= 1500: tier = 1500
        else: tier = 2000

        try:
            tree = ast.parse(code)
        except SyntaxError:
            section = first_code_section(code)
            try:
                tree = ast.parse(section)
            except SyntaxError:
                print(f"  Skipping P{pid}")
                continue

        parts = []
        parts.extend(gen_syntax(tree))
        parts.extend(gen_evaluation_order(tree))
        parts.extend(gen_execution_order(tree))
        parts.extend(gen_execution_flow(tree))

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
                f.write(f'"""\nProblem {pid}:\n#\n{content}\n\n"""\n\n')
        print(f"Wrote {outfile} ({len(entries)} problems)")

    print("\nDone!")


if __name__ == '__main__':
    main()
