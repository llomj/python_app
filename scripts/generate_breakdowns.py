#!/usr/bin/env python3
"""
Granular breakdown generator v2 — ~40 templates with robust keyword extraction.
"""
import re

EXERCISES_FILE = '/Users/moll/Desktop/python_app/exercises.ts'

with open(EXERCISES_FILE, 'r') as f:
    lines = f.readlines()

start_idx = 0
for i, line in enumerate(lines):
    if 'Exercise[] = [' in line or ('EXERCISES:' in line and '[' in line):
        start_idx = i + 1
        break

in_ex = False; depth = 0; cur = []; exercises = []
for i in range(start_idx, len(lines)):
    ob = lines[i].count('{'); cb = lines[i].count('}')
    if '{' in lines[i] and not in_ex:
        in_ex = True; depth = ob - cb; cur = [(lines[i], i)]
    elif in_ex:
        cur.append((lines[i], i)); depth += ob - cb
        if depth <= 0:
            exercises.append(cur); cur = []; in_ex = False

def extract_field(block, field):
    full = ''.join(l for l, _ in block)
    m = re.search(r'"' + field + r'":\s*"((?:[^"\\]|\\.)*)"', full)
    return m.group(1) if m else ''

def extract_fn(desc):
    """Extract the function name most reliably."""
    # Priority 1: "function called `name`" or "function named `name`"
    m = re.search(r'function\s+(?:called|named)\s+[`\x27](\w+)[`\x27]', desc, re.I)
    if m: return m.group(1)
    # Priority 2: "function called NAME" (no backticks — rare)
    m = re.search(r'function\s+(?:called|named)\s+(\w+)', desc, re.I)
    if m: return m.group(1)
    # Priority 3: "a function NAME" where NAME is lowercase (not a keyword)
    m = re.search(r'a\s+function\s+[`\x27](\w+)[`\x27]', desc, re.I)
    if m: return m.group(1)
    # Priority 4: name in backticks inside parentheses like `name()` or `name`
    m = re.search(r'[`\x27](\w+)(?:\(\))?[`\x27]', desc)
    if m: return m.group(1)
    # Priority 5: name with parentheses after, no backticks
    m = re.search(r'[`\x27](\w+)[`\x27]\s*\(', desc)
    if m: return m.group(1)
    return None

def is_vowel(c):
    return c.lower() in 'aeiou'

def generate_breakdown(desc: str) -> str:
    d = desc.lower()
    fn = extract_fn(desc) or 'solution'
    steps = []
    add = lambda s: steps.append(s)

    intro = f'Read the problem carefully. Key details: (1) function name is `{fn}`, (2) identify the parameter(s) it takes, (3) what it should return or print. Check the examples to infer exact input/output format.'

    # ─── 0. KNOWN KEYWORD OVERRIDES ─────────────────────────
    if re.search(r'`all\(\)`|all\(\)', d) and re.search(r'\.endswith|extension|verify.*file', d):
        # "Use all() to verify that all files have a .txt extension"
        add(intro)
        add('This problem asks you to use the built-in `all()` function [returns True if EVERY item in the iterable is truthy]')
        add('Create a list of filenames or receive one as input — each filename is a string like `"document.txt"`')
        add('Use a generator expression: `(f.endswith(".txt") for f in filenames)` — `.endswith()` [string method that checks the suffix] returns True/False for each name')
        add('Pass the generator to `all()`: `all(f.endswith(".txt") for f in filenames)` — all() iterates lazily [one at a time] and short-circuits on the first False')
        add('`all()` returns True if EVERY filename ends with ".txt", False if ANY filename has a different extension')
        add('Return or print the boolean result — test with mixed extensions to verify the logic works both ways')
        return '\n'.join(f'{i+1}. {s}' for i, s in enumerate(steps))

    if re.search(r'`any\(\)`|any\(\)', d):
        add(intro)
        add('Use `any(condition for x in iterable)` — `any()` [built-in: returns True if AT LEAST ONE item is truthy]')
        add('The generator expression `(condition for x in items)` produces a boolean [True/False] for each element lazily')
        add('`any()` short-circuits [stops checking as soon as it finds the first True], making it efficient for large data')
        return '\n'.join(f'{i+1}. {s}' for i, s in enumerate(steps))

    # ─── EXTRACT SPECIFICS FROM DESCRIPTION ──────────────────
    # Parameters
    params = []
    pm = re.search(r'takes\s+(?:a\s+)?(\w+(?:\s+\w+)?)\s+(?:as\s+)?(?:parameter|input|argument)', d)
    if pm: params.append(pm.group(1))

    # Class names
    cls_names = re.findall(r'\bclass\s+(\w+)', desc)
    base_cls = cls_names[0] if cls_names else None
    child_cls = cls_names[-1] if len(cls_names) > 1 else None
    # If only one class mentioned, check for "base" / "derived" clues
    single_cls = cls_names[0] if cls_names else None

    # ─── 1. CLASS / OOP ─────────────────────────────────────
    if re.search(r'\bclass\b', d) and not re.search(r'recursi|comprehension|lambda|decorator', d):
        if re.search(r'\binherit\b|\bderived\b|\boverride\b|\bbase\b.*\bclass\b|\bsubclass\b', d):
            # Inheritance pattern
            pname = base_cls or 'ParentClass'
            cname = child_cls or 'ChildClass'
            add(intro)
            add(f'Define the base class: `class {pname}:` — a class [blueprint for objects] is a template with attributes and methods')
            if re.search(r'__init__|constructor|initialize|attribute', d):
                add(f'In {pname}, add `__init__(self, ...)` — the constructor [runs automatically when creating an object]. Use `self.attr = value` to store attributes')
            if re.search(r'method', d):
                add(f'Define a method in {pname}: `def method_name(self):` — `self` [reference to the current instance] is always the first parameter, passed automatically')
            add(f'Create the derived class: `class {cname}({pname}):` — the parent name in parentheses is how Python does inheritance [child inherits everything from parent]')
            if re.search(r'override|own\s+.*method', d) or re.search(r'same method|same name', d):
                add(f'In {cname}, define a method with the SAME name as one in {pname} — this overrides [replaces] the parent version with the child\'s specific behavior')
            if re.search(r'super\(\)', d):
                add(f'Use `super().__init__(args)` inside the child\'s __init__ — `super()` [refers to the parent class] calls the parent constructor so you don\'t repeat setup logic')
            if re.search(r'extra|additional|new\s+.*method|unique', d):
                add(f'Add extra methods in {cname} that only the child has — the parent does NOT get these methods [inheritance is one-way: child → parent, not parent → child]')
            if re.search(r'__str__|to_string|represent', d):
                add(f'`__str__` returns a string representation [used by print()]. Implement it in both classes to show different info')
            add(f'Test: `obj = {cname}(args)` creates an instance. `obj.method()` calls the method. Verify that a {pname} instance shows base behavior and a {cname} instance shows overridden behavior')
            return '\n'.join(f'{i+1}. {s}' for i, s in enumerate(steps))

        # Plain class (no inheritance keywords)
        add(intro)
        cname = single_cls or fn
        add(f'Define the class: `class {cname}:` — a class [blueprint for objects] bundles related data and functions together')
        if re.search(r'__init__|constructor|initiali[zZ]e', d):
            add(f'Add `__init__(self, ...)` — the constructor [runs when a new object is created]. Store values with `self.attribute = value` [self links to the specific instance]')
        if re.search(r'method', d):
            add(f'Define methods as `def method_name(self, ...):` — `self` [the current object] must come first, Python passes it automatically when you call `obj.method()`')
        if re.search(r'static|@staticmethod', d):
            add(f'Use `@staticmethod` [decorator for class-level utility] — no `self` needed, call it as `ClassName.method()` directly')
        if re.search(r'classmethod|@classmethod', d):
            add(f'Use `@classmethod` with `cls` parameter [refers to the class itself, not an instance] — often used for alternative constructors')
        if re.search(r'encapsulation|private|_\w+', d):
            add(f'Prefix "private" attributes with `_` [convention: signals "internal use, don\'t touch directly" — Python does NOT enforce this, it\'s an agreement between programmers]')
        if re.search(r'getter|@property|property', d):
            add(f'Use `@property` [decorator that makes a method look like an attribute] — access without `()` like `obj.property_name`')
        if re.search(r'setter|@.*\.setter', d):
            add(f'Use `@attribute.setter` [decorator for setting a property with validation] — called when you assign `obj.attribute = value`')
        if re.search(r'__str__|to_string|repr', d):
            add(f'`__str__` returns a human-readable string [used by `print()`]. `__repr__` returns a developer-readable string [used by debugger/repl]')
        add(f'Create instances: `obj = {cname}(args)` [constructor call with `()`], then call methods: `obj.method()`')
        return '\n'.join(f'{i+1}. {s}' for i, s in enumerate(steps))

    # ─── 2. RECURSION ────────────────────────────────────────
    if re.search(r'\brecursi', d) or re.search(r'recursion|recursive', d):
        add(intro)
        add(f'Every recursive function needs a base case [simplest input — answer is known immediately, no more calls] and a recursive case [break into smaller sub-problem]')
        if re.search(r'fib|fibonacci', d):
            add('Base: if n <= 1, return n [fib(0)=0, fib(1)=1]. Recursive: return fib(n-1) + fib(n-2) — the sum of the two preceding numbers')
        elif re.search(r'factorial', d):
            add('Base: if n <= 1, return 1 [0! = 1, 1! = 1]. Recursive: return n * factorial(n-1) [n! = n × (n-1)!]')
        elif re.search(r'palindrom', d):
            add('Base: if len(s) <= 1, return True [a single char is always a palindrome]. Recursive: check if first and last chars match, then recurse on s[1:-1] [the inner substring without first/last]')
        elif re.search(r'tower|hanoi', d):
            add('Base: move 1 disk from source to target. Recursive: move n-1 from source→aux, move largest source→target, move n-1 from aux→target')
        elif re.search(r'tree|director', d):
            add('Process the current node, then recursively call the function on each child — the call stack [Python\'s record of active function calls] grows and shrinks naturally with the tree structure')
        elif re.search(r'sum.*(list|digit)|total.*(list|digit)', d):
            add('Base: empty input returns 0. Recursive: first element + recursive call on the rest [lst[0] + sum(lst[1:]) for lists, or n%10 + sum(n//10) for digits]')
        elif re.search(r'reverse|backward.*(string|list)', d):
            add('Base: empty string/list returns itself. Recursive: last character + reverse(rest) [s[-1] + reverse(s[:-1]) for strings]')
        else:
            add(f'Define `{fn}` so it calls ITSELF with a smaller version of the problem — each call gets closer to the base case')
        add('CRITICAL: every recursive call must REDUCE the problem size [smaller n, shorter string, fewer elements] — without progress toward the base, you get infinite recursion [RecursionError: maximum depth exceeded]')
        add(f'Test the base case FIRST: call `{fn}` with the smallest valid input before trying complex cases')
        return '\n'.join(f'{i+1}. {s}' for i, s in enumerate(steps))

    # ─── 3. LAMBDA / MAP / FILTER / REDUCE ──────────────────
    if re.search(r'\blambda\b', d) or re.search(r'\bfilter\b', d) or re.search(r'\bmap\b', d) or re.search(r'\breduce\b', d):
        add(intro)
        add('A lambda [anonymous inline function] is written: `lambda params: expression` — no `return` keyword, the expression result IS the return value')
        if re.search(r'\bmap\b', d):
            add('`map(func, iterable)` applies func to EVERY element — returns a map object [lazy iterator]. Wrap with `list()` to materialize: `list(map(lambda x: x*2, numbers))`')
        if re.search(r'\bfilter\b', d):
            add('`filter(func, iterable)` keeps elements where func returns True [boolean predicate]. The lambda should return True for items you want to KEEP')
        if re.search(r'\breduce\b', d):
            add('`reduce(func, iterable)` cumulatively applies func: takes first two items → result, then result + next item → new result. Import: `from functools import reduce`')
        if re.search(r'\bsort\b|\bsorted\b', d):
            add('Use `key` parameter: `sorted(items, key=lambda x: expression)` — key [transformation applied before comparison] changes what elements are compared BY, without modifying values')
        if re.search(r'\beven\b|\bodd\b', d):
            add('`lambda x: x % 2 == 0` [x modulo 2 equals 0 — even numbers have no remainder when divided by 2]. `% 2 != 0` for odd')
        if re.search(r'\bsquare\b', d):
            add('`lambda x: x ** 2` — `**` [exponentiation operator: x raised to power 2] squares the value')
        if re.search(r'\bstring\b|\bstr\b', d) and re.search(r'\blower\b|\bupper\b|\blen\b', d):
            add('String functions as lambda: `lambda s: s.lower()` [convert to lowercase], `lambda s: len(s)` [length]')
        if re.search(r'\btranspos|matrix|zip', d):
            add('`list(zip(*matrix))` transposes rows and columns — `*matrix` [unpacking operator: passes each row as a separate argument] to zip')
        add('Result from map/filter is an iterator [lazy: computed on demand, not stored]. Use `list(...)` to collect when you need to reuse or print the values')
        return '\n'.join(f'{i+1}. {s}' for i, s in enumerate(steps))

    # ─── 4. DECORATOR ────────────────────────────────────────
    if re.search(r'decorator|@\s*\w+', d):
        add(intro)
        add('A decorator [function that wraps another function to extend its behavior] takes a function as input and returns a modified function')
        add(f'Define the decorator: `def {fn}(func):` — `func` [the original function being decorated] comes in as a parameter')
        add('Inside, define a nested `wrapper(*args, **kwargs)` — `*args` [any number of positional arguments] and `**kwargs` [any number of keyword arguments] make it flexible for any function')
        add('Inside wrapper, add behavior BEFORE calling the original, then call `func(*args, **kwargs)` [the brackets `()` execute the original function], then add behavior AFTER')
        add('Return `wrapper` (NO brackets) — you return the wrapper FUNCTION OBJECT itself, not its result [this is what replaces the original function]')
        if re.search(r'timer|time|duration|speed', d):
            add('Use `time.time()` [current timestamp in seconds since epoch] before and after `func()` — subtract to get duration, then print it')
        if re.search(r'log|debug|trace', d):
            add('Print the function name with `func.__name__` [attribute that stores the original name] and the arguments before calling it')
        if re.search(r'cache|memoiz', d):
            add('Store results in a dictionary `cache = {}` keyed by args — if key exists [already computed], return cached value instead of recalculating')
        if re.search(r'auth|login|permission', d):
            add('Check a condition before calling `func()` — if not authorized, print an error or return early without calling the function')
        add('Apply: `@{fn}` above `def my_func():` — shorthand for `my_func = {fn}(my_func)`. Or call directly: `decorated = {fn}(original_func)`')
        return '\n'.join(f'{i+1}. {s}' for i, s in enumerate(steps))

    # ─── 5. GENERATOR / YIELD ────────────────────────────────
    if re.search(r'\byield\b|\bgenerator\b', d):
        add(intro)
        add('A generator function uses `yield` instead of `return` — it produces one value and PAUSES execution, saving its state [all local variables, where it left off]')
        add('When called, a generator returns a generator OBJECT (not a value) — it does NOT run the function body until you start iterating')
        add('Use a `for` loop: `for val in {fn}():` — each iteration runs the function up to the next `yield` and gives you that value')
        if re.search(r'fib|fibonacci|sequence|number', d):
            add('Initialize `a, b = 0, 1` [parallel assignment: both right-side values are computed before any left-side assignment]. In a loop: `yield a`, then `a, b = b, a + b`')
        if re.search(r'infinite|endless', d):
            add('Use `while True:` with `yield` inside — the caller controls how many values to consume, so an infinite loop is safe when terminated by the consumer')
        if re.search(r'filter|condition|even|odd', d):
            add('Inside the loop, check a condition with `if` — only `yield` values that pass the filter. The generator naturally stops when the source data runs out')
        add('Memory advantage: generators produce values on demand [lazy evaluation] instead of storing the whole sequence in memory')
        return '\n'.join(f'{i+1}. {s}' for i, s in enumerate(steps))

    # ─── 6. CONTEXT MANAGER ────────────────────────────────
    if re.search(r'context manager|with\s+open|__enter__|__exit__', d):
        add(intro)
        add('A context manager [object that guarantees setup/cleanup] implements `__enter__` and `__exit__` methods')
        add('`__enter__(self)` runs at the START of the `with` block — return the managed resource [what `as` assigns to]')
        add('`__exit__(self, exc_type, exc_val, exc_tb)` runs at the END — handles cleanup [close files, release locks] EVEN if an exception occurred')
        add(f'Usage: `with {fn}() as x:` — the `as` variable gets whatever `__enter__` returns. Cleanup always runs, so resources are never leaked')
        return '\n'.join(f'{i+1}. {s}' for i, s in enumerate(steps))

    # ─── 7. COMPREHENSION ──────────────────────────────────
    if re.search(r'\bcomprehension\b', d):
        add(intro)
        add('A comprehension [concise one-liner to build a sequence] follows the order: expression → for clause → optional if filter')
        add('`[expr for item in iterable if condition]` — reads as: for each item IN iterable, IF condition passes, add expr to the result list')
        add('Use `[]` for list, `{expr}` for set [unique unordered], `{key: val}` for dict, `(expr for item in iterable)` for generator [lazy — no memory until iterated]')
        if re.search(r'nested|matrix|2d|two.*dimension', d):
            add('Nested: `[expr for a in outer for b in inner]` — the order follows nested for loops: outer first, then inner')
        if re.search(r'dict|key', d):
            add('Dict comprehension: `{key_expr: value_expr for item in iterable}` — the colon `:` separates keys from values')
        add('Write the for-loop version FIRST if you\'re stuck, then compress it into a comprehension — it\'s the same logic in different syntax')
        return '\n'.join(f'{i+1}. {s}' for i, s in enumerate(steps))

    # ─── 8. INPUT / FILE I/O ────────────────────────────────
    if re.search(r'input\(\)|prompt.*user|read.*user|enter', d) or re.search(r'file|open\(|read.*program', d):
        add(intro)
        if re.search(r'input\(\)|prompt|enter|user', d):
            add('`input()` [reads a line from keyboard as a STRING] — ALWAYS returns a string. Convert: `int(input())` [for integers], `float(input())` [for decimals]')
        if re.search(r'multiple|several|numerous|\bn\b.*input|input.*\bn\b', d):
            add('Multiple values: `input().split()` [splits the string by whitespace into a list of strings], then `map(int, ...)` or a list comprehension to convert to numbers')
        if re.search(r'file|open\(|read.*(?:file|content|text)|write.*file', d):
            add('Open: `open("filename", "r")` — modes: `"r"` [read], `"w"` [write — overwrites!], `"a"` [append], `"r+"` [read and write]')
            add('Use `with open(...) as f:` — the with statement [context manager] closes the file automatically even if an error occurs. Methods: `f.read()` [entire file as string], `f.readlines()` [list of lines], `for line in f:` [iterate line by line, memory efficient]')
        if re.search(r'write|save|store|output', d):
            add('Write with `f.write(string)` — does NOT add a newline automatically. Add `\\n` manually or use `print(string, file=f)` [print can write to any file object]')
        if re.search(r'menu|choice|option|select', d):
            add('Print options, get `input()`, then handle with `if/elif/else` [conditional chain] or a dictionary mapping choices to actions [more scalable for many options]')
        if re.search(r'csv|excel|spreadsheet', d):
            add('`import csv` — use `csv.reader(file)` [returns iterator of lists] or `csv.DictReader(file)` [each row as a dictionary with header keys]')
        if re.search(r'json', d):
            add('`import json` — `json.load(file)` [read JSON from file → Python dict/list], `json.dumps(data)` [Python object → JSON string]')
        if re.search(r'random|randint|choice|shuffle', d):
            add('`import random` — `random.choice(list)` [pick one], `random.randint(a, b)` [random integer between a and b inclusive], `random.shuffle(list)` [shuffle in-place]')
        add('Use `print()` for output — it adds `\\n` by default. `print(x, end="")` for no newline')
        return '\n'.join(f'{i+1}. {s}' for i, s in enumerate(steps))

    # ─── 9. RANDOM ────────────────────────────────────────
    if re.search(r'\brandom|\brandint\b|\bchoice\b|\bshuffle\b|\bsample\b|\bseed\b', d):
        add(intro)
        add('Import: `import random` — gives access to all random functions')
        if re.search(r'\bchoice\b', d):
            add('`random.choice(seq)` — returns one RANDOM element from the sequence [list, tuple, or string]')
        if re.search(r'\brandint\b', d):
            add('`random.randint(a, b)` — random integer N where a <= N <= b [BOTH inclusive]')
        if re.search(r'\bshuffle\b', d):
            add('`random.shuffle(lst)` — shuffles the list IN-PLACE [modifies the original, returns None]. Use `random.sample(lst, len(lst))` for a new shuffled copy')
        if re.search(r'\bsample\b', d):
            add('`random.sample(population, k)` — returns a NEW list of k UNIQUE elements [no repeats]. Raises ValueError if k > population size')
        if re.search(r'\bseed\b', d):
            add('`random.seed(n)` — initializes the random generator to a FIXED state. Same seed → same sequence — useful for reproducible tests')
        add('Return or print the random result. Each run may produce different output [unless you set a seed]')
        return '\n'.join(f'{i+1}. {s}' for i, s in enumerate(steps))

    # ─── 10. LIST / ITERABLE OPERATIONS ────────────────────
    if re.search(r'\blists?\b', d) or re.search(r'\barrays?\b', d):
        add(intro)
        add(f'Define `def {fn}(lst):` where `lst` is a list [ordered, MUTABLE collection — you CAN change elements]. Access with `lst[index]` [0-based: first element is at 0]')

        if re.search(r'\bsum\b|\btotal\b', d):
            add('`sum(lst)` — built-in [adds all elements in one call]. Or manual: `total = 0` then `for x in lst: total += x` [accumulator pattern, step through each element]')

        if re.search(r'\bmax\b|\b(?:largest|biggest|highest)\b', d):
            add('`max(lst)` — built-in. Or manual: set `max_val = lst[0]` [start with first element], then `for item in lst: if item > max_val: max_val = item` [linear scan — O(n) time]')

        if re.search(r'\bmin\b|\b(?:smallest|lowest)\b', d):
            add('`min(lst)` — built-in. Or manual: same as max but check `if item < min_val` [comparison operator flipped]')

        if re.search(r'\bavg\b|\baverage\b|\bmean\b', d):
            add('`sum(lst) / len(lst)` — total divided by count. `/` gives float division [3.5], `//` gives floor division [3]')

        if re.search(r'\bmedian\b', d):
            add('Sort first: `sorted(lst)` [returns sorted copy], then pick the middle element. Even-length: average of two middle elements')

        if re.search(r'\bsort\b|\border\b|\barrange\b', d):
            add('`sorted(lst)` — returns NEW sorted list [original unchanged]. `lst.sort()` — sorts IN-PLACE [modifies original, returns None]. Both take a `key=` function and `reverse=True`')

        if re.search(r'\breverse\b|\bbackward\b|\bflip\b', d):
            add('`lst[::-1]` — slicing with step -1 [creates a new reversed list]. `reversed(lst)` — returns a lazy iterator [memory efficient]. `lst.reverse()` — reverses IN-PLACE')

        if re.search(r'\bduplicate\b|\bunique\b|\bdistinct\b', d):
            add('Track seen items: create `seen = []`, loop through items. If `item not in seen:` [membership test], append to seen. Return seen [preserves order]. Alternative: `set(lst)` if order doesn\'t matter')

        if re.search(r'\bcommon\b', d):
            add('Find intersection: convert first list to `set()` for O(1) lookups [instant membership check], then loop through second and check `if item in set1:` — much faster than nested loops')

        if re.search(r'\beven\b|\bodd\b', d) and not re.search(r'position|index', d):
            add('Filter with `x % 2 == 0` [even — no remainder when divided by 2] or `x % 2 == 1` / `x % 2 != 0` [odd]')

        if re.search(r'\bprime\b', d):
            add('Check from 2 to `int(n**0.5) + 1` [sqrt(n) — if n has a factor larger than sqrt, it must have one smaller too]. If `n % i == 0` [divisible], it\'s NOT prime')

        if re.search(r'\brange\b|\bbetween\b|\bsequence\b', d):
            add('`range(stop)` — 0 to stop-1. `range(start, stop)` — start to stop-1. `range(start, stop, step)` — with custom step. Convert with `list(range(...))`')

        if re.search(r'\bsquare\b', d) and re.search(r'each|element|number|item', d):
            add('`[x**2 for x in lst]` — list comprehension: `**` is exponentiation [x squared = x to power 2]. For each x, compute x**2 and add to result')

        if re.search(r'\bpattern\b|\btriangle\b|\bpyramid\b|\bdiamond\b|\bstar\b', d):
            add('Nested loops: outer loop [controls rows / height], inner loop [controls characters per row]. Inner loop range depends on outer loop variable. Use `"*" * n` [string repetition: multiply a string by an integer] for padding')

        if re.search(r'\bmatrix\b|\bgrid\b|\b2[dD]\b|\btwo.?dimension', d):
            add('A 2D list is `list[list[element]]`: access with `matrix[row][col]` [row first, then column]. Nested loops: `for r in range(rows): for c in range(cols):`')

        if re.search(r'\btranspos', d):
            add('`zip(*matrix)` — `*matrix` [unpacking: each row becomes a separate argument to zip]. `zip` pairs up elements at the same index across all rows')

        if re.search(r'\bcount\b|\bfrequency\b|\boccurrence\b', d):
            add('`lst.count(x)` — counts single value. For all frequencies: loop with a dictionary: `if x in counts: counts[x] += 1 else: counts[x] = 1`')

        if re.search(r'\bremove\b|\bdelete\b|\beliminate\b|\bfilter\b', d):
            add('Build a NEW list with items you KEEP: `[x for x in lst if condition]` [list comprehension + filter]. OR `list(filter(lambda x: condition, lst))`')

        if re.search(r'\bshift\b|\brotate\b', d):
            add('Rotate: `lst[k:] + lst[:k]` [slicing + concatenation]. For k=1: `[lst[-1]] + lst[:-1]` rotates right, `lst[1:] + [lst[0]]` rotates left')

        if re.search(r'\bremove.*duplicate|unique', d):
            add('Convert to `set(lst)` automatically removes duplicates [but loses order]. To preserve order: loop and only add unseen items to a new list')

        if re.search(r'\bsecond.*(?:largest|biggest|smallest|lowest|highest)\b', d):
            add('Sort descending: `sorted(lst, reverse=True)`. The second element `[1]` is the second largest. Use `set()` first if duplicates would cause issues')

        if re.search(r'\bmerge\b|\bcombine\b|\bconcat', d):
            add('`list1 + list2` — concatenation [creates a new list with all elements from both]. `list1.extend(list2)` — adds list2 elements to list1 IN-PLACE')

        # If we got specific content, great; otherwise add generic list step
        st = str(steps)
        has_specific = any(x in st for x in ['sum(', 'max(', 'min(', 'sorted', 'reverse', ' even', ' odd', 'prime', 'range(', 'square', 'triangle', 'pattern', 'matrix', 'transpos', 'counts', 'duplicate', 'set(lst', 'second', 'rotate', 'common'])
        if not has_specific:
            add('Loop through the list: `for item in lst:` — each iteration gives one element. Build the result inside the loop [accumulate in a variable, new list, or string]')

        add('Return the result. Check edge cases: empty list [avoid IndexError with `if not lst:`], single element, all-same values')
        return '\n'.join(f'{i+1}. {s}' for i, s in enumerate(steps))

    # ─── 10. STRING-SPECIFIC ────────────────────────────────
    if re.search(r'\bstring\b', d) or re.search(r'\b(?:upper|lower|capitalize|title|strip|lstrip|rstrip|split|join|replace|startswith|endswith|find)\b', d):
        add(intro)
        add(f'Define `def {fn}(s):` where `s` is a string [ordered sequence of characters, IMMUTABLE — methods return NEW strings, originals never change]')
        if re.search(r'\bupper\b', d):
            add('`s.upper()` — returns a new string with all letters capitalized [a→A, b→B]')
        if re.search(r'\blower\b', d):
            add('`s.lower()` — returns a new string with all letters lowercased [A→a, B→b]')
        if re.search(r'\bcapitalize\b', d):
            add('`s.capitalize()` — first character uppercase, rest lowercase')
        if re.search(r'\btitle\b', d):
            add('`s.title()` — first letter of EACH word uppercase [word boundaries are whitespace/punctuation]')
        if re.search(r'\bstrip\b', d):
            add('`s.strip()` — removes whitespace from both ends. `lstrip()` [left] and `rstrip()` [right] for one side only')
        if re.search(r'\bsplit\b', d):
            add('`s.split(sep)` — splits into a list at each separator. Default is whitespace. `s.split(",")` splits at commas')
        if re.search(r'\bjoin\b', d):
            add('`"glue".join(list_of_strings)` — joins elements with the "glue" string between each. Elements MUST be strings')
        if re.search(r'\breplace\b', d):
            add('`s.replace(old, new)` — replaces ALL occurrences of `old` with `new`. Returns a new string')
        if re.search(r'\bstartswith\b', d):
            add('`s.startswith(prefix)` — returns True if s begins with prefix [useful for filtering filenames or URLs]')
        if re.search(r'\bendswith\b', d):
            add('`s.endswith(suffix)` — returns True if s ends with suffix [checking file extensions: `".txt"`, `".jpg"`]')
        if re.search(r'\bfind\b', d) and not re.search(r'find.*common|find.*max|find.*min', d):
            add('`s.find(sub)` — returns the INDEX (position) of first occurrence, or -1 if not found [different from `in` which returns a boolean]')
        if re.search(r'\breverse\b', d) or re.search(r'backward|flip', d):
            add('`s[::-1]` — slicing with step -1 reverses the string. The bracket notation is `[start:stop:step]`: start defaults to beginning, stop defaults to end, -1 means go backward')
        if re.search(r'\bpalindrom\b', d):
            add('Check if the string equals its reverse: `s == s[::-1]` — if True, it reads the same forward and backward [racecar, level]')
        if re.search(r'\bvowel\b', d):
            add('Define `vowels = "aeiou"`. Loop through chars: `if ch.lower() in vowels:` — `in` [membership operator: True if value exists in the collection]. Count matches')
        if re.search(r'\bconsonant\b', d):
            add('Same as vowel check but invert: `if ch.lower() not in "aeiou" and ch.isalpha():` — `isalpha()` [True if the character is a letter]')
        if re.search(r'\banagram\b', d):
            add('Two strings are anagrams if they contain the same letters: `sorted(s1) == sorted(s2)` — `sorted()` [returns an alphabetically ordered list of characters]')
        if re.search(r'\bodd.index|odd.*position|odd.*character|every.*other|alternating', d):
            add('Use slicing: `s[1::2]` — start at index 1 [second character], step 2 [every other one]. The bracket syntax is `[start:stop:step]`')
        if re.search(r'\beven.index|even.*position|every.*second', d):
            add('Use slicing: `s[::2]` — start at index 0 [first], step 2 [every other one]')
        if re.search(r'\bdigit\b|\bnumber\b', d) and re.search(r'char|letter|string', d):
            add('`isdigit()` [True if all characters are digits (0-9)] — useful for separating digits from letters in a string')
        if re.search(r'\bcount\b', d) and re.search(r'char|letter|occurrence', d):
            add('`s.count(ch)` — returns the number of NON-OVERLAPPING occurrences of substring ch in s. Or loop manually with a counter variable')
        add('Return the result. Remember: strings are immutable [cannot be changed in-place], so all operations create new strings')
        return '\n'.join(f'{i+1}. {s}' for i, s in enumerate(steps))

    # ─── 11. TWO-NUMBER ARITHMETIC ──────────────────────────
    if re.search(r'takes\s+(?:a\s+)?(\w+\s+)?(?:two|2)\s+(?:numbers?|integers?|arguments?|parameters?|inputs?)', d):
        add(intro)
        add(f'Define `def {fn}(a, b):` — `a` and `b` are the parameters [inputs passed to the function inside brackets]')
        add('Implement the required operation: `+` [addition], `-` [subtraction], `*` [multiplication], `/` [float division: returns a float even if inputs are ints], `//` [floor division: integer quotient], `%` [modulo: remainder after division]')
        add('Compute the result and `return result` — `return` [keyword that exits function and sends value back to the caller]. Everything after return does NOT run')
        add(f'Test: `print({fn}(5, 3))` — the brackets `()` execute the function with arguments 5 and 3')
        return '\n'.join(f'{i+1}. {s}' for i, s in enumerate(steps))

    # ─── 12. MATH / DATE / OTHER BUILT-INS ──────────────────
    if re.search(r'\bimport\b', d) and not re.search(r'random|input|file|open', d):
        if re.search(r'\bmath\b', d):
            add(intro)
            add('`import math` — gives `math.sqrt()` [square root], `math.pi` [π constant], `math.factorial()` [factorial], `math.sin/cos/tan` [trigonometry]')
            if re.search(r'\bsqrt\b|square\s*root', d):
                add('`math.sqrt(x)` — returns the square root as a float. For integers only: `int(x**0.5)` checks if it\'s a perfect square')
            if re.search(r'\bsin\b|\bcos\b|\btan\b', d):
                add('Trig functions take RADIANS [not degrees]. Convert: `math.radians(degrees)` to convert, or `math.degrees(radians)` to go back')
            add('Use `math.<function>(...)` — the dot `.` accesses the function from the math module')

        elif re.search(r'datetime|time|date', d):
            add(intro)
            add('`from datetime import datetime` — or `import datetime`. Current time: `datetime.datetime.now()`')
            if re.search(r'\bformat\b|\bstrftime\b', d):
                add('`dt.strftime(format)` — formats datetime as string. Codes: `%Y` [year], `%m` [month], `%d` [day], `%H` [hour 24h], `%M` [minute], `%S` [second]')
            if re.search(r'\bparse\b|\bstrptime\b', d):
                add('`datetime.strptime(date_string, format)` — parses a STRING into a datetime OBJECT')
            if re.search(r'\bdiff\b|\bdelta\b|between', d):
                add('Subtract two datetimes: `diff = dt2 - dt1` — returns a `timedelta` [duration]. Access `.days` or `.total_seconds()`')

        else:
            add(intro)
            add(f'Import the required module at the top of your code: `import module_name`')
            add(f'Then use `module_name.function_name()` to access the imported functionality')

        return '\n'.join(f'{i+1}. {s}' for i, s in enumerate(steps))

    # ─── 13. FALLBACK ──────────────────────────────────────
    if re.search(r'\breturn\b|\bfind\b|\bget\b|\bcheck\b|\bdetermine\b|\bcalculate\b|\bcompute\b', d):
        add(intro)
        add(f'Define `def {fn}(parameters):` — colon `:` marks the start of the function body [all code INSIDE is indented 4 spaces]')
        add('Break down the problem: identify the INPUT (parameters), the PROCESS (what to do with it), and the OUTPUT (what to return)')
        add('Implement step-by-step logic in the function body — you can use intermediate variables to hold partial results')
        add('Use `return result` — the `return` keyword [exits function and sends a value back]. The caller gets this value')

    elif re.search(r'\bprint\b|\bdisplay\b|\bshow\b|\boutput\b', d):
        add(intro)
        add(f'Define `def {fn}(parameters):` — colon `:` marks the function body. Everything indented after is part of the function')
        add('Compute or prepare the value to display')
        add('Use `print(value)` — displays the value on screen (but does NOT return it). Use `print(f"template {var}")` for formatted output')
        add(f'Call `{fn}(args)` to see the output')

    elif re.search(r'\bmodify\b|\bupdate\b|\bchange\b|\btransform\b|\bconvert\b', d):
        add(intro)
        add(f'Define `def {fn}(input):` — the input parameter holds the original data')
        add('Create a new version with the changes applied [for immutable types like strings/numbers] or modify in-place [for mutable types like lists/dicts]')
        add('Return the modified result (for a function) or print it (for a script)')

    else:
        add(intro)
        add(f'Define `def {fn}(parameters):` — the function name matches the problem description exactly')
        add('Think about: What data comes in? What steps transform it? What comes out? Write each step on its own line')
        add('Use `return` to send the result back, or `print()` to display it')
        add('Test with the examples provided and compare output character by character')

    # Add edge case reminder
    has_tested = any(w in (steps[-1].lower() if steps else '') for w in ['test', 'verify', 'example', 'trace', 'check', 'edge'])
    if not has_tested:
        add('Test with the example inputs and outputs from the problem — compare exact values. Check edge cases like empty input, zero, or negative values')
    
    return '\n'.join(f'{i+1}. {s}' for i, s in enumerate(steps))

# ─── APPLY TO ALL EXERCISES ─────────────────────────────────
insertions = []
for block_lines in exercises:
    desc = extract_field(block_lines, 'description')
    if desc:
        desc_clean = desc.replace('\\n', ' ').replace('\\"', '"').replace('\\t', ' ')
        breakdown = generate_breakdown(desc_clean)

        hint_field = '"hint":'
        rel_hi = None
        for j, (bl, _) in enumerate(block_lines):
            if hint_field in bl:
                rel_hi = j; break

        if rel_hi is not None:
            hint_li = block_lines[rel_hi][1]
            esc = breakdown.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n').replace('\t', '\\t')
            insertions.append((hint_li, f'            "breakdown": "{esc}",\n'))

insertions.sort(key=lambda x: x[0], reverse=True)
for idx, text in insertions:
    lines.insert(idx, text)

with open(EXERCISES_FILE, 'w') as f:
    f.writelines(lines)

print(f'Done. Generated {len(insertions)} granular breakdowns.')
