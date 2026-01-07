import React, { useState, useEffect, useCallback, useRef, useMemo } from 'react';
import {
    Settings,
    Book,
    Lightbulb,
    Bot,
    CheckCircle,
    XCircle,
    RotateCcw,
    Play,
    Plus,
    Minus,
    Pencil,
    FileCode,
    AlertTriangle,
    Key,
    ExternalLink,
    Loader2,
    Trash2,
    Zap,
    Copy,
    Check,
    MousePointer2,
    ArrowUpRight,
    RefreshCw,
    Info,
    ChevronDown,
    ChevronUp
} from 'lucide-react';
import CodeMirror from '@uiw/react-codemirror';
import { python } from '@codemirror/lang-python';
import { indentUnit } from '@codemirror/language';
import { autocompletion, snippetCompletion, CompletionContext } from '@codemirror/autocomplete';
import { EXERCISES } from './exercises';
import { Exercise, Stats } from './types';
import { getAiHint } from './services/geminiService';
import { customPythonTheme } from './editorTheme';

// Fixed: Removed local AIStudio interface definition as it conflicts with environment-provided types.

declare global {
    interface Window {
        __PYODIDE_INSTANCE__: any;
        __PYODIDE_INIT_LOCK__: boolean;
        loadPyodide: any;
        // Fixed: Removed aistudio declaration to resolve redeclaration conflict with identical modifiers/types.
    }
}

interface ProjectFile {
    name: string;
    content: string;
}

// CHEAT TAB - Python Examples Only
const CHEAT_CONTENT = `# Python Cheat Sheet - Templates & Examples
import collections
from collections import Counter
import datetime
from functools import reduce
import math
import os
from pathlib import Path
import random
import string
import re
import time
from urllib.parse import parse_qs

# Dictionary Example
def main(dic):
    return len(dic)
    
dic = {"apple": 1, "orange": 33}
print(main(dic))

# List Comprehension
squares = [x**2 for x in range(10)]
print(squares)

# Dictionary with target
def main(dic, target):
    return dic.get(target)

dic = {"apple": 1, "orange": 33, "mango": 5}
target = "orange"
main(dic, target)

# Two dictionaries
def main(dic1, dic2):
    return {**dic1, **dic2}

dic1 = {"apple": 1, "orange": 33}
dic2 = {"storm": 11, "sky": 36}
main(dic1, dic2)

# List of dictionaries
lst_dic = [
    {"name": "Jon", "age": 67},
    {"name": "mike", "age": 55},
    {"name": "dilly", "age": 23}
]

# Nested list
nested_lst = [[1,2,3], [4,5,6], [7,8,9]]

# List of tuples
lst_tuples = [(55,7), (2,4), (27,23)]

# Keyword arguments
def main(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

main(a=1, b=2, c="hot", d="cold")

# Helper function pattern
def helper(x):
    return x * 2

def main():
    result = helper(5)
    return result

main()
`;

// GLOSSARY TAB - Complete Python Glossary
const GLOSSARY_CONTENT = `#glossary python 
"""
PYTHON GLOSSARY - COMPREHENSIVE REFERENCE
==========================================

A
---

**all()** - all(iterable)
    Returns True if all elements in the iterable are truthy, otherwise False.
    Example: all([True, True, False]) returns False

**any()** - any(iterable)
    Returns True if any element in the iterable is truthy, otherwise False.
    Example: any([False, False, True]) returns True

**Argument**
    A value passed to a function or method when it is called. An argument can be an expression, 
    a value, or even another function call. Arguments are assigned to parameters when the function executes.

**Assert** - assert expression, message
    A debugging aid that tests a condition. If the condition is False, it raises an AssertionError 
    with an optional message. Used to catch programming errors early.

**Attribute**
    A value associated with an object. Attributes are accessed using dot notation (object.attribute).
    Can be data attributes (variables) or method attributes (functions).

B
---

**Built-in Function**
    Functions that are always available in Python without needing to import them.
    Examples: print(), len(), range(), type(), str(), int(), float(), list(), dict(), set(), tuple()

**Built-in Scope (B in LEGB)**
    The outermost scope containing Python's built-in names (like print, len, etc.).
    Always checked last in the LEGB lookup order.

C
---

**Class** - Class_name: attribute
    A blueprint for creating objects. Defines attributes and methods that all instances of the class will have.
    Example: class Person: pass

**Class Object** - obj = ClassName()
    An instance of a class. Created by calling the class like a function.
    Example: person = Person() creates a Person object

**Closure**
    A function that has access to variables from its enclosing (outer) scope even after the outer 
    function has finished executing. Closures "remember" the environment in which they were created.

**Comprehension**
    A concise way to create collections (lists, dictionaries, sets) using a single expression.
    1. List comprehension: [expression for item in iterable if condition]
    2. Dictionary comprehension: {key: value for item in iterable if condition}
    3. Set comprehension: {value for item in iterable if condition}
    4. Generator expression: (expression for variable in iterable)

**Constant**
    A variable that is intended not to be changed after its initial assignment. 
    In Python, constants are typically written in UPPER_CASE by convention (though not enforced).

**Constructor**
    A special method (__init__) that is automatically called when an object is created.
    Used to initialize the object's attributes.

D
---

**Decorator**
    A function that modifies or extends the behavior of another function without permanently modifying it.
    Applied using the @decorator_name syntax above a function definition.

**Dictionary (dict)**
    An unordered, mutable collection of key-value pairs. Keys must be hashable (immutable).
    Example: {"name": "Alice", "age": 30}

**Docstring**
    A string literal that appears as the first statement in a function, class, or module.
    Used to document code and accessible via the __doc__ attribute.

E
---

**Enclosing Scope (E in LEGB)**
    The scope of an outer function that contains a nested function. Variables from the enclosing 
    scope are accessible to the inner function, forming closures.

**Enclosing Variable**
    A variable defined in an outer (enclosing) function that is accessible to an inner function.
    Part of how closures work in Python.

**Exception**
    An error that occurs during program execution. Can be caught and handled using try/except blocks.
    Examples: ValueError, TypeError, IndexError, KeyError, AttributeError

**Expression**
    A piece of code that evaluates to a value. Can be a simple value, a variable, or a combination 
    of operators and values. Examples: 2 + 2, name = "Sam", len([1, 2, 3])

F
---

**Filter** - filter(function, iterable)
    Returns an iterator containing only the elements from the iterable for which the function 
    returns True. Example: filter(lambda x: x > 0, [-1, 0, 1, 2]) returns [1, 2]

**Function**
    A block of code that performs a specific task. Defined using the def keyword.
    Can accept parameters and return values. Syntax: function_name(arguments)

**Function Call**
    The act of executing a function by using its name followed by parentheses.
    Example: print("Hello") calls the print function

G
---

**Generator**
    A special type of iterator that generates values on-the-fly using the yield keyword.
    More memory-efficient than lists for large sequences. Created using generator functions or expressions.

**Generator Expression**
    A compact way to create a generator. Syntax: (expression for variable in iterable)
    Similar to list comprehension but uses parentheses and returns a generator object.

**Global Variable**
    A variable defined outside of any function, accessible from anywhere in the program.
    To modify a global variable inside a function, use the global keyword.

**Global Scope (G in LEGB)**
    The module-level scope where global variables are defined. Checked third in the LEGB lookup order.

I
---

**Immutable**
    An object whose value cannot be changed after it is created. Examples: int, float, str, tuple, frozenset.
    Operations on immutable objects create new objects rather than modifying existing ones.

**Import**
    The process of bringing code from one module into another. Syntax: import module_name
    or from module_name import function_name

**Inheritance**
    A mechanism where a class (child/subclass) can inherit attributes and methods from another class (parent/superclass).
    Promotes code reuse and establishes relationships between classes.

**Instance**
    An individual object created from a class. Each instance has its own set of attributes.

**Instance Method**
    A method that operates on an instance of a class. Takes self as the first parameter.

**Instance Variable**
    A variable that belongs to a specific instance of a class. Each instance has its own copy.

**isinstance()** - isinstance(expression, classinfo)
    Returns True if the object is an instance of the specified class or a subclass thereof.
    Example: isinstance(5, int) returns True

**Iterable**
    An object that can be iterated over (used in a for loop). Must implement the __iter__() method.
    Examples: lists, tuples, strings, dictionaries, sets, file objects

**Iteration**
    The process of repeating a set of instructions for a specified number of times or until a 
    certain condition is met. Often done using for loops or while loops.

**Iterator**
    An object that allows you to iterate over a sequence, accessing its elements one at a time 
    without loading the entire collection into memory. Implements __iter__() and __next__() methods.
    More memory-efficient than loading entire sequences.

K
---

**Key (in dictionaries)**
    The first element in a key-value pair in a dictionary. Keys must be hashable (immutable).
    Used to access the corresponding value. Example: dict["key"] returns the value

**Keyword Argument**
    An argument passed to a function using the parameter name. Allows arguments to be passed 
    in any order. Example: function(name="Alice", age=30)

**kwargs** - **kwargs
    A special parameter that collects all keyword arguments into a dictionary.
    The double asterisk (**) unpacks keyword arguments.

L
---

**Lambda**
    An anonymous function defined using the lambda keyword. Syntax: lambda argument: expression
    Used for simple, one-line functions. Example: lambda x: x * 2

**List**
    An ordered, mutable collection of items. Items can be of any type and can be duplicated.
    Example: [1, 2, 3, "hello", True]

**List Comprehension**
    A concise way to create lists. Syntax: [expression for item in iterable if condition]
    More readable and often faster than equivalent for loops.

**Local Scope (L in LEGB)**
    The innermost scope, typically inside a function. Variables defined here are local to that function.
    Checked first in the LEGB lookup order.

**Local Variable**
    A variable defined within a function or block of code, only accessible within that scope.
    Takes precedence over variables with the same name in outer scopes.

M
---

**Map** - map(function, iterable)
    Returns an iterator that applies the function to every item in the iterable.
    Example: map(str.upper, ["hello", "world"]) returns ["HELLO", "WORLD"]

**Max** - max(expression, [default])
    Returns the largest item in an iterable or the largest of two or more arguments.
    Example: max([1, 5, 3]) returns 5

**Method**
    A function that belongs to an object. Called using dot notation: object.method(arguments)
    Methods can be instance methods, class methods, or static methods.

**Min** - min(expression, [default])
    Returns the smallest item in an iterable or the smallest of two or more arguments.
    Example: min([1, 5, 3]) returns 1

**Module**
    A file containing Python code (functions, classes, variables). Can be imported into other programs.
    Example: math, os, datetime, random

**Mutable**
    An object whose value can be changed after it is created. Examples: list, dict, set.
    Mutable objects can be modified in-place.

N
---

**Next** - next(iterable, [default])
    Returns the next item from an iterator. Raises StopIteration when exhausted, 
    or returns default if provided. Example: next(iter([1, 2, 3])) returns 1

**None**
    A special constant representing the absence of a value. The only value of the NoneType.
    Used to indicate that a variable has no value assigned.

O
---

**Object**
    An instance of a class. Everything in Python is an object, including numbers, strings, functions, and classes.
    Objects are self-contained units that combine data (attributes) and behavior (methods).
    Example: class Person(name, age): pass creates a Person class that can be instantiated into objects

**Operator**
    A symbol that performs an operation on one or more operands. Examples: +, -, *, /, ==, !=, <, >, and, or, not

P
---

**Parameter**
    An input variable defined in a function's definition. When the function is called, arguments 
    are passed and assigned to these parameters. Example: def add(a, b): where a and b are parameters

**Perfect Number**
    A positive integer that is equal to the sum of its proper divisors (excluding itself).
    Example: 6 = 1 + 2 + 3, so 6 is a perfect number

**Pop** - pop([index])
    Removes and returns an item from a list at the specified index (default is the last item).
    Example: [1, 2, 3].pop() returns 3 and the list becomes [1, 2]

**Property**
    A special kind of method that is accessed like an attribute. Defined using the @property decorator.
    Allows controlled access to instance variables.

R
---

**Range**
    A built-in function that generates a sequence of numbers. Syntax: range(start, stop, step)
    Returns an immutable sequence type. Example: range(5) generates 0, 1, 2, 3, 4

**Return**
    A statement that exits a function and optionally returns a value to the caller.
    If no value is specified, returns None.

S
---

**Scope**
    A region of code where variables are defined and accessible. Python uses LEGB (Local, Enclosing, Global, Built-in) 
    to determine which variable to use. Scopes help prevent naming conflicts and manage variable lifetimes.

**Set**
    An unordered, mutable collection of unique elements. No duplicates allowed.
    Example: {1, 2, 3, 4}

**Set Comprehension**
    A concise way to create sets. Syntax: {value for item in iterable if condition}
    Similar to list comprehension but creates a set instead.

**Sorted** - sorted(iterable, key=None, reverse=False)
    Returns a new sorted list from the items in the iterable. Does not modify the original.
    key parameter specifies a function to extract a comparison key. reverse=True sorts in descending order.
    Example: sorted([3, 1, 2]) returns [1, 2, 3]

**Statement**
    A line of code that performs an action. Unlike expressions, statements don't necessarily return a value.
    Examples: if, for, while, def, class, import, return, pass

**String (str)**
    An immutable sequence of characters. Can be created using single, double, or triple quotes.
    Example: "Hello, World!" or 'Python' or """Multi-line string"""

**Subclass**
    A class that inherits from another class (superclass). Also called a child class or derived class.

**Superclass**
    A class that is inherited by another class. Also called a parent class or base class.

**Syntax**
    The set of rules that define how Python code must be written. Syntax errors occur when code 
    doesn't follow these rules and prevent the program from running.

T
---

**Tuple**
    An ordered, immutable collection of objects. Used to store groups of related data.
    Created using parentheses: (1, 2, 3) or just commas: 1, 2, 3
    Example: coordinates = (10, 20)

**Type**
    The category or class of a value. Determines what operations can be performed on it.
    Examples: int, float, str, list, dict, bool, NoneType

**Type Hinting**
    A feature that allows you to indicate the expected types of function parameters and return values.
    Example: def add(a: int, b: int) -> int:

V
---

**Variable**
    A container that holds a value. Created by assigning a value to a name using the = operator.
    Variables can hold different types of data: numbers, strings, lists, objects, etc.
    Example: name = "Alice" or count = 42

**Variable Scope**
    The region of code where a variable is accessible. Determined by where the variable is defined.
    See: Local Scope, Global Scope, Enclosing Scope

Z
---

**Zip** - zip([iterable1], [iterable2], [iterable3], ...)
    Combines multiple iterables element-wise into tuples. Returns an iterator of tuples.
    Example: zip([1, 2], ['a', 'b']) returns [(1, 'a'), (2, 'b')]
    Stops when the shortest iterable is exhausted.

LEGB RULE - SCOPE RESOLUTION ORDER
==================================
Python finds names by searching in this order:

    • L = Local (inner function) - Variables defined inside the current function
    • E = Enclosing (closures) - Variables from outer functions that contain the current function
    • G = Global (module) - Variables defined at the module level
    • B = Builtins - Python's built-in names (print, len, etc.)

This order ensures that local variables take precedence over global ones, and allows closures 
to access variables from their enclosing functions.

"""
`;

// REGEX TAB - Regular Expressions Reference
const REGEX_CONTENT = `#regular expressions
"""
**Character Classes**

* \`a-z\`: Matches any lowercase letter
* \`A-Z\`: Matches any uppercase letter
* \`0-9\`: Matches any digit
* \`[a-zA-Z]\`: Matches any letter (both lowercase and uppercase)
* \`[0-9]\`: Matches any digit
* \`\\d\`: Matches any digit
* \`\\w\`: Matches any word character (alphanumeric plus underscore)
* \`\\s\`: Matches any whitespace character

**Special Characters**

* \`.\`: Matches any single character
* \`^\`: Matches the start of a string
* \`$\`: Matches the end of a string
* \`*\`: Matches 0 or more of the preceding character
* \`+\`: Matches 1 or more of the preceding character
* \`?\`: Matches 0 or 1 of the preceding character
* \`{n, m}\`: Matches between n and m of the preceding character
* \`{n,}\`: Matches at least n of the preceding character
* \`{, m}\`: Matches at most m of the preceding character

**Quantifiers**

* \`*\`: Matches 0 or more of the preceding character
* \`+\`: Matches 1 or more of the preceding character
* \`?\`: Matches 0 or 1 of the preceding character
* \`{n, m}\`: Matches between n and m of the preceding character
* \`{n,}\`: Matches at least n of the preceding character
* \`{, m}\`: Matches at most m of the preceding character

**Groups and Capturing**

* \`(\` and \`)\`: Used to group parts of a pattern together
* \`\\1\`, \`\\2\`, etc.: Refer to the capturing groups in the pattern

**Escaping**

* \`\\\`: Escapes special characters
* \`\\b\`: Matches a word boundary

Here are some examples of regex patterns:

* \`\\d{4}-\\d{2}-\\d{2}\`: Matches a date in the format DD-MM-YYYY
* \`[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}\`: Matches an email address
* \`\\d{3}-\\d{3}-\\d{4}\`: Matches a credit card number
* \`[a-zA-Z]+ [a-zA-Z]+, [A-Z]{2}\`: Matches a full name
* \`\\d{1,3}\\.\\d{3,5}/\\d{4}\`: Matches a phone number

These are just a few examples of the many patterns you can use in regex. The specific patterns you use will depend on the problem you're trying to solve.

Do you have a specific problem you'd like me to help you solve using regex?
"""
`;


const pythonSnippets = (context: CompletionContext) => {
    const word = context.matchBefore(/\w*/);
    if (!word || (word.from === word.to && !context.explicit)) return null;

    return {
        from: word.from,
        options: [
            snippetCompletion("print(${0})", { label: "print", detail: "built-in function", type: "function" }),
            snippetCompletion("def ${name}(${args}):\n    ${0}", { label: "def", detail: "define function", type: "keyword" }),
        ]
    };
};

const App: React.FC = () => {
    const [exercise, setExercise] = useState<Exercise>(EXERCISES[0]);
    const [files, setFiles] = useState<ProjectFile[]>([{ name: 'main.py', content: EXERCISES[0].initialCode }]);
    const [activeFileIndex, setActiveFileIndex] = useState(0);
    const [isEditingFileName, setIsEditingFileName] = useState(false);
    const [newName, setNewName] = useState('');

    const [output, setOutput] = useState('Run code to see output...');
    const [isRunning, setIsRunning] = useState(false);
    const [stats, setStats] = useState<Stats>({ shots: 0, success: 0, failed: 0 });
    const [pyodide, setPyodide] = useState<any>(null);
    const [bootStage, setBootStage] = useState<'loading' | 'ready' | 'launched'>('loading');
    const [bootLog, setBootLog] = useState<string>('Handshaking...');
    const [loadTime, setLoadTime] = useState<number>(0);
    const [isInFrame, setIsInFrame] = useState(false);
    const [showModal, setShowModal] = useState<'none' | 'instructions' | 'hint' | 'solution' | 'settings' | 'restart_confirm' | 'problem_full'>('none');
    const [modalTab, setModalTab] = useState<'how' | 'cheat' | 'glossary' | 'regex'>('how');
    const [aiHintText, setAiHintText] = useState<string>('');
    const [copyFeedback, setCopyFeedback] = useState(false);
    const [apiKey, setApiKey] = useState<string>(() => {
        return localStorage.getItem('gemini_api_key') || '';
    });
    const [isProblemExpanded, setIsProblemExpanded] = useState(false);

    const outputRef = useRef<HTMLDivElement>(null);
    const headerRef = useRef<HTMLDivElement>(null);
    const problemPanelRef = useRef<HTMLDivElement>(null);
    const problemDescriptionRef = useRef<HTMLDivElement>(null);
    const [headerHeight, setHeaderHeight] = useState(280);
    const [problemPanelHeight, setProblemPanelHeight] = useState(200);
    const [problemDescriptionHeight, setProblemDescriptionHeight] = useState<number | 'auto'>('auto');

    useEffect(() => {
        setIsInFrame(window.self !== window.top);
        const savedStats = localStorage.getItem('python_mastery_stats');
        if (savedStats) setStats(JSON.parse(savedStats));

        const bootEl = document.getElementById('boot');
        if (bootEl) {
            setTimeout(() => { bootEl.style.opacity = '0'; }, 500);
            setTimeout(() => { bootEl.style.display = 'none'; }, 1000);
        }
    }, []);

    useEffect(() => {
        const updateHeaderHeight = () => {
            if (headerRef.current) {
                setHeaderHeight(headerRef.current.offsetHeight);
            }
        };
        const updateProblemPanelHeight = () => {
            if (problemPanelRef.current) {
                setProblemPanelHeight(problemPanelRef.current.offsetHeight);
            }
        };
        updateHeaderHeight();
        updateProblemPanelHeight();
        // Update height when exercise changes
        const timeoutId = setTimeout(() => {
            updateHeaderHeight();
            updateProblemPanelHeight();
        }, 100);
        window.addEventListener('resize', () => {
            updateHeaderHeight();
            updateProblemPanelHeight();
        });
        
        // Use ResizeObserver to watch for content changes
        let headerObserver: ResizeObserver | null = null;
        let problemObserver: ResizeObserver | null = null;
        if (headerRef.current && typeof ResizeObserver !== 'undefined') {
            headerObserver = new ResizeObserver(() => {
                updateHeaderHeight();
            });
            headerObserver.observe(headerRef.current);
        }
        if (problemPanelRef.current && typeof ResizeObserver !== 'undefined') {
            problemObserver = new ResizeObserver(() => {
                updateProblemPanelHeight();
            });
            problemObserver.observe(problemPanelRef.current);
        }
        
        return () => {
            clearTimeout(timeoutId);
            window.removeEventListener('resize', updateHeaderHeight);
            if (headerObserver) {
                headerObserver.disconnect();
            }
            if (problemObserver) {
                problemObserver.disconnect();
            }
        };
    }, [exercise]);

    // Removed problematic useEffect - inline styles now properly set in JSX to allow scrolling
    // maxHeight: '300px' and overflowY: 'auto' are set directly in the style prop

    useEffect(() => {
        localStorage.setItem('python_mastery_stats', JSON.stringify(stats));
    }, [stats]);

    useEffect(() => {
        let interval: any;
        if (bootStage === 'loading') {
            interval = setInterval(() => {
                setLoadTime(prev => {
                    const next = prev + 1;
                    if (next === 3) setBootLog('Network verified...');
                    if (next === 8) setBootLog('Streaming binaries...');
                    if (next === 15) setBootLog('Extracting modules...');
                    if (next === 25) setBootLog('Finalizing compile...');
                    return next;
                });
            }, 1000);
        }
        return () => clearInterval(interval);
    }, [bootStage]);

    useEffect(() => {
        async function initPyodide() {
            if (window.__PYODIDE_INSTANCE__) {
                setPyodide(window.__PYODIDE_INSTANCE__);
                setBootStage('ready');
                return;
            }

            if (window.__PYODIDE_INIT_LOCK__) return;
            window.__PYODIDE_INIT_LOCK__ = true;

            try {
                setBootLog('Fetching interpreter...');

                let retries = 0;
                while (typeof window.loadPyodide === 'undefined' && retries < 120) {
                    await new Promise(r => setTimeout(r, 500));
                    retries++;
                }

                if (typeof window.loadPyodide === 'undefined') {
                    throw new Error("WASM source unavailable. Please refresh.");
                }

                const py = await window.loadPyodide({
                    indexURL: "https://cdn.jsdelivr.net/pyodide/v0.26.1/full/"
                });

                await py.loadPackage([]);
                window.__PYODIDE_INSTANCE__ = py;
                setPyodide(py);
                setBootStage('ready');
            } catch (err: any) {
                console.error("Pyodide error:", err);
                setBootLog(`Error: ${err.message || 'Engine Fail'}`);
                window.__PYODIDE_INIT_LOCK__ = false;
            }
        }
        initPyodide();
    }, []);

    const handleLaunch = () => {
        setBootStage('launched');
    };

    const forceResetCache = async () => {
        if (window.localStorage) window.localStorage.clear();
        if (window.caches) {
            const keys = await window.caches.keys();
            await Promise.all(keys.map(k => window.caches.delete(k)));
        }
        window.location.reload();
    };

    const handleCopyLink = () => {
        const url = window.location.href;
        navigator.clipboard.writeText(url);
        setCopyFeedback(true);
        setTimeout(() => setCopyFeedback(false), 2000);
    };

    const setProblemById = (id: number) => {
        const targetId = Math.min(Math.max(1, id), 2000);
        const ex = EXERCISES[targetId - 1];
        setExercise(ex);
        setFiles([{ name: 'main.py', content: ex.initialCode }]);
        setActiveFileIndex(0);
        setOutput('Run code to see output...');
        setAiHintText('');
    };

    const loadRandomExercise = useCallback(() => {
        const randomIndex = Math.floor(Math.random() * EXERCISES.length);
        setProblemById(randomIndex + 1);
    }, []);

    const handleRestartProgress = () => {
        setStats({ shots: 0, success: 0, failed: 0 });
        loadRandomExercise();
        setShowModal('none');
    };

    const runCode = async () => {
        if (!pyodide || isRunning) return;
        setIsRunning(true);
        setOutput('Executing...');
        try {
            // Write all files to the virtual filesystem
            files.forEach(file => {
                pyodide.FS.writeFile(file.name, file.content);
            });

            // Clear user-defined modules from sys.modules to ensure fresh imports
            const userModules = files.map(f => f.name.replace('.py', ''));
            const clearModulesCode = `
import sys
import importlib
import io

# Ensure current directory is in path (crucial for imports)
if '.' not in sys.path:
    sys.path.insert(0, '.')

for mod in ${JSON.stringify(userModules)}:
    if mod in sys.modules:
        del sys.modules[mod]

importlib.invalidate_caches()
sys.stdout = io.StringIO()
`;
            pyodide.runPython(clearModulesCode);

            const activeFile = files[activeFileIndex];
            // CRITICAL FIX: Use exec with filename context so imports work
            const code = `exec(compile(${JSON.stringify(activeFile.content)}, ${JSON.stringify(activeFile.name)}, 'exec'))`;
            await pyodide.runPythonAsync(code);
            const stdout = pyodide.runPython("sys.stdout.getvalue()");
            setOutput(stdout || 'Success (No output).');
        } catch (err: any) {
            setOutput(err.message);
        } finally {
            setIsRunning(false);
        }
    };

    const addFile = () => {
        const name = `file_${files.length + 1}.py`;
        setFiles([...files, { name, content: '# New module\n' }]);
        setActiveFileIndex(files.length);
    };

    const removeFile = () => {
        if (files.length <= 1) return;
        const newFiles = files.filter((_, i) => i !== activeFileIndex);
        setFiles(newFiles);
        setActiveFileIndex(Math.max(0, activeFileIndex - 1));
    };

    const startRenaming = () => {
        setNewName(files[activeFileIndex].name);
        setIsEditingFileName(true);
    };

    const finishRenaming = () => {
        if (!newName.trim()) return setIsEditingFileName(false);
        const updatedFiles = [...files];
        updatedFiles[activeFileIndex].name = newName.endsWith('.py') ? newName : `${newName}.py`;
        setFiles(updatedFiles);
        setIsEditingFileName(false);
    };

    const updateActiveContent = (val: string) => {
        const updatedFiles = [...files];
        updatedFiles[activeFileIndex].content = val;
        setFiles(updatedFiles);
    };

    const handleMarkSuccess = () => {
        setStats(prev => ({ ...prev, shots: prev.shots + 1, success: prev.success + 1 }));
        loadRandomExercise();
    };

    const handleMarkFailed = () => {
        setStats(prev => ({ ...prev, shots: prev.shots + 1, failed: prev.failed + 1 }));
        loadRandomExercise();
    };

    const handleAiHint = async () => {
        if (!apiKey || apiKey.trim() === '') {
            setShowModal('settings');
            return;
        }
        setShowModal('hint');
        if (!aiHintText) {
            setAiHintText('Asking Gemini...');
            const hint = await getAiHint(exercise.description, files[activeFileIndex].content, apiKey);
            setAiHintText(hint);
        }
    };

    const rate = stats.shots > 0 ? ((stats.success / stats.shots) * 100).toFixed(2) : '0.00';

    const editorExtensions = useMemo(() => [
        python(),
        indentUnit.of("    "),
        autocompletion({ override: [pythonSnippets] }),
        ...customPythonTheme
    ], []);

    if (bootStage !== 'launched') {
        return (
            <div className="fixed inset-0 z-[100] bg-[#040b16] flex flex-col items-center justify-start pt-16 p-8 text-center text-white overflow-y-auto animate-in fade-in duration-500">
                <div className="relative mb-8 flex-shrink-0">
                    <div className="absolute inset-0 bg-[#3b82f6]/20 blur-3xl rounded-full animate-pulse"></div>
                    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" className={`w-20 h-20 relative z-10 ${bootStage === 'loading' ? 'animate-bounce' : 'scale-110'}`} alt="Python" />
                </div>

                {bootStage === 'loading' ? (
                    <>
                        <Loader2 className="animate-spin text-[#3b82f6] mb-4" size={40} />
                        <h1 className="text-2xl font-black tracking-tighter mb-2 italic uppercase">Starting Engine...</h1>
                        <p className="text-[#3b82f6] text-[10px] font-mono tracking-widest mb-6 uppercase animate-pulse">{bootLog}</p>
                        <p className="text-gray-400 text-[11px] max-w-xs leading-relaxed mb-8">Caching Standard Library (20MB) for offline use.</p>
                        <div className="flex flex-col gap-3 w-full max-w-xs animate-in slide-in-from-bottom-4">
                            <button onClick={() => window.location.reload()} className="w-full bg-[#1d2d44] text-white py-4 rounded-2xl font-black text-[10px] uppercase border border-white/5 flex items-center justify-center gap-2"><RefreshCw size={14} /> Refresh</button>
                            <button onClick={forceResetCache} className="w-full bg-red-500/10 border border-red-500/20 text-red-500 py-4 rounded-2xl font-black text-[10px] uppercase flex items-center justify-center gap-2"><Trash2 size={14} /> Wipe Cache</button>
                        </div>
                    </>
                ) : (
                    <div className="animate-in fade-in zoom-in duration-500 flex flex-col items-center flex-shrink-0">
                        <h1 className="text-3xl font-black tracking-tighter mb-2 text-[#3b82f6]">LOCAL ENGINE READY</h1>
                        <p className="text-gray-400 text-xs mb-6 uppercase tracking-widest font-bold">Standard Library Loaded</p>
                        <button onClick={handleLaunch} className="mt-4 bg-[#3b82f6] text-white px-10 py-4 rounded-2xl font-black text-lg shadow-[0_0_40px_rgba(59,130,246,0.3)] active:scale-95 transition-all flex items-center gap-2"><Zap size={20} fill="currentColor" /> ENTER EDITOR</button>
                    </div>
                )}

                {isInFrame && (
                    <div className="mt-10 w-full max-w-sm">
                        <div className="bg-[#112240] border-2 border-dashed border-[#3b82f6]/30 p-6 rounded-[2rem] text-left shadow-2xl">
                            <h3 className="text-[#3b82f6] font-black text-xs uppercase mb-4">iPhone Preview</h3>
                            <button onClick={handleCopyLink} className={`w-full py-2.5 rounded-lg font-bold text-[10px] flex items-center justify-center gap-2 transition-all ${copyFeedback ? 'bg-[#22c55e] text-white' : 'bg-[#1d2d44] text-gray-300'}`}>
                                {copyFeedback ? <Check size={14} /> : <Copy size={14} />} {copyFeedback ? 'LINK COPIED' : 'COPY URL'}
                            </button>
                        </div>
                    </div>
                )}
            </div>
        );
    }

    return (
        <div className="h-screen bg-[#040b16] text-white flex flex-col max-w-2xl mx-auto overflow-hidden animate-in fade-in duration-700 relative">
            {/* Fixed Header Section */}
            <div ref={headerRef} className="fixed top-0 left-1/2 transform -translate-x-1/2 w-full max-w-2xl z-20 bg-[#040b16] pt-4 px-4 pb-2" style={{ height: 'auto', maxHeight: 'none', overflow: 'visible' }}>
                <div className="relative flex items-center justify-center mb-4">
                <div className="flex gap-4 sm:gap-5 items-center bg-[#0a1628] border border-[#1d2d44] px-4 py-2 rounded-full shadow-lg text-[10px] sm:text-xs font-black tracking-tight">
                    <div className="flex items-center"><span className="text-[#3b82f6] mr-1 uppercase">Shot:</span><span>{stats.shots}</span></div>
                        <div className="flex items-center"><span className="text-[#22c55e] mr-1 uppercase">Wins:</span><span>{stats.success}</span></div>
                    <div className="flex items-center"><span className="text-[#ef4444] mr-1 uppercase">Fail:</span><span>{stats.failed}</span></div>
                    <div className="flex items-center border-l border-[#1d2d44] pl-4 ml-1"><span className="text-[#f59e0b] mr-1 uppercase">Rate:</span><span>{rate}%</span></div>
                </div>
                    <div className="absolute right-4">
                    <button onClick={() => setShowModal('settings')} className="text-gray-400 hover:text-[#3b82f6] transition-all bg-[#0a1628] p-2 rounded-full border border-[#1d2d44]"><Key size={16} /></button>
                </div>
            </div>

                <div className="flex justify-center gap-2 sm:gap-3 mb-4">
                <ActionButton icon={<Book size={16} />} color="rgba(245, 158, 11, 0.15)" borderColor="rgba(245, 158, 11, 0.3)" iconColor="#f59e0b" description="Info" onClick={() => { setShowModal('instructions'); setModalTab('how'); }} />
                <ActionButton icon={<Lightbulb size={16} />} color="rgba(59, 130, 246, 0.15)" borderColor="rgba(59, 130, 246, 0.3)" iconColor="#3b82f6" description="Sol" onClick={() => setShowModal('solution')} />
                <ActionButton icon={<Bot size={16} />} color="rgba(139, 92, 246, 0.15)" borderColor="rgba(139, 92, 246, 0.3)" iconColor="#8b5cf6" description="AI" onClick={handleAiHint} />
                <ActionButton icon={<CheckCircle size={16} />} color="rgba(34, 197, 94, 0.15)" borderColor="rgba(34, 197, 94, 0.3)" iconColor="#22c55e" description="Win" onClick={handleMarkSuccess} />
                <ActionButton icon={<XCircle size={16} />} color="rgba(239, 68, 68, 0.15)" borderColor="rgba(239, 68, 68, 0.3)" iconColor="#ef4444" description="Failed" onClick={handleMarkFailed} />
                <ActionButton icon={<RotateCcw size={16} />} color="rgba(249, 115, 22, 0.15)" borderColor="rgba(249, 115, 22, 0.3)" iconColor="#f97316" description="Reset" onClick={() => setShowModal('restart_confirm')} />
                </div>
            </div>

            {/* Fixed Problem Panel - Directly below score panel */}
            <div 
                ref={problemPanelRef}
                style={{ 
                    position: 'fixed',
                    top: `${headerHeight}px`,
                    left: '50%',
                    transform: 'translateX(-50%)',
                    width: '100%',
                    maxWidth: '42rem',
                    zIndex: 15,
                    backgroundColor: '#040b16',
                    padding: '0 1rem',
                    paddingTop: '0',
                    paddingBottom: '0.75rem'
                }}
            >
                <div style={{ 
                    backgroundColor: '#0a1628', 
                    borderRadius: '0.75rem', 
                    padding: '1.5rem', 
                    boxShadow: '0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)', 
                    border: '1px solid #1d2d44',
                    maxHeight: 'none',
                    height: 'auto',
                    overflow: 'visible',
                    width: '100%',
                    minWidth: '100%'
                }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.25rem' }}>
                        <h2 style={{ fontSize: '1.125rem', fontWeight: 'bold', color: 'white', margin: 0 }}>Problem {exercise.id}</h2>
                        <button 
                            onClick={() => setShowModal('problem_full')}
                            style={{
                                backgroundColor: 'transparent',
                                border: '1px solid #1d2d44',
                                borderRadius: '0.5rem',
                                padding: '0.25rem 0.5rem',
                                color: '#3b82f6',
                                cursor: 'pointer',
                                display: 'flex',
                                alignItems: 'center',
                                gap: '0.25rem',
                                fontSize: '0.75rem'
                            }}
                        >
                            <ExternalLink size={14} />
                            <span>View Full</span>
                        </button>
                    </div>
                    <pre 
                        data-problem-description
                        className="problem-description-scroll"
                        id={`problem-desc-${exercise.id}`}
                        ref={problemDescriptionRef}
                        style={{ 
                            color: '#d1d5db',
                            fontSize: '0.875rem',
                            lineHeight: '1.75',
                            whiteSpace: 'pre-wrap',
                            wordWrap: 'break-word',
                            overflowWrap: 'break-word',
                            maxHeight: 'none',
                            height: 'auto',
                            overflowY: 'visible',
                            overflowX: 'hidden',
                            paddingRight: '12px',
                            paddingLeft: '4px',
                            marginBottom: '0.5rem',
                            margin: 0,
                            paddingTop: '8px',
                            paddingBottom: '8px',
                            fontFamily: 'inherit',
                            textOverflow: 'clip',
                            display: 'block',
                            WebkitLineClamp: 'unset',
                            lineClamp: 'unset',
                            width: '100%',
                            minWidth: '100%'
                        }}
                    >
                        {exercise.description}
                    </pre>
                </div>
            </div>

            {/* Scrollable Editor Section - Scrolls behind problem panel */}
            <div className="flex-1 overflow-y-auto px-4 pb-4" style={{ paddingTop: `${headerHeight + problemPanelHeight}px` }}>
                <div className="bg-[#0a1628] rounded-xl flex flex-col shadow-2xl border border-[#1d2d44] overflow-hidden" style={{ minHeight: `calc(100vh - ${headerHeight + problemPanelHeight}px)` }}>
                <div className="flex items-center justify-between p-2 bg-[#0d1b2a] border-b border-[#1d2d44] flex-shrink-0">
                    <div className="flex items-center gap-2 overflow-hidden">
                        <button onClick={startRenaming} className="p-1 hover:bg-[#1d2d44] rounded-full text-gray-400"><Pencil size={14} /></button>
                        {isEditingFileName ? (
                            <input autoFocus value={newName} onChange={(e) => setNewName(e.target.value)} onBlur={finishRenaming} onKeyDown={(e) => e.key === 'Enter' && finishRenaming()} className="bg-[#112240] text-sm border border-[#3b82f6] rounded px-2 py-0.5 outline-none text-white w-24" />
                        ) : (
                            <span className="text-sm font-bold text-gray-300 font-mono truncate max-w-[100px]">{files[activeFileIndex].name}</span>
                        )}
                    </div>
                    <div className="flex items-center gap-1">
                        <button onClick={addFile} className="p-1.5 hover:bg-[#1d2d44] rounded-full text-[#22c55e]"><Plus size={18} /></button>
                        <button onClick={removeFile} disabled={files.length <= 1} className="p-1.5 hover:bg-[#1d2d44] rounded-full text-[#ef4444] disabled:opacity-30"><Minus size={18} /></button>
                        <button onClick={runCode} disabled={isRunning} className="ml-1 flex items-center gap-1.5 px-3 py-1 rounded-lg font-bold text-xs bg-[#22c55e1a] border border-[#22c55e4d] text-[#22c55e]">
                            {isRunning ? <Loader2 size={12} className="animate-spin" /> : <Play size={12} fill="currentColor" />} RUN
                        </button>
                    </div>
                </div>
                <div className="flex bg-[#0a1628] border-b border-[#1d2d44] overflow-x-auto no-scrollbar">
                    {files.map((f, idx) => (
                        <button key={idx} onClick={() => setActiveFileIndex(idx)} className={`px-4 py-1.5 text-[10px] font-bold tracking-wider transition-all border-r border-[#1d2d44] whitespace-nowrap ${activeFileIndex === idx ? 'bg-[#050c18] text-[#3b82f6] border-b-2 border-b-[#3b82f6]' : 'text-gray-500'}`}>
                            {f.name}
                        </button>
                    ))}
                </div>
                <div className="flex-grow bg-[#050c18] relative" style={{ minHeight: '500px' }}>
                    <CodeMirror
                        value={files[activeFileIndex].content} height="500px" extensions={editorExtensions} onChange={updateActiveContent}
                        basicSetup={{ lineNumbers: true, autocompletion: true, bracketMatching: true, closeBrackets: true, indentOnInput: true }}
                    />
                </div>
                <div className="border-t border-[#1d2d44] p-2 bg-[#0a1628] flex-shrink-0">
                    <div ref={outputRef} className="h-24 overflow-y-auto">
                        <pre className="text-[10px] font-mono text-[#4ade80] whitespace-pre-wrap select-text">{output}</pre>

                    </div>
                    </div>
                </div>
            </div>

            {showModal !== 'none' && (
                <div className="fixed inset-0 bg-black/80 backdrop-blur-md flex items-center justify-center p-4 z-50 animate-in fade-in duration-200">
                    <div className="bg-[#112240] rounded-3xl p-6 max-w-lg w-full border border-[#1d2d44] shadow-2xl relative max-h-[80vh] flex flex-col overflow-hidden">
                        <button onClick={() => setShowModal('none')} className="absolute top-4 right-4 text-gray-400 z-10"><X size={24} /></button>
                        {showModal === 'instructions' && (
                            <div className="flex flex-col h-full">
                                <div className="flex gap-4 mb-4 border-b border-[#1d2d44]">
                                    <TabButton active={modalTab === 'how'} onClick={() => setModalTab('how')} label="Guide" />
                                    <TabButton active={modalTab === 'cheat'} onClick={() => setModalTab('cheat')} label="Cheat" />
                                    <TabButton active={modalTab === 'glossary'} onClick={() => setModalTab('glossary')} label="Glossary" />
                                    <TabButton active={modalTab === 'regex'} onClick={() => setModalTab('regex')} label="Regex" />
                                </div>
                                <div className="overflow-y-auto text-xs text-gray-300 space-y-4 flex-grow">
                                    {modalTab === 'how' && <p className="select-text">For full offline mode, add to <b>Home Screen</b>. Python logic is executed locally.</p>}
                                    {modalTab === 'cheat' && (
                                        <div className="bg-[#050c18] rounded-xl overflow-hidden border border-[#1d2d44]">
                                            <CodeMirror
                                                value={CHEAT_CONTENT}
                                                height="400px"
                                                readOnly={true}
                                                extensions={[python(), ...customPythonTheme]}
                                                basicSetup={{ lineNumbers: false, foldGutter: false }}
                                            />
                                        </div>
                                    )}
                                    {modalTab === 'glossary' && (
                                        <div className="bg-[#050c18] rounded-xl overflow-auto h-[400px] p-4 border border-[#1d2d44]">
                                            <pre className="text-[#4ade80] font-mono text-xs whitespace-pre-wrap select-text m-0">{GLOSSARY_CONTENT}</pre>
                                        </div>
                                    )}
                                    {modalTab === 'regex' && (
                                        <div className="bg-[#050c18] rounded-xl overflow-hidden border border-[#1d2d44]">
                                            <CodeMirror
                                                value={REGEX_CONTENT}
                                                height="400px"
                                                readOnly={true}
                                                extensions={[python(), ...customPythonTheme]}
                                                basicSetup={{ lineNumbers: false, foldGutter: false }}
                                            />
                                        </div>
                                    )}
                                </div>
                            </div>
                        )}
                        {showModal === 'solution' && (
                            <div className="flex flex-col h-full overflow-hidden">
                                <h2 className="text-lg font-bold mb-3 text-[#3b82f6]">Solution</h2>
                                <div className="bg-[#050c18] rounded-xl overflow-hidden border border-[#1d2d44] flex-grow">
                                    <CodeMirror value={exercise.solution} height="100%" readOnly={true} extensions={[python(), ...customPythonTheme]} />
                                </div>
                            </div>
                        )}
                        {showModal === 'hint' && (
                            <div className="flex flex-col">
                                <h2 className="text-lg font-bold mb-3 text-[#8b5cf6]">AI Analysis</h2>
                                <div className="bg-[#0d1b2a] p-3 rounded-xl border border-[#1d2d44] text-gray-200 italic mb-3 text-xs">{aiHintText}</div>
                            </div>
                        )}
                        {showModal === 'settings' && (
                            <div className="py-2">
                                <h2 className="text-lg font-bold mb-4 text-center">Settings</h2>

                                <div className="mb-6">
                                    <label className="block text-sm font-bold mb-2 text-gray-300">
                                        <Key size={14} className="inline mr-1" /> Gemini API Key
                                    </label>
                                    <input
                                        type="text"
                                        value={apiKey}
                                        onChange={(e) => setApiKey(e.target.value)}
                                        placeholder="Paste your API key here..."
                                        className="w-full bg-[#0d1b2a] border border-[#1d2d44] text-white px-4 py-3 rounded-xl text-sm font-mono focus:outline-none focus:border-[#3b82f6] transition-colors"
                                    />
                                    <p className="text-[10px] text-gray-400 mt-2 leading-relaxed">
                                        Get your API key from{' '}
                                        <a href="https://aistudio.google.com/app/apikey" target="_blank" rel="noreferrer" className="text-[#3b82f6] underline inline-flex items-center gap-0.5">
                                            Google AI Studio <ExternalLink size={10} />
                                        </a>
                                    </p>
                                </div>

                                <button
                                    onClick={() => {
                                        localStorage.setItem('gemini_api_key', apiKey);
                                        setShowModal('none');
                                    }}
                                    className="w-full bg-[#3b82f6] text-white font-bold py-4 rounded-xl mb-3 flex items-center justify-center gap-2 hover:bg-[#3b82f6]/90 transition-colors"
                                >
                                    <Check size={18} /> Save API Key
                                </button>

                                <button onClick={() => setShowModal('restart_confirm')} className="w-full border border-red-500/30 text-red-500 py-3 rounded-xl hover:bg-red-500/10 transition-colors">Reset Progress</button>
                            </div>
                        )}
                        {showModal === 'restart_confirm' && (
                            <div className="text-center py-4">
                                <h2 className="text-lg font-bold mb-2">Clear Stats?</h2>
                                <button onClick={handleRestartProgress} className="w-full bg-red-500 py-4 rounded-xl font-bold mb-3">Reset Now</button>
                                <button onClick={() => setShowModal('none')} className="w-full bg-[#1d2d44] py-4 rounded-xl">Cancel</button>
                            </div>
                        )}
                        {showModal === 'problem_full' && (
                            <div className="flex flex-col h-full overflow-hidden">
                                <h2 className="text-lg font-bold mb-3 text-[#3b82f6]">Problem {exercise.id} - Full Description</h2>
                                <div 
                                    className="bg-[#0d1b2a] p-4 rounded-xl border border-[#1d2d44] text-gray-200 text-sm leading-relaxed whitespace-pre-wrap break-words overflow-y-auto flex-grow" 
                                    style={{ 
                                        maxHeight: '60vh',
                                        minHeight: '200px',
                                        overflowY: 'auto',
                                        overflowX: 'hidden'
                                    }}
                                >
                                    <pre style={{ 
                                        margin: 0, 
                                        padding: 0, 
                                        fontFamily: 'inherit',
                                        whiteSpace: 'pre-wrap',
                                        wordWrap: 'break-word',
                                        overflowWrap: 'break-word'
                                    }}>
                                        {exercise.description}
                                    </pre>
                                </div>
                            </div>
                        )}
                    </div>
                </div>
            )}
        </div>
    );
};

const ActionButton: React.FC<{ icon: React.ReactNode, color: string, borderColor: string, iconColor: string, description: string, onClick: () => void }> = ({ icon, color, borderColor, iconColor, description, onClick }) => (
    <button onClick={onClick} style={{ backgroundColor: color, borderColor: borderColor, color: iconColor }} className="w-[42px] h-[42px] rounded-full flex flex-col items-center justify-center shadow-lg active:scale-90 transition-all border border-white/5">
        {icon}
        <span className="text-[6px] font-bold mt-0.5 uppercase tracking-tighter">{description}</span>
    </button>
);

const TabButton: React.FC<{ active: boolean, onClick: () => void, label: string }> = ({ active: isActive, onClick, label }) => (
    <button onClick={onClick} className={`pb-2 px-1 font-bold transition-all text-xs ${isActive ? 'text-white border-b-2 border-[#3b82f6]' : 'text-gray-500'}`}>{label}</button>
);

const X = ({ size, className }: { size: number, className?: string }) => (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className={className}><path d="M18 6 6 18" /><path d="m6 6 12 12" /></svg>
);

export default App;
