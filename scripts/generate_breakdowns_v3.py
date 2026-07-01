#!/usr/bin/env python3
"""
V3 breakdown generator — metadata-driven template engine.
Extracts rich metadata (functions, concepts, patterns) from each exercise
and generates specific, correct step-by-step guides without AI.
"""
import re, json

EXERCISES_FILE = '/Users/moll/Desktop/python_app/exercises.ts'


def read_exercises(path):
    with open(path, 'r') as f:
        content = f.read()
    lines = content.split('\n')

    start_idx = 0
    for i, line in enumerate(lines):
        if 'Exercise[] = [' in line or ('EXERCISES:' in line and '[' in line):
            start_idx = i + 1
            break

    blocks = []
    in_ex = False
    depth = 0
    cur = []
    for i in range(start_idx, len(lines)):
        ob = lines[i].count('{')
        cb = lines[i].count('}')
        if '{' in lines[i] and not in_ex:
            in_ex = True
            depth = ob - cb
            cur = [(lines[i], i)]
        elif in_ex:
            cur.append((lines[i], i))
            depth += ob - cb
            if depth <= 0:
                blocks.append(cur)
                cur = []
                in_ex = False
    return lines, blocks


def get_field(block, field):
    full = ''.join(l for l, _ in block)
    m = re.search(r'"' + field + r'":\s*"((?:[^"\\]|\\.)*)"', full)
    return m.group(1) if m else ''

def get_id(block):
    full = ''.join(l for l, _ in block)
    m = re.search(r'"id":\s*(\d+)', full)
    return int(m.group(1)) if m else 0


# ─── EXERCISE METADATA EXTRACTION ──────────────────────────────

def extract_metadata(desc, initial_code):
    """Analyze a description + initialCode and return a metadata dict."""
    meta = {}
    d = desc.lower()
    full = desc + ' ' + initial_code

    # 1. Function names (from description backticks)
    fn_matches = re.findall(r'`(\w+)`', desc)
    # Filter out keywords and non-function-like names
    keywords = {'true', 'false', 'none', 'and', 'or', 'not', 'if', 'else', 'elif',
                'for', 'while', 'in', 'is', 'def', 'class', 'return', 'import',
                'from', 'as', 'with', 'try', 'except', 'finally', 'raise',
                'lambda', 'yield', 'pass', 'break', 'continue'}
    fns = [f for f in fn_matches if f.lower() not in keywords and len(f) > 1]
    meta['functions'] = fns

    # 2. Key concepts
    meta['concepts'] = []
    if re.search(r'\*\*kwargs|kwargs', d): meta['concepts'].append('kwargs')
    if re.search(r'\*args', d): meta['concepts'].append('args')
    if re.search(r'\bclass\b', d): meta['concepts'].append('class')
    if re.search(r'\binherit\b|\bderived\b|\bsubclass\b|\bbase\b.*\bclass\b', d): meta['concepts'].append('inheritance')
    if re.search(r'\bdecorator\b|@\w+', d) and not re.search(r'@property|@\w+\.(setter|deleter)', d): meta['concepts'].append('decorator')
    if re.search(r'\brecursi', d): meta['concepts'].append('recursion')
    if re.search(r'\byield\b|\bgenerator\b', d): meta['concepts'].append('generator')
    if re.search(r'\blambda\b', d): meta['concepts'].append('lambda')
    if re.search(r'\bmap\b', d): meta['concepts'].append('map')
    if re.search(r'\bfilter\b', d): meta['concepts'].append('filter')
    if re.search(r'\breduce\b', d): meta['concepts'].append('reduce')
    if re.search(r'\bcomprehension\b', d): meta['concepts'].append('comprehension')
    if re.search(r'\bcontext.manager\b|__enter__|__exit__', d): meta['concepts'].append('context_manager')
    if re.search(r'__init__|__str__|__repr__|__len__|__getitem__|__setitem__|__delitem__|__contains__|__iter__|__next__|__call__|__eq__|__hash__|__enter__|__exit__|__add__', d): meta['concepts'].append('magic_methods')
    if re.search(r'\bproperty\b|@property|@\w+\.setter|@\w+\.deleter', d): meta['concepts'].append('property')
    if re.search(r'\benum\b|\benumeration\b|from enum import', d): meta['concepts'].append('enum')
    if re.search(r'\bdataclass', d): meta['concepts'].append('dataclass')
    if re.search(r'\btyping\.', d) or re.search(r'from typing import|Callable|List\[|Dict\[|Optional|Union', full): meta['concepts'].append('typing')
    if re.search(r'\bmatch\b.*\bcase\b', d) or re.search(r'match/case', d): meta['concepts'].append('match_case')
    if re.search(r'\btry\b|\bexcept\b|\bexception\b', d): meta['concepts'].append('exception')
    if re.search(r'\bwith\b.*\bopen\b|file.*(?:read|write|open)', d): meta['concepts'].append('file_io')
    if re.search(r'\bcsv\b', d): meta['concepts'].append('csv')
    if re.search(r'\bjson\b', d): meta['concepts'].append('json')
    if re.search(r'\brandom\b|\brandint\b|\bchoice\b|\bshuffle\b|\bsample\b', d): meta['concepts'].append('random')
    if re.search(r'\bmath\b', d): meta['concepts'].append('math')
    if re.search(r'\bdatetime\b', d): meta['concepts'].append('datetime')
    if re.search(r'\bregex?\b|\bre\.(search|match|findall|sub|split)', d): meta['concepts'].append('regex')
    if re.search(r'\ball\(\)', d): meta['concepts'].append('all')
    if re.search(r'\bany\(\)', d): meta['concepts'].append('any')
    if re.search(r'\bsorted\(\)|\bsort\b', d): meta['concepts'].append('sorting')
    if re.search(r'\blambda\b', d): meta['concepts'].append('lambda')
    if re.search(r'__init__', d): meta['concepts'].append('init')
    if re.search(r'__str__', d): meta['concepts'].append('str_magic')
    if re.search(r'super\(\)', d): meta['concepts'].append('super')

    return meta


# ─── TEMPLATES ─────────────────────────────────────────────────

BASIC_TEMPLATES = {
    'kwargs': (
        'Identify that `**kwargs` [special parameter that captures ALL extra keyword arguments as a dictionary] '
        'will collect the variable number of named arguments.',
        'Inside the function, `kwargs` is a regular dict — iterate over it with `.items()` or access keys directly.',
        'Check what the problem asks you to DO with the kwargs: find the longest key name, sum the values, print them, etc.',
        'Use `max(kwargs, key=len)` to find the key with the longest name [max with `key=len` compares items by their length].',
        'Return or print the result depending on what the function signature requires.',
        'Test with different keyword arguments to verify your logic handles all cases.',
    ),
    'all_endswith': (
        'Use `all(condition for item in iterable)` — `all()` [built-in: returns True only if EVERY item passes the condition].',
        'Build a generator expression: `(f.endswith(".ext") for f in filenames)` — `.endswith()` returns True/False for each.',
        'Pass the generator to `all()`: it iterates lazily [one item at a time] and short-circuits [stops] on the first False.',
        'Return the boolean result — True if every item matches, False if any item fails.',
        'Test with mixed data: some matching files and some non-matching to verify both outcomes.',
    ),
    'any_check': (
        'Use `any(condition for item in iterable)` — `any()` [built-in: returns True if AT LEAST ONE item passes the condition].',
        'The generator expression produces a True/False for each element, evaluated lazily [one at a time, on demand].',
        '`any()` short-circuits [stops checking as soon as it finds the first True].',
        'Return the boolean result.',
    ),
    'lambda': (
        'A lambda [anonymous inline function] syntax: `lambda params: expression` — no `return` keyword needed, the expression IS the return value.',
        'Use it where a function is expected temporarily: as a `key` for sorting, or inside `map()`, `filter()`, `sorted()`.',
        'Keep lambdas simple — one expression only. For complex logic, use a regular `def` function.',
        'Pass the lambda to the required function (map, filter, sorted, etc.) and collect the result.',
    ),
    'class_basic': (
        'Define the class: `class ClassName:` — a class [blueprint for creating objects] bundles data (attributes) and behavior (methods).',
        'Add `__init__(self, ...)` — the constructor [runs automatically when you create an instance]. Store values with `self.attr = value`.',
        'Define methods as `def method_name(self, ...):` — `self` [reference to the current instance] is always the first parameter.',
        'Create instances: `obj = ClassName(args)` — this triggers `__init__` with the args passed.',
        'Call methods with `obj.method()` — Python passes `self` automatically.',
    ),
    'inheritance': (
        'Define the parent (base) class: `class Parent:` with its attributes and methods.',
        'Define the child (derived) class: `class Child(Parent):` — the parent name in parentheses sets up inheritance [child gets all parent methods].',
        'Use `super().__init__(args)` in the child\'s `__init__` to call the parent constructor — avoids duplicating setup code.',
        'Override a method by defining it with the same name in the child — the child version replaces the parent version for Child instances.',
        'Add child-specific methods or attributes that the parent does not have.',
        'Test: create both a Parent instance and a Child instance, verify parent-only methods work on child but child-specific methods do not work on parent.',
    ),
    'recursion': (
        'Every recursive function needs a base case [simplest input, answer is known immediately] and a recursive case [call itself with a smaller version].',
        'The base case stops the recursion — without it, you get infinite recursion [RecursionError].',
        'The recursive case must REDUCE the problem size each time (smaller number, shorter string, fewer elements).',
        'Return the combination of results: base case result directly, recursive case combines smaller result with current step.',
        'Test the base case FIRST with the smallest valid input before testing complex cases.',
    ),
    'decorator': (
        'A decorator [function that wraps another to extend behavior] takes a function as input and returns a modified function.',
        'Define the decorator: `def decorator_name(func):` — `func` is the original function being wrapped.',
        'Inside, define `wrapper(*args, **kwargs)` — extra parameters make it flexible for any function signature.',
        'Inside wrapper, add pre-behavior, call `func(*args, **kwargs)`, then add post-behavior.',
        'Return the `wrapper` function object (no parentheses) — this replaces the original function.',
        'Apply with `@decorator_name` above the function definition, or `decorated = decorator_name(original_func)`.',
    ),
    'generator': (
        'A generator function uses `yield` instead of `return` — it produces one value and PAUSES [saves its state for the next call].',
        'When called, it returns a generator object — the body does NOT run until you iterate over it.',
        'Use `for value in generator_func():` — each iteration runs up to the next `yield` and returns that value.',
        'Generators are memory-efficient [lazy evaluation]: they produce values on demand instead of storing the entire sequence.',
    ),
    'magic_methods': (
        'Magic methods [dunder methods with double underscores] define how objects behave with Python operators and built-in functions.',
        '`__init__(self, ...)` — constructor, runs on object creation.',
        '`__str__(self)` — string representation for `print()` and `str()`. `__repr__(self)` — developer representation for debugging.',
        '`__len__(self)` — enables `len(obj)`. `__getitem__(self, key)` — enables `obj[key]`.',
        '`__eq__(self, other)` — enables `==` comparison. `__hash__(self)` — enables use in sets and as dict keys.',
        'Implement the specific magic method(s) the problem asks for, then test with the corresponding operator or function.',
    ),
    'property': (
        '`@property` [decorator that makes a method behave like an attribute] — access without `()` like `obj.attr`.',
        'Define the getter: `@property` above `def attr(self): return self._attr`.',
        'Define the setter: `@attr.setter` above `def attr(self, value): self._attr = value` — called on assignment `obj.attr = val`.',
        'Define the deleter: `@attr.deleter` above `def attr(self): del self._attr` — called on `del obj.attr`.',
        'Properties enable validation, computed values, or read-only access while keeping the interface simple.',
    ),
    'match_case': (
        '`match value:` starts a pattern-matching block [Python 3.10+ structural pattern matching].',
        'Each `case pattern:` branch is checked in order — the FIRST matching case runs.',
        'Use `case _:` as the catch-all [matches anything, like `default` in other languages].',
        'Add guards with `if` conditions: `case x if x > 0:` matches only when the condition is True.',
        'Return or assign a value inside each case branch.',
    ),
    'exception': (
        'Wrap the risky code in a `try:` block — Python executes it and if an error occurs, jumps to the matching `except`.',
        'Catch specific exceptions: `except ValueError:` for type conversion errors, `except ZeroDivisionError:` for division by zero.',
        'Use `except Exception as e:` to capture the error message. Use `finally:` for cleanup that runs no matter what.',
        'Return an appropriate value from each branch (success value in try, fallback in except).',
    ),
    'file_io': (
        'Open the file with `with open(filename, mode) as f:` — the `with` block [context manager] closes the file automatically.',
        'Read modes: `"r"` [read text], `"rb"` [read binary]. Write modes: `"w"` [write, overwrites], `"a"` [append].',
        'Read with `f.read()` [entire file as string], `f.readlines()` [list of lines], or `for line in f:` [iterate, memory efficient].',
        'Write with `f.write(text)` — does NOT add newlines automatically. Use `print(text, file=f)` for automatic newlines.',
    ),
}


# ─── GENERATOR ─────────────────────────────────────────────────

def generate_breakdown(desc, initial_code, exercise_id):
    meta = extract_metadata(desc, initial_code)
    d = desc.lower()
    steps = []

    # Priority: try concept-specific templates first
    # kwargs
    if 'kwargs' in meta['concepts']:
        for s in BASIC_TEMPLATES['kwargs']:
            steps.append(s)
        return steps

    # all() + endswith
    if 'all' in meta['concepts'] and re.search(r'\.endswith|extension|verify.*file', d):
        for s in BASIC_TEMPLATES['all_endswith']:
            steps.append(s)
        return steps

    # any()
    if 'any' in meta['concepts']:
        for s in BASIC_TEMPLATES['any_check']:
            steps.append(s)
        return steps

    # Property (check BEFORE decorator since @property matches @\w+)
    if 'property' in meta['concepts']:
        for s in BASIC_TEMPLATES['property']:
            steps.append(s)
        return steps

    # Decorator
    if 'decorator' in meta['concepts']:
        for s in BASIC_TEMPLATES['decorator']:
            steps.append(s)
        return steps

    # Generator
    if 'generator' in meta['concepts']:
        for s in BASIC_TEMPLATES['generator']:
            steps.append(s)
        return steps

    # Match/case
    if 'match_case' in meta['concepts']:
        for s in BASIC_TEMPLATES['match_case']:
            steps.append(s)
        return steps

    # Exception handling
    if 'exception' in meta['concepts']:
        for s in BASIC_TEMPLATES['exception']:
            steps.append(s)
        return steps

    # File I/O
    if 'file_io' in meta['concepts']:
        for s in BASIC_TEMPLATES['file_io']:
            steps.append(s)
        return steps

    # Lambda / map / filter
    if 'lambda' in meta['concepts'] or 'map' in meta['concepts'] or 'filter' in meta['concepts']:
        for s in BASIC_TEMPLATES['lambda']:
            steps.append(s)
        return steps

    # Recursion
    if 'recursion' in meta['concepts']:
        for s in BASIC_TEMPLATES['recursion']:
            steps.append(s)
        return steps

    # Magic methods
    if 'magic_methods' in meta['concepts']:
        for s in BASIC_TEMPLATES['magic_methods']:
            steps.append(s)
        return steps

    # Property
    if 'property' in meta['concepts']:
        for s in BASIC_TEMPLATES['property']:
            steps.append(s)
        return steps

    # Inheritance
    if 'inheritance' in meta['concepts']:
        for s in BASIC_TEMPLATES['inheritance']:
            steps.append(s)
        return steps

    # Class (basic)
    if 'class' in meta['concepts']:
        for s in BASIC_TEMPLATES['class_basic']:
            steps.append(s)
        return steps

    # ─── PATTERN-BASED GENERATION ────────────────────────
    # Fall through to pattern detection for common patterns

    # Extract function name from description backticks
    fn_name = meta['functions'][0] if meta['functions'] else 'solution'

    # Detect data type from description
    has_list = bool(re.search(r'\blist\b|\barray\b', d))
    has_string = bool(re.search(r'\bstring\b|\bstr\b', d))
    has_dict = bool(re.search(r'\bdict\b|\bdictionary\b', d))
    has_tuple = bool(re.search(r'\btuple\b', d))
    has_two_numbers = bool(re.search(r'two\s+numbers|two\s+integers|two\s+arguments', d))
    has_single_number = bool(re.search(r'takes?\s+(?:a\s+)?number|an\s+integer|a\s+single', d))

    # 1. Number operations
    if has_two_numbers:
        steps.append(f'Define `def {fn_name}(a, b):` — two parameters [inputs to the function].')
        op = 'addition (+)'
        if re.search(r'\bmultiply\b|\bproduct\b', d): op = 'multiplication (*)'
        elif re.search(r'\bsubtract\b|\bdifference\b', d): op = 'subtraction (-)'
        elif re.search(r'\bdivide\b|\bquotient\b', d): op = 'division (/)'
        elif re.search(r'\bmodulo\b|\bremainder\b', d): op = 'modulo (%)'
        elif re.search(r'\bpower\b|\bexponent\b', d): op = 'exponentiation (**)'
        symbol = {'addition (+)': '+', 'multiplication (*)': '*', 'subtraction (-)': '-',
                  'division (/)': '/', 'modulo (%)': '%', 'exponentiation (**)': '**'}
        sym = symbol.get(op, '+')
        steps.append(f'Implement the operation with `return a {sym} b` using the {op} operator.')
        steps.append('Test with the example inputs to verify the output matches exactly.')
        return steps

    # 2. List operations
    if has_list:
        steps.append(f'Define `def {fn_name}(items):` — `items` is a list [ordered, mutable collection].')
        if re.search(r'\bsum\b|\btotal\b', d):
            steps.append('Use `sum(items)` [built-in that adds all elements] to calculate the total.')
        elif re.search(r'\bmax\b|\blargest\b|\bbiggest\b|\bhighest\b', d):
            steps.append('Use `max(items)` [built-in that returns the largest element].')
        elif re.search(r'\bmin\b|\bsmallest\b|\blowest\b', d):
            steps.append('Use `min(items)` [built-in that returns the smallest element].')
        elif re.search(r'\baverage\b|\bmean\b', d):
            steps.append('Use `sum(items) / len(items)` — total divided by count [float division].')
        elif re.search(r'\bsorted\b|\bsort\b|\border\b', d):
            steps.append('Use `sorted(items)` [returns a new sorted list] — or `items.sort()` [sorts in-place].')
        elif re.search(r'\breverse\b|\bflip\b|\bbackward\b', d):
            steps.append('Use `items[::-1]` [slice with step -1] to create a reversed copy. Or `reversed(items)` for a lazy iterator.')
        elif re.search(r'\bunique\b|\bdistinct\b|\bduplicate\b', d):
            steps.append('Loop through items: if `item not in result: result.append(item)` — or use `list(set(items))` if order doesn\'t matter.')
        elif re.search(r'\bfilter\b|\below\b|\bgreater\b', d):
            steps.append('Loop with `if condition:` to select matching elements, building a new list.')
        elif re.search(r'\bcount\b|\bfrequency\b|\boccurrence\b', d):
            steps.append('Use a dictionary to tally: `if x in counts: counts[x] += 1 else: counts[x] = 1`.')
        elif re.search(r'\bsquare\b', d):
            steps.append('Use a list comprehension: `[x**2 for x in items]` — the `**` operator raises to a power.')
        elif re.search(r'\beven\b|\bodd\b', d):
            steps.append('Filter with `x % 2 == 0` [even] or `x % 2 != 0` [odd] — modulo detects divisibility.')
        else:
            steps.append(f'Loop through the list with `for item in items:` and accumulate the result.')
        steps.append('Return the result. Check edge cases: empty list, single element.')
        return steps

    # 3. String operations
    if has_string:
        steps.append(f'Define `def {fn_name}(s):` — `s` is a string [immutable sequence of characters].')
        if re.search(r'\bupper\b', d):
            steps.append('Use `s.upper()` — returns a new string with all letters capitalized [original unchanged].')
        elif re.search(r'\blower\b', d):
            steps.append('Use `s.lower()` — returns a new string with all letters lowercased.')
        elif re.search(r'\bcapitalize\b', d):
            steps.append('Use `s.capitalize()` — first letter uppercase, rest lowercase.')
        elif re.search(r'\breverse\b', d):
            steps.append('Use `s[::-1]` — slice with step -1 creates a reversed copy.')
        elif re.search(r'\bvowels?\b', d):
            steps.append('Loop through chars: `if ch.lower() in "aeiou": count += 1` — increment the counter for each vowel.')
        elif re.search(r'\bpalindrom\b', d):
            steps.append('Check `s == s[::-1]` — if the string equals its reverse, it\'s a palindrome.')
        elif re.search(r'\bsplit\b', d):
            steps.append('Use `s.split(sep)` to split into a list. Default separator is whitespace.')
        elif re.search(r'\bjoin\b', d):
            steps.append('Use `"separator".join(list_of_strings)` to concatenate with a separator between each.')
        elif re.search(r'\bstrip\b', d):
            steps.append('Use `s.strip()` to remove whitespace from both ends. `lstrip()` / `rstrip()` for one side.')
        elif re.search(r'\bcount\b', d):
            steps.append('Use `s.count(substring)` to count non-overlapping occurrences.')
        elif re.search(r'\bstartswith\b', d):
            steps.append('Use `s.startswith(prefix)` — returns True if string begins with that prefix.')
        elif re.search(r'\bendswith\b', d):
            steps.append('Use `s.endswith(suffix)` — returns True if string ends with that suffix.')
        elif re.search(r'\breplace\b', d):
            steps.append('Use `s.replace(old, new)` — replaces ALL occurrences of old with new.')
        else:
            steps.append(f'Analyze the string: loop through characters or use string methods to transform/count.')
        steps.append('Return the result. Remember: strings are immutable [methods return new strings, originals never change].')
        return steps

    # ─── GENERIC FALLBACK ────────────────────────────────
    # Use extracted function name and basic parameter/return info

    param_hint = ''
    if meta['functions']:
        fn = meta['functions'][0]
        param_hint = f'Define `def {fn}(parameters):` — the function name is `{fn}`. '
    else:
        param_hint = 'Define the function with the name given in the description. '

    steps.append(param_hint + 'Identify what parameters it takes and what it should return.')
    steps.append('Break the problem into steps: what data comes in, what transformations are needed, what comes out.')
    steps.append('Write each step in the function body, using intermediate variables for partial results.')
    steps.append('Use `return` to send the result back to the caller.')
    steps.append('Test with the example inputs and verify the output matches character for character.')
    steps.append('Check edge cases: empty input, very large input, negative values, and type mismatches.')

    return steps


def main():
    lines, blocks = read_exercises(EXERCISES_FILE)
    print(f'Read {len(blocks)} exercises.')

    edits = []
    for block in blocks:
        desc = get_field(block, 'description').replace('\\n', ' ').replace('\\"', '"').replace('\\t', ' ')
        icode = get_field(block, 'initialCode').replace('\\n', ' ').replace('\\"', '"')
        eid = get_id(block)
        title = get_field(block, 'title')

        if not desc:
            continue

        # Find hint line and existing breakdown line
        full = ''.join(l for l, _ in block)
        hint_m = re.search(r'("hint":)', full)
        if not hint_m:
            continue

        # Find the line index of hint
        hint_lineno = None
        brk_lineno = None
        for bl, lineno in block:
            if '"hint":' in bl:
                hint_lineno = lineno
            if '"breakdown":' in bl:
                brk_lineno = lineno

        if hint_lineno is None:
            continue

        steps = generate_breakdown(desc, icode, eid)
        numbered = '\n'.join(f'{i+1}. {s}' for i, s in enumerate(steps))
        esc = numbered.replace('\\', '\\\\').replace('\n', '\\n').replace('"', '\\"')

        edits.append((hint_lineno, f'            "breakdown": "{esc}",\n', brk_lineno))

    # Apply bottom-to-top
    edits.sort(key=lambda x: x[0], reverse=True)
    new_lines = lines[:]
    for insert_at, text, remove_at in edits:
        if remove_at is not None:
            if remove_at < len(new_lines) and '"breakdown":' in new_lines[remove_at]:
                new_lines.pop(remove_at)
                if insert_at > remove_at:
                    insert_at -= 1
        new_lines.insert(insert_at, text)

    # Write to main file
    with open(EXERCISES_FILE, 'w') as f:
        f.write('\n'.join(new_lines))

    print(f'Done. Generated {len(edits)} metadata-driven breakdowns.')


if __name__ == '__main__':
    main()
