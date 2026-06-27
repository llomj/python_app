#!/usr/bin/env python3
# Generate syntax analysis files for all problems using AST analysis.
#
# Output: level1_{500,1000,1500,2000}_syntax.py using the same
# """ Problem N: """ marker format as the requirements files.
#
# For each problem, produces four sections:
#   Syntax         - keywords, structures, operators, patterns used
#   Evaluation Order - how expressions evaluate step by step
#   Execution Order  - statement-by-statement execution sequence
#   Execution Flow   - runtime control flow (branches, loops, calls)

import ast
import re
import sys
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


# ── AST analysis helpers ──────────────────────────────────────────────

def describe_node(node: ast.AST, indent: str = "") -> list[str]:
    """Return a list of description lines for a given AST node."""
    lines = []
    if isinstance(node, ast.FunctionDef):
        params = [a.arg for a in node.args.args]
        lines.append(f"{indent}Function '{node.name}' defined with parameters: {', '.join(params)}")
        for stmt in node.body:
            lines.extend(describe_node(stmt, indent + "  "))
    elif isinstance(node, ast.ClassDef):
        bases = [b.id if isinstance(b, ast.Name) else ast.dump(b) for b in node.bases]
        base_str = f"({', '.join(bases)})" if bases else ""
        lines.append(f"{indent}Class '{node.name}'{base_str} defined")
        for stmt in node.body:
            lines.extend(describe_node(stmt, indent + "  "))
    elif isinstance(node, ast.Return):
        if node.value:
            lines.append(f"{indent}Return statement: returns the computed value")
        else:
            lines.append(f"{indent}Return statement: returns None")
    elif isinstance(node, ast.Assign):
        targets = [ast.dump(t) if isinstance(t, (ast.Tuple, ast.List)) else (t.id if isinstance(t, ast.Name) else 'subscript') for t in node.targets]
        lines.append(f"{indent}Assignment: {', '.join(targets)} = <expression>")
    elif isinstance(node, ast.AugAssign):
        op = _op_name(node.op)
        target = node.target.id if isinstance(node.target, ast.Name) else 'target'
        lines.append(f"{indent}Augmented assignment: {target} {op}= <expression>")
    elif isinstance(node, ast.For):
        target = ast.dump(node.target) if isinstance(node.target, (ast.Tuple, ast.List)) else (node.target.id if isinstance(node.target, ast.Name) else 'target')
        iter_name = _safe_name(node.iter)
        lines.append(f"{indent}For loop: iterating over {iter_name}")
        for stmt in node.body:
            lines.extend(describe_node(stmt, indent + "  "))
    elif isinstance(node, ast.While):
        lines.append(f"{indent}While loop: conditionally repeating")
        for stmt in node.body:
            lines.extend(describe_node(stmt, indent + "  "))
    elif isinstance(node, ast.If):
        lines.append(f"{indent}If condition: branching based on condition")
        for stmt in node.body:
            lines.extend(describe_node(stmt, indent + "  "))
        if node.orelse:
            lines.append(f"{indent}else: alternative branch")
            for stmt in node.orelse:
                lines.extend(describe_node(stmt, indent + "  "))
    elif isinstance(node, ast.Try):
        lines.append(f"{indent}Try block: exception handling")
        for stmt in node.body:
            lines.extend(describe_node(stmt, indent + "  "))
        for handler in node.handlers:
            lines.append(f"{indent}Except: catches {handler.type.id if handler.type else 'Exception'}")
            for stmt in handler.body:
                lines.extend(describe_node(stmt, indent + "  "))
    elif isinstance(node, ast.Expr):
        if isinstance(node.value, ast.Call):
            call = _describe_call(node.value)
            lines.append(f"{indent}Call: {call}")
        elif isinstance(node.value, ast.Constant):
            lines.append(f"{indent}Expression: literal value")
    elif isinstance(node, ast.Print) if hasattr(ast, 'Print') else False:
        lines.append(f"{indent}Print statement")
    return lines


def _op_name(op: ast.operator) -> str:
    op_map = {
        ast.Add: '+', ast.Sub: '-', ast.Mult: '*', ast.Div: '/',
        ast.FloorDiv: '//', ast.Mod: '%', ast.Pow: '**',
        ast.LShift: '<<', ast.RShift: '>>', ast.BitOr: '|',
        ast.BitXor: '^', ast.BitAnd: '&',
    }
    for cls, name in op_map.items():
        if isinstance(op, cls):
            return name
    return '?'


def _safe_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return f"{_safe_name(node.value)}.{node.attr}"
    if isinstance(node, ast.Call):
        return f"{_safe_name(node.func)}(...)"
    if isinstance(node, ast.Constant):
        return repr(node.value)
    return 'expression'


def _describe_call(node: ast.Call) -> str:
    func_name = _safe_name(node.func)
    args = []
    for a in node.args:
        if isinstance(a, ast.Name):
            args.append(a.id)
        elif isinstance(a, ast.Constant):
            args.append(repr(a.value))
        elif isinstance(a, ast.Call):
            args.append(_safe_name(a))
        elif isinstance(a, ast.BinOp):
            args.append(f"<expr>")
        else:
            args.append('value')
    return f"{func_name}({', '.join(args)})"


def gather_functions(tree: ast.Module) -> list[ast.FunctionDef]:
    """Get top-level function definitions."""
    return [n for n in tree.body if isinstance(n, ast.FunctionDef)]


def gather_classes(tree: ast.Module) -> list[ast.ClassDef]:
    return [n for n in tree.body if isinstance(n, ast.ClassDef)]


def gather_top_level_calls(tree: ast.Module) -> list[ast.Call]:
    calls = []
    for n in tree.body:
        if isinstance(n, ast.Expr) and isinstance(n.value, ast.Call):
            calls.append(n.value)
    return calls


def get_keywords_used(tree: ast.Module) -> list[str]:
    keywords = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.FunctionDef):
            keywords.add('def')
        elif isinstance(n, ast.ClassDef):
            keywords.add('class')
        elif isinstance(n, ast.If):
            keywords.add('if/elif/else')
        elif isinstance(n, ast.For):
            keywords.add('for')
        elif isinstance(n, ast.While):
            keywords.add('while')
        elif isinstance(n, ast.Try):
            keywords.add('try/except')
        elif isinstance(n, ast.Return):
            keywords.add('return')
        elif isinstance(n, ast.Raise):
            keywords.add('raise')
        elif isinstance(n, ast.With):
            keywords.add('with')
        elif isinstance(n, ast.AsyncFunctionDef):
            keywords.add('async def')
        elif isinstance(n, ast.Lambda):
            keywords.add('lambda')
        elif isinstance(n, ast.Assert):
            keywords.add('assert')
        elif isinstance(n, ast.Global):
            keywords.add('global')
        elif isinstance(n, ast.Nonlocal):
            keywords.add('nonlocal')
        elif isinstance(n, ast.Delete):
            keywords.add('del')
        elif isinstance(n, ast.Pass):
            keywords.add('pass')
        elif isinstance(n, ast.Break):
            keywords.add('break')
        elif isinstance(n, ast.Continue):
            keywords.add('continue')
        elif isinstance(n, ast.Yield):
            keywords.add('yield')
    return sorted(keywords)


def get_operators_used(tree: ast.Module) -> list[str]:
    ops = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.BinOp):
            ops.add(_op_name(n.op))
        elif isinstance(n, ast.UnaryOp):
            if isinstance(n.op, ast.Not):
                ops.add('not')
            elif isinstance(n.op, ast.USub):
                ops.add('-')
            elif isinstance(n.op, ast.UAdd):
                ops.add('+')
            elif isinstance(n.op, ast.Invert):
                ops.add('~')
        elif isinstance(n, ast.Compare):
            for op in n.ops:
                if isinstance(op, ast.Eq):
                    ops.add('==')
                elif isinstance(op, ast.NotEq):
                    ops.add('!=')
                elif isinstance(op, ast.Lt):
                    ops.add('<')
                elif isinstance(op, ast.LtE):
                    ops.add('<=')
                elif isinstance(op, ast.Gt):
                    ops.add('>')
                elif isinstance(op, ast.GtE):
                    ops.add('>=')
                elif isinstance(op, ast.In):
                    ops.add('in')
                elif isinstance(op, ast.NotIn):
                    ops.add('not in')
                elif isinstance(op, ast.Is):
                    ops.add('is')
                elif isinstance(op, ast.IsNot):
                    ops.add('is not')
        elif isinstance(n, ast.BoolOp):
            if isinstance(n.op, ast.And):
                ops.add('and')
            elif isinstance(n.op, ast.Or):
                ops.add('or')
        elif isinstance(n, ast.Subscript):
            ops.add('[]')
        elif isinstance(n, ast.Call):
            ops.add('()')
        elif isinstance(n, ast.Attribute):
            ops.add('.')
    return sorted(ops, key=lambda x: (len(x), x))


def get_builtins_used(tree: ast.Module) -> list[str]:
    builtins = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name):
            builtins.add(n.func.id)
    return sorted(builtins)


def get_control_structures(tree: ast.Module) -> list[str]:
    structures = []
    for n in ast.walk(tree):
        if isinstance(n, ast.If) and not any(isinstance(p, ast.If) for p in ast.walk(tree) if p is not n):
            structures.append('if/else conditional branching')
            break
    for n in ast.walk(tree):
        if isinstance(n, ast.For):
            structures.append('for loop iteration')
            break
    for n in ast.walk(tree):
        if isinstance(n, ast.While):
            structures.append('while loop')
            break
    for n in ast.walk(tree):
        if isinstance(n, ast.Try):
            structures.append('try/except error handling')
            break
    for n in ast.walk(tree):
        if isinstance(n, ast.ListComp):
            structures.append('list comprehension')
            break
    for n in ast.walk(tree):
        if isinstance(n, ast.DictComp):
            structures.append('dict comprehension')
            break
    for n in ast.walk(tree):
        if isinstance(n, ast.GeneratorExp):
            structures.append('generator expression')
            break
    for n in ast.walk(tree):
        if isinstance(n, ast.Lambda):
            structures.append('lambda expression')
            break
    return structures


# ── Section generators ────────────────────────────────────────────────

def gen_syntax(tree: ast.Module, code: str) -> str:
    lines = []
    funcs = gather_functions(tree)
    classes = gather_classes(tree)
    keywords = get_keywords_used(tree)
    operators = get_operators_used(tree)
    builtins = get_builtins_used(tree)
    structures = get_control_structures(tree)

    lines.append("▸ SYNTAX HIGHLIGHTS")
    lines.append("")

    if classes:
        lines.append(f"  Classes defined: {', '.join(c.name for c in classes)}")
        for c in classes:
            methods = [n.name for n in c.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
            if methods:
                lines.append(f"    {c.name} methods: {', '.join(methods)}")

    if funcs:
        lines.append(f"  Functions defined: {len(funcs)}")
        for f in funcs:
            params = [a.arg for a in f.args.args]
            default_count = len(f.args.defaults)
            lines.append(f"    def {f.name}({', '.join(params)})")
            if default_count:
                lines.append(f"      ({default_count} parameter(s) with default values)")
            returns = [n for n in ast.walk(f) if isinstance(n, ast.Return)]
            if returns:
                lines.append(f"      Returns a value via 'return' keyword")

    if keywords:
        lines.append(f"  Keywords used: {', '.join(keywords)}")
    if operators:
        lines.append(f"  Operators used: {', '.join(operators)}")
    if structures:
        lines.append(f"  Control structures: {'; '.join(structures)}")
    if builtins:
        lines.append(f"  Functions called: {', '.join(builtins)}")

    # Check for specific patterns
    has_input = any(isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == 'input' for n in ast.walk(tree))
    has_print = any(isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == 'print' for n in ast.walk(tree))
    if has_input:
        lines.append("  User input: uses input() for interactive data entry")
    if has_print:
        lines.append("  Output: uses print() to display results")
    if any(isinstance(n, (ast.List, ast.Tuple, ast.Dict, ast.Set)) for n in ast.walk(tree)):
        lines.append("  Data structures: uses Python collections (list, tuple, dict, set)")

    return '\n'.join(lines)


def gen_evaluation_order(tree: ast.Module, code: str) -> str:
    lines = []
    lines.append("▸ EVALUATION ORDER")
    lines.append("")
    lines.append("  Python evaluates expressions using left-to-right, inner-to-outer rules:")

    # Find key expression patterns in the code
    expr_patterns = []

    for n in ast.walk(tree):
        if isinstance(n, ast.BinOp):
            left = _safe_name(n.left)
            right = _safe_name(n.right)
            expr_patterns.append((n.lineno, f"Binary operation: {left} {_op_name(n.op)} {right}"))

    for n in ast.walk(tree):
        if isinstance(n, ast.Call):
            args_info = []
            for a in n.args:
                if isinstance(a, ast.Name):
                    args_info.append(a.id)
                elif isinstance(a, ast.Constant):
                    args_info.append(repr(a.value))
                elif isinstance(a, ast.BinOp):
                    args_info.append('computed expression')
                else:
                    args_info.append('value')
            expr_patterns.append((n.lineno, f"Function call: {_safe_name(n.func)}({', '.join(args_info)})"))

    for n in ast.walk(tree):
        if isinstance(n, ast.If):
            expr_patterns.append((n.lineno, "Condition branch: evaluates boolean expression first"))

    for n in ast.walk(tree):
        if isinstance(n, ast.Assign):
            for t in n.targets:
                if isinstance(t, ast.Name):
                    expr_patterns.append((n.lineno, f"Assignment: right side evaluated first, then stored in '{t.id}'"))

    expr_patterns.sort(key=lambda x: x[0])

    if expr_patterns:
        lines.append("")
        for lineno, desc in expr_patterns:
            lines.append(f"  • {desc}")
    else:
        lines.append("")
        lines.append("  • Top-level expressions evaluated sequentially")

    return '\n'.join(lines)


def gen_execution_order(tree: ast.Module, code: str) -> str:
    lines = []
    lines.append("▸ EXECUTION ORDER")
    lines.append("")

    # Walk top-level body
    lines.append("  Statement execution sequence (top to bottom):")
    for i, stmt in enumerate(tree.body, 1):
        desc = _describe_stmt_exec(stmt)
        lines.append(f"  {i}. {desc}")

    return '\n'.join(lines)


def _describe_stmt_exec(node: ast.AST) -> str:
    if isinstance(node, ast.FunctionDef):
        return f"Define function '{node.name}' (stored in memory, not executed yet)"
    elif isinstance(node, ast.ClassDef):
        return f"Define class '{node.name}'"
    elif isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
        call = _describe_call(node.value)
        return f"Execute function call: {call}"
    elif isinstance(node, ast.Assign):
        targets = [t.id if isinstance(t, ast.Name) else 'target' for t in node.targets]
        return f"Assign value to variable: {', '.join(targets)}"
    elif isinstance(node, ast.For):
        iter_name = _safe_name(node.iter)
        return f"For loop: iterate over {iter_name}"
    elif isinstance(node, ast.While):
        return "While loop: repeat while condition is true"
    elif isinstance(node, ast.If):
        return "If/else: conditional execution"
    elif isinstance(node, ast.Try):
        return "Try block: execute with error handling"
    elif isinstance(node, ast.Return):
        return "Return: exit function and return value"
    elif isinstance(node, ast.Import):
        names = [a.name for a in node.names]
        return f"Import module: {', '.join(names)}"
    elif isinstance(node, ast.ImportFrom):
        names = [a.name for a in node.names]
        return f"Import from {node.module}: {', '.join(names)}"
    elif isinstance(node, ast.Pass):
        return "Pass: no operation"
    elif isinstance(node, ast.Break):
        return "Break: exit current loop"
    elif isinstance(node, ast.Continue):
        return "Continue: skip to next loop iteration"
    elif isinstance(node, ast.Expr):
        return "Evaluate expression (result discarded)"
    else:
        return f"Execute {type(node).__name__}"


def gen_execution_flow(tree: ast.Module, code: str) -> str:
    lines = []
    lines.append("▸ EXECUTION FLOW")
    lines.append("")

    funcs = gather_functions(tree)
    classes = gather_classes(tree)
    top_calls = [n for n in tree.body if isinstance(n, ast.Expr) and isinstance(n.value, ast.Call)]

    if classes:
        lines.append("  Class definition phase:")
        for c in classes:
            methods = [n.name for n in c.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
            lines.append(f"    - Class '{c.name}' is defined with methods: {', '.join(methods)}")
            for m in c.body:
                if isinstance(m, ast.FunctionDef):
                    if m.name == '__init__':
                        lines.append(f"      • __init__ runs automatically on instantiation to initialize attributes")
                    else:
                        lines.append(f"      • '{m.name}' is a regular method — runs when called on an instance")

    if funcs:
        lines.append("  Function definition phase:")
        for f in funcs:
            lines.append(f"    - '{f.name}' is defined but NOT executed until called")

    if top_calls:
        lines.append("  Runtime execution (top-level code):")
        for expr in top_calls:
            call = expr.value
            func_name = _safe_name(call.func)
            lines.append(f"    - {func_name}() is invoked")
            if any(f.name == func_name for f in funcs):
                lines.append(f"      → Execution jumps to the function body of '{func_name}'")
                lines.append(f"      → Function executes its statements sequentially")
                lines.append(f"      → Returns result to the caller")
                lines.append(f"      → Result is printed to console")

    has_loops = any(isinstance(n, (ast.For, ast.While)) for n in ast.walk(tree))
    if has_loops:
        lines.append("  Loop execution flow:")
        for n in ast.walk(tree):
            if isinstance(n, ast.For):
                iter_name = _safe_name(n.iter)
                lines.append(f"    - For loop iterates over {iter_name}, one element at a time")
                lines.append(f"    - Body executes once per element, then loop exits")
            elif isinstance(n, ast.While):
                lines.append(f"    - While loop checks condition before each iteration")
                lines.append(f"    - Body repeats as long as condition remains True")

    has_conditionals = any(isinstance(n, ast.If) for n in ast.walk(tree))
    if has_conditionals:
        lines.append("  Conditional flow:")
        lines.append("    - If condition is evaluated as True → enters the if-block")
        lines.append("    - If condition is False → skips to else/elif or continues")

    return '\n'.join(lines)


# ── Main ──────────────────────────────────────────────────────────────

def main():
    with open(TS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    id_matches = list(re.finditer(r'"id": (\d+),', content))
    total = len(id_matches)

    # Group problem entries by tier
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

        sol_raw = content[val_start:close_quote]
        code = unescape_ts(sol_raw)

        # Insert the # Using function approach delimiter so we only analyze up to that point,
        # but actually we want the full solution — all alternatives, all code.
        # Actually no — the syntax analysis is about the *solution code* which includes everything.
        # But the alternatives start after the first approach. Let's analyze the full solution.

        # Determine tier
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
            # Try extracting just the code before alternatives (first section)
            alt_markers = ['# Using built-in approach', '# Using manual approach',
                           '# Script approach', '# Direct approach',
                           '# Using function approach']
            alt_pos = None
            for marker in alt_markers:
                p = code.find(marker)
                if p is not None and (alt_pos is None or (p != -1 and (alt_pos is None or p < alt_pos))):
                    alt_pos = p if p != -1 else None
            if alt_pos:
                code_section = code[:alt_pos].strip()
            else:
                code_section = code.strip()
            # If still fails, try even tighter
            try:
                tree = ast.parse(code_section if code_section else code.strip())
            except SyntaxError:
                print(f"  Skipping P{pid} — syntax error in source")
                continue

        # Generate all sections
        parts = []
        parts.append(gen_syntax(tree, code))
        parts.append("")
        parts.append(gen_evaluation_order(tree, code))
        parts.append("")
        parts.append(gen_execution_order(tree, code))
        parts.append("")
        parts.append(gen_execution_flow(tree, code))

        full = '\n'.join(parts)
        tiers[tier].append((pid, full))

        if pid % 200 == 0:
            print(f"  Processed P{pid}...")

    # Write tier files
    for tier, entries in sorted(tiers.items()):
        if not entries:
            continue
        outfile = OUT_DIR / f'level1_{tier}_syntax.py'
        with open(outfile, 'w', encoding='utf-8') as f:
            f.write(f'# Syntax documentation for level 1 (problems 1-{tier})\n')
            f.write(f'# Auto-generated by gen_syntax_files.py\n\n')
            for pid, content in entries:
                f.write(f'"""\nProblem {pid}:\n')
                f.write(f'{content}\n')
                f.write(f'"""\n\n')
        print(f"Wrote {outfile} ({len(entries)} problems)")

    print("\nDone!")


if __name__ == '__main__':
    main()
