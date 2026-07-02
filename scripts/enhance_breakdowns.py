#!/usr/bin/env python3
"""Enhance exercise breakdowns with concept-specific syntax explanations."""
import re

EXERCISES_FILE = '/Users/moll/Desktop/python_app/exercises.ts'

# ── Concept library ──────────────────────────────────────────────────
# Each concept has: trigger pattern(s), label, and explanation template
# The explanation should explain syntax structure + order of operations
# {concept} and {syntax} are placeholders for label/example syntax

CONCEPTS = [
    {
        'name': 'lambda',
        'patterns': [r'\blambda\b'],
        'label': 'lambda function',
        'syntax': 'lambda parameters: expression',
        'explanation': (
            'A **lambda** is a small, anonymous function written as a single expression.\n'
            'Syntax: `lambda parameters: expression`\n\n'
            'Order of operations:\n'
            '1. `lambda` keyword — tells Python you are creating an anonymous function\n'
            '2. `parameters` — comma-separated input variables (like a regular function)\n'
            '3. `:` colon — separates parameters from the return expression\n'
            '4. `expression` — a single Python expression that is **implicitly returned**\n\n'
            'Unlike `def`, a lambda does not have a `return` statement — the expression result is automatically returned.'
        )
    },
    {
        'name': 'list comprehension',
        'patterns': [r'\[([^\]]*?)\s+for\s+'],
        'label': 'list comprehension',
        'syntax': '[expression for item in iterable if condition]',
        'explanation': (
            'A **list comprehension** builds a new list by applying an expression to each item.\n'
            'Syntax: `[expression for item in iterable if condition]`\n\n'
            'Order of operations:\n'
            '1. `for item in iterable` — iterate over each element\n'
            '2. `if condition` (optional) — filter; only items that pass are processed\n'
            '3. `expression` — the value to include in the output list, evaluated per item\n'
            '4. `[...]` — the entire expression produces a `list` object'
        )
    },
    {
        'name': 'generator expression',
        'patterns': [r'\(([^)]*?)\s+for\s+'],
        'label': 'generator expression',
        'syntax': '(expression for item in iterable if condition)',
        'explanation': (
            'A **generator expression** produces values lazily (one at a time) without storing the whole list in memory.\n'
            'Syntax: `(expression for item in iterable if condition)`\n\n'
            'Order of operations:\n'
            '1. `for item in iterable` — iterate over each element\n'
            '2. `if condition` (optional) — only items that pass continue\n'
            '3. `expression` — the value to yield, evaluated per item\n'
            '4. `(...)` — produces a generator **object**, not a list; values are computed on demand'
        )
    },
    {
        'name': 'dict comprehension',
        'patterns': [r'\{[^:]+?:\s*[^}]*?\s+for\s+'],
        'label': 'dictionary comprehension',
        'syntax': '{key_expression: value_expression for item in iterable}',
        'explanation': (
            'A **dictionary comprehension** builds a dict from an iterable.\n'
            'Syntax: `{key_expression: value_expression for item in iterable}`\n\n'
            'Order of operations:\n'
            '1. `for item in iterable` — iterate over each element\n'
            '2. `key_expression` — evaluated for each item to produce the key\n'
            '3. `value_expression` — evaluated to produce the matching value\n'
            '4. `{...}` — wraps key-value pairs into a `dict` object'
        )
    },
    {
        'name': 'map',
        'patterns': [r'\bmap\s*\('],
        'label': 'map() function',
        'syntax': 'map(function, iterable)',
        'explanation': (
            '**map()** applies a function to every item in an iterable and returns a lazy iterator.\n'
            'Syntax: `map(function, iterable)`\n\n'
            'Order of operations:\n'
            '1. Takes a **callable** (function or lambda) as the first argument\n'
            '2. Takes an **iterable** as the second argument\n'
            '3. Calls the function once for each item: `function(item)`\n'
            '4. Returns a `map` **object** (iterator); use `list()` to materialize or loop directly'
        )
    },
    {
        'name': 'filter',
        'patterns': [r'\bfilter\s*\('],
        'label': 'filter() function',
        'syntax': 'filter(function, iterable)',
        'explanation': (
            '**filter()** keeps only items where the function returns `True`.\n'
            'Syntax: `filter(function, iterable)`\n\n'
            'Order of operations:\n'
            '1. Takes a **callable** that returns a boolean (or truthy/falsy value)\n'
            '2. Calls it on each item in the iterable\n'
            '3. Keeps items where the result is truthy\n'
            '4. Returns a `filter` **object** (iterator); use `list()` to materialize'
        )
    },
    {
        'name': 'reduce',
        'patterns': [r'\breduce\s*\('],
        'label': 'reduce() function',
        'syntax': 'functools.reduce(function, iterable[, initial])',
        'explanation': (
            '**reduce()** cumulatively applies a function to pairs of items, reducing the iterable to a single value.\n'
            'Syntax: `functools.reduce(function, iterable, initial)`\n\n'
            'Order of operations:\n'
            '1. Import: `from functools import reduce`\n'
            '2. The function takes **two arguments**: the accumulated value and the next item\n'
            '3. Starts with the first two items (or `initial` if provided)\n'
            '4. Processes left to right, building up a single result'
        )
    },
    {
        'name': 'sorted',
        'patterns': [r'\bsorted\s*\('],
        'label': 'sorted() function',
        'syntax': 'sorted(iterable, key=None, reverse=False)',
        'explanation': (
            '**sorted()** returns a new sorted list from any iterable.\n'
            'Syntax: `sorted(iterable, key=None, reverse=False)`\n\n'
            'Order of operations:\n'
            '1. Takes an **iterable** (list, tuple, string, etc.)\n'
            '2. `key=` — optional callable that transforms each item before comparison (e.g., `key=len` sorts by length)\n'
            '3. `reverse=True` — sorts descending instead of ascending\n'
            '4. Returns a **new sorted list** (original is unchanged)'
        )
    },
    {
        'name': 'enumerate',
        'patterns': [r'\benumerate\s*\('],
        'label': 'enumerate() function',
        'syntax': 'enumerate(iterable, start=0)',
        'explanation': (
            '**enumerate()** adds a counter to an iterable, yielding `(index, value)` pairs.\n'
            'Syntax: `enumerate(iterable, start=0)`\n\n'
            'Order of operations:\n'
            '1. Iterates over the given iterable\n'
            '2. For each item, yields a **tuple**: `(index, item)`\n'
            '3. `start=` — optionally set the starting index (default 0)\n'
            '4. Commonly used in `for` loops: `for i, value in enumerate(items):`'
        )
    },
    {
        'name': 'zip',
        'patterns': [r'\bzip\s*\('],
        'label': 'zip() function',
        'syntax': 'zip(*iterables)',
        'explanation': (
            '**zip()** aggregates elements from multiple iterables into tuples.\n'
            'Syntax: `zip(iterable1, iterable2, ...)`\n\n'
            'Order of operations:\n'
            '1. Takes two or more iterables as arguments\n'
            '2. Pairs up the **first** items from each iterable, then the **second**, etc.\n'
            '3. Stops when the shortest iterable is exhausted\n'
            '4. Returns a `zip` **object** (iterator); use `list()` to materialize as a list of tuples'
        )
    },
    {
        'name': 'all',
        'patterns': [r'\ball\s*\('],
        'label': 'all() function',
        'syntax': 'all(iterable)',
        'explanation': (
            '**all()** returns `True` if **every** element in the iterable is truthy.\n'
            'Syntax: `all(iterable)`\n\n'
            'Order of operations:\n'
            '1. Takes a single **iterable** as argument\n'
            '2. Checks each element for truthiness (implicitly `bool(element)`)\n'
            '3. Returns `True` only if **all** elements are truthy\n'
            '4. Returns `False` as soon as it finds a falsy element (short-circuits)'
        )
    },
    {
        'name': 'any',
        'patterns': [r'\bany\s*\('],
        'label': 'any() function',
        'syntax': 'any(iterable)',
        'explanation': (
            '**any()** returns `True` if **at least one** element in the iterable is truthy.\n'
            'Syntax: `any(iterable)`\n\n'
            'Order of operations:\n'
            '1. Takes a single **iterable** as argument\n'
            '2. Checks each element for truthiness\n'
            '3. Returns `True` as soon as it finds a truthy element (short-circuits)\n'
            '4. Returns `False` if all elements are falsy'
        )
    },
    {
        'name': '*args',
        'patterns': [r'\*args\b'],
        'label': '*args parameter',
        'syntax': 'def function(*args):',
        'explanation': (
            '**`*args`** collects extra positional arguments into a **tuple**.\n'
            'Syntax: `def function(*args):`\n\n'
            'Order of operations:\n'
            '1. `*` — the unpacking operator, tells Python to collect remaining positional args\n'
            '2. `args` — the name of the tuple (convention, not required)\n'
            '3. Inside the function, `args` behaves as a **tuple** you can iterate over\n'
            '4. Can be combined with regular parameters: `def function(a, b, *args):`'
        )
    },
    {
        'name': '**kwargs',
        'patterns': [r'\*\*kwargs\b'],
        'label': '**kwargs parameter',
        'syntax': 'def function(**kwargs):',
        'explanation': (
            '**`**kwargs`** collects extra keyword arguments into a **dictionary**.\n'
            'Syntax: `def function(**kwargs):`\n\n'
            'Order of operations:\n'
            '1. `**` — the double-star unpacking operator\n'
            '2. `kwargs` — the dictionary (convention; any name works)\n'
            '3. Keys are the parameter **names** as strings, values are the **arguments**\n'
            '4. Iterate with `for key, value in kwargs.items():` to access all passed keyword args'
        )
    },
    {
        'name': '@property',
        'patterns': [r'@property'],
        'label': '@property decorator',
        'syntax': '@property\ndef name(self):\n    return self._name',
        'explanation': (
            '**`@property`** turns a method into a **read-only attribute**.\n'
            'Syntax:\n'
            '```\n@property\ndef name(self):\n    return self._name\n```\n\n'
            'Order of operations:\n'
            '1. Add `@property` above the method — makes it behave like an attribute\n'
            '2. Access with `obj.name` instead of `obj.name()` (no parentheses)\n'
            '3. Typically paired with `@name.setter` for write access and `@name.deleter` for delete\n'
            '4. The getter method must return the underlying (usually private) attribute'
        )
    },
    {
        'name': 'decorator',
        'patterns': [r'@(?!property\b)(?!staticmethod\b)(?!classmethod\b)[a-zA-Z]\w*'],
        'label': 'decorator pattern',
        'syntax': '@decorator\ndef function(): ...',
        'explanation': (
            'A **decorator** is a function that wraps another function to extend its behavior.\n'
            'Syntax: `@decorator_name` placed above a function definition\n\n'
            'Order of operations:\n'
            '1. Define a decorator function that takes a function as its parameter\n'
            '2. Inside, define a `wrapper()` function that adds behavior before/after the original\n'
            '3. The decorator returns the wrapper function\n'
            '4. Using `@decorator_name` is shorthand for `function = decorator_name(function)`'
        )
    },
    {
        'name': 'recursion',
        'patterns': [r'\bdef\s+(\w+).*:\s*\n\s+\1\('],
        'label': 'recursion',
        'syntax': 'def func(n):\n    if base_case:\n        return result\n    return func(n-1)',
        'explanation': (
            '**Recursion** is when a function calls itself to solve a smaller version of the problem.\n'
            'Structure:\n'
            '1. **Base case** — a condition where the function returns without calling itself (stops the recursion)\n'
            '2. **Recursive case** — the function calls itself with modified arguments\n'
            '3. Each call uses a separate stack frame with its own local variables\n'
            '4. Results propagate back up the call stack'
        )
    },
    {
        'name': 'class definition',
        'patterns': [r'\bclass\s+\w+'],
        'label': 'class definition',
        'syntax': 'class ClassName:\n    def __init__(self, ...):\n        ...',
        'explanation': (
            'A **class** is a blueprint for creating objects with attributes and methods.\n'
            'Syntax:\n'
            '```\nclass ClassName:\n    def __init__(self, param):\n        self.attribute = param\n    def method(self):\n        return self.attribute\n```\n\n'
            'Order of operations:\n'
            '1. `class ClassName:` — defines the class\n'
            '2. `__init__` — the **constructor** method, runs when you create an instance\n'
            '3. `self` — refers to the **instance** being created; first param of every instance method\n'
            '4. `self.attribute` — instance attributes, accessible by all methods\n'
            '5. Create an instance: `obj = ClassName(arg)`'
        )
    },
    {
        'name': 'inheritance',
        'patterns': [r'\bclass\s+\w+\s*\([^)]*\)'],
        'label': 'class inheritance',
        'syntax': 'class Child(Parent):\n    def __init__(self, ...):\n        super().__init__(...)',
        'explanation': (
            '**Inheritance** lets a child class reuse and extend a parent class.\n'
            'Syntax: `class ChildClass(ParentClass):`\n\n'
            'Order of operations:\n'
            '1. Parent class name goes in **parentheses** after the child class name\n'
            '2. The child inherits all attributes and methods from the parent\n'
            '3. `super().__init__(...)` — calls the parent constructor from the child\n'
            '4. The child can **override** methods by redefining them with the same name'
        )
    },
    {
        'name': 'super',
        'patterns': [r'\bsuper\s*\('],
        'label': 'super() function',
        'syntax': 'super().__init__(...)',
        'explanation': (
            '**super()** gives access to methods of a parent class from a child class.\n'
            'Syntax: `super().__init__(args)` or `super().parent_method(args)`\n\n'
            'Order of operations:\n'
            '1. Called **without** arguments inside a child class method (Python fills in `self` and the class)\n'
            '2. Returns a **proxy object** that delegates calls to the parent class\n'
            '3. Commonly used to call the parent `__init__` from the child\'s `__init__`\n'
            '4. Ensures the parent is properly initialized before the child adds its own attributes'
        )
    },
    {
        'name': '__init__',
        'patterns': [r'__init__\s*\('],
        'label': '__init__ constructor',
        'syntax': 'def __init__(self, ...):\n    self.attribute = value',
        'explanation': (
            '**`__init__`** is the constructor method that runs automatically when a new object is created.\n'
            'Syntax: `def __init__(self, param1, param2):`\n\n'
            'Order of operations:\n'
            '1. Called **automatically** when you do `obj = ClassName(args)`\n'
            '2. `self` — the first parameter, refers to the new instance\n'
            '3. `self.attribute = value` — store values on the instance\n'
            '4. Does **not** return anything (implicitly returns `None`)'
        )
    },
    {
        'name': 'try/except',
        'patterns': [r'\btry\s*:'],
        'label': 'try/except error handling',
        'syntax': 'try:\n    risky_code()\nexcept ErrorType:\n    handle_error()',
        'explanation': (
            '**`try/except`** catches runtime errors so the program does not crash.\n'
            'Syntax:\n'
            '```\ntry:\n    risky_code()\nexcept SomeError:\n    handle()\n```\n\n'
            'Order of operations:\n'
            '1. `try:` — Python attempts to run the indented code\n'
            '2. If no error occurs, `except` is **skipped**\n'
            '3. If an error matches the exception type, the `except` block runs\n'
            '4. After handling, execution continues after the `try/except` block (does not crash)'
        )
    },
    {
        'name': 'yield',
        'patterns': [r'\byield\b'],
        'label': 'yield / generator function',
        'syntax': 'def generator():\n    for item in items:\n        yield item',
        'explanation': (
            '**`yield`** produces a value from a generator function without exiting; the function can resume later.\n'
            'Syntax: `yield value` inside a function\n\n'
            'Order of operations:\n'
            '1. When called, the function returns a **generator object** (code does not run yet)\n'
            '2. Each time `next()` is called, execution runs until the next `yield`\n'
            '3. The yielded value is sent to the caller, and the function **pauses**\n'
            '4. Calling `next()` again **resumes** from where it paused, maintaining local state'
        )
    },
    {
        'name': 'with',
        'patterns': [r'\bwith\s+\w+\s*:'],
        'label': 'with statement / context manager',
        'syntax': 'with open(filename) as f:\n    data = f.read()',
        'explanation': (
            '**`with`** ensures proper setup and cleanup of resources (files, connections, locks).\n'
            'Syntax: `with expression as variable:`\n\n'
            'Order of operations:\n'
            '1. The `expression` returns a **context manager** with `__enter__` and `__exit__` methods\n'
            '2. `__enter__` runs, and its result is assigned to the `as variable`\n'
            '3. The indented block runs with the resource\n'
            '4. When the block ends (even by error), `__exit__` runs **automatically** (e.g., closes a file)'
        )
    },
    {
        'name': 'Counter',
        'patterns': [r'\bCounter\b'],
        'label': 'collections.Counter',
        'syntax': 'from collections import Counter\nCounter(iterable)',
        'explanation': (
            '**Counter** is a dict subclass that counts hashable objects.\n'
            'Syntax: `Counter(iterable)` or `Counter(**mapping)`\n\n'
            'Order of operations:\n'
            '1. Import: `from collections import Counter`\n'
            '2. Pass an iterable — counts each element automatically\n'
            '3. Elements become **keys**, their counts become **values**\n'
            '4. Useful methods: `.most_common(n)`, `+`/`-` for combining counts, `.elements()`'
        )
    },
    {
        'name': 'defaultdict',
        'patterns': [r'\bdefaultdict\b'],
        'label': 'collections.defaultdict',
        'syntax': 'from collections import defaultdict\nd = defaultdict(list)',
        'explanation': (
            '**defaultdict** creates a default value for missing keys automatically.\n'
            'Syntax: `defaultdict(factory_function)` where `factory_function` is `list`, `int`, `set`, etc.\n\n'
            'Order of operations:\n'
            '1. Import: `from collections import defaultdict`\n'
            '2. Pass a **factory function** — called with no args to create the default value\n'
            '3. When you access a missing key, the factory runs **automatically** and stores the result\n'
            '4. `defaultdict(list)` — missing keys start with an empty list (no need to check `if key in d`)'
        )
    },
    {
        'name': '@property.setter',
        'patterns': [r'@\w+\.setter'],
        'label': '@property.setter decorator',
        'syntax': '@property\ndef name(self):\n    return self._name\n@name.setter\ndef name(self, value):\n    self._name = value',
        'explanation': (
            '**`@property.setter`** allows controlled write access to a property.\n'
            'Syntax:\n'
            '```\n@name.setter\ndef name(self, value):\n    self._name = value\n```\n\n'
            'Order of operations:\n'
            '1. Must come after a `@property` getter with the **same method name**\n'
            '2. The setter method takes `self` and the new **value** as parameters\n'
            '3. Called when you assign: `obj.name = "new value"`\n'
            '4. Lets you add validation, type checking, or side effects before storing'
        )
    },
    {
        'name': '@property.deleter',
        'patterns': [r'@\w+\.deleter'],
        'label': '@property.deleter decorator',
        'syntax': '@name.deleter\ndef name(self):\n    del self._name',
        'explanation': (
            '**`@property.deleter`** defines what happens when you use `del obj.name`.\n'
            'Syntax:\n'
            '```\n@name.deleter\ndef name(self):\n    del self._name\n```\n\n'
            'Order of operations:\n'
            '1. Must follow a `@property` getter with the same method name\n'
            '2. Runs automatically when `del` is used: `del obj.name`\n'
            '3. Typically used to reset or clean up the underlying attribute\n'
            '4. Can include side effects like print/log messages'
        )
    },
    {
        'name': '@staticmethod',
        'patterns': [r'@staticmethod'],
        'label': '@staticmethod decorator',
        'syntax': '@staticmethod\ndef method(args):\n    ...',
        'explanation': (
            '**`@staticmethod`** defines a method that does **not** receive `self` or `cls`.\n'
            'Syntax:\n'
            '```\n@staticmethod\ndef method_name(args):\n    return result\n```\n\n'
            'Order of operations:\n'
            '1. Applied above a method inside a class\n'
            '2. No `self` or `cls` parameter — it is just a regular function namespaced in the class\n'
            '3. Call with `ClassName.method()` or `instance.method()`\n'
            '4. Used when the method does not need access to instance or class state'
        )
    },
    {
        'name': '@classmethod',
        'patterns': [r'@classmethod'],
        'label': '@classmethod decorator',
        'syntax': '@classmethod\ndef method(cls, args):\n    ...',
        'explanation': (
            '**`@classmethod`** receives the **class** instead of the instance.\n'
            'Syntax:\n'
            '```\n@classmethod\ndef method_name(cls, args):\n    return cls(...)\n```\n\n'
            'Order of operations:\n'
            '1. Applied above a method inside a class\n'
            '2. First parameter is `cls` (the class itself), not `self`\n'
            '3. Can be called on the class or any instance\n'
            '4. Commonly used as **alternative constructors** (`dict.fromkeys()`, `cls.new_instance()`)'
        )
    },
    {
        'name': '__str__',
        'patterns': [r'__str__\s*\('],
        'label': '__str__ method',
        'syntax': 'def __str__(self):\n    return "description"',
        'explanation': (
            '**`__str__`** defines a human-readable string representation for an object.\n'
            'Syntax: `def __str__(self):` returning a string\n\n'
            'Order of operations:\n'
            '1. Defined inside a class\n'
            '2. Must return a **string**\n'
            '3. Called automatically by `print(obj)` and `str(obj)`\n'
            '4. Should return something **readable** for end users (compare: `__repr__` is for developers)'
        )
    },
    {
        'name': '__repr__',
        'patterns': [r'__repr__\s*\('],
        'label': '__repr__ method',
        'syntax': 'def __repr__(self):\n    return "ClassName(args)"',
        'explanation': (
            '**`__repr__`** defines an unambiguous string representation, usually for debugging.\n'
            'Syntax: `def __repr__(self):` returning a string\n\n'
            'Order of operations:\n'
            '1. Defined inside a class\n'
            '2. Must return a **string**\n'
            '3. Called by `repr(obj)`, in the REPL, and as fallback for `print(obj)` if `__str__` is missing\n'
            '4. Convention: return something that could recreate the object, like `"ClassName(arg1, arg2)"`'
        )
    },
    {
        'name': 'set comprehension',
        'patterns': [r'\{\s*[^}:]+\s+for\s+'],
        'label': 'set comprehension',
        'syntax': '{expression for item in iterable if condition}',
        'explanation': (
            'A **set comprehension** builds a set (unique unordered elements) from an iterable.\n'
            'Syntax: `{expression for item in iterable if condition}`\n\n'
            'Order of operations:\n'
            '1. `for item in iterable` — iterate over each element\n'
            '2. `if condition` (optional) — filter items\n'
            '3. `expression` — evaluated per item and added to the set\n'
            '4. `{...}` — produces a `set` with **unique** elements (duplicates are dropped)'
        )
    },
    {
        'name': 'deque',
        'patterns': [r'\bdeque\b'],
        'label': 'collections.deque',
        'syntax': 'from collections import deque\nd = deque(iterable)',
        'explanation': (
            '**deque** (double-ended queue) is optimized for fast appends/pops from both ends.\n'
            'Syntax: `deque(iterable, maxlen=None)`\n\n'
            'Order of operations:\n'
            '1. Import: `from collections import deque`\n'
            '2. `d.append(x)` — add to the **right** end (O(1))\n'
            '3. `d.appendleft(x)` — add to the **left** end (O(1))\n'
            '4. `d.pop()` and `d.popleft()` — remove from either end (O(1))\n'
            '5. `maxlen=N` — optional, creates a **bounded** deque that discards items from the opposite end'
        )
    },
    {
        'name': 'functools.partial',
        'patterns': [r'\bpartial\b'],
        'label': 'functools.partial',
        'syntax': 'from functools import partial\nnew_func = partial(func, arg1, arg2)',
        'explanation': (
            '**partial()** creates a new function with some arguments already filled in (preset).\n'
            'Syntax: `partial(func, *args, **kwargs)`\n\n'
            'Order of operations:\n'
            '1. Import: `from functools import partial`\n'
            '2. Takes an existing function and **pre-fills** some arguments\n'
            '3. Returns a **new callable** with those arguments baked in\n'
            '4. When called, passes the pre-filled args followed by any additional args'
        )
    },
    {
        'name': 'namedtuple',
        'patterns': [r'\bnamedtuple\b'],
        'label': 'collections.namedtuple',
        'syntax': 'Point = namedtuple("Point", ["x", "y"])',
        'explanation': (
            '**namedtuple** creates tuple-like objects with named fields.\n'
            'Syntax: `ClassName = namedtuple("ClassName", ["field1", "field2"])`\n\n'
            'Order of operations:\n'
            '1. Import: `from collections import namedtuple`\n'
            '2. First arg: the **class name** (string)\n'
            '3. Second arg: field names (list of strings, or space-separated string)\n'
            '4. Access fields by **name** (`pt.x`) or by **index** (`pt[0]`) — immutable like a tuple'
        )
    },
]


def normalize_newlines(text):
    """Normalize 3+ newlines to 2 in JSON string content."""
    return re.sub(r'\n{3,}', r'\n\n', text)


def decode_solution(raw):
    """Decode JSON-escaped solution string."""
    return raw.replace('\\n', '\n').replace('\\"', '"').replace('\\\\', '\\')


def encode_solution(text):
    """Encode solution string for JSON."""
    return text.replace('\\', '\\\\').replace('\n', '\\n').replace('"', '\\"')


with open(EXERCISES_FILE, 'r') as f:
    content = f.read()

lines = content.split('\n')

# Find start of exercise array
start_idx = 0
for i, line in enumerate(lines):
    if 'Exercise[] = [' in line:
        start_idx = i + 1
        break

fixed = 0
matched_concepts = set()

for i in range(start_idx, len(lines)):
    line = lines[i]
    if '"solution":' not in line:
        continue

    m = re.search(r'"solution":\s*"(?:\\.|[^"\\])*"', line)
    if not m:
        continue

    full_match = m.group(0)
    inner_m = re.search(r'":\s*"(.*)"$', full_match)
    if not inner_m:
        continue

    sol_raw = inner_m.group(1)
    sol_text = decode_solution(sol_raw)

    # Find the corresponding breakdown on a nearby line
    breakdown_line_idx = -1
    bd_m = None
    for j in range(max(0, i - 5), min(len(lines), i + 8)):
        if '"breakdown":' in lines[j]:
            breakdown_line_idx = j
            bd_match = re.search(r'"breakdown":\s*"((?:\\.|[^"\\])*)"', lines[j])
            if bd_match:
                bd_m = bd_match.group(1)
            break

    if bd_m is None:
        continue  # skip exercises without breakdown

    bd_text = decode_solution(bd_m)
    bd_stripped = bd_text.strip()

    # Detect concepts
    found_concepts = []
    for concept in CONCEPTS:
        for pat in concept['patterns']:
            if re.search(pat, sol_text):
                found_concepts.append(concept)
                break

    if not found_concepts:
        continue

    # Build concept explanation section
    concept_parts = []
    first_label = None
    for c in found_concepts:
        if first_label is None:
            first_label = c['label']
        concept_parts.append(f"**What is {c['label']}?**\n{c['syntax']}\n\n{c['explanation']}")
        matched_concepts.add(c['name'])

    concept_block = '\n\n'.join(concept_parts)

    # Prepend concept explanation to the breakdown
    new_bd = concept_block + '\n\n' + bd_stripped
    new_bd_normalized = normalize_newlines(new_bd)

    # Only update if changed
    if new_bd_normalized == bd_stripped:
        continue

    # Escape and write back
    escaped_bd = encode_solution(new_bd_normalized)
    indent = lines[breakdown_line_idx][:len(lines[breakdown_line_idx]) - len(lines[breakdown_line_idx].lstrip())]
    lines[breakdown_line_idx] = f'{indent}"breakdown": "{escaped_bd}",'
    fixed += 1

with open(EXERCISES_FILE, 'w') as f:
    f.write('\n'.join(lines))

print(f'Updated breakdowns: {fixed}')
print(f'Concepts matched: {sorted(matched_concepts)}')
print(f'Concepts not triggered (0 exercises): {set(c["name"] for c in CONCEPTS) - matched_concepts}')
