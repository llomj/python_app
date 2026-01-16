

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to reverse a list using slicing.
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
Problem: 1001
Write a Python program to reverse a list using slicing.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax to extract the desired portion
# of the sequence. Slicing is efficient and readable, making it the preferred
# method for extracting subsequences from strings, lists, and tuples.

numbers = [1, 2, 3, 4, 5]  # Initialize list
reversed_list = numbers[::-1]  # Slice: reverse the sequence
print(reversed_list)  # Expected output: [5, 4, 3, 2, 1]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to extract every third element from a list.
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
Problem: 1002
Write a Python program to extract every third element from a list.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax to extract the desired portion
# of the sequence. Slicing is efficient and readable, making it the preferred
# method for extracting subsequences from strings, lists, and tuples.

numbers = [10, 20, 30, 40, 50, 60, 70, 80]  # Initialize list
sliced_list = numbers[::3]  # Slice: extract elements with step 3
print(sliced_list)  # Expected output: [10, 40, 70]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to extract every second character from a string in reverse order.
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
Problem: 1003
Write a Python program to extract every second character from a string in reverse order.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax to extract the desired portion
# of the sequence. Slicing is efficient and readable, making it the preferred
# method for extracting subsequences from strings, lists, and tuples.

text = "abcdefghij"  # Initialize string variable
sliced_text = text[::-2]  # Slice: reverse sequence with step 2
print(sliced_text)  # Expected output: jhfdb

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to slice the middle three characters from a string with an odd length.
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
Problem: 1004
Write a Python program to slice the middle three characters from a string with an odd length.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax to extract the desired portion
# of the sequence. Slicing is efficient and readable, making it the preferred
# method for extracting subsequences from strings, lists, and tuples.

text = "abcdefg"  # Initialize string variable
middle_index = len(text) // 2  # Calculate index position (middle or specific index)
sliced_text = text[middle_index - 1: middle_index + 2]  # Slice: extract a portion of the sequence
print(sliced_text)  # Expected output: cde

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to remove the first and last characters from a string using slicing.
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
Problem: 1005
Write a Python program to remove the first and last characters from a string using slicing.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax to extract the desired portion
# of the sequence. Slicing is efficient and readable, making it the preferred
# method for extracting subsequences from strings, lists, and tuples.

text = "Python"  # Initialize string variable
sliced_text = text[1:-1]  # Slice: extract a portion of the sequence
print(sliced_text)  # Expected output: ytho

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to get the first half of a string using slicing.
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
Problem: 1006
Write a Python program to get the first half of a string using slicing.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax to extract the desired portion
# of the sequence. Slicing is efficient and readable, making it the preferred
# method for extracting subsequences from strings, lists, and tuples.

text = "abcdefgh"  # Initialize string variable
sliced_text = text[:len(text) // 2]  # Slice: extract a portion of the sequence
print(sliced_text)  # Expected output: abcd

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to get the second half of a string using slicing.
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
Problem: 1007
Write a Python program to get the second half of a string using slicing.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax to extract the desired portion
# of the sequence. Slicing is efficient and readable, making it the preferred
# method for extracting subsequences from strings, lists, and tuples.

text = "abcdefgh"  # Initialize string variable
sliced_text = text[len(text) // 2:]  # Slice: extract a portion of the sequence
print(sliced_text)  # Expected output: efgh

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to extract the middle two characters from an even-length string.
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
Problem: 1008
Write a Python program to extract the middle two characters from an even-length string.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax to extract the desired portion
# of the sequence. Slicing is efficient and readable, making it the preferred
# method for extracting subsequences from strings, lists, and tuples.

text = "abcdef"  # Initialize string variable
middle_index = len(text) // 2  # Calculate index position (middle or specific index)
sliced_text = text[middle_index - 1: middle_index + 1]  # Slice: extract a portion of the sequence
print(sliced_text)  # Expected output: cd

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to remove the first three elements from a list using slicing.
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
Problem: 1009
Write a Python program to remove the first three elements from a list using slicing.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax to extract the desired portion
# of the sequence. Slicing is efficient and readable, making it the preferred
# method for extracting subsequences from strings, lists, and tuples.

numbers = [1, 2, 3, 4, 5, 6]  # Initialize list
sliced_list = numbers[3:]  # Slice: extract a portion of the sequence
print(sliced_list)  # Expected output: [4, 5, 6]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to remove the last two elements from a tuple using slicing.
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
Problem: 1010
Write a Python program to remove the last two elements from a tuple using slicing.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax to extract the desired portion
# of the sequence. Slicing is efficient and readable, making it the preferred
# method for extracting subsequences from strings, lists, and tuples.

numbers = (10, 20, 30, 40, 50)  # Initialize tuple
sliced_tuple = numbers[:-2]  # Slice: extract a portion of the sequence
print(sliced_tuple)  # Expected output: (10, 20, 30)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to slice every alternate element from a list.
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
Problem: 1011
Write a Python program to slice every alternate element from a list.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax to extract the desired portion
# of the sequence. Slicing is efficient and readable, making it the preferred
# method for extracting subsequences from strings, lists, and tuples.

numbers = [1, 2, 3, 4, 5, 6, 7, 8]  # Initialize list
sliced_list = numbers[::2]  # Slice: extract elements with step 2
print(sliced_list)  # Expected output: [1, 3, 5, 7]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to extract a substring from index 3 to 7 using slicing.
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
Problem: 1012
Write a Python program to extract a substring from index 3 to 7 using slicing.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax to extract the desired portion
# of the sequence. Slicing is efficient and readable, making it the preferred
# method for extracting subsequences from strings, lists, and tuples.

text = "PythonProgramming"  # Initialize string variable
sliced_text = text[3:8]  # Slice: extract a portion of the sequence
print(sliced_text)  # Expected output: honPr

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to extract a tuple slice from index 2 to 5.
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
Problem: 1013
Write a Python program to extract a tuple slice from index 2 to 5.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax to extract the desired portion
# of the sequence. Slicing is efficient and readable, making it the preferred
# method for extracting subsequences from strings, lists, and tuples.

numbers = (100, 200, 300, 400, 500, 600)  # Initialize tuple
sliced_tuple = numbers[2:6]  # Slice: extract a portion of the sequence
print(sliced_tuple)  # Expected output: (300, 400, 500, 600)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a string is a palindrome using slicing.
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
Problem: 1014
Write a Python program to check if a string is a palindrome using slicing.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax to extract the desired portion
# of the sequence. Slicing is efficient and readable, making it the preferred
# method for extracting subsequences from strings, lists, and tuples.

def is_palindrome(s):  # Function definition: is_palindrome
    return s == s[::-1]  # Return the result

print(is_palindrome("madam"))  # Expected output: True
print(is_palindrome("hello"))  # Expected output: False

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to extract the last three characters of a string using slicing.
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
Problem: 1015
Write a Python program to extract the last three characters of a string using slicing.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax to extract the desired portion
# of the sequence. Slicing is efficient and readable, making it the preferred
# method for extracting subsequences from strings, lists, and tuples.

text = "Programming"  # Initialize string variable
sliced_text = text[-3:]  # Slice: extract a portion of the sequence
print(sliced_text)  # Expected output: ing

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to extract the first five elements of a list using slicing.
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
Problem: 1016
Write a Python program to extract the first five elements of a list using slicing.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax to extract the desired portion
# of the sequence. Slicing is efficient and readable, making it the preferred
# method for extracting subsequences from strings, lists, and tuples.

numbers = [10, 20, 30, 40, 50, 60, 70]  # Initialize list
sliced_list = numbers[:5]  # Slice: extract a portion of the sequence
print(sliced_list)  # Expected output: [10, 20, 30, 40, 50]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to extract all but the last three elements from a tuple using slicing.
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
Problem: 1017
Write a Python program to extract all but the last three elements from a tuple using slicing.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax to extract the desired portion
# of the sequence. Slicing is efficient and readable, making it the preferred
# method for extracting subsequences from strings, lists, and tuples.

numbers = (5, 10, 15, 20, 25, 30, 35)  # Initialize tuple
sliced_tuple = numbers[:-3]  # Slice: extract a portion of the sequence
print(sliced_tuple)  # Expected output: (5, 10, 15, 20)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to extract a string without its first and last two characters.
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
Problem: 1018
Write a Python program to extract a string without its first and last two characters.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax to extract the desired portion
# of the sequence. Slicing is efficient and readable, making it the preferred
# method for extracting subsequences from strings, lists, and tuples.

text = "HelloWorld"  # Initialize string variable
sliced_text = text[2:-2]  # Slice: extract a portion of the sequence
print(sliced_text)  # Expected output: lloWor

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a list of squares of numbers from 1 to 10 using list comprehension.
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
Problem: 1019
Write a Python program to create a list of squares of numbers from 1 to 10 using list comprehension.
"""

# SOLUTION EXPLANATION:
# This solution uses a list comprehension to create a new list based on the
# specified conditions. List comprehensions are concise, readable, and often
# more efficient than equivalent loops for creating lists.

squares = [x ** 2 for x in range(1, 11)]  # List comprehension: creates a new list
print(squares)  # Expected output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a list of even numbers from 1 to 20 using list comprehension.
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
Problem: 1020
Write a Python program to create a list of even numbers from 1 to 20 using list comprehension.
"""

# SOLUTION EXPLANATION:
# This solution uses a list comprehension to create a new list based on the
# specified conditions. List comprehensions are concise, readable, and often
# more efficient than equivalent loops for creating lists.

evens = [x for x in range(1, 21) if x % 2 == 0]  # List comprehension: creates a new list
print(evens)  # Expected output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a list of numbers from 1 to 50 that are divisible by 5 using list comprehension.
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
Problem: 1021
Write a Python program to create a list of numbers from 1 to 50 that are divisible by 5 using list comprehension.
"""

# SOLUTION EXPLANATION:
# This solution uses a list comprehension to create a new list based on the
# specified conditions. List comprehensions are concise, readable, and often
# more efficient than equivalent loops for creating lists.

div_by_5 = [x for x in range(1, 51) if x % 5 == 0]  # List comprehension: creates a new list
print(div_by_5)  # Expected output: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a list of the first letter of each word in a given sentence using list comprehension.
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
Problem: 1022
Write a Python program to create a list of the first letter of each word in a given sentence using list comprehension.
"""

# SOLUTION EXPLANATION:
# This solution uses a list comprehension to create a new list based on the
# specified conditions. List comprehensions are concise, readable, and often
# more efficient than equivalent loops for creating lists.

sentence = "Python is a powerful programming language"  # Initialize string variable
first_letters = [word[0] for word in sentence.split()]  # List comprehension: creates a new list
print(first_letters)  # Expected output: ['P', 'i', 'a', 'p', 'p', 'l']

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a list of words with more than three letters from a sentence using list comprehension.
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
Problem: 1023
Write a Python program to create a list of words with more than three letters from a sentence using list comprehension.
"""

# SOLUTION EXPLANATION:
# This solution uses a list comprehension to create a new list based on the
# specified conditions. List comprehensions are concise, readable, and often
# more efficient than equivalent loops for creating lists.

sentence = "The sun is bright today"  # Initialize string variable
long_words = [word for word in sentence.split() if len(word) > 3]  # List comprehension: creates a new list
print(long_words)  # Expected output: ['bright', 'today']

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to generate a list of tuples containing a number and its square for numbers from 1 to 10. List comprehension.
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
Problem: 1024
Write a Python program to generate a list of tuples containing a number and its square for numbers from 1 to 10. List comprehension.
"""

# SOLUTION EXPLANATION:
# This solution uses a list comprehension to create a new list based on the
# specified conditions. List comprehensions are concise, readable, and often
# more efficient than equivalent loops for creating lists.

squares_tuples = [(x, x**2) for x in range(1, 11)]  # List comprehension: creates a new list
print(squares_tuples)  # Expected output: [(1, 1), (2, 4), ..., (10, 100)]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a new list where every element from an existing list is doubled. List comprehension.
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
Problem: 1025
Write a Python program to create a new list where every element from an existing list is doubled. List comprehension.
"""

# SOLUTION EXPLANATION:
# This solution uses a list comprehension to create a new list based on the
# specified conditions. List comprehensions are concise, readable, and often
# more efficient than equivalent loops for creating lists.

numbers = [3, 5, 7, 9]  # Initialize list
doubled = [x * 2 for x in numbers]  # List comprehension: creates a new list
print(doubled)  # Expected output: [6, 10, 14, 18]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a list of numbers from 1 to 100 that are either divisible by 3 or 7. List comprehension.
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
Problem: 1026
Write a Python program to create a list of numbers from 1 to 100 that are either divisible by 3 or 7. List comprehension.
"""

# SOLUTION EXPLANATION:
# This solution uses a list comprehension to create a new list based on the
# specified conditions. List comprehensions are concise, readable, and often
# more efficient than equivalent loops for creating lists.

div_by_3_or_7 = [x for x in range(1, 101) if x % 3 == 0 or x % 7 == 0]  # List comprehension: creates a new list
print(div_by_3_or_7)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to convert a list of strings to uppercase using list comprehension.
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
Problem: 1027
Write a Python program to convert a list of strings to uppercase using list comprehension.
"""

# SOLUTION EXPLANATION:
# This solution uses a list comprehension to create a new list based on the
# specified conditions. List comprehensions are concise, readable, and often
# more efficient than equivalent loops for creating lists.

words = ["hello", "world", "python"]  # Initialize list
upper_words = [word.upper() for word in words]  # List comprehension: creates a new list
print(upper_words)  # Expected output: ['HELLO', 'WORLD', 'PYTHON']

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to flatten a nested list using list comprehension.
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
Problem: 1028
Write a Python program to flatten a nested list using list comprehension.
"""

# SOLUTION EXPLANATION:
# This solution uses a list comprehension to create a new list based on the
# specified conditions. List comprehensions are concise, readable, and often
# more efficient than equivalent loops for creating lists.

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Initialize list
flattened = [num for sublist in nested_list for num in sublist]  # List comprehension: creates a new list
print(flattened)  # Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a list of vowels from a given string using list comprehension.
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
Problem: 1029
Write a Python program to create a list of vowels from a given string using list comprehension.
"""

# SOLUTION EXPLANATION:
# This solution uses a list comprehension to create a new list based on the
# specified conditions. List comprehensions are concise, readable, and often
# more efficient than equivalent loops for creating lists.

text = "List Comprehension is Powerful"  # Initialize string variable
vowels = [char for char in text if char.lower() in "aeiou"]  # List comprehension: creates a new list
print(vowels)  # Expected output: ['i', 'o', 'e', 'e', 'i', 'o', 'i', 'o', 'e']

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to extract only numeric values from a mixed list. List comprehension.
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
Problem: 1030
Write a Python program to extract only numeric values from a mixed list. List comprehension.
"""

# SOLUTION EXPLANATION:
# This solution uses a list comprehension to create a new list based on the
# specified conditions. List comprehensions are concise, readable, and often
# more efficient than equivalent loops for creating lists.

mixed_list = [10, "apple", 15.5, "banana", 30, "42"]  # Initialize list
numbers = [x for x in mixed_list if isinstance(x, (int, float))]  # List comprehension: creates a new list
print(numbers)  # Expected output: [10, 15.5, 30]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to generate a list of first 10 Fibonacci numbers using list comprehension.
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
Problem: 1031
Write a Python program to generate a list of first 10 Fibonacci numbers using list comprehension.
"""

# SOLUTION EXPLANATION:
# This solution uses a list comprehension to create a new list based on the
# specified conditions. List comprehensions are concise, readable, and often
# more efficient than equivalent loops for creating lists.

fib = [0, 1]  # Initialize list
[fib.append(fib[-1] + fib[-2]) for _ in range(8)]  # Method or function call
print(fib)  # Expected output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a list of prime numbers up to 50 using list comprehension.
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
Problem: 1032
Write a Python program to create a list of prime numbers up to 50 using list comprehension.
"""

# SOLUTION EXPLANATION:
# This solution uses a list comprehension to create a new list based on the
# specified conditions. List comprehensions are concise, readable, and often
# more efficient than equivalent loops for creating lists.

primes = [x for x in range(2, 51) if all(x % y != 0 for y in range(2, int(x**0.5) + 1))]  # List comprehension: creates a new list
print(primes)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to generate a list of all words in a sentence that end with a vowel. List comprehension.
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
Problem: 1033
Write a Python program to generate a list of all words in a sentence that end with a vowel. List comprehension.
"""

# SOLUTION EXPLANATION:
# This solution uses a list comprehension to create a new list based on the
# specified conditions. List comprehensions are concise, readable, and often
# more efficient than equivalent loops for creating lists.

sentence = "The apple is on the tree"  # Initialize string variable
vowel_ending_words = [word for word in sentence.split() if word[-1].lower() in "aeiou"]  # List comprehension: creates a new list
print(vowel_ending_words)  # Expected output: ['The', 'apple', 'is', 'tree']

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a list of lowercase characters from a given string. List comprehension.
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
Problem: 1034
Write a Python program to create a list of lowercase characters from a given string. List comprehension.
"""

# SOLUTION EXPLANATION:
# This solution uses a list comprehension to create a new list based on the
# specified conditions. List comprehensions are concise, readable, and often
# more efficient than equivalent loops for creating lists.

text = "Python List Comprehension"  # Initialize string variable
lower_chars = [char for char in text if char.islower()]  # List comprehension: creates a new list
print(lower_chars)  # Expected output: ['y', 't', 'h', 'o', 'n', 'i', 's', 't', 'o', 'm', 'p', 'r', 'e', 'h', 'e', 'n', 's', 'i', 'o', 'n']

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a list of words with their lengths from a given sentence. List comprehension.
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
Problem: 1035
Write a Python program to create a list of words with their lengths from a given sentence. List comprehension.
"""

# SOLUTION EXPLANATION:
# This solution uses a list comprehension to create a new list based on the
# specified conditions. List comprehensions are concise, readable, and often
# more efficient than equivalent loops for creating lists.

sentence = "List comprehension makes Python concise"  # Initialize string variable
word_lengths = [(word, len(word)) for word in sentence.split()]  # List comprehension: creates a new list
print(word_lengths)  # Expected output: [('List', 4), ('comprehension', 13), ('makes', 5), ('Python', 6), ('concise', 7)]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to remove duplicates from a list using list comprehension.
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
Problem: 1036
Write a Python program to remove duplicates from a list using list comprehension.
"""

# SOLUTION EXPLANATION:
# This solution uses a list comprehension to create a new list based on the
# specified conditions. List comprehensions are concise, readable, and often
# more efficient than equivalent loops for creating lists.

numbers = [1, 2, 2, 3, 4, 4, 5]  # Initialize list
unique_numbers = list(dict.fromkeys(numbers))  # Variable assignment
print(unique_numbers)  # Expected output: [1, 2, 3, 4, 5]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to filter words containing the letter 'p' from a given list. List comprehension.
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
Problem: 1037
Write a Python program to filter words containing the letter 'p' from a given list. List comprehension.
"""

# SOLUTION EXPLANATION:
# This solution uses a list comprehension to create a new list based on the
# specified conditions. List comprehensions are concise, readable, and often
# more efficient than equivalent loops for creating lists.

words = ["apple", "banana", "grape", "cherry", "peach"]  # Initialize list
filtered_words = [word for word in words if "p" in word]  # List comprehension: creates a new list
print(filtered_words)  # Expected output: ['apple', 'grape', 'peach']

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python recursive function to calculate the factorial of a given number.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1038
Write a Python recursive function to calculate the factorial of a given number.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def factorial(n):  # Function definition: factorial
    return 1 if n == 0 else n * factorial(n - 1)  # Return the result

print(factorial(5))  # Expected output: 120

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python recursive function to calculate the sum of all numbers from 1 to n.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1039
Write a Python recursive function to calculate the sum of all numbers from 1 to n.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def sum_n(n):  # Function definition: sum_n
    return n if n == 1 else n + sum_n(n - 1)  # Return the result

print(sum_n(10))  # Expected output: 55

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python recursive function to compute the nth Fibonacci number.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1040
Write a Python recursive function to compute the nth Fibonacci number.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def fibonacci(n):  # Function definition: fibonacci
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)  # Return the result

print(fibonacci(6))  # Expected output: 8

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python recursive function to reverse a string.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1041
Write a Python recursive function to reverse a string.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def reverse_string(s):  # Function definition: reverse_string
    return s if len(s) == 0 else s[-1] + reverse_string(s[:-1])  # Return the result

print(reverse_string("hello"))  # Expected output: olleh

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python recursive function to count the number of digits in a given number.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1042
Write a Python recursive function to count the number of digits in a given number.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def count_digits(n):  # Function definition: count_digits
    return 1 if n < 10 else 1 + count_digits(n // 10)  # Return the result

print(count_digits(12345))  # Expected output: 5

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python recursive function to find the greatest common divisor (GCD) of two numbers.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1043
Write a Python recursive function to find the greatest common divisor (GCD) of two numbers.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def gcd(a, b):  # Function definition: gcd
    return a if b == 0 else gcd(b, a % b)  # Return the result

print(gcd(48, 18))  # Expected output: 6

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python recursive function to find the sum of elements in a list.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1044
Write a Python recursive function to find the sum of elements in a list.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def list_sum(lst):  # Function definition: list_sum
    return 0 if not lst else lst[0] + list_sum(lst[1:])  # Return the result

print(list_sum([1, 2, 3, 4, 5]))  # Expected output: 15

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python recursive function to check if a number is a palindrome.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1045
Write a Python recursive function to check if a number is a palindrome.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def is_palindrome(n, temp=None):  # Function definition: is_palindrome
    if temp is None:  # Conditional check
        temp = str(n)  # Variable assignment
    return True if len(temp) <= 1 else temp[0] == temp[-1] and is_palindrome(n, temp[1:-1])  # Return the result

print(is_palindrome(121))  # Expected output: True
print(is_palindrome(123))  # Expected output: False

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python recursive function to find the power of a number.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1046
Write a Python recursive function to find the power of a number.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def power(x, n):  # Function definition: power
    return 1 if n == 0 else x * power(x, n - 1)  # Return the result

print(power(2, 3))  # Expected output: 8

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python recursive function to compute the product of two numbers.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1047
Write a Python recursive function to compute the product of two numbers.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def multiply(a, b):  # Function definition: multiply
    return 0 if b == 0 else a + multiply(a, b - 1)  # Return the result

print(multiply(5, 4))  # Expected output: 20

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python recursive function to print numbers from 1 to n.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1048
Write a Python recursive function to print numbers from 1 to n.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def print_numbers(n):  # Function definition: print_numbers
    if n > 0:  # Conditional check
        print_numbers(n - 1)
        print(n)  # Print the result

print_numbers(5)  
# Expected output:
# 1
# 2
# 3
# 4
# 5

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python recursive function to print numbers from n to 1.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1049
Write a Python recursive function to print numbers from n to 1.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def print_reverse(n):  # Function definition: print_reverse
    if n > 0:  # Conditional check
        print(n)  # Print the result
        print_reverse(n - 1)

print_reverse(5)  
# Expected output:
# 5
# 4
# 3
# 2
# 1

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python recursive function to check if a list is sorted in ascending order.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1050
Write a Python recursive function to check if a list is sorted in ascending order.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def is_sorted(lst):  # Function definition: is_sorted
    return True if len(lst) <= 1 else lst[0] <= lst[1] and is_sorted(lst[1:])  # Return the result

print(is_sorted([1, 2, 3, 4, 5]))  # Expected output: True
print(is_sorted([5, 3, 1]))  # Expected output: False

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python recursive function to count the occurrences of a character in a string.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1051
Write a Python recursive function to count the occurrences of a character in a string.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def char_count(s, c):  # Function definition: char_count
    return 0 if not s else (1 if s[0] == c else 0) + char_count(s[1:], c)  # Return the result

print(char_count("banana", "a"))  # Expected output: 3

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python recursive function to generate all binary strings of length n.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1052
Write a Python recursive function to generate all binary strings of length n.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def binary_strings(n, s=""):  # Function definition: binary_strings
    if n == 0:  # Conditional check
        print(s)  # Print the result
    else:
        binary_strings(n - 1, s + "0")
        binary_strings(n - 1, s + "1")

binary_strings(3)  
# Expected output:
# 000
# 001
# 010
# 011
# 100
# 101
# 110
# 111

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python recursive function to compute the sum of digits of a number.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1053
Write a Python recursive function to compute the sum of digits of a number.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def sum_of_digits(n):  # Function definition: sum_of_digits
    if n == 0:  # Conditional check
        return 0  # Return the result
    # Recursive case: add the last digit to the sum of the remaining digits
    else:
        return n % 10 + sum_of_digits(n // 10)  # Return the result

string = 1244  # Variable assignment
print(sum_of_digits(string))  # Output: 11  # Print the result

def sum_of_digits(n):  # Function definition: sum_of_digits
    return n if n < 10 else (n % 10) + sum_of_digits(n // 10)  # Return the result

print(sum_of_digits(1234))  # Expected output: 10

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python recursive function to calculate the nth triangular number.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1054
Write a Python recursive function to calculate the nth triangular number.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def triangular_number(n):  # Function definition: triangular_number
    return 0 if n == 0 else n + triangular_number(n - 1)  # Return the result

print(triangular_number(5))  # Expected output: 15

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python recursive function to remove duplicates from a string.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1055
Write a Python recursive function to remove duplicates from a string.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def remove_duplicates(s, seen=""):  # Function definition: remove_duplicates
    return "" if not s else (remove_duplicates(s[1:], seen) if s[0] in seen else s[0] + remove_duplicates(s[1:], seen + s[0]))  # Return the result

print(remove_duplicates("banana"))  # Expected output: ban

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python recursive function to generate all permutations of a given string.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1056
Write a Python recursive function to generate all permutations of a given string.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def permutations(s, prefix=""):  # Function definition: permutations
    if not s:  # Conditional check
        print(prefix)  # Print the result
    else:
        for i in range(len(s)):  # Loop through items
            permutations(s[:i] + s[i+1:], prefix + s[i])

permutations("abc")  
# Expected output:
# abc
# acb
# bac
# bca
# cab
# cba

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to find the longest string in a list using the `max()` function with a lambda expression.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1057
Write a Python program to find the longest string in a list using the `max()` function with a lambda expression.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def longest_string(words):  # Function definition: longest_string
    return max(words, key=lambda word: len(word))  # Return the result

result = longest_string(["apple", "banana", "cherry"])  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a number is even using a lambda function.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1058
Write a Python program to check if a number is even using a lambda function.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

is_even = lambda x: x % 2 == 0  # Variable assignment

result = is_even(4)  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to calculate the square root of all elements in a list using a lambda function.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1059
Write a Python program to calculate the square root of all elements in a list using a lambda function.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

import math  # Import module or function

def square_roots(numbers):  # Function definition: square_roots
    return list(map(lambda x: math.sqrt(x), numbers))  # Return the result

result = square_roots([4, 9, 16])  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a string contains any digits using a lambda function.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1060
Write a Python program to check if a string contains any digits using a lambda function.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

contains_digits = lambda s: any(map(str.isdigit, s))  # Variable assignment

result = contains_digits("hello123")  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to sort a list of tuples based on the first element in descending order using a lambda expression.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1061
Write a Python program to sort a list of tuples based on the first element in descending order using a lambda expression.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def sort_by_first_element_desc(tuples):  # Function definition: sort_by_first_element_desc
    return sorted(tuples, key=lambda x: x[0], reverse=True)  # Return the result

result = sort_by_first_element_desc([(3, "apple"), (1, "banana"), (2, "cherry")])  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to filter out words that are shorter than a given length using the `filter()` function with a lambda expression.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1062
Write a Python program to filter out words that are shorter than a given length using the `filter()` function with a lambda expression.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def filter_short_words(words, length):  # Function definition: filter_short_words
    return list(filter(lambda word: len(word) >= length, words))  # Return the result

result = filter_short_words(["apple", "banana", "cherry", "date"], 6)  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to double all elements in a list using a lambda function.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1063
Write a Python program to double all elements in a list using a lambda function.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def double_elements(numbers):  # Function definition: double_elements
    return list(map(lambda x: x * 2, numbers))  # Return the result

result = double_elements([1, 2, 3, 4])  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a number is divisible by 3 using a lambda function.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1064
Write a Python program to check if a number is divisible by 3 using a lambda function.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

is_divisible_by_3 = lambda x: x % 3 == 0  # Variable assignment

result = is_divisible_by_3(9)  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to find the second largest number in a list using a lambda function.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1065
Write a Python program to find the second largest number in a list using a lambda function.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

second_largest = lambda numbers: sorted(set(numbers))[-2]  # Slice: extract a portion of the sequence

result = second_largest([10, 20, 30, 40, 50])  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to map a list of numbers into their cubes using a lambda function.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1066
Write a Python program to map a list of numbers into their cubes using a lambda function.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def cube_elements(numbers):  # Function definition: cube_elements
    return list(map(lambda x: x ** 3, numbers))  # Return the result

result = cube_elements([1, 2, 3, 4])  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to sort a list of words by their lengths using the `sorted()` function with a lambda expression.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1067
Write a Python program to sort a list of words by their lengths using the `sorted()` function with a lambda expression.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def sort_by_length(words):  # Function definition: sort_by_length
    return sorted(words, key=lambda word: len(word))  # Return the result

result = sort_by_length(["apple", "banana", "kiwi", "cherry"])  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a number is odd using a lambda function.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1068
Write a Python program to check if a number is odd using a lambda function.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

is_odd = lambda x: x % 2 != 0  # Variable assignment

result = is_odd(5)  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to find the sum of all elements in a list using the `reduce()` function with a lambda expression.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1069
Write a Python program to find the sum of all elements in a list using the `reduce()` function with a lambda expression.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

from functools import reduce  # Import module or function

def sum_of_elements(numbers):  # Function definition: sum_of_elements
    return reduce(lambda x, y: x + y, numbers)  # Return the result

result = sum_of_elements([1, 2, 3, 4])  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a string ends with a vowel using a lambda function.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1070
Write a Python program to check if a string ends with a vowel using a lambda function.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

ends_with_vowel = lambda s: s[-1].lower() in 'aeiou'  # Slice: extract a portion of the sequence

result = ends_with_vowel("hello")  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to find the smallest number in a list using the `min()` function with a lambda expression.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1071
Write a Python program to find the smallest number in a list using the `min()` function with a lambda expression.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

# Define a list of numbers
numbers = [12, 45, 7, 23, 56, 89, 34]  # Initialize list

# Use the min() function with a lambda expression to find the smallest number
smallest_number = min(numbers, key=lambda x: x)  # Find maximum or minimum value

# Print the result
print("The smallest number in the list is:", smallest_number)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a string contains only alphabetic characters using a lambda function.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1072
Write a Python program to check if a string contains only alphabetic characters using a lambda function.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

is_alpha = lambda s: s.isalpha()  # Variable assignment

result = is_alpha("hello")  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to convert all integers in a list to strings using a lambda function.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1073
Write a Python program to convert all integers in a list to strings using a lambda function.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def convert_to_strings(numbers):  # Function definition: convert_to_strings
    return list(map(lambda x: str(x), numbers))  # Return the result

result = convert_to_strings([1, 2, 3, 4])  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to find the sum of all even numbers in a list using a lambda expression.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1074
Write a Python program to find the sum of all even numbers in a list using a lambda expression.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def sum_of_even(numbers):  # Function definition: sum_of_even
    return sum(filter(lambda x: x % 2 == 0, numbers))  # Return the result

result = sum_of_even([1, 2, 3, 4, 5, 6])  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to remove all whitespace from a string using a lambda function.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1075
Write a Python program to remove all whitespace from a string using a lambda function.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

string = "i'm going for a walk"  # Initialize string variable
result = lambda char: char.replace(" ", "")  # Variable assignment

result(string)

remove_whitespace = lambda s: ''.join(s.split())  # Split string into a list

result = remove_whitespace("hello world")  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to count the number of even numbers in a list using a lambda function.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1076
Write a Python program to count the number of even numbers in a list using a lambda function.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

count_even = lambda numbers: len(list(filter(lambda x: x % 2 == 0, numbers)))  # Calculate the length

result = count_even([1, 2, 3, 4, 5, 6])  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to find the product of all odd numbers in a list using a lambda function.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1077
Write a Python program to find the product of all odd numbers in a list using a lambda function.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

from functools import reduce  # Import module or function

product_of_odds = lambda numbers: reduce(lambda x, y: x * y, filter(lambda x: x % 2 != 0, numbers))  # Variable assignment

result = product_of_odds([1, 2, 3, 4, 5])  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a number is prime using a lambda function.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1078
Write a Python program to check if a number is prime using a lambda function.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

is_prime = lambda n: all(n % i != 0 for i in range(2, int(n ** 0.5) + 1)) if n > 1 else False  # Variable assignment: create a range

result = is_prime(7)  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a list of tuples (number, square root) for each number in a given list using a lambda function.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1079
Write a Python program to create a list of tuples (number, square root) for each number in a given list using a lambda function.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

import math  # Import module or function

def create_square_root_tuples(numbers):  # Function definition: create_square_root_tuples
    return list(map(lambda x: (x, math.sqrt(x)), numbers))  # Return the result

result = create_square_root_tuples([4, 9, 16])  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a string contains any uppercase letters using a lambda function.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1080
Write a Python program to check if a string contains any uppercase letters using a lambda function.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

contains_uppercase = lambda s: any(map(str.isupper, s))  # Variable assignment

result = contains_uppercase("Hello")  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to find the average of odd numbers in a list using a lambda function.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1081
Write a Python program to find the average of odd numbers in a list using a lambda function.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def average_of_odds(lst):  # Function definition: average_of_odds
    odd = list(filter(lambda num: num % 2 !=0, lst))  # Variable assignment
    total = sum(odd)  # Variable assignment
    count = len(odd)  # Calculate the length
    average = total / count  # Variable assignment
    return average  # Return the result
lst = [1,2,3,4,5,6,7,8,9]  # Initialize list

average_of_odds(lst)

def average_of_odds(numbers):  # Function definition: average_of_odds
    odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))  # Variable assignment
    return sum(odd_numbers) / len(odd_numbers) if odd_numbers else 0  # Return the result

result = average_of_odds([1, 2, 3, 4, 5])  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a list of squares for all odd numbers in a list using a lambda function.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1082
Write a Python program to create a list of squares for all odd numbers in a list using a lambda function.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def square_odd_numbers(numbers):  # Function definition: square_odd_numbers
    return list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, numbers)))  # Return the result

result = square_odd_numbers([1, 2, 3, 4, 5])  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a list contains any negative numbers using a lambda function.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1083
Write a Python program to check if a list contains any negative numbers using a lambda function.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

contains_negative = lambda numbers: any(map(lambda x: x < 0, numbers))  # Variable assignment

result = contains_negative([1, -2, 3, 4])  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a list of tuples where the first element is the original number and the second element is its cube using a lambda function.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1084
Write a Python program to create a list of tuples where the first element is the original number and the second element is its cube using a lambda function.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def create_cube_tuples(numbers):  # Function definition: create_cube_tuples
    return list(map(lambda x: (x, x**3), numbers))  # Return the result

result = create_cube_tuples([1, 2, 3])  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to filter out numbers greater than a given value using a lambda function.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1085
Write a Python program to filter out numbers greater than a given value using a lambda function.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def filter_greater_than(numbers, value):  # Function definition: filter_greater_than
    return list(filter(lambda x: x <= value, numbers))  # Return the result

result = filter_greater_than([1, 2, 3, 4, 5], 3)  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to convert a list of strings to their lengths using a lambda function.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1086
Write a Python program to convert a list of strings to their lengths using a lambda function.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def convert_to_lengths(strings):  # Function definition: convert_to_lengths
    return list(map(lambda x: len(x), strings))  # Return the result

result = convert_to_lengths(["apple", "banana", "cherry"])  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a number is a perfect square using a lambda function.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1087
Write a Python program to check if a number is a perfect square using a lambda function.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

is_perfect_square = lambda x: int(x**0.5) ** 2 == x  # Variable assignment

result = is_perfect_square(16)  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to find the sum of the cubes of all numbers in a list using a lambda function.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1088
Write a Python program to find the sum of the cubes of all numbers in a list using a lambda function.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def sum_of_cubes(numbers):  # Function definition: sum_of_cubes
    return sum(map(lambda x: x**3, numbers))  # Return the result

result = sum_of_cubes([1, 2, 3])  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to remove all elements greater than a specific value in a list using a lambda function.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1089
Write a Python program to remove all elements greater than a specific value in a list using a lambda function.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def remove_elements_greater_than(numbers, value):  # Function definition: remove_elements_greater_than
    return list(filter(lambda x: x <= value, numbers))  # Return the result

result = remove_elements_greater_than([1, 2, 3, 4, 5], 3)  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if all elements in a list are positive using a lambda function.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1090
Write a Python program to check if all elements in a list are positive using a lambda function.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

all_positive = lambda numbers: all(map(lambda x: x > 0, numbers))  # Variable assignment

result = all_positive([1, 2, 3, 4])  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a generator that yields the square of each number in a given range.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1091
Write a Python program to create a generator that yields the square of each number in a given range.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def square_generator(n):  # Function definition: square_generator
    for i in range(n):  # Loop through items
        yield i**2

result = list(square_generator(5))  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a generator that yields Fibonacci numbers up to a given number.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1092
Write a Python program to create a generator that yields Fibonacci numbers up to a given number.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def fibonacci_generator(limit):  # Function definition: fibonacci_generator
    a, b = 0, 1  # Variable assignment
    while a <= limit:  # Code block
        yield a
        a, b = b, a + b  # Variable assignment

result = list(fibonacci_generator(20))  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a generator that yields the characters of a string one by one.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1093
Write a Python program to create a generator that yields the characters of a string one by one.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def char_generator(s):  # Function definition: char_generator
    for char in s:  # Loop through items
        yield char

result = list(char_generator("hello"))  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a generator that yields numbers from 1 to n with a step of 2.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1094
Write a Python program to create a generator that yields numbers from 1 to n with a step of 2.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def step_generator(n):  # Function definition: step_generator
    for i in range(1, n, 2):  # Loop through items
        yield i

result = list(step_generator(10))  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a generator that yields even numbers from 1 to n.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1095
Write a Python program to create a generator that yields even numbers from 1 to n.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def even_number_generator(n):  # Function definition: even_number_generator
    for i in range(2, n+1, 2):  # Loop through items
        yield i

result = list(even_number_generator(10))  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a generator that yields squares of even numbers from 1 to n.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1096
Write a Python program to create a generator that yields squares of even numbers from 1 to n.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def square_even_generator(n):  # Function definition: square_even_generator
    for i in range(2, n+1, 2):  # Loop through items
        yield i**2

result = list(square_even_generator(10))  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a generator that yields the first n prime numbers.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1097
Write a Python program to create a generator that yields the first n prime numbers.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def prime_generator(n):  # Function definition: prime_generator
    primes = []  # Initialize list
    num = 2  # Variable assignment
    while len(primes) < n:  # Code block
        if all(num % p != 0 for p in primes):  # Conditional check
            primes.append(num)  # Method or function call
        num += 1
    yield from primes

result = list(prime_generator(5))  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a generator that yields the sum of consecutive pairs from a given list.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1098
Write a Python program to create a generator that yields the sum of consecutive pairs from a given list.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def consecutive_pair_sum(lst):  # Function definition: consecutive_pair_sum
    for i in range(len(lst)-1):  # Loop through items
        yield lst[i] + lst[i+1]

result = list(consecutive_pair_sum([1, 2, 3, 4, 5]))  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a generator that yields the factorial of each number from 1 to n.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1099
Write a Python program to create a generator that yields the factorial of each number from 1 to n.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def factorial_generator(n):  # Function definition: factorial_generator
    def factorial(x):  # Function definition: factorial
        result = 1  # Variable assignment
        for i in range(1, x+1):  # Loop through items
            result *= i
        return result  # Return the result
    for i in range(1, n+1):  # Loop through items
        yield factorial(i)

result = list(factorial_generator(5))  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a generator that yields numbers divisible by 3 and 5 from 1 to n.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1100
Write a Python program to create a generator that yields numbers divisible by 3 and 5 from 1 to n.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def divisible_by_3_and_5_generator(n):  # Function definition: divisible_by_3_and_5_generator
    for i in range(1, n+1):  # Loop through items
        if i % 3 == 0 and i % 5 == 0:  # Conditional check
            yield i

result = list(divisible_by_3_and_5_generator(50))  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a generator that filters out the odd numbers from a list.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1101
Write a Python program to create a generator that filters out the odd numbers from a list.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def odd_filter_generator(lst):  # Function definition: odd_filter_generator
    for num in lst:  # Loop through items
        if num % 2 == 0:  # Conditional check
            yield num

result = list(odd_filter_generator([1, 2, 3, 4, 5, 6]))  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a generator that yields the cumulative sum of a given list of numbers.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1102
Write a Python program to create a generator that yields the cumulative sum of a given list of numbers.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def cumulative_sum_generator(lst):  # Function definition: cumulative_sum_generator
    total = 0  # Variable assignment
    for num in lst:  # Loop through items
        total += num
        yield total

result = list(cumulative_sum_generator([1, 2, 3, 4, 5]))  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a generator that yields the n-th power of each number from 1 to n.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1103
Write a Python program to create a generator that yields the n-th power of each number from 1 to n.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def power_generator(n, power):  # Function definition: power_generator
    for i in range(1, n+1):  # Loop through items
        yield i**power

result = list(power_generator(5, 3))  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a generator that yields each word in a sentence.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1104
Write a Python program to create a generator that yields each word in a sentence.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def word_generator(sentence):  # Function definition: word_generator
    words = sentence.split()  # Split string into a list
    for word in words:  # Loop through items
        yield word

result = list(word_generator("This is a test sentence"))  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a generator that yields numbers that are squares of integers up to n.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1105
Write a Python program to create a generator that yields numbers that are squares of integers up to n.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def square_number_generator(n):  # Function definition: square_number_generator
    for i in range(1, n+1):  # Loop through items
        yield i**2

result = list(square_number_generator(5))  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a generator that yields the squares of odd numbers from 1 to n.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1106
Write a Python program to create a generator that yields the squares of odd numbers from 1 to n.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def main(n):  # Function definition: main
    for num in range(1, n+1):  # Loop through items
        if num % 2 != 0:  # Conditional check
            yield num ** 2

n = 10  # Variable assignment
result = list(main(n))  # Variable assignment
print(result)  # Print the result

def square_odd_number_generator(n):  # Function definition: square_odd_number_generator
    for i in range(1, n+1, 2):  # Loop through items
        yield i**2

result = list(square_odd_number_generator(10))  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a generator that yields the elements of a given list in reverse order.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1107
Write a Python program to create a generator that yields the elements of a given list in reverse order.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def reverse_list_generator(lst):  # Function definition: reverse_list_generator
    for i in range(len(lst)-1, -1, -1):  # Loop through items
        yield lst[i]

result = list(reverse_list_generator([1, 2, 3, 4, 5]))  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a generator that yields multiples of a given number up to n.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1108
Write a Python program to create a generator that yields multiples of a given number up to n.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def multiple_generator(n, multiple):  # Function definition: multiple_generator
    for i in range(multiple, n+1, multiple):  # Loop through items
        yield i

result = list(multiple_generator(20, 3))  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a generator that yields all the uppercase letters in a string.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1109
Write a Python program to create a generator that yields all the uppercase letters in a string.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def uppercase_generator(s):  # Function definition: uppercase_generator
    for char in s:  # Loop through items
        if char.isupper():  # Conditional check
            yield char

result = list(uppercase_generator("Hello World"))  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a generator that yields the differences between consecutive elements of a list.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1110
Write a Python program to create a generator that yields the differences between consecutive elements of a list.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def consecutive_diff_generator(lst):  # Function definition: consecutive_diff_generator
    for i in range(len(lst)-1):  # Loop through items
        yield lst[i+1] - lst[i]

result = list(consecutive_diff_generator([1, 3, 6, 10]))  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a generator that yields numbers greater than a given value in a list.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1111
Write a Python program to create a generator that yields numbers greater than a given value in a list.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def greater_than_generator(lst, value):  # Function definition: greater_than_generator
    for num in lst:  # Loop through items
        if num > value:  # Conditional check
            yield num

result = list(greater_than_generator([1, 2, 3, 4, 5, 6], 3))  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a generator that yields the sum of each element with its index from a list.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1112
Write a Python program to create a generator that yields the sum of each element with its index from a list.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def sum_with_index_generator(lst):  # Function definition: sum_with_index_generator
    for index, num in enumerate(lst):  # Loop through items
        yield num + index

result = list(sum_with_index_generator([10, 20, 30, 40]))  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a generator that yields all palindromes from a list of strings.
# 
# This problem demonstrates string manipulation and comparison. A palindrome
# is a sequence that reads the same forwards and backwards. This problem
# tests understanding of string operations and logical comparisons.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1113
Write a Python program to create a generator that yields all palindromes from a list of strings.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def palindrome_generator(lst):  # Function definition: palindrome_generator
    for word in lst:  # Loop through items
        if word == word[::-1]:  # Conditional check
            yield word

result = list(palindrome_generator(["madam", "apple", "racecar", "banana"]))  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a generator that yields the product of elements in pairs from a given list.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1114
Write a Python program to create a generator that yields the product of elements in pairs from a given list.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def pair_product_generator(lst):  # Function definition: pair_product_generator
    for i in range(len(lst)-1):  # Loop through items
        yield lst[i] * lst[i+1]

result = list(pair_product_generator([1, 2, 3, 4]))  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a generator that yields elements from a list that are greater than the previous element.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1115
Write a Python program to create a generator that yields elements from a list that are greater than the previous element.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def greater_than_previous_generator(lst):  # Function definition: greater_than_previous_generator
    for i in range(1, len(lst)):  # Loop through items
        if lst[i] > lst[i-1]:  # Conditional check
            yield lst[i]

result = list(greater_than_previous_generator([1, 2, 1, 4, 3]))  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a generator that yields all numbers in a list that are divisible by a given number.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1116
Write a Python program to create a generator that yields all numbers in a list that are divisible by a given number.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def divisible_by_generator(lst, divisor):  # Function definition: divisible_by_generator
    for num in lst:  # Loop through items
        if num % divisor == 0:  # Conditional check
            yield num

result = list(divisible_by_generator([10, 15, 20, 25, 30], 5))  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a generator that yields the first n even Fibonacci numbers.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1117
Write a Python program to create a generator that yields the first n even Fibonacci numbers.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def even_fibonacci_generator(n):  # Function definition: even_fibonacci_generator
    a, b = 0, 2  # Variable assignment
    count = 0  # Variable assignment
    while count < n:  # Code block
        yield a
        a, b = b, 4 * b + a  # Variable assignment
        count += 1

result = list(even_fibonacci_generator(5))  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a generator that yields all the even-indexed elements of a list.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1118
Write a Python program to create a generator that yields all the even-indexed elements of a list.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def even_index_generator(lst):  # Function definition: even_index_generator
    for i in range(0, len(lst), 2):  # Loop through items
        yield lst[i]

result = list(even_index_generator([1, 2, 3, 4, 5, 6]))  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a generator that yields each word in a sentence, but only those with an even number of characters.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1119
Write a Python program to create a generator that yields each word in a sentence, but only those with an even number of characters.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def even_length_word_generator(sentence):  # Function definition: even_length_word_generator
    words = sentence.split()  # Split string into a list
    for word in words:  # Loop through items
        if len(word) % 2 == 0:  # Conditional check
            yield word

result = list(even_length_word_generator("This is a simple test sentence"))  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a number is positive, negative, or zero. Control flow.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1120
Write a Python program to check if a number is positive, negative, or zero. Control flow.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_number(n):  # Function definition: check_number
    if n > 0:  # Conditional check
        return "Positive"  # Return the result
    elif n < 0:  # Comparison operation
        return "Negative"  # Return the result
    else:
        return "Zero"  # Return the result

result = check_number(5)  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to find the largest of three numbers. Control flow.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1121
Write a Python program to find the largest of three numbers. Control flow.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def largest_of_three(a, b, c):  # Function definition: largest_of_three
    if a >= b and a >= c:  # Conditional check
        return a  # Return the result
    elif b >= a and b >= c:  # Comparison operation
        return b  # Return the result
    else:
        return c  # Return the result

result = largest_of_three(10, 20, 15)  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a given year is a leap year. Control flow.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1122
Write a Python program to check if a given year is a leap year. Control flow.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def is_leap_year(year):  # Function definition: is_leap_year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):  # Conditional check
        return True  # Return the result
    else:
        return False  # Return the result

result = is_leap_year(2024)  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a number is even or odd. Control flow.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1123
Write a Python program to check if a number is even or odd. Control flow.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_even_odd(n):  # Function definition: check_even_odd
    if n % 2 == 0:  # Conditional check
        return "Even"  # Return the result
    else:
        return "Odd"  # Return the result

result = check_even_odd(7)  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a number is divisible by both 3 and 5. Control flow.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1124
Write a Python program to check if a number is divisible by both 3 and 5. Control flow.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def divisible_by_3_and_5(n):  # Function definition: divisible_by_3_and_5
    if n % 3 == 0 and n % 5 == 0:  # Conditional check
        return True  # Return the result
    else:
        return False  # Return the result

result = divisible_by_3_and_5(15)  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to print all numbers from 1 to n that are divisible by 7. Control flow.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1125
Write a Python program to print all numbers from 1 to n that are divisible by 7. Control flow.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def divisible_by_7(n):  # Function definition: divisible_by_7
    for i in range(1, n+1):  # Loop through items
        if i % 7 == 0:  # Conditional check
            print(i)  # Print the result

divisible_by_7(50)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a given number is a prime number. Control flow.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1126
Write a Python program to check if a given number is a prime number. Control flow.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def is_prime(n):  # Function definition: is_prime
    if n < 2:  # Conditional check
        return False  # Return the result
    for i in range(2, int(n**0.5) + 1):  # Loop through items
        if n % i == 0:  # Conditional check
            return False  # Return the result
    return True  # Return the result

result = is_prime(11)  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to find the factorial of a number using recursion. Control flow.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1127
Write a Python program to find the factorial of a number using recursion. Control flow.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def factorial(n):  # Function definition: factorial
    if n == 0 or n == 1:  # Conditional check
        return 1  # Return the result
    return n * factorial(n-1)  # Return the result

result = factorial(5)  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a string is a palindrome. Control flow.
# 
# This problem demonstrates string manipulation and comparison. A palindrome
# is a sequence that reads the same forwards and backwards. This problem
# tests understanding of string operations and logical comparisons.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1128
Write a Python program to check if a string is a palindrome. Control flow.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def is_palindrome(s):  # Function definition: is_palindrome
    if s == s[::-1]:  # Conditional check
        return True  # Return the result
    else:
        return False  # Return the result

result = is_palindrome("madam")  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to count the number of vowels in a given string. Control flow.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1129
Write a Python program to count the number of vowels in a given string. Control flow.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def count_vowels(s):  # Function definition: count_vowels
    vowels = "aeiou"  # Initialize string variable
    count = 0  # Variable assignment
    for char in s:  # Loop through items
        if char.lower() in vowels:  # Conditional check
            count += 1
    return count  # Return the result

result = count_vowels("Hello World")  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a number is a perfect number. Control flow.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1130
Write a Python program to check if a number is a perfect number. Control flow.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def is_perfect_number(n):  # Function definition: is_perfect_number
    divisors = [i for i in range(1, n) if n % i == 0]  # List comprehension: creates a new list
    if sum(divisors) == n:  # Conditional check
        return True  # Return the result
    else:
        return False  # Return the result

result = is_perfect_number(6)  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a number is Armstrong number. Control flow.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1131
Write a Python program to check if a number is Armstrong number. Control flow.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def is_armstrong(n):  # Function definition: is_armstrong
    num_str = str(n)  # Variable assignment
    length = len(num_str)  # Calculate the length
    total = sum(int(digit) ** length for digit in num_str)  # Variable assignment
    if total == n:  # Conditional check
        return True  # Return the result
    else:
        return False  # Return the result

result = is_armstrong(153)  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to print all the prime numbers less than or equal to n. Control flow.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1132
Write a Python program to print all the prime numbers less than or equal to n. Control flow.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def prime_numbers_up_to_n(n):  # Function definition: prime_numbers_up_to_n
    primes = []  # Initialize list
    for num in range(2, n+1):  # Loop through items
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):  # Conditional check
            primes.append(num)  # Method or function call
    return primes  # Return the result

result = prime_numbers_up_to_n(20)  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a number is an even number and greater than 10. Control flow.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1133
Write a Python program to check if a number is an even number and greater than 10. Control flow.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def even_and_greater_than_10(n):  # Function definition: even_and_greater_than_10
    if n % 2 == 0 and n > 10:  # Conditional check
        return True  # Return the result
    else:
        return False  # Return the result

result = even_and_greater_than_10(12)  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to find all the divisors of a number. Control flow.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1134
Write a Python program to find all the divisors of a number. Control flow.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

n = 20  # Variable assignment

for i in range(1, n + 1):  # Loop through items
    if n % i == 0:  # Conditional check
        print(i)  # Print the result

def find_divisors(n):  # Function definition: find_divisors
    divisors = [i for i in range(1, n+1) if n % i == 0]  # List comprehension: creates a new list
    return divisors  # Return the result

result = find_divisors(12)  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to print the multiplication table of a number up to 10. Control flow.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1135
Write a Python program to print the multiplication table of a number up to 10. Control flow.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def multiplication_table(n):  # Function definition: multiplication_table
    for i in range(1, 11):  # Loop through items
        print(f"{n} x {i} = {n*i}")  # Initialize dictionary

multiplication_table(7)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a number is a perfect square. Control flow.
# 
# This problem demonstrates regular expressions (regex) in Python. Regular
# expressions are powerful patterns for matching and manipulating text.
# They allow complex string searches, replacements, and validations.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1136
Write a Python program to check if a number is a perfect square. Control flow.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def is_perfect_square(n):  # Function definition: is_perfect_square
    return int(n**0.5) ** 2 == n  # Return the result

result = is_perfect_square(25)  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a number is a power of 2. Control flow.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1137
Write a Python program to check if a number is a power of 2. Control flow.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def is_power_of_2(n):  # Function definition: is_power_of_2
    return n > 0 and (n & (n - 1)) == 0  # Return the result

result = is_power_of_2(16)  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to find the second largest number in a list. Control flow.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1138
Write a Python program to find the second largest number in a list. Control flow.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def second_largest(lst):  # Function definition: second_largest
    lst = sorted(set(lst), reverse=True)  # Variable assignment
    return lst[1] if len(lst) > 1 else None  # Return the result

result = second_largest([10, 20, 4, 45, 99])  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a given number is a power of 3. Control flow.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1139
Write a Python program to check if a given number is a power of 3. Control flow.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def is_power_of_3(n):  # Function definition: is_power_of_3
    while n % 3 == 0 and n > 0:  # Code block
        n //= 3
    return n == 1  # Return the result

result = is_power_of_3(27)  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to print Fibonacci numbers up to n. Control flow.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1140
Write a Python program to print Fibonacci numbers up to n. Control flow.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def fibonacci_up_to_n(n):  # Function definition: fibonacci_up_to_n
    a, b = 0, 1  # Variable assignment
    while a <= n:  # Code block
        print(a, end=" ")  # Print the result
        a, b = b, a + b  # Variable assignment

fibonacci_up_to_n(20)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to count the occurrences of a specific element in a list. Control flow.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1141
Write a Python program to count the occurrences of a specific element in a list. Control flow.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def count_occurrences(lst, element):  # Function definition: count_occurrences
    return lst.count(element)  # Return the result

result = count_occurrences([1, 2, 2, 3, 4, 2], 2)  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a given number is a perfect square and an Armstrong number. Control flow.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1142
Write a Python program to check if a given number is a perfect square and an Armstrong number. Control flow.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def is_perfect_square_and_armstrong(n):  # Function definition: is_perfect_square_and_armstrong
    if is_perfect_square(n) and is_armstrong(n):  # Conditional check
        return True  # Return the result
    else:
        return False  # Return the result

result = is_perfect_square_and_armstrong(153)  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to find all numbers in a given range that are divisible by 7 and 11. Control flow.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1143
Write a Python program to find all numbers in a given range that are divisible by 7 and 11. Control flow.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def divisible_by_7_and_11(start, end):  # Function definition: divisible_by_7_and_11
    return [num for num in range(start, end+1) if num % 7 == 0 and num % 11 == 0]  # Return the result

result = divisible_by_7_and_11(1, 100)  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to print the factorial of a number using a while loop. Control flow.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1144
Write a Python program to print the factorial of a number using a while loop. Control flow.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def factorial_while(n):  # Function definition: factorial_while
    result = 1  # Variable assignment
    while n > 1:  # Code block
        result *= n
        n -= 1
    return result  # Return the result

result = factorial_while(5)  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to print a list of numbers in reverse order. Control flow.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1145
Write a Python program to print a list of numbers in reverse order. Control flow.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def reverse_list(lst):  # Function definition: reverse_list
    return lst[::-1]  # Return the result

result = reverse_list([1, 2, 3, 4, 5])  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a number is divisible by 5 or 10. Control flow.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1146
Write a Python program to check if a number is divisible by 5 or 10. Control flow.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def divisible_by_5_or_10(n):  # Function definition: divisible_by_5_or_10
    if n % 5 == 0 or n % 10 == 0:  # Conditional check
        return True  # Return the result
    else:
        return False  # Return the result

result = divisible_by_5_or_10(50)  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a number is divisible by any number in a given list. Control flow.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1147
Write a Python program to check if a number is divisible by any number in a given list. Control flow.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def divisible_by_any_number(n, lst):  # Function definition: divisible_by_any_number
    for num in lst:  # Loop through items
        if n % num == 0:  # Conditional check
            return True  # Return the result
    return False  # Return the result

result = divisible_by_any_number(10, [3, 5, 7])  # Variable assignment
print(result)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to demonstrate variable scope in a function. Scope.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1148
Write a Python program to demonstrate variable scope in a function. Scope.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def outer_function():  # Function definition: outer_function
    x = 10  # Local variable  # Variable assignment
    def inner_function():  # Function definition: inner_function
        print(x)  # Accessing the outer function's variable  # Print the result
    inner_function()

outer_function()

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to show the difference between global and local variables. Scope.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1149
Write a Python program to show the difference between global and local variables. Scope.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

x = 20  # Global variable  # Variable assignment

def test_scope():  # Function definition: test_scope
    x = 10  # Local variable  # Variable assignment
    print(f"Local variable: {x}")  # Print the result

test_scope()
print(f"Global variable: {x}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to demonstrate the use of the `global` keyword. Scope.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1150
Write a Python program to demonstrate the use of the `global` keyword. Scope.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def modify_global_variable():  # Function definition: modify_global_variable
    global x
    x = 30  # Modifies the global variable  # Variable assignment

x = 10  # Variable assignment
modify_global_variable()
print(x)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to demonstrate the use of `nonlocal` keyword. Scope.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1151
Write a Python program to demonstrate the use of `nonlocal` keyword. Scope.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def outer_function():  # Function definition: outer_function
    x = 10  # Variable assignment
    def inner_function():  # Function definition: inner_function
        nonlocal x
        x = 20  # Modifies the variable in the outer function's scope  # Variable assignment
    inner_function()
    print(x)  # Print the result

outer_function()

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to demonstrate variable shadowing. Scope.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1152
Write a Python program to demonstrate variable shadowing. Scope.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

x = 100  # Global variable  # Variable assignment

def shadowing_example():  # Function definition: shadowing_example
    x = 50  # Local variable, shadows the global variable  # Variable assignment
    print(f"Local x: {x}")  # Print the result

shadowing_example()
print(f"Global x: {x}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to demonstrate the use of function arguments as local variables. Scope.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1153
Write a Python program to demonstrate the use of function arguments as local variables. Scope.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def example_function(a, b):  # Function definition: example_function
    c = a + b  # c is a local variable  # Variable assignment
    print(f"The sum of {a} and {b} is {c}")  # Print the result

example_function(5, 7)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to demonstrate how to pass a variable as a default argument. Scope.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1154
Write a Python program to demonstrate how to pass a variable as a default argument. Scope.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def greet(name="John"):  # Function definition: greet
    print(f"Hello, {name}!")  # Print the result

greet()  # Uses default value
greet("Alice")  # Uses passed argument

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to show the use of mutable and immutable types in functions. Scope.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1155
Write a Python program to show the use of mutable and immutable types in functions. Scope.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def modify_list(lst):  # Function definition: modify_list
    lst.append(4)  # List is mutable, so it is modified  # Method or function call
    print(f"Modified list: {lst}")  # Print the result

my_list = [1, 2, 3]  # Initialize list
modify_list(my_list)
print(f"Original list: {my_list}")  # Print the result

def modify_integer(n):  # Function definition: modify_integer
    n += 1  # Integer is immutable, so it cannot be modified  # Identity check
    print(f"Modified integer: {n}")  # Print the result

my_int = 5  # Variable assignment
modify_integer(my_int)
print(f"Original integer: {my_int}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to demonstrate the scope of variables in a loop. Scope.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1156
Write a Python program to demonstrate the scope of variables in a loop. Scope.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def loop_scope():  # Function definition: loop_scope
    for i in range(3):  # Loop through items
        x = i  # Variable assignment
        print(f"Inside loop: {x}")  # Print the result
    # x is accessible here after the loop ends
    print(f"Outside loop: {x}")  # Print the result

loop_scope()

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a variable is defined. Scope.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1157
Write a Python program to check if a variable is defined. Scope.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_variable():  # Function definition: check_variable
    try:  # Code block
        print(x)  # Print the result
    except NameError:  # Code block
        print("x is not defined")  # Print the result

check_variable()

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to demonstrate the scope of variables in nested functions. Scope.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1158
Write a Python program to demonstrate the scope of variables in nested functions. Scope.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def outer_function():  # Function definition: outer_function
    x = 10  # Local variable in outer function  # Variable assignment
    def inner_function():  # Function definition: inner_function
        y = 20  # Local variable in inner function  # Variable assignment
        print(f"Inner function: x = {x}, y = {y}")  # Initialize dictionary
    inner_function()
    print(f"Outer function: x = {x}")  # Initialize dictionary

outer_function()

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to demonstrate how to return a variable from a function. Scope.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1159
Write a Python program to demonstrate how to return a variable from a function. Scope.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def add_numbers(a, b):  # Function definition: add_numbers
    sum_result = a + b  # Variable assignment
    return sum_result  # Return the result

result = add_numbers(3, 5)  # Variable assignment
print(f"The sum is {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to explain how default mutable arguments work in functions. Scope.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1160
Write a Python program to explain how default mutable arguments work in functions. Scope.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def append_to_list(n, default_list=[]):  # Function definition: append_to_list
    default_list.append(n)  # Method or function call
    return default_list  # Return the result

# Test the function
print(append_to_list(1))  # [1]  # Print the result
print(append_to_list(2))  # [1, 2]  # Print the result
print(append_to_list(3))  # [1, 2, 3]  # Print the result


def append_to_list(lst=None):  # Function definition: append_to_list
    if lst is None:  # Conditional check
        lst = []  # Initialize list
    lst.append(1)  # Method or function call
    return lst  # Return the result

print(append_to_list())  # Returns [1]  # Print the result
print(append_to_list())  # Returns [1], new list is created each time  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to demonstrate the use of variables in list comprehensions. Scope.
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
Problem: 1161
Write a Python program to demonstrate the use of variables in list comprehensions. Scope.
"""

# SOLUTION EXPLANATION:
# This solution uses a list comprehension to create a new list based on the
# specified conditions. List comprehensions are concise, readable, and often
# more efficient than equivalent loops for creating lists.

def square_numbers(lst):  # Function definition: square_numbers
    return [x**2 for x in lst]  # Return the result

numbers = [1, 2, 3, 4]  # Initialize list
result = square_numbers(numbers)  # Variable assignment
print(f"Squares: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to show the effect of reusing the same variable in a function. Scope.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1162
Write a Python program to show the effect of reusing the same variable in a function. Scope.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def reuse_variable():  # Function definition: reuse_variable
    x = 5  # Variable assignment
    x = x * 2  # Reuses the variable  # Variable assignment
    print(f"New value of x: {x}")  # Print the result

reuse_variable()

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to demonstrate variable scope in different functions. Scope.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1163
Write a Python program to demonstrate variable scope in different functions. Scope.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

x = 50  # Global variable  # Variable assignment

def function_one():  # Function definition: function_one
    print(f"Function One: {x}")  # Print the result

def function_two():  # Function definition: function_two
    x = 40  # Variable assignment
    print(f"Function Two: {x}")  # Print the result

function_one()
function_two()

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to demonstrate the use of `global` for modifying variables in different functions. Scope.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1164
Write a Python program to demonstrate the use of `global` for modifying variables in different functions. Scope.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

x = 10  # Global variable  # Variable assignment

def function_one():  # Function definition: function_one
    global x
    x += 5

def function_two():  # Function definition: function_two
    global x
    x -= 3

function_one()
function_two()
print(f"Global variable x: {x}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to show how variable values are changed in nested functions. Scope.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1165
Write a Python program to show how variable values are changed in nested functions. Scope.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def outer_function():  # Function definition: outer_function
    x = 15  # Local variable in outer function  # Variable assignment
    def inner_function():  # Function definition: inner_function
        nonlocal x
        x += 10  # Modifies x in the outer function's scope
        print(f"Inner function: x = {x}")  # Initialize dictionary
    inner_function()
    print(f"Outer function: x = {x}")  # Initialize dictionary

outer_function()

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to demonstrate the use of variable arguments in functions. Scope.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1166
Write a Python program to demonstrate the use of variable arguments in functions. Scope.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def print_arguments(*args):  # Function definition: print_arguments
    for arg in args:  # Loop through items
        print(arg)  # Print the result

print_arguments(1, 2, 3, "hello", [1, 2, 3])

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to show how the scope of a variable changes in a for loop. Scope.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1167
Write a Python program to show how the scope of a variable changes in a for loop. Scope.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def loop_variable_scope():  # Function definition: loop_variable_scope
    for i in range(3):  # Loop through items
        y = i  # Local variable in the loop  # Variable assignment
        print(f"In the loop: y = {y}")  # Initialize dictionary
    print(f"After the loop: y = {y}")  # y still exists outside the loop  # Initialize dictionary

loop_variable_scope()

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to show the behavior of variables in global scope inside functions. Scope.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1168
Write a Python program to show the behavior of variables in global scope inside functions. Scope.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def global_inside_function():  # Function definition: global_inside_function
    print(f"Global variable x inside function: {x}")  # Print the result

x = 10  # Global variable  # Variable assignment
global_inside_function()

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to explain the difference between mutable and immutable variables in terms of scope. Scope.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1169
Write a Python program to explain the difference between mutable and immutable variables in terms of scope. Scope.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def test_mutability():  # Function definition: test_mutability
    mutable = [1, 2, 3]  # Mutable variable (list)  # Initialize list
    immutable = 10  # Immutable variable (integer)  # Variable assignment

    mutable[0] = 100  # Modifies the mutable variable  # Variable assignment
    immutable = 20  # This does not change the original variable  # Variable assignment

    print(f"Mutable variable: {mutable}")  # Print the result
    print(f"Immutable variable: {immutable}")  # Print the result

test_mutability()

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to show the behavior of variables declared in a list comprehension. Scope.
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
Problem: 1170
Write a Python program to show the behavior of variables declared in a list comprehension. Scope.
"""

# SOLUTION EXPLANATION:
# This solution uses a list comprehension to create a new list based on the
# specified conditions. List comprehensions are concise, readable, and often
# more efficient than equivalent loops for creating lists.

def list_comprehension_variable_scope():  # Function definition: list_comprehension_variable_scope
    lst = [x**2 for x in range(5)]  # List comprehension: creates a new list
    print(f"List comprehension result: {lst}")  # Print the result

list_comprehension_variable_scope()

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to show that function arguments can be variables with different scopes. Scope.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1171
Write a Python program to show that function arguments can be variables with different scopes. Scope.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def print_variable_in_function(x):  # Function definition: print_variable_in_function
    y = x * 2  # Local variable inside function  # Variable assignment
    print(f"Function variable y: {y}")  # Print the result

z = 10  # Global variable  # Variable assignment
print_variable_in_function(z)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to show that a variable in a for loop can be accessed outside the loop. Scope.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1172
Write a Python program to show that a variable in a for loop can be accessed outside the loop. Scope.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def for_loop_variable_scope():  # Function definition: for_loop_variable_scope
    for i in range(3):  # Loop through items
        x = i  # Variable assignment
        print(f"In the loop: x = {x}")  # Initialize dictionary
    print(f"Outside the loop: x = {x}")  # Initialize dictionary

for_loop_variable_scope()

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to demonstrate the impact of changing a global variable inside a function. Scope.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1173
Write a Python program to demonstrate the impact of changing a global variable inside a function. Scope.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

x = 100  # Variable assignment

def change_global_variable():  # Function definition: change_global_variable
    global x
    x = 50  # Variable assignment

change_global_variable()
print(f"Global x after modification: {x}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to demonstrate variable accessibility within different levels of nested functions. Scope.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1174
Write a Python program to demonstrate variable accessibility within different levels of nested functions. Scope.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def outer_function():  # Function definition: outer_function
    x = 5  # Variable assignment
    def middle_function():  # Function definition: middle_function
        y = 10  # Variable assignment
        def inner_function():  # Function definition: inner_function
            z = 15  # Variable assignment
            print(f"Inner function: x = {x}, y = {y}, z = {z}")  # Initialize dictionary
        inner_function()
    middle_function()

outer_function()

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to demonstrate how function arguments can access global variables. Scope.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1175
Write a Python program to demonstrate how function arguments can access global variables. Scope.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

x = 100  # Variable assignment

def print_global_variable(x):  # Function definition: print_global_variable
    print(f"Global x inside function: {x}")  # Print the result

print_global_variable(x)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to demonstrate the scope of variables in a recursive function. Scope.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1176
Write a Python program to demonstrate the scope of variables in a recursive function. Scope.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def factorial_recursive(n):  # Function definition: factorial_recursive
    if n == 1:  # Conditional check
        return 1  # Return the result
    else:
        return n * factorial_recursive(n - 1)  # Return the result

result = factorial_recursive(5)  # Variable assignment
print(f"Factorial: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to import the `math` module and calculate the square root of a number. Module.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1177
Write a Python program to import the `math` module and calculate the square root of a number. Module.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

import math  # Import module or function

def calculate_square_root(number):  # Function definition: calculate_square_root
    return math.sqrt(number)  # Return the result

result = calculate_square_root(16)  # Variable assignment
print(f"The square root of 16 is {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to use the `random` module to generate a random number between 1 and 100. Module.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1178
Write a Python program to use the `random` module to generate a random number between 1 and 100. Module.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

import random  # Import module or function

def generate_random_number():  # Function definition: generate_random_number
    return random.randint(1, 100)  # Return the result

random_number = generate_random_number()  # Variable assignment
print(f"Random number between 1 and 100: {random_number}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to use the `datetime` module to get the current date and time. Module.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1179
Write a Python program to use the `datetime` module to get the current date and time. Module.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

import datetime  # Import module or function

def current_datetime():  # Function definition: current_datetime
    return datetime.datetime.now()  # Return the result

now = current_datetime()  # Variable assignment
print(f"Current date and time: {now}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to use the `os` module to get the current working directory. Module.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1180
Write a Python program to use the `os` module to get the current working directory. Module.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

import os  # Import module or function

def current_working_directory():  # Function definition: current_working_directory
    return os.getcwd()  # Return the result

cwd = current_working_directory()  # Variable assignment
print(f"Current working directory: {cwd}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to use the `sys` module to get the Python version. Module.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1181
Write a Python program to use the `sys` module to get the Python version. Module.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

import sys  # Import module or function

def python_version():  # Function definition: python_version
    return sys.version  # Return the result

version = python_version()  # Variable assignment
print(f"Python version: {version}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to use the `json` module to convert a Python dictionary to a JSON string. Module.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1182
Write a Python program to use the `json` module to convert a Python dictionary to a JSON string. Module.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

import json  # Import module or function

def dict_to_json():  # Function definition: dict_to_json
    sample_dict = {"name": "Alice", "age": 30}  # Initialize dictionary
    return json.dumps(sample_dict)  # Return the result

json_str = dict_to_json()  # Variable assignment
print(f"JSON string: {json_str}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to use the `re` module to check if a string contains a number. Module.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1183
Write a Python program to use the `re` module to check if a string contains a number. Module.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

import re  # Import module or function

def contains_number(string):  # Function definition: contains_number
    return bool(re.search(r'\d', string))  # Return the result

result = contains_number("Hello123")  # Variable assignment
print(f"Does the string contain a number? {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to use the `os` module to list all files in a directory. Module.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1184
Write a Python program to use the `os` module to list all files in a directory. Module.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

import os  # Import module or function

def list_files(directory):  # Function definition: list_files
    return os.listdir(directory)  # Return the result

files = list_files(".")  # Variable assignment
print(f"Files in the current directory: {files}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to use the `math` module to calculate the factorial of a number. Module.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1185
Write a Python program to use the `math` module to calculate the factorial of a number. Module.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

import math  # Import module or function

def calculate_factorial(number):  # Function definition: calculate_factorial
    return math.factorial(number)  # Return the result

factorial_result = calculate_factorial(5)  # Variable assignment
print(f"The factorial of 5 is {factorial_result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to use the `time` module to measure the execution time of a block of code. Module.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1186
Write a Python program to use the `time` module to measure the execution time of a block of code. Module.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

import time  # Import module or function

def measure_time():  # Function definition: measure_time
    start_time = time.time()  # Variable assignment
    sum(range(1000000))
    end_time = time.time()  # Variable assignment
    return end_time - start_time  # Return the result

execution_time = measure_time()  # Variable assignment
print(f"Execution time: {execution_time} seconds")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to use the `calendar` module to check if a year is a leap year. Module.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1187
Write a Python program to use the `calendar` module to check if a year is a leap year. Module.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

import calendar  # Import module or function

def is_leap_year(year):  # Function definition: is_leap_year
    return calendar.isleap(year)  # Return the result

result = is_leap_year(2024)  # Variable assignment
print(f"Is 2024 a leap year? {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to use the `math` module to find the value of pi. Module.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1188
Write a Python program to use the `math` module to find the value of pi. Module.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

import math  # Import module or function

def get_pi_value():  # Function definition: get_pi_value
    return math.pi  # Return the result

pi_value = get_pi_value()  # Variable assignment
print(f"The value of pi is {pi_value}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to use the `random` module to shuffle a list of numbers. Module.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1189
Write a Python program to use the `random` module to shuffle a list of numbers. Module.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

import random  # Import module or function

def shuffle_list(lst):  # Function definition: shuffle_list
    random.shuffle(lst)  # Method or function call
    return lst  # Return the result

numbers = [1, 2, 3, 4, 5]  # Initialize list
shuffled_numbers = shuffle_list(numbers)  # Variable assignment
print(f"Shuffled list: {shuffled_numbers}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to use the `collections` module to count the occurrences of elements in a list. Module.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1190
Write a Python program to use the `collections` module to count the occurrences of elements in a list. Module.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

import collections  # Import module or function

def count_occurrences(lst):  # Function definition: count_occurrences
    return collections.Counter(lst)  # Return the result

numbers = [1, 2, 2, 3, 3, 3]  # Initialize list
occurrences = count_occurrences(numbers)  # Variable assignment
print(f"Occurrences: {occurrences}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to use the `math` module to calculate the greatest common divisor (GCD) of two numbers. Module.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1191
Write a Python program to use the `math` module to calculate the greatest common divisor (GCD) of two numbers. Module.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

import math  # Import module or function

def calculate_gcd(a, b):  # Function definition: calculate_gcd
    return math.gcd(a, b)  # Return the result

gcd_result = calculate_gcd(48, 180)  # Variable assignment
print(f"The GCD of 48 and 180 is {gcd_result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to use the `os` module to rename a file. Module.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1192
Write a Python program to use the `os` module to rename a file. Module.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

import os  # Import module or function

def rename_file(old_name, new_name):  # Function definition: rename_file
    os.rename(old_name, new_name)  # Method or function call

# Uncomment the following lines to test the rename_file function:
rename_file("old_file.txt", "new_file.txt")  # Method or function call

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to use the `datetime` module to format the current date. Module.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1193
Write a Python program to use the `datetime` module to format the current date. Module.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

import datetime  # Import module or function

def format_current_date():  # Function definition: format_current_date
    return datetime.datetime.now().strftime("%Y-%m-%d")  # Return the result

formatted_date = format_current_date()  # Variable assignment
print(f"Formatted current date: {formatted_date}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to use the `json` module to parse a JSON string into a Python dictionary. Module.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1194
Write a Python program to use the `json` module to parse a JSON string into a Python dictionary. Module.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

import json  # Import module or function

def json_to_dict(json_str):  # Function definition: json_to_dict
    return json.loads(json_str)  # Return the result

json_str = '{"name": "Bob", "age": 25}'  # Initialize string variable
parsed_dict = json_to_dict(json_str)  # Variable assignment
print(f"Parsed dictionary: {parsed_dict}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to use the `random` module to select a random element from a list. Module.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1195
Write a Python program to use the `random` module to select a random element from a list. Module.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

import random  # Import module or function

def select_random_element(lst):  # Function definition: select_random_element
    return random.choice(lst)  # Return the result

elements = [10, 20, 30, 40]  # Initialize list
random_element = select_random_element(elements)  # Variable assignment
print(f"Random element: {random_element}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to use the `math` module to round a floating-point number to the nearest integer. Module.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1196
Write a Python program to use the `math` module to round a floating-point number to the nearest integer. Module.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

import math  # Import module or function

def round_number(number):  # Function definition: round_number
    return round(number)  # Return the result

rounded_value = round_number(7.5)  # Variable assignment
print(f"Rounded value of 7.5: {rounded_value}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a dictionary and access its value using a key. Dictionary operations.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1197
Write a Python program to create a dictionary and access its value using a key. Dictionary operations.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def access_value():  # Function definition: access_value
    sample_dict = {"name": "Alice", "age": 30}  # Initialize dictionary
    return sample_dict["name"]  # Return the result

result = access_value()  # Variable assignment
print(f"Value accessed: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to add a key-value pair to an existing dictionary. Dictionary operations.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1198
Write a Python program to add a key-value pair to an existing dictionary. Dictionary operations.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def add_key_value():  # Function definition: add_key_value
    sample_dict = {"name": "Alice", "age": 30}  # Initialize dictionary
    sample_dict["city"] = "New York"  # Initialize string variable
    return sample_dict  # Return the result

updated_dict = add_key_value()  # Variable assignment
print(f"Updated dictionary: {updated_dict}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to remove a key-value pair from a dictionary. Dictionary operations.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1199
Write a Python program to remove a key-value pair from a dictionary. Dictionary operations.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def remove_key():  # Function definition: remove_key
    sample_dict = {"name": "Alice", "age": 30, "city": "New York"}  # Initialize dictionary
    del sample_dict["city"]
    return sample_dict  # Return the result

updated_dict = remove_key()  # Variable assignment
print(f"Dictionary after removal: {updated_dict}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to get all the keys from a dictionary. Dictionary operations.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1200
Write a Python program to get all the keys from a dictionary. Dictionary operations.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def get_keys():  # Function definition: get_keys
    sample_dict = {"name": "Alice", "age": 30, "city": "New York"}  # Initialize dictionary
    return sample_dict.keys()  # Return the result

keys = get_keys()  # Variable assignment
print(f"Keys in dictionary: {keys}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to get all the values from a dictionary. Dictionary operations.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1201
Write a Python program to get all the values from a dictionary. Dictionary operations.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def get_values():  # Function definition: get_values
    sample_dict = {"name": "Alice", "age": 30, "city": "New York"}  # Initialize dictionary
    return sample_dict.values()  # Return the result

values = get_values()  # Variable assignment
print(f"Values in dictionary: {values}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a key exists in a dictionary. Dictionary operations.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1202
Write a Python program to check if a key exists in a dictionary. Dictionary operations.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_key():  # Function definition: check_key
    sample_dict = {"name": "Alice", "age": 30, "city": "New York"}  # Initialize dictionary
    return "age" in sample_dict  # Return the result

result = check_key()  # Variable assignment
print(f"Key exists: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to get the value associated with a key, or return a default value if the key doesn't exist. Dictionary operations.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1203
Write a Python program to get the value associated with a key, or return a default value if the key doesn't exist. Dictionary operations.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def get_value(dictionary, key, default=None):  # Function definition: get_value

    return dictionary.get(key, default)  # Return the result

# Example usage:
my_dict = {'a': 1, 'b': 2, 'c': 3}  # Initialize dictionary
print(get_value(my_dict, 'a'))  # Output: 1  # Print the result
print(get_value(my_dict, 'd', 'not found'))  # Output: not found  # Print the result

def get_value_or_default():  # Function definition: get_value_or_default
    sample_dict = {"name": "Alice", "age": 30}  # Initialize dictionary
    return sample_dict.get("city", "Unknown")  # Return the result

result = get_value_or_default()  # Variable assignment
print(f"Value: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to clear all items from a dictionary. Dictionary operations.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1204
Write a Python program to clear all items from a dictionary. Dictionary operations.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def clear_dict():  # Function definition: clear_dict
    sample_dict = {"name": "Alice", "age": 30, "city": "New York"}  # Initialize dictionary
    sample_dict.clear()  # Method or function call
    return sample_dict  # Return the result

updated_dict = clear_dict()  # Variable assignment
print(f"Dictionary after clearing: {updated_dict}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to copy a dictionary. Dictionary operations.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1205
Write a Python program to copy a dictionary. Dictionary operations.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def copy_dict():  # Function definition: copy_dict
    sample_dict = {"name": "Alice", "age": 30}  # Initialize dictionary
    return sample_dict.copy()  # Return the result

copied_dict = copy_dict()  # Variable assignment
print(f"Copied dictionary: {copied_dict}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to merge two dictionaries. Dictionary operations.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1206
Write a Python program to merge two dictionaries. Dictionary operations.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def merge_dicts():  # Function definition: merge_dicts
    dict1 = {"name": "Alice", "age": 30}  # Initialize dictionary
    dict2 = {"city": "New York", "job": "Engineer"}  # Initialize dictionary
    dict1.update(dict2)  # Method or function call
    return dict1  # Return the result

merged_dict = merge_dicts()  # Variable assignment
print(f"Merged dictionary: {merged_dict}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to iterate through all key-value pairs in a dictionary. Dictionary operations.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1207
Write a Python program to iterate through all key-value pairs in a dictionary. Dictionary operations.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def iterate_dict():  # Function definition: iterate_dict
    sample_dict = {"name": "Alice", "age": 30, "city": "New York"}  # Initialize dictionary
    for key, value in sample_dict.items():  # Loop through items
        print(f"{key}: {value}")  # Print the result

iterate_dict()

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to find the length of a dictionary. Dictionary operations.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1208
Write a Python program to find the length of a dictionary. Dictionary operations.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def dict_length():  # Function definition: dict_length
    sample_dict = {"name": "Alice", "age": 30, "city": "New York"}  # Initialize dictionary
    return len(sample_dict)  # Return the result

length = dict_length()  # Variable assignment
print(f"Length of dictionary: {length}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to reverse the keys and values in a dictionary. Dictionary operations.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1209
Write a Python program to reverse the keys and values in a dictionary. Dictionary operations.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def reverse_dict():  # Function definition: reverse_dict
    sample_dict = {"name": "Alice", "age": 30, "city": "New York"}  # Initialize dictionary
    return {v: k for k, v in sample_dict.items()}  # Return the result

reversed_dict = reverse_dict()  # Variable assignment
print(f"Reversed dictionary: {reversed_dict}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a dictionary from two lists, one for keys and one for values. Dictionary operations.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1210
Write a Python program to create a dictionary from two lists, one for keys and one for values. Dictionary operations.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def create_dict_from_lists():  # Function definition: create_dict_from_lists
    keys = ["name", "age", "city"]  # Initialize list
    values = ["Alice", 30, "New York"]  # Initialize list
    return dict(zip(keys, values))  # Return the result

created_dict = create_dict_from_lists()  # Variable assignment
print(f"Created dictionary: {created_dict}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to get the sum of all values in a dictionary. Dictionary operations.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1211
Write a Python program to get the sum of all values in a dictionary. Dictionary operations.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def sum_values():  # Function definition: sum_values
    sample_dict = {"a": 10, "b": 20, "c": 30}  # Initialize dictionary
    return sum(sample_dict.values())  # Return the result

total = sum_values()  # Variable assignment
print(f"Sum of values: {total}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to filter a dictionary based on a condition. Dictionary operations.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1212
Write a Python program to filter a dictionary based on a condition. Dictionary operations.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def filter_dict():  # Function definition: filter_dict
    sample_dict = {"name": "Alice", "age": 30, "city": "New York"}  # Initialize dictionary
    return {key: value for key, value in sample_dict.items() if isinstance(value, str)}  # Return the result

filtered_dict = filter_dict()  # Variable assignment
print(f"Filtered dictionary: {filtered_dict}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to find the maximum value in a dictionary. Dictionary operations.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1213
Write a Python program to find the maximum value in a dictionary. Dictionary operations.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def max_value():  # Function definition: max_value
    sample_dict = {"a": 10, "b": 20, "c": 30}  # Initialize dictionary
    return max(sample_dict.values())  # Return the result

max_val = max_value()  # Variable assignment
print(f"Maximum value: {max_val}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a dictionary is empty. Dictionary operations.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1214
Write a Python program to check if a dictionary is empty. Dictionary operations.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def is_dict_empty():  # Function definition: is_dict_empty
    sample_dict = {}  # Initialize dictionary
    return len(sample_dict) == 0  # Return the result

result = is_dict_empty()  # Variable assignment
print(f"Is dictionary empty? {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to remove all occurrences of a value in a dictionary. Dictionary operations.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1215
Write a Python program to remove all occurrences of a value in a dictionary. Dictionary operations.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def remove_value():  # Function definition: remove_value
    sample_dict = {"a": 10, "b": 20, "c": 10}  # Initialize dictionary
    sample_dict = {k: v for k, v in sample_dict.items() if v != 10}  # Initialize dictionary
    return sample_dict  # Return the result

updated_dict = remove_value()  # Variable assignment
print(f"Dictionary after removal: {updated_dict}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to find the key associated with a given value in a dictionary. Dictionary operations.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1216
Write a Python program to find the key associated with a given value in a dictionary. Dictionary operations.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def find_key_by_value():  # Function definition: find_key_by_value
    sample_dict = {"a": 10, "b": 20, "c": 30}  # Initialize dictionary
    return [k for k, v in sample_dict.items() if v == 20]  # Return the result

key = find_key_by_value()  # Variable assignment
print(f"Key for value 20: {key}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a dictionary with default values using `defaultdict`. Dictionary operations.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1217
Write a Python program to create a dictionary with default values using `defaultdict`. Dictionary operations.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

from collections import defaultdict  # Import module or function

def create_defaultdict():  # Function definition: create_defaultdict
    sample_dict = defaultdict(int)  # Variable assignment
    sample_dict["a"] += 1
    sample_dict["b"] += 2
    return dict(sample_dict)  # Return the result

default_dict = create_defaultdict()  # Variable assignment
print(f"Default dictionary: {default_dict}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to get the first key-value pair from a dictionary. Dictionary operations.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1218
Write a Python program to get the first key-value pair from a dictionary. Dictionary operations.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def first_key_value():  # Function definition: first_key_value
    sample_dict = {"a": 10, "b": 20, "c": 30}  # Initialize dictionary
    first_item = list(sample_dict.items())[0]  # Variable assignment
    return first_item  # Return the result

first_item = first_key_value()  # Variable assignment
print(f"First key-value pair: {first_item}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to merge multiple dictionaries into one. Dictionary operations.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1219
Write a Python program to merge multiple dictionaries into one. Dictionary operations.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def merge_multiple_dicts():  # Function definition: merge_multiple_dicts
    dict1 = {"a": 10, "b": 20}  # Initialize dictionary
    dict2 = {"c": 30, "d": 40}  # Initialize dictionary
    dict3 = {"e": 50}  # Initialize dictionary
    merged_dict = {**dict1, **dict2, **dict3}  # Initialize dictionary
    return merged_dict  # Return the result

merged_dict = merge_multiple_dicts()  # Variable assignment
print(f"Merged dictionary: {merged_dict}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to convert a list of tuples into a dictionary. Dictionary operations.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1220
Write a Python program to convert a list of tuples into a dictionary. Dictionary operations.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def list_to_dict():  # Function definition: list_to_dict
    sample_list = [("a", 1), ("b", 2), ("c", 3)]  # Initialize list
    return dict(sample_list)  # Return the result

converted_dict = list_to_dict()  # Variable assignment
print(f"Converted dictionary: {converted_dict}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a Path object using the `pathlib` module.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1221
Write a Python program to create a Path object using the `pathlib` module.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

from pathlib import Path  # Import module or function

def create_path():  # Function definition: create_path
    p = Path("example_directory")  # Variable assignment
    return p  # Return the result

path = create_path()  # Variable assignment
print(f"Created path: {path}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a path exists using `pathlib`.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1222
Write a Python program to check if a path exists using `pathlib`.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

from pathlib import Path  # Import module or function

def check_path_exists():  # Function definition: check_path_exists
    p = Path("example_directory")  # Variable assignment
    return p.exists()  # Return the result

exists = check_path_exists()  # Variable assignment
print(f"Path exists: {exists}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a path is a file using `pathlib`.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1223
Write a Python program to check if a path is a file using `pathlib`.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

from pathlib import Path  # Import module or function

def check_if_file():  # Function definition: check_if_file
    p = Path("example_file.txt")  # Variable assignment
    return p.is_file()  # Return the result

is_file = check_if_file()  # Variable assignment
print(f"Is it a file? {is_file}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a path is a directory using `pathlib`.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1224
Write a Python program to check if a path is a directory using `pathlib`.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

from pathlib import Path  # Import module or function

def check_if_directory():  # Function definition: check_if_directory
    p = Path("example_directory")  # Variable assignment
    return p.is_dir()  # Return the result

is_directory = check_if_directory()  # Variable assignment
print(f"Is it a directory? {is_directory}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to get the file name from a path using `pathlib`.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1225
Write a Python program to get the file name from a path using `pathlib`.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

from pathlib import Path  # Import module or function

def get_file_name():  # Function definition: get_file_name
    p = Path("example_directory/example_file.txt")  # Variable assignment
    return p.name  # Return the result

file_name = get_file_name()  # Variable assignment
print(f"File name: {file_name}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to get the parent directory of a path using `pathlib`.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1226
Write a Python program to get the parent directory of a path using `pathlib`.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

from pathlib import Path  # Import module or function

def get_parent_directory():  # Function definition: get_parent_directory
    p = Path("example_directory/example_file.txt")  # Variable assignment
    return p.parent  # Return the result

parent_directory = get_parent_directory()  # Variable assignment
print(f"Parent directory: {parent_directory}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to join two paths using `pathlib`.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1227
Write a Python program to join two paths using `pathlib`.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

from pathlib import Path  # Import module or function

def join_paths():  # Function definition: join_paths
    p1 = Path("example_directory")  # Variable assignment
    p2 = "example_file.txt"  # Initialize string variable
    return p1 / p2  # Return the result

joined_path = join_paths()  # Variable assignment
print(f"Joined path: {joined_path}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to get the file extension of a path using `pathlib`.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1228
Write a Python program to get the file extension of a path using `pathlib`.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

from pathlib import Path  # Import module or function

def get_file_extension():  # Function definition: get_file_extension
    p = Path("example_file.txt")  # Variable assignment
    return p.suffix  # Return the result

file_extension = get_file_extension()  # Variable assignment
print(f"File extension: {file_extension}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to get the size of a file using `pathlib`.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1229
Write a Python program to get the size of a file using `pathlib`.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

from pathlib import Path  # Import module or function

def get_file_size():  # Function definition: get_file_size
    p = Path("example_file.txt")  # Variable assignment
    return p.stat().st_size  # Return the result

file_size = get_file_size()  # Variable assignment
print(f"File size: {file_size} bytes")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to rename a file using `pathlib`.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1230
Write a Python program to rename a file using `pathlib`.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

from pathlib import Path  # Import module or function

def rename_file():  # Function definition: rename_file
    old_path = Path("old_file.txt")  # Variable assignment
    new_path = Path("new_file.txt")  # Variable assignment
    old_path.rename(new_path)  # Method or function call
    return new_path  # Return the result

renamed_file = rename_file()  # Variable assignment
print(f"Renamed file: {renamed_file}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a new directory using `pathlib`.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1231
Write a Python program to create a new directory using `pathlib`.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

from pathlib import Path  # Import module or function

def create_directory():  # Function definition: create_directory
    p = Path("new_directory")  # Variable assignment
    p.mkdir(parents=True, exist_ok=True)
    return p  # Return the result

created_directory = create_directory()  # Variable assignment
print(f"Created directory: {created_directory}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to remove a directory using `pathlib`.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1232
Write a Python program to remove a directory using `pathlib`.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

from pathlib import Path  # Import module or function

def remove_directory():  # Function definition: remove_directory
    p = Path("new_directory")  # Variable assignment
    p.rmdir()  # Method or function call
    return f"Directory {p} removed"  # Return the result

removed_directory = remove_directory()  # Variable assignment
print(removed_directory)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to remove a file using `pathlib`.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1233
Write a Python program to remove a file using `pathlib`.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

from pathlib import Path  # Import module or function

def remove_file():  # Function definition: remove_file
    p = Path("example_file.txt")  # Variable assignment
    p.unlink()  # Method or function call
    return f"File {p} removed"  # Return the result

removed_file = remove_file()  # Variable assignment
print(removed_file)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to get the absolute path of a file using `pathlib`.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1234
Write a Python program to get the absolute path of a file using `pathlib`.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

from pathlib import Path  # Import module or function

def get_absolute_path():  # Function definition: get_absolute_path
    p = Path("example_file.txt")  # Variable assignment
    return p.resolve()  # Return the result

absolute_path = get_absolute_path()  # Variable assignment
print(f"Absolute path: {absolute_path}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a path is a symbolic link using `pathlib`.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1235
Write a Python program to check if a path is a symbolic link using `pathlib`.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

from pathlib import Path  # Import module or function

def check_if_symlink():  # Function definition: check_if_symlink
    p = Path("example_symlink")  # Variable assignment
    return p.is_symlink()  # Return the result

is_symlink = check_if_symlink()  # Variable assignment
print(f"Is it a symbolic link? {is_symlink}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to create a symbolic link using `pathlib`.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1236
Write a Python program to create a symbolic link using `pathlib`.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

from pathlib import Path  # Import module or function

def create_symlink():  # Function definition: create_symlink
    target = Path("example_file.txt")  # Variable assignment
    symlink = Path("example_symlink")  # Variable assignment
    symlink.symlink_to(target)  # Method or function call
    return symlink  # Return the result

symlink = create_symlink()  # Variable assignment
print(f"Created symlink: {symlink}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a path is a directory and if it contains files using `pathlib`.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1237
Write a Python program to check if a path is a directory and if it contains files using `pathlib`.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

from pathlib import Path  # Import module or function

def check_directory_and_files():  # Function definition: check_directory_and_files
    p = Path("example_directory")  # Variable assignment
    if p.is_dir():  # Conditional check
        return [file.name for file in p.iterdir()]  # Return the result
    return []  # Return the result

directory_files = check_directory_and_files()  # Variable assignment
print(f"Files in directory: {directory_files}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to get the last modified time of a file using `pathlib`.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1238
Write a Python program to get the last modified time of a file using `pathlib`.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

from pathlib import Path  # Import module or function
import time  # Import module or function

def get_last_modified_time():  # Function definition: get_last_modified_time
    p = Path("example_file.txt")  # Variable assignment
    timestamp = p.stat().st_mtime  # Variable assignment
    return time.ctime(timestamp)  # Return the result

last_modified_time = get_last_modified_time()  # Variable assignment
print(f"Last modified time: {last_modified_time}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to get the directory name from a path using `pathlib`.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1239
Write a Python program to get the directory name from a path using `pathlib`.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

from pathlib import Path  # Import module or function

def get_directory_name():  # Function definition: get_directory_name
    p = Path("example_directory/example_file.txt")  # Variable assignment
    return p.parent.name  # Return the result

directory_name = get_directory_name()  # Variable assignment
print(f"Directory name: {directory_name}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a path is empty (no files) using `pathlib`.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1240
Write a Python program to check if a path is empty (no files) using `pathlib`.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

from pathlib import Path  # Import module or function

def check_if_empty():  # Function definition: check_if_empty
    p = Path("example_directory")  # Variable assignment
    return len(list(p.iterdir())) == 0  # Return the result

is_empty = check_if_empty()  # Variable assignment
print(f"Is directory empty? {is_empty}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to iterate over all files in a directory using `pathlib`.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1241
Write a Python program to iterate over all files in a directory using `pathlib`.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

from pathlib import Path  # Import module or function

def iterate_files():  # Function definition: iterate_files
    p = Path("example_directory")  # Variable assignment
    return [file.name for file in p.iterdir() if file.is_file()]  # Return the result

files_in_directory = iterate_files()  # Variable assignment
print(f"Files in directory: {files_in_directory}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to find the path to the parent directory using `pathlib`.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1242
Write a Python program to find the path to the parent directory using `pathlib`.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

from pathlib import Path  # Import module or function

def get_parent_directory():  # Function definition: get_parent_directory
    p = Path("example_directory/example_file.txt")  # Variable assignment
    return p.parent.parent  # Return the result

parent_directory = get_parent_directory()  # Variable assignment
print(f"Parent directory: {parent_directory}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a file has a certain extension using `pathlib`.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1243
Write a Python program to check if a file has a certain extension using `pathlib`.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

from pathlib import Path  # Import module or function

def check_file_extension():  # Function definition: check_file_extension
    p = Path("example_file.txt")  # Variable assignment
    return p.suffix == ".txt"  # Return the result

has_extension = check_file_extension()  # Variable assignment
print(f"Has .txt extension? {has_extension}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to get the file size using `pathlib` in human-readable format.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1244
Write a Python program to get the file size using `pathlib` in human-readable format.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

from pathlib import Path  # Import module or function

def get_human_readable_size():  # Function definition: get_human_readable_size
    p = Path("example_file.txt")  # Variable assignment
    size_in_bytes = p.stat().st_size  # Variable assignment
    return f"{size_in_bytes / 1024:.2f} KB"  # Return the result

size = get_human_readable_size()  # Variable assignment
print(f"File size: {size}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to change the current working directory using `pathlib`.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1245
Write a Python program to change the current working directory using `pathlib`.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

from pathlib import Path  # Import module or function

def change_working_directory():  # Function definition: change_working_directory
    p = Path("example_directory")  # Variable assignment
    p.chdir()  # Method or function call
    return f"Changed working directory to: {p}"  # Return the result

changed_directory = change_working_directory()  # Variable assignment
print(changed_directory)  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if two conditions are true using the `and` operator.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1246
Write a Python program to check if two conditions are true using the `and` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_conditions():  # Function definition: check_conditions
    a = 5  # Variable assignment
    b = 10  # Variable assignment
    return a > 3 and b < 15  # Return the result

result = check_conditions()  # Variable assignment
print(f"Both conditions are true: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a number is between 10 and 20 (both inclusive) using the `and` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1247
Write a Python program to check if a number is between 10 and 20 (both inclusive) using the `and` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_range():  # Function definition: check_range
    num = 15  # Variable assignment
    return num >= 10 and num <= 20  # Return the result

result = check_range()  # Variable assignment: create a range
print(f"Number is between 10 and 20: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a string is non-empty and contains a specific character using the `and` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1248
Write a Python program to check if a string is non-empty and contains a specific character using the `and` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_string():  # Function definition: check_string
    text = "hello"  # Initialize string variable
    return len(text) > 0 and "e" in text  # Return the result

result = check_string()  # Variable assignment
print(f"String is non-empty and contains 'e': {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a number is divisible by both 3 and 5 using the `and` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1249
Write a Python program to check if a number is divisible by both 3 and 5 using the `and` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def main(number):  # Function definition: main
    return True if number % 3 == 0 and number % 5 == 0 else False  # Return the result

number = 15  # Variable assignment
main(number)

def check_divisibility():  # Function definition: check_divisibility
    num = 15  # Variable assignment
    return num % 3 == 0 and num % 5 == 0  # Return the result

result = check_divisibility()  # Variable assignment
print(f"Number is divisible by both 3 and 5: {result}")  # Print the result

def main(number):  # Function definition: main
    return number % 3 == 0 and number % 5 == 0  # Return the result

number = 15  # Variable assignment
main(number)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a list is non-empty and the first element is greater than 5 using the `and` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1250
Write a Python program to check if a list is non-empty and the first element is greater than 5 using the `and` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_list():  # Function definition: check_list
    lst = [6, 2, 8]  # Initialize list
    return len(lst) > 0 and lst[0] > 5  # Return the result

result = check_list()  # Variable assignment
print(f"List is non-empty and first element is greater than 5: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a year is a leap year using the `and` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1251
Write a Python program to check if a year is a leap year using the `and` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_leap_year():  # Function definition: check_leap_year
    year = 2024  # Variable assignment
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)  # Return the result

result = check_leap_year()  # Variable assignment
print(f"Year is a leap year: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a number is positive, even, and divisible by 4 using the `and` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1252
Write a Python program to check if a number is positive, even, and divisible by 4 using the `and` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_number():  # Function definition: check_number
    num = 8  # Variable assignment
    return num > 0 and num % 2 == 0 and num % 4 == 0  # Return the result

result = check_number()  # Variable assignment
print(f"Number is positive, even, and divisible by 4: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a list contains exactly three elements, and the first element is greater than 5 using the `and` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1253
Write a Python program to check if a list contains exactly three elements, and the first element is greater than 5 using the `and` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_list_conditions():  # Function definition: check_list_conditions
    lst = [6, 2, 8]  # Initialize list
    return len(lst) == 3 and lst[0] > 5  # Return the result

result = check_list_conditions()  # Variable assignment
print(f"List has three elements and first is greater than 5: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a string is lowercase and its length is greater than 3 using the `and` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1254
Write a Python program to check if a string is lowercase and its length is greater than 3 using the `and` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_string_conditions():  # Function definition: check_string_conditions
    text = "hello"  # Initialize string variable
    return text.islower() and len(text) > 3  # Return the result

result = check_string_conditions()  # Variable assignment
print(f"String is lowercase and its length is greater than 3: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a number is greater than 10 and less than 50 using the `and` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1255
Write a Python program to check if a number is greater than 10 and less than 50 using the `and` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_range_conditions():  # Function definition: check_range_conditions
    num = 30  # Variable assignment
    return num > 10 and num < 50  # Return the result

result = check_range_conditions()  # Variable assignment
print(f"Number is between 10 and 50: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a number is both a multiple of 7 and 11 using the `and` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1256
Write a Python program to check if a number is both a multiple of 7 and 11 using the `and` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_multiples():  # Function definition: check_multiples
    num = 77  # Variable assignment
    return num % 7 == 0 and num % 11 == 0  # Return the result

result = check_multiples()  # Variable assignment
print(f"Number is a multiple of both 7 and 11: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a person is eligible to vote, meaning the age is greater than 18 and they are a citizen, using the `and` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1257
Write a Python program to check if a person is eligible to vote, meaning the age is greater than 18 and they are a citizen, using the `and` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_voting_eligibility():  # Function definition: check_voting_eligibility
    age = 20  # Variable assignment
    is_citizen = True  # Variable assignment
    return age > 18 and is_citizen  # Return the result

result = check_voting_eligibility()  # Variable assignment
print(f"Person is eligible to vote: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a number is divisible by 2, 3, and 5 using the `and` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1258
Write a Python program to check if a number is divisible by 2, 3, and 5 using the `and` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_divisibility_all():  # Function definition: check_divisibility_all
    num = 30  # Variable assignment
    return num % 2 == 0 and num % 3 == 0 and num % 5 == 0  # Return the result

result = check_divisibility_all()  # Variable assignment
print(f"Number is divisible by 2, 3, and 5: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a dictionary contains a specific key and the value is greater than a specified number using the `and` operator.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1259
Write a Python program to check if a dictionary contains a specific key and the value is greater than a specified number using the `and` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_dict_conditions():  # Function definition: check_dict_conditions
    sample_dict = {"age": 30, "city": "New York"}  # Initialize dictionary
    return "age" in sample_dict and sample_dict["age"] > 25  # Return the result

result = check_dict_conditions()  # Variable assignment
print(f"Dictionary contains 'age' and its value is greater than 25: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a string is not empty and its length is an even number using the `and` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1260
Write a Python program to check if a string is not empty and its length is an even number using the `and` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_string_length():  # Function definition: check_string_length
    text = "hello"  # Initialize string variable
    return len(text) > 0 and len(text) % 2 == 0  # Return the result

result = check_string_length()  # Variable assignment
print(f"String is not empty and its length is even: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a number is within the range of 20 to 100 (inclusive) using the `and` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1261
Write a Python program to check if a number is within the range of 20 to 100 (inclusive) using the `and` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_range_inclusive():  # Function definition: check_range_inclusive
    num = 50  # Variable assignment
    return num >= 20 and num <= 100  # Return the result

result = check_range_inclusive()  # Variable assignment
print(f"Number is between 20 and 100 (inclusive): {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a number is divisible by both 2 and 7 using the `and` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1262
Write a Python program to check if a number is divisible by both 2 and 7 using the `and` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_divisible_by_2_and_7():  # Function definition: check_divisible_by_2_and_7
    num = 14  # Variable assignment
    return num % 2 == 0 and num % 7 == 0  # Return the result

result = check_divisible_by_2_and_7()  # Variable assignment
print(f"Number is divisible by both 2 and 7: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a number is negative and divisible by 5 using the `and` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1263
Write a Python program to check if a number is negative and divisible by 5 using the `and` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_negative_and_divisible():  # Function definition: check_negative_and_divisible
    num = -25  # Variable assignment
    return num < 0 and num % 5 == 0  # Return the result

result = check_negative_and_divisible()  # Variable assignment
print(f"Number is negative and divisible by 5: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a string contains only digits and its length is greater than 5 using the `and` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1264
Write a Python program to check if a string contains only digits and its length is greater than 5 using the `and` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_digit_string():  # Function definition: check_digit_string
    text = "123456"  # Initialize string variable
    return text.isdigit() and len(text) > 5  # Return the result

result = check_digit_string()  # Variable assignment
print(f"String contains only digits and its length is greater than 5: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a number is a prime number and greater than 10 using the `and` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1265
Write a Python program to check if a number is a prime number and greater than 10 using the `and` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_prime_and_greater_than_10():  # Function definition: check_prime_and_greater_than_10
    num = 13  # Variable assignment
    return num > 10 and all(num % i != 0 for i in range(2, num))  # Return the result

result = check_prime_and_greater_than_10()  # Variable assignment
print(f"Number is prime and greater than 10: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a number is odd and greater than 0 using the `and` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1266
Write a Python program to check if a number is odd and greater than 0 using the `and` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_odd_and_positive():  # Function definition: check_odd_and_positive
    num = 7  # Variable assignment
    return num % 2 != 0 and num > 0  # Return the result

result = check_odd_and_positive()  # Variable assignment
print(f"Number is odd and positive: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a file exists and its size is greater than 100 KB using the `and` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1267
Write a Python program to check if a file exists and its size is greater than 100 KB using the `and` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

from pathlib import Path  # Import module or function

def check_file_exists_and_size():  # Function definition: check_file_exists_and_size
    p = Path("example_file.txt")  # Variable assignment
    return p.exists() and p.stat().st_size > 100 * 1024  # Return the result

result = check_file_exists_and_size()  # Variable assignment
print(f"File exists and its size is greater than 100 KB: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a list contains exactly 5 elements and the last element is greater than 10 using the `and` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1268
Write a Python program to check if a list contains exactly 5 elements and the last element is greater than 10 using the `and` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_list_length_and_last_element():  # Function definition: check_list_length_and_last_element
    lst = [1, 2, 3, 4, 12]  # Initialize list
    return len(lst) == 5 and lst[-1] > 10  # Return the result

result = check_list_length_and_last_element()  # Variable assignment
print(f"List contains exactly 5 elements and last element is greater than 10: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a number is between 1 and 10 (inclusive) and is odd using the `and` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1269
Write a Python program to check if a number is between 1 and 10 (inclusive) and is odd using the `and` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_range_and_odd():  # Function definition: check_range_and_odd
    num = 7  # Variable assignment
    return num >= 1 and num <= 10 and num % 2 != 0  # Return the result

result = check_range_and_odd()  # Variable assignment
print(f"Number is between 1 and 10 and odd: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if at least one of two conditions is true using the `or` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1270
Write a Python program to check if at least one of two conditions is true using the `or` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_conditions():  # Function definition: check_conditions
    a = 5  # Variable assignment
    b = 10  # Variable assignment
    return a > 10 or b < 15  # Return the result

result = check_conditions()  # Variable assignment
print(f"At least one condition is true: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a number is either less than 10 or greater than 20 using the `or` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1271
Write a Python program to check if a number is either less than 10 or greater than 20 using the `or` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_range():  # Function definition: check_range
    num = 5  # Variable assignment
    return num < 10 or num > 20  # Return the result

result = check_range()  # Variable assignment: create a range
print(f"Number is either less than 10 or greater than 20: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a string is empty or contains a specific character using the `or` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1272
Write a Python program to check if a string is empty or contains a specific character using the `or` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_string():  # Function definition: check_string
    text = "hello"  # Initialize string variable
    return len(text) == 0 or "e" in text  # Return the result

result = check_string()  # Variable assignment
print(f"String is empty or contains 'e': {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a number is divisible by 3 or 5 using the `or` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1273
Write a Python program to check if a number is divisible by 3 or 5 using the `or` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_divisibility():  # Function definition: check_divisibility
    num = 9  # Variable assignment
    return num % 3 == 0 or num % 5 == 0  # Return the result

result = check_divisibility()  # Variable assignment
print(f"Number is divisible by 3 or 5: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a list is empty or its first element is greater than 5 using the `or` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1274
Write a Python program to check if a list is empty or its first element is greater than 5 using the `or` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_list():  # Function definition: check_list
    lst = [6, 2, 8]  # Initialize list
    return len(lst) == 0 or lst[0] > 5  # Return the result

result = check_list()  # Variable assignment
print(f"List is empty or its first element is greater than 5: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a year is a leap year or divisible by 100 using the `or` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1275
Write a Python program to check if a year is a leap year or divisible by 100 using the `or` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_leap_year():  # Function definition: check_leap_year
    year = 2024  # Variable assignment
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)  # Return the result

result = check_leap_year()  # Variable assignment
print(f"Year is a leap year or divisible by 100: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a number is positive or divisible by 7 using the `or` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1276
Write a Python program to check if a number is positive or divisible by 7 using the `or` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_number():  # Function definition: check_number
    num = 10  # Variable assignment
    return num > 0 or num % 7 == 0  # Return the result

result = check_number()  # Variable assignment
print(f"Number is positive or divisible by 7: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a string is lowercase or its length is greater than 3 using the `or` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1277
Write a Python program to check if a string is lowercase or its length is greater than 3 using the `or` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_string_conditions():  # Function definition: check_string_conditions
    text = "HELLO"  # Initialize string variable
    return text.islower() or len(text) > 3  # Return the result

result = check_string_conditions()  # Variable assignment
print(f"String is lowercase or its length is greater than 3: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a number is between 10 and 50 or divisible by 7 using the `or` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1278
Write a Python program to check if a number is between 10 and 50 or divisible by 7 using the `or` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_conditions():  # Function definition: check_conditions
    num = 30  # Variable assignment
    return (num >= 10 and num <= 50) or num % 7 == 0  # Return the result

result = check_conditions()  # Variable assignment
print(f"Number is between 10 and 50 or divisible by 7: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a number is a multiple of 7 or 11 using the `or` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1279
Write a Python program to check if a number is a multiple of 7 or 11 using the `or` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_multiples():  # Function definition: check_multiples
    num = 77  # Variable assignment
    return num % 7 == 0 or num % 11 == 0  # Return the result

result = check_multiples()  # Variable assignment
print(f"Number is a multiple of 7 or 11: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a person is eligible to vote, meaning the age is greater than 18 or they are a citizen, using the `or` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1280
Write a Python program to check if a person is eligible to vote, meaning the age is greater than 18 or they are a citizen, using the `or` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_voting_eligibility():  # Function definition: check_voting_eligibility
    age = 17  # Variable assignment
    is_citizen = True  # Variable assignment
    return age > 18 or is_citizen  # Return the result

result = check_voting_eligibility()  # Variable assignment
print(f"Person is eligible to vote: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a number is divisible by 2 or 3 using the `or` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1281
Write a Python program to check if a number is divisible by 2 or 3 using the `or` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_divisibility_all():  # Function definition: check_divisibility_all
    num = 9  # Variable assignment
    return num % 2 == 0 or num % 3 == 0  # Return the result

result = check_divisibility_all()  # Variable assignment
print(f"Number is divisible by 2 or 3: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a dictionary contains a specific key or if the value is greater than a specified number using the `or` operator.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1282
Write a Python program to check if a dictionary contains a specific key or if the value is greater than a specified number using the `or` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_dict_conditions():  # Function definition: check_dict_conditions
    sample_dict = {"age": 20, "city": "New York"}  # Initialize dictionary
    return "name" in sample_dict or sample_dict["age"] > 25  # Return the result

result = check_dict_conditions()  # Variable assignment
print(f"Dictionary contains 'name' or age is greater than 25: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a string is empty or contains a number using the `or` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1283
Write a Python program to check if a string is empty or contains a number using the `or` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_string_empty_or_number():  # Function definition: check_string_empty_or_number
    text = "hello123"  # Initialize string variable
    return len(text) == 0 or any(char.isdigit() for char in text)  # Return the result

result = check_string_empty_or_number()  # Variable assignment
print(f"String is empty or contains a number: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a number is either negative or divisible by 3 using the `or` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1284
Write a Python program to check if a number is either negative or divisible by 3 using the `or` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_negative_or_divisible_by_3():  # Function definition: check_negative_or_divisible_by_3
    num = -15  # Variable assignment
    return num < 0 or num % 3 == 0  # Return the result

result = check_negative_or_divisible_by_3()  # Variable assignment
print(f"Number is negative or divisible by 3: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a list is empty or contains more than 5 elements using the `or` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1285
Write a Python program to check if a list is empty or contains more than 5 elements using the `or` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_list_conditions():  # Function definition: check_list_conditions
    lst = [1, 2, 3]  # Initialize list
    return len(lst) == 0 or len(lst) > 5  # Return the result

result = check_list_conditions()  # Variable assignment
print(f"List is empty or contains more than 5 elements: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a number is a perfect square or a perfect cube using the `or` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1286
Write a Python program to check if a number is a perfect square or a perfect cube using the `or` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

import math  # Import module or function

def check_perfect_square_or_cube():  # Function definition: check_perfect_square_or_cube
    num = 16  # Variable assignment
    return math.isqrt(num) ** 2 == num or round(num ** (1 / 3)) ** 3 == num  # Return the result

result = check_perfect_square_or_cube()  # Variable assignment
print(f"Number is a perfect square or cube: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a string contains only letters or only digits using the `or` operator.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1287
Write a Python program to check if a string contains only letters or only digits using the `or` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_string_type():  # Function definition: check_string_type
    text = "1234"  # Initialize string variable
    return text.isalpha() or text.isdigit()  # Return the result

result = check_string_type()  # Variable assignment
print(f"String contains only letters or digits: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a list contains exactly 3 elements or its sum is greater than 50 using the `or` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1288
Write a Python program to check if a list contains exactly 3 elements or its sum is greater than 50 using the `or` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_list_conditions():  # Function definition: check_list_conditions
    lst = [6, 2, 8]  # Initialize list
    return len(lst) == 3 or sum(lst) > 50  # Return the result

result = check_list_conditions()  # Variable assignment
print(f"List has exactly 3 elements or its sum is greater than 50: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a number is divisible by 2 or 5 using the `or` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1289
Write a Python program to check if a number is divisible by 2 or 5 using the `or` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_divisible_by_2_or_5():  # Function definition: check_divisible_by_2_or_5
    num = 10  # Variable assignment
    return num % 2 == 0 or num % 5 == 0  # Return the result

result = check_divisible_by_2_or_5()  # Variable assignment
print(f"Number is divisible by 2 or 5: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a file exists or if it is writable using the `or` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1290
Write a Python program to check if a file exists or if it is writable using the `or` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

from pathlib import Path  # Import module or function

def check_file_conditions():  # Function definition: check_file_conditions
    p = Path("example_file.txt")  # Variable assignment
    return p.exists() or p.is_file()  # Return the result

result = check_file_conditions()  # Variable assignment
print(f"File exists or is a file: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a number is greater than 100 or less than 10 using the `or` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1291
Write a Python program to check if a number is greater than 100 or less than 10 using the `or` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_number():  # Function definition: check_number
    num = 5  # Variable assignment
    return num > 100 or num < 10  # Return the result

result = check_number()  # Variable assignment
print(f"Number is greater than 100 or less than 10: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a string is uppercase or its length is even using the `or` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1292
Write a Python program to check if a string is uppercase or its length is even using the `or` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_string_conditions():  # Function definition: check_string_conditions
    text = "HELLO"  # Initialize string variable
    return text.isupper() or len(text) % 2 == 0  # Return the result

result = check_string_conditions()  # Variable assignment
print(f"String is uppercase or its length is even: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a list is non-empty or its last element is greater than 10 using the `or` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1293
Write a Python program to check if a list is non-empty or its last element is greater than 10 using the `or` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_list_conditions():  # Function definition: check_list_conditions
    lst = [6, 2, 8]  # Initialize list
    return len(lst) > 0 or lst[-1] > 10  # Return the result

result = check_list_conditions()  # Variable assignment
print(f"List is non-empty or its last element is greater than 10: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a number is even or divisible by 3 using the `or` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1294
Write a Python program to check if a number is even or divisible by 3 using the `or` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_even_or_divisible_by_3():  # Function definition: check_even_or_divisible_by_3
    num = 8  # Variable assignment
    return num % 2 == 0 or num % 3 == 0  # Return the result

result = check_even_or_divisible_by_3()  # Variable assignment
print(f"Number is even or divisible by 3: {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a string is not empty or contains the character 'a' using the `or` operator.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1295
Write a Python program to check if a string is not empty or contains the character 'a' using the `or` operator.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_string():  # Function definition: check_string
    text = "apple"  # Initialize string variable
    return len(text) > 0 or "a" in text  # Return the result

result = check_string()  # Variable assignment
print(f"String is not empty or contains 'a': {result}")  # Print the result

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to extract all words starting with a capital letter.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1296
Write a Python program to extract all words starting with a capital letter.
"""

# SOLUTION EXPLANATION:
# This solution uses regular expressions to match or manipulate text according
# to a pattern. Regular expressions provide powerful and flexible text processing.

s = "Hello World, this is Python."  # Initialize string variable
words = re.findall(r"\b[A-Z][a-z]*\b", s)  # Regex operation
print(words)  # Expected output: ['Hello', 'World', 'Python']

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to split a string by commas and optional whitespace.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1297
Write a Python program to split a string by commas and optional whitespace.
"""

# SOLUTION EXPLANATION:
# This solution uses regular expressions to match or manipulate text according
# to a pattern. Regular expressions provide powerful and flexible text processing.

s = "apple, banana ,cherry , grape"  # Initialize string variable
items = re.split(r"\s*,\s*", s)  # Split string into a list
print(items)  # Expected output: ['apple', 'banana', 'cherry', 'grape']

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a password contains at least one digit, one uppercase, and one lowercase letter.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1298
Write a Python program to check if a password contains at least one digit, one uppercase, and one lowercase letter.
"""

# SOLUTION EXPLANATION:
# This solution uses regular expressions to match or manipulate text according
# to a pattern. Regular expressions provide powerful and flexible text processing.

password = "Password123"  # Initialize string variable
match = bool(re.search(r"[A-Z]", password) and re.search(r"[a-z]", password) and re.search(r"\d", password))  # Regex operation
print(match)  # Expected output: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to find all email addresses in a text.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1299
Write a Python program to find all email addresses in a text.
"""

# SOLUTION EXPLANATION:
# This solution uses regular expressions to match or manipulate text according
# to a pattern. Regular expressions provide powerful and flexible text processing.

text = "Send to alice@example.com and bob99@domain.co.uk"  # Initialize string variable
emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)  # Regex operation
print(emails)  # Expected output: ['alice@example.com', 'bob99@domain.co.uk']

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to extract hashtags from a tweet.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1300
Write a Python program to extract hashtags from a tweet.
"""

# SOLUTION EXPLANATION:
# This solution uses regular expressions to match or manipulate text according
# to a pattern. Regular expressions provide powerful and flexible text processing.

tweet = "Loving the #Python #coding journey!"  # Initialize string variable
hashtags = re.findall(r"#\w+", tweet)  # Regex operation
print(hashtags)  # Expected output: ['#Python', '#coding']

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to extract domain names from URLs.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1301
Write a Python program to extract domain names from URLs.
"""

# SOLUTION EXPLANATION:
# This solution uses regular expressions to match or manipulate text according
# to a pattern. Regular expressions provide powerful and flexible text processing.

text = "Visit us at https://example.com or http://test.org"  # Initialize string variable
domains = re.findall(r"https?://([\w.-]+)", text)  # Slice: extract a portion of the sequence
print(domains)  # Expected output: ['example.com', 'test.org']

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to validate if a string is a valid IPv4 address.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1302
Write a Python program to validate if a string is a valid IPv4 address.
"""

# SOLUTION EXPLANATION:
# This solution uses regular expressions to match or manipulate text according
# to a pattern. Regular expressions provide powerful and flexible text processing.

ip = "192.168.1.1"  # Initialize string variable
pattern = r"^(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(?!$)){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$"  # Variable assignment
match = bool(re.fullmatch(pattern, ip))  # Regex operation
print(match)  # Expected output: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to remove all punctuation from a string.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1303
Write a Python program to remove all punctuation from a string.
"""

# SOLUTION EXPLANATION:
# This solution uses regular expressions to match or manipulate text according
# to a pattern. Regular expressions provide powerful and flexible text processing.

text = "Hello, world! Python is great."  # Initialize string variable
clean = re.sub(r"[^\w\s]", "", text)  # Regex operation
print(clean)  # Expected output: Hello world Python is great

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to match a string that starts with a vowel.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1304
Write a Python program to match a string that starts with a vowel.
"""

# SOLUTION EXPLANATION:
# This solution uses regular expressions to match or manipulate text according
# to a pattern. Regular expressions provide powerful and flexible text processing.

s = "apple"  # Initialize string variable
match = bool(re.match(r"^[aeiouAEIOU]", s))  # Regex operation
print(match)  # Expected output: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to extract all valid dates in the format YYYY-MM-DD.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1305
Write a Python program to extract all valid dates in the format YYYY-MM-DD.
"""

# SOLUTION EXPLANATION:
# This solution uses regular expressions to match or manipulate text according
# to a pattern. Regular expressions provide powerful and flexible text processing.

text = "Events: 2024-06-01, 2025-07-04, 99-01-01"  # Initialize string variable
dates = re.findall(r"\b\d{4}-\d{2}-\d{2}\b", text)  # Regex operation
print(dates)  # Expected output: ['2024-06-01', '2025-07-04']

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to validate a hexadecimal color code.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1306
Write a Python program to validate a hexadecimal color code.
"""

# SOLUTION EXPLANATION:
# This solution uses regular expressions to match or manipulate text according
# to a pattern. Regular expressions provide powerful and flexible text processing.

color = "#1a2b3c"  # Initialize string variable
match = bool(re.fullmatch(r"#([A-Fa-f0-9]{6})", color))  # Regex operation
print(match)  # Expected output: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to extract all words that end with 'ing'.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1307
Write a Python program to extract all words that end with 'ing'.
"""

# SOLUTION EXPLANATION:
# This solution uses regular expressions to match or manipulate text according
# to a pattern. Regular expressions provide powerful and flexible text processing.

text = "I am running and jumping while singing."  # Initialize string variable
words = re.findall(r"\b\w+ing\b", text)  # Regex operation
print(words)  # Expected output: ['running', 'jumping', 'singing']

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to extract the file extension from a filename.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1308
Write a Python program to extract the file extension from a filename.
"""

# SOLUTION EXPLANATION:
# This solution uses regular expressions to match or manipulate text according
# to a pattern. Regular expressions provide powerful and flexible text processing.

filename = "document.pdf"  # Initialize string variable
ext = re.search(r"\.(\w+)$", filename).group(1)  # Regex operation
print(ext)  # Expected output: pdf

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to find duplicated words in a sentence.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1309
Write a Python program to find duplicated words in a sentence.
"""

# SOLUTION EXPLANATION:
# This solution uses regular expressions to match or manipulate text according
# to a pattern. Regular expressions provide powerful and flexible text processing.

text = "This is is a test test string"  # Initialize string variable
duplicates = re.findall(r"\b(\w+)\s+\1\b", text)  # Regex operation
print(duplicates)  # Expected output: ['is', 'test']

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to extract all capitalized words from a paragraph.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1310
Write a Python program to extract all capitalized words from a paragraph.
"""

# SOLUTION EXPLANATION:
# This solution uses regular expressions to match or manipulate text according
# to a pattern. Regular expressions provide powerful and flexible text processing.

text = "Alice and Bob went to New York City on Monday."  # Initialize string variable
capitalized = re.findall(r"\b[A-Z][a-z]*\b", text)  # Regex operation
print(capitalized)  # Expected: ['Alice', 'Bob', 'New', 'York', 'City', 'Monday']

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to validate a time in 24-hour format (HH:MM).
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1311
Write a Python program to validate a time in 24-hour format (HH:MM).
"""

# SOLUTION EXPLANATION:
# This solution uses regular expressions to match or manipulate text according
# to a pattern. Regular expressions provide powerful and flexible text processing.

time = "23:59"  # Initialize string variable
match = bool(re.fullmatch(r"([01]\d|2[0-3]):[0-5]\d", time))  # Slice: extract a portion of the sequence
print(match)  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to extract all integers and floats from a string.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1312
Write a Python program to extract all integers and floats from a string.
"""

# SOLUTION EXPLANATION:
# This solution uses regular expressions to match or manipulate text according
# to a pattern. Regular expressions provide powerful and flexible text processing.

text = "The temperature is 21.5C, and humidity is 60% with 0.25 inches rain."  # Initialize string variable
numbers = re.findall(r"\d+\.\d+|\d+", text)  # Regex operation
print(numbers)  # Expected: ['21.5', '60', '0.25']

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to remove leading zeros from an IP address.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1313
Write a Python program to remove leading zeros from an IP address.
"""

# SOLUTION EXPLANATION:
# This solution uses regular expressions to match or manipulate text according
# to a pattern. Regular expressions provide powerful and flexible text processing.

ip = "192.168.001.001"  # Initialize string variable
clean_ip = re.sub(r"\b0+(\d)", r"\1", ip)  # Regex operation
print(clean_ip)  # Expected: 192.168.1.1

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a string is a valid slug (only lowercase letters, numbers, hyphens).
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1314
Write a Python program to check if a string is a valid slug (only lowercase letters, numbers, hyphens).
"""

# SOLUTION EXPLANATION:
# This solution uses regular expressions to match or manipulate text according
# to a pattern. Regular expressions provide powerful and flexible text processing.

slug = "python-tips-101"  # Initialize string variable
match = bool(re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", slug))  # Regex operation
print(match)  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to extract content inside parentheses.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1315
Write a Python program to extract content inside parentheses.
"""

# SOLUTION EXPLANATION:
# This solution uses regular expressions to match or manipulate text according
# to a pattern. Regular expressions provide powerful and flexible text processing.

text = "This is a sample (with content) and (another one)."  # Initialize string variable
content = re.findall(r"\((.*?)\)", text)  # Regex operation
print(content)  # Expected: ['with content', 'another one']

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to match all valid HTML tags in a string.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1316
Write a Python program to match all valid HTML tags in a string.
"""

# SOLUTION EXPLANATION:
# This solution uses regular expressions to match or manipulate text according
# to a pattern. Regular expressions provide powerful and flexible text processing.

html = "<div><p>Hello</p></div>"  # Initialize string variable
tags = re.findall(r"<[^>]+>", html)  # Regex operation
print(tags)  # Expected: ['<div>', '<p>', '</p>', '</div>']

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to validate if a string is a US ZIP code (5 digits).
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1317
Write a Python program to validate if a string is a US ZIP code (5 digits).
"""

# SOLUTION EXPLANATION:
# This solution uses regular expressions to match or manipulate text according
# to a pattern. Regular expressions provide powerful and flexible text processing.

zip_code = "12345"  # Initialize string variable
match = bool(re.fullmatch(r"\d{5}", zip_code))  # Regex operation
print(match)  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

""" 
Problem: 1318
Write a Python program to find all abbreviations like "U.S.A." in a string.
"""

text = "Some examples: U.S.A. and E.U."
abbreviations = re.findall(r"(?:[A-Z]\.){2,}", text)
print(abbreviations)  # Expected: ['U.S.A.', 'E.U.']


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to count how many times a word appears in a case-insensitive way.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1319
Write a Python program to count how many times a word appears in a case-insensitive way.
"""

# SOLUTION EXPLANATION:
# This solution uses regular expressions to match or manipulate text according
# to a pattern. Regular expressions provide powerful and flexible text processing.

text = "Python is great. I love python because PYTHON is powerful."  # Initialize string variable
count = len(re.findall(r"\bpython\b", text, re.IGNORECASE))  # Calculate the length
print(count)  # Expected: 3

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to replace duplicate spaces with a single space.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1320
Write a Python program to replace duplicate spaces with a single space.
"""

# SOLUTION EXPLANATION:
# This solution uses regular expressions to match or manipulate text according
# to a pattern. Regular expressions provide powerful and flexible text processing.

text = "This    is  a    spaced   sentence."  # Initialize string variable
clean = re.sub(r"\s{2,}", " ", text)  # Regex operation
print(clean)  # Expected: "This is a spaced sentence."

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to validate a MAC address (e.g., 00:1A:2B:3C:4D:5E).
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1321
Write a Python program to validate a MAC address (e.g., 00:1A:2B:3C:4D:5E).
"""

# SOLUTION EXPLANATION:
# This solution uses regular expressions to match or manipulate text according
# to a pattern. Regular expressions provide powerful and flexible text processing.

mac = "00:1A:2B:3C:4D:5E"  # Initialize string variable
match = bool(re.fullmatch(r"([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}", mac))  # Slice: extract a portion of the sequence
print(match)  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to extract the username from an email address.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1322
Write a Python program to extract the username from an email address.
"""

# SOLUTION EXPLANATION:
# This solution uses regular expressions to match or manipulate text according
# to a pattern. Regular expressions provide powerful and flexible text processing.

email = "john.doe@example.com"  # Initialize string variable
username = re.match(r"([^@]+)", email).group(1)  # Regex operation
print(username)  # Expected: john.doe

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to insert commas into a numeric string every three digits.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1323
Write a Python program to insert commas into a numeric string every three digits.
"""

# SOLUTION EXPLANATION:
# This solution uses regular expressions to match or manipulate text according
# to a pattern. Regular expressions provide powerful and flexible text processing.

num = "1000000"  # Initialize string variable
formatted = re.sub(r"(?<=\d)(?=(\d{3})+$)", ",", num)  # Regex operation
print(formatted)  # Expected: 1,000,000

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to extract all valid Twitter handles from a string.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1324
Write a Python program to extract all valid Twitter handles from a string.
"""

# SOLUTION EXPLANATION:
# This solution uses regular expressions to match or manipulate text according
# to a pattern. Regular expressions provide powerful and flexible text processing.

text = "Follow @python, @realpython, and @openai!"  # Initialize string variable
handles = re.findall(r"@\w+", text)  # Regex operation
print(handles)  # Expected: ['@python', '@realpython', '@openai']

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a string contains any emoji.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1325
Write a Python program to check if a string contains any emoji.
"""

# SOLUTION EXPLANATION:
# This solution uses regular expressions to match or manipulate text according
# to a pattern. Regular expressions provide powerful and flexible text processing.

emoji_text = "I love 🍕 and 🐍"  # Initialize string variable
match = bool(re.search(r"[\U0001F600-\U0001F64F]", emoji_text))  # Regex operation
print(match)  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to extract time values in 12-hour format with AM/PM.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1326
Write a Python program to extract time values in 12-hour format with AM/PM.
"""

# SOLUTION EXPLANATION:
# This solution uses regular expressions to match or manipulate text according
# to a pattern. Regular expressions provide powerful and flexible text processing.

text = "Meeting at 02:30 PM and dinner at 07:45 AM."  # Initialize string variable
times = re.findall(r"\b\d{2}:\d{2} [AP]M\b", text)  # Slice: extract a portion of the sequence
print(times)  # Expected: ['02:30 PM', '07:45 AM']

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to extract prices with a dollar sign.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1327
Write a Python program to extract prices with a dollar sign.
"""

# SOLUTION EXPLANATION:
# This solution uses regular expressions to match or manipulate text according
# to a pattern. Regular expressions provide powerful and flexible text processing.

text = "Items: $20.99, $3.50, $100"  # Initialize string variable
prices = re.findall(r"\$\d+(\.\d{2})?", text)  # Regex operation
print(prices)  # Expected: ['$20.99', '$3.50', '$100']

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to detect duplicate characters in a string using regex.
# 
# This problem demonstrates regular expressions (regex) in Python. Regular
# expressions are powerful patterns for matching and manipulating text.
# They allow complex string searches, replacements, and validations.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1328
Write a Python program to detect duplicate characters in a string using regex.
"""

# SOLUTION EXPLANATION:
# This solution uses regular expressions to match or manipulate text according
# to a pattern. Regular expressions provide powerful and flexible text processing.

s = "programming"  # Initialize string variable
duplicates = re.findall(r"(\w)(?=.*\1)", s)  # Regex operation
print(set(duplicates))  # Expected: {'r', 'g', 'm'}

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to validate a hexadecimal number (e.g., 0x1A3F).
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1329
Write a Python program to validate a hexadecimal number (e.g., 0x1A3F).
"""

# SOLUTION EXPLANATION:
# This solution uses regular expressions to match or manipulate text according
# to a pattern. Regular expressions provide powerful and flexible text processing.

hex_num = "0x1A3F"  # Initialize string variable
match = bool(re.fullmatch(r"0x[0-9A-Fa-f]+", hex_num))  # Regex operation
print(match)  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to extract quoted strings (single or double quotes).
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1330
Write a Python program to extract quoted strings (single or double quotes).
"""

# SOLUTION EXPLANATION:
# This solution uses regular expressions to match or manipulate text according
# to a pattern. Regular expressions provide powerful and flexible text processing.

import re  # Import module or function

text = "'Hello', she said. \"How are you?\""  # Initialize string variable
quotes = re.findall(r"(['\"])(.*?)\1", text)  # Regex operation
print([q[1] for q in quotes])  # Expected: ['Hello', 'How are you?']

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a variable is an integer using isinstance().
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1331
Write a Python program to check if a variable is an integer using isinstance().
"""

# SOLUTION EXPLANATION:
# This solution uses the 'is' operator to check object identity. This is
# different from '==' which checks value equality.

x = 10  # Variable assignment
print(isinstance(x, int))  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a variable is a string using isinstance().
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1332
Write a Python program to check if a variable is a string using isinstance().
"""

# SOLUTION EXPLANATION:
# This solution uses the 'is' operator to check object identity. This is
# different from '==' which checks value equality.

x = "hello"  # Initialize string variable
print(isinstance(x, str))  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a variable is a float using isinstance().
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1333
Write a Python program to check if a variable is a float using isinstance().
"""

# SOLUTION EXPLANATION:
# This solution uses the 'is' operator to check object identity. This is
# different from '==' which checks value equality.

x = 3.14  # Variable assignment
print(isinstance(x, float))  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a variable is a list using isinstance().
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1334
Write a Python program to check if a variable is a list using isinstance().
"""

# SOLUTION EXPLANATION:
# This solution uses the 'is' operator to check object identity. This is
# different from '==' which checks value equality.

x = [1, 2, 3]  # Initialize list
print(isinstance(x, list))  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a variable is a dictionary using isinstance().
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1335
Write a Python program to check if a variable is a dictionary using isinstance().
"""

# SOLUTION EXPLANATION:
# This solution uses the 'is' operator to check object identity. This is
# different from '==' which checks value equality.

x = {"a": 1}  # Initialize dictionary
print(isinstance(x, dict))  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a variable is either int or float using isinstance().
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1336
Write a Python program to check if a variable is either int or float using isinstance().
"""

# SOLUTION EXPLANATION:
# This solution uses the 'is' operator to check object identity. This is
# different from '==' which checks value equality.

x = 10.0  # Variable assignment
print(isinstance(x, (int, float)))  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if each element in a list is a string.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1337
Write a Python program to check if each element in a list is a string.
"""

# SOLUTION EXPLANATION:
# This solution uses the 'is' operator to check object identity. This is
# different from '==' which checks value equality.

lst = ["apple", "banana", "cherry"]  # Initialize list
result = all(isinstance(item, str) for item in lst)  # Variable assignment
print(result)  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to filter only integers from a mixed list using isinstance().
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1338
Write a Python program to filter only integers from a mixed list using isinstance().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

items = [1, "a", 3.5, 4, "b"]  # Initialize list
ints = [x for x in items if isinstance(x, int)]  # List comprehension: creates a new list
print(ints)  # Expected: [1, 4]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to filter only strings from a mixed list using isinstance().
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1339
Write a Python program to filter only strings from a mixed list using isinstance().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

items = [1, "apple", 2.5, "banana"]  # Initialize list
strings = [x for x in items if isinstance(x, str)]  # List comprehension: creates a new list
print(strings)  # Expected: ['apple', 'banana']

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if an object is a boolean using isinstance().
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1340
Write a Python program to check if an object is a boolean using isinstance().
"""

# SOLUTION EXPLANATION:
# This solution uses the 'is' operator to check object identity. This is
# different from '==' which checks value equality.

x = True  # Variable assignment
print(isinstance(x, bool))  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a variable is a tuple using isinstance().
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1341
Write a Python program to check if a variable is a tuple using isinstance().
"""

# SOLUTION EXPLANATION:
# This solution uses the 'is' operator to check object identity. This is
# different from '==' which checks value equality.

x = (1, 2, 3)  # Initialize tuple
print(isinstance(x, tuple))  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if an object is not a string using isinstance().
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1342
Write a Python program to check if an object is not a string using isinstance().
"""

# SOLUTION EXPLANATION:
# This solution uses the 'is' operator to check object identity. This is
# different from '==' which checks value equality.

x = 42  # Variable assignment
print(not isinstance(x, str))  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to define a function that accepts only strings using isinstance().
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1343
Write a Python program to define a function that accepts only strings using isinstance().
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def greet(name):  # Function definition: greet
    if not isinstance(name, str):  # Conditional check
        return "Invalid input"  # Return the result
    return f"Hello, {name}!"  # Return the result

print(greet("Alice"))  # Expected: Hello, Alice!
print(greet(123))      # Expected: Invalid input

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if all elements in a nested list are lists.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1344
Write a Python program to check if all elements in a nested list are lists.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

nested = [[1, 2], [3, 4]]  # Initialize list
result = all(isinstance(sub, list) for sub in nested)  # Variable assignment
print(result)  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to separate strings and numbers from a list.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1345
Write a Python program to separate strings and numbers from a list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

mixed = [1, "one", 2, "two", 3, "three"]  # Initialize list
nums = [x for x in mixed if isinstance(x, int)]  # List comprehension: creates a new list
words = [x for x in mixed if isinstance(x, str)]  # List comprehension: creates a new list
print(nums)   # Expected: [1, 2, 3]
print(words)  # Expected: ['one', 'two', 'three']

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to validate argument types in a function.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1346
Write a Python program to validate argument types in a function.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def multiply(a, b):  # Function definition: multiply
    if not all(isinstance(x, (int, float)) for x in (a, b)):  # Conditional check
        return "Invalid input"  # Return the result
    return a * b  # Return the result

print(multiply(2, 3))     # Expected: 6
print(multiply(2, "x"))   # Expected: Invalid input

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a variable is a set using isinstance().
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1347
Write a Python program to check if a variable is a set using isinstance().
"""

# SOLUTION EXPLANATION:
# This solution uses the 'is' operator to check object identity. This is
# different from '==' which checks value equality.

x = {1, 2, 3}  # Initialize dictionary
print(isinstance(x, set))  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to validate that dictionary keys are all strings.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1348
Write a Python program to validate that dictionary keys are all strings.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

d = {"a": 1, "b": 2}  # Initialize dictionary
result = all(isinstance(k, str) for k in d.keys())  # Variable assignment
print(result)  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to validate that dictionary values are all integers.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1349
Write a Python program to validate that dictionary values are all integers.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

d = {"x": 1, "y": 2}  # Initialize dictionary
result = all(isinstance(v, int) for v in d.values())  # Variable assignment
print(result)  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if an object is a file-like object (has read method).
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1350
Write a Python program to check if an object is a file-like object (has read method).
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

class FakeFile:  # Class definition: FakeFile
    def read(self):  # Function definition: read
        pass

f = FakeFile()  # Variable assignment
print(hasattr(f, "read") and callable(f.read))  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to remove a key from a dictionary using pop() and print the updated dictionary.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1351
Write a Python program to remove a key from a dictionary using pop() and print the updated dictionary.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

d = {"a": 1, "b": 2, "c": 3}  # Initialize dictionary
d.pop("b")  # Method or function call
print(d)  # Expected: {'a': 1, 'c': 3}

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to use pop() to retrieve the value of a key from a dictionary.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1352
Write a Python program to use pop() to retrieve the value of a key from a dictionary.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

d = {"a": 10, "b": 20}  # Initialize dictionary
value = d.pop("a")  # Variable assignment
print(value)  # Expected: 10

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to use pop() on a list to remove the last item.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1353
Write a Python program to use pop() on a list to remove the last item.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

lst = [1, 2, 3, 4]  # Initialize list
lst.pop()  # Method or function call
print(lst)  # Expected: [1, 2, 3]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to remove a specific index from a list using pop().
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1354
Write a Python program to remove a specific index from a list using pop().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

lst = [10, 20, 30, 40]  # Initialize list
lst.pop(1)  # Method or function call
print(lst)  # Expected: [10, 30, 40]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to capture and print the element removed using pop() from a list.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1355
Write a Python program to capture and print the element removed using pop() from a list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

lst = [5, 6, 7]  # Initialize list
removed = lst.pop()  # Variable assignment
print(removed)  # Expected: 7

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to remove all elements from a list using pop() in a loop.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1356
Write a Python program to remove all elements from a list using pop() in a loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

lst = [1, 2, 3]  # Initialize list
while lst:  # Code block
    print(lst.pop())  # Expected: 3, 2, 1 (on separate lines)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to handle IndexError when popping from an empty list.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1357
Write a Python program to handle IndexError when popping from an empty list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

lst = []  # Initialize list
try:  # Code block
    lst.pop()  # Method or function call
except IndexError:  # Code block
    print("List is empty")  # Expected: "List is empty"

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to use pop() with dictionaries and provide a default return value if the key doesn't exist.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1358
Write a Python program to use pop() with dictionaries and provide a default return value if the key doesn't exist.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

d = {"x": 5}  # Initialize dictionary
val = d.pop("y", "Not Found")  # Variable assignment
print(val)  # Expected: "Not Found"

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to safely remove a key from a dictionary using pop() inside a try block.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1359
Write a Python program to safely remove a key from a dictionary using pop() inside a try block.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

d = {"a": 100}  # Initialize dictionary
try:  # Code block
    print(d.pop("b"))  # Print the result
except KeyError:  # Code block
    print("Key not found")  # Expected: "Key not found"

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to remove keys one by one using pop() until the dictionary is empty.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1360
Write a Python program to remove keys one by one using pop() until the dictionary is empty.
"""

# SOLUTION EXPLANATION:
# This solution uses the 'is' operator to check object identity. This is
# different from '==' which checks value equality.

d = {"k1": 1, "k2": 2}  # Initialize dictionary
while d:  # Code block
    print(d.popitem())  # Expected: tuple key-value pairs

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to pop elements from a stack represented by a list.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1361
Write a Python program to pop elements from a stack represented by a list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

stack = [1, 2, 3]  # Initialize list
print(stack.pop())  # Expected: 3

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to simulate queue dequeue using pop(0).
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1362
Write a Python program to simulate queue dequeue using pop(0).
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

queue = [10, 20, 30]  # Initialize list
print(queue.pop(0))  # Expected: 10

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to remove the last element from a list using pop() and store it.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1363
Write a Python program to remove the last element from a list using pop() and store it.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

numbers = [4, 5, 6]  # Initialize list
last = numbers.pop()  # Variable assignment
print(last)  # Expected: 6

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to demonstrate the use of pop() on a string key in a dictionary.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1364
Write a Python program to demonstrate the use of pop() on a string key in a dictionary.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

d = {"name": "Alice", "age": 30}  # Initialize dictionary
print(d.pop("name"))  # Expected: "Alice"

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to pop multiple elements from the end of a list using a loop.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1365
Write a Python program to pop multiple elements from the end of a list using a loop.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

lst = [1, 2, 3, 4, 5]  # Initialize list
for _ in range(3):  # Loop through items
    lst.pop()  # Method or function call
print(lst)  # Expected: [1, 2]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to pop and sum the last two numbers from a list.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1366
Write a Python program to pop and sum the last two numbers from a list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

lst = [100, 200, 300]  # Initialize list
sum_last_two = lst.pop() + lst.pop()  # Variable assignment
print(sum_last_two)  # Expected: 500

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to use pop() in a function that removes a key from a given dictionary.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1367
Write a Python program to use pop() in a function that removes a key from a given dictionary.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def remove_key(d, key):  # Function definition: remove_key
    return d.pop(key, None)  # Return the result

print(remove_key({"a": 1, "b": 2}, "a"))  # Expected: 1

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to pop an element from a list and append it to another list.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1368
Write a Python program to pop an element from a list and append it to another list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

src = [9, 8, 7]  # Initialize list
dst = []  # Initialize list
dst.append(src.pop())  # Method or function call
print(dst)  # Expected: [7]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to implement a basic undo feature using pop() on a list of actions.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1369
Write a Python program to implement a basic undo feature using pop() on a list of actions.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

actions = ["type", "edit", "save"]  # Initialize list
undo = actions.pop()  # Variable assignment
print(undo)  # Expected: "save"

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to pop elements from a nested list.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1370
Write a Python program to pop elements from a nested list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

nested = [[1, 2], [3, 4], [5, 6]]  # Initialize list
last_sublist = nested.pop()  # Variable assignment
print(last_sublist)  # Expected: [5, 6]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program with a function that accepts arbitrary keyword arguments and prints them.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1371
Write a Python program with a function that accepts arbitrary keyword arguments and prints them.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def print_kwargs(**kwargs):  # Function definition: print_kwargs
    print(kwargs)  # Print the result

print_kwargs(a=1, b=2)  # Expected: {'a': 1, 'b': 2}

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function that prints each key-value pair in **kwargs on a separate line.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1372
Write a Python function that prints each key-value pair in **kwargs on a separate line.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def display_kwargs(**kwargs):  # Function definition: display_kwargs
    for key, value in kwargs.items():  # Loop through items
        print(f"{key}: {value}")  # Print the result

display_kwargs(name="Alice", age=30)
# Expected:
# name: Alice
# age: 30

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to count the number of keyword arguments passed to a function.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1373
Write a Python program to count the number of keyword arguments passed to a function.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def count_kwargs(**kwargs):  # Function definition: count_kwargs
    print(len(kwargs))  # Print the result

count_kwargs(a=1, b=2, c=3)  # Expected: 3

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function that returns the keys of **kwargs as a list.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1374
Write a Python function that returns the keys of **kwargs as a list.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def kwargs_keys(**kwargs):  # Function definition: kwargs_keys
    return list(kwargs.keys())  # Return the result

print(kwargs_keys(x=10, y=20))  # Expected: ['x', 'y']

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function that returns the values of **kwargs as a list.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1375
Write a Python function that returns the values of **kwargs as a list.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def kwargs_values(**kwargs):  # Function definition: kwargs_values
    return list(kwargs.values())  # Return the result

print(kwargs_values(x=10, y=20))  # Expected: [10, 20]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function that returns True if 'id' is in **kwargs.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1376
Write a Python function that returns True if 'id' is in **kwargs.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def has_id(**kwargs):  # Function definition: has_id
    return 'id' in kwargs  # Return the result

print(has_id(name="A", id=123))  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function that returns the value of a keyword argument 'name' if it exists, else return 'Unknown'.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1377
Write a Python function that returns the value of a keyword argument 'name' if it exists, else return 'Unknown'.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def get_name(**kwargs):  # Function definition: get_name
    return kwargs.get('name', 'Unknown')  # Return the result

print(get_name(age=22))  # Expected: "Unknown"

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function that sums all numeric values in **kwargs.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1378
Write a Python function that sums all numeric values in **kwargs.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def sum_kwargs(**kwargs):  # Function definition: sum_kwargs
    return sum(v for v in kwargs.values() if isinstance(v, (int, float)))  # Return the result

print(sum_kwargs(a=10, b=5.5, c="x"))  # Expected: 15.5

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function that filters and returns keyword arguments where values are strings.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1379
Write a Python function that filters and returns keyword arguments where values are strings.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def string_kwargs(**kwargs):  # Function definition: string_kwargs
    return {k: v for k, v in kwargs.items() if isinstance(v, str)}  # Return the result

print(string_kwargs(a="hi", b=2, c="hello"))  # Expected: {'a': 'hi', 'c': 'hello'}

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function that prints a formatted string from **kwargs using name and age keys.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1380
Write a Python function that prints a formatted string from **kwargs using name and age keys.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def greet(**kwargs):  # Function definition: greet
    print(f"Hello {kwargs.get('name', 'Guest')}, age {kwargs.get('age', 'N/A')}")  # Print the result

greet(name="Bob", age=40)  # Expected: Hello Bob, age 40

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function that updates a dictionary with keyword arguments.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1381
Write a Python function that updates a dictionary with keyword arguments.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def update_dict(base, **kwargs):  # Function definition: update_dict
    base.update(kwargs)  # Method or function call
    return base  # Return the result

print(update_dict({'x': 1}, y=2, z=3))  # Expected: {'x': 1, 'y': 2, 'z': 3}

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function that merges two dictionaries using **kwargs.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1382
Write a Python function that merges two dictionaries using **kwargs.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def merge_dicts(d1, **kwargs):  # Function definition: merge_dicts
    merged = d1.copy()  # Variable assignment
    merged.update(kwargs)  # Method or function call
    return merged  # Return the result

print(merge_dicts({'a': 1}, b=2))  # Expected: {'a': 1, 'b': 2}

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function that prints only the keyword arguments with even integer values.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1383
Write a Python function that prints only the keyword arguments with even integer values.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def even_kwargs(**kwargs):  # Function definition: even_kwargs
    for k, v in kwargs.items():  # Loop through items
        if isinstance(v, int) and v % 2 == 0:  # Conditional check
            print(f"{k}: {v}")  # Print the result

even_kwargs(a=1, b=2, c=4)
# Expected:
# b: 2
# c: 4

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function that accepts any number of keyword arguments and prints them sorted by key.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1384
Write a Python function that accepts any number of keyword arguments and prints them sorted by key.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def sorted_kwargs(**kwargs):  # Function definition: sorted_kwargs
    for k in sorted(kwargs.keys()):  # Loop through items
        print(f"{k}: {kwargs[k]}")  # Print the result

sorted_kwargs(z=9, a=1, m=5)
# Expected:
# a: 1
# m: 5
# z: 9

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function that prints the number of string values in **kwargs.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1385
Write a Python function that prints the number of string values in **kwargs.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def count_strings(**kwargs):  # Function definition: count_strings
    print(sum(1 for v in kwargs.values() if isinstance(v, str)))  # Print the result

count_strings(a="one", b=2, c="three")  # Expected: 2

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function that prints whether each value in **kwargs is truthy or falsy.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1386
Write a Python function that prints whether each value in **kwargs is truthy or falsy.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def check_truthy(**kwargs):  # Function definition: check_truthy
    for k, v in kwargs.items():  # Loop through items
        print(f"{k}: {'Truthy' if v else 'Falsy'}")  # Print the result

check_truthy(a=0, b="hello", c=[])  
# Expected:
# a: Falsy
# b: Truthy
# c: Falsy

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function that prints all key-value pairs in **kwargs where the key starts with 'a'.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1387
Write a Python function that prints all key-value pairs in **kwargs where the key starts with 'a'.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def starts_with_a(**kwargs):  # Function definition: starts_with_a
    for k, v in kwargs.items():  # Loop through items
        if k.startswith('a'):  # Conditional check
            print(f"{k}: {v}")  # Print the result

starts_with_a(apple=1, banana=2, ant=3)
# Expected:
# apple: 1
# ant: 3

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function that returns a reversed dictionary built from **kwargs.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1388
Write a Python function that returns a reversed dictionary built from **kwargs.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def reverse_kwargs(**kwargs):  # Function definition: reverse_kwargs
    return {v: k for k, v in kwargs.items()}  # Return the result

print(reverse_kwargs(a=1, b=2))  # Expected: {1: 'a', 2: 'b'}

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function that returns the longest key in **kwargs.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1389
Write a Python function that returns the longest key in **kwargs.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def longest_key(**kwargs):  # Function definition: longest_key
    return max(kwargs, key=len)  # Return the result

print(longest_key(short=1, muchlonger=2))  # Expected: 'muchlonger'

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function that creates a string from **kwargs as key=value pairs joined by commas.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1390
Write a Python function that creates a string from **kwargs as key=value pairs joined by commas.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def stringify_kwargs(**kwargs):  # Function definition: stringify_kwargs
    return ', '.join(f"{k}={v}" for k, v in kwargs.items())  # Return the result

print(stringify_kwargs(x=10, y=20))  # Expected: "x=10, y=20"

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function that checks if all values in **kwargs are integers.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1391
Write a Python function that checks if all values in **kwargs are integers.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def all_ints(**kwargs):  # Function definition: all_ints
    return all(isinstance(v, int) for v in kwargs.values())  # Return the result

print(all_ints(a=1, b=2))  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function that finds and returns the maximum numeric value in **kwargs.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1392
Write a Python function that finds and returns the maximum numeric value in **kwargs.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def max_numeric(**kwargs):  # Function definition: max_numeric
    nums = [v for v in kwargs.values() if isinstance(v, (int, float))]  # List comprehension: creates a new list
    return max(nums) if nums else None  # Return the result

print(max_numeric(a=1, b=3.5, c="x"))  # Expected: 3.5

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function that counts the keyword arguments whose value is None.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1393
Write a Python function that counts the keyword arguments whose value is None.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def count_none(**kwargs):  # Function definition: count_none
    return sum(1 for v in kwargs.values() if v is None)  # Return the result

print(count_none(a=None, b=1, c=None))  # Expected: 2

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function that prints the types of values in **kwargs.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1394
Write a Python function that prints the types of values in **kwargs.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def print_types(**kwargs):  # Function definition: print_types
    for k, v in kwargs.items():  # Loop through items
        print(f"{k}: {type(v).__name__}")  # Print the result

print_types(a=1, b="str", c=3.14)
# Expected:
# a: int
# b: str
# c: float

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function that creates a list of key-value pairs (tuples) from **kwargs.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1395
Write a Python function that creates a list of key-value pairs (tuples) from **kwargs.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def kv_pairs(**kwargs):  # Function definition: kv_pairs
    return list(kwargs.items())  # Return the result

print(kv_pairs(a=1, b=2))  # Expected: [('a', 1), ('b', 2)]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function that filters out keyword arguments with falsy values.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1396
Write a Python function that filters out keyword arguments with falsy values.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def remove_falsy(**kwargs):  # Function definition: remove_falsy
    return {k: v for k, v in kwargs.items() if v}  # Return the result

print(remove_falsy(a=0, b=1, c=""))  # Expected: {'b': 1}

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function that returns True if at least one value in **kwargs is a list.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1397
Write a Python function that returns True if at least one value in **kwargs is a list.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def has_list(**kwargs):  # Function definition: has_list
    return any(isinstance(v, list) for v in kwargs.values())  # Return the result

print(has_list(a=[1,2], b="x"))  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function that prints whether the number of keyword arguments is even or odd.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1398
Write a Python function that prints whether the number of keyword arguments is even or odd.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def even_or_odd_kwargs(**kwargs):  # Function definition: even_or_odd_kwargs
    print("Even" if len(kwargs) % 2 == 0 else "Odd")  # Print the result

even_or_odd_kwargs(a=1, b=2, c=3)  # Expected: Odd

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function that accepts **kwargs and renames any keys that start with 'temp_' by removing the prefix.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1399
Write a Python function that accepts **kwargs and renames any keys that start with 'temp_' by removing the prefix.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def clean_temp_keys(**kwargs):  # Function definition: clean_temp_keys
    return {k[5:] if k.startswith('temp_') else k: v for k, v in kwargs.items()}  # Return the result

print(clean_temp_keys(temp_x=1, y=2))  # Expected: {'x': 1, 'y': 2}

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python function that accepts **kwargs and returns only those key-value pairs where the key is uppercase.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1400
Write a Python function that accepts **kwargs and returns only those key-value pairs where the key is uppercase.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def uppercase_keys_only(**kwargs):  # Function definition: uppercase_keys_only
    return {k: v for k, v in kwargs.items() if k.isupper()}  # Return the result

print(uppercase_keys_only(AGE=30, name="Ann"))  # Expected: {'AGE': 30}

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `enumerate()` to get both index and value from a list.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1402
Write a Pythonic way to use `enumerate()` to get both index and value from a list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

fruits = ['apple', 'banana', 'cherry']  # Initialize list
for index, value in enumerate(fruits):  # Loop through items
    print(f"{index}: {value}")  # Expected: 0: apple, 1: banana, 2: cherry

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `zip()` to combine two lists into a list of tuples.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1403
Write a Pythonic way to use `zip()` to combine two lists into a list of tuples.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

names = ['Alice', 'Bob', 'Charlie']  # Initialize list
ages = [25, 30, 35]  # Initialize list
combined = list(zip(names, ages))  # Variable assignment
print(combined)  # Expected: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use a dictionary comprehension to swap keys and values.
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
Problem: 1404
Write a Pythonic way to use a dictionary comprehension to swap keys and values.
"""

# SOLUTION EXPLANATION:
# This solution uses a list comprehension to create a new list based on the
# specified conditions. List comprehensions are concise, readable, and often
# more efficient than equivalent loops for creating lists.

original = {'a': 1, 'b': 2, 'c': 3}  # Initialize dictionary
swapped = {v: k for k, v in original.items()}  # Initialize dictionary
print(swapped)  # Expected: {1: 'a', 2: 'b', 3: 'c'}

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `all()` to check if all elements in a list satisfy a condition.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1405
Write a Pythonic way to use `all()` to check if all elements in a list satisfy a condition.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

numbers = [2, 4, 6, 8]  # Initialize list
all_even = all(x % 2 == 0 for x in numbers)  # Variable assignment
print(all_even)  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to flatten a list of lists using a list comprehension.
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
Problem: 1406
Write a Pythonic way to flatten a list of lists using a list comprehension.
"""

# SOLUTION EXPLANATION:
# This solution uses a list comprehension to create a new list based on the
# specified conditions. List comprehensions are concise, readable, and often
# more efficient than equivalent loops for creating lists.

nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]  # Initialize list
flattened = [item for sublist in nested for item in sublist]  # List comprehension: creates a new list
print(flattened)  # Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `map()` to convert a list of strings to uppercase.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1407
Write a Pythonic way to use `map()` to convert a list of strings to uppercase.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

words = ['hello', 'world', 'python']  # Initialize list
uppercase_words = list(map(str.upper, words))  # Variable assignment
print(uppercase_words)  # Expected: ['HELLO', 'WORLD', 'PYTHON']

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `filter()` with a lambda to get even numbers from a list.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1408
Write a Pythonic way to use `filter()` with a lambda to get even numbers from a list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Initialize list
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # Variable assignment
print(even_numbers)  # Expected: [2, 4, 6, 8, 10]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `set()` to remove duplicates from a list while preserving order using dict.fromkeys().
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1409
Write a Pythonic way to use `set()` to remove duplicates from a list while preserving order using dict.fromkeys().
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

items = [1, 2, 2, 3, 3, 3, 4, 5, 5]  # Initialize list
unique_ordered = list(dict.fromkeys(items))  # Variable assignment
print(unique_ordered)  # Expected: [1, 2, 3, 4, 5]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `str.join()` to concatenate a list of strings with a separator.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1410
Write a Pythonic way to use `str.join()` to concatenate a list of strings with a separator.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

words = ['Python', 'is', 'great']  # Initialize list
sentence = ' '.join(words)  # Initialize string variable
print(sentence)  # Expected: Python is great

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use list slicing to reverse a string.
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
Problem: 1411
Write a Pythonic way to use list slicing to reverse a string.
"""

# SOLUTION EXPLANATION:
# This solution uses Python's slicing syntax to extract the desired portion
# of the sequence. Slicing is efficient and readable, making it the preferred
# method for extracting subsequences from strings, lists, and tuples.

text = "Python"  # Initialize string variable
reversed_text = text[::-1]  # Slice: reverse the sequence
print(reversed_text)  # Expected: nohtyP

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `collections.Counter` to count character frequencies in a string.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1412
Write a Pythonic way to use `collections.Counter` to count character frequencies in a string.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

from collections import Counter  # Import module or function
text = "hello world"  # Initialize string variable
char_counts = Counter(text)  # Variable assignment
print(char_counts)  # Expected: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `itertools.chain()` to combine multiple lists into one.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1413
Write a Pythonic way to use `itertools.chain()` to combine multiple lists into one.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

from itertools import chain  # Import module or function
list1 = [1, 2, 3]  # Initialize list
list2 = [4, 5, 6]  # Initialize list
list3 = [7, 8, 9]  # Initialize list
combined = list(chain(list1, list2, list3))  # Variable assignment
print(combined)  # Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `str.split()` and list comprehension to capitalize each word.
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
Problem: 1414
Write a Pythonic way to use `str.split()` and list comprehension to capitalize each word.
"""

# SOLUTION EXPLANATION:
# This solution uses a list comprehension to create a new list based on the
# specified conditions. List comprehensions are concise, readable, and often
# more efficient than equivalent loops for creating lists.

text = "hello world python"  # Initialize string variable
capitalized = ' '.join(word.capitalize() for word in text.split())  # Split string into a list
print(capitalized)  # Expected: Hello World Python

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `zip()` with `*` to transpose a list of lists.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1415
Write a Pythonic way to use `zip()` with `*` to transpose a list of lists.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Initialize list
transposed = list(zip(*matrix))  # Variable assignment
print(transposed)  # Expected: [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `dict.get()` with a default value to safely access dictionary keys.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1416
Write a Pythonic way to use `dict.get()` with a default value to safely access dictionary keys.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

data = {'name': 'Alice', 'age': 30}  # Initialize dictionary
name = data.get('name', 'Unknown')  # Variable assignment
city = data.get('city', 'Unknown')  # Variable assignment
print(name, city)  # Expected: Alice Unknown

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `collections.defaultdict` to group items by a key.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1417
Write a Pythonic way to use `collections.defaultdict` to group items by a key.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

from collections import defaultdict  # Import module or function
items = [('fruit', 'apple'), ('fruit', 'banana'), ('vegetable', 'carrot'), ('fruit', 'cherry')]  # Initialize list
grouped = defaultdict(list)  # Variable assignment
for category, item in items:  # Loop through items
    grouped[category].append(item)  # Method or function call
print(dict(grouped))  # Expected: {'fruit': ['apple', 'banana', 'cherry'], 'vegetable': ['carrot']}

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `itertools.groupby()` to group consecutive identical elements.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1418
Write a Pythonic way to use `itertools.groupby()` to group consecutive identical elements.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

from itertools import groupby  # Import module or function
data = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4]  # Initialize list
grouped = {k: list(g) for k, g in groupby(data)}  # Initialize dictionary
print(grouped)  # Expected: {1: [1, 1, 1], 2: [2, 2], 3: [3, 3, 3, 3], 4: [4]}

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `str.maketrans()` and `str.translate()` to replace multiple characters.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1419
Write a Pythonic way to use `str.maketrans()` and `str.translate()` to replace multiple characters.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

text = "hello world"  # Initialize string variable
translation = str.maketrans('lo', '12')  # Variable assignment
result = text.translate(translation)  # Variable assignment
print(result)  # Expected: he112 w2r1d

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `frozenset()` to create an immutable set for use as a dictionary key.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1420
Write a Pythonic way to use `frozenset()` to create an immutable set for use as a dictionary key.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

fs1 = frozenset([1, 2, 3])  # Variable assignment
fs2 = frozenset([4, 5, 6])  # Variable assignment
mapping = {fs1: 'first', fs2: 'second'}  # Initialize dictionary
print(mapping[fs1])  # Expected: first

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `itertools.combinations()` to generate all pairs from a list.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1421
Write a Pythonic way to use `itertools.combinations()` to generate all pairs from a list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

from itertools import combinations  # Import module or function
items = ['a', 'b', 'c', 'd']  # Initialize list
pairs = list(combinations(items, 2))  # Variable assignment
print(pairs)  # Expected: [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `collections.deque` to implement a queue with append and popleft.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1422
Write a Pythonic way to use `collections.deque` to implement a queue with append and popleft.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

from collections import deque  # Import module or function
queue = deque()  # Variable assignment
queue.append(1)  # Method or function call
queue.append(2)  # Method or function call
queue.append(3)  # Method or function call
first = queue.popleft()  # Variable assignment
print(first, list(queue))  # Expected: 1 [2, 3]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `str.partition()` to split a string at the first occurrence of a delimiter.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1423
Write a Pythonic way to use `str.partition()` to split a string at the first occurrence of a delimiter.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

text = "hello:world:python"  # Initialize string variable
before, sep, after = text.partition(':')  # Variable assignment
print(before, after)  # Expected: hello world:python

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `operator.itemgetter()` to sort a list of dictionaries by a key.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1424
Write a Pythonic way to use `operator.itemgetter()` to sort a list of dictionaries by a key.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

from operator import itemgetter  # Import module or function
people = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]  # Initialize list
sorted_people = sorted(people, key=itemgetter('age'))  # Variable assignment
print(sorted_people)  # Expected: [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `contextlib.suppress()` to ignore specific exceptions.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1425
Write a Pythonic way to use `contextlib.suppress()` to ignore specific exceptions.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

from contextlib import suppress  # Import module or function
with suppress(ValueError, ZeroDivisionError):  # Code block
    result = int("not a number")  # This would raise ValueError, but it's suppressed  # Variable assignment
    print("This won't print")  # Print the result
print("Continues after exception")  # Expected: Continues after exception

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to check if any item in a list is true.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1426
Write a Pythonic way to check if any item in a list is true.
"""

# SOLUTION EXPLANATION:
# This solution uses the 'is' operator to check object identity. This is
# different from '==' which checks value equality.

lst = [0, False, 5]  # Initialize list
print(any(lst))  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use a generator expression to calculate the sum of squares.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1427
Write a Pythonic way to use a generator expression to calculate the sum of squares.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

lst = [1, 2, 3]  # Initialize list
total = sum(x**2 for x in lst)  # Variable assignment
print(total)  # Expected: 14

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic program to get the intersection of two sets.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1428
Write a Pythonic program to get the intersection of two sets.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

a = {1, 2, 3}  # Initialize dictionary
b = {2, 3, 4}  # Initialize dictionary
print(a & b)  # Expected: {2, 3}

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic program to get the union of two sets.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1429
Write a Pythonic program to get the union of two sets.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

print(a | b)  # Expected: {1, 2, 3, 4}

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to check if a string contains only digits.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1430
Write a Pythonic way to check if a string contains only digits.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

s = "12345"  # Initialize string variable
print(s.isdigit())  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic one-liner to reverse a list.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1431
Write a Pythonic one-liner to reverse a list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

lst = [1, 2, 3]  # Initialize list
print(lst[::-1])  # Expected: [3, 2, 1]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to zip dictionary keys and values into a list of tuples.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1432
Write a Pythonic way to zip dictionary keys and values into a list of tuples.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

d = {'a': 1, 'b': 2}  # Initialize dictionary
zipped = list(zip(d.keys(), d.values()))  # Variable assignment
print(zipped)  # Expected: [('a', 1), ('b', 2)]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to initialize a dictionary with default integer values.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1433
Write a Pythonic way to initialize a dictionary with default integer values.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

from collections import defaultdict  # Import module or function
d = defaultdict(int)  # Variable assignment
d["x"] += 1
print(d["x"])  # Expected: 1

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic program to group elements by length from a list of words.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1434
Write a Pythonic program to group elements by length from a list of words.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

words = ["hi", "hello", "yes", "no"]  # Initialize list
from collections import defaultdict  # Import module or function
grouped = defaultdict(list)  # Variable assignment
for word in words:  # Loop through items
    grouped[len(word)].append(word)  # Method or function call
print(dict(grouped))  # Expected: {2: ['hi', 'no'], 5: ['hello'], 3: ['yes']}

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic program to sort a list of tuples by the second item.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1435
Write a Pythonic program to sort a list of tuples by the second item.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

lst = [(1, 3), (2, 1), (4, 2)]  # Initialize list
sorted_lst = sorted(lst, key=lambda x: x[1])  # Slice: extract a portion of the sequence
print(sorted_lst)  # Expected: [(2, 1), (4, 2), (1, 3)]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use a context manager to read a file.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1436
Write a Pythonic way to use a context manager to read a file.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

# Simulated context manager example
with open("temp.txt", "w") as f:  # Code block
    f.write("Hello")  # Method or function call
with open("temp.txt") as f:  # Code block
    print(f.read())  # Expected: "Hello"

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic one-liner to find the maximum item in a list.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1437
Write a Pythonic one-liner to find the maximum item in a list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

lst = [1, 5, 2]  # Initialize list
print(max(lst))  # Expected: 5

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to assign multiple variables from a list.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1438
Write a Pythonic way to assign multiple variables from a list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

lst = [1, 2, 3]  # Initialize list
a, b, c = lst  # Variable assignment
print(a, b, c)  # Expected: 1 2 3

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to create a dictionary from two lists.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1439
Write a Pythonic way to create a dictionary from two lists.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

keys = ['a', 'b']  # Initialize list
values = [1, 2]  # Initialize list
d = dict(zip(keys, values))  # Variable assignment
print(d)  # Expected: {'a': 1, 'b': 2}

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to remove a key from a dictionary if it exists.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1440
Write a Pythonic way to remove a key from a dictionary if it exists.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

d = {'a': 1, 'b': 2}  # Initialize dictionary
d.pop('b', None)  # Method or function call
print(d)  # Expected: {'a': 1}

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to check if a variable is None.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1441
Write a Pythonic way to check if a variable is None.
"""

# SOLUTION EXPLANATION:
# This solution uses the 'is' operator to check object identity. This is
# different from '==' which checks value equality.

x = None  # Variable assignment
print(x is None)  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to handle a missing dictionary key using try-except.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1442
Write a Pythonic way to handle a missing dictionary key using try-except.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

d = {'a': 1}  # Initialize dictionary
try:  # Code block
    print(d['b'])  # Print the result
except KeyError:  # Code block
    print("Key not found")  # Expected: Key not found

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to unpack a tuple into variables.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1443
Write a Pythonic way to unpack a tuple into variables.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

t = (1, 2)  # Initialize tuple
x, y = t  # Variable assignment
print(x, y)  # Expected: 1 2

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic one-liner to check if a list contains duplicates.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1444
Write a Pythonic one-liner to check if a list contains duplicates.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

lst = [1, 2, 2]  # Initialize list
print(len(lst) != len(set(lst)))  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic program to count character frequencies in a string.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1445
Write a Pythonic program to count character frequencies in a string.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

s = "banana"  # Initialize string variable
freq = Counter(s)  # Variable assignment
print(freq)  # Expected: {'b': 1, 'a': 3, 'n': 2}

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic one-liner to filter out negative numbers from a list.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1446
Write a Pythonic one-liner to filter out negative numbers from a list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

lst = [1, -2, 3, -4]  # Initialize list
print([x for x in lst if x >= 0])  # Expected: [1, 3]

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to test if a list has at least one even number.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1447
Write a Pythonic way to test if a list has at least one even number.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

lst = [1, 3, 4]  # Initialize list
print(any(x % 2 == 0 for x in lst))  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to get the index of an item in a list.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1448
Write a Pythonic way to get the index of an item in a list.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

lst = ['a', 'b', 'c']  # Initialize list
print(lst.index('b'))  # Expected: 1

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to filter dictionary items with values > 10.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1449
Write a Pythonic way to filter dictionary items with values > 10.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

d = {'a': 5, 'b': 15}  # Initialize dictionary
filtered = {k: v for k, v in d.items() if v > 10}  # Initialize dictionary
print(filtered)  # Expected: {'b': 15}

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic program to invert a dictionary (keys become values, values become keys).
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1450
Write a Pythonic program to invert a dictionary (keys become values, values become keys).
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

d = {'a': 1, 'b': 2}  # Initialize dictionary
inverted = {v: k for k, v in d.items()}  # Initialize dictionary
print(inverted)  # Expected: {1: 'a', 2: 'b'}

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program using `all()` to check if all numbers in a list are positive.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1451
Write a Python program using `all()` to check if all numbers in a list are positive.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

lst = [1, 2, 3, 4]  # Initialize list
print(all(x > 0 for x in lst))  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `all()` to determine if all characters in a string are lowercase.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1452
Use `all()` to determine if all characters in a string are lowercase.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

s = "hello"  # Initialize string variable
print(all(c.islower() for c in s))  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Pythonic way to use `all()` to check if all elements in a list are even.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1453
Write a Pythonic way to use `all()` to check if all elements in a list are even.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

lst = [2, 4, 6]  # Initialize list
print(all(x % 2 == 0 for x in lst))  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Check if all items in a dictionary have non-empty values using `all()`.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1454
Check if all items in a dictionary have non-empty values using `all()`.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

d = {"a": 1, "b": "hello", "c": [1]}  # Initialize dictionary
print(all(bool(v) for v in d.values()))  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `all()` to check if all items in a set are greater than 10.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1455
Use `all()` to check if all items in a set are greater than 10.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

s = {11, 12, 13}  # Initialize dictionary
print(all(x > 10 for x in s))  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `all()` to validate that all lines in a list start with a capital letter.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1456
Use `all()` to validate that all lines in a list start with a capital letter.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

lines = ["Hello", "World", "Python"]  # Initialize list
print(all(line[0].isupper() for line in lines))  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `all()` to check if all elements in a matrix row are equal.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1457
Use `all()` to check if all elements in a matrix row are equal.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

row = [5, 5, 5]  # Initialize list
print(all(x == row[0] for x in row))  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `all()` to check if all values in a list are strings.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1458
Use `all()` to check if all values in a list are strings.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

lst = ["a", "b", "c"]  # Initialize list
print(all(isinstance(x, str) for x in lst))  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program that uses `all()` to check if all keys in a dictionary are strings.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1459
Write a Python program that uses `all()` to check if all keys in a dictionary are strings.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

d = {"a": 1, "b": 2}  # Initialize dictionary
print(all(isinstance(k, str) for k in d.keys()))  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

""" 
Problem: 1460  
Use `all()` to verify that all files have a ".txt" extension.
"""
files = ["doc1.txt", "doc2.txt"]
print(all(f.endswith(".txt") for f in files))  # Expected: True


# ============================================================================
# PROBLEM EXPLANATION:
# Use `all()` to check if all numbers in a list are within a certain range.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1461
Use `all()` to check if all numbers in a list are within a certain range.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

nums = [5, 6, 7]  # Initialize list
print(all(1 <= x <= 10 for x in nums))  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Check if all sublists in a 2D list are non-empty using `all()`.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1462
Check if all sublists in a 2D list are non-empty using `all()`.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

matrix = [[1], [2], [3]]  # Initialize list
print(all(len(sublist) > 0 for sublist in matrix))  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `all()` to confirm all booleans in a list are True.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1463
Use `all()` to confirm all booleans in a list are True.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

flags = [True, True, True]  # Initialize list
print(all(flags))  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

""" 
Problem: 1464  
Use `all()` to verify all words in a list contain the letter "a".
"""
words = ["apple", "banana", "grape"]
print(all("a" in word for word in words))  # Expected: True


# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program using `all()` to check if a list of numbers is strictly increasing.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1465
Write a Python program using `all()` to check if a list of numbers is strictly increasing.
"""

# SOLUTION EXPLANATION:
# This solution uses the 'is' operator to check object identity. This is
# different from '==' which checks value equality.

nums = [1, 2, 3, 4]  # Initialize list
print(all(x < y for x, y in zip(nums, nums[1:])))  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Check if all environment variables in a list are defined (non-empty strings).
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1466
Check if all environment variables in a list are defined (non-empty strings).
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

envs = ["PATH", "HOME", "USER"]  # Initialize list
print(all(isinstance(env, str) and env for env in envs))  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `all()` to ensure all items in a tuple are of the same type.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1467
Use `all()` to ensure all items in a tuple are of the same type.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

t = (1, 2, 3)  # Initialize tuple
print(all(type(x) == type(t[0]) for x in t))  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Check if all numbers in a list are prime using `all()` and a helper function.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1468
Check if all numbers in a list are prime using `all()` and a helper function.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def is_prime(n):  # Function definition: is_prime
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1))  # Return the result

lst = [2, 3, 5, 7]  # Initialize list
print(all(is_prime(x) for x in lst))  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `all()` to confirm all values in a list are not None.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1469
Use `all()` to confirm all values in a list are not None.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

lst = [1, 2, 3]  # Initialize list
print(all(x is not None for x in lst))  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `all()` to verify that all passwords in a list are at least 8 characters long.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1470
Use `all()` to verify that all passwords in a list are at least 8 characters long.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

passwords = ["abcdefgh", "12345678", "password"]  # Initialize list
print(all(len(p) >= 8 for p in passwords))  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Write a Python program to check if a variable is `None` using `is`.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1471
Write a Python program to check if a variable is `None` using `is`.
"""

# SOLUTION EXPLANATION:
# This solution uses the 'is' operator to check object identity. This is
# different from '==' which checks value equality.

x = None  # Variable assignment
print(x is None)  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Check if two variables point to the same list object using `is`.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1472
Check if two variables point to the same list object using `is`.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

a = []  # Initialize list
b = a  # Variable assignment
print(a is b)  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Check if two separately created lists are not the same object using `is`.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1473
Check if two separately created lists are not the same object using `is`.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

a = []  # Initialize list
b = []  # Initialize list
print(a is not b)  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `is` to check if a variable is exactly `True`.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1474
Use `is` to check if a variable is exactly `True`.
"""

# SOLUTION EXPLANATION:
# This solution uses the 'is' operator to check object identity. This is
# different from '==' which checks value equality.

flag = True  # Variable assignment
print(flag is True)  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `is` to check identity of two strings (interned strings).
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1475
Use `is` to check identity of two strings (interned strings).
"""

# SOLUTION EXPLANATION:
# This solution uses the 'is' operator to check object identity. This is
# different from '==' which checks value equality.

s1 = "hello"  # Initialize string variable
s2 = "hello"  # Initialize string variable
print(s1 is s2)  # Expected: True (implementation detail in CPython)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `is` to check identity of small integers.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1476
Use `is` to check identity of small integers.
"""

# SOLUTION EXPLANATION:
# This solution uses the 'is' operator to check object identity. This is
# different from '==' which checks value equality.

a = 100  # Variable assignment
b = 100  # Variable assignment
print(a is b)  # Expected: True (due to integer caching)

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Check if a function return value is `None` using `is`.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1477
Check if a function return value is `None` using `is`.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def do_nothing():  # Function definition: do_nothing
    pass

print(do_nothing() is None)  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `is` to check if a class attribute is shared.
# 
# This problem demonstrates object-oriented programming concepts in Python.
# Classes are blueprints for creating objects, and they can have attributes
# (data) and methods (functions) that operate on that data.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1478
Use `is` to check if a class attribute is shared.
"""

# SOLUTION EXPLANATION:
# This solution uses the 'is' operator to check object identity. This is
# different from '==' which checks value equality.

class A:  # Class definition: A
    x = []  # Initialize list

a1 = A()  # Variable assignment
a2 = A()  # Variable assignment
print(a1.x is a2.x)  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `is` to check if an object is the same before and after a function call.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1479
Use `is` to check if an object is the same before and after a function call.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def identity(x):  # Function definition: identity
    return x  # Return the result

obj = []  # Initialize list
print(obj is identity(obj))  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `is` to compare with built-in singleton `Ellipsis`.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1480
Use `is` to compare with built-in singleton `Ellipsis`.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

x = ...  # Variable assignment
print(x is Ellipsis)  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Check if two instances of a class are not the same object.
# 
# This problem demonstrates object-oriented programming concepts in Python.
# Classes are blueprints for creating objects, and they can have attributes
# (data) and methods (functions) that operate on that data.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1481
Check if two instances of a class are not the same object.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

class X:  # Class definition: X
    pass

x1 = X()  # Variable assignment
x2 = X()  # Variable assignment
print(x1 is not x2)  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Check identity of two variables referencing the same dictionary.
# 
# This problem demonstrates dictionary operations in Python. Dictionaries are
# key-value pairs that allow efficient lookups and data organization. This
# problem may involve creating, accessing, modifying, or iterating over
# dictionary structures.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1482
Check identity of two variables referencing the same dictionary.
"""

# SOLUTION EXPLANATION:
# This solution uses the 'is' operator to check object identity. This is
# different from '==' which checks value equality.

d1 = {"a": 1}  # Initialize dictionary
d2 = d1  # Variable assignment
print(d1 is d2)  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `is` in an assertion to verify object identity.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1483
Use `is` in an assertion to verify object identity.
"""

# SOLUTION EXPLANATION:
# This solution uses the 'is' operator to check object identity. This is
# different from '==' which checks value equality.

a = b = object()  # Variable assignment
assert a is b  # Identity check
print("Assertion passed")  # Expected: Assertion passed

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Compare identity of two Boolean values using `is`.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1484
Compare identity of two Boolean values using `is`.
"""

# SOLUTION EXPLANATION:
# This solution uses the 'is' operator to check object identity. This is
# different from '==' which checks value equality.

x = (2 < 3)  # Initialize tuple
y = True  # Variable assignment
print(x is y)  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `is not` to verify a function argument is not None.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1485
Use `is not` to verify a function argument is not None.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

def greet(name):  # Function definition: greet
    if name is not None:  # Conditional check
        print(f"Hello, {name}!")  # Print the result

greet("Alice")  # Expected: Hello, Alice!

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `is` to test if a global constant is unchanged.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1486
Use `is` to test if a global constant is unchanged.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

SENTINEL = object()  # Variable assignment
def check(x):  # Function definition: check
    return x is SENTINEL  # Return the result

value = SENTINEL  # Variable assignment
print(check(value))  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Check that changing a variable makes it no longer the same object.
# 
# This problem demonstrates Python programming concepts and syntax.
# It requires understanding of basic Python operations, data structures, and
# control flow to solve effectively.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1487
Check that changing a variable makes it no longer the same object.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

a = [1, 2]  # Initialize list
b = a  # Variable assignment
a = [1, 2]  # Initialize list
print(a is b)  # Expected: False

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `is` to compare with a constant declared elsewhere.
# 
# This problem demonstrates regular expressions (regex) in Python. Regular
# expressions are powerful patterns for matching and manipulating text.
# They allow complex string searches, replacements, and validations.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1488
Use `is` to compare with a constant declared elsewhere.
"""

# SOLUTION EXPLANATION:
# This solution implements the required functionality using appropriate Python
# syntax and built-in functions to achieve the desired result.

NONE_CONST = None  # Variable assignment
x = None  # Variable assignment
print(x is NONE_CONST)  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `is` with `not` to check that a value is not `False`.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1489
Use `is` with `not` to check that a value is not `False`.
"""

# SOLUTION EXPLANATION:
# This solution uses the 'is' operator to check object identity. This is
# different from '==' which checks value equality.

value = "some text"  # Initialize string variable
print(value is not False)  # Expected: True

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Show that identity and equality are not always the same.
# 
# This problem demonstrates identity comparison using the 'is' operator in Python.
# The 'is' operator checks if two variables refer to the same object in memory,
# which is different from equality (==) which checks if values are equal.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1490
Show that identity and equality are not always the same.
"""

# SOLUTION EXPLANATION:
# This solution uses the 'is' operator to check object identity. This is
# different from '==' which checks value equality.

a = [1]  # Initialize list
b = [1]  # Initialize list
print(a == b)   # Expected: True
print(a is b)   # Expected: False

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `default=` with the `max()` function to return a default when the list is empty.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1491
Use `default=` with the `max()` function to return a default when the list is empty.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

nums = []  # Initialize list
print(max(nums, default=0))  # Expected: 0

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `default=` with the `min()` function to avoid an error on an empty sequence.
# 
# This problem demonstrates function definition and usage in Python. Functions
# allow code reuse and modularity. This problem may involve creating functions
# with specific parameters, return values, or handling edge cases.
# 
# Key Requirements:
# - Understand the problem statement and expected output
# - Use appropriate Python syntax and built-in functions
# - Handle edge cases and input validation if needed
# - Write clean, readable, and efficient code
# 
# Example Input/Output:
# - See the test cases below for expected behavior
# - The solution should produce the correct output for the given inputs
# ============================================================================

"""
Problem: 1492
Use `default=` with the `min()` function to avoid an error on an empty sequence.
"""

# SOLUTION EXPLANATION:
# This solution defines a function that performs the required operation.
# Functions encapsulate logic and make code reusable and testable.

values = []  # Initialize list
print(min(values, default=-1))  # Expected: -1

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `default=` in `max()` to safely get the longest word from a list.
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
Problem: 1493
Use `default=` in `max()` to safely get the longest word from a list.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

words = []  # Initialize list
print(max(words, key=len, default="None"))  # Expected: "None"

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `default=` with `next()` to get the first even number or -1.
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
Problem: 1494
Use `default=` with `next()` to get the first even number or -1.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

lst = [1, 3, 5]  # Initialize list
print(next((x for x in lst if x % 2 == 0), default=-1))  # Expected: -1

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `default=` in `next()` to safely access an item in a generator.
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
Problem: 1495
Use `default=` in `next()` to safely access an item in a generator.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

gen = (x for x in range(5) if x > 10)  # Variable assignment: create a range
print(next(gen, default="No item"))  # Expected: "No item"

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `default=` with `max()` on a filtered list to handle no matches.
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
Problem: 1496
Use `default=` with `max()` on a filtered list to handle no matches.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

nums = [1, 3, 5]  # Initialize list
print(max((x for x in nums if x % 2 == 0), default=None))  # Expected: None

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `default=` in `min()` to get a fallback value when no condition matches.
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
Problem: 1497
Use `default=` in `min()` to get a fallback value when no condition matches.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

nums = [1, 3, 5]  # Initialize list
print(min((x for x in nums if x % 2 == 0), default=-1))  # Expected: -1

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

""" 
Problem: 1498  
Use `default=` with `next()` to find the first name starting with "Z".
"""
names = ["Alice", "Bob"]
print(next((name for name in names if name.startswith("Z")), default="Not found"))  # Expected: "Not found"


# ============================================================================
# PROBLEM EXPLANATION:
# Use `default=` with `max()` to find the max in a sublist or return a placeholder.
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
Problem: 1499
Use `default=` with `max()` to find the max in a sublist or return a placeholder.
"""

# SOLUTION EXPLANATION:
# This solution uses the default parameter to provide a fallback value when
# the function encounters an empty sequence or no matching elements.

data = []  # Initialize list
print(max(data, default="empty"))  # Expected: "empty"

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

# ============================================================================
# PROBLEM EXPLANATION:
# Use `default=` in `next()` to handle an empty comprehension.
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
Problem: 1500
Use `default=` in `next()` to handle an empty comprehension.
"""

# SOLUTION EXPLANATION:
# This solution uses a list comprehension to create a new list based on the
# specified conditions. List comprehensions are concise, readable, and often
# more efficient than equivalent loops for creating lists.

print(next((x for x in []), default="Empty"))  # Expected: "Empty"

# TEST CASE:
# This test case demonstrates the functionality with example inputs.
# The output should match the expected result shown in the comments.

