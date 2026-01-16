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


numbers = [1, 2, 3, 4, 5]                                # [Line 8] | ASSIGNMENT: Creates variable 'numbers' and stores the result of '[1, 2, 3, 4, 5]' in it | DATA TYPE: List - A mutable ordered collection. Contains 5 elements
reversed_list = numbers[::-1]                            # [Line 9] | SLICING OPERATION [::-1] - This is a reverse slice. The syntax [::-1] means: start at the beginning (no start index), stop at the end (no stop index), and step backwards by 1. This effectively reverses the entire sequence. Example: [1,2,3][::-1] becomes [3,2,1] | ASSIGNMENT: Creates variable 'reversed_list' and stores the result of 'numbers[::-1]' in it | SUBSCRIPTION: Accesses an element or slice from a sequence using []
print(reversed_list)                                     # [Line 10] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: [5, 4, 3, 2, 1]


"""
Problem: 1002
Write a Python program to extract every third element from a list.
"""

# ======================================================================
# PROBLEM 1002 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


numbers = [10, 20, 30, 40, 50, 60, 70, 80]               # [Line 18] | ASSIGNMENT: Creates variable 'numbers' and stores the result of '[10, 20, 30, 40, 50, 60, 70, 80]' in it | DATA TYPE: List - A mutable ordered collection. Contains 8 elements
sliced_list = numbers[::3]                               # [Line 19] | SLICING OPERATION [::3] - Extracts every 3th element. The step value of 3 means we skip 2 elements between each selected element. No start index means begin from the start (or end if step is negative). No stop index means go to the end (or beginning if step is negative).  | ASSIGNMENT: Creates variable 'sliced_list' and stores the result of 'numbers[::3]' in it | SUBSCRIPTION: Accesses an element or slice from a sequence using []
print(sliced_list)                                       # [Line 20] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: [10, 40, 70]


"""
Problem: 1003
Write a Python program to extract every second character from a string in reverse order.
"""

# ======================================================================
# PROBLEM 1003 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "abcdefghij"                                      # [Line 28] | ASSIGNMENT: Creates variable 'text' and stores the result of ''abcdefghij'' in it | DATA TYPE: String - A sequence of characters. Length: 10
sliced_text = text[::-2]                                 # [Line 29] | SLICING OPERATION [::-2] - Reverses the sequence with step -2. Negative step means we traverse backwards. No start index means begin from the start (or end if step is negative). No stop index means go to the end (or beginning if step is negative).  | ASSIGNMENT: Creates variable 'sliced_text' and stores the result of 'text[::-2]' in it | SUBSCRIPTION: Accesses an element or slice from a sequence using []
print(sliced_text)                                       # [Line 30] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: jhfdb


"""
Problem: 1004
Write a Python program to slice the middle three characters from a string with an odd length.
"""

# ======================================================================
# PROBLEM 1004 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "abcdefg"                                         # [Line 38] | ASSIGNMENT: Creates variable 'text' and stores the result of ''abcdefg'' in it | DATA TYPE: String - A sequence of characters. Length: 7
middle_index = len(text) // 2                            # [Line 39] | FLOOR DIVISION (//) - Divides two numbers and returns the largest integer less than or equal to the result. Example: 7 // 2 = 3 (not 3.5). This is useful for integer division when you don't want decimal results. | ASSIGNMENT: Creates variable 'middle_index' and stores the result of 'len(text) // 2' in it | BINARY OPERATION: Performs a calculation between two operands
sliced_text = text[middle_index - 1: middle_index + 2]   # [Line 40] | SLICING OPERATION - Extracts a portion of the sequence | ASSIGNMENT: Creates variable 'sliced_text' and stores the result of 'text[middle_index - 1:middle_index + 2]' in it | SUBSCRIPTION: Accesses an element or slice from a sequence using []
print(sliced_text)                                       # [Line 41] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: cde


"""
Problem: 1005
Write a Python program to remove the first and last characters from a string using slicing.
"""

# ======================================================================
# PROBLEM 1005 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "Python"                                          # [Line 49] | ASSIGNMENT: Creates variable 'text' and stores the result of ''Python'' in it | DATA TYPE: String - A sequence of characters. Length: 6
sliced_text = text[1:-1]                                 # [Line 50] | SLICING OPERATION [1:-1] - Extracts elements from index 1 to -2 (stop is exclusive).  | ASSIGNMENT: Creates variable 'sliced_text' and stores the result of 'text[1:-1]' in it | SUBSCRIPTION: Accesses an element or slice from a sequence using []
print(sliced_text)                                       # [Line 51] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: ytho


"""
Problem: 1006
Write a Python program to get the first half of a string using slicing.
"""

# ======================================================================
# PROBLEM 1006 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "abcdefgh"                                        # [Line 59] | ASSIGNMENT: Creates variable 'text' and stores the result of ''abcdefgh'' in it | DATA TYPE: String - A sequence of characters. Length: 8
sliced_text = text[:len(text) // 2]                      # [Line 60] | SLICING OPERATION - Extracts a portion of the sequence | FLOOR DIVISION (//) - Divides two numbers and returns the largest integer less than or equal to the result. Example: 7 // 2 = 3 (not 3.5). This is useful for integer division when you don't want decimal results. | ASSIGNMENT: Creates variable 'sliced_text' and stores the result of 'text[:len(text) // 2]' in it | SUBSCRIPTION: Accesses an element or slice from a sequence using []
print(sliced_text)                                       # [Line 61] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: abcd


"""
Problem: 1007
Write a Python program to get the second half of a string using slicing.
"""

# ======================================================================
# PROBLEM 1007 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "abcdefgh"                                        # [Line 69] | ASSIGNMENT: Creates variable 'text' and stores the result of ''abcdefgh'' in it | DATA TYPE: String - A sequence of characters. Length: 8
sliced_text = text[len(text) // 2:]                      # [Line 70] | SLICING OPERATION - Extracts a portion of the sequence | FLOOR DIVISION (//) - Divides two numbers and returns the largest integer less than or equal to the result. Example: 7 // 2 = 3 (not 3.5). This is useful for integer division when you don't want decimal results. | ASSIGNMENT: Creates variable 'sliced_text' and stores the result of 'text[len(text) // 2:]' in it | SUBSCRIPTION: Accesses an element or slice from a sequence using []
print(sliced_text)                                       # [Line 71] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: efgh


"""
Problem: 1008
Write a Python program to extract the middle two characters from an even-length string.
"""

# ======================================================================
# PROBLEM 1008 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "abcdef"                                          # [Line 79] | ASSIGNMENT: Creates variable 'text' and stores the result of ''abcdef'' in it | DATA TYPE: String - A sequence of characters. Length: 6
middle_index = len(text) // 2                            # [Line 80] | FLOOR DIVISION (//) - Divides two numbers and returns the largest integer less than or equal to the result. Example: 7 // 2 = 3 (not 3.5). This is useful for integer division when you don't want decimal results. | ASSIGNMENT: Creates variable 'middle_index' and stores the result of 'len(text) // 2' in it | BINARY OPERATION: Performs a calculation between two operands
sliced_text = text[middle_index - 1: middle_index + 1]   # [Line 81] | SLICING OPERATION - Extracts a portion of the sequence | ASSIGNMENT: Creates variable 'sliced_text' and stores the result of 'text[middle_index - 1:middle_index + 1]' in it | SUBSCRIPTION: Accesses an element or slice from a sequence using []
print(sliced_text)                                       # [Line 82] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: cd


"""
Problem: 1009
Write a Python program to remove the first three elements from a list using slicing.
"""

# ======================================================================
# PROBLEM 1009 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


numbers = [1, 2, 3, 4, 5, 6]                             # [Line 90] | ASSIGNMENT: Creates variable 'numbers' and stores the result of '[1, 2, 3, 4, 5, 6]' in it | DATA TYPE: List - A mutable ordered collection. Contains 6 elements
sliced_list = numbers[3:]                                # [Line 91] | SLICING OPERATION [3:] - Extracts all elements starting from index 3 to the end.  | ASSIGNMENT: Creates variable 'sliced_list' and stores the result of 'numbers[3:]' in it | SUBSCRIPTION: Accesses an element or slice from a sequence using []
print(sliced_list)                                       # [Line 92] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: [4, 5, 6]


"""
Problem: 1010
Write a Python program to remove the last two elements from a tuple using slicing.
"""

# ======================================================================
# PROBLEM 1010 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


numbers = (10, 20, 30, 40, 50)                           # [Line 100] | ASSIGNMENT: Creates variable 'numbers' and stores the result of '(10, 20, 30, 40, 50)' in it | DATA TYPE: Tuple - An immutable ordered collection. Contains 5 elements
sliced_tuple = numbers[:-2]                              # [Line 101] | SLICING OPERATION [:-2] - Extracts elements from the beginning up to (but not including) index -2.  | ASSIGNMENT: Creates variable 'sliced_tuple' and stores the result of 'numbers[:-2]' in it | SUBSCRIPTION: Accesses an element or slice from a sequence using []
print(sliced_tuple)                                      # [Line 102] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: (10, 20, 30)


"""
Problem: 1011
Write a Python program to slice every alternate element from a list.
"""

# ======================================================================
# PROBLEM 1011 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


numbers = [1, 2, 3, 4, 5, 6, 7, 8]                       # [Line 110] | ASSIGNMENT: Creates variable 'numbers' and stores the result of '[1, 2, 3, 4, 5, 6, 7, 8]' in it | DATA TYPE: List - A mutable ordered collection. Contains 8 elements
sliced_list = numbers[::2]                               # [Line 111] | SLICING OPERATION [::2] - Extracts every 2th element. The step value of 2 means we skip 1 elements between each selected element. No start index means begin from the start (or end if step is negative). No stop index means go to the end (or beginning if step is negative).  | ASSIGNMENT: Creates variable 'sliced_list' and stores the result of 'numbers[::2]' in it | SUBSCRIPTION: Accesses an element or slice from a sequence using []
print(sliced_list)                                       # [Line 112] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: [1, 3, 5, 7]


"""
Problem: 1012
Write a Python program to extract a substring from index 3 to 7 using slicing.
"""

# ======================================================================
# PROBLEM 1012 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "PythonProgramming"                               # [Line 120] | ASSIGNMENT: Creates variable 'text' and stores the result of ''PythonProgramming'' in it | DATA TYPE: String - A sequence of characters. Length: 17
sliced_text = text[3:8]                                  # [Line 121] | SLICING OPERATION [3:8] - Extracts elements from index 3 to 7 (stop is exclusive).  | ASSIGNMENT: Creates variable 'sliced_text' and stores the result of 'text[3:8]' in it | SUBSCRIPTION: Accesses an element or slice from a sequence using []
print(sliced_text)                                       # [Line 122] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: honPr


"""
Problem: 1013
Write a Python program to extract a tuple slice from index 2 to 5.
"""

# ======================================================================
# PROBLEM 1013 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


numbers = (100, 200, 300, 400, 500, 600)                 # [Line 130] | ASSIGNMENT: Creates variable 'numbers' and stores the result of '(100, 200, 300, 400, 500, 600)' in it | DATA TYPE: Tuple - An immutable ordered collection. Contains 6 elements
sliced_tuple = numbers[2:6]                              # [Line 131] | SLICING OPERATION [2:6] - Extracts elements from index 2 to 5 (stop is exclusive).  | ASSIGNMENT: Creates variable 'sliced_tuple' and stores the result of 'numbers[2:6]' in it | SUBSCRIPTION: Accesses an element or slice from a sequence using []
print(sliced_tuple)                                      # [Line 132] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: (300, 400, 500, 600)


"""
Problem: 1014
Write a Python program to check if a string is a palindrome using slicing.
"""

# ======================================================================
# PROBLEM 1014 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def is_palindrome(s):                                    # [Line 140]
    return s == s[::-1]                                  # [Line 141] | SLICING OPERATION [::-1] - This is a reverse slice. The syntax [::-1] means: start at the beginning (no start index), stop at the end (no stop index), and step backwards by 1. This effectively reverses the entire sequence. Example: [1,2,3][::-1] becomes [3,2,1] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

print(is_palindrome("madam"))                            # [Line 143] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: True
print(is_palindrome("hello"))                            # [Line 144] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: False


"""
Problem: 1015
Write a Python program to extract the last three characters of a string using slicing.
"""

# ======================================================================
# PROBLEM 1015 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "Programming"                                     # [Line 152] | ASSIGNMENT: Creates variable 'text' and stores the result of ''Programming'' in it | DATA TYPE: String - A sequence of characters. Length: 11
sliced_text = text[-3:]                                  # [Line 153] | SLICING OPERATION [-3:] - Extracts from -3 positions from the end to the end of the sequence.  | ASSIGNMENT: Creates variable 'sliced_text' and stores the result of 'text[-3:]' in it | SUBSCRIPTION: Accesses an element or slice from a sequence using []
print(sliced_text)                                       # [Line 154] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: ing


"""
Problem: 1016
Write a Python program to extract the first five elements of a list using slicing.
"""

# ======================================================================
# PROBLEM 1016 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


numbers = [10, 20, 30, 40, 50, 60, 70]                   # [Line 162] | ASSIGNMENT: Creates variable 'numbers' and stores the result of '[10, 20, 30, 40, 50, 60, 70]' in it | DATA TYPE: List - A mutable ordered collection. Contains 7 elements
sliced_list = numbers[:5]                                # [Line 163] | SLICING OPERATION [:5] - Extracts elements from the beginning up to (but not including) index 5.  | ASSIGNMENT: Creates variable 'sliced_list' and stores the result of 'numbers[:5]' in it | SUBSCRIPTION: Accesses an element or slice from a sequence using []
print(sliced_list)                                       # [Line 164] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: [10, 20, 30, 40, 50]


"""
Problem: 1017
Write a Python program to extract all but the last three elements from a tuple using slicing.
"""

# ======================================================================
# PROBLEM 1017 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


numbers = (5, 10, 15, 20, 25, 30, 35)                    # [Line 172] | ASSIGNMENT: Creates variable 'numbers' and stores the result of '(5, 10, 15, 20, 25, 30, 35)' in it | DATA TYPE: Tuple - An immutable ordered collection. Contains 7 elements
sliced_tuple = numbers[:-3]                              # [Line 173] | SLICING OPERATION [:-3] - Extracts elements from the beginning up to (but not including) index -3.  | ASSIGNMENT: Creates variable 'sliced_tuple' and stores the result of 'numbers[:-3]' in it | SUBSCRIPTION: Accesses an element or slice from a sequence using []
print(sliced_tuple)                                      # [Line 174] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: (5, 10, 15, 20)


"""
Problem: 1018
Write a Python program to extract a string without its first and last two characters.
"""

# ======================================================================
# PROBLEM 1018 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "HelloWorld"                                      # [Line 182] | ASSIGNMENT: Creates variable 'text' and stores the result of ''HelloWorld'' in it | DATA TYPE: String - A sequence of characters. Length: 10
sliced_text = text[2:-2]                                 # [Line 183] | SLICING OPERATION [2:-2] - Extracts elements from index 2 to -3 (stop is exclusive).  | ASSIGNMENT: Creates variable 'sliced_text' and stores the result of 'text[2:-2]' in it | SUBSCRIPTION: Accesses an element or slice from a sequence using []
print(sliced_text)                                       # [Line 184] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: lloWor

"""
Problem: 1019
Write a Python program to create a list of squares of numbers from 1 to 10 using list comprehension.
"""

# ======================================================================
# PROBLEM 1019 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


squares = [x ** 2 for x in range(1, 11)]                 # [Line 191] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2. | ASSIGNMENT: Creates variable 'squares' and stores the result of '[x ** 2 for x in range(1, 11)]' in it
print(squares)                                           # [Line 192] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


"""
Problem: 1020
Write a Python program to create a list of even numbers from 1 to 20 using list comprehension.
"""

# ======================================================================
# PROBLEM 1020 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


evens = [x for x in range(1, 21) if x % 2 == 0]          # [Line 200] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1). | ASSIGNMENT: Creates variable 'evens' and stores the result of '[x for x in range(1, 21) if x % 2 == 0]' in it
print(evens)                                             # [Line 201] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


"""
Problem: 1021
Write a Python program to create a list of numbers from 1 to 50 that are divisible by 5 using list comprehension.
"""

# ======================================================================
# PROBLEM 1021 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


div_by_5 = [x for x in range(1, 51) if x % 5 == 0]       # [Line 209] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1). | ASSIGNMENT: Creates variable 'div_by_5' and stores the result of '[x for x in range(1, 51) if x % 5 == 0]' in it
print(div_by_5)                                          # [Line 210] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]


"""
Problem: 1022
Write a Python program to create a list of the first letter of each word in a given sentence using list comprehension.
"""

# ======================================================================
# PROBLEM 1022 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


sentence = "Python is a powerful programming language"   # [Line 218] | ASSIGNMENT: Creates variable 'sentence' and stores the result of ''Python is a powerful programming language'' in it | DATA TYPE: String - A sequence of characters. Length: 41
first_letters = [word[0] for word in sentence.split()]   # [Line 219] | ASSIGNMENT: Creates variable 'first_letters' and stores the result of '[word[0] for word in sentence.split()]' in it
print(first_letters)                                     # [Line 220] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: ['P', 'i', 'a', 'p', 'p', 'l']


"""
Problem: 1023
Write a Python program to create a list of words with more than three letters from a sentence using list comprehension.
"""

# ======================================================================
# PROBLEM 1023 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


sentence = "The sun is bright today"                     # [Line 228] | ASSIGNMENT: Creates variable 'sentence' and stores the result of ''The sun is bright today'' in it | DATA TYPE: String - A sequence of characters. Length: 23
long_words = [word for word in sentence.split() if len(word) > 3]  # [Line 229] | ASSIGNMENT: Creates variable 'long_words' and stores the result of '[word for word in sentence.split() if len(word) > 3]' in it
print(long_words)                                        # [Line 230] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: ['bright', 'today']


"""
Problem: 1024
Write a Python program to generate a list of tuples containing a number and its square for numbers from 1 to 10. List comprehension.
"""

# ======================================================================
# PROBLEM 1024 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


squares_tuples = [(x, x**2) for x in range(1, 11)]       # [Line 238] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2. | ASSIGNMENT: Creates variable 'squares_tuples' and stores the result of '[(x, x ** 2) for x in range(1, 11)]' in it
print(squares_tuples)                                    # [Line 239] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: [(1, 1), (2, 4), ..., (10, 100)]


"""
Problem: 1025
Write a Python program to create a new list where every element from an existing list is doubled. List comprehension.
"""

# ======================================================================
# PROBLEM 1025 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


numbers = [3, 5, 7, 9]                                   # [Line 247] | ASSIGNMENT: Creates variable 'numbers' and stores the result of '[3, 5, 7, 9]' in it | DATA TYPE: List - A mutable ordered collection. Contains 4 elements
doubled = [x * 2 for x in numbers]                       # [Line 248] | ASSIGNMENT: Creates variable 'doubled' and stores the result of '[x * 2 for x in numbers]' in it
print(doubled)                                           # [Line 249] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: [6, 10, 14, 18]


"""
Problem: 1026
Write a Python program to create a list of numbers from 1 to 100 that are either divisible by 3 or 7. List comprehension.
"""

# ======================================================================
# PROBLEM 1026 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


div_by_3_or_7 = [x for x in range(1, 101) if x % 3 == 0 or x % 7 == 0]  # [Line 257] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1). | ASSIGNMENT: Creates variable 'div_by_3_or_7' and stores the result of '[x for x in range(1, 101) if x % 3 == 0 or x % 7 == 0]' in it
print(div_by_3_or_7)                                     # [Line 258] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user


"""
Problem: 1027
Write a Python program to convert a list of strings to uppercase using list comprehension.
"""

# ======================================================================
# PROBLEM 1027 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


words = ["hello", "world", "python"]                     # [Line 266] | ASSIGNMENT: Creates variable 'words' and stores the result of '['hello', 'world', 'python']' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
upper_words = [word.upper() for word in words]           # [Line 267] | ASSIGNMENT: Creates variable 'upper_words' and stores the result of '[word.upper() for word in words]' in it
print(upper_words)                                       # [Line 268] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: ['HELLO', 'WORLD', 'PYTHON']


"""
Problem: 1028
Write a Python program to flatten a nested list using list comprehension.
"""

# ======================================================================
# PROBLEM 1028 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]          # [Line 276] | ASSIGNMENT: Creates variable 'nested_list' and stores the result of '[[1, 2, 3], [4, 5, 6], [7, 8, 9]]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
flattened = [num for sublist in nested_list for num in sublist]  # [Line 277] | ASSIGNMENT: Creates variable 'flattened' and stores the result of '[num for sublist in nested_list for num in sublist]' in it
print(flattened)                                         # [Line 278] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9]


"""
Problem: 1029
Write a Python program to create a list of vowels from a given string using list comprehension.
"""

# ======================================================================
# PROBLEM 1029 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "List Comprehension is Powerful"                  # [Line 286] | ASSIGNMENT: Creates variable 'text' and stores the result of ''List Comprehension is Powerful'' in it | DATA TYPE: String - A sequence of characters. Length: 30
vowels = [char for char in text if char.lower() in "aeiou"]  # [Line 287] | ASSIGNMENT: Creates variable 'vowels' and stores the result of '[char for char in text if char.lower() in 'aeiou']' in it
print(vowels)                                            # [Line 288] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: ['i', 'o', 'e', 'e', 'i', 'o', 'i', 'o', 'e']


"""
Problem: 1030
Write a Python program to extract only numeric values from a mixed list. List comprehension.
"""

# ======================================================================
# PROBLEM 1030 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


mixed_list = [10, "apple", 15.5, "banana", 30, "42"]     # [Line 296] | ASSIGNMENT: Creates variable 'mixed_list' and stores the result of '[10, 'apple', 15.5, 'banana', 30, '42']' in it | DATA TYPE: List - A mutable ordered collection. Contains 6 elements
numbers = [x for x in mixed_list if isinstance(x, (int, float))]  # [Line 297] | ASSIGNMENT: Creates variable 'numbers' and stores the result of '[x for x in mixed_list if isinstance(x, (int, float))]' in it
print(numbers)                                           # [Line 298] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: [10, 15.5, 30]


"""
Problem: 1031
Write a Python program to generate a list of first 10 Fibonacci numbers using list comprehension.
"""

# ======================================================================
# PROBLEM 1031 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


fib = [0, 1]                                             # [Line 306] | ASSIGNMENT: Creates variable 'fib' and stores the result of '[0, 1]' in it | DATA TYPE: List - A mutable ordered collection. Contains 2 elements
[fib.append(fib[-1] + fib[-2]) for _ in range(8)]        # [Line 307] | LIST COMPREHENSION - A concise way to create lists. The expression 'fib.append(fib[-1] + fib[-2])' is evaluated for each iteration. The variable '_' takes each value from 'range(8)]' during iteration. 
print(fib)                                               # [Line 308] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


"""
Problem: 1032
Write a Python program to create a list of prime numbers up to 50 using list comprehension.
"""

# ======================================================================
# PROBLEM 1032 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


primes = [x for x in range(2, 51) if all(x % y != 0 for y in range(2, int(x**0.5) + 1))]  # [Line 316] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1). | ASSIGNMENT: Creates variable 'primes' and stores the result of '[x for x in range(2, 51) if all((x % y != 0 for y in range(2, int(x ** 0.5) + 1)))]' in it
print(primes)                                            # [Line 317] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user


"""
Problem: 1033
Write a Python program to generate a list of all words in a sentence that end with a vowel. List comprehension.
"""

# ======================================================================
# PROBLEM 1033 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


sentence = "The apple is on the tree"                    # [Line 325] | ASSIGNMENT: Creates variable 'sentence' and stores the result of ''The apple is on the tree'' in it | DATA TYPE: String - A sequence of characters. Length: 24
vowel_ending_words = [word for word in sentence.split() if word[-1].lower() in "aeiou"]  # [Line 326] | ASSIGNMENT: Creates variable 'vowel_ending_words' and stores the result of '[word for word in sentence.split() if word[-1].lower() in 'aeiou']' in it
print(vowel_ending_words)                                # [Line 327] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: ['The', 'apple', 'is', 'tree']


"""
Problem: 1034
Write a Python program to create a list of lowercase characters from a given string. List comprehension.
"""

# ======================================================================
# PROBLEM 1034 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "Python List Comprehension"                       # [Line 335] | ASSIGNMENT: Creates variable 'text' and stores the result of ''Python List Comprehension'' in it | DATA TYPE: String - A sequence of characters. Length: 25
lower_chars = [char for char in text if char.islower()]  # [Line 336] | ASSIGNMENT: Creates variable 'lower_chars' and stores the result of '[char for char in text if char.islower()]' in it
print(lower_chars)                                       # [Line 337] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: ['y', 't', 'h', 'o', 'n', 'i', 's', 't', 'o', 'm', 'p', 'r', 'e', 'h', 'e', 'n', 's', 'i', 'o', 'n']


"""
Problem: 1035
Write a Python program to create a list of words with their lengths from a given sentence. List comprehension.
"""

# ======================================================================
# PROBLEM 1035 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


sentence = "List comprehension makes Python concise"     # [Line 345] | ASSIGNMENT: Creates variable 'sentence' and stores the result of ''List comprehension makes Python concise'' in it | DATA TYPE: String - A sequence of characters. Length: 39
word_lengths = [(word, len(word)) for word in sentence.split()]  # [Line 346] | ASSIGNMENT: Creates variable 'word_lengths' and stores the result of '[(word, len(word)) for word in sentence.split()]' in it
print(word_lengths)                                      # [Line 347] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: [('List', 4), ('comprehension', 13), ('makes', 5), ('Python', 6), ('concise', 7)]


"""
Problem: 1036
Write a Python program to remove duplicates from a list using list comprehension.
"""

# ======================================================================
# PROBLEM 1036 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


numbers = [1, 2, 2, 3, 4, 4, 5]                          # [Line 355] | ASSIGNMENT: Creates variable 'numbers' and stores the result of '[1, 2, 2, 3, 4, 4, 5]' in it | DATA TYPE: List - A mutable ordered collection. Contains 7 elements
unique_numbers = list(dict.fromkeys(numbers))            # [Line 356] | ASSIGNMENT: Creates variable 'unique_numbers' and stores the result of 'list(dict.fromkeys(numbers))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(unique_numbers)                                    # [Line 357] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: [1, 2, 3, 4, 5]


"""
Problem: 1037
Write a Python program to filter words containing the letter 'p' from a given list. List comprehension.
"""

# ======================================================================
# PROBLEM 1037 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


words = ["apple", "banana", "grape", "cherry", "peach"]  # [Line 365] | ASSIGNMENT: Creates variable 'words' and stores the result of '['apple', 'banana', 'grape', 'cherry', 'peach']' in it | DATA TYPE: List - A mutable ordered collection. Contains 5 elements
filtered_words = [word for word in words if "p" in word]  # [Line 366] | ASSIGNMENT: Creates variable 'filtered_words' and stores the result of '[word for word in words if 'p' in word]' in it
print(filtered_words)                                    # [Line 367] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: ['apple', 'grape', 'peach']

"""
Problem: 1038
Write a Python recursive function to calculate the factorial of a given number.
"""

# ======================================================================
# PROBLEM 1038 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def factorial(n):                                        # [Line 374]
    return 1 if n == 0 else n * factorial(n - 1)         # [Line 375] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

print(factorial(5))                                      # [Line 377] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: 120


"""
Problem: 1039
Write a Python recursive function to calculate the sum of all numbers from 1 to n.
"""

# ======================================================================
# PROBLEM 1039 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def sum_n(n):                                            # [Line 385]
    return n if n == 1 else n + sum_n(n - 1)             # [Line 386] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

print(sum_n(10))                                         # [Line 388] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: 55


"""
Problem: 1040
Write a Python recursive function to compute the nth Fibonacci number.
"""

# ======================================================================
# PROBLEM 1040 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def fibonacci(n):                                        # [Line 396]
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)  # [Line 397]

print(fibonacci(6))                                      # [Line 399] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: 8


"""
Problem: 1041
Write a Python recursive function to reverse a string.
"""

# ======================================================================
# PROBLEM 1041 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def reverse_string(s):                                   # [Line 407]
    return s if len(s) == 0 else s[-1] + reverse_string(s[:-1])  # [Line 408] | SLICING OPERATION [:-1] - Extracts elements from the beginning up to (but not including) index -1.  | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

print(reverse_string("hello"))                           # [Line 410] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: olleh


"""
Problem: 1042
Write a Python recursive function to count the number of digits in a given number.
"""

# ======================================================================
# PROBLEM 1042 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def count_digits(n):                                     # [Line 418]
    return 1 if n < 10 else 1 + count_digits(n // 10)    # [Line 419] | FLOOR DIVISION (//) - Divides two numbers and returns the largest integer less than or equal to the result. Example: 7 // 2 = 3 (not 3.5). This is useful for integer division when you don't want decimal results.

print(count_digits(12345))                               # [Line 421] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: 5


"""
Problem: 1043
Write a Python recursive function to find the greatest common divisor (GCD) of two numbers.
"""

# ======================================================================
# PROBLEM 1043 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def gcd(a, b):                                           # [Line 429]
    return a if b == 0 else gcd(b, a % b)                # [Line 430] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

print(gcd(48, 18))                                       # [Line 432] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: 6


"""
Problem: 1044
Write a Python recursive function to find the sum of elements in a list.
"""

# ======================================================================
# PROBLEM 1044 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def list_sum(lst):                                       # [Line 440]
    return 0 if not lst else lst[0] + list_sum(lst[1:])  # [Line 441] | SLICING OPERATION [1:] - Extracts all elements starting from index 1 to the end. 

print(list_sum([1, 2, 3, 4, 5]))                         # [Line 443] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: 15


"""
Problem: 1045
Write a Python recursive function to check if a number is a palindrome.
"""

# ======================================================================
# PROBLEM 1045 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def is_palindrome(n, temp=None):                         # [Line 451]
    if temp is None:                                     # [Line 452]
        temp = str(n)                                    # [Line 453]
    return True if len(temp) <= 1 else temp[0] == temp[-1] and is_palindrome(n, temp[1:-1])  # [Line 454] | SLICING OPERATION [1:-1] - Extracts elements from index 1 to -2 (stop is exclusive).  | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

print(is_palindrome(121))                                # [Line 456] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: True
print(is_palindrome(123))                                # [Line 457] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: False


"""
Problem: 1046
Write a Python recursive function to find the power of a number.
"""

# ======================================================================
# PROBLEM 1046 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def power(x, n):                                         # [Line 465]
    return 1 if n == 0 else x * power(x, n - 1)          # [Line 466] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

print(power(2, 3))                                       # [Line 468] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: 8


"""
Problem: 1047
Write a Python recursive function to compute the product of two numbers.
"""

# ======================================================================
# PROBLEM 1047 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def multiply(a, b):                                      # [Line 476]
    return 0 if b == 0 else a + multiply(a, b - 1)       # [Line 477] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

print(multiply(5, 4))                                    # [Line 479] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: 20


"""
Problem: 1048
Write a Python recursive function to print numbers from 1 to n.
"""

# ======================================================================
# PROBLEM 1048 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def print_numbers(n):                                    # [Line 487]
    if n > 0:                                            # [Line 488]
        print_numbers(n - 1)                             # [Line 489]
        print(n)                                         # [Line 490]

print_numbers(5)                                         # [Line 492] | FUNCTION CALL: Executes the function 'print_numbers' | ARGUMENTS: Passes 1 argument(s) to the function
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


def print_reverse(n):                                    # [Line 506]
    if n > 0:                                            # [Line 507]
        print(n)                                         # [Line 508]
        print_reverse(n - 1)                             # [Line 509]

print_reverse(5)                                         # [Line 511] | FUNCTION CALL: Executes the function 'print_reverse' | ARGUMENTS: Passes 1 argument(s) to the function
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


def is_sorted(lst):                                      # [Line 525]
    return True if len(lst) <= 1 else lst[0] <= lst[1] and is_sorted(lst[1:])  # [Line 526] | SLICING OPERATION [1:] - Extracts all elements starting from index 1 to the end. 

print(is_sorted([1, 2, 3, 4, 5]))                        # [Line 528] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: True
print(is_sorted([5, 3, 1]))                              # [Line 529] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: False


"""
Problem: 1051
Write a Python recursive function to count the occurrences of a character in a string.
"""

# ======================================================================
# PROBLEM 1051 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def char_count(s, c):                                    # [Line 537]
    return 0 if not s else (1 if s[0] == c else 0) + char_count(s[1:], c)  # [Line 538] | SLICING OPERATION [1:] - Extracts all elements starting from index 1 to the end.  | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

print(char_count("banana", "a"))                         # [Line 540] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: 3


"""
Problem: 1052
Write a Python recursive function to generate all binary strings of length n.
"""

# ======================================================================
# PROBLEM 1052 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def binary_strings(n, s=""):                             # [Line 548]
    if n == 0:                                           # [Line 549] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).
        print(s)                                         # [Line 550]
    else:                                                # [Line 551]
        binary_strings(n - 1, s + "0")                   # [Line 552]
        binary_strings(n - 1, s + "1")                   # [Line 553]

binary_strings(3)                                        # [Line 555] | FUNCTION CALL: Executes the function 'binary_strings' | ARGUMENTS: Passes 1 argument(s) to the function
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


def sum_of_digits(n):                                    # [Line 572]
    if n == 0:                                           # [Line 573] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).
        return 0                                         # [Line 574]
    # Recursive case: add the last digit to the sum of the remaining digits
    else:                                                # [Line 576]
        return n % 10 + sum_of_digits(n // 10)           # [Line 577] | FLOOR DIVISION (//) - Divides two numbers and returns the largest integer less than or equal to the result. Example: 7 // 2 = 3 (not 3.5). This is useful for integer division when you don't want decimal results.

string = 1244                                            # [Line 579] | ASSIGNMENT: Creates variable 'string' and stores the result of '1244' in it | DATA TYPE: Integer - A whole number: 1244
print(sum_of_digits(string))                             # [Line 580] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Output: 11

def sum_of_digits(n):                                    # [Line 582]
    return n if n < 10 else (n % 10) + sum_of_digits(n // 10)  # [Line 583] | FLOOR DIVISION (//) - Divides two numbers and returns the largest integer less than or equal to the result. Example: 7 // 2 = 3 (not 3.5). This is useful for integer division when you don't want decimal results.

print(sum_of_digits(1234))                               # [Line 585] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: 10


"""
Problem: 1054
Write a Python recursive function to calculate the nth triangular number.
"""

# ======================================================================
# PROBLEM 1054 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def triangular_number(n):                                # [Line 593]
    return 0 if n == 0 else n + triangular_number(n - 1)  # [Line 594] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

print(triangular_number(5))                              # [Line 596] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: 15


"""
Problem: 1055
Write a Python recursive function to remove duplicates from a string.
"""

# ======================================================================
# PROBLEM 1055 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def remove_duplicates(s, seen=""):                       # [Line 604]
    return "" if not s else (remove_duplicates(s[1:], seen) if s[0] in seen else s[0] + remove_duplicates(s[1:], seen + s[0]))  # [Line 605] | SLICING OPERATION [1:] - Extracts all elements starting from index 1 to the end. 

print(remove_duplicates("banana"))                       # [Line 607] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: ban


"""
Problem: 1056
Write a Python recursive function to generate all permutations of a given string.
"""

# ======================================================================
# PROBLEM 1056 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def permutations(s, prefix=""):                          # [Line 615]
    if not s:                                            # [Line 616]
        print(prefix)                                    # [Line 617]
    else:                                                # [Line 618]
        for i in range(len(s)):                          # [Line 619]
            permutations(s[:i] + s[i+1:], prefix + s[i])  # [Line 620] | SLICING OPERATION - Extracts a portion of the sequence

permutations("abc")                                      # [Line 622] | FUNCTION CALL: Executes the function 'permutations' | ARGUMENTS: Passes 1 argument(s) to the function
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


def longest_string(words):                               # [Line 636]
    return max(words, key=lambda word: len(word))        # [Line 637]

result = longest_string(["apple", "banana", "cherry"])   # [Line 639] | ASSIGNMENT: Creates variable 'result' and stores the result of 'longest_string(['apple', 'banana', 'cherry'])' in it | FUNCTION CALL: Calls 'longest_string()' and stores its return value
print(result)                                            # [Line 640] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1058
Write a Python program to check if a number is even using a lambda function.
"""

# ======================================================================
# PROBLEM 1058 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


is_even = lambda x: x % 2 == 0                           # [Line 647] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1). | ASSIGNMENT: Creates variable 'is_even' and stores the result of 'lambda x: x % 2 == 0' in it

result = is_even(4)                                      # [Line 649] | ASSIGNMENT: Creates variable 'result' and stores the result of 'is_even(4)' in it | FUNCTION CALL: Calls 'is_even()' and stores its return value
print(result)                                            # [Line 650] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1059
Write a Python program to calculate the square root of all elements in a list using a lambda function.
"""

# ======================================================================
# PROBLEM 1059 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import math                                              # [Line 657]

def square_roots(numbers):                               # [Line 659]
    return list(map(lambda x: math.sqrt(x), numbers))    # [Line 660]

result = square_roots([4, 9, 16])                        # [Line 662] | ASSIGNMENT: Creates variable 'result' and stores the result of 'square_roots([4, 9, 16])' in it | FUNCTION CALL: Calls 'square_roots()' and stores its return value
print(result)                                            # [Line 663] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1060
Write a Python program to check if a string contains any digits using a lambda function.
"""

# ======================================================================
# PROBLEM 1060 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


contains_digits = lambda s: any(map(str.isdigit, s))     # [Line 670] | ASSIGNMENT: Creates variable 'contains_digits' and stores the result of 'lambda s: any(map(str.isdigit, s))' in it

result = contains_digits("hello123")                     # [Line 672] | ASSIGNMENT: Creates variable 'result' and stores the result of 'contains_digits('hello123')' in it | FUNCTION CALL: Calls 'contains_digits()' and stores its return value
print(result)                                            # [Line 673] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1061
Write a Python program to sort a list of tuples based on the first element in descending order using a lambda expression.
"""

# ======================================================================
# PROBLEM 1061 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def sort_by_first_element_desc(tuples):                  # [Line 680]
    return sorted(tuples, key=lambda x: x[0], reverse=True)  # [Line 681] | SLICING OPERATION - Extracts a portion of the sequence

result = sort_by_first_element_desc([(3, "apple"), (1, "banana"), (2, "cherry")])  # [Line 683] | ASSIGNMENT: Creates variable 'result' and stores the result of 'sort_by_first_element_desc([(3, 'apple'), (1, 'banana'), (2, 'cherry')])' in it | FUNCTION CALL: Calls 'sort_by_first_element_desc()' and stores its return value
print(result)                                            # [Line 684] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1062
Write a Python program to filter out words that are shorter than a given length using the `filter()` function with a lambda expression.
"""

# ======================================================================
# PROBLEM 1062 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def filter_short_words(words, length):                   # [Line 691]
    return list(filter(lambda word: len(word) >= length, words))  # [Line 692]

result = filter_short_words(["apple", "banana", "cherry", "date"], 6)  # [Line 694] | ASSIGNMENT: Creates variable 'result' and stores the result of 'filter_short_words(['apple', 'banana', 'cherry', 'date'], 6)' in it | FUNCTION CALL: Calls 'filter_short_words()' and stores its return value
print(result)                                            # [Line 695] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1063
Write a Python program to double all elements in a list using a lambda function.
"""

# ======================================================================
# PROBLEM 1063 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def double_elements(numbers):                            # [Line 702]
    return list(map(lambda x: x * 2, numbers))           # [Line 703]

result = double_elements([1, 2, 3, 4])                   # [Line 705] | ASSIGNMENT: Creates variable 'result' and stores the result of 'double_elements([1, 2, 3, 4])' in it | FUNCTION CALL: Calls 'double_elements()' and stores its return value
print(result)                                            # [Line 706] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1064
Write a Python program to check if a number is divisible by 3 using a lambda function.
"""

# ======================================================================
# PROBLEM 1064 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


is_divisible_by_3 = lambda x: x % 3 == 0                 # [Line 713] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1). | ASSIGNMENT: Creates variable 'is_divisible_by_3' and stores the result of 'lambda x: x % 3 == 0' in it

result = is_divisible_by_3(9)                            # [Line 715] | ASSIGNMENT: Creates variable 'result' and stores the result of 'is_divisible_by_3(9)' in it | FUNCTION CALL: Calls 'is_divisible_by_3()' and stores its return value
print(result)                                            # [Line 716] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1065
Write a Python program to find the second largest number in a list using a lambda function.
"""

# ======================================================================
# PROBLEM 1065 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


second_largest = lambda numbers: sorted(set(numbers))[-2]  # [Line 723] | SLICING OPERATION - Extracts a portion of the sequence | ASSIGNMENT: Creates variable 'second_largest' and stores the result of 'lambda numbers: sorted(set(numbers))[-2]' in it

result = second_largest([10, 20, 30, 40, 50])            # [Line 725] | ASSIGNMENT: Creates variable 'result' and stores the result of 'second_largest([10, 20, 30, 40, 50])' in it | FUNCTION CALL: Calls 'second_largest()' and stores its return value
print(result)                                            # [Line 726] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1066
Write a Python program to map a list of numbers into their cubes using a lambda function.
"""

# ======================================================================
# PROBLEM 1066 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def cube_elements(numbers):                              # [Line 733]
    return list(map(lambda x: x ** 3, numbers))          # [Line 734] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.

result = cube_elements([1, 2, 3, 4])                     # [Line 736] | ASSIGNMENT: Creates variable 'result' and stores the result of 'cube_elements([1, 2, 3, 4])' in it | FUNCTION CALL: Calls 'cube_elements()' and stores its return value
print(result)                                            # [Line 737] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1067
Write a Python program to sort a list of words by their lengths using the `sorted()` function with a lambda expression.
"""

# ======================================================================
# PROBLEM 1067 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def sort_by_length(words):                               # [Line 744]
    return sorted(words, key=lambda word: len(word))     # [Line 745]

result = sort_by_length(["apple", "banana", "kiwi", "cherry"])  # [Line 747] | ASSIGNMENT: Creates variable 'result' and stores the result of 'sort_by_length(['apple', 'banana', 'kiwi', 'cherry'])' in it | FUNCTION CALL: Calls 'sort_by_length()' and stores its return value
print(result)                                            # [Line 748] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1068
Write a Python program to check if a number is odd using a lambda function.
"""

# ======================================================================
# PROBLEM 1068 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


is_odd = lambda x: x % 2 != 0                            # [Line 755] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1). | ASSIGNMENT: Creates variable 'is_odd' and stores the result of 'lambda x: x % 2 != 0' in it

result = is_odd(5)                                       # [Line 757] | ASSIGNMENT: Creates variable 'result' and stores the result of 'is_odd(5)' in it | FUNCTION CALL: Calls 'is_odd()' and stores its return value
print(result)                                            # [Line 758] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1069
Write a Python program to find the sum of all elements in a list using the `reduce()` function with a lambda expression.
"""

# ======================================================================
# PROBLEM 1069 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from functools import reduce                             # [Line 765]

def sum_of_elements(numbers):                            # [Line 767]
    return reduce(lambda x, y: x + y, numbers)           # [Line 768]

result = sum_of_elements([1, 2, 3, 4])                   # [Line 770] | ASSIGNMENT: Creates variable 'result' and stores the result of 'sum_of_elements([1, 2, 3, 4])' in it | FUNCTION CALL: Calls 'sum_of_elements()' and stores its return value
print(result)                                            # [Line 771] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1070
Write a Python program to check if a string ends with a vowel using a lambda function.
"""

# ======================================================================
# PROBLEM 1070 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


ends_with_vowel = lambda s: s[-1].lower() in 'aeiou'     # [Line 778] | SLICING OPERATION - Extracts a portion of the sequence | ASSIGNMENT: Creates variable 'ends_with_vowel' and stores the result of 'lambda s: s[-1].lower() in 'aeiou'' in it

result = ends_with_vowel("hello")                        # [Line 780] | ASSIGNMENT: Creates variable 'result' and stores the result of 'ends_with_vowel('hello')' in it | FUNCTION CALL: Calls 'ends_with_vowel()' and stores its return value
print(result)                                            # [Line 781] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

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
numbers = [12, 45, 7, 23, 56, 89, 34]                    # [Line 789] | ASSIGNMENT: Creates variable 'numbers' and stores the result of '[12, 45, 7, 23, 56, 89, 34]' in it | DATA TYPE: List - A mutable ordered collection. Contains 7 elements

# Use the min() function with a lambda expression to find the smallest number
smallest_number = min(numbers, key=lambda x: x)          # [Line 792] | ASSIGNMENT: Creates variable 'smallest_number' and stores the result of 'min(numbers, key=lambda x: x)' in it | FUNCTION CALL: Calls 'min()' and stores its return value

# Print the result
print("The smallest number in the list is:", smallest_number)  # [Line 795] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1072
Write a Python program to check if a string contains only alphabetic characters using a lambda function.
"""

# ======================================================================
# PROBLEM 1072 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


is_alpha = lambda s: s.isalpha()                         # [Line 802] | ASSIGNMENT: Creates variable 'is_alpha' and stores the result of 'lambda s: s.isalpha()' in it

result = is_alpha("hello")                               # [Line 804] | ASSIGNMENT: Creates variable 'result' and stores the result of 'is_alpha('hello')' in it | FUNCTION CALL: Calls 'is_alpha()' and stores its return value
print(result)                                            # [Line 805] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1073
Write a Python program to convert all integers in a list to strings using a lambda function.
"""

# ======================================================================
# PROBLEM 1073 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def convert_to_strings(numbers):                         # [Line 812]
    return list(map(lambda x: str(x), numbers))          # [Line 813]

result = convert_to_strings([1, 2, 3, 4])                # [Line 815] | ASSIGNMENT: Creates variable 'result' and stores the result of 'convert_to_strings([1, 2, 3, 4])' in it | FUNCTION CALL: Calls 'convert_to_strings()' and stores its return value
print(result)                                            # [Line 816] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1074
Write a Python program to find the sum of all even numbers in a list using a lambda expression.
"""

# ======================================================================
# PROBLEM 1074 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def sum_of_even(numbers):                                # [Line 823]
    return sum(filter(lambda x: x % 2 == 0, numbers))    # [Line 824] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = sum_of_even([1, 2, 3, 4, 5, 6])                 # [Line 826] | ASSIGNMENT: Creates variable 'result' and stores the result of 'sum_of_even([1, 2, 3, 4, 5, 6])' in it | FUNCTION CALL: Calls 'sum_of_even()' and stores its return value
print(result)                                            # [Line 827] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1075
Write a Python program to remove all whitespace from a string using a lambda function.
"""

# ======================================================================
# PROBLEM 1075 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


string = "i'm going for a walk"                          # [Line 834] | ASSIGNMENT: Creates variable 'string' and stores the result of '"i'm going for a walk"' in it | DATA TYPE: String - A sequence of characters. Length: 20
result = lambda char: char.replace(" ", "")              # [Line 835] | ASSIGNMENT: Creates variable 'result' and stores the result of 'lambda char: char.replace(' ', '')' in it

result(string)                                           # [Line 837] | FUNCTION CALL: Executes the function 'result' | ARGUMENTS: Passes 1 argument(s) to the function

remove_whitespace = lambda s: ''.join(s.split())         # [Line 839] | ASSIGNMENT: Creates variable 'remove_whitespace' and stores the result of 'lambda s: ''.join(s.split())' in it

result = remove_whitespace("hello world")                # [Line 841] | ASSIGNMENT: Creates variable 'result' and stores the result of 'remove_whitespace('hello world')' in it | FUNCTION CALL: Calls 'remove_whitespace()' and stores its return value
print(result)                                            # [Line 842] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1076
Write a Python program to count the number of even numbers in a list using a lambda function.
"""

# ======================================================================
# PROBLEM 1076 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


count_even = lambda numbers: len(list(filter(lambda x: x % 2 == 0, numbers)))  # [Line 849] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1). | ASSIGNMENT: Creates variable 'count_even' and stores the result of 'lambda numbers: len(list(filter(lambda x: x % 2 == 0, numbers)))' in it

result = count_even([1, 2, 3, 4, 5, 6])                  # [Line 851] | ASSIGNMENT: Creates variable 'result' and stores the result of 'count_even([1, 2, 3, 4, 5, 6])' in it | FUNCTION CALL: Calls 'count_even()' and stores its return value
print(result)                                            # [Line 852] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1077
Write a Python program to find the product of all odd numbers in a list using a lambda function.
"""

# ======================================================================
# PROBLEM 1077 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from functools import reduce                             # [Line 859]

product_of_odds = lambda numbers: reduce(lambda x, y: x * y, filter(lambda x: x % 2 != 0, numbers))  # [Line 861] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1). | ASSIGNMENT: Creates variable 'product_of_odds' and stores the result of 'lambda numbers: reduce(lambda x, y: x * y, filter(lambda x: x % 2 != 0, numbers))' in it

result = product_of_odds([1, 2, 3, 4, 5])                # [Line 863] | ASSIGNMENT: Creates variable 'result' and stores the result of 'product_of_odds([1, 2, 3, 4, 5])' in it | FUNCTION CALL: Calls 'product_of_odds()' and stores its return value
print(result)                                            # [Line 864] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1078
Write a Python program to check if a number is prime using a lambda function.
"""

# ======================================================================
# PROBLEM 1078 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


is_prime = lambda n: all(n % i != 0 for i in range(2, int(n ** 0.5) + 1)) if n > 1 else False  # [Line 871] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1). | ASSIGNMENT: Creates variable 'is_prime' and stores the result of 'lambda n: all((n % i != 0 for i in range(2, int(n ** 0.5) + 1))) if n > 1 else False' in it

result = is_prime(7)                                     # [Line 873] | ASSIGNMENT: Creates variable 'result' and stores the result of 'is_prime(7)' in it | FUNCTION CALL: Calls 'is_prime()' and stores its return value
print(result)                                            # [Line 874] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1079
Write a Python program to create a list of tuples (number, square root) for each number in a given list using a lambda function.
"""

# ======================================================================
# PROBLEM 1079 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import math                                              # [Line 881]

def create_square_root_tuples(numbers):                  # [Line 883]
    return list(map(lambda x: (x, math.sqrt(x)), numbers))  # [Line 884]

result = create_square_root_tuples([4, 9, 16])           # [Line 886] | ASSIGNMENT: Creates variable 'result' and stores the result of 'create_square_root_tuples([4, 9, 16])' in it | FUNCTION CALL: Calls 'create_square_root_tuples()' and stores its return value
print(result)                                            # [Line 887] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1080
Write a Python program to check if a string contains any uppercase letters using a lambda function.
"""

# ======================================================================
# PROBLEM 1080 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


contains_uppercase = lambda s: any(map(str.isupper, s))  # [Line 894] | ASSIGNMENT: Creates variable 'contains_uppercase' and stores the result of 'lambda s: any(map(str.isupper, s))' in it

result = contains_uppercase("Hello")                     # [Line 896] | ASSIGNMENT: Creates variable 'result' and stores the result of 'contains_uppercase('Hello')' in it | FUNCTION CALL: Calls 'contains_uppercase()' and stores its return value
print(result)                                            # [Line 897] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1081
Write a Python program to find the average of odd numbers in a list using a lambda function.
"""

# ======================================================================
# PROBLEM 1081 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def average_of_odds(lst):                                # [Line 904]
    odd = list(filter(lambda num: num % 2 !=0, lst))     # [Line 905] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
    total = sum(odd)                                     # [Line 906]
    count = len(odd)                                     # [Line 907]
    average = total / count                              # [Line 908]
    return average                                       # [Line 909]
lst = [1,2,3,4,5,6,7,8,9]                                # [Line 910] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[1, 2, 3, 4, 5, 6, 7, 8, 9]' in it | DATA TYPE: List - A mutable ordered collection. Contains 9 elements

average_of_odds(lst)                                     # [Line 912] | FUNCTION CALL: Executes the function 'average_of_odds' | ARGUMENTS: Passes 1 argument(s) to the function

def average_of_odds(numbers):                            # [Line 914]
    odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))  # [Line 915] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
    return sum(odd_numbers) / len(odd_numbers) if odd_numbers else 0  # [Line 916]

result = average_of_odds([1, 2, 3, 4, 5])                # [Line 918] | ASSIGNMENT: Creates variable 'result' and stores the result of 'average_of_odds([1, 2, 3, 4, 5])' in it | FUNCTION CALL: Calls 'average_of_odds()' and stores its return value
print(result)                                            # [Line 919] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1082
Write a Python program to create a list of squares for all odd numbers in a list using a lambda function.
"""

# ======================================================================
# PROBLEM 1082 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def square_odd_numbers(numbers):                         # [Line 926]
    return list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, numbers)))  # [Line 927] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = square_odd_numbers([1, 2, 3, 4, 5])             # [Line 929] | ASSIGNMENT: Creates variable 'result' and stores the result of 'square_odd_numbers([1, 2, 3, 4, 5])' in it | FUNCTION CALL: Calls 'square_odd_numbers()' and stores its return value
print(result)                                            # [Line 930] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1083
Write a Python program to check if a list contains any negative numbers using a lambda function.
"""

# ======================================================================
# PROBLEM 1083 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


contains_negative = lambda numbers: any(map(lambda x: x < 0, numbers))  # [Line 937] | ASSIGNMENT: Creates variable 'contains_negative' and stores the result of 'lambda numbers: any(map(lambda x: x < 0, numbers))' in it

result = contains_negative([1, -2, 3, 4])                # [Line 939] | ASSIGNMENT: Creates variable 'result' and stores the result of 'contains_negative([1, -2, 3, 4])' in it | FUNCTION CALL: Calls 'contains_negative()' and stores its return value
print(result)                                            # [Line 940] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1084
Write a Python program to create a list of tuples where the first element is the original number and the second element is its cube using a lambda function.
"""

# ======================================================================
# PROBLEM 1084 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def create_cube_tuples(numbers):                         # [Line 947]
    return list(map(lambda x: (x, x**3), numbers))       # [Line 948] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.

result = create_cube_tuples([1, 2, 3])                   # [Line 950] | ASSIGNMENT: Creates variable 'result' and stores the result of 'create_cube_tuples([1, 2, 3])' in it | FUNCTION CALL: Calls 'create_cube_tuples()' and stores its return value
print(result)                                            # [Line 951] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1085
Write a Python program to filter out numbers greater than a given value using a lambda function.
"""

# ======================================================================
# PROBLEM 1085 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def filter_greater_than(numbers, value):                 # [Line 958]
    return list(filter(lambda x: x <= value, numbers))   # [Line 959]

result = filter_greater_than([1, 2, 3, 4, 5], 3)         # [Line 961] | ASSIGNMENT: Creates variable 'result' and stores the result of 'filter_greater_than([1, 2, 3, 4, 5], 3)' in it | FUNCTION CALL: Calls 'filter_greater_than()' and stores its return value
print(result)                                            # [Line 962] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1086
Write a Python program to convert a list of strings to their lengths using a lambda function.
"""

# ======================================================================
# PROBLEM 1086 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def convert_to_lengths(strings):                         # [Line 969]
    return list(map(lambda x: len(x), strings))          # [Line 970]

result = convert_to_lengths(["apple", "banana", "cherry"])  # [Line 972] | ASSIGNMENT: Creates variable 'result' and stores the result of 'convert_to_lengths(['apple', 'banana', 'cherry'])' in it | FUNCTION CALL: Calls 'convert_to_lengths()' and stores its return value
print(result)                                            # [Line 973] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1087
Write a Python program to check if a number is a perfect square using a lambda function.
"""

# ======================================================================
# PROBLEM 1087 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


is_perfect_square = lambda x: int(x**0.5) ** 2 == x      # [Line 980] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2. | ASSIGNMENT: Creates variable 'is_perfect_square' and stores the result of 'lambda x: int(x ** 0.5) ** 2 == x' in it

result = is_perfect_square(16)                           # [Line 982] | ASSIGNMENT: Creates variable 'result' and stores the result of 'is_perfect_square(16)' in it | FUNCTION CALL: Calls 'is_perfect_square()' and stores its return value
print(result)                                            # [Line 983] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1088
Write a Python program to find the sum of the cubes of all numbers in a list using a lambda function.
"""

# ======================================================================
# PROBLEM 1088 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def sum_of_cubes(numbers):                               # [Line 990]
    return sum(map(lambda x: x**3, numbers))             # [Line 991] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.

result = sum_of_cubes([1, 2, 3])                         # [Line 993] | ASSIGNMENT: Creates variable 'result' and stores the result of 'sum_of_cubes([1, 2, 3])' in it | FUNCTION CALL: Calls 'sum_of_cubes()' and stores its return value
print(result)                                            # [Line 994] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1089
Write a Python program to remove all elements greater than a specific value in a list using a lambda function.
"""

# ======================================================================
# PROBLEM 1089 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def remove_elements_greater_than(numbers, value):        # [Line 1001]
    return list(filter(lambda x: x <= value, numbers))   # [Line 1002]

result = remove_elements_greater_than([1, 2, 3, 4, 5], 3)  # [Line 1004] | ASSIGNMENT: Creates variable 'result' and stores the result of 'remove_elements_greater_than([1, 2, 3, 4, 5], 3)' in it | FUNCTION CALL: Calls 'remove_elements_greater_than()' and stores its return value
print(result)                                            # [Line 1005] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1090
Write a Python program to check if all elements in a list are positive using a lambda function.
"""

# ======================================================================
# PROBLEM 1090 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


all_positive = lambda numbers: all(map(lambda x: x > 0, numbers))  # [Line 1012] | ASSIGNMENT: Creates variable 'all_positive' and stores the result of 'lambda numbers: all(map(lambda x: x > 0, numbers))' in it

result = all_positive([1, 2, 3, 4])                      # [Line 1014] | ASSIGNMENT: Creates variable 'result' and stores the result of 'all_positive([1, 2, 3, 4])' in it | FUNCTION CALL: Calls 'all_positive()' and stores its return value
print(result)                                            # [Line 1015] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1091
Write a Python program to create a generator that yields the square of each number in a given range.
"""

# ======================================================================
# PROBLEM 1091 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def square_generator(n):                                 # [Line 1022]
    for i in range(n):                                   # [Line 1023]
        yield i**2                                       # [Line 1024] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.

result = list(square_generator(5))                       # [Line 1026] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(square_generator(5))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 1027] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1092
Write a Python program to create a generator that yields Fibonacci numbers up to a given number.
"""

# ======================================================================
# PROBLEM 1092 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def fibonacci_generator(limit):                          # [Line 1034]
    a, b = 0, 1                                          # [Line 1035]
    while a <= limit:                                    # [Line 1036]
        yield a                                          # [Line 1037]
        a, b = b, a + b                                  # [Line 1038]

result = list(fibonacci_generator(20))                   # [Line 1040] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(fibonacci_generator(20))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 1041] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1093
Write a Python program to create a generator that yields the characters of a string one by one.
"""

# ======================================================================
# PROBLEM 1093 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def char_generator(s):                                   # [Line 1048]
    for char in s:                                       # [Line 1049]
        yield char                                       # [Line 1050]

result = list(char_generator("hello"))                   # [Line 1052] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(char_generator('hello'))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 1053] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1094
Write a Python program to create a generator that yields numbers from 1 to n with a step of 2.
"""

# ======================================================================
# PROBLEM 1094 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def step_generator(n):                                   # [Line 1060]
    for i in range(1, n, 2):                             # [Line 1061]
        yield i                                          # [Line 1062]

result = list(step_generator(10))                        # [Line 1064] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(step_generator(10))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 1065] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1095
Write a Python program to create a generator that yields even numbers from 1 to n.
"""

# ======================================================================
# PROBLEM 1095 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def even_number_generator(n):                            # [Line 1072]
    for i in range(2, n+1, 2):                           # [Line 1073]
        yield i                                          # [Line 1074]

result = list(even_number_generator(10))                 # [Line 1076] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(even_number_generator(10))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 1077] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1096
Write a Python program to create a generator that yields squares of even numbers from 1 to n.
"""

# ======================================================================
# PROBLEM 1096 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def square_even_generator(n):                            # [Line 1084]
    for i in range(2, n+1, 2):                           # [Line 1085]
        yield i**2                                       # [Line 1086] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.

result = list(square_even_generator(10))                 # [Line 1088] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(square_even_generator(10))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 1089] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1097
Write a Python program to create a generator that yields the first n prime numbers.
"""

# ======================================================================
# PROBLEM 1097 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def prime_generator(n):                                  # [Line 1096]
    primes = []                                          # [Line 1097]
    num = 2                                              # [Line 1098]
    while len(primes) < n:                               # [Line 1099]
        if all(num % p != 0 for p in primes):            # [Line 1100] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
            primes.append(num)                           # [Line 1101]
        num += 1                                         # [Line 1102]
    yield from primes                                    # [Line 1103]

result = list(prime_generator(5))                        # [Line 1105] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(prime_generator(5))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 1106] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1098
Write a Python program to create a generator that yields the sum of consecutive pairs from a given list.
"""

# ======================================================================
# PROBLEM 1098 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def consecutive_pair_sum(lst):                           # [Line 1113]
    for i in range(len(lst)-1):                          # [Line 1114]
        yield lst[i] + lst[i+1]                          # [Line 1115]

result = list(consecutive_pair_sum([1, 2, 3, 4, 5]))     # [Line 1117] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(consecutive_pair_sum([1, 2, 3, 4, 5]))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 1118] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1099
Write a Python program to create a generator that yields the factorial of each number from 1 to n.
"""

# ======================================================================
# PROBLEM 1099 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def factorial_generator(n):                              # [Line 1125]
    def factorial(x):                                    # [Line 1126]
        result = 1                                       # [Line 1127]
        for i in range(1, x+1):                          # [Line 1128]
            result *= i                                  # [Line 1129]
        return result                                    # [Line 1130]
    for i in range(1, n+1):                              # [Line 1131]
        yield factorial(i)                               # [Line 1132]

result = list(factorial_generator(5))                    # [Line 1134] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(factorial_generator(5))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 1135] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1100
Write a Python program to create a generator that yields numbers divisible by 3 and 5 from 1 to n.
"""

# ======================================================================
# PROBLEM 1100 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def divisible_by_3_and_5_generator(n):                   # [Line 1142]
    for i in range(1, n+1):                              # [Line 1143]
        if i % 3 == 0 and i % 5 == 0:                    # [Line 1144] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
            yield i                                      # [Line 1145]

result = list(divisible_by_3_and_5_generator(50))        # [Line 1147] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(divisible_by_3_and_5_generator(50))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 1148] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1101
Write a Python program to create a generator that filters out the odd numbers from a list.
"""

# ======================================================================
# PROBLEM 1101 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def odd_filter_generator(lst):                           # [Line 1155]
    for num in lst:                                      # [Line 1156]
        if num % 2 == 0:                                 # [Line 1157] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
            yield num                                    # [Line 1158]

result = list(odd_filter_generator([1, 2, 3, 4, 5, 6]))  # [Line 1160] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(odd_filter_generator([1, 2, 3, 4, 5, 6]))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 1161] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1102
Write a Python program to create a generator that yields the cumulative sum of a given list of numbers.
"""

# ======================================================================
# PROBLEM 1102 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def cumulative_sum_generator(lst):                       # [Line 1168]
    total = 0                                            # [Line 1169]
    for num in lst:                                      # [Line 1170]
        total += num                                     # [Line 1171]
        yield total                                      # [Line 1172]

result = list(cumulative_sum_generator([1, 2, 3, 4, 5]))  # [Line 1174] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(cumulative_sum_generator([1, 2, 3, 4, 5]))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 1175] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1103
Write a Python program to create a generator that yields the n-th power of each number from 1 to n.
"""

# ======================================================================
# PROBLEM 1103 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def power_generator(n, power):                           # [Line 1182]
    for i in range(1, n+1):                              # [Line 1183]
        yield i**power                                   # [Line 1184] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.

result = list(power_generator(5, 3))                     # [Line 1186] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(power_generator(5, 3))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 1187] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1104
Write a Python program to create a generator that yields each word in a sentence.
"""

# ======================================================================
# PROBLEM 1104 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def word_generator(sentence):                            # [Line 1194]
    words = sentence.split()                             # [Line 1195]
    for word in words:                                   # [Line 1196]
        yield word                                       # [Line 1197]

result = list(word_generator("This is a test sentence"))  # [Line 1199] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(word_generator('This is a test sentence'))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 1200] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1105
Write a Python program to create a generator that yields numbers that are squares of integers up to n.
"""

# ======================================================================
# PROBLEM 1105 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def square_number_generator(n):                          # [Line 1207]
    for i in range(1, n+1):                              # [Line 1208]
        yield i**2                                       # [Line 1209] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.

result = list(square_number_generator(5))                # [Line 1211] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(square_number_generator(5))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 1212] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1106
Write a Python program to create a generator that yields the squares of odd numbers from 1 to n.
"""

# ======================================================================
# PROBLEM 1106 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def main(n):                                             # [Line 1219]
    for num in range(1, n+1):                            # [Line 1220]
        if num % 2 != 0:                                 # [Line 1221] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
            yield num ** 2                               # [Line 1222] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.

n = 10                                                   # [Line 1224] | ASSIGNMENT: Creates variable 'n' and stores the result of '10' in it | DATA TYPE: Integer - A whole number: 10
result = list(main(n))                                   # [Line 1225] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(main(n))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 1226] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

def square_odd_number_generator(n):                      # [Line 1228]
    for i in range(1, n+1, 2):                           # [Line 1229]
        yield i**2                                       # [Line 1230] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.

result = list(square_odd_number_generator(10))           # [Line 1232] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(square_odd_number_generator(10))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 1233] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1107
Write a Python program to create a generator that yields the elements of a given list in reverse order.
"""

# ======================================================================
# PROBLEM 1107 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def reverse_list_generator(lst):                         # [Line 1240]
    for i in range(len(lst)-1, -1, -1):                  # [Line 1241]
        yield lst[i]                                     # [Line 1242]

result = list(reverse_list_generator([1, 2, 3, 4, 5]))   # [Line 1244] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(reverse_list_generator([1, 2, 3, 4, 5]))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 1245] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1108
Write a Python program to create a generator that yields multiples of a given number up to n.
"""

# ======================================================================
# PROBLEM 1108 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def multiple_generator(n, multiple):                     # [Line 1252]
    for i in range(multiple, n+1, multiple):             # [Line 1253]
        yield i                                          # [Line 1254]

result = list(multiple_generator(20, 3))                 # [Line 1256] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(multiple_generator(20, 3))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 1257] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1109
Write a Python program to create a generator that yields all the uppercase letters in a string.
"""

# ======================================================================
# PROBLEM 1109 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def uppercase_generator(s):                              # [Line 1264]
    for char in s:                                       # [Line 1265]
        if char.isupper():                               # [Line 1266]
            yield char                                   # [Line 1267]

result = list(uppercase_generator("Hello World"))        # [Line 1269] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(uppercase_generator('Hello World'))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 1270] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1110
Write a Python program to create a generator that yields the differences between consecutive elements of a list.
"""

# ======================================================================
# PROBLEM 1110 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def consecutive_diff_generator(lst):                     # [Line 1277]
    for i in range(len(lst)-1):                          # [Line 1278]
        yield lst[i+1] - lst[i]                          # [Line 1279]

result = list(consecutive_diff_generator([1, 3, 6, 10]))  # [Line 1281] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(consecutive_diff_generator([1, 3, 6, 10]))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 1282] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1111
Write a Python program to create a generator that yields numbers greater than a given value in a list.
"""

# ======================================================================
# PROBLEM 1111 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def greater_than_generator(lst, value):                  # [Line 1289]
    for num in lst:                                      # [Line 1290]
        if num > value:                                  # [Line 1291]
            yield num                                    # [Line 1292]

result = list(greater_than_generator([1, 2, 3, 4, 5, 6], 3))  # [Line 1294] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(greater_than_generator([1, 2, 3, 4, 5, 6], 3))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 1295] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1112
Write a Python program to create a generator that yields the sum of each element with its index from a list.
"""

# ======================================================================
# PROBLEM 1112 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def sum_with_index_generator(lst):                       # [Line 1302]
    for index, num in enumerate(lst):                    # [Line 1303]
        yield num + index                                # [Line 1304]

result = list(sum_with_index_generator([10, 20, 30, 40]))  # [Line 1306] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(sum_with_index_generator([10, 20, 30, 40]))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 1307] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1113
Write a Python program to create a generator that yields all palindromes from a list of strings. 
"""

# ======================================================================
# PROBLEM 1113 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def palindrome_generator(lst):                           # [Line 1314]
    for word in lst:                                     # [Line 1315]
        if word == word[::-1]:                           # [Line 1316] | SLICING OPERATION [::-1] - This is a reverse slice. The syntax [::-1] means: start at the beginning (no start index), stop at the end (no stop index), and step backwards by 1. This effectively reverses the entire sequence. Example: [1,2,3][::-1] becomes [3,2,1] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).
            yield word                                   # [Line 1317]

result = list(palindrome_generator(["madam", "apple", "racecar", "banana"]))  # [Line 1319] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(palindrome_generator(['madam', 'apple', 'racecar', 'banana']))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 1320] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1114
Write a Python program to create a generator that yields the product of elements in pairs from a given list.
"""

# ======================================================================
# PROBLEM 1114 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def pair_product_generator(lst):                         # [Line 1327]
    for i in range(len(lst)-1):                          # [Line 1328]
        yield lst[i] * lst[i+1]                          # [Line 1329]

result = list(pair_product_generator([1, 2, 3, 4]))      # [Line 1331] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(pair_product_generator([1, 2, 3, 4]))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 1332] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1115
Write a Python program to create a generator that yields elements from a list that are greater than the previous element. 
"""

# ======================================================================
# PROBLEM 1115 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def greater_than_previous_generator(lst):                # [Line 1339]
    for i in range(1, len(lst)):                         # [Line 1340]
        if lst[i] > lst[i-1]:                            # [Line 1341] | SLICING OPERATION - Extracts a portion of the sequence
            yield lst[i]                                 # [Line 1342]

result = list(greater_than_previous_generator([1, 2, 1, 4, 3]))  # [Line 1344] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(greater_than_previous_generator([1, 2, 1, 4, 3]))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 1345] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1116
Write a Python program to create a generator that yields all numbers in a list that are divisible by a given number.
"""

# ======================================================================
# PROBLEM 1116 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def divisible_by_generator(lst, divisor):                # [Line 1352]
    for num in lst:                                      # [Line 1353]
        if num % divisor == 0:                           # [Line 1354] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
            yield num                                    # [Line 1355]

result = list(divisible_by_generator([10, 15, 20, 25, 30], 5))  # [Line 1357] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(divisible_by_generator([10, 15, 20, 25, 30], 5))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 1358] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1117
Write a Python program to create a generator that yields the first n even Fibonacci numbers.
"""

# ======================================================================
# PROBLEM 1117 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def even_fibonacci_generator(n):                         # [Line 1365]
    a, b = 0, 2                                          # [Line 1366]
    count = 0                                            # [Line 1367]
    while count < n:                                     # [Line 1368]
        yield a                                          # [Line 1369]
        a, b = b, 4 * b + a                              # [Line 1370]
        count += 1                                       # [Line 1371]

result = list(even_fibonacci_generator(5))               # [Line 1373] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(even_fibonacci_generator(5))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 1374] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1118
Write a Python program to create a generator that yields all the even-indexed elements of a list.
"""

# ======================================================================
# PROBLEM 1118 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def even_index_generator(lst):                           # [Line 1381]
    for i in range(0, len(lst), 2):                      # [Line 1382]
        yield lst[i]                                     # [Line 1383]

result = list(even_index_generator([1, 2, 3, 4, 5, 6]))  # [Line 1385] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(even_index_generator([1, 2, 3, 4, 5, 6]))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 1386] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1119
Write a Python program to create a generator that yields each word in a sentence, but only those with an even number of characters. 
"""

# ======================================================================
# PROBLEM 1119 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def even_length_word_generator(sentence):                # [Line 1393]
    words = sentence.split()                             # [Line 1394]
    for word in words:                                   # [Line 1395]
        if len(word) % 2 == 0:                           # [Line 1396] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
            yield word                                   # [Line 1397]

result = list(even_length_word_generator("This is a simple test sentence"))  # [Line 1399] | ASSIGNMENT: Creates variable 'result' and stores the result of 'list(even_length_word_generator('This is a simple test sentence'))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(result)                                            # [Line 1400] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1120
Write a Python program to check if a number is positive, negative, or zero. Control flow.
"""

# ======================================================================
# PROBLEM 1120 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_number(n):                                     # [Line 1407]
    if n > 0:                                            # [Line 1408]
        return "Positive"                                # [Line 1409]
    elif n < 0:                                          # [Line 1410]
        return "Negative"                                # [Line 1411]
    else:                                                # [Line 1412]
        return "Zero"                                    # [Line 1413]

result = check_number(5)                                 # [Line 1415] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_number(5)' in it | FUNCTION CALL: Calls 'check_number()' and stores its return value
print(result)                                            # [Line 1416] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1121
Write a Python program to find the largest of three numbers. Control flow.
"""

# ======================================================================
# PROBLEM 1121 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def largest_of_three(a, b, c):                           # [Line 1423]
    if a >= b and a >= c:                                # [Line 1424]
        return a                                         # [Line 1425]
    elif b >= a and b >= c:                              # [Line 1426]
        return b                                         # [Line 1427]
    else:                                                # [Line 1428]
        return c                                         # [Line 1429]

result = largest_of_three(10, 20, 15)                    # [Line 1431] | ASSIGNMENT: Creates variable 'result' and stores the result of 'largest_of_three(10, 20, 15)' in it | FUNCTION CALL: Calls 'largest_of_three()' and stores its return value
print(result)                                            # [Line 1432] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1122
Write a Python program to check if a given year is a leap year. Control flow.
"""

# ======================================================================
# PROBLEM 1122 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def is_leap_year(year):                                  # [Line 1439]
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):  # [Line 1440] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
        return True                                      # [Line 1441]
    else:                                                # [Line 1442]
        return False                                     # [Line 1443]

result = is_leap_year(2024)                              # [Line 1445] | ASSIGNMENT: Creates variable 'result' and stores the result of 'is_leap_year(2024)' in it | FUNCTION CALL: Calls 'is_leap_year()' and stores its return value
print(result)                                            # [Line 1446] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1123
Write a Python program to check if a number is even or odd. Control flow.
"""

# ======================================================================
# PROBLEM 1123 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_even_odd(n):                                   # [Line 1453]
    if n % 2 == 0:                                       # [Line 1454] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
        return "Even"                                    # [Line 1455]
    else:                                                # [Line 1456]
        return "Odd"                                     # [Line 1457]

result = check_even_odd(7)                               # [Line 1459] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_even_odd(7)' in it | FUNCTION CALL: Calls 'check_even_odd()' and stores its return value
print(result)                                            # [Line 1460] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1124
Write a Python program to check if a number is divisible by both 3 and 5. Control flow.
"""

# ======================================================================
# PROBLEM 1124 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def divisible_by_3_and_5(n):                             # [Line 1467]
    if n % 3 == 0 and n % 5 == 0:                        # [Line 1468] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
        return True                                      # [Line 1469]
    else:                                                # [Line 1470]
        return False                                     # [Line 1471]

result = divisible_by_3_and_5(15)                        # [Line 1473] | ASSIGNMENT: Creates variable 'result' and stores the result of 'divisible_by_3_and_5(15)' in it | FUNCTION CALL: Calls 'divisible_by_3_and_5()' and stores its return value
print(result)                                            # [Line 1474] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1125
Write a Python program to print all numbers from 1 to n that are divisible by 7. Control flow.
"""

# ======================================================================
# PROBLEM 1125 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def divisible_by_7(n):                                   # [Line 1481]
    for i in range(1, n+1):                              # [Line 1482]
        if i % 7 == 0:                                   # [Line 1483] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
            print(i)                                     # [Line 1484]

divisible_by_7(50)                                       # [Line 1486] | FUNCTION CALL: Executes the function 'divisible_by_7' | ARGUMENTS: Passes 1 argument(s) to the function

"""
Problem: 1126
Write a Python program to check if a given number is a prime number. Control flow.
"""

# ======================================================================
# PROBLEM 1126 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def is_prime(n):                                         # [Line 1493]
    if n < 2:                                            # [Line 1494]
        return False                                     # [Line 1495]
    for i in range(2, int(n**0.5) + 1):                  # [Line 1496] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
        if n % i == 0:                                   # [Line 1497] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
            return False                                 # [Line 1498]
    return True                                          # [Line 1499]

result = is_prime(11)                                    # [Line 1501] | ASSIGNMENT: Creates variable 'result' and stores the result of 'is_prime(11)' in it | FUNCTION CALL: Calls 'is_prime()' and stores its return value
print(result)                                            # [Line 1502] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1127
Write a Python program to find the factorial of a number using recursion. Control flow.
"""

# ======================================================================
# PROBLEM 1127 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def factorial(n):                                        # [Line 1509]
    if n == 0 or n == 1:                                 # [Line 1510] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).
        return 1                                         # [Line 1511]
    return n * factorial(n-1)                            # [Line 1512]

result = factorial(5)                                    # [Line 1514] | ASSIGNMENT: Creates variable 'result' and stores the result of 'factorial(5)' in it | FUNCTION CALL: Calls 'factorial()' and stores its return value
print(result)                                            # [Line 1515] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1128
Write a Python program to check if a string is a palindrome. Control flow.
"""

# ======================================================================
# PROBLEM 1128 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def is_palindrome(s):                                    # [Line 1522]
    if s == s[::-1]:                                     # [Line 1523] | SLICING OPERATION [::-1] - This is a reverse slice. The syntax [::-1] means: start at the beginning (no start index), stop at the end (no stop index), and step backwards by 1. This effectively reverses the entire sequence. Example: [1,2,3][::-1] becomes [3,2,1] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).
        return True                                      # [Line 1524]
    else:                                                # [Line 1525]
        return False                                     # [Line 1526]

result = is_palindrome("madam")                          # [Line 1528] | ASSIGNMENT: Creates variable 'result' and stores the result of 'is_palindrome('madam')' in it | FUNCTION CALL: Calls 'is_palindrome()' and stores its return value
print(result)                                            # [Line 1529] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1129
Write a Python program to count the number of vowels in a given string. Control flow.
"""

# ======================================================================
# PROBLEM 1129 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def count_vowels(s):                                     # [Line 1536]
    vowels = "aeiou"                                     # [Line 1537]
    count = 0                                            # [Line 1538]
    for char in s:                                       # [Line 1539]
        if char.lower() in vowels:                       # [Line 1540]
            count += 1                                   # [Line 1541]
    return count                                         # [Line 1542]

result = count_vowels("Hello World")                     # [Line 1544] | ASSIGNMENT: Creates variable 'result' and stores the result of 'count_vowels('Hello World')' in it | FUNCTION CALL: Calls 'count_vowels()' and stores its return value
print(result)                                            # [Line 1545] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1130
Write a Python program to check if a number is a perfect number. Control flow.
"""

# ======================================================================
# PROBLEM 1130 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def is_perfect_number(n):                                # [Line 1552]
    divisors = [i for i in range(1, n) if n % i == 0]    # [Line 1553] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
    if sum(divisors) == n:                               # [Line 1554] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).
        return True                                      # [Line 1555]
    else:                                                # [Line 1556]
        return False                                     # [Line 1557]

result = is_perfect_number(6)                            # [Line 1559] | ASSIGNMENT: Creates variable 'result' and stores the result of 'is_perfect_number(6)' in it | FUNCTION CALL: Calls 'is_perfect_number()' and stores its return value
print(result)                                            # [Line 1560] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1131
Write a Python program to check if a number is Armstrong number. Control flow.
"""

# ======================================================================
# PROBLEM 1131 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def is_armstrong(n):                                     # [Line 1567]
    num_str = str(n)                                     # [Line 1568]
    length = len(num_str)                                # [Line 1569]
    total = sum(int(digit) ** length for digit in num_str)  # [Line 1570] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    if total == n:                                       # [Line 1571] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).
        return True                                      # [Line 1572]
    else:                                                # [Line 1573]
        return False                                     # [Line 1574]

result = is_armstrong(153)                               # [Line 1576] | ASSIGNMENT: Creates variable 'result' and stores the result of 'is_armstrong(153)' in it | FUNCTION CALL: Calls 'is_armstrong()' and stores its return value
print(result)                                            # [Line 1577] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1132
Write a Python program to print all the prime numbers less than or equal to n. Control flow.
"""

# ======================================================================
# PROBLEM 1132 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def prime_numbers_up_to_n(n):                            # [Line 1584]
    primes = []                                          # [Line 1585]
    for num in range(2, n+1):                            # [Line 1586]
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):  # [Line 1587] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
            primes.append(num)                           # [Line 1588]
    return primes                                        # [Line 1589]

result = prime_numbers_up_to_n(20)                       # [Line 1591] | ASSIGNMENT: Creates variable 'result' and stores the result of 'prime_numbers_up_to_n(20)' in it | FUNCTION CALL: Calls 'prime_numbers_up_to_n()' and stores its return value
print(result)                                            # [Line 1592] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1133
Write a Python program to check if a number is an even number and greater than 10. Control flow.
"""

# ======================================================================
# PROBLEM 1133 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def even_and_greater_than_10(n):                         # [Line 1599]
    if n % 2 == 0 and n > 10:                            # [Line 1600] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
        return True                                      # [Line 1601]
    else:                                                # [Line 1602]
        return False                                     # [Line 1603]

result = even_and_greater_than_10(12)                    # [Line 1605] | ASSIGNMENT: Creates variable 'result' and stores the result of 'even_and_greater_than_10(12)' in it | FUNCTION CALL: Calls 'even_and_greater_than_10()' and stores its return value
print(result)                                            # [Line 1606] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1134
Write a Python program to find all the divisors of a number. Control flow.
"""

# ======================================================================
# PROBLEM 1134 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


n = 20                                                   # [Line 1613] | ASSIGNMENT: Creates variable 'n' and stores the result of '20' in it | DATA TYPE: Integer - A whole number: 20

for i in range(1, n + 1):                                # [Line 1615]
    if n % i == 0:                                       # [Line 1616] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
        print(i)                                         # [Line 1617]

def find_divisors(n):                                    # [Line 1619]
    divisors = [i for i in range(1, n+1) if n % i == 0]  # [Line 1620] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
    return divisors                                      # [Line 1621]

result = find_divisors(12)                               # [Line 1623] | ASSIGNMENT: Creates variable 'result' and stores the result of 'find_divisors(12)' in it | FUNCTION CALL: Calls 'find_divisors()' and stores its return value
print(result)                                            # [Line 1624] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1135
Write a Python program to print the multiplication table of a number up to 10. Control flow.
"""

# ======================================================================
# PROBLEM 1135 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def multiplication_table(n):                             # [Line 1631]
    for i in range(1, 11):                               # [Line 1632]
        print(f"{n} x {i} = {n*i}")                      # [Line 1633]

multiplication_table(7)                                  # [Line 1635] | FUNCTION CALL: Executes the function 'multiplication_table' | ARGUMENTS: Passes 1 argument(s) to the function

"""
Problem: 1136
Write a Python program to check if a number is a perfect square. Control flow.
"""

# ======================================================================
# PROBLEM 1136 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def is_perfect_square(n):                                # [Line 1642]
    return int(n**0.5) ** 2 == n                         # [Line 1643] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.

result = is_perfect_square(25)                           # [Line 1645] | ASSIGNMENT: Creates variable 'result' and stores the result of 'is_perfect_square(25)' in it | FUNCTION CALL: Calls 'is_perfect_square()' and stores its return value
print(result)                                            # [Line 1646] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1137
Write a Python program to check if a number is a power of 2. Control flow.
"""

# ======================================================================
# PROBLEM 1137 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def is_power_of_2(n):                                    # [Line 1653]
    return n > 0 and (n & (n - 1)) == 0                  # [Line 1654] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

result = is_power_of_2(16)                               # [Line 1656] | ASSIGNMENT: Creates variable 'result' and stores the result of 'is_power_of_2(16)' in it | FUNCTION CALL: Calls 'is_power_of_2()' and stores its return value
print(result)                                            # [Line 1657] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1138
Write a Python program to find the second largest number in a list. Control flow.
"""

# ======================================================================
# PROBLEM 1138 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def second_largest(lst):                                 # [Line 1664]
    lst = sorted(set(lst), reverse=True)                 # [Line 1665]
    return lst[1] if len(lst) > 1 else None              # [Line 1666]

result = second_largest([10, 20, 4, 45, 99])             # [Line 1668] | ASSIGNMENT: Creates variable 'result' and stores the result of 'second_largest([10, 20, 4, 45, 99])' in it | FUNCTION CALL: Calls 'second_largest()' and stores its return value
print(result)                                            # [Line 1669] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1139
Write a Python program to check if a given number is a power of 3. Control flow.
"""

# ======================================================================
# PROBLEM 1139 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def is_power_of_3(n):                                    # [Line 1676]
    while n % 3 == 0 and n > 0:                          # [Line 1677] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
        n //= 3                                          # [Line 1678] | FLOOR DIVISION (//) - Divides two numbers and returns the largest integer less than or equal to the result. Example: 7 // 2 = 3 (not 3.5). This is useful for integer division when you don't want decimal results.
    return n == 1                                        # [Line 1679] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

result = is_power_of_3(27)                               # [Line 1681] | ASSIGNMENT: Creates variable 'result' and stores the result of 'is_power_of_3(27)' in it | FUNCTION CALL: Calls 'is_power_of_3()' and stores its return value
print(result)                                            # [Line 1682] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1140
Write a Python program to print Fibonacci numbers up to n. Control flow.
"""

# ======================================================================
# PROBLEM 1140 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def fibonacci_up_to_n(n):                                # [Line 1689]
    a, b = 0, 1                                          # [Line 1690]
    while a <= n:                                        # [Line 1691]
        print(a, end=" ")                                # [Line 1692]
        a, b = b, a + b                                  # [Line 1693]

fibonacci_up_to_n(20)                                    # [Line 1695] | FUNCTION CALL: Executes the function 'fibonacci_up_to_n' | ARGUMENTS: Passes 1 argument(s) to the function

"""
Problem: 1141
Write a Python program to count the occurrences of a specific element in a list. Control flow.
"""

# ======================================================================
# PROBLEM 1141 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def count_occurrences(lst, element):                     # [Line 1702]
    return lst.count(element)                            # [Line 1703]

result = count_occurrences([1, 2, 2, 3, 4, 2], 2)        # [Line 1705] | ASSIGNMENT: Creates variable 'result' and stores the result of 'count_occurrences([1, 2, 2, 3, 4, 2], 2)' in it | FUNCTION CALL: Calls 'count_occurrences()' and stores its return value
print(result)                                            # [Line 1706] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1142
Write a Python program to check if a given number is a perfect square and an Armstrong number. Control flow.
"""

# ======================================================================
# PROBLEM 1142 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def is_perfect_square_and_armstrong(n):                  # [Line 1713]
    if is_perfect_square(n) and is_armstrong(n):         # [Line 1714]
        return True                                      # [Line 1715]
    else:                                                # [Line 1716]
        return False                                     # [Line 1717]

result = is_perfect_square_and_armstrong(153)            # [Line 1719] | ASSIGNMENT: Creates variable 'result' and stores the result of 'is_perfect_square_and_armstrong(153)' in it | FUNCTION CALL: Calls 'is_perfect_square_and_armstrong()' and stores its return value
print(result)                                            # [Line 1720] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1143
Write a Python program to find all numbers in a given range that are divisible by 7 and 11. Control flow.
"""

# ======================================================================
# PROBLEM 1143 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def divisible_by_7_and_11(start, end):                   # [Line 1727]
    return [num for num in range(start, end+1) if num % 7 == 0 and num % 11 == 0]  # [Line 1728] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = divisible_by_7_and_11(1, 100)                   # [Line 1730] | ASSIGNMENT: Creates variable 'result' and stores the result of 'divisible_by_7_and_11(1, 100)' in it | FUNCTION CALL: Calls 'divisible_by_7_and_11()' and stores its return value
print(result)                                            # [Line 1731] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1144
Write a Python program to print the factorial of a number using a while loop. Control flow.
"""

# ======================================================================
# PROBLEM 1144 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def factorial_while(n):                                  # [Line 1738]
    result = 1                                           # [Line 1739]
    while n > 1:                                         # [Line 1740]
        result *= n                                      # [Line 1741]
        n -= 1                                           # [Line 1742]
    return result                                        # [Line 1743]

result = factorial_while(5)                              # [Line 1745] | ASSIGNMENT: Creates variable 'result' and stores the result of 'factorial_while(5)' in it | FUNCTION CALL: Calls 'factorial_while()' and stores its return value
print(result)                                            # [Line 1746] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1145
Write a Python program to print a list of numbers in reverse order. Control flow.
"""

# ======================================================================
# PROBLEM 1145 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def reverse_list(lst):                                   # [Line 1753]
    return lst[::-1]                                     # [Line 1754] | SLICING OPERATION [::-1] - This is a reverse slice. The syntax [::-1] means: start at the beginning (no start index), stop at the end (no stop index), and step backwards by 1. This effectively reverses the entire sequence. Example: [1,2,3][::-1] becomes [3,2,1]

result = reverse_list([1, 2, 3, 4, 5])                   # [Line 1756] | ASSIGNMENT: Creates variable 'result' and stores the result of 'reverse_list([1, 2, 3, 4, 5])' in it | FUNCTION CALL: Calls 'reverse_list()' and stores its return value
print(result)                                            # [Line 1757] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1146
Write a Python program to check if a number is divisible by 5 or 10. Control flow.
"""

# ======================================================================
# PROBLEM 1146 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def divisible_by_5_or_10(n):                             # [Line 1764]
    if n % 5 == 0 or n % 10 == 0:                        # [Line 1765] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
        return True                                      # [Line 1766]
    else:                                                # [Line 1767]
        return False                                     # [Line 1768]

result = divisible_by_5_or_10(50)                        # [Line 1770] | ASSIGNMENT: Creates variable 'result' and stores the result of 'divisible_by_5_or_10(50)' in it | FUNCTION CALL: Calls 'divisible_by_5_or_10()' and stores its return value
print(result)                                            # [Line 1771] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1147
Write a Python program to check if a number is divisible by any number in a given list. Control flow.
"""

# ======================================================================
# PROBLEM 1147 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def divisible_by_any_number(n, lst):                     # [Line 1778]
    for num in lst:                                      # [Line 1779]
        if n % num == 0:                                 # [Line 1780] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
            return True                                  # [Line 1781]
    return False                                         # [Line 1782]

result = divisible_by_any_number(10, [3, 5, 7])          # [Line 1784] | ASSIGNMENT: Creates variable 'result' and stores the result of 'divisible_by_any_number(10, [3, 5, 7])' in it | FUNCTION CALL: Calls 'divisible_by_any_number()' and stores its return value
print(result)                                            # [Line 1785] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1148
Write a Python program to demonstrate variable scope in a function. Scope.
"""

# ======================================================================
# PROBLEM 1148 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def outer_function():                                    # [Line 1792]
    x = 10                                               # [Line 1793] | Local variable
    def inner_function():                                # [Line 1794]
        print(x)                                         # [Line 1795] | Accessing the outer function's variable
    inner_function()                                     # [Line 1796]

outer_function()                                         # [Line 1798] | FUNCTION CALL: Executes the function 'outer_function'

"""
Problem: 1149
Write a Python program to show the difference between global and local variables. Scope.
"""

# ======================================================================
# PROBLEM 1149 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


x = 20                                                   # [Line 1805] | ASSIGNMENT: Creates variable 'x' and stores the result of '20' in it | DATA TYPE: Integer - A whole number: 20 | Global variable

def test_scope():                                        # [Line 1807]
    x = 10                                               # [Line 1808] | Local variable
    print(f"Local variable: {x}")                        # [Line 1809]

test_scope()                                             # [Line 1811] | FUNCTION CALL: Executes the function 'test_scope'
print(f"Global variable: {x}")                           # [Line 1812] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1150
Write a Python program to demonstrate the use of the `global` keyword. Scope.
"""

# ======================================================================
# PROBLEM 1150 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def modify_global_variable():                            # [Line 1819]
    global x                                             # [Line 1820]
    x = 30                                               # [Line 1821] | Modifies the global variable

x = 10                                                   # [Line 1823] | ASSIGNMENT: Creates variable 'x' and stores the result of '10' in it | DATA TYPE: Integer - A whole number: 10
modify_global_variable()                                 # [Line 1824] | FUNCTION CALL: Executes the function 'modify_global_variable'
print(x)                                                 # [Line 1825] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1151
Write a Python program to demonstrate the use of `nonlocal` keyword. Scope.
"""

# ======================================================================
# PROBLEM 1151 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def outer_function():                                    # [Line 1832]
    x = 10                                               # [Line 1833]
    def inner_function():                                # [Line 1834]
        nonlocal x                                       # [Line 1835]
        x = 20                                           # [Line 1836] | Modifies the variable in the outer function's scope
    inner_function()                                     # [Line 1837]
    print(x)                                             # [Line 1838]

outer_function()                                         # [Line 1840] | FUNCTION CALL: Executes the function 'outer_function'

"""
Problem: 1152
Write a Python program to demonstrate variable shadowing. Scope.
"""

# ======================================================================
# PROBLEM 1152 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


x = 100                                                  # [Line 1847] | ASSIGNMENT: Creates variable 'x' and stores the result of '100' in it | DATA TYPE: Integer - A whole number: 100 | Global variable

def shadowing_example():                                 # [Line 1849]
    x = 50                                               # [Line 1850] | Local variable, shadows the global variable
    print(f"Local x: {x}")                               # [Line 1851]

shadowing_example()                                      # [Line 1853] | FUNCTION CALL: Executes the function 'shadowing_example'
print(f"Global x: {x}")                                  # [Line 1854] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1153
Write a Python program to demonstrate the use of function arguments as local variables. Scope.
"""

# ======================================================================
# PROBLEM 1153 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def example_function(a, b):                              # [Line 1861]
    c = a + b                                            # [Line 1862] | c is a local variable
    print(f"The sum of {a} and {b} is {c}")              # [Line 1863]

example_function(5, 7)                                   # [Line 1865] | FUNCTION CALL: Executes the function 'example_function' | ARGUMENTS: Passes 2 argument(s) to the function

"""
Problem: 1154
Write a Python program to demonstrate how to pass a variable as a default argument. Scope.
"""

# ======================================================================
# PROBLEM 1154 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def greet(name="John"):                                  # [Line 1872]
    print(f"Hello, {name}!")                             # [Line 1873]

greet()                                                  # [Line 1875] | FUNCTION CALL: Executes the function 'greet' | Uses default value
greet("Alice")                                           # [Line 1876] | FUNCTION CALL: Executes the function 'greet' | ARGUMENTS: Passes 1 argument(s) to the function | Uses passed argument

"""
Problem: 1155
Write a Python program to show the use of mutable and immutable types in functions. Scope.
"""

# ======================================================================
# PROBLEM 1155 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def modify_list(lst):                                    # [Line 1883]
    lst.append(4)                                        # [Line 1884] | List is mutable, so it is modified
    print(f"Modified list: {lst}")                       # [Line 1885]

my_list = [1, 2, 3]                                      # [Line 1887] | ASSIGNMENT: Creates variable 'my_list' and stores the result of '[1, 2, 3]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
modify_list(my_list)                                     # [Line 1888] | FUNCTION CALL: Executes the function 'modify_list' | ARGUMENTS: Passes 1 argument(s) to the function
print(f"Original list: {my_list}")                       # [Line 1889] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

def modify_integer(n):                                   # [Line 1891]
    n += 1                                               # [Line 1892] | Integer is immutable, so it cannot be modified
    print(f"Modified integer: {n}")                      # [Line 1893]

my_int = 5                                               # [Line 1895] | ASSIGNMENT: Creates variable 'my_int' and stores the result of '5' in it | DATA TYPE: Integer - A whole number: 5
modify_integer(my_int)                                   # [Line 1896] | FUNCTION CALL: Executes the function 'modify_integer' | ARGUMENTS: Passes 1 argument(s) to the function
print(f"Original integer: {my_int}")                     # [Line 1897] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1156
Write a Python program to demonstrate the scope of variables in a loop. Scope.
"""

# ======================================================================
# PROBLEM 1156 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def loop_scope():                                        # [Line 1904]
    for i in range(3):                                   # [Line 1905]
        x = i                                            # [Line 1906]
        print(f"Inside loop: {x}")                       # [Line 1907]
    # x is accessible here after the loop ends
    print(f"Outside loop: {x}")                          # [Line 1909]

loop_scope()                                             # [Line 1911] | FUNCTION CALL: Executes the function 'loop_scope'

"""
Problem: 1157
Write a Python program to check if a variable is defined. Scope.
"""

# ======================================================================
# PROBLEM 1157 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_variable():                                    # [Line 1918]
    try:                                                 # [Line 1919]
        print(x)                                         # [Line 1920]
    except NameError:                                    # [Line 1921]
        print("x is not defined")                        # [Line 1922]

check_variable()                                         # [Line 1924] | FUNCTION CALL: Executes the function 'check_variable'

"""
Problem: 1158
Write a Python program to demonstrate the scope of variables in nested functions. Scope.
"""

# ======================================================================
# PROBLEM 1158 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def outer_function():                                    # [Line 1931]
    x = 10                                               # [Line 1932] | Local variable in outer function
    def inner_function():                                # [Line 1933]
        y = 20                                           # [Line 1934] | Local variable in inner function
        print(f"Inner function: x = {x}, y = {y}")       # [Line 1935]
    inner_function()                                     # [Line 1936]
    print(f"Outer function: x = {x}")                    # [Line 1937]

outer_function()                                         # [Line 1939] | FUNCTION CALL: Executes the function 'outer_function'

"""
Problem: 1159
Write a Python program to demonstrate how to return a variable from a function. Scope.
"""

# ======================================================================
# PROBLEM 1159 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def add_numbers(a, b):                                   # [Line 1946]
    sum_result = a + b                                   # [Line 1947]
    return sum_result                                    # [Line 1948]

result = add_numbers(3, 5)                               # [Line 1950] | ASSIGNMENT: Creates variable 'result' and stores the result of 'add_numbers(3, 5)' in it | FUNCTION CALL: Calls 'add_numbers()' and stores its return value
print(f"The sum is {result}")                            # [Line 1951] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1160
Write a Python program to explain how default mutable arguments work in functions. Scope.
"""

# ======================================================================
# PROBLEM 1160 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def append_to_list(n, default_list=[]):                  # [Line 1958] | SLICING OPERATION - Extracts a portion of the sequence
    default_list.append(n)                               # [Line 1959]
    return default_list                                  # [Line 1960]

# Test the function
print(append_to_list(1))                                 # [Line 1963] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | [1]
print(append_to_list(2))                                 # [Line 1964] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | [1, 2]
print(append_to_list(3))                                 # [Line 1965] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | [1, 2, 3]


def append_to_list(lst=None):                            # [Line 1968]
    if lst is None:                                      # [Line 1969]
        lst = []                                         # [Line 1970]
    lst.append(1)                                        # [Line 1971]
    return lst                                           # [Line 1972]

print(append_to_list())                                  # [Line 1974] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Returns [1]
print(append_to_list())                                  # [Line 1975] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Returns [1], new list is created each time

"""
Problem: 1161
Write a Python program to demonstrate the use of variables in list comprehensions. Scope.
"""

# ======================================================================
# PROBLEM 1161 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def square_numbers(lst):                                 # [Line 1982]
    return [x**2 for x in lst]                           # [Line 1983] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.

numbers = [1, 2, 3, 4]                                   # [Line 1985] | ASSIGNMENT: Creates variable 'numbers' and stores the result of '[1, 2, 3, 4]' in it | DATA TYPE: List - A mutable ordered collection. Contains 4 elements
result = square_numbers(numbers)                         # [Line 1986] | ASSIGNMENT: Creates variable 'result' and stores the result of 'square_numbers(numbers)' in it | FUNCTION CALL: Calls 'square_numbers()' and stores its return value
print(f"Squares: {result}")                              # [Line 1987] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1162
Write a Python program to show the effect of reusing the same variable in a function. Scope.
"""

# ======================================================================
# PROBLEM 1162 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def reuse_variable():                                    # [Line 1994]
    x = 5                                                # [Line 1995]
    x = x * 2                                            # [Line 1996] | Reuses the variable
    print(f"New value of x: {x}")                        # [Line 1997]

reuse_variable()                                         # [Line 1999] | FUNCTION CALL: Executes the function 'reuse_variable'

"""
Problem: 1163
Write a Python program to demonstrate variable scope in different functions. Scope.
"""

# ======================================================================
# PROBLEM 1163 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


x = 50                                                   # [Line 2006] | ASSIGNMENT: Creates variable 'x' and stores the result of '50' in it | DATA TYPE: Integer - A whole number: 50 | Global variable

def function_one():                                      # [Line 2008]
    print(f"Function One: {x}")                          # [Line 2009]

def function_two():                                      # [Line 2011]
    x = 40                                               # [Line 2012]
    print(f"Function Two: {x}")                          # [Line 2013]

function_one()                                           # [Line 2015] | FUNCTION CALL: Executes the function 'function_one'
function_two()                                           # [Line 2016] | FUNCTION CALL: Executes the function 'function_two'

"""
Problem: 1164
Write a Python program to demonstrate the use of `global` for modifying variables in different functions. Scope.
"""

# ======================================================================
# PROBLEM 1164 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


x = 10                                                   # [Line 2023] | ASSIGNMENT: Creates variable 'x' and stores the result of '10' in it | DATA TYPE: Integer - A whole number: 10 | Global variable

def function_one():                                      # [Line 2025]
    global x                                             # [Line 2026]
    x += 5                                               # [Line 2027]

def function_two():                                      # [Line 2029]
    global x                                             # [Line 2030]
    x -= 3                                               # [Line 2031]

function_one()                                           # [Line 2033] | FUNCTION CALL: Executes the function 'function_one'
function_two()                                           # [Line 2034] | FUNCTION CALL: Executes the function 'function_two'
print(f"Global variable x: {x}")                         # [Line 2035] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1165
Write a Python program to show how variable values are changed in nested functions. Scope.
"""

# ======================================================================
# PROBLEM 1165 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def outer_function():                                    # [Line 2042]
    x = 15                                               # [Line 2043] | Local variable in outer function
    def inner_function():                                # [Line 2044]
        nonlocal x                                       # [Line 2045]
        x += 10                                          # [Line 2046] | Modifies x in the outer function's scope
        print(f"Inner function: x = {x}")                # [Line 2047]
    inner_function()                                     # [Line 2048]
    print(f"Outer function: x = {x}")                    # [Line 2049]

outer_function()                                         # [Line 2051] | FUNCTION CALL: Executes the function 'outer_function'

"""
Problem: 1166
Write a Python program to demonstrate the use of variable arguments in functions. Scope.
"""

# ======================================================================
# PROBLEM 1166 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def print_arguments(*args):                              # [Line 2058]
    for arg in args:                                     # [Line 2059]
        print(arg)                                       # [Line 2060]

print_arguments(1, 2, 3, "hello", [1, 2, 3])             # [Line 2062] | FUNCTION CALL: Executes the function 'print_arguments' | ARGUMENTS: Passes 5 argument(s) to the function

"""
Problem: 1167
Write a Python program to show how the scope of a variable changes in a for loop. Scope.

"""

# ======================================================================
# PROBLEM 1167 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def loop_variable_scope():                               # [Line 2070]
    for i in range(3):                                   # [Line 2071]
        y = i                                            # [Line 2072] | Local variable in the loop
        print(f"In the loop: y = {y}")                   # [Line 2073]
    print(f"After the loop: y = {y}")                    # [Line 2074] | y still exists outside the loop

loop_variable_scope()                                    # [Line 2076] | FUNCTION CALL: Executes the function 'loop_variable_scope'

"""
Problem: 1168
Write a Python program to show the behavior of variables in global scope inside functions. Scope.
"""

# ======================================================================
# PROBLEM 1168 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def global_inside_function():                            # [Line 2083]
    print(f"Global variable x inside function: {x}")     # [Line 2084]

x = 10                                                   # [Line 2086] | ASSIGNMENT: Creates variable 'x' and stores the result of '10' in it | DATA TYPE: Integer - A whole number: 10 | Global variable
global_inside_function()                                 # [Line 2087] | FUNCTION CALL: Executes the function 'global_inside_function'

"""
Problem: 1169
Write a Python program to explain the difference between mutable and immutable variables in terms of scope. Scope.
"""

# ======================================================================
# PROBLEM 1169 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def test_mutability():                                   # [Line 2094]
    mutable = [1, 2, 3]                                  # [Line 2095] | Mutable variable (list)
    immutable = 10                                       # [Line 2096] | Immutable variable (integer)
    
    mutable[0] = 100                                     # [Line 2098] | Modifies the mutable variable
    immutable = 20                                       # [Line 2099] | This does not change the original variable
    
    print(f"Mutable variable: {mutable}")                # [Line 2101]
    print(f"Immutable variable: {immutable}")            # [Line 2102]

test_mutability()                                        # [Line 2104] | FUNCTION CALL: Executes the function 'test_mutability'

"""
Problem: 1170
Write a Python program to show the behavior of variables declared in a list comprehension. Scope.
"""

# ======================================================================
# PROBLEM 1170 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def list_comprehension_variable_scope():                 # [Line 2111]
    lst = [x**2 for x in range(5)]                       # [Line 2112] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    print(f"List comprehension result: {lst}")           # [Line 2113]

list_comprehension_variable_scope()                      # [Line 2115] | FUNCTION CALL: Executes the function 'list_comprehension_variable_scope'

"""
Problem: 1171
Write a Python program to show that function arguments can be variables with different scopes. Scope.
"""

# ======================================================================
# PROBLEM 1171 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def print_variable_in_function(x):                       # [Line 2122]
    y = x * 2                                            # [Line 2123] | Local variable inside function
    print(f"Function variable y: {y}")                   # [Line 2124]

z = 10                                                   # [Line 2126] | ASSIGNMENT: Creates variable 'z' and stores the result of '10' in it | DATA TYPE: Integer - A whole number: 10 | Global variable
print_variable_in_function(z)                            # [Line 2127] | FUNCTION CALL: Executes the function 'print_variable_in_function' | ARGUMENTS: Passes 1 argument(s) to the function

"""
Problem: 1172
Write a Python program to show that a variable in a for loop can be accessed outside the loop. Scope.
"""

# ======================================================================
# PROBLEM 1172 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def for_loop_variable_scope():                           # [Line 2134]
    for i in range(3):                                   # [Line 2135]
        x = i                                            # [Line 2136]
        print(f"In the loop: x = {x}")                   # [Line 2137]
    print(f"Outside the loop: x = {x}")                  # [Line 2138]

for_loop_variable_scope()                                # [Line 2140] | FUNCTION CALL: Executes the function 'for_loop_variable_scope'

"""
Problem: 1173
Write a Python program to demonstrate the impact of changing a global variable inside a function. Scope.
"""

# ======================================================================
# PROBLEM 1173 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


x = 100                                                  # [Line 2147] | ASSIGNMENT: Creates variable 'x' and stores the result of '100' in it | DATA TYPE: Integer - A whole number: 100

def change_global_variable():                            # [Line 2149]
    global x                                             # [Line 2150]
    x = 50                                               # [Line 2151]

change_global_variable()                                 # [Line 2153] | FUNCTION CALL: Executes the function 'change_global_variable'
print(f"Global x after modification: {x}")               # [Line 2154] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1174
Write a Python program to demonstrate variable accessibility within different levels of nested functions. Scope.
"""

# ======================================================================
# PROBLEM 1174 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def outer_function():                                    # [Line 2161]
    x = 5                                                # [Line 2162]
    def middle_function():                               # [Line 2163]
        y = 10                                           # [Line 2164]
        def inner_function():                            # [Line 2165]
            z = 15                                       # [Line 2166]
            print(f"Inner function: x = {x}, y = {y}, z = {z}")  # [Line 2167]
        inner_function()                                 # [Line 2168]
    middle_function()                                    # [Line 2169]

outer_function()                                         # [Line 2171] | FUNCTION CALL: Executes the function 'outer_function'

"""
Problem: 1175
Write a Python program to demonstrate how function arguments can access global variables. Scope.
"""

# ======================================================================
# PROBLEM 1175 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


x = 100                                                  # [Line 2178] | ASSIGNMENT: Creates variable 'x' and stores the result of '100' in it | DATA TYPE: Integer - A whole number: 100

def print_global_variable(x):                            # [Line 2180]
    print(f"Global x inside function: {x}")              # [Line 2181]

print_global_variable(x)                                 # [Line 2183] | FUNCTION CALL: Executes the function 'print_global_variable' | ARGUMENTS: Passes 1 argument(s) to the function

"""
Problem: 1176
Write a Python program to demonstrate the scope of variables in a recursive function. Scope.
"""

# ======================================================================
# PROBLEM 1176 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def factorial_recursive(n):                              # [Line 2190]
    if n == 1:                                           # [Line 2191] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).
        return 1                                         # [Line 2192]
    else:                                                # [Line 2193]
        return n * factorial_recursive(n - 1)            # [Line 2194]

result = factorial_recursive(5)                          # [Line 2196] | ASSIGNMENT: Creates variable 'result' and stores the result of 'factorial_recursive(5)' in it | FUNCTION CALL: Calls 'factorial_recursive()' and stores its return value
print(f"Factorial: {result}")                            # [Line 2197] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1177
Write a Python program to import the `math` module and calculate the square root of a number. Module.
"""

# ======================================================================
# PROBLEM 1177 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import math                                              # [Line 2204]

def calculate_square_root(number):                       # [Line 2206]
    return math.sqrt(number)                             # [Line 2207]

result = calculate_square_root(16)                       # [Line 2209] | ASSIGNMENT: Creates variable 'result' and stores the result of 'calculate_square_root(16)' in it | FUNCTION CALL: Calls 'calculate_square_root()' and stores its return value
print(f"The square root of 16 is {result}")              # [Line 2210] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1178
Write a Python program to use the `random` module to generate a random number between 1 and 100. Module.
"""

# ======================================================================
# PROBLEM 1178 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import random                                            # [Line 2217]

def generate_random_number():                            # [Line 2219]
    return random.randint(1, 100)                        # [Line 2220]

random_number = generate_random_number()                 # [Line 2222] | ASSIGNMENT: Creates variable 'random_number' and stores the result of 'generate_random_number()' in it | FUNCTION CALL: Calls 'generate_random_number()' and stores its return value
print(f"Random number between 1 and 100: {random_number}")  # [Line 2223] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1179
Write a Python program to use the `datetime` module to get the current date and time. Module.
"""

# ======================================================================
# PROBLEM 1179 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import datetime                                          # [Line 2230]

def current_datetime():                                  # [Line 2232]
    return datetime.datetime.now()                       # [Line 2233]

now = current_datetime()                                 # [Line 2235] | ASSIGNMENT: Creates variable 'now' and stores the result of 'current_datetime()' in it | FUNCTION CALL: Calls 'current_datetime()' and stores its return value
print(f"Current date and time: {now}")                   # [Line 2236] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1180
Write a Python program to use the `os` module to get the current working directory. Module.
"""

# ======================================================================
# PROBLEM 1180 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import os                                                # [Line 2243]

def current_working_directory():                         # [Line 2245]
    return os.getcwd()                                   # [Line 2246]

cwd = current_working_directory()                        # [Line 2248] | ASSIGNMENT: Creates variable 'cwd' and stores the result of 'current_working_directory()' in it | FUNCTION CALL: Calls 'current_working_directory()' and stores its return value
print(f"Current working directory: {cwd}")               # [Line 2249] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1181
Write a Python program to use the `sys` module to get the Python version. Module.
"""

# ======================================================================
# PROBLEM 1181 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import sys                                               # [Line 2256]

def python_version():                                    # [Line 2258]
    return sys.version                                   # [Line 2259]

version = python_version()                               # [Line 2261] | ASSIGNMENT: Creates variable 'version' and stores the result of 'python_version()' in it | FUNCTION CALL: Calls 'python_version()' and stores its return value
print(f"Python version: {version}")                      # [Line 2262] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1182
Write a Python program to use the `json` module to convert a Python dictionary to a JSON string. Module.
"""

# ======================================================================
# PROBLEM 1182 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import json                                              # [Line 2269]

def dict_to_json():                                      # [Line 2271]
    sample_dict = {"name": "Alice", "age": 30}           # [Line 2272]
    return json.dumps(sample_dict)                       # [Line 2273]

json_str = dict_to_json()                                # [Line 2275] | ASSIGNMENT: Creates variable 'json_str' and stores the result of 'dict_to_json()' in it | FUNCTION CALL: Calls 'dict_to_json()' and stores its return value
print(f"JSON string: {json_str}")                        # [Line 2276] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1183
Write a Python program to use the `re` module to check if a string contains a number. Module.
"""

# ======================================================================
# PROBLEM 1183 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import re                                                # [Line 2283]

def contains_number(string):                             # [Line 2285]
    return bool(re.search(r'\d', string))                # [Line 2286]

result = contains_number("Hello123")                     # [Line 2288] | ASSIGNMENT: Creates variable 'result' and stores the result of 'contains_number('Hello123')' in it | FUNCTION CALL: Calls 'contains_number()' and stores its return value
print(f"Does the string contain a number? {result}")     # [Line 2289] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1184
Write a Python program to use the `os` module to list all files in a directory. Module.
"""

# ======================================================================
# PROBLEM 1184 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import os                                                # [Line 2296]

def list_files(directory):                               # [Line 2298]
    return os.listdir(directory)                         # [Line 2299]

files = list_files(".")                                  # [Line 2301] | ASSIGNMENT: Creates variable 'files' and stores the result of 'list_files('.')' in it | FUNCTION CALL: Calls 'list_files()' and stores its return value
print(f"Files in the current directory: {files}")        # [Line 2302] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1185
Write a Python program to use the `math` module to calculate the factorial of a number. Module.
"""

# ======================================================================
# PROBLEM 1185 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import math                                              # [Line 2309]

def calculate_factorial(number):                         # [Line 2311]
    return math.factorial(number)                        # [Line 2312]

factorial_result = calculate_factorial(5)                # [Line 2314] | ASSIGNMENT: Creates variable 'factorial_result' and stores the result of 'calculate_factorial(5)' in it | FUNCTION CALL: Calls 'calculate_factorial()' and stores its return value
print(f"The factorial of 5 is {factorial_result}")       # [Line 2315] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1186
Write a Python program to use the `time` module to measure the execution time of a block of code. Module.
"""

# ======================================================================
# PROBLEM 1186 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import time                                              # [Line 2322]

def measure_time():                                      # [Line 2324]
    start_time = time.time()                             # [Line 2325]
    sum(range(1000000))                                  # [Line 2326]
    end_time = time.time()                               # [Line 2327]
    return end_time - start_time                         # [Line 2328]

execution_time = measure_time()                          # [Line 2330] | ASSIGNMENT: Creates variable 'execution_time' and stores the result of 'measure_time()' in it | FUNCTION CALL: Calls 'measure_time()' and stores its return value
print(f"Execution time: {execution_time} seconds")       # [Line 2331] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1187
Write a Python program to use the `calendar` module to check if a year is a leap year. Module.
"""

# ======================================================================
# PROBLEM 1187 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import calendar                                          # [Line 2338]

def is_leap_year(year):                                  # [Line 2340]
    return calendar.isleap(year)                         # [Line 2341]

result = is_leap_year(2024)                              # [Line 2343] | ASSIGNMENT: Creates variable 'result' and stores the result of 'is_leap_year(2024)' in it | FUNCTION CALL: Calls 'is_leap_year()' and stores its return value
print(f"Is 2024 a leap year? {result}")                  # [Line 2344] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1188
Write a Python program to use the `math` module to find the value of pi. Module.
"""

# ======================================================================
# PROBLEM 1188 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import math                                              # [Line 2351]

def get_pi_value():                                      # [Line 2353]
    return math.pi                                       # [Line 2354]

pi_value = get_pi_value()                                # [Line 2356] | ASSIGNMENT: Creates variable 'pi_value' and stores the result of 'get_pi_value()' in it | FUNCTION CALL: Calls 'get_pi_value()' and stores its return value
print(f"The value of pi is {pi_value}")                  # [Line 2357] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1189
Write a Python program to use the `random` module to shuffle a list of numbers. Module.
"""

# ======================================================================
# PROBLEM 1189 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import random                                            # [Line 2364]

def shuffle_list(lst):                                   # [Line 2366]
    random.shuffle(lst)                                  # [Line 2367]
    return lst                                           # [Line 2368]

numbers = [1, 2, 3, 4, 5]                                # [Line 2370] | ASSIGNMENT: Creates variable 'numbers' and stores the result of '[1, 2, 3, 4, 5]' in it | DATA TYPE: List - A mutable ordered collection. Contains 5 elements
shuffled_numbers = shuffle_list(numbers)                 # [Line 2371] | ASSIGNMENT: Creates variable 'shuffled_numbers' and stores the result of 'shuffle_list(numbers)' in it | FUNCTION CALL: Calls 'shuffle_list()' and stores its return value
print(f"Shuffled list: {shuffled_numbers}")              # [Line 2372] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1190
Write a Python program to use the `collections` module to count the occurrences of elements in a list. Module.
"""

# ======================================================================
# PROBLEM 1190 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import collections                                       # [Line 2379]

def count_occurrences(lst):                              # [Line 2381]
    return collections.Counter(lst)                      # [Line 2382]

numbers = [1, 2, 2, 3, 3, 3]                             # [Line 2384] | ASSIGNMENT: Creates variable 'numbers' and stores the result of '[1, 2, 2, 3, 3, 3]' in it | DATA TYPE: List - A mutable ordered collection. Contains 6 elements
occurrences = count_occurrences(numbers)                 # [Line 2385] | ASSIGNMENT: Creates variable 'occurrences' and stores the result of 'count_occurrences(numbers)' in it | FUNCTION CALL: Calls 'count_occurrences()' and stores its return value
print(f"Occurrences: {occurrences}")                     # [Line 2386] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1191
Write a Python program to use the `math` module to calculate the greatest common divisor (GCD) of two numbers. Module.
"""

# ======================================================================
# PROBLEM 1191 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import math                                              # [Line 2393]

def calculate_gcd(a, b):                                 # [Line 2395]
    return math.gcd(a, b)                                # [Line 2396]

gcd_result = calculate_gcd(48, 180)                      # [Line 2398] | ASSIGNMENT: Creates variable 'gcd_result' and stores the result of 'calculate_gcd(48, 180)' in it | FUNCTION CALL: Calls 'calculate_gcd()' and stores its return value
print(f"The GCD of 48 and 180 is {gcd_result}")          # [Line 2399] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1192
Write a Python program to use the `os` module to rename a file. Module.
"""

# ======================================================================
# PROBLEM 1192 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import os                                                # [Line 2406]

def rename_file(old_name, new_name):                     # [Line 2408]
    os.rename(old_name, new_name)                        # [Line 2409]

# Uncomment the following lines to test the rename_file function:
rename_file("old_file.txt", "new_file.txt")              # [Line 2412] | FUNCTION CALL: Executes the function 'rename_file' | ARGUMENTS: Passes 2 argument(s) to the function

"""
Problem: 1193
Write a Python program to use the `datetime` module to format the current date. Module.
"""

# ======================================================================
# PROBLEM 1193 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import datetime                                          # [Line 2419]

def format_current_date():                               # [Line 2421]
    return datetime.datetime.now().strftime("%Y-%m-%d")  # [Line 2422] | OPERATION - Performs a calculation or comparison

formatted_date = format_current_date()                   # [Line 2424] | ASSIGNMENT: Creates variable 'formatted_date' and stores the result of 'format_current_date()' in it | FUNCTION CALL: Calls 'format_current_date()' and stores its return value
print(f"Formatted current date: {formatted_date}")       # [Line 2425] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1194
Write a Python program to use the `json` module to parse a JSON string into a Python dictionary. Module.
"""

# ======================================================================
# PROBLEM 1194 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import json                                              # [Line 2432]

def json_to_dict(json_str):                              # [Line 2434]
    return json.loads(json_str)                          # [Line 2435]

json_str = '{"name": "Bob", "age": 25}'                  # [Line 2437] | ASSIGNMENT: Creates variable 'json_str' and stores the result of ''{"name": "Bob", "age": 25}'' in it | DATA TYPE: String - A sequence of characters. Length: 26
parsed_dict = json_to_dict(json_str)                     # [Line 2438] | ASSIGNMENT: Creates variable 'parsed_dict' and stores the result of 'json_to_dict(json_str)' in it | FUNCTION CALL: Calls 'json_to_dict()' and stores its return value
print(f"Parsed dictionary: {parsed_dict}")               # [Line 2439] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1195
Write a Python program to use the `random` module to select a random element from a list. Module.
"""

# ======================================================================
# PROBLEM 1195 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import random                                            # [Line 2446]

def select_random_element(lst):                          # [Line 2448]
    return random.choice(lst)                            # [Line 2449]

elements = [10, 20, 30, 40]                              # [Line 2451] | ASSIGNMENT: Creates variable 'elements' and stores the result of '[10, 20, 30, 40]' in it | DATA TYPE: List - A mutable ordered collection. Contains 4 elements
random_element = select_random_element(elements)         # [Line 2452] | ASSIGNMENT: Creates variable 'random_element' and stores the result of 'select_random_element(elements)' in it | FUNCTION CALL: Calls 'select_random_element()' and stores its return value
print(f"Random element: {random_element}")               # [Line 2453] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1196
Write a Python program to use the `math` module to round a floating-point number to the nearest integer. Module.
"""

# ======================================================================
# PROBLEM 1196 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import math                                              # [Line 2460]

def round_number(number):                                # [Line 2462]
    return round(number)                                 # [Line 2463]

rounded_value = round_number(7.5)                        # [Line 2465] | ASSIGNMENT: Creates variable 'rounded_value' and stores the result of 'round_number(7.5)' in it | FUNCTION CALL: Calls 'round_number()' and stores its return value
print(f"Rounded value of 7.5: {rounded_value}")          # [Line 2466] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1197
Write a Python program to create a dictionary and access its value using a key. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1197 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def access_value():                                      # [Line 2473]
    sample_dict = {"name": "Alice", "age": 30}           # [Line 2474]
    return sample_dict["name"]                           # [Line 2475]

result = access_value()                                  # [Line 2477] | ASSIGNMENT: Creates variable 'result' and stores the result of 'access_value()' in it | FUNCTION CALL: Calls 'access_value()' and stores its return value
print(f"Value accessed: {result}")                       # [Line 2478] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1198
Write a Python program to add a key-value pair to an existing dictionary. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1198 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def add_key_value():                                     # [Line 2485]
    sample_dict = {"name": "Alice", "age": 30}           # [Line 2486]
    sample_dict["city"] = "New York"                     # [Line 2487]
    return sample_dict                                   # [Line 2488]

updated_dict = add_key_value()                           # [Line 2490] | ASSIGNMENT: Creates variable 'updated_dict' and stores the result of 'add_key_value()' in it | FUNCTION CALL: Calls 'add_key_value()' and stores its return value
print(f"Updated dictionary: {updated_dict}")             # [Line 2491] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1199
Write a Python program to remove a key-value pair from a dictionary. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1199 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def remove_key():                                        # [Line 2498]
    sample_dict = {"name": "Alice", "age": 30, "city": "New York"}  # [Line 2499]
    del sample_dict["city"]                              # [Line 2500]
    return sample_dict                                   # [Line 2501]

updated_dict = remove_key()                              # [Line 2503] | ASSIGNMENT: Creates variable 'updated_dict' and stores the result of 'remove_key()' in it | FUNCTION CALL: Calls 'remove_key()' and stores its return value
print(f"Dictionary after removal: {updated_dict}")       # [Line 2504] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1200
Write a Python program to get all the keys from a dictionary. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1200 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def get_keys():                                          # [Line 2511]
    sample_dict = {"name": "Alice", "age": 30, "city": "New York"}  # [Line 2512]
    return sample_dict.keys()                            # [Line 2513]

keys = get_keys()                                        # [Line 2515] | ASSIGNMENT: Creates variable 'keys' and stores the result of 'get_keys()' in it | FUNCTION CALL: Calls 'get_keys()' and stores its return value
print(f"Keys in dictionary: {keys}")                     # [Line 2516] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1201
Write a Python program to get all the values from a dictionary. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1201 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def get_values():                                        # [Line 2523]
    sample_dict = {"name": "Alice", "age": 30, "city": "New York"}  # [Line 2524]
    return sample_dict.values()                          # [Line 2525]

values = get_values()                                    # [Line 2527] | ASSIGNMENT: Creates variable 'values' and stores the result of 'get_values()' in it | FUNCTION CALL: Calls 'get_values()' and stores its return value
print(f"Values in dictionary: {values}")                 # [Line 2528] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1202
Write a Python program to check if a key exists in a dictionary. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1202 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_key():                                         # [Line 2535]
    sample_dict = {"name": "Alice", "age": 30, "city": "New York"}  # [Line 2536]
    return "age" in sample_dict                          # [Line 2537]

result = check_key()                                     # [Line 2539] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_key()' in it | FUNCTION CALL: Calls 'check_key()' and stores its return value
print(f"Key exists: {result}")                           # [Line 2540] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1203
Write a Python program to get the value associated with a key, or return a default value if the key doesn't exist. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1203 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def get_value(dictionary, key, default=None):            # [Line 2547]
    
    return dictionary.get(key, default)                  # [Line 2549]

# Example usage:
my_dict = {'a': 1, 'b': 2, 'c': 3}                       # [Line 2552] | ASSIGNMENT: Creates variable 'my_dict' and stores the result of '{'a': 1, 'b': 2, 'c': 3}' in it
print(get_value(my_dict, 'a'))                           # [Line 2553] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Output: 1
print(get_value(my_dict, 'd', 'not found'))              # [Line 2554] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Output: not found

def get_value_or_default():                              # [Line 2556]
    sample_dict = {"name": "Alice", "age": 30}           # [Line 2557]
    return sample_dict.get("city", "Unknown")            # [Line 2558]

result = get_value_or_default()                          # [Line 2560] | ASSIGNMENT: Creates variable 'result' and stores the result of 'get_value_or_default()' in it | FUNCTION CALL: Calls 'get_value_or_default()' and stores its return value
print(f"Value: {result}")                                # [Line 2561] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1204
Write a Python program to clear all items from a dictionary. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1204 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def clear_dict():                                        # [Line 2568]
    sample_dict = {"name": "Alice", "age": 30, "city": "New York"}  # [Line 2569]
    sample_dict.clear()                                  # [Line 2570]
    return sample_dict                                   # [Line 2571]

updated_dict = clear_dict()                              # [Line 2573] | ASSIGNMENT: Creates variable 'updated_dict' and stores the result of 'clear_dict()' in it | FUNCTION CALL: Calls 'clear_dict()' and stores its return value
print(f"Dictionary after clearing: {updated_dict}")      # [Line 2574] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1205
Write a Python program to copy a dictionary. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1205 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def copy_dict():                                         # [Line 2581]
    sample_dict = {"name": "Alice", "age": 30}           # [Line 2582]
    return sample_dict.copy()                            # [Line 2583]

copied_dict = copy_dict()                                # [Line 2585] | ASSIGNMENT: Creates variable 'copied_dict' and stores the result of 'copy_dict()' in it | FUNCTION CALL: Calls 'copy_dict()' and stores its return value
print(f"Copied dictionary: {copied_dict}")               # [Line 2586] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1206
Write a Python program to merge two dictionaries. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1206 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def merge_dicts():                                       # [Line 2593]
    dict1 = {"name": "Alice", "age": 30}                 # [Line 2594]
    dict2 = {"city": "New York", "job": "Engineer"}      # [Line 2595]
    dict1.update(dict2)                                  # [Line 2596]
    return dict1                                         # [Line 2597]

merged_dict = merge_dicts()                              # [Line 2599] | ASSIGNMENT: Creates variable 'merged_dict' and stores the result of 'merge_dicts()' in it | FUNCTION CALL: Calls 'merge_dicts()' and stores its return value
print(f"Merged dictionary: {merged_dict}")               # [Line 2600] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1207
Write a Python program to iterate through all key-value pairs in a dictionary. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1207 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def iterate_dict():                                      # [Line 2607]
    sample_dict = {"name": "Alice", "age": 30, "city": "New York"}  # [Line 2608]
    for key, value in sample_dict.items():               # [Line 2609]
        print(f"{key}: {value}")                         # [Line 2610]

iterate_dict()                                           # [Line 2612] | FUNCTION CALL: Executes the function 'iterate_dict'

"""
Problem: 1208
Write a Python program to find the length of a dictionary. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1208 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def dict_length():                                       # [Line 2619]
    sample_dict = {"name": "Alice", "age": 30, "city": "New York"}  # [Line 2620]
    return len(sample_dict)                              # [Line 2621]

length = dict_length()                                   # [Line 2623] | ASSIGNMENT: Creates variable 'length' and stores the result of 'dict_length()' in it | FUNCTION CALL: Calls 'dict_length()' and stores its return value
print(f"Length of dictionary: {length}")                 # [Line 2624] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1209
Write a Python program to reverse the keys and values in a dictionary. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1209 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def reverse_dict():                                      # [Line 2631]
    sample_dict = {"name": "Alice", "age": 30, "city": "New York"}  # [Line 2632]
    return {v: k for k, v in sample_dict.items()}        # [Line 2633]

reversed_dict = reverse_dict()                           # [Line 2635] | ASSIGNMENT: Creates variable 'reversed_dict' and stores the result of 'reverse_dict()' in it | FUNCTION CALL: Calls 'reverse_dict()' and stores its return value
print(f"Reversed dictionary: {reversed_dict}")           # [Line 2636] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1210
Write a Python program to create a dictionary from two lists, one for keys and one for values. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1210 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def create_dict_from_lists():                            # [Line 2643]
    keys = ["name", "age", "city"]                       # [Line 2644]
    values = ["Alice", 30, "New York"]                   # [Line 2645]
    return dict(zip(keys, values))                       # [Line 2646]

created_dict = create_dict_from_lists()                  # [Line 2648] | ASSIGNMENT: Creates variable 'created_dict' and stores the result of 'create_dict_from_lists()' in it | FUNCTION CALL: Calls 'create_dict_from_lists()' and stores its return value
print(f"Created dictionary: {created_dict}")             # [Line 2649] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1211
Write a Python program to get the sum of all values in a dictionary. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1211 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def sum_values():                                        # [Line 2656]
    sample_dict = {"a": 10, "b": 20, "c": 30}            # [Line 2657]
    return sum(sample_dict.values())                     # [Line 2658]

total = sum_values()                                     # [Line 2660] | ASSIGNMENT: Creates variable 'total' and stores the result of 'sum_values()' in it | FUNCTION CALL: Calls 'sum_values()' and stores its return value
print(f"Sum of values: {total}")                         # [Line 2661] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1212
Write a Python program to filter a dictionary based on a condition. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1212 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def filter_dict():                                       # [Line 2668]
    sample_dict = {"name": "Alice", "age": 30, "city": "New York"}  # [Line 2669]
    return {key: value for key, value in sample_dict.items() if isinstance(value, str)}  # [Line 2670]

filtered_dict = filter_dict()                            # [Line 2672] | ASSIGNMENT: Creates variable 'filtered_dict' and stores the result of 'filter_dict()' in it | FUNCTION CALL: Calls 'filter_dict()' and stores its return value
print(f"Filtered dictionary: {filtered_dict}")           # [Line 2673] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1213
Write a Python program to find the maximum value in a dictionary. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1213 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def max_value():                                         # [Line 2680]
    sample_dict = {"a": 10, "b": 20, "c": 30}            # [Line 2681]
    return max(sample_dict.values())                     # [Line 2682]

max_val = max_value()                                    # [Line 2684] | ASSIGNMENT: Creates variable 'max_val' and stores the result of 'max_value()' in it | FUNCTION CALL: Calls 'max_value()' and stores its return value
print(f"Maximum value: {max_val}")                       # [Line 2685] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1214
Write a Python program to check if a dictionary is empty. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1214 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def is_dict_empty():                                     # [Line 2692]
    sample_dict = {}                                     # [Line 2693]
    return len(sample_dict) == 0                         # [Line 2694] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

result = is_dict_empty()                                 # [Line 2696] | ASSIGNMENT: Creates variable 'result' and stores the result of 'is_dict_empty()' in it | FUNCTION CALL: Calls 'is_dict_empty()' and stores its return value
print(f"Is dictionary empty? {result}")                  # [Line 2697] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1215
Write a Python program to remove all occurrences of a value in a dictionary. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1215 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def remove_value():                                      # [Line 2704]
    sample_dict = {"a": 10, "b": 20, "c": 10}            # [Line 2705]
    sample_dict = {k: v for k, v in sample_dict.items() if v != 10}  # [Line 2706]
    return sample_dict                                   # [Line 2707]

updated_dict = remove_value()                            # [Line 2709] | ASSIGNMENT: Creates variable 'updated_dict' and stores the result of 'remove_value()' in it | FUNCTION CALL: Calls 'remove_value()' and stores its return value
print(f"Dictionary after removal: {updated_dict}")       # [Line 2710] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1216
Write a Python program to find the key associated with a given value in a dictionary. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1216 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def find_key_by_value():                                 # [Line 2717]
    sample_dict = {"a": 10, "b": 20, "c": 30}            # [Line 2718]
    return [k for k, v in sample_dict.items() if v == 20]  # [Line 2719] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

key = find_key_by_value()                                # [Line 2721] | ASSIGNMENT: Creates variable 'key' and stores the result of 'find_key_by_value()' in it | FUNCTION CALL: Calls 'find_key_by_value()' and stores its return value
print(f"Key for value 20: {key}")                        # [Line 2722] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1217
Write a Python program to create a dictionary with default values using `defaultdict`. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1217 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from collections import defaultdict                      # [Line 2729]

def create_defaultdict():                                # [Line 2731]
    sample_dict = defaultdict(int)                       # [Line 2732]
    sample_dict["a"] += 1                                # [Line 2733]
    sample_dict["b"] += 2                                # [Line 2734]
    return dict(sample_dict)                             # [Line 2735]

default_dict = create_defaultdict()                      # [Line 2737] | ASSIGNMENT: Creates variable 'default_dict' and stores the result of 'create_defaultdict()' in it | FUNCTION CALL: Calls 'create_defaultdict()' and stores its return value
print(f"Default dictionary: {default_dict}")             # [Line 2738] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1218
Write a Python program to get the first key-value pair from a dictionary. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1218 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def first_key_value():                                   # [Line 2745]
    sample_dict = {"a": 10, "b": 20, "c": 30}            # [Line 2746]
    first_item = list(sample_dict.items())[0]            # [Line 2747]
    return first_item                                    # [Line 2748]

first_item = first_key_value()                           # [Line 2750] | ASSIGNMENT: Creates variable 'first_item' and stores the result of 'first_key_value()' in it | FUNCTION CALL: Calls 'first_key_value()' and stores its return value
print(f"First key-value pair: {first_item}")             # [Line 2751] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1219
Write a Python program to merge multiple dictionaries into one. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1219 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def merge_multiple_dicts():                              # [Line 2758]
    dict1 = {"a": 10, "b": 20}                           # [Line 2759]
    dict2 = {"c": 30, "d": 40}                           # [Line 2760]
    dict3 = {"e": 50}                                    # [Line 2761]
    merged_dict = {**dict1, **dict2, **dict3}            # [Line 2762] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    return merged_dict                                   # [Line 2763]

merged_dict = merge_multiple_dicts()                     # [Line 2765] | ASSIGNMENT: Creates variable 'merged_dict' and stores the result of 'merge_multiple_dicts()' in it | FUNCTION CALL: Calls 'merge_multiple_dicts()' and stores its return value
print(f"Merged dictionary: {merged_dict}")               # [Line 2766] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1220
Write a Python program to convert a list of tuples into a dictionary. Dictionary operations.
"""

# ======================================================================
# PROBLEM 1220 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def list_to_dict():                                      # [Line 2773]
    sample_list = [("a", 1), ("b", 2), ("c", 3)]         # [Line 2774]
    return dict(sample_list)                             # [Line 2775]

converted_dict = list_to_dict()                          # [Line 2777] | ASSIGNMENT: Creates variable 'converted_dict' and stores the result of 'list_to_dict()' in it | FUNCTION CALL: Calls 'list_to_dict()' and stores its return value
print(f"Converted dictionary: {converted_dict}")         # [Line 2778] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1221
Write a Python program to create a Path object using the `pathlib` module.
"""

# ======================================================================
# PROBLEM 1221 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 2785]

def create_path():                                       # [Line 2787]
    p = Path("example_directory")                        # [Line 2788]
    return p                                             # [Line 2789]

path = create_path()                                     # [Line 2791] | ASSIGNMENT: Creates variable 'path' and stores the result of 'create_path()' in it | FUNCTION CALL: Calls 'create_path()' and stores its return value
print(f"Created path: {path}")                           # [Line 2792] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1222
Write a Python program to check if a path exists using `pathlib`.
"""

# ======================================================================
# PROBLEM 1222 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 2799]

def check_path_exists():                                 # [Line 2801]
    p = Path("example_directory")                        # [Line 2802]
    return p.exists()                                    # [Line 2803]

exists = check_path_exists()                             # [Line 2805] | ASSIGNMENT: Creates variable 'exists' and stores the result of 'check_path_exists()' in it | FUNCTION CALL: Calls 'check_path_exists()' and stores its return value
print(f"Path exists: {exists}")                          # [Line 2806] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1223
Write a Python program to check if a path is a file using `pathlib`.
"""

# ======================================================================
# PROBLEM 1223 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 2813]

def check_if_file():                                     # [Line 2815]
    p = Path("example_file.txt")                         # [Line 2816]
    return p.is_file()                                   # [Line 2817]

is_file = check_if_file()                                # [Line 2819] | ASSIGNMENT: Creates variable 'is_file' and stores the result of 'check_if_file()' in it | FUNCTION CALL: Calls 'check_if_file()' and stores its return value
print(f"Is it a file? {is_file}")                        # [Line 2820] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1224
Write a Python program to check if a path is a directory using `pathlib`.
"""

# ======================================================================
# PROBLEM 1224 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 2827]

def check_if_directory():                                # [Line 2829]
    p = Path("example_directory")                        # [Line 2830]
    return p.is_dir()                                    # [Line 2831]

is_directory = check_if_directory()                      # [Line 2833] | ASSIGNMENT: Creates variable 'is_directory' and stores the result of 'check_if_directory()' in it | FUNCTION CALL: Calls 'check_if_directory()' and stores its return value
print(f"Is it a directory? {is_directory}")              # [Line 2834] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1225
Write a Python program to get the file name from a path using `pathlib`.
"""

# ======================================================================
# PROBLEM 1225 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 2841]

def get_file_name():                                     # [Line 2843]
    p = Path("example_directory/example_file.txt")       # [Line 2844]
    return p.name                                        # [Line 2845]

file_name = get_file_name()                              # [Line 2847] | ASSIGNMENT: Creates variable 'file_name' and stores the result of 'get_file_name()' in it | FUNCTION CALL: Calls 'get_file_name()' and stores its return value
print(f"File name: {file_name}")                         # [Line 2848] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1226
Write a Python program to get the parent directory of a path using `pathlib`.
"""

# ======================================================================
# PROBLEM 1226 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 2855]

def get_parent_directory():                              # [Line 2857]
    p = Path("example_directory/example_file.txt")       # [Line 2858]
    return p.parent                                      # [Line 2859]

parent_directory = get_parent_directory()                # [Line 2861] | ASSIGNMENT: Creates variable 'parent_directory' and stores the result of 'get_parent_directory()' in it | FUNCTION CALL: Calls 'get_parent_directory()' and stores its return value
print(f"Parent directory: {parent_directory}")           # [Line 2862] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1227
Write a Python program to join two paths using `pathlib`.
"""

# ======================================================================
# PROBLEM 1227 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 2869]

def join_paths():                                        # [Line 2871]
    p1 = Path("example_directory")                       # [Line 2872]
    p2 = "example_file.txt"                              # [Line 2873]
    return p1 / p2                                       # [Line 2874]

joined_path = join_paths()                               # [Line 2876] | ASSIGNMENT: Creates variable 'joined_path' and stores the result of 'join_paths()' in it | FUNCTION CALL: Calls 'join_paths()' and stores its return value
print(f"Joined path: {joined_path}")                     # [Line 2877] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1228
Write a Python program to get the file extension of a path using `pathlib`.
"""

# ======================================================================
# PROBLEM 1228 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 2884]

def get_file_extension():                                # [Line 2886]
    p = Path("example_file.txt")                         # [Line 2887]
    return p.suffix                                      # [Line 2888]

file_extension = get_file_extension()                    # [Line 2890] | ASSIGNMENT: Creates variable 'file_extension' and stores the result of 'get_file_extension()' in it | FUNCTION CALL: Calls 'get_file_extension()' and stores its return value
print(f"File extension: {file_extension}")               # [Line 2891] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1229
Write a Python program to get the size of a file using `pathlib`.
"""

# ======================================================================
# PROBLEM 1229 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 2898]

def get_file_size():                                     # [Line 2900]
    p = Path("example_file.txt")                         # [Line 2901]
    return p.stat().st_size                              # [Line 2902]

file_size = get_file_size()                              # [Line 2904] | ASSIGNMENT: Creates variable 'file_size' and stores the result of 'get_file_size()' in it | FUNCTION CALL: Calls 'get_file_size()' and stores its return value
print(f"File size: {file_size} bytes")                   # [Line 2905] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1230
Write a Python program to rename a file using `pathlib`.
"""

# ======================================================================
# PROBLEM 1230 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 2912]

def rename_file():                                       # [Line 2914]
    old_path = Path("old_file.txt")                      # [Line 2915]
    new_path = Path("new_file.txt")                      # [Line 2916]
    old_path.rename(new_path)                            # [Line 2917]
    return new_path                                      # [Line 2918]

renamed_file = rename_file()                             # [Line 2920] | ASSIGNMENT: Creates variable 'renamed_file' and stores the result of 'rename_file()' in it | FUNCTION CALL: Calls 'rename_file()' and stores its return value
print(f"Renamed file: {renamed_file}")                   # [Line 2921] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1231
Write a Python program to create a new directory using `pathlib`.
"""

# ======================================================================
# PROBLEM 1231 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 2928]

def create_directory():                                  # [Line 2930]
    p = Path("new_directory")                            # [Line 2931]
    p.mkdir(parents=True, exist_ok=True)                 # [Line 2932]
    return p                                             # [Line 2933]

created_directory = create_directory()                   # [Line 2935] | ASSIGNMENT: Creates variable 'created_directory' and stores the result of 'create_directory()' in it | FUNCTION CALL: Calls 'create_directory()' and stores its return value
print(f"Created directory: {created_directory}")         # [Line 2936] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1232
Write a Python program to remove a directory using `pathlib`.
"""

# ======================================================================
# PROBLEM 1232 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 2943]

def remove_directory():                                  # [Line 2945]
    p = Path("new_directory")                            # [Line 2946]
    p.rmdir()                                            # [Line 2947]
    return f"Directory {p} removed"                      # [Line 2948]

removed_directory = remove_directory()                   # [Line 2950] | ASSIGNMENT: Creates variable 'removed_directory' and stores the result of 'remove_directory()' in it | FUNCTION CALL: Calls 'remove_directory()' and stores its return value
print(removed_directory)                                 # [Line 2951] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1233
Write a Python program to remove a file using `pathlib`.
"""

# ======================================================================
# PROBLEM 1233 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 2958]

def remove_file():                                       # [Line 2960]
    p = Path("example_file.txt")                         # [Line 2961]
    p.unlink()                                           # [Line 2962]
    return f"File {p} removed"                           # [Line 2963]

removed_file = remove_file()                             # [Line 2965] | ASSIGNMENT: Creates variable 'removed_file' and stores the result of 'remove_file()' in it | FUNCTION CALL: Calls 'remove_file()' and stores its return value
print(removed_file)                                      # [Line 2966] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1234
Write a Python program to get the absolute path of a file using `pathlib`.
"""

# ======================================================================
# PROBLEM 1234 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 2973]

def get_absolute_path():                                 # [Line 2975]
    p = Path("example_file.txt")                         # [Line 2976]
    return p.resolve()                                   # [Line 2977]

absolute_path = get_absolute_path()                      # [Line 2979] | ASSIGNMENT: Creates variable 'absolute_path' and stores the result of 'get_absolute_path()' in it | FUNCTION CALL: Calls 'get_absolute_path()' and stores its return value
print(f"Absolute path: {absolute_path}")                 # [Line 2980] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1235
Write a Python program to check if a path is a symbolic link using `pathlib`.
"""

# ======================================================================
# PROBLEM 1235 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 2987]

def check_if_symlink():                                  # [Line 2989]
    p = Path("example_symlink")                          # [Line 2990]
    return p.is_symlink()                                # [Line 2991]

is_symlink = check_if_symlink()                          # [Line 2993] | ASSIGNMENT: Creates variable 'is_symlink' and stores the result of 'check_if_symlink()' in it | FUNCTION CALL: Calls 'check_if_symlink()' and stores its return value
print(f"Is it a symbolic link? {is_symlink}")            # [Line 2994] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1236
Write a Python program to create a symbolic link using `pathlib`.
"""

# ======================================================================
# PROBLEM 1236 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 3001]

def create_symlink():                                    # [Line 3003]
    target = Path("example_file.txt")                    # [Line 3004]
    symlink = Path("example_symlink")                    # [Line 3005]
    symlink.symlink_to(target)                           # [Line 3006]
    return symlink                                       # [Line 3007]

symlink = create_symlink()                               # [Line 3009] | ASSIGNMENT: Creates variable 'symlink' and stores the result of 'create_symlink()' in it | FUNCTION CALL: Calls 'create_symlink()' and stores its return value
print(f"Created symlink: {symlink}")                     # [Line 3010] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1237
Write a Python program to check if a path is a directory and if it contains files using `pathlib`.
"""

# ======================================================================
# PROBLEM 1237 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 3017]

def check_directory_and_files():                         # [Line 3019]
    p = Path("example_directory")                        # [Line 3020]
    if p.is_dir():                                       # [Line 3021]
        return [file.name for file in p.iterdir()]       # [Line 3022]
    return []                                            # [Line 3023]

directory_files = check_directory_and_files()            # [Line 3025] | ASSIGNMENT: Creates variable 'directory_files' and stores the result of 'check_directory_and_files()' in it | FUNCTION CALL: Calls 'check_directory_and_files()' and stores its return value
print(f"Files in directory: {directory_files}")          # [Line 3026] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1238
Write a Python program to get the last modified time of a file using `pathlib`.
"""

# ======================================================================
# PROBLEM 1238 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 3033]
import time                                              # [Line 3034]

def get_last_modified_time():                            # [Line 3036]
    p = Path("example_file.txt")                         # [Line 3037]
    timestamp = p.stat().st_mtime                        # [Line 3038]
    return time.ctime(timestamp)                         # [Line 3039]

last_modified_time = get_last_modified_time()            # [Line 3041] | ASSIGNMENT: Creates variable 'last_modified_time' and stores the result of 'get_last_modified_time()' in it | FUNCTION CALL: Calls 'get_last_modified_time()' and stores its return value
print(f"Last modified time: {last_modified_time}")       # [Line 3042] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1239
Write a Python program to get the directory name from a path using `pathlib`.
"""

# ======================================================================
# PROBLEM 1239 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 3049]

def get_directory_name():                                # [Line 3051]
    p = Path("example_directory/example_file.txt")       # [Line 3052]
    return p.parent.name                                 # [Line 3053]

directory_name = get_directory_name()                    # [Line 3055] | ASSIGNMENT: Creates variable 'directory_name' and stores the result of 'get_directory_name()' in it | FUNCTION CALL: Calls 'get_directory_name()' and stores its return value
print(f"Directory name: {directory_name}")               # [Line 3056] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1240
Write a Python program to check if a path is empty (no files) using `pathlib`.
"""

# ======================================================================
# PROBLEM 1240 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 3063]

def check_if_empty():                                    # [Line 3065]
    p = Path("example_directory")                        # [Line 3066]
    return len(list(p.iterdir())) == 0                   # [Line 3067] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

is_empty = check_if_empty()                              # [Line 3069] | ASSIGNMENT: Creates variable 'is_empty' and stores the result of 'check_if_empty()' in it | FUNCTION CALL: Calls 'check_if_empty()' and stores its return value
print(f"Is directory empty? {is_empty}")                 # [Line 3070] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1241
Write a Python program to iterate over all files in a directory using `pathlib`.
"""

# ======================================================================
# PROBLEM 1241 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 3077]

def iterate_files():                                     # [Line 3079]
    p = Path("example_directory")                        # [Line 3080]
    return [file.name for file in p.iterdir() if file.is_file()]  # [Line 3081]

files_in_directory = iterate_files()                     # [Line 3083] | ASSIGNMENT: Creates variable 'files_in_directory' and stores the result of 'iterate_files()' in it | FUNCTION CALL: Calls 'iterate_files()' and stores its return value
print(f"Files in directory: {files_in_directory}")       # [Line 3084] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1242
Write a Python program to find the path to the parent directory using `pathlib`.
"""

# ======================================================================
# PROBLEM 1242 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 3091]

def get_parent_directory():                              # [Line 3093]
    p = Path("example_directory/example_file.txt")       # [Line 3094]
    return p.parent.parent                               # [Line 3095]

parent_directory = get_parent_directory()                # [Line 3097] | ASSIGNMENT: Creates variable 'parent_directory' and stores the result of 'get_parent_directory()' in it | FUNCTION CALL: Calls 'get_parent_directory()' and stores its return value
print(f"Parent directory: {parent_directory}")           # [Line 3098] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1243
Write a Python program to check if a file has a certain extension using `pathlib`.
"""

# ======================================================================
# PROBLEM 1243 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 3105]

def check_file_extension():                              # [Line 3107]
    p = Path("example_file.txt")                         # [Line 3108]
    return p.suffix == ".txt"                            # [Line 3109] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

has_extension = check_file_extension()                   # [Line 3111] | ASSIGNMENT: Creates variable 'has_extension' and stores the result of 'check_file_extension()' in it | FUNCTION CALL: Calls 'check_file_extension()' and stores its return value
print(f"Has .txt extension? {has_extension}")            # [Line 3112] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1244
Write a Python program to get the file size using `pathlib` in human-readable format.
"""

# ======================================================================
# PROBLEM 1244 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 3119]

def get_human_readable_size():                           # [Line 3121]
    p = Path("example_file.txt")                         # [Line 3122]
    size_in_bytes = p.stat().st_size                     # [Line 3123]
    return f"{size_in_bytes / 1024:.2f} KB"              # [Line 3124]

size = get_human_readable_size()                         # [Line 3126] | ASSIGNMENT: Creates variable 'size' and stores the result of 'get_human_readable_size()' in it | FUNCTION CALL: Calls 'get_human_readable_size()' and stores its return value
print(f"File size: {size}")                              # [Line 3127] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1245
Write a Python program to change the current working directory using `pathlib`.
"""

# ======================================================================
# PROBLEM 1245 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 3134]

def change_working_directory():                          # [Line 3136]
    p = Path("example_directory")                        # [Line 3137]
    p.chdir()                                            # [Line 3138]
    return f"Changed working directory to: {p}"          # [Line 3139]

changed_directory = change_working_directory()           # [Line 3141] | ASSIGNMENT: Creates variable 'changed_directory' and stores the result of 'change_working_directory()' in it | FUNCTION CALL: Calls 'change_working_directory()' and stores its return value
print(changed_directory)                                 # [Line 3142] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1246
Write a Python program to check if two conditions are true using the `and` operator.
"""

# ======================================================================
# PROBLEM 1246 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_conditions():                                  # [Line 3149]
    a = 5                                                # [Line 3150]
    b = 10                                               # [Line 3151]
    return a > 3 and b < 15                              # [Line 3152]

result = check_conditions()                              # [Line 3154] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_conditions()' in it | FUNCTION CALL: Calls 'check_conditions()' and stores its return value
print(f"Both conditions are true: {result}")             # [Line 3155] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1247
Write a Python program to check if a number is between 10 and 20 (both inclusive) using the `and` operator.
"""

# ======================================================================
# PROBLEM 1247 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_range():                                       # [Line 3162]
    num = 15                                             # [Line 3163]
    return num >= 10 and num <= 20                       # [Line 3164]

result = check_range()                                   # [Line 3166] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_range()' in it | FUNCTION CALL: Calls 'check_range()' and stores its return value
print(f"Number is between 10 and 20: {result}")          # [Line 3167] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1248
Write a Python program to check if a string is non-empty and contains a specific character using the `and` operator.
"""

# ======================================================================
# PROBLEM 1248 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_string():                                      # [Line 3174]
    text = "hello"                                       # [Line 3175]
    return len(text) > 0 and "e" in text                 # [Line 3176]

result = check_string()                                  # [Line 3178] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_string()' in it | FUNCTION CALL: Calls 'check_string()' and stores its return value
print(f"String is non-empty and contains 'e': {result}")  # [Line 3179] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1249
Write a Python program to check if a number is divisible by both 3 and 5 using the `and` operator.
"""

# ======================================================================
# PROBLEM 1249 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def main(number):                                        # [Line 3186]
    return True if number % 3 == 0 and number % 5 == 0 else False  # [Line 3187] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
    
number = 15                                              # [Line 3189] | ASSIGNMENT: Creates variable 'number' and stores the result of '15' in it | DATA TYPE: Integer - A whole number: 15
main(number)                                             # [Line 3190] | FUNCTION CALL: Executes the function 'main' | ARGUMENTS: Passes 1 argument(s) to the function

def check_divisibility():                                # [Line 3192]
    num = 15                                             # [Line 3193]
    return num % 3 == 0 and num % 5 == 0                 # [Line 3194] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_divisibility()                            # [Line 3196] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_divisibility()' in it | FUNCTION CALL: Calls 'check_divisibility()' and stores its return value
print(f"Number is divisible by both 3 and 5: {result}")  # [Line 3197] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

def main(number):                                        # [Line 3199]
    return number % 3 == 0 and number % 5 == 0           # [Line 3200] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
    
number = 15                                              # [Line 3202] | ASSIGNMENT: Creates variable 'number' and stores the result of '15' in it | DATA TYPE: Integer - A whole number: 15
main(number)                                             # [Line 3203] | FUNCTION CALL: Executes the function 'main' | ARGUMENTS: Passes 1 argument(s) to the function

"""
Problem: 1250
Write a Python program to check if a list is non-empty and the first element is greater than 5 using the `and` operator.
"""

# ======================================================================
# PROBLEM 1250 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_list():                                        # [Line 3210]
    lst = [6, 2, 8]                                      # [Line 3211]
    return len(lst) > 0 and lst[0] > 5                   # [Line 3212]

result = check_list()                                    # [Line 3214] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_list()' in it | FUNCTION CALL: Calls 'check_list()' and stores its return value
print(f"List is non-empty and first element is greater than 5: {result}")  # [Line 3215] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1251
Write a Python program to check if a year is a leap year using the `and` operator.
"""

# ======================================================================
# PROBLEM 1251 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_leap_year():                                   # [Line 3222]
    year = 2024                                          # [Line 3223]
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)  # [Line 3224] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_leap_year()                               # [Line 3226] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_leap_year()' in it | FUNCTION CALL: Calls 'check_leap_year()' and stores its return value
print(f"Year is a leap year: {result}")                  # [Line 3227] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1252
Write a Python program to check if a number is positive, even, and divisible by 4 using the `and` operator.
"""

# ======================================================================
# PROBLEM 1252 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_number():                                      # [Line 3234]
    num = 8                                              # [Line 3235]
    return num > 0 and num % 2 == 0 and num % 4 == 0     # [Line 3236] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_number()                                  # [Line 3238] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_number()' in it | FUNCTION CALL: Calls 'check_number()' and stores its return value
print(f"Number is positive, even, and divisible by 4: {result}")  # [Line 3239] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1253
Write a Python program to check if a list contains exactly three elements, and the first element is greater than 5 using the `and` operator.
"""

# ======================================================================
# PROBLEM 1253 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_list_conditions():                             # [Line 3246]
    lst = [6, 2, 8]                                      # [Line 3247]
    return len(lst) == 3 and lst[0] > 5                  # [Line 3248] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

result = check_list_conditions()                         # [Line 3250] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_list_conditions()' in it | FUNCTION CALL: Calls 'check_list_conditions()' and stores its return value
print(f"List has three elements and first is greater than 5: {result}")  # [Line 3251] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1254
Write a Python program to check if a string is lowercase and its length is greater than 3 using the `and` operator.
"""

# ======================================================================
# PROBLEM 1254 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_string_conditions():                           # [Line 3258]
    text = "hello"                                       # [Line 3259]
    return text.islower() and len(text) > 3              # [Line 3260]

result = check_string_conditions()                       # [Line 3262] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_string_conditions()' in it | FUNCTION CALL: Calls 'check_string_conditions()' and stores its return value
print(f"String is lowercase and its length is greater than 3: {result}")  # [Line 3263] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1255
Write a Python program to check if a number is greater than 10 and less than 50 using the `and` operator.
"""

# ======================================================================
# PROBLEM 1255 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_range_conditions():                            # [Line 3270]
    num = 30                                             # [Line 3271]
    return num > 10 and num < 50                         # [Line 3272]

result = check_range_conditions()                        # [Line 3274] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_range_conditions()' in it | FUNCTION CALL: Calls 'check_range_conditions()' and stores its return value
print(f"Number is between 10 and 50: {result}")          # [Line 3275] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1256
Write a Python program to check if a number is both a multiple of 7 and 11 using the `and` operator.
"""

# ======================================================================
# PROBLEM 1256 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_multiples():                                   # [Line 3282]
    num = 77                                             # [Line 3283]
    return num % 7 == 0 and num % 11 == 0                # [Line 3284] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_multiples()                               # [Line 3286] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_multiples()' in it | FUNCTION CALL: Calls 'check_multiples()' and stores its return value
print(f"Number is a multiple of both 7 and 11: {result}")  # [Line 3287] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1257
Write a Python program to check if a person is eligible to vote, meaning the age is greater than 18 and they are a citizen, using the `and` operator.
"""

# ======================================================================
# PROBLEM 1257 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_voting_eligibility():                          # [Line 3294]
    age = 20                                             # [Line 3295]
    is_citizen = True                                    # [Line 3296]
    return age > 18 and is_citizen                       # [Line 3297]

result = check_voting_eligibility()                      # [Line 3299] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_voting_eligibility()' in it | FUNCTION CALL: Calls 'check_voting_eligibility()' and stores its return value
print(f"Person is eligible to vote: {result}")           # [Line 3300] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1258
Write a Python program to check if a number is divisible by 2, 3, and 5 using the `and` operator.
"""

# ======================================================================
# PROBLEM 1258 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_divisibility_all():                            # [Line 3307]
    num = 30                                             # [Line 3308]
    return num % 2 == 0 and num % 3 == 0 and num % 5 == 0  # [Line 3309] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_divisibility_all()                        # [Line 3311] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_divisibility_all()' in it | FUNCTION CALL: Calls 'check_divisibility_all()' and stores its return value
print(f"Number is divisible by 2, 3, and 5: {result}")   # [Line 3312] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1259
Write a Python program to check if a dictionary contains a specific key and the value is greater than a specified number using the `and` operator.
"""

# ======================================================================
# PROBLEM 1259 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_dict_conditions():                             # [Line 3319]
    sample_dict = {"age": 30, "city": "New York"}        # [Line 3320]
    return "age" in sample_dict and sample_dict["age"] > 25  # [Line 3321]

result = check_dict_conditions()                         # [Line 3323] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_dict_conditions()' in it | FUNCTION CALL: Calls 'check_dict_conditions()' and stores its return value
print(f"Dictionary contains 'age' and its value is greater than 25: {result}")  # [Line 3324] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1260
Write a Python program to check if a string is not empty and its length is an even number using the `and` operator.
"""

# ======================================================================
# PROBLEM 1260 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_string_length():                               # [Line 3331]
    text = "hello"                                       # [Line 3332]
    return len(text) > 0 and len(text) % 2 == 0          # [Line 3333] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_string_length()                           # [Line 3335] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_string_length()' in it | FUNCTION CALL: Calls 'check_string_length()' and stores its return value
print(f"String is not empty and its length is even: {result}")  # [Line 3336] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1261
Write a Python program to check if a number is within the range of 20 to 100 (inclusive) using the `and` operator.
"""

# ======================================================================
# PROBLEM 1261 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_range_inclusive():                             # [Line 3343]
    num = 50                                             # [Line 3344]
    return num >= 20 and num <= 100                      # [Line 3345]

result = check_range_inclusive()                         # [Line 3347] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_range_inclusive()' in it | FUNCTION CALL: Calls 'check_range_inclusive()' and stores its return value
print(f"Number is between 20 and 100 (inclusive): {result}")  # [Line 3348] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1262
Write a Python program to check if a number is divisible by both 2 and 7 using the `and` operator.
"""

# ======================================================================
# PROBLEM 1262 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_divisible_by_2_and_7():                        # [Line 3355]
    num = 14                                             # [Line 3356]
    return num % 2 == 0 and num % 7 == 0                 # [Line 3357] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_divisible_by_2_and_7()                    # [Line 3359] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_divisible_by_2_and_7()' in it | FUNCTION CALL: Calls 'check_divisible_by_2_and_7()' and stores its return value
print(f"Number is divisible by both 2 and 7: {result}")  # [Line 3360] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1263
Write a Python program to check if a number is negative and divisible by 5 using the `and` operator.
"""

# ======================================================================
# PROBLEM 1263 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_negative_and_divisible():                      # [Line 3367]
    num = -25                                            # [Line 3368]
    return num < 0 and num % 5 == 0                      # [Line 3369] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_negative_and_divisible()                  # [Line 3371] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_negative_and_divisible()' in it | FUNCTION CALL: Calls 'check_negative_and_divisible()' and stores its return value
print(f"Number is negative and divisible by 5: {result}")  # [Line 3372] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1264
Write a Python program to check if a string contains only digits and its length is greater than 5 using the `and` operator.
"""

# ======================================================================
# PROBLEM 1264 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_digit_string():                                # [Line 3379]
    text = "123456"                                      # [Line 3380]
    return text.isdigit() and len(text) > 5              # [Line 3381]

result = check_digit_string()                            # [Line 3383] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_digit_string()' in it | FUNCTION CALL: Calls 'check_digit_string()' and stores its return value
print(f"String contains only digits and its length is greater than 5: {result}")  # [Line 3384] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1265
Write a Python program to check if a number is a prime number and greater than 10 using the `and` operator.
"""

# ======================================================================
# PROBLEM 1265 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_prime_and_greater_than_10():                   # [Line 3391]
    num = 13                                             # [Line 3392]
    return num > 10 and all(num % i != 0 for i in range(2, num))  # [Line 3393] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_prime_and_greater_than_10()               # [Line 3395] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_prime_and_greater_than_10()' in it | FUNCTION CALL: Calls 'check_prime_and_greater_than_10()' and stores its return value
print(f"Number is prime and greater than 10: {result}")  # [Line 3396] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1266
Write a Python program to check if a number is odd and greater than 0 using the `and` operator.
"""

# ======================================================================
# PROBLEM 1266 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_odd_and_positive():                            # [Line 3403]
    num = 7                                              # [Line 3404]
    return num % 2 != 0 and num > 0                      # [Line 3405] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_odd_and_positive()                        # [Line 3407] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_odd_and_positive()' in it | FUNCTION CALL: Calls 'check_odd_and_positive()' and stores its return value
print(f"Number is odd and positive: {result}")           # [Line 3408] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1267
Write a Python program to check if a file exists and its size is greater than 100 KB using the `and` operator.
"""

# ======================================================================
# PROBLEM 1267 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 3415]

def check_file_exists_and_size():                        # [Line 3417]
    p = Path("example_file.txt")                         # [Line 3418]
    return p.exists() and p.stat().st_size > 100 * 1024  # [Line 3419]

result = check_file_exists_and_size()                    # [Line 3421] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_file_exists_and_size()' in it | FUNCTION CALL: Calls 'check_file_exists_and_size()' and stores its return value
print(f"File exists and its size is greater than 100 KB: {result}")  # [Line 3422] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1268
Write a Python program to check if a list contains exactly 5 elements and the last element is greater than 10 using the `and` operator.
"""

# ======================================================================
# PROBLEM 1268 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_list_length_and_last_element():                # [Line 3429]
    lst = [1, 2, 3, 4, 12]                               # [Line 3430]
    return len(lst) == 5 and lst[-1] > 10                # [Line 3431] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

result = check_list_length_and_last_element()            # [Line 3433] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_list_length_and_last_element()' in it | FUNCTION CALL: Calls 'check_list_length_and_last_element()' and stores its return value
print(f"List contains exactly 5 elements and last element is greater than 10: {result}")  # [Line 3434] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1269
Write a Python program to check if a number is between 1 and 10 (inclusive) and is odd using the `and` operator.
"""

# ======================================================================
# PROBLEM 1269 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_range_and_odd():                               # [Line 3441]
    num = 7                                              # [Line 3442]
    return num >= 1 and num <= 10 and num % 2 != 0       # [Line 3443] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_range_and_odd()                           # [Line 3445] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_range_and_odd()' in it | FUNCTION CALL: Calls 'check_range_and_odd()' and stores its return value
print(f"Number is between 1 and 10 and odd: {result}")   # [Line 3446] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1270
Write a Python program to check if at least one of two conditions is true using the `or` operator.
"""

# ======================================================================
# PROBLEM 1270 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_conditions():                                  # [Line 3453]
    a = 5                                                # [Line 3454]
    b = 10                                               # [Line 3455]
    return a > 10 or b < 15                              # [Line 3456]

result = check_conditions()                              # [Line 3458] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_conditions()' in it | FUNCTION CALL: Calls 'check_conditions()' and stores its return value
print(f"At least one condition is true: {result}")       # [Line 3459] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1271
Write a Python program to check if a number is either less than 10 or greater than 20 using the `or` operator.
"""

# ======================================================================
# PROBLEM 1271 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_range():                                       # [Line 3466]
    num = 5                                              # [Line 3467]
    return num < 10 or num > 20                          # [Line 3468]

result = check_range()                                   # [Line 3470] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_range()' in it | FUNCTION CALL: Calls 'check_range()' and stores its return value
print(f"Number is either less than 10 or greater than 20: {result}")  # [Line 3471] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1272
Write a Python program to check if a string is empty or contains a specific character using the `or` operator.
"""

# ======================================================================
# PROBLEM 1272 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_string():                                      # [Line 3478]
    text = "hello"                                       # [Line 3479]
    return len(text) == 0 or "e" in text                 # [Line 3480] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

result = check_string()                                  # [Line 3482] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_string()' in it | FUNCTION CALL: Calls 'check_string()' and stores its return value
print(f"String is empty or contains 'e': {result}")      # [Line 3483] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1273
Write a Python program to check if a number is divisible by 3 or 5 using the `or` operator.
"""

# ======================================================================
# PROBLEM 1273 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_divisibility():                                # [Line 3490]
    num = 9                                              # [Line 3491]
    return num % 3 == 0 or num % 5 == 0                  # [Line 3492] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_divisibility()                            # [Line 3494] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_divisibility()' in it | FUNCTION CALL: Calls 'check_divisibility()' and stores its return value
print(f"Number is divisible by 3 or 5: {result}")        # [Line 3495] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1274
Write a Python program to check if a list is empty or its first element is greater than 5 using the `or` operator.
"""

# ======================================================================
# PROBLEM 1274 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_list():                                        # [Line 3502]
    lst = [6, 2, 8]                                      # [Line 3503]
    return len(lst) == 0 or lst[0] > 5                   # [Line 3504] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

result = check_list()                                    # [Line 3506] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_list()' in it | FUNCTION CALL: Calls 'check_list()' and stores its return value
print(f"List is empty or its first element is greater than 5: {result}")  # [Line 3507] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1275
Write a Python program to check if a year is a leap year or divisible by 100 using the `or` operator.
"""

# ======================================================================
# PROBLEM 1275 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_leap_year():                                   # [Line 3514]
    year = 2024                                          # [Line 3515]
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)  # [Line 3516] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_leap_year()                               # [Line 3518] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_leap_year()' in it | FUNCTION CALL: Calls 'check_leap_year()' and stores its return value
print(f"Year is a leap year or divisible by 100: {result}")  # [Line 3519] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1276
Write a Python program to check if a number is positive or divisible by 7 using the `or` operator.
"""

# ======================================================================
# PROBLEM 1276 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_number():                                      # [Line 3526]
    num = 10                                             # [Line 3527]
    return num > 0 or num % 7 == 0                       # [Line 3528] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_number()                                  # [Line 3530] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_number()' in it | FUNCTION CALL: Calls 'check_number()' and stores its return value
print(f"Number is positive or divisible by 7: {result}")  # [Line 3531] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1277
Write a Python program to check if a string is lowercase or its length is greater than 3 using the `or` operator.
"""

# ======================================================================
# PROBLEM 1277 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_string_conditions():                           # [Line 3538]
    text = "HELLO"                                       # [Line 3539]
    return text.islower() or len(text) > 3               # [Line 3540]

result = check_string_conditions()                       # [Line 3542] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_string_conditions()' in it | FUNCTION CALL: Calls 'check_string_conditions()' and stores its return value
print(f"String is lowercase or its length is greater than 3: {result}")  # [Line 3543] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1278
Write a Python program to check if a number is between 10 and 50 or divisible by 7 using the `or` operator.
"""

# ======================================================================
# PROBLEM 1278 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_conditions():                                  # [Line 3550]
    num = 30                                             # [Line 3551]
    return (num >= 10 and num <= 50) or num % 7 == 0     # [Line 3552] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_conditions()                              # [Line 3554] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_conditions()' in it | FUNCTION CALL: Calls 'check_conditions()' and stores its return value
print(f"Number is between 10 and 50 or divisible by 7: {result}")  # [Line 3555] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1279
Write a Python program to check if a number is a multiple of 7 or 11 using the `or` operator.
"""

# ======================================================================
# PROBLEM 1279 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_multiples():                                   # [Line 3562]
    num = 77                                             # [Line 3563]
    return num % 7 == 0 or num % 11 == 0                 # [Line 3564] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_multiples()                               # [Line 3566] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_multiples()' in it | FUNCTION CALL: Calls 'check_multiples()' and stores its return value
print(f"Number is a multiple of 7 or 11: {result}")      # [Line 3567] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1280
Write a Python program to check if a person is eligible to vote, meaning the age is greater than 18 or they are a citizen, using the `or` operator.
"""

# ======================================================================
# PROBLEM 1280 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_voting_eligibility():                          # [Line 3574]
    age = 17                                             # [Line 3575]
    is_citizen = True                                    # [Line 3576]
    return age > 18 or is_citizen                        # [Line 3577]

result = check_voting_eligibility()                      # [Line 3579] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_voting_eligibility()' in it | FUNCTION CALL: Calls 'check_voting_eligibility()' and stores its return value
print(f"Person is eligible to vote: {result}")           # [Line 3580] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1281
Write a Python program to check if a number is divisible by 2 or 3 using the `or` operator.
"""

# ======================================================================
# PROBLEM 1281 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_divisibility_all():                            # [Line 3587]
    num = 9                                              # [Line 3588]
    return num % 2 == 0 or num % 3 == 0                  # [Line 3589] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_divisibility_all()                        # [Line 3591] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_divisibility_all()' in it | FUNCTION CALL: Calls 'check_divisibility_all()' and stores its return value
print(f"Number is divisible by 2 or 3: {result}")        # [Line 3592] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1282
Write a Python program to check if a dictionary contains a specific key or if the value is greater than a specified number using the `or` operator.
"""

# ======================================================================
# PROBLEM 1282 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_dict_conditions():                             # [Line 3599]
    sample_dict = {"age": 20, "city": "New York"}        # [Line 3600]
    return "name" in sample_dict or sample_dict["age"] > 25  # [Line 3601]

result = check_dict_conditions()                         # [Line 3603] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_dict_conditions()' in it | FUNCTION CALL: Calls 'check_dict_conditions()' and stores its return value
print(f"Dictionary contains 'name' or age is greater than 25: {result}")  # [Line 3604] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1283
Write a Python program to check if a string is empty or contains a number using the `or` operator.
"""

# ======================================================================
# PROBLEM 1283 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_string_empty_or_number():                      # [Line 3611]
    text = "hello123"                                    # [Line 3612]
    return len(text) == 0 or any(char.isdigit() for char in text)  # [Line 3613] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

result = check_string_empty_or_number()                  # [Line 3615] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_string_empty_or_number()' in it | FUNCTION CALL: Calls 'check_string_empty_or_number()' and stores its return value
print(f"String is empty or contains a number: {result}")  # [Line 3616] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1284
Write a Python program to check if a number is either negative or divisible by 3 using the `or` operator.
"""

# ======================================================================
# PROBLEM 1284 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_negative_or_divisible_by_3():                  # [Line 3623]
    num = -15                                            # [Line 3624]
    return num < 0 or num % 3 == 0                       # [Line 3625] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_negative_or_divisible_by_3()              # [Line 3627] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_negative_or_divisible_by_3()' in it | FUNCTION CALL: Calls 'check_negative_or_divisible_by_3()' and stores its return value
print(f"Number is negative or divisible by 3: {result}")  # [Line 3628] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1285
Write a Python program to check if a list is empty or contains more than 5 elements using the `or` operator.
"""

# ======================================================================
# PROBLEM 1285 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_list_conditions():                             # [Line 3635]
    lst = [1, 2, 3]                                      # [Line 3636]
    return len(lst) == 0 or len(lst) > 5                 # [Line 3637] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

result = check_list_conditions()                         # [Line 3639] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_list_conditions()' in it | FUNCTION CALL: Calls 'check_list_conditions()' and stores its return value
print(f"List is empty or contains more than 5 elements: {result}")  # [Line 3640] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1286
Write a Python program to check if a number is a perfect square or a perfect cube using the `or` operator.
"""

# ======================================================================
# PROBLEM 1286 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


import math                                              # [Line 3647]

def check_perfect_square_or_cube():                      # [Line 3649]
    num = 16                                             # [Line 3650]
    return math.isqrt(num) ** 2 == num or round(num ** (1 / 3)) ** 3 == num  # [Line 3651] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.

result = check_perfect_square_or_cube()                  # [Line 3653] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_perfect_square_or_cube()' in it | FUNCTION CALL: Calls 'check_perfect_square_or_cube()' and stores its return value
print(f"Number is a perfect square or cube: {result}")   # [Line 3654] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1287
Write a Python program to check if a string contains only letters or only digits using the `or` operator.
"""

# ======================================================================
# PROBLEM 1287 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_string_type():                                 # [Line 3661]
    text = "1234"                                        # [Line 3662]
    return text.isalpha() or text.isdigit()              # [Line 3663]

result = check_string_type()                             # [Line 3665] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_string_type()' in it | FUNCTION CALL: Calls 'check_string_type()' and stores its return value
print(f"String contains only letters or digits: {result}")  # [Line 3666] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1288
Write a Python program to check if a list contains exactly 3 elements or its sum is greater than 50 using the `or` operator.
"""

# ======================================================================
# PROBLEM 1288 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_list_conditions():                             # [Line 3673]
    lst = [6, 2, 8]                                      # [Line 3674]
    return len(lst) == 3 or sum(lst) > 50                # [Line 3675] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity).

result = check_list_conditions()                         # [Line 3677] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_list_conditions()' in it | FUNCTION CALL: Calls 'check_list_conditions()' and stores its return value
print(f"List has exactly 3 elements or its sum is greater than 50: {result}")  # [Line 3678] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1289
Write a Python program to check if a number is divisible by 2 or 5 using the `or` operator.
"""

# ======================================================================
# PROBLEM 1289 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_divisible_by_2_or_5():                         # [Line 3685]
    num = 10                                             # [Line 3686]
    return num % 2 == 0 or num % 5 == 0                  # [Line 3687] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_divisible_by_2_or_5()                     # [Line 3689] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_divisible_by_2_or_5()' in it | FUNCTION CALL: Calls 'check_divisible_by_2_or_5()' and stores its return value
print(f"Number is divisible by 2 or 5: {result}")        # [Line 3690] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1290
Write a Python program to check if a file exists or if it is writable using the `or` operator.
"""

# ======================================================================
# PROBLEM 1290 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


from pathlib import Path                                 # [Line 3697]

def check_file_conditions():                             # [Line 3699]
    p = Path("example_file.txt")                         # [Line 3700]
    return p.exists() or p.is_file()                     # [Line 3701]

result = check_file_conditions()                         # [Line 3703] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_file_conditions()' in it | FUNCTION CALL: Calls 'check_file_conditions()' and stores its return value
print(f"File exists or is a file: {result}")             # [Line 3704] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1291
Write a Python program to check if a number is greater than 100 or less than 10 using the `or` operator.
"""

# ======================================================================
# PROBLEM 1291 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_number():                                      # [Line 3711]
    num = 5                                              # [Line 3712]
    return num > 100 or num < 10                         # [Line 3713]

result = check_number()                                  # [Line 3715] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_number()' in it | FUNCTION CALL: Calls 'check_number()' and stores its return value
print(f"Number is greater than 100 or less than 10: {result}")  # [Line 3716] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1292
Write a Python program to check if a string is uppercase or its length is even using the `or` operator.
"""

# ======================================================================
# PROBLEM 1292 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_string_conditions():                           # [Line 3723]
    text = "HELLO"                                       # [Line 3724]
    return text.isupper() or len(text) % 2 == 0          # [Line 3725] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_string_conditions()                       # [Line 3727] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_string_conditions()' in it | FUNCTION CALL: Calls 'check_string_conditions()' and stores its return value
print(f"String is uppercase or its length is even: {result}")  # [Line 3728] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1293
Write a Python program to check if a list is non-empty or its last element is greater than 10 using the `or` operator.
"""

# ======================================================================
# PROBLEM 1293 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_list_conditions():                             # [Line 3735]
    lst = [6, 2, 8]                                      # [Line 3736]
    return len(lst) > 0 or lst[-1] > 10                  # [Line 3737]

result = check_list_conditions()                         # [Line 3739] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_list_conditions()' in it | FUNCTION CALL: Calls 'check_list_conditions()' and stores its return value
print(f"List is non-empty or its last element is greater than 10: {result}")  # [Line 3740] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1294
Write a Python program to check if a number is even or divisible by 3 using the `or` operator.
"""

# ======================================================================
# PROBLEM 1294 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_even_or_divisible_by_3():                      # [Line 3747]
    num = 8                                              # [Line 3748]
    return num % 2 == 0 or num % 3 == 0                  # [Line 3749] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

result = check_even_or_divisible_by_3()                  # [Line 3751] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_even_or_divisible_by_3()' in it | FUNCTION CALL: Calls 'check_even_or_divisible_by_3()' and stores its return value
print(f"Number is even or divisible by 3: {result}")     # [Line 3752] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

"""
Problem: 1295
Write a Python program to check if a string is not empty or contains the character 'a' using the `or` operator.
"""

# ======================================================================
# PROBLEM 1295 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def check_string():                                      # [Line 3759]
    text = "apple"                                       # [Line 3760]
    return len(text) > 0 or "a" in text                  # [Line 3761]

result = check_string()                                  # [Line 3763] | ASSIGNMENT: Creates variable 'result' and stores the result of 'check_string()' in it | FUNCTION CALL: Calls 'check_string()' and stores its return value
print(f"String is not empty or contains 'a': {result}")  # [Line 3764] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user

""" 
Problem: 1296
Write a Python program to extract all words starting with a capital letter.
"""

# ======================================================================
# PROBLEM 1296 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


s = "Hello World, this is Python."                       # [Line 3771] | ASSIGNMENT: Creates variable 's' and stores the result of ''Hello World, this is Python.'' in it | DATA TYPE: String - A sequence of characters. Length: 28
words = re.findall(r"\b[A-Z][a-z]*\b", s)                # [Line 3772] | ASSIGNMENT: Creates variable 'words' and stores the result of 're.findall('\\b[A-Z][a-z]*\\b', s)' in it | FUNCTION CALL: Calls 're.findall()' and stores its return value
print(words)                                             # [Line 3773] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: ['Hello', 'World', 'Python']


""" 
Problem: 1297
Write a Python program to split a string by commas and optional whitespace.
"""

# ======================================================================
# PROBLEM 1297 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


s = "apple, banana ,cherry , grape"                      # [Line 3781] | ASSIGNMENT: Creates variable 's' and stores the result of ''apple, banana ,cherry , grape'' in it | DATA TYPE: String - A sequence of characters. Length: 29
items = re.split(r"\s*,\s*", s)                          # [Line 3782] | ASSIGNMENT: Creates variable 'items' and stores the result of 're.split('\\s*,\\s*', s)' in it | FUNCTION CALL: Calls 're.split()' and stores its return value
print(items)                                             # [Line 3783] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: ['apple', 'banana', 'cherry', 'grape']


""" 
Problem: 1298
Write a Python program to check if a password contains at least one digit, one uppercase, and one lowercase letter.
"""

# ======================================================================
# PROBLEM 1298 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


password = "Password123"                                 # [Line 3791] | ASSIGNMENT: Creates variable 'password' and stores the result of ''Password123'' in it | DATA TYPE: String - A sequence of characters. Length: 11
match = bool(re.search(r"[A-Z]", password) and re.search(r"[a-z]", password) and re.search(r"\d", password))  # [Line 3792] | ASSIGNMENT: Creates variable 'match' and stores the result of 'bool(re.search('[A-Z]', password) and re.search('[a-z]', password) and re.search('\\d', password))' in it | FUNCTION CALL: Calls 'bool()' and stores its return value
print(match)                                             # [Line 3793] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: True


""" 
Problem: 1299
Write a Python program to find all email addresses in a text.
"""

# ======================================================================
# PROBLEM 1299 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "Send to alice@example.com and bob99@domain.co.uk"  # [Line 3801] | ASSIGNMENT: Creates variable 'text' and stores the result of ''Send to alice@example.com and bob99@domain.co.uk'' in it | DATA TYPE: String - A sequence of characters. Length: 48
emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)  # [Line 3802] | ASSIGNMENT: Creates variable 'emails' and stores the result of 're.findall('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+', text)' in it | FUNCTION CALL: Calls 're.findall()' and stores its return value
print(emails)                                            # [Line 3803] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: ['alice@example.com', 'bob99@domain.co.uk']


""" 
Problem: 1300
Write a Python program to extract hashtags from a tweet.
"""

# ======================================================================
# PROBLEM 1300 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


tweet = "Loving the                                      # [Line 3811] | Python #coding journey!"
hashtags = re.findall(r"                                 # [Line 3812] | \w+", tweet)
print(hashtags)                                          # [Line 3813] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: ['#Python', '#coding']


""" 
Problem: 1301
Write a Python program to extract domain names from URLs.
"""

# ======================================================================
# PROBLEM 1301 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "Visit us at https://example.com or http://test.org"  # [Line 3821] | FLOOR DIVISION (//) - Divides two numbers and returns the largest integer less than or equal to the result. Example: 7 // 2 = 3 (not 3.5). This is useful for integer division when you don't want decimal results. | ASSIGNMENT: Creates variable 'text' and stores the result of ''Visit us at https://example.com or http://test.org'' in it | DATA TYPE: String - A sequence of characters. Length: 50
domains = re.findall(r"https?://([\w.-]+)", text)        # [Line 3822] | SLICING OPERATION - Extracts a portion of the sequence | FLOOR DIVISION (//) - Divides two numbers and returns the largest integer less than or equal to the result. Example: 7 // 2 = 3 (not 3.5). This is useful for integer division when you don't want decimal results. | ASSIGNMENT: Creates variable 'domains' and stores the result of 're.findall('https?://([\\w.-]+)', text)' in it | FUNCTION CALL: Calls 're.findall()' and stores its return value
print(domains)                                           # [Line 3823] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: ['example.com', 'test.org']


""" 
Problem: 1302
Write a Python program to validate if a string is a valid IPv4 address.
"""

# ======================================================================
# PROBLEM 1302 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


ip = "192.168.1.1"                                       # [Line 3831] | ASSIGNMENT: Creates variable 'ip' and stores the result of ''192.168.1.1'' in it | DATA TYPE: String - A sequence of characters. Length: 11
pattern = r"^(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(?!$)){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$"  # [Line 3832] | ASSIGNMENT: Creates variable 'pattern' and stores the result of ''^(25[0-5]|2[0-4]\\d|1\\d\\d|[1-9]?\\d)(\\.(?!$)){3}(25[0-5]|2[0-4]\\d|1\\d\\d|[1-9]?\\d)$'' in it | DATA TYPE: String - A sequence of characters. Length: 80
match = bool(re.fullmatch(pattern, ip))                  # [Line 3833] | ASSIGNMENT: Creates variable 'match' and stores the result of 'bool(re.fullmatch(pattern, ip))' in it | FUNCTION CALL: Calls 'bool()' and stores its return value
print(match)                                             # [Line 3834] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: True


""" 
Problem: 1303
Write a Python program to remove all punctuation from a string.
"""

# ======================================================================
# PROBLEM 1303 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "Hello, world! Python is great."                  # [Line 3842] | ASSIGNMENT: Creates variable 'text' and stores the result of ''Hello, world! Python is great.'' in it | DATA TYPE: String - A sequence of characters. Length: 30
clean = re.sub(r"[^\w\s]", "", text)                     # [Line 3843] | ASSIGNMENT: Creates variable 'clean' and stores the result of 're.sub('[^\\w\\s]', '', text)' in it | FUNCTION CALL: Calls 're.sub()' and stores its return value
print(clean)                                             # [Line 3844] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: Hello world Python is great


""" 
Problem: 1304
Write a Python program to match a string that starts with a vowel.
"""

# ======================================================================
# PROBLEM 1304 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


s = "apple"                                              # [Line 3852] | ASSIGNMENT: Creates variable 's' and stores the result of ''apple'' in it | DATA TYPE: String - A sequence of characters. Length: 5
match = bool(re.match(r"^[aeiouAEIOU]", s))              # [Line 3853] | ASSIGNMENT: Creates variable 'match' and stores the result of 'bool(re.match('^[aeiouAEIOU]', s))' in it | FUNCTION CALL: Calls 'bool()' and stores its return value
print(match)                                             # [Line 3854] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: True


""" 
Problem: 1305
Write a Python program to extract all valid dates in the format YYYY-MM-DD.
"""

# ======================================================================
# PROBLEM 1305 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "Events: 2024-06-01, 2025-07-04, 99-01-01"        # [Line 3862] | ASSIGNMENT: Creates variable 'text' and stores the result of ''Events: 2024-06-01, 2025-07-04, 99-01-01'' in it | DATA TYPE: String - A sequence of characters. Length: 40
dates = re.findall(r"\b\d{4}-\d{2}-\d{2}\b", text)       # [Line 3863] | ASSIGNMENT: Creates variable 'dates' and stores the result of 're.findall('\\b\\d{4}-\\d{2}-\\d{2}\\b', text)' in it | FUNCTION CALL: Calls 're.findall()' and stores its return value
print(dates)                                             # [Line 3864] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: ['2024-06-01', '2025-07-04']


""" 
Problem: 1306
Write a Python program to validate a hexadecimal color code.
"""

# ======================================================================
# PROBLEM 1306 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


color = "                                                # [Line 3872] | 1a2b3c"
match = bool(re.fullmatch(r"                             # [Line 3873] | ([A-Fa-f0-9]{6})", color))
print(match)                                             # [Line 3874] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: True


""" 
Problem: 1307
Write a Python program to extract all words that end with 'ing'.
"""

# ======================================================================
# PROBLEM 1307 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "I am running and jumping while singing."         # [Line 3882] | ASSIGNMENT: Creates variable 'text' and stores the result of ''I am running and jumping while singing.'' in it | DATA TYPE: String - A sequence of characters. Length: 39
words = re.findall(r"\b\w+ing\b", text)                  # [Line 3883] | ASSIGNMENT: Creates variable 'words' and stores the result of 're.findall('\\b\\w+ing\\b', text)' in it | FUNCTION CALL: Calls 're.findall()' and stores its return value
print(words)                                             # [Line 3884] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: ['running', 'jumping', 'singing']


""" 
Problem: 1308
Write a Python program to extract the file extension from a filename.
"""

# ======================================================================
# PROBLEM 1308 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


filename = "document.pdf"                                # [Line 3892] | ASSIGNMENT: Creates variable 'filename' and stores the result of ''document.pdf'' in it | DATA TYPE: String - A sequence of characters. Length: 12
ext = re.search(r"\.(\w+)$", filename).group(1)          # [Line 3893] | ASSIGNMENT: Creates variable 'ext' and stores the result of 're.search('\\.(\\w+)$', filename).group(1)' in it | FUNCTION CALL: Calls 're.search('\\.(\\w+)$', filename).group()' and stores its return value
print(ext)                                               # [Line 3894] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: pdf


""" 
Problem: 1309
Write a Python program to find duplicated words in a sentence.
"""

# ======================================================================
# PROBLEM 1309 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "This is is a test test string"                   # [Line 3902] | ASSIGNMENT: Creates variable 'text' and stores the result of ''This is is a test test string'' in it | DATA TYPE: String - A sequence of characters. Length: 29
duplicates = re.findall(r"\b(\w+)\s+\1\b", text)         # [Line 3903] | ASSIGNMENT: Creates variable 'duplicates' and stores the result of 're.findall('\\b(\\w+)\\s+\\1\\b', text)' in it | FUNCTION CALL: Calls 're.findall()' and stores its return value
print(duplicates)                                        # [Line 3904] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected output: ['is', 'test']

""" 
Problem: 1310
Write a Python program to extract all capitalized words from a paragraph.
"""

# ======================================================================
# PROBLEM 1310 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "Alice and Bob went to New York City on Monday."  # [Line 3911] | ASSIGNMENT: Creates variable 'text' and stores the result of ''Alice and Bob went to New York City on Monday.'' in it | DATA TYPE: String - A sequence of characters. Length: 46
capitalized = re.findall(r"\b[A-Z][a-z]*\b", text)       # [Line 3912] | ASSIGNMENT: Creates variable 'capitalized' and stores the result of 're.findall('\\b[A-Z][a-z]*\\b', text)' in it | FUNCTION CALL: Calls 're.findall()' and stores its return value
print(capitalized)                                       # [Line 3913] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: ['Alice', 'Bob', 'New', 'York', 'City', 'Monday']


""" 
Problem: 1311
Write a Python program to validate a time in 24-hour format (HH:MM).
"""

# ======================================================================
# PROBLEM 1311 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


time = "23:59"                                           # [Line 3921] | ASSIGNMENT: Creates variable 'time' and stores the result of ''23:59'' in it | DATA TYPE: String - A sequence of characters. Length: 5
match = bool(re.fullmatch(r"([01]\d|2[0-3]):[0-5]\d", time))  # [Line 3922] | SLICING OPERATION - Extracts a portion of the sequence | ASSIGNMENT: Creates variable 'match' and stores the result of 'bool(re.fullmatch('([01]\\d|2[0-3]):[0-5]\\d', time))' in it | FUNCTION CALL: Calls 'bool()' and stores its return value
print(match)                                             # [Line 3923] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1312
Write a Python program to extract all integers and floats from a string.
"""

# ======================================================================
# PROBLEM 1312 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "The temperature is 21.5C, and humidity is 60% with 0.25 inches rain."  # [Line 3931] | OPERATION - Performs a calculation or comparison | ASSIGNMENT: Creates variable 'text' and stores the result of ''The temperature is 21.5C, and humidity is 60% with 0.25 inches rain.'' in it | DATA TYPE: String - A sequence of characters. Length: 68
numbers = re.findall(r"\d+\.\d+|\d+", text)              # [Line 3932] | ASSIGNMENT: Creates variable 'numbers' and stores the result of 're.findall('\\d+\\.\\d+|\\d+', text)' in it | FUNCTION CALL: Calls 're.findall()' and stores its return value
print(numbers)                                           # [Line 3933] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: ['21.5', '60', '0.25']


""" 
Problem: 1313
Write a Python program to remove leading zeros from an IP address.
"""

# ======================================================================
# PROBLEM 1313 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


ip = "192.168.001.001"                                   # [Line 3941] | ASSIGNMENT: Creates variable 'ip' and stores the result of ''192.168.001.001'' in it | DATA TYPE: String - A sequence of characters. Length: 15
clean_ip = re.sub(r"\b0+(\d)", r"\1", ip)                # [Line 3942] | ASSIGNMENT: Creates variable 'clean_ip' and stores the result of 're.sub('\\b0+(\\d)', '\\1', ip)' in it | FUNCTION CALL: Calls 're.sub()' and stores its return value
print(clean_ip)                                          # [Line 3943] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 192.168.1.1


""" 
Problem: 1314
Write a Python program to check if a string is a valid slug (only lowercase letters, numbers, hyphens).
"""

# ======================================================================
# PROBLEM 1314 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


slug = "python-tips-101"                                 # [Line 3951] | ASSIGNMENT: Creates variable 'slug' and stores the result of ''python-tips-101'' in it | DATA TYPE: String - A sequence of characters. Length: 15
match = bool(re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", slug))  # [Line 3952] | ASSIGNMENT: Creates variable 'match' and stores the result of 'bool(re.fullmatch('[a-z0-9]+(-[a-z0-9]+)*', slug))' in it | FUNCTION CALL: Calls 'bool()' and stores its return value
print(match)                                             # [Line 3953] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1315
Write a Python program to extract content inside parentheses.
"""

# ======================================================================
# PROBLEM 1315 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "This is a sample (with content) and (another one)."  # [Line 3961] | ASSIGNMENT: Creates variable 'text' and stores the result of ''This is a sample (with content) and (another one).'' in it | DATA TYPE: String - A sequence of characters. Length: 50
content = re.findall(r"\((.*?)\)", text)                 # [Line 3962] | ASSIGNMENT: Creates variable 'content' and stores the result of 're.findall('\\((.*?)\\)', text)' in it | FUNCTION CALL: Calls 're.findall()' and stores its return value
print(content)                                           # [Line 3963] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: ['with content', 'another one']


""" 
Problem: 1316
Write a Python program to match all valid HTML tags in a string.
"""

# ======================================================================
# PROBLEM 1316 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


html = "<div><p>Hello</p></div>"                         # [Line 3971] | ASSIGNMENT: Creates variable 'html' and stores the result of ''<div><p>Hello</p></div>'' in it | DATA TYPE: String - A sequence of characters. Length: 23
tags = re.findall(r"<[^>]+>", html)                      # [Line 3972] | ASSIGNMENT: Creates variable 'tags' and stores the result of 're.findall('<[^>]+>', html)' in it | FUNCTION CALL: Calls 're.findall()' and stores its return value
print(tags)                                              # [Line 3973] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: ['<div>', '<p>', '</p>', '</div>']


""" 
Problem: 1317
Write a Python program to validate if a string is a US ZIP code (5 digits).
"""

# ======================================================================
# PROBLEM 1317 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


zip_code = "12345"                                       # [Line 3981] | ASSIGNMENT: Creates variable 'zip_code' and stores the result of ''12345'' in it | DATA TYPE: String - A sequence of characters. Length: 5
match = bool(re.fullmatch(r"\d{5}", zip_code))           # [Line 3982] | ASSIGNMENT: Creates variable 'match' and stores the result of 'bool(re.fullmatch('\\d{5}', zip_code))' in it | FUNCTION CALL: Calls 'bool()' and stores its return value
print(match)                                             # [Line 3983] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1318
Write a Python program to find all abbreviations like "U.S.A." in a string.
"""

# ======================================================================
# PROBLEM 1318 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "Some examples: U.S.A. and E.U."                  # [Line 3991] | ASSIGNMENT: Creates variable 'text' and stores the result of ''Some examples: U.S.A. and E.U.'' in it | DATA TYPE: String - A sequence of characters. Length: 30
abbreviations = re.findall(r"(?:[A-Z]\.){2,}", text)     # [Line 3992] | SLICING OPERATION - Extracts a portion of the sequence | ASSIGNMENT: Creates variable 'abbreviations' and stores the result of 're.findall('(?:[A-Z]\\.){2,}', text)' in it | FUNCTION CALL: Calls 're.findall()' and stores its return value
print(abbreviations)                                     # [Line 3993] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: ['U.S.A.', 'E.U.']


""" 
Problem: 1319
Write a Python program to count how many times a word appears in a case-insensitive way.
"""

# ======================================================================
# PROBLEM 1319 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "Python is great. I love python because PYTHON is powerful."  # [Line 4001] | ASSIGNMENT: Creates variable 'text' and stores the result of ''Python is great. I love python because PYTHON is powerful.'' in it | DATA TYPE: String - A sequence of characters. Length: 58
count = len(re.findall(r"\bpython\b", text, re.IGNORECASE))  # [Line 4002] | ASSIGNMENT: Creates variable 'count' and stores the result of 'len(re.findall('\\bpython\\b', text, re.IGNORECASE))' in it | FUNCTION CALL: Calls 'len()' and stores its return value
print(count)                                             # [Line 4003] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 3


""" 
Problem: 1320
Write a Python program to replace duplicate spaces with a single space.
"""

# ======================================================================
# PROBLEM 1320 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "This    is  a    spaced   sentence."             # [Line 4011] | ASSIGNMENT: Creates variable 'text' and stores the result of ''This    is  a    spaced   sentence.'' in it | DATA TYPE: String - A sequence of characters. Length: 35
clean = re.sub(r"\s{2,}", " ", text)                     # [Line 4012] | ASSIGNMENT: Creates variable 'clean' and stores the result of 're.sub('\\s{2,}', ' ', text)' in it | FUNCTION CALL: Calls 're.sub()' and stores its return value
print(clean)                                             # [Line 4013] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: "This is a spaced sentence."


""" 
Problem: 1321
Write a Python program to validate a MAC address (e.g., 00:1A:2B:3C:4D:5E).
"""

# ======================================================================
# PROBLEM 1321 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


mac = "00:1A:2B:3C:4D:5E"                                # [Line 4021] | ASSIGNMENT: Creates variable 'mac' and stores the result of ''00:1A:2B:3C:4D:5E'' in it | DATA TYPE: String - A sequence of characters. Length: 17
match = bool(re.fullmatch(r"([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}", mac))  # [Line 4022] | SLICING OPERATION - Extracts a portion of the sequence | ASSIGNMENT: Creates variable 'match' and stores the result of 'bool(re.fullmatch('([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}', mac))' in it | FUNCTION CALL: Calls 'bool()' and stores its return value
print(match)                                             # [Line 4023] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1322
Write a Python program to extract the username from an email address.
"""

# ======================================================================
# PROBLEM 1322 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


email = "john.doe@example.com"                           # [Line 4031] | ASSIGNMENT: Creates variable 'email' and stores the result of ''john.doe@example.com'' in it | DATA TYPE: String - A sequence of characters. Length: 20
username = re.match(r"([^@]+)", email).group(1)          # [Line 4032] | ASSIGNMENT: Creates variable 'username' and stores the result of 're.match('([^@]+)', email).group(1)' in it | FUNCTION CALL: Calls 're.match('([^@]+)', email).group()' and stores its return value
print(username)                                          # [Line 4033] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: john.doe


""" 
Problem: 1323
Write a Python program to insert commas into a numeric string every three digits.
"""

# ======================================================================
# PROBLEM 1323 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


num = "1000000"                                          # [Line 4041] | ASSIGNMENT: Creates variable 'num' and stores the result of ''1000000'' in it | DATA TYPE: String - A sequence of characters. Length: 7
formatted = re.sub(r"(?<=\d)(?=(\d{3})+$)", ",", num)    # [Line 4042] | ASSIGNMENT: Creates variable 'formatted' and stores the result of 're.sub('(?<=\\d)(?=(\\d{3})+$)', ',', num)' in it | FUNCTION CALL: Calls 're.sub()' and stores its return value
print(formatted)                                         # [Line 4043] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 1,000,000


""" 
Problem: 1324
Write a Python program to extract all valid Twitter handles from a string.
"""

# ======================================================================
# PROBLEM 1324 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "Follow @python, @realpython, and @openai!"       # [Line 4051] | ASSIGNMENT: Creates variable 'text' and stores the result of ''Follow @python, @realpython, and @openai!'' in it | DATA TYPE: String - A sequence of characters. Length: 41
handles = re.findall(r"@\w+", text)                      # [Line 4052] | ASSIGNMENT: Creates variable 'handles' and stores the result of 're.findall('@\\w+', text)' in it | FUNCTION CALL: Calls 're.findall()' and stores its return value
print(handles)                                           # [Line 4053] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: ['@python', '@realpython', '@openai']


""" 
Problem: 1325
Write a Python program to check if a string contains any emoji.
"""

# ======================================================================
# PROBLEM 1325 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


emoji_text = "I love 🍕 and 🐍"                            # [Line 4061] | ASSIGNMENT: Creates variable 'emoji_text' and stores the result of ''I love 🍕 and 🐍'' in it | DATA TYPE: String - A sequence of characters. Length: 14
match = bool(re.search(r"[\U0001F600-\U0001F64F]", emoji_text))  # [Line 4062] | ASSIGNMENT: Creates variable 'match' and stores the result of 'bool(re.search('[\\U0001F600-\\U0001F64F]', emoji_text))' in it | FUNCTION CALL: Calls 'bool()' and stores its return value
print(match)                                             # [Line 4063] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1326
Write a Python program to extract time values in 12-hour format with AM/PM.
"""

# ======================================================================
# PROBLEM 1326 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "Meeting at 02:30 PM and dinner at 07:45 AM."     # [Line 4071] | ASSIGNMENT: Creates variable 'text' and stores the result of ''Meeting at 02:30 PM and dinner at 07:45 AM.'' in it | DATA TYPE: String - A sequence of characters. Length: 43
times = re.findall(r"\b\d{2}:\d{2} [AP]M\b", text)       # [Line 4072] | SLICING OPERATION - Extracts a portion of the sequence | ASSIGNMENT: Creates variable 'times' and stores the result of 're.findall('\\b\\d{2}:\\d{2} [AP]M\\b', text)' in it | FUNCTION CALL: Calls 're.findall()' and stores its return value
print(times)                                             # [Line 4073] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: ['02:30 PM', '07:45 AM']


""" 
Problem: 1327
Write a Python program to extract prices with a dollar sign.
"""

# ======================================================================
# PROBLEM 1327 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


text = "Items: $20.99, $3.50, $100"                      # [Line 4081] | ASSIGNMENT: Creates variable 'text' and stores the result of ''Items: $20.99, $3.50, $100'' in it | DATA TYPE: String - A sequence of characters. Length: 26
prices = re.findall(r"\$\d+(\.\d{2})?", text)            # [Line 4082] | ASSIGNMENT: Creates variable 'prices' and stores the result of 're.findall('\\$\\d+(\\.\\d{2})?', text)' in it | FUNCTION CALL: Calls 're.findall()' and stores its return value
print(prices)                                            # [Line 4083] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: ['$20.99', '$3.50', '$100']


""" 
Problem: 1328
Write a Python program to detect duplicate characters in a string using regex.
"""

# ======================================================================
# PROBLEM 1328 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


s = "programming"                                        # [Line 4091] | ASSIGNMENT: Creates variable 's' and stores the result of ''programming'' in it | DATA TYPE: String - A sequence of characters. Length: 11
duplicates = re.findall(r"(\w)(?=.*\1)", s)              # [Line 4092] | ASSIGNMENT: Creates variable 'duplicates' and stores the result of 're.findall('(\\w)(?=.*\\1)', s)' in it | FUNCTION CALL: Calls 're.findall()' and stores its return value
print(set(duplicates))                                   # [Line 4093] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {'r', 'g', 'm'}


""" 
Problem: 1329
Write a Python program to validate a hexadecimal number (e.g., 0x1A3F).
"""

# ======================================================================
# PROBLEM 1329 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


hex_num = "0x1A3F"                                       # [Line 4101] | ASSIGNMENT: Creates variable 'hex_num' and stores the result of ''0x1A3F'' in it | DATA TYPE: String - A sequence of characters. Length: 6
match = bool(re.fullmatch(r"0x[0-9A-Fa-f]+", hex_num))   # [Line 4102] | ASSIGNMENT: Creates variable 'match' and stores the result of 'bool(re.fullmatch('0x[0-9A-Fa-f]+', hex_num))' in it | FUNCTION CALL: Calls 'bool()' and stores its return value
print(match)                                             # [Line 4103] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1330
Write a Python program to extract quoted strings (single or double quotes).
"""

# ======================================================================
# PROBLEM 1330 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

import re                                                # [Line 4110]

text = "'Hello', she said. \"How are you?\""             # [Line 4112] | ASSIGNMENT: Creates variable 'text' and stores the result of ''\'Hello\', she said. "How are you?"'' in it | DATA TYPE: String - A sequence of characters. Length: 33
quotes = re.findall(r"(['\"])(.*?)\1", text)             # [Line 4113] | ASSIGNMENT: Creates variable 'quotes' and stores the result of 're.findall('([\'\\"])(.*?)\\1', text)' in it | FUNCTION CALL: Calls 're.findall()' and stores its return value
print([q[1] for q in quotes])                            # [Line 4114] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: ['Hello', 'How are you?']


""" 
Problem: 1331
Write a Python program to check if a variable is an integer using isinstance().
"""

# ======================================================================
# PROBLEM 1331 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


x = 10                                                   # [Line 4122] | ASSIGNMENT: Creates variable 'x' and stores the result of '10' in it | DATA TYPE: Integer - A whole number: 10
print(isinstance(x, int))                                # [Line 4123] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1332
Write a Python program to check if a variable is a string using isinstance().
"""

# ======================================================================
# PROBLEM 1332 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


x = "hello"                                              # [Line 4131] | ASSIGNMENT: Creates variable 'x' and stores the result of ''hello'' in it | DATA TYPE: String - A sequence of characters. Length: 5
print(isinstance(x, str))                                # [Line 4132] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1333
Write a Python program to check if a variable is a float using isinstance().
"""

# ======================================================================
# PROBLEM 1333 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


x = 3.14                                                 # [Line 4140] | ASSIGNMENT: Creates variable 'x' and stores the result of '3.14' in it
print(isinstance(x, float))                              # [Line 4141] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1334
Write a Python program to check if a variable is a list using isinstance().
"""

# ======================================================================
# PROBLEM 1334 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


x = [1, 2, 3]                                            # [Line 4149] | ASSIGNMENT: Creates variable 'x' and stores the result of '[1, 2, 3]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(isinstance(x, list))                               # [Line 4150] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1335
Write a Python program to check if a variable is a dictionary using isinstance().
"""

# ======================================================================
# PROBLEM 1335 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


x = {"a": 1}                                             # [Line 4158] | ASSIGNMENT: Creates variable 'x' and stores the result of '{'a': 1}' in it
print(isinstance(x, dict))                               # [Line 4159] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1336
Write a Python program to check if a variable is either int or float using isinstance().
"""

# ======================================================================
# PROBLEM 1336 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


x = 10.0                                                 # [Line 4167] | ASSIGNMENT: Creates variable 'x' and stores the result of '10.0' in it
print(isinstance(x, (int, float)))                       # [Line 4168] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1337
Write a Python program to check if each element in a list is a string.
"""

# ======================================================================
# PROBLEM 1337 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


lst = ["apple", "banana", "cherry"]                      # [Line 4176] | ASSIGNMENT: Creates variable 'lst' and stores the result of '['apple', 'banana', 'cherry']' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
result = all(isinstance(item, str) for item in lst)      # [Line 4177] | ASSIGNMENT: Creates variable 'result' and stores the result of 'all((isinstance(item, str) for item in lst))' in it | FUNCTION CALL: Calls 'all()' and stores its return value
print(result)                                            # [Line 4178] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1338
Write a Python program to filter only integers from a mixed list using isinstance().
"""

# ======================================================================
# PROBLEM 1338 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


items = [1, "a", 3.5, 4, "b"]                            # [Line 4186] | ASSIGNMENT: Creates variable 'items' and stores the result of '[1, 'a', 3.5, 4, 'b']' in it | DATA TYPE: List - A mutable ordered collection. Contains 5 elements
ints = [x for x in items if isinstance(x, int)]          # [Line 4187] | ASSIGNMENT: Creates variable 'ints' and stores the result of '[x for x in items if isinstance(x, int)]' in it
print(ints)                                              # [Line 4188] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [1, 4]


""" 
Problem: 1339
Write a Python program to filter only strings from a mixed list using isinstance().
"""

# ======================================================================
# PROBLEM 1339 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


items = [1, "apple", 2.5, "banana"]                      # [Line 4196] | ASSIGNMENT: Creates variable 'items' and stores the result of '[1, 'apple', 2.5, 'banana']' in it | DATA TYPE: List - A mutable ordered collection. Contains 4 elements
strings = [x for x in items if isinstance(x, str)]       # [Line 4197] | ASSIGNMENT: Creates variable 'strings' and stores the result of '[x for x in items if isinstance(x, str)]' in it
print(strings)                                           # [Line 4198] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: ['apple', 'banana']


""" 
Problem: 1340
Write a Python program to check if an object is a boolean using isinstance().
"""

# ======================================================================
# PROBLEM 1340 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


x = True                                                 # [Line 4206] | ASSIGNMENT: Creates variable 'x' and stores the result of 'True' in it | DATA TYPE: Integer - A whole number: True
print(isinstance(x, bool))                               # [Line 4207] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1341
Write a Python program to check if a variable is a tuple using isinstance().
"""

# ======================================================================
# PROBLEM 1341 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


x = (1, 2, 3)                                            # [Line 4215] | ASSIGNMENT: Creates variable 'x' and stores the result of '(1, 2, 3)' in it | DATA TYPE: Tuple - An immutable ordered collection. Contains 3 elements
print(isinstance(x, tuple))                              # [Line 4216] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1342
Write a Python program to check if an object is not a string using isinstance().
"""

# ======================================================================
# PROBLEM 1342 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


x = 42                                                   # [Line 4224] | ASSIGNMENT: Creates variable 'x' and stores the result of '42' in it | DATA TYPE: Integer - A whole number: 42
print(not isinstance(x, str))                            # [Line 4225] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1343
Write a Python program to define a function that accepts only strings using isinstance().
"""

# ======================================================================
# PROBLEM 1343 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def greet(name):                                         # [Line 4233]
    if not isinstance(name, str):                        # [Line 4234]
        return "Invalid input"                           # [Line 4235]
    return f"Hello, {name}!"                             # [Line 4236]

print(greet("Alice"))                                    # [Line 4238] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: Hello, Alice!
print(greet(123))                                        # [Line 4239] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: Invalid input


""" 
Problem: 1344
Write a Python program to check if all elements in a nested list are lists.
"""

# ======================================================================
# PROBLEM 1344 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


nested = [[1, 2], [3, 4]]                                # [Line 4247] | ASSIGNMENT: Creates variable 'nested' and stores the result of '[[1, 2], [3, 4]]' in it | DATA TYPE: List - A mutable ordered collection. Contains 2 elements
result = all(isinstance(sub, list) for sub in nested)    # [Line 4248] | ASSIGNMENT: Creates variable 'result' and stores the result of 'all((isinstance(sub, list) for sub in nested))' in it | FUNCTION CALL: Calls 'all()' and stores its return value
print(result)                                            # [Line 4249] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1345
Write a Python program to separate strings and numbers from a list.
"""

# ======================================================================
# PROBLEM 1345 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


mixed = [1, "one", 2, "two", 3, "three"]                 # [Line 4257] | ASSIGNMENT: Creates variable 'mixed' and stores the result of '[1, 'one', 2, 'two', 3, 'three']' in it | DATA TYPE: List - A mutable ordered collection. Contains 6 elements
nums = [x for x in mixed if isinstance(x, int)]          # [Line 4258] | ASSIGNMENT: Creates variable 'nums' and stores the result of '[x for x in mixed if isinstance(x, int)]' in it
words = [x for x in mixed if isinstance(x, str)]         # [Line 4259] | ASSIGNMENT: Creates variable 'words' and stores the result of '[x for x in mixed if isinstance(x, str)]' in it
print(nums)                                              # [Line 4260] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [1, 2, 3]
print(words)                                             # [Line 4261] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: ['one', 'two', 'three']


""" 
Problem: 1346
Write a Python program to validate argument types in a function.
"""

# ======================================================================
# PROBLEM 1346 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


def multiply(a, b):                                      # [Line 4269]
    if not all(isinstance(x, (int, float)) for x in (a, b)):  # [Line 4270]
        return "Invalid input"                           # [Line 4271]
    return a * b                                         # [Line 4272]

print(multiply(2, 3))                                    # [Line 4274] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 6
print(multiply(2, "x"))                                  # [Line 4275] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: Invalid input


""" 
Problem: 1347
Write a Python program to check if a variable is a set using isinstance().
"""

# ======================================================================
# PROBLEM 1347 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


x = {1, 2, 3}                                            # [Line 4283] | ASSIGNMENT: Creates variable 'x' and stores the result of '{1, 2, 3}' in it
print(isinstance(x, set))                                # [Line 4284] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1348
Write a Python program to validate that dictionary keys are all strings.
"""

# ======================================================================
# PROBLEM 1348 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


d = {"a": 1, "b": 2}                                     # [Line 4292] | ASSIGNMENT: Creates variable 'd' and stores the result of '{'a': 1, 'b': 2}' in it
result = all(isinstance(k, str) for k in d.keys())       # [Line 4293] | ASSIGNMENT: Creates variable 'result' and stores the result of 'all((isinstance(k, str) for k in d.keys()))' in it | FUNCTION CALL: Calls 'all()' and stores its return value
print(result)                                            # [Line 4294] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1349
Write a Python program to validate that dictionary values are all integers.
"""

# ======================================================================
# PROBLEM 1349 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


d = {"x": 1, "y": 2}                                     # [Line 4302] | ASSIGNMENT: Creates variable 'd' and stores the result of '{'x': 1, 'y': 2}' in it
result = all(isinstance(v, int) for v in d.values())     # [Line 4303] | ASSIGNMENT: Creates variable 'result' and stores the result of 'all((isinstance(v, int) for v in d.values()))' in it | FUNCTION CALL: Calls 'all()' and stores its return value
print(result)                                            # [Line 4304] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1350
Write a Python program to check if an object is a file-like object (has read method).
"""

# ======================================================================
# PROBLEM 1350 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:


class FakeFile:                                          # [Line 4312]
    def read(self):                                      # [Line 4313]
        pass                                             # [Line 4314]

f = FakeFile()                                           # [Line 4316] | ASSIGNMENT: Creates variable 'f' and stores the result of 'FakeFile()' in it | FUNCTION CALL: Calls 'FakeFile()' and stores its return value
print(hasattr(f, "read") and callable(f.read))           # [Line 4317] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True

""" 
Problem: 1351
Write a Python program to remove a key from a dictionary using pop() and print the updated dictionary.
"""

# ======================================================================
# PROBLEM 1351 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

d = {"a": 1, "b": 2, "c": 3}                             # [Line 4323] | ASSIGNMENT: Creates variable 'd' and stores the result of '{'a': 1, 'b': 2, 'c': 3}' in it
d.pop("b")                                               # [Line 4324] | FUNCTION CALL: Executes the function 'd.pop' | ARGUMENTS: Passes 1 argument(s) to the function
print(d)                                                 # [Line 4325] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {'a': 1, 'c': 3}


""" 
Problem: 1352
Write a Python program to use pop() to retrieve the value of a key from a dictionary.
"""

# ======================================================================
# PROBLEM 1352 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

d = {"a": 10, "b": 20}                                   # [Line 4332] | ASSIGNMENT: Creates variable 'd' and stores the result of '{'a': 10, 'b': 20}' in it
value = d.pop("a")                                       # [Line 4333] | ASSIGNMENT: Creates variable 'value' and stores the result of 'd.pop('a')' in it | FUNCTION CALL: Calls 'd.pop()' and stores its return value
print(value)                                             # [Line 4334] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 10


""" 
Problem: 1353
Write a Python program to use pop() on a list to remove the last item.
"""

# ======================================================================
# PROBLEM 1353 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = [1, 2, 3, 4]                                       # [Line 4341] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[1, 2, 3, 4]' in it | DATA TYPE: List - A mutable ordered collection. Contains 4 elements
lst.pop()                                                # [Line 4342] | FUNCTION CALL: Executes the function 'lst.pop'
print(lst)                                               # [Line 4343] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [1, 2, 3]


""" 
Problem: 1354
Write a Python program to remove a specific index from a list using pop().
"""

# ======================================================================
# PROBLEM 1354 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = [10, 20, 30, 40]                                   # [Line 4350] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[10, 20, 30, 40]' in it | DATA TYPE: List - A mutable ordered collection. Contains 4 elements
lst.pop(1)                                               # [Line 4351] | FUNCTION CALL: Executes the function 'lst.pop' | ARGUMENTS: Passes 1 argument(s) to the function
print(lst)                                               # [Line 4352] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [10, 30, 40]


""" 
Problem: 1355
Write a Python program to capture and print the element removed using pop() from a list.
"""

# ======================================================================
# PROBLEM 1355 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = [5, 6, 7]                                          # [Line 4359] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[5, 6, 7]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
removed = lst.pop()                                      # [Line 4360] | ASSIGNMENT: Creates variable 'removed' and stores the result of 'lst.pop()' in it | FUNCTION CALL: Calls 'lst.pop()' and stores its return value
print(removed)                                           # [Line 4361] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 7


""" 
Problem: 1356
Write a Python program to remove all elements from a list using pop() in a loop.
"""

# ======================================================================
# PROBLEM 1356 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = [1, 2, 3]                                          # [Line 4368] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[1, 2, 3]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
while lst:                                               # [Line 4369]
    print(lst.pop())                                     # [Line 4370] | Expected: 3, 2, 1 (on separate lines)


""" 
Problem: 1357
Write a Python program to handle IndexError when popping from an empty list.
"""

# ======================================================================
# PROBLEM 1357 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = []                                                 # [Line 4377] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[]' in it | DATA TYPE: List - A mutable ordered collection. Contains 0 elements
try:                                                     # [Line 4378]
    lst.pop()                                            # [Line 4379]
except IndexError:                                       # [Line 4380]
    print("List is empty")                               # [Line 4381] | Expected: "List is empty"


""" 
Problem: 1358
Write a Python program to use pop() with dictionaries and provide a default return value if the key doesn't exist.
"""

# ======================================================================
# PROBLEM 1358 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

d = {"x": 5}                                             # [Line 4388] | ASSIGNMENT: Creates variable 'd' and stores the result of '{'x': 5}' in it
val = d.pop("y", "Not Found")                            # [Line 4389] | ASSIGNMENT: Creates variable 'val' and stores the result of 'd.pop('y', 'Not Found')' in it | FUNCTION CALL: Calls 'd.pop()' and stores its return value
print(val)                                               # [Line 4390] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: "Not Found"


""" 
Problem: 1359
Write a Python program to safely remove a key from a dictionary using pop() inside a try block.
"""

# ======================================================================
# PROBLEM 1359 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

d = {"a": 100}                                           # [Line 4397] | ASSIGNMENT: Creates variable 'd' and stores the result of '{'a': 100}' in it
try:                                                     # [Line 4398]
    print(d.pop("b"))                                    # [Line 4399]
except KeyError:                                         # [Line 4400]
    print("Key not found")                               # [Line 4401] | Expected: "Key not found"


""" 
Problem: 1360
Write a Python program to remove keys one by one using pop() until the dictionary is empty.
"""

# ======================================================================
# PROBLEM 1360 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

d = {"k1": 1, "k2": 2}                                   # [Line 4408] | ASSIGNMENT: Creates variable 'd' and stores the result of '{'k1': 1, 'k2': 2}' in it
while d:                                                 # [Line 4409]
    print(d.popitem())                                   # [Line 4410] | Expected: tuple key-value pairs


""" 
Problem: 1361
Write a Python program to pop elements from a stack represented by a list.
"""

# ======================================================================
# PROBLEM 1361 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

stack = [1, 2, 3]                                        # [Line 4417] | ASSIGNMENT: Creates variable 'stack' and stores the result of '[1, 2, 3]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(stack.pop())                                       # [Line 4418] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 3


""" 
Problem: 1362
Write a Python program to simulate queue dequeue using pop(0).
"""

# ======================================================================
# PROBLEM 1362 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

queue = [10, 20, 30]                                     # [Line 4425] | ASSIGNMENT: Creates variable 'queue' and stores the result of '[10, 20, 30]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(queue.pop(0))                                      # [Line 4426] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 10


""" 
Problem: 1363
Write a Python program to remove the last element from a list using pop() and store it.
"""

# ======================================================================
# PROBLEM 1363 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

numbers = [4, 5, 6]                                      # [Line 4433] | ASSIGNMENT: Creates variable 'numbers' and stores the result of '[4, 5, 6]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
last = numbers.pop()                                     # [Line 4434] | ASSIGNMENT: Creates variable 'last' and stores the result of 'numbers.pop()' in it | FUNCTION CALL: Calls 'numbers.pop()' and stores its return value
print(last)                                              # [Line 4435] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 6


""" 
Problem: 1364
Write a Python program to demonstrate the use of pop() on a string key in a dictionary.
"""

# ======================================================================
# PROBLEM 1364 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

d = {"name": "Alice", "age": 30}                         # [Line 4442] | ASSIGNMENT: Creates variable 'd' and stores the result of '{'name': 'Alice', 'age': 30}' in it
print(d.pop("name"))                                     # [Line 4443] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: "Alice"


""" 
Problem: 1365
Write a Python program to pop multiple elements from the end of a list using a loop.
"""

# ======================================================================
# PROBLEM 1365 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = [1, 2, 3, 4, 5]                                    # [Line 4450] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[1, 2, 3, 4, 5]' in it | DATA TYPE: List - A mutable ordered collection. Contains 5 elements
for _ in range(3):                                       # [Line 4451]
    lst.pop()                                            # [Line 4452]
print(lst)                                               # [Line 4453] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [1, 2]


""" 
Problem: 1366
Write a Python program to pop and sum the last two numbers from a list.
"""

# ======================================================================
# PROBLEM 1366 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = [100, 200, 300]                                    # [Line 4460] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[100, 200, 300]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
sum_last_two = lst.pop() + lst.pop()                     # [Line 4461] | ASSIGNMENT: Creates variable 'sum_last_two' and stores the result of 'lst.pop() + lst.pop()' in it | BINARY OPERATION: Performs a calculation between two operands
print(sum_last_two)                                      # [Line 4462] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 500


""" 
Problem: 1367
Write a Python program to use pop() in a function that removes a key from a given dictionary.
"""

# ======================================================================
# PROBLEM 1367 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def remove_key(d, key):                                  # [Line 4469]
    return d.pop(key, None)                              # [Line 4470]

print(remove_key({"a": 1, "b": 2}, "a"))                 # [Line 4472] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 1


""" 
Problem: 1368
Write a Python program to pop an element from a list and append it to another list.
"""

# ======================================================================
# PROBLEM 1368 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

src = [9, 8, 7]                                          # [Line 4479] | ASSIGNMENT: Creates variable 'src' and stores the result of '[9, 8, 7]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
dst = []                                                 # [Line 4480] | ASSIGNMENT: Creates variable 'dst' and stores the result of '[]' in it | DATA TYPE: List - A mutable ordered collection. Contains 0 elements
dst.append(src.pop())                                    # [Line 4481] | FUNCTION CALL: Executes the function 'dst.append' | ARGUMENTS: Passes 1 argument(s) to the function
print(dst)                                               # [Line 4482] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [7]


""" 
Problem: 1369
Write a Python program to implement a basic undo feature using pop() on a list of actions.
"""

# ======================================================================
# PROBLEM 1369 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

actions = ["type", "edit", "save"]                       # [Line 4489] | ASSIGNMENT: Creates variable 'actions' and stores the result of '['type', 'edit', 'save']' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
undo = actions.pop()                                     # [Line 4490] | ASSIGNMENT: Creates variable 'undo' and stores the result of 'actions.pop()' in it | FUNCTION CALL: Calls 'actions.pop()' and stores its return value
print(undo)                                              # [Line 4491] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: "save"


""" 
Problem: 1370
Write a Python program to pop elements from a nested list.
"""

# ======================================================================
# PROBLEM 1370 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

nested = [[1, 2], [3, 4], [5, 6]]                        # [Line 4498] | ASSIGNMENT: Creates variable 'nested' and stores the result of '[[1, 2], [3, 4], [5, 6]]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
last_sublist = nested.pop()                              # [Line 4499] | ASSIGNMENT: Creates variable 'last_sublist' and stores the result of 'nested.pop()' in it | FUNCTION CALL: Calls 'nested.pop()' and stores its return value
print(last_sublist)                                      # [Line 4500] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [5, 6]

""" 
Problem: 1371  
Write a Python program with a function that accepts arbitrary keyword arguments and prints them.
"""

# ======================================================================
# PROBLEM 1371 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def print_kwargs(**kwargs):                              # [Line 4506] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    print(kwargs)                                        # [Line 4507]

print_kwargs(a=1, b=2)                                   # [Line 4509] | FUNCTION CALL: Executes the function 'print_kwargs' | Expected: {'a': 1, 'b': 2}


""" 
Problem: 1372  
Write a Python function that prints each key-value pair in **kwargs on a separate line.
"""

# ======================================================================
# PROBLEM 1372 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def display_kwargs(**kwargs):                            # [Line 4516] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    for key, value in kwargs.items():                    # [Line 4517]
        print(f"{key}: {value}")                         # [Line 4518]

display_kwargs(name="Alice", age=30)                     # [Line 4520] | FUNCTION CALL: Executes the function 'display_kwargs'
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

def count_kwargs(**kwargs):                              # [Line 4530] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    print(len(kwargs))                                   # [Line 4531]

count_kwargs(a=1, b=2, c=3)                              # [Line 4533] | FUNCTION CALL: Executes the function 'count_kwargs' | Expected: 3


""" 
Problem: 1374  
Write a Python function that returns the keys of **kwargs as a list.
"""

# ======================================================================
# PROBLEM 1374 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def kwargs_keys(**kwargs):                               # [Line 4540] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    return list(kwargs.keys())                           # [Line 4541]

print(kwargs_keys(x=10, y=20))                           # [Line 4543] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: ['x', 'y']


""" 
Problem: 1375  
Write a Python function that returns the values of **kwargs as a list.
"""

# ======================================================================
# PROBLEM 1375 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def kwargs_values(**kwargs):                             # [Line 4550] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    return list(kwargs.values())                         # [Line 4551]

print(kwargs_values(x=10, y=20))                         # [Line 4553] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [10, 20]


""" 
Problem: 1376  
Write a Python function that returns True if 'id' is in **kwargs.
"""

# ======================================================================
# PROBLEM 1376 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def has_id(**kwargs):                                    # [Line 4560] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    return 'id' in kwargs                                # [Line 4561]

print(has_id(name="A", id=123))                          # [Line 4563] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1377  
Write a Python function that returns the value of a keyword argument 'name' if it exists, else return 'Unknown'.
"""

# ======================================================================
# PROBLEM 1377 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def get_name(**kwargs):                                  # [Line 4570] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    return kwargs.get('name', 'Unknown')                 # [Line 4571]

print(get_name(age=22))                                  # [Line 4573] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: "Unknown"


""" 
Problem: 1378  
Write a Python function that sums all numeric values in **kwargs.
"""

# ======================================================================
# PROBLEM 1378 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def sum_kwargs(**kwargs):                                # [Line 4580] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    return sum(v for v in kwargs.values() if isinstance(v, (int, float)))  # [Line 4581]

print(sum_kwargs(a=10, b=5.5, c="x"))                    # [Line 4583] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 15.5


""" 
Problem: 1379  
Write a Python function that filters and returns keyword arguments where values are strings.
"""

# ======================================================================
# PROBLEM 1379 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def string_kwargs(**kwargs):                             # [Line 4590] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    return {k: v for k, v in kwargs.items() if isinstance(v, str)}  # [Line 4591]

print(string_kwargs(a="hi", b=2, c="hello"))             # [Line 4593] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {'a': 'hi', 'c': 'hello'}


""" 
Problem: 1380  
Write a Python function that prints a formatted string from **kwargs using name and age keys.
"""

# ======================================================================
# PROBLEM 1380 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def greet(**kwargs):                                     # [Line 4600] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    print(f"Hello {kwargs.get('name', 'Guest')}, age {kwargs.get('age', 'N/A')}")  # [Line 4601]

greet(name="Bob", age=40)                                # [Line 4603] | FUNCTION CALL: Executes the function 'greet' | Expected: Hello Bob, age 40


""" 
Problem: 1381  
Write a Python function that updates a dictionary with keyword arguments.
"""

# ======================================================================
# PROBLEM 1381 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def update_dict(base, **kwargs):                         # [Line 4610] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    base.update(kwargs)                                  # [Line 4611]
    return base                                          # [Line 4612]

print(update_dict({'x': 1}, y=2, z=3))                   # [Line 4614] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {'x': 1, 'y': 2, 'z': 3}


""" 
Problem: 1382  
Write a Python function that merges two dictionaries using **kwargs.
"""

# ======================================================================
# PROBLEM 1382 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def merge_dicts(d1, **kwargs):                           # [Line 4621] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    merged = d1.copy()                                   # [Line 4622]
    merged.update(kwargs)                                # [Line 4623]
    return merged                                        # [Line 4624]

print(merge_dicts({'a': 1}, b=2))                        # [Line 4626] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {'a': 1, 'b': 2}


""" 
Problem: 1383  
Write a Python function that prints only the keyword arguments with even integer values.
"""

# ======================================================================
# PROBLEM 1383 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def even_kwargs(**kwargs):                               # [Line 4633] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    for k, v in kwargs.items():                          # [Line 4634]
        if isinstance(v, int) and v % 2 == 0:            # [Line 4635] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).
            print(f"{k}: {v}")                           # [Line 4636]

even_kwargs(a=1, b=2, c=4)                               # [Line 4638] | FUNCTION CALL: Executes the function 'even_kwargs'
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

def sorted_kwargs(**kwargs):                             # [Line 4648] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    for k in sorted(kwargs.keys()):                      # [Line 4649]
        print(f"{k}: {kwargs[k]}")                       # [Line 4650] | SLICING OPERATION - Extracts a portion of the sequence

sorted_kwargs(z=9, a=1, m=5)                             # [Line 4652] | FUNCTION CALL: Executes the function 'sorted_kwargs'
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

def count_strings(**kwargs):                             # [Line 4663] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    print(sum(1 for v in kwargs.values() if isinstance(v, str)))  # [Line 4664]

count_strings(a="one", b=2, c="three")                   # [Line 4666] | FUNCTION CALL: Executes the function 'count_strings' | Expected: 2


""" 
Problem: 1386  
Write a Python function that prints whether each value in **kwargs is truthy or falsy.
"""

# ======================================================================
# PROBLEM 1386 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def check_truthy(**kwargs):                              # [Line 4673] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    for k, v in kwargs.items():                          # [Line 4674]
        print(f"{k}: {'Truthy' if v else 'Falsy'}")      # [Line 4675]

check_truthy(a=0, b="hello", c=[])                       # [Line 4677] | FUNCTION CALL: Executes the function 'check_truthy'
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

def starts_with_a(**kwargs):                             # [Line 4688] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    for k, v in kwargs.items():                          # [Line 4689]
        if k.startswith('a'):                            # [Line 4690]
            print(f"{k}: {v}")                           # [Line 4691]

starts_with_a(apple=1, banana=2, ant=3)                  # [Line 4693] | FUNCTION CALL: Executes the function 'starts_with_a'
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

def reverse_kwargs(**kwargs):                            # [Line 4703] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    return {v: k for k, v in kwargs.items()}             # [Line 4704]

print(reverse_kwargs(a=1, b=2))                          # [Line 4706] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {1: 'a', 2: 'b'}


""" 
Problem: 1389  
Write a Python function that returns the longest key in **kwargs.
"""

# ======================================================================
# PROBLEM 1389 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def longest_key(**kwargs):                               # [Line 4713] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    return max(kwargs, key=len)                          # [Line 4714]

print(longest_key(short=1, muchlonger=2))                # [Line 4716] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 'muchlonger'


""" 
Problem: 1390  
Write a Python function that creates a string from **kwargs as key=value pairs joined by commas.
"""

# ======================================================================
# PROBLEM 1390 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def stringify_kwargs(**kwargs):                          # [Line 4723] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    return ', '.join(f"{k}={v}" for k, v in kwargs.items())  # [Line 4724]

print(stringify_kwargs(x=10, y=20))                      # [Line 4726] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: "x=10, y=20"


""" 
Problem: 1391  
Write a Python function that checks if all values in **kwargs are integers.
"""

# ======================================================================
# PROBLEM 1391 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def all_ints(**kwargs):                                  # [Line 4733] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    return all(isinstance(v, int) for v in kwargs.values())  # [Line 4734]

print(all_ints(a=1, b=2))                                # [Line 4736] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1392  
Write a Python function that finds and returns the maximum numeric value in **kwargs.
"""

# ======================================================================
# PROBLEM 1392 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def max_numeric(**kwargs):                               # [Line 4743] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    nums = [v for v in kwargs.values() if isinstance(v, (int, float))]  # [Line 4744]
    return max(nums) if nums else None                   # [Line 4745]

print(max_numeric(a=1, b=3.5, c="x"))                    # [Line 4747] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 3.5


""" 
Problem: 1393  
Write a Python function that counts the keyword arguments whose value is None.
"""

# ======================================================================
# PROBLEM 1393 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def count_none(**kwargs):                                # [Line 4754] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    return sum(1 for v in kwargs.values() if v is None)  # [Line 4755]

print(count_none(a=None, b=1, c=None))                   # [Line 4757] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 2


""" 
Problem: 1394  
Write a Python function that prints the types of values in **kwargs.
"""

# ======================================================================
# PROBLEM 1394 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def print_types(**kwargs):                               # [Line 4764] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    for k, v in kwargs.items():                          # [Line 4765]
        print(f"{k}: {type(v).__name__}")                # [Line 4766]

print_types(a=1, b="str", c=3.14)                        # [Line 4768] | FUNCTION CALL: Executes the function 'print_types'
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

def kv_pairs(**kwargs):                                  # [Line 4779] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    return list(kwargs.items())                          # [Line 4780]

print(kv_pairs(a=1, b=2))                                # [Line 4782] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [('a', 1), ('b', 2)]


""" 
Problem: 1396  
Write a Python function that filters out keyword arguments with falsy values.
"""

# ======================================================================
# PROBLEM 1396 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def remove_falsy(**kwargs):                              # [Line 4789] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    return {k: v for k, v in kwargs.items() if v}        # [Line 4790]

print(remove_falsy(a=0, b=1, c=""))                      # [Line 4792] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {'b': 1}


""" 
Problem: 1397  
Write a Python function that returns True if at least one value in **kwargs is a list.
"""

# ======================================================================
# PROBLEM 1397 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def has_list(**kwargs):                                  # [Line 4799] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    return any(isinstance(v, list) for v in kwargs.values())  # [Line 4800]

print(has_list(a=[1,2], b="x"))                          # [Line 4802] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1398  
Write a Python function that prints whether the number of keyword arguments is even or odd.
"""

# ======================================================================
# PROBLEM 1398 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def even_or_odd_kwargs(**kwargs):                        # [Line 4809] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    print("Even" if len(kwargs) % 2 == 0 else "Odd")     # [Line 4810] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

even_or_odd_kwargs(a=1, b=2, c=3)                        # [Line 4812] | FUNCTION CALL: Executes the function 'even_or_odd_kwargs' | Expected: Odd


""" 
Problem: 1399  
Write a Python function that accepts **kwargs and renames any keys that start with 'temp_' by removing the prefix.
"""

# ======================================================================
# PROBLEM 1399 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def clean_temp_keys(**kwargs):                           # [Line 4819] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    return {k[5:] if k.startswith('temp_') else k: v for k, v in kwargs.items()}  # [Line 4820] | SLICING OPERATION [5:] - Extracts all elements starting from index 5 to the end. 

print(clean_temp_keys(temp_x=1, y=2))                    # [Line 4822] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {'x': 1, 'y': 2}


""" 
Problem: 1400  
Write a Python function that accepts **kwargs and returns only those key-value pairs where the key is uppercase.
"""

# ======================================================================
# PROBLEM 1400 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def uppercase_keys_only(**kwargs):                       # [Line 4829] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2.
    return {k: v for k, v in kwargs.items() if k.isupper()}  # [Line 4830]

print(uppercase_keys_only(AGE=30, name="Ann"))           # [Line 4832] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {'AGE': 30}

""" 
Problem: 1402  
Write a Pythonic way to use `enumerate()` to get both index and value from a list.
"""

# ======================================================================
# PROBLEM 1402 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

fruits = ['apple', 'banana', 'cherry']                   # [Line 4838] | ASSIGNMENT: Creates variable 'fruits' and stores the result of '['apple', 'banana', 'cherry']' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
for index, value in enumerate(fruits):                   # [Line 4839]
    print(f"{index}: {value}")                           # [Line 4840] | Expected: 0: apple, 1: banana, 2: cherry


""" 
Problem: 1403  
Write a Pythonic way to use `zip()` to combine two lists into a list of tuples.
"""

# ======================================================================
# PROBLEM 1403 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

names = ['Alice', 'Bob', 'Charlie']                      # [Line 4847] | ASSIGNMENT: Creates variable 'names' and stores the result of '['Alice', 'Bob', 'Charlie']' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
ages = [25, 30, 35]                                      # [Line 4848] | ASSIGNMENT: Creates variable 'ages' and stores the result of '[25, 30, 35]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
combined = list(zip(names, ages))                        # [Line 4849] | ASSIGNMENT: Creates variable 'combined' and stores the result of 'list(zip(names, ages))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(combined)                                          # [Line 4850] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]


""" 
Problem: 1404  
Write a Pythonic way to use a dictionary comprehension to swap keys and values.
"""

# ======================================================================
# PROBLEM 1404 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

original = {'a': 1, 'b': 2, 'c': 3}                      # [Line 4857] | ASSIGNMENT: Creates variable 'original' and stores the result of '{'a': 1, 'b': 2, 'c': 3}' in it
swapped = {v: k for k, v in original.items()}            # [Line 4858] | ASSIGNMENT: Creates variable 'swapped' and stores the result of '{v: k for k, v in original.items()}' in it
print(swapped)                                           # [Line 4859] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {1: 'a', 2: 'b', 3: 'c'}


""" 
Problem: 1405  
Write a Pythonic way to use `all()` to check if all elements in a list satisfy a condition.
"""

# ======================================================================
# PROBLEM 1405 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

numbers = [2, 4, 6, 8]                                   # [Line 4866] | ASSIGNMENT: Creates variable 'numbers' and stores the result of '[2, 4, 6, 8]' in it | DATA TYPE: List - A mutable ordered collection. Contains 4 elements
all_even = all(x % 2 == 0 for x in numbers)              # [Line 4867] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1). | ASSIGNMENT: Creates variable 'all_even' and stores the result of 'all((x % 2 == 0 for x in numbers))' in it | FUNCTION CALL: Calls 'all()' and stores its return value
print(all_even)                                          # [Line 4868] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1406  
Write a Pythonic way to flatten a list of lists using a list comprehension.
"""

# ======================================================================
# PROBLEM 1406 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]               # [Line 4875] | ASSIGNMENT: Creates variable 'nested' and stores the result of '[[1, 2, 3], [4, 5], [6, 7, 8, 9]]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
flattened = [item for sublist in nested for item in sublist]  # [Line 4876] | ASSIGNMENT: Creates variable 'flattened' and stores the result of '[item for sublist in nested for item in sublist]' in it
print(flattened)                                         # [Line 4877] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9]


""" 
Problem: 1407  
Write a Pythonic way to use `map()` to convert a list of strings to uppercase.
"""

# ======================================================================
# PROBLEM 1407 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

words = ['hello', 'world', 'python']                     # [Line 4884] | ASSIGNMENT: Creates variable 'words' and stores the result of '['hello', 'world', 'python']' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
uppercase_words = list(map(str.upper, words))            # [Line 4885] | ASSIGNMENT: Creates variable 'uppercase_words' and stores the result of 'list(map(str.upper, words))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(uppercase_words)                                   # [Line 4886] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: ['HELLO', 'WORLD', 'PYTHON']


""" 
Problem: 1408  
Write a Pythonic way to use `filter()` with a lambda to get even numbers from a list.
"""

# ======================================================================
# PROBLEM 1408 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]                # [Line 4893] | ASSIGNMENT: Creates variable 'numbers' and stores the result of '[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]' in it | DATA TYPE: List - A mutable ordered collection. Contains 10 elements
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # [Line 4894] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1). | ASSIGNMENT: Creates variable 'even_numbers' and stores the result of 'list(filter(lambda x: x % 2 == 0, numbers))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(even_numbers)                                      # [Line 4895] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [2, 4, 6, 8, 10]


""" 
Problem: 1409  
Write a Pythonic way to use `set()` to remove duplicates from a list while preserving order using dict.fromkeys().
"""

# ======================================================================
# PROBLEM 1409 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

items = [1, 2, 2, 3, 3, 3, 4, 5, 5]                      # [Line 4902] | ASSIGNMENT: Creates variable 'items' and stores the result of '[1, 2, 2, 3, 3, 3, 4, 5, 5]' in it | DATA TYPE: List - A mutable ordered collection. Contains 9 elements
unique_ordered = list(dict.fromkeys(items))              # [Line 4903] | ASSIGNMENT: Creates variable 'unique_ordered' and stores the result of 'list(dict.fromkeys(items))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(unique_ordered)                                    # [Line 4904] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [1, 2, 3, 4, 5]


""" 
Problem: 1410  
Write a Pythonic way to use `str.join()` to concatenate a list of strings with a separator.
"""

# ======================================================================
# PROBLEM 1410 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

words = ['Python', 'is', 'great']                        # [Line 4911] | ASSIGNMENT: Creates variable 'words' and stores the result of '['Python', 'is', 'great']' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
sentence = ' '.join(words)                               # [Line 4912] | ASSIGNMENT: Creates variable 'sentence' and stores the result of '' '.join(words)' in it | FUNCTION CALL: Calls '' '.join()' and stores its return value
print(sentence)                                          # [Line 4913] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: Python is great


""" 
Problem: 1411  
Write a Pythonic way to use list slicing to reverse a string.
"""

# ======================================================================
# PROBLEM 1411 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

text = "Python"                                          # [Line 4920] | ASSIGNMENT: Creates variable 'text' and stores the result of ''Python'' in it | DATA TYPE: String - A sequence of characters. Length: 6
reversed_text = text[::-1]                               # [Line 4921] | SLICING OPERATION [::-1] - This is a reverse slice. The syntax [::-1] means: start at the beginning (no start index), stop at the end (no stop index), and step backwards by 1. This effectively reverses the entire sequence. Example: [1,2,3][::-1] becomes [3,2,1] | ASSIGNMENT: Creates variable 'reversed_text' and stores the result of 'text[::-1]' in it | SUBSCRIPTION: Accesses an element or slice from a sequence using []
print(reversed_text)                                     # [Line 4922] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: nohtyP


""" 
Problem: 1412  
Write a Pythonic way to use `collections.Counter` to count character frequencies in a string.
"""

# ======================================================================
# PROBLEM 1412 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

from collections import Counter                          # [Line 4929]
text = "hello world"                                     # [Line 4930] | ASSIGNMENT: Creates variable 'text' and stores the result of ''hello world'' in it | DATA TYPE: String - A sequence of characters. Length: 11
char_counts = Counter(text)                              # [Line 4931] | ASSIGNMENT: Creates variable 'char_counts' and stores the result of 'Counter(text)' in it | FUNCTION CALL: Calls 'Counter()' and stores its return value
print(char_counts)                                       # [Line 4932] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})


""" 
Problem: 1413  
Write a Pythonic way to use `itertools.chain()` to combine multiple lists into one.
"""

# ======================================================================
# PROBLEM 1413 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

from itertools import chain                              # [Line 4939]
list1 = [1, 2, 3]                                        # [Line 4940] | ASSIGNMENT: Creates variable 'list1' and stores the result of '[1, 2, 3]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
list2 = [4, 5, 6]                                        # [Line 4941] | ASSIGNMENT: Creates variable 'list2' and stores the result of '[4, 5, 6]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
list3 = [7, 8, 9]                                        # [Line 4942] | ASSIGNMENT: Creates variable 'list3' and stores the result of '[7, 8, 9]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
combined = list(chain(list1, list2, list3))              # [Line 4943] | ASSIGNMENT: Creates variable 'combined' and stores the result of 'list(chain(list1, list2, list3))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(combined)                                          # [Line 4944] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9]


""" 
Problem: 1414  
Write a Pythonic way to use `str.split()` and list comprehension to capitalize each word.
"""

# ======================================================================
# PROBLEM 1414 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

text = "hello world python"                              # [Line 4951] | ASSIGNMENT: Creates variable 'text' and stores the result of ''hello world python'' in it | DATA TYPE: String - A sequence of characters. Length: 18
capitalized = ' '.join(word.capitalize() for word in text.split())  # [Line 4952] | ASSIGNMENT: Creates variable 'capitalized' and stores the result of '' '.join((word.capitalize() for word in text.split()))' in it | FUNCTION CALL: Calls '' '.join()' and stores its return value
print(capitalized)                                       # [Line 4953] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: Hello World Python


""" 
Problem: 1415  
Write a Pythonic way to use `zip()` with `*` to transpose a list of lists.
"""

# ======================================================================
# PROBLEM 1415 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]               # [Line 4960] | ASSIGNMENT: Creates variable 'matrix' and stores the result of '[[1, 2, 3], [4, 5, 6], [7, 8, 9]]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
transposed = list(zip(*matrix))                          # [Line 4961] | ASSIGNMENT: Creates variable 'transposed' and stores the result of 'list(zip(*matrix))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(transposed)                                        # [Line 4962] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [(1, 4, 7), (2, 5, 8), (3, 6, 9)]


""" 
Problem: 1416  
Write a Pythonic way to use `dict.get()` with a default value to safely access dictionary keys.
"""

# ======================================================================
# PROBLEM 1416 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

data = {'name': 'Alice', 'age': 30}                      # [Line 4969] | ASSIGNMENT: Creates variable 'data' and stores the result of '{'name': 'Alice', 'age': 30}' in it
name = data.get('name', 'Unknown')                       # [Line 4970] | ASSIGNMENT: Creates variable 'name' and stores the result of 'data.get('name', 'Unknown')' in it | FUNCTION CALL: Calls 'data.get()' and stores its return value
city = data.get('city', 'Unknown')                       # [Line 4971] | ASSIGNMENT: Creates variable 'city' and stores the result of 'data.get('city', 'Unknown')' in it | FUNCTION CALL: Calls 'data.get()' and stores its return value
print(name, city)                                        # [Line 4972] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: Alice Unknown


""" 
Problem: 1417  
Write a Pythonic way to use `collections.defaultdict` to group items by a key.
"""

# ======================================================================
# PROBLEM 1417 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

from collections import defaultdict                      # [Line 4979]
items = [('fruit', 'apple'), ('fruit', 'banana'), ('vegetable', 'carrot'), ('fruit', 'cherry')]  # [Line 4980] | ASSIGNMENT: Creates variable 'items' and stores the result of '[('fruit', 'apple'), ('fruit', 'banana'), ('vegetable', 'carrot'), ('fruit', 'cherry')]' in it | DATA TYPE: List - A mutable ordered collection. Contains 4 elements
grouped = defaultdict(list)                              # [Line 4981] | ASSIGNMENT: Creates variable 'grouped' and stores the result of 'defaultdict(list)' in it | FUNCTION CALL: Calls 'defaultdict()' and stores its return value
for category, item in items:                             # [Line 4982]
    grouped[category].append(item)                       # [Line 4983]
print(dict(grouped))                                     # [Line 4984] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {'fruit': ['apple', 'banana', 'cherry'], 'vegetable': ['carrot']}


""" 
Problem: 1418  
Write a Pythonic way to use `itertools.groupby()` to group consecutive identical elements.
"""

# ======================================================================
# PROBLEM 1418 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

from itertools import groupby                            # [Line 4991]
data = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4]                    # [Line 4992] | ASSIGNMENT: Creates variable 'data' and stores the result of '[1, 1, 1, 2, 2, 3, 3, 3, 3, 4]' in it | DATA TYPE: List - A mutable ordered collection. Contains 10 elements
grouped = {k: list(g) for k, g in groupby(data)}         # [Line 4993] | ASSIGNMENT: Creates variable 'grouped' and stores the result of '{k: list(g) for k, g in groupby(data)}' in it
print(grouped)                                           # [Line 4994] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {1: [1, 1, 1], 2: [2, 2], 3: [3, 3, 3, 3], 4: [4]}


""" 
Problem: 1419  
Write a Pythonic way to use `str.maketrans()` and `str.translate()` to replace multiple characters.
"""

# ======================================================================
# PROBLEM 1419 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

text = "hello world"                                     # [Line 5001] | ASSIGNMENT: Creates variable 'text' and stores the result of ''hello world'' in it | DATA TYPE: String - A sequence of characters. Length: 11
translation = str.maketrans('lo', '12')                  # [Line 5002] | ASSIGNMENT: Creates variable 'translation' and stores the result of 'str.maketrans('lo', '12')' in it | FUNCTION CALL: Calls 'str.maketrans()' and stores its return value
result = text.translate(translation)                     # [Line 5003] | ASSIGNMENT: Creates variable 'result' and stores the result of 'text.translate(translation)' in it | FUNCTION CALL: Calls 'text.translate()' and stores its return value
print(result)                                            # [Line 5004] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: he112 w2r1d


""" 
Problem: 1420  
Write a Pythonic way to use `frozenset()` to create an immutable set for use as a dictionary key.
"""

# ======================================================================
# PROBLEM 1420 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

fs1 = frozenset([1, 2, 3])                               # [Line 5011] | ASSIGNMENT: Creates variable 'fs1' and stores the result of 'frozenset([1, 2, 3])' in it | FUNCTION CALL: Calls 'frozenset()' and stores its return value
fs2 = frozenset([4, 5, 6])                               # [Line 5012] | ASSIGNMENT: Creates variable 'fs2' and stores the result of 'frozenset([4, 5, 6])' in it | FUNCTION CALL: Calls 'frozenset()' and stores its return value
mapping = {fs1: 'first', fs2: 'second'}                  # [Line 5013] | ASSIGNMENT: Creates variable 'mapping' and stores the result of '{fs1: 'first', fs2: 'second'}' in it
print(mapping[fs1])                                      # [Line 5014] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: first


""" 
Problem: 1421  
Write a Pythonic way to use `itertools.combinations()` to generate all pairs from a list.
"""

# ======================================================================
# PROBLEM 1421 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

from itertools import combinations                       # [Line 5021]
items = ['a', 'b', 'c', 'd']                             # [Line 5022] | ASSIGNMENT: Creates variable 'items' and stores the result of '['a', 'b', 'c', 'd']' in it | DATA TYPE: List - A mutable ordered collection. Contains 4 elements
pairs = list(combinations(items, 2))                     # [Line 5023] | ASSIGNMENT: Creates variable 'pairs' and stores the result of 'list(combinations(items, 2))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(pairs)                                             # [Line 5024] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')]


""" 
Problem: 1422  
Write a Pythonic way to use `collections.deque` to implement a queue with append and popleft.
"""

# ======================================================================
# PROBLEM 1422 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

from collections import deque                            # [Line 5031]
queue = deque()                                          # [Line 5032] | ASSIGNMENT: Creates variable 'queue' and stores the result of 'deque()' in it | FUNCTION CALL: Calls 'deque()' and stores its return value
queue.append(1)                                          # [Line 5033] | FUNCTION CALL: Executes the function 'queue.append' | ARGUMENTS: Passes 1 argument(s) to the function
queue.append(2)                                          # [Line 5034] | FUNCTION CALL: Executes the function 'queue.append' | ARGUMENTS: Passes 1 argument(s) to the function
queue.append(3)                                          # [Line 5035] | FUNCTION CALL: Executes the function 'queue.append' | ARGUMENTS: Passes 1 argument(s) to the function
first = queue.popleft()                                  # [Line 5036] | ASSIGNMENT: Creates variable 'first' and stores the result of 'queue.popleft()' in it | FUNCTION CALL: Calls 'queue.popleft()' and stores its return value
print(first, list(queue))                                # [Line 5037] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 1 [2, 3]


""" 
Problem: 1423  
Write a Pythonic way to use `str.partition()` to split a string at the first occurrence of a delimiter.
"""

# ======================================================================
# PROBLEM 1423 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

text = "hello:world:python"                              # [Line 5044] | ASSIGNMENT: Creates variable 'text' and stores the result of ''hello:world:python'' in it | DATA TYPE: String - A sequence of characters. Length: 18
before, sep, after = text.partition(':')                 # [Line 5045] | ASSIGNMENT: Creates variable '(before, sep, after)' and stores the result of 'text.partition(':')' in it | FUNCTION CALL: Calls 'text.partition()' and stores its return value
print(before, after)                                     # [Line 5046] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: hello world:python


""" 
Problem: 1424  
Write a Pythonic way to use `operator.itemgetter()` to sort a list of dictionaries by a key.
"""

# ======================================================================
# PROBLEM 1424 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

from operator import itemgetter                          # [Line 5053]
people = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]  # [Line 5054] | SLICING OPERATION - Extracts a portion of the sequence | ASSIGNMENT: Creates variable 'people' and stores the result of '[{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
sorted_people = sorted(people, key=itemgetter('age'))    # [Line 5055] | ASSIGNMENT: Creates variable 'sorted_people' and stores the result of 'sorted(people, key=itemgetter('age'))' in it | FUNCTION CALL: Calls 'sorted()' and stores its return value
print(sorted_people)                                     # [Line 5056] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]


""" 
Problem: 1425  
Write a Pythonic way to use `contextlib.suppress()` to ignore specific exceptions.
"""

# ======================================================================
# PROBLEM 1425 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

from contextlib import suppress                          # [Line 5063]
with suppress(ValueError, ZeroDivisionError):            # [Line 5064]
    result = int("not a number")                         # [Line 5065] | This would raise ValueError, but it's suppressed
    print("This won't print")                            # [Line 5066]
print("Continues after exception")                       # [Line 5067] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: Continues after exception


""" 
Problem: 1426  
Write a Pythonic way to check if any item in a list is true.
"""

# ======================================================================
# PROBLEM 1426 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = [0, False, 5]                                      # [Line 5074] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[0, False, 5]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(any(lst))                                          # [Line 5075] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1427  
Write a Pythonic way to use a generator expression to calculate the sum of squares.
"""

# ======================================================================
# PROBLEM 1427 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = [1, 2, 3]                                          # [Line 5082] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[1, 2, 3]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
total = sum(x**2 for x in lst)                           # [Line 5083] | EXPONENTIATION OPERATOR (**) - Raises a number to a power. Example: 2 ** 3 = 8 (2 to the power of 3). This is equivalent to 2 * 2 * 2. | ASSIGNMENT: Creates variable 'total' and stores the result of 'sum((x ** 2 for x in lst))' in it | FUNCTION CALL: Calls 'sum()' and stores its return value
print(total)                                             # [Line 5084] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 14


""" 
Problem: 1428  
Write a Pythonic program to get the intersection of two sets.
"""

# ======================================================================
# PROBLEM 1428 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

a = {1, 2, 3}                                            # [Line 5091] | ASSIGNMENT: Creates variable 'a' and stores the result of '{1, 2, 3}' in it
b = {2, 3, 4}                                            # [Line 5092] | ASSIGNMENT: Creates variable 'b' and stores the result of '{2, 3, 4}' in it
print(a & b)                                             # [Line 5093] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {2, 3}


""" 
Problem: 1429  
Write a Pythonic program to get the union of two sets.
"""

# ======================================================================
# PROBLEM 1429 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

print(a | b)                                             # [Line 5100] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {1, 2, 3, 4}


""" 
Problem: 1430  
Write a Pythonic way to check if a string contains only digits.
"""

# ======================================================================
# PROBLEM 1430 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

s = "12345"                                              # [Line 5107] | ASSIGNMENT: Creates variable 's' and stores the result of ''12345'' in it | DATA TYPE: String - A sequence of characters. Length: 5
print(s.isdigit())                                       # [Line 5108] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1431  
Write a Pythonic one-liner to reverse a list.
"""

# ======================================================================
# PROBLEM 1431 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = [1, 2, 3]                                          # [Line 5115] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[1, 2, 3]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(lst[::-1])                                         # [Line 5116] | SLICING OPERATION [::-1] - This is a reverse slice. The syntax [::-1] means: start at the beginning (no start index), stop at the end (no stop index), and step backwards by 1. This effectively reverses the entire sequence. Example: [1,2,3][::-1] becomes [3,2,1] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [3, 2, 1]


""" 
Problem: 1432  
Write a Pythonic way to zip dictionary keys and values into a list of tuples.
"""

# ======================================================================
# PROBLEM 1432 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

d = {'a': 1, 'b': 2}                                     # [Line 5123] | ASSIGNMENT: Creates variable 'd' and stores the result of '{'a': 1, 'b': 2}' in it
zipped = list(zip(d.keys(), d.values()))                 # [Line 5124] | ASSIGNMENT: Creates variable 'zipped' and stores the result of 'list(zip(d.keys(), d.values()))' in it | FUNCTION CALL: Calls 'list()' and stores its return value
print(zipped)                                            # [Line 5125] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [('a', 1), ('b', 2)]


""" 
Problem: 1433  
Write a Pythonic way to initialize a dictionary with default integer values.
"""

# ======================================================================
# PROBLEM 1433 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

from collections import defaultdict                      # [Line 5132]
d = defaultdict(int)                                     # [Line 5133] | ASSIGNMENT: Creates variable 'd' and stores the result of 'defaultdict(int)' in it | FUNCTION CALL: Calls 'defaultdict()' and stores its return value
d["x"] += 1                                              # [Line 5134]
print(d["x"])                                            # [Line 5135] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 1


""" 
Problem: 1434  
Write a Pythonic program to group elements by length from a list of words.
"""

# ======================================================================
# PROBLEM 1434 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

words = ["hi", "hello", "yes", "no"]                     # [Line 5142] | ASSIGNMENT: Creates variable 'words' and stores the result of '['hi', 'hello', 'yes', 'no']' in it | DATA TYPE: List - A mutable ordered collection. Contains 4 elements
from collections import defaultdict                      # [Line 5143]
grouped = defaultdict(list)                              # [Line 5144] | ASSIGNMENT: Creates variable 'grouped' and stores the result of 'defaultdict(list)' in it | FUNCTION CALL: Calls 'defaultdict()' and stores its return value
for word in words:                                       # [Line 5145]
    grouped[len(word)].append(word)                      # [Line 5146]
print(dict(grouped))                                     # [Line 5147] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {2: ['hi', 'no'], 5: ['hello'], 3: ['yes']}


""" 
Problem: 1435  
Write a Pythonic program to sort a list of tuples by the second item.
"""

# ======================================================================
# PROBLEM 1435 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = [(1, 3), (2, 1), (4, 2)]                           # [Line 5154] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[(1, 3), (2, 1), (4, 2)]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
sorted_lst = sorted(lst, key=lambda x: x[1])             # [Line 5155] | SLICING OPERATION - Extracts a portion of the sequence | ASSIGNMENT: Creates variable 'sorted_lst' and stores the result of 'sorted(lst, key=lambda x: x[1])' in it | FUNCTION CALL: Calls 'sorted()' and stores its return value
print(sorted_lst)                                        # [Line 5156] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [(2, 1), (4, 2), (1, 3)]


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
with open("temp.txt", "w") as f:                         # [Line 5164]
    f.write("Hello")                                     # [Line 5165]
with open("temp.txt") as f:                              # [Line 5166]
    print(f.read())                                      # [Line 5167] | Expected: "Hello"


""" 
Problem: 1437  
Write a Pythonic one-liner to find the maximum item in a list.
"""

# ======================================================================
# PROBLEM 1437 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = [1, 5, 2]                                          # [Line 5174] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[1, 5, 2]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(max(lst))                                          # [Line 5175] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 5


""" 
Problem: 1438  
Write a Pythonic way to assign multiple variables from a list.
"""

# ======================================================================
# PROBLEM 1438 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = [1, 2, 3]                                          # [Line 5182] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[1, 2, 3]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
a, b, c = lst                                            # [Line 5183] | ASSIGNMENT: Creates variable '(a, b, c)' and stores the result of 'lst' in it
print(a, b, c)                                           # [Line 5184] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 1 2 3


""" 
Problem: 1439  
Write a Pythonic way to create a dictionary from two lists.
"""

# ======================================================================
# PROBLEM 1439 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

keys = ['a', 'b']                                        # [Line 5191] | ASSIGNMENT: Creates variable 'keys' and stores the result of '['a', 'b']' in it | DATA TYPE: List - A mutable ordered collection. Contains 2 elements
values = [1, 2]                                          # [Line 5192] | ASSIGNMENT: Creates variable 'values' and stores the result of '[1, 2]' in it | DATA TYPE: List - A mutable ordered collection. Contains 2 elements
d = dict(zip(keys, values))                              # [Line 5193] | ASSIGNMENT: Creates variable 'd' and stores the result of 'dict(zip(keys, values))' in it | FUNCTION CALL: Calls 'dict()' and stores its return value
print(d)                                                 # [Line 5194] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {'a': 1, 'b': 2}


""" 
Problem: 1440  
Write a Pythonic way to remove a key from a dictionary if it exists.
"""

# ======================================================================
# PROBLEM 1440 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

d = {'a': 1, 'b': 2}                                     # [Line 5201] | ASSIGNMENT: Creates variable 'd' and stores the result of '{'a': 1, 'b': 2}' in it
d.pop('b', None)                                         # [Line 5202] | FUNCTION CALL: Executes the function 'd.pop' | ARGUMENTS: Passes 2 argument(s) to the function
print(d)                                                 # [Line 5203] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {'a': 1}


""" 
Problem: 1441  
Write a Pythonic way to check if a variable is None.
"""

# ======================================================================
# PROBLEM 1441 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

x = None                                                 # [Line 5210] | ASSIGNMENT: Creates variable 'x' and stores the result of 'None' in it
print(x is None)                                         # [Line 5211] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1442  
Write a Pythonic way to handle a missing dictionary key using try-except.
"""

# ======================================================================
# PROBLEM 1442 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

d = {'a': 1}                                             # [Line 5218] | ASSIGNMENT: Creates variable 'd' and stores the result of '{'a': 1}' in it
try:                                                     # [Line 5219]
    print(d['b'])                                        # [Line 5220]
except KeyError:                                         # [Line 5221]
    print("Key not found")                               # [Line 5222] | Expected: Key not found


""" 
Problem: 1443  
Write a Pythonic way to unpack a tuple into variables.
"""

# ======================================================================
# PROBLEM 1443 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

t = (1, 2)                                               # [Line 5229] | ASSIGNMENT: Creates variable 't' and stores the result of '(1, 2)' in it | DATA TYPE: Tuple - An immutable ordered collection. Contains 2 elements
x, y = t                                                 # [Line 5230] | ASSIGNMENT: Creates variable '(x, y)' and stores the result of 't' in it
print(x, y)                                              # [Line 5231] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 1 2


""" 
Problem: 1444  
Write a Pythonic one-liner to check if a list contains duplicates.
"""

# ======================================================================
# PROBLEM 1444 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = [1, 2, 2]                                          # [Line 5238] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[1, 2, 2]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(len(lst) != len(set(lst)))                         # [Line 5239] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1445  
Write a Pythonic program to count character frequencies in a string.
"""

# ======================================================================
# PROBLEM 1445 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

s = "banana"                                             # [Line 5246] | ASSIGNMENT: Creates variable 's' and stores the result of ''banana'' in it | DATA TYPE: String - A sequence of characters. Length: 6
freq = Counter(s)                                        # [Line 5247] | ASSIGNMENT: Creates variable 'freq' and stores the result of 'Counter(s)' in it | FUNCTION CALL: Calls 'Counter()' and stores its return value
print(freq)                                              # [Line 5248] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {'b': 1, 'a': 3, 'n': 2}


""" 
Problem: 1446  
Write a Pythonic one-liner to filter out negative numbers from a list.
"""

# ======================================================================
# PROBLEM 1446 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = [1, -2, 3, -4]                                     # [Line 5255] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[1, -2, 3, -4]' in it | DATA TYPE: List - A mutable ordered collection. Contains 4 elements
print([x for x in lst if x >= 0])                        # [Line 5256] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: [1, 3]


""" 
Problem: 1447  
Write a Pythonic way to test if a list has at least one even number.
"""

# ======================================================================
# PROBLEM 1447 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = [1, 3, 4]                                          # [Line 5263] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[1, 3, 4]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(any(x % 2 == 0 for x in lst))                      # [Line 5264] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1). | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1448  
Write a Pythonic way to get the index of an item in a list.
"""

# ======================================================================
# PROBLEM 1448 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = ['a', 'b', 'c']                                    # [Line 5271] | ASSIGNMENT: Creates variable 'lst' and stores the result of '['a', 'b', 'c']' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(lst.index('b'))                                    # [Line 5272] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 1


""" 
Problem: 1449  
Write a Pythonic way to filter dictionary items with values > 10.
"""

# ======================================================================
# PROBLEM 1449 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

d = {'a': 5, 'b': 15}                                    # [Line 5279] | ASSIGNMENT: Creates variable 'd' and stores the result of '{'a': 5, 'b': 15}' in it
filtered = {k: v for k, v in d.items() if v > 10}        # [Line 5280] | ASSIGNMENT: Creates variable 'filtered' and stores the result of '{k: v for k, v in d.items() if v > 10}' in it
print(filtered)                                          # [Line 5281] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {'b': 15}


""" 
Problem: 1450  
Write a Pythonic program to invert a dictionary (keys become values, values become keys).
"""

# ======================================================================
# PROBLEM 1450 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

d = {'a': 1, 'b': 2}                                     # [Line 5288] | ASSIGNMENT: Creates variable 'd' and stores the result of '{'a': 1, 'b': 2}' in it
inverted = {v: k for k, v in d.items()}                  # [Line 5289] | ASSIGNMENT: Creates variable 'inverted' and stores the result of '{v: k for k, v in d.items()}' in it
print(inverted)                                          # [Line 5290] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: {1: 'a', 2: 'b'}

""" 
Problem: 1451  
Write a Python program using `all()` to check if all numbers in a list are positive.
"""

# ======================================================================
# PROBLEM 1451 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = [1, 2, 3, 4]                                       # [Line 5296] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[1, 2, 3, 4]' in it | DATA TYPE: List - A mutable ordered collection. Contains 4 elements
print(all(x > 0 for x in lst))                           # [Line 5297] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1452  
Use `all()` to determine if all characters in a string are lowercase.
"""

# ======================================================================
# PROBLEM 1452 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

s = "hello"                                              # [Line 5304] | ASSIGNMENT: Creates variable 's' and stores the result of ''hello'' in it | DATA TYPE: String - A sequence of characters. Length: 5
print(all(c.islower() for c in s))                       # [Line 5305] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1453  
Write a Pythonic way to use `all()` to check if all elements in a list are even.
"""

# ======================================================================
# PROBLEM 1453 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = [2, 4, 6]                                          # [Line 5312] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[2, 4, 6]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(all(x % 2 == 0 for x in lst))                      # [Line 5313] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1). | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1454  
Check if all items in a dictionary have non-empty values using `all()`.
"""

# ======================================================================
# PROBLEM 1454 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

d = {"a": 1, "b": "hello", "c": [1]}                     # [Line 5320] | SLICING OPERATION - Extracts a portion of the sequence | ASSIGNMENT: Creates variable 'd' and stores the result of '{'a': 1, 'b': 'hello', 'c': [1]}' in it
print(all(bool(v) for v in d.values()))                  # [Line 5321] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1455  
Use `all()` to check if all items in a set are greater than 10.
"""

# ======================================================================
# PROBLEM 1455 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

s = {11, 12, 13}                                         # [Line 5328] | ASSIGNMENT: Creates variable 's' and stores the result of '{11, 12, 13}' in it
print(all(x > 10 for x in s))                            # [Line 5329] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1456  
Use `all()` to validate that all lines in a list start with a capital letter.
"""

# ======================================================================
# PROBLEM 1456 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lines = ["Hello", "World", "Python"]                     # [Line 5336] | ASSIGNMENT: Creates variable 'lines' and stores the result of '['Hello', 'World', 'Python']' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(all(line[0].isupper() for line in lines))          # [Line 5337] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1457  
Use `all()` to check if all elements in a matrix row are equal.
"""

# ======================================================================
# PROBLEM 1457 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

row = [5, 5, 5]                                          # [Line 5344] | ASSIGNMENT: Creates variable 'row' and stores the result of '[5, 5, 5]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(all(x == row[0] for x in row))                     # [Line 5345] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity). | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1458  
Use `all()` to check if all values in a list are strings.
"""

# ======================================================================
# PROBLEM 1458 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = ["a", "b", "c"]                                    # [Line 5352] | ASSIGNMENT: Creates variable 'lst' and stores the result of '['a', 'b', 'c']' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(all(isinstance(x, str) for x in lst))              # [Line 5353] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1459  
Write a Python program that uses `all()` to check if all keys in a dictionary are strings.
"""

# ======================================================================
# PROBLEM 1459 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

d = {"a": 1, "b": 2}                                     # [Line 5360] | ASSIGNMENT: Creates variable 'd' and stores the result of '{'a': 1, 'b': 2}' in it
print(all(isinstance(k, str) for k in d.keys()))         # [Line 5361] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1460  
Use `all()` to verify that all files have a ".txt" extension.
"""

# ======================================================================
# PROBLEM 1460 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

files = ["doc1.txt", "doc2.txt"]                         # [Line 5368] | ASSIGNMENT: Creates variable 'files' and stores the result of '['doc1.txt', 'doc2.txt']' in it | DATA TYPE: List - A mutable ordered collection. Contains 2 elements
print(all(f.endswith(".txt") for f in files))            # [Line 5369] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1461  
Use `all()` to check if all numbers in a list are within a certain range.
"""

# ======================================================================
# PROBLEM 1461 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

nums = [5, 6, 7]                                         # [Line 5376] | ASSIGNMENT: Creates variable 'nums' and stores the result of '[5, 6, 7]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(all(1 <= x <= 10 for x in nums))                   # [Line 5377] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1462  
Check if all sublists in a 2D list are non-empty using `all()`.
"""

# ======================================================================
# PROBLEM 1462 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

matrix = [[1], [2], [3]]                                 # [Line 5384] | ASSIGNMENT: Creates variable 'matrix' and stores the result of '[[1], [2], [3]]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(all(len(sublist) > 0 for sublist in matrix))       # [Line 5385] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1463  
Use `all()` to confirm all booleans in a list are True.
"""

# ======================================================================
# PROBLEM 1463 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

flags = [True, True, True]                               # [Line 5392] | ASSIGNMENT: Creates variable 'flags' and stores the result of '[True, True, True]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(all(flags))                                        # [Line 5393] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1464  
Use `all()` to verify all words in a list contain the letter "a".
"""

# ======================================================================
# PROBLEM 1464 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

words = ["apple", "banana", "grape"]                     # [Line 5400] | ASSIGNMENT: Creates variable 'words' and stores the result of '['apple', 'banana', 'grape']' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(all("a" in word for word in words))                # [Line 5401] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1465  
Write a Python program using `all()` to check if a list of numbers is strictly increasing.
"""

# ======================================================================
# PROBLEM 1465 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

nums = [1, 2, 3, 4]                                      # [Line 5408] | ASSIGNMENT: Creates variable 'nums' and stores the result of '[1, 2, 3, 4]' in it | DATA TYPE: List - A mutable ordered collection. Contains 4 elements
print(all(x < y for x, y in zip(nums, nums[1:])))        # [Line 5409] | SLICING OPERATION [1:] - Extracts all elements starting from index 1 to the end.  | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1466  
Check if all environment variables in a list are defined (non-empty strings).
"""

# ======================================================================
# PROBLEM 1466 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

envs = ["PATH", "HOME", "USER"]                          # [Line 5416] | ASSIGNMENT: Creates variable 'envs' and stores the result of '['PATH', 'HOME', 'USER']' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(all(isinstance(env, str) and env for env in envs))  # [Line 5417] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1467  
Use `all()` to ensure all items in a tuple are of the same type.
"""

# ======================================================================
# PROBLEM 1467 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

t = (1, 2, 3)                                            # [Line 5424] | ASSIGNMENT: Creates variable 't' and stores the result of '(1, 2, 3)' in it | DATA TYPE: Tuple - An immutable ordered collection. Contains 3 elements
print(all(type(x) == type(t[0]) for x in t))             # [Line 5425] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity). | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1468  
Check if all numbers in a list are prime using `all()` and a helper function.
"""

# ======================================================================
# PROBLEM 1468 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def is_prime(n):                                         # [Line 5432]
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1))  # [Line 5433] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1).

lst = [2, 3, 5, 7]                                       # [Line 5435] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[2, 3, 5, 7]' in it | DATA TYPE: List - A mutable ordered collection. Contains 4 elements
print(all(is_prime(x) for x in lst))                     # [Line 5436] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1469  
Use `all()` to confirm all values in a list are not None.
"""

# ======================================================================
# PROBLEM 1469 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = [1, 2, 3]                                          # [Line 5443] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[1, 2, 3]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(all(x is not None for x in lst))                   # [Line 5444] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1470  
Use `all()` to verify that all passwords in a list are at least 8 characters long.
"""

# ======================================================================
# PROBLEM 1470 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

passwords = ["abcdefgh", "12345678", "password"]         # [Line 5451] | ASSIGNMENT: Creates variable 'passwords' and stores the result of '['abcdefgh', '12345678', 'password']' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(all(len(p) >= 8 for p in passwords))               # [Line 5452] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True

""" 
Problem: 1471  
Write a Python program to check if a variable is `None` using `is`.
"""

# ======================================================================
# PROBLEM 1471 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

x = None                                                 # [Line 5458] | ASSIGNMENT: Creates variable 'x' and stores the result of 'None' in it
print(x is None)                                         # [Line 5459] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1472  
Check if two variables point to the same list object using `is`.
"""

# ======================================================================
# PROBLEM 1472 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

a = []                                                   # [Line 5466] | ASSIGNMENT: Creates variable 'a' and stores the result of '[]' in it | DATA TYPE: List - A mutable ordered collection. Contains 0 elements
b = a                                                    # [Line 5467] | ASSIGNMENT: Creates variable 'b' and stores the result of 'a' in it
print(a is b)                                            # [Line 5468] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1473  
Check if two separately created lists are not the same object using `is`.
"""

# ======================================================================
# PROBLEM 1473 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

a = []                                                   # [Line 5475] | ASSIGNMENT: Creates variable 'a' and stores the result of '[]' in it | DATA TYPE: List - A mutable ordered collection. Contains 0 elements
b = []                                                   # [Line 5476] | ASSIGNMENT: Creates variable 'b' and stores the result of '[]' in it | DATA TYPE: List - A mutable ordered collection. Contains 0 elements
print(a is not b)                                        # [Line 5477] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1474  
Use `is` to check if a variable is exactly `True`.
"""

# ======================================================================
# PROBLEM 1474 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

flag = True                                              # [Line 5484] | ASSIGNMENT: Creates variable 'flag' and stores the result of 'True' in it | DATA TYPE: Integer - A whole number: True
print(flag is True)                                      # [Line 5485] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1475  
Use `is` to check identity of two strings (interned strings).
"""

# ======================================================================
# PROBLEM 1475 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

s1 = "hello"                                             # [Line 5492] | ASSIGNMENT: Creates variable 's1' and stores the result of ''hello'' in it | DATA TYPE: String - A sequence of characters. Length: 5
s2 = "hello"                                             # [Line 5493] | ASSIGNMENT: Creates variable 's2' and stores the result of ''hello'' in it | DATA TYPE: String - A sequence of characters. Length: 5
print(s1 is s2)                                          # [Line 5494] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True (implementation detail in CPython)


""" 
Problem: 1476  
Use `is` to check identity of small integers.
"""

# ======================================================================
# PROBLEM 1476 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

a = 100                                                  # [Line 5501] | ASSIGNMENT: Creates variable 'a' and stores the result of '100' in it | DATA TYPE: Integer - A whole number: 100
b = 100                                                  # [Line 5502] | ASSIGNMENT: Creates variable 'b' and stores the result of '100' in it | DATA TYPE: Integer - A whole number: 100
print(a is b)                                            # [Line 5503] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True (due to integer caching)


""" 
Problem: 1477  
Check if a function return value is `None` using `is`.
"""

# ======================================================================
# PROBLEM 1477 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def do_nothing():                                        # [Line 5510]
    pass                                                 # [Line 5511]

print(do_nothing() is None)                              # [Line 5513] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1478  
Use `is` to check if a class attribute is shared.
"""

# ======================================================================
# PROBLEM 1478 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

class A:                                                 # [Line 5520]
    x = []                                               # [Line 5521]

a1 = A()                                                 # [Line 5523] | ASSIGNMENT: Creates variable 'a1' and stores the result of 'A()' in it | FUNCTION CALL: Calls 'A()' and stores its return value
a2 = A()                                                 # [Line 5524] | ASSIGNMENT: Creates variable 'a2' and stores the result of 'A()' in it | FUNCTION CALL: Calls 'A()' and stores its return value
print(a1.x is a2.x)                                      # [Line 5525] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1479  
Use `is` to check if an object is the same before and after a function call.
"""

# ======================================================================
# PROBLEM 1479 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def identity(x):                                         # [Line 5532]
    return x                                             # [Line 5533]

obj = []                                                 # [Line 5535] | ASSIGNMENT: Creates variable 'obj' and stores the result of '[]' in it | DATA TYPE: List - A mutable ordered collection. Contains 0 elements
print(obj is identity(obj))                              # [Line 5536] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1480  
Use `is` to compare with built-in singleton `Ellipsis`.
"""

# ======================================================================
# PROBLEM 1480 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

x = ...                                                  # [Line 5543] | ASSIGNMENT: Creates variable 'x' and stores the result of '...' in it
print(x is Ellipsis)                                     # [Line 5544] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1481  
Check if two instances of a class are not the same object.
"""

# ======================================================================
# PROBLEM 1481 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

class X:                                                 # [Line 5551]
    pass                                                 # [Line 5552]

x1 = X()                                                 # [Line 5554] | ASSIGNMENT: Creates variable 'x1' and stores the result of 'X()' in it | FUNCTION CALL: Calls 'X()' and stores its return value
x2 = X()                                                 # [Line 5555] | ASSIGNMENT: Creates variable 'x2' and stores the result of 'X()' in it | FUNCTION CALL: Calls 'X()' and stores its return value
print(x1 is not x2)                                      # [Line 5556] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1482  
Check identity of two variables referencing the same dictionary.
"""

# ======================================================================
# PROBLEM 1482 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

d1 = {"a": 1}                                            # [Line 5563] | ASSIGNMENT: Creates variable 'd1' and stores the result of '{'a': 1}' in it
d2 = d1                                                  # [Line 5564] | ASSIGNMENT: Creates variable 'd2' and stores the result of 'd1' in it
print(d1 is d2)                                          # [Line 5565] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1483  
Use `is` in an assertion to verify object identity.
"""

# ======================================================================
# PROBLEM 1483 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

a = b = object()                                         # [Line 5572] | ASSIGNMENT: Creates variable 'a' and stores the result of 'object()' in it | FUNCTION CALL: Calls 'object()' and stores its return value
assert a is b                                            # [Line 5573]
print("Assertion passed")                                # [Line 5574] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: Assertion passed

""" 
Problem: 1484  
Compare identity of two Boolean values using `is`.
"""

# ======================================================================
# PROBLEM 1484 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

x = (2 < 3)                                              # [Line 5580] | ASSIGNMENT: Creates variable 'x' and stores the result of '2 < 3' in it
y = True                                                 # [Line 5581] | ASSIGNMENT: Creates variable 'y' and stores the result of 'True' in it | DATA TYPE: Integer - A whole number: True
print(x is y)                                            # [Line 5582] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1485  
Use `is not` to verify a function argument is not None.
"""

# ======================================================================
# PROBLEM 1485 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

def greet(name):                                         # [Line 5589]
    if name is not None:                                 # [Line 5590]
        print(f"Hello, {name}!")                         # [Line 5591]

greet("Alice")                                           # [Line 5593] | FUNCTION CALL: Executes the function 'greet' | ARGUMENTS: Passes 1 argument(s) to the function | Expected: Hello, Alice!


""" 
Problem: 1486  
Use `is` to test if a global constant is unchanged.
"""

# ======================================================================
# PROBLEM 1486 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

SENTINEL = object()                                      # [Line 5600] | ASSIGNMENT: Creates variable 'SENTINEL' and stores the result of 'object()' in it | FUNCTION CALL: Calls 'object()' and stores its return value
def check(x):                                            # [Line 5601]
    return x is SENTINEL                                 # [Line 5602]

value = SENTINEL                                         # [Line 5604] | ASSIGNMENT: Creates variable 'value' and stores the result of 'SENTINEL' in it
print(check(value))                                      # [Line 5605] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1487  
Check that changing a variable makes it no longer the same object.
"""

# ======================================================================
# PROBLEM 1487 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

a = [1, 2]                                               # [Line 5612] | ASSIGNMENT: Creates variable 'a' and stores the result of '[1, 2]' in it | DATA TYPE: List - A mutable ordered collection. Contains 2 elements
b = a                                                    # [Line 5613] | ASSIGNMENT: Creates variable 'b' and stores the result of 'a' in it
a = [1, 2]                                               # [Line 5614] | ASSIGNMENT: Creates variable 'a' and stores the result of '[1, 2]' in it | DATA TYPE: List - A mutable ordered collection. Contains 2 elements
print(a is b)                                            # [Line 5615] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: False


""" 
Problem: 1488  
Use `is` to compare with a constant declared elsewhere.
"""

# ======================================================================
# PROBLEM 1488 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

NONE_CONST = None                                        # [Line 5622] | ASSIGNMENT: Creates variable 'NONE_CONST' and stores the result of 'None' in it
x = None                                                 # [Line 5623] | ASSIGNMENT: Creates variable 'x' and stores the result of 'None' in it
print(x is NONE_CONST)                                   # [Line 5624] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1489  
Use `is` with `not` to check that a value is not `False`.
"""

# ======================================================================
# PROBLEM 1489 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

value = "some text"                                      # [Line 5631] | ASSIGNMENT: Creates variable 'value' and stores the result of ''some text'' in it | DATA TYPE: String - A sequence of characters. Length: 9
print(value is not False)                                # [Line 5632] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True


""" 
Problem: 1490  
Show that identity and equality are not always the same.
"""

# ======================================================================
# PROBLEM 1490 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

a = [1]                                                  # [Line 5639] | ASSIGNMENT: Creates variable 'a' and stores the result of '[1]' in it | DATA TYPE: List - A mutable ordered collection. Contains 1 elements
b = [1]                                                  # [Line 5640] | ASSIGNMENT: Creates variable 'b' and stores the result of '[1]' in it | DATA TYPE: List - A mutable ordered collection. Contains 1 elements
print(a == b)                                            # [Line 5641] | EQUALITY OPERATOR (==) - Compares two values and returns True if they are equal, False otherwise. Note: == checks value equality, not identity (use 'is' for identity). | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: True
print(a is b)                                            # [Line 5642] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: False

""" 
Problem: 1491  
Use `default=` with the `max()` function to return a default when the list is empty.
"""

# ======================================================================
# PROBLEM 1491 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

nums = []                                                # [Line 5648] | ASSIGNMENT: Creates variable 'nums' and stores the result of '[]' in it | DATA TYPE: List - A mutable ordered collection. Contains 0 elements
print(max(nums, default=0))                              # [Line 5649] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: 0


""" 
Problem: 1492  
Use `default=` with the `min()` function to avoid an error on an empty sequence.
"""

# ======================================================================
# PROBLEM 1492 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

values = []                                              # [Line 5656] | ASSIGNMENT: Creates variable 'values' and stores the result of '[]' in it | DATA TYPE: List - A mutable ordered collection. Contains 0 elements
print(min(values, default=-1))                           # [Line 5657] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: -1


""" 
Problem: 1493  
Use `default=` in `max()` to safely get the longest word from a list.
"""

# ======================================================================
# PROBLEM 1493 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

words = []                                               # [Line 5664] | ASSIGNMENT: Creates variable 'words' and stores the result of '[]' in it | DATA TYPE: List - A mutable ordered collection. Contains 0 elements
print(max(words, key=len, default="None"))               # [Line 5665] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: "None"


""" 
Problem: 1494  
Use `default=` with `next()` to get the first even number or -1.
"""

# ======================================================================
# PROBLEM 1494 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

lst = [1, 3, 5]                                          # [Line 5672] | ASSIGNMENT: Creates variable 'lst' and stores the result of '[1, 3, 5]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(next((x for x in lst if x % 2 == 0), default=-1))  # [Line 5673] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1). | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: -1


""" 
Problem: 1495  
Use `default=` in `next()` to safely access an item in a generator.
"""

# ======================================================================
# PROBLEM 1495 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

gen = (x for x in range(5) if x > 10)                    # [Line 5680] | ASSIGNMENT: Creates variable 'gen' and stores the result of '(x for x in range(5) if x > 10)' in it
print(next(gen, default="No item"))                      # [Line 5681] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: "No item"


""" 
Problem: 1496  
Use `default=` with `max()` on a filtered list to handle no matches.
"""

# ======================================================================
# PROBLEM 1496 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

nums = [1, 3, 5]                                         # [Line 5688] | ASSIGNMENT: Creates variable 'nums' and stores the result of '[1, 3, 5]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(max((x for x in nums if x % 2 == 0), default=None))  # [Line 5689] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1). | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: None


""" 
Problem: 1497  
Use `default=` in `min()` to get a fallback value when no condition matches.
"""

# ======================================================================
# PROBLEM 1497 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

nums = [1, 3, 5]                                         # [Line 5696] | ASSIGNMENT: Creates variable 'nums' and stores the result of '[1, 3, 5]' in it | DATA TYPE: List - A mutable ordered collection. Contains 3 elements
print(min((x for x in nums if x % 2 == 0), default=-1))  # [Line 5697] | MODULO OPERATOR (%) - Returns the remainder after division. Example: 10 % 3 = 1 (because 10 divided by 3 is 3 with remainder 1). Commonly used to check if a number is even (x % 2 == 0) or odd (x % 2 == 1). | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: -1


""" 
Problem: 1498  
Use `default=` with `next()` to find the first name starting with "Z".
"""

# ======================================================================
# PROBLEM 1498 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

names = ["Alice", "Bob"]                                 # [Line 5704] | ASSIGNMENT: Creates variable 'names' and stores the result of '['Alice', 'Bob']' in it | DATA TYPE: List - A mutable ordered collection. Contains 2 elements
print(next((name for name in names if name.startswith("Z")), default="Not found"))  # [Line 5705] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: "Not found"


""" 
Problem: 1499  
Use `default=` with `max()` to find the max in a sublist or return a placeholder.
"""

# ======================================================================
# PROBLEM 1499 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

data = []                                                # [Line 5712] | ASSIGNMENT: Creates variable 'data' and stores the result of '[]' in it | DATA TYPE: List - A mutable ordered collection. Contains 0 elements
print(max(data, default="empty"))                        # [Line 5713] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: "empty"


""" 
Problem: 1500  
Use `default=` in `next()` to handle an empty comprehension.
"""

# ======================================================================
# PROBLEM 1500 - WORKFLOW SUMMARY
# ======================================================================
# This problem demonstrates Python programming concepts.
# Let's trace through the code step by step:

print(next((x for x in []), default="Empty"))            # [Line 5720] | PRINT FUNCTION: Outputs one or more values to the console/terminal | WORKFLOW: This is an output statement that displays results to the user | Expected: "Empty"








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
