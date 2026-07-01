#!/usr/bin/env python3
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

# Parse exercises into blocks (tracking their line ranges)
in_exercise = False
depth = 0
current = []
exercises = []  # list of (block_lines, block_start_idx)

for i in range(start_idx, len(lines)):
    line = lines[i]
    ob = line.count('{')
    cb = line.count('}')
    
    if '{' in line and not in_exercise:
        in_exercise = True
        depth = ob - cb
        current = [line]
        current_start = i
    elif in_exercise:
        current.append(line)
        depth += ob - cb
        if depth <= 0:
            exercises.append((current, current_start))
            current = []
            in_exercise = False

def extract_field(block_lines, field):
    full = ''.join(block_lines)
    m = re.search(r'"' + field + r'":\s*"((?:[^"\\]|\\.)*)"', full)
    if m:
        return m.group(1)
    return ''

def generate_breakdown(desc):
    d = desc.lower()
    steps = []
    is_simple_arith = bool(re.search(r'takes two (numbers|parameters|arguments|integers)', d)) and not re.search(r'list', d)

    if re.search(r'\bclass\b', d) or re.search(r'\binherit', d) or re.search(r'base class', d):
        steps.append('Define the class structure using the class keyword.')
        if re.search(r'base class|parent', d):
            steps.append('Create the base/parent class first with the required methods.')
        if re.search(r'__init__|constructor|initialize', d):
            steps.append('Add an __init__ method to initialize object attributes.')
        if re.search(r'derived|child|inherit|subclass|override', d):
            steps.append('Create the derived class by passing the parent class name in parentheses: class Child(Parent).')
            steps.append('Override the required methods in the derived class.')
        if re.search(r'method', d):
            steps.append('Define methods inside the class with self as the first parameter.')
        if re.search(r'encapsulation|private|_', d) and 'attribute' in d:
            steps.append('Use underscore prefix (_attr) for private attributes and create getter/setter methods.')
        if re.search(r'static|@staticmethod', d):
            steps.append('Use the @staticmethod decorator for methods that don\'t need instance access.')
        if re.search(r'duck typing|duck', d):
            steps.append('Focus on what methods the object has rather than its type.')
        steps.append('Test by creating instances and calling their methods.')

    elif re.search(r'\brecursi', d) or re.search(r'recursive', d) or re.search(r'recursion', d):
        steps.append('Identify the base case — the simplest input where you return a direct answer without recursing.')
        steps.append('Identify the recursive case — break the problem into a smaller version of the same problem.')
        steps.append('Define a function that calls itself with modified arguments (moving toward the base case).')
        steps.append('Ensure each recursive call reduces the problem size so you eventually hit the base case.')
        if re.search(r'fibonacci|fib', d):
            steps.append('Base: fib(0)=0, fib(1)=1. Recursive: fib(n) = fib(n-1) + fib(n-2).')
        if re.search(r'factorial', d):
            steps.append('Base: factorial(0)=1. Recursive: factorial(n) = n * factorial(n-1).')
        if re.search(r'tree|directory', d):
            steps.append('Process the current node, then recursively process each child/subdirectory.')
        if re.search(r'tower|hanoi', d):
            steps.append('Move n-1 disks to auxiliary peg, move largest disk to target, move n-1 disks to target.')
        if re.search(r'palindrome', d):
            steps.append('Base: string of length 0 or 1 is a palindrome. Recursive: check first and last char, then recurse on the inner substring.')
        if re.search(r'sum|total|add', d):
            steps.append('Base: empty list sums to 0. Recursive: first element + sum of rest.')
        steps.append('Always test with the smallest input first to verify your base case.')

    elif re.search(r'\blambda\b', d) or re.search(r'\bfilter\b', d) or re.search(r'\bmap\b', d) or re.search(r'\breduce\b', d):
        steps.append('Identify whether you need map (transform), filter (select), or reduce (accumulate).')
        steps.append('Write a lambda function for the transformation or condition: lambda x: expression.')
        steps.append('Pass the lambda as the first argument to map/filter/reduce.')
        if re.search(r'map', d):
            steps.append('map(function, iterable) applies the function to each element and returns an iterator.')
        if re.search(r'filter', d):
            steps.append('filter(function, iterable) keeps elements where the function returns True.')
        if re.search(r'reduce', d):
            steps.append('reduce(function, iterable) cumulatively applies the function — import from functools first.')
        if re.search(r'sort|sorted', d):
            steps.append('Use the key parameter: sorted(list, key=lambda x: expression) for custom sort order.')
        steps.append('Convert the result to a list if needed: list(result).')

    elif re.search(r'@|decorator', d):
        steps.append('A decorator is a function that takes another function and extends its behavior.')
        steps.append('Define the decorator function that accepts a function as a parameter.')
        steps.append('Define a wrapper function inside the decorator that adds behavior before/after the original function.')
        steps.append('Return the wrapper function from the decorator.')
        if re.search(r'timer|time|duration', d):
            steps.append('Use time.time() before and after calling the original function to measure duration.')
        if re.search(r'log|debug|trace', d):
            steps.append('Print or store the function name and arguments before calling it.')
        if re.search(r'auth|login|access', d):
            steps.append('Check credentials/permissions inside the wrapper before calling the original function.')
        if re.search(r'memoize|cache', d):
            steps.append('Store results in a dictionary keyed by arguments; return cached result if available.')
        steps.append('Apply the decorator with @decorator_name above the function definition.')

    elif re.search(r'\byield\b|\bgenerator\b', d):
        steps.append('Define a function using def — generators look like functions.')
        steps.append('Use the yield keyword instead of return to produce each value one at a time.')
        steps.append('The function state is preserved between calls — each yield pauses execution.')
        steps.append('Use the generator in a for loop or with next() to get values.')
        if re.search(r'fibonacci|fib|sequence', d):
            steps.append('Initialize the first two values, then yield each value and update in a loop.')
        if re.search(r'infinite', d):
            steps.append('Use while True with yield inside — the caller controls when to stop.')

    elif re.search(r'context|__enter__|__exit__|with\b', d) and not re.search(r'with no.*set|with.*set|with.*list', d):
        steps.append('Define a class with __enter__ and __exit__ methods.')
        steps.append('__enter__ sets up the resource and returns it (as the "as" target).')
        steps.append('__exit__ handles cleanup and takes (self, exc_type, exc_val, exc_tb) parameters.')
        steps.append('Use the class with the with statement: with MyManager() as x:.')

    elif re.search(r'input\(\)|read.*from.*user|prompt|read.*keyboard', d) or re.search(r'write.*program.*(input|asks|enter)', d):
        steps.append('Use input() to read user input — it returns a string by default.')
        steps.append('Convert the input to the correct type (int, float) if you need to do math.')
        if re.search(r'multiple|several|number of|n\b', d):
            steps.append('Use a loop to collect or process multiple inputs.')
        if re.search(r'file|read|write|open\b', d):
            steps.append('Open the file using open(filename, mode) — "r" for reading, "w" for writing.')
            steps.append('Use a with statement to ensure the file is closed automatically.')
            steps.append('Iterate over the file object or use .read() / .readlines().')
        if re.search(r'menu|choice|option', d):
            steps.append('Display options using print(), then use input() to get the user\'s choice.')
            steps.append('Use if/elif/else or a dictionary to handle each choice.')
        steps.append('Print the result using print().')

    else:
        steps.append('Read the problem carefully to understand what the function should do.')
        steps.append('Define the function using def function_name(parameters): — match the exact name from the problem.')
        if re.search(r'takes.*list|takes.*array|a list|the list|list\b.*parameter|parameter.*list', d) or re.search(r'\blist\b', d):
            steps.append('The parameter is a list — use list operations like indexing, loops, and built-in methods.')
        if re.search(r'takes.*string|a string|the string|string\b.*parameter|parameter.*string', d) or re.search(r'\bstring\b', d):
            steps.append('The parameter is a string — use string methods like .upper(), .lower(), .split(), .join().')
        if re.search(r'takes.*number|takes.*integer|takes.*int|two numbers|a number|numbers\b', d) or re.search(r'parameter.*int|int.*parameter', d):
            steps.append('The parameters are numbers — use arithmetic operators (+, -, *, /, //, %).')
        if re.search(r'takes.*dictionary|takes.*dict|a dictionary|the dictionary', d) or re.search(r'\bdict\b', d):
            steps.append('The parameter is a dictionary — use keys, .get(), .items(), .values().')
        if re.search(r'takes.*tuple|a tuple|the tuple', d):
            steps.append('The parameter is a tuple — tuples support indexing and iteration like lists (but are immutable).')
        if re.search(r'takes.*set|a set|the set', d):
            steps.append('The parameter is a set — use set operations like union, intersection, difference.')
        if re.search(r'takes.*boolean|takes.*bool|boolean|True|False', d):
            steps.append('The parameter is a boolean — use if/else logic based on the boolean value.')

        if re.search(r'return|find|get|check|determine|calculate|compute', d):
            steps.append('Add logic inside the function body to compute the result.')
            steps.append('Use return to send the result back to the caller.')
        elif re.search(r'print|display|show|output', d):
            steps.append('Use print() inside the function to display the result.')
        elif re.search(r'modify|update|change|transform|convert', d):
            steps.append('Modify the input or create a transformed version and return or print it.')

        if not is_simple_arith:
            if re.search(r'\bsum\b|\btotal\b', d) or (re.search(r'\baccumulate\b', d)):
                steps.append('Initialize an accumulator variable and add each element in a loop, or use sum().')
            if re.search(r'\bmax\b|\bmaximum\b|\blargest\b|\bbiggest\b', d):
                steps.append('Track the largest value seen so far: initialize to the first element, update when a larger one is found.')
            if re.search(r'\bmin\b|\bminimum\b|\bsmallest\b', d):
                steps.append('Track the smallest value: initialize to the first element, update when a smaller one is found.')
            if re.search(r'\baverage\b|\bmean\b|\bavg\b', d):
                steps.append('Compute sum / count — use sum(lst) / len(lst) or accumulate manually.')
        if re.search(r'\breverse\b|\bbackward\b|\bflip\b', d):
            steps.append('Iterate in reverse using slicing [::-1] or a reverse loop.')
        if re.search(r'\bsort\b|\bsorted\b|\border\b|\barrange\b', d):
            steps.append('Use sorted() to return a new sorted list or .sort() to sort in place.')
        if re.search(r'\bcount\b|\bfrequency\b|\boccurrence\b', d):
            steps.append('Use .count() for single value counts, or a loop/dict for multiple frequencies.')
        if re.search(r'\bremove\b|\bdelete\b|\beliminate\b|\bfilter out\b', d):
            steps.append('Use a loop to collect items that should stay, or use list comprehension with a condition.')
        if re.search(r'\bduplicate\b|\bunique\b|\bdistinct\b', d) or re.search(r'common.*number.*list|takes.*list.*return.*common', d):
            steps.append('Track seen items in a list/set and collect items that appear more than once.')
        if re.search(r'\bpalindrome\b', d):
            steps.append('Compare the string to its reverse: s == s[::-1].')
        if re.search(r'\banagram\b', d):
            steps.append('Sort both strings and compare: sorted(s1) == sorted(s2).')
        if re.search(r'\bvowel\b|\bconsonant\b', d):
            steps.append('Define a string of vowels, then count characters that appear in it using a loop or comprehension.')
        if re.search(r'\bprime\b', d):
            steps.append('Check divisibility from 2 to sqrt(n) — if any divides evenly, it is not prime.')
        if re.search(r'\beven\b|\bodd\b', d):
            steps.append('Use the modulo operator % — number % 2 == 0 for even, != 0 for odd.')
        if re.search(r'\bleap\b', d) and 'year' in d:
            steps.append('Leap year rule: divisible by 4 AND (not divisible by 100 OR divisible by 400).')
        if re.search(r'\bfactor\b|\bdivisor\b|\bgcd\b|\bhcf\b', d):
            steps.append('Find the greatest common divisor using math.gcd() or the Euclidean algorithm with the % operator.')
        if re.search(r'\blcm\b|\blcd\b', d):
            steps.append('LCM = a * b // gcd(a, b).')
        if re.search(r'\brange\b|\bbetween\b', d):
            steps.append('Use range(start, stop, step) to generate sequence bounds.')
        if re.search(r'\bpattern\b|\btriangle\b|\bpyramid\b|\bstar\b|\bdiamond\b', d):
            steps.append('Use nested loops: outer loop for rows, inner loop for columns.')
        if re.search(r'\bmatrix\b|\bgrid\b|\b2d\b|\btwo dimension\b', d):
            steps.append('Use nested loops — the outer loop iterates rows, the inner loop iterates columns.')
        if re.search(r'\btemperature\b|\bcelsius\b|\bfahrenheit\b', d):
            steps.append('Apply the conversion formula: F = C * 9/5 + 32 or C = (F - 32) * 5/9.')
        if re.search(r'\bcurrency\b|\bdollar\b', d) or re.search(r'format.*money', d):
            steps.append('Format with f-strings: f"${value:.2f}" for two decimal places.')
        if re.search(r'\bemail\b|\bvalid\b|\bvalidate\b', d) or re.search(r'check.*format', d):
            steps.append('Check for @ symbol, dot, and minimum length. Use "in" operator or regex.')

        step_text = '\n'.join(steps)
        has_logic = any(w in step_text for w in ['Initialize', 'Track', 'Add logic', 'Compute', 'The parameter', 'The parameters', 'Use'])
        if not has_logic:
            steps.append('Set up the function structure with the correct name and parameters.')
            steps.append('Implement the logic step by step inside the function body.')

    if steps:
        last = steps[-1].lower()
        if 'test' not in last and 'edge' not in last:
            steps.append('Test your solution with the provided example inputs.')
            steps.append('Check edge cases — empty inputs, single elements, negative numbers, etc.')

    return '\n'.join(f'{i+1}. {s}' for i, s in enumerate(steps))


# Collect all insertion points first, then insert in reverse order
insertions = []  # list of (line_index, text)

for block_lines, block_start in exercises:
    desc = extract_field(block_lines, 'description')
    if desc:
        desc_clean = desc.replace('\\n', ' ').replace('\\"', '"').replace('\\t', ' ')
        breakdown = generate_breakdown(desc_clean)

        # Find hint line within block
        hint_field = '"hint":'
        rel_hint_idx = None
        for j, bl in enumerate(block_lines):
            if hint_field in bl:
                rel_hint_idx = j
                break

        if rel_hint_idx is not None:
            hint_line_idx = block_start + rel_hint_idx
            esc_breakdown = breakdown.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n').replace('\t', '\\t')
            insert_text = f'            "breakdown": "{esc_breakdown}",\n'
            insertions.append((hint_line_idx, insert_text))

# Insert in reverse order so indexes don't shift
insertions.sort(key=lambda x: x[0], reverse=True)
for idx, text in insertions:
    lines.insert(idx, text)

with open(EXERCISES_FILE, 'w') as f:
    f.writelines(lines)

print(f'Done. Inserted {len(insertions)} breakdowns.')
