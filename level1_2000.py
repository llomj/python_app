""" 
Problem: 1501  
Use `default=` with `min()` to avoid crash on an empty set.
"""
s = set()
print(min(s, default=0))  # Expected: 0


""" 
Problem: 1502  
Use `default=` with `next()` to check for existence of an element in a list.
"""
nums = [1, 3, 5]
print(next((x for x in nums if x == 4), default="Missing"))  # Expected: "Missing"


""" 
Problem: 1503  
Use `default=` in `max()` to return fallback when list is empty.
"""
scores = []
print(max(scores, default="No scores"))  # Expected: "No scores"


""" 
Problem: 1504  
Use `default=` with `next()` to return a default if no element satisfies the condition.
"""
letters = ['a', 'b', 'c']
print(next((ch for ch in letters if ch == 'z'), default="Not found"))  # Expected: "Not found"


""" 
Problem: 1505  
Use `default=` in `max()` with a custom key function and empty input.
"""
strings = []
print(max(strings, key=str.lower, default="None"))  # Expected: "None"


""" 
Problem: 1506  
Use `default=` with `next()` to safely iterate a condition on a list of dictionaries.
"""
users = [{"name": "Alice"}, {"name": "Bob"}]
print(next((u for u in users if u["name"] == "Zoe"), default="No match"))  # Expected: "No match"


""" 
Problem: 1507  
Use `default=` with `min()` to handle a list that may be empty.
"""
data = []
print(min(data, default=-99))  # Expected: -99


""" 
Problem: 1508  
Use `default=` in `max()` to get highest score or "No data".
"""
scores = []
print(max(scores, default="No data"))  # Expected: "No data"


""" 
Problem: 1509  
Use `default=` in `next()` to avoid StopIteration on empty input.
"""
print(next(iter([]), default="Nothing"))  # Expected: "Nothing"


""" 
Problem: 1510  
Use `default=` with `max()` to find max string or return fallback.
"""
words = []
print(max(words, default="N/A"))  # Expected: "N/A"


""" 
Problem: 1511  
Use `default=` with `sorted()` to handle empty iterables and return a default sorted list.
"""
# Note: sorted() doesn't have a default parameter, but we can handle empty iterables
items = []
result = sorted(items) if items else []
print(result)  # Expected: []


""" 
Problem: 1512  
Use `default=` with `min()` to find the minimum value in a list of dictionaries by a key, or return a default.
"""
people = [{'age': 25}, {'age': 30}, {'age': 20}]
min_age_dict = min(people, key=lambda x: x.get('age', 0), default={'age': 0})
print(min_age_dict)  # Expected: {'age': 20}


""" 
Problem: 1513  
Use `default=` with `max()` to find the maximum length string in a list, or return 'No items' if empty.
"""
words = ['hello', 'world', 'python']
max_word = max(words, key=len, default='No items')
print(max_word)  # Expected: python


""" 
Problem: 1514  
Use `dict.get()` with a default value to safely access nested dictionary keys.
"""
data = {'user': {'name': 'Alice', 'age': 30}}
name = data.get('user', {}).get('name', 'Unknown')
city = data.get('user', {}).get('city', 'Unknown')
print(name, city)  # Expected: Alice Unknown


""" 
Problem: 1515  
Use `collections.defaultdict` with `int` as default factory to count occurrences of items in a list.
"""
from collections import defaultdict
items = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
counter = defaultdict(int)
for item in items:
    counter[item] += 1
print(dict(counter))  # Expected: {'apple': 3, 'banana': 2, 'cherry': 1}


""" 
Problem: 1516  
Use `dict.setdefault()` to initialize a list value in a dictionary if the key doesn't exist.
"""
data = {}
data.setdefault('items', []).append('apple')
data.setdefault('items', []).append('banana')
print(data)  # Expected: {'items': ['apple', 'banana']}


""" 
Problem: 1517  
Use `default=` with `next()` to get the first element from a filtered iterator, or return None.
"""
numbers = [1, 3, 5, 8, 10]
first_even = next((x for x in numbers if x % 2 == 0), None)
print(first_even)  # Expected: 8


""" 
Problem: 1518  
Use `collections.defaultdict` with `list` as default factory to group items by category.
"""
from collections import defaultdict
items = [('fruit', 'apple'), ('fruit', 'banana'), ('vegetable', 'carrot')]
grouped = defaultdict(list)
for category, item in items:
    grouped[category].append(item)
print(dict(grouped))  # Expected: {'fruit': ['apple', 'banana'], 'vegetable': ['carrot']}


""" 
Problem: 1519  
Use `dict.get()` with a default empty dictionary to safely access dictionary values.
"""
data = {'user': {'name': 'Alice'}}
user_info = data.get('user', {})
name = user_info.get('name', 'Unknown')
print(name)  # Expected: Alice


""" 
Problem: 1520  
Use `default=` with `min()` and a key function to find the shortest string, or return an empty string.
"""
words = ['hello', 'world', 'python', 'hi']
shortest = min(words, key=len, default='')
print(shortest)  # Expected: hi


""" 
Problem: 1521  
Use `dict.setdefault()` to create a nested dictionary structure with default values.
"""
data = {}
data.setdefault('user', {}).setdefault('profile', {})['name'] = 'Alice'
print(data)  # Expected: {'user': {'profile': {'name': 'Alice'}}}


""" 
Problem: 1522  
Use `default=` with `max()` to find the maximum value in a list of tuples by index, or return (0, 0).
"""
tuples = [(1, 5), (3, 2), (2, 8)]
max_tuple = max(tuples, key=lambda x: x[1], default=(0, 0))
print(max_tuple)  # Expected: (2, 8)


""" 
Problem: 1523  
Use `collections.defaultdict` with `set` as default factory to collect unique values per key.
"""
from collections import defaultdict
items = [('a', 1), ('a', 2), ('b', 1), ('a', 1), ('b', 3)]
grouped = defaultdict(set)
for key, value in items:
    grouped[key].add(value)
print({k: list(v) for k, v in grouped.items()})  # Expected: {'a': [1, 2], 'b': [1, 3]}


""" 
Problem: 1524  
Use `dict.get()` with a default value of 0 to safely sum values from multiple dictionaries.
"""
dict1 = {'a': 10, 'b': 20}
dict2 = {'b': 30, 'c': 40}
total = sum(dict1.get(k, 0) + dict2.get(k, 0) for k in set(dict1) | set(dict2))
print(total)  # Expected: 100


""" 
Problem: 1525  
Use `default=` with `next()` to get the first even number from an iterator, or return -1.
"""
numbers = [1, 3, 5, 7]
first_even = next((x for x in numbers if x % 2 == 0), -1)
print(first_even)  # Expected: -1


""" 
Problem: 1526  
Use `dict.setdefault()` to append items to a list value, creating the list if it doesn't exist.
"""
data = {}
data.setdefault('items', []).append('apple')
data.setdefault('items', []).append('banana')
print(data['items'])  # Expected: ['apple', 'banana']


""" 
Problem: 1527  
Use `default=` with `min()` to find the minimum age from a list of person dictionaries, or return 0.
"""
people = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
min_age = min((p.get('age', 0) for p in people), default=0)
print(min_age)  # Expected: 25


""" 
Problem: 1528  
Use `collections.defaultdict` with `lambda: []` to group strings by their first character.
"""
from collections import defaultdict
words = ['apple', 'banana', 'apricot', 'cherry', 'blueberry']
grouped = defaultdict(lambda: [])
for word in words:
    grouped[word[0]].append(word)
print(dict(grouped))  # Expected: {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}


""" 
Problem: 1529  
Use `dict.get()` with a default empty list to safely access list values from a dictionary.
"""
data = {'items': ['apple', 'banana']}
items = data.get('items', [])
missing = data.get('missing', [])
print(items, missing)  # Expected: ['apple', 'banana'] []


""" 
Problem: 1530  
Use `default=` with `max()` and a key function to find the longest word, or return 'N/A'.
"""
words = ['hello', 'world', 'python']
longest = max(words, key=len, default='N/A')
print(longest)  # Expected: python


""" 
Problem: 1531  
Use `dict.setdefault()` to initialize a counter dictionary with default value 0.
"""
counter = {}
counter.setdefault('count', 0)
counter['count'] += 1
print(counter)  # Expected: {'count': 1}


""" 
Problem: 1532  
Use `default=` with `next()` to get the first prime number from an iterator, or return None.
"""
def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

numbers = [4, 6, 8, 11, 12]
first_prime = next((x for x in numbers if is_prime(x)), None)
print(first_prime)  # Expected: 11


""" 
Problem: 1533  
Use `collections.defaultdict` with `int` to create a frequency counter for characters in a string.
"""
from collections import defaultdict
text = "hello"
char_count = defaultdict(int)
for char in text:
    char_count[char] += 1
print(dict(char_count))  # Expected: {'h': 1, 'e': 1, 'l': 2, 'o': 1}


""" 
Problem: 1534  
Use `dict.get()` with a default value to safely merge two dictionaries, handling missing keys.
"""
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = {k: dict1.get(k, 0) + dict2.get(k, 0) for k in set(dict1) | set(dict2)}
print(merged)  # Expected: {'a': 1, 'b': 5, 'c': 4}


""" 
Problem: 1535  
Use `default=` with `min()` to find the minimum score from a list of student records, or return 0.0.
"""
students = [{'name': 'Alice', 'score': 85.5}, {'name': 'Bob', 'score': 92.0}]
min_score = min((s.get('score', 0.0) for s in students), default=0.0)
print(min_score)  # Expected: 85.5


""" 
Problem: 1536  
Use `dict.setdefault()` to create a dictionary of lists, appending values to existing lists.
"""
data = {}
data.setdefault('fruits', []).append('apple')
data.setdefault('fruits', []).append('banana')
data.setdefault('vegetables', []).append('carrot')
print(data)  # Expected: {'fruits': ['apple', 'banana'], 'vegetables': ['carrot']}


""" 
Problem: 1537  
Use `default=` with `max()` to find the maximum price from a list of products, or return 'No products'.
"""
products = [{'name': 'laptop', 'price': 999}, {'name': 'phone', 'price': 699}]
max_price = max((p.get('price', 0) for p in products), default='No products')
print(max_price)  # Expected: 999


""" 
Problem: 1538  
Use `collections.defaultdict` with `lambda: defaultdict(int)` to create nested counters.
"""
from collections import defaultdict
data = [('a', 'x'), ('a', 'y'), ('b', 'x'), ('a', 'x')]
nested = defaultdict(lambda: defaultdict(int))
for key1, key2 in data:
    nested[key1][key2] += 1
print({k: dict(v) for k, v in nested.items()})  # Expected: {'a': {'x': 2, 'y': 1}, 'b': {'x': 1}}


""" 
Problem: 1539  
Use `dict.get()` with a default empty string to safely concatenate values from multiple dictionaries.
"""
dict1 = {'name': 'Alice'}
dict2 = {'surname': 'Smith'}
full_name = dict1.get('name', '') + ' ' + dict2.get('surname', '')
print(full_name)  # Expected: Alice Smith


""" 
Problem: 1540  
Use `default=` with `next()` to get the first element matching a condition, or return a default object.
"""
numbers = [1, 3, 5, 7, 9]
first_greater_than_5 = next((x for x in numbers if x > 5), None)
print(first_greater_than_5)  # Expected: 7


""" 
Problem: 1541  
Use `dict.setdefault()` to initialize a set value in a dictionary, adding items to the set.
"""
data = {}
data.setdefault('tags', set()).add('python')
data.setdefault('tags', set()).add('programming')
print(data)  # Expected: {'tags': {'python', 'programming'}}


""" 
Problem: 1542  
Use `default=` with `min()` and a custom key to find the oldest person, or return a default person dict.
"""
people = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
oldest = min(people, key=lambda x: x.get('age', 0), default={'name': 'Unknown', 'age': 0})
print(oldest)  # Expected: {'name': 'Bob', 'age': 25}


""" 
Problem: 1543  
Use `collections.defaultdict` with `str` as default factory to build a string concatenation dictionary.
"""
from collections import defaultdict
words = [('category', 'apple'), ('category', 'banana'), ('type', 'fruit')]
result = defaultdict(str)
for key, value in words:
    result[key] += value + ' '
print({k: v.strip() for k, v in result.items()})  # Expected: {'category': 'apple banana', 'type': 'fruit'}


""" 
Problem: 1544  
Use `dict.get()` with a default value of [] to safely extend a list from dictionary values.
"""
data = {'items': [1, 2, 3]}
existing = data.get('items', [])
existing.extend([4, 5])
print(existing)  # Expected: [1, 2, 3, 4, 5]


""" 
Problem: 1545  
Use `default=` with `max()` to find the maximum timestamp from a list of events, or return datetime.min.
"""
from datetime import datetime
events = [datetime(2023, 1, 1), datetime(2023, 2, 1), datetime(2023, 3, 1)]
max_date = max(events, default=datetime.min)
print(max_date)  # Expected: 2023-03-01 00:00:00


""" 
Problem: 1546  
Use `dict.setdefault()` to create a dictionary of dictionaries with nested default values.
"""
data = {}
data.setdefault('users', {}).setdefault('alice', {})['age'] = 30
data.setdefault('users', {}).setdefault('bob', {})['age'] = 25
print(data)  # Expected: {'users': {'alice': {'age': 30}, 'bob': {'age': 25}}}


""" 
Problem: 1547  
Use `default=` with `next()` to safely get the first item from a generator, or return a sentinel value.
"""
def number_gen():
    yield 1
    yield 2
    yield 3

gen = number_gen()
first = next(gen, 'END')
empty_gen = iter([])
empty_result = next(empty_gen, 'END')
print(first, empty_result)  # Expected: 1 END


""" 
Problem: 1548  
Use `collections.defaultdict` with `lambda: {'count': 0, 'total': 0}` to create statistics dictionaries.
"""
from collections import defaultdict
stats = defaultdict(lambda: {'count': 0, 'total': 0})
stats['item1']['count'] += 1
stats['item1']['total'] += 10
stats['item2']['count'] += 1
stats['item2']['total'] += 20
print(dict(stats))  # Expected: {'item1': {'count': 1, 'total': 10}, 'item2': {'count': 1, 'total': 20}}


""" 
Problem: 1549  
Use `dict.get()` with a default function call to lazily initialize dictionary values only when accessed.
"""
def create_list():
    return []

data = {}
# Using get with a callable default (note: dict.get doesn't support callables directly)
# This is a pattern where we check and initialize if needed
if 'items' not in data:
    data['items'] = create_list()
items = data.get('items', create_list())
items.append('apple')
print(data)  # Expected: {'items': ['apple']}


""" 
Problem: 1550  
Write a Pythonic way to use `functools.reduce()` to calculate the product of all numbers in a list.
"""
from functools import reduce
numbers = [2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Expected: 120


""" 
Problem: 1551  
Write a Pythonic way to use `functools.partial()` to create a function that multiplies a number by a fixed value.
"""
from functools import partial
multiply_by_5 = partial(lambda x, y: x * y, 5)
result = multiply_by_5(10)
print(result)  # Expected: 50


""" 
Problem: 1552  
Write a Pythonic way to use `functools.lru_cache()` to memoize a recursive Fibonacci function.
"""
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # Expected: 55


""" 
Problem: 1553  
Write a Pythonic way to use `itertools.permutations()` to generate all permutations of a list.
"""
from itertools import permutations
items = [1, 2, 3]
perms = list(permutations(items))
print(perms)  # Expected: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]


""" 
Problem: 1554  
Write a Pythonic way to use `itertools.product()` to generate the Cartesian product of two lists.
"""
from itertools import product
list1 = [1, 2]
list2 = ['a', 'b']
cartesian = list(product(list1, list2))
print(cartesian)  # Expected: [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]


""" 
Problem: 1555  
Write a Pythonic way to use `itertools.cycle()` to cycle through a list indefinitely.
"""
from itertools import cycle
colors = ['red', 'green', 'blue']
color_cycle = cycle(colors)
first_5 = [next(color_cycle) for _ in range(5)]
print(first_5)  # Expected: ['red', 'green', 'blue', 'red', 'green']


""" 
Problem: 1556  
Write a Pythonic way to use `itertools.repeat()` to create an iterator that repeats a value a specified number of times.
"""
from itertools import repeat
repeated = list(repeat('hello', 3))
print(repeated)  # Expected: ['hello', 'hello', 'hello']


""" 
Problem: 1557  
Write a Pythonic way to use `itertools.islice()` to get the first n elements from an iterator.
"""
from itertools import islice
numbers = range(10)
first_5 = list(islice(numbers, 5))
print(first_5)  # Expected: [0, 1, 2, 3, 4]


""" 
Problem: 1558  
Write a Pythonic way to use `itertools.tee()` to split an iterator into multiple independent iterators.
"""
from itertools import tee
numbers = iter([1, 2, 3, 4, 5])
iter1, iter2 = tee(numbers, 2)
print(list(iter1), list(iter2))  # Expected: [1, 2, 3, 4, 5] [1, 2, 3, 4, 5]


""" 
Problem: 1559  
Write a Pythonic way to use `itertools.accumulate()` to calculate cumulative sums of a list.
"""
from itertools import accumulate
numbers = [1, 2, 3, 4, 5]
cumulative = list(accumulate(numbers))
print(cumulative)  # Expected: [1, 3, 6, 10, 15]


""" 
Problem: 1560  
Write a Python program using `dataclasses` to create a simple Person class with name and age fields.
"""
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

person = Person("Alice", 30)
print(person)  # Expected: Person(name='Alice', age=30)


""" 
Problem: 1561  
Write a Python program using `dataclasses.field()` to set default values in a dataclass.
"""
from dataclasses import dataclass, field

@dataclass
class Student:
    name: str
    age: int = field(default=18)
    grades: list = field(default_factory=list)

student = Student("Bob")
print(student)  # Expected: Student(name='Bob', age=18, grades=[])


""" 
Problem: 1562  
Write a Python program using `@dataclass(frozen=True)` to create an immutable dataclass.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int

point = Point(3, 4)
print(point)  # Expected: Point(x=3, y=4)


""" 
Problem: 1563  
Write a Python function with type hints using `typing.List` to specify a function that takes a list of integers.
"""
from typing import List

def sum_numbers(numbers: List[int]) -> int:
    return sum(numbers)

result = sum_numbers([1, 2, 3, 4])
print(result)  # Expected: 10


""" 
Problem: 1564  
Write a Python function with type hints using `typing.Optional` to indicate a parameter that can be None.
"""
from typing import Optional

def greet(name: Optional[str] = None) -> str:
    if name is None:
        return "Hello, Guest!"
    return f"Hello, {name}!"

print(greet("Alice"), greet())  # Expected: Hello, Alice! Hello, Guest!


""" 
Problem: 1565  
Write a Python function with type hints using `typing.Union` to accept multiple types.
"""
from typing import Union

def process_value(value: Union[int, str]) -> str:
    return str(value)

print(process_value(42), process_value("hello"))  # Expected: 42 hello


""" 
Problem: 1566  
Write a Pythonic way to use the walrus operator (`:=`) to assign and check a value in a while loop condition.
"""
numbers = [1, 2, 3, 4, 5]
while (n := len(numbers)) > 0:
    numbers.pop()
    print(f"Remaining: {n}")  # Expected: Remaining: 5, 4, 3, 2, 1


""" 
Problem: 1567  
Write a Pythonic way to use the walrus operator (`:=`) in a list comprehension to avoid repeated function calls.
"""
def expensive_function(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]
result = [y for x in numbers if (y := expensive_function(x)) > 4]
print(result)  # Expected: [6, 8, 10]


""" 
Problem: 1568  
Write a Python program using `match/case` statements to handle different string patterns.
"""
def handle_command(cmd: str) -> str:
    match cmd:
        case "start":
            return "Starting..."
        case "stop":
            return "Stopping..."
        case "pause":
            return "Paused"
        case _:
            return "Unknown command"

print(handle_command("start"))  # Expected: Starting...


""" 
Problem: 1569  
Write a Python program using `match/case` with pattern matching to destructure a tuple.
"""
def process_point(point):
    match point:
        case (0, 0):
            return "Origin"
        case (x, 0):
            return f"On x-axis at {x}"
        case (0, y):
            return f"On y-axis at {y}"
        case (x, y):
            return f"Point at ({x}, {y})"

print(process_point((3, 4)))  # Expected: Point at (3, 4)


""" 
Problem: 1570  
Write a Python class using `@property` decorator to create a computed attribute.
"""
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def area(self):
        return 3.14159 * self.radius ** 2

circle = Circle(5)
print(circle.area)  # Expected: 78.53975


""" 
Problem: 1571  
Write a Python class using `@property.setter` to validate and set a property value.
"""
class Temperature:
    def __init__(self):
        self._celsius = 0
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = value

temp = Temperature()
temp.celsius = 25
print(temp.celsius)  # Expected: 25


""" 
Problem: 1572  
Write a Python class implementing `__str__` magic method to customize string representation.
"""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"{self.title} by {self.author}"

book = Book("Python Guide", "John Doe")
print(str(book))  # Expected: Python Guide by John Doe


""" 
Problem: 1573  
Write a Python class implementing `__repr__` magic method to provide a developer-friendly representation.
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

point = Point(3, 4)
print(repr(point))  # Expected: Point(x=3, y=4)


""" 
Problem: 1574  
Write a Python class implementing `__eq__` magic method to define equality comparison.
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        return self.name == other.name and self.age == other.age

p1 = Person("Alice", 30)
p2 = Person("Alice", 30)
print(p1 == p2)  # Expected: True


""" 
Problem: 1575  
Write a Python class implementing `__hash__` magic method to make an object hashable.
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

point = Point(3, 4)
points_set = {point}
print(len(points_set))  # Expected: 1


""" 
Problem: 1576  
Write a Python class implementing `__len__` magic method to make an object work with `len()`.
"""
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def __len__(self):
        return len(self.items)

stack = Stack()
stack.push(1)
stack.push(2)
print(len(stack))  # Expected: 2


""" 
Problem: 1577  
Write a Python class implementing `__getitem__` magic method to enable indexing.
"""
class MyList:
    def __init__(self, items):
        self.items = items
    
    def __getitem__(self, index):
        return self.items[index]

my_list = MyList([10, 20, 30, 40])
print(my_list[2])  # Expected: 30


""" 
Problem: 1578  
Write a Python program using a custom context manager class with `__enter__` and `__exit__` methods.
"""
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.elapsed = time.time() - self.start
        print(f"Elapsed time: {self.elapsed:.2f} seconds")

with Timer():
    sum(range(1000000))  # Expected: Elapsed time: ~0.XX seconds


""" 
Problem: 1579  
Write a Pythonic way to use `contextlib.ExitStack` to manage multiple context managers.
"""
from contextlib import ExitStack

class Resource:
    def __enter__(self):
        print("Entering resource")
        return self
    def __exit__(self, *args):
        print("Exiting resource")

with ExitStack() as stack:
    r1 = stack.enter_context(Resource())
    r2 = stack.enter_context(Resource())
    print("Using resources")  # Expected: Entering resource, Entering resource, Using resources, Exiting resource, Exiting resource


""" 
Problem: 1580  
Write a Pythonic way to use `pathlib.Path` to check if a file exists.
"""
from pathlib import Path

# Note: This is a demonstration - actual file may not exist
path = Path("example.txt")
exists = path.exists()
print(f"File exists: {exists}")  # Expected: File exists: False (or True if file exists)


""" 
Problem: 1581  
Write a Pythonic way to use `pathlib.Path` to get the parent directory of a file path.
"""
from pathlib import Path

path = Path("/home/user/documents/file.txt")
parent = path.parent
print(parent)  # Expected: /home/user/documents


""" 
Problem: 1582  
Write a Pythonic way to use `pathlib.Path` to join path components.
"""
from pathlib import Path

base = Path("/home/user")
full_path = base / "documents" / "file.txt"
print(full_path)  # Expected: /home/user/documents/file.txt


""" 
Problem: 1583  
Write a Python program using `json.dumps()` to convert a Python dictionary to a JSON string.
"""
import json

data = {"name": "Alice", "age": 30, "city": "New York"}
json_string = json.dumps(data)
print(json_string)  # Expected: {"name": "Alice", "age": 30, "city": "New York"}


""" 
Problem: 1584  
Write a Python program using `json.loads()` to parse a JSON string into a Python dictionary.
"""
import json

json_string = '{"name": "Alice", "age": 30}'
data = json.loads(json_string)
print(data)  # Expected: {'name': 'Alice', 'age': 30}


""" 
Problem: 1585  
Write a Python program using `re.sub()` to replace all occurrences of a pattern in a string.
"""
import re

text = "The cat sat on the mat"
new_text = re.sub(r'cat', 'dog', text)
print(new_text)  # Expected: The dog sat on the mat


""" 
Problem: 1586  
Write a Python program using `re.finditer()` to find all matches of a pattern and get their positions.
"""
import re

text = "The cat and the hat"
pattern = r'\b\w{3}\b'
matches = [(m.group(), m.start()) for m in re.finditer(pattern, text)]
print(matches)  # Expected: [('The', 0), ('cat', 4), ('and', 8), ('the', 12), ('hat', 16)]


""" 
Problem: 1587  
Write a Python program using named groups in regex to extract specific parts of a string.
"""
import re

text = "John Doe, age 30"
pattern = r'(?P<name>\w+\s+\w+).*age\s+(?P<age>\d+)'
match = re.search(pattern, text)
if match:
    print(match.group('name'), match.group('age'))  # Expected: John Doe 30


""" 
Problem: 1588  
Write a Pythonic way to use `collections.OrderedDict` to maintain insertion order in a dictionary.
"""
from collections import OrderedDict

od = OrderedDict()
od['first'] = 1
od['second'] = 2
od['third'] = 3
print(list(od.keys()))  # Expected: ['first', 'second', 'third']


""" 
Problem: 1589  
Write a Pythonic way to use `collections.ChainMap` to combine multiple dictionaries into a single mapping.
"""
from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
chain = ChainMap(dict1, dict2)
print(dict(chain))  # Expected: {'a': 1, 'b': 2, 'c': 3, 'd': 4}


""" 
Problem: 1590  
Write a Pythonic way to use `collections.namedtuple` to create a simple data structure with named fields.
"""
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
print(p.x, p.y)  # Expected: 3 4


""" 
Problem: 1591  
Write a Pythonic way to use nested list comprehensions to create a matrix.
"""
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)  # Expected: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]


""" 
Problem: 1592  
Write a Pythonic way to use a list comprehension with multiple conditions to filter elements.
"""
numbers = range(20)
filtered = [x for x in numbers if x % 2 == 0 and x % 3 == 0]
print(filtered)  # Expected: [0, 6, 12, 18]


""" 
Problem: 1593  
Write a Pythonic way to use `operator.attrgetter()` to sort a list of objects by an attribute.
"""
from operator import attrgetter

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 35)]
sorted_people = sorted(people, key=attrgetter('age'))
print([p.name for p in sorted_people])  # Expected: ['Bob', 'Alice', 'Charlie']


""" 
Problem: 1594  
Write a Pythonic way to use `operator.methodcaller()` to call a method on multiple objects.
"""
from operator import methodcaller

class Person:
    def greet(self):
        return "Hello"

people = [Person(), Person(), Person()]
greetings = list(map(methodcaller('greet'), people))
print(greetings)  # Expected: ['Hello', 'Hello', 'Hello']


""" 
Problem: 1595  
Write a Pythonic way to use `str.removeprefix()` to remove a prefix from a string if it exists.
"""
text = "HelloWorld"
result = text.removeprefix("Hello")
print(result)  # Expected: World


""" 
Problem: 1596  
Write a Pythonic way to use `str.removesuffix()` to remove a suffix from a string if it exists.
"""
text = "HelloWorld"
result = text.removesuffix("World")
print(result)  # Expected: Hello


""" 
Problem: 1597  
Write a Pythonic way to use `str.rsplit()` to split a string from the right, limiting the number of splits.
"""
text = "one.two.three.four"
parts = text.rsplit('.', 2)
print(parts)  # Expected: ['one.two', 'three', 'four']


""" 
Problem: 1598  
Write a Pythonic way to use `list.copy()` to create a shallow copy of a list.
"""
original = [1, 2, [3, 4]]
copied = original.copy()
copied[0] = 10
print(original, copied)  # Expected: [1, 2, [3, 4]] [10, 2, [3, 4]]


""" 
Problem: 1599  
Write a Pythonic way to use `list.clear()` to remove all elements from a list.
"""
my_list = [1, 2, 3, 4, 5]
my_list.clear()
print(my_list)  # Expected: []


""" 
Problem: 1600  
Write a Pythonic way to use `dict.popitem()` to remove and return the last key-value pair from a dictionary.
"""
d = {'a': 1, 'b': 2, 'c': 3}
item = d.popitem()
print(item, d)  # Expected: ('c', 3) {'a': 1, 'b': 2}


""" 
Problem: 1601  
Write a Pythonic way to use `dict.update()` to merge another dictionary into an existing one.
"""
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict1.update(dict2)
print(dict1)  # Expected: {'a': 1, 'b': 2, 'c': 3, 'd': 4}


""" 
Problem: 1602  
Write a Pythonic way to use `dict.keys()` to iterate over dictionary keys.
"""
d = {'a': 1, 'b': 2, 'c': 3}
keys = list(d.keys())
print(keys)  # Expected: ['a', 'b', 'c']


""" 
Problem: 1603  
Write a Pythonic way to use `dict.values()` to get all values from a dictionary as a view.
"""
d = {'a': 1, 'b': 2, 'c': 3}
values = list(d.values())
print(values)  # Expected: [1, 2, 3]


""" 
Problem: 1604  
Write a Pythonic way to use `dict.items()` to iterate over key-value pairs in a dictionary.
"""
d = {'a': 1, 'b': 2, 'c': 3}
items = list(d.items())
print(items)  # Expected: [('a', 1), ('b', 2), ('c', 3)]


""" 
Problem: 1605  
Write a Python program to define a custom exception class that inherits from Exception.
"""
class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom error")
except CustomError as e:
    print(f"Caught: {e}")  # Expected: Caught: This is a custom error


""" 
Problem: 1606  
Write a Python program using exception chaining with `raise...from` to preserve the original exception.
"""
try:
    try:
        int("not a number")
    except ValueError as e:
        raise TypeError("Conversion failed") from e
except TypeError as e:
    print(f"Error: {e}, caused by: {e.__cause__}")  # Expected: Error: Conversion failed, caused by: invalid literal for int() with base 10: 'not a number'


""" 
Problem: 1607  
Write a Pythonic way to use `contextlib.redirect_stdout` to capture print output to a string.
"""
from contextlib import redirect_stdout
from io import StringIO

f = StringIO()
with redirect_stdout(f):
    print("Hello, World!")
    print("Python is great!")
output = f.getvalue()
print(f"Captured: {output}")  # Expected: Captured: Hello, World!\nPython is great!\n


""" 
Problem: 1608  
Write a Pythonic way to use `functools.wraps` to preserve function metadata in a decorator.
"""
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def my_function():
    """This is a docstring."""
    pass

print(my_function.__name__)  # Expected: my_function


""" 
Problem: 1609  
Write a Pythonic way to use `itertools.accumulate()` with a custom function to calculate cumulative products.
"""
from itertools import accumulate
import operator

numbers = [2, 3, 4, 5]
cumulative_products = list(accumulate(numbers, operator.mul))
print(cumulative_products)  # Expected: [2, 6, 24, 120]


""" 
Problem: 1610  
Write a Pythonic way to use `itertools.combinations_with_replacement()` to generate combinations allowing repeated elements.
"""
from itertools import combinations_with_replacement

items = ['a', 'b', 'c']
combs = list(combinations_with_replacement(items, 2))
print(combs)  # Expected: [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'b'), ('b', 'c'), ('c', 'c')]


""" 
Problem: 1611  
Write a Pythonic way to use `itertools.dropwhile()` to skip elements until a condition is false.
"""
from itertools import dropwhile

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = list(dropwhile(lambda x: x < 5, numbers))
print(result)  # Expected: [5, 6, 7, 8]


""" 
Problem: 1612  
Write a Pythonic way to use `itertools.takewhile()` to take elements from an iterator while a condition is true.
"""
from itertools import takewhile

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = list(takewhile(lambda x: x < 5, numbers))
print(result)  # Expected: [1, 2, 3, 4]


""" 
Problem: 1613  
Write a Pythonic way to use `itertools.starmap()` to apply a function to arguments unpacked from tuples.
"""
from itertools import starmap
import operator

pairs = [(2, 3), (4, 5), (6, 7)]
products = list(starmap(operator.mul, pairs))
print(products)  # Expected: [6, 20, 42]


""" 
Problem: 1614  
Write a Pythonic way to use `functools.cmp_to_key()` to convert an old-style comparison function to a key function.
"""
from functools import cmp_to_key

def compare(x, y):
    return y - x  # Reverse order

numbers = [3, 1, 4, 1, 5]
sorted_nums = sorted(numbers, key=cmp_to_key(compare))
print(sorted_nums)  # Expected: [5, 4, 3, 1, 1]


""" 
Problem: 1615  
Write a Pythonic way to use `functools.singledispatch` to create a function with method overloading based on argument type.
"""
from functools import singledispatch

@singledispatch
def process(value):
    return f"Unknown type: {type(value).__name__}"

@process.register
def _(value: int):
    return f"Integer: {value}"

@process.register
def _(value: str):
    return f"String: {value}"

print(process(42), process("hello"))  # Expected: Integer: 42 String: hello


""" 
Problem: 1616  
Write a Python program using `typing.Dict` to specify a function parameter that accepts a dictionary with string keys and integer values.
"""
from typing import Dict

def process_scores(scores: Dict[str, int]) -> int:
    return sum(scores.values())

result = process_scores({"Alice": 85, "Bob": 90})
print(result)  # Expected: 175


""" 
Problem: 1617  
Write a Python program using `typing.Tuple` to specify a function that returns a tuple of specific types.
"""
from typing import Tuple

def get_name_age() -> Tuple[str, int]:
    return ("Alice", 30)

name, age = get_name_age()
print(f"{name} is {age}")  # Expected: Alice is 30


""" 
Problem: 1618  
Write a Python program using `typing.Callable` to specify a function parameter that accepts a callable.
"""
from typing import Callable

def apply_operation(x: int, y: int, op: Callable[[int, int], int]) -> int:
    return op(x, y)

result = apply_operation(5, 3, lambda a, b: a * b)
print(result)  # Expected: 15


""" 
Problem: 1619  
Write a Python program using `match/case` with guards (if conditions) to add additional pattern matching logic.
"""
def categorize(value):
    match value:
        case x if x < 0:
            return "Negative"
        case x if x == 0:
            return "Zero"
        case x if x > 0:
            return "Positive"

print(categorize(-5), categorize(0), categorize(5))  # Expected: Negative Zero Positive


""" 
Problem: 1620  
Write a Python program using `match/case` with `_` as a catch-all pattern to handle unmatched cases.
"""
def handle_status(code):
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _:
            return "Unknown Status"

print(handle_status(200), handle_status(999))  # Expected: OK Unknown Status


""" 
Problem: 1621  
Write a Python class using `@property.deleter` to define behavior when a property is deleted.
"""
class Person:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.deleter
    def name(self):
        print("Deleting name")
        self._name = None

p = Person("Alice")
del p.name
print(p.name)  # Expected: Deleting name, None


""" 
Problem: 1622  
Write a Python class implementing `__setitem__` magic method to enable item assignment.
"""
class MyDict:
    def __init__(self):
        self._data = {}
    
    def __setitem__(self, key, value):
        self._data[key] = value
    
    def __getitem__(self, key):
        return self._data[key]

my_dict = MyDict()
my_dict['key'] = 'value'
print(my_dict['key'])  # Expected: value


""" 
Problem: 1623  
Write a Python class implementing `__delitem__` magic method to enable item deletion.
"""
class MyList:
    def __init__(self, items):
        self.items = items
    
    def __delitem__(self, index):
        del self.items[index]

my_list = MyList([1, 2, 3, 4, 5])
del my_list[2]
print(my_list.items)  # Expected: [1, 2, 4, 5]


""" 
Problem: 1624  
Write a Python class implementing `__contains__` magic method to enable `in` operator support.
"""
class MyContainer:
    def __init__(self, items):
        self.items = items
    
    def __contains__(self, item):
        return item in self.items

container = MyContainer([1, 2, 3, 4, 5])
print(3 in container)  # Expected: True


""" 
Problem: 1625  
Write a Python class implementing `__iter__` and `__next__` magic methods to create a custom iterator.
"""
class CountDown:
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

counter = CountDown(5)
print(list(counter))  # Expected: [5, 4, 3, 2, 1]


""" 
Problem: 1626  
Write a Python program using `contextlib.contextmanager` decorator to create a context manager from a generator function.
"""
from contextlib import contextmanager

@contextmanager
def my_context():
    print("Entering context")
    yield "context value"
    print("Exiting context")

with my_context() as value:
    print(f"Inside context: {value}")  # Expected: Entering context, Inside context: context value, Exiting context


""" 
Problem: 1627  
Write a Pythonic way to use `pathlib.Path.read_text()` to read the entire contents of a text file.
"""
from pathlib import Path

# Note: This is a demonstration - file may not exist
# In practice: content = Path("file.txt").read_text()
print("Demonstration: Path('file.txt').read_text() reads file content")


""" 
Problem: 1628  
Write a Pythonic way to use `pathlib.Path.write_text()` to write text to a file.
"""
from pathlib import Path

# Note: This is a demonstration - file may not exist
# In practice: Path("file.txt").write_text("Hello, World!")
print("Demonstration: Path('file.txt').write_text('Hello, World!') writes to file")


""" 
Problem: 1629  
Write a Pythonic way to use `pathlib.Path.glob()` to find all files matching a pattern.
"""
from pathlib import Path

# Note: This is a demonstration
# In practice: files = list(Path('.').glob('*.py'))
print("Demonstration: Path('.').glob('*.py') finds all .py files")


""" 
Problem: 1630  
Write a Python program using `json.dump()` to write a Python object to a JSON file.
"""
import json
from pathlib import Path

data = {"name": "Alice", "age": 30}
# Note: In practice: json.dump(data, open("data.json", "w"))
print("Demonstration: json.dump(data, open('data.json', 'w')) writes JSON to file")


""" 
Problem: 1631  
Write a Python program using `json.load()` to read a JSON file and parse it into a Python object.
"""
import json

# Note: In practice: data = json.load(open("data.json"))
print("Demonstration: json.load(open('data.json')) reads and parses JSON file")


""" 
Problem: 1632  
Write a Python program using `re.compile()` to create a compiled regex pattern for repeated use.
"""
import re

pattern = re.compile(r'\d+')
text = "I have 3 cats and 2 dogs"
matches = pattern.findall(text)
print(matches)  # Expected: ['3', '2']


""" 
Problem: 1633  
Write a Python program using `re.split()` to split a string by a regex pattern.
"""
import re

text = "apple,banana;cherry:date"
parts = re.split(r'[,;:]', text)
print(parts)  # Expected: ['apple', 'banana', 'cherry', 'date']


""" 
Problem: 1634  
Write a Pythonic way to use `collections.OrderedDict.move_to_end()` to move a key to the end of an ordered dictionary.
"""
from collections import OrderedDict

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
od.move_to_end('a')
print(list(od.keys()))  # Expected: ['b', 'c', 'a']


""" 
Problem: 1635  
Write a Pythonic way to use `collections.ChainMap.new_child()` to add a new dictionary to the beginning of a ChainMap.
"""
from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3}
chain = ChainMap(dict1)
new_chain = chain.new_child(dict2)
print(dict(new_chain))  # Expected: {'c': 3, 'a': 1, 'b': 2}


""" 
Problem: 1636  
Write a Pythonic way to use `collections.namedtuple._replace()` to create a new namedtuple with updated fields.
"""
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p1 = Point(3, 4)
p2 = p1._replace(x=10)
print(p1, p2)  # Expected: Point(x=3, y=4) Point(x=10, y=4)


""" 
Problem: 1637  
Write a Pythonic way to use a dictionary comprehension with nested loops to create a multiplication table dictionary.
"""
table = {f"{i}x{j}": i * j for i in range(1, 4) for j in range(1, 4)}
print(table)  # Expected: {'1x1': 1, '1x2': 2, ..., '3x3': 9}


""" 
Problem: 1638  
Write a Pythonic way to use a set comprehension to create a set of unique characters from multiple strings.
"""
strings = ["hello", "world", "python"]
unique_chars = {char for s in strings for char in s}
print(sorted(unique_chars))  # Expected: ['d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y']


""" 
Problem: 1639  
Write a Pythonic way to use `operator.add` with `functools.reduce()` to sum a list of numbers.
"""
from functools import reduce
import operator

numbers = [1, 2, 3, 4, 5]
total = reduce(operator.add, numbers)
print(total)  # Expected: 15


""" 
Problem: 1640  
Write a Pythonic way to use `operator.mul` with `functools.reduce()` to calculate the product of a list.
"""
from functools import reduce
import operator

numbers = [2, 3, 4]
product = reduce(operator.mul, numbers)
print(product)  # Expected: 24


""" 
Problem: 1641  
Write a Python program using `str.casefold()` to perform case-insensitive string comparison.
"""
str1 = "Hello"
str2 = "HELLO"
print(str1.casefold() == str2.casefold())  # Expected: True


""" 
Problem: 1642  
Write a Python program using `str.encode()` to convert a string to bytes using UTF-8 encoding.
"""
text = "Hello, World!"
encoded = text.encode('utf-8')
print(encoded)  # Expected: b'Hello, World!'


""" 
Problem: 1643  
Write a Python program using `bytes.decode()` to convert bytes back to a string.
"""
bytes_data = b'Hello, World!'
decoded = bytes_data.decode('utf-8')
print(decoded)  # Expected: Hello, World!


""" 
Problem: 1644  
Write a Pythonic way to use `list.extend()` to add multiple elements from an iterable to a list.
"""
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list)  # Expected: [1, 2, 3, 4, 5, 6]


""" 
Problem: 1645  
Write a Pythonic way to use `list.index()` to find the index of the first occurrence of an element.
"""
my_list = [10, 20, 30, 20, 40]
index = my_list.index(20)
print(index)  # Expected: 1


""" 
Problem: 1646  
Write a Pythonic way to use `dict.fromkeys()` to create a dictionary with keys from a list and a default value.
"""
keys = ['a', 'b', 'c']
d = dict.fromkeys(keys, 0)
print(d)  # Expected: {'a': 0, 'b': 0, 'c': 0}


""" 
Problem: 1647  
Write a Python program using a try-except-else block where the else clause runs only if no exception occurs.
"""
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division by zero")
else:
    print(f"Result: {result}")  # Expected: Result: 5.0


""" 
Problem: 1648  
Write a Python program using a try-except-finally block where finally always executes regardless of exceptions.
"""
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Caught division by zero")
finally:
    print("This always executes")  # Expected: Caught division by zero, This always executes


""" 
Problem: 1649  
Write a Pythonic way to use `contextlib.suppress()` with multiple exception types to ignore multiple types of errors.
"""
from contextlib import suppress

with suppress(ValueError, TypeError, ZeroDivisionError):
    result = int("not a number")  # Would raise ValueError, but suppressed
    print("This won't print")
print("Continues after suppressed exception")  # Expected: Continues after suppressed exception


""" 
Problem: 1650  
Write a Python function called `subtract_numbers` that takes two numbers as parameters and returns their difference.
"""
def subtract_numbers(a, b):
    return a - b

result = subtract_numbers(10, 3)
print(result)  # Expected: 7


""" 
Problem: 1651  
Write a Python function called `divide_numbers` that takes two numbers as parameters and returns their quotient.
"""
def divide_numbers(a, b):
    return a / b

result = divide_numbers(10, 2)
print(result)  # Expected: 5.0


""" 
Problem: 1652  
Write a Python function called `calculate_remainder` that takes two numbers as parameters and returns the remainder when the first number is divided by the second.
"""
def calculate_remainder(a, b):
    return a % b

result = calculate_remainder(10, 3)
print(result)  # Expected: 1


""" 
Problem: 1653  
Write a Python function called `calculate_power` that takes a base and exponent as parameters and returns the base raised to the exponent.
"""
def calculate_power(base, exponent):
    return base ** exponent

result = calculate_power(2, 3)
print(result)  # Expected: 8


""" 
Problem: 1654  
Write a Python function called `calculate_circle_area` that takes the radius as a parameter and returns the area of a circle (use 3.14 for pi).
"""
def calculate_circle_area(radius):
    return 3.14 * radius * radius

result = calculate_circle_area(5)
print(result)  # Expected: 78.5


""" 
Problem: 1655  
Write a Python function called `calculate_rectangle_area` that takes length and width as parameters and returns the area of a rectangle.
"""
def calculate_rectangle_area(length, width):
    return length * width

result = calculate_rectangle_area(5, 3)
print(result)  # Expected: 15


""" 
Problem: 1656  
Write a Python function called `calculate_triangle_area` that takes base and height as parameters and returns the area of a triangle.
"""
def calculate_triangle_area(base, height):
    return 0.5 * base * height

result = calculate_triangle_area(4, 6)
print(result)  # Expected: 12.0


""" 
Problem: 1657  
Write a Python function called `convert_celsius_to_fahrenheit` that takes a temperature in Celsius and returns it converted to Fahrenheit.
"""
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

result = convert_celsius_to_fahrenheit(25)
print(result)  # Expected: 77.0


""" 
Problem: 1658  
Write a Python function called `convert_fahrenheit_to_celsius` that takes a temperature in Fahrenheit and returns it converted to Celsius.
"""
def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

result = convert_fahrenheit_to_celsius(77)
print(result)  # Expected: 25.0


""" 
Problem: 1659  
Write a Python function called `is_positive` that takes a number as input and returns True if the number is positive, and False otherwise.
"""
def is_positive(number):
    return number > 0

print(is_positive(5), is_positive(-3))  # Expected: True False


""" 
Problem: 1660  
Write a Python function called `is_negative` that takes a number as input and returns True if the number is negative, and False otherwise.
"""
def is_negative(number):
    return number < 0

print(is_negative(-5), is_negative(3))  # Expected: True False


""" 
Problem: 1661  
Write a Python function called `get_first_char` that takes a string as input and returns the first character of the string.
"""
def get_first_char(text):
    return text[0]

result = get_first_char("Hello")
print(result)  # Expected: H


""" 
Problem: 1662  
Write a Python function called `get_last_char` that takes a string as input and returns the last character of the string.
"""
def get_last_char(text):
    return text[-1]

result = get_last_char("Hello")
print(result)  # Expected: o


""" 
Problem: 1663  
Write a Python function called `get_middle_char` that takes a string as input and returns the middle character. If the string has even length, return the character at index length//2.
"""
def get_middle_char(text):
    return text[len(text) // 2]

result = get_middle_char("Hello")
print(result)  # Expected: l


""" 
Problem: 1664  
Write a Python function called `repeat_string` that takes a string and a number n, and returns the string repeated n times.
"""
def repeat_string(text, n):
    return text * n

result = repeat_string("Hi", 3)
print(result)  # Expected: HiHiHi


""" 
Problem: 1665  
Write a Python function called `swap_first_last` that takes a string as input and returns a new string with the first and last characters swapped.
"""
def swap_first_last(text):
    if len(text) <= 1:
        return text
    return text[-1] + text[1:-1] + text[0]

result = swap_first_last("Hello")
print(result)  # Expected: oellH


""" 
Problem: 1666  
Write a Python function called `remove_first_char` that takes a string as input and returns the string with the first character removed.
"""
def remove_first_char(text):
    return text[1:]

result = remove_first_char("Hello")
print(result)  # Expected: ello


""" 
Problem: 1667  
Write a Python function called `remove_last_char` that takes a string as input and returns the string with the last character removed.
"""
def remove_last_char(text):
    return text[:-1]

result = remove_last_char("Hello")
print(result)  # Expected: Hell


""" 
Problem: 1668  
Write a Python function called `get_first_word` that takes a string of words separated by spaces and returns the first word.
"""
def get_first_word(text):
    return text.split()[0]

result = get_first_word("Hello World Python")
print(result)  # Expected: Hello


""" 
Problem: 1669  
Write a Python function called `get_last_word` that takes a string of words separated by spaces and returns the last word.
"""
def get_last_word(text):
    return text.split()[-1]

result = get_last_word("Hello World Python")
print(result)  # Expected: Python


""" 
Problem: 1670  
Write a Python function called `count_characters` that takes a string as input and returns the number of characters in the string (excluding spaces).
"""
def count_characters(text):
    return len(text.replace(" ", ""))

result = count_characters("Hello World")
print(result)  # Expected: 10


""" 
Problem: 1671  
Write a Python function called `add_to_list` that takes a list and an element, and returns a new list with the element added at the end.
"""
def add_to_list(my_list, element):
    new_list = my_list.copy()
    new_list.append(element)
    return new_list

result = add_to_list([1, 2, 3], 4)
print(result)  # Expected: [1, 2, 3, 4]


""" 
Problem: 1672  
Write a Python function called `get_first_element` that takes a list and returns the first element of the list.
"""
def get_first_element(my_list):
    return my_list[0]

result = get_first_element([10, 20, 30])
print(result)  # Expected: 10


""" 
Problem: 1673  
Write a Python function called `get_last_element` that takes a list and returns the last element of the list.
"""
def get_last_element(my_list):
    return my_list[-1]

result = get_last_element([10, 20, 30])
print(result)  # Expected: 30


""" 
Problem: 1674  
Write a Python function called `get_middle_element` that takes a list and returns the middle element. If the list has even length, return the element at index length//2.
"""
def get_middle_element(my_list):
    return my_list[len(my_list) // 2]

result = get_middle_element([10, 20, 30, 40, 50])
print(result)  # Expected: 30


""" 
Problem: 1675  
Write a Python function called `remove_first_element` that takes a list and returns a new list with the first element removed.
"""
def remove_first_element(my_list):
    return my_list[1:]

result = remove_first_element([10, 20, 30])
print(result)  # Expected: [20, 30]


""" 
Problem: 1676  
Write a Python function called `remove_last_element` that takes a list and returns a new list with the last element removed.
"""
def remove_last_element(my_list):
    return my_list[:-1]

result = remove_last_element([10, 20, 30])
print(result)  # Expected: [10, 20]


""" 
Problem: 1677  
Write a Python function called `get_list_slice` that takes a list, start index, and end index, and returns a slice of the list from start to end.
"""
def get_list_slice(my_list, start, end):
    return my_list[start:end]

result = get_list_slice([10, 20, 30, 40, 50], 1, 4)
print(result)  # Expected: [20, 30, 40]


""" 
Problem: 1678  
Write a Python function called `combine_lists` that takes two lists and returns a new list containing all elements from both lists.
"""
def combine_lists(list1, list2):
    return list1 + list2

result = combine_lists([1, 2, 3], [4, 5, 6])
print(result)  # Expected: [1, 2, 3, 4, 5, 6]


""" 
Problem: 1679  
Write a Python function called `multiply_list` that takes a list of numbers and returns a new list where each number is multiplied by 2.
"""
def multiply_list(numbers):
    return [x * 2 for x in numbers]

result = multiply_list([1, 2, 3, 4])
print(result)  # Expected: [2, 4, 6, 8]


""" 
Problem: 1680  
Write a Python function called `add_one_to_all` that takes a list of numbers and returns a new list where 1 is added to each number.
"""
def add_one_to_all(numbers):
    return [x + 1 for x in numbers]

result = add_one_to_all([1, 2, 3, 4])
print(result)  # Expected: [2, 3, 4, 5]


""" 
Problem: 1681  
Write a Python program to print numbers from 1 to 10 using a for loop.
"""
for i in range(1, 11):
    print(i)  # Expected: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10


""" 
Problem: 1682  
Write a Python program to print all even numbers from 1 to 20 using a for loop.
"""
for i in range(1, 21):
    if i % 2 == 0:
        print(i)  # Expected: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20


""" 
Problem: 1683  
Write a Python program to print all odd numbers from 1 to 20 using a for loop.
"""
for i in range(1, 21):
    if i % 2 != 0:
        print(i)  # Expected: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19


""" 
Problem: 1684  
Write a Python program to print the multiplication table of 5 from 1 to 10 using a for loop.
"""
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")  # Expected: 5 x 1 = 5, 5 x 2 = 10, ..., 5 x 10 = 50


""" 
Problem: 1685  
Write a Python program to print each character of a string on a separate line using a for loop.
"""
text = "Hello"
for char in text:
    print(char)  # Expected: H, e, l, l, o (each on new line)


""" 
Problem: 1686  
Write a Python program to print each element of a list on a separate line using a for loop.
"""
my_list = [10, 20, 30]
for element in my_list:
    print(element)  # Expected: 10, 20, 30 (each on new line)


""" 
Problem: 1687  
Write a Python program to calculate the sum of numbers from 1 to 10 using a for loop.
"""
total = 0
for i in range(1, 11):
    total += i
print(total)  # Expected: 55


""" 
Problem: 1688  
Write a Python program to calculate the product of numbers from 1 to 5 using a for loop.
"""
product = 1
for i in range(1, 6):
    product *= i
print(product)  # Expected: 120


""" 
Problem: 1689  
Write a Python program to count from 10 down to 1 using a for loop.
"""
for i in range(10, 0, -1):
    print(i)  # Expected: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1


""" 
Problem: 1690  
Write a Python program to print numbers from 0 to 20 that are divisible by 3 using a for loop.
"""
for i in range(0, 21):
    if i % 3 == 0:
        print(i)  # Expected: 0, 3, 6, 9, 12, 15, 18


""" 
Problem: 1691  
Write a Python program using a while loop to print numbers from 1 to 5.
"""
i = 1
while i <= 5:
    print(i)
    i += 1  # Expected: 1, 2, 3, 4, 5


""" 
Problem: 1692  
Write a Python program using a while loop to calculate the sum of numbers from 1 to 10.
"""
total = 0
i = 1
while i <= 10:
    total += i
    i += 1
print(total)  # Expected: 55


""" 
Problem: 1693  
Write a Python program using a while loop to print all even numbers from 2 to 20.
"""
i = 2
while i <= 20:
    print(i)
    i += 2  # Expected: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20


""" 
Problem: 1694  
Write a Python program using a while loop to count down from 10 to 1.
"""
i = 10
while i >= 1:
    print(i)
    i -= 1  # Expected: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1


""" 
Problem: 1695  
Write a Python function called `check_greater` that takes two numbers and returns True if the first number is greater than the second, otherwise False.
"""
def check_greater(a, b):
    return a > b

print(check_greater(5, 3), check_greater(2, 4))  # Expected: True False


""" 
Problem: 1696  
Write a Python function called `check_less` that takes two numbers and returns True if the first number is less than the second, otherwise False.
"""
def check_less(a, b):
    return a < b

print(check_less(3, 5), check_less(5, 3))  # Expected: True False


""" 
Problem: 1697  
Write a Python function called `check_equal` that takes two values and returns True if they are equal, otherwise False.
"""
def check_equal(a, b):
    return a == b

print(check_equal(5, 5), check_equal(5, 3))  # Expected: True False


""" 
Problem: 1698  
Write a Python function called `check_not_equal` that takes two values and returns True if they are not equal, otherwise False.
"""
def check_not_equal(a, b):
    return a != b

print(check_not_equal(5, 3), check_not_equal(5, 5))  # Expected: True False


""" 
Problem: 1699  
Write a Python function called `check_greater_equal` that takes two numbers and returns True if the first number is greater than or equal to the second, otherwise False.
"""
def check_greater_equal(a, b):
    return a >= b

print(check_greater_equal(5, 5), check_greater_equal(3, 5))  # Expected: True False


""" 
Problem: 1700  
Write a Python function called `check_less_equal` that takes two numbers and returns True if the first number is less than or equal to the second, otherwise False.
"""
def check_less_equal(a, b):
    return a <= b

print(check_less_equal(3, 5), check_less_equal(5, 3))  # Expected: True False


""" 
Problem: 1701  
Write a Python function called `get_absolute_value` that takes a number and returns its absolute value.
"""
def get_absolute_value(number):
    return abs(number)

print(get_absolute_value(-5), get_absolute_value(5))  # Expected: 5 5


""" 
Problem: 1702  
Write a Python function called `round_number` that takes a number and returns it rounded to the nearest integer.
"""
def round_number(number):
    return round(number)

print(round_number(3.7), round_number(3.2))  # Expected: 4 3


""" 
Problem: 1703  
Write a Python function called `get_maximum` that takes three numbers and returns the largest one.
"""
def get_maximum(a, b, c):
    return max(a, b, c)

result = get_maximum(10, 5, 8)
print(result)  # Expected: 10


""" 
Problem: 1704  
Write a Python function called `get_minimum` that takes three numbers and returns the smallest one.
"""
def get_minimum(a, b, c):
    return min(a, b, c)

result = get_minimum(10, 5, 8)
print(result)  # Expected: 5


""" 
Problem: 1705  
Write a Python function called `check_divisible` that takes two numbers and returns True if the first number is divisible by the second, otherwise False.
"""
def check_divisible(a, b):
    return a % b == 0

print(check_divisible(10, 2), check_divisible(10, 3))  # Expected: True False


""" 
Problem: 1706  
Write a Python function called `convert_to_string` that takes a number and returns it as a string.
"""
def convert_to_string(number):
    return str(number)

result = convert_to_string(123)
print(result, type(result))  # Expected: 123 <class 'str'>


""" 
Problem: 1707  
Write a Python function called `convert_to_integer` that takes a string containing a number and returns it as an integer.
"""
def convert_to_integer(text):
    return int(text)

result = convert_to_integer("123")
print(result, type(result))  # Expected: 123 <class 'int'>


""" 
Problem: 1708  
Write a Python function called `convert_to_float` that takes a string containing a number and returns it as a float.
"""
def convert_to_float(text):
    return float(text)

result = convert_to_float("3.14")
print(result, type(result))  # Expected: 3.14 <class 'float'>


""" 
Problem: 1709  
Write a Python function called `get_type` that takes a value and returns its data type as a string.
"""
def get_type(value):
    return str(type(value).__name__)

print(get_type(5), get_type("hello"))  # Expected: int str


""" 
Problem: 1710  
Write a Python function called `check_is_integer` that takes a value and returns True if it is an integer, otherwise False.
"""
def check_is_integer(value):
    return isinstance(value, int)

print(check_is_integer(5), check_is_integer("5"))  # Expected: True False


""" 
Problem: 1711  
Write a Python function called `check_is_string` that takes a value and returns True if it is a string, otherwise False.
"""
def check_is_string(value):
    return isinstance(value, str)

print(check_is_string("hello"), check_is_string(5))  # Expected: True False


""" 
Problem: 1712  
Write a Python function called `check_is_list` that takes a value and returns True if it is a list, otherwise False.
"""
def check_is_list(value):
    return isinstance(value, list)

print(check_is_list([1, 2, 3]), check_is_list("hello"))  # Expected: True False


""" 
Problem: 1713  
Write a Python function called `format_greeting` that takes a name and returns a greeting message using an f-string: 'Hello, {name}!'.
"""
def format_greeting(name):
    return f"Hello, {name}!"

result = format_greeting("Alice")
print(result)  # Expected: Hello, Alice!


""" 
Problem: 1714  
Write a Python function called `format_age_message` that takes a name and age, and returns a message using an f-string: '{name} is {age} years old.'.
"""
def format_age_message(name, age):
    return f"{name} is {age} years old."

result = format_age_message("Bob", 25)
print(result)  # Expected: Bob is 25 years old.


""" 
Problem: 1715  
Write a Python function called `format_calculation` that takes two numbers and returns a formatted string showing their sum: '{num1} + {num2} = {sum}'.
"""
def format_calculation(num1, num2):
    return f"{num1} + {num2} = {num1 + num2}"

result = format_calculation(5, 3)
print(result)  # Expected: 5 + 3 = 8


""" 
Problem: 1716  
Write a Python function called `calculate_perimeter_rectangle` that takes length and width and returns the perimeter of a rectangle.
"""
def calculate_perimeter_rectangle(length, width):
    return 2 * (length + width)

result = calculate_perimeter_rectangle(5, 3)
print(result)  # Expected: 16


""" 
Problem: 1717  
Write a Python function called `calculate_perimeter_square` that takes the side length and returns the perimeter of a square.
"""
def calculate_perimeter_square(side):
    return 4 * side

result = calculate_perimeter_square(5)
print(result)  # Expected: 20


""" 
Problem: 1718  
Write a Python function called `calculate_circle_circumference` that takes the radius and returns the circumference of a circle (use 3.14 for pi).
"""
def calculate_circle_circumference(radius):
    return 2 * 3.14 * radius

result = calculate_circle_circumference(5)
print(result)  # Expected: 31.4


""" 
Problem: 1719  
Write a Python function called `convert_km_to_miles` that takes a distance in kilometers and returns it converted to miles (1 km = 0.621371 miles).
"""
def convert_km_to_miles(km):
    return km * 0.621371

result = convert_km_to_miles(10)
print(result)  # Expected: 6.21371


""" 
Problem: 1720  
Write a Python function called `convert_miles_to_km` that takes a distance in miles and returns it converted to kilometers.
"""
def convert_miles_to_km(miles):
    return miles / 0.621371

result = convert_miles_to_km(6.21371)
print(round(result, 2))  # Expected: 10.0


""" 
Problem: 1721  
Write a Python function called `convert_kg_to_pounds` that takes a weight in kilograms and returns it converted to pounds (1 kg = 2.20462 pounds).
"""
def convert_kg_to_pounds(kg):
    return kg * 2.20462

result = convert_kg_to_pounds(10)
print(result)  # Expected: 22.0462


""" 
Problem: 1722  
Write a Python function called `convert_pounds_to_kg` that takes a weight in pounds and returns it converted to kilograms.
"""
def convert_pounds_to_kg(pounds):
    return pounds / 2.20462

result = convert_pounds_to_kg(22.0462)
print(round(result, 2))  # Expected: 10.0


""" 
Problem: 1723  
Write a Python function called `check_vowel` that takes a character and returns True if it is a vowel (a, e, i, o, u), otherwise False.
"""
def check_vowel(char):
    return char.lower() in 'aeiou'

print(check_vowel('a'), check_vowel('b'))  # Expected: True False


""" 
Problem: 1724  
Write a Python function called `check_consonant` that takes a character and returns True if it is a consonant, otherwise False.
"""
def check_consonant(char):
    return char.isalpha() and char.lower() not in 'aeiou'

print(check_consonant('b'), check_consonant('a'))  # Expected: True False


""" 
Problem: 1725  
Write a Python function called `check_digit` that takes a character and returns True if it is a digit (0-9), otherwise False.
"""
def check_digit(char):
    return char.isdigit()

print(check_digit('5'), check_digit('a'))  # Expected: True False


""" 
Problem: 1726  
Write a Python function called `check_letter` that takes a character and returns True if it is a letter (a-z or A-Z), otherwise False.
"""
def check_letter(char):
    return char.isalpha()

print(check_letter('a'), check_letter('5'))  # Expected: True False


""" 
Problem: 1727  
Write a Python function called `check_uppercase` that takes a character and returns True if it is uppercase, otherwise False.
"""
def check_uppercase(char):
    return char.isupper()

print(check_uppercase('A'), check_uppercase('a'))  # Expected: True False


""" 
Problem: 1728  
Write a Python function called `check_lowercase` that takes a character and returns True if it is lowercase, otherwise False.
"""
def check_lowercase(char):
    return char.islower()

print(check_lowercase('a'), check_lowercase('A'))  # Expected: True False


""" 
Problem: 1729  
Write a Python function called `find_char_index` that takes a string and a character, and returns the index of the first occurrence of the character in the string, or -1 if not found.
"""
def find_char_index(text, char):
    return text.find(char)

print(find_char_index("Hello", "e"), find_char_index("Hello", "x"))  # Expected: 1 -1


""" 
Problem: 1730  
Write a Python function called `count_char_in_string` that takes a string and a character, and returns how many times the character appears in the string.
"""
def count_char_in_string(text, char):
    return text.count(char)

result = count_char_in_string("Hello", "l")
print(result)  # Expected: 2


""" 
Problem: 1731  
Write a Python function called `check_starts_with` that takes a string and a prefix, and returns True if the string starts with the prefix, otherwise False.
"""
def check_starts_with(text, prefix):
    return text.startswith(prefix)

print(check_starts_with("Hello", "He"), check_starts_with("Hello", "lo"))  # Expected: True False


""" 
Problem: 1732  
Write a Python function called `check_ends_with` that takes a string and a suffix, and returns True if the string ends with the suffix, otherwise False.
"""
def check_ends_with(text, suffix):
    return text.endswith(suffix)

print(check_ends_with("Hello", "lo"), check_ends_with("Hello", "He"))  # Expected: True False


""" 
Problem: 1733  
Write a Python function called `replace_char` that takes a string, old character, and new character, and returns a new string with all occurrences of old character replaced with new character.
"""
def replace_char(text, old_char, new_char):
    return text.replace(old_char, new_char)

result = replace_char("Hello", "l", "x")
print(result)  # Expected: Hexxo


""" 
Problem: 1734  
Write a Python function called `remove_char` that takes a string and a character, and returns a new string with all occurrences of that character removed.
"""
def remove_char(text, char):
    return text.replace(char, "")

result = remove_char("Hello", "l")
print(result)  # Expected: Heo


""" 
Problem: 1735  
Write a Python function called `get_substring` that takes a string, start index, and end index, and returns the substring from start to end (not including end).
"""
def get_substring(text, start, end):
    return text[start:end]

result = get_substring("Hello World", 0, 5)
print(result)  # Expected: Hello


""" 
Problem: 1736  
Write a Python function called `reverse_list` that takes a list and returns a new list with elements in reverse order.
"""
def reverse_list(my_list):
    return my_list[::-1]

result = reverse_list([1, 2, 3, 4])
print(result)  # Expected: [4, 3, 2, 1]


""" 
Problem: 1737  
Write a Python function called `get_list_length` that takes a list and returns the number of elements in the list.
"""
def get_list_length(my_list):
    return len(my_list)

result = get_list_length([1, 2, 3, 4, 5])
print(result)  # Expected: 5


""" 
Problem: 1738  
Write a Python function called `check_element_in_list` that takes a list and an element, and returns True if the element is in the list, otherwise False.
"""
def check_element_in_list(my_list, element):
    return element in my_list

print(check_element_in_list([1, 2, 3], 2), check_element_in_list([1, 2, 3], 5))  # Expected: True False


""" 
Problem: 1739  
Write a Python function called `get_element_count` that takes a list and an element, and returns how many times the element appears in the list.
"""
def get_element_count(my_list, element):
    return my_list.count(element)

result = get_element_count([1, 2, 2, 3, 2], 2)
print(result)  # Expected: 3


""" 
Problem: 1740  
Write a Python function called `get_element_index` that takes a list and an element, and returns the index of the first occurrence of the element, or -1 if not found.
"""
def get_element_index(my_list, element):
    if element in my_list:
        return my_list.index(element)
    return -1

print(get_element_index([10, 20, 30], 20), get_element_index([10, 20, 30], 40))  # Expected: 1 -1


""" 
Problem: 1741  
Write a Python function called `get_even_numbers` that takes a list of numbers and returns a new list containing only the even numbers.
"""
def get_even_numbers(numbers):
    return [x for x in numbers if x % 2 == 0]

result = get_even_numbers([1, 2, 3, 4, 5, 6])
print(result)  # Expected: [2, 4, 6]


""" 
Problem: 1742  
Write a Python function called `get_odd_numbers` that takes a list of numbers and returns a new list containing only the odd numbers.
"""
def get_odd_numbers(numbers):
    return [x for x in numbers if x % 2 != 0]

result = get_odd_numbers([1, 2, 3, 4, 5, 6])
print(result)  # Expected: [1, 3, 5]


""" 
Problem: 1743  
Write a Python function called `get_positive_numbers` that takes a list of numbers and returns a new list containing only the positive numbers.
"""
def get_positive_numbers(numbers):
    return [x for x in numbers if x > 0]

result = get_positive_numbers([-2, -1, 0, 1, 2, 3])
print(result)  # Expected: [1, 2, 3]


""" 
Problem: 1744  
Write a Python function called `get_negative_numbers` that takes a list of numbers and returns a new list containing only the negative numbers.
"""
def get_negative_numbers(numbers):
    return [x for x in numbers if x < 0]

result = get_negative_numbers([-2, -1, 0, 1, 2, 3])
print(result)  # Expected: [-2, -1]


""" 
Problem: 1745  
Write a Python function called `get_numbers_greater_than` that takes a list of numbers and a threshold, and returns a new list containing only numbers greater than the threshold.
"""
def get_numbers_greater_than(numbers, threshold):
    return [x for x in numbers if x > threshold]

result = get_numbers_greater_than([1, 5, 10, 15, 20], 10)
print(result)  # Expected: [15, 20]


""" 
Problem: 1746  
Write a Python function called `get_numbers_less_than` that takes a list of numbers and a threshold, and returns a new list containing only numbers less than the threshold.
"""
def get_numbers_less_than(numbers, threshold):
    return [x for x in numbers if x < threshold]

result = get_numbers_less_than([1, 5, 10, 15, 20], 10)
print(result)  # Expected: [1, 5]


""" 
Problem: 1747  
Write a Python function called `calculate_sum_of_list` that takes a list of numbers and returns the sum of all numbers in the list.
"""
def calculate_sum_of_list(numbers):
    return sum(numbers)

result = calculate_sum_of_list([1, 2, 3, 4, 5])
print(result)  # Expected: 15


""" 
Problem: 1748  
Write a Python function called `calculate_product_of_list` that takes a list of numbers and returns the product of all numbers in the list.
"""
def calculate_product_of_list(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

result = calculate_product_of_list([2, 3, 4])
print(result)  # Expected: 24


""" 
Problem: 1749  
Write a Python function called `get_average_of_list` that takes a list of numbers and returns the average (mean) of all numbers.
"""
def get_average_of_list(numbers):
    return sum(numbers) / len(numbers)

result = get_average_of_list([10, 20, 30, 40])
print(result)  # Expected: 25.0


""" 
Problem: 1750  
Write a Python function called `create_dictionary` that takes two lists (keys and values) and returns a dictionary created from them.
"""
def create_dictionary(keys, values):
    return dict(zip(keys, values))

result = create_dictionary(['a', 'b', 'c'], [1, 2, 3])
print(result)  # Expected: {'a': 1, 'b': 2, 'c': 3}


""" 
Problem: 1751  
Write a Python function called `get_dictionary_value` that takes a dictionary and a key, and returns the value associated with that key, or None if the key doesn't exist.
"""
def get_dictionary_value(d, key):
    return d.get(key)

print(get_dictionary_value({'a': 1, 'b': 2}, 'a'), get_dictionary_value({'a': 1, 'b': 2}, 'c'))  # Expected: 1 None


""" 
Problem: 1752  
Write a Python function called `get_dictionary_keys` that takes a dictionary and returns a list of all keys.
"""
def get_dictionary_keys(d):
    return list(d.keys())

result = get_dictionary_keys({'a': 1, 'b': 2, 'c': 3})
print(result)  # Expected: ['a', 'b', 'c']


""" 
Problem: 1753  
Write a Python function called `get_dictionary_values` that takes a dictionary and returns a list of all values.
"""
def get_dictionary_values(d):
    return list(d.values())

result = get_dictionary_values({'a': 1, 'b': 2, 'c': 3})
print(result)  # Expected: [1, 2, 3]


""" 
Problem: 1754  
Write a Python function called `check_key_in_dictionary` that takes a dictionary and a key, and returns True if the key exists in the dictionary, otherwise False.
"""
def check_key_in_dictionary(d, key):
    return key in d

print(check_key_in_dictionary({'a': 1}, 'a'), check_key_in_dictionary({'a': 1}, 'b'))  # Expected: True False


""" 
Problem: 1755  
Write a Python function called `add_to_dictionary` that takes a dictionary, a key, and a value, and returns a new dictionary with the key-value pair added.
"""
def add_to_dictionary(d, key, value):
    new_dict = d.copy()
    new_dict[key] = value
    return new_dict

result = add_to_dictionary({'a': 1}, 'b', 2)
print(result)  # Expected: {'a': 1, 'b': 2}


""" 
Problem: 1756  
Write a Python function called `create_tuple` that takes any number of arguments and returns a tuple containing those arguments.
"""
def create_tuple(*args):
    return tuple(args)

result = create_tuple(1, 2, 3, 4)
print(result)  # Expected: (1, 2, 3, 4)


""" 
Problem: 1757  
Write a Python function called `get_tuple_element` that takes a tuple and an index, and returns the element at that index.
"""
def get_tuple_element(my_tuple, index):
    return my_tuple[index]

result = get_tuple_element((10, 20, 30), 1)
print(result)  # Expected: 20


""" 
Problem: 1758  
Write a Python function called `unpack_tuple` that takes a tuple of two elements and returns them as separate values.
"""
def unpack_tuple(my_tuple):
    a, b = my_tuple
    return a, b

result = unpack_tuple((10, 20))
print(result)  # Expected: (10, 20)


""" 
Problem: 1759  
Write a Python function called `create_set` that takes a list and returns a set containing the unique elements from the list.
"""
def create_set(my_list):
    return set(my_list)

result = create_set([1, 2, 2, 3, 3, 3])
print(result)  # Expected: {1, 2, 3}


""" 
Problem: 1760  
Write a Python function called `check_element_in_set` that takes a set and an element, and returns True if the element is in the set, otherwise False.
"""
def check_element_in_set(my_set, element):
    return element in my_set

print(check_element_in_set({1, 2, 3}, 2), check_element_in_set({1, 2, 3}, 5))  # Expected: True False


""" 
Problem: 1761  
Write a Python function called `union_sets` that takes two sets and returns a new set containing all elements from both sets.
"""
def union_sets(set1, set2):
    return set1 | set2

result = union_sets({1, 2, 3}, {3, 4, 5})
print(result)  # Expected: {1, 2, 3, 4, 5}


""" 
Problem: 1762  
Write a Python function called `intersection_sets` that takes two sets and returns a new set containing only elements that are in both sets.
"""
def intersection_sets(set1, set2):
    return set1 & set2

result = intersection_sets({1, 2, 3}, {2, 3, 4})
print(result)  # Expected: {2, 3}


""" 
Problem: 1763  
Write a Python function called `difference_sets` that takes two sets and returns a new set containing elements that are in the first set but not in the second.
"""
def difference_sets(set1, set2):
    return set1 - set2

result = difference_sets({1, 2, 3}, {2, 3, 4})
print(result)  # Expected: {1}


""" 
Problem: 1764  
Write a Python function called `read_file_content` that takes a filename and returns the content of the file as a string.
"""
def read_file_content(filename):
    with open(filename, 'r') as f:
        return f.read()

# Note: This requires a file to exist. Demonstration only.
# content = read_file_content("example.txt")
print("Function defined: read_file_content(filename)")


""" 
Problem: 1765  
Write a Python function called `write_to_file` that takes a filename and content, and writes the content to the file.
"""
def write_to_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

# Note: This writes to a file. Demonstration only.
# write_to_file("example.txt", "Hello, World!")
print("Function defined: write_to_file(filename, content)")


""" 
Problem: 1766  
Write a Python function called `append_to_file` that takes a filename and content, and appends the content to the end of the file.
"""
def append_to_file(filename, content):
    with open(filename, 'a') as f:
        f.write(content)

# Note: This appends to a file. Demonstration only.
# append_to_file("example.txt", "New line")
print("Function defined: append_to_file(filename, content)")


""" 
Problem: 1767  
Write a Python function called `safe_divide` that takes two numbers and returns their division result. If division by zero occurs, return None instead of raising an error.
"""
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

print(safe_divide(10, 2), safe_divide(10, 0))  # Expected: 5.0 None


""" 
Problem: 1768  
Write a Python function called `safe_convert_to_int` that takes a string and tries to convert it to an integer. If conversion fails, return None.
"""
def safe_convert_to_int(text):
    try:
        return int(text)
    except ValueError:
        return None

print(safe_convert_to_int("123"), safe_convert_to_int("abc"))  # Expected: 123 None


""" 
Problem: 1769  
Write a Python function called `safe_get_list_element` that takes a list and an index, and returns the element at that index. If index is out of range, return None.
"""
def safe_get_list_element(my_list, index):
    try:
        return my_list[index]
    except IndexError:
        return None

print(safe_get_list_element([1, 2, 3], 1), safe_get_list_element([1, 2, 3], 10))  # Expected: 2 None


""" 
Problem: 1770  
Write a Python function called `join_strings` that takes a list of strings and a separator, and returns a single string with all strings joined by the separator.
"""
def join_strings(strings, separator):
    return separator.join(strings)

result = join_strings(["Hello", "World", "Python"], "-")
print(result)  # Expected: Hello-World-Python


""" 
Problem: 1771  
Write a Python function called `split_string` that takes a string and a delimiter, and returns a list of strings split by the delimiter.
"""
def split_string(text, delimiter):
    return text.split(delimiter)

result = split_string("Hello-World-Python", "-")
print(result)  # Expected: ['Hello', 'World', 'Python']


""" 
Problem: 1772  
Write a Python function called `strip_whitespace` that takes a string and returns a new string with leading and trailing whitespace removed.
"""
def strip_whitespace(text):
    return text.strip()

result = strip_whitespace("  Hello World  ")
print(result)  # Expected: Hello World


""" 
Problem: 1773  
Write a Python function called `capitalize_first_letter` that takes a string and returns a new string with only the first letter capitalized.
"""
def capitalize_first_letter(text):
    return text.capitalize()

result = capitalize_first_letter("hello world")
print(result)  # Expected: Hello world


""" 
Problem: 1774  
Write a Python function called `swap_case` that takes a string and returns a new string with uppercase letters converted to lowercase and vice versa.
"""
def swap_case(text):
    return text.swapcase()

result = swap_case("Hello World")
print(result)  # Expected: hELLO wORLD


""" 
Problem: 1775  
Write a Python function called `check_all_digits` that takes a string and returns True if all characters in the string are digits, otherwise False.
"""
def check_all_digits(text):
    return text.isdigit()

print(check_all_digits("12345"), check_all_digits("12a45"))  # Expected: True False


""" 
Problem: 1776  
Write a Python function called `check_all_letters` that takes a string and returns True if all characters in the string are letters, otherwise False.
"""
def check_all_letters(text):
    return text.isalpha()

print(check_all_letters("Hello"), check_all_letters("Hello123"))  # Expected: True False


""" 
Problem: 1777  
Write a Python function called `check_all_alphanumeric` that takes a string and returns True if all characters are letters or digits, otherwise False.
"""
def check_all_alphanumeric(text):
    return text.isalnum()

print(check_all_alphanumeric("Hello123"), check_all_alphanumeric("Hello 123"))  # Expected: True False


""" 
Problem: 1778  
Write a Python function called `get_squared_numbers` that takes a list of numbers and returns a new list with each number squared, using a list comprehension.
"""
def get_squared_numbers(numbers):
    return [x ** 2 for x in numbers]

result = get_squared_numbers([1, 2, 3, 4])
print(result)  # Expected: [1, 4, 9, 16]


""" 
Problem: 1779  
Write a Python function called `get_doubled_numbers` that takes a list of numbers and returns a new list with each number doubled, using a list comprehension.
"""
def get_doubled_numbers(numbers):
    return [x * 2 for x in numbers]

result = get_doubled_numbers([1, 2, 3, 4])
print(result)  # Expected: [2, 4, 6, 8]


""" 
Problem: 1780  
Write a Python function called `get_even_numbers_comprehension` that takes a list of numbers and returns a new list containing only even numbers, using a list comprehension.
"""
def get_even_numbers_comprehension(numbers):
    return [x for x in numbers if x % 2 == 0]

result = get_even_numbers_comprehension([1, 2, 3, 4, 5, 6])
print(result)  # Expected: [2, 4, 6]


""" 
Problem: 1781  
Write a Python function called `get_uppercase_strings` that takes a list of strings and returns a new list with all strings converted to uppercase, using a list comprehension.
"""
def get_uppercase_strings(strings):
    return [s.upper() for s in strings]

result = get_uppercase_strings(["hello", "world", "python"])
print(result)  # Expected: ['HELLO', 'WORLD', 'PYTHON']


""" 
Problem: 1782  
Write a Python function called `get_string_lengths` that takes a list of strings and returns a new list with the length of each string, using a list comprehension.
"""
def get_string_lengths(strings):
    return [len(s) for s in strings]

result = get_string_lengths(["hello", "world", "python"])
print(result)  # Expected: [5, 5, 6]


""" 
Problem: 1783  
Write a Python function called `print_number_pattern` that takes a number n and prints a pattern of numbers from 1 to n, where each line contains numbers from 1 to the line number.
"""
def print_number_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

print_number_pattern(5)  # Expected: 1, 1 2, 1 2 3, 1 2 3 4, 1 2 3 4 5


""" 
Problem: 1784  
Write a Python function called `print_star_pattern` that takes a number n and prints n lines of stars, where the first line has 1 star, second has 2 stars, and so on.
"""
def print_star_pattern(n):
    for i in range(1, n + 1):
        print("*" * i)

print_star_pattern(5)  # Expected: *, **, ***, ****, *****


""" 
Problem: 1785  
Write a Python function called `print_reverse_star_pattern` that takes a number n and prints n lines of stars in reverse order, where the first line has n stars, second has n-1 stars, and so on.
"""
def print_reverse_star_pattern(n):
    for i in range(n, 0, -1):
        print("*" * i)

print_reverse_star_pattern(5)  # Expected: *****, ****, ***, **, *


""" 
Problem: 1786  
Write a Python function called `print_number_square` that takes a number n and prints an n by n square of numbers from 1 to n*n.
"""
def print_number_square(n):
    for i in range(1, n * n + 1, n):
        row = [str(j) for j in range(i, i + n)]
        print(" ".join(row))

print_number_square(3)  # Expected: 1 2 3, 4 5 6, 7 8 9


""" 
Problem: 1787  
Write a Python function called `calculate_factorial` that takes a number n and returns the factorial of n (n! = n * (n-1) * ... * 1).
"""
def calculate_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

result = calculate_factorial(5)
print(result)  # Expected: 120


""" 
Problem: 1788  
Write a Python function called `calculate_sum_range` that takes two numbers start and end, and returns the sum of all numbers from start to end (inclusive).
"""
def calculate_sum_range(start, end):
    return sum(range(start, end + 1))

result = calculate_sum_range(1, 10)
print(result)  # Expected: 55


""" 
Problem: 1789  
Write a Python function called `calculate_product_range` that takes two numbers start and end, and returns the product of all numbers from start to end (inclusive).
"""
def calculate_product_range(start, end):
    product = 1
    for i in range(start, end + 1):
        product *= i
    return product

result = calculate_product_range(1, 5)
print(result)  # Expected: 120


""" 
Problem: 1790  
Write a Python function called `get_fibonacci_sequence` that takes a number n and returns a list containing the first n numbers of the Fibonacci sequence.
"""
def get_fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

result = get_fibonacci_sequence(8)
print(result)  # Expected: [0, 1, 1, 2, 3, 5, 8, 13]


""" 
Problem: 1791  
Write a Python function called `check_palindrome_number` that takes a number and returns True if the number is a palindrome (reads the same forwards and backwards), otherwise False.
"""
def check_palindrome_number(number):
    return str(number) == str(number)[::-1]

print(check_palindrome_number(121), check_palindrome_number(123))  # Expected: True False


""" 
Problem: 1792  
Write a Python function called `sum_of_digits` that takes a number and returns the sum of all its digits.
"""
def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

result = sum_of_digits(12345)
print(result)  # Expected: 15


""" 
Problem: 1793  
Write a Python function called `product_of_digits` that takes a number and returns the product of all its digits.
"""
def product_of_digits(number):
    product = 1
    for digit in str(number):
        product *= int(digit)
    return product

result = product_of_digits(234)
print(result)  # Expected: 24


""" 
Problem: 1794  
Write a Python function called `count_digits` that takes a number and returns the number of digits in the number.
"""
def count_digits(number):
    return len(str(number))

result = count_digits(12345)
print(result)  # Expected: 5


""" 
Problem: 1795  
Write a Python function called `reverse_number` that takes a number and returns the number with its digits reversed.
"""
def reverse_number(number):
    return int(str(number)[::-1])

result = reverse_number(12345)
print(result)  # Expected: 54321


""" 
Problem: 1796  
Write a Python function called `get_first_n_elements` that takes a list and a number n, and returns the first n elements of the list.
"""
def get_first_n_elements(my_list, n):
    return my_list[:n]

result = get_first_n_elements([1, 2, 3, 4, 5], 3)
print(result)  # Expected: [1, 2, 3]


""" 
Problem: 1797  
Write a Python function called `get_last_n_elements` that takes a list and a number n, and returns the last n elements of the list.
"""
def get_last_n_elements(my_list, n):
    return my_list[-n:]

result = get_last_n_elements([1, 2, 3, 4, 5], 3)
print(result)  # Expected: [3, 4, 5]


""" 
Problem: 1798  
Write a Python function called `remove_duplicates_from_list` that takes a list and returns a new list with duplicate elements removed, preserving order.
"""
def remove_duplicates_from_list(my_list):
    seen = []
    result = []
    for item in my_list:
        if item not in seen:
            seen.append(item)
            result.append(item)
    return result

result = remove_duplicates_from_list([1, 2, 2, 3, 3, 3, 4])
print(result)  # Expected: [1, 2, 3, 4]


""" 
Problem: 1799  
Write a Python function called `merge_two_lists` that takes two lists and returns a new list containing all elements from both lists, alternating between them.
"""
def merge_two_lists(list1, list2):
    result = []
    max_len = max(len(list1), len(list2))
    for i in range(max_len):
        if i < len(list1):
            result.append(list1[i])
        if i < len(list2):
            result.append(list2[i])
    return result

result = merge_two_lists([1, 2, 3], ['a', 'b', 'c'])
print(result)  # Expected: [1, 'a', 2, 'b', 3, 'c']


""" 
Problem: 1800  
Write a Python function called `get_common_elements` that takes two lists and returns a new list containing elements that appear in both lists.
"""
def get_common_elements(list1, list2):
    return [x for x in list1 if x in list2]

result = get_common_elements([1, 2, 3, 4], [3, 4, 5, 6])
print(result)  # Expected: [3, 4]


""" 
Problem: 1801  
Write a Python function called `get_unique_elements` that takes two lists and returns a new list containing elements that appear in only one of the lists.
"""
def get_unique_elements(list1, list2):
    result = []
    for item in list1:
        if item not in list2:
            result.append(item)
    for item in list2:
        if item not in list1:
            result.append(item)
    return result

result = get_unique_elements([1, 2, 3, 4], [3, 4, 5, 6])
print(result)  # Expected: [1, 2, 5, 6]


""" 
Problem: 1802  
Write a Python function called `sort_list_ascending` that takes a list of numbers and returns a new list sorted in ascending order.
"""
def sort_list_ascending(numbers):
    return sorted(numbers)

result = sort_list_ascending([3, 1, 4, 1, 5, 9, 2])
print(result)  # Expected: [1, 1, 2, 3, 4, 5, 9]


""" 
Problem: 1803  
Write a Python function called `sort_list_descending` that takes a list of numbers and returns a new list sorted in descending order.
"""
def sort_list_descending(numbers):
    return sorted(numbers, reverse=True)

result = sort_list_descending([3, 1, 4, 1, 5, 9, 2])
print(result)  # Expected: [9, 5, 4, 3, 2, 1, 1]


""" 
Problem: 1804  
Write a Python function called `get_second_largest` that takes a list of numbers and returns the second largest number in the list.
"""
def get_second_largest(numbers):
    unique_numbers = sorted(set(numbers), reverse=True)
    return unique_numbers[1] if len(unique_numbers) > 1 else None

result = get_second_largest([3, 1, 4, 1, 5, 9, 2])
print(result)  # Expected: 5


""" 
Problem: 1805  
Write a Python function called `get_second_smallest` that takes a list of numbers and returns the second smallest number in the list.
"""
def get_second_smallest(numbers):
    unique_numbers = sorted(set(numbers))
    return unique_numbers[1] if len(unique_numbers) > 1 else None

result = get_second_smallest([3, 1, 4, 1, 5, 9, 2])
print(result)  # Expected: 2


""" 
Problem: 1806  
Write a Python function called `check_sorted` that takes a list of numbers and returns True if the list is sorted in ascending order, otherwise False.
"""
def check_sorted(numbers):
    return numbers == sorted(numbers)

print(check_sorted([1, 2, 3, 4]), check_sorted([1, 3, 2, 4]))  # Expected: True False


""" 
Problem: 1807  
Write a Python function called `count_occurrences_in_list` that takes a list and returns a dictionary where keys are elements and values are their counts.
"""
def count_occurrences_in_list(my_list):
    counts = {}
    for item in my_list:
        counts[item] = counts.get(item, 0) + 1
    return counts

result = count_occurrences_in_list([1, 2, 2, 3, 3, 3])
print(result)  # Expected: {1: 1, 2: 2, 3: 3}


""" 
Problem: 1808  
Write a Python function called `get_most_frequent` that takes a list and returns the element that appears most frequently.
"""
def get_most_frequent(my_list):
    counts = {}
    for item in my_list:
        counts[item] = counts.get(item, 0) + 1
    return max(counts, key=counts.get)

result = get_most_frequent([1, 2, 2, 3, 3, 3, 3])
print(result)  # Expected: 3


""" 
Problem: 1809  
Write a Python function called `get_least_frequent` that takes a list and returns the element that appears least frequently.
"""
def get_least_frequent(my_list):
    counts = {}
    for item in my_list:
        counts[item] = counts.get(item, 0) + 1
    return min(counts, key=counts.get)

result = get_least_frequent([1, 1, 2, 2, 2, 3])
print(result)  # Expected: 3


""" 
Problem: 1810  
Write a Python function called `flatten_nested_list` that takes a list of lists and returns a single list containing all elements.
"""
def flatten_nested_list(nested_list):
    result = []
    for sublist in nested_list:
        result.extend(sublist)
    return result

result = flatten_nested_list([[1, 2], [3, 4], [5, 6]])
print(result)  # Expected: [1, 2, 3, 4, 5, 6]


""" 
Problem: 1811  
Write a Python function called `group_by_length` that takes a list of strings and returns a dictionary where keys are lengths and values are lists of strings with that length.
"""
def group_by_length(strings):
    groups = {}
    for s in strings:
        length = len(s)
        if length not in groups:
            groups[length] = []
        groups[length].append(s)
    return groups

result = group_by_length(["a", "ab", "abc", "ab", "abcd"])
print(result)  # Expected: {1: ['a'], 2: ['ab', 'ab'], 3: ['abc'], 4: ['abcd']}


""" 
Problem: 1812  
Write a Python function called `filter_by_length` that takes a list of strings and a minimum length, and returns a new list containing only strings with length greater than or equal to the minimum.
"""
def filter_by_length(strings, min_length):
    return [s for s in strings if len(s) >= min_length]

result = filter_by_length(["a", "ab", "abc", "abcd"], 3)
print(result)  # Expected: ['abc', 'abcd']


""" 
Problem: 1813  
Write a Python function called `get_longest_string` that takes a list of strings and returns the longest string.
"""
def get_longest_string(strings):
    return max(strings, key=len)

result = get_longest_string(["a", "ab", "abc", "abcd"])
print(result)  # Expected: abcd


""" 
Problem: 1814  
Write a Python function called `get_shortest_string` that takes a list of strings and returns the shortest string.
"""
def get_shortest_string(strings):
    return min(strings, key=len)

result = get_shortest_string(["a", "ab", "abc", "abcd"])
print(result)  # Expected: a


""" 
Problem: 1815  
Write a Python function called `capitalize_all_words` that takes a string of words separated by spaces and returns a new string with the first letter of each word capitalized.
"""
def capitalize_all_words(text):
    return " ".join(word.capitalize() for word in text.split())

result = capitalize_all_words("hello world python")
print(result)  # Expected: Hello World Python


""" 
Problem: 1816  
Write a Python function called `reverse_words` that takes a string of words separated by spaces and returns a new string with the order of words reversed.
"""
def reverse_words(text):
    words = text.split()
    return " ".join(reversed(words))

result = reverse_words("hello world python")
print(result)  # Expected: python world hello


""" 
Problem: 1817  
Write a Python function called `count_words` that takes a string and returns the number of words in the string (words are separated by spaces).
"""
def count_words(text):
    return len(text.split())

result = count_words("Hello World Python")
print(result)  # Expected: 3


""" 
Problem: 1818  
Write a Python function called `get_longest_word` that takes a string of words separated by spaces and returns the longest word.
"""
def get_longest_word(text):
    words = text.split()
    return max(words, key=len)

result = get_longest_word("hello world python programming")
print(result)  # Expected: programming


""" 
Problem: 1819  
Write a Python function called `get_shortest_word` that takes a string of words separated by spaces and returns the shortest word.
"""
def get_shortest_word(text):
    words = text.split()
    return min(words, key=len)

result = get_shortest_word("hello world python programming")
print(result)  # Expected: python


""" 
Problem: 1820  
Write a Python function called `remove_vowels_from_string` that takes a string and returns a new string with all vowels (a, e, i, o, u) removed.
"""
def remove_vowels_from_string(text):
    vowels = "aeiouAEIOU"
    return "".join(char for char in text if char not in vowels)

result = remove_vowels_from_string("Hello World")
print(result)  # Expected: Hll Wrld


""" 
Problem: 1821  
Write a Python function called `remove_consonants_from_string` that takes a string and returns a new string with all consonants removed, keeping only vowels and other characters.
"""
def remove_consonants_from_string(text):
    vowels = "aeiouAEIOU"
    return "".join(char for char in text if char in vowels or not char.isalpha())

result = remove_consonants_from_string("Hello World")
print(result)  # Expected: eo o


""" 
Problem: 1822  
Write a Python function called `count_vowels_in_string` that takes a string and returns the number of vowels (a, e, i, o, u) in the string.
"""
def count_vowels_in_string(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

result = count_vowels_in_string("Hello World")
print(result)  # Expected: 3


""" 
Problem: 1823  
Write a Python function called `count_consonants_in_string` that takes a string and returns the number of consonants in the string.
"""
def count_consonants_in_string(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char.isalpha() and char not in vowels)

result = count_consonants_in_string("Hello World")
print(result)  # Expected: 7


""" 
Problem: 1824  
Write a Python function called `swap_first_last_words` that takes a string of words separated by spaces and returns a new string with the first and last words swapped.
"""
def swap_first_last_words(text):
    words = text.split()
    if len(words) < 2:
        return text
    words[0], words[-1] = words[-1], words[0]
    return " ".join(words)

result = swap_first_last_words("Hello World Python")
print(result)  # Expected: Python World Hello


""" 
Problem: 1825  
Write a Python function called `get_middle_word` that takes a string of words separated by spaces and returns the middle word. If there are even number of words, return the word at index length//2.
"""
def get_middle_word(text):
    words = text.split()
    return words[len(words) // 2]

result = get_middle_word("Hello World Python Programming")
print(result)  # Expected: Python


""" 
Problem: 1826  
Write a Python function called `check_all_same` that takes a list and returns True if all elements in the list are the same, otherwise False.
"""
def check_all_same(my_list):
    return all(x == my_list[0] for x in my_list) if my_list else True

print(check_all_same([1, 1, 1]), check_all_same([1, 2, 1]))  # Expected: True False


""" 
Problem: 1827  
Write a Python function called `check_all_different` that takes a list and returns True if all elements in the list are different, otherwise False.
"""
def check_all_different(my_list):
    return len(my_list) == len(set(my_list))

print(check_all_different([1, 2, 3]), check_all_different([1, 2, 2]))  # Expected: True False


""" 
Problem: 1828  
Write a Python function called `get_range_list` that takes two numbers start and end, and returns a list containing all numbers from start to end (inclusive).
"""
def get_range_list(start, end):
    return list(range(start, end + 1))

result = get_range_list(1, 5)
print(result)  # Expected: [1, 2, 3, 4, 5]


""" 
Problem: 1829  
Write a Python function called `get_even_range` that takes two numbers start and end, and returns a list containing all even numbers from start to end (inclusive).
"""
def get_even_range(start, end):
    return [x for x in range(start, end + 1) if x % 2 == 0]

result = get_even_range(1, 10)
print(result)  # Expected: [2, 4, 6, 8, 10]


""" 
Problem: 1830  
Write a Python function called `get_odd_range` that takes two numbers start and end, and returns a list containing all odd numbers from start to end (inclusive).
"""
def get_odd_range(start, end):
    return [x for x in range(start, end + 1) if x % 2 != 0]

result = get_odd_range(1, 10)
print(result)  # Expected: [1, 3, 5, 7, 9]


""" 
Problem: 1831  
Write a Python function called `multiply_lists` that takes two lists of numbers of the same length and returns a new list where each element is the product of corresponding elements from both lists.
"""
def multiply_lists(list1, list2):
    return [a * b for a, b in zip(list1, list2)]

result = multiply_lists([1, 2, 3], [4, 5, 6])
print(result)  # Expected: [4, 10, 18]


""" 
Problem: 1832  
Write a Python function called `add_lists` that takes two lists of numbers of the same length and returns a new list where each element is the sum of corresponding elements from both lists.
"""
def add_lists(list1, list2):
    return [a + b for a, b in zip(list1, list2)]

result = add_lists([1, 2, 3], [4, 5, 6])
print(result)  # Expected: [5, 7, 9]


""" 
Problem: 1833  
Write a Python function called `subtract_lists` that takes two lists of numbers of the same length and returns a new list where each element is the difference of corresponding elements from both lists.
"""
def subtract_lists(list1, list2):
    return [a - b for a, b in zip(list1, list2)]

result = subtract_lists([10, 20, 30], [4, 5, 6])
print(result)  # Expected: [6, 15, 24]


""" 
Problem: 1834  
Write a Python function called `get_index_of_max` that takes a list of numbers and returns the index of the maximum value.
"""
def get_index_of_max(numbers):
    return numbers.index(max(numbers))

result = get_index_of_max([10, 5, 30, 20])
print(result)  # Expected: 2


""" 
Problem: 1835  
Write a Python function called `get_index_of_min` that takes a list of numbers and returns the index of the minimum value.
"""
def get_index_of_min(numbers):
    return numbers.index(min(numbers))

result = get_index_of_min([10, 5, 30, 20])
print(result)  # Expected: 1


""" 
Problem: 1836  
Write a Python function called `rotate_list_left` that takes a list and a number n, and returns a new list rotated n positions to the left.
"""
def rotate_list_left(my_list, n):
    n = n % len(my_list)
    return my_list[n:] + my_list[:n]

result = rotate_list_left([1, 2, 3, 4, 5], 2)
print(result)  # Expected: [3, 4, 5, 1, 2]


""" 
Problem: 1837  
Write a Python function called `rotate_list_right` that takes a list and a number n, and returns a new list rotated n positions to the right.
"""
def rotate_list_right(my_list, n):
    n = n % len(my_list)
    return my_list[-n:] + my_list[:-n]

result = rotate_list_right([1, 2, 3, 4, 5], 2)
print(result)  # Expected: [4, 5, 1, 2, 3]


""" 
Problem: 1838  
Write a Python function called `chunk_list` that takes a list and a number n, and returns a list of lists where each inner list contains n elements (except possibly the last one).
"""
def chunk_list(my_list, n):
    return [my_list[i:i+n] for i in range(0, len(my_list), n)]

result = chunk_list([1, 2, 3, 4, 5, 6, 7], 3)
print(result)  # Expected: [[1, 2, 3], [4, 5, 6], [7]]


""" 
Problem: 1839  
Write a Python function called `interleave_lists` that takes two lists and returns a new list with elements from both lists interleaved (alternating).
"""
def interleave_lists(list1, list2):
    result = []
    max_len = max(len(list1), len(list2))
    for i in range(max_len):
        if i < len(list1):
            result.append(list1[i])
        if i < len(list2):
            result.append(list2[i])
    return result

result = interleave_lists([1, 2, 3], ['a', 'b'])
print(result)  # Expected: [1, 'a', 2, 'b', 3]


""" 
Problem: 1840  
Write a Python function called `zip_lists` that takes two lists and returns a list of tuples, where each tuple contains corresponding elements from both lists.
"""
def zip_lists(list1, list2):
    return list(zip(list1, list2))

result = zip_lists([1, 2, 3], ['a', 'b', 'c'])
print(result)  # Expected: [(1, 'a'), (2, 'b'), (3, 'c')]


""" 
Problem: 1841  
Write a Python function called `unzip_list` that takes a list of tuples and returns two lists: one with all first elements and one with all second elements.
"""
def unzip_list(tuples_list):
    if not tuples_list:
        return [], []
    first_elements = [t[0] for t in tuples_list]
    second_elements = [t[1] for t in tuples_list]
    return first_elements, second_elements

result = unzip_list([(1, 'a'), (2, 'b'), (3, 'c')])
print(result)  # Expected: ([1, 2, 3], ['a', 'b', 'c'])


""" 
Problem: 1842  
Write a Python function called `count_uppercase_letters` that takes a string and returns the number of uppercase letters in the string.
"""
def count_uppercase_letters(text):
    return sum(1 for char in text if char.isupper())

result = count_uppercase_letters("Hello World")
print(result)  # Expected: 2


""" 
Problem: 1843  
Write a Python function called `count_lowercase_letters` that takes a string and returns the number of lowercase letters in the string.
"""
def count_lowercase_letters(text):
    return sum(1 for char in text if char.islower())

result = count_lowercase_letters("Hello World")
print(result)  # Expected: 8


""" 
Problem: 1844  
Write a Python function called `swap_uppercase_lowercase` that takes a string and returns a new string where uppercase letters become lowercase and lowercase letters become uppercase.
"""
def swap_uppercase_lowercase(text):
    return text.swapcase()

result = swap_uppercase_lowercase("Hello World")
print(result)  # Expected: hELLO wORLD


""" 
Problem: 1845  
Write a Python function called `remove_numbers_from_string` that takes a string and returns a new string with all digits removed.
"""
def remove_numbers_from_string(text):
    return "".join(char for char in text if not char.isdigit())

result = remove_numbers_from_string("Hello123World456")
print(result)  # Expected: HelloWorld


""" 
Problem: 1846  
Write a Python function called `remove_letters_from_string` that takes a string and returns a new string with all letters removed, keeping only digits and other characters.
"""
def remove_letters_from_string(text):
    return "".join(char for char in text if not char.isalpha())

result = remove_letters_from_string("Hello123World456!")
print(result)  # Expected: 123456!


""" 
Problem: 1847  
Write a Python function called `extract_numbers_from_string` that takes a string and returns a list of all numbers found in the string (as strings).
"""
def extract_numbers_from_string(text):
    return [char for char in text if char.isdigit()]

result = extract_numbers_from_string("Hello123World456")
print(result)  # Expected: ['1', '2', '3', '4', '5', '6']


""" 
Problem: 1848  
Write a Python function called `extract_letters_from_string` that takes a string and returns a list of all letters found in the string.
"""
def extract_letters_from_string(text):
    return [char for char in text if char.isalpha()]

result = extract_letters_from_string("Hello123World456")
print(result)  # Expected: ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']


""" 
Problem: 1849  
Write a Python function called `format_phone_number` that takes a string of 10 digits and returns it formatted as (XXX) XXX-XXXX.
"""
def format_phone_number(digits):
    return f"({digits[0:3]}) {digits[3:6]}-{digits[6:10]}"

result = format_phone_number("1234567890")
print(result)  # Expected: (123) 456-7890


""" 
Problem: 1850  
Write a Python function called `calculate_volume_box` that takes length, width, and height as parameters and returns the volume of a rectangular box.
"""
def calculate_volume_box(length, width, height):
    return length * width * height

result = calculate_volume_box(5, 3, 4)
print(result)  # Expected: 60


""" 
Problem: 1851  
Write a Python function called `check_triangle_valid` that takes three numbers representing side lengths and returns True if they can form a valid triangle, otherwise False.
"""
def check_triangle_valid(a, b, c):
    return a + b > c and a + c > b and b + c > a

print(check_triangle_valid(3, 4, 5), check_triangle_valid(1, 2, 5))  # Expected: True False


""" 
Problem: 1852  
Write a Python function called `find_grade` that takes a score and returns a letter grade: 'A' for 90+, 'B' for 80-89, 'C' for 70-79, 'D' for 60-69, 'F' for below 60.
"""
def find_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

print(find_grade(95), find_grade(75), find_grade(55))  # Expected: A C F


""" 
Problem: 1853  
Write a Python function called `get_season` that takes a month number (1-12) and returns the season: 'Winter' for 12,1,2; 'Spring' for 3,4,5; 'Summer' for 6,7,8; 'Fall' for 9,10,11.
"""
def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Fall'

print(get_season(1), get_season(4), get_season(7), get_season(10))  # Expected: Winter Spring Summer Fall


""" 
Problem: 1854  
Write a Python function called `calculate_discount` that takes a price and discount percentage, and returns the final price after applying the discount.
"""
def calculate_discount(price, discount_percent):
    return price * (1 - discount_percent / 100)

result = calculate_discount(100, 20)
print(result)  # Expected: 80.0


""" 
Problem: 1855  
Write a Python function called `calculate_tip` that takes a bill amount and tip percentage, and returns both the tip amount and total amount as a tuple.
"""
def calculate_tip(bill_amount, tip_percent):
    tip = bill_amount * (tip_percent / 100)
    total = bill_amount + tip
    return (tip, total)

result = calculate_tip(100, 15)
print(result)  # Expected: (15.0, 115.0)


""" 
Problem: 1856  
Write a Python function called `swap_two_elements` that takes a list and two indices, and returns a new list with the elements at those indices swapped.
"""
def swap_two_elements(my_list, index1, index2):
    new_list = my_list.copy()
    new_list[index1], new_list[index2] = new_list[index2], new_list[index1]
    return new_list

result = swap_two_elements([10, 20, 30, 40], 0, 3)
print(result)  # Expected: [40, 20, 30, 10]


""" 
Problem: 1857  
Write a Python function called `insert_at_index` that takes a list, an index, and a value, and returns a new list with the value inserted at that index.
"""
def insert_at_index(my_list, index, value):
    new_list = my_list.copy()
    new_list.insert(index, value)
    return new_list

result = insert_at_index([1, 2, 3, 4], 2, 99)
print(result)  # Expected: [1, 2, 99, 3, 4]


""" 
Problem: 1858  
Write a Python function called `remove_at_index` that takes a list and an index, and returns a new list with the element at that index removed.
"""
def remove_at_index(my_list, index):
    new_list = my_list.copy()
    new_list.pop(index)
    return new_list

result = remove_at_index([10, 20, 30, 40], 1)
print(result)  # Expected: [10, 30, 40]


""" 
Problem: 1859  
Write a Python function called `count_vowels_and_consonants` that takes a string and returns a tuple containing the count of vowels and consonants.
"""
def count_vowels_and_consonants(text):
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in text if char in vowels)
    consonant_count = sum(1 for char in text if char.isalpha() and char not in vowels)
    return (vowel_count, consonant_count)

result = count_vowels_and_consonants("Hello World")
print(result)  # Expected: (3, 7)


""" 
Problem: 1860  
Write a Python function called `get_min_max` that takes a list of numbers and returns a tuple containing the minimum and maximum values.
"""
def get_min_max(numbers):
    return (min(numbers), max(numbers))

result = get_min_max([10, 5, 30, 20, 15])
print(result)  # Expected: (5, 30)


""" 
Problem: 1861  
Write a Python function called `check_all_conditions` that takes a number and returns True if it is positive, even, and divisible by 3, otherwise False.
"""
def check_all_conditions(number):
    return number > 0 and number % 2 == 0 and number % 3 == 0

print(check_all_conditions(6), check_all_conditions(5))  # Expected: True False


""" 
Problem: 1862  
Write a Python function called `format_full_name` that takes first name, middle name, and last name, and returns a formatted full name string.
"""
def format_full_name(first, middle, last):
    return f"{first} {middle} {last}"

result = format_full_name("John", "Michael", "Doe")
print(result)  # Expected: John Michael Doe


""" 
Problem: 1863  
Write a Python function called `calculate_bmi` that takes weight in kg and height in meters, and returns the BMI value rounded to one decimal place.
"""
def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)

result = calculate_bmi(70, 1.75)
print(result)  # Expected: 22.9


""" 
Problem: 1864  
Write a Python function called `check_bmi_category` that takes weight and height, calculates BMI, and returns the category: 'Underweight' (<18.5), 'Normal' (18.5-24.9), 'Overweight' (25-29.9), 'Obese' (30+).
"""
def check_bmi_category(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    if bmi < 18.5:
        return 'Underweight'
    elif bmi < 25:
        return 'Normal'
    elif bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'

result = check_bmi_category(70, 1.75)
print(result)  # Expected: Normal


""" 
Problem: 1865  
Write a Python function called `find_common_elements_three` that takes three lists and returns a list of elements that appear in all three lists.
"""
def find_common_elements_three(list1, list2, list3):
    return [x for x in list1 if x in list2 and x in list3]

result = find_common_elements_three([1, 2, 3], [2, 3, 4], [3, 4, 5])
print(result)  # Expected: [3]


""" 
Problem: 1866  
Write a Python function called `merge_three_lists` that takes three lists and returns a new list containing all elements from all three lists.
"""
def merge_three_lists(list1, list2, list3):
    return list1 + list2 + list3

result = merge_three_lists([1, 2], [3, 4], [5, 6])
print(result)  # Expected: [1, 2, 3, 4, 5, 6]


""" 
Problem: 1867  
Write a Python function called `get_elements_at_indices` that takes a list and a list of indices, and returns a list of elements at those indices.
"""
def get_elements_at_indices(my_list, indices):
    return [my_list[i] for i in indices]

result = get_elements_at_indices([10, 20, 30, 40, 50], [0, 2, 4])
print(result)  # Expected: [10, 30, 50]


""" 
Problem: 1868  
Write a Python function called `replace_multiple_chars` that takes a string and a dictionary mapping old characters to new characters, and returns a string with all replacements made.
"""
def replace_multiple_chars(text, replacements):
    result = text
    for old_char, new_char in replacements.items():
        result = result.replace(old_char, new_char)
    return result

result = replace_multiple_chars("Hello World", {'H': 'J', 'o': 'a'})
print(result)  # Expected: Jella Warld


""" 
Problem: 1869  
Write a Python function called `count_words_by_length` that takes a string and returns a dictionary where keys are word lengths and values are counts of words with that length.
"""
def count_words_by_length(text):
    words = text.split()
    counts = {}
    for word in words:
        length = len(word)
        counts[length] = counts.get(length, 0) + 1
    return counts

result = count_words_by_length("hello world python programming")
print(result)  # Expected: {5: 2, 6: 2, 11: 1}


""" 
Problem: 1870  
Write a Python function called `filter_and_transform` that takes a list of numbers and returns a new list containing only even numbers, each multiplied by 2.
"""
def filter_and_transform(numbers):
    return [x * 2 for x in numbers if x % 2 == 0]

result = filter_and_transform([1, 2, 3, 4, 5, 6])
print(result)  # Expected: [4, 8, 12]


""" 
Problem: 1871  
Write a Python function called `get_strings_starting_with` that takes a list of strings and a prefix, and returns a new list containing only strings that start with that prefix.
"""
def get_strings_starting_with(strings, prefix):
    return [s for s in strings if s.startswith(prefix)]

result = get_strings_starting_with(["apple", "banana", "apricot", "cherry"], "ap")
print(result)  # Expected: ['apple', 'apricot']


""" 
Problem: 1872  
Write a Python function called `get_strings_ending_with` that takes a list of strings and a suffix, and returns a new list containing only strings that end with that suffix.
"""
def get_strings_ending_with(strings, suffix):
    return [s for s in strings if s.endswith(suffix)]

result = get_strings_ending_with(["running", "walking", "jumping", "swimming"], "ing")
print(result)  # Expected: ['running', 'walking', 'jumping', 'swimming']


""" 
Problem: 1873  
Write a Python function called `calculate_total_cost` that takes a list of prices and a tax rate percentage, and returns the total cost including tax.
"""
def calculate_total_cost(prices, tax_rate):
    subtotal = sum(prices)
    tax = subtotal * (tax_rate / 100)
    return subtotal + tax

result = calculate_total_cost([10, 20, 30], 10)
print(result)  # Expected: 66.0


""" 
Problem: 1874  
Write a Python function called `find_all_indices` that takes a list and an element, and returns a list of all indices where that element appears.
"""
def find_all_indices(my_list, element):
    return [i for i, x in enumerate(my_list) if x == element]

result = find_all_indices([10, 20, 10, 30, 10], 10)
print(result)  # Expected: [0, 2, 4]


""" 
Problem: 1875  
Write a Python function called `split_into_chunks` that takes a list and a chunk size, and returns a list of lists where each inner list has at most chunk_size elements.
"""
def split_into_chunks(my_list, chunk_size):
    return [my_list[i:i+chunk_size] for i in range(0, len(my_list), chunk_size)]

result = split_into_chunks([1, 2, 3, 4, 5, 6, 7], 3)
print(result)  # Expected: [[1, 2, 3], [4, 5, 6], [7]]


""" 
Problem: 1876  
Write a Python function called `remove_multiple_elements` that takes a list and a list of elements to remove, and returns a new list with all those elements removed.
"""
def remove_multiple_elements(my_list, elements_to_remove):
    return [x for x in my_list if x not in elements_to_remove]

result = remove_multiple_elements([1, 2, 3, 4, 5, 6], [2, 4, 6])
print(result)  # Expected: [1, 3, 5]


""" 
Problem: 1877  
Write a Python function called `count_occurrences_multiple` that takes a list and a list of elements, and returns a dictionary with counts of each element.
"""
def count_occurrences_multiple(my_list, elements):
    return {elem: my_list.count(elem) for elem in elements}

result = count_occurrences_multiple([1, 2, 2, 3, 3, 3, 4], [2, 3])
print(result)  # Expected: {2: 2, 3: 3}


""" 
Problem: 1878  
Write a Python function called `get_unique_elements_three` that takes three lists and returns a list of elements that appear in exactly one of the three lists.
"""
def get_unique_elements_three(list1, list2, list3):
    all_elements = list1 + list2 + list3
    result = []
    for elem in all_elements:
        count = list1.count(elem) + list2.count(elem) + list3.count(elem)
        if count == 1:
            result.append(elem)
    return list(set(result))

result = get_unique_elements_three([1, 2, 3], [2, 3, 4], [3, 4, 5])
print(sorted(result))  # Expected: [1, 5]


""" 
Problem: 1879  
Write a Python function called `sort_by_multiple_criteria` that takes a list of tuples (name, age, score) and returns the list sorted first by age, then by score.
"""
def sort_by_multiple_criteria(people):
    return sorted(people, key=lambda x: (x[1], x[2]))

result = sort_by_multiple_criteria([("Alice", 25, 85), ("Bob", 25, 90), ("Charlie", 30, 80)])
print(result)  # Expected: [('Alice', 25, 85), ('Bob', 25, 90), ('Charlie', 30, 80)]


""" 
Problem: 1880  
Write a Python function called `calculate_statistics` that takes a list of numbers and returns a dictionary with 'sum', 'average', 'min', and 'max' keys.
"""
def calculate_statistics(numbers):
    return {
        'sum': sum(numbers),
        'average': sum(numbers) / len(numbers),
        'min': min(numbers),
        'max': max(numbers)
    }

result = calculate_statistics([10, 20, 30, 40])
print(result)  # Expected: {'sum': 100, 'average': 25.0, 'min': 10, 'max': 40}


""" 
Problem: 1881  
Write a Python function called `extract_numbers_from_string` that takes a string and returns a list of all numbers found in the string (as integers).
"""
def extract_numbers_from_string(text):
    import re
    return [int(match) for match in re.findall(r'\d+', text)]

result = extract_numbers_from_string("I have 3 cats and 2 dogs")
print(result)  # Expected: [3, 2]


""" 
Problem: 1882  
Write a Python function called `format_address` that takes street, city, state, and zipcode, and returns a formatted address string on separate lines.
"""
def format_address(street, city, state, zipcode):
    return f"{street}\n{city}, {state} {zipcode}"

result = format_address("123 Main St", "New York", "NY", "10001")
print(result)  # Expected: 123 Main St\nNew York, NY 10001


""" 
Problem: 1883  
Write a Python function called `check_password_strength` that takes a password string and returns True if it has at least 8 characters, contains both letters and digits, otherwise False.
"""
def check_password_strength(password):
    return len(password) >= 8 and any(c.isalpha() for c in password) and any(c.isdigit() for c in password)

print(check_password_strength("Password123"), check_password_strength("weak"))  # Expected: True False


""" 
Problem: 1884  
Write a Python function called `get_words_by_length_range` that takes a string and min/max length, and returns a list of words within that length range.
"""
def get_words_by_length_range(text, min_length, max_length):
    words = text.split()
    return [word for word in words if min_length <= len(word) <= max_length]

result = get_words_by_length_range("hello world python programming", 5, 6)
print(result)  # Expected: ['hello', 'world', 'python']


""" 
Problem: 1885  
Write a Python function called `calculate_compound_interest` that takes principal, rate, time, and compounding frequency, and returns the final amount.
"""
def calculate_compound_interest(principal, rate, time, frequency):
    return principal * (1 + rate / (100 * frequency)) ** (frequency * time)

result = calculate_compound_interest(1000, 5, 2, 12)
print(round(result, 2))  # Expected: 1104.94


""" 
Problem: 1886  
Write a Python function called `find_duplicate_elements` that takes a list and returns a list of elements that appear more than once.
"""
def find_duplicate_elements(my_list):
    seen = set()
    duplicates = set()
    for item in my_list:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return list(duplicates)

result = find_duplicate_elements([1, 2, 2, 3, 3, 3, 4])
print(sorted(result))  # Expected: [2, 3]


""" 
Problem: 1887  
Write a Python function called `group_by_first_letter` that takes a list of strings and returns a dictionary where keys are first letters and values are lists of strings starting with that letter.
"""
def group_by_first_letter(strings):
    groups = {}
    for s in strings:
        first_letter = s[0].lower()
        if first_letter not in groups:
            groups[first_letter] = []
        groups[first_letter].append(s)
    return groups

result = group_by_first_letter(["apple", "banana", "apricot", "cherry"])
print(result)  # Expected: {'a': ['apple', 'apricot'], 'b': ['banana'], 'c': ['cherry']}


""" 
Problem: 1888  
Write a Python function called `calculate_distance` that takes two points (x1, y1) and (x2, y2) and returns the Euclidean distance between them.
"""
import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

result = calculate_distance(0, 0, 3, 4)
print(result)  # Expected: 5.0


""" 
Problem: 1889  
Write a Python function called `check_in_range` that takes a number and a range (min, max), and returns True if the number is within the range (inclusive), otherwise False.
"""
def check_in_range(number, min_val, max_val):
    return min_val <= number <= max_val

print(check_in_range(5, 1, 10), check_in_range(15, 1, 10))  # Expected: True False


""" 
Problem: 1890  
Write a Python function called `get_divisors` that takes a number and returns a list of all divisors of that number.
"""
def get_divisors(number):
    return [i for i in range(1, number + 1) if number % i == 0]

result = get_divisors(12)
print(result)  # Expected: [1, 2, 3, 4, 6, 12]


""" 
Problem: 1891  
Write a Python function called `check_perfect_square` that takes a number and returns True if it is a perfect square, otherwise False.
"""
def check_perfect_square(number):
    import math
    root = math.sqrt(number)
    return root == int(root)

print(check_perfect_square(16), check_perfect_square(15))  # Expected: True False


""" 
Problem: 1892  
Write a Python function called `format_time` that takes hours, minutes, and seconds, and returns a formatted time string as HH:MM:SS.
"""
def format_time(hours, minutes, seconds):
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

result = format_time(9, 5, 3)
print(result)  # Expected: 09:05:03


""" 
Problem: 1893  
Write a Python function called `calculate_age` that takes birth year, birth month, and birth day, and returns the age in years (assuming current date is 2024-01-01).
"""
def calculate_age(birth_year, birth_month, birth_day):
    current_year = 2024
    current_month = 1
    current_day = 1
    age = current_year - birth_year
    if (current_month, current_day) < (birth_month, birth_day):
        age -= 1
    return age

result = calculate_age(2000, 6, 15)
print(result)  # Expected: 23


""" 
Problem: 1894  
Write a Python function called `get_middle_elements` that takes a list and returns a new list containing elements from index 1 to -1 (excluding first and last).
"""
def get_middle_elements(my_list):
    return my_list[1:-1]

result = get_middle_elements([10, 20, 30, 40, 50])
print(result)  # Expected: [20, 30, 40]


""" 
Problem: 1895  
Write a Python function called `swap_adjacent_elements` that takes a list and returns a new list with adjacent elements swapped (1st with 2nd, 3rd with 4th, etc.).
"""
def swap_adjacent_elements(my_list):
    new_list = my_list.copy()
    for i in range(0, len(new_list) - 1, 2):
        new_list[i], new_list[i + 1] = new_list[i + 1], new_list[i]
    return new_list

result = swap_adjacent_elements([1, 2, 3, 4, 5, 6])
print(result)  # Expected: [2, 1, 4, 3, 6, 5]


""" 
Problem: 1896  
Write a Python function called `get_every_nth_element` that takes a list and a number n, and returns a list containing every nth element starting from index 0.
"""
def get_every_nth_element(my_list, n):
    return my_list[::n]

result = get_every_nth_element([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
print(result)  # Expected: [0, 3, 6, 9]


""" 
Problem: 1897  
Write a Python function called `count_uppercase_lowercase` that takes a string and returns a dictionary with 'uppercase' and 'lowercase' keys containing their counts.
"""
def count_uppercase_lowercase(text):
    return {
        'uppercase': sum(1 for c in text if c.isupper()),
        'lowercase': sum(1 for c in text if c.islower())
    }

result = count_uppercase_lowercase("Hello World")
print(result)  # Expected: {'uppercase': 2, 'lowercase': 8}


""" 
Problem: 1898  
Write a Python function called `remove_duplicates_preserve_order` that takes a list and returns a new list with duplicates removed while preserving the order of first occurrence.
"""
def remove_duplicates_preserve_order(my_list):
    seen = set()
    result = []
    for item in my_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

result = remove_duplicates_preserve_order([1, 2, 2, 3, 3, 3, 4, 2])
print(result)  # Expected: [1, 2, 3, 4]


""" 
Problem: 1899  
Write a Python function called `get_intersection_three_lists` that takes three lists and returns a list of elements that appear in all three lists.
"""
def get_intersection_three_lists(list1, list2, list3):
    return [x for x in list1 if x in list2 and x in list3]

result = get_intersection_three_lists([1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6])
print(result)  # Expected: [3, 4]


""" 
Problem: 1900  
Write a Python function called `calculate_percentage` that takes a part and a whole, and returns the percentage as a float rounded to 2 decimal places.
"""
def calculate_percentage(part, whole):
    return round((part / whole) * 100, 2)

result = calculate_percentage(25, 100)
print(result)  # Expected: 25.0


""" 
Problem: 1901  
Write a Python function called `find_largest_three` that takes a list of numbers and returns a list containing the three largest numbers.
"""
def find_largest_three(numbers):
    return sorted(numbers, reverse=True)[:3]

result = find_largest_three([10, 5, 30, 20, 15, 25])
print(result)  # Expected: [30, 25, 20]


""" 
Problem: 1902  
Write a Python function called `find_smallest_three` that takes a list of numbers and returns a list containing the three smallest numbers.
"""
def find_smallest_three(numbers):
    return sorted(numbers)[:3]

result = find_smallest_three([10, 5, 30, 20, 15, 25])
print(result)  # Expected: [5, 10, 15]


""" 
Problem: 1903  
Write a Python function called `check_palindrome_and_length` that takes a string and returns a tuple containing True/False for palindrome and the string length.
"""
def check_palindrome_and_length(text):
    is_palindrome = text == text[::-1]
    length = len(text)
    return (is_palindrome, length)

result = check_palindrome_and_length("racecar")
print(result)  # Expected: (True, 7)


""" 
Problem: 1904  
Write a Python function called `get_words_starting_with_vowel` that takes a string and returns a list of words that start with a vowel.
"""
def get_words_starting_with_vowel(text):
    vowels = "aeiouAEIOU"
    words = text.split()
    return [word for word in words if word[0] in vowels]

result = get_words_starting_with_vowel("apple orange banana cherry")
print(result)  # Expected: ['apple', 'orange']


""" 
Problem: 1905  
Write a Python function called `get_words_ending_with_consonant` that takes a string and returns a list of words that end with a consonant.
"""
def get_words_ending_with_consonant(text):
    vowels = "aeiouAEIOU"
    words = text.split()
    return [word for word in words if word[-1] not in vowels and word[-1].isalpha()]

result = get_words_ending_with_consonant("hello world python")
print(result)  # Expected: ['hello', 'world', 'python']


""" 
Problem: 1906  
Write a Python function called `calculate_area_perimeter` that takes length and width, and returns a tuple containing area and perimeter of a rectangle.
"""
def calculate_area_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return (area, perimeter)

result = calculate_area_perimeter(5, 3)
print(result)  # Expected: (15, 16)


""" 
Problem: 1907  
Write a Python function called `format_currency` that takes a number and returns it formatted as currency with dollar sign and two decimal places.
"""
def format_currency(amount):
    return f"${amount:.2f}"

result = format_currency(1234.5)
print(result)  # Expected: $1234.50


""" 
Problem: 1908  
Write a Python function called `get_even_indices` that takes a list and returns a list containing elements at even indices (0, 2, 4, ...).
"""
def get_even_indices(my_list):
    return [my_list[i] for i in range(0, len(my_list), 2)]

result = get_even_indices([10, 20, 30, 40, 50])
print(result)  # Expected: [10, 30, 50]


""" 
Problem: 1909  
Write a Python function called `get_odd_indices` that takes a list and returns a list containing elements at odd indices (1, 3, 5, ...).
"""
def get_odd_indices(my_list):
    return [my_list[i] for i in range(1, len(my_list), 2)]

result = get_odd_indices([10, 20, 30, 40, 50])
print(result)  # Expected: [20, 40]


""" 
Problem: 1910  
Write a Python function called `multiply_corresponding` that takes two lists of numbers and returns a new list where each element is the product of corresponding elements.
"""
def multiply_corresponding(list1, list2):
    return [a * b for a, b in zip(list1, list2)]

result = multiply_corresponding([2, 3, 4], [5, 6, 7])
print(result)  # Expected: [10, 18, 28]


""" 
Problem: 1911  
Write a Python function called `divide_corresponding` that takes two lists of numbers and returns a new list where each element is the division of corresponding elements (handle division by zero by returning None).
"""
def divide_corresponding(list1, list2):
    result = []
    for a, b in zip(list1, list2):
        if b == 0:
            result.append(None)
        else:
            result.append(a / b)
    return result

result = divide_corresponding([10, 20, 30], [2, 0, 5])
print(result)  # Expected: [5.0, None, 6.0]


""" 
Problem: 1912  
Write a Python function called `get_strings_containing` that takes a list of strings and a substring, and returns a list of strings that contain that substring.
"""
def get_strings_containing(strings, substring):
    return [s for s in strings if substring in s]

result = get_strings_containing(["hello", "world", "python", "programming"], "on")
print(result)  # Expected: ['python', 'programming']


""" 
Problem: 1913  
Write a Python function called `count_characters_by_type` that takes a string and returns a dictionary with 'letters', 'digits', and 'others' keys containing their counts.
"""
def count_characters_by_type(text):
    return {
        'letters': sum(1 for c in text if c.isalpha()),
        'digits': sum(1 for c in text if c.isdigit()),
        'others': sum(1 for c in text if not c.isalnum() and not c.isspace())
    }

result = count_characters_by_type("Hello123!")
print(result)  # Expected: {'letters': 5, 'digits': 3, 'others': 1}


""" 
Problem: 1914  
Write a Python function called `get_range_between` that takes a list and two values, and returns a list of elements that fall between those two values (inclusive).
"""
def get_range_between(my_list, min_val, max_val):
    return [x for x in my_list if min_val <= x <= max_val]

result = get_range_between([10, 20, 30, 40, 50], 20, 40)
print(result)  # Expected: [20, 30, 40]


""" 
Problem: 1915  
Write a Python function called `format_date` that takes year, month, and day, and returns a formatted date string as YYYY-MM-DD.
"""
def format_date(year, month, day):
    return f"{year}-{month:02d}-{day:02d}"

result = format_date(2024, 3, 5)
print(result)  # Expected: 2024-03-05


""" 
Problem: 1916  
Write a Python function called `calculate_simple_interest` that takes principal, rate, and time, and returns the simple interest amount.
"""
def calculate_simple_interest(principal, rate, time):
    return principal * rate * time / 100

result = calculate_simple_interest(1000, 5, 2)
print(result)  # Expected: 100.0


""" 
Problem: 1917  
Write a Python function called `get_unique_characters` that takes a string and returns a list of unique characters in the order they first appear.
"""
def get_unique_characters(text):
    seen = set()
    result = []
    for char in text:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return result

result = get_unique_characters("hello")
print(result)  # Expected: ['h', 'e', 'l', 'o']


""" 
Problem: 1918  
Write a Python function called `count_words_ending_with` that takes a string and a suffix, and returns the number of words that end with that suffix.
"""
def count_words_ending_with(text, suffix):
    words = text.split()
    return sum(1 for word in words if word.endswith(suffix))

result = count_words_ending_with("running walking jumping", "ing")
print(result)  # Expected: 3


""" 
Problem: 1919  
Write a Python function called `get_numbers_in_range` that takes a list of numbers and a range (min, max), and returns a list of numbers within that range.
"""
def get_numbers_in_range(numbers, min_val, max_val):
    return [x for x in numbers if min_val <= x <= max_val]

result = get_numbers_in_range([10, 20, 30, 40, 50], 25, 45)
print(result)  # Expected: [30, 40]


""" 
Problem: 1920  
Write a Python function called `format_name_age_city` that takes name, age, and city, and returns a formatted string: 'Name: {name}, Age: {age}, City: {city}'.
"""
def format_name_age_city(name, age, city):
    return f"Name: {name}, Age: {age}, City: {city}"

result = format_name_age_city("Alice", 30, "New York")
print(result)  # Expected: Name: Alice, Age: 30, City: New York


""" 
Problem: 1921  
Write a Python function called `check_multiple_of` that takes a number and a list of divisors, and returns True if the number is divisible by all divisors, otherwise False.
"""
def check_multiple_of(number, divisors):
    return all(number % d == 0 for d in divisors)

print(check_multiple_of(12, [2, 3, 4]), check_multiple_of(12, [2, 3, 5]))  # Expected: True False


""" 
Problem: 1922  
Write a Python function called `get_sum_of_squares` that takes a list of numbers and returns the sum of squares of all numbers.
"""
def get_sum_of_squares(numbers):
    return sum(x ** 2 for x in numbers)

result = get_sum_of_squares([1, 2, 3, 4])
print(result)  # Expected: 30


""" 
Problem: 1923  
Write a Python function called `get_product_of_even` that takes a list of numbers and returns the product of all even numbers.
"""
def get_product_of_even(numbers):
    product = 1
    for x in numbers:
        if x % 2 == 0:
            product *= x
    return product

result = get_product_of_even([1, 2, 3, 4, 5, 6])
print(result)  # Expected: 48


""" 
Problem: 1924  
Write a Python function called `get_sum_of_odd` that takes a list of numbers and returns the sum of all odd numbers.
"""
def get_sum_of_odd(numbers):
    return sum(x for x in numbers if x % 2 != 0)

result = get_sum_of_odd([1, 2, 3, 4, 5, 6])
print(result)  # Expected: 9


""" 
Problem: 1925  
Write a Python function called `find_second_occurrence` that takes a list and an element, and returns the index of the second occurrence of that element, or -1 if not found.
"""
def find_second_occurrence(my_list, element):
    count = 0
    for i, item in enumerate(my_list):
        if item == element:
            count += 1
            if count == 2:
                return i
    return -1

result = find_second_occurrence([10, 20, 10, 30, 10], 10)
print(result)  # Expected: 2


""" 
Problem: 1926  
Write a Python function called `get_elements_greater_than_average` that takes a list of numbers and returns a list of numbers greater than the average.
"""
def get_elements_greater_than_average(numbers):
    avg = sum(numbers) / len(numbers)
    return [x for x in numbers if x > avg]

result = get_elements_greater_than_average([10, 20, 30, 40])
print(result)  # Expected: [30, 40]


""" 
Problem: 1927  
Write a Python function called `get_elements_less_than_average` that takes a list of numbers and returns a list of numbers less than the average.
"""
def get_elements_less_than_average(numbers):
    avg = sum(numbers) / len(numbers)
    return [x for x in numbers if x < avg]

result = get_elements_less_than_average([10, 20, 30, 40])
print(result)  # Expected: [10, 20]


""" 
Problem: 1928  
Write a Python function called `count_digits_letters` that takes a string and returns a tuple containing the count of digits and the count of letters.
"""
def count_digits_letters(text):
    digits = sum(1 for c in text if c.isdigit())
    letters = sum(1 for c in text if c.isalpha())
    return (digits, letters)

result = count_digits_letters("Hello123World")
print(result)  # Expected: (3, 10)


""" 
Problem: 1929  
Write a Python function called `get_words_with_length` that takes a string and a length, and returns a list of words with exactly that length.
"""
def get_words_with_length(text, length):
    words = text.split()
    return [word for word in words if len(word) == length]

result = get_words_with_length("hello world python programming", 5)
print(result)  # Expected: ['hello', 'world']


""" 
Problem: 1930  
Write a Python function called `format_full_address` that takes street number, street name, city, state, and zipcode, and returns a complete formatted address.
"""
def format_full_address(street_num, street_name, city, state, zipcode):
    return f"{street_num} {street_name}, {city}, {state} {zipcode}"

result = format_full_address("123", "Main St", "New York", "NY", "10001")
print(result)  # Expected: 123 Main St, New York, NY 10001


""" 
Problem: 1931  
Write a Python function called `calculate_total_with_discount` that takes a list of prices, a discount percentage, and a tax rate, and returns the final total.
"""
def calculate_total_with_discount(prices, discount_percent, tax_rate):
    subtotal = sum(prices)
    discounted = subtotal * (1 - discount_percent / 100)
    total = discounted * (1 + tax_rate / 100)
    return total

result = calculate_total_with_discount([100, 50], 10, 8)
print(round(result, 2))  # Expected: 145.8


""" 
Problem: 1932  
Write a Python function called `get_common_prefix` that takes two strings and returns the longest common prefix they share.
"""
def get_common_prefix(str1, str2):
    prefix = ""
    for i in range(min(len(str1), len(str2))):
        if str1[i] == str2[i]:
            prefix += str1[i]
        else:
            break
    return prefix

result = get_common_prefix("hello", "help")
print(result)  # Expected: hel


""" 
Problem: 1933  
Write a Python function called `get_common_suffix` that takes two strings and returns the longest common suffix they share.
"""
def get_common_suffix(str1, str2):
    suffix = ""
    for i in range(1, min(len(str1), len(str2)) + 1):
        if str1[-i] == str2[-i]:
            suffix = str1[-i] + suffix
        else:
            break
    return suffix

result = get_common_suffix("running", "walking")
print(result)  # Expected: ing


""" 
Problem: 1934  
Write a Python function called `check_all_uppercase_words` that takes a string and returns True if all words start with uppercase letters, otherwise False.
"""
def check_all_uppercase_words(text):
    words = text.split()
    return all(word[0].isupper() for word in words if word)

result = check_all_uppercase_words("Hello World Python")
print(result)  # Expected: True


""" 
Problem: 1935  
Write a Python function called `get_strings_with_length_range` that takes a list of strings and min/max length, and returns strings within that length range.
"""
def get_strings_with_length_range(strings, min_length, max_length):
    return [s for s in strings if min_length <= len(s) <= max_length]

result = get_strings_with_length_range(["a", "ab", "abc", "abcd", "abcde"], 3, 4)
print(result)  # Expected: ['abc', 'abcd']


""" 
Problem: 1936  
Write a Python function called `calculate_median` that takes a list of numbers and returns the median value (middle value when sorted).
"""
def calculate_median(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    if n % 2 == 0:
        return (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
    else:
        return sorted_nums[n//2]

result = calculate_median([1, 3, 5, 7, 9])
print(result)  # Expected: 5


""" 
Problem: 1937  
Write a Python function called `get_mode` that takes a list and returns the element that appears most frequently (mode).
"""
def get_mode(my_list):
    counts = {}
    for item in my_list:
        counts[item] = counts.get(item, 0) + 1
    return max(counts, key=counts.get)

result = get_mode([1, 2, 2, 3, 3, 3, 4])
print(result)  # Expected: 3


""" 
Problem: 1938  
Write a Python function called `format_multiline_string` that takes name, age, and email, and returns a formatted multiline string with each piece of information on a separate line.
"""
def format_multiline_string(name, age, email):
    return f"Name: {name}\nAge: {age}\nEmail: {email}"

result = format_multiline_string("Alice", 30, "alice@example.com")
print(result)  # Expected: Name: Alice\nAge: 30\nEmail: alice@example.com


""" 
Problem: 1939  
Write a Python function called `get_numbers_divisible_by_all` that takes a list of numbers and a list of divisors, and returns numbers divisible by all divisors.
"""
def get_numbers_divisible_by_all(numbers, divisors):
    return [n for n in numbers if all(n % d == 0 for d in divisors)]

result = get_numbers_divisible_by_all([12, 18, 24, 30], [2, 3])
print(result)  # Expected: [12, 18, 24, 30]


""" 
Problem: 1940  
Write a Python function called `count_vowels_per_word` that takes a string and returns a dictionary where keys are words and values are vowel counts.
"""
def count_vowels_per_word(text):
    vowels = "aeiouAEIOU"
    words = text.split()
    return {word: sum(1 for c in word if c in vowels) for word in words}

result = count_vowels_per_word("hello world python")
print(result)  # Expected: {'hello': 2, 'world': 1, 'python': 1}


""" 
Problem: 1941  
Write a Python function called `get_words_with_vowel_count` that takes a string and a number n, and returns words that have exactly n vowels.
"""
def get_words_with_vowel_count(text, n):
    vowels = "aeiouAEIOU"
    words = text.split()
    return [word for word in words if sum(1 for c in word if c in vowels) == n]

result = get_words_with_vowel_count("hello world python programming", 2)
print(result)  # Expected: ['hello']


""" 
Problem: 1942  
Write a Python function called `format_table_row` that takes three values and returns a formatted string with values separated by pipes: 'value1 | value2 | value3'.
"""
def format_table_row(value1, value2, value3):
    return f"{value1} | {value2} | {value3}"

result = format_table_row("Alice", 30, "Engineer")
print(result)  # Expected: Alice | 30 | Engineer


""" 
Problem: 1943  
Write a Python function called `get_elements_not_in_both` that takes two lists and returns a list of elements that are in one list but not the other.
"""
def get_elements_not_in_both(list1, list2):
    result = []
    for item in list1:
        if item not in list2:
            result.append(item)
    for item in list2:
        if item not in list1:
            result.append(item)
    return result

result = get_elements_not_in_both([1, 2, 3, 4], [3, 4, 5, 6])
print(sorted(result))  # Expected: [1, 2, 5, 6]


""" 
Problem: 1944  
Write a Python function called `calculate_weighted_average` that takes a list of values and a list of weights, and returns the weighted average.
"""
def calculate_weighted_average(values, weights):
    weighted_sum = sum(v * w for v, w in zip(values, weights))
    total_weight = sum(weights)
    return weighted_sum / total_weight

result = calculate_weighted_average([10, 20, 30], [1, 2, 3])
print(result)  # Expected: 23.333333333333332


""" 
Problem: 1945  
Write a Python function called `get_strings_sorted_by_length` that takes a list of strings and returns the list sorted by length (shortest to longest).
"""
def get_strings_sorted_by_length(strings):
    return sorted(strings, key=len)

result = get_strings_sorted_by_length(["python", "a", "hello", "world"])
print(result)  # Expected: ['a', 'hello', 'world', 'python']


""" 
Problem: 1946  
Write a Python function called `format_percentage_list` that takes a list of numbers and returns a list of strings, each formatted as a percentage with % sign.
"""
def format_percentage_list(numbers):
    return [f"{n}%" for n in numbers]

result = format_percentage_list([25, 50, 75])
print(result)  # Expected: ['25%', '50%', '75%']


""" 
Problem: 1947  
Write a Python function called `get_pairs_summing_to` that takes a list of numbers and a target sum, and returns a list of tuples containing pairs that sum to the target.
"""
def get_pairs_summing_to(numbers, target):
    pairs = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                pairs.append((numbers[i], numbers[j]))
    return pairs

result = get_pairs_summing_to([1, 2, 3, 4, 5], 7)
print(result)  # Expected: [(2, 5), (3, 4)]


""" 
Problem: 1948  
Write a Python function called `count_character_types` that takes a string and returns a dictionary with 'vowels', 'consonants', 'digits', and 'spaces' counts.
"""
def count_character_types(text):
    vowels = "aeiouAEIOU"
    return {
        'vowels': sum(1 for c in text if c in vowels),
        'consonants': sum(1 for c in text if c.isalpha() and c not in vowels),
        'digits': sum(1 for c in text if c.isdigit()),
        'spaces': sum(1 for c in text if c.isspace())
    }

result = count_character_types("Hello World 123")
print(result)  # Expected: {'vowels': 3, 'consonants': 7, 'digits': 3, 'spaces': 2}


""" 
Problem: 1949  
Write a Python function called `get_words_by_vowel_count` that takes a string and returns a dictionary where keys are vowel counts and values are lists of words with that count.
"""
def get_words_by_vowel_count(text):
    vowels = "aeiouAEIOU"
    words = text.split()
    result = {}
    for word in words:
        count = sum(1 for c in word if c in vowels)
        if count not in result:
            result[count] = []
        result[count].append(word)
    return result

result = get_words_by_vowel_count("hello world python")
print(result)  # Expected: {2: ['hello'], 1: ['world', 'python']}


""" 
Problem: 1950  
Write a Python function called `format_name_with_title` that takes first name, last name, and title, and returns a formatted string: 'Title. First Last'.
"""
def format_name_with_title(first, last, title):
    return f"{title}. {first} {last}"

result = format_name_with_title("John", "Doe", "Dr")
print(result)  # Expected: Dr. John Doe


""" 
Problem: 1951  
Write a Python function called `calculate_area_circle_sector` that takes radius and angle in degrees, and returns the area of the sector.
"""
import math

def calculate_area_circle_sector(radius, angle_degrees):
    return (angle_degrees / 360) * math.pi * radius ** 2

result = calculate_area_circle_sector(5, 90)
print(round(result, 2))  # Expected: 19.63


""" 
Problem: 1952  
Write a Python function called `get_elements_at_multiple_indices` that takes a list and a list of indices, and returns a dictionary where keys are indices and values are elements.
"""
def get_elements_at_multiple_indices(my_list, indices):
    return {i: my_list[i] for i in indices if i < len(my_list)}

result = get_elements_at_multiple_indices([10, 20, 30, 40], [0, 2, 3])
print(result)  # Expected: {0: 10, 2: 30, 3: 40}


""" 
Problem: 1953  
Write a Python function called `check_string_properties` that takes a string and returns a dictionary with boolean values for 'has_uppercase', 'has_lowercase', 'has_digit', 'has_special'.
"""
def check_string_properties(text):
    return {
        'has_uppercase': any(c.isupper() for c in text),
        'has_lowercase': any(c.islower() for c in text),
        'has_digit': any(c.isdigit() for c in text),
        'has_special': any(not c.isalnum() and not c.isspace() for c in text)
    }

result = check_string_properties("Hello123!")
print(result)  # Expected: {'has_uppercase': True, 'has_lowercase': True, 'has_digit': True, 'has_special': True}


""" 
Problem: 1954  
Write a Python function called `get_numbers_summing_to_range` that takes a list of numbers and a range (min_sum, max_sum), and returns pairs of numbers whose sum is in that range.
"""
def get_numbers_summing_to_range(numbers, min_sum, max_sum):
    pairs = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            total = numbers[i] + numbers[j]
            if min_sum <= total <= max_sum:
                pairs.append((numbers[i], numbers[j]))
    return pairs

result = get_numbers_summing_to_range([1, 2, 3, 4, 5], 5, 7)
print(result)  # Expected: [(1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4)]


""" 
Problem: 1955  
Write a Python function called `format_phone_with_country` that takes country code, area code, and number, and returns a formatted phone number: '+{country} ({area}) {number}'.
"""
def format_phone_with_country(country_code, area_code, number):
    return f"+{country_code} ({area_code}) {number}"

result = format_phone_with_country("1", "555", "1234567")
print(result)  # Expected: +1 (555) 1234567


""" 
Problem: 1956  
Write a Python function called `get_consecutive_elements` that takes a list and a number n, and returns a list of lists where each inner list contains n consecutive elements.
"""
def get_consecutive_elements(my_list, n):
    return [my_list[i:i+n] for i in range(len(my_list) - n + 1)]

result = get_consecutive_elements([1, 2, 3, 4, 5], 3)
print(result)  # Expected: [[1, 2, 3], [2, 3, 4], [3, 4, 5]]


""" 
Problem: 1957  
Write a Python function called `calculate_gcd` that takes two numbers and returns their greatest common divisor using Euclidean algorithm.
"""
def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

result = calculate_gcd(48, 18)
print(result)  # Expected: 6


""" 
Problem: 1958  
Write a Python function called `calculate_lcm` that takes two numbers and returns their least common multiple.
"""
def calculate_lcm(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return abs(a * b) // gcd(a, b)

result = calculate_lcm(12, 18)
print(result)  # Expected: 36


""" 
Problem: 1959  
Write a Python function called `get_frequency_dict` that takes a list and returns a dictionary sorted by frequency (most frequent first).
"""
def get_frequency_dict(my_list):
    counts = {}
    for item in my_list:
        counts[item] = counts.get(item, 0) + 1
    return dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))

result = get_frequency_dict([1, 2, 2, 3, 3, 3, 4])
print(result)  # Expected: {3: 3, 2: 2, 1: 1, 4: 1}


""" 
Problem: 1960  
Write a Python function called `format_number_with_commas` that takes a number and returns it as a string with comma separators (e.g., 1000 becomes '1,000').
"""
def format_number_with_commas(number):
    return f"{number:,}"

result = format_number_with_commas(1234567)
print(result)  # Expected: 1,234,567


""" 
Problem: 1961  
Write a Python function called `get_words_with_same_length` that takes a list of strings and returns a dictionary where keys are lengths and values are lists of strings with that length.
"""
def get_words_with_same_length(strings):
    result = {}
    for s in strings:
        length = len(s)
        if length not in result:
            result[length] = []
        result[length].append(s)
    return result

result = get_words_with_same_length(["a", "ab", "abc", "ab", "abcd"])
print(result)  # Expected: {1: ['a'], 2: ['ab', 'ab'], 3: ['abc'], 4: ['abcd']}


""" 
Problem: 1962  
Write a Python function called `check_anagram_pair` that takes two strings and returns True if they are anagrams (contain same characters), otherwise False.
"""
def check_anagram_pair(str1, str2):
    return sorted(str1.lower().replace(" ", "")) == sorted(str2.lower().replace(" ", ""))

print(check_anagram_pair("listen", "silent"), check_anagram_pair("hello", "world"))  # Expected: True False


""" 
Problem: 1963  
Write a Python function called `get_sublist_sum` that takes a list and start/end indices, and returns the sum of elements in that sublist.
"""
def get_sublist_sum(my_list, start, end):
    return sum(my_list[start:end])

result = get_sublist_sum([10, 20, 30, 40, 50], 1, 4)
print(result)  # Expected: 90


""" 
Problem: 1964  
Write a Python function called `format_time_12hour` that takes hours (24-hour format) and returns time in 12-hour format with AM/PM.
"""
def format_time_12hour(hours_24):
    if hours_24 == 0:
        return "12 AM"
    elif hours_24 < 12:
        return f"{hours_24} AM"
    elif hours_24 == 12:
        return "12 PM"
    else:
        return f"{hours_24 - 12} PM"

print(format_time_12hour(0), format_time_12hour(14), format_time_12hour(23))  # Expected: 12 AM 2 PM 11 PM


""" 
Problem: 1965  
Write a Python function called `get_elements_between_values` that takes a list and two values, and returns elements that are greater than the first value and less than the second.
"""
def get_elements_between_values(my_list, min_val, max_val):
    return [x for x in my_list if min_val < x < max_val]

result = get_elements_between_values([10, 20, 30, 40, 50], 15, 45)
print(result)  # Expected: [20, 30, 40]


""" 
Problem: 1966  
Write a Python function called `count_substring_occurrences` that takes a string and a substring, and returns how many times the substring appears (overlapping allowed).
"""
def count_substring_occurrences(text, substring):
    count = 0
    for i in range(len(text) - len(substring) + 1):
        if text[i:i+len(substring)] == substring:
            count += 1
    return count

result = count_substring_occurrences("ababab", "aba")
print(result)  # Expected: 2


""" 
Problem: 1967  
Write a Python function called `format_list_as_string` that takes a list and a separator, and returns a string with elements joined by separator and enclosed in brackets.
"""
def format_list_as_string(my_list, separator):
    return f"[{separator.join(str(x) for x in my_list)}]"

result = format_list_as_string([1, 2, 3], ", ")
print(result)  # Expected: [1, 2, 3]


""" 
Problem: 1968  
Write a Python function called `get_unique_combinations` that takes two lists and returns a list of tuples containing all unique combinations of elements.
"""
def get_unique_combinations(list1, list2):
    return [(a, b) for a in list1 for b in list2]

result = get_unique_combinations([1, 2], ['a', 'b'])
print(result)  # Expected: [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]


""" 
Problem: 1969  
Write a Python function called `calculate_quadratic_roots` that takes coefficients a, b, c and returns the roots of ax^2 + bx + c = 0 as a tuple (or None if no real roots).
"""
import math

def calculate_quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    return (root1, root2)

result = calculate_quadratic_roots(1, -5, 6)
print(result)  # Expected: (3.0, 2.0)


""" 
Problem: 1970  
Write a Python function called `get_strings_matching_pattern` that takes a list of strings and a pattern (substring), and returns strings that contain the pattern at least twice.
"""
def get_strings_matching_pattern(strings, pattern):
    result = []
    for s in strings:
        if s.count(pattern) >= 2:
            result.append(s)
    return result

result = get_strings_matching_pattern(["hello", "lollipop", "world"], "l")
print(result)  # Expected: ['hello', 'lollipop']


""" 
Problem: 1971  
Write a Python function called `format_name_initials` that takes first name, middle name, and last name, and returns initials with periods: 'F.M.L.'.
"""
def format_name_initials(first, middle, last):
    return f"{first[0]}.{middle[0]}.{last[0]}."

result = format_name_initials("John", "Michael", "Doe")
print(result)  # Expected: J.M.D.


""" 
Problem: 1972  
Write a Python function called `get_elements_with_condition` that takes a list and a function (lambda), and returns elements that satisfy the condition.
"""
def get_elements_with_condition(my_list, condition_func):
    return [x for x in my_list if condition_func(x)]

result = get_elements_with_condition([1, 2, 3, 4, 5, 6], lambda x: x > 3)
print(result)  # Expected: [4, 5, 6]


""" 
Problem: 1973  
Write a Python function called `calculate_total_area` that takes a list of shapes represented as tuples (shape_type, dimensions), and returns the total area. Shape types: 'rectangle' (length, width), 'circle' (radius).
"""
import math

def calculate_total_area(shapes):
    total = 0
    for shape_type, dimensions in shapes:
        if shape_type == 'rectangle':
            total += dimensions[0] * dimensions[1]
        elif shape_type == 'circle':
            total += math.pi * dimensions[0] ** 2
    return total

result = calculate_total_area([('rectangle', (5, 3)), ('circle', (2,))])
print(round(result, 2))  # Expected: 27.57


""" 
Problem: 1974  
Write a Python function called `get_words_with_repeated_chars` that takes a string and returns a list of words that contain at least one repeated character.
"""
def get_words_with_repeated_chars(text):
    words = text.split()
    result = []
    for word in words:
        if len(word) != len(set(word)):
            result.append(word)
    return result

result = get_words_with_repeated_chars("hello world python programming")
print(result)  # Expected: ['hello', 'world', 'programming']


""" 
Problem: 1975  
Write a Python function called `format_multi_value_string` that takes a name and a list of scores, and returns a formatted string: 'Name: {name}, Scores: {scores}'.
"""
def format_multi_value_string(name, scores):
    scores_str = ", ".join(str(s) for s in scores)
    return f"Name: {name}, Scores: {scores_str}"

result = format_multi_value_string("Alice", [85, 90, 88])
print(result)  # Expected: Name: Alice, Scores: 85, 90, 88


""" 
Problem: 1976  
Write a Python function called `get_symmetric_difference` that takes two lists and returns a list of elements that are in one list but not the other (symmetric difference).
"""
def get_symmetric_difference(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.symmetric_difference(set2))

result = get_symmetric_difference([1, 2, 3, 4], [3, 4, 5, 6])
print(sorted(result))  # Expected: [1, 2, 5, 6]


""" 
Problem: 1977  
Write a Python function called `count_words_by_first_letter` that takes a string and returns a dictionary where keys are first letters and values are word counts.
"""
def count_words_by_first_letter(text):
    words = text.split()
    counts = {}
    for word in words:
        first_letter = word[0].lower()
        counts[first_letter] = counts.get(first_letter, 0) + 1
    return counts

result = count_words_by_first_letter("apple apricot banana cherry")
print(result)  # Expected: {'a': 2, 'b': 1, 'c': 1}


""" 
Problem: 1978  
Write a Python function called `format_decimal_places` that takes a number and decimal places, and returns the number formatted to that many decimal places.
"""
def format_decimal_places(number, decimal_places):
    return f"{number:.{decimal_places}f}"

result = format_decimal_places(3.14159, 2)
print(result)  # Expected: 3.14


""" 
Problem: 1979  
Write a Python function called `get_elements_satisfying_all` that takes a list and multiple conditions (functions), and returns elements that satisfy all conditions.
"""
def get_elements_satisfying_all(my_list, *conditions):
    result = []
    for item in my_list:
        if all(cond(item) for cond in conditions):
            result.append(item)
    return result

result = get_elements_satisfying_all([1, 2, 3, 4, 5, 6], lambda x: x > 2, lambda x: x < 6)
print(result)  # Expected: [3, 4, 5]


""" 
Problem: 1980  
Write a Python function called `calculate_net_price` that takes original price, discount percentage, and tax rate, and returns the final price after discount and tax.
"""
def calculate_net_price(original_price, discount_percent, tax_rate):
    discounted = original_price * (1 - discount_percent / 100)
    final = discounted * (1 + tax_rate / 100)
    return final

result = calculate_net_price(100, 20, 10)
print(result)  # Expected: 88.0


""" 
Problem: 1981  
Write a Python function called `get_strings_with_all_vowels` that takes a list of strings and returns strings that contain all five vowels (a, e, i, o, u).
"""
def get_strings_with_all_vowels(strings):
    vowels = set("aeiou")
    result = []
    for s in strings:
        if vowels.issubset(set(s.lower())):
            result.append(s)
    return result

result = get_strings_with_all_vowels(["education", "hello", "facetious"])
print(result)  # Expected: ['education', 'facetious']


""" 
Problem: 1982  
Write a Python function called `format_currency_multiple` that takes a list of numbers and returns a list of strings, each formatted as currency.
"""
def format_currency_multiple(numbers):
    return [f"${n:.2f}" for n in numbers]

result = format_currency_multiple([10.5, 20.75, 30.25])
print(result)  # Expected: ['$10.50', '$20.75', '$30.25']


""" 
Problem: 1983  
Write a Python function called `get_consecutive_pairs` that takes a list and returns a list of tuples containing consecutive pairs of elements.
"""
def get_consecutive_pairs(my_list):
    return [(my_list[i], my_list[i+1]) for i in range(len(my_list) - 1)]

result = get_consecutive_pairs([1, 2, 3, 4, 5])
print(result)  # Expected: [(1, 2), (2, 3), (3, 4), (4, 5)]


""" 
Problem: 1984  
Write a Python function called `calculate_geometric_mean` that takes a list of positive numbers and returns the geometric mean.
"""
import math

def calculate_geometric_mean(numbers):
    product = 1
    for n in numbers:
        product *= n
    return product ** (1 / len(numbers))

result = calculate_geometric_mean([2, 8, 32])
print(round(result, 2))  # Expected: 8.0


""" 
Problem: 1985  
Write a Python function called `get_words_sorted_by_vowels` that takes a string and returns a list of words sorted by the number of vowels they contain.
"""
def get_words_sorted_by_vowels(text):
    vowels = "aeiouAEIOU"
    words = text.split()
    return sorted(words, key=lambda w: sum(1 for c in w if c in vowels))

result = get_words_sorted_by_vowels("hello world python programming")
print(result)  # Expected: ['world', 'python', 'hello', 'programming']


""" 
Problem: 1986  
Write a Python function called `format_name_age_grade` that takes name, age, and grade, and returns a formatted string: '{name} (Age: {age}) - Grade: {grade}'.
"""
def format_name_age_grade(name, age, grade):
    return f"{name} (Age: {age}) - Grade: {grade}"

result = format_name_age_grade("Alice", 20, "A")
print(result)  # Expected: Alice (Age: 20) - Grade: A


""" 
Problem: 1987  
Write a Python function called `get_elements_with_max_frequency` that takes a list and returns a list of all elements that appear with the maximum frequency.
"""
def get_elements_with_max_frequency(my_list):
    counts = {}
    for item in my_list:
        counts[item] = counts.get(item, 0) + 1
    max_count = max(counts.values())
    return [item for item, count in counts.items() if count == max_count]

result = get_elements_with_max_frequency([1, 2, 2, 3, 3, 3, 4, 4, 4])
print(sorted(result))  # Expected: [3, 4]


""" 
Problem: 1988  
Write a Python function called `calculate_harmonic_mean` that takes a list of positive numbers and returns the harmonic mean.
"""
def calculate_harmonic_mean(numbers):
    reciprocal_sum = sum(1 / n for n in numbers)
    return len(numbers) / reciprocal_sum

result = calculate_harmonic_mean([2, 4, 8])
print(round(result, 2))  # Expected: 3.43


""" 
Problem: 1989  
Write a Python function called `format_list_items` that takes a list and returns a formatted string: 'Item 1: {item1}, Item 2: {item2}, ...'.
"""
def format_list_items(my_list):
    return ", ".join(f"Item {i+1}: {item}" for i, item in enumerate(my_list))

result = format_list_items(["apple", "banana", "cherry"])
print(result)  # Expected: Item 1: apple, Item 2: banana, Item 3: cherry


""" 
Problem: 1990  
Write a Python function called `get_strings_with_pattern_count` that takes a list of strings and a pattern, and returns strings where the pattern appears exactly n times.
"""
def get_strings_with_pattern_count(strings, pattern, n):
    result = []
    for s in strings:
        if s.count(pattern) == n:
            result.append(s)
    return result

result = get_strings_with_pattern_count(["hello", "lollipop", "world"], "l", 2)
print(result)  # Expected: ['hello']


""" 
Problem: 1991  
Write a Python function called `calculate_compound_growth` that takes initial value, growth rate, and number of periods, and returns the final value.
"""
def calculate_compound_growth(initial, rate, periods):
    return initial * (1 + rate / 100) ** periods

result = calculate_compound_growth(1000, 5, 3)
print(round(result, 2))  # Expected: 1157.63


""" 
Problem: 1992  
Write a Python function called `get_elements_by_frequency_range` that takes a list and min/max frequency, and returns elements that appear within that frequency range.
"""
def get_elements_by_frequency_range(my_list, min_freq, max_freq):
    counts = {}
    for item in my_list:
        counts[item] = counts.get(item, 0) + 1
    return [item for item, count in counts.items() if min_freq <= count <= max_freq]

result = get_elements_by_frequency_range([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 2, 3)
print(sorted(result))  # Expected: [2, 3]


""" 
Problem: 1993  
Write a Python function called `format_table_data` that takes a list of tuples (name, value) and returns a formatted table string with aligned columns.
"""
def format_table_data(data):
    lines = []
    for name, value in data:
        lines.append(f"{name:10s} | {value}")
    return "\n".join(lines)

result = format_table_data([("Alice", 85), ("Bob", 90), ("Charlie", 75)])
print(result)  # Expected: Alice      | 85\nBob        | 90\nCharlie    | 75


""" 
Problem: 1994  
Write a Python function called `get_words_with_unique_chars` that takes a string and returns words where all characters are unique (no repeated characters).
"""
def get_words_with_unique_chars(text):
    words = text.split()
    return [word for word in words if len(word) == len(set(word))]

result = get_words_with_unique_chars("hello world python")
print(result)  # Expected: ['world', 'python']


""" 
Problem: 1995  
Write a Python function called `calculate_total_with_multiple_discounts` that takes a price and a list of discount percentages, and returns the final price after applying all discounts sequentially.
"""
def calculate_total_with_multiple_discounts(price, discounts):
    result = price
    for discount in discounts:
        result = result * (1 - discount / 100)
    return result

result = calculate_total_with_multiple_discounts(100, [10, 20])
print(round(result, 2))  # Expected: 72.0


""" 
Problem: 1996  
Write a Python function called `format_multi_line_address` that takes name, street, city, state, zipcode, and returns a formatted multi-line address block.
"""
def format_multi_line_address(name, street, city, state, zipcode):
    return f"{name}\n{street}\n{city}, {state} {zipcode}"

result = format_multi_line_address("John Doe", "123 Main St", "New York", "NY", "10001")
print(result)  # Expected: John Doe\n123 Main St\nNew York, NY 10001


""" 
Problem: 1997  
Write a Python function called `get_elements_matching_multiple_patterns` that takes a list of strings and multiple patterns, and returns strings that match all patterns.
"""
def get_elements_matching_multiple_patterns(strings, *patterns):
    result = []
    for s in strings:
        if all(pattern in s for pattern in patterns):
            result.append(s)
    return result

result = get_elements_matching_multiple_patterns(["hello", "world", "python", "programming"], "o", "r")
print(result)  # Expected: ['world', 'programming']


""" 
Problem: 1998  
Write a Python function called `calculate_statistical_summary` that takes a list of numbers and returns a dictionary with 'mean', 'median', 'min', 'max', and 'range'.
"""
def calculate_statistical_summary(numbers):
    sorted_nums = sorted(numbers)
    n = len(numbers)
    mean = sum(numbers) / n
    median = sorted_nums[n//2] if n % 2 else (sorted_nums[n//2-1] + sorted_nums[n//2]) / 2
    min_val = min(numbers)
    max_val = max(numbers)
    return {
        'mean': mean,
        'median': median,
        'min': min_val,
        'max': max_val,
        'range': max_val - min_val
    }

result = calculate_statistical_summary([10, 20, 30, 40, 50])
print(result)  # Expected: {'mean': 30.0, 'median': 30, 'min': 10, 'max': 50, 'range': 40}


""" 
Problem: 1999  
Write a Python function called `format_contact_info` that takes name, phone, email, and address, and returns a formatted contact card as a multi-line string.
"""
def format_contact_info(name, phone, email, address):
    return f"Name: {name}\nPhone: {phone}\nEmail: {email}\nAddress: {address}"

result = format_contact_info("Alice", "555-1234", "alice@example.com", "123 Main St")
print(result)  # Expected: Name: Alice\nPhone: 555-1234\nEmail: alice@example.com\nAddress: 123 Main St


""" 
Problem: 2000  
Write a Python function called `get_comprehensive_statistics` that takes a list of numbers and returns a dictionary with sum, average, min, max, count, and standard deviation (using basic formula).
"""
import math

def get_comprehensive_statistics(numbers):
    n = len(numbers)
    mean = sum(numbers) / n
    variance = sum((x - mean) ** 2 for x in numbers) / n
    std_dev = math.sqrt(variance)
    return {
        'sum': sum(numbers),
        'average': mean,
        'min': min(numbers),
        'max': max(numbers),
        'count': n,
        'standard_deviation': std_dev
    }

result = get_comprehensive_statistics([10, 20, 30, 40, 50])
print(result)  # Expected: {'sum': 150, 'average': 30.0, 'min': 10, 'max': 50, 'count': 5, 'standard_deviation': ~14.14}

