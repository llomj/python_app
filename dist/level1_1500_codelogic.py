"""
Refined Prompt:
You are a Python code tutor and explainer. I will provide you with a Python script, and your task is to add detailed, line-by-line comments explaining everything happening in the code. For each line, include:

* The purpose of the line in the program's logic.
* Explanations of data types and how they are used.
* Details of control structures like `for` loops, `while` loops, `if` statements.
* Descriptions of built-in functions and any method calls.
* Any subtle Python behaviors that might affect execution.
* Explanations of the workflow: how data moves through the program, how functions interact, and the overall program flow.
* Examples or analogies to clarify concepts, when relevant.

Your comments should be verbose and educational, effectively turning the code into a learning guide for someone studying Python, from beginner to intermediate level. Preserve the original code structure and functionality, only adding explanatory comments above or beside each line.

Enhancements:

* Include occasional "learning notes" that highlight common pitfalls or best practices.
* Include a summary of the overall workflow of the program at the start and end, describing how all components interact.
* Color-code or format comments in a way that visually separates explanations from code, if possible in the environment.
* Optionally, summarize the overall logic of each function or block after explaining individual lines.
"""


# ======================================================================
# ORIGINAL CODE SOURCE: level1_1500.py
# ======================================================================




"""
Problem: 1001
Write a Python program to reverse a list using slicing.
"""

# ======================================================================
# PROBLEM 1001 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


numbers = [1, 2, 3, 4, 5]                                # [Line 13] | ASSIGNMENT: Creates variable 'numbers' and stores the result of '[1, 2, 3, 4, 5]' in it | DATA TYPE: List - A mutable ordered collection. Contains 5 elements
reversed_list = numbers[::-1]                            # [Line 14] | SLICING OPERATION [::-1] - This is a reverse slice. The syntax [::-1] means: start at the beginning (no start index), stop at the end (no stop index), and step backwards by 1. This effectively reverses the entire sequence. Example: [1,2,3][::-1] becomes [3,2,1] | ASSIGNMENT: Creates variable 'reversed_list' and stores the result of 'numbers[::-1]' in it | SUBSCRIPTION: Accesses an element or slice from a sequence using []
print(reversed_list)                                     # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: [5, 4, 3, 2, 1]


"""
Problem: 1002
Write a Python program to extract every third element from a list.
"""

# ======================================================================
# PROBLEM 1002 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


numbers = [10, 20, 30, 40, 50, 60, 70, 80]               # [Line 13] | ASSIGNMENT: Creates variable 'numbers' and stores the result of '[10, 20, 30, 40, 50, 60, 70, 80]' in it | DATA TYPE: List - A mutable ordered collection. Contains 8 elements
sliced_list = numbers[::3]                               # [Line 14] | SLICING OPERATION [::3] - Extracts every 3th element. The step value of 3 means we skip 2 elements between each selected element. No start index means begin from the start (or end if step is negative). No stop index means go to the end (or beginning if step is negative).  | ASSIGNMENT: Creates variable 'sliced_list' and stores the result of 'numbers[::3]' in it | SUBSCRIPTION: Accesses an element or slice from a sequence using []
print(sliced_list)                                       # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: [10, 40, 70]


"""
Problem: 1003
Write a Python program to extract every second character from a string in reverse order.
"""

# ======================================================================
# PROBLEM 1003 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "abcdefghij"                                      # [Line 13] | ASSIGNMENT: Creates variable 'text' and stores the result of ''abcdefghij'' in it | DATA TYPE: String - A sequence of characters. Length: 10
sliced_text = text[::-2]                                 # [Line 14] | SLICING OPERATION [::-2] - Reverses the sequence with step -2. Negative step means we traverse backwards. No start index means begin from the start (or end if step is negative). No stop index means go to the end (or beginning if step is negative).  | ASSIGNMENT: Creates variable 'sliced_text' and stores the result of 'text[::-2]' in it | SUBSCRIPTION: Accesses an element or slice from a sequence using []
print(sliced_text)                                       # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: jhfdb


"""
Problem: 1004
Write a Python program to slice the middle three characters from a string with an odd length.
"""

# ======================================================================
# PROBLEM 1004 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "abcdefg"                                         # [Line 13] | ASSIGNMENT: Creates variable 'text' and stores the result of ''abcdefg'' in it | DATA TYPE: String - A sequence of characters. Length: 7
middle_index = len(text) // 2                            # [Line 14] | FLOOR DIVISION (//) - Divides two numbers and returns the largest integer less than or equal to the result. Example: 7 // 2 = 3 (not 3.5). This is useful for integer division when you don't want decimal results. | ASSIGNMENT: Creates variable 'middle_index' and stores the result of 'len(text) // 2' in it | BINARY OPERATION: Performs a calculation between two operands
sliced_text = text[middle_index - 1: middle_index + 2]   # [Line 15] | SLICING OPERATION - Extracts a portion of the sequence | ASSIGNMENT: Creates variable 'sliced_text' and stores the result of 'text[middle_index - 1:middle_index + 2]' in it | SUBSCRIPTION: Accesses an element or slice from a sequence using []
print(sliced_text)                                       # [Line 16] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: cde


"""
Problem: 1005
Write a Python program to remove the first and last characters from a string using slicing.
"""

# ======================================================================
# PROBLEM 1005 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "Python"                                          # [Line 13] | ASSIGNMENT: Creates variable 'text' and stores the result of ''Python'' in it | DATA TYPE: String - A sequence of characters. Length: 6
sliced_text = text[1:-1]                                 # [Line 14] | SLICING OPERATION [1:-1] - Extracts elements from index 1 to -2 (stop is exclusive).  | ASSIGNMENT: Creates variable 'sliced_text' and stores the result of 'text[1:-1]' in it | SUBSCRIPTION: Accesses an element or slice from a sequence using []
print(sliced_text)                                       # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: ytho


"""
Problem: 1006
Write a Python program to get the first half of a string using slicing.
"""

# ======================================================================
# PROBLEM 1006 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "abcdefgh"                                        # [Line 13] | ASSIGNMENT: Creates variable 'text' and stores the result of ''abcdefgh'' in it | DATA TYPE: String - A sequence of characters. Length: 8
sliced_text = text[:len(text) // 2]                      # [Line 14] | SLICING OPERATION - Extracts a portion of the sequence | FLOOR DIVISION (//) - Divides two numbers and returns the largest integer less than or equal to the result. Example: 7 // 2 = 3 (not 3.5). This is useful for integer division when you don't want decimal results. | ASSIGNMENT: Creates variable 'sliced_text' and stores the result of 'text[:len(text) // 2]' in it | SUBSCRIPTION: Accesses an element or slice from a sequence using []
print(sliced_text)                                       # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: abcd


"""
Problem: 1007
Write a Python program to get the second half of a string using slicing.
"""

# ======================================================================
# PROBLEM 1007 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "abcdefgh"                                        # [Line 13] | ASSIGNMENT: Creates variable 'text' and stores the result of ''abcdefgh'' in it | DATA TYPE: String - A sequence of characters. Length: 8
sliced_text = text[len(text) // 2:]                      # [Line 14] | SLICING OPERATION - Extracts a portion of the sequence | FLOOR DIVISION (//) - Divides two numbers and returns the largest integer less than or equal to the result. Example: 7 // 2 = 3 (not 3.5). This is useful for integer division when you don't want decimal results. | ASSIGNMENT: Creates variable 'sliced_text' and stores the result of 'text[len(text) // 2:]' in it | SUBSCRIPTION: Accesses an element or slice from a sequence using []
print(sliced_text)                                       # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: efgh


"""
Problem: 1008
Write a Python program to extract the middle two characters from an even-length string.
"""

# ======================================================================
# PROBLEM 1008 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "abcdef"                                          # [Line 13] | ASSIGNMENT: Creates variable 'text' and stores the result of ''abcdef'' in it | DATA TYPE: String - A sequence of characters. Length: 6
middle_index = len(text) // 2                            # [Line 14] | FLOOR DIVISION (//) - Divides two numbers and returns the largest integer less than or equal to the result. Example: 7 // 2 = 3 (not 3.5). This is useful for integer division when you don't want decimal results. | ASSIGNMENT: Creates variable 'middle_index' and stores the result of 'len(text) // 2' in it | BINARY OPERATION: Performs a calculation between two operands
sliced_text = text[middle_index - 1: middle_index + 1]   # [Line 15] | SLICING OPERATION - Extracts a portion of the sequence | ASSIGNMENT: Creates variable 'sliced_text' and stores the result of 'text[middle_index - 1:middle_index + 1]' in it | SUBSCRIPTION: Accesses an element or slice from a sequence using []
print(sliced_text)                                       # [Line 16] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: cd


"""
Problem: 1009
Write a Python program to remove the first three elements from a list using slicing.
"""

# ======================================================================
# PROBLEM 1009 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


numbers = [1, 2, 3, 4, 5, 6]                             # [Line 13] | ASSIGNMENT: Creates variable 'numbers' and stores the result of '[1, 2, 3, 4, 5, 6]' in it | DATA TYPE: List - A mutable ordered collection. Contains 6 elements
sliced_list = numbers[3:]                                # [Line 14] | SLICING OPERATION [3:] - Extracts all elements starting from index 3 to the end.  | ASSIGNMENT: Creates variable 'sliced_list' and stores the result of 'numbers[3:]' in it | SUBSCRIPTION: Accesses an element or slice from a sequence using []
print(sliced_list)                                       # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: [4, 5, 6]


"""
Problem: 1010
Write a Python program to remove the last two elements from a tuple using slicing.
"""

# ======================================================================
# PROBLEM 1010 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


numbers = (10, 20, 30, 40, 50)                           # [Line 13] | ASSIGNMENT: Creates variable 'numbers' and stores the result of '(10, 20, 30, 40, 50)' in it | DATA TYPE: Tuple - An immutable ordered collection. Contains 5 elements
sliced_tuple = numbers[:-2]                              # [Line 14] | SLICING OPERATION [:-2] - Extracts elements from the beginning up to (but not including) index -2.  | ASSIGNMENT: Creates variable 'sliced_tuple' and stores the result of 'numbers[:-2]' in it | SUBSCRIPTION: Accesses an element or slice from a sequence using []
print(sliced_tuple)                                      # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: (10, 20, 30)


"""
Problem: 1011
Write a Python program to slice every alternate element from a list.
"""

# ======================================================================
# PROBLEM 1011 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


numbers = [1, 2, 3, 4, 5, 6, 7, 8]                       # [Line 13] | ASSIGNMENT: Creates variable 'numbers' and stores the result of '[1, 2, 3, 4, 5, 6, 7, 8]' in it | DATA TYPE: List - A mutable ordered collection. Contains 8 elements
sliced_list = numbers[::2]                               # [Line 14] | SLICING OPERATION [::2] - Extracts every 2th element. The step value of 2 means we skip 1 elements between each selected element. No start index means begin from the start (or end if step is negative). No stop index means go to the end (or beginning if step is negative).  | ASSIGNMENT: Creates variable 'sliced_list' and stores the result of 'numbers[::2]' in it | SUBSCRIPTION: Accesses an element or slice from a sequence using []
print(sliced_list)                                       # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: [1, 3, 5, 7]


"""
Problem: 1012
Write a Python program to extract a substring from index 3 to 7 using slicing.
"""

# ======================================================================
# PROBLEM 1012 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "PythonProgramming"                               # [Line 13] | ASSIGNMENT: Creates variable 'text' and stores the result of ''PythonProgramming'' in it | DATA TYPE: String - A sequence of characters. Length: 17
sliced_text = text[3:8]                                  # [Line 14] | SLICING OPERATION [3:8] - Extracts elements from index 3 to 7 (stop is exclusive).  | ASSIGNMENT: Creates variable 'sliced_text' and stores the result of 'text[3:8]' in it | SUBSCRIPTION: Accesses an element or slice from a sequence using []
print(sliced_text)                                       # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: honPr


"""
Problem: 1013
Write a Python program to extract a tuple slice from index 2 to 5.
"""

# ======================================================================
# PROBLEM 1013 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


numbers = (100, 200, 300, 400, 500, 600)                 # [Line 13] | ASSIGNMENT: Creates variable 'numbers' and stores the result of '(100, 200, 300, 400, 500, 600)' in it | DATA TYPE: Tuple - An immutable ordered collection. Contains 6 elements
sliced_tuple = numbers[2:6]                              # [Line 14] | SLICING OPERATION [2:6] - Extracts elements from index 2 to 5 (stop is exclusive).  | ASSIGNMENT: Creates variable 'sliced_tuple' and stores the result of 'numbers[2:6]' in it | SUBSCRIPTION: Accesses an element or slice from a sequence using []
print(sliced_tuple)                                      # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: (300, 400, 500, 600)


"""
Problem: 1014
Write a Python program to check if a string is a palindrome using slicing.
"""

# ======================================================================
# PROBLEM 1014 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def is_palindrome(s):                                    # [Line 13]
    return s == s[::-1]                                  # [Line 14] | SLICING OPERATION [::-1] - This is a reverse slice. The syntax [::-1] means: start at the beginning (no start index), stop at the end (no stop index), and step backwards by 1. This effectively reverses the entire sequence. Example: [1,2,3][::-1] becomes [3,2,1] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

print(is_palindrome("madam"))                            # [Line 16] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: True
print(is_palindrome("hello"))                            # [Line 17] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: False


"""
Problem: 1015
Write a Python program to extract the last three characters of a string using slicing.
"""

# ======================================================================
# PROBLEM 1015 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "Programming"                                     # [Line 13] | ASSIGNMENT: Creates variable 'text' and stores the result of ''Programming'' in it | DATA TYPE: String - A sequence of characters. Length: 11
sliced_text = text[-3:]                                  # [Line 14] | SLICING OPERATION [-3:] - Extracts from -3 positions from the end to the end of the sequence.  | ASSIGNMENT: Creates variable 'sliced_text' and stores the result of 'text[-3:]' in it | SUBSCRIPTION: Accesses an element or slice from a sequence using []
print(sliced_text)                                       # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: ing


"""
Problem: 1016
Write a Python program to extract the first five elements of a list using slicing.
"""

# ======================================================================
# PROBLEM 1016 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


numbers = [10, 20, 30, 40, 50, 60, 70]                   # [Line 13] | ASSIGNMENT: Creates variable 'numbers' and stores the result of '[10, 20, 30, 40, 50, 60, 70]' in it | DATA TYPE: List - A mutable ordered collection. Contains 7 elements
sliced_list = numbers[:5]                                # [Line 14] | SLICING OPERATION [:5] - Extracts elements from the beginning up to (but not including) index 5.  | ASSIGNMENT: Creates variable 'sliced_list' and stores the result of 'numbers[:5]' in it | SUBSCRIPTION: Accesses an element or slice from a sequence using []
print(sliced_list)                                       # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: [10, 20, 30, 40, 50]


"""
Problem: 1017
Write a Python program to extract all but the last three elements from a tuple using slicing.
"""

# ======================================================================
# PROBLEM 1017 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


numbers = (5, 10, 15, 20, 25, 30, 35)                    # [Line 13] | ASSIGNMENT: Creates variable 'numbers' and stores the result of '(5, 10, 15, 20, 25, 30, 35)' in it | DATA TYPE: Tuple - An immutable ordered collection. Contains 7 elements
sliced_tuple = numbers[:-3]                              # [Line 14] | SLICING OPERATION [:-3] - Extracts elements from the beginning up to (but not including) index -3.  | ASSIGNMENT: Creates variable 'sliced_tuple' and stores the result of 'numbers[:-3]' in it | SUBSCRIPTION: Accesses an element or slice from a sequence using []
print(sliced_tuple)                                      # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: (5, 10, 15, 20)


"""
Problem: 1018
Write a Python program to extract a string without its first and last two characters.
"""

# ======================================================================
# PROBLEM 1018 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "HelloWorld"                                      # [Line 13] | ASSIGNMENT: Creates variable 'text' and stores the result of ''HelloWorld'' in it | DATA TYPE: String - A sequence of characters. Length: 10
sliced_text = text[2:-2]                                 # [Line 14] | SLICING OPERATION [2:-2] - Extracts elements from index 2 to -3 (stop is exclusive).  | ASSIGNMENT: Creates variable 'sliced_text' and stores the result of 'text[2:-2]' in it | SUBSCRIPTION: Accesses an element or slice from a sequence using []
print(sliced_text)                                       # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: lloWor

"""
Problem: 1019
Write a Python program to create a list of squares of numbers from 1 to 10 using list comprehension.
"""

# ======================================================================
# PROBLEM 1019 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


squares = [x ** 2 for x in range(1, 11)]                 # [Line 13] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2. | ASSIGNMENT: Creates variable 'squares' and stores the result of '[x ** 2 for x in range(1, 11)]' in it
print(squares)                                           # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


"""
Problem: 1020
Write a Python program to create a list of even numbers from 1 to 20 using list comprehension.
"""

# ======================================================================
# PROBLEM 1020 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


evens = [x for x in range(1, 21) if x % 2 == 0]          # [Line 13] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1). | ASSIGNMENT: Creates variable 'evens' and stores the result of '[x for x in range(1, 21) if x % 2 == 0]' in it
print(evens)                                             # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


"""
Problem: 1021
Write a Python program to create a list of numbers from 1 to 50 that are divisible by 5 using list comprehension.
"""

# ======================================================================
# PROBLEM 1021 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


div_by_5 = [x for x in range(1, 51) if x % 5 == 0]       # [Line 13] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1). | ASSIGNMENT: Creates variable 'div_by_5' and stores the result of '[x for x in range(1, 51) if x % 5 == 0]' in it
print(div_by_5)                                          # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]


"""
Problem: 1022
Write a Python program to create a list of the first letter of each word in a given sentence using list comprehension.
"""

# ======================================================================
# PROBLEM 1022 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


sentence = "Python is a powerful programming language"   # [Line 13] | ASSIGNMENT: Creates variable 'sentence' and stores the result of ''Python is a powerful programming language'' in it | DATA TYPE: String - A sequence of characters. Length: 41
first_letters = [word[0] for word in sentence.split()]   # [Line 14] | ASSIGNMENT: Creates variable 'first_letters' and stores the result of '[word[0] for word in sentence.split()]' in it
print(first_letters)                                     # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: ['P', 'i', 'a', 'p', 'p', 'l']


"""
Problem: 1023
Write a Python program to create a list of words with more than three letters from a sentence using list comprehension.
"""

# ======================================================================
# PROBLEM 1023 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


sentence = "The sun is bright today"                     # [Line 13] | ASSIGNMENT: Creates variable 'sentence' and stores the result of ''The sun is bright today'' in it | DATA TYPE: String - A sequence of characters. Length: 23
long_words = [word for word in sentence.split() if len(word) > 3]  # [Line 14] | ASSIGNMENT: Creates variable 'long_words' and stores the result of '[word for word in sentence.split() if len(word) > 3]' in it
print(long_words)                                        # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: ['bright', 'today']


"""
Problem: 1024
Write a Python program to generate a list of tuples containing a number and its square for numbers from 1 to 10. List comprehension.
"""

# ======================================================================
# PROBLEM 1024 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


squares_tuples = [(x, x**2) for x in range(1, 11)]       # [Line 13] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2. | ASSIGNMENT: Creates variable 'squares_tuples' and stores the result of '[(x, x ** 2) for x in range(1, 11)]' in it
print(squares_tuples)                                    # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: [(1, 1), (2, 4), ..., (10, 100)]


"""
Problem: 1025
Write a Python program to create a new list where every element from an existing list is doubled. List comprehension.
"""

# ======================================================================
# PROBLEM 1025 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


numbers = [3, 5, 7, 9]                                   # [Line 13] | ASSIGNMENT: Creates variable 'numbers' and stores the result of '[3, 5, 7, 9]' in it | DATA TYPE: List - A mutable ordered collection. Contains 4 elements
doubled = [x * 2 for x in numbers]                       # [Line 14] | ASSIGNMENT: Creates variable 'doubled' and stores the result of '[x * 2 for x in numbers]' in it
print(doubled)                                           # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: [6, 10, 14, 18]


"""
Problem: 1026
Write a Python program to create a list of numbers from 1 to 100 that are either divisible by 3 or 7. List comprehension.
"""

# ======================================================================
# PROBLEM 1026 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


div_by_3_or_7 = [x for x in range(1, 101) if x % 3 == 0 or x % 7 == 0]  # [Line 13] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1). | ASSIGNMENT: Creates variable 'div_by_3_or_7' and stores the result of '[x for x in range(1, 101) if x % 3 == 0 or x % 7 == 0]' in it
print(div_by_3_or_7)                                     # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user


"""
Problem: 1027
Write a Python program to convert a list of strings to uppercase using list comprehension.
"""

# ======================================================================
# PROBLEM 1027 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


words = ["hello", "world", "python"]                     # [Line 13] | ASSIGNMENT: Creates variable 'words' and stores the result of '['hello', 'world', 'python']' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
upper_words = [word.upper() for word in words]           # [Line 14] | ASSIGNMENT: Creates variable 'upper_words' and stores the result of '[word.upper() for word in words]' in it
print(upper_words)                                       # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: ['HELLO', 'WORLD', 'PYTHON']


"""
Problem: 1028
Write a Python program to flatten a nested list using list comprehension.
"""

# ======================================================================
# PROBLEM 1028 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]          # [Line 13] | ASSIGNMENT: Creates variable 'nested_list' and stores the result of '[[1, 2, 3], [4, 5, 6], [7, 8, 9]]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
flattened = [num for sublist in nested_list for num in sublist]  # [Line 14] | ASSIGNMENT: Creates variable 'flattened' and stores the result of '[num for sublist in nested_list for num in sublist]' in it
print(flattened)                                         # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9]


"""
Problem: 1029
Write a Python program to create a list of vowels from a given string using list comprehension.
"""

# ======================================================================
# PROBLEM 1029 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "List Comprehension is Powerful"                  # [Line 13] | ASSIGNMENT: Creates variable 'text' and stores the result of ''List Comprehension is Powerful'' in it | DATA TYPE: String - A sequence of characters. Length: 30
vowels = [char for char in text if char.lower() in "aeiou"]  # [Line 14] | ASSIGNMENT: Creates variable 'vowels' and stores the result of '[char for char in text if char.lower() in 'aeiou']' in it
print(vowels)                                            # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: ['i', 'o', 'e', 'e', 'i', 'o', 'i', 'o', 'e']


"""
Problem: 1030
Write a Python program to extract only numeric values from a mixed list. List comprehension.
"""

# ======================================================================
# PROBLEM 1030 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


mixed_list = [10, "apple", 15.5, "banana", 30, "42"]     # [Line 13] | ASSIGNMENT: Creates variable 'mixed_list' and stores the result of '[10, 'apple', 15.5, 'banana', 30, '42']' in it | DATA TYPE: List - A mutable ordered collection. Contains 6 elements
numbers = [x for x in mixed_list if isinstance(x, (int, float))]  # [Line 14] | ASSIGNMENT: Creates variable 'numbers' and stores the result of '[x for x in mixed_list if isinstance(x, (int, float))]' in it
print(numbers)                                           # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: [10, 15.5, 30]


"""
Problem: 1031
Write a Python program to generate a list of first 10 Fibonacci numbers using list comprehension.
"""

# ======================================================================
# PROBLEM 1031 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


fib = [0, 1]                                             # [Line 13] | ASSIGNMENT: Creates variable 'fib' and stores the result of '[0, 1]' in it | DATA TYPE: List - A mutable ordered collection. Contains 2 elements
[fib.append(fib[-1] + fib[-2]) for _ in range(8)]        # [Line 14] | LIST COMPREHENSION - A concise way to create lists. The expression 'fib.append(fib[-1] + fib[-2])' is evaluated for each iteration. The variable '_' takes each value from 'range(8)]' during iteration. 
print(fib)                                               # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


"""
Problem: 1032
Write a Python program to create a list of prime numbers up to 50 using list comprehension.
"""

# ======================================================================
# PROBLEM 1032 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


primes = [x for x in range(2, 51) if all(x % y != 0 for y in range(2, int(x**0.5) + 1))]  # [Line 13] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1). | ASSIGNMENT: Creates variable 'primes' and stores the result of '[x for x in range(2, 51) if all((x % y != 0 for y in range(2, int(x ** 0.5) + 1)))]' in it
print(primes)                                            # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user


"""
Problem: 1033
Write a Python program to generate a list of all words in a sentence that end with a vowel. List comprehension.
"""

# ======================================================================
# PROBLEM 1033 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


sentence = "The apple is on the tree"                    # [Line 13] | ASSIGNMENT: Creates variable 'sentence' and stores the result of ''The apple is on the tree'' in it | DATA TYPE: String - A sequence of characters. Length: 24
vowel_ending_words = [word for word in sentence.split() if word[-1].lower() in "aeiou"]  # [Line 14] | ASSIGNMENT: Creates variable 'vowel_ending_words' and stores the result of '[word for word in sentence.split() if word[-1].lower() in 'aeiou']' in it
print(vowel_ending_words)                                # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: ['The', 'apple', 'is', 'tree']


"""
Problem: 1034
Write a Python program to create a list of lowercase characters from a given string. List comprehension.
"""

# ======================================================================
# PROBLEM 1034 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "Python List Comprehension"                       # [Line 13] | ASSIGNMENT: Creates variable 'text' and stores the result of ''Python List Comprehension'' in it | DATA TYPE: String - A sequence of characters. Length: 25
lower_chars = [char for char in text if char.islower()]  # [Line 14] | ASSIGNMENT: Creates variable 'lower_chars' and stores the result of '[char for char in text if char.islower()]' in it
print(lower_chars)                                       # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: ['y', 't', 'h', 'o', 'n', 'i', 's', 't', 'o', 'm', 'p', 'r', 'e', 'h', 'e', 'n', 's', 'i', 'o', 'n']


"""
Problem: 1035
Write a Python program to create a list of words with their lengths from a given sentence. List comprehension.
"""

# ======================================================================
# PROBLEM 1035 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


sentence = "List comprehension makes Python concise"     # [Line 13] | ASSIGNMENT: Creates variable 'sentence' and stores the result of ''List comprehension makes Python concise'' in it | DATA TYPE: String - A sequence of characters. Length: 39
word_lengths = [(word, len(word)) for word in sentence.split()]  # [Line 14] | ASSIGNMENT: Creates variable 'word_lengths' and stores the result of '[(word, len(word)) for word in sentence.split()]' in it
print(word_lengths)                                      # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: [('List', 4), ('comprehension', 13), ('makes', 5), ('Python', 6), ('concise', 7)]


"""
Problem: 1036
Write a Python program to remove duplicates from a list using list comprehension.
"""

# ======================================================================
# PROBLEM 1036 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


numbers = [1, 2, 2, 3, 4, 4, 5]                          # [Line 13] | ASSIGNMENT: Creates variable 'numbers' and stores the result of '[1, 2, 2, 3, 4, 4, 5]' in it | DATA TYPE: List - A mutable ordered collection. Contains 7 elements
unique_numbers = list(dict.fromkeys(numbers))            # [Line 14] | ASSIGNMENT: Creates variable 'unique_numbers' and stores the result of 'list(dict.fromkeys(numbers))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(unique_numbers)                                    # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: [1, 2, 3, 4, 5]


"""
Problem: 1037
Write a Python program to filter words containing the letter 'p' from a given list. List comprehension.
"""

# ======================================================================
# PROBLEM 1037 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


words = ["apple", "banana", "grape", "cherry", "peach"]  # [Line 13] | ASSIGNMENT: Creates variable 'words' and stores the result of '['apple', 'banana', 'grape', 'cherry', 'peach']' in it | DATA TYPE: List - A mutable ordered collection. Contains 5 elements
filtered_words = [word for word in words if "p" in word]  # [Line 14] | ASSIGNMENT: Creates variable 'filtered_words' and stores the result of '[word for word in words if 'p' in word]' in it
print(filtered_words)                                    # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: ['apple', 'grape', 'peach']

"""
Problem: 1038
Write a Python recursive function to calculate the factorial of a given number.
"""

# ======================================================================
# PROBLEM 1038 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def factorial(n):                                        # [Line 13]
    return 1 if n == 0 else n * factorial(n - 1)         # [Line 14] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

print(factorial(5))                                      # [Line 16] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: 120


"""
Problem: 1039
Write a Python recursive function to calculate the sum of all numbers from 1 to n.
"""

# ======================================================================
# PROBLEM 1039 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def sum_n(n):                                            # [Line 13]
    return n if n == 1 else n + sum_n(n - 1)             # [Line 14] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

print(sum_n(10))                                         # [Line 16] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: 55


"""
Problem: 1040
Write a Python recursive function to compute the nth Fibonacci number.
"""

# ======================================================================
# PROBLEM 1040 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def fibonacci(n):                                        # [Line 13]
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)  # [Line 14]

print(fibonacci(6))                                      # [Line 16] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: 8


"""
Problem: 1041
Write a Python recursive function to reverse a string.
"""

# ======================================================================
# PROBLEM 1041 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def reverse_string(s):                                   # [Line 13]
    return s if len(s) == 0 else s[-1] + reverse_string(s[:-1])  # [Line 14] | SLICING OPERATION [:-1] - Extracts elements from the beginning up to (but not including) index -1.  | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

print(reverse_string("hello"))                           # [Line 16] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: olleh


"""
Problem: 1042
Write a Python recursive function to count the number of digits in a given number.
"""

# ======================================================================
# PROBLEM 1042 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def count_digits(n):                                     # [Line 13]
    return 1 if n < 10 else 1 + count_digits(n // 10)    # [Line 14] | FLOOR DIVISION (//) - Divides two numbers and returns the largest integer less than or equal to the result. Example: 7 // 2 = 3 (not 3.5). This is useful for integer division when you don't want decimal results.

print(count_digits(12345))                               # [Line 16] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: 5


"""
Problem: 1043
Write a Python recursive function to find the greatest common divisor (GCD) of two numbers.
"""

# ======================================================================
# PROBLEM 1043 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def gcd(a, b):                                           # [Line 13]
    return a if b == 0 else gcd(b, a % b)                # [Line 14] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

print(gcd(48, 18))                                       # [Line 16] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: 6


"""
Problem: 1044
Write a Python recursive function to find the sum of elements in a list.
"""

# ======================================================================
# PROBLEM 1044 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def list_sum(lst):                                       # [Line 13]
    return 0 if not lst else lst[0] + list_sum(lst[1:])  # [Line 14] | SLICING OPERATION [1:] - Extracts all elements starting from index 1 to the end. 

print(list_sum([1, 2, 3, 4, 5]))                         # [Line 16] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: 15


"""
Problem: 1045
Write a Python recursive function to check if a number is a palindrome.
"""

# ======================================================================
# PROBLEM 1045 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def is_palindrome(n, temp=None):                         # [Line 13]
    if temp is None:                                     # [Line 14]
        temp = str(n)                                    # [Line 15]
    return True if len(temp) <= 1 else temp[0] == temp[-1] and is_palindrome(n, temp[1:-1])  # [Line 16] | SLICING OPERATION [1:-1] - Extracts elements from index 1 to -2 (stop is exclusive).  | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

print(is_palindrome(121))                                # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: True
print(is_palindrome(123))                                # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: False


"""
Problem: 1046
Write a Python recursive function to find the power of a number.
"""

# ======================================================================
# PROBLEM 1046 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def power(x, n):                                         # [Line 13]
    return 1 if n == 0 else x * power(x, n - 1)          # [Line 14] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

print(power(2, 3))                                       # [Line 16] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: 8


"""
Problem: 1047
Write a Python recursive function to compute the product of two numbers.
"""

# ======================================================================
# PROBLEM 1047 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def multiply(a, b):                                      # [Line 13]
    return 0 if b == 0 else a + multiply(a, b - 1)       # [Line 14] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

print(multiply(5, 4))                                    # [Line 16] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: 20


"""
Problem: 1048
Write a Python recursive function to print numbers from 1 to n.
"""

# ======================================================================
# PROBLEM 1048 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def print_numbers(n):                                    # [Line 13]
    if n > 0:                                            # [Line 14]
        print_numbers(n - 1)                             # [Line 15]
        print(n)                                         # [Line 16]

print_numbers(5)                                         # [Line 18] | FUNCTION CALL: Executes the function 'print_numbers' | ARGUMENTS: Passes 1 argument(s) to the function
# Expected output:
# 1
# 2
# 3
# 4
# 5


"""
Problem: 1049
Write a Python recursive function to print numbers from n to 1.
"""

# ======================================================================
# PROBLEM 1049 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def print_reverse(n):                                    # [Line 13]
    if n > 0:                                            # [Line 14]
        print(n)                                         # [Line 15]
        print_reverse(n - 1)                             # [Line 16]

print_reverse(5)                                         # [Line 18] | FUNCTION CALL: Executes the function 'print_reverse' | ARGUMENTS: Passes 1 argument(s) to the function
# Expected output:
# 5
# 4
# 3
# 2
# 1


"""
Problem: 1050
Write a Python recursive function to check if a list is sorted in ascending order.
"""

# ======================================================================
# PROBLEM 1050 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def is_sorted(lst):                                      # [Line 13]
    return True if len(lst) <= 1 else lst[0] <= lst[1] and is_sorted(lst[1:])  # [Line 14] | SLICING OPERATION [1:] - Extracts all elements starting from index 1 to the end. 

print(is_sorted([1, 2, 3, 4, 5]))                        # [Line 16] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: True
print(is_sorted([5, 3, 1]))                              # [Line 17] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: False


"""
Problem: 1051
Write a Python recursive function to count the occurrences of a character in a string.
"""

# ======================================================================
# PROBLEM 1051 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def char_count(s, c):                                    # [Line 13]
    return 0 if not s else (1 if s[0] == c else 0) + char_count(s[1:], c)  # [Line 14] | SLICING OPERATION [1:] - Extracts all elements starting from index 1 to the end.  | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

print(char_count("banana", "a"))                         # [Line 16] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: 3


"""
Problem: 1052
Write a Python recursive function to generate all binary strings of length n.
"""

# ======================================================================
# PROBLEM 1052 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def binary_strings(n, s=""):                             # [Line 13]
    if n == 0:                                           # [Line 14] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).
        print(s)                                         # [Line 15]
    else:                                                # [Line 16]
        binary_strings(n - 1, s + "0")                   # [Line 17]
        binary_strings(n - 1, s + "1")                   # [Line 18]

binary_strings(3)                                        # [Line 20] | FUNCTION CALL: Executes the function 'binary_strings' | ARGUMENTS: Passes 1 argument(s) to the function
# Expected output:
# 000
# 001
# 010
# 011
# 100
# 101
# 110
# 111


"""
Problem: 1053
Write a Python recursive function to compute the sum of digits of a number.
"""

# ======================================================================
# PROBLEM 1053 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def sum_of_digits(n):                                    # [Line 13]
    if n == 0:                                           # [Line 14] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).
        return 0                                         # [Line 15]
    # Recursive case: add the last digit to the sum of the remaining digits
    else:                                                # [Line 17]
        return n % 10 + sum_of_digits(n // 10)           # [Line 18] | FLOOR DIVISION (//) - Divides two numbers and returns the largest integer less than or equal to the result. Example: 7 // 2 = 3 (not 3.5). This is useful for integer division when you don't want decimal results.

string = 1244                                            # [Line 20] | ASSIGNMENT: Creates variable 'string' and stores the result of '1244' in it | DATA TYPE: Integer - A whole number: 1244
print(sum_of_digits(string))                             # [Line 21] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Output: 11

def sum_of_digits(n):                                    # [Line 23]
    return n if n < 10 else (n % 10) + sum_of_digits(n // 10)  # [Line 24] | FLOOR DIVISION (//) - Divides two numbers and returns the largest integer less than or equal to the result. Example: 7 // 2 = 3 (not 3.5). This is useful for integer division when you don't want decimal results.

print(sum_of_digits(1234))                               # [Line 26] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: 10


"""
Problem: 1054
Write a Python recursive function to calculate the nth triangular number.
"""

# ======================================================================
# PROBLEM 1054 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def triangular_number(n):                                # [Line 13]
    return 0 if n == 0 else n + triangular_number(n - 1)  # [Line 14] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

print(triangular_number(5))                              # [Line 16] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: 15


"""
Problem: 1055
Write a Python recursive function to remove duplicates from a string.
"""

# ======================================================================
# PROBLEM 1055 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def remove_duplicates(s, seen=""):                       # [Line 13]
    return "" if not s else (remove_duplicates(s[1:], seen) if s[0] in seen else s[0] + remove_duplicates(s[1:], seen + s[0]))  # [Line 14] | SLICING OPERATION [1:] - Extracts all elements starting from index 1 to the end. 

print(remove_duplicates("banana"))                       # [Line 16] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: ban


"""
Problem: 1056
Write a Python recursive function to generate all permutations of a given string.
"""

# ======================================================================
# PROBLEM 1056 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def permutations(s, prefix=""):                          # [Line 13]
    if not s:                                            # [Line 14]
        print(prefix)                                    # [Line 15]
    else:                                                # [Line 16]
        for i in range(len(s)):                          # [Line 17]
            permutations(s[:i] + s[i+1:], prefix + s[i])  # [Line 18] | SLICING OPERATION - Extracts a portion of the sequence

permutations("abc")                                      # [Line 20] | FUNCTION CALL: Executes the function 'permutations' | ARGUMENTS: Passes 1 argument(s) to the function
# Expected output:
# abc
# acb
# bac
# bca
# cab
# cba

"""
Problem: 1057
Write a Python program to find the longest string in a list using the `max()` function with a lambda expression.
"""

# ======================================================================
# PROBLEM 1057 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def longest_string(words):                               # [Line 13]
    return max(words, key=lambda word: len(word))        # [Line 14]

result = longest_string(["apple", "banana", "cherry"])   # [Line 16] | ASSIGNMENT: Creates variable 'result' and stores the result of 'longest_string(['apple', 'banana', 'cherry'])' in it | FUNCTION CALL: Calls 'longest_string()' and stores its return value
print(result)                                            # [Line 17] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1058
Write a Python program to check if a number is even using a lambda function.
"""

# ======================================================================
# PROBLEM 1058 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


is_even = lambda x: x % 2 == 0                           # [Line 13] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1). | ASSIGNMENT: Creates variable 'is_even' and stores the result of 'lambda x: x % 2 == 0' in it

result = is_even(4)                                      # [Line 15] | ASSIGNMENT: Creates variable 'result' and stores the result of 'is_even(4)' in it | FUNCTION CALL: Calls 'is_even()' and stores its return value
print(result)                                            # [Line 16] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1059
Write a Python program to calculate the square root of all elements in a list using a lambda function.
"""

# ======================================================================
# PROBLEM 1059 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import math                                              # [Line 13]

def square_roots(numbers):                               # [Line 15]
    return list(map(lambda x: math.sqrt(x), numbers))    # [Line 16]

result = square_roots([4, 9, 16])                        # [Line 18] | ASSIGNMENT: Creates variable 'result' and stores the result of 'square_roots([4, 9, 16])' in it | FUNCTION CALL: Calls 'square_roots()' and stores its return value
print(result)                                            # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1060
Write a Python program to check if a string contains any digits using a lambda function.
"""

# ======================================================================
# PROBLEM 1060 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


contains_digits = lambda s: any(map(str.isdigit, s))     # [Line 13] | ASSIGNMENT: Creates variable 'contains_digits' and stores the result of 'lambda s: any(map(str.isdigit, s))' in it

result = contains_digits("hello123")                     # [Line 15] | ASSIGNMENT: Creates variable 'result' and stores the result of 'contains_digits('hello123')' in it | FUNCTION CALL: Calls 'contains_digits()' and stores its return value
print(result)                                            # [Line 16] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1061
Write a Python program to sort a list of tuples based on the first element in descending order using a lambda expression.
"""

# ======================================================================
# PROBLEM 1061 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def sort_by_first_element_desc(tuples):                  # [Line 13]
    return sorted(tuples, key=lambda x: x[0], reverse=True)  # [Line 14] | SLICING OPERATION - Extracts a portion of the sequence

result = sort_by_first_element_desc([(3, "apple"), (1, "banana"), (2, "cherry")])  # [Line 16] | ASSIGNMENT: Creates variable 'result' and stores the result of 'sort_by_first_element_desc([(3, 'apple'), (1, 'banana'), (2, 'cherry')])' in it | FUNCTION CALL: Calls 'sort_by_first_element_desc()' and stores its return value
print(result)                                            # [Line 17] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1062
Write a Python program to filter out words that are shorter than a given length using the `filter()` function with a lambda expression.
"""

# ======================================================================
# PROBLEM 1062 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def filter_short_words(words, length):                   # [Line 13]
    return list(filter(lambda word: len(word) >= length, words))  # [Line 14]

result = filter_short_words(["apple", "banana", "cherry", "date"], 6)  # [Line 16] | ASSIGNMENT: Creates variable 'result' and stores the result of 'filter_short_words(['apple', 'banana', 'cherry', 'date'], 6)' in it | FUNCTION CALL: Calls 'filter_short_words()' and stores its return value
print(result)                                            # [Line 17] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1063
Write a Python program to double all elements in a list using a lambda function.
"""

# ======================================================================
# PROBLEM 1063 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def double_elements(numbers):                            # [Line 13]
    return list(map(lambda x: x * 2, numbers))           # [Line 14]

result = double_elements([1, 2, 3, 4])                   # [Line 16] | ASSIGNMENT: Creates variable 'result' and stores the result of 'double_elements([1, 2, 3, 4])' in it | FUNCTION CALL: Calls 'double_elements()' and stores its return value
print(result)                                            # [Line 17] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1064
Write a Python program to check if a number is divisible by 3 using a lambda function.
"""

# ======================================================================
# PROBLEM 1064 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


is_divisible_by_3 = lambda x: x % 3 == 0                 # [Line 13] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1). | ASSIGNMENT: Creates variable 'is_divisible_by_3' and stores the result of 'lambda x: x % 3 == 0' in it

result = is_divisible_by_3(9)                            # [Line 15] | ASSIGNMENT: Creates variable 'result' and stores the result of 'is_divisible_by_3(9)' in it | FUNCTION CALL: Calls 'is_divisible_by_3()' and stores its return value
print(result)                                            # [Line 16] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1065
Write a Python program to find the second largest number in a list using a lambda function.
"""

# ======================================================================
# PROBLEM 1065 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


second_largest = lambda numbers: sorted(set(numbers))[-2]  # [Line 13] | SLICING OPERATION - Extracts a portion of the sequence | ASSIGNMENT: Creates variable 'second_largest' and stores the result of 'lambda numbers: sorted(set(numbers))[-2]' in it

result = second_largest([10, 20, 30, 40, 50])            # [Line 15] | ASSIGNMENT: Creates variable 'result' and stores the result of 'second_largest([10, 20, 30, 40, 50])' in it | FUNCTION CALL: Calls 'second_largest()' and stores its return value
print(result)                                            # [Line 16] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1066
Write a Python program to map a list of numbers into their cubes using a lambda function.
"""

# ======================================================================
# PROBLEM 1066 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def cube_elements(numbers):                              # [Line 13]
    return list(map(lambda x: x ** 3, numbers))          # [Line 14] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.

result = cube_elements([1, 2, 3, 4])                     # [Line 16] | ASSIGNMENT: Creates variable 'result' and stores the result of 'cube_elements([1, 2, 3, 4])' in it | FUNCTION CALL: Calls 'cube_elements()' and stores its return value
print(result)                                            # [Line 17] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1067
Write a Python program to sort a list of words by their lengths using the `sorted()` function with a lambda expression.
"""

# ======================================================================
# PROBLEM 1067 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def sort_by_length(words):                               # [Line 13]
    return sorted(words, key=lambda word: len(word))     # [Line 14]

result = sort_by_length(["apple", "banana", "kiwi", "cherry"])  # [Line 16] | ASSIGNMENT: Creates variable 'result' and stores the result of 'sort_by_length(['apple', 'banana', 'kiwi', 'cherry'])' in it | FUNCTION CALL: Calls 'sort_by_length()' and stores its return value
print(result)                                            # [Line 17] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1068
Write a Python program to check if a number is odd using a lambda function.
"""

# ======================================================================
# PROBLEM 1068 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


is_odd = lambda x: x % 2 != 0                            # [Line 13] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1). | ASSIGNMENT: Creates variable 'is_odd' and stores the result of 'lambda x: x % 2 != 0' in it

result = is_odd(5)                                       # [Line 15] | ASSIGNMENT: Creates variable 'result' and stores the result of 'is_odd(5)' in it | FUNCTION CALL: Calls 'is_odd()' and stores its return value
print(result)                                            # [Line 16] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1069
Write a Python program to find the sum of all elements in a list using the `reduce()` function with a lambda expression.
"""

# ======================================================================
# PROBLEM 1069 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from functools import reduce                             # [Line 13]

def sum_of_elements(numbers):                            # [Line 15]
    return reduce(lambda x, y: x + y, numbers)           # [Line 16]

result = sum_of_elements([1, 2, 3, 4])                   # [Line 18] | ASSIGNMENT: Creates variable 'result' and stores the result of 'sum_of_elements([1, 2, 3, 4])' in it | FUNCTION CALL: Calls 'sum_of_elements()' and stores its return value
print(result)                                            # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1070
Write a Python program to check if a string ends with a vowel using a lambda function.
"""

# ======================================================================
# PROBLEM 1070 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


ends_with_vowel = lambda s: s[-1].lower() in 'aeiou'     # [Line 13] | SLICING OPERATION - Extracts a portion of the sequence | ASSIGNMENT: Creates variable 'ends_with_vowel' and stores the result of 'lambda s: s[-1].lower() in 'aeiou'' in it

result = ends_with_vowel("hello")                        # [Line 15] | ASSIGNMENT: Creates variable 'result' and stores the result of 'ends_with_vowel('hello')' in it | FUNCTION CALL: Calls 'ends_with_vowel()' and stores its return value
print(result)                                            # [Line 16] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1071
Write a Python program to find the smallest number in a list using the `min()` function with a lambda expression.
"""

# ======================================================================
# PROBLEM 1071 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


# Define a list of numbers
numbers = [12, 45, 7, 23, 56, 89, 34]                    # [Line 14] | ASSIGNMENT: Creates variable 'numbers' and stores the result of '[12, 45, 7, 23, 56, 89, 34]' in it | DATA TYPE: List - A mutable ordered collection. Contains 7 elements

# Use the min() function with a lambda expression to find the smallest number
smallest_number = min(numbers, key=lambda x: x)          # [Line 17] | ASSIGNMENT: Creates variable 'smallest_number' and stores the result of 'min(numbers, key=lambda x: x)' in it | FUNCTION CALL: Calls 'min()' and stores its return value

# Print the result
print("The smallest number in the list is:", smallest_number)  # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1072
Write a Python program to check if a string contains only alphabetic characters using a lambda function.
"""

# ======================================================================
# PROBLEM 1072 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


is_alpha = lambda s: s.isalpha()                         # [Line 13] | ASSIGNMENT: Creates variable 'is_alpha' and stores the result of 'lambda s: s.isalpha()' in it

result = is_alpha("hello")                               # [Line 15] | ASSIGNMENT: Creates variable 'result' and stores the result of 'is_alpha('hello')' in it | FUNCTION CALL: Calls 'is_alpha()' and stores its return value
print(result)                                            # [Line 16] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1073
Write a Python program to convert all integers in a list to strings using a lambda function.
"""

# ======================================================================
# PROBLEM 1073 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def convert_to_strings(numbers):                         # [Line 13]
    return list(map(lambda x: str(x), numbers))          # [Line 14]

result = convert_to_strings([1, 2, 3, 4])                # [Line 16] | ASSIGNMENT: Creates variable 'result' and stores the result of 'convert_to_strings([1, 2, 3, 4])' in it | FUNCTION CALL: Calls 'convert_to_strings()' and stores its return value
print(result)                                            # [Line 17] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1074
Write a Python program to find the sum of all even numbers in a list using a lambda expression.
"""

# ======================================================================
# PROBLEM 1074 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def sum_of_even(numbers):                                # [Line 13]
    return sum(filter(lambda x: x % 2 == 0, numbers))    # [Line 14] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = sum_of_even([1, 2, 3, 4, 5, 6])                 # [Line 16] | ASSIGNMENT: Creates variable 'result' and stores the result of 'sum_of_even([1, 2, 3, 4, 5, 6])' in it | FUNCTION CALL: Calls 'sum_of_even()' and stores its return value
print(result)                                            # [Line 17] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1075
Write a Python program to remove all whitespace from a string using a lambda function.
"""

# ======================================================================
# PROBLEM 1075 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


string = "i'm going for a walk"                          # [Line 13] | ASSIGNMENT: Creates variable 'string' and stores the result of '"i'm going for a walk"' in it | DATA TYPE: String - A sequence of characters. Length: 20
result = lambda char: char.replace(" ", "")              # [Line 14] | ASSIGNMENT: Creates variable 'result' and stores the result of 'lambda char: char.replace(' ', '')' in it

result(string)                                           # [Line 16] | FUNCTION CALL: Executes the function 'result' | ARGUMENTS: Passes 1 argument(s) to the function

remove_whitespace = lambda s: ''.join(s.split())         # [Line 18] | ASSIGNMENT: Creates variable 'remove_whitespace' and stores the result of 'lambda s: ''.join(s.split())' in it

result = remove_whitespace("hello world")                # [Line 20] | ASSIGNMENT: Creates variable 'result' and stores the result of 'remove_whitespace('hello world')' in it | FUNCTION CALL: Calls 'remove_whitespace()' and stores its return value
print(result)                                            # [Line 21] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1076
Write a Python program to count the number of even numbers in a list using a lambda function.
"""

# ======================================================================
# PROBLEM 1076 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


count_even = lambda numbers: len(list(filter(lambda x: x % 2 == 0, numbers)))  # [Line 13] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1). | ASSIGNMENT: Creates variable 'count_even' and stores the result of 'lambda numbers: len(list(filter(lambda x: x % 2 == 0, numbers)))' in it

result = count_even([1, 2, 3, 4, 5, 6])                  # [Line 15] | ASSIGNMENT: Creates variable 'result' and stores the result of 'count_even([1, 2, 3, 4, 5, 6])' in it | FUNCTION CALL: Calls 'count_even()' and stores its return value
print(result)                                            # [Line 16] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1077
Write a Python program to find the product of all odd numbers in a list using a lambda function.
"""

# ======================================================================
# PROBLEM 1077 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from functools import reduce                             # [Line 13]

product_of_odds = lambda numbers: reduce(lambda x, y: x * y, filter(lambda x: x % 2 != 0, numbers))  # [Line 15] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1). | ASSIGNMENT: Creates variable 'product_of_odds' and stores the result of 'lambda numbers: reduce(lambda x, y: x * y, filter(lambda x: x % 2 != 0, numbers))' in it

result = product_of_odds([1, 2, 3, 4, 5])                # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'product_of_odds([1, 2, 3, 4, 5])' in it | FUNCTION CALL: Calls 'product_of_odds()' and stores its return value
print(result)                                            # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1078
Write a Python program to check if a number is prime using a lambda function.
"""

# ======================================================================
# PROBLEM 1078 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


is_prime = lambda n: all(n % i != 0 for i in range(2, int(n ** 0.5) + 1)) if n > 1 else False  # [Line 13] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1). | ASSIGNMENT: Creates variable 'is_prime' and stores the result of 'lambda n: all((n % i != 0 for i in range(2, int(n ** 0.5) + 1))) if n > 1 else False' in it

result = is_prime(7)                                     # [Line 15] | ASSIGNMENT: Creates variable 'result' and stores the result of 'is_prime(7)' in it | FUNCTION CALL: Calls 'is_prime()' and stores its return value
print(result)                                            # [Line 16] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1079
Write a Python program to create a list of tuples (number, square root) for each number in a given list using a lambda function.
"""

# ======================================================================
# PROBLEM 1079 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import math                                              # [Line 13]

def create_square_root_tuples(numbers):                  # [Line 15]
    return list(map(lambda x: (x, math.sqrt(x)), numbers))  # [Line 16]

result = create_square_root_tuples([4, 9, 16])           # [Line 18] | ASSIGNMENT: Creates variable 'result' and stores the result of 'create_square_root_tuples([4, 9, 16])' in it | FUNCTION CALL: Calls 'create_square_root_tuples()' and stores its return value
print(result)                                            # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1080
Write a Python program to check if a string contains any uppercase letters using a lambda function.
"""

# ======================================================================
# PROBLEM 1080 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


contains_uppercase = lambda s: any(map(str.isupper, s))  # [Line 13] | ASSIGNMENT: Creates variable 'contains_uppercase' and stores the result of 'lambda s: any(map(str.isupper, s))' in it

result = contains_uppercase("Hello")                     # [Line 15] | ASSIGNMENT: Creates variable 'result' and stores the result of 'contains_uppercase('Hello')' in it | FUNCTION CALL: Calls 'contains_uppercase()' and stores its return value
print(result)                                            # [Line 16] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1081
Write a Python program to find the average of odd numbers in a list using a lambda function.
"""

# ======================================================================
# PROBLEM 1081 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def average_of_odds(lst):                                # [Line 13]
    odd = list(filter(lambda num: num % 2 !=0, lst))     # [Line 14] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
    total = sum(odd)                                     # [Line 15]
    count = len(odd)                                     # [Line 16]
    average = total / count                              # [Line 17]
    return average                                       # [Line 18]
lst = [1,2,3,4,5,6,7,8,9]                                # [Line 19] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[1, 2, 3, 4, 5, 6, 7, 8, 9]' in it | DATA TYPE: List - A mutable ordered collection. Contains 9 elements

average_of_odds(lst)                                     # [Line 21] | FUNCTION CALL: Executes the function 'average_of_odds' | ARGUMENTS: Passes 1 argument(s) to the function

def average_of_odds(numbers):                            # [Line 23]
    odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))  # [Line 24] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
    return sum(odd_numbers) / len(odd_numbers) if odd_numbers else 0  # [Line 25]

result = average_of_odds([1, 2, 3, 4, 5])                # [Line 27] | ASSIGNMENT: Creates variable 'result' and stores the result of 'average_of_odds([1, 2, 3, 4, 5])' in it | FUNCTION CALL: Calls 'average_of_odds()' and stores its return value
print(result)                                            # [Line 28] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1082
Write a Python program to create a list of squares for all odd numbers in a list using a lambda function.
"""

# ======================================================================
# PROBLEM 1082 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def square_odd_numbers(numbers):                         # [Line 13]
    return list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, numbers)))  # [Line 14] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = square_odd_numbers([1, 2, 3, 4, 5])             # [Line 16] | ASSIGNMENT: Creates variable 'result' and stores the result of 'square_odd_numbers([1, 2, 3, 4, 5])' in it | FUNCTION CALL: Calls 'square_odd_numbers()' and stores its return value
print(result)                                            # [Line 17] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1083
Write a Python program to check if a list contains any negative numbers using a lambda function.
"""

# ======================================================================
# PROBLEM 1083 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


contains_negative = lambda numbers: any(map(lambda x: x < 0, numbers))  # [Line 13] | ASSIGNMENT: Creates variable 'contains_negative' and stores the result of 'lambda numbers: any(map(lambda x: x < 0, numbers))' in it

result = contains_negative([1, -2, 3, 4])                # [Line 15] | ASSIGNMENT: Creates variable 'result' and stores the result of 'contains_negative([1, -2, 3, 4])' in it | FUNCTION CALL: Calls 'contains_negative()' and stores its return value
print(result)                                            # [Line 16] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1084
Write a Python program to create a list of tuples where the first element is the original number and the second element is its cube using a lambda function.
"""

# ======================================================================
# PROBLEM 1084 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def create_cube_tuples(numbers):                         # [Line 13]
    return list(map(lambda x: (x, x**3), numbers))       # [Line 14] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.

result = create_cube_tuples([1, 2, 3])                   # [Line 16] | ASSIGNMENT: Creates variable 'result' and stores the result of 'create_cube_tuples([1, 2, 3])' in it | FUNCTION CALL: Calls 'create_cube_tuples()' and stores its return value
print(result)                                            # [Line 17] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1085
Write a Python program to filter out numbers greater than a given value using a lambda function.
"""

# ======================================================================
# PROBLEM 1085 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def filter_greater_than(numbers, value):                 # [Line 13]
    return list(filter(lambda x: x <= value, numbers))   # [Line 14]

result = filter_greater_than([1, 2, 3, 4, 5], 3)         # [Line 16] | ASSIGNMENT: Creates variable 'result' and stores the result of 'filter_greater_than([1, 2, 3, 4, 5], 3)' in it | FUNCTION CALL: Calls 'filter_greater_than()' and stores its return value
print(result)                                            # [Line 17] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1086
Write a Python program to convert a list of strings to their lengths using a lambda function.
"""

# ======================================================================
# PROBLEM 1086 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def convert_to_lengths(strings):                         # [Line 13]
    return list(map(lambda x: len(x), strings))          # [Line 14]

result = convert_to_lengths(["apple", "banana", "cherry"])  # [Line 16] | ASSIGNMENT: Creates variable 'result' and stores the result of 'convert_to_lengths(['apple', 'banana', 'cherry'])' in it | FUNCTION CALL: Calls 'convert_to_lengths()' and stores its return value
print(result)                                            # [Line 17] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1087
Write a Python program to check if a number is a perfect square using a lambda function.
"""

# ======================================================================
# PROBLEM 1087 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


is_perfect_square = lambda x: int(x**0.5) ** 2 == x      # [Line 13] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2. | ASSIGNMENT: Creates variable 'is_perfect_square' and stores the result of 'lambda x: int(x ** 0.5) ** 2 == x' in it

result = is_perfect_square(16)                           # [Line 15] | ASSIGNMENT: Creates variable 'result' and stores the result of 'is_perfect_square(16)' in it | FUNCTION CALL: Calls 'is_perfect_square()' and stores its return value
print(result)                                            # [Line 16] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1088
Write a Python program to find the sum of the cubes of all numbers in a list using a lambda function.
"""

# ======================================================================
# PROBLEM 1088 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def sum_of_cubes(numbers):                               # [Line 13]
    return sum(map(lambda x: x**3, numbers))             # [Line 14] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.

result = sum_of_cubes([1, 2, 3])                         # [Line 16] | ASSIGNMENT: Creates variable 'result' and stores the result of 'sum_of_cubes([1, 2, 3])' in it | FUNCTION CALL: Calls 'sum_of_cubes()' and stores its return value
print(result)                                            # [Line 17] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1089
Write a Python program to remove all elements greater than a specific value in a list using a lambda function.
"""

# ======================================================================
# PROBLEM 1089 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def remove_elements_greater_than(numbers, value):        # [Line 13]
    return list(filter(lambda x: x <= value, numbers))   # [Line 14]

result = remove_elements_greater_than([1, 2, 3, 4, 5], 3)  # [Line 16] | ASSIGNMENT: Creates variable 'result' and stores the result of 'remove_elements_greater_than([1, 2, 3, 4, 5], 3)' in it | FUNCTION CALL: Calls 'remove_elements_greater_than()' and stores its return value
print(result)                                            # [Line 17] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1090
Write a Python program to check if all elements in a list are positive using a lambda function.
"""

# ======================================================================
# PROBLEM 1090 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


all_positive = lambda numbers: all(map(lambda x: x > 0, numbers))  # [Line 13] | ASSIGNMENT: Creates variable 'all_positive' and stores the result of 'lambda numbers: all(map(lambda x: x > 0, numbers))' in it

result = all_positive([1, 2, 3, 4])                      # [Line 15] | ASSIGNMENT: Creates variable 'result' and stores the result of 'all_positive([1, 2, 3, 4])' in it | FUNCTION CALL: Calls 'all_positive()' and stores its return value
print(result)                                            # [Line 16] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1091
Write a Python program to create a generator that yields the square of each number in a given range.
"""

# ======================================================================
# PROBLEM 1091 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def square_generator(n):                                 # [Line 13]
    for i in range(n):                                   # [Line 14]
        yield i**2                                       # [Line 15] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.

result = list(square_generator(5))                       # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(square_generator(5))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1092
Write a Python program to create a generator that yields Fibonacci numbers up to a given number.
"""

# ======================================================================
# PROBLEM 1092 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def fibonacci_generator(limit):                          # [Line 13]
    a, b = 0, 1                                          # [Line 14]
    while a <= limit:                                    # [Line 15]
        yield a                                          # [Line 16]
        a, b = b, a + b                                  # [Line 17]

result = list(fibonacci_generator(20))                   # [Line 19] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(fibonacci_generator(20))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1093
Write a Python program to create a generator that yields the characters of a string one by one.
"""

# ======================================================================
# PROBLEM 1093 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def char_generator(s):                                   # [Line 13]
    for char in s:                                       # [Line 14]
        yield char                                       # [Line 15]

result = list(char_generator("hello"))                   # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(char_generator('hello'))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1094
Write a Python program to create a generator that yields numbers from 1 to n with a step of 2.
"""

# ======================================================================
# PROBLEM 1094 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def step_generator(n):                                   # [Line 13]
    for i in range(1, n, 2):                             # [Line 14]
        yield i                                          # [Line 15]

result = list(step_generator(10))                        # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(step_generator(10))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1095
Write a Python program to create a generator that yields even numbers from 1 to n.
"""

# ======================================================================
# PROBLEM 1095 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def even_number_generator(n):                            # [Line 13]
    for i in range(2, n+1, 2):                           # [Line 14]
        yield i                                          # [Line 15]

result = list(even_number_generator(10))                 # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(even_number_generator(10))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1096
Write a Python program to create a generator that yields squares of even numbers from 1 to n.
"""

# ======================================================================
# PROBLEM 1096 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def square_even_generator(n):                            # [Line 13]
    for i in range(2, n+1, 2):                           # [Line 14]
        yield i**2                                       # [Line 15] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.

result = list(square_even_generator(10))                 # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(square_even_generator(10))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1097
Write a Python program to create a generator that yields the first n prime numbers.
"""

# ======================================================================
# PROBLEM 1097 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def prime_generator(n):                                  # [Line 13]
    primes = []                                          # [Line 14]
    num = 2                                              # [Line 15]
    while len(primes) < n:                               # [Line 16]
        if all(num % p != 0 for p in primes):            # [Line 17] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
            primes.append(num)                           # [Line 18]
        num += 1                                         # [Line 19]
    yield from primes                                    # [Line 20]

result = list(prime_generator(5))                        # [Line 22] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(prime_generator(5))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 23] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1098
Write a Python program to create a generator that yields the sum of consecutive pairs from a given list.
"""

# ======================================================================
# PROBLEM 1098 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def consecutive_pair_sum(lst):                           # [Line 13]
    for i in range(len(lst)-1):                          # [Line 14]
        yield lst[i] + lst[i+1]                          # [Line 15]

result = list(consecutive_pair_sum([1, 2, 3, 4, 5]))     # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(consecutive_pair_sum([1, 2, 3, 4, 5]))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1099
Write a Python program to create a generator that yields the factorial of each number from 1 to n.
"""

# ======================================================================
# PROBLEM 1099 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def factorial_generator(n):                              # [Line 13]
    def factorial(x):                                    # [Line 14]
        result = 1                                       # [Line 15]
        for i in range(1, x+1):                          # [Line 16]
            result *= i                                  # [Line 17]
        return result                                    # [Line 18]
    for i in range(1, n+1):                              # [Line 19]
        yield factorial(i)                               # [Line 20]

result = list(factorial_generator(5))                    # [Line 22] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(factorial_generator(5))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 23] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1100
Write a Python program to create a generator that yields numbers divisible by 3 and 5 from 1 to n.
"""

# ======================================================================
# PROBLEM 1100 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def divisible_by_3_and_5_generator(n):                   # [Line 13]
    for i in range(1, n+1):                              # [Line 14]
        if i % 3 == 0 and i % 5 == 0:                    # [Line 15] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
            yield i                                      # [Line 16]

result = list(divisible_by_3_and_5_generator(50))        # [Line 18] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(divisible_by_3_and_5_generator(50))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1101
Write a Python program to create a generator that filters out the odd numbers from a list.
"""

# ======================================================================
# PROBLEM 1101 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def odd_filter_generator(lst):                           # [Line 13]
    for num in lst:                                      # [Line 14]
        if num % 2 == 0:                                 # [Line 15] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
            yield num                                    # [Line 16]

result = list(odd_filter_generator([1, 2, 3, 4, 5, 6]))  # [Line 18] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(odd_filter_generator([1, 2, 3, 4, 5, 6]))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1102
Write a Python program to create a generator that yields the cumulative sum of a given list of numbers.
"""

# ======================================================================
# PROBLEM 1102 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def cumulative_sum_generator(lst):                       # [Line 13]
    total = 0                                            # [Line 14]
    for num in lst:                                      # [Line 15]
        total += num                                     # [Line 16]
        yield total                                      # [Line 17]

result = list(cumulative_sum_generator([1, 2, 3, 4, 5]))  # [Line 19] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(cumulative_sum_generator([1, 2, 3, 4, 5]))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1103
Write a Python program to create a generator that yields the n-th power of each number from 1 to n.
"""

# ======================================================================
# PROBLEM 1103 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def power_generator(n, power):                           # [Line 13]
    for i in range(1, n+1):                              # [Line 14]
        yield i**power                                   # [Line 15] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.

result = list(power_generator(5, 3))                     # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(power_generator(5, 3))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1104
Write a Python program to create a generator that yields each word in a sentence.
"""

# ======================================================================
# PROBLEM 1104 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def word_generator(sentence):                            # [Line 13]
    words = sentence.split()                             # [Line 14]
    for word in words:                                   # [Line 15]
        yield word                                       # [Line 16]

result = list(word_generator("This is a test sentence"))  # [Line 18] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(word_generator('This is a test sentence'))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1105
Write a Python program to create a generator that yields numbers that are squares of integers up to n.
"""

# ======================================================================
# PROBLEM 1105 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def square_number_generator(n):                          # [Line 13]
    for i in range(1, n+1):                              # [Line 14]
        yield i**2                                       # [Line 15] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.

result = list(square_number_generator(5))                # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(square_number_generator(5))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1106
Write a Python program to create a generator that yields the squares of odd numbers from 1 to n.
"""

# ======================================================================
# PROBLEM 1106 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def main(n):                                             # [Line 13]
    for num in range(1, n+1):                            # [Line 14]
        if num % 2 != 0:                                 # [Line 15] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
            yield num ** 2                               # [Line 16] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.

n = 10                                                   # [Line 18] | ASSIGNMENT: Creates variable 'n' and stores the result of '10' in it | DATA TYPE: Integer - A whole number: 10
result = list(main(n))                                   # [Line 19] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(main(n))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

def square_odd_number_generator(n):                      # [Line 22]
    for i in range(1, n+1, 2):                           # [Line 23]
        yield i**2                                       # [Line 24] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.

result = list(square_odd_number_generator(10))           # [Line 26] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(square_odd_number_generator(10))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 27] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1107
Write a Python program to create a generator that yields the elements of a given list in reverse order.
"""

# ======================================================================
# PROBLEM 1107 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def reverse_list_generator(lst):                         # [Line 13]
    for i in range(len(lst)-1, -1, -1):                  # [Line 14]
        yield lst[i]                                     # [Line 15]

result = list(reverse_list_generator([1, 2, 3, 4, 5]))   # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(reverse_list_generator([1, 2, 3, 4, 5]))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1108
Write a Python program to create a generator that yields multiples of a given number up to n.
"""

# ======================================================================
# PROBLEM 1108 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def multiple_generator(n, multiple):                     # [Line 13]
    for i in range(multiple, n+1, multiple):             # [Line 14]
        yield i                                          # [Line 15]

result = list(multiple_generator(20, 3))                 # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(multiple_generator(20, 3))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1109
Write a Python program to create a generator that yields all the uppercase letters in a string.
"""

# ======================================================================
# PROBLEM 1109 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def uppercase_generator(s):                              # [Line 13]
    for char in s:                                       # [Line 14]
        if char.isupper():                               # [Line 15]
            yield char                                   # [Line 16]

result = list(uppercase_generator("Hello World"))        # [Line 18] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(uppercase_generator('Hello World'))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1110
Write a Python program to create a generator that yields the differences between consecutive elements of a list.
"""

# ======================================================================
# PROBLEM 1110 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def consecutive_diff_generator(lst):                     # [Line 13]
    for i in range(len(lst)-1):                          # [Line 14]
        yield lst[i+1] - lst[i]                          # [Line 15]

result = list(consecutive_diff_generator([1, 3, 6, 10]))  # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(consecutive_diff_generator([1, 3, 6, 10]))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1111
Write a Python program to create a generator that yields numbers greater than a given value in a list.
"""

# ======================================================================
# PROBLEM 1111 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def greater_than_generator(lst, value):                  # [Line 13]
    for num in lst:                                      # [Line 14]
        if num > value:                                  # [Line 15]
            yield num                                    # [Line 16]

result = list(greater_than_generator([1, 2, 3, 4, 5, 6], 3))  # [Line 18] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(greater_than_generator([1, 2, 3, 4, 5, 6], 3))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1112
Write a Python program to create a generator that yields the sum of each element with its index from a list.
"""

# ======================================================================
# PROBLEM 1112 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def sum_with_index_generator(lst):                       # [Line 13]
    for index, num in enumerate(lst):                    # [Line 14]
        yield num + index                                # [Line 15]

result = list(sum_with_index_generator([10, 20, 30, 40]))  # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(sum_with_index_generator([10, 20, 30, 40]))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1113
Write a Python program to create a generator that yields all palindromes from a list of strings. 
"""

# ======================================================================
# PROBLEM 1113 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def palindrome_generator(lst):                           # [Line 13]
    for word in lst:                                     # [Line 14]
        if word == word[::-1]:                           # [Line 15] | SLICING OPERATION [::-1] - This is a reverse slice. The syntax [::-1] means: start at the beginning (no start index), stop at the end (no stop index), and step backwards by 1. This effectively reverses the entire sequence. Example: [1,2,3][::-1] becomes [3,2,1] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).
            yield word                                   # [Line 16]

result = list(palindrome_generator(["madam", "apple", "racecar", "banana"]))  # [Line 18] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(palindrome_generator(['madam', 'apple', 'racecar', 'banana']))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1114
Write a Python program to create a generator that yields the product of elements in pairs from a given list.
"""

# ======================================================================
# PROBLEM 1114 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def pair_product_generator(lst):                         # [Line 13]
    for i in range(len(lst)-1):                          # [Line 14]
        yield lst[i] * lst[i+1]                          # [Line 15]

result = list(pair_product_generator([1, 2, 3, 4]))      # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(pair_product_generator([1, 2, 3, 4]))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1115
Write a Python program to create a generator that yields elements from a list that are greater than the previous element. 
"""

# ======================================================================
# PROBLEM 1115 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def greater_than_previous_generator(lst):                # [Line 13]
    for i in range(1, len(lst)):                         # [Line 14]
        if lst[i] > lst[i-1]:                            # [Line 15] | SLICING OPERATION - Extracts a portion of the sequence
            yield lst[i]                                 # [Line 16]

result = list(greater_than_previous_generator([1, 2, 1, 4, 3]))  # [Line 18] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(greater_than_previous_generator([1, 2, 1, 4, 3]))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1116
Write a Python program to create a generator that yields all numbers in a list that are divisible by a given number.
"""

# ======================================================================
# PROBLEM 1116 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def divisible_by_generator(lst, divisor):                # [Line 13]
    for num in lst:                                      # [Line 14]
        if num % divisor == 0:                           # [Line 15] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
            yield num                                    # [Line 16]

result = list(divisible_by_generator([10, 15, 20, 25, 30], 5))  # [Line 18] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(divisible_by_generator([10, 15, 20, 25, 30], 5))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1117
Write a Python program to create a generator that yields the first n even Fibonacci numbers.
"""

# ======================================================================
# PROBLEM 1117 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def even_fibonacci_generator(n):                         # [Line 13]
    a, b = 0, 2                                          # [Line 14]
    count = 0                                            # [Line 15]
    while count < n:                                     # [Line 16]
        yield a                                          # [Line 17]
        a, b = b, 4 * b + a                              # [Line 18]
        count += 1                                       # [Line 19]

result = list(even_fibonacci_generator(5))               # [Line 21] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(even_fibonacci_generator(5))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 22] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1118
Write a Python program to create a generator that yields all the even-indexed elements of a list.
"""

# ======================================================================
# PROBLEM 1118 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def even_index_generator(lst):                           # [Line 13]
    for i in range(0, len(lst), 2):                      # [Line 14]
        yield lst[i]                                     # [Line 15]

result = list(even_index_generator([1, 2, 3, 4, 5, 6]))  # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(even_index_generator([1, 2, 3, 4, 5, 6]))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1119
Write a Python program to create a generator that yields each word in a sentence, but only those with an even number of characters. 
"""

# ======================================================================
# PROBLEM 1119 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def even_length_word_generator(sentence):                # [Line 13]
    words = sentence.split()                             # [Line 14]
    for word in words:                                   # [Line 15]
        if len(word) % 2 == 0:                           # [Line 16] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
            yield word                                   # [Line 17]

result = list(even_length_word_generator("This is a simple test sentence"))  # [Line 19] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(even_length_word_generator('This is a simple test sentence'))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1120
Write a Python program to check if a number is positive, negative, or zero. Control flow.
"""

# ======================================================================
# PROBLEM 1120 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_number(n):                                     # [Line 13]
    if n > 0:                                            # [Line 14]
        return "Positive"                                # [Line 15]
    elif n < 0:                                          # [Line 16]
        return "Negative"                                # [Line 17]
    else:                                                # [Line 18]
        return "Zero"                                    # [Line 19]

result = check_number(5)                                 # [Line 21] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_number(5)' in it | FUNCTION CALL: Calls 'check_number()' and stores its return value
print(result)                                            # [Line 22] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1121
Write a Python program to find the largest of three numbers. Control flow.
"""

# ======================================================================
# PROBLEM 1121 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def largest_of_three(a, b, c):                           # [Line 13]
    if a >= b and a >= c:                                # [Line 14]
        return a                                         # [Line 15]
    elif b >= a and b >= c:                              # [Line 16]
        return b                                         # [Line 17]
    else:                                                # [Line 18]
        return c                                         # [Line 19]

result = largest_of_three(10, 20, 15)                    # [Line 21] | ASSIGNMENT: Creates variable 'result' and stores the result of 'largest_of_three(10, 20, 15)' in it | FUNCTION CALL: Calls 'largest_of_three()' and stores its return value
print(result)                                            # [Line 22] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1122
Write a Python program to check if a given year is a leap year. Control flow.
"""

# ======================================================================
# PROBLEM 1122 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def is_leap_year(year):                                  # [Line 13]
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):  # [Line 14] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
        return True                                      # [Line 15]
    else:                                                # [Line 16]
        return False                                     # [Line 17]

result = is_leap_year(2024)                              # [Line 19] | ASSIGNMENT: Creates variable 'result' and stores the result of 'is_leap_year(2024)' in it | FUNCTION CALL: Calls 'is_leap_year()' and stores its return value
print(result)                                            # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1123
Write a Python program to check if a number is even or odd. Control flow.
"""

# ======================================================================
# PROBLEM 1123 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_even_odd(n):                                   # [Line 13]
    if n % 2 == 0:                                       # [Line 14] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
        return "Even"                                    # [Line 15]
    else:                                                # [Line 16]
        return "Odd"                                     # [Line 17]

result = check_even_odd(7)                               # [Line 19] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_even_odd(7)' in it | FUNCTION CALL: Calls 'check_even_odd()' and stores its return value
print(result)                                            # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1124
Write a Python program to check if a number is divisible by both 3 and 5. Control flow.
"""

# ======================================================================
# PROBLEM 1124 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def divisible_by_3_and_5(n):                             # [Line 13]
    if n % 3 == 0 and n % 5 == 0:                        # [Line 14] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
        return True                                      # [Line 15]
    else:                                                # [Line 16]
        return False                                     # [Line 17]

result = divisible_by_3_and_5(15)                        # [Line 19] | ASSIGNMENT: Creates variable 'result' and stores the result of 'divisible_by_3_and_5(15)' in it | FUNCTION CALL: Calls 'divisible_by_3_and_5()' and stores its return value
print(result)                                            # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1125
Write a Python program to print all numbers from 1 to n that are divisible by 7. Control flow.
"""

# ======================================================================
# PROBLEM 1125 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def divisible_by_7(n):                                   # [Line 13]
    for i in range(1, n+1):                              # [Line 14]
        if i % 7 == 0:                                   # [Line 15] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
            print(i)                                     # [Line 16]

divisible_by_7(50)                                       # [Line 18] | FUNCTION CALL: Executes the function 'divisible_by_7' | ARGUMENTS: Passes 1 argument(s) to the function

"""
Problem: 1126
Write a Python program to check if a given number is a prime number. Control flow.
"""

# ======================================================================
# PROBLEM 1126 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def is_prime(n):                                         # [Line 13]
    if n < 2:                                            # [Line 14]
        return False                                     # [Line 15]
    for i in range(2, int(n**0.5) + 1):                  # [Line 16] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
        if n % i == 0:                                   # [Line 17] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
            return False                                 # [Line 18]
    return True                                          # [Line 19]

result = is_prime(11)                                    # [Line 21] | ASSIGNMENT: Creates variable 'result' and stores the result of 'is_prime(11)' in it | FUNCTION CALL: Calls 'is_prime()' and stores its return value
print(result)                                            # [Line 22] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1127
Write a Python program to find the factorial of a number using recursion. Control flow.
"""

# ======================================================================
# PROBLEM 1127 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def factorial(n):                                        # [Line 13]
    if n == 0 or n == 1:                                 # [Line 14] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).
        return 1                                         # [Line 15]
    return n * factorial(n-1)                            # [Line 16]

result = factorial(5)                                    # [Line 18] | ASSIGNMENT: Creates variable 'result' and stores the result of 'factorial(5)' in it | FUNCTION CALL: Calls 'factorial()' and stores its return value
print(result)                                            # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1128
Write a Python program to check if a string is a palindrome. Control flow.
"""

# ======================================================================
# PROBLEM 1128 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def is_palindrome(s):                                    # [Line 13]
    if s == s[::-1]:                                     # [Line 14] | SLICING OPERATION [::-1] - This is a reverse slice. The syntax [::-1] means: start at the beginning (no start index), stop at the end (no stop index), and step backwards by 1. This effectively reverses the entire sequence. Example: [1,2,3][::-1] becomes [3,2,1] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).
        return True                                      # [Line 15]
    else:                                                # [Line 16]
        return False                                     # [Line 17]

result = is_palindrome("madam")                          # [Line 19] | ASSIGNMENT: Creates variable 'result' and stores the result of 'is_palindrome('madam')' in it | FUNCTION CALL: Calls 'is_palindrome()' and stores its return value
print(result)                                            # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1129
Write a Python program to count the number of vowels in a given string. Control flow.
"""

# ======================================================================
# PROBLEM 1129 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def count_vowels(s):                                     # [Line 13]
    vowels = "aeiou"                                     # [Line 14]
    count = 0                                            # [Line 15]
    for char in s:                                       # [Line 16]
        if char.lower() in vowels:                       # [Line 17]
            count += 1                                   # [Line 18]
    return count                                         # [Line 19]

result = count_vowels("Hello World")                     # [Line 21] | ASSIGNMENT: Creates variable 'result' and stores the result of 'count_vowels('Hello World')' in it | FUNCTION CALL: Calls 'count_vowels()' and stores its return value
print(result)                                            # [Line 22] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1130
Write a Python program to check if a number is a perfect number. Control flow.
"""

# ======================================================================
# PROBLEM 1130 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def is_perfect_number(n):                                # [Line 13]
    divisors = [i for i in range(1, n) if n % i == 0]    # [Line 14] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
    if sum(divisors) == n:                               # [Line 15] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).
        return True                                      # [Line 16]
    else:                                                # [Line 17]
        return False                                     # [Line 18]

result = is_perfect_number(6)                            # [Line 20] | ASSIGNMENT: Creates variable 'result' and stores the result of 'is_perfect_number(6)' in it | FUNCTION CALL: Calls 'is_perfect_number()' and stores its return value
print(result)                                            # [Line 21] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1131
Write a Python program to check if a number is Armstrong number. Control flow.
"""

# ======================================================================
# PROBLEM 1131 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def is_armstrong(n):                                     # [Line 13]
    num_str = str(n)                                     # [Line 14]
    length = len(num_str)                                # [Line 15]
    total = sum(int(digit) ** length for digit in num_str)  # [Line 16] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    if total == n:                                       # [Line 17] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).
        return True                                      # [Line 18]
    else:                                                # [Line 19]
        return False                                     # [Line 20]

result = is_armstrong(153)                               # [Line 22] | ASSIGNMENT: Creates variable 'result' and stores the result of 'is_armstrong(153)' in it | FUNCTION CALL: Calls 'is_armstrong()' and stores its return value
print(result)                                            # [Line 23] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1132
Write a Python program to print all the prime numbers less than or equal to n. Control flow.
"""

# ======================================================================
# PROBLEM 1132 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def prime_numbers_up_to_n(n):                            # [Line 13]
    primes = []                                          # [Line 14]
    for num in range(2, n+1):                            # [Line 15]
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):  # [Line 16] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
            primes.append(num)                           # [Line 17]
    return primes                                        # [Line 18]

result = prime_numbers_up_to_n(20)                       # [Line 20] | ASSIGNMENT: Creates variable 'result' and stores the result of 'prime_numbers_up_to_n(20)' in it | FUNCTION CALL: Calls 'prime_numbers_up_to_n()' and stores its return value
print(result)                                            # [Line 21] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1133
Write a Python program to check if a number is an even number and greater than 10. Control flow.
"""

# ======================================================================
# PROBLEM 1133 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def even_and_greater_than_10(n):                         # [Line 13]
    if n % 2 == 0 and n > 10:                            # [Line 14] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
        return True                                      # [Line 15]
    else:                                                # [Line 16]
        return False                                     # [Line 17]

result = even_and_greater_than_10(12)                    # [Line 19] | ASSIGNMENT: Creates variable 'result' and stores the result of 'even_and_greater_than_10(12)' in it | FUNCTION CALL: Calls 'even_and_greater_than_10()' and stores its return value
print(result)                                            # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1134
Write a Python program to find all the divisors of a number. Control flow.
"""

# ======================================================================
# PROBLEM 1134 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


n = 20                                                   # [Line 13] | ASSIGNMENT: Creates variable 'n' and stores the result of '20' in it | DATA TYPE: Integer - A whole number: 20

for i in range(1, n + 1):                                # [Line 15]
    if n % i == 0:                                       # [Line 16] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
        print(i)                                         # [Line 17]

def find_divisors(n):                                    # [Line 19]
    divisors = [i for i in range(1, n+1) if n % i == 0]  # [Line 20] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
    return divisors                                      # [Line 21]

result = find_divisors(12)                               # [Line 23] | ASSIGNMENT: Creates variable 'result' and stores the result of 'find_divisors(12)' in it | FUNCTION CALL: Calls 'find_divisors()' and stores its return value
print(result)                                            # [Line 24] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1135
Write a Python program to print the multiplication table of a number up to 10. Control flow.
"""

# ======================================================================
# PROBLEM 1135 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def multiplication_table(n):                             # [Line 13]
    for i in range(1, 11):                               # [Line 14]
        print(f"{n} x {i} = {n*i}")                      # [Line 15]

multiplication_table(7)                                  # [Line 17] | FUNCTION CALL: Executes the function 'multiplication_table' | ARGUMENTS: Passes 1 argument(s) to the function

"""
Problem: 1136
Write a Python program to check if a number is a perfect square. Control flow.
"""

# ======================================================================
# PROBLEM 1136 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def is_perfect_square(n):                                # [Line 13]
    return int(n**0.5) ** 2 == n                         # [Line 14] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.

result = is_perfect_square(25)                           # [Line 16] | ASSIGNMENT: Creates variable 'result' and stores the result of 'is_perfect_square(25)' in it | FUNCTION CALL: Calls 'is_perfect_square()' and stores its return value
print(result)                                            # [Line 17] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1137
Write a Python program to check if a number is a power of 2. Control flow.
"""

# ======================================================================
# PROBLEM 1137 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def is_power_of_2(n):                                    # [Line 13]
    return n > 0 and (n & (n - 1)) == 0                  # [Line 14] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

result = is_power_of_2(16)                               # [Line 16] | ASSIGNMENT: Creates variable 'result' and stores the result of 'is_power_of_2(16)' in it | FUNCTION CALL: Calls 'is_power_of_2()' and stores its return value
print(result)                                            # [Line 17] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1138
Write a Python program to find the second largest number in a list. Control flow.
"""

# ======================================================================
# PROBLEM 1138 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def second_largest(lst):                                 # [Line 13]
    lst = sorted(set(lst), reverse=True)                 # [Line 14]
    return lst[1] if len(lst) > 1 else None              # [Line 15]

result = second_largest([10, 20, 4, 45, 99])             # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'second_largest([10, 20, 4, 45, 99])' in it | FUNCTION CALL: Calls 'second_largest()' and stores its return value
print(result)                                            # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1139
Write a Python program to check if a given number is a power of 3. Control flow.
"""

# ======================================================================
# PROBLEM 1139 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def is_power_of_3(n):                                    # [Line 13]
    while n % 3 == 0 and n > 0:                          # [Line 14] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
        n //= 3                                          # [Line 15] | FLOOR DIVISION (//) - Divides two numbers and returns the largest integer less than or equal to the result. Example: 7 // 2 = 3 (not 3.5). This is useful for integer division when you don't want decimal results.
    return n == 1                                        # [Line 16] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

result = is_power_of_3(27)                               # [Line 18] | ASSIGNMENT: Creates variable 'result' and stores the result of 'is_power_of_3(27)' in it | FUNCTION CALL: Calls 'is_power_of_3()' and stores its return value
print(result)                                            # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1140
Write a Python program to print Fibonacci numbers up to n. Control flow.
"""

# ======================================================================
# PROBLEM 1140 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def fibonacci_up_to_n(n):                                # [Line 13]
    a, b = 0, 1                                          # [Line 14]
    while a <= n:                                        # [Line 15]
        print(a, end=" ")                                # [Line 16]
        a, b = b, a + b                                  # [Line 17]

fibonacci_up_to_n(20)                                    # [Line 19] | FUNCTION CALL: Executes the function 'fibonacci_up_to_n' | ARGUMENTS: Passes 1 argument(s) to the function

"""
Problem: 1141
Write a Python program to count the occurrences of a specific element in a list. Control flow.
"""

# ======================================================================
# PROBLEM 1141 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def count_occurrences(lst, element):                     # [Line 13]
    return lst.count(element)                            # [Line 14]

result = count_occurrences([1, 2, 2, 3, 4, 2], 2)        # [Line 16] | ASSIGNMENT: Creates variable 'result' and stores the result of 'count_occurrences([1, 2, 2, 3, 4, 2], 2)' in it | FUNCTION CALL: Calls 'count_occurrences()' and stores its return value
print(result)                                            # [Line 17] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1142
Write a Python program to check if a given number is a perfect square and an Armstrong number. Control flow.
"""

# ======================================================================
# PROBLEM 1142 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def is_perfect_square_and_armstrong(n):                  # [Line 13]
    if is_perfect_square(n) and is_armstrong(n):         # [Line 14]
        return True                                      # [Line 15]
    else:                                                # [Line 16]
        return False                                     # [Line 17]

result = is_perfect_square_and_armstrong(153)            # [Line 19] | ASSIGNMENT: Creates variable 'result' and stores the result of 'is_perfect_square_and_armstrong(153)' in it | FUNCTION CALL: Calls 'is_perfect_square_and_armstrong()' and stores its return value
print(result)                                            # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1143
Write a Python program to find all numbers in a given range that are divisible by 7 and 11. Control flow.
"""

# ======================================================================
# PROBLEM 1143 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def divisible_by_7_and_11(start, end):                   # [Line 13]
    return [num for num in range(start, end+1) if num % 7 == 0 and num % 11 == 0]  # [Line 14] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = divisible_by_7_and_11(1, 100)                   # [Line 16] | ASSIGNMENT: Creates variable 'result' and stores the result of 'divisible_by_7_and_11(1, 100)' in it | FUNCTION CALL: Calls 'divisible_by_7_and_11()' and stores its return value
print(result)                                            # [Line 17] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1144
Write a Python program to print the factorial of a number using a while loop. Control flow.
"""

# ======================================================================
# PROBLEM 1144 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def factorial_while(n):                                  # [Line 13]
    result = 1                                           # [Line 14]
    while n > 1:                                         # [Line 15]
        result *= n                                      # [Line 16]
        n -= 1                                           # [Line 17]
    return result                                        # [Line 18]

result = factorial_while(5)                              # [Line 20] | ASSIGNMENT: Creates variable 'result' and stores the result of 'factorial_while(5)' in it | FUNCTION CALL: Calls 'factorial_while()' and stores its return value
print(result)                                            # [Line 21] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1145
Write a Python program to print a list of numbers in reverse order. Control flow.
"""

# ======================================================================
# PROBLEM 1145 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def reverse_list(lst):                                   # [Line 13]
    return lst[::-1]                                     # [Line 14] | SLICING OPERATION [::-1] - This is a reverse slice. The syntax [::-1] means: start at the beginning (no start index), stop at the end (no stop index), and step backwards by 1. This effectively reverses the entire sequence. Example: [1,2,3][::-1] becomes [3,2,1]

result = reverse_list([1, 2, 3, 4, 5])                   # [Line 16] | ASSIGNMENT: Creates variable 'result' and stores the result of 'reverse_list([1, 2, 3, 4, 5])' in it | FUNCTION CALL: Calls 'reverse_list()' and stores its return value
print(result)                                            # [Line 17] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1146
Write a Python program to check if a number is divisible by 5 or 10. Control flow.
"""

# ======================================================================
# PROBLEM 1146 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def divisible_by_5_or_10(n):                             # [Line 13]
    if n % 5 == 0 or n % 10 == 0:                        # [Line 14] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
        return True                                      # [Line 15]
    else:                                                # [Line 16]
        return False                                     # [Line 17]

result = divisible_by_5_or_10(50)                        # [Line 19] | ASSIGNMENT: Creates variable 'result' and stores the result of 'divisible_by_5_or_10(50)' in it | FUNCTION CALL: Calls 'divisible_by_5_or_10()' and stores its return value
print(result)                                            # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1147
Write a Python program to check if a number is divisible by any number in a given list. Control flow.
"""

# ======================================================================
# PROBLEM 1147 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def divisible_by_any_number(n, lst):                     # [Line 13]
    for num in lst:                                      # [Line 14]
        if n % num == 0:                                 # [Line 15] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
            return True                                  # [Line 16]
    return False                                         # [Line 17]

result = divisible_by_any_number(10, [3, 5, 7])          # [Line 19] | ASSIGNMENT: Creates variable 'result' and stores the result of 'divisible_by_any_number(10, [3, 5, 7])' in it | FUNCTION CALL: Calls 'divisible_by_any_number()' and stores its return value
print(result)                                            # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1148
Write a Python program to demonstrate variable scope in a function. Scope.
"""

# ======================================================================
# PROBLEM 1148 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def outer_function():                                    # [Line 13]
    x = 10                                               # [Line 14] | Local variable
    def inner_function():                                # [Line 15]
        print(x)                                         # [Line 16] | Accessing the outer function's variable
    inner_function()                                     # [Line 17]

outer_function()                                         # [Line 19] | FUNCTION CALL: Executes the function 'outer_function'

"""
Problem: 1149
Write a Python program to show the difference between global and local variables. Scope.
"""

# ======================================================================
# PROBLEM 1149 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


x = 20                                                   # [Line 13] | ASSIGNMENT: Creates variable 'x' and stores the result of '20' in it | DATA TYPE: Integer - A whole number: 20 | Global variable

def test_scope():                                        # [Line 15]
    x = 10                                               # [Line 16] | Local variable
    print(f"Local variable: {x}")                        # [Line 17]

test_scope()                                             # [Line 19] | FUNCTION CALL: Executes the function 'test_scope'
print(f"Global variable: {x}")                           # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1150
Write a Python program to demonstrate the use of the `global` keyword. Scope.
"""

# ======================================================================
# PROBLEM 1150 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def modify_global_variable():                            # [Line 13]
    global x                                             # [Line 14]
    x = 30                                               # [Line 15] | Modifies the global variable

x = 10                                                   # [Line 17] | ASSIGNMENT: Creates variable 'x' and stores the result of '10' in it | DATA TYPE: Integer - A whole number: 10
modify_global_variable()                                 # [Line 18] | FUNCTION CALL: Executes the function 'modify_global_variable'
print(x)                                                 # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1151
Write a Python program to demonstrate the use of `nonlocal` keyword. Scope.
"""

# ======================================================================
# PROBLEM 1151 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def outer_function():                                    # [Line 13]
    x = 10                                               # [Line 14]
    def inner_function():                                # [Line 15]
        nonlocal x                                       # [Line 16]
        x = 20                                           # [Line 17] | Modifies the variable in the outer function's scope
    inner_function()                                     # [Line 18]
    print(x)                                             # [Line 19]

outer_function()                                         # [Line 21] | FUNCTION CALL: Executes the function 'outer_function'

"""
Problem: 1152
Write a Python program to demonstrate variable shadowing. Scope.
"""

# ======================================================================
# PROBLEM 1152 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


x = 100                                                  # [Line 13] | ASSIGNMENT: Creates variable 'x' and stores the result of '100' in it | DATA TYPE: Integer - A whole number: 100 | Global variable

def shadowing_example():                                 # [Line 15]
    x = 50                                               # [Line 16] | Local variable, shadows the global variable
    print(f"Local x: {x}")                               # [Line 17]

shadowing_example()                                      # [Line 19] | FUNCTION CALL: Executes the function 'shadowing_example'
print(f"Global x: {x}")                                  # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1153
Write a Python program to demonstrate the use of function arguments as local variables. Scope.
"""

# ======================================================================
# PROBLEM 1153 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def example_function(a, b):                              # [Line 13]
    c = a + b                                            # [Line 14] | c is a local variable
    print(f"The sum of {a} and {b} is {c}")              # [Line 15]

example_function(5, 7)                                   # [Line 17] | FUNCTION CALL: Executes the function 'example_function' | ARGUMENTS: Passes 2 argument(s) to the function

"""
Problem: 1154
Write a Python program to demonstrate how to pass a variable as a default argument. Scope.
"""

# ======================================================================
# PROBLEM 1154 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def greet(name="John"):                                  # [Line 13]
    print(f"Hello, {name}!")                             # [Line 14]

greet()                                                  # [Line 16] | FUNCTION CALL: Executes the function 'greet' | Uses default value
greet("Alice")                                           # [Line 17] | FUNCTION CALL: Executes the function 'greet' | ARGUMENTS: Passes 1 argument(s) to the function | Uses passed argument

"""
Problem: 1155
Write a Python program to show the use of mutable and immutable types in functions. Scope.
"""

# ======================================================================
# PROBLEM 1155 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def modify_list(lst):                                    # [Line 13]
    lst.append(4)                                        # [Line 14] | List is mutable, so it is modified
    print(f"Modified list: {lst}")                       # [Line 15]

my_list = [1, 2, 3]                                      # [Line 17] | ASSIGNMENT: Creates variable 'my_list' and stores the result of '[1, 2, 3]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
modify_list(my_list)                                     # [Line 18] | FUNCTION CALL: Executes the function 'modify_list' | ARGUMENTS: Passes 1 argument(s) to the function
print(f"Original list: {my_list}")                       # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

def modify_integer(n):                                   # [Line 21]
    n += 1                                               # [Line 22] | Integer is immutable, so it cannot be modified
    print(f"Modified integer: {n}")                      # [Line 23]

my_int = 5                                               # [Line 25] | ASSIGNMENT: Creates variable 'my_int' and stores the result of '5' in it | DATA TYPE: Integer - A whole number: 5
modify_integer(my_int)                                   # [Line 26] | FUNCTION CALL: Executes the function 'modify_integer' | ARGUMENTS: Passes 1 argument(s) to the function
print(f"Original integer: {my_int}")                     # [Line 27] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1156
Write a Python program to demonstrate the scope of variables in a loop. Scope.
"""

# ======================================================================
# PROBLEM 1156 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def loop_scope():                                        # [Line 13]
    for i in range(3):                                   # [Line 14]
        x = i                                            # [Line 15]
        print(f"Inside loop: {x}")                       # [Line 16]
    # x is accessible here after the loop ends
    print(f"Outside loop: {x}")                          # [Line 18]

loop_scope()                                             # [Line 20] | FUNCTION CALL: Executes the function 'loop_scope'

"""
Problem: 1157
Write a Python program to check if a variable is defined. Scope.
"""

# ======================================================================
# PROBLEM 1157 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_variable():                                    # [Line 13]
    try:                                                 # [Line 14]
        print(x)                                         # [Line 15]
    except NameError:                                    # [Line 16]
        print("x is not defined")                        # [Line 17]

check_variable()                                         # [Line 19] | FUNCTION CALL: Executes the function 'check_variable'

"""
Problem: 1158
Write a Python program to demonstrate the scope of variables in nested functions. Scope.
"""

# ======================================================================
# PROBLEM 1158 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def outer_function():                                    # [Line 13]
    x = 10                                               # [Line 14] | Local variable in outer function
    def inner_function():                                # [Line 15]
        y = 20                                           # [Line 16] | Local variable in inner function
        print(f"Inner function: x = {x}, y = {y}")       # [Line 17]
    inner_function()                                     # [Line 18]
    print(f"Outer function: x = {x}")                    # [Line 19]

outer_function()                                         # [Line 21] | FUNCTION CALL: Executes the function 'outer_function'

"""
Problem: 1159
Write a Python program to demonstrate how to return a variable from a function. Scope.
"""

# ======================================================================
# PROBLEM 1159 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def add_numbers(a, b):                                   # [Line 13]
    sum_result = a + b                                   # [Line 14]
    return sum_result                                    # [Line 15]

result = add_numbers(3, 5)                               # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'add_numbers(3, 5)' in it | FUNCTION CALL: Calls 'add_numbers()' and stores its return value
print(f"The sum is {result}")                            # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1160
Write a Python program to explain how default mutable arguments work in functions. Scope.
"""

# ======================================================================
# PROBLEM 1160 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def append_to_list(n, default_list=[]):                  # [Line 13] | SLICING OPERATION - Extracts a portion of the sequence
    default_list.append(n)                               # [Line 14]
    return default_list                                  # [Line 15]

# Test the function
print(append_to_list(1))                                 # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | [1]
print(append_to_list(2))                                 # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | [1, 2]
print(append_to_list(3))                                 # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | [1, 2, 3]


def append_to_list(lst=None):                            # [Line 23]
    if lst is None:                                      # [Line 24]
        lst = []                                         # [Line 25]
    lst.append(1)                                        # [Line 26]
    return lst                                           # [Line 27]

print(append_to_list())                                  # [Line 29] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Returns [1]
print(append_to_list())                                  # [Line 30] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Returns [1], new list is created each time

"""
Problem: 1161
Write a Python program to demonstrate the use of variables in list comprehensions. Scope.
"""

# ======================================================================
# PROBLEM 1161 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def square_numbers(lst):                                 # [Line 13]
    return [x**2 for x in lst]                           # [Line 14] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.

numbers = [1, 2, 3, 4]                                   # [Line 16] | ASSIGNMENT: Creates variable 'numbers' and stores the result of '[1, 2, 3, 4]' in it | DATA TYPE: List - A mutable ordered collection. Contains 4 elements
result = square_numbers(numbers)                         # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'square_numbers(numbers)' in it | FUNCTION CALL: Calls 'square_numbers()' and stores its return value
print(f"Squares: {result}")                              # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1162
Write a Python program to show the effect of reusing the same variable in a function. Scope.
"""

# ======================================================================
# PROBLEM 1162 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def reuse_variable():                                    # [Line 13]
    x = 5                                                # [Line 14]
    x = x * 2                                            # [Line 15] | Reuses the variable
    print(f"New value of x: {x}")                        # [Line 16]

reuse_variable()                                         # [Line 18] | FUNCTION CALL: Executes the function 'reuse_variable'

"""
Problem: 1163
Write a Python program to demonstrate variable scope in different functions. Scope.
"""

# ======================================================================
# PROBLEM 1163 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


x = 50                                                   # [Line 13] | ASSIGNMENT: Creates variable 'x' and stores the result of '50' in it | DATA TYPE: Integer - A whole number: 50 | Global variable

def function_one():                                      # [Line 15]
    print(f"Function One: {x}")                          # [Line 16]

def function_two():                                      # [Line 18]
    x = 40                                               # [Line 19]
    print(f"Function Two: {x}")                          # [Line 20]

function_one()                                           # [Line 22] | FUNCTION CALL: Executes the function 'function_one'
function_two()                                           # [Line 23] | FUNCTION CALL: Executes the function 'function_two'

"""
Problem: 1164
Write a Python program to demonstrate the use of `global` for modifying variables in different functions. Scope.
"""

# ======================================================================
# PROBLEM 1164 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


x = 10                                                   # [Line 13] | ASSIGNMENT: Creates variable 'x' and stores the result of '10' in it | DATA TYPE: Integer - A whole number: 10 | Global variable

def function_one():                                      # [Line 15]
    global x                                             # [Line 16]
    x += 5                                               # [Line 17]

def function_two():                                      # [Line 19]
    global x                                             # [Line 20]
    x -= 3                                               # [Line 21]

function_one()                                           # [Line 23] | FUNCTION CALL: Executes the function 'function_one'
function_two()                                           # [Line 24] | FUNCTION CALL: Executes the function 'function_two'
print(f"Global variable x: {x}")                         # [Line 25] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1165
Write a Python program to show how variable values are changed in nested functions. Scope.
"""

# ======================================================================
# PROBLEM 1165 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def outer_function():                                    # [Line 13]
    x = 15                                               # [Line 14] | Local variable in outer function
    def inner_function():                                # [Line 15]
        nonlocal x                                       # [Line 16]
        x += 10                                          # [Line 17] | Modifies x in the outer function's scope
        print(f"Inner function: x = {x}")                # [Line 18]
    inner_function()                                     # [Line 19]
    print(f"Outer function: x = {x}")                    # [Line 20]

outer_function()                                         # [Line 22] | FUNCTION CALL: Executes the function 'outer_function'

"""
Problem: 1166
Write a Python program to demonstrate the use of variable arguments in functions. Scope.
"""

# ======================================================================
# PROBLEM 1166 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def print_arguments(*args):                              # [Line 13]
    for arg in args:                                     # [Line 14]
        print(arg)                                       # [Line 15]

print_arguments(1, 2, 3, "hello", [1, 2, 3])             # [Line 17] | FUNCTION CALL: Executes the function 'print_arguments' | ARGUMENTS: Passes 5 argument(s) to the function

"""
Problem: 1167
Write a Python program to show how the scope of a variable changes in a for loop. Scope.

"""

# ======================================================================
# PROBLEM 1167 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def loop_variable_scope():                               # [Line 14]
    for i in range(3):                                   # [Line 15]
        y = i                                            # [Line 16] | Local variable in the loop
        print(f"In the loop: y = {y}")                   # [Line 17]
    print(f"After the loop: y = {y}")                    # [Line 18] | y still exists outside the loop

loop_variable_scope()                                    # [Line 20] | FUNCTION CALL: Executes the function 'loop_variable_scope'

"""
Problem: 1168
Write a Python program to show the behavior of variables in global scope inside functions. Scope.
"""

# ======================================================================
# PROBLEM 1168 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def global_inside_function():                            # [Line 13]
    print(f"Global variable x inside function: {x}")     # [Line 14]

x = 10                                                   # [Line 16] | ASSIGNMENT: Creates variable 'x' and stores the result of '10' in it | DATA TYPE: Integer - A whole number: 10 | Global variable
global_inside_function()                                 # [Line 17] | FUNCTION CALL: Executes the function 'global_inside_function'

"""
Problem: 1169
Write a Python program to explain the difference between mutable and immutable variables in terms of scope. Scope.
"""

# ======================================================================
# PROBLEM 1169 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def test_mutability():                                   # [Line 13]
    mutable = [1, 2, 3]                                  # [Line 14] | Mutable variable (list)
    immutable = 10                                       # [Line 15] | Immutable variable (integer)
    
    mutable[0] = 100                                     # [Line 17] | Modifies the mutable variable
    immutable = 20                                       # [Line 18] | This does not change the original variable
    
    print(f"Mutable variable: {mutable}")                # [Line 20]
    print(f"Immutable variable: {immutable}")            # [Line 21]

test_mutability()                                        # [Line 23] | FUNCTION CALL: Executes the function 'test_mutability'

"""
Problem: 1170
Write a Python program to show the behavior of variables declared in a list comprehension. Scope.
"""

# ======================================================================
# PROBLEM 1170 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def list_comprehension_variable_scope():                 # [Line 13]
    lst = [x**2 for x in range(5)]                       # [Line 14] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    print(f"List comprehension result: {lst}")           # [Line 15]

list_comprehension_variable_scope()                      # [Line 17] | FUNCTION CALL: Executes the function 'list_comprehension_variable_scope'

"""
Problem: 1171
Write a Python program to show that function arguments can be variables with different scopes. Scope.
"""

# ======================================================================
# PROBLEM 1171 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def print_variable_in_function(x):                       # [Line 13]
    y = x * 2                                            # [Line 14] | Local variable inside function
    print(f"Function variable y: {y}")                   # [Line 15]

z = 10                                                   # [Line 17] | ASSIGNMENT: Creates variable 'z' and stores the result of '10' in it | DATA TYPE: Integer - A whole number: 10 | Global variable
print_variable_in_function(z)                            # [Line 18] | FUNCTION CALL: Executes the function 'print_variable_in_function' | ARGUMENTS: Passes 1 argument(s) to the function

"""
Problem: 1172
Write a Python program to show that a variable in a for loop can be accessed outside the loop. Scope.
"""

# ======================================================================
# PROBLEM 1172 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def for_loop_variable_scope():                           # [Line 13]
    for i in range(3):                                   # [Line 14]
        x = i                                            # [Line 15]
        print(f"In the loop: x = {x}")                   # [Line 16]
    print(f"Outside the loop: x = {x}")                  # [Line 17]

for_loop_variable_scope()                                # [Line 19] | FUNCTION CALL: Executes the function 'for_loop_variable_scope'

"""
Problem: 1173
Write a Python program to demonstrate the impact of changing a global variable inside a function. Scope.
"""

# ======================================================================
# PROBLEM 1173 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


x = 100                                                  # [Line 13] | ASSIGNMENT: Creates variable 'x' and stores the result of '100' in it | DATA TYPE: Integer - A whole number: 100

def change_global_variable():                            # [Line 15]
    global x                                             # [Line 16]
    x = 50                                               # [Line 17]

change_global_variable()                                 # [Line 19] | FUNCTION CALL: Executes the function 'change_global_variable'
print(f"Global x after modification: {x}")               # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1174
Write a Python program to demonstrate variable accessibility within different levels of nested functions. Scope.
"""

# ======================================================================
# PROBLEM 1174 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def outer_function():                                    # [Line 13]
    x = 5                                                # [Line 14]
    def middle_function():                               # [Line 15]
        y = 10                                           # [Line 16]
        def inner_function():                            # [Line 17]
            z = 15                                       # [Line 18]
            print(f"Inner function: x = {x}, y = {y}, z = {z}")  # [Line 19]
        inner_function()                                 # [Line 20]
    middle_function()                                    # [Line 21]

outer_function()                                         # [Line 23] | FUNCTION CALL: Executes the function 'outer_function'

"""
Problem: 1175
Write a Python program to demonstrate how function arguments can access global variables. Scope.
"""

# ======================================================================
# PROBLEM 1175 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


x = 100                                                  # [Line 13] | ASSIGNMENT: Creates variable 'x' and stores the result of '100' in it | DATA TYPE: Integer - A whole number: 100

def print_global_variable(x):                            # [Line 15]
    print(f"Global x inside function: {x}")              # [Line 16]

print_global_variable(x)                                 # [Line 18] | FUNCTION CALL: Executes the function 'print_global_variable' | ARGUMENTS: Passes 1 argument(s) to the function

"""
Problem: 1176
Write a Python program to demonstrate the scope of variables in a recursive function. Scope.
"""

# ======================================================================
# PROBLEM 1176 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def factorial_recursive(n):                              # [Line 13]
    if n == 1:                                           # [Line 14] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).
        return 1                                         # [Line 15]
    else:                                                # [Line 16]
        return n * factorial_recursive(n - 1)            # [Line 17]

result = factorial_recursive(5)                          # [Line 19] | ASSIGNMENT: Creates variable 'result' and stores the result of 'factorial_recursive(5)' in it | FUNCTION CALL: Calls 'factorial_recursive()' and stores its return value
print(f"Factorial: {result}")                            # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1177
Write a Python program to import the `math` module and calculate the square root of a number. Module.
"""

# ======================================================================
# PROBLEM 1177 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import math                                              # [Line 13]

def calculate_square_root(number):                       # [Line 15]
    return math.sqrt(number)                             # [Line 16]

result = calculate_square_root(16)                       # [Line 18] | ASSIGNMENT: Creates variable 'result' and stores the result of 'calculate_square_root(16)' in it | FUNCTION CALL: Calls 'calculate_square_root()' and stores its return value
print(f"The square root of 16 is {result}")              # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1178
Write a Python program to use the `random` module to generate a random number between 1 and 100. Module.
"""

# ======================================================================
# PROBLEM 1178 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import random                                            # [Line 13]

def generate_random_number():                            # [Line 15]
    return random.randint(1, 100)                        # [Line 16]

random_number = generate_random_number()                 # [Line 18] | ASSIGNMENT: Creates variable 'random_number' and stores the result of 'generate_random_number()' in it | FUNCTION CALL: Calls 'generate_random_number()' and stores its return value
print(f"Random number between 1 and 100: {random_number}")  # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1179
Write a Python program to use the `datetime` module to get the current date and time. Module.
"""

# ======================================================================
# PROBLEM 1179 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import datetime                                          # [Line 13]

def current_datetime():                                  # [Line 15]
    return datetime.datetime.now()                       # [Line 16]

now = current_datetime()                                 # [Line 18] | ASSIGNMENT: Creates variable 'now' and stores the result of 'current_datetime()' in it | FUNCTION CALL: Calls 'current_datetime()' and stores its return value
print(f"Current date and time: {now}")                   # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1180
Write a Python program to use the `os` module to get the current working directory. Module.
"""

# ======================================================================
# PROBLEM 1180 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import os                                                # [Line 13]

def current_working_directory():                         # [Line 15]
    return os.getcwd()                                   # [Line 16]

cwd = current_working_directory()                        # [Line 18] | ASSIGNMENT: Creates variable 'cwd' and stores the result of 'current_working_directory()' in it | FUNCTION CALL: Calls 'current_working_directory()' and stores its return value
print(f"Current working directory: {cwd}")               # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1181
Write a Python program to use the `sys` module to get the Python version. Module.
"""

# ======================================================================
# PROBLEM 1181 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import sys                                               # [Line 13]

def python_version():                                    # [Line 15]
    return sys.version                                   # [Line 16]

version = python_version()                               # [Line 18] | ASSIGNMENT: Creates variable 'version' and stores the result of 'python_version()' in it | FUNCTION CALL: Calls 'python_version()' and stores its return value
print(f"Python version: {version}")                      # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1182
Write a Python program to use the `json` module to convert a Python dictionary to a JSON string. Module.
"""

# ======================================================================
# PROBLEM 1182 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import json                                              # [Line 13]

def dict_to_json():                                      # [Line 15]
    sample_dict = {"name": "Alice", "age": 30}           # [Line 16]
    return json.dumps(sample_dict)                       # [Line 17]

json_str = dict_to_json()                                # [Line 19] | ASSIGNMENT: Creates variable 'json_str' and stores the result of 'dict_to_json()' in it | FUNCTION CALL: Calls 'dict_to_json()' and stores its return value
print(f"JSON string: {json_str}")                        # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1183
Write a Python program to use the `re` module to check if a string contains a number. Module.
"""

# ======================================================================
# PROBLEM 1183 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import re                                                # [Line 13]

def contains_number(string):                             # [Line 15]
    return bool(re.search(r'\d', string))                # [Line 16]

result = contains_number("Hello123")                     # [Line 18] | ASSIGNMENT: Creates variable 'result' and stores the result of 'contains_number('Hello123')' in it | FUNCTION CALL: Calls 'contains_number()' and stores its return value
print(f"Does the string contain a number? {result}")     # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1184
Write a Python program to use the `os` module to list all files in a directory. Module.
"""

# ======================================================================
# PROBLEM 1184 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import os                                                # [Line 13]

def list_files(directory):                               # [Line 15]
    return os.listdir(directory)                         # [Line 16]

files = list_files(".")                                  # [Line 18] | ASSIGNMENT: Creates variable 'files' and stores the result of 'list_files('.')' in it | FUNCTION CALL: Calls 'list_files()' and stores its return value
print(f"Files in the current directory: {files}")        # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1185
Write a Python program to use the `math` module to calculate the factorial of a number. Module.
"""

# ======================================================================
# PROBLEM 1185 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import math                                              # [Line 13]

def calculate_factorial(number):                         # [Line 15]
    return math.factorial(number)                        # [Line 16]

factorial_result = calculate_factorial(5)                # [Line 18] | ASSIGNMENT: Creates variable 'factorial_result' and stores the result of 'calculate_factorial(5)' in it | FUNCTION CALL: Calls 'calculate_factorial()' and stores its return value
print(f"The factorial of 5 is {factorial_result}")       # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1186
Write a Python program to use the `time` module to measure the execution time of a block of code. Module.
"""

# ======================================================================
# PROBLEM 1186 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import time                                              # [Line 13]

def measure_time():                                      # [Line 15]
    start_time = time.time()                             # [Line 16]
    sum(range(1000000))                                  # [Line 17]
    end_time = time.time()                               # [Line 18]
    return end_time - start_time                         # [Line 19]

execution_time = measure_time()                          # [Line 21] | ASSIGNMENT: Creates variable 'execution_time' and stores the result of 'measure_time()' in it | FUNCTION CALL: Calls 'measure_time()' and stores its return value
print(f"Execution time: {execution_time} seconds")       # [Line 22] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1187
Write a Python program to use the `calendar` module to check if a year is a leap year. Module.
"""

# ======================================================================
# PROBLEM 1187 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import calendar                                          # [Line 13]

def is_leap_year(year):                                  # [Line 15]
    return calendar.isleap(year)                         # [Line 16]

result = is_leap_year(2024)                              # [Line 18] | ASSIGNMENT: Creates variable 'result' and stores the result of 'is_leap_year(2024)' in it | FUNCTION CALL: Calls 'is_leap_year()' and stores its return value
print(f"Is 2024 a leap year? {result}")                  # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1188
Write a Python program to use the `math` module to find the value of pi. Module.
"""

# ======================================================================
# PROBLEM 1188 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import math                                              # [Line 13]

def get_pi_value():                                      # [Line 15]
    return math.pi                                       # [Line 16]

pi_value = get_pi_value()                                # [Line 18] | ASSIGNMENT: Creates variable 'pi_value' and stores the result of 'get_pi_value()' in it | FUNCTION CALL: Calls 'get_pi_value()' and stores its return value
print(f"The value of pi is {pi_value}")                  # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1189
Write a Python program to use the `random` module to shuffle a list of numbers. Module.
"""

# ======================================================================
# PROBLEM 1189 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import random                                            # [Line 13]

def shuffle_list(lst):                                   # [Line 15]
    random.shuffle(lst)                                  # [Line 16]
    return lst                                           # [Line 17]

numbers = [1, 2, 3, 4, 5]                                # [Line 19] | ASSIGNMENT: Creates variable 'numbers' and stores the result of '[1, 2, 3, 4, 5]' in it | DATA TYPE: List - A mutable ordered collection. Contains 5 elements
shuffled_numbers = shuffle_list(numbers)                 # [Line 20] | ASSIGNMENT: Creates variable 'shuffled_numbers' and stores the result of 'shuffle_list(numbers)' in it | FUNCTION CALL: Calls 'shuffle_list()' and stores its return value
print(f"Shuffled list: {shuffled_numbers}")              # [Line 21] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1190
Write a Python program to use the `collections` module to count the occurrences of elements in a list. Module.
"""

# ======================================================================
# PROBLEM 1190 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import collections                                       # [Line 13]

def count_occurrences(lst):                              # [Line 15]
    return collections.Counter(lst)                      # [Line 16]

numbers = [1, 2, 2, 3, 3, 3]                             # [Line 18] | ASSIGNMENT: Creates variable 'numbers' and stores the result of '[1, 2, 2, 3, 3, 3]' in it | DATA TYPE: List - A mutable ordered collection. Contains 6 elements
occurrences = count_occurrences(numbers)                 # [Line 19] | ASSIGNMENT: Creates variable 'occurrences' and stores the result of 'count_occurrences(numbers)' in it | FUNCTION CALL: Calls 'count_occurrences()' and stores its return value
print(f"Occurrences: {occurrences}")                     # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1191
Write a Python program to use the `math` module to calculate the greatest common divisor (GCD) of two numbers. Module.
"""

# ======================================================================
# PROBLEM 1191 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import math                                              # [Line 13]

def calculate_gcd(a, b):                                 # [Line 15]
    return math.gcd(a, b)                                # [Line 16]

gcd_result = calculate_gcd(48, 180)                      # [Line 18] | ASSIGNMENT: Creates variable 'gcd_result' and stores the result of 'calculate_gcd(48, 180)' in it | FUNCTION CALL: Calls 'calculate_gcd()' and stores its return value
print(f"The GCD of 48 and 180 is {gcd_result}")          # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1192
Write a Python program to use the `os` module to rename a file. Module.
"""

# ======================================================================
# PROBLEM 1192 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import os                                                # [Line 13]

def rename_file(old_name, new_name):                     # [Line 15]
    os.rename(old_name, new_name)                        # [Line 16]

# Uncomment the following lines to test the rename_file function:
rename_file("old_file.txt", "new_file.txt")              # [Line 19] | FUNCTION CALL: Executes the function 'rename_file' | ARGUMENTS: Passes 2 argument(s) to the function

"""
Problem: 1193
Write a Python program to use the `datetime` module to format the current date. Module.
"""

# ======================================================================
# PROBLEM 1193 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import datetime                                          # [Line 13]

def format_current_date():                               # [Line 15]
    return datetime.datetime.now().strftime("%Y-%m-%d")  # [Line 16] | OPERATION - Performs a calculation or comparison

formatted_date = format_current_date()                   # [Line 18] | ASSIGNMENT: Creates variable 'formatted_date' and stores the result of 'format_current_date()' in it | FUNCTION CALL: Calls 'format_current_date()' and stores its return value
print(f"Formatted current date: {formatted_date}")       # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1194
Write a Python program to use the `json` module to parse a JSON string into a Python dictionary. Module.
"""

# ======================================================================
# PROBLEM 1194 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import json                                              # [Line 13]

def json_to_dict(json_str):                              # [Line 15]
    return json.loads(json_str)                          # [Line 16]

json_str = '{"name": "Bob", "age": 25}'                  # [Line 18] | ASSIGNMENT: Creates variable 'json_str' and stores the result of ''{"name": "Bob", "age": 25}'' in it | DATA TYPE: String - A sequence of characters. Length: 26
parsed_dict = json_to_dict(json_str)                     # [Line 19] | ASSIGNMENT: Creates variable 'parsed_dict' and stores the result of 'json_to_dict(json_str)' in it | FUNCTION CALL: Calls 'json_to_dict()' and stores its return value
print(f"Parsed dictionary: {parsed_dict}")               # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1195
Write a Python program to use the `random` module to select a random element from a list. Module.
"""

# ======================================================================
# PROBLEM 1195 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import random                                            # [Line 13]

def select_random_element(lst):                          # [Line 15]
    return random.choice(lst)                            # [Line 16]

elements = [10, 20, 30, 40]                              # [Line 18] | ASSIGNMENT: Creates variable 'elements' and stores the result of '[10, 20, 30, 40]' in it | DATA TYPE: List - A mutable ordered collection. Contains 4 elements
random_element = select_random_element(elements)         # [Line 19] | ASSIGNMENT: Creates variable 'random_element' and stores the result of 'select_random_element(elements)' in it | FUNCTION CALL: Calls 'select_random_element()' and stores its return value
print(f"Random element: {random_element}")               # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1196
Write a Python program to use the `math` module to round a floating-point number to the nearest integer. Module.
"""

# ======================================================================
# PROBLEM 1196 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import math                                              # [Line 13]

def round_number(number):                                # [Line 15]
    return round(number)                                 # [Line 16]

rounded_value = round_number(7.5)                        # [Line 18] | ASSIGNMENT: Creates variable 'rounded_value' and stores the result of 'round_number(7.5)' in it | FUNCTION CALL: Calls 'round_number()' and stores its return value
print(f"Rounded value of 7.5: {rounded_value}")          # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1197
Write a Python program to create a dictionary and access its value using a key. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1197 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def access_value():                                      # [Line 13]
    sample_dict = {"name": "Alice", "age": 30}           # [Line 14]
    return sample_dict["name"]                           # [Line 15]

result = access_value()                                  # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'access_value()' in it | FUNCTION CALL: Calls 'access_value()' and stores its return value
print(f"Value accessed: {result}")                       # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1198
Write a Python program to add a key-value pair to an existing dictionary. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1198 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def add_key_value():                                     # [Line 13]
    sample_dict = {"name": "Alice", "age": 30}           # [Line 14]
    sample_dict["city"] = "New York"                     # [Line 15]
    return sample_dict                                   # [Line 16]

updated_dict = add_key_value()                           # [Line 18] | ASSIGNMENT: Creates variable 'updated_dict' and stores the result of 'add_key_value()' in it | FUNCTION CALL: Calls 'add_key_value()' and stores its return value
print(f"Updated dictionary: {updated_dict}")             # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1199
Write a Python program to remove a key-value pair from a dictionary. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1199 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def remove_key():                                        # [Line 13]
    sample_dict = {"name": "Alice", "age": 30, "city": "New York"}  # [Line 14]
    del sample_dict["city"]                              # [Line 15]
    return sample_dict                                   # [Line 16]

updated_dict = remove_key()                              # [Line 18] | ASSIGNMENT: Creates variable 'updated_dict' and stores the result of 'remove_key()' in it | FUNCTION CALL: Calls 'remove_key()' and stores its return value
print(f"Dictionary after removal: {updated_dict}")       # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1200
Write a Python program to get all the keys from a dictionary. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1200 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def get_keys():                                          # [Line 13]
    sample_dict = {"name": "Alice", "age": 30, "city": "New York"}  # [Line 14]
    return sample_dict.keys()                            # [Line 15]

keys = get_keys()                                        # [Line 17] | ASSIGNMENT: Creates variable 'keys' and stores the result of 'get_keys()' in it | FUNCTION CALL: Calls 'get_keys()' and stores its return value
print(f"Keys in dictionary: {keys}")                     # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1201
Write a Python program to get all the values from a dictionary. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1201 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def get_values():                                        # [Line 13]
    sample_dict = {"name": "Alice", "age": 30, "city": "New York"}  # [Line 14]
    return sample_dict.values()                          # [Line 15]

values = get_values()                                    # [Line 17] | ASSIGNMENT: Creates variable 'values' and stores the result of 'get_values()' in it | FUNCTION CALL: Calls 'get_values()' and stores its return value
print(f"Values in dictionary: {values}")                 # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1202
Write a Python program to check if a key exists in a dictionary. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1202 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_key():                                         # [Line 13]
    sample_dict = {"name": "Alice", "age": 30, "city": "New York"}  # [Line 14]
    return "age" in sample_dict                          # [Line 15]

result = check_key()                                     # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_key()' in it | FUNCTION CALL: Calls 'check_key()' and stores its return value
print(f"Key exists: {result}")                           # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1203
Write a Python program to get the value associated with a key, or return a default value if the key doesn't exist. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1203 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def get_value(dictionary, key, default=None):            # [Line 13]
    
    return dictionary.get(key, default)                  # [Line 15]

# Example usage:
my_dict = {'a': 1, 'b': 2, 'c': 3}                       # [Line 18] | ASSIGNMENT: Creates variable 'my_dict' and stores the result of '{'a': 1, 'b': 2, 'c': 3}' in it
print(get_value(my_dict, 'a'))                           # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Output: 1
print(get_value(my_dict, 'd', 'not found'))              # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Output: not found

def get_value_or_default():                              # [Line 22]
    sample_dict = {"name": "Alice", "age": 30}           # [Line 23]
    return sample_dict.get("city", "Unknown")            # [Line 24]

result = get_value_or_default()                          # [Line 26] | ASSIGNMENT: Creates variable 'result' and stores the result of 'get_value_or_default()' in it | FUNCTION CALL: Calls 'get_value_or_default()' and stores its return value
print(f"Value: {result}")                                # [Line 27] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1204
Write a Python program to clear all items from a dictionary. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1204 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def clear_dict():                                        # [Line 13]
    sample_dict = {"name": "Alice", "age": 30, "city": "New York"}  # [Line 14]
    sample_dict.clear()                                  # [Line 15]
    return sample_dict                                   # [Line 16]

updated_dict = clear_dict()                              # [Line 18] | ASSIGNMENT: Creates variable 'updated_dict' and stores the result of 'clear_dict()' in it | FUNCTION CALL: Calls 'clear_dict()' and stores its return value
print(f"Dictionary after clearing: {updated_dict}")      # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1205
Write a Python program to copy a dictionary. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1205 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def copy_dict():                                         # [Line 13]
    sample_dict = {"name": "Alice", "age": 30}           # [Line 14]
    return sample_dict.copy()                            # [Line 15]

copied_dict = copy_dict()                                # [Line 17] | ASSIGNMENT: Creates variable 'copied_dict' and stores the result of 'copy_dict()' in it | FUNCTION CALL: Calls 'copy_dict()' and stores its return value
print(f"Copied dictionary: {copied_dict}")               # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1206
Write a Python program to merge two dictionaries. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1206 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def merge_dicts():                                       # [Line 13]
    dict1 = {"name": "Alice", "age": 30}                 # [Line 14]
    dict2 = {"city": "New York", "job": "Engineer"}      # [Line 15]
    dict1.update(dict2)                                  # [Line 16]
    return dict1                                         # [Line 17]

merged_dict = merge_dicts()                              # [Line 19] | ASSIGNMENT: Creates variable 'merged_dict' and stores the result of 'merge_dicts()' in it | FUNCTION CALL: Calls 'merge_dicts()' and stores its return value
print(f"Merged dictionary: {merged_dict}")               # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1207
Write a Python program to iterate through all key-value pairs in a dictionary. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1207 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def iterate_dict():                                      # [Line 13]
    sample_dict = {"name": "Alice", "age": 30, "city": "New York"}  # [Line 14]
    for key, value in sample_dict.items():               # [Line 15]
        print(f"{key}: {value}")                         # [Line 16]

iterate_dict()                                           # [Line 18] | FUNCTION CALL: Executes the function 'iterate_dict'

"""
Problem: 1208
Write a Python program to find the length of a dictionary. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1208 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def dict_length():                                       # [Line 13]
    sample_dict = {"name": "Alice", "age": 30, "city": "New York"}  # [Line 14]
    return len(sample_dict)                              # [Line 15]

length = dict_length()                                   # [Line 17] | ASSIGNMENT: Creates variable 'length' and stores the result of 'dict_length()' in it | FUNCTION CALL: Calls 'dict_length()' and stores its return value
print(f"Length of dictionary: {length}")                 # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1209
Write a Python program to reverse the keys and values in a dictionary. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1209 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def reverse_dict():                                      # [Line 13]
    sample_dict = {"name": "Alice", "age": 30, "city": "New York"}  # [Line 14]
    return {v: k for k, v in sample_dict.items()}        # [Line 15]

reversed_dict = reverse_dict()                           # [Line 17] | ASSIGNMENT: Creates variable 'reversed_dict' and stores the result of 'reverse_dict()' in it | FUNCTION CALL: Calls 'reverse_dict()' and stores its return value
print(f"Reversed dictionary: {reversed_dict}")           # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1210
Write a Python program to create a dictionary from two lists, one for keys and one for values. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1210 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def create_dict_from_lists():                            # [Line 13]
    keys = ["name", "age", "city"]                       # [Line 14]
    values = ["Alice", 30, "New York"]                   # [Line 15]
    return dict(zip(keys, values))                       # [Line 16]

created_dict = create_dict_from_lists()                  # [Line 18] | ASSIGNMENT: Creates variable 'created_dict' and stores the result of 'create_dict_from_lists()' in it | FUNCTION CALL: Calls 'create_dict_from_lists()' and stores its return value
print(f"Created dictionary: {created_dict}")             # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1211
Write a Python program to get the sum of all values in a dictionary. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1211 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def sum_values():                                        # [Line 13]
    sample_dict = {"a": 10, "b": 20, "c": 30}            # [Line 14]
    return sum(sample_dict.values())                     # [Line 15]

total = sum_values()                                     # [Line 17] | ASSIGNMENT: Creates variable 'total' and stores the result of 'sum_values()' in it | FUNCTION CALL: Calls 'sum_values()' and stores its return value
print(f"Sum of values: {total}")                         # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1212
Write a Python program to filter a dictionary based on a condition. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1212 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def filter_dict():                                       # [Line 13]
    sample_dict = {"name": "Alice", "age": 30, "city": "New York"}  # [Line 14]
    return {key: value for key, value in sample_dict.items() if isinstance(value, str)}  # [Line 15]

filtered_dict = filter_dict()                            # [Line 17] | ASSIGNMENT: Creates variable 'filtered_dict' and stores the result of 'filter_dict()' in it | FUNCTION CALL: Calls 'filter_dict()' and stores its return value
print(f"Filtered dictionary: {filtered_dict}")           # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1213
Write a Python program to find the maximum value in a dictionary. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1213 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def max_value():                                         # [Line 13]
    sample_dict = {"a": 10, "b": 20, "c": 30}            # [Line 14]
    return max(sample_dict.values())                     # [Line 15]

max_val = max_value()                                    # [Line 17] | ASSIGNMENT: Creates variable 'max_val' and stores the result of 'max_value()' in it | FUNCTION CALL: Calls 'max_value()' and stores its return value
print(f"Maximum value: {max_val}")                       # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1214
Write a Python program to check if a dictionary is empty. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1214 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def is_dict_empty():                                     # [Line 13]
    sample_dict = {}                                     # [Line 14]
    return len(sample_dict) == 0                         # [Line 15] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

result = is_dict_empty()                                 # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'is_dict_empty()' in it | FUNCTION CALL: Calls 'is_dict_empty()' and stores its return value
print(f"Is dictionary empty? {result}")                  # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1215
Write a Python program to remove all occurrences of a value in a dictionary. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1215 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def remove_value():                                      # [Line 13]
    sample_dict = {"a": 10, "b": 20, "c": 10}            # [Line 14]
    sample_dict = {k: v for k, v in sample_dict.items() if v != 10}  # [Line 15]
    return sample_dict                                   # [Line 16]

updated_dict = remove_value()                            # [Line 18] | ASSIGNMENT: Creates variable 'updated_dict' and stores the result of 'remove_value()' in it | FUNCTION CALL: Calls 'remove_value()' and stores its return value
print(f"Dictionary after removal: {updated_dict}")       # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1216
Write a Python program to find the key associated with a given value in a dictionary. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1216 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def find_key_by_value():                                 # [Line 13]
    sample_dict = {"a": 10, "b": 20, "c": 30}            # [Line 14]
    return [k for k, v in sample_dict.items() if v == 20]  # [Line 15] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

key = find_key_by_value()                                # [Line 17] | ASSIGNMENT: Creates variable 'key' and stores the result of 'find_key_by_value()' in it | FUNCTION CALL: Calls 'find_key_by_value()' and stores its return value
print(f"Key for value 20: {key}")                        # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1217
Write a Python program to create a dictionary with default values using `defaultdict`. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1217 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from collections import defaultdict                      # [Line 13]

def create_defaultdict():                                # [Line 15]
    sample_dict = defaultdict(int)                       # [Line 16]
    sample_dict["a"] += 1                                # [Line 17]
    sample_dict["b"] += 2                                # [Line 18]
    return dict(sample_dict)                             # [Line 19]

default_dict = create_defaultdict()                      # [Line 21] | ASSIGNMENT: Creates variable 'default_dict' and stores the result of 'create_defaultdict()' in it | FUNCTION CALL: Calls 'create_defaultdict()' and stores its return value
print(f"Default dictionary: {default_dict}")             # [Line 22] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1218
Write a Python program to get the first key-value pair from a dictionary. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1218 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def first_key_value():                                   # [Line 13]
    sample_dict = {"a": 10, "b": 20, "c": 30}            # [Line 14]
    first_item = list(sample_dict.items())[0]            # [Line 15]
    return first_item                                    # [Line 16]

first_item = first_key_value()                           # [Line 18] | ASSIGNMENT: Creates variable 'first_item' and stores the result of 'first_key_value()' in it | FUNCTION CALL: Calls 'first_key_value()' and stores its return value
print(f"First key-value pair: {first_item}")             # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1219
Write a Python program to merge multiple dictionaries into one. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1219 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def merge_multiple_dicts():                              # [Line 13]
    dict1 = {"a": 10, "b": 20}                           # [Line 14]
    dict2 = {"c": 30, "d": 40}                           # [Line 15]
    dict3 = {"e": 50}                                    # [Line 16]
    merged_dict = {**dict1, **dict2, **dict3}            # [Line 17] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    return merged_dict                                   # [Line 18]

merged_dict = merge_multiple_dicts()                     # [Line 20] | ASSIGNMENT: Creates variable 'merged_dict' and stores the result of 'merge_multiple_dicts()' in it | FUNCTION CALL: Calls 'merge_multiple_dicts()' and stores its return value
print(f"Merged dictionary: {merged_dict}")               # [Line 21] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1220
Write a Python program to convert a list of tuples into a dictionary. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1220 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def list_to_dict():                                      # [Line 13]
    sample_list = [("a", 1), ("b", 2), ("c", 3)]         # [Line 14]
    return dict(sample_list)                             # [Line 15]

converted_dict = list_to_dict()                          # [Line 17] | ASSIGNMENT: Creates variable 'converted_dict' and stores the result of 'list_to_dict()' in it | FUNCTION CALL: Calls 'list_to_dict()' and stores its return value
print(f"Converted dictionary: {converted_dict}")         # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1221
Write a Python program to create a Path object using the `pathlib` module.
"""

# ======================================================================
# PROBLEM 1221 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 13]

def create_path():                                       # [Line 15]
    p = Path("example_directory")                        # [Line 16]
    return p                                             # [Line 17]

path = create_path()                                     # [Line 19] | ASSIGNMENT: Creates variable 'path' and stores the result of 'create_path()' in it | FUNCTION CALL: Calls 'create_path()' and stores its return value
print(f"Created path: {path}")                           # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1222
Write a Python program to check if a path exists using `pathlib`.
"""

# ======================================================================
# PROBLEM 1222 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 13]

def check_path_exists():                                 # [Line 15]
    p = Path("example_directory")                        # [Line 16]
    return p.exists()                                    # [Line 17]

exists = check_path_exists()                             # [Line 19] | ASSIGNMENT: Creates variable 'exists' and stores the result of 'check_path_exists()' in it | FUNCTION CALL: Calls 'check_path_exists()' and stores its return value
print(f"Path exists: {exists}")                          # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1223
Write a Python program to check if a path is a file using `pathlib`.
"""

# ======================================================================
# PROBLEM 1223 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 13]

def check_if_file():                                     # [Line 15]
    p = Path("example_file.txt")                         # [Line 16]
    return p.is_file()                                   # [Line 17]

is_file = check_if_file()                                # [Line 19] | ASSIGNMENT: Creates variable 'is_file' and stores the result of 'check_if_file()' in it | FUNCTION CALL: Calls 'check_if_file()' and stores its return value
print(f"Is it a file? {is_file}")                        # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1224
Write a Python program to check if a path is a directory using `pathlib`.
"""

# ======================================================================
# PROBLEM 1224 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 13]

def check_if_directory():                                # [Line 15]
    p = Path("example_directory")                        # [Line 16]
    return p.is_dir()                                    # [Line 17]

is_directory = check_if_directory()                      # [Line 19] | ASSIGNMENT: Creates variable 'is_directory' and stores the result of 'check_if_directory()' in it | FUNCTION CALL: Calls 'check_if_directory()' and stores its return value
print(f"Is it a directory? {is_directory}")              # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1225
Write a Python program to get the file name from a path using `pathlib`.
"""

# ======================================================================
# PROBLEM 1225 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 13]

def get_file_name():                                     # [Line 15]
    p = Path("example_directory/example_file.txt")       # [Line 16]
    return p.name                                        # [Line 17]

file_name = get_file_name()                              # [Line 19] | ASSIGNMENT: Creates variable 'file_name' and stores the result of 'get_file_name()' in it | FUNCTION CALL: Calls 'get_file_name()' and stores its return value
print(f"File name: {file_name}")                         # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1226
Write a Python program to get the parent directory of a path using `pathlib`.
"""

# ======================================================================
# PROBLEM 1226 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 13]

def get_parent_directory():                              # [Line 15]
    p = Path("example_directory/example_file.txt")       # [Line 16]
    return p.parent                                      # [Line 17]

parent_directory = get_parent_directory()                # [Line 19] | ASSIGNMENT: Creates variable 'parent_directory' and stores the result of 'get_parent_directory()' in it | FUNCTION CALL: Calls 'get_parent_directory()' and stores its return value
print(f"Parent directory: {parent_directory}")           # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1227
Write a Python program to join two paths using `pathlib`.
"""

# ======================================================================
# PROBLEM 1227 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 13]

def join_paths():                                        # [Line 15]
    p1 = Path("example_directory")                       # [Line 16]
    p2 = "example_file.txt"                              # [Line 17]
    return p1 / p2                                       # [Line 18]

joined_path = join_paths()                               # [Line 20] | ASSIGNMENT: Creates variable 'joined_path' and stores the result of 'join_paths()' in it | FUNCTION CALL: Calls 'join_paths()' and stores its return value
print(f"Joined path: {joined_path}")                     # [Line 21] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1228
Write a Python program to get the file extension of a path using `pathlib`.
"""

# ======================================================================
# PROBLEM 1228 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 13]

def get_file_extension():                                # [Line 15]
    p = Path("example_file.txt")                         # [Line 16]
    return p.suffix                                      # [Line 17]

file_extension = get_file_extension()                    # [Line 19] | ASSIGNMENT: Creates variable 'file_extension' and stores the result of 'get_file_extension()' in it | FUNCTION CALL: Calls 'get_file_extension()' and stores its return value
print(f"File extension: {file_extension}")               # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1229
Write a Python program to get the size of a file using `pathlib`.
"""

# ======================================================================
# PROBLEM 1229 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 13]

def get_file_size():                                     # [Line 15]
    p = Path("example_file.txt")                         # [Line 16]
    return p.stat().st_size                              # [Line 17]

file_size = get_file_size()                              # [Line 19] | ASSIGNMENT: Creates variable 'file_size' and stores the result of 'get_file_size()' in it | FUNCTION CALL: Calls 'get_file_size()' and stores its return value
print(f"File size: {file_size} bytes")                   # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1230
Write a Python program to rename a file using `pathlib`.
"""

# ======================================================================
# PROBLEM 1230 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 13]

def rename_file():                                       # [Line 15]
    old_path = Path("old_file.txt")                      # [Line 16]
    new_path = Path("new_file.txt")                      # [Line 17]
    old_path.rename(new_path)                            # [Line 18]
    return new_path                                      # [Line 19]

renamed_file = rename_file()                             # [Line 21] | ASSIGNMENT: Creates variable 'renamed_file' and stores the result of 'rename_file()' in it | FUNCTION CALL: Calls 'rename_file()' and stores its return value
print(f"Renamed file: {renamed_file}")                   # [Line 22] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1231
Write a Python program to create a new directory using `pathlib`.
"""

# ======================================================================
# PROBLEM 1231 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 13]

def create_directory():                                  # [Line 15]
    p = Path("new_directory")                            # [Line 16]
    p.mkdir(parents=True, exist_ok=True)                 # [Line 17]
    return p                                             # [Line 18]

created_directory = create_directory()                   # [Line 20] | ASSIGNMENT: Creates variable 'created_directory' and stores the result of 'create_directory()' in it | FUNCTION CALL: Calls 'create_directory()' and stores its return value
print(f"Created directory: {created_directory}")         # [Line 21] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1232
Write a Python program to remove a directory using `pathlib`.
"""

# ======================================================================
# PROBLEM 1232 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 13]

def remove_directory():                                  # [Line 15]
    p = Path("new_directory")                            # [Line 16]
    p.rmdir()                                            # [Line 17]
    return f"Directory {p} removed"                      # [Line 18]

removed_directory = remove_directory()                   # [Line 20] | ASSIGNMENT: Creates variable 'removed_directory' and stores the result of 'remove_directory()' in it | FUNCTION CALL: Calls 'remove_directory()' and stores its return value
print(removed_directory)                                 # [Line 21] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1233
Write a Python program to remove a file using `pathlib`.
"""

# ======================================================================
# PROBLEM 1233 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 13]

def remove_file():                                       # [Line 15]
    p = Path("example_file.txt")                         # [Line 16]
    p.unlink()                                           # [Line 17]
    return f"File {p} removed"                           # [Line 18]

removed_file = remove_file()                             # [Line 20] | ASSIGNMENT: Creates variable 'removed_file' and stores the result of 'remove_file()' in it | FUNCTION CALL: Calls 'remove_file()' and stores its return value
print(removed_file)                                      # [Line 21] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1234
Write a Python program to get the absolute path of a file using `pathlib`.
"""

# ======================================================================
# PROBLEM 1234 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 13]

def get_absolute_path():                                 # [Line 15]
    p = Path("example_file.txt")                         # [Line 16]
    return p.resolve()                                   # [Line 17]

absolute_path = get_absolute_path()                      # [Line 19] | ASSIGNMENT: Creates variable 'absolute_path' and stores the result of 'get_absolute_path()' in it | FUNCTION CALL: Calls 'get_absolute_path()' and stores its return value
print(f"Absolute path: {absolute_path}")                 # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1235
Write a Python program to check if a path is a symbolic link using `pathlib`.
"""

# ======================================================================
# PROBLEM 1235 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 13]

def check_if_symlink():                                  # [Line 15]
    p = Path("example_symlink")                          # [Line 16]
    return p.is_symlink()                                # [Line 17]

is_symlink = check_if_symlink()                          # [Line 19] | ASSIGNMENT: Creates variable 'is_symlink' and stores the result of 'check_if_symlink()' in it | FUNCTION CALL: Calls 'check_if_symlink()' and stores its return value
print(f"Is it a symbolic link? {is_symlink}")            # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1236
Write a Python program to create a symbolic link using `pathlib`.
"""

# ======================================================================
# PROBLEM 1236 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 13]

def create_symlink():                                    # [Line 15]
    target = Path("example_file.txt")                    # [Line 16]
    symlink = Path("example_symlink")                    # [Line 17]
    symlink.symlink_to(target)                           # [Line 18]
    return symlink                                       # [Line 19]

symlink = create_symlink()                               # [Line 21] | ASSIGNMENT: Creates variable 'symlink' and stores the result of 'create_symlink()' in it | FUNCTION CALL: Calls 'create_symlink()' and stores its return value
print(f"Created symlink: {symlink}")                     # [Line 22] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1237
Write a Python program to check if a path is a directory and if it contains files using `pathlib`.
"""

# ======================================================================
# PROBLEM 1237 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 13]

def check_directory_and_files():                         # [Line 15]
    p = Path("example_directory")                        # [Line 16]
    if p.is_dir():                                       # [Line 17]
        return [file.name for file in p.iterdir()]       # [Line 18]
    return []                                            # [Line 19]

directory_files = check_directory_and_files()            # [Line 21] | ASSIGNMENT: Creates variable 'directory_files' and stores the result of 'check_directory_and_files()' in it | FUNCTION CALL: Calls 'check_directory_and_files()' and stores its return value
print(f"Files in directory: {directory_files}")          # [Line 22] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1238
Write a Python program to get the last modified time of a file using `pathlib`.
"""

# ======================================================================
# PROBLEM 1238 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 13]
import time                                              # [Line 14]

def get_last_modified_time():                            # [Line 16]
    p = Path("example_file.txt")                         # [Line 17]
    timestamp = p.stat().st_mtime                        # [Line 18]
    return time.ctime(timestamp)                         # [Line 19]

last_modified_time = get_last_modified_time()            # [Line 21] | ASSIGNMENT: Creates variable 'last_modified_time' and stores the result of 'get_last_modified_time()' in it | FUNCTION CALL: Calls 'get_last_modified_time()' and stores its return value
print(f"Last modified time: {last_modified_time}")       # [Line 22] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1239
Write a Python program to get the directory name from a path using `pathlib`.
"""

# ======================================================================
# PROBLEM 1239 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 13]

def get_directory_name():                                # [Line 15]
    p = Path("example_directory/example_file.txt")       # [Line 16]
    return p.parent.name                                 # [Line 17]

directory_name = get_directory_name()                    # [Line 19] | ASSIGNMENT: Creates variable 'directory_name' and stores the result of 'get_directory_name()' in it | FUNCTION CALL: Calls 'get_directory_name()' and stores its return value
print(f"Directory name: {directory_name}")               # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1240
Write a Python program to check if a path is empty (no files) using `pathlib`.
"""

# ======================================================================
# PROBLEM 1240 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 13]

def check_if_empty():                                    # [Line 15]
    p = Path("example_directory")                        # [Line 16]
    return len(list(p.iterdir())) == 0                   # [Line 17] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

is_empty = check_if_empty()                              # [Line 19] | ASSIGNMENT: Creates variable 'is_empty' and stores the result of 'check_if_empty()' in it | FUNCTION CALL: Calls 'check_if_empty()' and stores its return value
print(f"Is directory empty? {is_empty}")                 # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1241
Write a Python program to iterate over all files in a directory using `pathlib`.
"""

# ======================================================================
# PROBLEM 1241 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 13]

def iterate_files():                                     # [Line 15]
    p = Path("example_directory")                        # [Line 16]
    return [file.name for file in p.iterdir() if file.is_file()]  # [Line 17]

files_in_directory = iterate_files()                     # [Line 19] | ASSIGNMENT: Creates variable 'files_in_directory' and stores the result of 'iterate_files()' in it | FUNCTION CALL: Calls 'iterate_files()' and stores its return value
print(f"Files in directory: {files_in_directory}")       # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1242
Write a Python program to find the path to the parent directory using `pathlib`.
"""

# ======================================================================
# PROBLEM 1242 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 13]

def get_parent_directory():                              # [Line 15]
    p = Path("example_directory/example_file.txt")       # [Line 16]
    return p.parent.parent                               # [Line 17]

parent_directory = get_parent_directory()                # [Line 19] | ASSIGNMENT: Creates variable 'parent_directory' and stores the result of 'get_parent_directory()' in it | FUNCTION CALL: Calls 'get_parent_directory()' and stores its return value
print(f"Parent directory: {parent_directory}")           # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1243
Write a Python program to check if a file has a certain extension using `pathlib`.
"""

# ======================================================================
# PROBLEM 1243 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 13]

def check_file_extension():                              # [Line 15]
    p = Path("example_file.txt")                         # [Line 16]
    return p.suffix == ".txt"                            # [Line 17] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

has_extension = check_file_extension()                   # [Line 19] | ASSIGNMENT: Creates variable 'has_extension' and stores the result of 'check_file_extension()' in it | FUNCTION CALL: Calls 'check_file_extension()' and stores its return value
print(f"Has .txt extension? {has_extension}")            # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1244
Write a Python program to get the file size using `pathlib` in human-readable format.
"""

# ======================================================================
# PROBLEM 1244 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 13]

def get_human_readable_size():                           # [Line 15]
    p = Path("example_file.txt")                         # [Line 16]
    size_in_bytes = p.stat().st_size                     # [Line 17]
    return f"{size_in_bytes / 1024:.2f} KB"              # [Line 18]

size = get_human_readable_size()                         # [Line 20] | ASSIGNMENT: Creates variable 'size' and stores the result of 'get_human_readable_size()' in it | FUNCTION CALL: Calls 'get_human_readable_size()' and stores its return value
print(f"File size: {size}")                              # [Line 21] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1245
Write a Python program to change the current working directory using `pathlib`.
"""

# ======================================================================
# PROBLEM 1245 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 13]

def change_working_directory():                          # [Line 15]
    p = Path("example_directory")                        # [Line 16]
    p.chdir()                                            # [Line 17]
    return f"Changed working directory to: {p}"          # [Line 18]

changed_directory = change_working_directory()           # [Line 20] | ASSIGNMENT: Creates variable 'changed_directory' and stores the result of 'change_working_directory()' in it | FUNCTION CALL: Calls 'change_working_directory()' and stores its return value
print(changed_directory)                                 # [Line 21] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1246
Write a Python program to check if two conditions are true using the `and` operator.
"""

# ======================================================================
# PROBLEM 1246 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_conditions():                                  # [Line 13]
    a = 5                                                # [Line 14]
    b = 10                                               # [Line 15]
    return a > 3 and b < 15                              # [Line 16]

result = check_conditions()                              # [Line 18] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_conditions()' in it | FUNCTION CALL: Calls 'check_conditions()' and stores its return value
print(f"Both conditions are true: {result}")             # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1247
Write a Python program to check if a number is between 10 and 20 (both inclusive) using the `and` operator.
"""

# ======================================================================
# PROBLEM 1247 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_range():                                       # [Line 13]
    num = 15                                             # [Line 14]
    return num >= 10 and num <= 20                       # [Line 15]

result = check_range()                                   # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_range()' in it | FUNCTION CALL: Calls 'check_range()' and stores its return value
print(f"Number is between 10 and 20: {result}")          # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1248
Write a Python program to check if a string is non-empty and contains a specific character using the `and` operator.
"""

# ======================================================================
# PROBLEM 1248 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_string():                                      # [Line 13]
    text = "hello"                                       # [Line 14]
    return len(text) > 0 and "e" in text                 # [Line 15]

result = check_string()                                  # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_string()' in it | FUNCTION CALL: Calls 'check_string()' and stores its return value
print(f"String is non-empty and contains 'e': {result}")  # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1249
Write a Python program to check if a number is divisible by both 3 and 5 using the `and` operator.
"""

# ======================================================================
# PROBLEM 1249 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def main(number):                                        # [Line 13]
    return True if number % 3 == 0 and number % 5 == 0 else False  # [Line 14] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
    
number = 15                                              # [Line 16] | ASSIGNMENT: Creates variable 'number' and stores the result of '15' in it | DATA TYPE: Integer - A whole number: 15
main(number)                                             # [Line 17] | FUNCTION CALL: Executes the function 'main' | ARGUMENTS: Passes 1 argument(s) to the function

def check_divisibility():                                # [Line 19]
    num = 15                                             # [Line 20]
    return num % 3 == 0 and num % 5 == 0                 # [Line 21] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_divisibility()                            # [Line 23] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_divisibility()' in it | FUNCTION CALL: Calls 'check_divisibility()' and stores its return value
print(f"Number is divisible by both 3 and 5: {result}")  # [Line 24] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

def main(number):                                        # [Line 26]
    return number % 3 == 0 and number % 5 == 0           # [Line 27] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
    
number = 15                                              # [Line 29] | ASSIGNMENT: Creates variable 'number' and stores the result of '15' in it | DATA TYPE: Integer - A whole number: 15
main(number)                                             # [Line 30] | FUNCTION CALL: Executes the function 'main' | ARGUMENTS: Passes 1 argument(s) to the function

"""
Problem: 1250
Write a Python program to check if a list is non-empty and the first element is greater than 5 using the `and` operator.
"""

# ======================================================================
# PROBLEM 1250 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_list():                                        # [Line 13]
    lst = [6, 2, 8]                                      # [Line 14]
    return len(lst) > 0 and lst[0] > 5                   # [Line 15]

result = check_list()                                    # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_list()' in it | FUNCTION CALL: Calls 'check_list()' and stores its return value
print(f"List is non-empty and first element is greater than 5: {result}")  # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1251
Write a Python program to check if a year is a leap year using the `and` operator.
"""

# ======================================================================
# PROBLEM 1251 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_leap_year():                                   # [Line 13]
    year = 2024                                          # [Line 14]
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)  # [Line 15] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_leap_year()                               # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_leap_year()' in it | FUNCTION CALL: Calls 'check_leap_year()' and stores its return value
print(f"Year is a leap year: {result}")                  # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1252
Write a Python program to check if a number is positive, even, and divisible by 4 using the `and` operator.
"""

# ======================================================================
# PROBLEM 1252 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_number():                                      # [Line 13]
    num = 8                                              # [Line 14]
    return num > 0 and num % 2 == 0 and num % 4 == 0     # [Line 15] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_number()                                  # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_number()' in it | FUNCTION CALL: Calls 'check_number()' and stores its return value
print(f"Number is positive, even, and divisible by 4: {result}")  # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1253
Write a Python program to check if a list contains exactly three elements, and the first element is greater than 5 using the `and` operator.
"""

# ======================================================================
# PROBLEM 1253 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_list_conditions():                             # [Line 13]
    lst = [6, 2, 8]                                      # [Line 14]
    return len(lst) == 3 and lst[0] > 5                  # [Line 15] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

result = check_list_conditions()                         # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_list_conditions()' in it | FUNCTION CALL: Calls 'check_list_conditions()' and stores its return value
print(f"List has three elements and first is greater than 5: {result}")  # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1254
Write a Python program to check if a string is lowercase and its length is greater than 3 using the `and` operator.
"""

# ======================================================================
# PROBLEM 1254 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_string_conditions():                           # [Line 13]
    text = "hello"                                       # [Line 14]
    return text.islower() and len(text) > 3              # [Line 15]

result = check_string_conditions()                       # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_string_conditions()' in it | FUNCTION CALL: Calls 'check_string_conditions()' and stores its return value
print(f"String is lowercase and its length is greater than 3: {result}")  # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1255
Write a Python program to check if a number is greater than 10 and less than 50 using the `and` operator.
"""

# ======================================================================
# PROBLEM 1255 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_range_conditions():                            # [Line 13]
    num = 30                                             # [Line 14]
    return num > 10 and num < 50                         # [Line 15]

result = check_range_conditions()                        # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_range_conditions()' in it | FUNCTION CALL: Calls 'check_range_conditions()' and stores its return value
print(f"Number is between 10 and 50: {result}")          # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1256
Write a Python program to check if a number is both a multiple of 7 and 11 using the `and` operator.
"""

# ======================================================================
# PROBLEM 1256 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_multiples():                                   # [Line 13]
    num = 77                                             # [Line 14]
    return num % 7 == 0 and num % 11 == 0                # [Line 15] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_multiples()                               # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_multiples()' in it | FUNCTION CALL: Calls 'check_multiples()' and stores its return value
print(f"Number is a multiple of both 7 and 11: {result}")  # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1257
Write a Python program to check if a person is eligible to vote, meaning the age is greater than 18 and they are a citizen, using the `and` operator.
"""

# ======================================================================
# PROBLEM 1257 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_voting_eligibility():                          # [Line 13]
    age = 20                                             # [Line 14]
    is_citizen = True                                    # [Line 15]
    return age > 18 and is_citizen                       # [Line 16]

result = check_voting_eligibility()                      # [Line 18] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_voting_eligibility()' in it | FUNCTION CALL: Calls 'check_voting_eligibility()' and stores its return value
print(f"Person is eligible to vote: {result}")           # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1258
Write a Python program to check if a number is divisible by 2, 3, and 5 using the `and` operator.
"""

# ======================================================================
# PROBLEM 1258 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_divisibility_all():                            # [Line 13]
    num = 30                                             # [Line 14]
    return num % 2 == 0 and num % 3 == 0 and num % 5 == 0  # [Line 15] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_divisibility_all()                        # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_divisibility_all()' in it | FUNCTION CALL: Calls 'check_divisibility_all()' and stores its return value
print(f"Number is divisible by 2, 3, and 5: {result}")   # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1259
Write a Python program to check if a dictionary contains a specific key and the value is greater than a specified number using the `and` operator.
"""

# ======================================================================
# PROBLEM 1259 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_dict_conditions():                             # [Line 13]
    sample_dict = {"age": 30, "city": "New York"}        # [Line 14]
    return "age" in sample_dict and sample_dict["age"] > 25  # [Line 15]

result = check_dict_conditions()                         # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_dict_conditions()' in it | FUNCTION CALL: Calls 'check_dict_conditions()' and stores its return value
print(f"Dictionary contains 'age' and its value is greater than 25: {result}")  # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1260
Write a Python program to check if a string is not empty and its length is an even number using the `and` operator.
"""

# ======================================================================
# PROBLEM 1260 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_string_length():                               # [Line 13]
    text = "hello"                                       # [Line 14]
    return len(text) > 0 and len(text) % 2 == 0          # [Line 15] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_string_length()                           # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_string_length()' in it | FUNCTION CALL: Calls 'check_string_length()' and stores its return value
print(f"String is not empty and its length is even: {result}")  # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1261
Write a Python program to check if a number is within the range of 20 to 100 (inclusive) using the `and` operator.
"""

# ======================================================================
# PROBLEM 1261 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_range_inclusive():                             # [Line 13]
    num = 50                                             # [Line 14]
    return num >= 20 and num <= 100                      # [Line 15]

result = check_range_inclusive()                         # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_range_inclusive()' in it | FUNCTION CALL: Calls 'check_range_inclusive()' and stores its return value
print(f"Number is between 20 and 100 (inclusive): {result}")  # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1262
Write a Python program to check if a number is divisible by both 2 and 7 using the `and` operator.
"""

# ======================================================================
# PROBLEM 1262 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_divisible_by_2_and_7():                        # [Line 13]
    num = 14                                             # [Line 14]
    return num % 2 == 0 and num % 7 == 0                 # [Line 15] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_divisible_by_2_and_7()                    # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_divisible_by_2_and_7()' in it | FUNCTION CALL: Calls 'check_divisible_by_2_and_7()' and stores its return value
print(f"Number is divisible by both 2 and 7: {result}")  # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1263
Write a Python program to check if a number is negative and divisible by 5 using the `and` operator.
"""

# ======================================================================
# PROBLEM 1263 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_negative_and_divisible():                      # [Line 13]
    num = -25                                            # [Line 14]
    return num < 0 and num % 5 == 0                      # [Line 15] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_negative_and_divisible()                  # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_negative_and_divisible()' in it | FUNCTION CALL: Calls 'check_negative_and_divisible()' and stores its return value
print(f"Number is negative and divisible by 5: {result}")  # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1264
Write a Python program to check if a string contains only digits and its length is greater than 5 using the `and` operator.
"""

# ======================================================================
# PROBLEM 1264 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_digit_string():                                # [Line 13]
    text = "123456"                                      # [Line 14]
    return text.isdigit() and len(text) > 5              # [Line 15]

result = check_digit_string()                            # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_digit_string()' in it | FUNCTION CALL: Calls 'check_digit_string()' and stores its return value
print(f"String contains only digits and its length is greater than 5: {result}")  # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1265
Write a Python program to check if a number is a prime number and greater than 10 using the `and` operator.
"""

# ======================================================================
# PROBLEM 1265 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_prime_and_greater_than_10():                   # [Line 13]
    num = 13                                             # [Line 14]
    return num > 10 and all(num % i != 0 for i in range(2, num))  # [Line 15] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_prime_and_greater_than_10()               # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_prime_and_greater_than_10()' in it | FUNCTION CALL: Calls 'check_prime_and_greater_than_10()' and stores its return value
print(f"Number is prime and greater than 10: {result}")  # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1266
Write a Python program to check if a number is odd and greater than 0 using the `and` operator.
"""

# ======================================================================
# PROBLEM 1266 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_odd_and_positive():                            # [Line 13]
    num = 7                                              # [Line 14]
    return num % 2 != 0 and num > 0                      # [Line 15] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_odd_and_positive()                        # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_odd_and_positive()' in it | FUNCTION CALL: Calls 'check_odd_and_positive()' and stores its return value
print(f"Number is odd and positive: {result}")           # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1267
Write a Python program to check if a file exists and its size is greater than 100 KB using the `and` operator.
"""

# ======================================================================
# PROBLEM 1267 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 13]

def check_file_exists_and_size():                        # [Line 15]
    p = Path("example_file.txt")                         # [Line 16]
    return p.exists() and p.stat().st_size > 100 * 1024  # [Line 17]

result = check_file_exists_and_size()                    # [Line 19] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_file_exists_and_size()' in it | FUNCTION CALL: Calls 'check_file_exists_and_size()' and stores its return value
print(f"File exists and its size is greater than 100 KB: {result}")  # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1268
Write a Python program to check if a list contains exactly 5 elements and the last element is greater than 10 using the `and` operator.
"""

# ======================================================================
# PROBLEM 1268 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_list_length_and_last_element():                # [Line 13]
    lst = [1, 2, 3, 4, 12]                               # [Line 14]
    return len(lst) == 5 and lst[-1] > 10                # [Line 15] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

result = check_list_length_and_last_element()            # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_list_length_and_last_element()' in it | FUNCTION CALL: Calls 'check_list_length_and_last_element()' and stores its return value
print(f"List contains exactly 5 elements and last element is greater than 10: {result}")  # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1269
Write a Python program to check if a number is between 1 and 10 (inclusive) and is odd using the `and` operator.
"""

# ======================================================================
# PROBLEM 1269 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_range_and_odd():                               # [Line 13]
    num = 7                                              # [Line 14]
    return num >= 1 and num <= 10 and num % 2 != 0       # [Line 15] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_range_and_odd()                           # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_range_and_odd()' in it | FUNCTION CALL: Calls 'check_range_and_odd()' and stores its return value
print(f"Number is between 1 and 10 and odd: {result}")   # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1270
Write a Python program to check if at least one of two conditions is true using the `or` operator.
"""

# ======================================================================
# PROBLEM 1270 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_conditions():                                  # [Line 13]
    a = 5                                                # [Line 14]
    b = 10                                               # [Line 15]
    return a > 10 or b < 15                              # [Line 16]

result = check_conditions()                              # [Line 18] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_conditions()' in it | FUNCTION CALL: Calls 'check_conditions()' and stores its return value
print(f"At least one condition is true: {result}")       # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1271
Write a Python program to check if a number is either less than 10 or greater than 20 using the `or` operator.
"""

# ======================================================================
# PROBLEM 1271 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_range():                                       # [Line 13]
    num = 5                                              # [Line 14]
    return num < 10 or num > 20                          # [Line 15]

result = check_range()                                   # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_range()' in it | FUNCTION CALL: Calls 'check_range()' and stores its return value
print(f"Number is either less than 10 or greater than 20: {result}")  # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1272
Write a Python program to check if a string is empty or contains a specific character using the `or` operator.
"""

# ======================================================================
# PROBLEM 1272 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_string():                                      # [Line 13]
    text = "hello"                                       # [Line 14]
    return len(text) == 0 or "e" in text                 # [Line 15] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

result = check_string()                                  # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_string()' in it | FUNCTION CALL: Calls 'check_string()' and stores its return value
print(f"String is empty or contains 'e': {result}")      # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1273
Write a Python program to check if a number is divisible by 3 or 5 using the `or` operator.
"""

# ======================================================================
# PROBLEM 1273 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_divisibility():                                # [Line 13]
    num = 9                                              # [Line 14]
    return num % 3 == 0 or num % 5 == 0                  # [Line 15] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_divisibility()                            # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_divisibility()' in it | FUNCTION CALL: Calls 'check_divisibility()' and stores its return value
print(f"Number is divisible by 3 or 5: {result}")        # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1274
Write a Python program to check if a list is empty or its first element is greater than 5 using the `or` operator.
"""

# ======================================================================
# PROBLEM 1274 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_list():                                        # [Line 13]
    lst = [6, 2, 8]                                      # [Line 14]
    return len(lst) == 0 or lst[0] > 5                   # [Line 15] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

result = check_list()                                    # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_list()' in it | FUNCTION CALL: Calls 'check_list()' and stores its return value
print(f"List is empty or its first element is greater than 5: {result}")  # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1275
Write a Python program to check if a year is a leap year or divisible by 100 using the `or` operator.
"""

# ======================================================================
# PROBLEM 1275 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_leap_year():                                   # [Line 13]
    year = 2024                                          # [Line 14]
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)  # [Line 15] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_leap_year()                               # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_leap_year()' in it | FUNCTION CALL: Calls 'check_leap_year()' and stores its return value
print(f"Year is a leap year or divisible by 100: {result}")  # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1276
Write a Python program to check if a number is positive or divisible by 7 using the `or` operator.
"""

# ======================================================================
# PROBLEM 1276 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_number():                                      # [Line 13]
    num = 10                                             # [Line 14]
    return num > 0 or num % 7 == 0                       # [Line 15] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_number()                                  # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_number()' in it | FUNCTION CALL: Calls 'check_number()' and stores its return value
print(f"Number is positive or divisible by 7: {result}")  # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1277
Write a Python program to check if a string is lowercase or its length is greater than 3 using the `or` operator.
"""

# ======================================================================
# PROBLEM 1277 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_string_conditions():                           # [Line 13]
    text = "HELLO"                                       # [Line 14]
    return text.islower() or len(text) > 3               # [Line 15]

result = check_string_conditions()                       # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_string_conditions()' in it | FUNCTION CALL: Calls 'check_string_conditions()' and stores its return value
print(f"String is lowercase or its length is greater than 3: {result}")  # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1278
Write a Python program to check if a number is between 10 and 50 or divisible by 7 using the `or` operator.
"""

# ======================================================================
# PROBLEM 1278 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_conditions():                                  # [Line 13]
    num = 30                                             # [Line 14]
    return (num >= 10 and num <= 50) or num % 7 == 0     # [Line 15] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_conditions()                              # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_conditions()' in it | FUNCTION CALL: Calls 'check_conditions()' and stores its return value
print(f"Number is between 10 and 50 or divisible by 7: {result}")  # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1279
Write a Python program to check if a number is a multiple of 7 or 11 using the `or` operator.
"""

# ======================================================================
# PROBLEM 1279 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_multiples():                                   # [Line 13]
    num = 77                                             # [Line 14]
    return num % 7 == 0 or num % 11 == 0                 # [Line 15] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_multiples()                               # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_multiples()' in it | FUNCTION CALL: Calls 'check_multiples()' and stores its return value
print(f"Number is a multiple of 7 or 11: {result}")      # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1280
Write a Python program to check if a person is eligible to vote, meaning the age is greater than 18 or they are a citizen, using the `or` operator.
"""

# ======================================================================
# PROBLEM 1280 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_voting_eligibility():                          # [Line 13]
    age = 17                                             # [Line 14]
    is_citizen = True                                    # [Line 15]
    return age > 18 or is_citizen                        # [Line 16]

result = check_voting_eligibility()                      # [Line 18] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_voting_eligibility()' in it | FUNCTION CALL: Calls 'check_voting_eligibility()' and stores its return value
print(f"Person is eligible to vote: {result}")           # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1281
Write a Python program to check if a number is divisible by 2 or 3 using the `or` operator.
"""

# ======================================================================
# PROBLEM 1281 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_divisibility_all():                            # [Line 13]
    num = 9                                              # [Line 14]
    return num % 2 == 0 or num % 3 == 0                  # [Line 15] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_divisibility_all()                        # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_divisibility_all()' in it | FUNCTION CALL: Calls 'check_divisibility_all()' and stores its return value
print(f"Number is divisible by 2 or 3: {result}")        # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1282
Write a Python program to check if a dictionary contains a specific key or if the value is greater than a specified number using the `or` operator.
"""

# ======================================================================
# PROBLEM 1282 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_dict_conditions():                             # [Line 13]
    sample_dict = {"age": 20, "city": "New York"}        # [Line 14]
    return "name" in sample_dict or sample_dict["age"] > 25  # [Line 15]

result = check_dict_conditions()                         # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_dict_conditions()' in it | FUNCTION CALL: Calls 'check_dict_conditions()' and stores its return value
print(f"Dictionary contains 'name' or age is greater than 25: {result}")  # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1283
Write a Python program to check if a string is empty or contains a number using the `or` operator.
"""

# ======================================================================
# PROBLEM 1283 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_string_empty_or_number():                      # [Line 13]
    text = "hello123"                                    # [Line 14]
    return len(text) == 0 or any(char.isdigit() for char in text)  # [Line 15] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

result = check_string_empty_or_number()                  # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_string_empty_or_number()' in it | FUNCTION CALL: Calls 'check_string_empty_or_number()' and stores its return value
print(f"String is empty or contains a number: {result}")  # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1284
Write a Python program to check if a number is either negative or divisible by 3 using the `or` operator.
"""

# ======================================================================
# PROBLEM 1284 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_negative_or_divisible_by_3():                  # [Line 13]
    num = -15                                            # [Line 14]
    return num < 0 or num % 3 == 0                       # [Line 15] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_negative_or_divisible_by_3()              # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_negative_or_divisible_by_3()' in it | FUNCTION CALL: Calls 'check_negative_or_divisible_by_3()' and stores its return value
print(f"Number is negative or divisible by 3: {result}")  # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1285
Write a Python program to check if a list is empty or contains more than 5 elements using the `or` operator.
"""

# ======================================================================
# PROBLEM 1285 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_list_conditions():                             # [Line 13]
    lst = [1, 2, 3]                                      # [Line 14]
    return len(lst) == 0 or len(lst) > 5                 # [Line 15] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

result = check_list_conditions()                         # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_list_conditions()' in it | FUNCTION CALL: Calls 'check_list_conditions()' and stores its return value
print(f"List is empty or contains more than 5 elements: {result}")  # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1286
Write a Python program to check if a number is a perfect square or a perfect cube using the `or` operator.
"""

# ======================================================================
# PROBLEM 1286 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import math                                              # [Line 13]

def check_perfect_square_or_cube():                      # [Line 15]
    num = 16                                             # [Line 16]
    return math.isqrt(num) ** 2 == num or round(num ** (1 / 3)) ** 3 == num  # [Line 17] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.

result = check_perfect_square_or_cube()                  # [Line 19] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_perfect_square_or_cube()' in it | FUNCTION CALL: Calls 'check_perfect_square_or_cube()' and stores its return value
print(f"Number is a perfect square or cube: {result}")   # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1287
Write a Python program to check if a string contains only letters or only digits using the `or` operator.
"""

# ======================================================================
# PROBLEM 1287 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_string_type():                                 # [Line 13]
    text = "1234"                                        # [Line 14]
    return text.isalpha() or text.isdigit()              # [Line 15]

result = check_string_type()                             # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_string_type()' in it | FUNCTION CALL: Calls 'check_string_type()' and stores its return value
print(f"String contains only letters or digits: {result}")  # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1288
Write a Python program to check if a list contains exactly 3 elements or its sum is greater than 50 using the `or` operator.
"""

# ======================================================================
# PROBLEM 1288 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_list_conditions():                             # [Line 13]
    lst = [6, 2, 8]                                      # [Line 14]
    return len(lst) == 3 or sum(lst) > 50                # [Line 15] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

result = check_list_conditions()                         # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_list_conditions()' in it | FUNCTION CALL: Calls 'check_list_conditions()' and stores its return value
print(f"List has exactly 3 elements or its sum is greater than 50: {result}")  # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1289
Write a Python program to check if a number is divisible by 2 or 5 using the `or` operator.
"""

# ======================================================================
# PROBLEM 1289 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_divisible_by_2_or_5():                         # [Line 13]
    num = 10                                             # [Line 14]
    return num % 2 == 0 or num % 5 == 0                  # [Line 15] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_divisible_by_2_or_5()                     # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_divisible_by_2_or_5()' in it | FUNCTION CALL: Calls 'check_divisible_by_2_or_5()' and stores its return value
print(f"Number is divisible by 2 or 5: {result}")        # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1290
Write a Python program to check if a file exists or if it is writable using the `or` operator.
"""

# ======================================================================
# PROBLEM 1290 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 13]

def check_file_conditions():                             # [Line 15]
    p = Path("example_file.txt")                         # [Line 16]
    return p.exists() or p.is_file()                     # [Line 17]

result = check_file_conditions()                         # [Line 19] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_file_conditions()' in it | FUNCTION CALL: Calls 'check_file_conditions()' and stores its return value
print(f"File exists or is a file: {result}")             # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1291
Write a Python program to check if a number is greater than 100 or less than 10 using the `or` operator.
"""

# ======================================================================
# PROBLEM 1291 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_number():                                      # [Line 13]
    num = 5                                              # [Line 14]
    return num > 100 or num < 10                         # [Line 15]

result = check_number()                                  # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_number()' in it | FUNCTION CALL: Calls 'check_number()' and stores its return value
print(f"Number is greater than 100 or less than 10: {result}")  # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1292
Write a Python program to check if a string is uppercase or its length is even using the `or` operator.
"""

# ======================================================================
# PROBLEM 1292 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_string_conditions():                           # [Line 13]
    text = "HELLO"                                       # [Line 14]
    return text.isupper() or len(text) % 2 == 0          # [Line 15] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_string_conditions()                       # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_string_conditions()' in it | FUNCTION CALL: Calls 'check_string_conditions()' and stores its return value
print(f"String is uppercase or its length is even: {result}")  # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1293
Write a Python program to check if a list is non-empty or its last element is greater than 10 using the `or` operator.
"""

# ======================================================================
# PROBLEM 1293 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_list_conditions():                             # [Line 13]
    lst = [6, 2, 8]                                      # [Line 14]
    return len(lst) > 0 or lst[-1] > 10                  # [Line 15]

result = check_list_conditions()                         # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_list_conditions()' in it | FUNCTION CALL: Calls 'check_list_conditions()' and stores its return value
print(f"List is non-empty or its last element is greater than 10: {result}")  # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1294
Write a Python program to check if a number is even or divisible by 3 using the `or` operator.
"""

# ======================================================================
# PROBLEM 1294 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_even_or_divisible_by_3():                      # [Line 13]
    num = 8                                              # [Line 14]
    return num % 2 == 0 or num % 3 == 0                  # [Line 15] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_even_or_divisible_by_3()                  # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_even_or_divisible_by_3()' in it | FUNCTION CALL: Calls 'check_even_or_divisible_by_3()' and stores its return value
print(f"Number is even or divisible by 3: {result}")     # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1295
Write a Python program to check if a string is not empty or contains the character 'a' using the `or` operator.
"""

# ======================================================================
# PROBLEM 1295 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_string():                                      # [Line 13]
    text = "apple"                                       # [Line 14]
    return len(text) > 0 or "a" in text                  # [Line 15]

result = check_string()                                  # [Line 17] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_string()' in it | FUNCTION CALL: Calls 'check_string()' and stores its return value
print(f"String is not empty or contains 'a': {result}")  # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

""" 
Problem: 1296
Write a Python program to extract all words starting with a capital letter.
"""

# ======================================================================
# PROBLEM 1296 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


s = "Hello World, this is Python."                       # [Line 13] | ASSIGNMENT: Creates variable 's' and stores the result of ''Hello World, this is Python.'' in it | DATA TYPE: String - A sequence of characters. Length: 28
words = re.findall(r"\b[A-Z][a-z]*\b", s)                # [Line 14] | ASSIGNMENT: Creates variable 'words' and stores the result of 're.findall('\\b[A-Z][a-z]*\\b', s)' in it | FUNCTION CALL: Calls 're.findall()' and stores its return value
print(words)                                             # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: ['Hello', 'World', 'Python']


""" 
Problem: 1297
Write a Python program to split a string by commas and optional whitespace.
"""

# ======================================================================
# PROBLEM 1297 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


s = "apple, banana ,cherry , grape"                      # [Line 13] | ASSIGNMENT: Creates variable 's' and stores the result of ''apple, banana ,cherry , grape'' in it | DATA TYPE: String - A sequence of characters. Length: 29
items = re.split(r"\s*,\s*", s)                          # [Line 14] | ASSIGNMENT: Creates variable 'items' and stores the result of 're.split('\\s*,\\s*', s)' in it | FUNCTION CALL: Calls 're.split()' and stores its return value
print(items)                                             # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: ['apple', 'banana', 'cherry', 'grape']


""" 
Problem: 1298
Write a Python program to check if a password contains at least one digit, one uppercase, and one lowercase letter.
"""

# ======================================================================
# PROBLEM 1298 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


password = "Password123"                                 # [Line 13] | ASSIGNMENT: Creates variable 'password' and stores the result of ''Password123'' in it | DATA TYPE: String - A sequence of characters. Length: 11
match = bool(re.search(r"[A-Z]", password) and re.search(r"[a-z]", password) and re.search(r"\d", password))  # [Line 14] | ASSIGNMENT: Creates variable 'match' and stores the result of 'bool(re.search('[A-Z]', password) and re.search('[a-z]', password) and re.search('\\d', password))' in it | FUNCTION CALL: Calls 'bool()' and stores its return value
print(match)                                             # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: True


""" 
Problem: 1299
Write a Python program to find all email addresses in a text.
"""

# ======================================================================
# PROBLEM 1299 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "Send to alice@example.com and bob99@domain.co.uk"  # [Line 13] | ASSIGNMENT: Creates variable 'text' and stores the result of ''Send to alice@example.com and bob99@domain.co.uk'' in it | DATA TYPE: String - A sequence of characters. Length: 48
emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)  # [Line 14] | ASSIGNMENT: Creates variable 'emails' and stores the result of 're.findall('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+', text)' in it | FUNCTION CALL: Calls 're.findall()' and stores its return value
print(emails)                                            # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: ['alice@example.com', 'bob99@domain.co.uk']


""" 
Problem: 1300
Write a Python program to extract hashtags from a tweet.
"""

# ======================================================================
# PROBLEM 1300 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


tweet = "Loving the                                      # [Line 13] | Python #coding journey!"
hashtags = re.findall(r"                                 # [Line 14] | \w+", tweet)
print(hashtags)                                          # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: ['#Python', '#coding']


""" 
Problem: 1301
Write a Python program to extract domain names from URLs.
"""

# ======================================================================
# PROBLEM 1301 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "Visit us at https://example.com or http://test.org"  # [Line 13] | FLOOR DIVISION (//) - Divides two numbers and returns the largest integer less than or equal to the result. Example: 7 // 2 = 3 (not 3.5). This is useful for integer division when you don't want decimal results. | ASSIGNMENT: Creates variable 'text' and stores the result of ''Visit us at https://example.com or http://test.org'' in it | DATA TYPE: String - A sequence of characters. Length: 50
domains = re.findall(r"https?://([\w.-]+)", text)        # [Line 14] | SLICING OPERATION - Extracts a portion of the sequence | FLOOR DIVISION (//) - Divides two numbers and returns the largest integer less than or equal to the result. Example: 7 // 2 = 3 (not 3.5). This is useful for integer division when you don't want decimal results. | ASSIGNMENT: Creates variable 'domains' and stores the result of 're.findall('https?://([\\w.-]+)', text)' in it | FUNCTION CALL: Calls 're.findall()' and stores its return value
print(domains)                                           # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: ['example.com', 'test.org']


""" 
Problem: 1302
Write a Python program to validate if a string is a valid IPv4 address.
"""

# ======================================================================
# PROBLEM 1302 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


ip = "192.168.1.1"                                       # [Line 13] | ASSIGNMENT: Creates variable 'ip' and stores the result of ''192.168.1.1'' in it | DATA TYPE: String - A sequence of characters. Length: 11
pattern = r"^(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(?!$)){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$"  # [Line 14] | ASSIGNMENT: Creates variable 'pattern' and stores the result of ''^(25[0-5]|2[0-4]\\d|1\\d\\d|[1-9]?\\d)(\\.(?!$)){3}(25[0-5]|2[0-4]\\d|1\\d\\d|[1-9]?\\d)$'' in it | DATA TYPE: String - A sequence of characters. Length: 80
match = bool(re.fullmatch(pattern, ip))                  # [Line 15] | ASSIGNMENT: Creates variable 'match' and stores the result of 'bool(re.fullmatch(pattern, ip))' in it | FUNCTION CALL: Calls 'bool()' and stores its return value
print(match)                                             # [Line 16] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: True


""" 
Problem: 1303
Write a Python program to remove all punctuation from a string.
"""

# ======================================================================
# PROBLEM 1303 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "Hello, world! Python is great."                  # [Line 13] | ASSIGNMENT: Creates variable 'text' and stores the result of ''Hello, world! Python is great.'' in it | DATA TYPE: String - A sequence of characters. Length: 30
clean = re.sub(r"[^\w\s]", "", text)                     # [Line 14] | ASSIGNMENT: Creates variable 'clean' and stores the result of 're.sub('[^\\w\\s]', '', text)' in it | FUNCTION CALL: Calls 're.sub()' and stores its return value
print(clean)                                             # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: Hello world Python is great


""" 
Problem: 1304
Write a Python program to match a string that starts with a vowel.
"""

# ======================================================================
# PROBLEM 1304 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


s = "apple"                                              # [Line 13] | ASSIGNMENT: Creates variable 's' and stores the result of ''apple'' in it | DATA TYPE: String - A sequence of characters. Length: 5
match = bool(re.match(r"^[aeiouAEIOU]", s))              # [Line 14] | ASSIGNMENT: Creates variable 'match' and stores the result of 'bool(re.match('^[aeiouAEIOU]', s))' in it | FUNCTION CALL: Calls 'bool()' and stores its return value
print(match)                                             # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: True


""" 
Problem: 1305
Write a Python program to extract all valid dates in the format YYYY-MM-DD.
"""

# ======================================================================
# PROBLEM 1305 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "Events: 2024-06-01, 2025-07-04, 99-01-01"        # [Line 13] | ASSIGNMENT: Creates variable 'text' and stores the result of ''Events: 2024-06-01, 2025-07-04, 99-01-01'' in it | DATA TYPE: String - A sequence of characters. Length: 40
dates = re.findall(r"\b\d{4}-\d{2}-\d{2}\b", text)       # [Line 14] | ASSIGNMENT: Creates variable 'dates' and stores the result of 're.findall('\\b\\d{4}-\\d{2}-\\d{2}\\b', text)' in it | FUNCTION CALL: Calls 're.findall()' and stores its return value
print(dates)                                             # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: ['2024-06-01', '2025-07-04']


""" 
Problem: 1306
Write a Python program to validate a hexadecimal color code.
"""

# ======================================================================
# PROBLEM 1306 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


color = "                                                # [Line 13] | 1a2b3c"
match = bool(re.fullmatch(r"                             # [Line 14] | ([A-Fa-f0-9]{6})", color))
print(match)                                             # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: True


""" 
Problem: 1307
Write a Python program to extract all words that end with 'ing'.
"""

# ======================================================================
# PROBLEM 1307 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "I am running and jumping while singing."         # [Line 13] | ASSIGNMENT: Creates variable 'text' and stores the result of ''I am running and jumping while singing.'' in it | DATA TYPE: String - A sequence of characters. Length: 39
words = re.findall(r"\b\w+ing\b", text)                  # [Line 14] | ASSIGNMENT: Creates variable 'words' and stores the result of 're.findall('\\b\\w+ing\\b', text)' in it | FUNCTION CALL: Calls 're.findall()' and stores its return value
print(words)                                             # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: ['running', 'jumping', 'singing']


""" 
Problem: 1308
Write a Python program to extract the file extension from a filename.
"""

# ======================================================================
# PROBLEM 1308 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


filename = "document.pdf"                                # [Line 13] | ASSIGNMENT: Creates variable 'filename' and stores the result of ''document.pdf'' in it | DATA TYPE: String - A sequence of characters. Length: 12
ext = re.search(r"\.(\w+)$", filename).group(1)          # [Line 14] | ASSIGNMENT: Creates variable 'ext' and stores the result of 're.search('\\.(\\w+)$', filename).group(1)' in it | FUNCTION CALL: Calls 're.search('\\.(\\w+)$', filename).group()' and stores its return value
print(ext)                                               # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: pdf


""" 
Problem: 1309
Write a Python program to find duplicated words in a sentence.
"""

# ======================================================================
# PROBLEM 1309 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "This is is a test test string"                   # [Line 13] | ASSIGNMENT: Creates variable 'text' and stores the result of ''This is is a test test string'' in it | DATA TYPE: String - A sequence of characters. Length: 29
duplicates = re.findall(r"\b(\w+)\s+\1\b", text)         # [Line 14] | ASSIGNMENT: Creates variable 'duplicates' and stores the result of 're.findall('\\b(\\w+)\\s+\\1\\b', text)' in it | FUNCTION CALL: Calls 're.findall()' and stores its return value
print(duplicates)                                        # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: ['is', 'test']

""" 
Problem: 1310
Write a Python program to extract all capitalized words from a paragraph.
"""

# ======================================================================
# PROBLEM 1310 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "Alice and Bob went to New York City on Monday."  # [Line 13] | ASSIGNMENT: Creates variable 'text' and stores the result of ''Alice and Bob went to New York City on Monday.'' in it | DATA TYPE: String - A sequence of characters. Length: 46
capitalized = re.findall(r"\b[A-Z][a-z]*\b", text)       # [Line 14] | ASSIGNMENT: Creates variable 'capitalized' and stores the result of 're.findall('\\b[A-Z][a-z]*\\b', text)' in it | FUNCTION CALL: Calls 're.findall()' and stores its return value
print(capitalized)                                       # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: ['Alice', 'Bob', 'New', 'York', 'City', 'Monday']


""" 
Problem: 1311
Write a Python program to validate a time in 24-hour format (HH:MM).
"""

# ======================================================================
# PROBLEM 1311 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


time = "23:59"                                           # [Line 13] | ASSIGNMENT: Creates variable 'time' and stores the result of ''23:59'' in it | DATA TYPE: String - A sequence of characters. Length: 5
match = bool(re.fullmatch(r"([01]\d|2[0-3]):[0-5]\d", time))  # [Line 14] | SLICING OPERATION - Extracts a portion of the sequence | ASSIGNMENT: Creates variable 'match' and stores the result of 'bool(re.fullmatch('([01]\\d|2[0-3]):[0-5]\\d', time))' in it | FUNCTION CALL: Calls 'bool()' and stores its return value
print(match)                                             # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1312
Write a Python program to extract all integers and floats from a string.
"""

# ======================================================================
# PROBLEM 1312 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "The temperature is 21.5C, and humidity is 60% with 0.25 inches rain."  # [Line 13] | OPERATION - Performs a calculation or comparison | ASSIGNMENT: Creates variable 'text' and stores the result of ''The temperature is 21.5C, and humidity is 60% with 0.25 inches rain.'' in it | DATA TYPE: String - A sequence of characters. Length: 68
numbers = re.findall(r"\d+\.\d+|\d+", text)              # [Line 14] | ASSIGNMENT: Creates variable 'numbers' and stores the result of 're.findall('\\d+\\.\\d+|\\d+', text)' in it | FUNCTION CALL: Calls 're.findall()' and stores its return value
print(numbers)                                           # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: ['21.5', '60', '0.25']


""" 
Problem: 1313
Write a Python program to remove leading zeros from an IP address.
"""

# ======================================================================
# PROBLEM 1313 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


ip = "192.168.001.001"                                   # [Line 13] | ASSIGNMENT: Creates variable 'ip' and stores the result of ''192.168.001.001'' in it | DATA TYPE: String - A sequence of characters. Length: 15
clean_ip = re.sub(r"\b0+(\d)", r"\1", ip)                # [Line 14] | ASSIGNMENT: Creates variable 'clean_ip' and stores the result of 're.sub('\\b0+(\\d)', '\\1', ip)' in it | FUNCTION CALL: Calls 're.sub()' and stores its return value
print(clean_ip)                                          # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 192.168.1.1


""" 
Problem: 1314
Write a Python program to check if a string is a valid slug (only lowercase letters, numbers, hyphens).
"""

# ======================================================================
# PROBLEM 1314 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


slug = "python-tips-101"                                 # [Line 13] | ASSIGNMENT: Creates variable 'slug' and stores the result of ''python-tips-101'' in it | DATA TYPE: String - A sequence of characters. Length: 15
match = bool(re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", slug))  # [Line 14] | ASSIGNMENT: Creates variable 'match' and stores the result of 'bool(re.fullmatch('[a-z0-9]+(-[a-z0-9]+)*', slug))' in it | FUNCTION CALL: Calls 'bool()' and stores its return value
print(match)                                             # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1315
Write a Python program to extract content inside parentheses.
"""

# ======================================================================
# PROBLEM 1315 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "This is a sample (with content) and (another one)."  # [Line 13] | ASSIGNMENT: Creates variable 'text' and stores the result of ''This is a sample (with content) and (another one).'' in it | DATA TYPE: String - A sequence of characters. Length: 50
content = re.findall(r"\((.*?)\)", text)                 # [Line 14] | ASSIGNMENT: Creates variable 'content' and stores the result of 're.findall('\\((.*?)\\)', text)' in it | FUNCTION CALL: Calls 're.findall()' and stores its return value
print(content)                                           # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: ['with content', 'another one']


""" 
Problem: 1316
Write a Python program to match all valid HTML tags in a string.
"""

# ======================================================================
# PROBLEM 1316 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


html = "<div><p>Hello</p></div>"                         # [Line 13] | ASSIGNMENT: Creates variable 'html' and stores the result of ''<div><p>Hello</p></div>'' in it | DATA TYPE: String - A sequence of characters. Length: 23
tags = re.findall(r"<[^>]+>", html)                      # [Line 14] | ASSIGNMENT: Creates variable 'tags' and stores the result of 're.findall('<[^>]+>', html)' in it | FUNCTION CALL: Calls 're.findall()' and stores its return value
print(tags)                                              # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: ['<div>', '<p>', '</p>', '</div>']


""" 
Problem: 1317
Write a Python program to validate if a string is a US ZIP code (5 digits).
"""

# ======================================================================
# PROBLEM 1317 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


zip_code = "12345"                                       # [Line 13] | ASSIGNMENT: Creates variable 'zip_code' and stores the result of ''12345'' in it | DATA TYPE: String - A sequence of characters. Length: 5
match = bool(re.fullmatch(r"\d{5}", zip_code))           # [Line 14] | ASSIGNMENT: Creates variable 'match' and stores the result of 'bool(re.fullmatch('\\d{5}', zip_code))' in it | FUNCTION CALL: Calls 'bool()' and stores its return value
print(match)                                             # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1318
Write a Python program to find all abbreviations like "U.S.A." in a string.
"""

# ======================================================================
# PROBLEM 1318 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "Some examples: U.S.A. and E.U."                  # [Line 13] | ASSIGNMENT: Creates variable 'text' and stores the result of ''Some examples: U.S.A. and E.U.'' in it | DATA TYPE: String - A sequence of characters. Length: 30
abbreviations = re.findall(r"(?:[A-Z]\.){2,}", text)     # [Line 14] | SLICING OPERATION - Extracts a portion of the sequence | ASSIGNMENT: Creates variable 'abbreviations' and stores the result of 're.findall('(?:[A-Z]\\.){2,}', text)' in it | FUNCTION CALL: Calls 're.findall()' and stores its return value
print(abbreviations)                                     # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: ['U.S.A.', 'E.U.']


""" 
Problem: 1319
Write a Python program to count how many times a word appears in a case-insensitive way.
"""

# ======================================================================
# PROBLEM 1319 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "Python is great. I love python because PYTHON is powerful."  # [Line 13] | ASSIGNMENT: Creates variable 'text' and stores the result of ''Python is great. I love python because PYTHON is powerful.'' in it | DATA TYPE: String - A sequence of characters. Length: 58
count = len(re.findall(r"\bpython\b", text, re.IGNORECASE))  # [Line 14] | ASSIGNMENT: Creates variable 'count' and stores the result of 'len(re.findall('\\bpython\\b', text, re.IGNORECASE))' in it | FUNCTION CALL: Calls 'len()' and stores its return value
print(count)                                             # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 3


""" 
Problem: 1320
Write a Python program to replace duplicate spaces with a single space.
"""

# ======================================================================
# PROBLEM 1320 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "This    is  a    spaced   sentence."             # [Line 13] | ASSIGNMENT: Creates variable 'text' and stores the result of ''This    is  a    spaced   sentence.'' in it | DATA TYPE: String - A sequence of characters. Length: 35
clean = re.sub(r"\s{2,}", " ", text)                     # [Line 14] | ASSIGNMENT: Creates variable 'clean' and stores the result of 're.sub('\\s{2,}', ' ', text)' in it | FUNCTION CALL: Calls 're.sub()' and stores its return value
print(clean)                                             # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: "This is a spaced sentence."


""" 
Problem: 1321
Write a Python program to validate a MAC address (e.g., 00:1A:2B:3C:4D:5E).
"""

# ======================================================================
# PROBLEM 1321 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


mac = "00:1A:2B:3C:4D:5E"                                # [Line 13] | ASSIGNMENT: Creates variable 'mac' and stores the result of ''00:1A:2B:3C:4D:5E'' in it | DATA TYPE: String - A sequence of characters. Length: 17
match = bool(re.fullmatch(r"([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}", mac))  # [Line 14] | SLICING OPERATION - Extracts a portion of the sequence | ASSIGNMENT: Creates variable 'match' and stores the result of 'bool(re.fullmatch('([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}', mac))' in it | FUNCTION CALL: Calls 'bool()' and stores its return value
print(match)                                             # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1322
Write a Python program to extract the username from an email address.
"""

# ======================================================================
# PROBLEM 1322 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


email = "john.doe@example.com"                           # [Line 13] | ASSIGNMENT: Creates variable 'email' and stores the result of ''john.doe@example.com'' in it | DATA TYPE: String - A sequence of characters. Length: 20
username = re.match(r"([^@]+)", email).group(1)          # [Line 14] | ASSIGNMENT: Creates variable 'username' and stores the result of 're.match('([^@]+)', email).group(1)' in it | FUNCTION CALL: Calls 're.match('([^@]+)', email).group()' and stores its return value
print(username)                                          # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: john.doe


""" 
Problem: 1323
Write a Python program to insert commas into a numeric string every three digits.
"""

# ======================================================================
# PROBLEM 1323 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


num = "1000000"                                          # [Line 13] | ASSIGNMENT: Creates variable 'num' and stores the result of ''1000000'' in it | DATA TYPE: String - A sequence of characters. Length: 7
formatted = re.sub(r"(?<=\d)(?=(\d{3})+$)", ",", num)    # [Line 14] | ASSIGNMENT: Creates variable 'formatted' and stores the result of 're.sub('(?<=\\d)(?=(\\d{3})+$)', ',', num)' in it | FUNCTION CALL: Calls 're.sub()' and stores its return value
print(formatted)                                         # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 1,000,000


""" 
Problem: 1324
Write a Python program to extract all valid Twitter handles from a string.
"""

# ======================================================================
# PROBLEM 1324 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "Follow @python, @realpython, and @openai!"       # [Line 13] | ASSIGNMENT: Creates variable 'text' and stores the result of ''Follow @python, @realpython, and @openai!'' in it | DATA TYPE: String - A sequence of characters. Length: 41
handles = re.findall(r"@\w+", text)                      # [Line 14] | ASSIGNMENT: Creates variable 'handles' and stores the result of 're.findall('@\\w+', text)' in it | FUNCTION CALL: Calls 're.findall()' and stores its return value
print(handles)                                           # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: ['@python', '@realpython', '@openai']


""" 
Problem: 1325
Write a Python program to check if a string contains any emoji.
"""

# ======================================================================
# PROBLEM 1325 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


emoji_text = "I love 🍕 and 🐍"                            # [Line 13] | ASSIGNMENT: Creates variable 'emoji_text' and stores the result of ''I love 🍕 and 🐍'' in it | DATA TYPE: String - A sequence of characters. Length: 14
match = bool(re.search(r"[\U0001F600-\U0001F64F]", emoji_text))  # [Line 14] | ASSIGNMENT: Creates variable 'match' and stores the result of 'bool(re.search('[\\U0001F600-\\U0001F64F]', emoji_text))' in it | FUNCTION CALL: Calls 'bool()' and stores its return value
print(match)                                             # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1326
Write a Python program to extract time values in 12-hour format with AM/PM.
"""

# ======================================================================
# PROBLEM 1326 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "Meeting at 02:30 PM and dinner at 07:45 AM."     # [Line 13] | ASSIGNMENT: Creates variable 'text' and stores the result of ''Meeting at 02:30 PM and dinner at 07:45 AM.'' in it | DATA TYPE: String - A sequence of characters. Length: 43
times = re.findall(r"\b\d{2}:\d{2} [AP]M\b", text)       # [Line 14] | SLICING OPERATION - Extracts a portion of the sequence | ASSIGNMENT: Creates variable 'times' and stores the result of 're.findall('\\b\\d{2}:\\d{2} [AP]M\\b', text)' in it | FUNCTION CALL: Calls 're.findall()' and stores its return value
print(times)                                             # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: ['02:30 PM', '07:45 AM']


""" 
Problem: 1327
Write a Python program to extract prices with a dollar sign.
"""

# ======================================================================
# PROBLEM 1327 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "Items: $20.99, $3.50, $100"                      # [Line 13] | ASSIGNMENT: Creates variable 'text' and stores the result of ''Items: $20.99, $3.50, $100'' in it | DATA TYPE: String - A sequence of characters. Length: 26
prices = re.findall(r"\$\d+(\.\d{2})?", text)            # [Line 14] | ASSIGNMENT: Creates variable 'prices' and stores the result of 're.findall('\\$\\d+(\\.\\d{2})?', text)' in it | FUNCTION CALL: Calls 're.findall()' and stores its return value
print(prices)                                            # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: ['$20.99', '$3.50', '$100']


""" 
Problem: 1328
Write a Python program to detect duplicate characters in a string using regex.
"""

# ======================================================================
# PROBLEM 1328 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


s = "programming"                                        # [Line 13] | ASSIGNMENT: Creates variable 's' and stores the result of ''programming'' in it | DATA TYPE: String - A sequence of characters. Length: 11
duplicates = re.findall(r"(\w)(?=.*\1)", s)              # [Line 14] | ASSIGNMENT: Creates variable 'duplicates' and stores the result of 're.findall('(\\w)(?=.*\\1)', s)' in it | FUNCTION CALL: Calls 're.findall()' and stores its return value
print(set(duplicates))                                   # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {'r', 'g', 'm'}


""" 
Problem: 1329
Write a Python program to validate a hexadecimal number (e.g., 0x1A3F).
"""

# ======================================================================
# PROBLEM 1329 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


hex_num = "0x1A3F"                                       # [Line 13] | ASSIGNMENT: Creates variable 'hex_num' and stores the result of ''0x1A3F'' in it | DATA TYPE: String - A sequence of characters. Length: 6
match = bool(re.fullmatch(r"0x[0-9A-Fa-f]+", hex_num))   # [Line 14] | ASSIGNMENT: Creates variable 'match' and stores the result of 'bool(re.fullmatch('0x[0-9A-Fa-f]+', hex_num))' in it | FUNCTION CALL: Calls 'bool()' and stores its return value
print(match)                                             # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1330
Write a Python program to extract quoted strings (single or double quotes).
"""

# ======================================================================
# PROBLEM 1330 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

import re                                                # [Line 12]

text = "'Hello', she said. \"How are you?\""             # [Line 14] | ASSIGNMENT: Creates variable 'text' and stores the result of ''\'Hello\', she said. "How are you?"'' in it | DATA TYPE: String - A sequence of characters. Length: 33
quotes = re.findall(r"(['\"])(.*?)\1", text)             # [Line 15] | ASSIGNMENT: Creates variable 'quotes' and stores the result of 're.findall('([\'\\"])(.*?)\\1', text)' in it | FUNCTION CALL: Calls 're.findall()' and stores its return value
print([q[1] for q in quotes])                            # [Line 16] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: ['Hello', 'How are you?']


""" 
Problem: 1331
Write a Python program to check if a variable is an integer using isinstance().
"""

# ======================================================================
# PROBLEM 1331 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


x = 10                                                   # [Line 13] | ASSIGNMENT: Creates variable 'x' and stores the result of '10' in it | DATA TYPE: Integer - A whole number: 10
print(isinstance(x, int))                                # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1332
Write a Python program to check if a variable is a string using isinstance().
"""

# ======================================================================
# PROBLEM 1332 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


x = "hello"                                              # [Line 13] | ASSIGNMENT: Creates variable 'x' and stores the result of ''hello'' in it | DATA TYPE: String - A sequence of characters. Length: 5
print(isinstance(x, str))                                # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1333
Write a Python program to check if a variable is a float using isinstance().
"""

# ======================================================================
# PROBLEM 1333 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


x = 3.14                                                 # [Line 13] | ASSIGNMENT: Creates variable 'x' and stores the result of '3.14' in it
print(isinstance(x, float))                              # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1334
Write a Python program to check if a variable is a list using isinstance().
"""

# ======================================================================
# PROBLEM 1334 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


x = [1, 2, 3]                                            # [Line 13] | ASSIGNMENT: Creates variable 'x' and stores the result of '[1, 2, 3]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(isinstance(x, list))                               # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1335
Write a Python program to check if a variable is a dictionary using isinstance().
"""

# ======================================================================
# PROBLEM 1335 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


x = {"a": 1}                                             # [Line 13] | ASSIGNMENT: Creates variable 'x' and stores the result of '{'a': 1}' in it
print(isinstance(x, dict))                               # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1336
Write a Python program to check if a variable is either int or float using isinstance().
"""

# ======================================================================
# PROBLEM 1336 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


x = 10.0                                                 # [Line 13] | ASSIGNMENT: Creates variable 'x' and stores the result of '10.0' in it
print(isinstance(x, (int, float)))                       # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1337
Write a Python program to check if each element in a list is a string.
"""

# ======================================================================
# PROBLEM 1337 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


lst = ["apple", "banana", "cherry"]                      # [Line 13] | ASSIGNMENT: Creates variable 'lst' and stores the result of '['apple', 'banana', 'cherry']' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
result = all(isinstance(item, str) for item in lst)      # [Line 14] | ASSIGNMENT: Creates variable 'result' and stores the result of 'all((isinstance(item, str) for item in lst))' in it | FUNCTION CALL: Calls 'all()' and stores its return value
print(result)                                            # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1338
Write a Python program to filter only integers from a mixed list using isinstance().
"""

# ======================================================================
# PROBLEM 1338 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


items = [1, "a", 3.5, 4, "b"]                            # [Line 13] | ASSIGNMENT: Creates variable 'items' and stores the result of '[1, 'a', 3.5, 4, 'b']' in it | DATA TYPE: List - A mutable ordered collection. Contains 5 elements
ints = [x for x in items if isinstance(x, int)]          # [Line 14] | ASSIGNMENT: Creates variable 'ints' and stores the result of '[x for x in items if isinstance(x, int)]' in it
print(ints)                                              # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [1, 4]


""" 
Problem: 1339
Write a Python program to filter only strings from a mixed list using isinstance().
"""

# ======================================================================
# PROBLEM 1339 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


items = [1, "apple", 2.5, "banana"]                      # [Line 13] | ASSIGNMENT: Creates variable 'items' and stores the result of '[1, 'apple', 2.5, 'banana']' in it | DATA TYPE: List - A mutable ordered collection. Contains 4 elements
strings = [x for x in items if isinstance(x, str)]       # [Line 14] | ASSIGNMENT: Creates variable 'strings' and stores the result of '[x for x in items if isinstance(x, str)]' in it
print(strings)                                           # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: ['apple', 'banana']


""" 
Problem: 1340
Write a Python program to check if an object is a boolean using isinstance().
"""

# ======================================================================
# PROBLEM 1340 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


x = True                                                 # [Line 13] | ASSIGNMENT: Creates variable 'x' and stores the result of 'True' in it | DATA TYPE: Integer - A whole number: True
print(isinstance(x, bool))                               # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1341
Write a Python program to check if a variable is a tuple using isinstance().
"""

# ======================================================================
# PROBLEM 1341 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


x = (1, 2, 3)                                            # [Line 13] | ASSIGNMENT: Creates variable 'x' and stores the result of '(1, 2, 3)' in it | DATA TYPE: Tuple - An immutable ordered collection. Contains 3 elements
print(isinstance(x, tuple))                              # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1342
Write a Python program to check if an object is not a string using isinstance().
"""

# ======================================================================
# PROBLEM 1342 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


x = 42                                                   # [Line 13] | ASSIGNMENT: Creates variable 'x' and stores the result of '42' in it | DATA TYPE: Integer - A whole number: 42
print(not isinstance(x, str))                            # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1343
Write a Python program to define a function that accepts only strings using isinstance().
"""

# ======================================================================
# PROBLEM 1343 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def greet(name):                                         # [Line 13]
    if not isinstance(name, str):                        # [Line 14]
        return "Invalid input"                           # [Line 15]
    return f"Hello, {name}!"                             # [Line 16]

print(greet("Alice"))                                    # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: Hello, Alice!
print(greet(123))                                        # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: Invalid input


""" 
Problem: 1344
Write a Python program to check if all elements in a nested list are lists.
"""

# ======================================================================
# PROBLEM 1344 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


nested = [[1, 2], [3, 4]]                                # [Line 13] | ASSIGNMENT: Creates variable 'nested' and stores the result of '[[1, 2], [3, 4]]' in it | DATA TYPE: List - A mutable ordered collection. Contains 2 elements
result = all(isinstance(sub, list) for sub in nested)    # [Line 14] | ASSIGNMENT: Creates variable 'result' and stores the result of 'all((isinstance(sub, list) for sub in nested))' in it | FUNCTION CALL: Calls 'all()' and stores its return value
print(result)                                            # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1345
Write a Python program to separate strings and numbers from a list.
"""

# ======================================================================
# PROBLEM 1345 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


mixed = [1, "one", 2, "two", 3, "three"]                 # [Line 13] | ASSIGNMENT: Creates variable 'mixed' and stores the result of '[1, 'one', 2, 'two', 3, 'three']' in it | DATA TYPE: List - A mutable ordered collection. Contains 6 elements
nums = [x for x in mixed if isinstance(x, int)]          # [Line 14] | ASSIGNMENT: Creates variable 'nums' and stores the result of '[x for x in mixed if isinstance(x, int)]' in it
words = [x for x in mixed if isinstance(x, str)]         # [Line 15] | ASSIGNMENT: Creates variable 'words' and stores the result of '[x for x in mixed if isinstance(x, str)]' in it
print(nums)                                              # [Line 16] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [1, 2, 3]
print(words)                                             # [Line 17] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: ['one', 'two', 'three']


""" 
Problem: 1346
Write a Python program to validate argument types in a function.
"""

# ======================================================================
# PROBLEM 1346 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def multiply(a, b):                                      # [Line 13]
    if not all(isinstance(x, (int, float)) for x in (a, b)):  # [Line 14]
        return "Invalid input"                           # [Line 15]
    return a * b                                         # [Line 16]

print(multiply(2, 3))                                    # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 6
print(multiply(2, "x"))                                  # [Line 19] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: Invalid input


""" 
Problem: 1347
Write a Python program to check if a variable is a set using isinstance().
"""

# ======================================================================
# PROBLEM 1347 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


x = {1, 2, 3}                                            # [Line 13] | ASSIGNMENT: Creates variable 'x' and stores the result of '{1, 2, 3}' in it
print(isinstance(x, set))                                # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1348
Write a Python program to validate that dictionary keys are all strings.
"""

# ======================================================================
# PROBLEM 1348 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


d = {"a": 1, "b": 2}                                     # [Line 13] | ASSIGNMENT: Creates variable 'd' and stores the result of '{'a': 1, 'b': 2}' in it
result = all(isinstance(k, str) for k in d.keys())       # [Line 14] | ASSIGNMENT: Creates variable 'result' and stores the result of 'all((isinstance(k, str) for k in d.keys()))' in it | FUNCTION CALL: Calls 'all()' and stores its return value
print(result)                                            # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1349
Write a Python program to validate that dictionary values are all integers.
"""

# ======================================================================
# PROBLEM 1349 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


d = {"x": 1, "y": 2}                                     # [Line 13] | ASSIGNMENT: Creates variable 'd' and stores the result of '{'x': 1, 'y': 2}' in it
result = all(isinstance(v, int) for v in d.values())     # [Line 14] | ASSIGNMENT: Creates variable 'result' and stores the result of 'all((isinstance(v, int) for v in d.values()))' in it | FUNCTION CALL: Calls 'all()' and stores its return value
print(result)                                            # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1350
Write a Python program to check if an object is a file-like object (has read method).
"""

# ======================================================================
# PROBLEM 1350 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


class FakeFile:                                          # [Line 13]
    def read(self):                                      # [Line 14]
        pass                                             # [Line 15]

f = FakeFile()                                           # [Line 17] | ASSIGNMENT: Creates variable 'f' and stores the result of 'FakeFile()' in it | FUNCTION CALL: Calls 'FakeFile()' and stores its return value
print(hasattr(f, "read") and callable(f.read))           # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True

""" 
Problem: 1351
Write a Python program to remove a key from a dictionary using pop() and print the updated dictionary.
"""

# ======================================================================
# PROBLEM 1351 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

d = {"a": 1, "b": 2, "c": 3}                             # [Line 12] | ASSIGNMENT: Creates variable 'd' and stores the result of '{'a': 1, 'b': 2, 'c': 3}' in it
d.pop("b")                                               # [Line 13] | FUNCTION CALL: Executes the function 'd.pop' | ARGUMENTS: Passes 1 argument(s) to the function
print(d)                                                 # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {'a': 1, 'c': 3}


""" 
Problem: 1352
Write a Python program to use pop() to retrieve the value of a key from a dictionary.
"""

# ======================================================================
# PROBLEM 1352 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

d = {"a": 10, "b": 20}                                   # [Line 12] | ASSIGNMENT: Creates variable 'd' and stores the result of '{'a': 10, 'b': 20}' in it
value = d.pop("a")                                       # [Line 13] | ASSIGNMENT: Creates variable 'value' and stores the result of 'd.pop('a')' in it | FUNCTION CALL: Calls 'd.pop()' and stores its return value
print(value)                                             # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 10


""" 
Problem: 1353
Write a Python program to use pop() on a list to remove the last item.
"""

# ======================================================================
# PROBLEM 1353 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = [1, 2, 3, 4]                                       # [Line 12] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[1, 2, 3, 4]' in it | DATA TYPE: List - A mutable ordered collection. Contains 4 elements
lst.pop()                                                # [Line 13] | FUNCTION CALL: Executes the function 'lst.pop'
print(lst)                                               # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [1, 2, 3]


""" 
Problem: 1354
Write a Python program to remove a specific index from a list using pop().
"""

# ======================================================================
# PROBLEM 1354 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = [10, 20, 30, 40]                                   # [Line 12] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[10, 20, 30, 40]' in it | DATA TYPE: List - A mutable ordered collection. Contains 4 elements
lst.pop(1)                                               # [Line 13] | FUNCTION CALL: Executes the function 'lst.pop' | ARGUMENTS: Passes 1 argument(s) to the function
print(lst)                                               # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [10, 30, 40]


""" 
Problem: 1355
Write a Python program to capture and print the element removed using pop() from a list.
"""

# ======================================================================
# PROBLEM 1355 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = [5, 6, 7]                                          # [Line 12] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[5, 6, 7]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
removed = lst.pop()                                      # [Line 13] | ASSIGNMENT: Creates variable 'removed' and stores the result of 'lst.pop()' in it | FUNCTION CALL: Calls 'lst.pop()' and stores its return value
print(removed)                                           # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 7


""" 
Problem: 1356
Write a Python program to remove all elements from a list using pop() in a loop.
"""

# ======================================================================
# PROBLEM 1356 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = [1, 2, 3]                                          # [Line 12] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[1, 2, 3]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
while lst:                                               # [Line 13]
    print(lst.pop())                                     # [Line 14] | Expected: 3, 2, 1 (on separate lines)


""" 
Problem: 1357
Write a Python program to handle IndexError when popping from an empty list.
"""

# ======================================================================
# PROBLEM 1357 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = []                                                 # [Line 12] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[]' in it | DATA TYPE: List - A mutable ordered collection. Contains 0 elements
try:                                                     # [Line 13]
    lst.pop()                                            # [Line 14]
except IndexError:                                       # [Line 15]
    print("List is empty")                               # [Line 16] | Expected: "List is empty"


""" 
Problem: 1358
Write a Python program to use pop() with dictionaries and provide a default return value if the key doesn't exist.
"""

# ======================================================================
# PROBLEM 1358 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

d = {"x": 5}                                             # [Line 12] | ASSIGNMENT: Creates variable 'd' and stores the result of '{'x': 5}' in it
val = d.pop("y", "Not Found")                            # [Line 13] | ASSIGNMENT: Creates variable 'val' and stores the result of 'd.pop('y', 'Not Found')' in it | FUNCTION CALL: Calls 'd.pop()' and stores its return value
print(val)                                               # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: "Not Found"


""" 
Problem: 1359
Write a Python program to safely remove a key from a dictionary using pop() inside a try block.
"""

# ======================================================================
# PROBLEM 1359 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

d = {"a": 100}                                           # [Line 12] | ASSIGNMENT: Creates variable 'd' and stores the result of '{'a': 100}' in it
try:                                                     # [Line 13]
    print(d.pop("b"))                                    # [Line 14]
except KeyError:                                         # [Line 15]
    print("Key not found")                               # [Line 16] | Expected: "Key not found"


""" 
Problem: 1360
Write a Python program to remove keys one by one using pop() until the dictionary is empty.
"""

# ======================================================================
# PROBLEM 1360 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

d = {"k1": 1, "k2": 2}                                   # [Line 12] | ASSIGNMENT: Creates variable 'd' and stores the result of '{'k1': 1, 'k2': 2}' in it
while d:                                                 # [Line 13]
    print(d.popitem())                                   # [Line 14] | Expected: tuple key-value pairs


""" 
Problem: 1361
Write a Python program to pop elements from a stack represented by a list.
"""

# ======================================================================
# PROBLEM 1361 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

stack = [1, 2, 3]                                        # [Line 12] | ASSIGNMENT: Creates variable 'stack' and stores the result of '[1, 2, 3]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(stack.pop())                                       # [Line 13] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 3


""" 
Problem: 1362
Write a Python program to simulate queue dequeue using pop(0).
"""

# ======================================================================
# PROBLEM 1362 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

queue = [10, 20, 30]                                     # [Line 12] | ASSIGNMENT: Creates variable 'queue' and stores the result of '[10, 20, 30]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(queue.pop(0))                                      # [Line 13] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 10


""" 
Problem: 1363
Write a Python program to remove the last element from a list using pop() and store it.
"""

# ======================================================================
# PROBLEM 1363 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

numbers = [4, 5, 6]                                      # [Line 12] | ASSIGNMENT: Creates variable 'numbers' and stores the result of '[4, 5, 6]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
last = numbers.pop()                                     # [Line 13] | ASSIGNMENT: Creates variable 'last' and stores the result of 'numbers.pop()' in it | FUNCTION CALL: Calls 'numbers.pop()' and stores its return value
print(last)                                              # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 6


""" 
Problem: 1364
Write a Python program to demonstrate the use of pop() on a string key in a dictionary.
"""

# ======================================================================
# PROBLEM 1364 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

d = {"name": "Alice", "age": 30}                         # [Line 12] | ASSIGNMENT: Creates variable 'd' and stores the result of '{'name': 'Alice', 'age': 30}' in it
print(d.pop("name"))                                     # [Line 13] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: "Alice"


""" 
Problem: 1365
Write a Python program to pop multiple elements from the end of a list using a loop.
"""

# ======================================================================
# PROBLEM 1365 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = [1, 2, 3, 4, 5]                                    # [Line 12] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[1, 2, 3, 4, 5]' in it | DATA TYPE: List - A mutable ordered collection. Contains 5 elements
for _ in range(3):                                       # [Line 13]
    lst.pop()                                            # [Line 14]
print(lst)                                               # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [1, 2]


""" 
Problem: 1366
Write a Python program to pop and sum the last two numbers from a list.
"""

# ======================================================================
# PROBLEM 1366 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = [100, 200, 300]                                    # [Line 12] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[100, 200, 300]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
sum_last_two = lst.pop() + lst.pop()                     # [Line 13] | ASSIGNMENT: Creates variable 'sum_last_two' and stores the result of 'lst.pop() + lst.pop()' in it | BINARY OPERATION: Performs a calculation between two operands
print(sum_last_two)                                      # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 500


""" 
Problem: 1367
Write a Python program to use pop() in a function that removes a key from a given dictionary.
"""

# ======================================================================
# PROBLEM 1367 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def remove_key(d, key):                                  # [Line 12]
    return d.pop(key, None)                              # [Line 13]

print(remove_key({"a": 1, "b": 2}, "a"))                 # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 1


""" 
Problem: 1368
Write a Python program to pop an element from a list and append it to another list.
"""

# ======================================================================
# PROBLEM 1368 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

src = [9, 8, 7]                                          # [Line 12] | ASSIGNMENT: Creates variable 'src' and stores the result of '[9, 8, 7]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
dst = []                                                 # [Line 13] | ASSIGNMENT: Creates variable 'dst' and stores the result of '[]' in it | DATA TYPE: List - A mutable ordered collection. Contains 0 elements
dst.append(src.pop())                                    # [Line 14] | FUNCTION CALL: Executes the function 'dst.append' | ARGUMENTS: Passes 1 argument(s) to the function
print(dst)                                               # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [7]


""" 
Problem: 1369
Write a Python program to implement a basic undo feature using pop() on a list of actions.
"""

# ======================================================================
# PROBLEM 1369 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

actions = ["type", "edit", "save"]                       # [Line 12] | ASSIGNMENT: Creates variable 'actions' and stores the result of '['type', 'edit', 'save']' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
undo = actions.pop()                                     # [Line 13] | ASSIGNMENT: Creates variable 'undo' and stores the result of 'actions.pop()' in it | FUNCTION CALL: Calls 'actions.pop()' and stores its return value
print(undo)                                              # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: "save"


""" 
Problem: 1370
Write a Python program to pop elements from a nested list.
"""

# ======================================================================
# PROBLEM 1370 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

nested = [[1, 2], [3, 4], [5, 6]]                        # [Line 12] | ASSIGNMENT: Creates variable 'nested' and stores the result of '[[1, 2], [3, 4], [5, 6]]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
last_sublist = nested.pop()                              # [Line 13] | ASSIGNMENT: Creates variable 'last_sublist' and stores the result of 'nested.pop()' in it | FUNCTION CALL: Calls 'nested.pop()' and stores its return value
print(last_sublist)                                      # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [5, 6]

""" 
Problem: 1371  
Write a Python program with a function that accepts arbitrary keyword arguments and prints them.
"""

# ======================================================================
# PROBLEM 1371 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def print_kwargs(**kwargs):                              # [Line 12] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    print(kwargs)                                        # [Line 13]

print_kwargs(a=1, b=2)                                   # [Line 15] | FUNCTION CALL: Executes the function 'print_kwargs' | Expected: {'a': 1, 'b': 2}


""" 
Problem: 1372  
Write a Python function that prints each key-value pair in **kwargs on a separate line.
"""

# ======================================================================
# PROBLEM 1372 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def display_kwargs(**kwargs):                            # [Line 12] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    for key, value in kwargs.items():                    # [Line 13]
        print(f"{key}: {value}")                         # [Line 14]

display_kwargs(name="Alice", age=30)                     # [Line 16] | FUNCTION CALL: Executes the function 'display_kwargs'
# Expected:
# name: Alice
# age: 30


""" 
Problem: 1373  
Write a Python program to count the number of keyword arguments passed to a function.
"""

# ======================================================================
# PROBLEM 1373 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def count_kwargs(**kwargs):                              # [Line 12] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    print(len(kwargs))                                   # [Line 13]

count_kwargs(a=1, b=2, c=3)                              # [Line 15] | FUNCTION CALL: Executes the function 'count_kwargs' | Expected: 3


""" 
Problem: 1374  
Write a Python function that returns the keys of **kwargs as a list.
"""

# ======================================================================
# PROBLEM 1374 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def kwargs_keys(**kwargs):                               # [Line 12] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    return list(kwargs.keys())                           # [Line 13]

print(kwargs_keys(x=10, y=20))                           # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: ['x', 'y']


""" 
Problem: 1375  
Write a Python function that returns the values of **kwargs as a list.
"""

# ======================================================================
# PROBLEM 1375 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def kwargs_values(**kwargs):                             # [Line 12] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    return list(kwargs.values())                         # [Line 13]

print(kwargs_values(x=10, y=20))                         # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [10, 20]


""" 
Problem: 1376  
Write a Python function that returns True if 'id' is in **kwargs.
"""

# ======================================================================
# PROBLEM 1376 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def has_id(**kwargs):                                    # [Line 12] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    return 'id' in kwargs                                # [Line 13]

print(has_id(name="A", id=123))                          # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1377  
Write a Python function that returns the value of a keyword argument 'name' if it exists, else return 'Unknown'.
"""

# ======================================================================
# PROBLEM 1377 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def get_name(**kwargs):                                  # [Line 12] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    return kwargs.get('name', 'Unknown')                 # [Line 13]

print(get_name(age=22))                                  # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: "Unknown"


""" 
Problem: 1378  
Write a Python function that sums all numeric values in **kwargs.
"""

# ======================================================================
# PROBLEM 1378 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def sum_kwargs(**kwargs):                                # [Line 12] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    return sum(v for v in kwargs.values() if isinstance(v, (int, float)))  # [Line 13]

print(sum_kwargs(a=10, b=5.5, c="x"))                    # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 15.5


""" 
Problem: 1379  
Write a Python function that filters and returns keyword arguments where values are strings.
"""

# ======================================================================
# PROBLEM 1379 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def string_kwargs(**kwargs):                             # [Line 12] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    return {k: v for k, v in kwargs.items() if isinstance(v, str)}  # [Line 13]

print(string_kwargs(a="hi", b=2, c="hello"))             # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {'a': 'hi', 'c': 'hello'}


""" 
Problem: 1380  
Write a Python function that prints a formatted string from **kwargs using name and age keys.
"""

# ======================================================================
# PROBLEM 1380 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def greet(**kwargs):                                     # [Line 12] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    print(f"Hello {kwargs.get('name', 'Guest')}, age {kwargs.get('age', 'N/A')}")  # [Line 13]

greet(name="Bob", age=40)                                # [Line 15] | FUNCTION CALL: Executes the function 'greet' | Expected: Hello Bob, age 40


""" 
Problem: 1381  
Write a Python function that updates a dictionary with keyword arguments.
"""

# ======================================================================
# PROBLEM 1381 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def update_dict(base, **kwargs):                         # [Line 12] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    base.update(kwargs)                                  # [Line 13]
    return base                                          # [Line 14]

print(update_dict({'x': 1}, y=2, z=3))                   # [Line 16] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {'x': 1, 'y': 2, 'z': 3}


""" 
Problem: 1382  
Write a Python function that merges two dictionaries using **kwargs.
"""

# ======================================================================
# PROBLEM 1382 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def merge_dicts(d1, **kwargs):                           # [Line 12] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    merged = d1.copy()                                   # [Line 13]
    merged.update(kwargs)                                # [Line 14]
    return merged                                        # [Line 15]

print(merge_dicts({'a': 1}, b=2))                        # [Line 17] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {'a': 1, 'b': 2}


""" 
Problem: 1383  
Write a Python function that prints only the keyword arguments with even integer values.
"""

# ======================================================================
# PROBLEM 1383 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def even_kwargs(**kwargs):                               # [Line 12] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    for k, v in kwargs.items():                          # [Line 13]
        if isinstance(v, int) and v % 2 == 0:            # [Line 14] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
            print(f"{k}: {v}")                           # [Line 15]

even_kwargs(a=1, b=2, c=4)                               # [Line 17] | FUNCTION CALL: Executes the function 'even_kwargs'
# Expected:
# b: 2
# c: 4


""" 
Problem: 1384  
Write a Python function that accepts any number of keyword arguments and prints them sorted by key.
"""

# ======================================================================
# PROBLEM 1384 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def sorted_kwargs(**kwargs):                             # [Line 12] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    for k in sorted(kwargs.keys()):                      # [Line 13]
        print(f"{k}: {kwargs[k]}")                       # [Line 14] | SLICING OPERATION - Extracts a portion of the sequence

sorted_kwargs(z=9, a=1, m=5)                             # [Line 16] | FUNCTION CALL: Executes the function 'sorted_kwargs'
# Expected:
# a: 1
# m: 5
# z: 9


""" 
Problem: 1385  
Write a Python function that prints the number of string values in **kwargs.
"""

# ======================================================================
# PROBLEM 1385 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def count_strings(**kwargs):                             # [Line 12] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    print(sum(1 for v in kwargs.values() if isinstance(v, str)))  # [Line 13]

count_strings(a="one", b=2, c="three")                   # [Line 15] | FUNCTION CALL: Executes the function 'count_strings' | Expected: 2


""" 
Problem: 1386  
Write a Python function that prints whether each value in **kwargs is truthy or falsy.
"""

# ======================================================================
# PROBLEM 1386 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def check_truthy(**kwargs):                              # [Line 12] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    for k, v in kwargs.items():                          # [Line 13]
        print(f"{k}: {'Truthy' if v else 'Falsy'}")      # [Line 14]

check_truthy(a=0, b="hello", c=[])                       # [Line 16] | FUNCTION CALL: Executes the function 'check_truthy'
# Expected:
# a: Falsy
# b: Truthy
# c: Falsy


""" 
Problem: 1387  
Write a Python function that prints all key-value pairs in **kwargs where the key starts with 'a'.
"""

# ======================================================================
# PROBLEM 1387 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def starts_with_a(**kwargs):                             # [Line 12] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    for k, v in kwargs.items():                          # [Line 13]
        if k.startswith('a'):                            # [Line 14]
            print(f"{k}: {v}")                           # [Line 15]

starts_with_a(apple=1, banana=2, ant=3)                  # [Line 17] | FUNCTION CALL: Executes the function 'starts_with_a'
# Expected:
# apple: 1
# ant: 3


""" 
Problem: 1388  
Write a Python function that returns a reversed dictionary built from **kwargs.
"""

# ======================================================================
# PROBLEM 1388 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def reverse_kwargs(**kwargs):                            # [Line 12] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    return {v: k for k, v in kwargs.items()}             # [Line 13]

print(reverse_kwargs(a=1, b=2))                          # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {1: 'a', 2: 'b'}


""" 
Problem: 1389  
Write a Python function that returns the longest key in **kwargs.
"""

# ======================================================================
# PROBLEM 1389 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def longest_key(**kwargs):                               # [Line 12] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    return max(kwargs, key=len)                          # [Line 13]

print(longest_key(short=1, muchlonger=2))                # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 'muchlonger'


""" 
Problem: 1390  
Write a Python function that creates a string from **kwargs as key=value pairs joined by commas.
"""

# ======================================================================
# PROBLEM 1390 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def stringify_kwargs(**kwargs):                          # [Line 12] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    return ', '.join(f"{k}={v}" for k, v in kwargs.items())  # [Line 13]

print(stringify_kwargs(x=10, y=20))                      # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: "x=10, y=20"


""" 
Problem: 1391  
Write a Python function that checks if all values in **kwargs are integers.
"""

# ======================================================================
# PROBLEM 1391 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def all_ints(**kwargs):                                  # [Line 12] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    return all(isinstance(v, int) for v in kwargs.values())  # [Line 13]

print(all_ints(a=1, b=2))                                # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1392  
Write a Python function that finds and returns the maximum numeric value in **kwargs.
"""

# ======================================================================
# PROBLEM 1392 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def max_numeric(**kwargs):                               # [Line 12] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    nums = [v for v in kwargs.values() if isinstance(v, (int, float))]  # [Line 13]
    return max(nums) if nums else None                   # [Line 14]

print(max_numeric(a=1, b=3.5, c="x"))                    # [Line 16] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 3.5


""" 
Problem: 1393  
Write a Python function that counts the keyword arguments whose value is None.
"""

# ======================================================================
# PROBLEM 1393 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def count_none(**kwargs):                                # [Line 12] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    return sum(1 for v in kwargs.values() if v is None)  # [Line 13]

print(count_none(a=None, b=1, c=None))                   # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 2


""" 
Problem: 1394  
Write a Python function that prints the types of values in **kwargs.
"""

# ======================================================================
# PROBLEM 1394 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def print_types(**kwargs):                               # [Line 12] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    for k, v in kwargs.items():                          # [Line 13]
        print(f"{k}: {type(v).__name__}")                # [Line 14]

print_types(a=1, b="str", c=3.14)                        # [Line 16] | FUNCTION CALL: Executes the function 'print_types'
# Expected:
# a: int
# b: str
# c: float


""" 
Problem: 1395  
Write a Python function that creates a list of key-value pairs (tuples) from **kwargs.
"""

# ======================================================================
# PROBLEM 1395 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def kv_pairs(**kwargs):                                  # [Line 12] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    return list(kwargs.items())                          # [Line 13]

print(kv_pairs(a=1, b=2))                                # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [('a', 1), ('b', 2)]


""" 
Problem: 1396  
Write a Python function that filters out keyword arguments with falsy values.
"""

# ======================================================================
# PROBLEM 1396 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def remove_falsy(**kwargs):                              # [Line 12] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    return {k: v for k, v in kwargs.items() if v}        # [Line 13]

print(remove_falsy(a=0, b=1, c=""))                      # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {'b': 1}


""" 
Problem: 1397  
Write a Python function that returns True if at least one value in **kwargs is a list.
"""

# ======================================================================
# PROBLEM 1397 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def has_list(**kwargs):                                  # [Line 12] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    return any(isinstance(v, list) for v in kwargs.values())  # [Line 13]

print(has_list(a=[1,2], b="x"))                          # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1398  
Write a Python function that prints whether the number of keyword arguments is even or odd.
"""

# ======================================================================
# PROBLEM 1398 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def even_or_odd_kwargs(**kwargs):                        # [Line 12] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    print("Even" if len(kwargs) % 2 == 0 else "Odd")     # [Line 13] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

even_or_odd_kwargs(a=1, b=2, c=3)                        # [Line 15] | FUNCTION CALL: Executes the function 'even_or_odd_kwargs' | Expected: Odd


""" 
Problem: 1399  
Write a Python function that accepts **kwargs and renames any keys that start with 'temp_' by removing the prefix.
"""

# ======================================================================
# PROBLEM 1399 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def clean_temp_keys(**kwargs):                           # [Line 12] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    return {k[5:] if k.startswith('temp_') else k: v for k, v in kwargs.items()}  # [Line 13] | SLICING OPERATION [5:] - Extracts all elements starting from index 5 to the end. 

print(clean_temp_keys(temp_x=1, y=2))                    # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {'x': 1, 'y': 2}


""" 
Problem: 1400  
Write a Python function that accepts **kwargs and returns only those key-value pairs where the key is uppercase.
"""

# ======================================================================
# PROBLEM 1400 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def uppercase_keys_only(**kwargs):                       # [Line 12] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    return {k: v for k, v in kwargs.items() if k.isupper()}  # [Line 13]

print(uppercase_keys_only(AGE=30, name="Ann"))           # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {'AGE': 30}

""" 
Problem: 1402  
Write a Pythonic way to use `enumerate()` to get both index and value from a list.
"""

# ======================================================================
# PROBLEM 1402 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

fruits = ['apple', 'banana', 'cherry']                   # [Line 12] | ASSIGNMENT: Creates variable 'fruits' and stores the result of '['apple', 'banana', 'cherry']' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
for index, value in enumerate(fruits):                   # [Line 13]
    print(f"{index}: {value}")                           # [Line 14] | Expected: 0: apple, 1: banana, 2: cherry


""" 
Problem: 1403  
Write a Pythonic way to use `zip()` to combine two lists into a list of tuples.
"""

# ======================================================================
# PROBLEM 1403 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

names = ['Alice', 'Bob', 'Charlie']                      # [Line 12] | ASSIGNMENT: Creates variable 'names' and stores the result of '['Alice', 'Bob', 'Charlie']' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
ages = [25, 30, 35]                                      # [Line 13] | ASSIGNMENT: Creates variable 'ages' and stores the result of '[25, 30, 35]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
combined = list(zip(names, ages))                        # [Line 14] | ASSIGNMENT: Creates variable 'combined' and stores the result of 'list(zip(names, ages))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(combined)                                          # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]


""" 
Problem: 1404  
Write a Pythonic way to use a dictionary comprehension to swap keys and values.
"""

# ======================================================================
# PROBLEM 1404 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

original = {'a': 1, 'b': 2, 'c': 3}                      # [Line 12] | ASSIGNMENT: Creates variable 'original' and stores the result of '{'a': 1, 'b': 2, 'c': 3}' in it
swapped = {v: k for k, v in original.items()}            # [Line 13] | ASSIGNMENT: Creates variable 'swapped' and stores the result of '{v: k for k, v in original.items()}' in it
print(swapped)                                           # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {1: 'a', 2: 'b', 3: 'c'}


""" 
Problem: 1405  
Write a Pythonic way to use `all()` to check if all elements in a list satisfy a condition.
"""

# ======================================================================
# PROBLEM 1405 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

numbers = [2, 4, 6, 8]                                   # [Line 12] | ASSIGNMENT: Creates variable 'numbers' and stores the result of '[2, 4, 6, 8]' in it | DATA TYPE: List - A mutable ordered collection. Contains 4 elements
all_even = all(x % 2 == 0 for x in numbers)              # [Line 13] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1). | ASSIGNMENT: Creates variable 'all_even' and stores the result of 'all((x % 2 == 0 for x in numbers))' in it | FUNCTION CALL: Calls 'all()' and stores its return value
print(all_even)                                          # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1406  
Write a Pythonic way to flatten a list of lists using a list comprehension.
"""

# ======================================================================
# PROBLEM 1406 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]               # [Line 12] | ASSIGNMENT: Creates variable 'nested' and stores the result of '[[1, 2, 3], [4, 5], [6, 7, 8, 9]]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
flattened = [item for sublist in nested for item in sublist]  # [Line 13] | ASSIGNMENT: Creates variable 'flattened' and stores the result of '[item for sublist in nested for item in sublist]' in it
print(flattened)                                         # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9]


""" 
Problem: 1407  
Write a Pythonic way to use `map()` to convert a list of strings to uppercase.
"""

# ======================================================================
# PROBLEM 1407 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

words = ['hello', 'world', 'python']                     # [Line 12] | ASSIGNMENT: Creates variable 'words' and stores the result of '['hello', 'world', 'python']' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
uppercase_words = list(map(str.upper, words))            # [Line 13] | ASSIGNMENT: Creates variable 'uppercase_words' and stores the result of 'list(map(str.upper, words))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(uppercase_words)                                   # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: ['HELLO', 'WORLD', 'PYTHON']


""" 
Problem: 1408  
Write a Pythonic way to use `filter()` with a lambda to get even numbers from a list.
"""

# ======================================================================
# PROBLEM 1408 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]                # [Line 12] | ASSIGNMENT: Creates variable 'numbers' and stores the result of '[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]' in it | DATA TYPE: List - A mutable ordered collection. Contains 10 elements
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # [Line 13] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1). | ASSIGNMENT: Creates variable 'even_numbers' and stores the result of 'list(filter(lambda x: x % 2 == 0, numbers))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(even_numbers)                                      # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [2, 4, 6, 8, 10]


""" 
Problem: 1409  
Write a Pythonic way to use `set()` to remove duplicates from a list while preserving order using dict.fromkeys().
"""

# ======================================================================
# PROBLEM 1409 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

items = [1, 2, 2, 3, 3, 3, 4, 5, 5]                      # [Line 12] | ASSIGNMENT: Creates variable 'items' and stores the result of '[1, 2, 2, 3, 3, 3, 4, 5, 5]' in it | DATA TYPE: List - A mutable ordered collection. Contains 9 elements
unique_ordered = list(dict.fromkeys(items))              # [Line 13] | ASSIGNMENT: Creates variable 'unique_ordered' and stores the result of 'list(dict.fromkeys(items))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(unique_ordered)                                    # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [1, 2, 3, 4, 5]


""" 
Problem: 1410  
Write a Pythonic way to use `str.join()` to concatenate a list of strings with a separator.
"""

# ======================================================================
# PROBLEM 1410 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

words = ['Python', 'is', 'great']                        # [Line 12] | ASSIGNMENT: Creates variable 'words' and stores the result of '['Python', 'is', 'great']' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
sentence = ' '.join(words)                               # [Line 13] | ASSIGNMENT: Creates variable 'sentence' and stores the result of '' '.join(words)' in it | FUNCTION CALL: Calls '' '.join()' and stores its return value
print(sentence)                                          # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: Python is great


""" 
Problem: 1411  
Write a Pythonic way to use list slicing to reverse a string.
"""

# ======================================================================
# PROBLEM 1411 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

text = "Python"                                          # [Line 12] | ASSIGNMENT: Creates variable 'text' and stores the result of ''Python'' in it | DATA TYPE: String - A sequence of characters. Length: 6
reversed_text = text[::-1]                               # [Line 13] | SLICING OPERATION [::-1] - This is a reverse slice. The syntax [::-1] means: start at the beginning (no start index), stop at the end (no stop index), and step backwards by 1. This effectively reverses the entire sequence. Example: [1,2,3][::-1] becomes [3,2,1] | ASSIGNMENT: Creates variable 'reversed_text' and stores the result of 'text[::-1]' in it | SUBSCRIPTION: Accesses an element or slice from a sequence using []
print(reversed_text)                                     # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: nohtyP


""" 
Problem: 1412  
Write a Pythonic way to use `collections.Counter` to count character frequencies in a string.
"""

# ======================================================================
# PROBLEM 1412 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

from collections import Counter                          # [Line 12]
text = "hello world"                                     # [Line 13] | ASSIGNMENT: Creates variable 'text' and stores the result of ''hello world'' in it | DATA TYPE: String - A sequence of characters. Length: 11
char_counts = Counter(text)                              # [Line 14] | ASSIGNMENT: Creates variable 'char_counts' and stores the result of 'Counter(text)' in it | FUNCTION CALL: Calls 'Counter()' and stores its return value
print(char_counts)                                       # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})


""" 
Problem: 1413  
Write a Pythonic way to use `itertools.chain()` to combine multiple lists into one.
"""

# ======================================================================
# PROBLEM 1413 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

from itertools import chain                              # [Line 12]
list1 = [1, 2, 3]                                        # [Line 13] | ASSIGNMENT: Creates variable 'list1' and stores the result of '[1, 2, 3]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
list2 = [4, 5, 6]                                        # [Line 14] | ASSIGNMENT: Creates variable 'list2' and stores the result of '[4, 5, 6]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
list3 = [7, 8, 9]                                        # [Line 15] | ASSIGNMENT: Creates variable 'list3' and stores the result of '[7, 8, 9]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
combined = list(chain(list1, list2, list3))              # [Line 16] | ASSIGNMENT: Creates variable 'combined' and stores the result of 'list(chain(list1, list2, list3))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(combined)                                          # [Line 17] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9]


""" 
Problem: 1414  
Write a Pythonic way to use `str.split()` and list comprehension to capitalize each word.
"""

# ======================================================================
# PROBLEM 1414 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

text = "hello world python"                              # [Line 12] | ASSIGNMENT: Creates variable 'text' and stores the result of ''hello world python'' in it | DATA TYPE: String - A sequence of characters. Length: 18
capitalized = ' '.join(word.capitalize() for word in text.split())  # [Line 13] | ASSIGNMENT: Creates variable 'capitalized' and stores the result of '' '.join((word.capitalize() for word in text.split()))' in it | FUNCTION CALL: Calls '' '.join()' and stores its return value
print(capitalized)                                       # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: Hello World Python


""" 
Problem: 1415  
Write a Pythonic way to use `zip()` with `*` to transpose a list of lists.
"""

# ======================================================================
# PROBLEM 1415 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]               # [Line 12] | ASSIGNMENT: Creates variable 'matrix' and stores the result of '[[1, 2, 3], [4, 5, 6], [7, 8, 9]]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
transposed = list(zip(*matrix))                          # [Line 13] | ASSIGNMENT: Creates variable 'transposed' and stores the result of 'list(zip(*matrix))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(transposed)                                        # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [(1, 4, 7), (2, 5, 8), (3, 6, 9)]


""" 
Problem: 1416  
Write a Pythonic way to use `dict.get()` with a default value to safely access dictionary keys.
"""

# ======================================================================
# PROBLEM 1416 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

data = {'name': 'Alice', 'age': 30}                      # [Line 12] | ASSIGNMENT: Creates variable 'data' and stores the result of '{'name': 'Alice', 'age': 30}' in it
name = data.get('name', 'Unknown')                       # [Line 13] | ASSIGNMENT: Creates variable 'name' and stores the result of 'data.get('name', 'Unknown')' in it | FUNCTION CALL: Calls 'data.get()' and stores its return value
city = data.get('city', 'Unknown')                       # [Line 14] | ASSIGNMENT: Creates variable 'city' and stores the result of 'data.get('city', 'Unknown')' in it | FUNCTION CALL: Calls 'data.get()' and stores its return value
print(name, city)                                        # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: Alice Unknown


""" 
Problem: 1417  
Write a Pythonic way to use `collections.defaultdict` to group items by a key.
"""

# ======================================================================
# PROBLEM 1417 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

from collections import defaultdict                      # [Line 12]
items = [('fruit', 'apple'), ('fruit', 'banana'), ('vegetable', 'carrot'), ('fruit', 'cherry')]  # [Line 13] | ASSIGNMENT: Creates variable 'items' and stores the result of '[('fruit', 'apple'), ('fruit', 'banana'), ('vegetable', 'carrot'), ('fruit', 'cherry')]' in it | DATA TYPE: List - A mutable ordered collection. Contains 4 elements
grouped = defaultdict(list)                              # [Line 14] | ASSIGNMENT: Creates variable 'grouped' and stores the result of 'defaultdict(list)' in it | FUNCTION CALL: Calls 'defaultdict()' and stores its return value
for category, item in items:                             # [Line 15]
    grouped[category].append(item)                       # [Line 16]
print(dict(grouped))                                     # [Line 17] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {'fruit': ['apple', 'banana', 'cherry'], 'vegetable': ['carrot']}


""" 
Problem: 1418  
Write a Pythonic way to use `itertools.groupby()` to group consecutive identical elements.
"""

# ======================================================================
# PROBLEM 1418 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

from itertools import groupby                            # [Line 12]
data = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4]                    # [Line 13] | ASSIGNMENT: Creates variable 'data' and stores the result of '[1, 1, 1, 2, 2, 3, 3, 3, 3, 4]' in it | DATA TYPE: List - A mutable ordered collection. Contains 10 elements
grouped = {k: list(g) for k, g in groupby(data)}         # [Line 14] | ASSIGNMENT: Creates variable 'grouped' and stores the result of '{k: list(g) for k, g in groupby(data)}' in it
print(grouped)                                           # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {1: [1, 1, 1], 2: [2, 2], 3: [3, 3, 3, 3], 4: [4]}


""" 
Problem: 1419  
Write a Pythonic way to use `str.maketrans()` and `str.translate()` to replace multiple characters.
"""

# ======================================================================
# PROBLEM 1419 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

text = "hello world"                                     # [Line 12] | ASSIGNMENT: Creates variable 'text' and stores the result of ''hello world'' in it | DATA TYPE: String - A sequence of characters. Length: 11
translation = str.maketrans('lo', '12')                  # [Line 13] | ASSIGNMENT: Creates variable 'translation' and stores the result of 'str.maketrans('lo', '12')' in it | FUNCTION CALL: Calls 'str.maketrans()' and stores its return value
result = text.translate(translation)                     # [Line 14] | ASSIGNMENT: Creates variable 'result' and stores the result of 'text.translate(translation)' in it | FUNCTION CALL: Calls 'text.translate()' and stores its return value
print(result)                                            # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: he112 w2r1d


""" 
Problem: 1420  
Write a Pythonic way to use `frozenset()` to create an immutable set for use as a dictionary key.
"""

# ======================================================================
# PROBLEM 1420 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

fs1 = frozenset([1, 2, 3])                               # [Line 12] | ASSIGNMENT: Creates variable 'fs1' and stores the result of 'frozenset([1, 2, 3])' in it | FUNCTION CALL: Calls 'frozenset()' and stores its return value
fs2 = frozenset([4, 5, 6])                               # [Line 13] | ASSIGNMENT: Creates variable 'fs2' and stores the result of 'frozenset([4, 5, 6])' in it | FUNCTION CALL: Calls 'frozenset()' and stores its return value
mapping = {fs1: 'first', fs2: 'second'}                  # [Line 14] | ASSIGNMENT: Creates variable 'mapping' and stores the result of '{fs1: 'first', fs2: 'second'}' in it
print(mapping[fs1])                                      # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: first


""" 
Problem: 1421  
Write a Pythonic way to use `itertools.combinations()` to generate all pairs from a list.
"""

# ======================================================================
# PROBLEM 1421 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

from itertools import combinations                       # [Line 12]
items = ['a', 'b', 'c', 'd']                             # [Line 13] | ASSIGNMENT: Creates variable 'items' and stores the result of '['a', 'b', 'c', 'd']' in it | DATA TYPE: List - A mutable ordered collection. Contains 4 elements
pairs = list(combinations(items, 2))                     # [Line 14] | ASSIGNMENT: Creates variable 'pairs' and stores the result of 'list(combinations(items, 2))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(pairs)                                             # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')]


""" 
Problem: 1422  
Write a Pythonic way to use `collections.deque` to implement a queue with append and popleft.
"""

# ======================================================================
# PROBLEM 1422 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

from collections import deque                            # [Line 12]
queue = deque()                                          # [Line 13] | ASSIGNMENT: Creates variable 'queue' and stores the result of 'deque()' in it | FUNCTION CALL: Calls 'deque()' and stores its return value
queue.append(1)                                          # [Line 14] | FUNCTION CALL: Executes the function 'queue.append' | ARGUMENTS: Passes 1 argument(s) to the function
queue.append(2)                                          # [Line 15] | FUNCTION CALL: Executes the function 'queue.append' | ARGUMENTS: Passes 1 argument(s) to the function
queue.append(3)                                          # [Line 16] | FUNCTION CALL: Executes the function 'queue.append' | ARGUMENTS: Passes 1 argument(s) to the function
first = queue.popleft()                                  # [Line 17] | ASSIGNMENT: Creates variable 'first' and stores the result of 'queue.popleft()' in it | FUNCTION CALL: Calls 'queue.popleft()' and stores its return value
print(first, list(queue))                                # [Line 18] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 1 [2, 3]


""" 
Problem: 1423  
Write a Pythonic way to use `str.partition()` to split a string at the first occurrence of a delimiter.
"""

# ======================================================================
# PROBLEM 1423 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

text = "hello:world:python"                              # [Line 12] | ASSIGNMENT: Creates variable 'text' and stores the result of ''hello:world:python'' in it | DATA TYPE: String - A sequence of characters. Length: 18
before, sep, after = text.partition(':')                 # [Line 13] | ASSIGNMENT: Creates variable '(before, sep, after)' and stores the result of 'text.partition(':')' in it | FUNCTION CALL: Calls 'text.partition()' and stores its return value
print(before, after)                                     # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: hello world:python


""" 
Problem: 1424  
Write a Pythonic way to use `operator.itemgetter()` to sort a list of dictionaries by a key.
"""

# ======================================================================
# PROBLEM 1424 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

from operator import itemgetter                          # [Line 12]
people = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]  # [Line 13] | SLICING OPERATION - Extracts a portion of the sequence | ASSIGNMENT: Creates variable 'people' and stores the result of '[{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
sorted_people = sorted(people, key=itemgetter('age'))    # [Line 14] | ASSIGNMENT: Creates variable 'sorted_people' and stores the result of 'sorted(people, key=itemgetter('age'))' in it | FUNCTION CALL: Calls 'sorted()' and stores its return value
print(sorted_people)                                     # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]


""" 
Problem: 1425  
Write a Pythonic way to use `contextlib.suppress()` to ignore specific exceptions.
"""

# ======================================================================
# PROBLEM 1425 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

from contextlib import suppress                          # [Line 12]
with suppress(ValueError, ZeroDivisionError):            # [Line 13]
    result = int("not a number")                         # [Line 14] | This would raise ValueError, but it's suppressed
    print("This won't print")                            # [Line 15]
print("Continues after exception")                       # [Line 16] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: Continues after exception


""" 
Problem: 1426  
Write a Pythonic way to check if any item in a list is true.
"""

# ======================================================================
# PROBLEM 1426 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = [0, False, 5]                                      # [Line 12] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[0, False, 5]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(any(lst))                                          # [Line 13] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1427  
Write a Pythonic way to use a generator expression to calculate the sum of squares.
"""

# ======================================================================
# PROBLEM 1427 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = [1, 2, 3]                                          # [Line 12] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[1, 2, 3]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
total = sum(x**2 for x in lst)                           # [Line 13] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2. | ASSIGNMENT: Creates variable 'total' and stores the result of 'sum((x ** 2 for x in lst))' in it | FUNCTION CALL: Calls 'sum()' and stores its return value
print(total)                                             # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 14


""" 
Problem: 1428  
Write a Pythonic program to get the intersection of two sets.
"""

# ======================================================================
# PROBLEM 1428 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

a = {1, 2, 3}                                            # [Line 12] | ASSIGNMENT: Creates variable 'a' and stores the result of '{1, 2, 3}' in it
b = {2, 3, 4}                                            # [Line 13] | ASSIGNMENT: Creates variable 'b' and stores the result of '{2, 3, 4}' in it
print(a & b)                                             # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {2, 3}


""" 
Problem: 1429  
Write a Pythonic program to get the union of two sets.
"""

# ======================================================================
# PROBLEM 1429 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

print(a | b)                                             # [Line 12] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {1, 2, 3, 4}


""" 
Problem: 1430  
Write a Pythonic way to check if a string contains only digits.
"""

# ======================================================================
# PROBLEM 1430 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

s = "12345"                                              # [Line 12] | ASSIGNMENT: Creates variable 's' and stores the result of ''12345'' in it | DATA TYPE: String - A sequence of characters. Length: 5
print(s.isdigit())                                       # [Line 13] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1431  
Write a Pythonic one-liner to reverse a list.
"""

# ======================================================================
# PROBLEM 1431 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = [1, 2, 3]                                          # [Line 12] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[1, 2, 3]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(lst[::-1])                                         # [Line 13] | SLICING OPERATION [::-1] - This is a reverse slice. The syntax [::-1] means: start at the beginning (no start index), stop at the end (no stop index), and step backwards by 1. This effectively reverses the entire sequence. Example: [1,2,3][::-1] becomes [3,2,1] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [3, 2, 1]


""" 
Problem: 1432  
Write a Pythonic way to zip dictionary keys and values into a list of tuples.
"""

# ======================================================================
# PROBLEM 1432 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

d = {'a': 1, 'b': 2}                                     # [Line 12] | ASSIGNMENT: Creates variable 'd' and stores the result of '{'a': 1, 'b': 2}' in it
zipped = list(zip(d.keys(), d.values()))                 # [Line 13] | ASSIGNMENT: Creates variable 'zipped' and stores the result of 'list(zip(d.keys(), d.values()))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(zipped)                                            # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [('a', 1), ('b', 2)]


""" 
Problem: 1433  
Write a Pythonic way to initialize a dictionary with default integer values.
"""

# ======================================================================
# PROBLEM 1433 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

from collections import defaultdict                      # [Line 12]
d = defaultdict(int)                                     # [Line 13] | ASSIGNMENT: Creates variable 'd' and stores the result of 'defaultdict(int)' in it | FUNCTION CALL: Calls 'defaultdict()' and stores its return value
d["x"] += 1                                              # [Line 14]
print(d["x"])                                            # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 1


""" 
Problem: 1434  
Write a Pythonic program to group elements by length from a list of words.
"""

# ======================================================================
# PROBLEM 1434 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

words = ["hi", "hello", "yes", "no"]                     # [Line 12] | ASSIGNMENT: Creates variable 'words' and stores the result of '['hi', 'hello', 'yes', 'no']' in it | DATA TYPE: List - A mutable ordered collection. Contains 4 elements
from collections import defaultdict                      # [Line 13]
grouped = defaultdict(list)                              # [Line 14] | ASSIGNMENT: Creates variable 'grouped' and stores the result of 'defaultdict(list)' in it | FUNCTION CALL: Calls 'defaultdict()' and stores its return value
for word in words:                                       # [Line 15]
    grouped[len(word)].append(word)                      # [Line 16]
print(dict(grouped))                                     # [Line 17] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {2: ['hi', 'no'], 5: ['hello'], 3: ['yes']}


""" 
Problem: 1435  
Write a Pythonic program to sort a list of tuples by the second item.
"""

# ======================================================================
# PROBLEM 1435 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = [(1, 3), (2, 1), (4, 2)]                           # [Line 12] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[(1, 3), (2, 1), (4, 2)]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
sorted_lst = sorted(lst, key=lambda x: x[1])             # [Line 13] | SLICING OPERATION - Extracts a portion of the sequence | ASSIGNMENT: Creates variable 'sorted_lst' and stores the result of 'sorted(lst, key=lambda x: x[1])' in it | FUNCTION CALL: Calls 'sorted()' and stores its return value
print(sorted_lst)                                        # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [(2, 1), (4, 2), (1, 3)]


""" 
Problem: 1436  
Write a Pythonic way to use a context manager to read a file.
"""

# ======================================================================
# PROBLEM 1436 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

# Simulated context manager example
with open("temp.txt", "w") as f:                         # [Line 13]
    f.write("Hello")                                     # [Line 14]
with open("temp.txt") as f:                              # [Line 15]
    print(f.read())                                      # [Line 16] | Expected: "Hello"


""" 
Problem: 1437  
Write a Pythonic one-liner to find the maximum item in a list.
"""

# ======================================================================
# PROBLEM 1437 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = [1, 5, 2]                                          # [Line 12] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[1, 5, 2]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(max(lst))                                          # [Line 13] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 5


""" 
Problem: 1438  
Write a Pythonic way to assign multiple variables from a list.
"""

# ======================================================================
# PROBLEM 1438 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = [1, 2, 3]                                          # [Line 12] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[1, 2, 3]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
a, b, c = lst                                            # [Line 13] | ASSIGNMENT: Creates variable '(a, b, c)' and stores the result of 'lst' in it
print(a, b, c)                                           # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 1 2 3


""" 
Problem: 1439  
Write a Pythonic way to create a dictionary from two lists.
"""

# ======================================================================
# PROBLEM 1439 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

keys = ['a', 'b']                                        # [Line 12] | ASSIGNMENT: Creates variable 'keys' and stores the result of '['a', 'b']' in it | DATA TYPE: List - A mutable ordered collection. Contains 2 elements
values = [1, 2]                                          # [Line 13] | ASSIGNMENT: Creates variable 'values' and stores the result of '[1, 2]' in it | DATA TYPE: List - A mutable ordered collection. Contains 2 elements
d = dict(zip(keys, values))                              # [Line 14] | ASSIGNMENT: Creates variable 'd' and stores the result of 'dict(zip(keys, values))' in it | FUNCTION CALL: Calls 'dict()' and stores its return value
print(d)                                                 # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {'a': 1, 'b': 2}


""" 
Problem: 1440  
Write a Pythonic way to remove a key from a dictionary if it exists.
"""

# ======================================================================
# PROBLEM 1440 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

d = {'a': 1, 'b': 2}                                     # [Line 12] | ASSIGNMENT: Creates variable 'd' and stores the result of '{'a': 1, 'b': 2}' in it
d.pop('b', None)                                         # [Line 13] | FUNCTION CALL: Executes the function 'd.pop' | ARGUMENTS: Passes 2 argument(s) to the function
print(d)                                                 # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {'a': 1}


""" 
Problem: 1441  
Write a Pythonic way to check if a variable is None.
"""

# ======================================================================
# PROBLEM 1441 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

x = None                                                 # [Line 12] | ASSIGNMENT: Creates variable 'x' and stores the result of 'None' in it
print(x is None)                                         # [Line 13] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1442  
Write a Pythonic way to handle a missing dictionary key using try-except.
"""

# ======================================================================
# PROBLEM 1442 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

d = {'a': 1}                                             # [Line 12] | ASSIGNMENT: Creates variable 'd' and stores the result of '{'a': 1}' in it
try:                                                     # [Line 13]
    print(d['b'])                                        # [Line 14]
except KeyError:                                         # [Line 15]
    print("Key not found")                               # [Line 16] | Expected: Key not found


""" 
Problem: 1443  
Write a Pythonic way to unpack a tuple into variables.
"""

# ======================================================================
# PROBLEM 1443 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

t = (1, 2)                                               # [Line 12] | ASSIGNMENT: Creates variable 't' and stores the result of '(1, 2)' in it | DATA TYPE: Tuple - An immutable ordered collection. Contains 2 elements
x, y = t                                                 # [Line 13] | ASSIGNMENT: Creates variable '(x, y)' and stores the result of 't' in it
print(x, y)                                              # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 1 2


""" 
Problem: 1444  
Write a Pythonic one-liner to check if a list contains duplicates.
"""

# ======================================================================
# PROBLEM 1444 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = [1, 2, 2]                                          # [Line 12] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[1, 2, 2]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(len(lst) != len(set(lst)))                         # [Line 13] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1445  
Write a Pythonic program to count character frequencies in a string.
"""

# ======================================================================
# PROBLEM 1445 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

s = "banana"                                             # [Line 12] | ASSIGNMENT: Creates variable 's' and stores the result of ''banana'' in it | DATA TYPE: String - A sequence of characters. Length: 6
freq = Counter(s)                                        # [Line 13] | ASSIGNMENT: Creates variable 'freq' and stores the result of 'Counter(s)' in it | FUNCTION CALL: Calls 'Counter()' and stores its return value
print(freq)                                              # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {'b': 1, 'a': 3, 'n': 2}


""" 
Problem: 1446  
Write a Pythonic one-liner to filter out negative numbers from a list.
"""

# ======================================================================
# PROBLEM 1446 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = [1, -2, 3, -4]                                     # [Line 12] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[1, -2, 3, -4]' in it | DATA TYPE: List - A mutable ordered collection. Contains 4 elements
print([x for x in lst if x >= 0])                        # [Line 13] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [1, 3]


""" 
Problem: 1447  
Write a Pythonic way to test if a list has at least one even number.
"""

# ======================================================================
# PROBLEM 1447 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = [1, 3, 4]                                          # [Line 12] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[1, 3, 4]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(any(x % 2 == 0 for x in lst))                      # [Line 13] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1). | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1448  
Write a Pythonic way to get the index of an item in a list.
"""

# ======================================================================
# PROBLEM 1448 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = ['a', 'b', 'c']                                    # [Line 12] | ASSIGNMENT: Creates variable 'lst' and stores the result of '['a', 'b', 'c']' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(lst.index('b'))                                    # [Line 13] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 1


""" 
Problem: 1449  
Write a Pythonic way to filter dictionary items with values > 10.
"""

# ======================================================================
# PROBLEM 1449 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

d = {'a': 5, 'b': 15}                                    # [Line 12] | ASSIGNMENT: Creates variable 'd' and stores the result of '{'a': 5, 'b': 15}' in it
filtered = {k: v for k, v in d.items() if v > 10}        # [Line 13] | ASSIGNMENT: Creates variable 'filtered' and stores the result of '{k: v for k, v in d.items() if v > 10}' in it
print(filtered)                                          # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {'b': 15}


""" 
Problem: 1450  
Write a Pythonic program to invert a dictionary (keys become values, values become keys).
"""

# ======================================================================
# PROBLEM 1450 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

d = {'a': 1, 'b': 2}                                     # [Line 12] | ASSIGNMENT: Creates variable 'd' and stores the result of '{'a': 1, 'b': 2}' in it
inverted = {v: k for k, v in d.items()}                  # [Line 13] | ASSIGNMENT: Creates variable 'inverted' and stores the result of '{v: k for k, v in d.items()}' in it
print(inverted)                                          # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {1: 'a', 2: 'b'}

""" 
Problem: 1451  
Write a Python program using `all()` to check if all numbers in a list are positive.
"""

# ======================================================================
# PROBLEM 1451 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = [1, 2, 3, 4]                                       # [Line 12] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[1, 2, 3, 4]' in it | DATA TYPE: List - A mutable ordered collection. Contains 4 elements
print(all(x > 0 for x in lst))                           # [Line 13] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1452  
Use `all()` to determine if all characters in a string are lowercase.
"""

# ======================================================================
# PROBLEM 1452 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

s = "hello"                                              # [Line 12] | ASSIGNMENT: Creates variable 's' and stores the result of ''hello'' in it | DATA TYPE: String - A sequence of characters. Length: 5
print(all(c.islower() for c in s))                       # [Line 13] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1453  
Write a Pythonic way to use `all()` to check if all elements in a list are even.
"""

# ======================================================================
# PROBLEM 1453 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = [2, 4, 6]                                          # [Line 12] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[2, 4, 6]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(all(x % 2 == 0 for x in lst))                      # [Line 13] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1). | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1454  
Check if all items in a dictionary have non-empty values using `all()`.
"""

# ======================================================================
# PROBLEM 1454 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

d = {"a": 1, "b": "hello", "c": [1]}                     # [Line 12] | SLICING OPERATION - Extracts a portion of the sequence | ASSIGNMENT: Creates variable 'd' and stores the result of '{'a': 1, 'b': 'hello', 'c': [1]}' in it
print(all(bool(v) for v in d.values()))                  # [Line 13] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1455  
Use `all()` to check if all items in a set are greater than 10.
"""

# ======================================================================
# PROBLEM 1455 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

s = {11, 12, 13}                                         # [Line 12] | ASSIGNMENT: Creates variable 's' and stores the result of '{11, 12, 13}' in it
print(all(x > 10 for x in s))                            # [Line 13] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1456  
Use `all()` to validate that all lines in a list start with a capital letter.
"""

# ======================================================================
# PROBLEM 1456 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lines = ["Hello", "World", "Python"]                     # [Line 12] | ASSIGNMENT: Creates variable 'lines' and stores the result of '['Hello', 'World', 'Python']' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(all(line[0].isupper() for line in lines))          # [Line 13] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1457  
Use `all()` to check if all elements in a matrix row are equal.
"""

# ======================================================================
# PROBLEM 1457 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

row = [5, 5, 5]                                          # [Line 12] | ASSIGNMENT: Creates variable 'row' and stores the result of '[5, 5, 5]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(all(x == row[0] for x in row))                     # [Line 13] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity). | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1458  
Use `all()` to check if all values in a list are strings.
"""

# ======================================================================
# PROBLEM 1458 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = ["a", "b", "c"]                                    # [Line 12] | ASSIGNMENT: Creates variable 'lst' and stores the result of '['a', 'b', 'c']' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(all(isinstance(x, str) for x in lst))              # [Line 13] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1459  
Write a Python program that uses `all()` to check if all keys in a dictionary are strings.
"""

# ======================================================================
# PROBLEM 1459 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

d = {"a": 1, "b": 2}                                     # [Line 12] | ASSIGNMENT: Creates variable 'd' and stores the result of '{'a': 1, 'b': 2}' in it
print(all(isinstance(k, str) for k in d.keys()))         # [Line 13] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1460  
Use `all()` to verify that all files have a ".txt" extension.
"""

# ======================================================================
# PROBLEM 1460 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

files = ["doc1.txt", "doc2.txt"]                         # [Line 12] | ASSIGNMENT: Creates variable 'files' and stores the result of '['doc1.txt', 'doc2.txt']' in it | DATA TYPE: List - A mutable ordered collection. Contains 2 elements
print(all(f.endswith(".txt") for f in files))            # [Line 13] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1461  
Use `all()` to check if all numbers in a list are within a certain range.
"""

# ======================================================================
# PROBLEM 1461 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

nums = [5, 6, 7]                                         # [Line 12] | ASSIGNMENT: Creates variable 'nums' and stores the result of '[5, 6, 7]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(all(1 <= x <= 10 for x in nums))                   # [Line 13] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1462  
Check if all sublists in a 2D list are non-empty using `all()`.
"""

# ======================================================================
# PROBLEM 1462 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

matrix = [[1], [2], [3]]                                 # [Line 12] | ASSIGNMENT: Creates variable 'matrix' and stores the result of '[[1], [2], [3]]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(all(len(sublist) > 0 for sublist in matrix))       # [Line 13] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1463  
Use `all()` to confirm all booleans in a list are True.
"""

# ======================================================================
# PROBLEM 1463 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

flags = [True, True, True]                               # [Line 12] | ASSIGNMENT: Creates variable 'flags' and stores the result of '[True, True, True]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(all(flags))                                        # [Line 13] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1464  
Use `all()` to verify all words in a list contain the letter "a".
"""

# ======================================================================
# PROBLEM 1464 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

words = ["apple", "banana", "grape"]                     # [Line 12] | ASSIGNMENT: Creates variable 'words' and stores the result of '['apple', 'banana', 'grape']' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(all("a" in word for word in words))                # [Line 13] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1465  
Write a Python program using `all()` to check if a list of numbers is strictly increasing.
"""

# ======================================================================
# PROBLEM 1465 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

nums = [1, 2, 3, 4]                                      # [Line 12] | ASSIGNMENT: Creates variable 'nums' and stores the result of '[1, 2, 3, 4]' in it | DATA TYPE: List - A mutable ordered collection. Contains 4 elements
print(all(x < y for x, y in zip(nums, nums[1:])))        # [Line 13] | SLICING OPERATION [1:] - Extracts all elements starting from index 1 to the end.  | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1466  
Check if all environment variables in a list are defined (non-empty strings).
"""

# ======================================================================
# PROBLEM 1466 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

envs = ["PATH", "HOME", "USER"]                          # [Line 12] | ASSIGNMENT: Creates variable 'envs' and stores the result of '['PATH', 'HOME', 'USER']' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(all(isinstance(env, str) and env for env in envs))  # [Line 13] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1467  
Use `all()` to ensure all items in a tuple are of the same type.
"""

# ======================================================================
# PROBLEM 1467 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

t = (1, 2, 3)                                            # [Line 12] | ASSIGNMENT: Creates variable 't' and stores the result of '(1, 2, 3)' in it | DATA TYPE: Tuple - An immutable ordered collection. Contains 3 elements
print(all(type(x) == type(t[0]) for x in t))             # [Line 13] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity). | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1468  
Check if all numbers in a list are prime using `all()` and a helper function.
"""

# ======================================================================
# PROBLEM 1468 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def is_prime(n):                                         # [Line 12]
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1))  # [Line 13] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

lst = [2, 3, 5, 7]                                       # [Line 15] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[2, 3, 5, 7]' in it | DATA TYPE: List - A mutable ordered collection. Contains 4 elements
print(all(is_prime(x) for x in lst))                     # [Line 16] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1469  
Use `all()` to confirm all values in a list are not None.
"""

# ======================================================================
# PROBLEM 1469 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = [1, 2, 3]                                          # [Line 12] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[1, 2, 3]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(all(x is not None for x in lst))                   # [Line 13] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1470  
Use `all()` to verify that all passwords in a list are at least 8 characters long.
"""

# ======================================================================
# PROBLEM 1470 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

passwords = ["abcdefgh", "12345678", "password"]         # [Line 12] | ASSIGNMENT: Creates variable 'passwords' and stores the result of '['abcdefgh', '12345678', 'password']' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(all(len(p) >= 8 for p in passwords))               # [Line 13] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True

""" 
Problem: 1471  
Write a Python program to check if a variable is `None` using `is`.
"""

# ======================================================================
# PROBLEM 1471 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

x = None                                                 # [Line 12] | ASSIGNMENT: Creates variable 'x' and stores the result of 'None' in it
print(x is None)                                         # [Line 13] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1472  
Check if two variables point to the same list object using `is`.
"""

# ======================================================================
# PROBLEM 1472 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

a = []                                                   # [Line 12] | ASSIGNMENT: Creates variable 'a' and stores the result of '[]' in it | DATA TYPE: List - A mutable ordered collection. Contains 0 elements
b = a                                                    # [Line 13] | ASSIGNMENT: Creates variable 'b' and stores the result of 'a' in it
print(a is b)                                            # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1473  
Check if two separately created lists are not the same object using `is`.
"""

# ======================================================================
# PROBLEM 1473 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

a = []                                                   # [Line 12] | ASSIGNMENT: Creates variable 'a' and stores the result of '[]' in it | DATA TYPE: List - A mutable ordered collection. Contains 0 elements
b = []                                                   # [Line 13] | ASSIGNMENT: Creates variable 'b' and stores the result of '[]' in it | DATA TYPE: List - A mutable ordered collection. Contains 0 elements
print(a is not b)                                        # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1474  
Use `is` to check if a variable is exactly `True`.
"""

# ======================================================================
# PROBLEM 1474 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

flag = True                                              # [Line 12] | ASSIGNMENT: Creates variable 'flag' and stores the result of 'True' in it | DATA TYPE: Integer - A whole number: True
print(flag is True)                                      # [Line 13] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1475  
Use `is` to check identity of two strings (interned strings).
"""

# ======================================================================
# PROBLEM 1475 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

s1 = "hello"                                             # [Line 12] | ASSIGNMENT: Creates variable 's1' and stores the result of ''hello'' in it | DATA TYPE: String - A sequence of characters. Length: 5
s2 = "hello"                                             # [Line 13] | ASSIGNMENT: Creates variable 's2' and stores the result of ''hello'' in it | DATA TYPE: String - A sequence of characters. Length: 5
print(s1 is s2)                                          # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True (implementation detail in CPython)


""" 
Problem: 1476  
Use `is` to check identity of small integers.
"""

# ======================================================================
# PROBLEM 1476 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

a = 100                                                  # [Line 12] | ASSIGNMENT: Creates variable 'a' and stores the result of '100' in it | DATA TYPE: Integer - A whole number: 100
b = 100                                                  # [Line 13] | ASSIGNMENT: Creates variable 'b' and stores the result of '100' in it | DATA TYPE: Integer - A whole number: 100
print(a is b)                                            # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True (due to integer caching)


""" 
Problem: 1477  
Check if a function return value is `None` using `is`.
"""

# ======================================================================
# PROBLEM 1477 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def do_nothing():                                        # [Line 12]
    pass                                                 # [Line 13]

print(do_nothing() is None)                              # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1478  
Use `is` to check if a class attribute is shared.
"""

# ======================================================================
# PROBLEM 1478 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

class A:                                                 # [Line 12]
    x = []                                               # [Line 13]

a1 = A()                                                 # [Line 15] | ASSIGNMENT: Creates variable 'a1' and stores the result of 'A()' in it | FUNCTION CALL: Calls 'A()' and stores its return value
a2 = A()                                                 # [Line 16] | ASSIGNMENT: Creates variable 'a2' and stores the result of 'A()' in it | FUNCTION CALL: Calls 'A()' and stores its return value
print(a1.x is a2.x)                                      # [Line 17] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1479  
Use `is` to check if an object is the same before and after a function call.
"""

# ======================================================================
# PROBLEM 1479 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def identity(x):                                         # [Line 12]
    return x                                             # [Line 13]

obj = []                                                 # [Line 15] | ASSIGNMENT: Creates variable 'obj' and stores the result of '[]' in it | DATA TYPE: List - A mutable ordered collection. Contains 0 elements
print(obj is identity(obj))                              # [Line 16] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1480  
Use `is` to compare with built-in singleton `Ellipsis`.
"""

# ======================================================================
# PROBLEM 1480 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

x = ...                                                  # [Line 12] | ASSIGNMENT: Creates variable 'x' and stores the result of '...' in it
print(x is Ellipsis)                                     # [Line 13] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1481  
Check if two instances of a class are not the same object.
"""

# ======================================================================
# PROBLEM 1481 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

class X:                                                 # [Line 12]
    pass                                                 # [Line 13]

x1 = X()                                                 # [Line 15] | ASSIGNMENT: Creates variable 'x1' and stores the result of 'X()' in it | FUNCTION CALL: Calls 'X()' and stores its return value
x2 = X()                                                 # [Line 16] | ASSIGNMENT: Creates variable 'x2' and stores the result of 'X()' in it | FUNCTION CALL: Calls 'X()' and stores its return value
print(x1 is not x2)                                      # [Line 17] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1482  
Check identity of two variables referencing the same dictionary.
"""

# ======================================================================
# PROBLEM 1482 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

d1 = {"a": 1}                                            # [Line 12] | ASSIGNMENT: Creates variable 'd1' and stores the result of '{'a': 1}' in it
d2 = d1                                                  # [Line 13] | ASSIGNMENT: Creates variable 'd2' and stores the result of 'd1' in it
print(d1 is d2)                                          # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1483  
Use `is` in an assertion to verify object identity.
"""

# ======================================================================
# PROBLEM 1483 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

a = b = object()                                         # [Line 12] | ASSIGNMENT: Creates variable 'a' and stores the result of 'object()' in it | FUNCTION CALL: Calls 'object()' and stores its return value
assert a is b                                            # [Line 13]
print("Assertion passed")                                # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: Assertion passed

""" 
Problem: 1484  
Compare identity of two Boolean values using `is`.
"""

# ======================================================================
# PROBLEM 1484 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

x = (2 < 3)                                              # [Line 12] | ASSIGNMENT: Creates variable 'x' and stores the result of '2 < 3' in it
y = True                                                 # [Line 13] | ASSIGNMENT: Creates variable 'y' and stores the result of 'True' in it | DATA TYPE: Integer - A whole number: True
print(x is y)                                            # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1485  
Use `is not` to verify a function argument is not None.
"""

# ======================================================================
# PROBLEM 1485 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def greet(name):                                         # [Line 12]
    if name is not None:                                 # [Line 13]
        print(f"Hello, {name}!")                         # [Line 14]

greet("Alice")                                           # [Line 16] | FUNCTION CALL: Executes the function 'greet' | ARGUMENTS: Passes 1 argument(s) to the function | Expected: Hello, Alice!


""" 
Problem: 1486  
Use `is` to test if a global constant is unchanged.
"""

# ======================================================================
# PROBLEM 1486 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

SENTINEL = object()                                      # [Line 12] | ASSIGNMENT: Creates variable 'SENTINEL' and stores the result of 'object()' in it | FUNCTION CALL: Calls 'object()' and stores its return value
def check(x):                                            # [Line 13]
    return x is SENTINEL                                 # [Line 14]

value = SENTINEL                                         # [Line 16] | ASSIGNMENT: Creates variable 'value' and stores the result of 'SENTINEL' in it
print(check(value))                                      # [Line 17] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1487  
Check that changing a variable makes it no longer the same object.
"""

# ======================================================================
# PROBLEM 1487 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

a = [1, 2]                                               # [Line 12] | ASSIGNMENT: Creates variable 'a' and stores the result of '[1, 2]' in it | DATA TYPE: List - A mutable ordered collection. Contains 2 elements
b = a                                                    # [Line 13] | ASSIGNMENT: Creates variable 'b' and stores the result of 'a' in it
a = [1, 2]                                               # [Line 14] | ASSIGNMENT: Creates variable 'a' and stores the result of '[1, 2]' in it | DATA TYPE: List - A mutable ordered collection. Contains 2 elements
print(a is b)                                            # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: False


""" 
Problem: 1488  
Use `is` to compare with a constant declared elsewhere.
"""

# ======================================================================
# PROBLEM 1488 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

NONE_CONST = None                                        # [Line 12] | ASSIGNMENT: Creates variable 'NONE_CONST' and stores the result of 'None' in it
x = None                                                 # [Line 13] | ASSIGNMENT: Creates variable 'x' and stores the result of 'None' in it
print(x is NONE_CONST)                                   # [Line 14] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1489  
Use `is` with `not` to check that a value is not `False`.
"""

# ======================================================================
# PROBLEM 1489 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

value = "some text"                                      # [Line 12] | ASSIGNMENT: Creates variable 'value' and stores the result of ''some text'' in it | DATA TYPE: String - A sequence of characters. Length: 9
print(value is not False)                                # [Line 13] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1490  
Show that identity and equality are not always the same.
"""

# ======================================================================
# PROBLEM 1490 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

a = [1]                                                  # [Line 12] | ASSIGNMENT: Creates variable 'a' and stores the result of '[1]' in it | DATA TYPE: List - A mutable ordered collection. Contains 1 elements
b = [1]                                                  # [Line 13] | ASSIGNMENT: Creates variable 'b' and stores the result of '[1]' in it | DATA TYPE: List - A mutable ordered collection. Contains 1 elements
print(a == b)                                            # [Line 14] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity). | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True
print(a is b)                                            # [Line 15] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: False

""" 
Problem: 1491  
Use `default=` with the `max()` function to return a default when the list is empty.
"""

# ======================================================================
# PROBLEM 1491 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

nums = []                                                # [Line 12] | ASSIGNMENT: Creates variable 'nums' and stores the result of '[]' in it | DATA TYPE: List - A mutable ordered collection. Contains 0 elements
print(max(nums, default=0))                              # [Line 13] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 0


""" 
Problem: 1492  
Use `default=` with the `min()` function to avoid an error on an empty sequence.
"""

# ======================================================================
# PROBLEM 1492 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

values = []                                              # [Line 12] | ASSIGNMENT: Creates variable 'values' and stores the result of '[]' in it | DATA TYPE: List - A mutable ordered collection. Contains 0 elements
print(min(values, default=-1))                           # [Line 13] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: -1


""" 
Problem: 1493  
Use `default=` in `max()` to safely get the longest word from a list.
"""

# ======================================================================
# PROBLEM 1493 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

words = []                                               # [Line 12] | ASSIGNMENT: Creates variable 'words' and stores the result of '[]' in it | DATA TYPE: List - A mutable ordered collection. Contains 0 elements
print(max(words, key=len, default="None"))               # [Line 13] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: "None"


""" 
Problem: 1494  
Use `default=` with `next()` to get the first even number or -1.
"""

# ======================================================================
# PROBLEM 1494 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = [1, 3, 5]                                          # [Line 12] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[1, 3, 5]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(next((x for x in lst if x % 2 == 0), default=-1))  # [Line 13] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1). | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: -1


""" 
Problem: 1495  
Use `default=` in `next()` to safely access an item in a generator.
"""

# ======================================================================
# PROBLEM 1495 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

gen = (x for x in range(5) if x > 10)                    # [Line 12] | ASSIGNMENT: Creates variable 'gen' and stores the result of '(x for x in range(5) if x > 10)' in it
print(next(gen, default="No item"))                      # [Line 13] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: "No item"


""" 
Problem: 1496  
Use `default=` with `max()` on a filtered list to handle no matches.
"""

# ======================================================================
# PROBLEM 1496 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

nums = [1, 3, 5]                                         # [Line 12] | ASSIGNMENT: Creates variable 'nums' and stores the result of '[1, 3, 5]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(max((x for x in nums if x % 2 == 0), default=None))  # [Line 13] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1). | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: None


""" 
Problem: 1497  
Use `default=` in `min()` to get a fallback value when no condition matches.
"""

# ======================================================================
# PROBLEM 1497 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

nums = [1, 3, 5]                                         # [Line 12] | ASSIGNMENT: Creates variable 'nums' and stores the result of '[1, 3, 5]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(min((x for x in nums if x % 2 == 0), default=-1))  # [Line 13] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1). | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: -1


""" 
Problem: 1498  
Use `default=` with `next()` to find the first name starting with "Z".
"""

# ======================================================================
# PROBLEM 1498 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

names = ["Alice", "Bob"]                                 # [Line 12] | ASSIGNMENT: Creates variable 'names' and stores the result of '['Alice', 'Bob']' in it | DATA TYPE: List - A mutable ordered collection. Contains 2 elements
print(next((name for name in names if name.startswith("Z")), default="Not found"))  # [Line 13] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: "Not found"


""" 
Problem: 1499  
Use `default=` with `max()` to find the max in a sublist or return a placeholder.
"""

# ======================================================================
# PROBLEM 1499 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

data = []                                                # [Line 12] | ASSIGNMENT: Creates variable 'data' and stores the result of '[]' in it | DATA TYPE: List - A mutable ordered collection. Contains 0 elements
print(max(data, default="empty"))                        # [Line 13] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: "empty"


""" 
Problem: 1500  
Use `default=` in `next()` to handle an empty comprehension.
"""

# ======================================================================
# PROBLEM 1500 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

print(next((x for x in []), default="Empty"))            # [Line 12] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: "Empty"








# ======================================================================
# END OF CODE - SUMMARY
# ======================================================================
# This file contains 1500 Python programming problems with detailed explanations.
# Each problem demonstrates different Python concepts including:
# - Data structures (lists, tuples, dictionaries, sets)
# - Control flow (if/else, for/while loops)
# - Functions and lambda expressions
# - List comprehensions and generator expressions
# - String manipulation and slicing
# - File operations and path handling
# - And many more Python features!
# ======================================================================
