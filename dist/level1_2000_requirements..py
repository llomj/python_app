
# ============================================================================
# PROBLEM EXPLANATION:
# Use `default=` with `min()` to avoid crash on an empty set.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1501  
Use `default=` with `min()` to avoid crash on an empty set.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

s = set()  # Initialize empty list/dict/set
print(min(s, default=0))  # Expected: 0




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `default=` with `next()` to check for existence of an element in a list.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1502  
Use `default=` with `next()` to check for existence of an element in a list.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

nums = [1, 3, 5]  # Initialize list
print(next((x for x in nums if x == 4), default="Missing"))  # Expected: "Missing"




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `default=` in `max()` to return fallback when list is empty.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1503  
Use `default=` in `max()` to return fallback when list is empty.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

scores = []  # Initialize empty list/dict/set
print(max(scores, default="No scores"))  # Expected: "No scores"




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `default=` with `next()` to return a default if no element satisfies the condition.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1504  
Use `default=` with `next()` to return a default if no element satisfies the condition.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

letters = ['a', 'b', 'c']  # Initialize list
print(next((ch for ch in letters if ch == 'z'), default="Not found"))  # Expected: "Not found"




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `default=` in `max()` with a custom key function and empty input.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1505  
Use `default=` in `max()` with a custom key function and empty input.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

strings = []  # Initialize empty list/dict/set
print(max(strings, key=str.lower, default="None"))  # Expected: "None"




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `default=` with `next()` to safely iterate a condition on a list of dictionaries.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1506  
Use `default=` with `next()` to safely iterate a condition on a list of dictionaries.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

users = [{"name": "Alice"}, {"name": "Bob"}]  # Initialize list
print(next((u for u in users if u["name"] == "Zoe"), default="No match"))  # Expected: "No match"




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `default=` with `min()` to handle a list that may be empty.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1507  
Use `default=` with `min()` to handle a list that may be empty.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

data = []  # Initialize empty list/dict/set
print(min(data, default=-99))  # Expected: -99




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `default=` in `max()` to get highest score or "No data".
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1508  
Use `default=` in `max()` to get highest score or "No data".
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

scores = []  # Initialize empty list/dict/set
print(max(scores, default="No data"))  # Expected: "No data"




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `default=` in `next()` to avoid StopIteration on empty input.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1509  
Use `default=` in `next()` to avoid StopIteration on empty input.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

print(next(iter([]), default="Nothing"))  # Expected: "Nothing"




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `default=` with `max()` to find max string or return fallback.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1510  
Use `default=` with `max()` to find max string or return fallback.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

words = []  # Initialize empty list/dict/set
print(max(words, default="N/A"))  # Expected: "N/A"




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `default=` with `sorted()` to handle empty iterables and return a default sorted list.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1511  
Use `default=` with `sorted()` to handle empty iterables and return a default sorted list.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

# Note: sorted() doesn't have a default parameter, but we can handle empty iterables
items = []  # Initialize empty list/dict/set
result = sorted(items) if items else []  # Sort the sequence
print(result)  # Expected: []




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `default=` with `min()` to find the minimum value in a list of dictionaries by a key, or return a default.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1512  
Use `default=` with `min()` to find the minimum value in a list of dictionaries by a key, or return a default.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

people = [{'age': 25}, {'age': 30}, {'age': 20}]  # Initialize list
min_age_dict = min(people, key=lambda x: x.get('age', 0), default={'age': 0})  # Use get() to safely access dictionary value with default
print(min_age_dict)  # Expected: {'age': 20}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `default=` with `max()` to find the maximum length string in a list, or return 'No items' if empty.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1513  
Use `default=` with `max()` to find the maximum length string in a list, or return 'No items' if empty.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

words = ['hello', 'world', 'python']  # Initialize list
max_word = max(words, key=len, default='No items')  # Use min/max with default parameter to handle empty sequences
print(max_word)  # Expected: python




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `dict.get()` with a default value to safely access nested dictionary keys.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1514  
Use `dict.get()` with a default value to safely access nested dictionary keys.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

data = {'user': {'name': 'Alice', 'age': 30}}  # Initialize dictionary
name = data.get('user', {}).get('name', 'Unknown')  # Initialize variable or assign value
city = data.get('user', {}).get('city', 'Unknown')  # Initialize variable or assign value
print(name, city)  # Expected: Alice Unknown




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `collections.defaultdict` with `int` as default factory to count occurrences of items in a list.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1515  
Use `collections.defaultdict` with `int` as default factory to count occurrences of items in a list.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

from collections import defaultdict  # Import statement: load module or specific functions
items = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']  # Initialize list
counter = defaultdict(int)  # Initialize defaultdict with default factory
for item in items:  # Loop: iterate over sequence
    counter[item] += 1
print(dict(counter))  # Expected: {'apple': 3, 'banana': 2, 'cherry': 1}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `dict.setdefault()` to initialize a list value in a dictionary if the key doesn't exist.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1516  
Use `dict.setdefault()` to initialize a list value in a dictionary if the key doesn't exist.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

data = {}  # Initialize empty list/dict/set
data.setdefault('items', []).append('apple')  # Add element to list
data.setdefault('items', []).append('banana')  # Add element to list
print(data)  # Expected: {'items': ['apple', 'banana']}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `default=` with `next()` to get the first element from a filtered iterator, or return None.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1517  
Use `default=` with `next()` to get the first element from a filtered iterator, or return None.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

numbers = [1, 3, 5, 8, 10]  # Initialize list
first_even = next((x for x in numbers if x % 2 == 0), None)  # Use next() to get first element from iterator with default
print(first_even)  # Expected: 8




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `collections.defaultdict` with `list` as default factory to group items by category.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1518  
Use `collections.defaultdict` with `list` as default factory to group items by category.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

from collections import defaultdict  # Import statement: load module or specific functions
items = [('fruit', 'apple'), ('fruit', 'banana'), ('vegetable', 'carrot')]  # Initialize list
grouped = defaultdict(list)  # Initialize defaultdict with default factory
for category, item in items:  # Loop: iterate over sequence
    grouped[category].append(item)  # Add element to list
print(dict(grouped))  # Expected: {'fruit': ['apple', 'banana'], 'vegetable': ['carrot']}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `dict.get()` with a default empty dictionary to safely access dictionary values.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1519  
Use `dict.get()` with a default empty dictionary to safely access dictionary values.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

data = {'user': {'name': 'Alice'}}  # Initialize dictionary
user_info = data.get('user', {})  # Initialize variable or assign value
name = user_info.get('name', 'Unknown')  # Initialize variable or assign value
print(name)  # Expected: Alice




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `default=` with `min()` and a key function to find the shortest string, or return an empty string.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1520  
Use `default=` with `min()` and a key function to find the shortest string, or return an empty string.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

words = ['hello', 'world', 'python', 'hi']  # Initialize list
shortest = min(words, key=len, default='')  # Use min/max with default parameter to handle empty sequences
print(shortest)  # Expected: hi




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `dict.setdefault()` to create a nested dictionary structure with default values.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1521  
Use `dict.setdefault()` to create a nested dictionary structure with default values.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

data = {}  # Initialize empty list/dict/set
data.setdefault('user', {}).setdefault('profile', {})['name'] = 'Alice'  # Initialize string variable
print(data)  # Expected: {'user': {'profile': {'name': 'Alice'}}}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `default=` with `max()` to find the maximum value in a list of tuples by index, or return (0, 0).
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1522  
Use `default=` with `max()` to find the maximum value in a list of tuples by index, or return (0, 0).
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

tuples = [(1, 5), (3, 2), (2, 8)]  # Initialize list
max_tuple = max(tuples, key=lambda x: x[1], default=(0, 0))  # Use min/max with default parameter to handle empty sequences
print(max_tuple)  # Expected: (2, 8)




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `collections.defaultdict` with `set` as default factory to collect unique values per key.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1523  
Use `collections.defaultdict` with `set` as default factory to collect unique values per key.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

from collections import defaultdict  # Import statement: load module or specific functions
items = [('a', 1), ('a', 2), ('b', 1), ('a', 1), ('b', 3)]  # Initialize list
grouped = defaultdict(set)  # Initialize defaultdict with default factory
for key, value in items:  # Loop: iterate over sequence
    grouped[key].add(value)  # Add element to set
print({k: list(v) for k, v in grouped.items()})  # Expected: {'a': [1, 2], 'b': [1, 3]}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `dict.get()` with a default value of 0 to safely sum values from multiple dictionaries.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1524  
Use `dict.get()` with a default value of 0 to safely sum values from multiple dictionaries.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

dict1 = {'a': 10, 'b': 20}  # Initialize dictionary
dict2 = {'b': 30, 'c': 40}  # Initialize dictionary
total = sum(dict1.get(k, 0) + dict2.get(k, 0) for k in set(dict1) | set(dict2))  # Initialize variable or assign value
print(total)  # Expected: 100




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `default=` with `next()` to get the first even number from an iterator, or return -1.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1525  
Use `default=` with `next()` to get the first even number from an iterator, or return -1.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

numbers = [1, 3, 5, 7]  # Initialize list
first_even = next((x for x in numbers if x % 2 == 0), -1)  # Use next() to get first element from iterator with default
print(first_even)  # Expected: -1




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `dict.setdefault()` to append items to a list value, creating the list if it doesn't exist.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1526  
Use `dict.setdefault()` to append items to a list value, creating the list if it doesn't exist.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

data = {}  # Initialize empty list/dict/set
data.setdefault('items', []).append('apple')  # Add element to list
data.setdefault('items', []).append('banana')  # Add element to list
print(data['items'])  # Expected: ['apple', 'banana']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `default=` with `min()` to find the minimum age from a list of person dictionaries, or return 0.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1527  
Use `default=` with `min()` to find the minimum age from a list of person dictionaries, or return 0.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

people = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]  # Initialize list
min_age = min((p.get('age', 0) for p in people), default=0)  # Use get() to safely access dictionary value with default
print(min_age)  # Expected: 25




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `collections.defaultdict` with `lambda: []` to group strings by their first character.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1528  
Use `collections.defaultdict` with `lambda: []` to group strings by their first character.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

from collections import defaultdict  # Import statement: load module or specific functions
words = ['apple', 'banana', 'apricot', 'cherry', 'blueberry']  # Initialize list
grouped = defaultdict(lambda: [])  # Initialize defaultdict with default factory
for word in words:  # Loop: iterate over sequence
    grouped[word[0]].append(word)  # Add element to list
print(dict(grouped))  # Expected: {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `dict.get()` with a default empty list to safely access list values from a dictionary.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1529  
Use `dict.get()` with a default empty list to safely access list values from a dictionary.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

data = {'items': ['apple', 'banana']}  # Initialize dictionary
items = data.get('items', [])  # Initialize variable or assign value
missing = data.get('missing', [])  # Initialize variable or assign value
print(items, missing)  # Expected: ['apple', 'banana'] []




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `default=` with `max()` and a key function to find the longest word, or return 'N/A'.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1530  
Use `default=` with `max()` and a key function to find the longest word, or return 'N/A'.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

words = ['hello', 'world', 'python']  # Initialize list
longest = max(words, key=len, default='N/A')  # Use min/max with default parameter to handle empty sequences
print(longest)  # Expected: python




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `dict.setdefault()` to initialize a counter dictionary with default value 0.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1531  
Use `dict.setdefault()` to initialize a counter dictionary with default value 0.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

counter = {}  # Initialize empty list/dict/set
counter.setdefault('count', 0)
counter['count'] += 1
print(counter)  # Expected: {'count': 1}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `default=` with `next()` to get the first prime number from an iterator, or return None.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1532  
Use `default=` with `next()` to get the first prime number from an iterator, or return None.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

def is_prime(n):  # Function definition: is_prime
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))  # Return the result

numbers = [4, 6, 8, 11, 12]  # Initialize list
first_prime = next((x for x in numbers if is_prime(x)), None)  # Use next() to get first element from iterator with default
print(first_prime)  # Expected: 11




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `collections.defaultdict` with `int` to create a frequency counter for characters in a string.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1533  
Use `collections.defaultdict` with `int` to create a frequency counter for characters in a string.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

from collections import defaultdict  # Import statement: load module or specific functions
text = "hello"  # Initialize string variable
char_count = defaultdict(int)  # Initialize defaultdict with default factory
for char in text:  # Loop: iterate over sequence
    char_count[char] += 1
print(dict(char_count))  # Expected: {'h': 1, 'e': 1, 'l': 2, 'o': 1}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `dict.get()` with a default value to safely merge two dictionaries, handling missing keys.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1534  
Use `dict.get()` with a default value to safely merge two dictionaries, handling missing keys.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

dict1 = {'a': 1, 'b': 2}  # Initialize dictionary
dict2 = {'b': 3, 'c': 4}  # Initialize dictionary
merged = {k: dict1.get(k, 0) + dict2.get(k, 0) for k in set(dict1) | set(dict2)}  # Initialize dictionary
print(merged)  # Expected: {'a': 1, 'b': 5, 'c': 4}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `default=` with `min()` to find the minimum score from a list of student records, or return 0.0.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1535  
Use `default=` with `min()` to find the minimum score from a list of student records, or return 0.0.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

students = [{'name': 'Alice', 'score': 85.5}, {'name': 'Bob', 'score': 92.0}]  # Initialize list
min_score = min((s.get('score', 0.0) for s in students), default=0.0)  # Use get() to safely access dictionary value with default
print(min_score)  # Expected: 85.5




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `dict.setdefault()` to create a dictionary of lists, appending values to existing lists.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1536  
Use `dict.setdefault()` to create a dictionary of lists, appending values to existing lists.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

data = {}  # Initialize empty list/dict/set
data.setdefault('fruits', []).append('apple')  # Add element to list
data.setdefault('fruits', []).append('banana')  # Add element to list
data.setdefault('vegetables', []).append('carrot')  # Add element to list
print(data)  # Expected: {'fruits': ['apple', 'banana'], 'vegetables': ['carrot']}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `default=` with `max()` to find the maximum price from a list of products, or return 'No products'.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1537  
Use `default=` with `max()` to find the maximum price from a list of products, or return 'No products'.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

products = [{'name': 'laptop', 'price': 999}, {'name': 'phone', 'price': 699}]  # Initialize list
max_price = max((p.get('price', 0) for p in products), default='No products')  # Use get() to safely access dictionary value with default
print(max_price)  # Expected: 999




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `collections.defaultdict` with `lambda: defaultdict(int)` to create nested counters.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1538  
Use `collections.defaultdict` with `lambda: defaultdict(int)` to create nested counters.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

from collections import defaultdict  # Import statement: load module or specific functions
data = [('a', 'x'), ('a', 'y'), ('b', 'x'), ('a', 'x')]  # Initialize list
nested = defaultdict(lambda: defaultdict(int))  # Initialize defaultdict with default factory
for key1, key2 in data:  # Loop: iterate over sequence
    nested[key1][key2] += 1
print({k: dict(v) for k, v in nested.items()})  # Expected: {'a': {'x': 2, 'y': 1}, 'b': {'x': 1}}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `dict.get()` with a default empty string to safely concatenate values from multiple dictionaries.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1539  
Use `dict.get()` with a default empty string to safely concatenate values from multiple dictionaries.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

dict1 = {'name': 'Alice'}  # Initialize dictionary
dict2 = {'surname': 'Smith'}  # Initialize dictionary
full_name = dict1.get('name', '') + ' ' + dict2.get('surname', '')  # Initialize variable or assign value
print(full_name)  # Expected: Alice Smith




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `default=` with `next()` to get the first element matching a condition, or return a default object.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1540  
Use `default=` with `next()` to get the first element matching a condition, or return a default object.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

numbers = [1, 3, 5, 7, 9]  # Initialize list
first_greater_than_5 = next((x for x in numbers if x > 5), None)  # Use next() to get first element from iterator with default
print(first_greater_than_5)  # Expected: 7




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `dict.setdefault()` to initialize a set value in a dictionary, adding items to the set.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1541  
Use `dict.setdefault()` to initialize a set value in a dictionary, adding items to the set.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

data = {}  # Initialize empty list/dict/set
data.setdefault('tags', set()).add('python')  # Add element to set
data.setdefault('tags', set()).add('programming')  # Add element to set
print(data)  # Expected: {'tags': {'python', 'programming'}}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `default=` with `min()` and a custom key to find the oldest person, or return a default person dict.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1542  
Use `default=` with `min()` and a custom key to find the oldest person, or return a default person dict.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

people = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]  # Initialize list
oldest = min(people, key=lambda x: x.get('age', 0), default={'name': 'Unknown', 'age': 0})  # Use get() to safely access dictionary value with default
print(oldest)  # Expected: {'name': 'Bob', 'age': 25}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `collections.defaultdict` with `str` as default factory to build a string concatenation dictionary.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1543  
Use `collections.defaultdict` with `str` as default factory to build a string concatenation dictionary.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

from collections import defaultdict  # Import statement: load module or specific functions
words = [('category', 'apple'), ('category', 'banana'), ('type', 'fruit')]  # Initialize list
result = defaultdict(str)  # Initialize defaultdict with default factory
for key, value in words:  # Loop: iterate over sequence
    result[key] += value + ' '
print({k: v.strip() for k, v in result.items()})  # Expected: {'category': 'apple banana', 'type': 'fruit'}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `dict.get()` with a default value of [] to safely extend a list from dictionary values.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1544  
Use `dict.get()` with a default value of [] to safely extend a list from dictionary values.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

data = {'items': [1, 2, 3]}  # Initialize dictionary
existing = data.get('items', [])  # Initialize variable or assign value
existing.extend([4, 5])
print(existing)  # Expected: [1, 2, 3, 4, 5]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `default=` with `max()` to find the maximum timestamp from a list of events, or return datetime.min.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1545  
Use `default=` with `max()` to find the maximum timestamp from a list of events, or return datetime.min.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

from datetime import datetime  # Import statement: load module or specific functions
events = [datetime(2023, 1, 1), datetime(2023, 2, 1), datetime(2023, 3, 1)]  # Initialize list
max_date = max(events, default=datetime.min)  # Use min/max with default parameter to handle empty sequences
print(max_date)  # Expected: 2023-03-01 00:00:00




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `dict.setdefault()` to create a dictionary of dictionaries with nested default values.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1546  
Use `dict.setdefault()` to create a dictionary of dictionaries with nested default values.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

data = {}  # Initialize empty list/dict/set
data.setdefault('users', {}).setdefault('alice', {})['age'] = 30  # Initialize variable or assign value
data.setdefault('users', {}).setdefault('bob', {})['age'] = 25  # Initialize variable or assign value
print(data)  # Expected: {'users': {'alice': {'age': 30}, 'bob': {'age': 25}}}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `default=` with `next()` to safely get the first item from a generator, or return a sentinel value.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1547  
Use `default=` with `next()` to safely get the first item from a generator, or return a sentinel value.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

def number_gen():  # Function definition: number_gen
    yield 1
    yield 2
    yield 3

gen = number_gen()  # Initialize variable or assign value
first = next(gen, 'END')  # Use next() to get first element from iterator with default
empty_gen = iter([])  # Initialize variable or assign value
empty_result = next(empty_gen, 'END')  # Use next() to get first element from iterator with default
print(first, empty_result)  # Expected: 1 END




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `collections.defaultdict` with `lambda: {'count': 0, 'total': 0}` to create statistics dictionaries.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1548  
Use `collections.defaultdict` with `lambda: {'count': 0, 'total': 0}` to create statistics dictionaries.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

from collections import defaultdict  # Import statement: load module or specific functions
stats = defaultdict(lambda: {'count': 0, 'total': 0})  # Initialize defaultdict with default factory
stats['item1']['count'] += 1
stats['item1']['total'] += 10
stats['item2']['count'] += 1
stats['item2']['total'] += 20
print(dict(stats))  # Expected: {'item1': {'count': 1, 'total': 10}, 'item2': {'count': 1, 'total': 20}}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Use `dict.get()` with a default function call to lazily initialize dictionary values only when accessed.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1549  
Use `dict.get()` with a default function call to lazily initialize dictionary values only when accessed.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

def create_list():  # Function definition: create_list
    return []  # Return the result

data = {}  # Initialize empty list/dict/set
# Using get with a callable default (note: dict.get doesn't support callables directly)
# This is a pattern where we check and initialize if needed
if 'items' not in data:  # Conditional statement: check condition
    data['items'] = create_list()  # Initialize variable or assign value
items = data.get('items', create_list())  # Initialize variable or assign value
items.append('apple')  # Add element to list
print(data)  # Expected: {'items': ['apple']}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `functools.reduce()` to calculate the product of all numbers in a list.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1550  
Write a Pythonic way to use `functools.reduce()` to calculate the product of all numbers in a list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

from functools import reduce  # Import statement: load module or specific functions
numbers = [2, 3, 4, 5]  # Initialize list
product = reduce(lambda x, y: x * y, numbers)  # Initialize variable or assign value
print(product)  # Expected: 120




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `functools.partial()` to create a function that multiplies a number by a fixed value.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1551  
Write a Pythonic way to use `functools.partial()` to create a function that multiplies a number by a fixed value.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

from functools import partial  # Import statement: load module or specific functions
multiply_by_5 = partial(lambda x, y: x * y, 5)  # Initialize variable or assign value
result = multiply_by_5(10)  # Initialize variable or assign value
print(result)  # Expected: 50




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `functools.lru_cache()` to memoize a recursive Fibonacci function.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1552  
Write a Pythonic way to use `functools.lru_cache()` to memoize a recursive Fibonacci function.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

from functools import lru_cache  # Import statement: load module or specific functions

@lru_cache(maxsize=None)
def fibonacci(n):  # Function definition: fibonacci
    if n < 2:  # Conditional statement: check condition
        return n  # Return the result
    return fibonacci(n-1) + fibonacci(n-2)  # Return the result

print(fibonacci(10))  # Expected: 55




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `itertools.permutations()` to generate all permutations of a list.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1553  
Write a Pythonic way to use `itertools.permutations()` to generate all permutations of a list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

from itertools import permutations  # Import statement: load module or specific functions
items = [1, 2, 3]  # Initialize list
perms = list(permutations(items))  # Initialize variable or assign value
print(perms)  # Expected: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `itertools.product()` to generate the Cartesian product of two lists.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1554  
Write a Pythonic way to use `itertools.product()` to generate the Cartesian product of two lists.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

from itertools import product  # Import statement: load module or specific functions
list1 = [1, 2]  # Initialize list
list2 = ['a', 'b']  # Initialize list
cartesian = list(product(list1, list2))  # Initialize variable or assign value
print(cartesian)  # Expected: [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `itertools.cycle()` to cycle through a list indefinitely.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1555  
Write a Pythonic way to use `itertools.cycle()` to cycle through a list indefinitely.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

from itertools import cycle  # Import statement: load module or specific functions
colors = ['red', 'green', 'blue']  # Initialize list
color_cycle = cycle(colors)  # Initialize variable or assign value
first_5 = [next(color_cycle) for _ in range(5)]  # Use next() to get first element from iterator with default
print(first_5)  # Expected: ['red', 'green', 'blue', 'red', 'green']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `itertools.repeat()` to create an iterator that repeats a value a specified number of times.
# 
# This problem demonstrates generators and iterators in Python. Generators are
# functions that yield values instead of returning them, creating an iterator.
# They are memory-efficient for processing large datasets and can be used with
# functions like next() to retrieve values one at a time.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1556  
Write a Pythonic way to use `itertools.repeat()` to create an iterator that repeats a value a specified number of times.
"""

# SOLUTION EXPLANATION:
# This solution uses generators or iterators to process data efficiently.
# Generators yield values one at a time, making them memory-efficient for
# large datasets.

from itertools import repeat  # Import statement: load module or specific functions
repeated = list(repeat('hello', 3))  # Initialize variable or assign value
print(repeated)  # Expected: ['hello', 'hello', 'hello']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `itertools.islice()` to get the first n elements from an iterator.
# 
# This problem demonstrates Python's slicing syntax, which allows you to extract
# portions of sequences (strings, lists, tuples) using indices. Slicing uses the
# format [start:stop:step] where start is inclusive, stop is exclusive, and step
# determines the increment. Negative indices count from the end, and omitting
# indices allows you to slice from the beginning or to the end.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1557  
Write a Pythonic way to use `itertools.islice()` to get the first n elements from an iterator.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax to extract the desired portion
# of the sequence. Slicing is efficient and readable, making it the preferred
# method for extracting subsequences from strings, lists, and tuples.

from itertools import islice  # Import statement: load module or specific functions
numbers = range(10)  # Initialize variable or assign value
first_5 = list(islice(numbers, 5))  # Initialize variable or assign value
print(first_5)  # Expected: [0, 1, 2, 3, 4]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `itertools.tee()` to split an iterator into multiple independent iterators.
# 
# This problem demonstrates generators and iterators in Python. Generators are
# functions that yield values instead of returning them, creating an iterator.
# They are memory-efficient for processing large datasets and can be used with
# functions like next() to retrieve values one at a time.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1558  
Write a Pythonic way to use `itertools.tee()` to split an iterator into multiple independent iterators.
"""

# SOLUTION EXPLANATION:
# This solution uses generators or iterators to process data efficiently.
# Generators yield values one at a time, making them memory-efficient for
# large datasets.

from itertools import tee  # Import statement: load module or specific functions
numbers = iter([1, 2, 3, 4, 5])  # Initialize variable or assign value
iter1, iter2 = tee(numbers, 2)  # Initialize variable or assign value
print(list(iter1), list(iter2))  # Expected: [1, 2, 3, 4, 5] [1, 2, 3, 4, 5]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `itertools.accumulate()` to calculate cumulative sums of a list.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1559  
Write a Pythonic way to use `itertools.accumulate()` to calculate cumulative sums of a list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

from itertools import accumulate  # Import statement: load module or specific functions
numbers = [1, 2, 3, 4, 5]  # Initialize list
cumulative = list(accumulate(numbers))  # Initialize variable or assign value
print(cumulative)  # Expected: [1, 3, 6, 10, 15]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program using `dataclasses` to create a simple Person class with name and age fields.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1560  
Write a Python program using `dataclasses` to create a simple Person class with name and age fields.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

from dataclasses import dataclass  # Import statement: load module or specific functions

@dataclass
class Person:  # Statement block
    name: str
    age: int

person = Person("Alice", 30)  # Initialize variable or assign value
print(person)  # Expected: Person(name='Alice', age=30)




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program using `dataclasses.field()` to set default values in a dataclass.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1561  
Write a Python program using `dataclasses.field()` to set default values in a dataclass.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

from dataclasses import dataclass, field  # Import statement: load module or specific functions

@dataclass
class Student:  # Statement block
    name: str
    age: int = field(default=18)  # Initialize variable or assign value
    grades: list = field(default_factory=list)  # Initialize variable or assign value

student = Student("Bob")  # Initialize variable or assign value
print(student)  # Expected: Student(name='Bob', age=18, grades=[])




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program using `@dataclass(frozen=True)` to create an immutable dataclass.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1562  
Write a Python program using `@dataclass(frozen=True)` to create an immutable dataclass.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

from dataclasses import dataclass  # Import statement: load module or specific functions

@dataclass(frozen=True)
class Point:  # Statement block
    x: int
    y: int

point = Point(3, 4)  # Initialize variable or assign value
print(point)  # Expected: Point(x=3, y=4)




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function with type hints using `typing.List` to specify a function that takes a list of integers.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1563  
Write a Python function with type hints using `typing.List` to specify a function that takes a list of integers.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

from typing import List  # Import statement: load module or specific functions

def sum_numbers(numbers: List[int]) -> int:  # Function definition: sum_numbers
    return sum(numbers)  # Return the result

result = sum_numbers([1, 2, 3, 4])  # Initialize variable or assign value
print(result)  # Expected: 10




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function with type hints using `typing.Optional` to indicate a parameter that can be None.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1564  
Write a Python function with type hints using `typing.Optional` to indicate a parameter that can be None.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

from typing import Optional  # Import statement: load module or specific functions

def greet(name: Optional[str] = None) -> str:  # Function definition: greet
    if name is None:  # Conditional statement: check condition
        return "Hello, Guest!"  # Return the result
    return f"Hello, {name}!"  # Return the result

print(greet("Alice"), greet())  # Expected: Hello, Alice! Hello, Guest!




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function with type hints using `typing.Union` to accept multiple types.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1565  
Write a Python function with type hints using `typing.Union` to accept multiple types.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

from typing import Union  # Import statement: load module or specific functions

def process_value(value: Union[int, str]) -> str:  # Function definition: process_value
    return str(value)  # Return the result

print(process_value(42), process_value("hello"))  # Expected: 42 hello




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use the walrus operator (`:=`) to assign and check a value in a while loop condition.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1566  
Write a Pythonic way to use the walrus operator (`:=`) to assign and check a value in a while loop condition.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

numbers = [1, 2, 3, 4, 5]  # Initialize list
while (n := len(numbers)) > 0:  # Loop: iterate while condition is true
    numbers.pop()
    print(f"Remaining: {n}")  # Expected: Remaining: 5, 4, 3, 2, 1




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use the walrus operator (`:=`) in a list comprehension to avoid repeated function calls.
# 
# This problem demonstrates list comprehensions, a concise way to create lists
# in Python. List comprehensions are more readable and often faster than
# equivalent loops. They can include conditional expressions to filter or
# transform elements, making them a powerful tool for data manipulation.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1567  
Write a Pythonic way to use the walrus operator (`:=`) in a list comprehension to avoid repeated function calls.
"""

# SOLUTION EXPLANATION:
# This solution uses a list comprehension to create a new list based on the
# specified conditions. List comprehensions are concise, readable, and often
# more efficient than equivalent loops for creating lists.

def expensive_function(x):  # Function definition: expensive_function
    return x * 2  # Return the result

numbers = [1, 2, 3, 4, 5]  # Initialize list
result = [y for x in numbers if (y := expensive_function(x)) > 4]  # Initialize list
print(result)  # Expected: [6, 8, 10]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program using `match/case` statements to handle different string patterns.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1568  
Write a Python program using `match/case` statements to handle different string patterns.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

def handle_command(cmd: str) -> str:  # Function definition: handle_command
    match cmd:  # Statement block
        case "start":  # Statement block
            return "Starting..."  # Return the result
        case "stop":  # Statement block
            return "Stopping..."  # Return the result
        case "pause":  # Statement block
            return "Paused"  # Return the result
        case _:  # Statement block
            return "Unknown command"  # Return the result

print(handle_command("start"))  # Expected: Starting...




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program using `match/case` with pattern matching to destructure a tuple.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1569  
Write a Python program using `match/case` with pattern matching to destructure a tuple.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

def process_point(point):  # Function definition: process_point
    match point:  # Statement block
        case (0, 0):  # Statement block
            return "Origin"  # Return the result
        case (x, 0):  # Statement block
            return f"On x-axis at {x}"  # Return the result
        case (0, y):  # Statement block
            return f"On y-axis at {y}"  # Return the result
        case (x, y):  # Statement block
            return f"Point at ({x}, {y})"  # Return the result

print(process_point((3, 4)))  # Expected: Point at (3, 4)




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python class using `@property` decorator to create a computed attribute.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1570  
Write a Python class using `@property` decorator to create a computed attribute.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

class Circle:  # Statement block
    def __init__(self, radius):  # Function definition: __init__
        self.radius = radius  # Initialize variable or assign value
    
    @property
    def area(self):  # Function definition: area
        return 3.14159 * self.radius ** 2  # Return the result

circle = Circle(5)  # Initialize variable or assign value
print(circle.area)  # Expected: 78.53975




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python class using `@property.setter` to validate and set a property value.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1571  
Write a Python class using `@property.setter` to validate and set a property value.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

class Temperature:  # Statement block
    def __init__(self):  # Function definition: __init__
        self._celsius = 0  # Initialize variable or assign value
    
    @property
    def celsius(self):  # Function definition: celsius
        return self._celsius  # Return the result
    
    @celsius.setter
    def celsius(self, value):  # Function definition: celsius
        if value < -273.15:  # Conditional statement: check condition
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = value  # Initialize variable or assign value

temp = Temperature()  # Initialize variable or assign value
temp.celsius = 25  # Initialize variable or assign value
print(temp.celsius)  # Expected: 25




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python class implementing `__str__` magic method to customize string representation.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1572  
Write a Python class implementing `__str__` magic method to customize string representation.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

class Book:  # Statement block
    def __init__(self, title, author):  # Function definition: __init__
        self.title = title  # Initialize variable or assign value
        self.author = author  # Initialize variable or assign value
    
    def __str__(self):  # Function definition: __str__
        return f"{self.title} by {self.author}"  # Return the result

book = Book("Python Guide", "John Doe")  # Initialize variable or assign value
print(str(book))  # Expected: Python Guide by John Doe




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python class implementing `__repr__` magic method to provide a developer-friendly representation.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1573  
Write a Python class implementing `__repr__` magic method to provide a developer-friendly representation.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

class Point:  # Statement block
    def __init__(self, x, y):  # Function definition: __init__
        self.x = x  # Initialize variable or assign value
        self.y = y  # Initialize variable or assign value
    
    def __repr__(self):  # Function definition: __repr__
        return f"Point(x={self.x}, y={self.y})"  # Return the result

point = Point(3, 4)  # Initialize variable or assign value
print(repr(point))  # Expected: Point(x=3, y=4)




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python class implementing `__eq__` magic method to define equality comparison.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1574  
Write a Python class implementing `__eq__` magic method to define equality comparison.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

class Person:  # Statement block
    def __init__(self, name, age):  # Function definition: __init__
        self.name = name  # Initialize variable or assign value
        self.age = age  # Initialize variable or assign value
    
    def __eq__(self, other):  # Function definition: __eq__
        if not isinstance(other, Person):  # Conditional statement: check condition
            return False  # Return the result
        return self.name == other.name and self.age == other.age  # Return the result

p1 = Person("Alice", 30)  # Initialize variable or assign value
p2 = Person("Alice", 30)  # Initialize variable or assign value
print(p1 == p2)  # Expected: True




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python class implementing `__hash__` magic method to make an object hashable.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1575  
Write a Python class implementing `__hash__` magic method to make an object hashable.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

class Point:  # Statement block
    def __init__(self, x, y):  # Function definition: __init__
        self.x = x  # Initialize variable or assign value
        self.y = y  # Initialize variable or assign value
    
    def __hash__(self):  # Function definition: __hash__
        return hash((self.x, self.y))  # Return the result
    
    def __eq__(self, other):  # Function definition: __eq__
        return isinstance(other, Point) and self.x == other.x and self.y == other.y  # Return the result

point = Point(3, 4)  # Initialize variable or assign value
points_set = {point}  # Initialize dictionary
print(len(points_set))  # Expected: 1




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python class implementing `__len__` magic method to make an object work with `len()`.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1576  
Write a Python class implementing `__len__` magic method to make an object work with `len()`.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

class Stack:  # Statement block
    def __init__(self):  # Function definition: __init__
        self.items = []  # Initialize empty list/dict/set
    
    def push(self, item):  # Function definition: push
        self.items.append(item)  # Add element to list
    
    def __len__(self):  # Function definition: __len__
        return len(self.items)  # Return the result

stack = Stack()  # Initialize variable or assign value
stack.push(1)
stack.push(2)
print(len(stack))  # Expected: 2




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python class implementing `__getitem__` magic method to enable indexing.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1577  
Write a Python class implementing `__getitem__` magic method to enable indexing.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

class MyList:  # Statement block
    def __init__(self, items):  # Function definition: __init__
        self.items = items  # Initialize variable or assign value
    
    def __getitem__(self, index):  # Function definition: __getitem__
        return self.items[index]  # Return the result

my_list = MyList([10, 20, 30, 40])  # Initialize variable or assign value
print(my_list[2])  # Expected: 30




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program using a custom context manager class with `__enter__` and `__exit__` methods.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1578  
Write a Python program using a custom context manager class with `__enter__` and `__exit__` methods.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

class Timer:  # Statement block
    def __enter__(self):  # Function definition: __enter__
        import time  # Import statement: load module or specific functions
        self.start = time.time()  # Initialize variable or assign value
        return self  # Return the result
    
    def __exit__(self, exc_type, exc_val, exc_tb):  # Function definition: __exit__
        import time  # Import statement: load module or specific functions
        self.elapsed = time.time() - self.start  # Initialize variable or assign value
        print(f"Elapsed time: {self.elapsed:.2f} seconds")  # Print the result

with Timer():  # Statement block
    sum(range(1000000))  # Expected: Elapsed time: ~0.XX seconds




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `contextlib.ExitStack` to manage multiple context managers.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1579  
Write a Pythonic way to use `contextlib.ExitStack` to manage multiple context managers.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

from contextlib import ExitStack  # Import statement: load module or specific functions

class Resource:  # Statement block
    def __enter__(self):  # Function definition: __enter__
        print("Entering resource")  # Print the result
        return self  # Return the result
    def __exit__(self, *args):  # Function definition: __exit__
        print("Exiting resource")  # Print the result

with ExitStack() as stack:  # Statement block
    r1 = stack.enter_context(Resource())  # Initialize variable or assign value
    r2 = stack.enter_context(Resource())  # Initialize variable or assign value
    print("Using resources")  # Expected: Entering resource, Entering resource, Using resources, Exiting resource, Exiting resource




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `pathlib.Path` to check if a file exists.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1580  
Write a Pythonic way to use `pathlib.Path` to check if a file exists.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

from pathlib import Path  # Import statement: load module or specific functions

# Note: This is a demonstration - actual file may not exist
path = Path("example.txt")  # Initialize variable or assign value
exists = path.exists()  # Initialize variable or assign value
print(f"File exists: {exists}")  # Expected: File exists: False (or True if file exists)




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `pathlib.Path` to get the parent directory of a file path.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1581  
Write a Pythonic way to use `pathlib.Path` to get the parent directory of a file path.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

from pathlib import Path  # Import statement: load module or specific functions

path = Path("/home/user/documents/file.txt")  # Initialize variable or assign value
parent = path.parent  # Initialize variable or assign value
print(parent)  # Expected: /home/user/documents




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `pathlib.Path` to join path components.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1582  
Write a Pythonic way to use `pathlib.Path` to join path components.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

from pathlib import Path  # Import statement: load module or specific functions

base = Path("/home/user")  # Initialize variable or assign value
full_path = base / "documents" / "file.txt"  # Initialize variable or assign value
print(full_path)  # Expected: /home/user/documents/file.txt




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program using `json.dumps()` to convert a Python dictionary to a JSON string.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1583  
Write a Python program using `json.dumps()` to convert a Python dictionary to a JSON string.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

import json  # Import statement: load module or specific functions

data = {"name": "Alice", "age": 30, "city": "New York"}  # Initialize dictionary
json_string = json.dumps(data)  # Initialize variable or assign value
print(json_string)  # Expected: {"name": "Alice", "age": 30, "city": "New York"}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program using `json.loads()` to parse a JSON string into a Python dictionary.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1584  
Write a Python program using `json.loads()` to parse a JSON string into a Python dictionary.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

import json  # Import statement: load module or specific functions

json_string = '{"name": "Alice", "age": 30}'  # Initialize string variable
data = json.loads(json_string)  # Initialize variable or assign value
print(data)  # Expected: {'name': 'Alice', 'age': 30}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program using `re.sub()` to replace all occurrences of a pattern in a string.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1585  
Write a Python program using `re.sub()` to replace all occurrences of a pattern in a string.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

import re  # Import statement: load module or specific functions

text = "The cat sat on the mat"  # Initialize string variable
new_text = re.sub(r'cat', 'dog', text)  # Initialize variable or assign value
print(new_text)  # Expected: The dog sat on the mat




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program using `re.finditer()` to find all matches of a pattern and get their positions.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1586  
Write a Python program using `re.finditer()` to find all matches of a pattern and get their positions.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

import re  # Import statement: load module or specific functions

text = "The cat and the hat"  # Initialize string variable
pattern = r'\b\w{3}\b'  # Initialize variable or assign value
matches = [(m.group(), m.start()) for m in re.finditer(pattern, text)]  # Initialize list
print(matches)  # Expected: [('The', 0), ('cat', 4), ('and', 8), ('the', 12), ('hat', 16)]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program using named groups in regex to extract specific parts of a string.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1587  
Write a Python program using named groups in regex to extract specific parts of a string.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

import re  # Import statement: load module or specific functions

text = "John Doe, age 30"  # Initialize string variable
pattern = r'(?P<name>\w+\s+\w+).*age\s+(?P<age>\d+)'  # Initialize variable or assign value
match = re.search(pattern, text)  # Initialize variable or assign value
if match:  # Conditional statement: check condition
    print(match.group('name'), match.group('age'))  # Expected: John Doe 30




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `collections.OrderedDict` to maintain insertion order in a dictionary.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1588  
Write a Pythonic way to use `collections.OrderedDict` to maintain insertion order in a dictionary.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

from collections import OrderedDict  # Import statement: load module or specific functions

od = OrderedDict()  # Initialize variable or assign value
od['first'] = 1  # Initialize variable or assign value
od['second'] = 2  # Initialize variable or assign value
od['third'] = 3  # Initialize variable or assign value
print(list(od.keys()))  # Expected: ['first', 'second', 'third']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `collections.ChainMap` to combine multiple dictionaries into a single mapping.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1589  
Write a Pythonic way to use `collections.ChainMap` to combine multiple dictionaries into a single mapping.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

from collections import ChainMap  # Import statement: load module or specific functions

dict1 = {'a': 1, 'b': 2}  # Initialize dictionary
dict2 = {'c': 3, 'd': 4}  # Initialize dictionary
chain = ChainMap(dict1, dict2)  # Initialize variable or assign value
print(dict(chain))  # Expected: {'a': 1, 'b': 2, 'c': 3, 'd': 4}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `collections.namedtuple` to create a simple data structure with named fields.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1590  
Write a Pythonic way to use `collections.namedtuple` to create a simple data structure with named fields.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

from collections import namedtuple  # Import statement: load module or specific functions

Point = namedtuple('Point', ['x', 'y'])  # Initialize variable or assign value
p = Point(3, 4)  # Initialize variable or assign value
print(p.x, p.y)  # Expected: 3 4




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use nested list comprehensions to create a matrix.
# 
# This problem demonstrates list comprehensions, a concise way to create lists
# in Python. List comprehensions are more readable and often faster than
# equivalent loops. They can include conditional expressions to filter or
# transform elements, making them a powerful tool for data manipulation.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1591  
Write a Pythonic way to use nested list comprehensions to create a matrix.
"""

# SOLUTION EXPLANATION:
# This solution uses a list comprehension to create a new list based on the
# specified conditions. List comprehensions are concise, readable, and often
# more efficient than equivalent loops for creating lists.

matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]  # Initialize list
print(matrix)  # Expected: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use a list comprehension with multiple conditions to filter elements.
# 
# This problem demonstrates list comprehensions, a concise way to create lists
# in Python. List comprehensions are more readable and often faster than
# equivalent loops. They can include conditional expressions to filter or
# transform elements, making them a powerful tool for data manipulation.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1592  
Write a Pythonic way to use a list comprehension with multiple conditions to filter elements.
"""

# SOLUTION EXPLANATION:
# This solution uses a list comprehension to create a new list based on the
# specified conditions. List comprehensions are concise, readable, and often
# more efficient than equivalent loops for creating lists.

numbers = range(20)  # Initialize variable or assign value
filtered = [x for x in numbers if x % 2 == 0 and x % 3 == 0]  # Initialize list
print(filtered)  # Expected: [0, 6, 12, 18]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `operator.attrgetter()` to sort a list of objects by an attribute.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1593  
Write a Pythonic way to use `operator.attrgetter()` to sort a list of objects by an attribute.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

from operator import attrgetter  # Import statement: load module or specific functions

class Person:  # Statement block
    def __init__(self, name, age):  # Function definition: __init__
        self.name = name  # Initialize variable or assign value
        self.age = age  # Initialize variable or assign value

people = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 35)]  # Initialize list
sorted_people = sorted(people, key=attrgetter('age'))  # Sort the sequence
print([p.name for p in sorted_people])  # Expected: ['Bob', 'Alice', 'Charlie']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `operator.methodcaller()` to call a method on multiple objects.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1594  
Write a Pythonic way to use `operator.methodcaller()` to call a method on multiple objects.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

from operator import methodcaller  # Import statement: load module or specific functions

class Person:  # Statement block
    def greet(self):  # Function definition: greet
        return "Hello"  # Return the result

people = [Person(), Person(), Person()]  # Initialize list
greetings = list(map(methodcaller('greet'), people))  # Initialize variable or assign value
print(greetings)  # Expected: ['Hello', 'Hello', 'Hello']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `str.removeprefix()` to remove a prefix from a string if it exists.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1595  
Write a Pythonic way to use `str.removeprefix()` to remove a prefix from a string if it exists.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

text = "HelloWorld"  # Initialize string variable
result = text.removeprefix("Hello")  # Initialize variable or assign value
print(result)  # Expected: World




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `str.removesuffix()` to remove a suffix from a string if it exists.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1596  
Write a Pythonic way to use `str.removesuffix()` to remove a suffix from a string if it exists.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

text = "HelloWorld"  # Initialize string variable
result = text.removesuffix("World")  # Initialize variable or assign value
print(result)  # Expected: Hello




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `str.rsplit()` to split a string from the right, limiting the number of splits.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1597  
Write a Pythonic way to use `str.rsplit()` to split a string from the right, limiting the number of splits.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

text = "one.two.three.four"  # Initialize string variable
parts = text.rsplit('.', 2)  # Initialize variable or assign value
print(parts)  # Expected: ['one.two', 'three', 'four']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `list.copy()` to create a shallow copy of a list.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1598  
Write a Pythonic way to use `list.copy()` to create a shallow copy of a list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

original = [1, 2, [3, 4]]  # Initialize list
copied = original.copy()  # Initialize variable or assign value
copied[0] = 10  # Initialize variable or assign value
print(original, copied)  # Expected: [1, 2, [3, 4]] [10, 2, [3, 4]]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `list.clear()` to remove all elements from a list.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1599  
Write a Pythonic way to use `list.clear()` to remove all elements from a list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

my_list = [1, 2, 3, 4, 5]  # Initialize list
my_list.clear()
print(my_list)  # Expected: []




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `dict.popitem()` to remove and return the last key-value pair from a dictionary.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1600  
Write a Pythonic way to use `dict.popitem()` to remove and return the last key-value pair from a dictionary.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

d = {'a': 1, 'b': 2, 'c': 3}  # Initialize dictionary
item = d.popitem()  # Initialize variable or assign value
print(item, d)  # Expected: ('c', 3) {'a': 1, 'b': 2}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `dict.update()` to merge another dictionary into an existing one.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1601  
Write a Pythonic way to use `dict.update()` to merge another dictionary into an existing one.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

dict1 = {'a': 1, 'b': 2}  # Initialize dictionary
dict2 = {'c': 3, 'd': 4}  # Initialize dictionary
dict1.update(dict2)
print(dict1)  # Expected: {'a': 1, 'b': 2, 'c': 3, 'd': 4}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `dict.keys()` to iterate over dictionary keys.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1602  
Write a Pythonic way to use `dict.keys()` to iterate over dictionary keys.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

d = {'a': 1, 'b': 2, 'c': 3}  # Initialize dictionary
keys = list(d.keys())  # Initialize variable or assign value
print(keys)  # Expected: ['a', 'b', 'c']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `dict.values()` to get all values from a dictionary as a view.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1603  
Write a Pythonic way to use `dict.values()` to get all values from a dictionary as a view.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

d = {'a': 1, 'b': 2, 'c': 3}  # Initialize dictionary
values = list(d.values())  # Initialize variable or assign value
print(values)  # Expected: [1, 2, 3]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `dict.items()` to iterate over key-value pairs in a dictionary.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1604  
Write a Pythonic way to use `dict.items()` to iterate over key-value pairs in a dictionary.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

d = {'a': 1, 'b': 2, 'c': 3}  # Initialize dictionary
items = list(d.items())  # Initialize variable or assign value
print(items)  # Expected: [('a', 1), ('b', 2), ('c', 3)]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to define a custom exception class that inherits from Exception.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1605  
Write a Python program to define a custom exception class that inherits from Exception.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

class CustomError(Exception):  # Statement block
    pass

try:  # Statement block
    raise CustomError("This is a custom error")
except CustomError as e:  # Statement block
    print(f"Caught: {e}")  # Expected: Caught: This is a custom error




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program using exception chaining with `raise...from` to preserve the original exception.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1606  
Write a Python program using exception chaining with `raise...from` to preserve the original exception.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

try:  # Statement block
    try:  # Statement block
        int("not a number")
    except ValueError as e:  # Statement block
        raise TypeError("Conversion failed") from e
except TypeError as e:  # Statement block
    print(f"Error: {e}, caused by: {e.__cause__}")  # Expected: Error: Conversion failed, caused by: invalid literal for int() with base 10: 'not a number'




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `contextlib.redirect_stdout` to capture print output to a string.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1607  
Write a Pythonic way to use `contextlib.redirect_stdout` to capture print output to a string.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

from contextlib import redirect_stdout  # Import statement: load module or specific functions
from io import StringIO  # Import statement: load module or specific functions

f = StringIO()  # Initialize variable or assign value
with redirect_stdout(f):  # Statement block
    print("Hello, World!")  # Print the result
    print("Python is great!")  # Print the result
output = f.getvalue()  # Initialize variable or assign value
print(f"Captured: {output}")  # Expected: Captured: Hello, World!\nPython is great!\n




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `functools.wraps` to preserve function metadata in a decorator.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1608  
Write a Pythonic way to use `functools.wraps` to preserve function metadata in a decorator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

from functools import wraps  # Import statement: load module or specific functions

def my_decorator(func):  # Function definition: my_decorator
    @wraps(func)
    def wrapper(*args, **kwargs):  # Function definition: wrapper
        return func(*args, **kwargs)  # Return the result
    return wrapper  # Return the result

@my_decorator
def my_function():  # Function definition: my_function
    """This is a docstring."""
    pass

print(my_function.__name__)  # Expected: my_function




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `itertools.accumulate()` with a custom function to calculate cumulative products.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1609  
Write a Pythonic way to use `itertools.accumulate()` with a custom function to calculate cumulative products.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

from itertools import accumulate  # Import statement: load module or specific functions
import operator  # Import statement: load module or specific functions

numbers = [2, 3, 4, 5]  # Initialize list
cumulative_products = list(accumulate(numbers, operator.mul))  # Initialize variable or assign value
print(cumulative_products)  # Expected: [2, 6, 24, 120]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `itertools.combinations_with_replacement()` to generate combinations allowing repeated elements.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1610  
Write a Pythonic way to use `itertools.combinations_with_replacement()` to generate combinations allowing repeated elements.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

from itertools import combinations_with_replacement  # Import statement: load module or specific functions

items = ['a', 'b', 'c']  # Initialize list
combs = list(combinations_with_replacement(items, 2))  # Initialize variable or assign value
print(combs)  # Expected: [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'b'), ('b', 'c'), ('c', 'c')]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `itertools.dropwhile()` to skip elements until a condition is false.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1611  
Write a Pythonic way to use `itertools.dropwhile()` to skip elements until a condition is false.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

from itertools import dropwhile  # Import statement: load module or specific functions

numbers = [1, 2, 3, 4, 5, 6, 7, 8]  # Initialize list
result = list(dropwhile(lambda x: x < 5, numbers))  # Initialize variable or assign value
print(result)  # Expected: [5, 6, 7, 8]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `itertools.takewhile()` to take elements from an iterator while a condition is true.
# 
# This problem demonstrates generators and iterators in Python. Generators are
# functions that yield values instead of returning them, creating an iterator.
# They are memory-efficient for processing large datasets and can be used with
# functions like next() to retrieve values one at a time.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1612  
Write a Pythonic way to use `itertools.takewhile()` to take elements from an iterator while a condition is true.
"""

# SOLUTION EXPLANATION:
# This solution uses generators or iterators to process data efficiently.
# Generators yield values one at a time, making them memory-efficient for
# large datasets.

from itertools import takewhile  # Import statement: load module or specific functions

numbers = [1, 2, 3, 4, 5, 6, 7, 8]  # Initialize list
result = list(takewhile(lambda x: x < 5, numbers))  # Initialize variable or assign value
print(result)  # Expected: [1, 2, 3, 4]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `itertools.starmap()` to apply a function to arguments unpacked from tuples.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1613  
Write a Pythonic way to use `itertools.starmap()` to apply a function to arguments unpacked from tuples.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

from itertools import starmap  # Import statement: load module or specific functions
import operator  # Import statement: load module or specific functions

pairs = [(2, 3), (4, 5), (6, 7)]  # Initialize list
products = list(starmap(operator.mul, pairs))  # Initialize variable or assign value
print(products)  # Expected: [6, 20, 42]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `functools.cmp_to_key()` to convert an old-style comparison function to a key function.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1614  
Write a Pythonic way to use `functools.cmp_to_key()` to convert an old-style comparison function to a key function.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

from functools import cmp_to_key  # Import statement: load module or specific functions

def compare(x, y):  # Function definition: compare
    return y - x  # Reverse order

numbers = [3, 1, 4, 1, 5]  # Initialize list
sorted_nums = sorted(numbers, key=cmp_to_key(compare))  # Sort the sequence
print(sorted_nums)  # Expected: [5, 4, 3, 1, 1]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `functools.singledispatch` to create a function with method overloading based on argument type.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1615  
Write a Pythonic way to use `functools.singledispatch` to create a function with method overloading based on argument type.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

from functools import singledispatch  # Import statement: load module or specific functions

@singledispatch
def process(value):  # Function definition: process
    return f"Unknown type: {type(value).__name__}"  # Return the result

@process.register
def _(value: int):  # Function definition: _
    return f"Integer: {value}"  # Return the result

@process.register
def _(value: str):  # Function definition: _
    return f"String: {value}"  # Return the result

print(process(42), process("hello"))  # Expected: Integer: 42 String: hello




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program using `typing.Dict` to specify a function parameter that accepts a dictionary with string keys and integer values.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1616  
Write a Python program using `typing.Dict` to specify a function parameter that accepts a dictionary with string keys and integer values.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

from typing import Dict  # Import statement: load module or specific functions

def process_scores(scores: Dict[str, int]) -> int:  # Function definition: process_scores
    return sum(scores.values())  # Return the result

result = process_scores({"Alice": 85, "Bob": 90})  # Initialize variable or assign value
print(result)  # Expected: 175




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program using `typing.Tuple` to specify a function that returns a tuple of specific types.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1617  
Write a Python program using `typing.Tuple` to specify a function that returns a tuple of specific types.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

from typing import Tuple  # Import statement: load module or specific functions

def get_name_age() -> Tuple[str, int]:  # Function definition: get_name_age
    return ("Alice", 30)  # Return the result

name, age = get_name_age()  # Initialize variable or assign value
print(f"{name} is {age}")  # Expected: Alice is 30




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program using `typing.Callable` to specify a function parameter that accepts a callable.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1618  
Write a Python program using `typing.Callable` to specify a function parameter that accepts a callable.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

from typing import Callable  # Import statement: load module or specific functions

def apply_operation(x: int, y: int, op: Callable[[int, int], int]) -> int:  # Function definition: apply_operation
    return op(x, y)  # Return the result

result = apply_operation(5, 3, lambda a, b: a * b)  # Initialize variable or assign value
print(result)  # Expected: 15




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program using `match/case` with guards (if conditions) to add additional pattern matching logic.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1619  
Write a Python program using `match/case` with guards (if conditions) to add additional pattern matching logic.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

def categorize(value):  # Function definition: categorize
    match value:  # Statement block
        case x if x < 0:  # Statement block
            return "Negative"  # Return the result
        case x if x == 0:  # Statement block
            return "Zero"  # Return the result
        case x if x > 0:  # Statement block
            return "Positive"  # Return the result

print(categorize(-5), categorize(0), categorize(5))  # Expected: Negative Zero Positive




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program using `match/case` with `_` as a catch-all pattern to handle unmatched cases.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1620  
Write a Python program using `match/case` with `_` as a catch-all pattern to handle unmatched cases.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

def handle_status(code):  # Function definition: handle_status
    match code:  # Statement block
        case 200:  # Statement block
            return "OK"  # Return the result
        case 404:  # Statement block
            return "Not Found"  # Return the result
        case 500:  # Statement block
            return "Server Error"  # Return the result
        case _:  # Statement block
            return "Unknown Status"  # Return the result

print(handle_status(200), handle_status(999))  # Expected: OK Unknown Status




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python class using `@property.deleter` to define behavior when a property is deleted.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1621  
Write a Python class using `@property.deleter` to define behavior when a property is deleted.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

class Person:  # Statement block
    def __init__(self, name):  # Function definition: __init__
        self._name = name  # Initialize variable or assign value
    
    @property
    def name(self):  # Function definition: name
        return self._name  # Return the result
    
    @name.deleter
    def name(self):  # Function definition: name
        print("Deleting name")  # Print the result
        self._name = None  # Initialize variable or assign value

p = Person("Alice")  # Initialize variable or assign value
del p.name
print(p.name)  # Expected: Deleting name, None




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python class implementing `__setitem__` magic method to enable item assignment.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1622  
Write a Python class implementing `__setitem__` magic method to enable item assignment.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

class MyDict:  # Statement block
    def __init__(self):  # Function definition: __init__
        self._data = {}  # Initialize empty list/dict/set
    
    def __setitem__(self, key, value):  # Function definition: __setitem__
        self._data[key] = value  # Initialize variable or assign value
    
    def __getitem__(self, key):  # Function definition: __getitem__
        return self._data[key]  # Return the result

my_dict = MyDict()  # Initialize variable or assign value
my_dict['key'] = 'value'  # Initialize string variable
print(my_dict['key'])  # Expected: value




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python class implementing `__delitem__` magic method to enable item deletion.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1623  
Write a Python class implementing `__delitem__` magic method to enable item deletion.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

class MyList:  # Statement block
    def __init__(self, items):  # Function definition: __init__
        self.items = items  # Initialize variable or assign value
    
    def __delitem__(self, index):  # Function definition: __delitem__
        del self.items[index]

my_list = MyList([1, 2, 3, 4, 5])  # Initialize variable or assign value
del my_list[2]
print(my_list.items)  # Expected: [1, 2, 4, 5]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python class implementing `__contains__` magic method to enable `in` operator support.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1624  
Write a Python class implementing `__contains__` magic method to enable `in` operator support.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

class MyContainer:  # Statement block
    def __init__(self, items):  # Function definition: __init__
        self.items = items  # Initialize variable or assign value
    
    def __contains__(self, item):  # Function definition: __contains__
        return item in self.items  # Return the result

container = MyContainer([1, 2, 3, 4, 5])  # Initialize variable or assign value
print(3 in container)  # Expected: True




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python class implementing `__iter__` and `__next__` magic methods to create a custom iterator.
# 
# This problem demonstrates generators and iterators in Python. Generators are
# functions that yield values instead of returning them, creating an iterator.
# They are memory-efficient for processing large datasets and can be used with
# functions like next() to retrieve values one at a time.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1625  
Write a Python class implementing `__iter__` and `__next__` magic methods to create a custom iterator.
"""

# SOLUTION EXPLANATION:
# This solution uses generators or iterators to process data efficiently.
# Generators yield values one at a time, making them memory-efficient for
# large datasets.

class CountDown:  # Statement block
    def __init__(self, start):  # Function definition: __init__
        self.current = start  # Initialize variable or assign value
    
    def __iter__(self):  # Function definition: __iter__
        return self  # Return the result
    
    def __next__(self):  # Function definition: __next__
        if self.current <= 0:  # Conditional statement: check condition
            raise StopIteration
        self.current -= 1
        return self.current + 1  # Return the result

counter = CountDown(5)  # Initialize variable or assign value
print(list(counter))  # Expected: [5, 4, 3, 2, 1]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program using `contextlib.contextmanager` decorator to create a context manager from a generator function.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1626  
Write a Python program using `contextlib.contextmanager` decorator to create a context manager from a generator function.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

from contextlib import contextmanager  # Import statement: load module or specific functions

@contextmanager
def my_context():  # Function definition: my_context
    print("Entering context")  # Print the result
    yield "context value"
    print("Exiting context")  # Print the result

with my_context() as value:  # Statement block
    print(f"Inside context: {value}")  # Expected: Entering context, Inside context: context value, Exiting context




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `pathlib.Path.read_text()` to read the entire contents of a text file.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1627  
Write a Pythonic way to use `pathlib.Path.read_text()` to read the entire contents of a text file.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

from pathlib import Path  # Import statement: load module or specific functions

# Note: This is a demonstration - file may not exist
# In practice: content = Path("file.txt").read_text()
print("Demonstration: Path('file.txt').read_text() reads file content")  # Print the result




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `pathlib.Path.write_text()` to write text to a file.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1628  
Write a Pythonic way to use `pathlib.Path.write_text()` to write text to a file.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

from pathlib import Path  # Import statement: load module or specific functions

# Note: This is a demonstration - file may not exist
# In practice: Path("file.txt").write_text("Hello, World!")
print("Demonstration: Path('file.txt').write_text('Hello, World!') writes to file")  # Print the result




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `pathlib.Path.glob()` to find all files matching a pattern.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1629  
Write a Pythonic way to use `pathlib.Path.glob()` to find all files matching a pattern.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

from pathlib import Path  # Import statement: load module or specific functions

# Note: This is a demonstration
# In practice: files = list(Path('.').glob('*.py'))
print("Demonstration: Path('.').glob('*.py') finds all .py files")  # Print the result




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program using `json.dump()` to write a Python object to a JSON file.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1630  
Write a Python program using `json.dump()` to write a Python object to a JSON file.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

import json  # Import statement: load module or specific functions
from pathlib import Path  # Import statement: load module or specific functions

data = {"name": "Alice", "age": 30}  # Initialize dictionary
# Note: In practice: json.dump(data, open("data.json", "w"))
print("Demonstration: json.dump(data, open('data.json', 'w')) writes JSON to file")  # Print the result




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program using `json.load()` to read a JSON file and parse it into a Python object.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1631  
Write a Python program using `json.load()` to read a JSON file and parse it into a Python object.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

import json  # Import statement: load module or specific functions

# Note: In practice: data = json.load(open("data.json"))
print("Demonstration: json.load(open('data.json')) reads and parses JSON file")  # Print the result




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program using `re.compile()` to create a compiled regex pattern for repeated use.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1632  
Write a Python program using `re.compile()` to create a compiled regex pattern for repeated use.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

import re  # Import statement: load module or specific functions

pattern = re.compile(r'\d+')  # Initialize variable or assign value
text = "I have 3 cats and 2 dogs"  # Initialize string variable
matches = pattern.findall(text)  # Initialize variable or assign value
print(matches)  # Expected: ['3', '2']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program using `re.split()` to split a string by a regex pattern.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1633  
Write a Python program using `re.split()` to split a string by a regex pattern.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

import re  # Import statement: load module or specific functions

text = "apple,banana;cherry:date"  # Initialize string variable
parts = re.split(r'[,;:]', text)  # Initialize variable or assign value
print(parts)  # Expected: ['apple', 'banana', 'cherry', 'date']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `collections.OrderedDict.move_to_end()` to move a key to the end of an ordered dictionary.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1634  
Write a Pythonic way to use `collections.OrderedDict.move_to_end()` to move a key to the end of an ordered dictionary.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

from collections import OrderedDict  # Import statement: load module or specific functions

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])  # Initialize variable or assign value
od.move_to_end('a')
print(list(od.keys()))  # Expected: ['b', 'c', 'a']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `collections.ChainMap.new_child()` to add a new dictionary to the beginning of a ChainMap.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1635  
Write a Pythonic way to use `collections.ChainMap.new_child()` to add a new dictionary to the beginning of a ChainMap.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

from collections import ChainMap  # Import statement: load module or specific functions

dict1 = {'a': 1, 'b': 2}  # Initialize dictionary
dict2 = {'c': 3}  # Initialize dictionary
chain = ChainMap(dict1)  # Initialize variable or assign value
new_chain = chain.new_child(dict2)  # Initialize variable or assign value
print(dict(new_chain))  # Expected: {'c': 3, 'a': 1, 'b': 2}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `collections.namedtuple._replace()` to create a new namedtuple with updated fields.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1636  
Write a Pythonic way to use `collections.namedtuple._replace()` to create a new namedtuple with updated fields.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

from collections import namedtuple  # Import statement: load module or specific functions

Point = namedtuple('Point', ['x', 'y'])  # Initialize variable or assign value
p1 = Point(3, 4)  # Initialize variable or assign value
p2 = p1._replace(x=10)  # Initialize variable or assign value
print(p1, p2)  # Expected: Point(x=3, y=4) Point(x=10, y=4)




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use a dictionary comprehension with nested loops to create a multiplication table dictionary.
# 
# This problem demonstrates list comprehensions, a concise way to create lists
# in Python. List comprehensions are more readable and often faster than
# equivalent loops. They can include conditional expressions to filter or
# transform elements, making them a powerful tool for data manipulation.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1637  
Write a Pythonic way to use a dictionary comprehension with nested loops to create a multiplication table dictionary.
"""

# SOLUTION EXPLANATION:
# This solution uses a list comprehension to create a new list based on the
# specified conditions. List comprehensions are concise, readable, and often
# more efficient than equivalent loops for creating lists.

table = {f"{i}x{j}": i * j for i in range(1, 4) for j in range(1, 4)}  # Initialize dictionary
print(table)  # Expected: {'1x1': 1, '1x2': 2, ..., '3x3': 9}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use a set comprehension to create a set of unique characters from multiple strings.
# 
# This problem demonstrates list comprehensions, a concise way to create lists
# in Python. List comprehensions are more readable and often faster than
# equivalent loops. They can include conditional expressions to filter or
# transform elements, making them a powerful tool for data manipulation.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1638  
Write a Pythonic way to use a set comprehension to create a set of unique characters from multiple strings.
"""

# SOLUTION EXPLANATION:
# This solution uses a list comprehension to create a new list based on the
# specified conditions. List comprehensions are concise, readable, and often
# more efficient than equivalent loops for creating lists.

strings = ["hello", "world", "python"]  # Initialize list
unique_chars = {char for s in strings for char in s}  # Initialize dictionary
print(sorted(unique_chars))  # Expected: ['d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `operator.add` with `functools.reduce()` to sum a list of numbers.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1639  
Write a Pythonic way to use `operator.add` with `functools.reduce()` to sum a list of numbers.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

from functools import reduce  # Import statement: load module or specific functions
import operator  # Import statement: load module or specific functions

numbers = [1, 2, 3, 4, 5]  # Initialize list
total = reduce(operator.add, numbers)  # Initialize variable or assign value
print(total)  # Expected: 15




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `operator.mul` with `functools.reduce()` to calculate the product of a list.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1640  
Write a Pythonic way to use `operator.mul` with `functools.reduce()` to calculate the product of a list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

from functools import reduce  # Import statement: load module or specific functions
import operator  # Import statement: load module or specific functions

numbers = [2, 3, 4]  # Initialize list
product = reduce(operator.mul, numbers)  # Initialize variable or assign value
print(product)  # Expected: 24




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program using `str.casefold()` to perform case-insensitive string comparison.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1641  
Write a Python program using `str.casefold()` to perform case-insensitive string comparison.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

str1 = "Hello"  # Initialize string variable
str2 = "HELLO"  # Initialize string variable
print(str1.casefold() == str2.casefold())  # Expected: True




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program using `str.encode()` to convert a string to bytes using UTF-8 encoding.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1642  
Write a Python program using `str.encode()` to convert a string to bytes using UTF-8 encoding.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

text = "Hello, World!"  # Initialize string variable
encoded = text.encode('utf-8')  # Initialize variable or assign value
print(encoded)  # Expected: b'Hello, World!'




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program using `bytes.decode()` to convert bytes back to a string.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1643  
Write a Python program using `bytes.decode()` to convert bytes back to a string.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

bytes_data = b'Hello, World!'  # Initialize variable or assign value
decoded = bytes_data.decode('utf-8')  # Initialize variable or assign value
print(decoded)  # Expected: Hello, World!




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `list.extend()` to add multiple elements from an iterable to a list.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1644  
Write a Pythonic way to use `list.extend()` to add multiple elements from an iterable to a list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

my_list = [1, 2, 3]  # Initialize list
my_list.extend([4, 5, 6])
print(my_list)  # Expected: [1, 2, 3, 4, 5, 6]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `list.index()` to find the index of the first occurrence of an element.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1645  
Write a Pythonic way to use `list.index()` to find the index of the first occurrence of an element.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

my_list = [10, 20, 30, 20, 40]  # Initialize list
index = my_list.index(20)  # Initialize variable or assign value
print(index)  # Expected: 1




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `dict.fromkeys()` to create a dictionary with keys from a list and a default value.
# 
# This problem demonstrates the use of default parameters in built-in functions
# like max(), min(), and next(). The default parameter provides a fallback value
# when the function would otherwise raise an error (e.g., on empty sequences).
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1646  
Write a Pythonic way to use `dict.fromkeys()` to create a dictionary with keys from a list and a default value.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

keys = ['a', 'b', 'c']  # Initialize list
d = dict.fromkeys(keys, 0)  # Initialize variable or assign value
print(d)  # Expected: {'a': 0, 'b': 0, 'c': 0}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program using a try-except-else block where the else clause runs only if no exception occurs.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1647  
Write a Python program using a try-except-else block where the else clause runs only if no exception occurs.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

try:  # Statement block
    result = 10 / 2  # Initialize variable or assign value
except ZeroDivisionError:  # Statement block
    print("Division by zero")  # Print the result
else:  # Else clause: execute when condition is false
    print(f"Result: {result}")  # Expected: Result: 5.0




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program using a try-except-finally block where finally always executes regardless of exceptions.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1648  
Write a Python program using a try-except-finally block where finally always executes regardless of exceptions.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

try:  # Statement block
    result = 10 / 0  # Initialize variable or assign value
except ZeroDivisionError:  # Statement block
    print("Caught division by zero")  # Print the result
finally:  # Statement block
    print("This always executes")  # Expected: Caught division by zero, This always executes




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `contextlib.suppress()` with multiple exception types to ignore multiple types of errors.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1649  
Write a Pythonic way to use `contextlib.suppress()` with multiple exception types to ignore multiple types of errors.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

from contextlib import suppress  # Import statement: load module or specific functions

with suppress(ValueError, TypeError, ZeroDivisionError):  # Statement block
    result = int("not a number")  # Would raise ValueError, but suppressed
    print("This won't print")  # Print the result
print("Continues after suppressed exception")  # Expected: Continues after suppressed exception




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `subtract_numbers` that takes two numbers as parameters and returns their difference.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1650  
Write a Python function called `subtract_numbers` that takes two numbers as parameters and returns their difference.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def subtract_numbers(a, b):  # Function definition: subtract_numbers
    return a - b  # Return the result

result = subtract_numbers(10, 3)  # Initialize variable or assign value
print(result)  # Expected: 7




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `divide_numbers` that takes two numbers as parameters and returns their quotient.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1651  
Write a Python function called `divide_numbers` that takes two numbers as parameters and returns their quotient.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def divide_numbers(a, b):  # Function definition: divide_numbers
    return a / b  # Return the result

result = divide_numbers(10, 2)  # Initialize variable or assign value
print(result)  # Expected: 5.0




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_remainder` that takes two numbers as parameters and returns the remainder when the first number is divided by the second.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1652  
Write a Python function called `calculate_remainder` that takes two numbers as parameters and returns the remainder when the first number is divided by the second.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def calculate_remainder(a, b):  # Function definition: calculate_remainder
    return a % b  # Return the result

result = calculate_remainder(10, 3)  # Initialize variable or assign value
print(result)  # Expected: 1




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_power` that takes a base and exponent as parameters and returns the base raised to the exponent.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1653  
Write a Python function called `calculate_power` that takes a base and exponent as parameters and returns the base raised to the exponent.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def calculate_power(base, exponent):  # Function definition: calculate_power
    return base ** exponent  # Return the result

result = calculate_power(2, 3)  # Initialize variable or assign value
print(result)  # Expected: 8




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_circle_area` that takes the radius as a parameter and returns the area of a circle (use 3.14 for pi).
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1654  
Write a Python function called `calculate_circle_area` that takes the radius as a parameter and returns the area of a circle (use 3.14 for pi).
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def calculate_circle_area(radius):  # Function definition: calculate_circle_area
    return 3.14 * radius * radius  # Return the result

result = calculate_circle_area(5)  # Initialize variable or assign value
print(result)  # Expected: 78.5




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_rectangle_area` that takes length and width as parameters and returns the area of a rectangle.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1655  
Write a Python function called `calculate_rectangle_area` that takes length and width as parameters and returns the area of a rectangle.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def calculate_rectangle_area(length, width):  # Function definition: calculate_rectangle_area
    return length * width  # Return the result

result = calculate_rectangle_area(5, 3)  # Initialize variable or assign value
print(result)  # Expected: 15




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_triangle_area` that takes base and height as parameters and returns the area of a triangle.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1656  
Write a Python function called `calculate_triangle_area` that takes base and height as parameters and returns the area of a triangle.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def calculate_triangle_area(base, height):  # Function definition: calculate_triangle_area
    return 0.5 * base * height  # Return the result

result = calculate_triangle_area(4, 6)  # Initialize variable or assign value
print(result)  # Expected: 12.0




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `convert_celsius_to_fahrenheit` that takes a temperature in Celsius and returns it converted to Fahrenheit.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1657  
Write a Python function called `convert_celsius_to_fahrenheit` that takes a temperature in Celsius and returns it converted to Fahrenheit.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def convert_celsius_to_fahrenheit(celsius):  # Function definition: convert_celsius_to_fahrenheit
    return (celsius * 9/5) + 32  # Return the result

result = convert_celsius_to_fahrenheit(25)  # Initialize variable or assign value
print(result)  # Expected: 77.0




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `convert_fahrenheit_to_celsius` that takes a temperature in Fahrenheit and returns it converted to Celsius.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1658  
Write a Python function called `convert_fahrenheit_to_celsius` that takes a temperature in Fahrenheit and returns it converted to Celsius.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def convert_fahrenheit_to_celsius(fahrenheit):  # Function definition: convert_fahrenheit_to_celsius
    return (fahrenheit - 32) * 5/9  # Return the result

result = convert_fahrenheit_to_celsius(77)  # Initialize variable or assign value
print(result)  # Expected: 25.0




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `is_positive` that takes a number as input and returns True if the number is positive, and False otherwise.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1659  
Write a Python function called `is_positive` that takes a number as input and returns True if the number is positive, and False otherwise.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def is_positive(number):  # Function definition: is_positive
    return number > 0  # Return the result

print(is_positive(5), is_positive(-3))  # Expected: True False




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `is_negative` that takes a number as input and returns True if the number is negative, and False otherwise.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1660  
Write a Python function called `is_negative` that takes a number as input and returns True if the number is negative, and False otherwise.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def is_negative(number):  # Function definition: is_negative
    return number < 0  # Return the result

print(is_negative(-5), is_negative(3))  # Expected: True False




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_first_char` that takes a string as input and returns the first character of the string.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1661  
Write a Python function called `get_first_char` that takes a string as input and returns the first character of the string.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_first_char(text):  # Function definition: get_first_char
    return text[0]  # Return the result

result = get_first_char("Hello")  # Initialize variable or assign value
print(result)  # Expected: H




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_last_char` that takes a string as input and returns the last character of the string.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1662  
Write a Python function called `get_last_char` that takes a string as input and returns the last character of the string.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_last_char(text):  # Function definition: get_last_char
    return text[-1]  # Return the result

result = get_last_char("Hello")  # Initialize variable or assign value
print(result)  # Expected: o




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_middle_char` that takes a string as input and returns the middle character. If the string has even length, return the character at index length//2.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1663  
Write a Python function called `get_middle_char` that takes a string as input and returns the middle character. If the string has even length, return the character at index length//2.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_middle_char(text):  # Function definition: get_middle_char
    return text[len(text) // 2]  # Return the result

result = get_middle_char("Hello")  # Initialize variable or assign value
print(result)  # Expected: l




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `repeat_string` that takes a string and a number n, and returns the string repeated n times.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1664  
Write a Python function called `repeat_string` that takes a string and a number n, and returns the string repeated n times.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def repeat_string(text, n):  # Function definition: repeat_string
    return text * n  # Return the result

result = repeat_string("Hi", 3)  # Initialize variable or assign value
print(result)  # Expected: HiHiHi




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `swap_first_last` that takes a string as input and returns a new string with the first and last characters swapped.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1665  
Write a Python function called `swap_first_last` that takes a string as input and returns a new string with the first and last characters swapped.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def swap_first_last(text):  # Function definition: swap_first_last
    if len(text) <= 1:  # Conditional statement: check condition
        return text  # Return the result
    return text[-1] + text[1:-1] + text[0]  # Return the result

result = swap_first_last("Hello")  # Initialize variable or assign value
print(result)  # Expected: oellH




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `remove_first_char` that takes a string as input and returns the string with the first character removed.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1666  
Write a Python function called `remove_first_char` that takes a string as input and returns the string with the first character removed.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def remove_first_char(text):  # Function definition: remove_first_char
    return text[1:]  # Return the result

result = remove_first_char("Hello")  # Initialize variable or assign value
print(result)  # Expected: ello




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `remove_last_char` that takes a string as input and returns the string with the last character removed.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1667  
Write a Python function called `remove_last_char` that takes a string as input and returns the string with the last character removed.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def remove_last_char(text):  # Function definition: remove_last_char
    return text[:-1]  # Return the result

result = remove_last_char("Hello")  # Initialize variable or assign value
print(result)  # Expected: Hell




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_first_word` that takes a string of words separated by spaces and returns the first word.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1668  
Write a Python function called `get_first_word` that takes a string of words separated by spaces and returns the first word.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_first_word(text):  # Function definition: get_first_word
    return text.split()[0]  # Return the result

result = get_first_word("Hello World Python")  # Initialize variable or assign value
print(result)  # Expected: Hello




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_last_word` that takes a string of words separated by spaces and returns the last word.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1669  
Write a Python function called `get_last_word` that takes a string of words separated by spaces and returns the last word.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_last_word(text):  # Function definition: get_last_word
    return text.split()[-1]  # Return the result

result = get_last_word("Hello World Python")  # Initialize variable or assign value
print(result)  # Expected: Python




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `count_characters` that takes a string as input and returns the number of characters in the string (excluding spaces).
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1670  
Write a Python function called `count_characters` that takes a string as input and returns the number of characters in the string (excluding spaces).
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def count_characters(text):  # Function definition: count_characters
    return len(text.replace(" ", ""))  # Return the result

result = count_characters("Hello World")  # Initialize variable or assign value
print(result)  # Expected: 10




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `add_to_list` that takes a list and an element, and returns a new list with the element added at the end.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1671  
Write a Python function called `add_to_list` that takes a list and an element, and returns a new list with the element added at the end.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def add_to_list(my_list, element):  # Function definition: add_to_list
    new_list = my_list.copy()  # Initialize variable or assign value
    new_list.append(element)  # Add element to list
    return new_list  # Return the result

result = add_to_list([1, 2, 3], 4)  # Initialize variable or assign value
print(result)  # Expected: [1, 2, 3, 4]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_first_element` that takes a list and returns the first element of the list.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1672  
Write a Python function called `get_first_element` that takes a list and returns the first element of the list.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_first_element(my_list):  # Function definition: get_first_element
    return my_list[0]  # Return the result

result = get_first_element([10, 20, 30])  # Initialize variable or assign value
print(result)  # Expected: 10




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_last_element` that takes a list and returns the last element of the list.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1673  
Write a Python function called `get_last_element` that takes a list and returns the last element of the list.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_last_element(my_list):  # Function definition: get_last_element
    return my_list[-1]  # Return the result

result = get_last_element([10, 20, 30])  # Initialize variable or assign value
print(result)  # Expected: 30




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_middle_element` that takes a list and returns the middle element. If the list has even length, return the element at index length//2.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1674  
Write a Python function called `get_middle_element` that takes a list and returns the middle element. If the list has even length, return the element at index length//2.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_middle_element(my_list):  # Function definition: get_middle_element
    return my_list[len(my_list) // 2]  # Return the result

result = get_middle_element([10, 20, 30, 40, 50])  # Initialize variable or assign value
print(result)  # Expected: 30




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `remove_first_element` that takes a list and returns a new list with the first element removed.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1675  
Write a Python function called `remove_first_element` that takes a list and returns a new list with the first element removed.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def remove_first_element(my_list):  # Function definition: remove_first_element
    return my_list[1:]  # Return the result

result = remove_first_element([10, 20, 30])  # Initialize variable or assign value
print(result)  # Expected: [20, 30]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `remove_last_element` that takes a list and returns a new list with the last element removed.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1676  
Write a Python function called `remove_last_element` that takes a list and returns a new list with the last element removed.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def remove_last_element(my_list):  # Function definition: remove_last_element
    return my_list[:-1]  # Return the result

result = remove_last_element([10, 20, 30])  # Initialize variable or assign value
print(result)  # Expected: [10, 20]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_list_slice` that takes a list, start index, and end index, and returns a slice of the list from start to end.
# 
# This problem demonstrates Python's slicing syntax, which allows you to extract
# portions of sequences (strings, lists, tuples) using indices. Slicing uses the
# format [start:stop:step] where start is inclusive, stop is exclusive, and step
# determines the increment. Negative indices count from the end, and omitting
# indices allows you to slice from the beginning or to the end.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1677  
Write a Python function called `get_list_slice` that takes a list, start index, and end index, and returns a slice of the list from start to end.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax to extract the desired portion
# of the sequence. Slicing is efficient and readable, making it the preferred
# method for extracting subsequences from strings, lists, and tuples.

def get_list_slice(my_list, start, end):  # Function definition: get_list_slice
    return my_list[start:end]  # Return the result

result = get_list_slice([10, 20, 30, 40, 50], 1, 4)  # Initialize variable or assign value
print(result)  # Expected: [20, 30, 40]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `combine_lists` that takes two lists and returns a new list containing all elements from both lists.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1678  
Write a Python function called `combine_lists` that takes two lists and returns a new list containing all elements from both lists.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def combine_lists(list1, list2):  # Function definition: combine_lists
    return list1 + list2  # Return the result

result = combine_lists([1, 2, 3], [4, 5, 6])  # Initialize variable or assign value
print(result)  # Expected: [1, 2, 3, 4, 5, 6]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `multiply_list` that takes a list of numbers and returns a new list where each number is multiplied by 2.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1679  
Write a Python function called `multiply_list` that takes a list of numbers and returns a new list where each number is multiplied by 2.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def multiply_list(numbers):  # Function definition: multiply_list
    return [x * 2 for x in numbers]  # Return the result

result = multiply_list([1, 2, 3, 4])  # Initialize variable or assign value
print(result)  # Expected: [2, 4, 6, 8]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `add_one_to_all` that takes a list of numbers and returns a new list where 1 is added to each number.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1680  
Write a Python function called `add_one_to_all` that takes a list of numbers and returns a new list where 1 is added to each number.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def add_one_to_all(numbers):  # Function definition: add_one_to_all
    return [x + 1 for x in numbers]  # Return the result

result = add_one_to_all([1, 2, 3, 4])  # Initialize variable or assign value
print(result)  # Expected: [2, 3, 4, 5]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to print numbers from 1 to 10 using a for loop.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1681  
Write a Python program to print numbers from 1 to 10 using a for loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

for i in range(1, 11):  # Loop: iterate over sequence
    print(i)  # Expected: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to print all even numbers from 1 to 20 using a for loop.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1682  
Write a Python program to print all even numbers from 1 to 20 using a for loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

for i in range(1, 21):  # Loop: iterate over sequence
    if i % 2 == 0:  # Conditional statement: check condition
        print(i)  # Expected: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to print all odd numbers from 1 to 20 using a for loop.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1683  
Write a Python program to print all odd numbers from 1 to 20 using a for loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

for i in range(1, 21):  # Loop: iterate over sequence
    if i % 2 != 0:  # Conditional statement: check condition
        print(i)  # Expected: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to print the multiplication table of 5 from 1 to 10 using a for loop.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1684  
Write a Python program to print the multiplication table of 5 from 1 to 10 using a for loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

for i in range(1, 11):  # Loop: iterate over sequence
    print(f"5 x {i} = {5 * i}")  # Expected: 5 x 1 = 5, 5 x 2 = 10, ..., 5 x 10 = 50




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to print each character of a string on a separate line using a for loop.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1685  
Write a Python program to print each character of a string on a separate line using a for loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

text = "Hello"  # Initialize string variable
for char in text:  # Loop: iterate over sequence
    print(char)  # Expected: H, e, l, l, o (each on new line)




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to print each element of a list on a separate line using a for loop.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1686  
Write a Python program to print each element of a list on a separate line using a for loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

my_list = [10, 20, 30]  # Initialize list
for element in my_list:  # Loop: iterate over sequence
    print(element)  # Expected: 10, 20, 30 (each on new line)




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to calculate the sum of numbers from 1 to 10 using a for loop.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1687  
Write a Python program to calculate the sum of numbers from 1 to 10 using a for loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

total = 0  # Initialize variable or assign value
for i in range(1, 11):  # Loop: iterate over sequence
    total += i
print(total)  # Expected: 55




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to calculate the product of numbers from 1 to 5 using a for loop.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1688  
Write a Python program to calculate the product of numbers from 1 to 5 using a for loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

product = 1  # Initialize variable or assign value
for i in range(1, 6):  # Loop: iterate over sequence
    product *= i
print(product)  # Expected: 120




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to count from 10 down to 1 using a for loop.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1689  
Write a Python program to count from 10 down to 1 using a for loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

for i in range(10, 0, -1):  # Loop: iterate over sequence
    print(i)  # Expected: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to print numbers from 0 to 20 that are divisible by 3 using a for loop.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1690  
Write a Python program to print numbers from 0 to 20 that are divisible by 3 using a for loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

for i in range(0, 21):  # Loop: iterate over sequence
    if i % 3 == 0:  # Conditional statement: check condition
        print(i)  # Expected: 0, 3, 6, 9, 12, 15, 18




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program using a while loop to print numbers from 1 to 5.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1691  
Write a Python program using a while loop to print numbers from 1 to 5.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

i = 1  # Initialize variable or assign value
while i <= 5:  # Loop: iterate while condition is true
    print(i)  # Print the result
    i += 1  # Expected: 1, 2, 3, 4, 5




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program using a while loop to calculate the sum of numbers from 1 to 10.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1692  
Write a Python program using a while loop to calculate the sum of numbers from 1 to 10.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

total = 0  # Initialize variable or assign value
i = 1  # Initialize variable or assign value
while i <= 10:  # Loop: iterate while condition is true
    total += i
    i += 1
print(total)  # Expected: 55




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program using a while loop to print all even numbers from 2 to 20.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1693  
Write a Python program using a while loop to print all even numbers from 2 to 20.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

i = 2  # Initialize variable or assign value
while i <= 20:  # Loop: iterate while condition is true
    print(i)  # Print the result
    i += 2  # Expected: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program using a while loop to count down from 10 to 1.
# 
# This problem demonstrates fundamental Python programming concepts and syntax.
# Understanding these concepts is essential for writing effective Python programs
# and solving various programming challenges.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1694  
Write a Python program using a while loop to count down from 10 to 1.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

i = 10  # Initialize variable or assign value
while i >= 1:  # Loop: iterate while condition is true
    print(i)  # Print the result
    i -= 1  # Expected: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_greater` that takes two numbers and returns True if the first number is greater than the second, otherwise False.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1695  
Write a Python function called `check_greater` that takes two numbers and returns True if the first number is greater than the second, otherwise False.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_greater(a, b):  # Function definition: check_greater
    return a > b  # Return the result

print(check_greater(5, 3), check_greater(2, 4))  # Expected: True False




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_less` that takes two numbers and returns True if the first number is less than the second, otherwise False.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1696  
Write a Python function called `check_less` that takes two numbers and returns True if the first number is less than the second, otherwise False.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_less(a, b):  # Function definition: check_less
    return a < b  # Return the result

print(check_less(3, 5), check_less(5, 3))  # Expected: True False




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_equal` that takes two values and returns True if they are equal, otherwise False.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1697  
Write a Python function called `check_equal` that takes two values and returns True if they are equal, otherwise False.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_equal(a, b):  # Function definition: check_equal
    return a == b  # Return the result

print(check_equal(5, 5), check_equal(5, 3))  # Expected: True False




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_not_equal` that takes two values and returns True if they are not equal, otherwise False.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1698  
Write a Python function called `check_not_equal` that takes two values and returns True if they are not equal, otherwise False.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_not_equal(a, b):  # Function definition: check_not_equal
    return a != b  # Return the result

print(check_not_equal(5, 3), check_not_equal(5, 5))  # Expected: True False




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_greater_equal` that takes two numbers and returns True if the first number is greater than or equal to the second, otherwise False.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1699  
Write a Python function called `check_greater_equal` that takes two numbers and returns True if the first number is greater than or equal to the second, otherwise False.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_greater_equal(a, b):  # Function definition: check_greater_equal
    return a >= b  # Return the result

print(check_greater_equal(5, 5), check_greater_equal(3, 5))  # Expected: True False




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_less_equal` that takes two numbers and returns True if the first number is less than or equal to the second, otherwise False.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1700  
Write a Python function called `check_less_equal` that takes two numbers and returns True if the first number is less than or equal to the second, otherwise False.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_less_equal(a, b):  # Function definition: check_less_equal
    return a <= b  # Return the result

print(check_less_equal(3, 5), check_less_equal(5, 3))  # Expected: True False




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_absolute_value` that takes a number and returns its absolute value.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1701  
Write a Python function called `get_absolute_value` that takes a number and returns its absolute value.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_absolute_value(number):  # Function definition: get_absolute_value
    return abs(number)  # Return the result

print(get_absolute_value(-5), get_absolute_value(5))  # Expected: 5 5




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `round_number` that takes a number and returns it rounded to the nearest integer.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1702  
Write a Python function called `round_number` that takes a number and returns it rounded to the nearest integer.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def round_number(number):  # Function definition: round_number
    return round(number)  # Return the result

print(round_number(3.7), round_number(3.2))  # Expected: 4 3




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_maximum` that takes three numbers and returns the largest one.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1703  
Write a Python function called `get_maximum` that takes three numbers and returns the largest one.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_maximum(a, b, c):  # Function definition: get_maximum
    return max(a, b, c)  # Return the result

result = get_maximum(10, 5, 8)  # Initialize variable or assign value
print(result)  # Expected: 10




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_minimum` that takes three numbers and returns the smallest one.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1704  
Write a Python function called `get_minimum` that takes three numbers and returns the smallest one.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_minimum(a, b, c):  # Function definition: get_minimum
    return min(a, b, c)  # Return the result

result = get_minimum(10, 5, 8)  # Initialize variable or assign value
print(result)  # Expected: 5




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_divisible` that takes two numbers and returns True if the first number is divisible by the second, otherwise False.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1705  
Write a Python function called `check_divisible` that takes two numbers and returns True if the first number is divisible by the second, otherwise False.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_divisible(a, b):  # Function definition: check_divisible
    return a % b == 0  # Return the result

print(check_divisible(10, 2), check_divisible(10, 3))  # Expected: True False




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `convert_to_string` that takes a number and returns it as a string.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1706  
Write a Python function called `convert_to_string` that takes a number and returns it as a string.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def convert_to_string(number):  # Function definition: convert_to_string
    return str(number)  # Return the result

result = convert_to_string(123)  # Initialize variable or assign value
print(result, type(result))  # Expected: 123 <class 'str'>




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `convert_to_integer` that takes a string containing a number and returns it as an integer.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1707  
Write a Python function called `convert_to_integer` that takes a string containing a number and returns it as an integer.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def convert_to_integer(text):  # Function definition: convert_to_integer
    return int(text)  # Return the result

result = convert_to_integer("123")  # Initialize variable or assign value
print(result, type(result))  # Expected: 123 <class 'int'>




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `convert_to_float` that takes a string containing a number and returns it as a float.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1708  
Write a Python function called `convert_to_float` that takes a string containing a number and returns it as a float.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def convert_to_float(text):  # Function definition: convert_to_float
    return float(text)  # Return the result

result = convert_to_float("3.14")  # Initialize variable or assign value
print(result, type(result))  # Expected: 3.14 <class 'float'>




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_type` that takes a value and returns its data type as a string.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1709  
Write a Python function called `get_type` that takes a value and returns its data type as a string.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_type(value):  # Function definition: get_type
    return str(type(value).__name__)  # Return the result

print(get_type(5), get_type("hello"))  # Expected: int str




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_is_integer` that takes a value and returns True if it is an integer, otherwise False.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1710  
Write a Python function called `check_is_integer` that takes a value and returns True if it is an integer, otherwise False.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_is_integer(value):  # Function definition: check_is_integer
    return isinstance(value, int)  # Return the result

print(check_is_integer(5), check_is_integer("5"))  # Expected: True False




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_is_string` that takes a value and returns True if it is a string, otherwise False.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1711  
Write a Python function called `check_is_string` that takes a value and returns True if it is a string, otherwise False.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_is_string(value):  # Function definition: check_is_string
    return isinstance(value, str)  # Return the result

print(check_is_string("hello"), check_is_string(5))  # Expected: True False




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_is_list` that takes a value and returns True if it is a list, otherwise False.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1712  
Write a Python function called `check_is_list` that takes a value and returns True if it is a list, otherwise False.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_is_list(value):  # Function definition: check_is_list
    return isinstance(value, list)  # Return the result

print(check_is_list([1, 2, 3]), check_is_list("hello"))  # Expected: True False




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `format_greeting` that takes a name and returns a greeting message using an f-string: 'Hello, {name}!'.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1713  
Write a Python function called `format_greeting` that takes a name and returns a greeting message using an f-string: 'Hello, {name}!'.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def format_greeting(name):  # Function definition: format_greeting
    return f"Hello, {name}!"  # Return the result

result = format_greeting("Alice")  # Initialize variable or assign value
print(result)  # Expected: Hello, Alice!




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `format_age_message` that takes a name and age, and returns a message using an f-string: '{name} is {age} years old.'.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1714  
Write a Python function called `format_age_message` that takes a name and age, and returns a message using an f-string: '{name} is {age} years old.'.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def format_age_message(name, age):  # Function definition: format_age_message
    return f"{name} is {age} years old."  # Return the result

result = format_age_message("Bob", 25)  # Initialize variable or assign value
print(result)  # Expected: Bob is 25 years old.




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `format_calculation` that takes two numbers and returns a formatted string showing their sum: '{num1} + {num2} = {sum}'.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1715  
Write a Python function called `format_calculation` that takes two numbers and returns a formatted string showing their sum: '{num1} + {num2} = {sum}'.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def format_calculation(num1, num2):  # Function definition: format_calculation
    return f"{num1} + {num2} = {num1 + num2}"  # Return the result

result = format_calculation(5, 3)  # Initialize variable or assign value
print(result)  # Expected: 5 + 3 = 8




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_perimeter_rectangle` that takes length and width and returns the perimeter of a rectangle.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1716  
Write a Python function called `calculate_perimeter_rectangle` that takes length and width and returns the perimeter of a rectangle.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def calculate_perimeter_rectangle(length, width):  # Function definition: calculate_perimeter_rectangle
    return 2 * (length + width)  # Return the result

result = calculate_perimeter_rectangle(5, 3)  # Initialize variable or assign value
print(result)  # Expected: 16




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_perimeter_square` that takes the side length and returns the perimeter of a square.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1717  
Write a Python function called `calculate_perimeter_square` that takes the side length and returns the perimeter of a square.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def calculate_perimeter_square(side):  # Function definition: calculate_perimeter_square
    return 4 * side  # Return the result

result = calculate_perimeter_square(5)  # Initialize variable or assign value
print(result)  # Expected: 20




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_circle_circumference` that takes the radius and returns the circumference of a circle (use 3.14 for pi).
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1718  
Write a Python function called `calculate_circle_circumference` that takes the radius and returns the circumference of a circle (use 3.14 for pi).
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def calculate_circle_circumference(radius):  # Function definition: calculate_circle_circumference
    return 2 * 3.14 * radius  # Return the result

result = calculate_circle_circumference(5)  # Initialize variable or assign value
print(result)  # Expected: 31.4




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `convert_km_to_miles` that takes a distance in kilometers and returns it converted to miles (1 km = 0.621371 miles).
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1719  
Write a Python function called `convert_km_to_miles` that takes a distance in kilometers and returns it converted to miles (1 km = 0.621371 miles).
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def convert_km_to_miles(km):  # Function definition: convert_km_to_miles
    return km * 0.621371  # Return the result

result = convert_km_to_miles(10)  # Initialize variable or assign value
print(result)  # Expected: 6.21371




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `convert_miles_to_km` that takes a distance in miles and returns it converted to kilometers.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1720  
Write a Python function called `convert_miles_to_km` that takes a distance in miles and returns it converted to kilometers.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def convert_miles_to_km(miles):  # Function definition: convert_miles_to_km
    return miles / 0.621371  # Return the result

result = convert_miles_to_km(6.21371)  # Initialize variable or assign value
print(round(result, 2))  # Expected: 10.0




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `convert_kg_to_pounds` that takes a weight in kilograms and returns it converted to pounds (1 kg = 2.20462 pounds).
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1721  
Write a Python function called `convert_kg_to_pounds` that takes a weight in kilograms and returns it converted to pounds (1 kg = 2.20462 pounds).
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def convert_kg_to_pounds(kg):  # Function definition: convert_kg_to_pounds
    return kg * 2.20462  # Return the result

result = convert_kg_to_pounds(10)  # Initialize variable or assign value
print(result)  # Expected: 22.0462




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `convert_pounds_to_kg` that takes a weight in pounds and returns it converted to kilograms.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1722  
Write a Python function called `convert_pounds_to_kg` that takes a weight in pounds and returns it converted to kilograms.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def convert_pounds_to_kg(pounds):  # Function definition: convert_pounds_to_kg
    return pounds / 2.20462  # Return the result

result = convert_pounds_to_kg(22.0462)  # Initialize variable or assign value
print(round(result, 2))  # Expected: 10.0




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_vowel` that takes a character and returns True if it is a vowel (a, e, i, o, u), otherwise False.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1723  
Write a Python function called `check_vowel` that takes a character and returns True if it is a vowel (a, e, i, o, u), otherwise False.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_vowel(char):  # Function definition: check_vowel
    return char.lower() in 'aeiou'  # Return the result

print(check_vowel('a'), check_vowel('b'))  # Expected: True False




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_consonant` that takes a character and returns True if it is a consonant, otherwise False.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1724  
Write a Python function called `check_consonant` that takes a character and returns True if it is a consonant, otherwise False.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_consonant(char):  # Function definition: check_consonant
    return char.isalpha() and char.lower() not in 'aeiou'  # Return the result

print(check_consonant('b'), check_consonant('a'))  # Expected: True False




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_digit` that takes a character and returns True if it is a digit (0-9), otherwise False.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1725  
Write a Python function called `check_digit` that takes a character and returns True if it is a digit (0-9), otherwise False.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_digit(char):  # Function definition: check_digit
    return char.isdigit()  # Return the result

print(check_digit('5'), check_digit('a'))  # Expected: True False




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_letter` that takes a character and returns True if it is a letter (a-z or A-Z), otherwise False.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1726  
Write a Python function called `check_letter` that takes a character and returns True if it is a letter (a-z or A-Z), otherwise False.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_letter(char):  # Function definition: check_letter
    return char.isalpha()  # Return the result

print(check_letter('a'), check_letter('5'))  # Expected: True False




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_uppercase` that takes a character and returns True if it is uppercase, otherwise False.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1727  
Write a Python function called `check_uppercase` that takes a character and returns True if it is uppercase, otherwise False.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_uppercase(char):  # Function definition: check_uppercase
    return char.isupper()  # Return the result

print(check_uppercase('A'), check_uppercase('a'))  # Expected: True False




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_lowercase` that takes a character and returns True if it is lowercase, otherwise False.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1728  
Write a Python function called `check_lowercase` that takes a character and returns True if it is lowercase, otherwise False.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_lowercase(char):  # Function definition: check_lowercase
    return char.islower()  # Return the result

print(check_lowercase('a'), check_lowercase('A'))  # Expected: True False




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `find_char_index` that takes a string and a character, and returns the index of the first occurrence of the character in the string, or -1 if not found.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1729  
Write a Python function called `find_char_index` that takes a string and a character, and returns the index of the first occurrence of the character in the string, or -1 if not found.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def find_char_index(text, char):  # Function definition: find_char_index
    return text.find(char)  # Return the result

print(find_char_index("Hello", "e"), find_char_index("Hello", "x"))  # Expected: 1 -1




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `count_char_in_string` that takes a string and a character, and returns how many times the character appears in the string.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1730  
Write a Python function called `count_char_in_string` that takes a string and a character, and returns how many times the character appears in the string.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def count_char_in_string(text, char):  # Function definition: count_char_in_string
    return text.count(char)  # Return the result

result = count_char_in_string("Hello", "l")  # Initialize variable or assign value
print(result)  # Expected: 2




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_starts_with` that takes a string and a prefix, and returns True if the string starts with the prefix, otherwise False.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1731  
Write a Python function called `check_starts_with` that takes a string and a prefix, and returns True if the string starts with the prefix, otherwise False.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_starts_with(text, prefix):  # Function definition: check_starts_with
    return text.startswith(prefix)  # Return the result

print(check_starts_with("Hello", "He"), check_starts_with("Hello", "lo"))  # Expected: True False




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_ends_with` that takes a string and a suffix, and returns True if the string ends with the suffix, otherwise False.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1732  
Write a Python function called `check_ends_with` that takes a string and a suffix, and returns True if the string ends with the suffix, otherwise False.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_ends_with(text, suffix):  # Function definition: check_ends_with
    return text.endswith(suffix)  # Return the result

print(check_ends_with("Hello", "lo"), check_ends_with("Hello", "He"))  # Expected: True False




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `replace_char` that takes a string, old character, and new character, and returns a new string with all occurrences of old character replaced with new character.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1733  
Write a Python function called `replace_char` that takes a string, old character, and new character, and returns a new string with all occurrences of old character replaced with new character.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def replace_char(text, old_char, new_char):  # Function definition: replace_char
    return text.replace(old_char, new_char)  # Return the result

result = replace_char("Hello", "l", "x")  # Initialize variable or assign value
print(result)  # Expected: Hexxo




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `remove_char` that takes a string and a character, and returns a new string with all occurrences of that character removed.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1734  
Write a Python function called `remove_char` that takes a string and a character, and returns a new string with all occurrences of that character removed.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def remove_char(text, char):  # Function definition: remove_char
    return text.replace(char, "")  # Return the result

result = remove_char("Hello", "l")  # Initialize variable or assign value
print(result)  # Expected: Heo




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_substring` that takes a string, start index, and end index, and returns the substring from start to end (not including end).
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1735  
Write a Python function called `get_substring` that takes a string, start index, and end index, and returns the substring from start to end (not including end).
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_substring(text, start, end):  # Function definition: get_substring
    return text[start:end]  # Return the result

result = get_substring("Hello World", 0, 5)  # Initialize variable or assign value
print(result)  # Expected: Hello




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `reverse_list` that takes a list and returns a new list with elements in reverse order.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1736  
Write a Python function called `reverse_list` that takes a list and returns a new list with elements in reverse order.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def reverse_list(my_list):  # Function definition: reverse_list
    return my_list[::-1]  # Return the result

result = reverse_list([1, 2, 3, 4])  # Initialize variable or assign value
print(result)  # Expected: [4, 3, 2, 1]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_list_length` that takes a list and returns the number of elements in the list.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1737  
Write a Python function called `get_list_length` that takes a list and returns the number of elements in the list.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_list_length(my_list):  # Function definition: get_list_length
    return len(my_list)  # Return the result

result = get_list_length([1, 2, 3, 4, 5])  # Initialize variable or assign value
print(result)  # Expected: 5




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_element_in_list` that takes a list and an element, and returns True if the element is in the list, otherwise False.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1738  
Write a Python function called `check_element_in_list` that takes a list and an element, and returns True if the element is in the list, otherwise False.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_element_in_list(my_list, element):  # Function definition: check_element_in_list
    return element in my_list  # Return the result

print(check_element_in_list([1, 2, 3], 2), check_element_in_list([1, 2, 3], 5))  # Expected: True False




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_element_count` that takes a list and an element, and returns how many times the element appears in the list.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1739  
Write a Python function called `get_element_count` that takes a list and an element, and returns how many times the element appears in the list.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_element_count(my_list, element):  # Function definition: get_element_count
    return my_list.count(element)  # Return the result

result = get_element_count([1, 2, 2, 3, 2], 2)  # Initialize variable or assign value
print(result)  # Expected: 3




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_element_index` that takes a list and an element, and returns the index of the first occurrence of the element, or -1 if not found.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1740  
Write a Python function called `get_element_index` that takes a list and an element, and returns the index of the first occurrence of the element, or -1 if not found.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_element_index(my_list, element):  # Function definition: get_element_index
    if element in my_list:  # Conditional statement: check condition
        return my_list.index(element)  # Return the result
    return -1  # Return the result

print(get_element_index([10, 20, 30], 20), get_element_index([10, 20, 30], 40))  # Expected: 1 -1




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_even_numbers` that takes a list of numbers and returns a new list containing only the even numbers.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1741  
Write a Python function called `get_even_numbers` that takes a list of numbers and returns a new list containing only the even numbers.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_even_numbers(numbers):  # Function definition: get_even_numbers
    return [x for x in numbers if x % 2 == 0]  # Return the result

result = get_even_numbers([1, 2, 3, 4, 5, 6])  # Initialize variable or assign value
print(result)  # Expected: [2, 4, 6]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_odd_numbers` that takes a list of numbers and returns a new list containing only the odd numbers.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1742  
Write a Python function called `get_odd_numbers` that takes a list of numbers and returns a new list containing only the odd numbers.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_odd_numbers(numbers):  # Function definition: get_odd_numbers
    return [x for x in numbers if x % 2 != 0]  # Return the result

result = get_odd_numbers([1, 2, 3, 4, 5, 6])  # Initialize variable or assign value
print(result)  # Expected: [1, 3, 5]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_positive_numbers` that takes a list of numbers and returns a new list containing only the positive numbers.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1743  
Write a Python function called `get_positive_numbers` that takes a list of numbers and returns a new list containing only the positive numbers.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_positive_numbers(numbers):  # Function definition: get_positive_numbers
    return [x for x in numbers if x > 0]  # Return the result

result = get_positive_numbers([-2, -1, 0, 1, 2, 3])  # Initialize variable or assign value
print(result)  # Expected: [1, 2, 3]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_negative_numbers` that takes a list of numbers and returns a new list containing only the negative numbers.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1744  
Write a Python function called `get_negative_numbers` that takes a list of numbers and returns a new list containing only the negative numbers.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_negative_numbers(numbers):  # Function definition: get_negative_numbers
    return [x for x in numbers if x < 0]  # Return the result

result = get_negative_numbers([-2, -1, 0, 1, 2, 3])  # Initialize variable or assign value
print(result)  # Expected: [-2, -1]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_numbers_greater_than` that takes a list of numbers and a threshold, and returns a new list containing only numbers greater than the threshold.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1745  
Write a Python function called `get_numbers_greater_than` that takes a list of numbers and a threshold, and returns a new list containing only numbers greater than the threshold.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_numbers_greater_than(numbers, threshold):  # Function definition: get_numbers_greater_than
    return [x for x in numbers if x > threshold]  # Return the result

result = get_numbers_greater_than([1, 5, 10, 15, 20], 10)  # Initialize variable or assign value
print(result)  # Expected: [15, 20]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_numbers_less_than` that takes a list of numbers and a threshold, and returns a new list containing only numbers less than the threshold.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1746  
Write a Python function called `get_numbers_less_than` that takes a list of numbers and a threshold, and returns a new list containing only numbers less than the threshold.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_numbers_less_than(numbers, threshold):  # Function definition: get_numbers_less_than
    return [x for x in numbers if x < threshold]  # Return the result

result = get_numbers_less_than([1, 5, 10, 15, 20], 10)  # Initialize variable or assign value
print(result)  # Expected: [1, 5]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_sum_of_list` that takes a list of numbers and returns the sum of all numbers in the list.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1747  
Write a Python function called `calculate_sum_of_list` that takes a list of numbers and returns the sum of all numbers in the list.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def calculate_sum_of_list(numbers):  # Function definition: calculate_sum_of_list
    return sum(numbers)  # Return the result

result = calculate_sum_of_list([1, 2, 3, 4, 5])  # Initialize variable or assign value
print(result)  # Expected: 15




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_product_of_list` that takes a list of numbers and returns the product of all numbers in the list.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1748  
Write a Python function called `calculate_product_of_list` that takes a list of numbers and returns the product of all numbers in the list.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def calculate_product_of_list(numbers):  # Function definition: calculate_product_of_list
    product = 1  # Initialize variable or assign value
    for num in numbers:  # Loop: iterate over sequence
        product *= num
    return product  # Return the result

result = calculate_product_of_list([2, 3, 4])  # Initialize variable or assign value
print(result)  # Expected: 24




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_average_of_list` that takes a list of numbers and returns the average (mean) of all numbers.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1749  
Write a Python function called `get_average_of_list` that takes a list of numbers and returns the average (mean) of all numbers.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_average_of_list(numbers):  # Function definition: get_average_of_list
    return sum(numbers) / len(numbers)  # Return the result

result = get_average_of_list([10, 20, 30, 40])  # Initialize variable or assign value
print(result)  # Expected: 25.0




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `create_dictionary` that takes two lists (keys and values) and returns a dictionary created from them.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1750  
Write a Python function called `create_dictionary` that takes two lists (keys and values) and returns a dictionary created from them.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def create_dictionary(keys, values):  # Function definition: create_dictionary
    return dict(zip(keys, values))  # Return the result

result = create_dictionary(['a', 'b', 'c'], [1, 2, 3])  # Initialize variable or assign value
print(result)  # Expected: {'a': 1, 'b': 2, 'c': 3}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_dictionary_value` that takes a dictionary and a key, and returns the value associated with that key, or None if the key doesn't exist.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1751  
Write a Python function called `get_dictionary_value` that takes a dictionary and a key, and returns the value associated with that key, or None if the key doesn't exist.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_dictionary_value(d, key):  # Function definition: get_dictionary_value
    return d.get(key)  # Return the result

print(get_dictionary_value({'a': 1, 'b': 2}, 'a'), get_dictionary_value({'a': 1, 'b': 2}, 'c'))  # Expected: 1 None




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_dictionary_keys` that takes a dictionary and returns a list of all keys.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1752  
Write a Python function called `get_dictionary_keys` that takes a dictionary and returns a list of all keys.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_dictionary_keys(d):  # Function definition: get_dictionary_keys
    return list(d.keys())  # Return the result

result = get_dictionary_keys({'a': 1, 'b': 2, 'c': 3})  # Initialize variable or assign value
print(result)  # Expected: ['a', 'b', 'c']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_dictionary_values` that takes a dictionary and returns a list of all values.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1753  
Write a Python function called `get_dictionary_values` that takes a dictionary and returns a list of all values.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_dictionary_values(d):  # Function definition: get_dictionary_values
    return list(d.values())  # Return the result

result = get_dictionary_values({'a': 1, 'b': 2, 'c': 3})  # Initialize variable or assign value
print(result)  # Expected: [1, 2, 3]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_key_in_dictionary` that takes a dictionary and a key, and returns True if the key exists in the dictionary, otherwise False.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1754  
Write a Python function called `check_key_in_dictionary` that takes a dictionary and a key, and returns True if the key exists in the dictionary, otherwise False.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_key_in_dictionary(d, key):  # Function definition: check_key_in_dictionary
    return key in d  # Return the result

print(check_key_in_dictionary({'a': 1}, 'a'), check_key_in_dictionary({'a': 1}, 'b'))  # Expected: True False




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `add_to_dictionary` that takes a dictionary, a key, and a value, and returns a new dictionary with the key-value pair added.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1755  
Write a Python function called `add_to_dictionary` that takes a dictionary, a key, and a value, and returns a new dictionary with the key-value pair added.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def add_to_dictionary(d, key, value):  # Function definition: add_to_dictionary
    new_dict = d.copy()  # Initialize variable or assign value
    new_dict[key] = value  # Initialize variable or assign value
    return new_dict  # Return the result

result = add_to_dictionary({'a': 1}, 'b', 2)  # Initialize variable or assign value
print(result)  # Expected: {'a': 1, 'b': 2}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `create_tuple` that takes any number of arguments and returns a tuple containing those arguments.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1756  
Write a Python function called `create_tuple` that takes any number of arguments and returns a tuple containing those arguments.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def create_tuple(*args):  # Function definition: create_tuple
    return tuple(args)  # Return the result

result = create_tuple(1, 2, 3, 4)  # Initialize variable or assign value
print(result)  # Expected: (1, 2, 3, 4)




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_tuple_element` that takes a tuple and an index, and returns the element at that index.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1757  
Write a Python function called `get_tuple_element` that takes a tuple and an index, and returns the element at that index.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_tuple_element(my_tuple, index):  # Function definition: get_tuple_element
    return my_tuple[index]  # Return the result

result = get_tuple_element((10, 20, 30), 1)  # Initialize variable or assign value
print(result)  # Expected: 20




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `unpack_tuple` that takes a tuple of two elements and returns them as separate values.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1758  
Write a Python function called `unpack_tuple` that takes a tuple of two elements and returns them as separate values.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def unpack_tuple(my_tuple):  # Function definition: unpack_tuple
    a, b = my_tuple  # Initialize variable or assign value
    return a, b  # Return the result

result = unpack_tuple((10, 20))  # Initialize variable or assign value
print(result)  # Expected: (10, 20)




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `create_set` that takes a list and returns a set containing the unique elements from the list.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1759  
Write a Python function called `create_set` that takes a list and returns a set containing the unique elements from the list.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def create_set(my_list):  # Function definition: create_set
    return set(my_list)  # Return the result

result = create_set([1, 2, 2, 3, 3, 3])  # Initialize variable or assign value
print(result)  # Expected: {1, 2, 3}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_element_in_set` that takes a set and an element, and returns True if the element is in the set, otherwise False.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1760  
Write a Python function called `check_element_in_set` that takes a set and an element, and returns True if the element is in the set, otherwise False.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_element_in_set(my_set, element):  # Function definition: check_element_in_set
    return element in my_set  # Return the result

print(check_element_in_set({1, 2, 3}, 2), check_element_in_set({1, 2, 3}, 5))  # Expected: True False




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `union_sets` that takes two sets and returns a new set containing all elements from both sets.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1761  
Write a Python function called `union_sets` that takes two sets and returns a new set containing all elements from both sets.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def union_sets(set1, set2):  # Function definition: union_sets
    return set1 | set2  # Return the result

result = union_sets({1, 2, 3}, {3, 4, 5})  # Initialize variable or assign value
print(result)  # Expected: {1, 2, 3, 4, 5}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `intersection_sets` that takes two sets and returns a new set containing only elements that are in both sets.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1762  
Write a Python function called `intersection_sets` that takes two sets and returns a new set containing only elements that are in both sets.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def intersection_sets(set1, set2):  # Function definition: intersection_sets
    return set1 & set2  # Return the result

result = intersection_sets({1, 2, 3}, {2, 3, 4})  # Initialize variable or assign value
print(result)  # Expected: {2, 3}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `difference_sets` that takes two sets and returns a new set containing elements that are in the first set but not in the second.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1763  
Write a Python function called `difference_sets` that takes two sets and returns a new set containing elements that are in the first set but not in the second.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def difference_sets(set1, set2):  # Function definition: difference_sets
    return set1 - set2  # Return the result

result = difference_sets({1, 2, 3}, {2, 3, 4})  # Initialize variable or assign value
print(result)  # Expected: {1}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `read_file_content` that takes a filename and returns the content of the file as a string.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1764  
Write a Python function called `read_file_content` that takes a filename and returns the content of the file as a string.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def read_file_content(filename):  # Function definition: read_file_content
    with open(filename, 'r') as f:  # Statement block
        return f.read()  # Return the result

# Note: This requires a file to exist. Demonstration only.
# content = read_file_content("example.txt")
print("Function defined: read_file_content(filename)")  # Print the result




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `write_to_file` that takes a filename and content, and writes the content to the file.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1765  
Write a Python function called `write_to_file` that takes a filename and content, and writes the content to the file.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def write_to_file(filename, content):  # Function definition: write_to_file
    with open(filename, 'w') as f:  # Statement block
        f.write(content)

# Note: This writes to a file. Demonstration only.
# write_to_file("example.txt", "Hello, World!")
print("Function defined: write_to_file(filename, content)")  # Print the result




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `append_to_file` that takes a filename and content, and appends the content to the end of the file.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1766  
Write a Python function called `append_to_file` that takes a filename and content, and appends the content to the end of the file.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def append_to_file(filename, content):  # Function definition: append_to_file
    with open(filename, 'a') as f:  # Statement block
        f.write(content)

# Note: This appends to a file. Demonstration only.
# append_to_file("example.txt", "New line")
print("Function defined: append_to_file(filename, content)")  # Print the result




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `safe_divide` that takes two numbers and returns their division result. If division by zero occurs, return None instead of raising an error.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1767  
Write a Python function called `safe_divide` that takes two numbers and returns their division result. If division by zero occurs, return None instead of raising an error.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def safe_divide(a, b):  # Function definition: safe_divide
    try:  # Statement block
        return a / b  # Return the result
    except ZeroDivisionError:  # Statement block
        return None  # Return the result

print(safe_divide(10, 2), safe_divide(10, 0))  # Expected: 5.0 None




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `safe_convert_to_int` that takes a string and tries to convert it to an integer. If conversion fails, return None.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1768  
Write a Python function called `safe_convert_to_int` that takes a string and tries to convert it to an integer. If conversion fails, return None.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def safe_convert_to_int(text):  # Function definition: safe_convert_to_int
    try:  # Statement block
        return int(text)  # Return the result
    except ValueError:  # Statement block
        return None  # Return the result

print(safe_convert_to_int("123"), safe_convert_to_int("abc"))  # Expected: 123 None




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `safe_get_list_element` that takes a list and an index, and returns the element at that index. If index is out of range, return None.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1769  
Write a Python function called `safe_get_list_element` that takes a list and an index, and returns the element at that index. If index is out of range, return None.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def safe_get_list_element(my_list, index):  # Function definition: safe_get_list_element
    try:  # Statement block
        return my_list[index]  # Return the result
    except IndexError:  # Statement block
        return None  # Return the result

print(safe_get_list_element([1, 2, 3], 1), safe_get_list_element([1, 2, 3], 10))  # Expected: 2 None




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `join_strings` that takes a list of strings and a separator, and returns a single string with all strings joined by the separator.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1770  
Write a Python function called `join_strings` that takes a list of strings and a separator, and returns a single string with all strings joined by the separator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def join_strings(strings, separator):  # Function definition: join_strings
    return separator.join(strings)  # Return the result

result = join_strings(["Hello", "World", "Python"], "-")  # Initialize variable or assign value
print(result)  # Expected: Hello-World-Python




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `split_string` that takes a string and a delimiter, and returns a list of strings split by the delimiter.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1771  
Write a Python function called `split_string` that takes a string and a delimiter, and returns a list of strings split by the delimiter.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def split_string(text, delimiter):  # Function definition: split_string
    return text.split(delimiter)  # Return the result

result = split_string("Hello-World-Python", "-")  # Initialize variable or assign value
print(result)  # Expected: ['Hello', 'World', 'Python']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `strip_whitespace` that takes a string and returns a new string with leading and trailing whitespace removed.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1772  
Write a Python function called `strip_whitespace` that takes a string and returns a new string with leading and trailing whitespace removed.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def strip_whitespace(text):  # Function definition: strip_whitespace
    return text.strip()  # Return the result

result = strip_whitespace("  Hello World  ")  # Initialize variable or assign value
print(result)  # Expected: Hello World




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `capitalize_first_letter` that takes a string and returns a new string with only the first letter capitalized.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1773  
Write a Python function called `capitalize_first_letter` that takes a string and returns a new string with only the first letter capitalized.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def capitalize_first_letter(text):  # Function definition: capitalize_first_letter
    return text.capitalize()  # Return the result

result = capitalize_first_letter("hello world")  # Initialize variable or assign value
print(result)  # Expected: Hello world




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `swap_case` that takes a string and returns a new string with uppercase letters converted to lowercase and vice versa.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1774  
Write a Python function called `swap_case` that takes a string and returns a new string with uppercase letters converted to lowercase and vice versa.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def swap_case(text):  # Function definition: swap_case
    return text.swapcase()  # Return the result

result = swap_case("Hello World")  # Initialize variable or assign value
print(result)  # Expected: hELLO wORLD




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_all_digits` that takes a string and returns True if all characters in the string are digits, otherwise False.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1775  
Write a Python function called `check_all_digits` that takes a string and returns True if all characters in the string are digits, otherwise False.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_all_digits(text):  # Function definition: check_all_digits
    return text.isdigit()  # Return the result

print(check_all_digits("12345"), check_all_digits("12a45"))  # Expected: True False




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_all_letters` that takes a string and returns True if all characters in the string are letters, otherwise False.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1776  
Write a Python function called `check_all_letters` that takes a string and returns True if all characters in the string are letters, otherwise False.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_all_letters(text):  # Function definition: check_all_letters
    return text.isalpha()  # Return the result

print(check_all_letters("Hello"), check_all_letters("Hello123"))  # Expected: True False




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_all_alphanumeric` that takes a string and returns True if all characters are letters or digits, otherwise False.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1777  
Write a Python function called `check_all_alphanumeric` that takes a string and returns True if all characters are letters or digits, otherwise False.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_all_alphanumeric(text):  # Function definition: check_all_alphanumeric
    return text.isalnum()  # Return the result

print(check_all_alphanumeric("Hello123"), check_all_alphanumeric("Hello 123"))  # Expected: True False




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_squared_numbers` that takes a list of numbers and returns a new list with each number squared, using a list comprehension.
# 
# This problem demonstrates list comprehensions, a concise way to create lists
# in Python. List comprehensions are more readable and often faster than
# equivalent loops. They can include conditional expressions to filter or
# transform elements, making them a powerful tool for data manipulation.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1778  
Write a Python function called `get_squared_numbers` that takes a list of numbers and returns a new list with each number squared, using a list comprehension.
"""

# SOLUTION EXPLANATION:
# This solution uses a list comprehension to create a new list based on the
# specified conditions. List comprehensions are concise, readable, and often
# more efficient than equivalent loops for creating lists.

def get_squared_numbers(numbers):  # Function definition: get_squared_numbers
    return [x ** 2 for x in numbers]  # Return the result

result = get_squared_numbers([1, 2, 3, 4])  # Initialize variable or assign value
print(result)  # Expected: [1, 4, 9, 16]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_doubled_numbers` that takes a list of numbers and returns a new list with each number doubled, using a list comprehension.
# 
# This problem demonstrates list comprehensions, a concise way to create lists
# in Python. List comprehensions are more readable and often faster than
# equivalent loops. They can include conditional expressions to filter or
# transform elements, making them a powerful tool for data manipulation.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1779  
Write a Python function called `get_doubled_numbers` that takes a list of numbers and returns a new list with each number doubled, using a list comprehension.
"""

# SOLUTION EXPLANATION:
# This solution uses a list comprehension to create a new list based on the
# specified conditions. List comprehensions are concise, readable, and often
# more efficient than equivalent loops for creating lists.

def get_doubled_numbers(numbers):  # Function definition: get_doubled_numbers
    return [x * 2 for x in numbers]  # Return the result

result = get_doubled_numbers([1, 2, 3, 4])  # Initialize variable or assign value
print(result)  # Expected: [2, 4, 6, 8]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_even_numbers_comprehension` that takes a list of numbers and returns a new list containing only even numbers, using a list comprehension.
# 
# This problem demonstrates list comprehensions, a concise way to create lists
# in Python. List comprehensions are more readable and often faster than
# equivalent loops. They can include conditional expressions to filter or
# transform elements, making them a powerful tool for data manipulation.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1780  
Write a Python function called `get_even_numbers_comprehension` that takes a list of numbers and returns a new list containing only even numbers, using a list comprehension.
"""

# SOLUTION EXPLANATION:
# This solution uses a list comprehension to create a new list based on the
# specified conditions. List comprehensions are concise, readable, and often
# more efficient than equivalent loops for creating lists.

def get_even_numbers_comprehension(numbers):  # Function definition: get_even_numbers_comprehension
    return [x for x in numbers if x % 2 == 0]  # Return the result

result = get_even_numbers_comprehension([1, 2, 3, 4, 5, 6])  # Initialize variable or assign value
print(result)  # Expected: [2, 4, 6]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_uppercase_strings` that takes a list of strings and returns a new list with all strings converted to uppercase, using a list comprehension.
# 
# This problem demonstrates list comprehensions, a concise way to create lists
# in Python. List comprehensions are more readable and often faster than
# equivalent loops. They can include conditional expressions to filter or
# transform elements, making them a powerful tool for data manipulation.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1781  
Write a Python function called `get_uppercase_strings` that takes a list of strings and returns a new list with all strings converted to uppercase, using a list comprehension.
"""

# SOLUTION EXPLANATION:
# This solution uses a list comprehension to create a new list based on the
# specified conditions. List comprehensions are concise, readable, and often
# more efficient than equivalent loops for creating lists.

def get_uppercase_strings(strings):  # Function definition: get_uppercase_strings
    return [s.upper() for s in strings]  # Return the result

result = get_uppercase_strings(["hello", "world", "python"])  # Initialize variable or assign value
print(result)  # Expected: ['HELLO', 'WORLD', 'PYTHON']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_string_lengths` that takes a list of strings and returns a new list with the length of each string, using a list comprehension.
# 
# This problem demonstrates list comprehensions, a concise way to create lists
# in Python. List comprehensions are more readable and often faster than
# equivalent loops. They can include conditional expressions to filter or
# transform elements, making them a powerful tool for data manipulation.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1782  
Write a Python function called `get_string_lengths` that takes a list of strings and returns a new list with the length of each string, using a list comprehension.
"""

# SOLUTION EXPLANATION:
# This solution uses a list comprehension to create a new list based on the
# specified conditions. List comprehensions are concise, readable, and often
# more efficient than equivalent loops for creating lists.

def get_string_lengths(strings):  # Function definition: get_string_lengths
    return [len(s) for s in strings]  # Return the result

result = get_string_lengths(["hello", "world", "python"])  # Initialize variable or assign value
print(result)  # Expected: [5, 5, 6]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `print_number_pattern` that takes a number n and prints a pattern of numbers from 1 to n, where each line contains numbers from 1 to the line number.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1783  
Write a Python function called `print_number_pattern` that takes a number n and prints a pattern of numbers from 1 to n, where each line contains numbers from 1 to the line number.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def print_number_pattern(n):  # Function definition: print_number_pattern
    for i in range(1, n + 1):  # Loop: iterate over sequence
        for j in range(1, i + 1):  # Loop: iterate over sequence
            print(j, end=" ")  # Print the result
        print()  # Print the result

print_number_pattern(5)  # Expected: 1, 1 2, 1 2 3, 1 2 3 4, 1 2 3 4 5




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `print_star_pattern` that takes a number n and prints n lines of stars, where the first line has 1 star, second has 2 stars, and so on.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1784  
Write a Python function called `print_star_pattern` that takes a number n and prints n lines of stars, where the first line has 1 star, second has 2 stars, and so on.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def print_star_pattern(n):  # Function definition: print_star_pattern
    for i in range(1, n + 1):  # Loop: iterate over sequence
        print("*" * i)  # Print the result

print_star_pattern(5)  # Expected: *, **, ***, ****, *****




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `print_reverse_star_pattern` that takes a number n and prints n lines of stars in reverse order, where the first line has n stars, second has n-1 stars, and so on.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1785  
Write a Python function called `print_reverse_star_pattern` that takes a number n and prints n lines of stars in reverse order, where the first line has n stars, second has n-1 stars, and so on.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def print_reverse_star_pattern(n):  # Function definition: print_reverse_star_pattern
    for i in range(n, 0, -1):  # Loop: iterate over sequence
        print("*" * i)  # Print the result

print_reverse_star_pattern(5)  # Expected: *****, ****, ***, **, *




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `print_number_square` that takes a number n and prints an n by n square of numbers from 1 to n*n.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1786  
Write a Python function called `print_number_square` that takes a number n and prints an n by n square of numbers from 1 to n*n.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def print_number_square(n):  # Function definition: print_number_square
    for i in range(1, n * n + 1, n):  # Loop: iterate over sequence
        row = [str(j) for j in range(i, i + n)]  # Initialize list
        print(" ".join(row))  # Print the result

print_number_square(3)  # Expected: 1 2 3, 4 5 6, 7 8 9




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_factorial` that takes a number n and returns the factorial of n (n! = n * (n-1) * ... * 1).
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1787  
Write a Python function called `calculate_factorial` that takes a number n and returns the factorial of n (n! = n * (n-1) * ... * 1).
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def calculate_factorial(n):  # Function definition: calculate_factorial
    result = 1  # Initialize variable or assign value
    for i in range(1, n + 1):  # Loop: iterate over sequence
        result *= i
    return result  # Return the result

result = calculate_factorial(5)  # Initialize variable or assign value
print(result)  # Expected: 120




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_sum_range` that takes two numbers start and end, and returns the sum of all numbers from start to end (inclusive).
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1788  
Write a Python function called `calculate_sum_range` that takes two numbers start and end, and returns the sum of all numbers from start to end (inclusive).
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def calculate_sum_range(start, end):  # Function definition: calculate_sum_range
    return sum(range(start, end + 1))  # Return the result

result = calculate_sum_range(1, 10)  # Initialize variable or assign value
print(result)  # Expected: 55




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_product_range` that takes two numbers start and end, and returns the product of all numbers from start to end (inclusive).
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1789  
Write a Python function called `calculate_product_range` that takes two numbers start and end, and returns the product of all numbers from start to end (inclusive).
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def calculate_product_range(start, end):  # Function definition: calculate_product_range
    product = 1  # Initialize variable or assign value
    for i in range(start, end + 1):  # Loop: iterate over sequence
        product *= i
    return product  # Return the result

result = calculate_product_range(1, 5)  # Initialize variable or assign value
print(result)  # Expected: 120




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_fibonacci_sequence` that takes a number n and returns a list containing the first n numbers of the Fibonacci sequence.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1790  
Write a Python function called `get_fibonacci_sequence` that takes a number n and returns a list containing the first n numbers of the Fibonacci sequence.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_fibonacci_sequence(n):  # Function definition: get_fibonacci_sequence
    if n <= 0:  # Conditional statement: check condition
        return []  # Return the result
    elif n == 1:  # Conditional statement: check condition
        return [0]  # Return the result
    elif n == 2:  # Conditional statement: check condition
        return [0, 1]  # Return the result
    fib = [0, 1]  # Initialize list
    for i in range(2, n):  # Loop: iterate over sequence
        fib.append(fib[i-1] + fib[i-2])  # Add element to list
    return fib  # Return the result

result = get_fibonacci_sequence(8)  # Initialize variable or assign value
print(result)  # Expected: [0, 1, 1, 2, 3, 5, 8, 13]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_palindrome_number` that takes a number and returns True if the number is a palindrome (reads the same forwards and backwards), otherwise False.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1791  
Write a Python function called `check_palindrome_number` that takes a number and returns True if the number is a palindrome (reads the same forwards and backwards), otherwise False.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_palindrome_number(number):  # Function definition: check_palindrome_number
    return str(number) == str(number)[::-1]  # Return the result

print(check_palindrome_number(121), check_palindrome_number(123))  # Expected: True False




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `sum_of_digits` that takes a number and returns the sum of all its digits.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1792  
Write a Python function called `sum_of_digits` that takes a number and returns the sum of all its digits.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def sum_of_digits(number):  # Function definition: sum_of_digits
    return sum(int(digit) for digit in str(number))  # Return the result

result = sum_of_digits(12345)  # Initialize variable or assign value
print(result)  # Expected: 15




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `product_of_digits` that takes a number and returns the product of all its digits.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1793  
Write a Python function called `product_of_digits` that takes a number and returns the product of all its digits.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def product_of_digits(number):  # Function definition: product_of_digits
    product = 1  # Initialize variable or assign value
    for digit in str(number):  # Loop: iterate over sequence
        product *= int(digit)
    return product  # Return the result

result = product_of_digits(234)  # Initialize variable or assign value
print(result)  # Expected: 24




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `count_digits` that takes a number and returns the number of digits in the number.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1794  
Write a Python function called `count_digits` that takes a number and returns the number of digits in the number.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def count_digits(number):  # Function definition: count_digits
    return len(str(number))  # Return the result

result = count_digits(12345)  # Initialize variable or assign value
print(result)  # Expected: 5




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `reverse_number` that takes a number and returns the number with its digits reversed.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1795  
Write a Python function called `reverse_number` that takes a number and returns the number with its digits reversed.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def reverse_number(number):  # Function definition: reverse_number
    return int(str(number)[::-1])  # Return the result

result = reverse_number(12345)  # Initialize variable or assign value
print(result)  # Expected: 54321




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_first_n_elements` that takes a list and a number n, and returns the first n elements of the list.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1796  
Write a Python function called `get_first_n_elements` that takes a list and a number n, and returns the first n elements of the list.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_first_n_elements(my_list, n):  # Function definition: get_first_n_elements
    return my_list[:n]  # Return the result

result = get_first_n_elements([1, 2, 3, 4, 5], 3)  # Initialize variable or assign value
print(result)  # Expected: [1, 2, 3]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_last_n_elements` that takes a list and a number n, and returns the last n elements of the list.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1797  
Write a Python function called `get_last_n_elements` that takes a list and a number n, and returns the last n elements of the list.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_last_n_elements(my_list, n):  # Function definition: get_last_n_elements
    return my_list[-n:]  # Return the result

result = get_last_n_elements([1, 2, 3, 4, 5], 3)  # Initialize variable or assign value
print(result)  # Expected: [3, 4, 5]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `remove_duplicates_from_list` that takes a list and returns a new list with duplicate elements removed, preserving order.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1798  
Write a Python function called `remove_duplicates_from_list` that takes a list and returns a new list with duplicate elements removed, preserving order.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def remove_duplicates_from_list(my_list):  # Function definition: remove_duplicates_from_list
    seen = []  # Initialize empty list/dict/set
    result = []  # Initialize empty list/dict/set
    for item in my_list:  # Loop: iterate over sequence
        if item not in seen:  # Conditional statement: check condition
            seen.append(item)  # Add element to list
            result.append(item)  # Add element to list
    return result  # Return the result

result = remove_duplicates_from_list([1, 2, 2, 3, 3, 3, 4])  # Initialize variable or assign value
print(result)  # Expected: [1, 2, 3, 4]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `merge_two_lists` that takes two lists and returns a new list containing all elements from both lists, alternating between them.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1799  
Write a Python function called `merge_two_lists` that takes two lists and returns a new list containing all elements from both lists, alternating between them.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def merge_two_lists(list1, list2):  # Function definition: merge_two_lists
    result = []  # Initialize empty list/dict/set
    max_len = max(len(list1), len(list2))  # Use min/max with default parameter to handle empty sequences
    for i in range(max_len):  # Loop: iterate over sequence
        if i < len(list1):  # Conditional statement: check condition
            result.append(list1[i])  # Add element to list
        if i < len(list2):  # Conditional statement: check condition
            result.append(list2[i])  # Add element to list
    return result  # Return the result

result = merge_two_lists([1, 2, 3], ['a', 'b', 'c'])  # Initialize variable or assign value
print(result)  # Expected: [1, 'a', 2, 'b', 3, 'c']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_common_elements` that takes two lists and returns a new list containing elements that appear in both lists.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1800  
Write a Python function called `get_common_elements` that takes two lists and returns a new list containing elements that appear in both lists.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_common_elements(list1, list2):  # Function definition: get_common_elements
    return [x for x in list1 if x in list2]  # Return the result

result = get_common_elements([1, 2, 3, 4], [3, 4, 5, 6])  # Initialize variable or assign value
print(result)  # Expected: [3, 4]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_unique_elements` that takes two lists and returns a new list containing elements that appear in only one of the lists.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1801  
Write a Python function called `get_unique_elements` that takes two lists and returns a new list containing elements that appear in only one of the lists.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_unique_elements(list1, list2):  # Function definition: get_unique_elements
    result = []  # Initialize empty list/dict/set
    for item in list1:  # Loop: iterate over sequence
        if item not in list2:  # Conditional statement: check condition
            result.append(item)  # Add element to list
    for item in list2:  # Loop: iterate over sequence
        if item not in list1:  # Conditional statement: check condition
            result.append(item)  # Add element to list
    return result  # Return the result

result = get_unique_elements([1, 2, 3, 4], [3, 4, 5, 6])  # Initialize variable or assign value
print(result)  # Expected: [1, 2, 5, 6]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `sort_list_ascending` that takes a list of numbers and returns a new list sorted in ascending order.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1802  
Write a Python function called `sort_list_ascending` that takes a list of numbers and returns a new list sorted in ascending order.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def sort_list_ascending(numbers):  # Function definition: sort_list_ascending
    return sorted(numbers)  # Return the result

result = sort_list_ascending([3, 1, 4, 1, 5, 9, 2])  # Initialize variable or assign value
print(result)  # Expected: [1, 1, 2, 3, 4, 5, 9]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `sort_list_descending` that takes a list of numbers and returns a new list sorted in descending order.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1803  
Write a Python function called `sort_list_descending` that takes a list of numbers and returns a new list sorted in descending order.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def sort_list_descending(numbers):  # Function definition: sort_list_descending
    return sorted(numbers, reverse=True)  # Return the result

result = sort_list_descending([3, 1, 4, 1, 5, 9, 2])  # Initialize variable or assign value
print(result)  # Expected: [9, 5, 4, 3, 2, 1, 1]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_second_largest` that takes a list of numbers and returns the second largest number in the list.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1804  
Write a Python function called `get_second_largest` that takes a list of numbers and returns the second largest number in the list.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_second_largest(numbers):  # Function definition: get_second_largest
    unique_numbers = sorted(set(numbers), reverse=True)  # Sort the sequence
    return unique_numbers[1] if len(unique_numbers) > 1 else None  # Return the result

result = get_second_largest([3, 1, 4, 1, 5, 9, 2])  # Initialize variable or assign value
print(result)  # Expected: 5




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_second_smallest` that takes a list of numbers and returns the second smallest number in the list.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1805  
Write a Python function called `get_second_smallest` that takes a list of numbers and returns the second smallest number in the list.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_second_smallest(numbers):  # Function definition: get_second_smallest
    unique_numbers = sorted(set(numbers))  # Sort the sequence
    return unique_numbers[1] if len(unique_numbers) > 1 else None  # Return the result

result = get_second_smallest([3, 1, 4, 1, 5, 9, 2])  # Initialize variable or assign value
print(result)  # Expected: 2




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_sorted` that takes a list of numbers and returns True if the list is sorted in ascending order, otherwise False.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1806  
Write a Python function called `check_sorted` that takes a list of numbers and returns True if the list is sorted in ascending order, otherwise False.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_sorted(numbers):  # Function definition: check_sorted
    return numbers == sorted(numbers)  # Return the result

print(check_sorted([1, 2, 3, 4]), check_sorted([1, 3, 2, 4]))  # Expected: True False




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `count_occurrences_in_list` that takes a list and returns a dictionary where keys are elements and values are their counts.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1807  
Write a Python function called `count_occurrences_in_list` that takes a list and returns a dictionary where keys are elements and values are their counts.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def count_occurrences_in_list(my_list):  # Function definition: count_occurrences_in_list
    counts = {}  # Initialize empty list/dict/set
    for item in my_list:  # Loop: iterate over sequence
        counts[item] = counts.get(item, 0) + 1  # Initialize variable or assign value
    return counts  # Return the result

result = count_occurrences_in_list([1, 2, 2, 3, 3, 3])  # Initialize variable or assign value
print(result)  # Expected: {1: 1, 2: 2, 3: 3}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_most_frequent` that takes a list and returns the element that appears most frequently.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1808  
Write a Python function called `get_most_frequent` that takes a list and returns the element that appears most frequently.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_most_frequent(my_list):  # Function definition: get_most_frequent
    counts = {}  # Initialize empty list/dict/set
    for item in my_list:  # Loop: iterate over sequence
        counts[item] = counts.get(item, 0) + 1  # Initialize variable or assign value
    return max(counts, key=counts.get)  # Return the result

result = get_most_frequent([1, 2, 2, 3, 3, 3, 3])  # Initialize variable or assign value
print(result)  # Expected: 3




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_least_frequent` that takes a list and returns the element that appears least frequently.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1809  
Write a Python function called `get_least_frequent` that takes a list and returns the element that appears least frequently.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_least_frequent(my_list):  # Function definition: get_least_frequent
    counts = {}  # Initialize empty list/dict/set
    for item in my_list:  # Loop: iterate over sequence
        counts[item] = counts.get(item, 0) + 1  # Initialize variable or assign value
    return min(counts, key=counts.get)  # Return the result

result = get_least_frequent([1, 1, 2, 2, 2, 3])  # Initialize variable or assign value
print(result)  # Expected: 3




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `flatten_nested_list` that takes a list of lists and returns a single list containing all elements.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1810  
Write a Python function called `flatten_nested_list` that takes a list of lists and returns a single list containing all elements.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def flatten_nested_list(nested_list):  # Function definition: flatten_nested_list
    result = []  # Initialize empty list/dict/set
    for sublist in nested_list:  # Loop: iterate over sequence
        result.extend(sublist)
    return result  # Return the result

result = flatten_nested_list([[1, 2], [3, 4], [5, 6]])  # Initialize variable or assign value
print(result)  # Expected: [1, 2, 3, 4, 5, 6]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `group_by_length` that takes a list of strings and returns a dictionary where keys are lengths and values are lists of strings with that length.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1811  
Write a Python function called `group_by_length` that takes a list of strings and returns a dictionary where keys are lengths and values are lists of strings with that length.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def group_by_length(strings):  # Function definition: group_by_length
    groups = {}  # Initialize empty list/dict/set
    for s in strings:  # Loop: iterate over sequence
        length = len(s)  # Initialize variable or assign value
        if length not in groups:  # Conditional statement: check condition
            groups[length] = []  # Initialize empty list/dict/set
        groups[length].append(s)  # Add element to list
    return groups  # Return the result

result = group_by_length(["a", "ab", "abc", "ab", "abcd"])  # Initialize variable or assign value
print(result)  # Expected: {1: ['a'], 2: ['ab', 'ab'], 3: ['abc'], 4: ['abcd']}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `filter_by_length` that takes a list of strings and a minimum length, and returns a new list containing only strings with length greater than or equal to the minimum.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1812  
Write a Python function called `filter_by_length` that takes a list of strings and a minimum length, and returns a new list containing only strings with length greater than or equal to the minimum.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def filter_by_length(strings, min_length):  # Function definition: filter_by_length
    return [s for s in strings if len(s) >= min_length]  # Return the result

result = filter_by_length(["a", "ab", "abc", "abcd"], 3)  # Initialize variable or assign value
print(result)  # Expected: ['abc', 'abcd']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_longest_string` that takes a list of strings and returns the longest string.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1813  
Write a Python function called `get_longest_string` that takes a list of strings and returns the longest string.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_longest_string(strings):  # Function definition: get_longest_string
    return max(strings, key=len)  # Return the result

result = get_longest_string(["a", "ab", "abc", "abcd"])  # Initialize variable or assign value
print(result)  # Expected: abcd




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_shortest_string` that takes a list of strings and returns the shortest string.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1814  
Write a Python function called `get_shortest_string` that takes a list of strings and returns the shortest string.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_shortest_string(strings):  # Function definition: get_shortest_string
    return min(strings, key=len)  # Return the result

result = get_shortest_string(["a", "ab", "abc", "abcd"])  # Initialize variable or assign value
print(result)  # Expected: a




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `capitalize_all_words` that takes a string of words separated by spaces and returns a new string with the first letter of each word capitalized.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1815  
Write a Python function called `capitalize_all_words` that takes a string of words separated by spaces and returns a new string with the first letter of each word capitalized.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def capitalize_all_words(text):  # Function definition: capitalize_all_words
    return " ".join(word.capitalize() for word in text.split())  # Return the result

result = capitalize_all_words("hello world python")  # Initialize variable or assign value
print(result)  # Expected: Hello World Python




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `reverse_words` that takes a string of words separated by spaces and returns a new string with the order of words reversed.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1816  
Write a Python function called `reverse_words` that takes a string of words separated by spaces and returns a new string with the order of words reversed.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def reverse_words(text):  # Function definition: reverse_words
    words = text.split()  # Initialize variable or assign value
    return " ".join(reversed(words))  # Return the result

result = reverse_words("hello world python")  # Initialize variable or assign value
print(result)  # Expected: python world hello




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `count_words` that takes a string and returns the number of words in the string (words are separated by spaces).
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1817  
Write a Python function called `count_words` that takes a string and returns the number of words in the string (words are separated by spaces).
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def count_words(text):  # Function definition: count_words
    return len(text.split())  # Return the result

result = count_words("Hello World Python")  # Initialize variable or assign value
print(result)  # Expected: 3




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_longest_word` that takes a string of words separated by spaces and returns the longest word.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1818  
Write a Python function called `get_longest_word` that takes a string of words separated by spaces and returns the longest word.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_longest_word(text):  # Function definition: get_longest_word
    words = text.split()  # Initialize variable or assign value
    return max(words, key=len)  # Return the result

result = get_longest_word("hello world python programming")  # Initialize variable or assign value
print(result)  # Expected: programming




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_shortest_word` that takes a string of words separated by spaces and returns the shortest word.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1819  
Write a Python function called `get_shortest_word` that takes a string of words separated by spaces and returns the shortest word.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_shortest_word(text):  # Function definition: get_shortest_word
    words = text.split()  # Initialize variable or assign value
    return min(words, key=len)  # Return the result

result = get_shortest_word("hello world python programming")  # Initialize variable or assign value
print(result)  # Expected: python




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `remove_vowels_from_string` that takes a string and returns a new string with all vowels (a, e, i, o, u) removed.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1820  
Write a Python function called `remove_vowels_from_string` that takes a string and returns a new string with all vowels (a, e, i, o, u) removed.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def remove_vowels_from_string(text):  # Function definition: remove_vowels_from_string
    vowels = "aeiouAEIOU"  # Initialize string variable
    return "".join(char for char in text if char not in vowels)  # Return the result

result = remove_vowels_from_string("Hello World")  # Initialize variable or assign value
print(result)  # Expected: Hll Wrld




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `remove_consonants_from_string` that takes a string and returns a new string with all consonants removed, keeping only vowels and other characters.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1821  
Write a Python function called `remove_consonants_from_string` that takes a string and returns a new string with all consonants removed, keeping only vowels and other characters.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def remove_consonants_from_string(text):  # Function definition: remove_consonants_from_string
    vowels = "aeiouAEIOU"  # Initialize string variable
    return "".join(char for char in text if char in vowels or not char.isalpha())  # Return the result

result = remove_consonants_from_string("Hello World")  # Initialize variable or assign value
print(result)  # Expected: eo o




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `count_vowels_in_string` that takes a string and returns the number of vowels (a, e, i, o, u) in the string.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1822  
Write a Python function called `count_vowels_in_string` that takes a string and returns the number of vowels (a, e, i, o, u) in the string.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def count_vowels_in_string(text):  # Function definition: count_vowels_in_string
    vowels = "aeiouAEIOU"  # Initialize string variable
    return sum(1 for char in text if char in vowels)  # Return the result

result = count_vowels_in_string("Hello World")  # Initialize variable or assign value
print(result)  # Expected: 3




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `count_consonants_in_string` that takes a string and returns the number of consonants in the string.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1823  
Write a Python function called `count_consonants_in_string` that takes a string and returns the number of consonants in the string.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def count_consonants_in_string(text):  # Function definition: count_consonants_in_string
    vowels = "aeiouAEIOU"  # Initialize string variable
    return sum(1 for char in text if char.isalpha() and char not in vowels)  # Return the result

result = count_consonants_in_string("Hello World")  # Initialize variable or assign value
print(result)  # Expected: 7




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `swap_first_last_words` that takes a string of words separated by spaces and returns a new string with the first and last words swapped.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1824  
Write a Python function called `swap_first_last_words` that takes a string of words separated by spaces and returns a new string with the first and last words swapped.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def swap_first_last_words(text):  # Function definition: swap_first_last_words
    words = text.split()  # Initialize variable or assign value
    if len(words) < 2:  # Conditional statement: check condition
        return text  # Return the result
    words[0], words[-1] = words[-1], words[0]  # Initialize variable or assign value
    return " ".join(words)  # Return the result

result = swap_first_last_words("Hello World Python")  # Initialize variable or assign value
print(result)  # Expected: Python World Hello




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_middle_word` that takes a string of words separated by spaces and returns the middle word. If there are even number of words, return the word at index length//2.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1825  
Write a Python function called `get_middle_word` that takes a string of words separated by spaces and returns the middle word. If there are even number of words, return the word at index length//2.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_middle_word(text):  # Function definition: get_middle_word
    words = text.split()  # Initialize variable or assign value
    return words[len(words) // 2]  # Return the result

result = get_middle_word("Hello World Python Programming")  # Initialize variable or assign value
print(result)  # Expected: Python




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_all_same` that takes a list and returns True if all elements in the list are the same, otherwise False.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1826  
Write a Python function called `check_all_same` that takes a list and returns True if all elements in the list are the same, otherwise False.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_all_same(my_list):  # Function definition: check_all_same
    return all(x == my_list[0] for x in my_list) if my_list else True  # Return the result

print(check_all_same([1, 1, 1]), check_all_same([1, 2, 1]))  # Expected: True False




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_all_different` that takes a list and returns True if all elements in the list are different, otherwise False.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1827  
Write a Python function called `check_all_different` that takes a list and returns True if all elements in the list are different, otherwise False.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_all_different(my_list):  # Function definition: check_all_different
    return len(my_list) == len(set(my_list))  # Return the result

print(check_all_different([1, 2, 3]), check_all_different([1, 2, 2]))  # Expected: True False




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_range_list` that takes two numbers start and end, and returns a list containing all numbers from start to end (inclusive).
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1828  
Write a Python function called `get_range_list` that takes two numbers start and end, and returns a list containing all numbers from start to end (inclusive).
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_range_list(start, end):  # Function definition: get_range_list
    return list(range(start, end + 1))  # Return the result

result = get_range_list(1, 5)  # Initialize variable or assign value
print(result)  # Expected: [1, 2, 3, 4, 5]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_even_range` that takes two numbers start and end, and returns a list containing all even numbers from start to end (inclusive).
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1829  
Write a Python function called `get_even_range` that takes two numbers start and end, and returns a list containing all even numbers from start to end (inclusive).
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_even_range(start, end):  # Function definition: get_even_range
    return [x for x in range(start, end + 1) if x % 2 == 0]  # Return the result

result = get_even_range(1, 10)  # Initialize variable or assign value
print(result)  # Expected: [2, 4, 6, 8, 10]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_odd_range` that takes two numbers start and end, and returns a list containing all odd numbers from start to end (inclusive).
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1830  
Write a Python function called `get_odd_range` that takes two numbers start and end, and returns a list containing all odd numbers from start to end (inclusive).
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_odd_range(start, end):  # Function definition: get_odd_range
    return [x for x in range(start, end + 1) if x % 2 != 0]  # Return the result

result = get_odd_range(1, 10)  # Initialize variable or assign value
print(result)  # Expected: [1, 3, 5, 7, 9]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `multiply_lists` that takes two lists of numbers of the same length and returns a new list where each element is the product of corresponding elements from both lists.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1831  
Write a Python function called `multiply_lists` that takes two lists of numbers of the same length and returns a new list where each element is the product of corresponding elements from both lists.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def multiply_lists(list1, list2):  # Function definition: multiply_lists
    return [a * b for a, b in zip(list1, list2)]  # Return the result

result = multiply_lists([1, 2, 3], [4, 5, 6])  # Initialize variable or assign value
print(result)  # Expected: [4, 10, 18]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `add_lists` that takes two lists of numbers of the same length and returns a new list where each element is the sum of corresponding elements from both lists.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1832  
Write a Python function called `add_lists` that takes two lists of numbers of the same length and returns a new list where each element is the sum of corresponding elements from both lists.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def add_lists(list1, list2):  # Function definition: add_lists
    return [a + b for a, b in zip(list1, list2)]  # Return the result

result = add_lists([1, 2, 3], [4, 5, 6])  # Initialize variable or assign value
print(result)  # Expected: [5, 7, 9]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `subtract_lists` that takes two lists of numbers of the same length and returns a new list where each element is the difference of corresponding elements from both lists.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1833  
Write a Python function called `subtract_lists` that takes two lists of numbers of the same length and returns a new list where each element is the difference of corresponding elements from both lists.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def subtract_lists(list1, list2):  # Function definition: subtract_lists
    return [a - b for a, b in zip(list1, list2)]  # Return the result

result = subtract_lists([10, 20, 30], [4, 5, 6])  # Initialize variable or assign value
print(result)  # Expected: [6, 15, 24]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_index_of_max` that takes a list of numbers and returns the index of the maximum value.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1834  
Write a Python function called `get_index_of_max` that takes a list of numbers and returns the index of the maximum value.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_index_of_max(numbers):  # Function definition: get_index_of_max
    return numbers.index(max(numbers))  # Return the result

result = get_index_of_max([10, 5, 30, 20])  # Use min/max with default parameter to handle empty sequences
print(result)  # Expected: 2




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_index_of_min` that takes a list of numbers and returns the index of the minimum value.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1835  
Write a Python function called `get_index_of_min` that takes a list of numbers and returns the index of the minimum value.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_index_of_min(numbers):  # Function definition: get_index_of_min
    return numbers.index(min(numbers))  # Return the result

result = get_index_of_min([10, 5, 30, 20])  # Use min/max with default parameter to handle empty sequences
print(result)  # Expected: 1




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `rotate_list_left` that takes a list and a number n, and returns a new list rotated n positions to the left.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1836  
Write a Python function called `rotate_list_left` that takes a list and a number n, and returns a new list rotated n positions to the left.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def rotate_list_left(my_list, n):  # Function definition: rotate_list_left
    n = n % len(my_list)  # Initialize variable or assign value
    return my_list[n:] + my_list[:n]  # Return the result

result = rotate_list_left([1, 2, 3, 4, 5], 2)  # Initialize variable or assign value
print(result)  # Expected: [3, 4, 5, 1, 2]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `rotate_list_right` that takes a list and a number n, and returns a new list rotated n positions to the right.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1837  
Write a Python function called `rotate_list_right` that takes a list and a number n, and returns a new list rotated n positions to the right.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def rotate_list_right(my_list, n):  # Function definition: rotate_list_right
    n = n % len(my_list)  # Initialize variable or assign value
    return my_list[-n:] + my_list[:-n]  # Return the result

result = rotate_list_right([1, 2, 3, 4, 5], 2)  # Initialize variable or assign value
print(result)  # Expected: [4, 5, 1, 2, 3]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `chunk_list` that takes a list and a number n, and returns a list of lists where each inner list contains n elements (except possibly the last one).
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1838  
Write a Python function called `chunk_list` that takes a list and a number n, and returns a list of lists where each inner list contains n elements (except possibly the last one).
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def chunk_list(my_list, n):  # Function definition: chunk_list
    return [my_list[i:i+n] for i in range(0, len(my_list), n)]  # Return the result

result = chunk_list([1, 2, 3, 4, 5, 6, 7], 3)  # Initialize variable or assign value
print(result)  # Expected: [[1, 2, 3], [4, 5, 6], [7]]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `interleave_lists` that takes two lists and returns a new list with elements from both lists interleaved (alternating).
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1839  
Write a Python function called `interleave_lists` that takes two lists and returns a new list with elements from both lists interleaved (alternating).
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def interleave_lists(list1, list2):  # Function definition: interleave_lists
    result = []  # Initialize empty list/dict/set
    max_len = max(len(list1), len(list2))  # Use min/max with default parameter to handle empty sequences
    for i in range(max_len):  # Loop: iterate over sequence
        if i < len(list1):  # Conditional statement: check condition
            result.append(list1[i])  # Add element to list
        if i < len(list2):  # Conditional statement: check condition
            result.append(list2[i])  # Add element to list
    return result  # Return the result

result = interleave_lists([1, 2, 3], ['a', 'b'])  # Initialize variable or assign value
print(result)  # Expected: [1, 'a', 2, 'b', 3]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `zip_lists` that takes two lists and returns a list of tuples, where each tuple contains corresponding elements from both lists.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1840  
Write a Python function called `zip_lists` that takes two lists and returns a list of tuples, where each tuple contains corresponding elements from both lists.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def zip_lists(list1, list2):  # Function definition: zip_lists
    return list(zip(list1, list2))  # Return the result

result = zip_lists([1, 2, 3], ['a', 'b', 'c'])  # Initialize variable or assign value
print(result)  # Expected: [(1, 'a'), (2, 'b'), (3, 'c')]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `unzip_list` that takes a list of tuples and returns two lists: one with all first elements and one with all second elements.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1841  
Write a Python function called `unzip_list` that takes a list of tuples and returns two lists: one with all first elements and one with all second elements.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def unzip_list(tuples_list):  # Function definition: unzip_list
    if not tuples_list:  # Conditional statement: check condition
        return [], []  # Return the result
    first_elements = [t[0] for t in tuples_list]  # Initialize list
    second_elements = [t[1] for t in tuples_list]  # Initialize list
    return first_elements, second_elements  # Return the result

result = unzip_list([(1, 'a'), (2, 'b'), (3, 'c')])  # Initialize variable or assign value
print(result)  # Expected: ([1, 2, 3], ['a', 'b', 'c'])




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `count_uppercase_letters` that takes a string and returns the number of uppercase letters in the string.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1842  
Write a Python function called `count_uppercase_letters` that takes a string and returns the number of uppercase letters in the string.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def count_uppercase_letters(text):  # Function definition: count_uppercase_letters
    return sum(1 for char in text if char.isupper())  # Return the result

result = count_uppercase_letters("Hello World")  # Initialize variable or assign value
print(result)  # Expected: 2




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `count_lowercase_letters` that takes a string and returns the number of lowercase letters in the string.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1843  
Write a Python function called `count_lowercase_letters` that takes a string and returns the number of lowercase letters in the string.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def count_lowercase_letters(text):  # Function definition: count_lowercase_letters
    return sum(1 for char in text if char.islower())  # Return the result

result = count_lowercase_letters("Hello World")  # Initialize variable or assign value
print(result)  # Expected: 8




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `swap_uppercase_lowercase` that takes a string and returns a new string where uppercase letters become lowercase and lowercase letters become uppercase.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1844  
Write a Python function called `swap_uppercase_lowercase` that takes a string and returns a new string where uppercase letters become lowercase and lowercase letters become uppercase.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def swap_uppercase_lowercase(text):  # Function definition: swap_uppercase_lowercase
    return text.swapcase()  # Return the result

result = swap_uppercase_lowercase("Hello World")  # Initialize variable or assign value
print(result)  # Expected: hELLO wORLD




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `remove_numbers_from_string` that takes a string and returns a new string with all digits removed.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1845  
Write a Python function called `remove_numbers_from_string` that takes a string and returns a new string with all digits removed.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def remove_numbers_from_string(text):  # Function definition: remove_numbers_from_string
    return "".join(char for char in text if not char.isdigit())  # Return the result

result = remove_numbers_from_string("Hello123World456")  # Initialize variable or assign value
print(result)  # Expected: HelloWorld




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `remove_letters_from_string` that takes a string and returns a new string with all letters removed, keeping only digits and other characters.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1846  
Write a Python function called `remove_letters_from_string` that takes a string and returns a new string with all letters removed, keeping only digits and other characters.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def remove_letters_from_string(text):  # Function definition: remove_letters_from_string
    return "".join(char for char in text if not char.isalpha())  # Return the result

result = remove_letters_from_string("Hello123World456!")  # Initialize variable or assign value
print(result)  # Expected: 123456!




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `extract_numbers_from_string` that takes a string and returns a list of all numbers found in the string (as strings).
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1847  
Write a Python function called `extract_numbers_from_string` that takes a string and returns a list of all numbers found in the string (as strings).
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def extract_numbers_from_string(text):  # Function definition: extract_numbers_from_string
    return [char for char in text if char.isdigit()]  # Return the result

result = extract_numbers_from_string("Hello123World456")  # Initialize variable or assign value
print(result)  # Expected: ['1', '2', '3', '4', '5', '6']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `extract_letters_from_string` that takes a string and returns a list of all letters found in the string.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1848  
Write a Python function called `extract_letters_from_string` that takes a string and returns a list of all letters found in the string.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def extract_letters_from_string(text):  # Function definition: extract_letters_from_string
    return [char for char in text if char.isalpha()]  # Return the result

result = extract_letters_from_string("Hello123World456")  # Initialize variable or assign value
print(result)  # Expected: ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `format_phone_number` that takes a string of 10 digits and returns it formatted as (XXX) XXX-XXXX.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1849  
Write a Python function called `format_phone_number` that takes a string of 10 digits and returns it formatted as (XXX) XXX-XXXX.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def format_phone_number(digits):  # Function definition: format_phone_number
    return f"({digits[0:3]}) {digits[3:6]}-{digits[6:10]}"  # Return the result

result = format_phone_number("1234567890")  # Initialize variable or assign value
print(result)  # Expected: (123) 456-7890




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_volume_box` that takes length, width, and height as parameters and returns the volume of a rectangular box.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1850  
Write a Python function called `calculate_volume_box` that takes length, width, and height as parameters and returns the volume of a rectangular box.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def calculate_volume_box(length, width, height):  # Function definition: calculate_volume_box
    return length * width * height  # Return the result

result = calculate_volume_box(5, 3, 4)  # Initialize variable or assign value
print(result)  # Expected: 60




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_triangle_valid` that takes three numbers representing side lengths and returns True if they can form a valid triangle, otherwise False.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1851  
Write a Python function called `check_triangle_valid` that takes three numbers representing side lengths and returns True if they can form a valid triangle, otherwise False.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_triangle_valid(a, b, c):  # Function definition: check_triangle_valid
    return a + b > c and a + c > b and b + c > a  # Return the result

print(check_triangle_valid(3, 4, 5), check_triangle_valid(1, 2, 5))  # Expected: True False




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `find_grade` that takes a score and returns a letter grade: 'A' for 90+, 'B' for 80-89, 'C' for 70-79, 'D' for 60-69, 'F' for below 60.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1852  
Write a Python function called `find_grade` that takes a score and returns a letter grade: 'A' for 90+, 'B' for 80-89, 'C' for 70-79, 'D' for 60-69, 'F' for below 60.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def find_grade(score):  # Function definition: find_grade
    if score >= 90:  # Conditional statement: check condition
        return 'A'  # Return the result
    elif score >= 80:  # Conditional statement: check condition
        return 'B'  # Return the result
    elif score >= 70:  # Conditional statement: check condition
        return 'C'  # Return the result
    elif score >= 60:  # Conditional statement: check condition
        return 'D'  # Return the result
    else:  # Else clause: execute when condition is false
        return 'F'  # Return the result

print(find_grade(95), find_grade(75), find_grade(55))  # Expected: A C F




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_season` that takes a month number (1-12) and returns the season: 'Winter' for 12,1,2; 'Spring' for 3,4,5; 'Summer' for 6,7,8; 'Fall' for 9,10,11.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1853  
Write a Python function called `get_season` that takes a month number (1-12) and returns the season: 'Winter' for 12,1,2; 'Spring' for 3,4,5; 'Summer' for 6,7,8; 'Fall' for 9,10,11.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_season(month):  # Function definition: get_season
    if month in [12, 1, 2]:  # Conditional statement: check condition
        return 'Winter'  # Return the result
    elif month in [3, 4, 5]:  # Conditional statement: check condition
        return 'Spring'  # Return the result
    elif month in [6, 7, 8]:  # Conditional statement: check condition
        return 'Summer'  # Return the result
    else:  # Else clause: execute when condition is false
        return 'Fall'  # Return the result

print(get_season(1), get_season(4), get_season(7), get_season(10))  # Expected: Winter Spring Summer Fall




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_discount` that takes a price and discount percentage, and returns the final price after applying the discount.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1854  
Write a Python function called `calculate_discount` that takes a price and discount percentage, and returns the final price after applying the discount.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def calculate_discount(price, discount_percent):  # Function definition: calculate_discount
    return price * (1 - discount_percent / 100)  # Return the result

result = calculate_discount(100, 20)  # Initialize variable or assign value
print(result)  # Expected: 80.0




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_tip` that takes a bill amount and tip percentage, and returns both the tip amount and total amount as a tuple.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1855  
Write a Python function called `calculate_tip` that takes a bill amount and tip percentage, and returns both the tip amount and total amount as a tuple.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def calculate_tip(bill_amount, tip_percent):  # Function definition: calculate_tip
    tip = bill_amount * (tip_percent / 100)  # Initialize variable or assign value
    total = bill_amount + tip  # Initialize variable or assign value
    return (tip, total)  # Return the result

result = calculate_tip(100, 15)  # Initialize variable or assign value
print(result)  # Expected: (15.0, 115.0)




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `swap_two_elements` that takes a list and two indices, and returns a new list with the elements at those indices swapped.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1856  
Write a Python function called `swap_two_elements` that takes a list and two indices, and returns a new list with the elements at those indices swapped.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def swap_two_elements(my_list, index1, index2):  # Function definition: swap_two_elements
    new_list = my_list.copy()  # Initialize variable or assign value
    new_list[index1], new_list[index2] = new_list[index2], new_list[index1]  # Initialize variable or assign value
    return new_list  # Return the result

result = swap_two_elements([10, 20, 30, 40], 0, 3)  # Initialize variable or assign value
print(result)  # Expected: [40, 20, 30, 10]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `insert_at_index` that takes a list, an index, and a value, and returns a new list with the value inserted at that index.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1857  
Write a Python function called `insert_at_index` that takes a list, an index, and a value, and returns a new list with the value inserted at that index.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def insert_at_index(my_list, index, value):  # Function definition: insert_at_index
    new_list = my_list.copy()  # Initialize variable or assign value
    new_list.insert(index, value)
    return new_list  # Return the result

result = insert_at_index([1, 2, 3, 4], 2, 99)  # Initialize variable or assign value
print(result)  # Expected: [1, 2, 99, 3, 4]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `remove_at_index` that takes a list and an index, and returns a new list with the element at that index removed.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1858  
Write a Python function called `remove_at_index` that takes a list and an index, and returns a new list with the element at that index removed.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def remove_at_index(my_list, index):  # Function definition: remove_at_index
    new_list = my_list.copy()  # Initialize variable or assign value
    new_list.pop(index)
    return new_list  # Return the result

result = remove_at_index([10, 20, 30, 40], 1)  # Initialize variable or assign value
print(result)  # Expected: [10, 30, 40]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `count_vowels_and_consonants` that takes a string and returns a tuple containing the count of vowels and consonants.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1859  
Write a Python function called `count_vowels_and_consonants` that takes a string and returns a tuple containing the count of vowels and consonants.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def count_vowels_and_consonants(text):  # Function definition: count_vowels_and_consonants
    vowels = "aeiouAEIOU"  # Initialize string variable
    vowel_count = sum(1 for char in text if char in vowels)  # Initialize variable or assign value
    consonant_count = sum(1 for char in text if char.isalpha() and char not in vowels)  # Initialize variable or assign value
    return (vowel_count, consonant_count)  # Return the result

result = count_vowels_and_consonants("Hello World")  # Initialize variable or assign value
print(result)  # Expected: (3, 7)




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_min_max` that takes a list of numbers and returns a tuple containing the minimum and maximum values.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1860  
Write a Python function called `get_min_max` that takes a list of numbers and returns a tuple containing the minimum and maximum values.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_min_max(numbers):  # Function definition: get_min_max
    return (min(numbers), max(numbers))  # Return the result

result = get_min_max([10, 5, 30, 20, 15])  # Use min/max with default parameter to handle empty sequences
print(result)  # Expected: (5, 30)




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_all_conditions` that takes a number and returns True if it is positive, even, and divisible by 3, otherwise False.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1861  
Write a Python function called `check_all_conditions` that takes a number and returns True if it is positive, even, and divisible by 3, otherwise False.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_all_conditions(number):  # Function definition: check_all_conditions
    return number > 0 and number % 2 == 0 and number % 3 == 0  # Return the result

print(check_all_conditions(6), check_all_conditions(5))  # Expected: True False




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `format_full_name` that takes first name, middle name, and last name, and returns a formatted full name string.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1862  
Write a Python function called `format_full_name` that takes first name, middle name, and last name, and returns a formatted full name string.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def format_full_name(first, middle, last):  # Function definition: format_full_name
    return f"{first} {middle} {last}"  # Return the result

result = format_full_name("John", "Michael", "Doe")  # Initialize variable or assign value
print(result)  # Expected: John Michael Doe




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_bmi` that takes weight in kg and height in meters, and returns the BMI value rounded to one decimal place.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1863  
Write a Python function called `calculate_bmi` that takes weight in kg and height in meters, and returns the BMI value rounded to one decimal place.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def calculate_bmi(weight_kg, height_m):  # Function definition: calculate_bmi
    bmi = weight_kg / (height_m ** 2)  # Initialize variable or assign value
    return round(bmi, 1)  # Return the result

result = calculate_bmi(70, 1.75)  # Initialize variable or assign value
print(result)  # Expected: 22.9




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_bmi_category` that takes weight and height, calculates BMI, and returns the category: 'Underweight' (<18.5), 'Normal' (18.5-24.9), 'Overweight' (25-29.9), 'Obese' (30+).
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1864  
Write a Python function called `check_bmi_category` that takes weight and height, calculates BMI, and returns the category: 'Underweight' (<18.5), 'Normal' (18.5-24.9), 'Overweight' (25-29.9), 'Obese' (30+).
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_bmi_category(weight_kg, height_m):  # Function definition: check_bmi_category
    bmi = weight_kg / (height_m ** 2)  # Initialize variable or assign value
    if bmi < 18.5:  # Conditional statement: check condition
        return 'Underweight'  # Return the result
    elif bmi < 25:  # Conditional statement: check condition
        return 'Normal'  # Return the result
    elif bmi < 30:  # Conditional statement: check condition
        return 'Overweight'  # Return the result
    else:  # Else clause: execute when condition is false
        return 'Obese'  # Return the result

result = check_bmi_category(70, 1.75)  # Initialize variable or assign value
print(result)  # Expected: Normal




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `find_common_elements_three` that takes three lists and returns a list of elements that appear in all three lists.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1865  
Write a Python function called `find_common_elements_three` that takes three lists and returns a list of elements that appear in all three lists.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def find_common_elements_three(list1, list2, list3):  # Function definition: find_common_elements_three
    return [x for x in list1 if x in list2 and x in list3]  # Return the result

result = find_common_elements_three([1, 2, 3], [2, 3, 4], [3, 4, 5])  # Initialize variable or assign value
print(result)  # Expected: [3]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `merge_three_lists` that takes three lists and returns a new list containing all elements from all three lists.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1866  
Write a Python function called `merge_three_lists` that takes three lists and returns a new list containing all elements from all three lists.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def merge_three_lists(list1, list2, list3):  # Function definition: merge_three_lists
    return list1 + list2 + list3  # Return the result

result = merge_three_lists([1, 2], [3, 4], [5, 6])  # Initialize variable or assign value
print(result)  # Expected: [1, 2, 3, 4, 5, 6]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_elements_at_indices` that takes a list and a list of indices, and returns a list of elements at those indices.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1867  
Write a Python function called `get_elements_at_indices` that takes a list and a list of indices, and returns a list of elements at those indices.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_elements_at_indices(my_list, indices):  # Function definition: get_elements_at_indices
    return [my_list[i] for i in indices]  # Return the result

result = get_elements_at_indices([10, 20, 30, 40, 50], [0, 2, 4])  # Initialize variable or assign value
print(result)  # Expected: [10, 30, 50]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `replace_multiple_chars` that takes a string and a dictionary mapping old characters to new characters, and returns a string with all replacements made.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1868  
Write a Python function called `replace_multiple_chars` that takes a string and a dictionary mapping old characters to new characters, and returns a string with all replacements made.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def replace_multiple_chars(text, replacements):  # Function definition: replace_multiple_chars
    result = text  # Initialize variable or assign value
    for old_char, new_char in replacements.items():  # Loop: iterate over sequence
        result = result.replace(old_char, new_char)  # Initialize variable or assign value
    return result  # Return the result

result = replace_multiple_chars("Hello World", {'H': 'J', 'o': 'a'})  # Initialize variable or assign value
print(result)  # Expected: Jella Warld




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `count_words_by_length` that takes a string and returns a dictionary where keys are word lengths and values are counts of words with that length.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1869  
Write a Python function called `count_words_by_length` that takes a string and returns a dictionary where keys are word lengths and values are counts of words with that length.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def count_words_by_length(text):  # Function definition: count_words_by_length
    words = text.split()  # Initialize variable or assign value
    counts = {}  # Initialize empty list/dict/set
    for word in words:  # Loop: iterate over sequence
        length = len(word)  # Initialize variable or assign value
        counts[length] = counts.get(length, 0) + 1  # Initialize variable or assign value
    return counts  # Return the result

result = count_words_by_length("hello world python programming")  # Initialize variable or assign value
print(result)  # Expected: {5: 2, 6: 2, 11: 1}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `filter_and_transform` that takes a list of numbers and returns a new list containing only even numbers, each multiplied by 2.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1870  
Write a Python function called `filter_and_transform` that takes a list of numbers and returns a new list containing only even numbers, each multiplied by 2.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def filter_and_transform(numbers):  # Function definition: filter_and_transform
    return [x * 2 for x in numbers if x % 2 == 0]  # Return the result

result = filter_and_transform([1, 2, 3, 4, 5, 6])  # Initialize variable or assign value
print(result)  # Expected: [4, 8, 12]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_strings_starting_with` that takes a list of strings and a prefix, and returns a new list containing only strings that start with that prefix.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1871  
Write a Python function called `get_strings_starting_with` that takes a list of strings and a prefix, and returns a new list containing only strings that start with that prefix.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_strings_starting_with(strings, prefix):  # Function definition: get_strings_starting_with
    return [s for s in strings if s.startswith(prefix)]  # Return the result

result = get_strings_starting_with(["apple", "banana", "apricot", "cherry"], "ap")  # Initialize variable or assign value
print(result)  # Expected: ['apple', 'apricot']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_strings_ending_with` that takes a list of strings and a suffix, and returns a new list containing only strings that end with that suffix.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1872  
Write a Python function called `get_strings_ending_with` that takes a list of strings and a suffix, and returns a new list containing only strings that end with that suffix.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_strings_ending_with(strings, suffix):  # Function definition: get_strings_ending_with
    return [s for s in strings if s.endswith(suffix)]  # Return the result

result = get_strings_ending_with(["running", "walking", "jumping", "swimming"], "ing")  # Initialize variable or assign value
print(result)  # Expected: ['running', 'walking', 'jumping', 'swimming']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_total_cost` that takes a list of prices and a tax rate percentage, and returns the total cost including tax.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1873  
Write a Python function called `calculate_total_cost` that takes a list of prices and a tax rate percentage, and returns the total cost including tax.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def calculate_total_cost(prices, tax_rate):  # Function definition: calculate_total_cost
    subtotal = sum(prices)  # Initialize variable or assign value
    tax = subtotal * (tax_rate / 100)  # Initialize variable or assign value
    return subtotal + tax  # Return the result

result = calculate_total_cost([10, 20, 30], 10)  # Initialize variable or assign value
print(result)  # Expected: 66.0




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `find_all_indices` that takes a list and an element, and returns a list of all indices where that element appears.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1874  
Write a Python function called `find_all_indices` that takes a list and an element, and returns a list of all indices where that element appears.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def find_all_indices(my_list, element):  # Function definition: find_all_indices
    return [i for i, x in enumerate(my_list) if x == element]  # Return the result

result = find_all_indices([10, 20, 10, 30, 10], 10)  # Initialize variable or assign value
print(result)  # Expected: [0, 2, 4]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `split_into_chunks` that takes a list and a chunk size, and returns a list of lists where each inner list has at most chunk_size elements.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1875  
Write a Python function called `split_into_chunks` that takes a list and a chunk size, and returns a list of lists where each inner list has at most chunk_size elements.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def split_into_chunks(my_list, chunk_size):  # Function definition: split_into_chunks
    return [my_list[i:i+chunk_size] for i in range(0, len(my_list), chunk_size)]  # Return the result

result = split_into_chunks([1, 2, 3, 4, 5, 6, 7], 3)  # Initialize variable or assign value
print(result)  # Expected: [[1, 2, 3], [4, 5, 6], [7]]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `remove_multiple_elements` that takes a list and a list of elements to remove, and returns a new list with all those elements removed.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1876  
Write a Python function called `remove_multiple_elements` that takes a list and a list of elements to remove, and returns a new list with all those elements removed.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def remove_multiple_elements(my_list, elements_to_remove):  # Function definition: remove_multiple_elements
    return [x for x in my_list if x not in elements_to_remove]  # Return the result

result = remove_multiple_elements([1, 2, 3, 4, 5, 6], [2, 4, 6])  # Initialize variable or assign value
print(result)  # Expected: [1, 3, 5]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `count_occurrences_multiple` that takes a list and a list of elements, and returns a dictionary with counts of each element.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1877  
Write a Python function called `count_occurrences_multiple` that takes a list and a list of elements, and returns a dictionary with counts of each element.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def count_occurrences_multiple(my_list, elements):  # Function definition: count_occurrences_multiple
    return {elem: my_list.count(elem) for elem in elements}  # Return the result

result = count_occurrences_multiple([1, 2, 2, 3, 3, 3, 4], [2, 3])  # Initialize variable or assign value
print(result)  # Expected: {2: 2, 3: 3}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_unique_elements_three` that takes three lists and returns a list of elements that appear in exactly one of the three lists.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1878  
Write a Python function called `get_unique_elements_three` that takes three lists and returns a list of elements that appear in exactly one of the three lists.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_unique_elements_three(list1, list2, list3):  # Function definition: get_unique_elements_three
    all_elements = list1 + list2 + list3  # Initialize variable or assign value
    result = []  # Initialize empty list/dict/set
    for elem in all_elements:  # Loop: iterate over sequence
        count = list1.count(elem) + list2.count(elem) + list3.count(elem)  # Initialize variable or assign value
        if count == 1:  # Conditional statement: check condition
            result.append(elem)  # Add element to list
    return list(set(result))  # Return the result

result = get_unique_elements_three([1, 2, 3], [2, 3, 4], [3, 4, 5])  # Initialize variable or assign value
print(sorted(result))  # Expected: [1, 5]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `sort_by_multiple_criteria` that takes a list of tuples (name, age, score) and returns the list sorted first by age, then by score.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1879  
Write a Python function called `sort_by_multiple_criteria` that takes a list of tuples (name, age, score) and returns the list sorted first by age, then by score.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def sort_by_multiple_criteria(people):  # Function definition: sort_by_multiple_criteria
    return sorted(people, key=lambda x: (x[1], x[2]))  # Return the result

result = sort_by_multiple_criteria([("Alice", 25, 85), ("Bob", 25, 90), ("Charlie", 30, 80)])  # Initialize variable or assign value
print(result)  # Expected: [('Alice', 25, 85), ('Bob', 25, 90), ('Charlie', 30, 80)]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_statistics` that takes a list of numbers and returns a dictionary with 'sum', 'average', 'min', and 'max' keys.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1880  
Write a Python function called `calculate_statistics` that takes a list of numbers and returns a dictionary with 'sum', 'average', 'min', and 'max' keys.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def calculate_statistics(numbers):  # Function definition: calculate_statistics
    return {  # Return the result
        'sum': sum(numbers),
        'average': sum(numbers) / len(numbers),
        'min': min(numbers),
        'max': max(numbers)
    }

result = calculate_statistics([10, 20, 30, 40])  # Initialize variable or assign value
print(result)  # Expected: {'sum': 100, 'average': 25.0, 'min': 10, 'max': 40}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `extract_numbers_from_string` that takes a string and returns a list of all numbers found in the string (as integers).
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1881  
Write a Python function called `extract_numbers_from_string` that takes a string and returns a list of all numbers found in the string (as integers).
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def extract_numbers_from_string(text):  # Function definition: extract_numbers_from_string
    import re  # Import statement: load module or specific functions
    return [int(match) for match in re.findall(r'\d+', text)]  # Return the result

result = extract_numbers_from_string("I have 3 cats and 2 dogs")  # Initialize variable or assign value
print(result)  # Expected: [3, 2]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `format_address` that takes street, city, state, and zipcode, and returns a formatted address string on separate lines.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1882  
Write a Python function called `format_address` that takes street, city, state, and zipcode, and returns a formatted address string on separate lines.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def format_address(street, city, state, zipcode):  # Function definition: format_address
    return f"{street}\n{city}, {state} {zipcode}"  # Return the result

result = format_address("123 Main St", "New York", "NY", "10001")  # Initialize variable or assign value
print(result)  # Expected: 123 Main St\nNew York, NY 10001




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_password_strength` that takes a password string and returns True if it has at least 8 characters, contains both letters and digits, otherwise False.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1883  
Write a Python function called `check_password_strength` that takes a password string and returns True if it has at least 8 characters, contains both letters and digits, otherwise False.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_password_strength(password):  # Function definition: check_password_strength
    return len(password) >= 8 and any(c.isalpha() for c in password) and any(c.isdigit() for c in password)  # Return the result

print(check_password_strength("Password123"), check_password_strength("weak"))  # Expected: True False




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_words_by_length_range` that takes a string and min/max length, and returns a list of words within that length range.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1884  
Write a Python function called `get_words_by_length_range` that takes a string and min/max length, and returns a list of words within that length range.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_words_by_length_range(text, min_length, max_length):  # Function definition: get_words_by_length_range
    words = text.split()  # Initialize variable or assign value
    return [word for word in words if min_length <= len(word) <= max_length]  # Return the result

result = get_words_by_length_range("hello world python programming", 5, 6)  # Initialize variable or assign value
print(result)  # Expected: ['hello', 'world', 'python']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_compound_interest` that takes principal, rate, time, and compounding frequency, and returns the final amount.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1885  
Write a Python function called `calculate_compound_interest` that takes principal, rate, time, and compounding frequency, and returns the final amount.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def calculate_compound_interest(principal, rate, time, frequency):  # Function definition: calculate_compound_interest
    return principal * (1 + rate / (100 * frequency)) ** (frequency * time)  # Return the result

result = calculate_compound_interest(1000, 5, 2, 12)  # Initialize variable or assign value
print(round(result, 2))  # Expected: 1104.94




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `find_duplicate_elements` that takes a list and returns a list of elements that appear more than once.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1886  
Write a Python function called `find_duplicate_elements` that takes a list and returns a list of elements that appear more than once.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def find_duplicate_elements(my_list):  # Function definition: find_duplicate_elements
    seen = set()  # Initialize empty list/dict/set
    duplicates = set()  # Initialize empty list/dict/set
    for item in my_list:  # Loop: iterate over sequence
        if item in seen:  # Conditional statement: check condition
            duplicates.add(item)  # Add element to set
        seen.add(item)  # Add element to set
    return list(duplicates)  # Return the result

result = find_duplicate_elements([1, 2, 2, 3, 3, 3, 4])  # Initialize variable or assign value
print(sorted(result))  # Expected: [2, 3]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `group_by_first_letter` that takes a list of strings and returns a dictionary where keys are first letters and values are lists of strings starting with that letter.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1887  
Write a Python function called `group_by_first_letter` that takes a list of strings and returns a dictionary where keys are first letters and values are lists of strings starting with that letter.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def group_by_first_letter(strings):  # Function definition: group_by_first_letter
    groups = {}  # Initialize empty list/dict/set
    for s in strings:  # Loop: iterate over sequence
        first_letter = s[0].lower()  # Initialize variable or assign value
        if first_letter not in groups:  # Conditional statement: check condition
            groups[first_letter] = []  # Initialize empty list/dict/set
        groups[first_letter].append(s)  # Add element to list
    return groups  # Return the result

result = group_by_first_letter(["apple", "banana", "apricot", "cherry"])  # Initialize variable or assign value
print(result)  # Expected: {'a': ['apple', 'apricot'], 'b': ['banana'], 'c': ['cherry']}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_distance` that takes two points (x1, y1) and (x2, y2) and returns the Euclidean distance between them.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1888  
Write a Python function called `calculate_distance` that takes two points (x1, y1) and (x2, y2) and returns the Euclidean distance between them.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

import math  # Import statement: load module or specific functions

def calculate_distance(x1, y1, x2, y2):  # Function definition: calculate_distance
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  # Return the result

result = calculate_distance(0, 0, 3, 4)  # Initialize variable or assign value
print(result)  # Expected: 5.0




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_in_range` that takes a number and a range (min, max), and returns True if the number is within the range (inclusive), otherwise False.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1889  
Write a Python function called `check_in_range` that takes a number and a range (min, max), and returns True if the number is within the range (inclusive), otherwise False.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_in_range(number, min_val, max_val):  # Function definition: check_in_range
    return min_val <= number <= max_val  # Return the result

print(check_in_range(5, 1, 10), check_in_range(15, 1, 10))  # Expected: True False




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_divisors` that takes a number and returns a list of all divisors of that number.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1890  
Write a Python function called `get_divisors` that takes a number and returns a list of all divisors of that number.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_divisors(number):  # Function definition: get_divisors
    return [i for i in range(1, number + 1) if number % i == 0]  # Return the result

result = get_divisors(12)  # Initialize variable or assign value
print(result)  # Expected: [1, 2, 3, 4, 6, 12]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_perfect_square` that takes a number and returns True if it is a perfect square, otherwise False.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1891  
Write a Python function called `check_perfect_square` that takes a number and returns True if it is a perfect square, otherwise False.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_perfect_square(number):  # Function definition: check_perfect_square
    import math  # Import statement: load module or specific functions
    root = math.sqrt(number)  # Initialize variable or assign value
    return root == int(root)  # Return the result

print(check_perfect_square(16), check_perfect_square(15))  # Expected: True False




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `format_time` that takes hours, minutes, and seconds, and returns a formatted time string as HH:MM:SS.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1892  
Write a Python function called `format_time` that takes hours, minutes, and seconds, and returns a formatted time string as HH:MM:SS.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def format_time(hours, minutes, seconds):  # Function definition: format_time
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"  # Return the result

result = format_time(9, 5, 3)  # Initialize variable or assign value
print(result)  # Expected: 09:05:03




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_age` that takes birth year, birth month, and birth day, and returns the age in years (assuming current date is 2024-01-01).
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1893  
Write a Python function called `calculate_age` that takes birth year, birth month, and birth day, and returns the age in years (assuming current date is 2024-01-01).
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def calculate_age(birth_year, birth_month, birth_day):  # Function definition: calculate_age
    current_year = 2024  # Initialize variable or assign value
    current_month = 1  # Initialize variable or assign value
    current_day = 1  # Initialize variable or assign value
    age = current_year - birth_year  # Initialize variable or assign value
    if (current_month, current_day) < (birth_month, birth_day):  # Conditional statement: check condition
        age -= 1
    return age  # Return the result

result = calculate_age(2000, 6, 15)  # Initialize variable or assign value
print(result)  # Expected: 23




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_middle_elements` that takes a list and returns a new list containing elements from index 1 to -1 (excluding first and last).
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1894  
Write a Python function called `get_middle_elements` that takes a list and returns a new list containing elements from index 1 to -1 (excluding first and last).
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_middle_elements(my_list):  # Function definition: get_middle_elements
    return my_list[1:-1]  # Return the result

result = get_middle_elements([10, 20, 30, 40, 50])  # Initialize variable or assign value
print(result)  # Expected: [20, 30, 40]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `swap_adjacent_elements` that takes a list and returns a new list with adjacent elements swapped (1st with 2nd, 3rd with 4th, etc.).
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1895  
Write a Python function called `swap_adjacent_elements` that takes a list and returns a new list with adjacent elements swapped (1st with 2nd, 3rd with 4th, etc.).
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def swap_adjacent_elements(my_list):  # Function definition: swap_adjacent_elements
    new_list = my_list.copy()  # Initialize variable or assign value
    for i in range(0, len(new_list) - 1, 2):  # Loop: iterate over sequence
        new_list[i], new_list[i + 1] = new_list[i + 1], new_list[i]  # Initialize variable or assign value
    return new_list  # Return the result

result = swap_adjacent_elements([1, 2, 3, 4, 5, 6])  # Initialize variable or assign value
print(result)  # Expected: [2, 1, 4, 3, 6, 5]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_every_nth_element` that takes a list and a number n, and returns a list containing every nth element starting from index 0.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1896  
Write a Python function called `get_every_nth_element` that takes a list and a number n, and returns a list containing every nth element starting from index 0.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_every_nth_element(my_list, n):  # Function definition: get_every_nth_element
    return my_list[::n]  # Return the result

result = get_every_nth_element([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3)  # Initialize variable or assign value
print(result)  # Expected: [0, 3, 6, 9]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `count_uppercase_lowercase` that takes a string and returns a dictionary with 'uppercase' and 'lowercase' keys containing their counts.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1897  
Write a Python function called `count_uppercase_lowercase` that takes a string and returns a dictionary with 'uppercase' and 'lowercase' keys containing their counts.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def count_uppercase_lowercase(text):  # Function definition: count_uppercase_lowercase
    return {  # Return the result
        'uppercase': sum(1 for c in text if c.isupper()),  # Generator expression or comprehension
        'lowercase': sum(1 for c in text if c.islower())  # Generator expression or comprehension
    }

result = count_uppercase_lowercase("Hello World")  # Initialize variable or assign value
print(result)  # Expected: {'uppercase': 2, 'lowercase': 8}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `remove_duplicates_preserve_order` that takes a list and returns a new list with duplicates removed while preserving the order of first occurrence.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1898  
Write a Python function called `remove_duplicates_preserve_order` that takes a list and returns a new list with duplicates removed while preserving the order of first occurrence.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def remove_duplicates_preserve_order(my_list):  # Function definition: remove_duplicates_preserve_order
    seen = set()  # Initialize empty list/dict/set
    result = []  # Initialize empty list/dict/set
    for item in my_list:  # Loop: iterate over sequence
        if item not in seen:  # Conditional statement: check condition
            seen.add(item)  # Add element to set
            result.append(item)  # Add element to list
    return result  # Return the result

result = remove_duplicates_preserve_order([1, 2, 2, 3, 3, 3, 4, 2])  # Initialize variable or assign value
print(result)  # Expected: [1, 2, 3, 4]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_intersection_three_lists` that takes three lists and returns a list of elements that appear in all three lists.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1899  
Write a Python function called `get_intersection_three_lists` that takes three lists and returns a list of elements that appear in all three lists.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_intersection_three_lists(list1, list2, list3):  # Function definition: get_intersection_three_lists
    return [x for x in list1 if x in list2 and x in list3]  # Return the result

result = get_intersection_three_lists([1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6])  # Initialize variable or assign value
print(result)  # Expected: [3, 4]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_percentage` that takes a part and a whole, and returns the percentage as a float rounded to 2 decimal places.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1900  
Write a Python function called `calculate_percentage` that takes a part and a whole, and returns the percentage as a float rounded to 2 decimal places.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def calculate_percentage(part, whole):  # Function definition: calculate_percentage
    return round((part / whole) * 100, 2)  # Return the result

result = calculate_percentage(25, 100)  # Initialize variable or assign value
print(result)  # Expected: 25.0




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `find_largest_three` that takes a list of numbers and returns a list containing the three largest numbers.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1901  
Write a Python function called `find_largest_three` that takes a list of numbers and returns a list containing the three largest numbers.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def find_largest_three(numbers):  # Function definition: find_largest_three
    return sorted(numbers, reverse=True)[:3]  # Return the result

result = find_largest_three([10, 5, 30, 20, 15, 25])  # Initialize variable or assign value
print(result)  # Expected: [30, 25, 20]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `find_smallest_three` that takes a list of numbers and returns a list containing the three smallest numbers.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1902  
Write a Python function called `find_smallest_three` that takes a list of numbers and returns a list containing the three smallest numbers.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def find_smallest_three(numbers):  # Function definition: find_smallest_three
    return sorted(numbers)[:3]  # Return the result

result = find_smallest_three([10, 5, 30, 20, 15, 25])  # Initialize variable or assign value
print(result)  # Expected: [5, 10, 15]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_palindrome_and_length` that takes a string and returns a tuple containing True/False for palindrome and the string length.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1903  
Write a Python function called `check_palindrome_and_length` that takes a string and returns a tuple containing True/False for palindrome and the string length.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_palindrome_and_length(text):  # Function definition: check_palindrome_and_length
    is_palindrome = text == text[::-1]  # Initialize variable or assign value
    length = len(text)  # Initialize variable or assign value
    return (is_palindrome, length)  # Return the result

result = check_palindrome_and_length("racecar")  # Initialize variable or assign value
print(result)  # Expected: (True, 7)




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_words_starting_with_vowel` that takes a string and returns a list of words that start with a vowel.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1904  
Write a Python function called `get_words_starting_with_vowel` that takes a string and returns a list of words that start with a vowel.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_words_starting_with_vowel(text):  # Function definition: get_words_starting_with_vowel
    vowels = "aeiouAEIOU"  # Initialize string variable
    words = text.split()  # Initialize variable or assign value
    return [word for word in words if word[0] in vowels]  # Return the result

result = get_words_starting_with_vowel("apple orange banana cherry")  # Initialize variable or assign value
print(result)  # Expected: ['apple', 'orange']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_words_ending_with_consonant` that takes a string and returns a list of words that end with a consonant.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1905  
Write a Python function called `get_words_ending_with_consonant` that takes a string and returns a list of words that end with a consonant.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_words_ending_with_consonant(text):  # Function definition: get_words_ending_with_consonant
    vowels = "aeiouAEIOU"  # Initialize string variable
    words = text.split()  # Initialize variable or assign value
    return [word for word in words if word[-1] not in vowels and word[-1].isalpha()]  # Return the result

result = get_words_ending_with_consonant("hello world python")  # Initialize variable or assign value
print(result)  # Expected: ['hello', 'world', 'python']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_area_perimeter` that takes length and width, and returns a tuple containing area and perimeter of a rectangle.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1906  
Write a Python function called `calculate_area_perimeter` that takes length and width, and returns a tuple containing area and perimeter of a rectangle.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def calculate_area_perimeter(length, width):  # Function definition: calculate_area_perimeter
    area = length * width  # Initialize variable or assign value
    perimeter = 2 * (length + width)  # Initialize variable or assign value
    return (area, perimeter)  # Return the result

result = calculate_area_perimeter(5, 3)  # Initialize variable or assign value
print(result)  # Expected: (15, 16)




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `format_currency` that takes a number and returns it formatted as currency with dollar sign and two decimal places.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1907  
Write a Python function called `format_currency` that takes a number and returns it formatted as currency with dollar sign and two decimal places.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def format_currency(amount):  # Function definition: format_currency
    return f"${amount:.2f}"  # Return the result

result = format_currency(1234.5)  # Initialize variable or assign value
print(result)  # Expected: $1234.50




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_even_indices` that takes a list and returns a list containing elements at even indices (0, 2, 4, ...).
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1908  
Write a Python function called `get_even_indices` that takes a list and returns a list containing elements at even indices (0, 2, 4, ...).
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_even_indices(my_list):  # Function definition: get_even_indices
    return [my_list[i] for i in range(0, len(my_list), 2)]  # Return the result

result = get_even_indices([10, 20, 30, 40, 50])  # Initialize variable or assign value
print(result)  # Expected: [10, 30, 50]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_odd_indices` that takes a list and returns a list containing elements at odd indices (1, 3, 5, ...).
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1909  
Write a Python function called `get_odd_indices` that takes a list and returns a list containing elements at odd indices (1, 3, 5, ...).
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_odd_indices(my_list):  # Function definition: get_odd_indices
    return [my_list[i] for i in range(1, len(my_list), 2)]  # Return the result

result = get_odd_indices([10, 20, 30, 40, 50])  # Initialize variable or assign value
print(result)  # Expected: [20, 40]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `multiply_corresponding` that takes two lists of numbers and returns a new list where each element is the product of corresponding elements.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1910  
Write a Python function called `multiply_corresponding` that takes two lists of numbers and returns a new list where each element is the product of corresponding elements.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def multiply_corresponding(list1, list2):  # Function definition: multiply_corresponding
    return [a * b for a, b in zip(list1, list2)]  # Return the result

result = multiply_corresponding([2, 3, 4], [5, 6, 7])  # Initialize variable or assign value
print(result)  # Expected: [10, 18, 28]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `divide_corresponding` that takes two lists of numbers and returns a new list where each element is the division of corresponding elements (handle division by zero by returning None).
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1911  
Write a Python function called `divide_corresponding` that takes two lists of numbers and returns a new list where each element is the division of corresponding elements (handle division by zero by returning None).
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def divide_corresponding(list1, list2):  # Function definition: divide_corresponding
    result = []  # Initialize empty list/dict/set
    for a, b in zip(list1, list2):  # Loop: iterate over sequence
        if b == 0:  # Conditional statement: check condition
            result.append(None)  # Add element to list
        else:  # Else clause: execute when condition is false
            result.append(a / b)  # Add element to list
    return result  # Return the result

result = divide_corresponding([10, 20, 30], [2, 0, 5])  # Initialize variable or assign value
print(result)  # Expected: [5.0, None, 6.0]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_strings_containing` that takes a list of strings and a substring, and returns a list of strings that contain that substring.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1912  
Write a Python function called `get_strings_containing` that takes a list of strings and a substring, and returns a list of strings that contain that substring.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_strings_containing(strings, substring):  # Function definition: get_strings_containing
    return [s for s in strings if substring in s]  # Return the result

result = get_strings_containing(["hello", "world", "python", "programming"], "on")  # Initialize variable or assign value
print(result)  # Expected: ['python', 'programming']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `count_characters_by_type` that takes a string and returns a dictionary with 'letters', 'digits', and 'others' keys containing their counts.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1913  
Write a Python function called `count_characters_by_type` that takes a string and returns a dictionary with 'letters', 'digits', and 'others' keys containing their counts.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def count_characters_by_type(text):  # Function definition: count_characters_by_type
    return {  # Return the result
        'letters': sum(1 for c in text if c.isalpha()),  # Generator expression or comprehension
        'digits': sum(1 for c in text if c.isdigit()),  # Generator expression or comprehension
        'others': sum(1 for c in text if not c.isalnum() and not c.isspace())  # Generator expression or comprehension
    }

result = count_characters_by_type("Hello123!")  # Initialize variable or assign value
print(result)  # Expected: {'letters': 5, 'digits': 3, 'others': 1}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_range_between` that takes a list and two values, and returns a list of elements that fall between those two values (inclusive).
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1914  
Write a Python function called `get_range_between` that takes a list and two values, and returns a list of elements that fall between those two values (inclusive).
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_range_between(my_list, min_val, max_val):  # Function definition: get_range_between
    return [x for x in my_list if min_val <= x <= max_val]  # Return the result

result = get_range_between([10, 20, 30, 40, 50], 20, 40)  # Initialize variable or assign value
print(result)  # Expected: [20, 30, 40]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `format_date` that takes year, month, and day, and returns a formatted date string as YYYY-MM-DD.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1915  
Write a Python function called `format_date` that takes year, month, and day, and returns a formatted date string as YYYY-MM-DD.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def format_date(year, month, day):  # Function definition: format_date
    return f"{year}-{month:02d}-{day:02d}"  # Return the result

result = format_date(2024, 3, 5)  # Initialize variable or assign value
print(result)  # Expected: 2024-03-05




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_simple_interest` that takes principal, rate, and time, and returns the simple interest amount.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1916  
Write a Python function called `calculate_simple_interest` that takes principal, rate, and time, and returns the simple interest amount.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def calculate_simple_interest(principal, rate, time):  # Function definition: calculate_simple_interest
    return principal * rate * time / 100  # Return the result

result = calculate_simple_interest(1000, 5, 2)  # Initialize variable or assign value
print(result)  # Expected: 100.0




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_unique_characters` that takes a string and returns a list of unique characters in the order they first appear.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1917  
Write a Python function called `get_unique_characters` that takes a string and returns a list of unique characters in the order they first appear.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_unique_characters(text):  # Function definition: get_unique_characters
    seen = set()  # Initialize empty list/dict/set
    result = []  # Initialize empty list/dict/set
    for char in text:  # Loop: iterate over sequence
        if char not in seen:  # Conditional statement: check condition
            seen.add(char)  # Add element to set
            result.append(char)  # Add element to list
    return result  # Return the result

result = get_unique_characters("hello")  # Initialize variable or assign value
print(result)  # Expected: ['h', 'e', 'l', 'o']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `count_words_ending_with` that takes a string and a suffix, and returns the number of words that end with that suffix.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1918  
Write a Python function called `count_words_ending_with` that takes a string and a suffix, and returns the number of words that end with that suffix.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def count_words_ending_with(text, suffix):  # Function definition: count_words_ending_with
    words = text.split()  # Initialize variable or assign value
    return sum(1 for word in words if word.endswith(suffix))  # Return the result

result = count_words_ending_with("running walking jumping", "ing")  # Initialize variable or assign value
print(result)  # Expected: 3




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_numbers_in_range` that takes a list of numbers and a range (min, max), and returns a list of numbers within that range.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1919  
Write a Python function called `get_numbers_in_range` that takes a list of numbers and a range (min, max), and returns a list of numbers within that range.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_numbers_in_range(numbers, min_val, max_val):  # Function definition: get_numbers_in_range
    return [x for x in numbers if min_val <= x <= max_val]  # Return the result

result = get_numbers_in_range([10, 20, 30, 40, 50], 25, 45)  # Initialize variable or assign value
print(result)  # Expected: [30, 40]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `format_name_age_city` that takes name, age, and city, and returns a formatted string: 'Name: {name}, Age: {age}, City: {city}'.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1920  
Write a Python function called `format_name_age_city` that takes name, age, and city, and returns a formatted string: 'Name: {name}, Age: {age}, City: {city}'.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def format_name_age_city(name, age, city):  # Function definition: format_name_age_city
    return f"Name: {name}, Age: {age}, City: {city}"  # Return the result

result = format_name_age_city("Alice", 30, "New York")  # Initialize variable or assign value
print(result)  # Expected: Name: Alice, Age: 30, City: New York




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_multiple_of` that takes a number and a list of divisors, and returns True if the number is divisible by all divisors, otherwise False.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1921  
Write a Python function called `check_multiple_of` that takes a number and a list of divisors, and returns True if the number is divisible by all divisors, otherwise False.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_multiple_of(number, divisors):  # Function definition: check_multiple_of
    return all(number % d == 0 for d in divisors)  # Return the result

print(check_multiple_of(12, [2, 3, 4]), check_multiple_of(12, [2, 3, 5]))  # Expected: True False




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_sum_of_squares` that takes a list of numbers and returns the sum of squares of all numbers.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1922  
Write a Python function called `get_sum_of_squares` that takes a list of numbers and returns the sum of squares of all numbers.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_sum_of_squares(numbers):  # Function definition: get_sum_of_squares
    return sum(x ** 2 for x in numbers)  # Return the result

result = get_sum_of_squares([1, 2, 3, 4])  # Initialize variable or assign value
print(result)  # Expected: 30




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_product_of_even` that takes a list of numbers and returns the product of all even numbers.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1923  
Write a Python function called `get_product_of_even` that takes a list of numbers and returns the product of all even numbers.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_product_of_even(numbers):  # Function definition: get_product_of_even
    product = 1  # Initialize variable or assign value
    for x in numbers:  # Loop: iterate over sequence
        if x % 2 == 0:  # Conditional statement: check condition
            product *= x
    return product  # Return the result

result = get_product_of_even([1, 2, 3, 4, 5, 6])  # Initialize variable or assign value
print(result)  # Expected: 48




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_sum_of_odd` that takes a list of numbers and returns the sum of all odd numbers.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1924  
Write a Python function called `get_sum_of_odd` that takes a list of numbers and returns the sum of all odd numbers.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_sum_of_odd(numbers):  # Function definition: get_sum_of_odd
    return sum(x for x in numbers if x % 2 != 0)  # Return the result

result = get_sum_of_odd([1, 2, 3, 4, 5, 6])  # Initialize variable or assign value
print(result)  # Expected: 9




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `find_second_occurrence` that takes a list and an element, and returns the index of the second occurrence of that element, or -1 if not found.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1925  
Write a Python function called `find_second_occurrence` that takes a list and an element, and returns the index of the second occurrence of that element, or -1 if not found.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def find_second_occurrence(my_list, element):  # Function definition: find_second_occurrence
    count = 0  # Initialize variable or assign value
    for i, item in enumerate(my_list):  # Loop: iterate over sequence
        if item == element:  # Conditional statement: check condition
            count += 1
            if count == 2:  # Conditional statement: check condition
                return i  # Return the result
    return -1  # Return the result

result = find_second_occurrence([10, 20, 10, 30, 10], 10)  # Initialize variable or assign value
print(result)  # Expected: 2




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_elements_greater_than_average` that takes a list of numbers and returns a list of numbers greater than the average.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1926  
Write a Python function called `get_elements_greater_than_average` that takes a list of numbers and returns a list of numbers greater than the average.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_elements_greater_than_average(numbers):  # Function definition: get_elements_greater_than_average
    avg = sum(numbers) / len(numbers)  # Initialize variable or assign value
    return [x for x in numbers if x > avg]  # Return the result

result = get_elements_greater_than_average([10, 20, 30, 40])  # Initialize variable or assign value
print(result)  # Expected: [30, 40]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_elements_less_than_average` that takes a list of numbers and returns a list of numbers less than the average.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1927  
Write a Python function called `get_elements_less_than_average` that takes a list of numbers and returns a list of numbers less than the average.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_elements_less_than_average(numbers):  # Function definition: get_elements_less_than_average
    avg = sum(numbers) / len(numbers)  # Initialize variable or assign value
    return [x for x in numbers if x < avg]  # Return the result

result = get_elements_less_than_average([10, 20, 30, 40])  # Initialize variable or assign value
print(result)  # Expected: [10, 20]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `count_digits_letters` that takes a string and returns a tuple containing the count of digits and the count of letters.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1928  
Write a Python function called `count_digits_letters` that takes a string and returns a tuple containing the count of digits and the count of letters.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def count_digits_letters(text):  # Function definition: count_digits_letters
    digits = sum(1 for c in text if c.isdigit())  # Initialize variable or assign value
    letters = sum(1 for c in text if c.isalpha())  # Initialize variable or assign value
    return (digits, letters)  # Return the result

result = count_digits_letters("Hello123World")  # Initialize variable or assign value
print(result)  # Expected: (3, 10)




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_words_with_length` that takes a string and a length, and returns a list of words with exactly that length.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1929  
Write a Python function called `get_words_with_length` that takes a string and a length, and returns a list of words with exactly that length.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_words_with_length(text, length):  # Function definition: get_words_with_length
    words = text.split()  # Initialize variable or assign value
    return [word for word in words if len(word) == length]  # Return the result

result = get_words_with_length("hello world python programming", 5)  # Initialize variable or assign value
print(result)  # Expected: ['hello', 'world']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `format_full_address` that takes street number, street name, city, state, and zipcode, and returns a complete formatted address.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1930  
Write a Python function called `format_full_address` that takes street number, street name, city, state, and zipcode, and returns a complete formatted address.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def format_full_address(street_num, street_name, city, state, zipcode):  # Function definition: format_full_address
    return f"{street_num} {street_name}, {city}, {state} {zipcode}"  # Return the result

result = format_full_address("123", "Main St", "New York", "NY", "10001")  # Initialize variable or assign value
print(result)  # Expected: 123 Main St, New York, NY 10001




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_total_with_discount` that takes a list of prices, a discount percentage, and a tax rate, and returns the final total.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1931  
Write a Python function called `calculate_total_with_discount` that takes a list of prices, a discount percentage, and a tax rate, and returns the final total.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def calculate_total_with_discount(prices, discount_percent, tax_rate):  # Function definition: calculate_total_with_discount
    subtotal = sum(prices)  # Initialize variable or assign value
    discounted = subtotal * (1 - discount_percent / 100)  # Initialize variable or assign value
    total = discounted * (1 + tax_rate / 100)  # Initialize variable or assign value
    return total  # Return the result

result = calculate_total_with_discount([100, 50], 10, 8)  # Initialize variable or assign value
print(round(result, 2))  # Expected: 145.8




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_common_prefix` that takes two strings and returns the longest common prefix they share.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1932  
Write a Python function called `get_common_prefix` that takes two strings and returns the longest common prefix they share.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_common_prefix(str1, str2):  # Function definition: get_common_prefix
    prefix = ""  # Initialize string variable
    for i in range(min(len(str1), len(str2))):  # Loop: iterate over sequence
        if str1[i] == str2[i]:  # Conditional statement: check condition
            prefix += str1[i]
        else:  # Else clause: execute when condition is false
            break
    return prefix  # Return the result

result = get_common_prefix("hello", "help")  # Initialize variable or assign value
print(result)  # Expected: hel




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_common_suffix` that takes two strings and returns the longest common suffix they share.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1933  
Write a Python function called `get_common_suffix` that takes two strings and returns the longest common suffix they share.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_common_suffix(str1, str2):  # Function definition: get_common_suffix
    suffix = ""  # Initialize string variable
    for i in range(1, min(len(str1), len(str2)) + 1):  # Loop: iterate over sequence
        if str1[-i] == str2[-i]:  # Conditional statement: check condition
            suffix = str1[-i] + suffix  # Initialize variable or assign value
        else:  # Else clause: execute when condition is false
            break
    return suffix  # Return the result

result = get_common_suffix("running", "walking")  # Initialize variable or assign value
print(result)  # Expected: ing




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_all_uppercase_words` that takes a string and returns True if all words start with uppercase letters, otherwise False.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1934  
Write a Python function called `check_all_uppercase_words` that takes a string and returns True if all words start with uppercase letters, otherwise False.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_all_uppercase_words(text):  # Function definition: check_all_uppercase_words
    words = text.split()  # Initialize variable or assign value
    return all(word[0].isupper() for word in words if word)  # Return the result

result = check_all_uppercase_words("Hello World Python")  # Initialize variable or assign value
print(result)  # Expected: True




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_strings_with_length_range` that takes a list of strings and min/max length, and returns strings within that length range.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1935  
Write a Python function called `get_strings_with_length_range` that takes a list of strings and min/max length, and returns strings within that length range.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_strings_with_length_range(strings, min_length, max_length):  # Function definition: get_strings_with_length_range
    return [s for s in strings if min_length <= len(s) <= max_length]  # Return the result

result = get_strings_with_length_range(["a", "ab", "abc", "abcd", "abcde"], 3, 4)  # Initialize variable or assign value
print(result)  # Expected: ['abc', 'abcd']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_median` that takes a list of numbers and returns the median value (middle value when sorted).
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1936  
Write a Python function called `calculate_median` that takes a list of numbers and returns the median value (middle value when sorted).
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def calculate_median(numbers):  # Function definition: calculate_median
    sorted_nums = sorted(numbers)  # Sort the sequence
    n = len(sorted_nums)  # Initialize variable or assign value
    if n % 2 == 0:  # Conditional statement: check condition
        return (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2  # Return the result
    else:  # Else clause: execute when condition is false
        return sorted_nums[n//2]  # Return the result

result = calculate_median([1, 3, 5, 7, 9])  # Initialize variable or assign value
print(result)  # Expected: 5




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_mode` that takes a list and returns the element that appears most frequently (mode).
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1937  
Write a Python function called `get_mode` that takes a list and returns the element that appears most frequently (mode).
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_mode(my_list):  # Function definition: get_mode
    counts = {}  # Initialize empty list/dict/set
    for item in my_list:  # Loop: iterate over sequence
        counts[item] = counts.get(item, 0) + 1  # Initialize variable or assign value
    return max(counts, key=counts.get)  # Return the result

result = get_mode([1, 2, 2, 3, 3, 3, 4])  # Initialize variable or assign value
print(result)  # Expected: 3




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `format_multiline_string` that takes name, age, and email, and returns a formatted multiline string with each piece of information on a separate line.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1938  
Write a Python function called `format_multiline_string` that takes name, age, and email, and returns a formatted multiline string with each piece of information on a separate line.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def format_multiline_string(name, age, email):  # Function definition: format_multiline_string
    return f"Name: {name}\nAge: {age}\nEmail: {email}"  # Return the result

result = format_multiline_string("Alice", 30, "alice@example.com")  # Initialize variable or assign value
print(result)  # Expected: Name: Alice\nAge: 30\nEmail: alice@example.com




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_numbers_divisible_by_all` that takes a list of numbers and a list of divisors, and returns numbers divisible by all divisors.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1939  
Write a Python function called `get_numbers_divisible_by_all` that takes a list of numbers and a list of divisors, and returns numbers divisible by all divisors.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_numbers_divisible_by_all(numbers, divisors):  # Function definition: get_numbers_divisible_by_all
    return [n for n in numbers if all(n % d == 0 for d in divisors)]  # Return the result

result = get_numbers_divisible_by_all([12, 18, 24, 30], [2, 3])  # Initialize variable or assign value
print(result)  # Expected: [12, 18, 24, 30]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `count_vowels_per_word` that takes a string and returns a dictionary where keys are words and values are vowel counts.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1940  
Write a Python function called `count_vowels_per_word` that takes a string and returns a dictionary where keys are words and values are vowel counts.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def count_vowels_per_word(text):  # Function definition: count_vowels_per_word
    vowels = "aeiouAEIOU"  # Initialize string variable
    words = text.split()  # Initialize variable or assign value
    return {word: sum(1 for c in word if c in vowels) for word in words}  # Return the result

result = count_vowels_per_word("hello world python")  # Initialize variable or assign value
print(result)  # Expected: {'hello': 2, 'world': 1, 'python': 1}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_words_with_vowel_count` that takes a string and a number n, and returns words that have exactly n vowels.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1941  
Write a Python function called `get_words_with_vowel_count` that takes a string and a number n, and returns words that have exactly n vowels.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_words_with_vowel_count(text, n):  # Function definition: get_words_with_vowel_count
    vowels = "aeiouAEIOU"  # Initialize string variable
    words = text.split()  # Initialize variable or assign value
    return [word for word in words if sum(1 for c in word if c in vowels) == n]  # Return the result

result = get_words_with_vowel_count("hello world python programming", 2)  # Initialize variable or assign value
print(result)  # Expected: ['hello']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `format_table_row` that takes three values and returns a formatted string with values separated by pipes: 'value1 | value2 | value3'.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1942  
Write a Python function called `format_table_row` that takes three values and returns a formatted string with values separated by pipes: 'value1 | value2 | value3'.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def format_table_row(value1, value2, value3):  # Function definition: format_table_row
    return f"{value1} | {value2} | {value3}"  # Return the result

result = format_table_row("Alice", 30, "Engineer")  # Initialize variable or assign value
print(result)  # Expected: Alice | 30 | Engineer




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_elements_not_in_both` that takes two lists and returns a list of elements that are in one list but not the other.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1943  
Write a Python function called `get_elements_not_in_both` that takes two lists and returns a list of elements that are in one list but not the other.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_elements_not_in_both(list1, list2):  # Function definition: get_elements_not_in_both
    result = []  # Initialize empty list/dict/set
    for item in list1:  # Loop: iterate over sequence
        if item not in list2:  # Conditional statement: check condition
            result.append(item)  # Add element to list
    for item in list2:  # Loop: iterate over sequence
        if item not in list1:  # Conditional statement: check condition
            result.append(item)  # Add element to list
    return result  # Return the result

result = get_elements_not_in_both([1, 2, 3, 4], [3, 4, 5, 6])  # Initialize variable or assign value
print(sorted(result))  # Expected: [1, 2, 5, 6]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_weighted_average` that takes a list of values and a list of weights, and returns the weighted average.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1944  
Write a Python function called `calculate_weighted_average` that takes a list of values and a list of weights, and returns the weighted average.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def calculate_weighted_average(values, weights):  # Function definition: calculate_weighted_average
    weighted_sum = sum(v * w for v, w in zip(values, weights))  # Initialize variable or assign value
    total_weight = sum(weights)  # Initialize variable or assign value
    return weighted_sum / total_weight  # Return the result

result = calculate_weighted_average([10, 20, 30], [1, 2, 3])  # Initialize variable or assign value
print(result)  # Expected: 23.333333333333332




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_strings_sorted_by_length` that takes a list of strings and returns the list sorted by length (shortest to longest).
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1945  
Write a Python function called `get_strings_sorted_by_length` that takes a list of strings and returns the list sorted by length (shortest to longest).
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_strings_sorted_by_length(strings):  # Function definition: get_strings_sorted_by_length
    return sorted(strings, key=len)  # Return the result

result = get_strings_sorted_by_length(["python", "a", "hello", "world"])  # Initialize variable or assign value
print(result)  # Expected: ['a', 'hello', 'world', 'python']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `format_percentage_list` that takes a list of numbers and returns a list of strings, each formatted as a percentage with % sign.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1946  
Write a Python function called `format_percentage_list` that takes a list of numbers and returns a list of strings, each formatted as a percentage with % sign.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def format_percentage_list(numbers):  # Function definition: format_percentage_list
    return [f"{n}%" for n in numbers]  # Return the result

result = format_percentage_list([25, 50, 75])  # Initialize variable or assign value
print(result)  # Expected: ['25%', '50%', '75%']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_pairs_summing_to` that takes a list of numbers and a target sum, and returns a list of tuples containing pairs that sum to the target.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1947  
Write a Python function called `get_pairs_summing_to` that takes a list of numbers and a target sum, and returns a list of tuples containing pairs that sum to the target.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_pairs_summing_to(numbers, target):  # Function definition: get_pairs_summing_to
    pairs = []  # Initialize empty list/dict/set
    for i in range(len(numbers)):  # Loop: iterate over sequence
        for j in range(i + 1, len(numbers)):  # Loop: iterate over sequence
            if numbers[i] + numbers[j] == target:  # Conditional statement: check condition
                pairs.append((numbers[i], numbers[j]))  # Add element to list
    return pairs  # Return the result

result = get_pairs_summing_to([1, 2, 3, 4, 5], 7)  # Initialize variable or assign value
print(result)  # Expected: [(2, 5), (3, 4)]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `count_character_types` that takes a string and returns a dictionary with 'vowels', 'consonants', 'digits', and 'spaces' counts.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1948  
Write a Python function called `count_character_types` that takes a string and returns a dictionary with 'vowels', 'consonants', 'digits', and 'spaces' counts.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def count_character_types(text):  # Function definition: count_character_types
    vowels = "aeiouAEIOU"  # Initialize string variable
    return {  # Return the result
        'vowels': sum(1 for c in text if c in vowels),  # Generator expression or comprehension
        'consonants': sum(1 for c in text if c.isalpha() and c not in vowels),  # Generator expression or comprehension
        'digits': sum(1 for c in text if c.isdigit()),  # Generator expression or comprehension
        'spaces': sum(1 for c in text if c.isspace())  # Generator expression or comprehension
    }

result = count_character_types("Hello World 123")  # Initialize variable or assign value
print(result)  # Expected: {'vowels': 3, 'consonants': 7, 'digits': 3, 'spaces': 2}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_words_by_vowel_count` that takes a string and returns a dictionary where keys are vowel counts and values are lists of words with that count.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1949  
Write a Python function called `get_words_by_vowel_count` that takes a string and returns a dictionary where keys are vowel counts and values are lists of words with that count.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_words_by_vowel_count(text):  # Function definition: get_words_by_vowel_count
    vowels = "aeiouAEIOU"  # Initialize string variable
    words = text.split()  # Initialize variable or assign value
    result = {}  # Initialize empty list/dict/set
    for word in words:  # Loop: iterate over sequence
        count = sum(1 for c in word if c in vowels)  # Initialize variable or assign value
        if count not in result:  # Conditional statement: check condition
            result[count] = []  # Initialize empty list/dict/set
        result[count].append(word)  # Add element to list
    return result  # Return the result

result = get_words_by_vowel_count("hello world python")  # Initialize variable or assign value
print(result)  # Expected: {2: ['hello'], 1: ['world', 'python']}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `format_name_with_title` that takes first name, last name, and title, and returns a formatted string: 'Title. First Last'.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1950  
Write a Python function called `format_name_with_title` that takes first name, last name, and title, and returns a formatted string: 'Title. First Last'.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def format_name_with_title(first, last, title):  # Function definition: format_name_with_title
    return f"{title}. {first} {last}"  # Return the result

result = format_name_with_title("John", "Doe", "Dr")  # Initialize variable or assign value
print(result)  # Expected: Dr. John Doe




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_area_circle_sector` that takes radius and angle in degrees, and returns the area of the sector.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1951  
Write a Python function called `calculate_area_circle_sector` that takes radius and angle in degrees, and returns the area of the sector.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

import math  # Import statement: load module or specific functions

def calculate_area_circle_sector(radius, angle_degrees):  # Function definition: calculate_area_circle_sector
    return (angle_degrees / 360) * math.pi * radius ** 2  # Return the result

result = calculate_area_circle_sector(5, 90)  # Initialize variable or assign value
print(round(result, 2))  # Expected: 19.63




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_elements_at_multiple_indices` that takes a list and a list of indices, and returns a dictionary where keys are indices and values are elements.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1952  
Write a Python function called `get_elements_at_multiple_indices` that takes a list and a list of indices, and returns a dictionary where keys are indices and values are elements.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_elements_at_multiple_indices(my_list, indices):  # Function definition: get_elements_at_multiple_indices
    return {i: my_list[i] for i in indices if i < len(my_list)}  # Return the result

result = get_elements_at_multiple_indices([10, 20, 30, 40], [0, 2, 3])  # Initialize variable or assign value
print(result)  # Expected: {0: 10, 2: 30, 3: 40}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_string_properties` that takes a string and returns a dictionary with boolean values for 'has_uppercase', 'has_lowercase', 'has_digit', 'has_special'.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1953  
Write a Python function called `check_string_properties` that takes a string and returns a dictionary with boolean values for 'has_uppercase', 'has_lowercase', 'has_digit', 'has_special'.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_string_properties(text):  # Function definition: check_string_properties
    return {  # Return the result
        'has_uppercase': any(c.isupper() for c in text),  # Generator expression or comprehension
        'has_lowercase': any(c.islower() for c in text),  # Generator expression or comprehension
        'has_digit': any(c.isdigit() for c in text),  # Generator expression or comprehension
        'has_special': any(not c.isalnum() and not c.isspace() for c in text)  # Generator expression or comprehension
    }

result = check_string_properties("Hello123!")  # Initialize variable or assign value
print(result)  # Expected: {'has_uppercase': True, 'has_lowercase': True, 'has_digit': True, 'has_special': True}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_numbers_summing_to_range` that takes a list of numbers and a range (min_sum, max_sum), and returns pairs of numbers whose sum is in that range.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1954  
Write a Python function called `get_numbers_summing_to_range` that takes a list of numbers and a range (min_sum, max_sum), and returns pairs of numbers whose sum is in that range.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_numbers_summing_to_range(numbers, min_sum, max_sum):  # Function definition: get_numbers_summing_to_range
    pairs = []  # Initialize empty list/dict/set
    for i in range(len(numbers)):  # Loop: iterate over sequence
        for j in range(i + 1, len(numbers)):  # Loop: iterate over sequence
            total = numbers[i] + numbers[j]  # Initialize variable or assign value
            if min_sum <= total <= max_sum:  # Conditional statement: check condition
                pairs.append((numbers[i], numbers[j]))  # Add element to list
    return pairs  # Return the result

result = get_numbers_summing_to_range([1, 2, 3, 4, 5], 5, 7)  # Initialize variable or assign value
print(result)  # Expected: [(1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4)]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `format_phone_with_country` that takes country code, area code, and number, and returns a formatted phone number: '+{country} ({area}) {number}'.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1955  
Write a Python function called `format_phone_with_country` that takes country code, area code, and number, and returns a formatted phone number: '+{country} ({area}) {number}'.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def format_phone_with_country(country_code, area_code, number):  # Function definition: format_phone_with_country
    return f"+{country_code} ({area_code}) {number}"  # Return the result

result = format_phone_with_country("1", "555", "1234567")  # Initialize variable or assign value
print(result)  # Expected: +1 (555) 1234567




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_consecutive_elements` that takes a list and a number n, and returns a list of lists where each inner list contains n consecutive elements.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1956  
Write a Python function called `get_consecutive_elements` that takes a list and a number n, and returns a list of lists where each inner list contains n consecutive elements.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_consecutive_elements(my_list, n):  # Function definition: get_consecutive_elements
    return [my_list[i:i+n] for i in range(len(my_list) - n + 1)]  # Return the result

result = get_consecutive_elements([1, 2, 3, 4, 5], 3)  # Initialize variable or assign value
print(result)  # Expected: [[1, 2, 3], [2, 3, 4], [3, 4, 5]]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_gcd` that takes two numbers and returns their greatest common divisor using Euclidean algorithm.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1957  
Write a Python function called `calculate_gcd` that takes two numbers and returns their greatest common divisor using Euclidean algorithm.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def calculate_gcd(a, b):  # Function definition: calculate_gcd
    while b:  # Loop: iterate while condition is true
        a, b = b, a % b  # Initialize variable or assign value
    return a  # Return the result

result = calculate_gcd(48, 18)  # Initialize variable or assign value
print(result)  # Expected: 6




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_lcm` that takes two numbers and returns their least common multiple.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1958  
Write a Python function called `calculate_lcm` that takes two numbers and returns their least common multiple.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def calculate_lcm(a, b):  # Function definition: calculate_lcm
    def gcd(x, y):  # Function definition: gcd
        while y:  # Loop: iterate while condition is true
            x, y = y, x % y  # Initialize variable or assign value
        return x  # Return the result
    return abs(a * b) // gcd(a, b)  # Return the result

result = calculate_lcm(12, 18)  # Initialize variable or assign value
print(result)  # Expected: 36




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_frequency_dict` that takes a list and returns a dictionary sorted by frequency (most frequent first).
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1959  
Write a Python function called `get_frequency_dict` that takes a list and returns a dictionary sorted by frequency (most frequent first).
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_frequency_dict(my_list):  # Function definition: get_frequency_dict
    counts = {}  # Initialize empty list/dict/set
    for item in my_list:  # Loop: iterate over sequence
        counts[item] = counts.get(item, 0) + 1  # Initialize variable or assign value
    return dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))  # Return the result

result = get_frequency_dict([1, 2, 2, 3, 3, 3, 4])  # Initialize variable or assign value
print(result)  # Expected: {3: 3, 2: 2, 1: 1, 4: 1}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `format_number_with_commas` that takes a number and returns it as a string with comma separators (e.g., 1000 becomes '1,000').
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1960  
Write a Python function called `format_number_with_commas` that takes a number and returns it as a string with comma separators (e.g., 1000 becomes '1,000').
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def format_number_with_commas(number):  # Function definition: format_number_with_commas
    return f"{number:,}"  # Return the result

result = format_number_with_commas(1234567)  # Initialize variable or assign value
print(result)  # Expected: 1,234,567




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_words_with_same_length` that takes a list of strings and returns a dictionary where keys are lengths and values are lists of strings with that length.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1961  
Write a Python function called `get_words_with_same_length` that takes a list of strings and returns a dictionary where keys are lengths and values are lists of strings with that length.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_words_with_same_length(strings):  # Function definition: get_words_with_same_length
    result = {}  # Initialize empty list/dict/set
    for s in strings:  # Loop: iterate over sequence
        length = len(s)  # Initialize variable or assign value
        if length not in result:  # Conditional statement: check condition
            result[length] = []  # Initialize empty list/dict/set
        result[length].append(s)  # Add element to list
    return result  # Return the result

result = get_words_with_same_length(["a", "ab", "abc", "ab", "abcd"])  # Initialize variable or assign value
print(result)  # Expected: {1: ['a'], 2: ['ab', 'ab'], 3: ['abc'], 4: ['abcd']}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `check_anagram_pair` that takes two strings and returns True if they are anagrams (contain same characters), otherwise False.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1962  
Write a Python function called `check_anagram_pair` that takes two strings and returns True if they are anagrams (contain same characters), otherwise False.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def check_anagram_pair(str1, str2):  # Function definition: check_anagram_pair
    return sorted(str1.lower().replace(" ", "")) == sorted(str2.lower().replace(" ", ""))  # Return the result

print(check_anagram_pair("listen", "silent"), check_anagram_pair("hello", "world"))  # Expected: True False




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_sublist_sum` that takes a list and start/end indices, and returns the sum of elements in that sublist.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1963  
Write a Python function called `get_sublist_sum` that takes a list and start/end indices, and returns the sum of elements in that sublist.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_sublist_sum(my_list, start, end):  # Function definition: get_sublist_sum
    return sum(my_list[start:end])  # Return the result

result = get_sublist_sum([10, 20, 30, 40, 50], 1, 4)  # Initialize variable or assign value
print(result)  # Expected: 90




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `format_time_12hour` that takes hours (24-hour format) and returns time in 12-hour format with AM/PM.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1964  
Write a Python function called `format_time_12hour` that takes hours (24-hour format) and returns time in 12-hour format with AM/PM.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def format_time_12hour(hours_24):  # Function definition: format_time_12hour
    if hours_24 == 0:  # Conditional statement: check condition
        return "12 AM"  # Return the result
    elif hours_24 < 12:  # Conditional statement: check condition
        return f"{hours_24} AM"  # Return the result
    elif hours_24 == 12:  # Conditional statement: check condition
        return "12 PM"  # Return the result
    else:  # Else clause: execute when condition is false
        return f"{hours_24 - 12} PM"  # Return the result

print(format_time_12hour(0), format_time_12hour(14), format_time_12hour(23))  # Expected: 12 AM 2 PM 11 PM




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_elements_between_values` that takes a list and two values, and returns elements that are greater than the first value and less than the second.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1965  
Write a Python function called `get_elements_between_values` that takes a list and two values, and returns elements that are greater than the first value and less than the second.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_elements_between_values(my_list, min_val, max_val):  # Function definition: get_elements_between_values
    return [x for x in my_list if min_val < x < max_val]  # Return the result

result = get_elements_between_values([10, 20, 30, 40, 50], 15, 45)  # Initialize variable or assign value
print(result)  # Expected: [20, 30, 40]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `count_substring_occurrences` that takes a string and a substring, and returns how many times the substring appears (overlapping allowed).
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1966  
Write a Python function called `count_substring_occurrences` that takes a string and a substring, and returns how many times the substring appears (overlapping allowed).
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def count_substring_occurrences(text, substring):  # Function definition: count_substring_occurrences
    count = 0  # Initialize variable or assign value
    for i in range(len(text) - len(substring) + 1):  # Loop: iterate over sequence
        if text[i:i+len(substring)] == substring:  # Conditional statement: check condition
            count += 1
    return count  # Return the result

result = count_substring_occurrences("ababab", "aba")  # Initialize variable or assign value
print(result)  # Expected: 2




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `format_list_as_string` that takes a list and a separator, and returns a string with elements joined by separator and enclosed in brackets.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1967  
Write a Python function called `format_list_as_string` that takes a list and a separator, and returns a string with elements joined by separator and enclosed in brackets.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def format_list_as_string(my_list, separator):  # Function definition: format_list_as_string
    return f"[{separator.join(str(x) for x in my_list)}]"  # Return the result

result = format_list_as_string([1, 2, 3], ", ")  # Initialize variable or assign value
print(result)  # Expected: [1, 2, 3]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_unique_combinations` that takes two lists and returns a list of tuples containing all unique combinations of elements.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1968  
Write a Python function called `get_unique_combinations` that takes two lists and returns a list of tuples containing all unique combinations of elements.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_unique_combinations(list1, list2):  # Function definition: get_unique_combinations
    return [(a, b) for a in list1 for b in list2]  # Return the result

result = get_unique_combinations([1, 2], ['a', 'b'])  # Initialize variable or assign value
print(result)  # Expected: [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_quadratic_roots` that takes coefficients a, b, c and returns the roots of ax^2 + bx + c = 0 as a tuple (or None if no real roots).
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1969  
Write a Python function called `calculate_quadratic_roots` that takes coefficients a, b, c and returns the roots of ax^2 + bx + c = 0 as a tuple (or None if no real roots).
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

import math  # Import statement: load module or specific functions

def calculate_quadratic_roots(a, b, c):  # Function definition: calculate_quadratic_roots
    discriminant = b**2 - 4*a*c  # Initialize variable or assign value
    if discriminant < 0:  # Conditional statement: check condition
        return None  # Return the result
    root1 = (-b + math.sqrt(discriminant)) / (2*a)  # Initialize variable or assign value
    root2 = (-b - math.sqrt(discriminant)) / (2*a)  # Initialize variable or assign value
    return (root1, root2)  # Return the result

result = calculate_quadratic_roots(1, -5, 6)  # Initialize variable or assign value
print(result)  # Expected: (3.0, 2.0)




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_strings_matching_pattern` that takes a list of strings and a pattern (substring), and returns strings that contain the pattern at least twice.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1970  
Write a Python function called `get_strings_matching_pattern` that takes a list of strings and a pattern (substring), and returns strings that contain the pattern at least twice.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_strings_matching_pattern(strings, pattern):  # Function definition: get_strings_matching_pattern
    result = []  # Initialize empty list/dict/set
    for s in strings:  # Loop: iterate over sequence
        if s.count(pattern) >= 2:  # Conditional statement: check condition
            result.append(s)  # Add element to list
    return result  # Return the result

result = get_strings_matching_pattern(["hello", "lollipop", "world"], "l")  # Initialize variable or assign value
print(result)  # Expected: ['hello', 'lollipop']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `format_name_initials` that takes first name, middle name, and last name, and returns initials with periods: 'F.M.L.'.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1971  
Write a Python function called `format_name_initials` that takes first name, middle name, and last name, and returns initials with periods: 'F.M.L.'.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def format_name_initials(first, middle, last):  # Function definition: format_name_initials
    return f"{first[0]}.{middle[0]}.{last[0]}."  # Return the result

result = format_name_initials("John", "Michael", "Doe")  # Initialize variable or assign value
print(result)  # Expected: J.M.D.




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_elements_with_condition` that takes a list and a function (lambda), and returns elements that satisfy the condition.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1972  
Write a Python function called `get_elements_with_condition` that takes a list and a function (lambda), and returns elements that satisfy the condition.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_elements_with_condition(my_list, condition_func):  # Function definition: get_elements_with_condition
    return [x for x in my_list if condition_func(x)]  # Return the result

result = get_elements_with_condition([1, 2, 3, 4, 5, 6], lambda x: x > 3)  # Initialize variable or assign value
print(result)  # Expected: [4, 5, 6]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_total_area` that takes a list of shapes represented as tuples (shape_type, dimensions), and returns the total area. Shape types: 'rectangle' (length, width), 'circle' (radius).
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1973  
Write a Python function called `calculate_total_area` that takes a list of shapes represented as tuples (shape_type, dimensions), and returns the total area. Shape types: 'rectangle' (length, width), 'circle' (radius).
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

import math  # Import statement: load module or specific functions

def calculate_total_area(shapes):  # Function definition: calculate_total_area
    total = 0  # Initialize variable or assign value
    for shape_type, dimensions in shapes:  # Loop: iterate over sequence
        if shape_type == 'rectangle':  # Conditional statement: check condition
            total += dimensions[0] * dimensions[1]
        elif shape_type == 'circle':  # Conditional statement: check condition
            total += math.pi * dimensions[0] ** 2
    return total  # Return the result

result = calculate_total_area([('rectangle', (5, 3)), ('circle', (2,))])  # Initialize variable or assign value
print(round(result, 2))  # Expected: 27.57




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_words_with_repeated_chars` that takes a string and returns a list of words that contain at least one repeated character.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1974  
Write a Python function called `get_words_with_repeated_chars` that takes a string and returns a list of words that contain at least one repeated character.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_words_with_repeated_chars(text):  # Function definition: get_words_with_repeated_chars
    words = text.split()  # Initialize variable or assign value
    result = []  # Initialize empty list/dict/set
    for word in words:  # Loop: iterate over sequence
        if len(word) != len(set(word)):  # Conditional statement: check condition
            result.append(word)  # Add element to list
    return result  # Return the result

result = get_words_with_repeated_chars("hello world python programming")  # Initialize variable or assign value
print(result)  # Expected: ['hello', 'world', 'programming']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `format_multi_value_string` that takes a name and a list of scores, and returns a formatted string: 'Name: {name}, Scores: {scores}'.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1975  
Write a Python function called `format_multi_value_string` that takes a name and a list of scores, and returns a formatted string: 'Name: {name}, Scores: {scores}'.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def format_multi_value_string(name, scores):  # Function definition: format_multi_value_string
    scores_str = ", ".join(str(s) for s in scores)  # Initialize string variable
    return f"Name: {name}, Scores: {scores_str}"  # Return the result

result = format_multi_value_string("Alice", [85, 90, 88])  # Initialize variable or assign value
print(result)  # Expected: Name: Alice, Scores: 85, 90, 88




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_symmetric_difference` that takes two lists and returns a list of elements that are in one list but not the other (symmetric difference).
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1976  
Write a Python function called `get_symmetric_difference` that takes two lists and returns a list of elements that are in one list but not the other (symmetric difference).
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_symmetric_difference(list1, list2):  # Function definition: get_symmetric_difference
    set1 = set(list1)  # Initialize variable or assign value
    set2 = set(list2)  # Initialize variable or assign value
    return list(set1.symmetric_difference(set2))  # Return the result

result = get_symmetric_difference([1, 2, 3, 4], [3, 4, 5, 6])  # Initialize variable or assign value
print(sorted(result))  # Expected: [1, 2, 5, 6]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `count_words_by_first_letter` that takes a string and returns a dictionary where keys are first letters and values are word counts.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1977  
Write a Python function called `count_words_by_first_letter` that takes a string and returns a dictionary where keys are first letters and values are word counts.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def count_words_by_first_letter(text):  # Function definition: count_words_by_first_letter
    words = text.split()  # Initialize variable or assign value
    counts = {}  # Initialize empty list/dict/set
    for word in words:  # Loop: iterate over sequence
        first_letter = word[0].lower()  # Initialize variable or assign value
        counts[first_letter] = counts.get(first_letter, 0) + 1  # Initialize variable or assign value
    return counts  # Return the result

result = count_words_by_first_letter("apple apricot banana cherry")  # Initialize variable or assign value
print(result)  # Expected: {'a': 2, 'b': 1, 'c': 1}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `format_decimal_places` that takes a number and decimal places, and returns the number formatted to that many decimal places.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1978  
Write a Python function called `format_decimal_places` that takes a number and decimal places, and returns the number formatted to that many decimal places.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def format_decimal_places(number, decimal_places):  # Function definition: format_decimal_places
    return f"{number:.{decimal_places}f}"  # Return the result

result = format_decimal_places(3.14159, 2)  # Initialize variable or assign value
print(result)  # Expected: 3.14




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_elements_satisfying_all` that takes a list and multiple conditions (functions), and returns elements that satisfy all conditions.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1979  
Write a Python function called `get_elements_satisfying_all` that takes a list and multiple conditions (functions), and returns elements that satisfy all conditions.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_elements_satisfying_all(my_list, *conditions):  # Function definition: get_elements_satisfying_all
    result = []  # Initialize empty list/dict/set
    for item in my_list:  # Loop: iterate over sequence
        if all(cond(item) for cond in conditions):  # Conditional statement: check condition
            result.append(item)  # Add element to list
    return result  # Return the result

result = get_elements_satisfying_all([1, 2, 3, 4, 5, 6], lambda x: x > 2, lambda x: x < 6)  # Initialize variable or assign value
print(result)  # Expected: [3, 4, 5]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_net_price` that takes original price, discount percentage, and tax rate, and returns the final price after discount and tax.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1980  
Write a Python function called `calculate_net_price` that takes original price, discount percentage, and tax rate, and returns the final price after discount and tax.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def calculate_net_price(original_price, discount_percent, tax_rate):  # Function definition: calculate_net_price
    discounted = original_price * (1 - discount_percent / 100)  # Initialize variable or assign value
    final = discounted * (1 + tax_rate / 100)  # Initialize variable or assign value
    return final  # Return the result

result = calculate_net_price(100, 20, 10)  # Initialize variable or assign value
print(result)  # Expected: 88.0




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_strings_with_all_vowels` that takes a list of strings and returns strings that contain all five vowels (a, e, i, o, u).
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1981  
Write a Python function called `get_strings_with_all_vowels` that takes a list of strings and returns strings that contain all five vowels (a, e, i, o, u).
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_strings_with_all_vowels(strings):  # Function definition: get_strings_with_all_vowels
    vowels = set("aeiou")  # Initialize variable or assign value
    result = []  # Initialize empty list/dict/set
    for s in strings:  # Loop: iterate over sequence
        if vowels.issubset(set(s.lower())):  # Conditional statement: check condition
            result.append(s)  # Add element to list
    return result  # Return the result

result = get_strings_with_all_vowels(["education", "hello", "facetious"])  # Initialize variable or assign value
print(result)  # Expected: ['education', 'facetious']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `format_currency_multiple` that takes a list of numbers and returns a list of strings, each formatted as currency.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1982  
Write a Python function called `format_currency_multiple` that takes a list of numbers and returns a list of strings, each formatted as currency.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def format_currency_multiple(numbers):  # Function definition: format_currency_multiple
    return [f"${n:.2f}" for n in numbers]  # Return the result

result = format_currency_multiple([10.5, 20.75, 30.25])  # Initialize variable or assign value
print(result)  # Expected: ['$10.50', '$20.75', '$30.25']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_consecutive_pairs` that takes a list and returns a list of tuples containing consecutive pairs of elements.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1983  
Write a Python function called `get_consecutive_pairs` that takes a list and returns a list of tuples containing consecutive pairs of elements.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_consecutive_pairs(my_list):  # Function definition: get_consecutive_pairs
    return [(my_list[i], my_list[i+1]) for i in range(len(my_list) - 1)]  # Return the result

result = get_consecutive_pairs([1, 2, 3, 4, 5])  # Initialize variable or assign value
print(result)  # Expected: [(1, 2), (2, 3), (3, 4), (4, 5)]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_geometric_mean` that takes a list of positive numbers and returns the geometric mean.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1984  
Write a Python function called `calculate_geometric_mean` that takes a list of positive numbers and returns the geometric mean.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

import math  # Import statement: load module or specific functions

def calculate_geometric_mean(numbers):  # Function definition: calculate_geometric_mean
    product = 1  # Initialize variable or assign value
    for n in numbers:  # Loop: iterate over sequence
        product *= n
    return product ** (1 / len(numbers))  # Return the result

result = calculate_geometric_mean([2, 8, 32])  # Initialize variable or assign value
print(round(result, 2))  # Expected: 8.0




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_words_sorted_by_vowels` that takes a string and returns a list of words sorted by the number of vowels they contain.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1985  
Write a Python function called `get_words_sorted_by_vowels` that takes a string and returns a list of words sorted by the number of vowels they contain.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_words_sorted_by_vowels(text):  # Function definition: get_words_sorted_by_vowels
    vowels = "aeiouAEIOU"  # Initialize string variable
    words = text.split()  # Initialize variable or assign value
    return sorted(words, key=lambda w: sum(1 for c in w if c in vowels))  # Return the result

result = get_words_sorted_by_vowels("hello world python programming")  # Initialize variable or assign value
print(result)  # Expected: ['world', 'python', 'hello', 'programming']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `format_name_age_grade` that takes name, age, and grade, and returns a formatted string: '{name} (Age: {age}) - Grade: {grade}'.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1986  
Write a Python function called `format_name_age_grade` that takes name, age, and grade, and returns a formatted string: '{name} (Age: {age}) - Grade: {grade}'.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def format_name_age_grade(name, age, grade):  # Function definition: format_name_age_grade
    return f"{name} (Age: {age}) - Grade: {grade}"  # Return the result

result = format_name_age_grade("Alice", 20, "A")  # Initialize variable or assign value
print(result)  # Expected: Alice (Age: 20) - Grade: A




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_elements_with_max_frequency` that takes a list and returns a list of all elements that appear with the maximum frequency.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1987  
Write a Python function called `get_elements_with_max_frequency` that takes a list and returns a list of all elements that appear with the maximum frequency.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_elements_with_max_frequency(my_list):  # Function definition: get_elements_with_max_frequency
    counts = {}  # Initialize empty list/dict/set
    for item in my_list:  # Loop: iterate over sequence
        counts[item] = counts.get(item, 0) + 1  # Initialize variable or assign value
    max_count = max(counts.values())  # Use min/max with default parameter to handle empty sequences
    return [item for item, count in counts.items() if count == max_count]  # Return the result

result = get_elements_with_max_frequency([1, 2, 2, 3, 3, 3, 4, 4, 4])  # Initialize variable or assign value
print(sorted(result))  # Expected: [3, 4]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_harmonic_mean` that takes a list of positive numbers and returns the harmonic mean.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1988  
Write a Python function called `calculate_harmonic_mean` that takes a list of positive numbers and returns the harmonic mean.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def calculate_harmonic_mean(numbers):  # Function definition: calculate_harmonic_mean
    reciprocal_sum = sum(1 / n for n in numbers)  # Initialize variable or assign value
    return len(numbers) / reciprocal_sum  # Return the result

result = calculate_harmonic_mean([2, 4, 8])  # Initialize variable or assign value
print(round(result, 2))  # Expected: 3.43




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `format_list_items` that takes a list and returns a formatted string: 'Item 1: {item1}, Item 2: {item2}, ...'.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1989  
Write a Python function called `format_list_items` that takes a list and returns a formatted string: 'Item 1: {item1}, Item 2: {item2}, ...'.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def format_list_items(my_list):  # Function definition: format_list_items
    return ", ".join(f"Item {i+1}: {item}" for i, item in enumerate(my_list))  # Return the result

result = format_list_items(["apple", "banana", "cherry"])  # Initialize variable or assign value
print(result)  # Expected: Item 1: apple, Item 2: banana, Item 3: cherry




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_strings_with_pattern_count` that takes a list of strings and a pattern, and returns strings where the pattern appears exactly n times.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1990  
Write a Python function called `get_strings_with_pattern_count` that takes a list of strings and a pattern, and returns strings where the pattern appears exactly n times.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_strings_with_pattern_count(strings, pattern, n):  # Function definition: get_strings_with_pattern_count
    result = []  # Initialize empty list/dict/set
    for s in strings:  # Loop: iterate over sequence
        if s.count(pattern) == n:  # Conditional statement: check condition
            result.append(s)  # Add element to list
    return result  # Return the result

result = get_strings_with_pattern_count(["hello", "lollipop", "world"], "l", 2)  # Initialize variable or assign value
print(result)  # Expected: ['hello']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_compound_growth` that takes initial value, growth rate, and number of periods, and returns the final value.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1991  
Write a Python function called `calculate_compound_growth` that takes initial value, growth rate, and number of periods, and returns the final value.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def calculate_compound_growth(initial, rate, periods):  # Function definition: calculate_compound_growth
    return initial * (1 + rate / 100) ** periods  # Return the result

result = calculate_compound_growth(1000, 5, 3)  # Initialize variable or assign value
print(round(result, 2))  # Expected: 1157.63




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_elements_by_frequency_range` that takes a list and min/max frequency, and returns elements that appear within that frequency range.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1992  
Write a Python function called `get_elements_by_frequency_range` that takes a list and min/max frequency, and returns elements that appear within that frequency range.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_elements_by_frequency_range(my_list, min_freq, max_freq):  # Function definition: get_elements_by_frequency_range
    counts = {}  # Initialize empty list/dict/set
    for item in my_list:  # Loop: iterate over sequence
        counts[item] = counts.get(item, 0) + 1  # Initialize variable or assign value
    return [item for item, count in counts.items() if min_freq <= count <= max_freq]  # Return the result

result = get_elements_by_frequency_range([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 2, 3)  # Initialize variable or assign value
print(sorted(result))  # Expected: [2, 3]




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `format_table_data` that takes a list of tuples (name, value) and returns a formatted table string with aligned columns.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1993  
Write a Python function called `format_table_data` that takes a list of tuples (name, value) and returns a formatted table string with aligned columns.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def format_table_data(data):  # Function definition: format_table_data
    lines = []  # Initialize empty list/dict/set
    for name, value in data:  # Loop: iterate over sequence
        lines.append(f"{name:10s} | {value}")  # Add element to list
    return "\n".join(lines)  # Return the result

result = format_table_data([("Alice", 85), ("Bob", 90), ("Charlie", 75)])  # Initialize variable or assign value
print(result)  # Expected: Alice      | 85\nBob        | 90\nCharlie    | 75




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_words_with_unique_chars` that takes a string and returns words where all characters are unique (no repeated characters).
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1994  
Write a Python function called `get_words_with_unique_chars` that takes a string and returns words where all characters are unique (no repeated characters).
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_words_with_unique_chars(text):  # Function definition: get_words_with_unique_chars
    words = text.split()  # Initialize variable or assign value
    return [word for word in words if len(word) == len(set(word))]  # Return the result

result = get_words_with_unique_chars("hello world python")  # Initialize variable or assign value
print(result)  # Expected: ['world', 'python']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_total_with_multiple_discounts` that takes a price and a list of discount percentages, and returns the final price after applying all discounts sequentially.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1995  
Write a Python function called `calculate_total_with_multiple_discounts` that takes a price and a list of discount percentages, and returns the final price after applying all discounts sequentially.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def calculate_total_with_multiple_discounts(price, discounts):  # Function definition: calculate_total_with_multiple_discounts
    result = price  # Initialize variable or assign value
    for discount in discounts:  # Loop: iterate over sequence
        result = result * (1 - discount / 100)  # Initialize variable or assign value
    return result  # Return the result

result = calculate_total_with_multiple_discounts(100, [10, 20])  # Initialize variable or assign value
print(round(result, 2))  # Expected: 72.0




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `format_multi_line_address` that takes name, street, city, state, zipcode, and returns a formatted multi-line address block.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1996  
Write a Python function called `format_multi_line_address` that takes name, street, city, state, zipcode, and returns a formatted multi-line address block.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def format_multi_line_address(name, street, city, state, zipcode):  # Function definition: format_multi_line_address
    return f"{name}\n{street}\n{city}, {state} {zipcode}"  # Return the result

result = format_multi_line_address("John Doe", "123 Main St", "New York", "NY", "10001")  # Initialize variable or assign value
print(result)  # Expected: John Doe\n123 Main St\nNew York, NY 10001




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_elements_matching_multiple_patterns` that takes a list of strings and multiple patterns, and returns strings that match all patterns.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1997  
Write a Python function called `get_elements_matching_multiple_patterns` that takes a list of strings and multiple patterns, and returns strings that match all patterns.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def get_elements_matching_multiple_patterns(strings, *patterns):  # Function definition: get_elements_matching_multiple_patterns
    result = []  # Initialize empty list/dict/set
    for s in strings:  # Loop: iterate over sequence
        if all(pattern in s for pattern in patterns):  # Conditional statement: check condition
            result.append(s)  # Add element to list
    return result  # Return the result

result = get_elements_matching_multiple_patterns(["hello", "world", "python", "programming"], "o", "r")  # Initialize variable or assign value
print(result)  # Expected: ['world', 'programming']




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `calculate_statistical_summary` that takes a list of numbers and returns a dictionary with 'mean', 'median', 'min', 'max', and 'range'.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1998  
Write a Python function called `calculate_statistical_summary` that takes a list of numbers and returns a dictionary with 'mean', 'median', 'min', 'max', and 'range'.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def calculate_statistical_summary(numbers):  # Function definition: calculate_statistical_summary
    sorted_nums = sorted(numbers)  # Sort the sequence
    n = len(numbers)  # Initialize variable or assign value
    mean = sum(numbers) / n  # Initialize variable or assign value
    median = sorted_nums[n//2] if n % 2 else (sorted_nums[n//2-1] + sorted_nums[n//2]) / 2  # Initialize variable or assign value
    min_val = min(numbers)  # Use min/max with default parameter to handle empty sequences
    max_val = max(numbers)  # Use min/max with default parameter to handle empty sequences
    return {  # Return the result
        'mean': mean,
        'median': median,
        'min': min_val,
        'max': max_val,
        'range': max_val - min_val
    }

result = calculate_statistical_summary([10, 20, 30, 40, 50])  # Initialize variable or assign value
print(result)  # Expected: {'mean': 30.0, 'median': 30, 'min': 10, 'max': 50, 'range': 40}




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `format_contact_info` that takes name, phone, email, and address, and returns a formatted contact card as a multi-line string.
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 1999  
Write a Python function called `format_contact_info` that takes name, phone, email, and address, and returns a formatted contact card as a multi-line string.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

def format_contact_info(name, phone, email, address):  # Function definition: format_contact_info
    return f"Name: {name}\nPhone: {phone}\nEmail: {email}\nAddress: {address}"  # Return the result

result = format_contact_info("Alice", "555-1234", "alice@example.com", "123 Main St")  # Initialize variable or assign value
print(result)  # Expected: Name: Alice\nPhone: 555-1234\nEmail: alice@example.com\nAddress: 123 Main St




# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function called `get_comprehensive_statistics` that takes a list of numbers and returns a dictionary with sum, average, min, max, count, and standard deviation (using basic formula).
# 
# This problem demonstrates how to write Python functions to solve specific tasks.
# Functions allow you to encapsulate logic, make code reusable, and improve
# readability. Understanding function parameters, return values, and scope is
# essential for writing effective Python programs.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

""" 
Problem: 2000  
Write a Python function called `get_comprehensive_statistics` that takes a list of numbers and returns a dictionary with sum, average, min, max, count, and standard deviation (using basic formula).
"""

# SOLUTION EXPLANATION:
# This solution defines a function that encapsulates the required logic.
# Functions improve code organization, reusability, and maintainability.

import math  # Import statement: load module or specific functions

def get_comprehensive_statistics(numbers):  # Function definition: get_comprehensive_statistics
    n = len(numbers)  # Initialize variable or assign value
    mean = sum(numbers) / n  # Initialize variable or assign value
    variance = sum((x - mean) ** 2 for x in numbers) / n  # Initialize variable or assign value
    std_dev = math.sqrt(variance)  # Initialize variable or assign value
    return {  # Return the result
        'sum': sum(numbers),
        'average': mean,
        'min': min(numbers),
        'max': max(numbers),
        'count': n,
        'standard_deviation': std_dev
    }

result = get_comprehensive_statistics([10, 20, 30, 40, 50])  # Initialize variable or assign value
print(result)  # Expected: {'sum': 150, 'average': 30.0, 'min': 10, 'max': 50, 'count': 5, 'standard_deviation': ~14.14}



# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.
