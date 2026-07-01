#!/usr/bin/env python3
"""
Generate comprehensive step-by-step breakdowns for all Python exercises.
Each breakdown explains: the goal, the order of operations, key concepts (with definitions),
function/method call mechanics, variable flow, and edge cases — WITHOUT giving away the answer.
"""
import re

EXERCISES_FILE = '/Users/moll/Desktop/python_app/exercises.ts'

with open(EXERCISES_FILE, 'r') as f:
    lines = f.readlines()

# Find array start
start_idx = 0
for i, line in enumerate(lines):
    if 'Exercise[] = [' in line or ('EXERCISES:' in line and '[' in line):
        start_idx = i + 1
        break

# Parse exercise blocks (tracking line ranges)
in_exercise = False
depth = 0
current = []
exercises = []

for i in range(start_idx, len(lines)):
    line = lines[i]
    ob = line.count('{')
    cb = line.count('}')
    if '{' in line and not in_exercise:
        in_exercise = True
        depth = ob - cb
        current = [(line, i)]
    elif in_exercise:
        current.append((line, i))
        depth += ob - cb
        if depth <= 0:
            exercises.append(current)
            current = []
            in_exercise = False

def extract_field(block, field):
    """Extract a field value from an exercise block (handles string fields)."""
    full = ''.join(l for l, _ in block)
    m = re.search(r'"' + field + r'":\s*"((?:[^"\\]|\\.)*)"', full)
    if m:
        return m.group(1)
    return ''


def generate_breakdown(desc: str) -> str:
    d = desc.lower()
    steps = []

    # Common preamble for every exercise
    intro = 'Read the problem carefully. Identify: (1) what the function name is, (2) what parameters it takes, (3) what it should return or print. The examples show the expected inputs and outputs — use them to infer the logic.'

    # ─── CATEGORIES ───────────────────────────────────────────────

    # === CLASS / OOP ===
    if re.search(r'\bclass\b', d) or re.search(r'\binherit\b', d) or re.search(r'base class', d):
        steps.append(intro)
        steps.append('Define a class using the `class ClassName:` keyword (creates a blueprint for objects).')
        if re.search(r'__init__|constructor|initialize', d):
            steps.append('Add the `__init__` method (constructor — runs automatically when a new object is created). Inside it, assign attributes with `self.attr_name = value`.')
        if re.search(r'base class|parent', d):
            steps.append('Define the base (parent) class first with shared attributes and methods.')
        if re.search(r'derived|child|inherit|subclass|override', d):
            steps.append('Create the derived class: `class Child(Parent):` — the parent name in parentheses establishes inheritance (child gets all parent methods).')
            steps.append('Override methods by re-defining them in the child class with the same name. When called, the child version runs instead.')
        if re.search(r'method', d):
            steps.append('Define methods with `def method_name(self, ...):` — `self` (reference to the current instance) is always the first parameter, passed automatically when calling `obj.method()`.')
        if re.search(r'static|@staticmethod', d):
            steps.append('Use `@staticmethod` above a method that does NOT need `self` — it behaves like a regular function but lives inside the class namespace.')
        if re.search(r'encapsulation|private', d):
            steps.append('Prefix attribute names with one underscore `_attr` (convention for internal use). Provide getter/setter methods to access them.')
        steps.append('Test by creating instances: `obj = ClassName(args)`, then call methods: `obj.method()`. Remember the brackets `()` — they execute the function.')

    # === RECURSION ===
    elif re.search(r'\brecursi', d) or re.search(r'recursion|\brecursive\b', d):
        steps.append(intro)
        steps.append('Every recursive function needs TWO parts: a base case (stops the recursion) and a recursive case (calls itself with a smaller input).')
        if re.search(r'fibonacci|fib', d):
            steps.append('Base case: `if n <= 1: return n` (fib(0)=0, fib(1)=1). Recursive case: `return fib(n-1) + fib(n-2)` (sum of the two previous numbers).')
        if re.search(r'factorial', d):
            steps.append('Base case: `if n <= 1: return 1` (factorial of 0 or 1 is 1). Recursive case: `return n * factorial(n-1)` (n! = n × (n-1)!).')
        if re.search(r'palindrome', d):
            steps.append('Base case: `if len(s) <= 1: return True` (a single char or empty string is always a palindrome). Recursive case: check first == last, then recurse on `s[1:-1]`.')
        if re.search(r'sum|total|add', d) and not re.search(r'add_number|add_num', d):
            steps.append('Base case: empty list returns 0. Recursive case: `lst[0] + sum(lst[1:])` (first element + sum of the rest).')
        if re.search(r'tower|hanoi', d):
            steps.append('Move n-1 disks from source to auxiliary (helper peg), move the largest disk to target, then move n-1 disks from auxiliary to target.')
        if re.search(r'tree|directory', d):
            steps.append('Process the current node, then recursively process each child — the recursive call handles the branching structure naturally.')
        steps.append('Ensure each call moves toward the base case (e.g., reducing n, shortening the string, removing an element). Without this, you get infinite recursion.')
        steps.append('Trace through with a tiny input first to verify your logic before testing larger cases.')

    # === LAMBDA / HIGHER-ORDER FUNCTIONS ===
    elif re.search(r'\blambda\b', d) or re.search(r'\bfilter\b', d) or re.search(r'\bmap\b', d) or re.search(r'\breduce\b', d):
        steps.append(intro)
        steps.append('A lambda (anonymous inline function) is written as: `lambda parameters: expression` — no def, no return, just the expression result.')
        if re.search(r'\bmap\b', d):
            steps.append('`map(func, iterable)` applies func to every element and returns an iterator (lazy — values computed on demand). Convert to list: `list(map(...))`. The order of operations: func(element) for each element, result collected in the same order.')
        if re.search(r'\bfilter\b', d):
            steps.append('`filter(func, iterable)` keeps elements where func returns True. The lambda should return a boolean condition. Convert to list to see results.')
        if re.search(r'\breduce\b', d):
            steps.append('`reduce(func, iterable)` cumulatively applies func: first two elements → result, then result + next element, etc. Import it: `from functools import reduce`.')
        if re.search(r'\bsort\b|\bsorted\b', d):
            steps.append('Use the `key` parameter: `sorted(list, key=lambda x: expression)` — key transforms each element for comparison without changing the original values.')
        steps.append('Think of lambda as a shorthand — for simple one-line logic, it avoids writing a full `def`. Convert the result to a list if you need to store/display it.')

    # === DECORATOR ===
    elif re.search(r'@|decorator', d):
        steps.append(intro)
        steps.append('A decorator is a function that takes ANOTHER function as input and extends its behavior — think of it as wrapping the original.')
        steps.append('Define the decorator: `def decorator_name(func):` — it receives the original function as a parameter.')
        steps.append('Inside, define a wrapper function: `def wrapper(*args, **kwargs):` — this runs additional logic before/after calling `func(*args, **kwargs)`.')
        steps.append('Return the wrapper function (not the result of calling it — no brackets!). The decorator pattern: outer function receives func, inner function adds behavior.')
        if re.search(r'timer|time|duration', d):
            steps.append('Use `time.time()` before and after calling func, compute the difference, and print the duration.')
        if re.search(r'log|debug|trace', d):
            steps.append('Print `f"Calling {func.__name__} with {args}, {kwargs}"` before calling func.')
        if re.search(r'memoize|cache', d):
            steps.append('Store results in a dictionary `cache = {}` keyed by arguments. Before computing, check if args are already in cache.')
        steps.append('Apply with `@decorator_name` on the line above the function definition — this is syntactic sugar for `func = decorator_name(func)`.')

    # === GENERATOR ===
    elif re.search(r'\byield\b|\bgenerator\b', d):
        steps.append(intro)
        steps.append('A generator looks like a function but uses `yield` instead of `return` — it produces ONE value at a time and PAUSES execution between yields (lazy evaluation).')
        steps.append('When called, a generator function returns a generator object (not a value). It executes until the first `yield`, returns that value, and freezes state.')
        steps.append('Use a for loop to pull values: `for val in my_generator():` — or use `next(gen)` to get one value at a time.')
        if re.search(r'fibonacci|fib|sequence', d):
            steps.append('Initialize a=0, b=1. In an infinite loop: `yield a`, then `a, b = b, a + b` to advance the sequence.')
        if re.search(r'infinite', d):
            steps.append('Use `while True` with `yield` inside — the caller controls how many values to consume, so infinite generators are safe when used in a loop with a break condition.')
        steps.append('Generators are memory-efficient — they don\'t store the whole sequence, just produce values on the fly. Perfect for large or infinite data streams.')

    # === CONTEXT MANAGER ===
    elif re.search(r'context manager|__enter__|__exit__|with\s+(open|open\(|statement)', d) or (re.search(r'\bwith\b', d) and re.search(r'\bopen\b|\bcontext\b|\bmanager\b', d)):
        steps.append(intro)
        steps.append('A context manager uses `__enter__` (setup, runs when `with` block starts) and `__exit__` (cleanup, runs when block ends — even on errors).')
        steps.append('Define a class with `__enter__(self)` that returns the resource (this is what the `as` variable gets).')
        steps.append('Define `__exit__(self, exc_type, exc_val, exc_tb)` that handles cleanup (closing files, releasing locks, etc.).')
        steps.append('Usage: `with MyContext() as x:` — this guarantees `__exit__` runs even if the block raises an exception.')

    # === INPUT / OUTPUT ===
    elif re.search(r'input\(\)|read.*from.*user|prompt|write.*program.*(input|asks|enter)', d):
        steps.append(intro)
        steps.append('`input()` reads a line from the user as a STRING. If you need numbers, convert with `int(input())` or `float(input())`.')
        if re.search(r'multiple|several|number of|n\b', d) and not re.search(r'\bint\b|\breturn\b|\bparameter\b', d):
            steps.append('If the problem asks for multiple values, use a loop (for _ in range(n)) or `split()` on the input string.')
        if re.search(r'file|read|write|open\b', d):
            steps.append('Open a file with `open("filename", "r")` — "r" for reading, "w" for writing, "a" for appending.')
            steps.append('Use a `with` statement to auto-close the file: `with open(...) as f:` — this is the safe pattern.')
            steps.append('Read with `f.read()` (entire content), `f.readline()` (one line), or loop `for line in f:` (memory efficient).')
        if re.search(r'menu|choice|option', d):
            steps.append('Print available options, use `input()` to get the user\'s choice, then handle it with an if/elif chain or a dictionary mapping choices to actions.')
        steps.append('Print the result using `print()`. Remember: `print()` adds a newline by default, use `end=""` to stay on the same line.')

    # === COMPREHENSION ===
    elif re.search(r'\bcomprehension\b|\blist comprehension\b', d) or re.search(r'comprehension', d):
        steps.append(intro)
        steps.append('A comprehension builds a new sequence in one line. The order of operations is: `[expression  for  item  in  iterable  if  condition]`.')
        steps.append('Read it left-to-right in this mental order: (1) `for item in iterable` — loop over each element, (2) `if condition` — filter (optional), (3) the expression is the result that goes into the new list.')
        steps.append('List: `[x*2 for x in range(10)]` — square brackets `[]`. Set: `{x*2 for x in range(10)}` — curly braces `{}`. Dict: `{x: x*2 for x in range(10)}` — key:value pairs.')
        steps.append('Nested comprehensions: the outer loop comes first, inner loop second: `[expr for a in A for b in B]` reads as nested for loops.')
        steps.append('When in doubt, write the nested for loop version first, then compress it into a comprehension for practice.')

    # === FUNCTION DEFINITION (MOST COMMON) ===
    else:
        steps.append(intro)
        steps.append('Define the function: `def function_name(parameters):` — the name must match the problem exactly. The colon `:` starts the body, and everything INSIDE must be indented (typically 4 spaces).')
        steps.append('The parentheses `()` after the name hold the parameters (inputs). When calling a function, the values you pass IN the brackets map to these parameters in order (positional arguments).')

        # Parameter type guidance
        if re.search(r'takes.*list|takes.*array|a list|the list', d) or re.search(r'\blist\b', d):
            steps.append('The parameter is a list (ordered, mutable collection `[]`). Access elements by index: `lst[0]` (first element), `lst[-1]` (last). Use `len(lst)` for its size. Iterate with `for item in lst:` or `for i in range(len(lst)):`.')
        if re.search(r'takes.*string|a string|the string', d) or re.search(r'\bstring\b', d):
            steps.append('The parameter is a string (ordered, immutable sequence of characters). Strings support methods like `.upper()`, `.lower()`, `.split()`, `.join()`, `.strip()`. Use `for ch in string:` to iterate over characters.')
        if re.search(r'takes.*number|takes.*integer|takes.*int|two numbers|a number', d) or re.search(r'numbers\b', d):
            steps.append('The parameters are numbers. Use arithmetic operators: `+` (add), `-` (subtract), `*` (multiply), `/` (float division), `//` (integer division), `%` (modulo — remainder).')
        if re.search(r'takes.*dictionary|takes.*dict|a dictionary', d) or re.search(r'\bdict\b', d):
            steps.append('The parameter is a dictionary (key-value store `{}`). Access values: `d[key]` or `d.get(key)`. Iterate: `for k in d:` (keys), `for v in d.values():`, `for k, v in d.items():`.')
        if re.search(r'takes.*tuple|a tuple', d):
            steps.append('The parameter is a tuple (ordered, IMMUTABLE collection `()`). Supports indexing and iteration like lists, but cannot be modified after creation.')
        if re.search(r'takes.*set|a set', d):
            steps.append('The parameter is a set (unordered, unique collection `{}`). Supports `|` (union), `&` (intersection), `-` (difference), `.add()`, `.remove()`.')

        # What to produce
        if re.search(r'return|find|get|check|determine|calculate|compute', d):
            steps.append('Implement the logic inside the function body (indented under `def`). Use `return` to send the result back to the caller. `return` exits the function immediately — anything after it in the function does not run.')
        elif re.search(r'print|display|show|output', d):
            steps.append('Use `print(value)` inside the function to display output to the console. Unlike `return`, `print` shows the value but does NOT give it back to the caller.')
        elif re.search(r'modify|update|change|transform|convert', d):
            steps.append('Either modify the input in-place (for mutable types like lists) or create a transformed copy and return it.')

        # Specific patterns — each with full pedagogical explanation
        if re.search(r'\bsum\b|\btotal\b', d) and not re.search(r'takes two', d):
            steps.append('To sum elements: initialize `total = 0` (accumulator variable — starts empty, gets added to in a loop). Loop through each element and add to total: `total += element`. Alternatively, use the built-in `sum(iterable)` for simple cases.')
        if re.search(r'\bmax\b|\bmaximum\b|\blargest\b|\bbiggest\b', d):
            steps.append('To find the maximum: initialize `max_val = lst[0]` (first element as starting candidate). For each item, check `if item > max_val: max_val = item` (update when we find a larger one). This is called a "linear scan" — O(n) time.')
        if re.search(r'\bmin\b|\bminimum\b|\bsmallest\b', d):
            steps.append('To find the minimum: initialize `min_val = lst[0]`, loop through and update when `item < min_val`. Same pattern as max but with `<` instead of `>`.')
        if re.search(r'\baverage\b|\bmean\b|\bavg\b', d):
            steps.append('Average = (sum of values) / (count of values). Use `sum(lst) / len(lst)` or accumulate with a loop. Be careful: if using integer division `//`, you\'ll lose the decimal — use `/` for float division.')
        if re.search(r'\breverse\b|\bbackward\b|\bflip\b', d):
            steps.append('Reverse with slicing `[::-1]` (step of -1 traverses backward), `reversed(iterable)` (returns an iterator), or a loop building a new list from the end.')
        if re.search(r'\bsort\b|\bsorted\b|\border\b|\barrange\b', d):
            steps.append('`sorted(iterable)` returns a NEW sorted list (original unchanged). `list.sort()` sorts IN-PLACE (original is modified, returns None). Both accept `reverse=True` for descending order and `key=func` for custom sort logic.')
        if re.search(r'\bcount\b|\bfrequency\b|\boccurrence\b', d):
            steps.append('To count: use `.count(value)` for a single value, or iterate with a dictionary: `{item: lst.count(item) for item in set(lst)}` or `collections.Counter(lst)`.')
        if re.search(r'\bremove\b|\bdelete\b|\beliminate\b', d):
            steps.append('To filter items: build a NEW list with only the items you want to keep. Use a list comprehension: `[x for x in lst if condition(x)]`. Or loop and append to a new list.')
        if re.search(r'\bduplicate\b|\bunique\b|\bdistinct\b', d) or re.search(r'common.*number.*list', d):
            steps.append('To find duplicates: track "seen" items in a list or set. Loop through, check if already seen. If yes, it\'s a duplicate. To get unique items: `list(set(lst))` (sets automatically remove duplicates).')
        if re.search(r'\bpalindrome\b', d):
            steps.append('A palindrome reads the same forward and backward. Check with `s == s[::-1]` (compare string to its reverse). For case-insensitive: `s.lower() == s.lower()[::-1]`.')
        if re.search(r'\banagram\b', d):
            steps.append('Anagram: same letters, different order. Compare sorted versions: `sorted(s1) == sorted(s2)`. Or compare character counts with a dictionary or Counter.')
        if re.search(r'\bvowel\b|\bconsonant\b', d):
            steps.append('Define vowels as a string: `vowels = "aeiou"`. Loop through each character, check `if ch.lower() in vowels:` to count them. Use a list comprehension or loop with a counter.')
        if re.search(r'\bprime\b', d):
            steps.append('A prime is only divisible by 1 and itself. Check from 2 to sqrt(n): if any divides evenly (`n % i == 0`), it is not prime. You can speed this up by checking only up to `int(n**0.5) + 1`.')
        if re.search(r'\beven\b|\bodd\b', d):
            steps.append('Use the modulo operator `%`: `n % 2 == 0` means even (divisible by 2 with no remainder), `n % 2 != 0` means odd.')
        if re.search(r'\bleap\b', d) and 'year' in d:
            steps.append('Leap year logic: divisible by 4 AND (NOT divisible by 100 OR divisible by 400). In code: `year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)`.')
        if re.search(r'\bfactor\b|\bdivisor\b|\bgcd\b|\bhcf\b', d):
            steps.append('GCD (Greatest Common Divisor): use `math.gcd(a, b)` or the Euclidean algorithm — repeatedly take remainder: `while b: a, b = b, a % b`.')
        if re.search(r'\blcm\b|\blcd\b', d):
            steps.append('LCM (Least Common Multiple): `lcm = a * b // gcd(a, b)`. It\'s the product divided by the GCD.')
        if re.search(r'\brange\b|\bbetween\b|\bsequence\b', d):
            steps.append('`range(start, stop, step)` generates numbers from start to stop-1. Default start=0, step=1. Use `range(n)` for 0..n-1, `range(1, n+1)` for 1..n.')
        if re.search(r'\bpattern\b|\btriangle\b|\bpyramid\b|\bstar\b|\bdiamond\b', d):
            steps.append('Use nested loops: the OUTER loop handles rows, the INNER loop handles columns. The inner loop\'s range often depends on the outer loop variable to create the shape.')
        if re.search(r'\bmatrix\b|\bgrid\b|\b2d\b|\btwo dimension\b', d):
            steps.append('A 2D list (matrix) is a list of lists: `matrix = [[1,2],[3,4]]`. Access with `matrix[row][col]`. Use nested loops: outer iterates rows, inner iterates columns of each row.')
        if re.search(r'\btemperature\b|\bcelsius\b|\bfahrenheit\b', d):
            steps.append('Celsius to Fahrenheit: `F = C * 9/5 + 32`. Fahrenheit to Celsius: `C = (F - 32) * 5/9`. Watch the order of operations — multiplication/division happens before addition.')
        if re.search(r'\bcurrency\b|\bdollar\b|\bmoney\b', d) or re.search(r'format.*money|format.*curren', d):
            steps.append('Format currency: `f"${value:.2f}"` means: dollar sign, then the number rounded to 2 decimal places. If the value is in cents, divide by 100 first.')
        if re.search(r'\bemail\b', d) or re.search(r'valid.*email|check.*email', d):
            steps.append('Basic email validation: check for `@` and at least one `.` after the `@`. Use `in` operator: `if "@" in email and "." in email.split("@")[1]:`.')
        if re.search(r'\bpermutation\b|\bcombination\b', d):
            steps.append('Use `itertools.permutations(iterable, r)` for all ordered arrangements, `itertools.combinations(iterable, r)` for unordered selections. Import from itertools first.')

        # Fallback if no specific logic steps were added
        step_text = '\n'.join(steps)
        has_specific = any(w in step_text for w in ['Use arithmetic', 'Loop through', 'Initialize', 'Use the modulo', 'Use a for', 'Compare the'])
        if not has_specific:
            steps.append('Break the problem into smaller parts. What\'s the first step? The intermediate values? The final output? Write each step as a line of code and test incrementally.')

    # ─── CLOSING ──────────────────────────────────────────────
    steps.append('Test your function with the provided examples. Call it like: `function_name(test_input)` — the brackets `()` execute the function and pass the arguments.')
    steps.append('Check edge cases: empty list, single element, negative numbers, zero, very large values. Verify your function handles these without errors.')
    if re.search(r'\bsort\b|\bsearch\b|\bcount\b|\bfind\b|\bcheck\b', d):
        steps.append('If you\'re stuck, trace through the loop manually with pen and paper for a small input — write down the variable values at each step.')

    return '\n'.join(f'{i+1}. {s}' for i, s in enumerate(steps))


# Collect all insertion points
insertions = []

for block_lines in exercises:
    desc = extract_field(block_lines, 'description')
    if desc:
        desc_clean = desc.replace('\\n', ' ').replace('\\"', '"').replace('\\t', ' ')
        breakdown = generate_breakdown(desc_clean)

        hint_field = '"hint":'
        rel_hint_idx = None
        for j, (bl, _) in enumerate(block_lines):
            if hint_field in bl:
                rel_hint_idx = j
                break

        if rel_hint_idx is not None:
            hint_line_idx = block_lines[rel_hint_idx][1]
            esc_breakdown = breakdown.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n').replace('\t', '\\t')
            insert_text = f'            "breakdown": "{esc_breakdown}",\n'
            insertions.append((hint_line_idx, insert_text))

# Insert in reverse order
insertions.sort(key=lambda x: x[0], reverse=True)
for idx, text in insertions:
    lines.insert(idx, text)

with open(EXERCISES_FILE, 'w') as f:
    f.writelines(lines)

print(f'Done. Generated {len(insertions)} comprehensive breakdowns.')
