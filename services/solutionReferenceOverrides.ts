/** Problem-specific repairs for legacy solution text that cannot be safely parsed. */
export const SOLUTION_REFERENCE_OVERRIDES: Readonly<Record<number, string>> = {
    2: `# Using the multiplication operator
def multiply_numbers(a, b):
    return a * b

# Using repeated addition
def multiply_numbers(a, b):
    total = 0
    for _ in range(abs(b)):
        total += a
    return total if b >= 0 else -total

# Using operator.mul
from operator import mul

def multiply_numbers(a, b):
    return mul(a, b)`,
    5: `# Using an explicit loop
def count_vowels(text):
    count = 0
    for char in text.lower():
        if char in 'aeiou':
            count += 1
    return count

# Using a list comprehension
def count_vowels(text):
    return len([char for char in text.lower() if char in 'aeiou'])

# Using sum and a generator expression
def count_vowels(text):
    return sum(char in 'aeiou' for char in text.lower())`,
    110: `# Using one explicit pass
def vowels_consonates(string):
    vowel_count = 0
    consonant_count = 0
    for character in string:
        if character.isalpha():
            if character.lower() in 'aeiou':
                vowel_count += 1
            else:
                consonant_count += 1
    return {'vowels': vowel_count, 'consonants': consonant_count}

# Using generator expressions
def vowels_consonates(string):
    letters = [character.lower() for character in string if character.isalpha()]
    return {
        'vowels': sum(character in 'aeiou' for character in letters),
        'consonants': sum(character not in 'aeiou' for character in letters),
    }

# Using collections.Counter
from collections import Counter

def vowels_consonates(string):
    frequencies = Counter(character.lower() for character in string if character.isalpha())
    vowel_count = sum(frequencies[vowel] for vowel in 'aeiou')
    return {
        'vowels': vowel_count,
        'consonants': sum(frequencies.values()) - vowel_count,
    }`,
    539: `# Using str.count
def count_substring(text, substring='cat'):
    return text.count(substring)

# Using regular expressions
import re

def count_substring(text, substring='cat'):
    return len(re.findall(re.escape(substring), text))

# Using a sliding window
def count_substring(text, substring='cat'):
    width = len(substring)
    return sum(text[index:index + width] == substring for index in range(len(text) - width + 1))`,
    561: `# Using split and list.count
def count_phrase_occurrences(text, phrase):
    return text.split().count(phrase)

# Using a generator expression
def count_phrase_occurrences(text, phrase):
    return sum(word == phrase for word in text.split())

# Using an explicit loop
def count_phrase_occurrences(text, phrase):
    count = 0
    for word in text.split():
        if word == phrase:
            count += 1
    return count`,
    157: `# Using a seen and repeated set
def remove_duplicates(string):
    seen = set()
    repeated = []
    for word in string.split():
        if word in seen and word not in repeated:
            repeated.append(word)
        seen.add(word)
    return repeated

# Using collections.Counter
from collections import Counter

def remove_duplicates(string):
    counts = Counter(string.split())
    return [word for word, count in counts.items() if count > 1]

# Using list.count while preserving order
def remove_duplicates(string):
    words = string.split()
    return list(dict.fromkeys(word for word in words if words.count(word) > 1))`,
    620: `# Using sorted with len
def lst_of_sentences(sentences):
    return sorted(sentences, key=len)

# Using a lambda key
def lst_of_sentences(sentences):
    return sorted(sentences, key=lambda sentence: len(sentence))

# Using insertion sort
def lst_of_sentences(sentences):
    result = []
    for sentence in sentences:
        position = 0
        while position < len(result) and len(result[position]) <= len(sentence):
            position += 1
        result.insert(position, sentence)
    return result`,
    677: `# Using dictionary membership
def check_key_exists(dictionary, key):
    return key in dictionary

# Using the keys view
def check_key_exists(dictionary, key):
    return key in dictionary.keys()

# Using get with a unique sentinel
def check_key_exists(dictionary, key):
    missing = object()
    return dictionary.get(key, missing) is not missing`,
    711: `# Using map with a lambda
def lst_sentence(sentences):
    return list(map(lambda sentence: len(sentence.split()), sentences))

# Using a list comprehension
def lst_sentence(sentences):
    return [len(sentence.split()) for sentence in sentences]

# Using an explicit loop
def lst_sentence(sentences):
    counts = []
    for sentence in sentences:
        counts.append(len(sentence.split()))
    return counts`,
    850: `# Using trial division up to the square root
def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True

# Using all with a generator
def is_prime(number):
    return number >= 2 and all(number % divisor for divisor in range(2, int(number ** 0.5) + 1))

# Using any to detect a factor
def is_prime(number):
    if number < 2:
        return False
    has_factor = any(number % divisor == 0 for divisor in range(2, int(number ** 0.5) + 1))
    return not has_factor`,
    1549: `# Using get followed by explicit initialization
def create_list():
    return []

data = {}
items = data.get('items', None)
if items is None:
    items = create_list()
    data['items'] = items
items.append('apple')
print(data)

# Using get with a freshly created default
def create_list():
    return []

data = {}
items = data.get('items', create_list())
data['items'] = items
items.append('apple')
print(data)

# Using setdefault for stored initialization
data = {}
items = data.setdefault('items', [])
items.append('apple')
print(data)`,
    1608: `# Using functools.wraps
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# Using functools.update_wrapper
from functools import update_wrapper

def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return update_wrapper(wrapper, func)

# Copying the relevant metadata explicitly
def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper`,
    941: `# Using try with a context manager
try:
    with open('/root/protected.txt', 'w') as file:
        file.write('Test')
except PermissionError:
    print('Permission denied')

# Using contextlib.ExitStack
import contextlib

try:
    with contextlib.ExitStack() as stack:
        file = stack.enter_context(open('/root/protected.txt', 'w'))
        file.write('Test')
except PermissionError:
    print('Permission denied')

# Using an explicit open and close
try:
    file = open('/root/protected.txt', 'w')
    try:
        file.write('Test')
    finally:
        file.close()
except PermissionError:
    print('Permission denied')`,
    951: `# Raising and catching KeyboardInterrupt
try:
    raise KeyboardInterrupt
except KeyboardInterrupt:
    print('Process interrupted by user')

# Handling through a helper function
def simulate_interrupt():
    raise KeyboardInterrupt

try:
    simulate_interrupt()
except KeyboardInterrupt:
    print('Process interrupted by user')

# Catching the interrupt as BaseException
try:
    raise KeyboardInterrupt
except BaseException as error:
    if isinstance(error, KeyboardInterrupt):
        print('Process interrupted by user')`,
    982: `# Using csv.reader with StringIO
import csv
from io import StringIO

csv_text = 'name,age\\nAlice,25\\nBob,30'
rows = list(csv.reader(StringIO(csv_text)))
print(rows)

# Passing split lines to csv.reader
import csv

csv_text = 'name,age\\nAlice,25\\nBob,30'
rows = list(csv.reader(csv_text.splitlines()))
print(rows)

# Parsing a simple comma-separated string manually
csv_text = 'name,age\\nAlice,25\\nBob,30'
rows = [line.split(',') for line in csv_text.splitlines()]
print(rows)`,
    988: `# Using ConfigParser.read_string
import configparser

config = configparser.ConfigParser()
config.read_string('[Settings]\\nusername=admin\\npassword=1234')
print(config['Settings']['username'])

# Using ConfigParser.read_file
import configparser
from io import StringIO

config = configparser.ConfigParser()
config.read_file(StringIO('[Settings]\\nusername=admin\\npassword=1234'))
print(config.get('Settings', 'username'))

# Parsing the setting lines directly
lines = 'username=admin\\npassword=1234'.splitlines()
settings = dict(line.split('=', 1) for line in lines)
print(settings['username'])`,
    989: `# Using re.findall
import re

markdown = '# Hello World\\nText'
print(re.findall(r'^# (.+)', markdown, re.MULTILINE))

# Using re.finditer
import re

markdown = '# Hello World\\nText'
print([match.group(1) for match in re.finditer(r'^# (.+)', markdown, re.MULTILINE)])

# Scanning lines without a regular expression
markdown = '# Hello World\\nText'
print([line.removeprefix('# ') for line in markdown.splitlines() if line.startswith('# ')])`,
    993: `# Using argparse.parse_args
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name', default='User')
print(parser.parse_args(['--name', 'Alice']).name)

# Using argparse.parse_known_args
import argparse

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('--name', default='User')
arguments, unknown = parser.parse_known_args(['--name', 'Alice'])
print(arguments.name)

# Parsing an argument list directly
arguments = ['--name', 'Alice']
name = arguments[arguments.index('--name') + 1] if '--name' in arguments else 'User'
print(name)`,
    1048: `# Using recursion
def print_numbers(number):
    if number > 0:
        print_numbers(number - 1)
        print(number)

# Using range
def print_numbers(number):
    for value in range(1, number + 1):
        print(value)

# Using a while loop
def print_numbers(number):
    value = 1
    while value <= number:
        print(value)
        value += 1`,
    1049: `# Using recursion
def print_reverse(number):
    if number > 0:
        print(number)
        print_reverse(number - 1)

# Using descending range
def print_reverse(number):
    for value in range(number, 0, -1):
        print(value)

# Using a while loop
def print_reverse(number):
    while number > 0:
        print(number)
        number -= 1`,
    1052: `# Using recursive branching
def binary_strings(length, prefix=''):
    if length == 0:
        print(prefix)
        return
    binary_strings(length - 1, prefix + '0')
    binary_strings(length - 1, prefix + '1')

# Using itertools.product
from itertools import product

def binary_strings(length):
    for bits in product('01', repeat=length):
        print(''.join(bits))

# Formatting every integer in the range
def binary_strings(length):
    for value in range(2 ** length):
        print(format(value, f'0{length}b'))`,
    1151: `# Rebinding an enclosing variable with nonlocal
def outer_function():
    value = 10
    def inner_function():
        nonlocal value
        value = 20
    inner_function()
    print(value)

# Incrementing an enclosing counter
def outer_function():
    count = 0
    def inner_function():
        nonlocal count
        count += 1
    inner_function()
    print(count)

# Updating enclosing text from a nested function
def outer_function():
    message = 'before'
    def inner_function():
        nonlocal message
        for part in ['almost', 'after']:
            message = part
    inner_function()
    print(message)`,
    1157: `# Catching NameError inside a function
def check_variable():
    try:
        return x
    except NameError:
        return 'x is not defined'

# Checking globals while retaining explicit error handling
def check_variable():
    try:
        return globals()['x']
    except KeyError:
        return 'x is not defined'

# Looking up the name with eval
def check_variable():
    try:
        return eval('x')
    except NameError:
        return 'x is not defined'`,
    1192: `# Using os.rename
import os

def rename_file(old_name, new_name):
    os.rename(old_name, new_name)

# Using pathlib.Path.rename
from pathlib import Path

def rename_file(old_name, new_name):
    Path(old_name).rename(new_name)

# Using os.replace
import os

def rename_file(old_name, new_name):
    os.replace(old_name, new_name)`,
    1245: `# Passing a Path to os.chdir
from pathlib import Path
import os

def change_working_directory():
    target = Path('example_directory')
    os.chdir(target)
    return f'Changed working directory to: {target}'

# Passing the Path through os.fspath
from pathlib import Path
import os

def change_working_directory():
    target = Path('example_directory')
    os.chdir(os.fspath(target))
    return f'Changed working directory to: {target}'

# Using Path as the canonical target
from pathlib import Path
import os

def change_working_directory():
    target = Path('.') / 'example_directory'
    os.chdir(target)
    return 'Changed working directory to: example_directory'`,
    1371: `# Printing kwargs directly
def print_kwargs(**kwargs):
    print(kwargs)

# Returning a copied dictionary
def print_kwargs(**kwargs):
    return dict(kwargs)

# Building a dictionary comprehension
def print_kwargs(**kwargs):
    return {key: value for key, value in kwargs.items()}`,
    1514: `# Using chained get calls
data = {'user': {'name': 'Alice', 'age': 30}}
name = data.get('user', {}).get('name', 'Unknown')
city = data.get('user', {}).get('city', 'Unknown')
print(name, city)

# Using a helper with get defaults
def nested_get(mapping, section, key, default='Unknown'):
    return mapping.get(section, {}).get(key, default)

data = {'user': {'name': 'Alice', 'age': 30}}
print(nested_get(data, 'user', 'name'), nested_get(data, 'user', 'city'))

# Caching the nested dictionary first
data = {'user': {'name': 'Alice', 'age': 30}}
user = data.get('user', {})
print(user.get('name', 'Unknown'), user.get('city', 'Unknown'))`,
    42: `# Using a generator expression approach
def table(number):
    return '\\n'.join(f'{number} * {factor} = {number * factor}' for factor in range(11))

# Using a manual loop approach
def table(number):
    lines = []
    for factor in range(11):
        lines.append(f'{number} * {factor} = {number * factor}')
    return '\\n'.join(lines)

# Using map and a helper approach
def table(number):
    def make_line(factor):
        return f'{number} * {factor} = {number * factor}'
    return '\\n'.join(map(make_line, range(11)))`,
    125: `# Using a generator expression approach
def histogram(numbers):
    return '\\n'.join('*' * number for number in numbers)

# Using a manual loop approach
def histogram(numbers):
    rows = []
    for number in numbers:
        rows.append('*' * number)
    return '\\n'.join(rows)

# Using map approach
def histogram(numbers):
    return '\\n'.join(map(lambda number: '*' * number, numbers))`,
    1380: `# Using dict.get with defaults
def greet(**kwargs):
    name = kwargs.get('name', 'Guest')
    age = kwargs.get('age', 'N/A')
    return f'Hello {name}, age {age}'

# Using merged defaults and key indexing
def greet(**kwargs):
    values = {'name': 'Guest', 'age': 'N/A'}
    values.update(kwargs)
    return f"Hello {values['name']}, age {values['age']}"

# Using collections.ChainMap
from collections import ChainMap

def greet(**kwargs):
    values = ChainMap(kwargs, {'name': 'Guest', 'age': 'N/A'})
    return f"Hello {values['name']}, age {values['age']}"

# Using conditional key access
def greet(**kwargs):
    name = kwargs['name'] if 'name' in kwargs else 'Guest'
    age = kwargs['age'] if 'age' in kwargs else 'N/A'
    return f'Hello {name}, age {age}'`,
    669: `# Using a generator expression approach
def countries_capitals(data):
    return '\\n'.join(f'{country}: {capital}' for country, capital in data.items())

# Using a manual loop approach
def countries_capitals(data):
    lines = []
    for country, capital in data.items():
        lines.append(f'{country}: {capital}')
    return '\\n'.join(lines)

# Using map approach
def countries_capitals(data):
    return '\\n'.join(map(lambda item: f'{item[0]}: {item[1]}', data.items()))`,
    762: `# Using split and join approach
def remove_whitespace(text):
    return ''.join(text.split())

def main(text):
    return remove_whitespace(text)

print(main('a b c'))

# Using a character method approach
def remove_whitespace(text):
    return ''.join(char for char in text if not char.isspace())

def main(text):
    return remove_whitespace(text)

print(main('hello world'))

# Using a manual loop approach
def remove_whitespace(text):
    result = []
    for char in text:
        if not char.isspace():
            result.append(char)
    return ''.join(result)

def main(text):
    return remove_whitespace(text)`,
    777: `# Using a generator approach
def print_dict_items(data):
    return '\\n'.join(f'{key}: {value}' for key, value in data.items())

print(print_dict_items({'a': 1, 'b': 2}))

# Using a list-building approach
def print_dict_items(data):
    lines = []
    for key, value in data.items():
        lines.append(f'{key}: {value}')
    return '\\n'.join(lines)

# Using direct printing approach
def print_dict_items(data):
    for key, value in data.items():
        print(f'{key}: {value}')

print_dict_items({'x': 'yes'})`,
    805: `# Using dict.get approach
def string_dic(text):
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return counts

# Using collections.Counter approach
from collections import Counter

def string_dic(text):
    return dict(Counter(text))

# Using a dictionary comprehension approach
def string_dic(text):
    return {char: text.count(char) for char in dict.fromkeys(text)}

print(string_dic('banana'))`,
    809: `# Using a generator expression approach
def print_readable(data):
    return '\\n'.join(f'{key}: {value}' for key, value in data.items())

# Using a manual loop approach
def print_readable(data):
    lines = []
    for key, value in data.items():
        lines.append(f'{key}: {value}')
    return '\\n'.join(lines)

# Using map approach
def print_readable(data):
    return '\\n'.join(map(lambda item: f'{item[0]}: {item[1]}', data.items()))`,
    1500: `# Using next with a default approach
def first_item_or_empty(items):
    return next((item for item in items), 'Empty')

print(first_item_or_empty([]))

# Using an iterator approach
def first_item_or_empty(items):
    iterator = iter(items)
    return next(iterator, 'Empty')

# Using a filtered generator approach
def first_even_or_empty(items):
    return next((item for item in items if item % 2 == 0), 'Empty')

print(first_even_or_empty([1, 3, 5]))`,
    1509: `# Using next directly with a default
items = iter([])
print(next(items, 'Nothing'))

# Using a reusable helper function
def next_with_default(iterable, default='Nothing'):
    return next(iter(iterable), default)

print(next_with_default([]))

# Using a generator expression with a default
numbers = [1, 3, 5]
first_even = next((number for number in numbers if number % 2 == 0), 'Nothing')
print(first_even)`,
    1626: `# Using contextlib.contextmanager
from contextlib import contextmanager

@contextmanager
def my_context():
    print('Entering context')
    try:
        yield 'context value'
    finally:
        print('Exiting context')

with my_context() as value:
    print(f'Inside context: {value}')

# Using a context-manager class
class MyContext:
    def __enter__(self):
        print('Entering context')
        return 'context value'

    def __exit__(self, exc_type, exc_value, traceback):
        print('Exiting context')

with MyContext() as value:
    print(f'Inside context: {value}')

# Using ExitStack for cleanup registration
from contextlib import contextmanager, ExitStack

@contextmanager
def my_context():
    with ExitStack() as stack:
        stack.callback(print, 'Exiting context')
        print('Entering context')
        yield 'context value'

with my_context() as value:
    print(f'Inside context: {value}')`,
    1882: `# Using an f-string approach
def format_address(street, city, state, zipcode):
    return f'{street}\\n{city}, {state} {zipcode}'

# Using str.join approach
def format_address(street, city, state, zipcode):
    city_line = f'{city}, {state} {zipcode}'
    return '\\n'.join((street, city_line))

# Using str.format approach
def format_address(street, city, state, zipcode):
    return '{}\\n{}, {} {}'.format(street, city, state, zipcode)`,
    1938: `# Using an f-string approach
def format_multiline_string(name, age, email):
    return f'Name: {name}\\nAge: {age}\\nEmail: {email}'

# Using str.join approach
def format_multiline_string(name, age, email):
    return '\\n'.join((f'Name: {name}', f'Age: {age}', f'Email: {email}'))

# Using str.format approach
def format_multiline_string(name, age, email):
    return 'Name: {}\\nAge: {}\\nEmail: {}'.format(name, age, email)`,
    1993: `# Using a generator expression approach
def format_table_data(data):
    return '\\n'.join(f'{name:10s} | {value}' for name, value in data)

# Using a manual loop approach
def format_table_data(data):
    lines = []
    for name, value in data:
        lines.append(f'{name:10s} | {value}')
    return '\\n'.join(lines)

# Using map and a helper approach
def format_table_data(data):
    def format_row(row):
        name, value = row
        return f'{name:10s} | {value}'
    return '\\n'.join(map(format_row, data))`,
    1996: `# Using an f-string approach
def format_multi_line_address(name, street, city, state, zipcode):
    return f'{name}\\n{street}\\n{city}, {state} {zipcode}'

# Using str.join approach
def format_multi_line_address(name, street, city, state, zipcode):
    city_line = f'{city}, {state} {zipcode}'
    return '\\n'.join((str(name), str(street), city_line))

# Using str.format approach
def format_multi_line_address(name, street, city, state, zipcode):
    return '{}\\n{}\\n{}, {} {}'.format(name, street, city, state, zipcode)`,
    1999: `# Using an f-string approach
def format_contact_info(name, phone, email, address):
    return f'Name: {name}\\nPhone: {phone}\\nEmail: {email}\\nAddress: {address}'

# Using str.join approach
def format_contact_info(name, phone, email, address):
    lines = [f'Name: {name}', f'Phone: {phone}', f'Email: {email}', f'Address: {address}']
    return '\\n'.join(lines)

# Using str.format approach
def format_contact_info(name, phone, email, address):
    return 'Name: {}\\nPhone: {}\\nEmail: {}\\nAddress: {}'.format(name, phone, email, address)`,
};
