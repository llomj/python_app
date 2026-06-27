#!/usr/bin/env python3
# Generate comment-formatted syntax docs for every problem.
#
# Output lines are Python comments (#) so CodeMirror renders them
# in the theme's comment color (gray), not mixed colors.
#
# Four sections per problem:
#   SYNTAX          — what Python features this code uses
#   EVALUATION ORDER — how each expression is broken down step-by-step
#   EXECUTION ORDER  — what runs and in what sequence
#   EXECUTION FLOW   — how control jumps (function calls, loops, branches)

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
    if isinstance(node, ast.Dict):
        return '{...}'
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        return f"-{_name(node.operand)}"
    return '?'


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


def _func_signature(f: ast.FunctionDef) -> str:
    params = [a.arg for a in f.args.args]
    return f"def {f.name}({', '.join(params)})"


# ── Section generators ──────────────────────────────────────────────

def gen_syntax(tree: ast.Module) -> str:
    """What Python features are used."""
    lines = []
    lines.append("#")
    lines.append("# ===== SYNTAX =====")

    funcs = [n for n in tree.body if isinstance(n, ast.FunctionDef)]
    classes = [n for n in tree.body if isinstance(n, ast.ClassDef)]

    if classes:
        for c in classes:
            methods = [n.name for n in c.body if isinstance(n, ast.FunctionDef)]
            bases = [b.id if isinstance(b, ast.Name) else '?' for b in c.bases]
            if bases:
                lines.append(f"#   class {c.name}({', '.join(bases)}) — inherits from parent")
            else:
                lines.append(f"#   class {c.name} — defines a new type")
            for m in methods:
                lines.append(f"#     def {m} — method of {c.name}")

    if funcs:
        lines.append(f"#   {_func_signature(funcs[0])}")
        seen_returns = False
        seen_calls = set()
        for f in funcs:
            returns = any(isinstance(n, ast.Return) for n in ast.walk(f))
            if returns and not seen_returns:
                lines.append(f"#   return — exits the function and sends back a value")
                seen_returns = True
            calls = [n for n in ast.walk(f) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)]
            for c in calls:
                if c.func.id == 'print':
                    continue
                if c.func.id not in seen_calls:
                    lines.append(f"#   {c.func.id}() — built-in function call")
                    seen_calls.add(c.func.id)
            if not returns:
                lines.append(f"#   (no return — the function prints directly instead of returning)")

    # Gather keywords & operators from AST
    def _walk_keywords():
        ks = set()
        for n in ast.walk(tree):
            if isinstance(n, ast.For): ks.add('for'); ks.add('in')
            elif isinstance(n, ast.While): ks.add('while')
            elif isinstance(n, ast.If): ks.add('if/elif/else')
            elif isinstance(n, ast.Try): ks.add('try/except')
            elif isinstance(n, ast.Lambda): ks.add('lambda')
            elif isinstance(n, ast.With): ks.add('with')
            elif isinstance(n, ast.Break): ks.add('break')
            elif isinstance(n, ast.Continue): ks.add('continue')
            elif isinstance(n, (ast.ListComp, ast.DictComp, ast.GeneratorExp)): ks.add('comprehension')
        return ks
    for k in sorted(_walk_keywords()):
        lines.append(f"#   {k}")

    # Check operators
    def _walk_ops():
        ops = set()
        for n in ast.walk(tree):
            if isinstance(n, ast.BinOp): ops.add(_op_name(n.op))
            elif isinstance(n, ast.Compare):
                for op in n.ops:
                    cls_map = {ast.Eq: '==', ast.NotEq: '!=', ast.Lt: '<', ast.LtE: '<=',
                               ast.Gt: '>', ast.GtE: '>=', ast.In: 'in', ast.NotIn: 'not in',
                               ast.Is: 'is', ast.IsNot: 'is not'}
                    for cls, s in cls_map.items():
                        if isinstance(op, cls): ops.add(s)
            elif isinstance(n, ast.BoolOp):
                ops.add('and' if isinstance(n.op, ast.And) else 'or')
        return ops
    ops = [o for o in ['+', '-', '*', '/', '//', '%', '**', '==', '!=', '<', '>', '<=', '>=',
                        'and', 'or', 'not', 'in', 'is']
           if o in _walk_ops()]
    if ops:
        lines.append(f"#   operators: {' '.join(ops)}")

    return '\n'.join(lines)


def gen_evaluation_order(tree: ast.Module, code: str = '') -> str:
    """Step-by-step expression breakdown."""
    lines = []
    lines.append("#")
    lines.append("# ===== EVALUATION ORDER =====")

    func_names = {f.name: f for f in tree.body if isinstance(f, ast.FunctionDef)}
    has_expr = False

    for n in ast.walk(tree):
        if isinstance(n, ast.BinOp):
            has_expr = True
            left = _name(n.left)
            right = _name(n.right)
            op = _op_name(n.op)
            lines.append(f"#   {left} {op} {right}: first get {left}, then get {right}, then compute {left} {op} {right}")
        elif isinstance(n, ast.Call) and isinstance(n.func, ast.Name):
            if n.func.id in func_names:
                has_expr = True
                args_desc = []
                for a in n.args:
                    if isinstance(a, ast.Constant):
                        args_desc.append(f"gets the literal {repr(a.value)}")
                    elif isinstance(a, ast.Name):
                        args_desc.append(f"looks up variable '{a.id}'")
                    elif isinstance(a, ast.BinOp):
                        args_desc.append(f"computes the expression first")
                    else:
                        args_desc.append("resolves the value")
                prefix = f" {', '.join(args_desc)}, then runs the function body" if args_desc else " — no arguments needed"
                lines.append(f"#   {_call_str(n)}:{prefix}")
            elif n.func.id == 'print' and any(isinstance(a, ast.Call) for a in n.args):
                has_expr = True
                for a in n.args:
                    if isinstance(a, ast.Call):
                        inner_name = _name(a.func)
                        if inner_name in func_names:
                            lines.append(f"#   print({_call_str(a)}): the inner {inner_name}() executes FIRST, then print() outputs the result")
                        else:
                            lines.append(f"#   print({_call_str(a)}): inner expression resolves first, then print() outputs")

    # Conditions
    for n in ast.walk(tree):
        if isinstance(n, ast.If):
            has_expr = True
            for child in ast.walk(n):
                if isinstance(child, ast.Compare):
                    left = _name(child.left)
                    for i, op in enumerate(child.ops):
                        cls_map = {ast.Eq: '==', ast.NotEq: '!=', ast.Lt: '<', ast.LtE: '<=',
                                   ast.Gt: '>', ast.GtE: '>=', ast.In: 'in', ast.NotIn: 'not in'}
                        op_s = ''
                        for cls, s in cls_map.items():
                            if isinstance(op, cls): op_s = s
                        if i < len(child.comparators):
                            right = _name(child.comparators[i])
                            lines.append(f"#   {left} {op_s} {right}: is this True or False? The answer picks which branch")

    if not has_expr:
        lines.append(f"#   expressions evaluate left-to-right, inner calls first")

    return '\n'.join(lines)


def gen_execution_order(tree: ast.Module, code: str = '') -> str:
    """Top-to-bottom statement sequence."""
    lines = []
    lines.append("#")
    lines.append("# ===== EXECUTION ORDER =====")

    func_map = {f.name: f for f in tree.body if isinstance(f, ast.FunctionDef)}

    for i, stmt in enumerate(tree.body, 1):
        desc = _stmt_desc(stmt)
        lines.append(f"#   {i}. {desc}")

        # If it's a function call, show what happens inside
        if isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Call):
            call = stmt.value
            name = _name(call.func)
            # The call might be print(some_func(...)) — trace the inner call
            inner_call = None
            if call.args and isinstance(call.args[0], ast.Call):
                inner_call = call.args[0]
            target_func = func_map.get(name) or (func_map.get(_name(inner_call.func)) if inner_call else None)
            if target_func and target_func != name:
                pass  # We'll handle it below with inner_call
            
            if name in func_map:
                f = func_map[name]
                params = [a.arg for a in f.args.args]
                if params:
                    arg_values = [f"{p}={_name(a)}" for p, a in zip(params, call.args)]
                    lines.append(f"#       with: {', '.join(arg_values)}")
                for j, body_stmt in enumerate(f.body, 1):
                    body_desc = _stmt_desc(body_stmt)
                    lines.append(f"#         {i}.{j} {body_desc}")
            elif inner_call and _name(inner_call.func) in func_map:
                f = func_map[_name(inner_call.func)]
                params = [a.arg for a in f.args.args]
                if params:
                    arg_values = [f"{p}={_name(a)}" for p, a in zip(params, inner_call.args)]
                    lines.append(f"#       calls {_name(inner_call.func)} with: {', '.join(arg_values)}")
                for j, body_stmt in enumerate(f.body, 1):
                    body_desc = _stmt_desc(body_stmt)
                    lines.append(f"#         {i}.{j} {body_desc}")
        elif isinstance(stmt, ast.For):
            # Show loop body steps
            for j, body_stmt in enumerate(stmt.body, 1):
                body_desc = _stmt_desc(body_stmt)
                lines.append(f"#       {i}.{j} {body_desc}")

    return '\n'.join(lines)


def _stmt_desc(node: ast.AST) -> str:
    if isinstance(node, ast.FunctionDef):
        return f"Define {_func_signature(node)} — stored for later"
    if isinstance(node, ast.ClassDef):
        bases = [b.id if isinstance(b, ast.Name) else '?' for b in node.bases]
        return f"Define class {node.name}({', '.join(bases)})" if bases else f"Define class {node.name}"
    if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
        return f"Run {_call_str(node.value)}"
    if isinstance(node, ast.Assign):
        targets = [t.id if isinstance(t, ast.Name) else '?' for t in node.targets]
        return f"Assign to {', '.join(targets)}"
    if isinstance(node, ast.AugAssign):
        t = node.target.id if isinstance(node.target, ast.Name) else '?'
        return f"Update {t} {_op_name(node.op)}= ..."
    if isinstance(node, ast.For):
        return f"For loop over {_name(node.iter)}"
    if isinstance(node, ast.While):
        return "While loop"
    if isinstance(node, ast.If):
        return "If statement (one branch runs)"
    if isinstance(node, ast.Try):
        return "Try block (error handling)"
    if isinstance(node, ast.Return):
        return "Return from function"
    if isinstance(node, ast.Import):
        return f"Import {', '.join(a.name for a in node.names)}"
    if isinstance(node, ast.ImportFrom):
        return f"Import {', '.join(a.name for a in node.names)} from {node.module}"
    if isinstance(node, ast.Pass):
        return "Pass (placeholder)"
    if isinstance(node, ast.Break):
        return "Break out of loop"
    if isinstance(node, ast.Continue):
        return "Continue to next iteration"
    if isinstance(node, ast.Expr):
        return "Evaluate expression"
    return str(type(node).__name__)


def gen_execution_flow(tree: ast.Module) -> str:
    """How control jumps around at runtime."""
    lines = []
    lines.append("#")
    lines.append("# ===== EXECUTION FLOW =====")

    funcs = [n for n in tree.body if isinstance(n, ast.FunctionDef)]
    classes = [n for n in tree.body if isinstance(n, ast.ClassDef)]
    imports = [n for n in tree.body if isinstance(n, (ast.Import, ast.ImportFrom))]
    top_code = [n for n in tree.body if not isinstance(n, (ast.FunctionDef, ast.ClassDef, ast.Import, ast.ImportFrom))]

    if imports:
        lines.append(f"#   Python loads {len(imports)} import(s) first")

    if classes:
        lines.append(f"#   Class definitions are processed (methods stored)")
        for c in classes:
            inits = [n for n in c.body if isinstance(n, ast.FunctionDef) and n.name == '__init__']
            if inits:
                lines.append(f"#   {c.name}.__init__ runs automatically when you create an instance")

    if funcs:
        names = [f.name for f in funcs]
        lines.append(f"#   def lines are SKIPPED during execution — functions {', '.join(names)} are just stored")
    if not top_code:
        lines.append(f"#   Nothing runs at the top level — functions are only called externally")
    else:
        lines.append(f"#   Execution starts at the non-def lines below:")

    has_loop = any(isinstance(n, (ast.For, ast.While)) for n in ast.walk(tree))
    has_if = any(isinstance(n, ast.If) for n in ast.walk(tree))

    # Describe each top-level action
    func_names = {f.name for f in funcs}
    for stmt in top_code:
        desc = ""
        if isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Call):
            call = stmt.value
            name = _name(call.func)
            if name in func_names:
                desc = f"   {_call_str(call)} → jumps into function, runs body, returns result → printed"
            elif name == 'print':
                inner = ''
                if call.args and isinstance(call.args[0], ast.Call):
                    inner_call = call.args[0]
                    inner_name = _name(inner_call.func)
                    if inner_name in func_names:
                        desc = f"   print({_call_str(inner_call)}) → function runs first, then print shows the result"
                    else:
                        desc = f"   {_call_str(call)}"
                else:
                    desc = f"   {_call_str(call)}"
            else:
                desc = f"   {_call_str(call)}"
        elif isinstance(stmt, ast.For):
            desc = f"   for loop runs its body once per item"
        elif isinstance(stmt, ast.While):
            desc = f"   while loop repeats until condition is False"
        elif isinstance(stmt, ast.If):
            desc = f"   if checks a condition and runs ONE branch"
        elif isinstance(stmt, ast.Assign):
            targets = [t.id if isinstance(t, ast.Name) else '?' for t in stmt.targets]
            desc = f"   {', '.join(targets)} = ... (stored in memory)"
        else:
            desc = f"   top-level statement runs"

        if desc:
            lines.append(f"#   {desc}")

    if has_loop:
        lines.append(f"#")
        for n in ast.walk(tree):
            if isinstance(n, ast.For):
                lines.append(f"#   Loop: grabs one item from {_name(n.iter)} each round")
                break
        for n in ast.walk(tree):
            if isinstance(n, ast.While):
                lines.append(f"#   Loop: checks condition → if True runs body, then checks again")
                break

    if has_if:
        lines.append(f"#   Branch: only the True branch executes; the rest is skipped")

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

        # Try to parse full code, fall back to first section
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
            gen_syntax(tree),
            gen_evaluation_order(tree),
            gen_execution_order(tree),
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
