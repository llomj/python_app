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
