# Python Cheat Sheet - Templates & Examples
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

#glossary python 
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


#regular expressions
"""
**Character Classes**

* `a-z`: Matches any lowercase letter
* `A-Z`: Matches any uppercase letter
* `0-9`: Matches any digit
* `[a-zA-Z]`: Matches any letter (both lowercase and uppercase)
* `[0-9]`: Matches any digit
* `\d`: Matches any digit
* `\w`: Matches any word character (alphanumeric plus underscore)
* `\s`: Matches any whitespace character

**Special Characters**

* `.`: Matches any single character
* `^`: Matches the start of a string
* `$`: Matches the end of a string
* `*`: Matches 0 or more of the preceding character
* `+`: Matches 1 or more of the preceding character
* `?`: Matches 0 or 1 of the preceding character
* `{n, m}`: Matches between n and m of the preceding character
* `{n,}`: Matches at least n of the preceding character
* `{, m}`: Matches at most m of the preceding character

**Quantifiers**

* `*`: Matches 0 or more of the preceding character
* `+`: Matches 1 or more of the preceding character
* `?`: Matches 0 or 1 of the preceding character
* `{n, m}`: Matches between n and m of the preceding character
* `{n,}`: Matches at least n of the preceding character
* `{, m}`: Matches at most m of the preceding character

**Groups and Capturing**

* `(` and `)`: Used to group parts of a pattern together
* `\1`, `\2`, etc.: Refer to the capturing groups in the pattern

**Escaping**

* `\`: Escapes special characters
* `\b`: Matches a word boundary

Here are some examples of regex patterns:

* `\d{4}-\d{2}-\d{2}`: Matches a date in the format DD-MM-YYYY
* `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}`: Matches an email address
* `\d{3}-\d{3}-\d{4}`: Matches a credit card number
* `[a-zA-Z]+ [a-zA-Z]+, [A-Z]{2}`: Matches a full name
* `\d{1,3}\.\d{3,5}/\d{4}`: Matches a phone number

These are just a few examples of the many patterns you can use in regex. The specific patterns you use will depend on the problem you're trying to solve.

Do you have a specific problem you'd like me to help you solve using regex?
"""
