#function problems level 1 (chatGPT￼)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# Ce problème nous demande de créer une fonction that performs basic addition.
# La fonction doit accepter two paramètre numériques (integers or floats) and
# return their sum. C'est une opération fondamentale arithmetic operation qui démontre
# la définition de fonction, parameters, et les instructions de retour en Python.
#
# Prérequis Clés :
# - Function must take exactly two paramètre numériques
# - Function must return the sum of the two parameters
# - Doit fonctionner avec les entiers et les nombres à virgule flottante
#
# Exemple d'Entrée/Sortie :
# - add_numbers(5, 5) should return 10
# - add_numbers(3.5, 2.5) should return 6.0
# - add_numbers(-10, 15) should return 5
# ============================================================================
"""
Problème 1 :
Écrivez une fonction Python appelée `add_numbers` qui prend deux nombres comme paramètres et retourne leur somme.
"""

# EXPLICATION DE LA SOLUTION :
# C'est une solution concise en une ligne that directly returns the sum.
# La fonction prend two parameters 'a' and 'b' which peuvent être de tout type numérique.
# The '+' operator works with integers, floats, and even complex numbers.
# Cette approche est économe en mémoire car elle ne stocke pas de valeurs intermédiaires.
def add_number(a, b):
    return a + b  # Returns the sum of parameters a and b

# CAS DE TEST :
# This démontre la fonction with two positive integers (5 and 5).
# Le résultat attendu est 10, qui sera affiché dans la console.
print(add_number(5, 5))  # Sortie : 10

# ALTERNATIVE EXPLICATION DE LA SOLUTION :
# Cette solution utilise une variable intermédiaire pour stocker le résultat avant de le retourner.
# Bien que fonctionnellement identique à la solution précédente, this approach can be
# more readable for beginners et permet un débogage plus facile if you need to
# inspect the value before returning. The variable 'result' holds the sum.
def add_num(a, b):
    result = a + b  # Calculate the sum and store it in 'result'
    return result   # Return the stored result

# CAS DE TEST :
# Même cas de test que ci-dessus, démontrant que les deux solutions produisent la même sortie.
print(add_num(5, 5))  # Sortie : 10

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function that performs multiplication.
# La fonction doit accepter two paramètre numériques and return their product
# (the result of multiplying them together). Cela démontre the use of
# the multiplication operator (*) en Python functions.
#
# Prérequis Clés :
# - Function must take exactly two paramètre numériques
# - Function must return the product (multiplication result)
# - Should handle integers, floats, and negative numbers correctly
#
# Exemple d'Entrée/Sortie :
# - multiply_numbers(5, 5) should return 25
# - multiply_numbers(3.5, 2) should return 7.0
# - multiply_numbers(-4, 5) should return -20
# - multiply_numbers(0, 100) should return 0 (any number times zero is zero)
# ============================================================================
"""
Problème 2 :
Écrivez une fonction Python appelée `multiply_numbers` qui prend deux nombres comme paramètres et retourne leur produit.
"""

# EXPLICATION DE LA SOLUTION :
# This function uses Python's multiplication operator (*) to calculate the product.
# La fonction prend two parameters 'a' and 'b', multiplies them together, and
# returns the result directly. This is the most straightforward approach.
def multiply_numbers(a, b):
    return a * b  # Returns the product of a multiplied by b

# CAS DE TEST :
# This test multiplies 5 by 5, which should result in 25.
print(multiply_numbers(5, 5))  # Sortie : 25

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem asks us to find the largest (maximum) number in a list of numbers.
# La fonction doit accepter a list containing numeric values and return the
# highest value among them. This is une opération courante operation in data analysis and
# algorithm design.
#
# Prérequis Clés :
# - Function must accept a list of numbers as input
# - Function must return the maximum value from the list
# - Should handle both positive and negative numbers
# - Doit fonctionner avec integers and floats
#
# Exemple d'Entrée/Sortie :
# - find_max([2, 67, 300]) should return 300
# - find_max([5, 100, 3, 8, 15]) should return 100
# - find_max([-10, -5, -20]) should return -5 (least negative is maximum)
#
# Edge Cases:
# - Empty list would cause an error (not handled in these solutions)
# - Single-element list should return that element
# ============================================================================
"""
Problème 3 :
Écrivez une fonction Python appelée `find_max` qui prend une liste de nombres en entrée et retourne le maximum nombre dans la liste.
"""

# EXPLICATION DE LA SOLUTION (Using Built-in Function):
# This solution uses Python's built-in max() function, which is the most
# efficient and Pythonic way to find the maximum value. The max() function
# iterates through the list internally and returns the largest element.
# This is the recommended approach for production code.
def find_max(number):
    return max(number)  # Built-in function returns the maximum value

# CAS DE TEST :
# This test uses a list with three numbers: 2, 67, and 300.
# The maximum value is 300, which will be printed.
result = [2, 67, 300]
print(find_max(result))  # Sortie : 300

# ALTERNATIVE EXPLICATION DE LA SOLUTION (Manual Implementation):
# This solution manually implements the max-finding algorithm without using
# the built-in max() function. It demonstrates how to find the maximum using
# a loop and comparison. This approach is useful for learning purposes and
# understanding the underlying algorithm.
def find_max(numbers):
    # Initialize max_number with the first element of the list
    # This assumes the list is not empty
    max_number = numbers[0]

    # Iterate through each number in the list
    for num in numbers:
        # Compare current number with the current maximum
        # If current number is greater, update max_number
        if num > max_number:
            max_number = num  # Update max_number to the new maximum
    return max_number  # Return the maximum value found

# CAS DE TEST :
# This test uses a list with five numbers and includes a formatted output message.
numbers_list = [5, 100, 3, 8, 15]
print("The maximum number in the list is:", find_max(numbers_list))  # Sortie : The maximum number in the list is: 100

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires calculating the average (arithmetic mean) of a list
# of numbers. The average is calculated by summing all numbers and dividing
# by the count of numbers. The problem specifically asks to use sum() and len()
# functions, which are built-en Python functions.
#
# Prérequis Clés :
# - Function must accept a list of numbers
# - Function must return the average (mean) of all numbers
# - Must use sum() to calculate the total
# - Must use len() to get the count of numbers
#
# Formula: average = sum(numbers) / len(numbers)
#
# Exemple d'Entrée/Sortie :
# - calculate_average([1, 67, 888]) should return (1+67+888)/3 = 318.67...
# - calculate_average([44, 67, 54]) should return (44+67+54)/3 = 55.0
# - calculate_average([10, 20, 30, 40]) should return 25.0
#
# Edge Cases:
# - Empty list would cause division by zero error (not handled)
# - Single-element list returns that element
# ============================================================================
"""
Problème 4 :
Écrivez une fonction Python appelée `calculate_average` qui prend une liste de nombres en entrée et retourne le moyenne de ces nombres. Utilisez sum() et len().
"""

# EXPLICATION DE LA SOLUTION :
# This solution uses Python's built-in sum() function to add all numbers in
# the list, then divides by len() to get the count. The result is stored in
# a variable before returning, which makes the code clear and readable.
def calculate_average(number):
    # sum(number) adds all elements in the list
    # len(number) returns the number of elements
    # Division gives us the average (mean)
    result = sum(number) / len(number)
    return result  # Return the calculated average

# CAS DE TEST :
# This test calculates the average of [1, 67, 888].
# Sum = 956, Count = 3, Average = 956/3 = 318.666...
lst = [1, 67, 888]
print(calculate_average(lst))  # Sortie : 318.6666666666667

# ALTERNATIVE EXPLICATION DE LA SOLUTION :
# This is essentially the same solution with a different function name.
# The logic is identical: sum all numbers and divide by the count.
# The comment "#hardcoded" suggests this might have been intended as a
# manual calculation, but it still uses sum() and len() as required.
def cal_average(number):
    # Calculate sum of all numbers divided by the count
    result = sum(number) / len(number)

    return result  # Return the average

# CAS DE TEST :
# This test calculates the average of [44, 67, 54].
# Sum = 165, Count = 3, Average = 165/3 = 55.0
lst = [44,67,54]
print(cal_average(lst))  # Sortie : 55.0

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem asks us to count the number of vowels in a given string.
# Vowels are defined as the letters: a, e, i, o, u (both lowercase and uppercase).
# The problem specifies to ignore case sensitivity, meaning 'A' and 'a' should
# both be counted as vowels. This is une opération courante string processing task.
#
# Prérequis Clés :
# - Function must accept a string as input
# - Function must count vowels: a, e, i, o, u (case-insensitive)
# - Must return the total count of vowels found
#
# Exemple d'Entrée/Sortie :
# - count_vowels("Jonathan") should return 3 (o, a, a)
# - count_vowels("Hello") should return 2 (e, o)
# - count_vowels("AEIOU") should return 5 (all vowels)
# - count_vowels("xyz") should return 0 (no vowels)
#
# Remarque : The current solution only checks lowercase vowels, which may not
# fully satisfy the case-insensitive requirement. A better solution would
# convert the string to lowercase first.
# ============================================================================
"""
Problème 5 :
Écrivez une fonction Python appelée `count_vowels` qui prend une chaîne en entrée et retourne le nombre de voyelles (a, e, i, o, u) dans la chaîne. Ignorez la casse.
"""

# EXPLICATION DE LA SOLUTION :
# This solution iterates through each character in the string and checks if
# it's a vowel. However, it only checks against lowercase vowels "aeiou",
# which means uppercase vowels won't be counted. To properly handle
# case-insensitivity, the string should be converted to lowercase first.
def count_vowels(string):
    count = 0  # Initialize counter to zero

    # Iterate through each character in the string
    for char in string:
        # Check if the character is a lowercase vowel
        # Remarque : This doesn't handle uppercase vowels (A, E, I, O, U)
        if char in "aeiou":
            count += 1  # Increment counter if vowel found
    return count  # Return the total count of vowels

# CAS DE TEST :
# This test counts vowels in "Jonathan". The vowels are: o, a, a (3 total).
# However, if the string contained uppercase vowels, they wouldn't be counted
# with this implementation.
result = "Jonathan"
print(count_vowels(result))  # Sortie : 3

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires reversing a string - creating a new string where the
# characters appear in the opposite order. For example, "hello" becomes "olleh".
# This is une opération courante string manipulation task that can be solved using Python's
# slicing syntax or by iterating through the string.
#
# Prérequis Clés :
# - Function must accept a string as input
# - Function must return a new string with characters in reverse order
# - Original string should remain unchanged (though this solution modifies it)
#
# Exemple d'Entrée/Sortie :
# - reverse_string("Jonathan") should return "nahtanoJ"
# - reverse_string("hello") should return "olleh"
# - reverse_string("a") should return "a" (single character)
# - reverse_string("") should return "" (empty string)
#
# Remarque : The solution uses string slicing [::-1], which is the most Pythonic
# and efficient way to reverse a string en Python.
# ============================================================================
"""
Problème 6 :
Écrivez une fonction Python appelée `reverse_string` qui prend une chaîne en entrée et retourne le reverse de cette chaîne.
"""

# EXPLICATION DE LA SOLUTION :
# This solution uses Python's extended slicing syntax [::-1] to reverse the string.
# The syntax [start:stop:step] with step=-1 means:
# - Start from the end
# - Go to the beginning
# - Step backwards by 1
# This creates a reversed copy of the string efficiently.
def reverse_string(string):
    # [::-1] is Python's slicing syntax that reverses the string
    # It creates a new string with characters in reverse order
    string = string[::-1]

    return string  # Return the reversed string

# CAS DE TEST :
# This test reverses "Jonathan" to "nahtanoJ".
# Each character is placed in the opposite position.
result = "Jonathan"
print(reverse_string(result))  # Sortie : nahtanoJ

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem asks us to determine if a number is even. An even number is
# any integer that is divisible by 2 with no remainder. C'est une opération fondamentale
# mathematical operation that's commonly used in programming for conditional
# logic and loops.
#
# Prérequis Clés :
# - Function must accept an integer as input
# - Function must return True if the number is even
# - Function must return False if the number is odd
#
# Mathematical Definition:
# - Even number: divisible by 2 (remainder is 0 when divided by 2)
# - Odd number: not divisible by 2 (remainder is 1 when divided by 2)
#
# Exemple d'Entrée/Sortie :
# - is_even(10) should return True (10 ÷ 2 = 5 with remainder 0)
# - is_even(7) should return False (7 ÷ 2 = 3 with remainder 1)
# - is_even(0) should return True (0 is considered even)
# - is_even(-4) should return True (negative even numbers are still even)
#
# The modulo operator (%) is used to check the remainder after division.
# ============================================================================
"""
Problème 7 :
Écrivez une fonction Python appelée `is_even` qui prend un entier en entrée et retourne vrai si le nombre est pair, et False sinon.
"""

# EXPLICATION DE LA SOLUTION :
# This solution uses the modulo operator (%) to check if a number is even.
# The modulo operator returns the remainder after division. If number % 2 == 0,
# it means the number is divisible by 2 with no remainder, making it even.
# This is the most efficient and common way to check for even numbers.
def is_even(number):
    # number % 2 calculates the remainder when number is divided by 2
    # If remainder is 0, the number is even (returns True)
    # If remainder is 1, the number is odd (returns False)
    return number % 2 == 0

# CAS DE TEST :
# This test checks if 10 is even. Since 10 ÷ 2 = 5 with remainder 0,
# La fonction doit retourner True.
result = 10
print(is_even(result))  # Sortie : True

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires calculating the square of a number. The square of a
# number is the result of multiplying that number to the power of 2. For example,
# the square of 5 is 25 (5 × 5 = 25). C'est une opération de base mathematical operation.
#
# Prérequis Clés :
# - Function must accept a number (integer or float) as input
# - Function must return the square (number × number)
# - Doit fonctionner avec both positive and negative numbers
#
# Mathematical Definition:
# - Square of n = n × n = n²
# - Square of -5 = (-5) × (-5) = 25 (squares are always positive or zero)
#
# Exemple d'Entrée/Sortie :
# - calculate_square(6) should return 36 (6 ** 2)
# - calculate_square(9) should return 81 (9 ** 2)
# - calculate_square(-4) should return 16 ((-4) ** 2)
# - calculate_square(3.5) should return 12.25 (3.5 ** 2)
#
# Remarque : The first solution has a bug - it uses number ** 2 (power operation)
# instead of number ** 2, which would calculate number to the power of itself
# rather than the square. For example, 9 ** 9 = 387,420,489, not 81.
# ============================================================================
"""
Problème 8 :
Écrivez une fonction Python appelée `calculate_square` qui prend un nombre en entrée et retourne le carré de cette nombre.
"""

# EXPLICATION DE LA SOLUTION (BUGGY VERSION):
# ATTENTION : This solution has a bug! It uses number ** 2 instead of number ** 2.
# The ** operator is Python's exponentiation operator. number ** 2 means
# "number raised to the power of number", not "number squared".
# For example: 9 ** 9 = 387,420,489 (not 81, which is 9²).
# The correct syntax should be: number ** 2
def cal_square(number):
    # BUG: This calculates number**2, not number squared
    # Should be: return number ** 2
    return number ** 2

# CAS DE TEST :
# This test attempts to square 9, but due to the bug, it calculates 9^9 instead.
# Expected: 81, Actual: 387,420,489
lst = 9
print(cal_square(lst))  # Sortie : 81

# CORRECT EXPLICATION DE LA SOLUTION :
# This solution correctly calculates the square by multiplying the number to the power of 2.
# This is the most straightforward approach and clearly shows what "square" means.
def calculate_square(number):
    # Multiply number to the power of 2 to get the square
    square = number ** 2

    return square  # Return the squared value

# CAS DE TEST :
# This test correctly squares 6: 6 ** 2 = 36
print(calculate_square(6))  # Sortie : 36

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem asks us to create a greeting function that takes a person's name
# and returns a personalized greeting message. The function should format the
# message as "Hello, [name]!" where [name] is replaced with the actual name
# provided as input. Cela démontre string formatting and function usage.
#
# Prérequis Clés :
# - Function must accept a string parameter (the name)
# - Function must return or print a greeting message
# - Message format should be "Hello, [name]!"
#
# Exemple d'Entrée/Sortie :
# - greet_user("Jonathan") should return "Hello, Jonathan!"
# - greet_user("Alice") should return "Hello, Alice!"
#
# Remarque : The solution uses f-string formatting, which is a modern Python feature
# for string interpolation. The actual output format may vary slightly.
# ============================================================================
"""
Problème 9 :
Écrivez une fonction Python appelée `greet_user` qui prend une chaîne `name` en entrée et affiche un message de salutation message dans le format "Hello, [nom]!".
"""

# EXPLICATION DE LA SOLUTION :
# This solution uses Python's f-string (formatted string literal) to create
# the greeting message. The f-string allows embedding variables directly
# into the string using curly braces {}. This is the most readable and
# efficient way to format strings in modern Python.
def greet_user(string):
    # f-string syntax: f"text {variable}" embeds the variable value
    # Remarque : The output uses lowercase "hello" instead of "Hello" as specified
    return f"hello {string}"  # Returns formatted greeting string

# CAS DE TEST :
# This test greets "Jonathan" with the message "hello Jonathan"
print(greet_user("Jonathan"))  # Sortie : hello Jonathan

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function that squares each number in a list.
# La fonction doit prendre a list of numbers as input and return a new list
# where each element is the square of the corresponding element in the input list.
# Cela démontre list comprehension, iteration, and mathematical operations.
#
# Prérequis Clés :
# - Function must accept a list of numbers
# - Function must return a NEW list (not modify the original)
# - Each element in the new list should be the square of the corresponding element
#
# Exemple d'Entrée/Sortie :
# - square_list([2, 4, 5, 6]) should return [4, 16, 25, 36]
# - square_list([1, 3, 5]) should return [1, 9, 25]
# - square_list([-2, 0, 2]) should return [4, 0, 4]
#
# The square of a number n is n × n or n².
# ============================================================================
"""
Problème 10 :
Écrivez une fonction Python appelée `square_list` qui prend une liste de nombres en entrée et retourne une nouvelle liste avec chaque nombre au carré.
"""

# EXPLICATION DE LA SOLUTION :
# This solution creates a new empty list and iterates through each number in
# the input list. For each number, it calculates the square using the **
# operator (exponentiation) and appends it to the new list. This approach
# is clear and easy to understand, making it good for learning purposes.
def square_lst(numbers):
    squared_numbers = []  # Initialize empty list to store squared values

    # Iterate through each number in the input list
    for number in numbers:
        # Calculate square using ** operator (number ** 2 = number squared)
        # and append to the new list
        squared_numbers.append(number ** 2)
    return squared_numbers  # Return the new list with squared values

# CAS DE TEST :
# This test squares each number in [2, 4, 5, 6]:
# 2² = 4, 4² = 16, 5² = 25, 6² = 36
# Résultat: [4, 16, 25, 36]
result = [2, 4, 5, 6]
print(square_lst(result))  # Sortie : [4, 16, 25, 36]

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem asks us to convert all characters in a string to uppercase.
# La fonction doit prendre a string as input and return a new string where
# all lowercase letters are converted to their uppercase equivalents, while
# uppercase letters and non-letter characters remain unchanged.
#
# Prérequis Clés :
# - Function must accept a string as input
# - Function must return a string with all characters in uppercase
# - Non-letter characters (numbers, symbols, spaces) remain unchanged
#
# Exemple d'Entrée/Sortie :
# - convert_to_uppercase("Jonathan") should return "JONATHAN"
# - convert_to_uppercase("Hello World") should return "HELLO WORLD"
# - convert_to_uppercase("abc123") should return "ABC123"
#
# Python's built-in .upper() method handles this conversion efficiently.
# ============================================================================
"""
Problème 11 :
Écrivez une fonction Python appelée `convert_to_uppercase` qui prend une chaîne en entrée et retourne la chaîne avec tous ses caractères converted à uppercase.
"""

# EXPLICATION DE LA SOLUTION :
# This solution uses Python's built-in string method .upper() which converts
# all lowercase letters in the string to uppercase. This is the most efficient
# and Pythonic way to perform this operation. The method returns a new string
# and doesn't modify the original string.
def covert_uppercase(string):
    # .upper() is a string method that returns a new string with all
    # lowercase letters converted to uppercase
    return string.upper()  # Returns uppercase version of the string

# CAS DE TEST :
# This test converts "Jonathan" to "JONATHAN"
# All lowercase letters (o, a, t, h, a, n) are converted to uppercase
print(covert_uppercase("Jonathan"))  # Sortie : JONATHAN

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires calculating the sum of all numbers in a list. The
# function should take a list of numbers as input and return the total sum
# of all elements. C'est une opération fondamentale list operation that's commonly used
# in data processing and mathematical calculations.
#
# Prérequis Clés :
# - Function must accept a list of numbers
# - Function must return the sum of all numbers in the list
# - Doit fonctionner avec integers, floats, and mixed numeric types
#
# Exemple d'Entrée/Sortie :
# - calculate_sum([1, 56, 778]) should return 835 (1 + 56 + 778)
# - calculate_sum([10, 20, 30]) should return 60
# - calculate_sum([-5, 10, -3]) should return 2
#
# Python provides a built-in sum() function, but the problem can also be
# solved manually using a loop to demonstrate the algorithm.
# ============================================================================
"""
Problème 12 :
Écrivez une fonction Python appelée `calculate_sum` qui prend une liste de nombres en entrée et retourne le somme de tous le nombres dans la liste.
"""

# EXPLICATION DE LA SOLUTION (Using Built-in Function):
# This solution uses Python's built-in sum() function, which is the most
# efficient and Pythonic way to calculate the sum of a list. The sum()
# function internally iterates through the list and adds all elements together.
# This is the recommended approach for production code.
def calculate_sum(number):
    # sum() is a built-in function that returns the sum of all elements
    # in an iterable (list, tuple, etc.)
    return sum(number)  # Returns the total sum

# CAS DE TEST :
# This test sums [1, 56, 778]: 1 + 56 + 778 = 835
lst = [1, 56, 778]
print(calculate_sum(lst))  # Sortie : 835

# ALTERNATIVE EXPLICATION DE LA SOLUTION (Manual Implementation):
# This solution manually implements the sum calculation using a loop.
# It initializes a counter to 0, then iterates through each number and
# adds it to the counter. This approach demonstrates the underlying algorithm
# and is useful for learning purposes, though less efficient than sum().
def cal_sum(numbers):
    count = 0  # Initialize counter to zero (will accumulate the sum)

    # Iterate through each number in the list
    for number in numbers:
        count += number  # Add current number to the running total
    return count  # Return the final sum

# CAS DE TEST :
# Même cas de test que ci-dessus, demonstrating that both solutions produce
# the same result: 1 + 56 + 778 = 835
lst = [1, 56, 778]
print(cal_sum(lst))  # Sortie : 835

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem asks us to determine if a number is odd. An odd number is any
# integer that is NOT divisible by 2, meaning it has a remainder of 1 when
# divided by 2. This is the opposite of an even number check.
#
# Prérequis Clés :
# - Function must accept an integer as input
# - Function must return True if the number is odd
# - Function must return False if the number is even
#
# Mathematical Definition:
# - Odd number: NOT divisible by 2 (remainder is 1 when divided by 2)
# - Even number: divisible by 2 (remainder is 0 when divided by 2)
#
# Exemple d'Entrée/Sortie :
# - is_odd(7) should return True (7 ÷ 2 = 3 with remainder 1)
# - is_odd(10) should return False (10 ÷ 2 = 5 with remainder 0)
# - is_odd(0) should return False (0 is even)
# - is_odd(-3) should return True (negative odd numbers are still odd)
#
# ATTENTION : The current solution has a bug! It checks if number % 2 == 0,
# which actually checks if the number is EVEN, not odd. The correct check
# should be number % 2 != 0 or number % 2 == 1.
# ============================================================================
"""
Problème 13 :
Écrivez une fonction Python appelée `is_odd` qui prend un entier en entrée et retourne vrai si le nombre est impair, et False sinon.
"""

# EXPLICATION DE LA SOLUTION (BUGGY VERSION):
# ATTENTION : This solution has a critical bug! It checks if number % 2 == 0,
# which determines if a number is EVEN, not odd. This is the opposite of
# what the problem asks for. The correct implementation should check if
# number % 2 != 0 (or number % 2 == 1) to determine if a number is odd.
def is_odd(number):
    # BUG: This checks if number is even, not odd!
    # Should be: return number % 2 != 0  or  return number % 2 == 1
    return number % 2 == 0  # This returns True for even numbers (WRONG!)

# CAS DE TEST :
# This test checks if 10 is odd. Since 10 is even (10 % 2 == 0),
# the function incorrectly returns True when it should return False.
print(is_odd(10))  # Sortie : True (INCORRECT - 10 is even, not odd!)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires concatenating (joining together) two strings into a
# single string. La fonction doit prendre two string parameters and return a
# new string that contains the first string followed by the second string.
# C'est une opération fondamentale string operation in programming.
#
# Prérequis Clés :
# - Function must accept two string parameters
# - Function must return a new string (concatenation of both inputs)
# - The first string should come before the second string in the result
#
# Exemple d'Entrée/Sortie :
# - concatenate_strings("Jonathan", "noll") should return "Jonathannoll"
# - concatenate_strings("Hello", "World") should return "HelloWorld"
# - concatenate_strings("", "test") should return "test" (empty string + string)
#
# en Python, the + operator is used for string concatenation.
# ============================================================================
"""
Problème 14 :
Écrivez une fonction Python appelée `concatenate_strings` qui prend deux strings en entrée et retourne une nouvelle chaîne qui est le concatenation de le deux entrée strings.
"""

# EXPLICATION DE LA SOLUTION :
# Cette solution utilise une variable intermédiaire to store the concatenated result
# before returning it. The + operator joins the two strings together. This
# approach is clear and makes the concatenation operation explicit.
def concatenate_strings(string1, string2):
    # The + operator concatenates (joins) two strings together
    concatenate = string1 + string2  # Join string1 and string2
    return concatenate  # Return the concatenated string

# CAS DE TEST :
# This test concatenates "Jonathan" and "noll" to produce "Jonathannoll"
lst1 = "Jonathan"
lst2 = "noll"
print(concatenate_strings(lst1, lst2))  # Sortie : Jonathannoll

# ALTERNATIVE EXPLICATION DE LA SOLUTION :
# This is a more concise version that directly returns the concatenated string
# without using an intermediate variable. Both solutions are functionally
# identical, but this one is more compact.
def concatenate_string(string1, string2):
    # Directly return the concatenated string
    return string1 + string2  # Returns string1 followed by string2

# CAS DE TEST :
# Même cas de test que ci-dessus, demonstrating both solutions produce the same result
print(concatenate_string("Jonathan", "noll"))  # Sortie : Jonathannoll

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem asks us to find the length (number of characters) in a string.
# La fonction doit prendre a string as input and return the total count of
# characters in that string. C'est une opération de base string operation that's used
# frequently in programming for validation, formatting, and processing.
#
# Prérequis Clés :
# - Function must accept a string as input
# - Function must return the number of characters in the string
# - Should count all characters including spaces, punctuation, and numbers
#
# Exemple d'Entrée/Sortie :
# - find_length("Jonathan") should return 8 (8 characters)
# - find_length("Hello World") should return 11 (including the space)
# - find_length("") should return 0 (empty string has zero length)
#
# Python provides a built-in len() function, but the problem can also be
# solved manually to demonstrate the counting algorithm.
# ============================================================================
"""
Problème 15 :
Écrivez une fonction Python appelée `find_length` qui prend une chaîne en entrée et retourne la longueur de cette chaîne.
"""

# EXPLICATION DE LA SOLUTION (Using Built-in Function):
# This solution uses Python's built-in len() function, which is the most
# efficient and Pythonic way to get the length of a string (or any sequence).
# The len() function internally counts the elements and returns the count.
# This is the recommended approach for production code.
def find_length(string):
    # len() is a built-in function that returns the number of characters
    # in a string (or elements in any sequence)
    return len(string)  # Returns the length of the string

# CAS DE TEST :
# This test finds the length of "Jonathan", which has 8 characters:
# J-o-n-a-t-h-a-n
print(find_length("Jonathan"))  # Sortie : 8

# ALTERNATIVE EXPLICATION DE LA SOLUTION (Manual Implementation):
# This solution manually implements the length calculation by iterating
# through each character and counting them. Cela démontre the underlying
# algorithm and is useful for learning, though less efficient than len().
def find_len(string):
    count = 0  # Initialize counter to zero

    # Iterate through each character in the string
    for char in string:
        count += 1  # Increment counter for each character found
    return count  # Return the total count (length)

# CAS DE TEST :
# Même cas de test que ci-dessus, demonstrating that both solutions produce
# the same result: "Jonathan" has 8 characters
print(find_len("Jonathan"))  # Sortie : 8

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem asks us to determine if a string is a palindrome. A palindrome
# is a word, phrase, or sequence that reads the same forwards and backwards.
# Examples include "racecar", "level", and "madam". The function should handle
# case-insensitivity and ignore spaces for phrases like "A man a plan a canal Panama".
#
# Prérequis Clés :
# - Function must accept a string as input
# - Function must return True if the string is a palindrome, False otherwise
# - Should handle case-insensitivity (treat 'A' and 'a' as the same)
# - Should ignore spaces (for multi-word palindromes)
#
# Exemple d'Entrée/Sortie :
# - is_palindrome("racecar") should return True (reads same forwards/backwards)
# - is_palindrome("level") should return True
# - is_palindrome("tom") should return False (tom != mot)
# - is_palindrome("A man a plan a canal Panama") should return True (ignoring case/spaces)
#
# Algorithm: Compare the string with its reverse after normalizing (lowercase, no spaces).
# ============================================================================
"""
Problème 16 :
Écrivez une fonction Python appelée `is_palindrome` qui prend une chaîne en entrée et retourne vrai si la chaîne est un palindrome (lit le même forwards et backwards), et False sinon.
"""

# EXPLICATION DE LA SOLUTION :
# This solution normalizes the string first by removing spaces and converting
# to lowercase, then compares it with its reverse. If they're equal, it's a
# palindrome. The [::-1] slicing creates a reversed copy of the string.
def is_palindrome(string):
    # Normalize the string: remove spaces and convert to lowercase
    # This allows the function to handle phrases and case variations
    string = string.replace(" ", "").lower()  # Remove spaces, convert to lowercase

    # Compare the normalized string with its reverse
    # [::-1] creates a reversed copy of the string
    # If string == string[::-1], it reads the same forwards and backwards
    return string == string[::-1]  # Returns True if palindrome, False otherwise

# CAS DE TEST :
# This test checks if "tom" is a palindrome.
# Normalized: "tom", Reversed: "mot"
# Since "tom" != "mot", it returns False
print(is_palindrome("tom"))  # Sortie : False

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires counting the number of words in a string. Words are
# defined as sequences of characters separated by spaces. The function should
# split the string by spaces and count how many word segments exist. This is
# une opération courante text processing task used in word counting, text analysis, and
# natural language processing.
#
# Prérequis Clés :
# - Function must accept a string as input
# - Function must return the number of words (space-separated segments)
# - Words are separated by spaces (single or multiple spaces)
#
# Exemple d'Entrée/Sortie :
# - count_words("This is an example sentence.") should return 5
# - count_words("Hello World") should return 2
# - count_words("  multiple   spaces  ") should return 2 (leading/trailing spaces ignored)
# - count_words("") should return 0 (empty string has no words)
#
# Python's split() method automatically handles multiple spaces and trims whitespace.
# ============================================================================
"""
Problème 17 :
Écrivez une fonction Python appelée `count_words` qui prend une chaîne en entrée et retourne le nombre de mots dans la chaîne. Supposons que words sont séparés by spaces.
"""

# EXPLICATION DE LA SOLUTION (Manual Counting):
# This solution uses split() to separate words, then manually counts them
# using a loop. The split() method splits the string by whitespace (spaces,
# tabs, newlines) and returns a list of words. This approach demonstrates
# the counting process explicitly.
def count_words(string):
    # split() splits the string by whitespace and returns a list of words
    words = string.split()  # Creates list of words (e.g., ["This", "is", "an", ...])
    word_count = 0  # Initialize counter

    # Iterate through each word and increment counter
    for word in words:
        word_count += 1  # Count each word

    return word_count  # Return the total word count

# CAS DE TEST :
# This test counts words in "This is an example sentence."
# After splitting: ["This", "is", "an", "example", "sentence."] = 5 words
example_string = "This is an example sentence."
print(count_words(example_string))  # Sortie : 5

# ALTERNATIVE EXPLICATION DE LA SOLUTION (Using len()):
# This is a more concise solution that uses len() directly on the split result.
# Since split() returns a list, len() gives us the count of words directly.
# This is the most Pythonic and efficient approach.
def count_words(string):
    # split() creates a list of words, len() counts the elements
    words = string.split()  # Split string into list of words
    return len(words)  # Return the length of the list (word count)

# CAS DE TEST :
# Même cas de test que ci-dessus, demonstrating both solutions produce the same result
example_string = "This is an example sentence."
print(count_words(example_string))  # Sortie : 5

# ALTERNATIVE EXPLICATION DE LA SOLUTION :
# This solution uses split() and len() to count words directly.
def count_words(string):
    words = string.split()
    return len(words)

# CAS DE TEST :
# "hello you pal" has 3 words
arg = "hello you pal"
print(count_words(arg))  # Sortie : 3

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires finding the smallest (minimum) number in a list of numbers.
# La fonction doit accepter a list containing numeric values and return the
# lowest value among them. This is the opposite of finding the maximum and is
# a fundamental operation in data analysis and algorithm design.
#
# Prérequis Clés :
# - Function must accept a list of numbers as input
# - Function must return the minimum value from the list
# - Should handle both positive and negative numbers
# - Doit fonctionner avec integers and floats
#
# Exemple d'Entrée/Sortie :
# - find_min([1, 56, 68]) should return 1
# - find_min([45, 6, 1]) should return 1
# - find_min([-10, -5, -20]) should return -20 (most negative is minimum)
# - find_min([3.5, 1.2, 4.8]) should return 1.2
#
# Edge Cases:
# - Empty list would cause an error (not handled in these solutions)
# - Single-element list should return that element
# ============================================================================
"""
Problème 18 :
Écrivez une fonction Python appelée `find_min` qui prend une liste de nombres comme argument d'entrée et retourne le minimum nombre dans la liste.
"""

# EXPLICATION DE LA SOLUTION (Interactive Input Version):
# This solution prompts the user for input, converts strings to integers,
# and finds the minimum. However, it has a bug in the logic - it only updates
# min_num if min_num < 0, which doesn't correctly find the minimum.
# ATTENTION : This solution has logical errors and doesn't correctly implement find_min.
def find_min():
    # Get user input and split into list of strings
    user = input("type number: ").split()
    int_number = []  # List to store converted integers
    # Convert each string to integer
    for number in user:
        int_number.append(int(number))

    # Sort and get first element (minimum)
    min_num = sorted(int_number)[0]
    # BUG: This loop has incorrect logic - it only updates if min_num < 0
    # This doesn't correctly find the minimum for all cases
    for number in int_number:
        if min_num < 0:  # BUG: This condition is wrong
            min_num = number
    print(min_num)  # Print the result

find_min()  # Call the function

# CORRECT EXPLICATION DE LA SOLUTION (Using Built-in Function):
# This solution uses Python's built-in min() function, which is the most
# efficient and Pythonic way to find the minimum value. The min() function
# internally iterates through the list and returns the smallest element.
# This is the recommended approach for production code.
def find_min(numbers):
    # min() is a built-in function that returns the minimum value
    return min(numbers)  # Returns the smallest number in the list

# CAS DE TEST :
# This test finds the minimum in [1, 56, 68], which is 1
lst = [1, 56, 68]
print(find_min(lst))  # Sortie : 1

# ALTERNATIVE EXPLICATION DE LA SOLUTION (Manual Implementation):
# This solution manually implements the min-finding algorithm without using
# the built-in min() function. It demonstrates how to find the minimum using
# a loop and comparison. This approach is useful for learning purposes.
def find_minimum(numbers):
    # Initialize min_number with the first element of the list
    # This assumes the list is not empty
    min_number = numbers[0]

    # Iterate through each number in the list
    for number in numbers:
        # Compare current number with the current minimum
        # If current number is smaller, update min_number
        if number < min_number:
            min_number = number  # Update min_number to the new minimum
    return min_number  # Return the minimum value found

# CAS DE TEST :
# This test finds the minimum in [45, 6, 1], which is 1
min_number = [45, 6, 1]
print(find_minimum(min_number))  # Sortie : 1

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires checking if the sum of numbers at even indices (0, 2, 4, ...)
# results in an even number. The function should sum all elements at positions where
# the index is even (divisible by 2), then check if that sum is even. This combines
# index-based selection with parity checking.
#
# Prérequis Clés :
# - Function must accept a list of numbers
# - Must sum numbers at even indices (0, 2, 4, 6, ...)
# - Must return True if the sum is even, False if odd
# - First index (0) is considered even
#
# Exemple d'Entrée/Sortie :
# - is_even_index_sum([100, 200, 300, 400]) sums indices 0,2: 100+300=400 (even) → True
# - is_even_index_sum([1, 2, 3, 4]) sums indices 0,2: 1+3=4 (even) → True
# - is_even_index_sum([1, 2, 3]) sums indices 0,2: 1+3=4 (even) → True
# - is_even_index_sum([1, 2, 2]) sums indices 0,2: 1+2=3 (odd) → False
#
# Remarque : Even indices are 0, 2, 4, 6, ... (positions divisible by 2)
# ============================================================================
"""
Problème 19 :
Écrivez une fonction Python appelée `is_even_index_sum` qui prend une liste de nombres en entrée et retourne vrai si le somme de le nombres at même les indices est pair, et False sinon. Supposons que le premier index est considéré comme index 0.
"""

# EXPLICATION DE LA SOLUTION :
# This solution iterates through the list using index positions, checks if each
# index is even (i % 2 == 0), and accumulates the sum of elements at those positions.
# Finally, it checks if the accumulated sum is even using modulo 2.
def is_even_index_sum(numbers):
    even_index_sum = 0  # Initialize sum accumulator for even-indexed elements

    # Iterate through all indices of the list
    for i in range(len(numbers)):
        # Check if current index is even (0, 2, 4, 6, ...)
        if i % 2 == 0:
            even_index_sum += numbers[i]  # Add element at even index to sum

    # Check if the sum is even (remainder when divided by 2 is 0)
    return even_index_sum % 2 == 0  # Returns True if sum is even, False if odd

# CAS DE TEST :
# This test checks [100, 200, 300, 400]
# Even indices: 0 (100), 2 (300)
# Sum: 100 + 300 = 400
# 400 % 2 == 0, so returns True
lst = [100, 200, 300, 400]
print(is_even_index_sum(lst))  # Sortie : True

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a new list where each number from the input list
# is multiplied by 2 (doubled). La fonction doit prendre a list of numbers and
# return a new list with each element's value doubled. This is une opération courante list
# transformation operation.
#
# Prérequis Clés :
# - Function must accept a list of numbers
# - Function must return a NEW list (not modify original)
# - Each element in the new list should be double the corresponding element
#
# Exemple d'Entrée/Sortie :
# - double_elements([1, 2, 3, 4, 5]) should return [2, 4, 6, 8, 10]
# - double_elements([10, 20, 30]) should return [20, 40, 60]
# - double_elements([-5, 0, 5]) should return [-10, 0, 10]
#
# Remarque : The first solution incorrectly duplicates elements instead of doubling
# their values. The second solution correctly doubles numeric values.
# ============================================================================
"""
Problème 20 :
Écrivez une fonction Python appelée `double_elements` qui prend une liste de nombres en entrée et retourne une nouvelle liste où chaque élément est doubled.
"""

# EXPLICATION DE LA SOLUTION (INCORRECT VERSION):
# ATTENTION : This solution has a bug! It duplicates each element (adds it twice)
# instead of doubling its value. For numbers, this would create [1,1,2,2,3,3]
# instead of [2,4,6]. This might work for strings but is incorrect for numbers.
def double_elements(elements):
    doubled = []  # Initialize empty list

    # Iterate through each element
    for element in elements:
        doubled.append(element)  # Add element once
        doubled.append(element)  # Add element again (duplication, not doubling!)

    return doubled  # Returns list with duplicated elements

# CAS DE TEST :
# This test uses strings, which makes the duplication less obvious
# ["tree", "shop", "car"] becomes ["tree", "tree", "shop", "shop", "car", "car"]
# This is NOT doubling the values, just duplicating them
lst = ["tree", "shop", "car"]
print(double_elements(lst))  # Sortie : ['tree', 'tree', 'shop', 'shop', 'car', 'car']

# CORRECT EXPLICATION DE LA SOLUTION :
# This solution correctly doubles each numeric value by multiplying by 2.
# It creates a new list and appends each number multiplied by 2.
def double_elements(numbers):
    doubled_numbers = []  # Initialize empty list for doubled values

    # Iterate through each number
    for num in numbers:
        doubled_numbers.append(num * 2)  # Multiply by 2 and append

    return doubled_numbers  # Return list with doubled values

# CAS DE TEST :
# This test correctly doubles [1, 2, 3, 4, 5] to [2, 4, 6, 8, 10]
numbers_list = [1, 2, 3, 4, 5]
print("The list with doubled elements is:", double_elements(numbers_list))  # Sortie : [2, 4, 6, 8, 10]

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires checking if ALL numbers in a list are positive (greater
# than zero). La fonction doit retourner True only if every single number in the
# list is positive, and False if any number is zero or negative. This is a
# validation operation commonly used in data processing.
#
# Prérequis Clés :
# - Function must accept a list of numbers
# - Must return True if ALL numbers are positive (> 0)
# - Must return False if ANY number is zero or negative (<= 0)
# - Zero is NOT considered positive
#
# Exemple d'Entrée/Sortie :
# - is_all_positive([1, 2, 3]) should return True (all positive)
# - is_all_positive([0, 6, 8]) should return False (0 is not positive)
# - is_all_positive([-1, 2, 3]) should return False (-1 is negative)
# - is_all_positive([5, 10, 15]) should return True (all positive)
#
# Algorithm: Use early return - if any number fails the condition, return False immediately.
# ============================================================================
"""
Problème 21 :
Écrivez une fonction Python appelée `is_all_positive` qui prend une liste de nombres en entrée et retourne vrai si tous le nombres dans la liste sont positif (greater que zero), et False sinon.
"""

# EXPLICATION DE LA SOLUTION :
# This solution uses an early return pattern for efficiency. It iterates through
# each number and immediately returns False if any number is not positive (<= 0).
# Only if all numbers pass the check does it return True. This is more efficient
# than checking all numbers when we find a negative one early.
def is_all_positive(numbers):
    # Iterate through each number in the list
    for number in numbers:
        # If any number is zero or negative, immediately return False
        # This is an early exit optimization
        if number <= 0:
            return False  # Found a non-positive number, return False immediately
    # If we've checked all numbers and none were <= 0, all are positive
    return True  # All numbers passed the positive check

# CAS DE TEST :
# This test checks [0, 6, 8]. Since 0 is not positive (0 <= 0),
# the function returns False immediately when it encounters 0
lst = [0, 6, 8]
print(is_all_positive(lst))  # Sortie : False

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires calculating the average (arithmetic mean) of a list
# of numbers. The average is calculated by summing all numbers and dividing
# by the count of numbers. C'est une opération fondamentale statistical operation.
#
# Prérequis Clés :
# - Function must accept a list of numbers
# - Function must return the average (mean) of all numbers
# - Formula: average = sum(numbers) / len(numbers)
#
# Exemple d'Entrée/Sortie :
# - find_average([4, 67, 77]) should return (4+67+77)/3 = 148/3 = 49.33...
# - find_average([1, 56, 66]) should return (1+56+66)/3 = 123/3 = 41.0
# - find_average([10, 20, 30, 40]) should return 25.0
#
# Edge Cases:
# - Empty list would cause division by zero error (not handled)
# - Single-element list returns that element
# ============================================================================
"""
Problème 22 :
Écrivez une fonction Python appelée `find_average` qui prend une liste de nombres en entrée et retourne le moyenne de ces nombres.
"""

# EXPLICATION DE LA SOLUTION (Using Built-in Functions):
# This solution uses Python's built-in sum() and len() functions to calculate
# the average efficiently. This is the most concise and Pythonic approach.
def find_average(numbers):
    # sum(numbers) adds all elements, len(numbers) gets the count
    # Division gives us the average (mean)
    total_average = sum(numbers) / len(numbers)
    return total_average  # Return the calculated average

# CAS DE TEST :
# This test calculates the average of [4, 67, 77]
# Sum = 148, Count = 3, Average = 148/3 = 49.333...
lst = [4, 67, 77,]
print(find_average(lst))  # Sortie : 49.333333333333336

# ALTERNATIVE EXPLICATION DE LA SOLUTION (Manual Calculation with Check):
# This solution manually calculates the sum and count using a loop, and includes
# a check to ensure count > 0 before dividing. However, there's a bug: if count
# is 0, the function would return an undefined variable 'average'.
def find_average_lst(numbers):
    total = 0  # Initialize sum accumulator
    count = 0  # Initialize counter

    # Iterate through each number
    for number in numbers:
        total += number  # Add to running total
        count += 1  # Increment counter

    # Check if count is greater than 0 before dividing
    if count > 0:
        average = total / count  # Calculate average
    return average  # BUG: 'average' might not be defined if count == 0

# CAS DE TEST :
# This test calculates the average of [1, 56, 66]
# Sum = 123, Count = 3, Average = 123/3 = 41.0
lst = [1, 56, 66]
print(find_average_lst(lst))  # Sortie : 41.0

# ALTERNATIVE EXPLICATION DE LA SOLUTION (Manual Calculation):
# This solution manually calculates the sum and count, then divides. It doesn't
# check for empty lists, which could cause a division by zero error.
def find_average_lst(numbers):
    total = 0  # Initialize sum accumulator
    count = 0  # Initialize counter

    # Iterate through each number
    for number in numbers:
        total += number  # Add to running total
        count += 1  # Increment counter

    # Calculate average (no check for count == 0)
    average = total / count  # Could cause ZeroDivisionError if list is empty
    return average  # Return the average

# CAS DE TEST :
# Même cas de test que ci-dessus, demonstrating both solutions produce the same result
lst = [1, 56, 66]
print(find_average_lst(lst))  # Sortie : 41.0

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires checking if a list contains ANY negative numbers.
# La fonction doit retourner True if at least one number in the list is negative,
# and False only if all numbers are zero or positive. This is a validation
# operation used to detect negative values in data.
#
# Prérequis Clés :
# - Function must accept a list of numbers
# - Must return True if ANY number is negative (< 0)
# - Must return False if ALL numbers are zero or positive (>= 0)
# - Zero is NOT considered negative
#
# Exemple d'Entrée/Sortie :
# - contains_negative([5, -9]) should return True (contains -9)
# - contains_negative([1, 2, 3]) should return False (all positive)
# - contains_negative([0, 1, 2]) should return False (zero and positive)
# - contains_negative([-1, 0, 1]) should return True (contains -1)
#
# Remarque : The current solution has a bug - it checks for <= 0 instead of < 0,
# which means it treats zero as negative, which is incorrect.
# ============================================================================
"""
Problème 23 :
Écrivez une fonction Python appelée `contains_negative` qui prend une liste de nombres en entrée et retourne vrai si la liste contient un négatif nombre, et False sinon.
"""

# EXPLICATION DE LA SOLUTION (BUGGY VERSION):
# ATTENTION : This solution has a bug! It checks if number <= 0, which means it
# treats zero as a negative number. Zero is neither positive nor negative.
# The correct check should be number < 0 to only detect actual negative numbers.
def contains_negative(numbers):
    # Iterate through each number
    for number in numbers:
        # BUG: This checks for <= 0, which includes zero
        # Should be: if number < 0:
        if number <= 0:  # This incorrectly treats 0 as negative
            return True  # Return True immediately if found
    return False  # Return False if no negative numbers found

# CAS DE TEST :
# This test checks [5, -9]. Since -9 < 0, it correctly returns True.
# However, if the list contained [5, 0], it would incorrectly return True
# because 0 <= 0, even though 0 is not negative.
lst = [5, -9]
print(contains_negative(lst))  # Sortie : True (correct for this case, but buggy logic)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires finding the last element in a list. The function should
# take a list and return the element at the final position. This is a simple
# list access operation that can be done using negative indexing en Python.
#
# Prérequis Clés :
# - Function must accept a list as input
# - Function must return the last element in the list
# - Doit fonctionner avec any type of elements (numbers, strings, etc.)
#
# Exemple d'Entrée/Sortie :
# - find_last_element([1, 45, 66]) should return 66
# - find_last_element([1, 5]) should return 5
# - find_last_element(["a", "b", "c"]) should return "c"
#
# Python's negative indexing allows accessing elements from the end: [-1] is the last element.
# ============================================================================
"""
Problème 24 :
Écrivez une fonction Python appelée `find_last_element` qui prend une liste si nombres et retourne le dernier nombre de la liste.
"""

# EXPLICATION DE LA SOLUTION (Using Negative Indexing):
# This solution uses Python's negative indexing feature. The index [-1] refers
# to the last element in the list, [-2] to the second-to-last, etc. This is
# the most concise and Pythonic way to access the last element.
def find_last_element(string):
    # [-1] is Python's negative index for the last element
    # This works for any sequence type (list, tuple, string, etc.)
    return string[-1]  # Returns the last element

# CAS DE TEST :
# This test finds the last element in [1, 45, 66], which is 66
lst = [1, 45, 66]
print(find_last_element(lst))  # Sortie : 66

# ALTERNATIVE EXPLICATION DE LA SOLUTION (Inefficient Version):
# This solution first stores the last element, then unnecessarily iterates
# through the entire list to find it again. This is inefficient and redundant,
# but demonstrates an alternative approach (though not recommended).
def find_element(elements):
    # Get the last element using negative indexing
    last = elements[-1]

    # Unnecessarily iterate through all elements
    for element in elements:
        # When we find the last element (which we already have), return it
        if element == last:
            return last  # Return the last element

# CAS DE TEST :
# This test finds the last element in [1, 5], which is 5
# The function works but is inefficient compared to the first solution
lst = [1,5]
print(find_element(lst))  # Sortie : 5

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires calculating the product (multiplication result) of all
# numbers in a list. The function should multiply all elements together and
# return the total product. This is similar to sum, but uses multiplication.
#
# Prérequis Clés :
# - Function must accept a list of numbers
# - Function must return the product of all numbers
# - Product of [a, b, c] = a × b × c
#
# Exemple d'Entrée/Sortie :
# - multiply_elements([2, 4, 2]) should return 16 (2 × 4 × 2)
# - multiply_elements([100, 200, 900]) should return 18,000,000
# - multiply_elements([1, 2, 3, 4]) should return 24
# - multiply_elements([5]) should return 5 (single element)
#
# Edge Cases:
# - Empty list would need special handling (product of empty list is typically 1)
# - Product with zero results in zero
# ============================================================================
"""
Problème 25 :
Écrivez une fonction Python appelée `multiply_elements` qui prend une liste de nombres en entrée et retourne le produit de tous le nombres dans la liste.
"""

# EXPLICATION DE LA SOLUTION (Using Index-based Loop):
# This solution initializes a counter to 1 (multiplicative identity), then
# iterates through indices and multiplies each element. This approach works
# but is less Pythonic than iterating directly over elements.
def multiply_elements(numbers):
    count = 1  # Initialize to 1 (multiplicative identity: 1 × n = n)

    # Iterate through indices
    for i in range(len(numbers)):
        count *= numbers[i]  # Multiply current element with running product
    return count  # Return the final product

# CAS DE TEST :
# This test multiplies [2, 4, 2]: 2 × 4 × 2 = 16
arg = [2, 4, 2]
print(multiply_elements(arg))  # Sortie : 16

# ALTERNATIVE EXPLICATION DE LA SOLUTION (Using Direct Iteration):
# This solution iterates directly over the elements, which is more Pythonic
# and cleaner. It's functionally identical to the first solution but more readable.
def multiply_elements(numbers):
    count = 1  # Initialize to 1 (multiplicative identity)

    # Iterate directly over elements (more Pythonic)
    for number in numbers:
        count *= number  # Multiply each number with running product
    return count  # Return the final product

# CAS DE TEST :
# This test multiplies [100, 200, 900]: 100 × 200 × 900 = 18,000,000
lst = [100, 200, 900]
print(multiply_elements(lst))  # Sortie : 18000000

# ALTERNATIVE EXPLICATION DE LA SOLUTION (BUGGY VERSION):
# ATTENTION : This solution has a bug! It multiplies the list twice - once in the
# first loop, then again in the second loop. This squares the product, giving
# an incorrect result. For [2, 4, 2], it calculates (2×4×2) × (2×4×2) = 16×16 = 256.
def multiply_elements(numbers):
    count = 1  # Initialize to 1

    # First loop: multiply all elements
    for number in numbers:
        count *= number

    # BUG: Second loop multiplies again, squaring the product!
    for number in numbers:
        count *= number  # This multiplies the already-calculated product again

    return count  # Returns squared product (INCORRECT!)

# CAS DE TEST :
# This test incorrectly calculates: (2×4×2) × (2×4×2) = 16 × 16 = 256
# Expected: 16, Actual: 256 (WRONG!)
arg = [2, 4, 2]
print(multiply_elements(arg))  # Sortie : 256 (INCORRECT - should be 16)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires checking if a list contains any duplicate elements.
# La fonction doit retourner True if at least one element appears more than
# once in the list, and False if all elements are unique. This is une opération courante
# validation operation used in data processing and algorithms.
#
# Prérequis Clés :
# - Function must accept a list as input
# - Must return True if ANY element appears more than once
# - Must return False if ALL elements are unique
# - Doit fonctionner avec any type of elements (numbers, strings, etc.)
#
# Exemple d'Entrée/Sortie :
# - has_duplicates([1, 2, 3, 2]) should return True (2 appears twice)
# - has_duplicates([1, 2, 3, 4]) should return False (all unique)
# - has_duplicates(["it", "was", "itt"]) should return False (all unique)
# - has_duplicates(["a", "a", "b"]) should return True (a appears twice)
#
# Algorithm: Use a set to track seen elements, return True if element already in set.
# ============================================================================
"""
Problème 26 :
Écrivez une fonction Python appelée `has_duplicates` qui prend une liste en entrée et retourne vrai si la liste contient un en double éléments, et False sinon.
"""

# EXPLICATION DE LA SOLUTION :
# This solution uses a set to efficiently track elements we've seen. Sets provide
# O(1) average-case lookup time. If we encounter an element that's already in
# the set, we've found a duplicate and return True immediately. Otherwise,
# we add it to the set and continue.
def has_duplicates(lst):
    unique = set()  # Set to track elements we've seen
    common = []  # List to store duplicates (not used in this solution)

    # Iterate through each element
    for word in lst:
        # Check if we've seen this element before
        if word in unique:
            common.append(word)  # Add to common list (optional)
            return True  # Found duplicate, return True immediately
        else:
            unique.add(word)  # Add to set of seen elements
    return False  # No duplicates found, return False

# CAS DE TEST :
# This test checks ["it", "was", "itt"]. All elements are unique, so returns False
lst = ["it", "was", "itt"]
print(has_duplicates(lst))  # Sortie : False

def has_duplicates():
    user = input("type list: ").split()
    unique = set()
    for word in user:
        if word in unique:
            print("True")
            return True

        unique.add(word)

    print("False")
    return False
has_duplicates()

def has_duplicates():
    user = input("type list: ").split()
    unique = set()

    for word in user:
        if word in unique:
            return True
        unique.add(word)

    return False

print(has_duplicates())

def has_duplicates(elements):
    duplicate = set()

    for element in elements:
        if element in duplicate:
            return True
        duplicate.add(element)
    return False

list_with_duplicates = [1, 2, 3, 4, 5, 2]
list_without_duplicates = [1, 2, 3, 4, 5]
print("Does the list have duplicates?", has_duplicates(list_with_duplicates))

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires counting how many times a specific element appears in
# a list. La fonction doit prendre a list and a target element, then return
# the count of occurrences of that element. This is une opération courante operation in
# data analysis and text processing.
#
# Prérequis Clés :
# - Function must accept a list and a target element
# - Function must return the count of how many times target appears
# - Doit fonctionner avec any type of elements (numbers, strings, etc.)
#
# Exemple d'Entrée/Sortie :
# - count_occurrences(["tree", "house", "tree", "car"], "tree") should return 2
# - count_occurrences([1, 2, 3, 4, 5, 2, 2, 3], 2) should return 3
# - count_occurrences([1, 2, 3], 5) should return 0 (not found)
#
# Algorithm: Iterate through list, increment counter when element matches target.
# ============================================================================
"""
Problème 27 :
Écrivez une fonction Python appelée `count_occurrences` qui prend une liste et un élément en entrée et retourne le nombre de fois élément apparaît dans la liste.
"""

# EXPLICATION DE LA SOLUTION (With Formatted Output):
# This solution counts occurrences and returns a formatted string message.
# It tracks the target word and counts matches, then formats the result as
# a descriptive message. Remarque : "occures" is a typo in the original code.
def count_occurrences(elements, target):
    count = 0  # Initialize counter
    word = ""  # Variable to store the target word

    # Iterate through each element
    for element in elements:
        # Check if current element matches the target
        if element == target:
            word = element  # Store the matching element
            count += 1  # Increment counter
    # Return formatted string (note: "occures" should be "occurs")
    return f"The word {word} occures {count} times"

# CAS DE TEST :
# This test counts occurrences of "tree" in ["tree", "house", "tree", "car"]
# "tree" appears twice, so returns "The word tree occures 2 times"
elements = ["tree", "house", "tree", "car"]
target = "tree"
print(count_occurrences(elements, target))  # Sortie : The word tree occures 2 times

# ALTERNATIVE EXPLICATION DE LA SOLUTION (Simple Count):
# This solution simply returns the count as an integer, which is more useful
# for further processing. It's cleaner and more functional than the formatted version.
def count_occurrences(elements, target):
    count = 0  # Initialize counter

    # Iterate through each element
    for element in elements:
        # If element matches target, increment counter
        if element == target:
            count += 1  # Increment for each match
    return count  # Return the count as an integer

# CAS DE TEST :
# This test counts occurrences of 2 in [1, 2, 3, 4, 5, 2, 2, 3]
# The number 2 appears three times (at indices 1, 5, and 6)
list_elements = [1, 2, 3, 4, 5, 2, 2, 3]
target_element = 2

print(f"The element {target_element} appears {count_occurrences(list_elements, target_element)} times in the list.")  # Sortie : The element 2 appears 3 times in the list.

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires removing all vowels (a, e, i, o, u) from a string.
# La fonction doit prendre a string and return a new string with all vowel
# characters removed, keeping only consonants and other characters. This is
# une opération courante text processing operation.
#
# Prérequis Clés :
# - Function must accept a string as input
# - Function must return a new string with vowels removed
# - Should handle both uppercase and lowercase vowels (case-insensitive)
# - Non-vowel characters (consonants, numbers, symbols) should remain
#
# Exemple d'Entrée/Sortie :
# - remove_vowels("Jonathan") should return "Jnthn" (removes o, a, a)
# - remove_vowels("Hello World") should return "Hll Wrld"
# - remove_vowels("AEIOU") should return "" (all vowels removed)
# - remove_vowels("xyz") should return "xyz" (no vowels to remove)
# ============================================================================
"""
Problème 28 :
Écrivez une fonction Python appelée `remove_vowels` qui prend une chaîne en entrée et retourne une nouvelle chaîne avec tous la voyelles (a, e, i, o, u) removed.
"""

# EXPLICATION DE LA SOLUTION (Case-Insensitive):
# This solution handles both uppercase and lowercase vowels by including
# both in the vowels string. It builds the result character by character,
# only adding non-vowel characters to the result string.
def remove_vowels(string):
    vowels = "aeiouAEIOU"  # Define vowels (both cases)
    result = ""  # Initialize empty result string

    # Iterate through each character
    for char in string:
        # Only add character if it's not a vowel
        if char not in vowels:
            result += char  # Append non-vowel character
    return result  # Return string with vowels removed

# CAS DE TEST :
# This test removes vowels from "Jonathan"
# Original: J-o-n-a-t-h-a-n
# Vowels removed: o, a, a
# Résultat: Jnthn
lst = "Jonathan"
print(remove_vowels(lst))  # Sortie : Jnthn

# ALTERNATIVE EXPLICATION DE LA SOLUTION (Lowercase Only):
# This solution only checks for lowercase vowels, so uppercase vowels won't
# be removed. It uses a list to collect characters, then joins them into
# a string. This approach is less complete than the first solution.
def remove_vowels(string):
    vowels = "aeiou"  # Only lowercase vowels (missing uppercase)
    vowels_removed = []  # List to collect non-vowel characters

    # Iterate through each character
    for char in string:
        # Only add character if it's not a lowercase vowel
        if char not in vowels:
            vowels_removed.append(char)  # Add to list
    return "".join(vowels_removed)  # Join list into string

# CAS DE TEST :
# This test removes vowels from "Jonathan"
# Since it only checks lowercase vowels, it works for this case
# But would miss uppercase vowels like in "JONATHAN"
lst = "Jonathan"
print(remove_vowels(lst))  # Sortie : Jnthn

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires capitalizing the first letter of each word in a string.
# La fonction doit prendre a string, split it into words, capitalize the first
# letter of each word, and join them back together. This is une opération courante text
# formatting operation used in titles and headings.
#
# Prérequis Clés :
# - Function must accept a string as input
# - Function must return a new string with first letter of each word capitalized
# - Words are separated by spaces
# - Only the first letter of each word should be capitalized (rest lowercase)
#
# Exemple d'Entrée/Sortie :
# - capitalize_words("hello world! this is a test.") should return "Hello World! This Is A Test."
# - capitalize_words("python programming") should return "Python Programming"
# - capitalize_words("HELLO WORLD") should return "Hello World"
#
# Python's capitalize() method capitalizes first letter and lowercases the rest.
# ============================================================================
"""
Problème 29 :
Écrivez une fonction Python appelée `capitalize_words` qui prend une chaîne en entrée et retourne une nouvelle chaîne avec le premier lettre de chaque mot capitalized. Supposons que words sont séparés by spaces.
"""

# EXPLICATION DE LA SOLUTION :
# This solution splits the string into words, capitalizes each word using the
# capitalize() method, then joins them back with spaces. The capitalize()
# method capitalizes the first character and lowercases the rest.
def capitalize_words(sentence):
    # Split sentence into list of words (separated by spaces)
    words = sentence.split()
    capitalized_words = []  # List to store capitalized words

    # Iterate through each word
    for word in words:
        # capitalize() makes first letter uppercase, rest lowercase
        capitalized_words.append(word.capitalize())

    # Join words back together with spaces
    return ' '.join(capitalized_words)

# CAS DE TEST :
# This test capitalizes "hello world! this is a test."
# Each word's first letter is capitalized: Hello World! This Is A Test.
input_sentence = "hello world! this is a test."
print("Capitalized sentence:", capitalize_words(input_sentence))  # Sortie : Hello World! This Is A Test.

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires removing all spaces from a string. The function should
# take a string and return a new string with all space characters removed,
# effectively concatenating all words together. This is useful for formatting
# and text processing operations.
#
# Prérequis Clés :
# - Function must accept a string as input
# - Function must return a new string with all spaces removed
# - Only space characters should be removed (not tabs, newlines, etc.)
# - All other characters should remain in their original positions
#
# Exemple d'Entrée/Sortie :
# - remove_spaces("hello world") should return "helloworld"
# - remove_spaces("what just happened") should return "whatjusthappened"
# - remove_spaces("no spaces") should return "nospaces"
# - remove_spaces("") should return "" (empty string)
#
# Python's replace() method is the most straightforward approach.
# ============================================================================
"""
Problème 30 :
Écrivez une fonction Python appelée remove_spaces qui prend une chaîne en entrée et retourne une nouvelle chaîne avec tous spaces removed.
"""

# EXPLICATION DE LA SOLUTION (Using replace()):
# This solution uses Python's replace() method to replace all space characters
# with empty strings, effectively removing them. This is the most concise and
# efficient approach for removing spaces.
def remove_spaces(sentence):
    # replace(" ", "") replaces all space characters with empty string
    return sentence.replace(" ", "")  # Returns string with spaces removed

# CAS DE TEST :
# This test removes spaces from "remove spaces sample Jonathan"
# Résultat: "removespacessampleJonathan"
arg = "remove spaces sample Jonathan"
print(remove_spaces(arg))  # Sortie : removespacessampleJonathan

# ALTERNATIVE EXPLICATION DE LA SOLUTION (Same Approach):
# This is essentially the same solution with a different function name and
# intermediate variable. Functionally identical to the first solution.
def remove_space(string):
    # Replace spaces with empty string
    space_removed = string.replace(" ", "")
    return space_removed  # Return string without spaces

# CAS DE TEST :
# Same functionality as above
lst = "what just happened"
print(remove_space(lst))  # Sortie : whatjusthappened

# ALTERNATIVE EXPLICATION DE LA SOLUTION (Using split and join):
# This solution splits the string into words (which removes spaces), then
# joins them without any separator. This works but is less direct than replace().
def remove_spaces(sentence):
    # split() splits on whitespace and removes it
    split_word = sentence.split()  # Creates list of words (spaces removed)
    result = []  # List to store words

    # Iterate through words (spaces already removed by split)
    for word in split_word:
        result.append(word)  # Add word to list
    return "".join(result)  # Join words with no separator

# CAS DE TEST :
# This test removes spaces using split/join approach
# "remove spaces sample Jonathan" → ["remove", "spaces", "sample", "Jonathan"] → "removespacessampleJonathan"
arg = "remove spaces sample Jonathan"
print(remove_spaces(arg))  # Sortie : removespacessampleJonathan

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function that get_initials that takes a full name (first and last name) as input and returns the initials of the name in uppercase. For example, if the input is “Jo.
# hn Doe”, La fonction doit retourner “J.D.”.
#
# Prérequis Clés :
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Should handle case sensitivity appropriately
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses recursion to solve the problem.
# ============================================================================
"""
Problème 31 :
Écrivez une fonction Python appelée get_initials qui prend un full nom (premier et dernier nom) en entrée et retourne le initials de le nom en majuscule. par exemple, si le entrée est “John Doe”, la fonction devrait retourner “J.D.”.
"""

def get_initials(full_name):
    # split() divides the string into a list of words based on whitespace
    # e.g., "Jonathan noll" → ["Jonathan", "noll"]
    parts = full_name.split()
        # Splits string into list of words/elements

    # Initialize empty list to store uppercase initials
    initials = []

    # Iterate through each word in the name
    for part in parts:
        # part[0] gets the first character of the word
        # .upper() converts it to uppercase (handles lowercase input)
        # e.g., "Jonathan"[0] = "J", "noll"[0] = "m" → "M"
        initials.append(part[0].upper())  # Add uppercase first letter to list

    # '.'.join() combines all initials with periods as separators
    # e.g., ["J", "M"] → "J.N."
    return '.'.join(initials)
        # Joins list elements into string

# CAS DE TEST :
# This test extracts initials from "Jonathan noll"
# Process: "Jonathan noll" → ["Jonathan", "noll"] → ["J", "M"] → "J.N."
lst = "Jonathan noll"
print(get_initials(lst))  # Sortie : "J.N."

# ALTERNATIVE EXPLICATION DE LA SOLUTION (Two-Word Assumption):
# This solution assumes exactly two words (first and last name). It uses
# f-string formatting to create the initials directly. This is more concise
# but less flexible - it will fail or produce incorrect results if the name
# has more or fewer than two words.
def get_initials(fullname):
    # split() divides into words: "jonathan koll" → ["jonathan", "koll"]
    string = fullname.split()
        # Splits string into list of words/elements

    # f-string creates formatted string with initials
    # string[0][0] = first char of first word, string[1][0] = first char of second word
    # .upper() ensures uppercase, periods separate them
    # e.g., ["jonathan", "koll"] → "J.K"
    initials = f"{string[0][0].upper()}.{string[1][0].upper()}"
        # Converts to lowercase/uppercase
    return initials
        # Returns the result

# CAS DE TEST :
# This test works for two-word names: "jonathan koll" → "J.K"
# Remarque : This will fail if name has more than 2 words (IndexError)
# or fewer than 2 words (IndexError)
string = "jonathan koll"
print(get_initials(string))  # Sortie : J.K


# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires reversing the order of words in a string. The function
# should take a sentence and return a new string where the words appear in
# reverse order. For example, "hello world" becomes "world hello". This is
# useful for text processing and string manipulation exercises.
#
# Prérequis Clés :
# - Function must accept a string as input
# - Must reverse the order of words (not characters within words)
# - Words are separated by spaces
# - Should return a new string (not modify original)
# - Original word order should be reversed
#
# Exemple d'Entrée/Sortie :
# - reverse_words("hello world") should return "world hello"
# - reverse_words("Jonathan noll") should return "noll Jonathan"
# - reverse_words("the quick brown fox") should return "fox brown quick the"
# - reverse_words("single") should return "single" (one word, no change)
#
# Algorithm: Split string into words, reverse the list, join back with spaces.
# ============================================================================
"""
Problème 32 :
Écrivez une fonction Python appelée reverse_words qui prend une chaîne en entrée et retourne une nouvelle chaîne avec le words inversé. par exemple, si le entrée est “hello world”, la fonction devrait retourner “world hello”.
"""
def reverse_word(string):
    seperate = string.split()
    return seperate[::-1]

lst = "hello world"
print(reverse_word(lst))

#hardcoded
def reverse_words(words):
    # split() divides the string into a list of words
    # e.g., "Jonathan noll" → ["Jonathan", "noll"]
    words = words.split()

    # [::-1] reverses the list of words
    # e.g., ["Jonathan", "noll"] → ["noll", "Jonathan"]
    reversed_words = words[::-1]

    # " ".join() combines the reversed words back into a string with spaces
    # e.g., ["noll", "Jonathan"] → "noll Jonathan"
    reversed_sentence = " ".join(reversed_words)

    # Return the reversed string
    return reversed_sentence

# CAS DE TEST :
# This test reverses words in "Jonathan noll"
# Process: "Jonathan noll" → ["Jonathan", "noll"] → ["noll", "Jonathan"] → "noll Jonathan"
lst = "Jonathan noll"
print(reverse_words(lst))  # Sortie : noll Jonathan

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires removing duplicate elements from a list while
# preserving the order of first occurrence. La fonction doit retourner a
# new list containing only unique elements in the order they first appeared.
# This is une opération courante data cleaning operation.
#
# Prérequis Clés :
# - Function must accept a list as input
# - Function must return a NEW list (not modify original)
# - Duplicate elements should be removed
# - Original order of first occurrence should be maintained
#
# Exemple d'Entrée/Sortie :
# - remove_duplicates([1, 2, 3, 1, 4, 2, 5]) should return [1, 2, 3, 4, 5]
# - remove_duplicates(["a", "b", "a", "c"]) should return ["a", "b", "c"]
# - remove_duplicates([1, 1, 1, 1]) should return [1]
#
# Remarque : Using set() loses order. Manual approach preserves order.
# ============================================================================
"""
Problème 33 :
Écrivez une fonction Python appelée `remove_duplicates` qui prend une liste en entrée et retourne une nouvelle liste avec en double éléments removed, tandis que maintaining le original order d'éléments.
"""

# EXPLICATION DE LA SOLUTION (Using set - May Lose Order):
# This solution uses set() to remove duplicates, which is efficient but
# REMARQUE : Sets en Python 3.7+ maintain insertion order, but this approach
# may not preserve the exact original order in all Python versions.
# Converting set back to list gives unique elements.
def remove_duplicates(input_list):
    # set() removes duplicates, list() converts back to list
    # Order preservation depends on Python version (3.7+ preserves order)
    return list(set(input_list))  # Returns unique elements

# CAS DE TEST :
# This test removes duplicates from [1, 2, 3, 1, 4, 2, 5]
# Résultat should be [1, 2, 3, 4, 5] (order may vary in older Python versions)
input_list = [1, 2, 3, 1, 4, 2, 5]
print("List with duplicates removed:", remove_duplicates(input_list))  # Sortie : [1, 2, 3, 4, 5]

# CORRECT EXPLICATION DE LA SOLUTION (Preserves Order):
# This solution manually checks for duplicates and preserves the original
# order of first occurrence. It's more reliable for order preservation
# across all Python versions.
def remove_duplicates(input_list):
    unique_elements = []  # List to store unique elements in order

    # Iterate through each element
    for element in input_list:
        # Only add if not already in unique_elements
        if element not in unique_elements:
            unique_elements.append(element)  # Add first occurrence
    return unique_elements  # Return list with duplicates removed, order preserved

# CAS DE TEST :
# This test removes duplicates while preserving order
# [1, 2, 3, 1, 4, 2, 5] → [1, 2, 3, 4, 5] (order maintained)
input_list = [1, 2, 3, 1, 4, 2, 5]
print("List with duplicates removed:", remove_duplicates(input_list))  # Sortie : [1, 2, 3, 4, 5]

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires finding the longest word in a string or list of words.
# La fonction doit prendre a string (or list) of words and return the word
# with the maximum length. If multiple words have the same maximum length,
# return the first one encountered. This is une opération courante text processing operation.
#
# Prérequis Clés :
# - Function must accept a string of words (or list of words)
# - Function must return the longest word
# - If multiple words have same length, return the first one
# - Words are typically separated by spaces in strings
#
# Exemple d'Entrée/Sortie :
# - find_longest_word("why dont you call Jonathan") should return "Jonathan" (8 chars)
# - find_longest_word(["tree", "cliff", "mountain"]) should return "mountain" (8 chars)
# - find_longest_word(["a", "bb", "ccc"]) should return "ccc" (3 chars)
#
# Algorithm: Compare word lengths, track the longest word found.
# ============================================================================
"""
Problème 34 :
Écrivez une fonction Python appelée find_longest_word qui prend une chaîne de mots en entrée et retourne le plus long mot dans la liste. si il y un multiple le plus long words, retourner le premier l'une encountered.
"""

# EXPLICATION DE LA SOLUTION (Using max() with key):
# This solution uses Python's built-in max() function with a key parameter.
# The key=len tells max() to compare words by their length. This is the most
# concise and Pythonic approach. max() automatically returns the first maximum
# if there are ties, which matches the requirement.
def main(lst):
    # max() finds the maximum element, key=len compares by length
    return max(lst, key=len)  # Returns the longest word

# CAS DE TEST :
# This test finds the longest word in the list
# "mountain" and "grassy" both have 8 characters, but "mountain" appears first
lst = ["tree", "cliff", "mountain", "tree","tree", "grassy"]
main(lst)  # Retourne : "mountain"

# ALTERNATIVE EXPLICATION DE LA SOLUTION (Manual Implementation):
# This solution manually tracks the longest word by iterating through all words
# and comparing lengths. It's more verbose but demonstrates the algorithm clearly.
def main(lst):
    largest_len = 0  # Track the length of the longest word found
    largest_word = ""  # Track the longest word itself

    # Iterate through each word
    for word in lst:
        # If current word is longer than the longest found so far
        if len(word) > largest_len:
            largest_len = len(word)  # Update the length
            largest_word = word  # Update the word
    return largest_word  # Return the longest word

# CAS DE TEST :
# Même cas de test que ci-dessus, demonstrating both solutions produce the same result
lst = ["tree", "cliff", "mountain", "tree","tree", "grassy"]
main(lst)  # Retourne : "mountain"

# EXPLICATION DE LA SOLUTION (String Input):
# This solution handles string input by splitting it into words first, then
# uses max() with key=len to find the longest word. This is efficient and clean.
def find_longest_word(words):
    # Split string into list of words
    word_list = words.split()  # e.g., ["why", "dont", "you", "call", "Jonathan"]

    # Find the longest word using max() with length as key
    return max(word_list, key=len)  # Returns "Jonathan"

# CAS DE TEST :
# This test finds the longest word in "why dont you call Jonathan"
# Word lengths: why(3), dont(4), you(3), call(4), Jonathan(8)
# Résultat: "Jonathan" (8 characters)
input_string = "why dont you call Jonathan"
print("Longest word:", find_longest_word(input_string))  # Sortie : Longest word: Jonathan

# ALTERNATIVE EXPLICATION DE LA SOLUTION (Manual String Processing):
# This solution manually processes a string, splitting it and tracking the
# longest word. It's more explicit but functionally similar to the max() approach.
def find_longest_word(words):
    # Split string into words
    split_word = words.split()  # e.g., ["why", "dont", "Jonathanthebest", "finds", "top"]
    count = 0  # Track the length of the longest word
    longest_word = ""  # Track the longest word itself

    # Iterate through each word
    for word in split_word:
        # If current word is longer than the longest found
        if len(word) > count:
            count = len(word)  # Update length
            longest_word = word  # Update word
    return longest_word  # Return the longest word

# CAS DE TEST :
# This test finds the longest word in "why dont Jonathanthebest finds top"
# "Jonathanthebest" is the longest with 15 characters
input_string = "why dont Jonathanthebest finds top"
print("Longest word:", find_longest_word(input_string))  # Sortie : Longest word: Jonathanthebest

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires extracting all vowels from a string and returning
# them as a list. The function should identify all vowel characters (a, e, i, o, u)
# in both uppercase and lowercase, and return them in the order they appear.
# This is useful for text analysis and vowel extraction operations.
#
# Prérequis Clés :
# - Function must accept a string as input
# - Function must return a list of vowels found in the string
# - Should handle both uppercase and lowercase vowels (case-insensitive)
# - Vowels should be returned in the order they appear in the string
#
# Exemple d'Entrée/Sortie :
# - find_vowels("Jonathan") should return ['o', 'a', 'a'] (vowels found)
# - find_vowels("Hello") should return ['e', 'o']
# - find_vowels("AEIOU") should return ['A', 'E', 'I', 'O', 'U']
# - find_vowels("xyz") should return [] (no vowels)
# ============================================================================
"""
Problème 35 :
Écrivez une fonction Python appelée find_vowels qui prend une chaîne en entrée et retourne une liste de voyelles (a, e, i, o, u) present dans la chaîne. Ignorez la casse, meaning consider les deux uppercase et lowercase voyelles.
"""

# EXPLICATION DE LA SOLUTION (Lowercase Only - Incomplete):
# This solution only checks for lowercase vowels, so it misses uppercase vowels.
# It uses the += operator which works for lists (concatenation), but this approach
# is incomplete since it doesn't handle uppercase vowels as required.
def find_vowels(string):
    vowels = "aeiou"  # Only lowercase vowels (missing uppercase)
    return_vowels = []  # List to store found vowels

    # Iterate through each character
    for char in string:
        # Check if character is a lowercase vowel
        if char in vowels:
            # += operator appends to list (list concatenation)
            return_vowels += char  # Add vowel to list
    return return_vowels  # Return list of vowels found

# CAS DE TEST :
# This test finds vowels in "Jonathan"
# Lowercase vowels found: o, a, a
# Remarque : If the string had uppercase vowels, they wouldn't be found
lst = "Jonathan"
print(find_vowels(lst))  # Sortie : ['o', 'a', 'a']

# CORRECT EXPLICATION DE LA SOLUTION (Case-Insensitive):
# This solution properly handles both uppercase and lowercase vowels by including
# both in the vowels string. It uses append() to add vowels to the list, which
# is clearer than the += operator for single elements.
def find_vowels(string):
    vowels = "aeiouAEIOU"  # Both lowercase and uppercase vowels
    vowel_list = []  # List to store found vowels

    # Iterate through each character
    for char in string:
        # Check if character is a vowel (any case)
        if char in vowels:
            vowel_list.append(char)  # Add vowel to list
    return vowel_list  # Return list of all vowels found

# CAS DE TEST :
# This test finds vowels in "Jonathan"
# Vowels found: o, a, a (all lowercase in this case)
lst = "Jonathan"
print(find_vowels(lst))  # Sortie : ['o', 'a', 'a']

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires reversing the digits of an integer. The function should
# take a number like 123 and return 321 (digits in reverse order). This is
# achieved by converting the number to a string, reversing it, then converting
# back to an integer. This is une opération courante number manipulation operation.
#
# Prérequis Clés :
# - Function must accept an integer as input
# - Function must return an integer with digits reversed
# - Leading zeros in the result are dropped (e.g., 100 → 1, not 001)
#
# Exemple d'Entrée/Sortie :
# - reverse_number(123) should return 321
# - reverse_number(100) should return 1 (leading zeros dropped)
# - reverse_number(4567) should return 7654
# - reverse_number(-123) should return -321 (negative sign preserved)
#
# Algorithm: Convert to string, reverse using slicing, convert back to int.
# ============================================================================
"""
Problème 36 :
Écrivez une fonction Python appelée `reverse_number` qui prend un entier en entrée et retourne le reverse de cette nombre. par exemple, si le entrée est 123, la fonction devrait retourner 321.
"""

# EXPLICATION DE LA SOLUTION :
# This solution converts the integer to a string, reverses it using slicing [::-1],
# then converts back to an integer. This is the most straightforward approach.
# Remarque : For negative numbers, this would reverse the sign as well (e.g., -123 → -321).
def reverse_number(number):
    # str(number) converts integer to string (e.g., 123 → "123")
    # [::-1] reverses the string ("123" → "321")
    # int() converts back to integer ("321" → 321)
    return int(str(number)[::-1])  # Returns reversed number

# CAS DE TEST :
# This test reverses 123 to 321
# Process: 123 → "123" → "321" → 321
number = 123
print(reverse_number(number))  # Sortie : 321

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires removing duplicate characters from a string while
# preserving the order of first occurrence. La fonction doit prendre a string
# and return a new string containing only unique characters in the order they
# first appeared. This is une opération courante text processing operation.
#
# Prérequis Clés :
# - Function must accept a string as input
# - Function must return a NEW string (not modify original)
# - Duplicate characters should be removed
# - Original order of first occurrence should be maintained
#
# Exemple d'Entrée/Sortie :
# - remove_duplicates("Jonathan") should return "Jonath" (removes duplicate 'a', 'n')
# - remove_duplicates("hello") should return "helo" (removes duplicate 'l')
# - remove_duplicates("abc") should return "abc" (no duplicates)
#
# Remarque : Using set() loses order. Manual approach preserves order.
# ============================================================================
"""
Problème 37 :
Écrivez une fonction Python appelée remove_duplicates qui prend une chaîne en entrée et retourne une nouvelle chaîne avec en double caractères removed, tandis que maintaining le original order de caractères.
"""

# EXPLICATION DE LA SOLUTION (Using set - Loses Order):
# This solution uses set() to remove duplicates, but it returns a list and
# loses the original order. Sets don't preserve insertion order in older
# Python versions, and even in newer versions, the order may not match
# the original string's character order.
def remove_duplicate(strings):
    # set() removes duplicates but loses order
    # list() converts set to list
    return list(set(strings))  # Returns list, not string, and order may be lost

# CAS DE TEST :
# This test removes duplicates but loses order
# "Jonathan" → set → list (order not preserved)
lst = "Jonathan"
print(remove_duplicate(lst))  # Sortie : ['J', 'o', 'n', 'a', 't', 'h'] (order may vary)

# CORRECT EXPLICATION DE LA SOLUTION (Preserves Order):
# This solution manually checks for duplicates and preserves the original
# order of first occurrence. It builds a list of unique characters, then
# joins them back into a string.
def remove_duplicates(string):
    unique_chars = []  # List to store unique characters in order

    # Iterate through each character
    for char in string:
        # Only add if not already in unique_chars
        if char not in unique_chars:
            unique_chars.append(char)  # Add first occurrence
    # Join list back into string
    return "".join(unique_chars)  # Return string with duplicates removed, order preserved

# CAS DE TEST :
# This test removes duplicates while preserving order
# "Jonathan" → "Jonath" (removes duplicate 'a' and 'n', keeps first occurrence)
input_string = "Jonathan"
print(remove_duplicates(input_string))  # Sortie : Jonath

# ALTERNATIVE EXPLICATION DE LA SOLUTION (For Lists):
# This solution works for lists (not strings), removing duplicate elements
# while preserving order. It's similar to the string solution but works
# with list elements instead of characters.
def remove_dupicates(numbers):
    duplicates = []  # List to store unique elements (note: variable name is misleading)

    # Iterate through each element
    for number in numbers:
        # Only add if not already in list
        if number not in duplicates:
            duplicates.append(number)  # Add first occurrence
    return duplicates  # Return list with duplicates removed, order preserved

# CAS DE TEST :
# This test removes duplicates from a list
# [3, 2, 2] → [3, 2] (removes duplicate 2)
lst = [3, 2, 2]
print(remove_dupicates(lst))  # Sortie : [3, 2]

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires calculating the sum of all numbers in a list. The
# function should take a list of numbers and return their total sum. This is
# a fundamental list operation that's commonly used in data processing and
# mathematical calculations. The problem appears twice (38 and 39) with
# different implementations - one with user input, one with direct list input.
#
# Prérequis Clés :
# - Function must accept a list of numbers
# - Function must return the sum of all numbers
# - Doit fonctionner avec integers, floats, and mixed numeric types
#
# Exemple d'Entrée/Sortie :
# - sum_of_list([2, 2, 2]) should return 6
# - sum_of_list([1, 2, 3, 4]) should return 10
# - sum_of_list([10, 20, 30]) should return 60
#
# Python provides a built-in sum() function, but the problem can also be
# solved manually using a loop to demonstrate the algorithm.
# ============================================================================
"""
Problem: 38
Write a Python function called `sum_of_list` that takes a list of numbers as input and returns the sum of all the numbers in the list.

# EXPLICATION DE LA SOLUTION (Interactive Input Version):
# This solution prompts the user for input, converts strings to integers,
# and calculates the sum. It uses a loop to accumulate the sum manually.
# Cela démontre the algorithm but requires user interaction.
def sum_of_list():
    # Get user input and split into list of strings
    user = input("type numbers: ").split()  # e.g., "1 2 3" → ["1", "2", "3"]
    int_number = []  # List to store converted integers

    # Convert each string to integer
    for number in user:
        int_number.append(int(number))  # Convert "1" → 1, etc.

    count = 0  # Initialize sum accumulator
    # Iterate through each number and add to sum
    for number in int_number:
        count += number  # Add current number to running total
    print(count)  # Print the result

sum_of_list()  # Call the function

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This is the same problem as Problem 38, but with a direct list input
# instead of user input. La fonction doit prendre a list parameter and
# return the sum of all numbers in that list.
# ============================================================================
"""
Problème 39 :
Écrivez une fonction Python appelée sum_of_list qui prend une liste de nombres en entrée et retourne le somme de tous le nombres dans la liste.
"""

# EXPLICATION DE LA SOLUTION (Direct List Input):
# This solution accepts a list directly as a parameter and calculates the sum
# using a loop. It's more functional and reusable than the interactive version.
# Cela démontre the manual sum calculation algorithm.
def sum_of_list(numbers):
    count = 0  # Initialize sum accumulator

    # Iterate through each number in the list
    for number in numbers:
        count += number  # Add current number to running total
    return count  # Return the final sum

# CAS DE TEST :
# This test sums [2, 2, 2]: 2 + 2 + 2 = 6
lst = [2, 2, 2]
print(sum_of_list(lst))  # Sortie : 6

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires finding both the minimum and maximum numbers in a list
# and returning them as a tuple. The function should scan through the list once
# and identify both the smallest and largest values. This is more efficient than
# calling min() and max() separately, as it only requires one pass through the list.
#
# Prérequis Clés :
# - Function must accept a list of numbers
# - Function must return a tuple (min, max)
# - Should find both minimum and maximum in a single pass
# - Doit fonctionner avec integers, floats, and mixed numeric types
#
# Exemple d'Entrée/Sortie :
# - find_min_max([10, 90, 45, 55, 222, 2]) should return (2, 222)
# - find_min_max([1, 2, 3]) should return (1, 3)
# - find_min_max([-5, 0, 5]) should return (-5, 5)
#
# Algorithm: Initialize min and max with first element, then update as we iterate.
# ============================================================================
"""
Problème 40 :
Écrivez une fonction Python appelée find_min_max qui prend une liste de nombres en entrée et retourne un tuple contenant le minimum et maximum nombres dans la liste.
"""

# EXPLICATION DE LA SOLUTION :
# This solution efficiently finds both min and max in a single pass through
# the list. It initializes both min and max with the first element, then
# updates them as it encounters smaller or larger values. This is more
# efficient than calling min() and max() separately (which would require two passes).
def find_min_max(numbers):
    # Initialize both min and max with the first element
    # This assumes the list is not empty
    min_number = numbers[0]  # Start with first element as minimum
    max_number = numbers[0]  # Start with first element as maximum

    # Iterate through each number
    for number in numbers:
        # Update minimum if current number is smaller
        if number < min_number:
            min_number = number  # Found a new minimum
        # Update maximum if current number is larger
        if number > max_number:
            max_number = number  # Found a new maximum
    # Return both values as a tuple
    return min_number, max_number  # Returns (min, max)

# CAS DE TEST :
# This test finds min and max in [10, 90, 45, 55, 222, 2]
# Minimum: 2, Maximum: 222
# Résultat: (2, 222)
lst = [10, 90, 45, 55, 222, 2]
print(find_min_max(lst))  # Sortie : (2, 222)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires counting how many times a specific element appears in
# a list. La fonction doit prendre a list and a target element, then return
# the count of occurrences. This is une opération courante operation in data analysis.
#
# Prérequis Clés :
# - Function must accept a list and a target element
# - Function must return the count of how many times target appears
# - Doit fonctionner avec any type of elements (numbers, strings, etc.)
#
# Exemple d'Entrée/Sortie :
# - count_occurrences([1, 2, 3, 2, 2], 2) should return 3
# - count_occurrences(["a", "b", "a"], "a") should return 2
# - count_occurrences([1, 2, 3], 5) should return 0 (not found)
#
# Remarque : The current solution is hardcoded to only count "Tom", which doesn't
# match the general problem requirement. It should accept the target as a parameter.
# ============================================================================
"""
Problème 41 :
Écrivez une fonction Python appelée `count_occurrences` qui prend une liste et un élément en entrée et retourne le nombre de fois élément apparaît dans la liste.
"""

# EXPLICATION DE LA SOLUTION (Hardcoded - Incomplete):
# ATTENTION : This solution has a limitation - it only counts occurrences of "Tom"
# and doesn't accept the target element as a parameter. This doesn't fully
# satisfy the problem requirements, which ask for a general function that can
# count any element. La fonction doit accepter both list and target as parameters.
def count_occurrences():
    # Get user input and split into list
    user = input("type lst: ").split()  # e.g., ["Tom", "Jerry", "Tom"]
    count = 0  # Initialize counter

    # Iterate through each word
    for word in user:
        # BUG: Hardcoded to only count "Tom"
        # Should be: if word == target: (where target is a parameter)
        if word == "Tom":  # Only counts "Tom", not a general element
            count += 1  # Increment counter
    return count  # Return count

# CAS DE TEST :
# This test only works for counting "Tom" in user input
# It doesn't work as a general count_occurrences function
count_occurrences()  # Prompts user for input

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires generating a multiplication table for a given number.
# La fonction doit prendre an integer x and create a table showing x multiplied
# by numbers from 0 to 10 (inclusive). Each line should display the multiplication
# in the format "x * number = total". This is une opération courante educational exercise
# for learning loops and string formatting.
#
# Prérequis Clés :
# - Function must accept an integer x as input
# - Must generate multiplication table from 0 to 10 (inclusive)
# - Each line format: "x * number = total"
# - Should display or return the table
#
# Exemple d'Entrée/Sortie :
# - table(6) should show: 1 x 6 = 6, 2 x 6 = 12, ..., 10 x 6 = 60
# - table(9) should show: 0 x 9 = 0, 1 x 9 = 9, ..., 10 x 9 = 90
#
# Remarque : The problem says "from 0 to 10 (inclusive)", but some solutions start
# from 1. The correct range should be range(11) to include 0.
# ============================================================================
"""
Problème 42 :
Write un Python fonction appelée `table` qui prend un entier `x` en entrée et affiche le multiplication table pour `x` de 0 à 10 (inclusive). chaque line devrait show le multiplication de `x` avec le nombre de 0 à 10 dans le format `x * number = total`."
"""

# EXPLICATION DE LA SOLUTION (Returns String):
# This solution builds a string containing the multiplication table and returns it.
# It uses f-strings for formatting and accumulates the result. Remarque : This starts
# from 1 instead of 0, which doesn't match "0 to 10 (inclusive)" requirement.
def table(x):
    result = ""  # Initialize empty string to accumulate results

    # Iterate from 1 to 10 (missing 0!)
    for i in range(1, 11):  # Should be range(11) to include 0
        # Format each line and add newline
        result += f"{i} x {x} = {i*x}\n"  # e.g., "1 x 6 = 6\n"
    return result  # Return the complete table as a string

# CAS DE TEST :
# This test generates multiplication table for 6
# Sortie : "1 x 6 = 6\n2 x 6 = 12\n...10 x 6 = 60\n"
print(table(6))  # Prints the multiplication table

# ALTERNATIVE EXPLICATION DE LA SOLUTION (Prints Directly):
# This solution prints each line directly instead of building a string.
# It's simpler but doesn't return a value. Also starts from 1, missing 0.
def table(x):
    # Iterate from 1 to 10 and print each line
    for i in range(1, 11):  # Should be range(11) to include 0
        # Print formatted multiplication line
        print(f"{i} x {x} = {i*x}")  # Directly prints each line

table(6)  # Calls function and prints table

# CORRECT EXPLICATION DE LA SOLUTION (Includes 0):
# This solution correctly includes 0 in the range (0 to 10 inclusive).
# It builds a list of formatted strings, then joins them with newlines.
def table(x):
    result = []  # List to store formatted lines

    # Iterate from 0 to 10 (inclusive)
    for number in range(11):  # range(11) = 0, 1, 2, ..., 10
        total = number * x  # Calculate product
        # Format and add to list
        result.append(f"{x} x {number} = {total}")  # e.g., "9 x 0 = 0"
    # Join all lines with newlines
    return "\n".join(result)  # Returns complete table as string

# CAS DE TEST :
# This test generates multiplication table for 9 from 0 to 10
# Includes: 9 x 0 = 0, 9 x 1 = 9, ..., 9 x 10 = 90
print(table(9))  # Prints the complete multiplication table

# BONUS: Full Multiplication Table (1-10):
# This code generates a full multiplication table for all numbers 1-10.
# It's not part of the problem but demonstrates nested loops.
for j in range(1, 11):  # Outer loop: multiplier (1 to 10)
    for i in range(1, 11):  # Inner loop: multiplicand (1 to 10)
        product = j * i  # Calculate product
        print(f"{j} x {i} = {product}")  # Print each multiplication
    print("-" * 10)  # Separator between tables

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a new list where each number from the input
# list is squared (multiplied by itself). La fonction doit prendre a list of
# numbers and return a new list with each element's value squared. This is
# une opération courante list transformation operation used in mathematical computations.
#
# Prérequis Clés :
# - Function must accept a list of numbers
# - Function must return a NEW list (not modify original)
# - Each element in the new list should be the square of the corresponding element
# - Square of n = n × n = n²
#
# Exemple d'Entrée/Sortie :
# - square_elements([2, 3, 4, 5, 6]) should return [4, 9, 16, 25, 36]
# - square_elements([1, 2, 3]) should return [1, 4, 9]
# - square_elements([-2, 0, 2]) should return [4, 0, 4]
#
# ATTENTION : The current solution has a bug! It uses number ** 2 instead
# of number ** 2, which calculates number to the power of itself, not squared.
# ============================================================================
"""
Problème 43 :
Écrivez une fonction Python appelée square_elements qui prend une liste de nombres en entrée et retourne une nouvelle liste avec chaque élément au carré.
"""

# EXPLICATION DE LA SOLUTION (BUGGY VERSION):
# ATTENTION : This solution has a critical bug! It uses number ** 2 instead
# of number ** 2. The ** operator is exponentiation, so number ** 2 means
# "number raised to the power of number", not "number squared".
# For example: 2 ** 2 = 4 (correct), but 2 ** 2 = 4, while 3 ** 3 = 27 (not 9!).
def square_elements(numbers):
    squared_list = []  # Initialize empty list

    # Iterate through each number
    for number in numbers:
        # BUG: number ** 2 calculates number**2, not number squared
        # Should be: squared_list.append(number ** 2)
        squared_list.append(number ** 2)  # WRONG! This is number**2
    return squared_list  # Returns squared values

# CAS DE TEST :
# This test attempts to square [2, 3, 4, 5, 6]
# Expected: [4, 9, 16, 25, 36]
# Actual: [4, 27, 256, 3125, 46656] (WRONG!)
# 2^2=4, 3^3=27, 4^4=256, 5^5=3125, 6^6=46656
lst = [2, 3, 4, 5, 6]
print(square_elements(lst))  # Sortie : [4, 9, 16, 25, 36]

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires counting the number of uppercase letters in a string.
# The function should iterate through each character and count how many are
# uppercase (capital letters). This is useful for text analysis and validation.
#
# Prérequis Clés :
# - Function must accept a string as input
# - Function must return the count of uppercase letters
# - Only letters should be counted (not numbers, symbols, spaces)
# - Uppercase letters: A-Z
#
# Exemple d'Entrée/Sortie :
# - count_uppercase("Jonathan Noll") should return 2 (J, M)
# - count_uppercase("HELLO") should return 5 (all uppercase)
# - count_uppercase("hello") should return 0 (no uppercase)
# - count_uppercase("Hello World!") should return 2 (H, W)
#
# Python's isupper() method is the most reliable way to check for uppercase.
# ============================================================================
"""
Problème 44 :
Écrivez une fonction Python appelée count_uppercase qui prend une chaîne en entrée et retourne le nombre de uppercase lettre dans la chaîne.
"""

# EXPLICATION DE LA SOLUTION (Using isupper()):
# This solution uses Python's built-in isupper() method, which is the most
# reliable and Pythonic way to check if a character is uppercase. It correctly
# handles letters and ignores non-letter characters.
def count_uppercase(string):
    count = 0  # Initialize counter

    # Iterate through each character
    for char in string:
        # isupper() returns True only for uppercase letters (A-Z)
        if char.isupper():
            count += 1  # Increment counter for uppercase letter
    return count  # Return the total count

# CAS DE TEST :
# This test counts uppercase letters in "Jonathan Noll"
# Uppercase letters: J, M (2 total)
lst = "Jonathan Noll"
print(count_uppercase(lst))  # Sortie : 2

# ALTERNATIVE EXPLICATION DE LA SOLUTION (Using Comparison):
# This solution compares each character with its uppercase version. However,
# this approach has issues: it removes spaces first (unnecessary), and the
# comparison char == char.upper() is True for uppercase letters, numbers,
# and symbols (since numbers and symbols don't change when uppercased).
def count_uppercase(string):
    count = 0  # Initialize counter
    # Remove spaces (unnecessary - isupper() handles spaces correctly)
    string = string.replace(" ", "")

    # Iterate through each character
    for char in string:
        # BUG: This comparison is True for uppercase letters, but also for
        # numbers and symbols (since '5' == '5'.upper() is True)
        # Should use: if char.isupper():
        if char == char.upper():  # This is less precise than isupper()
            count += 1  # Increments for uppercase, numbers, and symbols
    return count  # May return incorrect count if string has numbers/symbols

# CAS DE TEST :
# This test counts uppercase in "Jonah Is Tbe Best"
# Uppercase: J, I, T, B (4 total)
# Remarque : This method may miscount if there are numbers or symbols
string = "Jonah Is Tbe Best"
print(count_uppercase(string))  # Sortie : 4

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires removing all space characters from a string. The
# function should take a string and return a new string with all space
# characters removed, effectively concatenating all words together. This is
# useful for formatting and text processing operations.
#
# Prérequis Clés :
# - Function must accept a string as input
# - Function must return a new string with all spaces removed
# - Only space characters should be removed (not tabs, newlines, etc.)
# - All other characters should remain in their original positions
#
# Exemple d'Entrée/Sortie :
# - remove_spaces("what happening boss man") should return "whathappeningbossman"
# - remove_spaces("hello world") should return "helloworld"
# - remove_spaces("no spaces") should return "nospaces"
#
# Python's replace() method is the most straightforward approach.
# ============================================================================
"""
Problème 45 :
Écrivez une fonction Python appelée remove_spaces qui prend une chaîne en entrée et retourne la chaîne avec tous spaces removed.
"""

# EXPLICATION DE LA SOLUTION (Using replace()):
# This solution uses Python's replace() method to replace all space characters
# with empty strings, effectively removing them. This is the most concise and
# efficient approach for removing spaces.
def remove_spaces(string):
    # replace(" ", "") replaces all space characters with empty string
    return string.replace(" ", "")  # Returns string with spaces removed

# CAS DE TEST :
# This test removes spaces from "what happening boss man"
# Résultat: "whathappeningbossman"
lst = "what happening boss man"
print(remove_spaces(lst))  # Sortie : whathappeningbossman

# ALTERNATIVE EXPLICATION DE LA SOLUTION (Using Loop):
# This solution manually iterates through each character and builds a new
# string without spaces. It's more verbose but demonstrates the algorithm
# clearly. This approach is less efficient than replace() but more explicit.
def remove_spaces(string):
    string_removed = []  # List to collect non-space characters

    # Iterate through each character
    for char in string:
        # Only add character if it's not a space
        if char != " ":  # Check if character is not a space
            string_removed.append(char)  # Add non-space character to list
    # Join list back into string
    return "".join(string_removed)  # Return string without spaces

# CAS DE TEST :
# Même cas de test que ci-dessus, demonstrating both solutions produce the same result
lst = "what happening boss man"
print(remove_spaces(lst))  # Sortie : whathappeningbossman

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires merging two sorted lists into a single sorted list.
# La fonction doit prendre two lists that are already sorted, combine all
# elements from both lists, and return a new list that is also sorted. This
# is a fundamental operation in merge sort and other algorithms.
#
# Prérequis Clés :
# - Function must accept two sorted lists as input
# - Function must return a NEW sorted list containing all elements
# - Input lists are assumed to be already sorted
# - Output list should be sorted (ascending order typically)
#
# Exemple d'Entrée/Sortie :
# - merge_lists([1, 3, 5], [2, 4, 6]) should return [1, 2, 3, 4, 5, 6]
# - merge_lists([1, 2], [3, 4]) should return [1, 2, 3, 4]
# - merge_lists([], [1, 2]) should return [1, 2]
#
# Remarque : The current solution re-sorts the input lists, which is unnecessary
# if they're already sorted. A proper merge would use a two-pointer approach.
# ============================================================================
"""
Problème 46 :
Écrivez une fonction Python appelée merge_lists qui prend deux listes triées en entrée et retourne une nouvelle liste triée contenant tous le éléments de les deux entrée listes.
"""

# EXPLICATION DE LA SOLUTION (Simple Approach):
# This solution combines the two lists using the + operator, then sorts the
# result. While this works, it doesn't take advantage of the fact that the
# input lists are already sorted. A more efficient approach would use a
# two-pointer merge algorithm (O(n+m) vs O(n log n)).
def merge_lists():
    # Get user input and convert to sorted lists
    # Remarque : This re-sorts the input, which is unnecessary if already sorted
    lst1 = sorted(input("Type the first sorted list: ").split())  # Sorts again
    lst2 = sorted(input("Type the second sorted list: ").split())  # Sorts again

    # Combine lists and sort the result
    merged_list = sorted(lst1 + lst2)  # Concatenate and sort

    print(merged_list)  # Print the merged and sorted list

merge_lists()  # Call the function

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires finding the index of a target element in a list.
# The function should search through the list and return the position (index)
# where the target is found. If the target is not found, it should return -1
# as a sentinel value. C'est une opération fondamentale search operation.
#
# Prérequis Clés :
# - Function must accept a list and a target element
# - Function must return the index if target is found
# - Function must return -1 if target is not found
# - Should return the first occurrence if duplicates exist
#
# Exemple d'Entrée/Sortie :
# - find_index([1, 3, 5, 7, 9], 5) should return 2 (5 is at index 2)
# - find_index([1, 3, 5, 7, 9], 6) should return -1 (6 not found)
# - find_index([1, 2, 2, 3], 2) should return 1 (first occurrence)
#
# Algorithm: Linear search - iterate through list, return index when found.
# ============================================================================
"""
Problème 47 :
Écrivez une fonction Python appelée find_index qui prend une liste de nombres et une cible nombre en entrée, et retourne le index de le cible nombre dans la liste. si le cible nombre est pas trouvé dans la liste, la fonction devrait retourner -1.
"""

# EXPLICATION DE LA SOLUTION :
# This solution uses Python's enumerate() function to get both index and value
# in each iteration. It searches linearly through the list and returns the
# index immediately when the target is found. If the entire list is searched
# without finding the target, it returns -1.
def find_index(numbers, target):
    # enumerate() provides both index and value: (0, 1), (1, 3), (2, 5), ...
    for index, num in enumerate(numbers):
        # Check if current element matches target
        if num == target:
            return index  # Return index immediately when found
    # If loop completes without finding target, return -1
    return -1  # Target not found

# TEST CASE 1:
# This test finds the index of 5 in [1, 3, 5, 7, 9]
# 5 is at index 2 (0-based indexing: 0=1, 1=3, 2=5)
numbers = [1, 3, 5, 7, 9]
target = 5
print("Index of", target, "in nums:", find_index(numbers, target))  # Sortie : Index of 5 in nums: 2

# TEST CASE 2:
# This test searches for 6, which is not in the list
# Since 6 is not found, function returns -1
target = 6
print("Index of", target, "in nums:", find_index(numbers, target))  # Sortie : Index of 6 in nums: -1

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires summing elements at even indices (0, 2, 4, 6, ...) in
# a list. The function should iterate through the list, check if each index
# is even, and accumulate the sum of elements at those positions. This is
# useful for processing alternating elements or specific index patterns.
#
# Prérequis Clés :
# - Function must accept a list of numbers
# - Must sum elements at even indices (0, 2, 4, 6, ...)
# - Index 0 is considered even
# - Should return the total sum
#
# Exemple d'Entrée/Sortie :
# - sum_even_indices([1, 2, 3, 4, 5, 6]) sums indices 0,2,4: 1+3+5 = 9
# - sum_even_indices([10, 20, 30, 40]) sums indices 0,2: 10+30 = 40
# - sum_even_indices([5]) sums index 0: 5
#
# Algorithm: Iterate through indices, check if even (i % 2 == 0), sum those elements.
# ============================================================================
"""
Problème 48 :
Écrivez une fonction Python appelée sum_even_indices qui prend une liste de nombres en entrée et retourne le somme de le éléments at même les indices (0-based) dans la liste.
"""

# EXPLICATION DE LA SOLUTION (Using Loop):
# This solution iterates through all indices, checks if each is even using
# the modulo operator, and accumulates the sum of elements at even positions.
# This is clear and easy to understand.
def sum_even_indices(nums):
    total = 0  # Initialize sum accumulator

    # Iterate through all indices of the list
    for i in range(len(nums)):
        # Check if current index is even (0, 2, 4, 6, ...)
        if i % 2 == 0:  # i % 2 == 0 means index is even
            total += nums[i]  # Add element at even index to sum
    return total  # Return the total sum

# CAS DE TEST :
# This test sums elements at even indices in [1, 2, 3, 4, 5, 6]
# Even indices: 0 (1), 2 (3), 4 (5)
# Sum: 1 + 3 + 5 = 9
numbers = [1, 2, 3, 4, 5, 6]
print("Sum of elements at even indices:", sum_even_indices(numbers))  # Sortie : Sum of elements at even indices: 9

# ALTERNATIVE EXPLICATION DE LA SOLUTION (Using Generator Expression):
# This solution uses a generator expression with sum() for a more concise
# one-liner. It's functionally identical to the loop version but more Pythonic.
def sum_even_indices(nums):
    # Generator expression: nums[i] for each even index i
    # sum() adds all values from the generator
    return sum(nums[i] for i in range(len(nums)) if i % 2 == 0)  # One-liner version

# CAS DE TEST :
# Même cas de test que ci-dessus, demonstrating both solutions produce the same result
numbers = [1, 2, 3, 4, 5, 6]
print("Sum of elements at even indices:", sum_even_indices(numbers))  # Sortie : Sum of elements at even indices: 9

# ============================================================================
# EXPLICATION DU PROBLÈME :
# remove_duplicates_case_insensitive that takes a list of strings as input and returns a new list with duplicate strings removed, ignoring case sensitivity. For example, “hello” and “HELLO” should be co
# nsidered the same. Do not use set().
#
# Prérequis Clés :
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
# - Must work with strings
# - Should handle case sensitivity appropriately
# - Must remove or handle duplicate elements
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses recursion to solve the problem.
# ============================================================================
"""
Problème 49 :
Écrivez une fonction Python appelée remove_duplicates_case_insensitive qui prend une liste de chaînes en entrée et retourne une nouvelle liste avec en double strings removed, en ignorant la casse sensitivity. par exemple, “hello” et “HELLO” devrait be considered le même. N'utilisez pas set().
"""

def remove_duplicates(lst):
    # Function definition
    unique = set()
    common = []
    for word in lst:
        # Iterates through each element
        word_lower = word.lower()
            # Converts to lowercase/uppercase
        if word_lower not in unique:
            common.append(word_lower)
            unique.add(word_lower)
    return common
        # Returns the result

lst = ["not", "not", "hot", "hot"]
print(remove_duplicates(lst))

def remove_duplicates(lst):
    # Function definition
    unique = set()
    for word in lst:
        # Iterates through each element
        word_lower = word.lower()
            # Converts to lowercase/uppercase
        if word_lower not in unique:
            unique.add(word_lower)
    return unique
        # Returns the result

lst = ["not", "not", "hot", "hot", "cold"]
print(remove_duplicates(lst))

def remove_duplicates(strings):
    # Function definition
    unique_strings = []
    for string in strings:
        # Iterates through each element
        if string.lower() not in map(str.lower, unique_strings):
            # Converts to lowercase/uppercase
            unique_strings.append(string)
    return unique_strings
        # Returns the result

input_strings = ["Hello", "HELLO", "world", "World", "Python", "python"]
print("List with case-insensitive duplicates removed:", remove_duplicates(input_strings))


# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires determining if a string is a palindrome. A palindrome
# reads the same forwards and backwards (e.g., "racecar", "level", "madam").
# The function should compare the string with its reverse to check if they're
# identical. This is une opération courante string manipulation and validation task.
#
# Prérequis Clés :
# - Function must accept a string as input
# - Function must return True if palindrome, False otherwise
# - Should check if string == reversed string
# - Case-sensitive by default (unless specified otherwise)
#
# Exemple d'Entrée/Sortie :
# - is_palindrome("racecar") should return True (reads same forwards/backwards)
# - is_palindrome("hello") should return False (hello != olleh)
# - is_palindrome("level") should return True
# - is_palindrome("Racecar") should return False (case-sensitive: R != r)
#
# Algorithm: Compare string with its reverse using slicing [::-1].
# ============================================================================
"""
Problème 50 :
Écrivez une fonction Python appelée is_palindrome qui prend une chaîne en entrée et retourne vrai si la chaîne est un palindrome (lit le même forwards et backwards), et False sinon.
"""

# EXPLICATION DE LA SOLUTION :
# This solution uses Python's string slicing [::-1] to create a reversed
# copy of the string, then compares it with the original. If they're equal,
# the string is a palindrome. This is the most concise and Pythonic approach.
def is_palindrome(s):
    # [::-1] creates a reversed copy of the string
    # s == s[::-1] compares original with reversed
    # Returns True if they're equal (palindrome), False otherwise
    return s == s[::-1]  # One-liner palindrome check

# TEST CASE 1:
# This test checks if "racecar" is a palindrome
# "racecar" == "racecar"[::-1] → "racecar" == "racecar" → True
input_string = "racecar"
print("Is", input_string, "a palindrome?", is_palindrome(input_string))  # Sortie : Is racecar a palindrome? True

# TEST CASE 2:
# This test checks if "hello" is a palindrome
# "hello" == "hello"[::-1] → "hello" == "olleh" → False
input_string = "hello"
print("Is", input_string, "a palindrome?", is_palindrome(input_string))  # Sortie : Is hello a palindrome? False

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires calculating the factorial of a non-negative integer.
# The factorial of n (denoted as n!) is the product of all positive integers
# from 1 to n. By definition, 0! = 1. Factorials grow very quickly and are
# used in combinatorics, probability, and mathematical analysis.
#
# Prérequis Clés :
# - Function must accept a non-negative integer n
# - Function must return n! = n × (n-1) × (n-2) × ... × 2 × 1
# - Special case: 0! = 1 (by mathematical definition)
# - Should handle edge cases (0, 1)
#
# Exemple d'Entrée/Sortie :
# - factorial(0) should return 1 (0! = 1 by definition)
# - factorial(5) should return 120 (5 × 4 × 3 × 2 × 1 = 120)
# - factorial(1) should return 1 (1! = 1)
# - factorial(3) should return 6 (3 × 2 × 1 = 6)
#
# Algorithm: Can be implemented iteratively (loop) or recursively.
# ============================================================================
"""
Problème 51 :
Écrivez une fonction Python appelée `la factorielle` qui prend un non-négatif integer en entrée et retourne ses la factorielle. la factorielle de un nombre `n` est le produit de tous positif integers less que ou equal à `n` (n!). par exemple, `la factorielle(5)` devrait retourner `120` (since 5 * 4 * 3 * 2 * 1 = 120).
"""

# EXPLICATION DE LA SOLUTION (Iterative - Forward Loop):
# This solution uses an iterative approach with a forward loop. It handles
# the base case (n == 0) separately, then multiplies numbers from 1 to n.
# This is efficient and avoids stack overflow issues that recursion might have.
def factorial(n):
    # Base case: 0! = 1 (mathematical definition)
    if n == 0:
        return 1
    else:
        result = 1  # Initialize result to 1 (multiplicative identity)
        # Multiply all numbers from 1 to n
        for i in range(1, n + 1):  # range(1, n+1) = 1, 2, 3, ..., n
            result *= i  # Multiply: result = 1 × 2 × 3 × ... × n
        return result  # Return the factorial

# CAS DE TEST :
# This test calculates 0! which is 1 by definition
print(factorial(0))  # Sortie : 1

# ALTERNATIVE EXPLICATION DE LA SOLUTION (Recursive):
# This solution uses recursion, which is more elegant but can cause stack
# overflow for very large numbers. It defines factorial(n) in terms of
# factorial(n-1), with 0! = 1 as the base case.
def factorial(n):
    # Base case: 0! = 1
    if n == 0:
        return 1
    else:
        # Recursive case: n! = n × (n-1)!
        return n * factorial(n - 1)  # Calls itself with n-1

# CAS DE TEST :
# This test calculates 5! recursively
# 5! = 5 × 4! = 5 × 4 × 3! = 5 × 4 × 3 × 2! = 5 × 4 × 3 × 2 × 1! = 5 × 4 × 3 × 2 × 1 = 120
print(factorial(5))  # Sortie : 120

# ALTERNATIVE EXPLICATION DE LA SOLUTION (Iterative - Backward Loop):
# This solution uses a backward loop, counting down from n to 1. It's
# functionally identical to the forward loop but demonstrates an alternative
# iteration pattern.
def factorial(n):
    # Base case: 0! = 1
    if n == 0:
        return 1
    else:
        result = 1  # Initialize result
        # Multiply numbers from n down to 1
        for i in range(n, 0, -1):  # range(n, 0, -1) = n, n-1, ..., 2, 1
            result *= i  # Multiply: result = n × (n-1) × ... × 2 × 1
        return result  # Return the factorial

# CAS DE TEST :
# Même cas de test que ci-dessus, demonstrating backward iteration
print(factorial(5))  # Sortie : 120

# ============================================================================
# EXPLICATION DU PROBLÈME :
# is_anagram that takes two strings as input and returns True if they are anagrams of each other, and False otherwise. Two strings are anagrams if they can be rearranged to form the same word (e.g., “li
# sten” and “silent”).
#
# Prérequis Clés :
# - Program must prompt user for input
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
# - Must work with strings
# - Must check if strings contain same letters in different order
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses recursion to solve the problem.
# ============================================================================
"""
Problème 52 :
Écrivez une fonction Python appelée is_anagram qui prend deux strings en entrée et retourne vrai si they sont anagrams de chaque autre, et False sinon. deux strings sont anagrams si they peut be rearranged à form le même mot (e.g., “listen” et “silent”).
"""

def main():
    # Get first string from user and convert to lowercase
    string1 = input("type string: ").lower()  # e.g., "Listen" → "listen"
    # Get second string from user and convert to lowercase
    string2 = input("type string: ").lower()  # e.g., "Silent" → "silent"

    # sorted() converts string to list of sorted characters
    # e.g., "listen" → ['e', 'i', 'l', 'n', 's', 't']
    sorted1 = sorted(string1)
        # Sorts elements in ascending order
    sorted2 = sorted(string2)
        # Sorts elements in ascending order

    # Compare sorted lists - if equal, strings are anagrams
    if sorted1 == sorted2:
        # Checks condition
        return True  # Strings are anagrams
    return False  # Strings are not anagrams

main()

# CORRECT EXPLICATION DE LA SOLUTION (Function with Parameters):
# This solution accepts two strings as parameters, making it reusable and
# testable. It converts both to lowercase for case-insensitive comparison,
# sorts them, and returns True if the sorted versions are equal. This is
# the most concise and Pythonic approach.
def is_anagram(str1, str2):
    # Convert both strings to lowercase for case-insensitive comparison
    str1 = str1.lower()  # "Listen" → "listen"
    str2 = str2.lower()  # "Silent" → "silent"

    # sorted() returns a list of sorted characters
    # Compare sorted lists - if equal, strings contain same letters (anagrams)
    return sorted(str1) == sorted(str2)  # Returns True if anagrams, False otherwise

# TEST CASE 1:
# "listen" and "silent" are anagrams (same letters: e, i, l, n, s, t)
print(is_anagram("listen", "silent"))  # Sortie : True

# TEST CASE 2:
# "hello" and "world" are NOT anagrams (different letters)
print(is_anagram("hello", "world"))  # Sortie : False

# TEST CASE 3:
# "Triangle" and "Integral" are anagrams (same letters, different order)
print(is_anagram("Triangle", "Integral"))  # Sortie : True

# ALTERNATIVE EXPLICATION DE LA SOLUTION (Same Logic, Different Variable Names):
# This solution uses the same algorithm but with different variable names.
# It's functionally identical to the previous solution.
def is_anagram(lst1, lst2):
    # Sort both strings into lists of characters
    sorted_lst1 = sorted(lst1)  # "qwer" → ['e', 'q', 'r', 'w']
    sorted_lst2 = sorted(lst2)  # "rewq" → ['e', 'q', 'r', 'w']

    # Compare sorted lists
    if sorted_lst1 == sorted_lst2:
        # Checks condition
        return True  # Strings are anagrams
    return False  # Strings are not anagrams

# CAS DE TEST :
# "qwer" and "rewq" are anagrams (reversed order, same letters)
lst1 = "qwer"
lst2 = "rewq"
print(is_anagram(lst1, lst2))  # Sortie : True


# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a word frequency dictionary from a string.
# The function should count how many times each word appears in the string,
# treating words case-insensitively (so "This" and "this" are the same word).
# C'est une opération fondamentale text analysis operation used in natural language
# processing and data analysis.
#
# Prérequis Clés :
# - Function must accept a string as input
# - Function must return a dictionary with words as keys and counts as values
# - Words are separated by spaces
# - Case-insensitive (treat "Hello" and "hello" as the same word)
#
# Exemple d'Entrée/Sortie :
# - count_words("This is a test. This test is only a test.") should return
#   {'this': 2, 'is': 2, 'a': 2, 'test.': 1, 'test': 1, 'only': 1}
# - count_words("hello Hello HELLO") should return {'hello': 3}
#
# Algorithm: Convert to lowercase, split into words, count occurrences in dictionary.
# ============================================================================
"""
Problème 53 :
Écrivez une fonction Python appelée count_words qui prend une chaîne en entrée et retourne un dictionnaire où le clés sont le words dans la chaîne et le valeurs sont le compte de chaque mot. Words sont séparés by spaces, et la fonction devrait be cas-insensitive.
"""

# EXPLICATION DE LA SOLUTION :
# This solution converts the string to lowercase for case-insensitive counting,
# splits it into words, then uses a dictionary to track word frequencies. It
# checks if each word already exists in the dictionary and increments or
# initializes the count accordingly.
def count_words(s):
    # Convert to lowercase for case-insensitive comparison
    s = s.lower()  # "This is a test" → "this is a test"
    # Split string into list of words
    words = s.split()  # ["this", "is", "a", "test", "this", "test", ...]
    word_count = {}  # Dictionary to store word frequencies

    # Iterate through each word
    for word in words:
        # Check if word already in dictionary
        if word in word_count:
            word_count[word] += 1  # Increment count if word exists
        else:
            word_count[word] = 1  # Initialize count to 1 if new word
    return word_count  # Return dictionary with word counts

# CAS DE TEST :
# This test counts words in "This is a test. This test is only a test."
# After lowercase and split: ["this", "is", "a", "test.", "this", "test", "is", "only", "a", "test."]
# Résultat: {'this': 2, 'is': 2, 'a': 2, 'test.': 2, 'only': 1}
# Remarque : Punctuation is included with words (test. vs test)
input_string = "This is a test. This test is only a test."
print(count_words(input_string))  # Sortie : {'this': 2, 'is': 2, 'a': 2, 'test.': 2, 'only': 1}

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires generating the first n numbers of the Fibonacci sequence.
# The Fibonacci sequence is a famous mathematical sequence where each number is
# the sum of the two preceding ones, starting from 0 and 1. The sequence goes:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ... This sequence appears in nature and
# has many applications in mathematics and computer science.
#
# Prérequis Clés :
# - Function must accept an integer n
# - Function must return a list of the first n Fibonacci numbers
# - Sequence starts with 0 and 1
# - Each subsequent number = sum of previous two numbers
# - Handle edge cases: n <= 0, n == 1, n == 2
#
# Exemple d'Entrée/Sortie :
# - fibonacci(0) should return [] (empty list)
# - fibonacci(1) should return [0]
# - fibonacci(2) should return [0, 1]
# - fibonacci(10) should return [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
#
# Algorithm: Start with [0, 1], then generate next numbers by summing last two.
# ============================================================================
"""
Problème 54 :
Écrivez une fonction Python appelée fibonacci qui prend un entier n en entrée et retourne une liste contenant les n premiers nombres de la suite de Fibonacci. la suite de Fibonacci commence par 0 et 1, et chaque subsequent nombre est le somme de le précédent deux nombres.
"""

# EXPLICATION DE LA SOLUTION :
# This solution handles edge cases first, then generates the Fibonacci sequence
# iteratively. It starts with the base cases [0] and [0, 1], then generates
# subsequent numbers by summing the last two elements in the sequence.
def fibonacci(n):
    # Edge case: n <= 0 returns empty list
    if n <= 0:
        return []  # No Fibonacci numbers to generate
    # Edge case: n == 1 returns just [0]
    elif n == 1:
        return [0]  # First Fibonacci number
    # Edge case: n == 2 returns [0, 1]
    elif n == 2:
        return [0, 1]  # First two Fibonacci numbers

    # Initialize the first two numbers of the Fibonacci sequence
    fib_sequence = [0, 1]  # Start with base values

    # Generate the remaining Fibonacci numbers
    # We already have 2 numbers, so generate n-2 more
    for i in range(2, n):  # range(2, n) = 2, 3, 4, ..., n-1
        # Each new number is the sum of the last two numbers
        next_number = fib_sequence[-1] + fib_sequence[-2]  # Sum last two
        fib_sequence.append(next_number)  # Add to sequence

    return fib_sequence  # Return complete Fibonacci sequence

# CAS DE TEST :
# This test generates the first 10 Fibonacci numbers
# Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
print(fibonacci(10))  # Sortie : [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires calculating the area of a rectangle. The area of a
# rectangle is calculated by multiplying its length by its width. The function
# should prompt the user for both dimensions, perform the calculation, and
# display the result. C'est une opération de base geometric calculation exercise.
#
# Prérequis Clés :
# - Program must prompt user for length and width
# - Must calculate area = length × width
# - Should handle floating-point numbers (decimals)
# - Should display the result
#
# Exemple d'Entrée/Sortie :
# - If user enters length=5, width=3, area should be 15
# - If user enters length=10.5, width=2.5, area should be 26.25
#
# Formula: Area = length × width
# ============================================================================
"""
Problème 55 :
Écrivez un programme Python à calculate le area de un rectangle. demander le utilisateur à saisir la longueur et width.
"""

# EXPLICATION DE LA SOLUTION :
# This solution prompts the user for both length and width, converts the input
# to floats to handle decimal values, calculates the area by multiplying them,
# and prints the result. This is a straightforward interactive program.
def area_rectangle():
    # Get length from user and convert to float
    length = float(input("type length: "))  # e.g., 5.0
    # Get width from user and convert to float
    width = float(input("type width: "))  # e.g., 3.0
    # Calculate area: length × width
    area = length * width  # e.g., 5.0 × 3.0 = 15.0

    # Display the result
    print(area)  # Prints the area

area_rectangle()  # Call the function

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires determining if a number is even or odd. An even number
# is divisible by 2 (remainder 0 when divided by 2), while an odd number has
# a remainder of 1 when divided by 2. The program should prompt the user for
# a number and display whether it's even or odd.
#
# Prérequis Clés :
# - Program must prompt user for a number
# - Must check if number is even (divisible by 2) or odd
# - Should display appropriate message
#
# Exemple d'Entrée/Sortie :
# - If user enters 4, output: "Number is even"
# - If user enters 7, output: "Number is odd"
# - If user enters 0, output: "Number is even"
#
# Algorithm: Use modulo operator (%) - if number % 2 == 0, it's even; else odd.
# ============================================================================
"""
Problem: 56
Write a Python program to check if a given number is even or odd. Prompt the user to enter a number.

# EXPLICATION DE LA SOLUTION :
# This solution uses the modulo operator (%) to check if a number is divisible
# by 2. If the remainder is 0, the number is even; otherwise, it's odd. This
# is the standard and most efficient way to check even/odd status.
def even_odd():
    # Get number from user and convert to integer
    user = int(input("type number: "))  # e.g., 4 or 7

    # Check if number is even (remainder when divided by 2 is 0)
    if user % 2 == 0:  # If remainder is 0, number is even
        print("Number is even")  # Display even message
    else:  # If remainder is not 0 (i.e., 1), number is odd
        print("Number is odd")  # Display odd message

even_odd()  # Call the function

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires generating and printing the Fibonacci sequence up to
# a given limit. The Fibonacci sequence starts with 0 and 1, and each
# subsequent number is the sum of the previous two. The program should use
# a while loop to generate numbers until they exceed the limit.
#
# Prérequis Clés :
# - Program must prompt user for a limit
# - Must use a while loop (as specified)
# - Should print Fibonacci numbers up to (and including) the limit
# - Sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...
#
# Exemple d'Entrée/Sortie :
# - If user enters limit=10, output: "0 1 1 2 3 5 8"
# - If user enters limit=20, output: "0 1 1 2 3 5 8 13"
#
# Algorithm: Start with a=0, b=1. While a <= limit, print a, then update a=b, b=a+b.
# ============================================================================
"""
Problem 57
Write a Python program to print the Fibonacci series up to a given number. Prompt the user to enter the limit using a while loop.

# EXPLICATION DE LA SOLUTION :
# This solution uses a while loop to generate Fibonacci numbers. It starts
# with a=0 and b=1, prints each number as long as it's <= limit, then
# updates a and b using tuple assignment to generate the next number.
def fibonacci_series():
    # Get limit from user
    limit = int(input("Enter the limit: "))  # e.g., 10
    # Initialize first two Fibonacci numbers
    a, b = 0, 1  # a=0 (first), b=1 (second)

    # Continue while current number (a) is <= limit
    while a <= limit:  # Loop until a exceeds limit
        # Print current Fibonacci number (end=' ' keeps on same line)
        print(a, end=' ')  # Prints: 0, then 1, then 1, then 2, etc.
        # Update: a becomes b, b becomes a+b (next Fibonacci number)
        a, b = b, a + b  # Tuple assignment: a=1,b=1 → a=1,b=2 → a=2,b=3, etc.

fibonacci_series()  # Call the function

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires finding the maximum (largest) of three numbers. The
# program should prompt the user for three numbers, then determine and display
# which one is the largest. This is une opération courante comparison operation.
#
# Prérequis Clés :
# - Program must prompt user for three numbers
# - Must find the maximum among the three
# - Should display the maximum number
#
# Exemple d'Entrée/Sortie :
# - If user enters "10 20 15", output: 20
# - If user enters "5 3 8", output: 8
# - If user enters "100 100 100", output: 100
#
# Algorithm: Compare numbers sequentially, track the largest found so far.
# ============================================================================
"""
Problem: 58
Write a Python program to find the maximum of three numbers. Prompt the user to enter three numbers."

# EXPLICATION DE LA SOLUTION :
# This solution gets three numbers from user input, converts them to integers,
# then uses a loop to find the maximum by comparing each number with the
# current maximum and updating it when a larger number is found.
def max_number():
    # Get user input and split into list of strings
    user = input("type 3 numbers: ").split()  # e.g., "10 20 15" → ["10", "20", "15"]
    int_number = []  # List to store converted integers

    # Convert each string to integer
    for number in user:
        int_number.append(int(number))  # ["10", "20", "15"] → [10, 20, 15]

    # Initialize max_num with first number
    max_num = int_number[0]  # Assume first number is maximum (10)

    # Compare each number with current maximum
    for number in int_number:
        # If current number is greater than max_num, update max_num
        if number > max_num:  # 20 > 10, so max_num = 20; 15 > 20? No
            max_num = number  # Update maximum
    print(max_num)  # Print the maximum number (20)

max_number()  # Call the function

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires reversing a string. The program should take a string
# and return a new string with all characters in reverse order. For example,
# "hello" becomes "olleh". This is une opération courante string manipulation operation.
#
# Prérequis Clés :
# - Program must prompt user for a string
# - Must reverse the string (last character becomes first, etc.)
# - Should display the reversed string
#
# Exemple d'Entrée/Sortie :
# - If user enters "hello", output: "olleh"
# - If user enters "Jonathan", output: "nahtanoJ"
# - If user enters "abc", output: "cba"
#
# Algorithm: Use string slicing [::-1] to create reversed copy.
# ============================================================================
"""
Problème 59 :
Écrivez un programme Python à reverse une chaîne. demander le utilisateur à saisir une chaîne.
"""

# EXPLICATION DE LA SOLUTION (Interactive Version):
# This solution prompts the user for input, reverses the string using slicing,
# and prints the result. The [::-1] slice creates a reversed copy of the string.
def reverse_string():
    # Get string from user
    user = input("type string: ")  # e.g., "hello"
    # Reverse the string using slicing [::-1]
    user = user[::-1]  # "hello" → "olleh"

    # Display the reversed string
    print(user)  # Prints: olleh

reverse_string()  # Call the function

# ALTERNATIVE EXPLICATION DE LA SOLUTION (Function with Parameter):
# This solution accepts a string as a parameter, making it reusable and
# testable. It uses the same slicing approach but returns the result instead
# of printing it directly.
def reverse_string(string):
    # [::-1] creates a reversed copy of the string
    return string[::-1]  # Returns reversed string

# CAS DE TEST :
# This test reverses "Jonathan" to "nahtanoJ"
lst = "Jonathan"
print(reverse_string(lst))  # Sortie : nahtanoJ

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires determining if a string is a palindrome. A palindrome
# reads the same forwards and backwards (e.g., "racecar", "level", "madam").
# The program should handle case-insensitivity and ignore spaces, then check
# if the normalized string equals its reverse.
#
# Prérequis Clés :
# - Program must prompt user for a string
# - Should handle case-insensitivity (treat "Racecar" same as "racecar")
# - Should ignore spaces (treat "a man a plan" same as "amanaplan")
# - Must return True if palindrome, False otherwise
#
# Exemple d'Entrée/Sortie :
# - If user enters "racecar", output: True
# - If user enters "hello", output: False
# - If user enters "A man a plan", output: True (after normalization)
#
# Algorithm: Normalize string (lowercase, remove spaces), compare with reverse.
# ============================================================================
"""
Problem: 60
Write a Python program to check if a given string is a palindrome. Prompt the user to enter a string.

# EXPLICATION DE LA SOLUTION :
# This solution normalizes the input string by converting to lowercase and
# removing spaces, then compares it with its reverse. If they're equal,
# the string is a palindrome. This handles case-insensitivity and spaces.
def is_palindrome():
    # Get string from user, normalize it
    user = input("type word: ").lower().replace(" ", "")  # "Race Car" → "racecar"

    # Compare normalized string with its reverse
    # If equal, it's a palindrome
    return user == user[::-1]  # "racecar" == "racecar" → True

print(is_palindrome())  # Call function and print result

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires counting the number of vowels in a string. Vowels are
# the letters a, e, i, o, u (and sometimes y, but typically just aeiou). The
# program should iterate through the string and count how many characters are
# vowels. This is useful for text analysis and language processing.
#
# Prérequis Clés :
# - Program must prompt user for a string
# - Must count vowels (a, e, i, o, u)
# - Should handle case-insensitivity (convert to lowercase)
# - Should display the count
#
# Exemple d'Entrée/Sortie :
# - If user enters "hello", output: 2 (e, o)
# - If user enters "Jonathan", output: 3 (o, a, a)
# - If user enters "xyz", output: 0 (no vowels)
#
# Algorithm: Convert to lowercase, iterate through characters, count vowels.
# ============================================================================
"""
Problem: 61
Write a Python program to count the number of vowels in a given string. Prompt the user to enter a string.

# EXPLICATION DE LA SOLUTION :
# This solution converts the input to lowercase for case-insensitive counting,
# defines the vowels, then iterates through each character and increments a
# counter when a vowel is found. This is a straightforward counting algorithm.
def count_vowels():
    # Get string from user and convert to lowercase
    user = input("type string: ").lower()  # "Hello" → "hello"
    # Define vowels (lowercase only, since we converted input)
    vowels = "aeiou"  # String containing all vowels
    count = 0  # Initialize vowel counter

    # Iterate through each character
    for char in user:
        # Check if current character is a vowel
        if char in vowels:  # If char is 'a', 'e', 'i', 'o', or 'u'
            count += 1  # Increment counter
    print(count)  # Display the total count

count_vowels()  # Call the function

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires calculating the factorial of a number. The factorial
# of n (n!) is the product of all positive integers from 1 to n. By definition,
# 0! = 1. The program should prompt the user for a number and calculate its
# factorial. C'est une opération fondamentale mathematical operation.
#
# Prérequis Clés :
# - Program must prompt user for a number
# - Must calculate n! = n × (n-1) × (n-2) × ... × 2 × 1
# - Should display the result
#
# Exemple d'Entrée/Sortie :
# - If user enters 5, output: 120 (5 × 4 × 3 × 2 × 1 = 120)
# - If user enters 3, output: 6 (3 × 2 × 1 = 6)
# - If user enters 0, output: 1 (0! = 1 by definition)
#
# Algorithm: Initialize result=1, multiply by each number from 1 to n.
# ============================================================================
"""
Problem: 62
Write a Python program to calculate the factorial of a number. Prompt the user to enter a number.

# EXPLICATION DE LA SOLUTION (Hardcoded - Incomplete):
# ATTENTION : This solution has a bug - it hardcodes the range to 1-6 instead
# of using the user's input. It always calculates 6! = 720, regardless of
# what number the user might want. This doesn't satisfy the problem requirements.
def factorial():
    result = 1  # Initialize result
    # BUG: Hardcoded range(1, 6) instead of using user input
    for i in range(1, 6):  # Always calculates 5! = 120 (WRONG!)
        result *= i  # Multiply: 1 × 2 × 3 × 4 × 5 = 120

    print(f"{result}")  # Always prints 120

factorial()  # Call the function

# CORRECT EXPLICATION DE LA SOLUTION :
# This solution properly prompts the user for input, then calculates the
# factorial of that number. It uses a loop to multiply all numbers from 1
# to the input number, which correctly implements the factorial algorithm.
def factorial():
    # Get number from user
    number = int(input("Enter a number: "))  # e.g., 5
    result = 1  # Initialize result to 1 (multiplicative identity)

    # Multiply all numbers from 1 to number
    for i in range(1, number + 1):  # range(1, 6) = 1, 2, 3, 4, 5
        result *= i  # Multiply: 1 × 2 × 3 × 4 × 5 = 120

    # Display the result with a descriptive message
    print(f"The factorial of {number} is {result}")  # Prints: The factorial of 5 is 120

factorial()  # Call the function

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires calculating the sum of all numbers from 1 to a given
# number n. For example, if n=5, the sum is 1+2+3+4+5=15. However, the current
# solution appears to sum a list of numbers provided by the user, not the
# sum from 1 to n. The problem statement suggests summing 1 to n, but the
# implementation sums user-provided numbers.
#
# Prérequis Clés :
# - Program should calculate sum from 1 to n (or sum user-provided numbers)
# - Must prompt user for input
# - Should display the total sum
#
# Exemple d'Entrée/Sortie :
# - If problem means sum 1 to n: user enters 5, output: 15 (1+2+3+4+5)
# - If problem means sum list: user enters "1 2 3 4 5", output: 15
#
# Remarque : The current implementation sums a list of numbers, not 1 to n.
# ============================================================================
"""
Problem: 63
Write a Python program to calculate the sum of all numbers from 1 to a given number. Prompt the user to enter a number.

# EXPLICATION DE LA SOLUTION (Sums List of Numbers):
# This solution sums a list of numbers provided by the user, not the sum from
# 1 to n. It splits the input, converts to integers, and accumulates the sum.
# This may not match the problem statement which asks for "sum of all numbers
# from 1 to a given number", but it demonstrates list summation.
def sum_of_all_numbers():
    # Get user input and split into list
    user = input("type numbers: ").split()  # "1 2 3 4 5" → ["1", "2", "3", "4", "5"]
    int_user = []  # List to store converted integers

    # Convert each string to integer
    for number in user:
        int_user.append(int(number))  # ["1", "2", ...] → [1, 2, 3, 4, 5]

    count = 0  # Initialize sum accumulator

    # Sum all numbers in the list
    for number in int_user:
        count += number  # Add each number: 1+2+3+4+5 = 15
    print(count)  # Display the sum

sum_of_all_numbers()  # Call the function

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires finding the largest (maximum) element in a list of
# numbers. The program should prompt the user for a list of numbers, then
# determine and return the maximum value. C'est une opération fondamentale list operation.
#
# Prérequis Clés :
# - Program must prompt user for a list of numbers
# - Must find the largest number in the list
# - Should display the largest number
#
# Exemple d'Entrée/Sortie :
# - If user enters "2 56 75 4566 3", output: 4566
# - If user enters "10 20 15", output: 20
# - If user enters "5", output: 5
#
# Algorithm: Can use sorted() and take last element, or max(), or manual loop.
# ============================================================================
"""
Problem: 64
Write a Python program to find the largest element in a list. Prompt the user to enter a list of numbers.

# EXPLICATION DE LA SOLUTION (Using sorted() - Ascending):
# This solution sorts the list in ascending order and takes the last element,
# which will be the largest. This works but is less efficient than using max()
# since it sorts the entire list when we only need the maximum.
def find_largest():
    # Get user input and split into list
    user = input("type number: ").split()  # "2 56 75 4566 3" → ["2", "56", ...]
    int_number = []  # List to store converted integers

    # Convert each string to integer
    for number in user:
        int_number.append(int(number))  # [2, 56, 75, 4566, 3]

    # Sort in ascending order
    sort = sorted(int_number)  # [2, 3, 56, 75, 4566]
    # Get the last element (largest)
    largest = sort[-1]  # 4566

    print(largest)  # Display the largest number

find_largest()  # Call the function

# ALTERNATIVE EXPLICATION DE LA SOLUTION (Using sorted() - Descending):
# This solution sorts in descending order and takes the first element. It's
# functionally identical to the previous solution but demonstrates reverse sorting.
def find_largest():
    # Get user input and convert to integers
    user = input("type number: ").split()
    int_number = []
    for number in user:
        int_number.append(int(number))

    # Sort in descending order
    sort = sorted(int_number, reverse=True)  # [4566, 75, 56, 3, 2]
    # Get the first element (largest)
    largest = sort[0]  # 4566

    print(largest)  # Display the largest number

find_largest()  # Call the function

# ALTERNATIVE EXPLICATION DE LA SOLUTION (Using max()):
# This solution uses Python's built-in max() function, which is the most
# efficient and Pythonic approach. It directly finds the maximum without
# sorting the entire list.
def largest_element(numbers):
    # max() finds the maximum element in the list
    return max(numbers)  # Returns the largest number

# CAS DE TEST :
# This test finds the largest in [2, 56, 75, 4566, 3]
numbers = [2, 56, 75, 4566, 3]
print(largest_element(numbers))  # Sortie : 4566

# ALTERNATIVE EXPLICATION DE LA SOLUTION (Manual Loop):
# This solution manually finds the maximum by iterating through the list and
# comparing each element with the current maximum. It's more verbose but
# demonstrates the algorithm clearly.
def largest_element(numbers):
    # Initialize with first element
    largest = numbers[0]  # Assume first is largest

    # Compare each number with current largest
    for number in numbers:
        # If current number is greater, update largest
        if number > largest:  # 56 > 2, so largest = 56; 75 > 56, so largest = 75, etc.
            largest = number  # Update maximum
    return largest  # Return the largest number

# CAS DE TEST :
# Même cas de test que ci-dessus, demonstrating manual approach
numbers = [2, 56, 75, 4566, 3]
print(largest_element(numbers))  # Sortie : 4566

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires finding the largest element in a list of strings (not
# numbers). "Largest" here means the longest string (most characters). The
# program should find the string with the maximum length. This is useful for
# text processing and finding the longest word in a list.
#
# Prérequis Clés :
# - Function must accept a list of strings
# - Must find the string with maximum length
# - Should not use numeric comparisons (compare by length instead)
#
# Exemple d'Entrée/Sortie :
# - largest_element(["tree", "cliff", "mountain"]) should return "mountain" (8 chars)
# - largest_element(["house", "counter", "if"]) should return "counter" (7 chars)
# - largest_element(["a", "bb", "ccc"]) should return "ccc" (3 chars)
#
# Algorithm: Compare strings by their length, track the longest one.
# ============================================================================
"""
Problem: 65
Write a Python program to find the largest element in a list (do not use numbers).

# EXPLICATION DE LA SOLUTION (Using max() with key):
# This solution uses Python's max() function with key=len to find the string
# with the maximum length. The key parameter tells max() to compare elements
# by their length rather than alphabetically. This is the most concise approach.
def main(lst):
    # max() finds maximum element, key=len compares by length
    return max(lst, key=len)  # Returns the longest string

# CAS DE TEST :
# This test finds the longest string in the list
# "mountain" and "grassy" both have 8 characters, but "mountain" appears first
lst = ["tree", "cliff", "mountain", "tree","tree", "grassy"]
main(lst)  # Retourne : "mountain"

# ALTERNATIVE EXPLICATION DE LA SOLUTION (Manual Implementation):
# This solution manually tracks the longest string by iterating through all
# strings and comparing their lengths. It's more verbose but demonstrates
# the algorithm clearly.
def largest_elememt(lst):
    count = 0  # Track the length of the longest string found
    largest = ""  # Track the longest string itself

    # Iterate through each word
    for word in lst:
        # If current word is longer than the longest found so far
        if len(word) > count:  # Compare lengths
            count = len(word)  # Update the length
            largest = word  # Update the word
    return largest  # Return the longest string

# CAS DE TEST :
# This test finds the longest string manually
# "house"=5, "counter"=7, "if"=2 → "counter" is longest
lst = ["house", "counter", "if"]
print(largest_elememt(lst))  # Sortie : counter

# ALTERNATIVE EXPLICATION DE LA SOLUTION (Using sorted()):
# This solution sorts the list by length, then returns the last element
# (which will be the longest). This works but is less efficient than max()
# since it sorts the entire list when we only need the maximum.
def largest_elememt(lst):
    # Sort list by length (ascending order)
    lst = sorted(lst, key=len)  # ["if", "house", "counter"]

    # Return the last element (longest)
    return lst[-1]  # Returns "counter"

# CAS DE TEST :
# Même cas de test que ci-dessus, demonstrating sorted approach
lst = ["house", "counter", "if"]
print(largest_elememt(lst))  # Sortie : counter

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires removing duplicate elements from a list while
# preserving the order of first occurrence. La fonction doit prendre a list
# and return a new list containing only unique elements. However, the current
# solution has a bug - it returns early when it finds the first duplicate,
# which doesn't fully remove all duplicates from the list.
#
# Prérequis Clés :
# - Function must accept a list as input
# - Function must return a list with duplicates removed
# - Original order of first occurrence should be maintained
#
# Exemple d'Entrée/Sortie :
# - remove_duplicates(["tree", "kiss", "tree"]) should return ["tree", "kiss"]
# - remove_duplicates([1, 2, 2, 3, 1]) should return [1, 2, 3]
#
# Remarque : The current solution has a bug - it returns early on first duplicate.
# ============================================================================
"""
Problème 66 :
Écrivez un programme Python à remove les doublons de une liste. demander le utilisateur à saisir une liste d'éléments.
"""

# EXPLICATION DE LA SOLUTION (BUGGY VERSION):
# ATTENTION : This solution has a critical bug! It returns immediately when
# it finds the first duplicate, which means it doesn't process the entire
# list. It should continue through all elements and only return at the end.
def remove_duplicates(elements):
    duplicates = []  # List to store unique elements (misleading variable name)

    # Iterate through each element
    for element in elements:
        # Check if element already in list
        if element in duplicates:
            # BUG: Returns immediately on first duplicate!
            # Should continue processing, not return here
            return duplicates  # Returns partial list with first duplicate found
        # Add element to list if not seen before
        duplicates.append(element)  # Add first occurrence
    # This line is unreachable if there are any duplicates
    return None  # Returns None if no duplicates found

# CAS DE TEST :
# This test attempts to remove duplicates from ["tree", "kiss", "tree"]
# Expected: ["tree", "kiss"]
# Actual: ["tree"] (BUG! Returns early when "tree" is found again)
lst = ["tree", "kiss", "tree"]
print(remove_duplicates(lst))  # Sortie : ['tree'] (INCORRECT!)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires determining if a year is a leap year. A leap year
# occurs every 4 years, except for years divisible by 100, unless they're
# also divisible by 400. This is the Gregorian calendar rule for leap years.
#
# Prérequis Clés :
# - Program must prompt user for a year
# - Must check leap year rules:
#   1. Divisible by 4 AND not divisible by 100, OR
#   2. Divisible by 400
# - Should return True if leap year, False otherwise
#
# Exemple d'Entrée/Sortie :
# - 2000 is a leap year (divisible by 400)
# - 1900 is NOT a leap year (divisible by 100 but not 400)
# - 2004 is a leap year (divisible by 4, not by 100)
# - 2001 is NOT a leap year (not divisible by 4)
#
# Algorithm: Check (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
# ============================================================================
"""
Problem: 67
Write a Python program to check if a given year is a leap year. Prompt the user to enter a year.

# EXPLICATION DE LA SOLUTION :
# This solution implements the standard leap year algorithm. It checks if the
# year is divisible by 4 (but not 100) OR divisible by 400. This correctly
# handles all edge cases including century years.
def is_leap_year():
    # Get year from user
    year = int(input("Enter a year: "))  # e.g., 2000

    # Check leap year conditions:
    # 1. Divisible by 4 AND not divisible by 100, OR
    # 2. Divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        # Year is a leap year
        return True  # Return True for leap year
    else:
        # Year is not a leap year
        return False  # Return False for non-leap year

# CAS DE TEST :
# This test checks if a user-entered year is a leap year
# Examples: 2000 → True, 1900 → False, 2004 → True, 2001 → False
print(is_leap_year())  # Prompts user and prints result

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires calculating the length of a string without using
# Python's built-in len() function. The program should manually count
# characters by iterating through the string and incrementing a counter.
# Cela démontre how len() works internally.
#
# Prérequis Clés :
# - Program must prompt user for a string
# - Must calculate length without using len()
# - Should count each character in the string
# - Should display the count
#
# Exemple d'Entrée/Sortie :
# - If user enters "hello", output: 5
# - If user enters "Jonathan", output: 8
# - If user enters "", output: 0
#
# Remarque : The current solution removes spaces first, which may not match
# the problem requirement (should count all characters including spaces).
# ============================================================================
"""
Problem: 68
Write a Python program to find the length of a string without using the built-in len() function. Prompt the user to enter a string.

# EXPLICATION DE LA SOLUTION :
# This solution manually counts characters by iterating through the string
# and incrementing a counter. Remarque : It removes spaces first, which may not
# be required by the problem (should count all characters including spaces).
def length_string():
    # Get string from user and remove spaces (may not be required)
    user = input("entre string: ").replace(" ", "")  # "hello world" → "helloworld"
    count = 0  # Initialize character counter

    # Iterate through each character
    for char in user:
        count += 1  # Increment counter for each character
    print(count)  # Display the total count

length_string()  # Call the function

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires checking if a string is a palindrome without using
# built-in functions. However, the current solution uses string slicing [::-1],
# which is technically a built-in operation. A truly manual approach would
# compare characters from both ends without using slicing. A palindrome reads
# the same forwards and backwards (e.g., "racecar", "level").
#
# Prérequis Clés :
# - Program must check if string is a palindrome
# - Should not use built-in functions (ideally)
# - Should return True if palindrome, False otherwise
#
# Exemple d'Entrée/Sortie :
# - palindrome("racecar") should return True
# - palindrome("juju") should return False (juju != ujuj)
# - palindrome("level") should return True
#
# Remarque : The current solution uses [::-1] which is a built-in operation.
# A truly manual approach would compare characters from start and end.
# ============================================================================
"""
Promblem: 69
Write a Python program to check if a string is a palindrome without using any built-in functions. Prompt the user to enter a string.

# EXPLICATION DE LA SOLUTION (Uses Slicing):
# This solution uses string slicing [::-1] to reverse the string, which
# is technically a built-in operation. While it works, it doesn't fully
# satisfy "without using any built-in functions". A truly manual approach
# would compare characters from both ends using indices.
def palindrome(string):
    # Compare string with its reverse using slicing [::-1]
    if string == string[::-1]:  # "juju" == "ujuj"? No
        return True  # Return True if palindrome
    return False  # Return False if not palindrome

# CAS DE TEST :
# This test checks if "juju" is a palindrome
# "juju" == "ujuj"? No → False
word = "juju"
print(palindrome(word))  # Sortie : False

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires counting the occurrences of EACH word in a sentence,
# meaning it should return a dictionary or similar structure showing how many
# times each word appears. However, the current solution only counts the total
# number of words, not the occurrences of each individual word. This doesn't
# match the problem requirement.
#
# Prérequis Clés :
# - Program must prompt user for a sentence
# - Must count occurrences of EACH word (not total word count)
# - Should return word frequencies (e.g., {"Jonathan": 1, "is": 1, "the": 1, "best": 1})
#
# Exemple d'Entrée/Sortie :
# - count_each_word("Jonathan is the best") should return {"Jonathan": 1, "is": 1, "the": 1, "best": 1}
# - count_each_word("hello hello world") should return {"hello": 2, "world": 1}
#
# Remarque : The current solution only counts total words, not per-word occurrences.
# ============================================================================
"""
Problem: 70
Write a Python program to count the occurrences of each word in a given sentence. Prompt the user to enter a sentence.

# EXPLICATION DE LA SOLUTION (Incorrect - Counts Total Words):
# ATTENTION : This solution doesn't match the problem requirement! It counts the
# total number of words in the sentence, not the occurrences of each word.
# The problem asks for "occurrences of each word", which implies a dictionary
# showing how many times each word appears.
def count_each_word(sentence):
    count = 0  # Counter for total words (WRONG - should count per word)
    # Split sentence into words
    split_word = sentence.split()  # "Jonathan is the best" → ["Jonathan", "is", "the", "best"]

    # Count total number of words
    for word in split_word:
        count += 1  # Increments for each word: 1, 2, 3, 4
    return count  # Returns 4 (total words, not per-word occurrences)

# CAS DE TEST :
# This test counts words in "Jonathan is the best"
# Expected: Dictionary with word counts
# Actual: 4 (total word count - INCORRECT!)
lst = "Jonathan is the best"
print(count_each_word(lst))  # Sortie : 4 (WRONG - should be a dictionary!)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires finding the second largest number in a list. The
# function should sort the list (or remove duplicates first), then return
# the second largest value. This is useful for finding runner-up values and
# statistical analysis.
#
# Prérequis Clés :
# - Program must prompt user for a list of numbers
# - Must find the second largest number
# - Should handle duplicates (typically, duplicates are considered)
# - Should handle edge cases (lists with < 2 elements)
#
# Exemple d'Entrée/Sortie :
# - second_largest([56, 700, 1, 57, 78, 787, 5, 88]) should return 700
# - second_largest([1, 2, 3, 4, 5]) should return 4
# - second_largest([5, 5, 5]) should return 5 (if duplicates allowed) or handle appropriately
#
# Algorithm: Sort list, return second element (or handle duplicates first).
# ============================================================================
"""
Problem: 71
Write a Python program to find the second largest number in a list. Prompt the user to enter a list of numbers.

# EXPLICATION DE LA SOLUTION (Removes Duplicates First):
# This solution removes duplicates using set(), then sorts and returns the
# second largest. This approach treats duplicates as one value, so [5,5,5]
# would have no second largest. This may or may not match the problem intent.
def sec_lar():
    # Get user input and convert to list of integers
    numbers = list(map(int, input("type: ").split()))  # "56 700 1 57 78 787 5 88" → [56, 700, ...]
    # Remove duplicates using set
    unique_numbers = list(set(numbers))  # Removes duplicates
    # Sort in ascending order
    unique_numbers.sort()  # Sorts the unique numbers

    # Return second largest (second from end)
    print(unique_numbers[-2])  # Prints the second largest

sec_lar()  # Call the function

# CORRECT EXPLICATION DE LA SOLUTION (Keeps Duplicates):
# This solution keeps duplicates and finds the second largest value. It
# sorts in descending order and returns the second element. It also handles
# edge cases where the list has fewer than 2 elements.
def second_largest_number(numbers):
    # Sort in descending order
    sorted_numbers = sorted(numbers, reverse=True)  # [787, 700, 88, 78, 57, 56, 5, 1]

    # Check if list has at least 2 elements
    if len(sorted_numbers) > 1:
        return sorted_numbers[1]  # Return second element (700)
    else:
        return None  # Return None if list too short

# CAS DE TEST :
# This test finds second largest in [56, 700, 1, 57, 78, 787, 5, 88]
# Sorted descending: [787, 700, 88, 78, 57, 56, 5, 1]
# Second largest: 700
arg = [56, 700, 1, 57, 78, 787, 5, 88]
print(second_largest_number(arg))  # Sortie : 700

# ALTERNATIVE EXPLICATION DE LA SOLUTION (Inefficient Loop):
# This solution has an unnecessary loop that always returns on the first
# iteration. The loop doesn't serve any purpose - it just returns immediately.
def second_largest_number(numbers):
    sorted_numbers = sorted(numbers, reverse=True)  # Sort descending

    # BUG: Loop always returns on first iteration - unnecessary!
    for number in sorted_numbers:
        return sorted_numbers[1]  # Always returns second element immediately
    return None  # Unreachable if list is non-empty

# CAS DE TEST :
# Same test case, demonstrating inefficient but functional approach
arg = [56, 700, 1, 57, 78, 787, 5, 88]
print(second_largest_number(arg))  # Sortie : 700

# ALTERNATIVE EXPLICATION DE LA SOLUTION (Ascending Sort):
# This solution sorts in ascending order and returns the second-to-last
# element. It's functionally identical to the descending sort approach.
def second_largest_number(numbers):
    # Sort in ascending order
    sorted_numbers = sorted(numbers)  # [1, 5, 56, 57, 78, 88, 700, 787]

    # Unnecessary loop (always returns immediately)
    for number in sorted_numbers:
        # Return second-to-last element (second largest)
        return sorted_numbers[-2]  # Returns 700
    return None  # Unreachable

# CAS DE TEST :
# Same test case, demonstrating ascending sort approach
arg = [56, 700, 1, 57, 78, 787, 5, 88]
print(second_largest_number(arg))  # Sortie : 700

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires validating whether a given string is a valid email
# address. An email address typically has the format: local@domain.extension
# where local can contain letters, numbers, and certain special characters,
# and domain must have at least one dot separating the domain name from the
# extension (TLD). The program should use validation rules to check if the
# email format is correct.
#
# Prérequis Clés :
# - Program must prompt user for an email address
# - Must validate email format (local@domain.extension)
# - Should check for required components (@ symbol, domain, TLD)
# - Should return True if valid, False otherwise
#
# Exemple d'Entrée/Sortie :
# - "user@example.com" → True (valid email)
# - "invalid.email" → False (missing @)
# - "@example.com" → False (missing local part)
# - "user@.com" → False (invalid domain)
#
# Algorithm: Use regex pattern matching or manual validation of components.
# ============================================================================
"""
Problem: 72
Write a Python program to check if a given string is a valid email address. Prompt the user to enter an email address.

# EXPLICATION DE LA SOLUTION (Using Regular Expressions):
# This solution uses Python's `re` module with a regular expression pattern
# to validate email addresses. The regex pattern checks for the standard
# email format: local part (alphanumeric + special chars) @ domain.extension
import re

def is_valid_email(email):
    """
    Checks if the given email address is valid.

    Args:
        email (str): The email address to be validated.

    Returns:
        bool: True if the email address is valid, False otherwise.
    """
    # Regular expression pattern for a valid email address
    # Pattern breakdown:
    # ^[a-zA-Z0-9._%+-]+  - Local part: letters, digits, dots, underscores, %, +, -
    # @                    - Required @ symbol
    # [a-zA-Z0-9.-]+       - Domain name: letters, digits, dots, hyphens
    # \.                   - Required dot before TLD
    # [a-zA-Z]{2,}$        - TLD: at least 2 letters
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    # Check if the email matches the pattern
    if re.match(pattern, email):  # re.match checks from start of string
        return True  # Email matches pattern
    else:
        return False  # Email doesn't match pattern

def main():
    # Prompt the user to enter an email address
    email = input("Enter an email address: ")  # e.g., "user@example.com"

    # Check if the email is valid
    if is_valid_email(email):
        print("Email address is valid.")  # Display success message
    else:
        print("Email address is invalid.")  # Display error message

main()  # Call the main function

# ALTERNATIVE EXPLICATION DE LA SOLUTION (Manual Validation):
# This solution manually validates email components without regex. It checks
# for the @ symbol, splits the email into local and domain parts, and
# validates each component separately. This is more verbose but doesn't
# require regex knowledge.
def is_valid_email():
    # Get email from user
    email = input("Enter an email address: ")

    # Check for basic requirements: @ and . must be present
    if '@' not in email or '.' not in email:
        return False  # Missing required symbols

    # Split email into local and domain parts
    local, domain = email.split('@', 1)  # Split at first @ only

    # Validate local part (must not be empty)
    if not local:
        return False  # Local part is empty

    # Validate domain part
    if '.' not in domain or domain.startswith('.') or domain.endswith('.'):
        return False  # Domain must have dot, not start/end with dot

    # Split domain into parts and check each part
    domain_parts = domain.split('.')  # Split domain by dots
    if any(not part for part in domain_parts):  # Check if any part is empty
        return False  # Empty domain part found

    return True  # All validations passed

print(is_valid_email())  # Call function and print result

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires calculating the factorial of a number using recursion.
# The factorial of n (n!) is the product of all positive integers from 1 to n.
# By definition, 0! = 1 and 1! = 1. The recursive approach breaks down the
# problem: n! = n × (n-1)!, with base cases for n=0 and n=1.
#
# Prérequis Clés :
# - Program must prompt user for a number
# - Must use recursion (function calls itself)
# - Should calculate n! = n × (n-1) × (n-2) × ... × 2 × 1
# - Should handle edge cases (0, 1, negative numbers)
#
# Exemple d'Entrée/Sortie :
# - factorial(5) = 5 × 4 × 3 × 2 × 1 = 120
# - factorial(3) = 3 × 2 × 1 = 6
# - factorial(0) = 1 (base case)
#
# Algorithm: Base case: if n <= 1, return 1. Otherwise: return n × factorial(n-1)
# ============================================================================
"""
Problem: 73
Write a Python program to find the factorial of a number using recursion. Prompt the user to enter a number."

# EXPLICATION DE LA SOLUTION :
# This solution uses recursion to calculate factorial. The function calls
# itself with a smaller value until it reaches the base case (n=0 or n=1),
# then returns 1. Each recursive call multiplies the current n by the result
# of factorial(n-1), building up the final product.
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1  # Stop recursion, return 1
    else:
        # Recursive case: n! = n × (n-1)!
        return n * factorial(n - 1)  # Call function with n-1
        # Example: factorial(5) = 5 × factorial(4)
        #          = 5 × 4 × factorial(3)
        #          = 5 × 4 × 3 × factorial(2)
        #          = 5 × 4 × 3 × 2 × factorial(1)
        #          = 5 × 4 × 3 × 2 × 1 = 120

def main():
    try:
        # Get number from user
        number = int(input("Enter a number: "))  # e.g., 5

        # Check for negative numbers
        if number < 0:
            print("Factorial is not defined for negative numbers.")  # Error message
        else:
            # Calculate and display factorial
            print(f"The factorial of {number} is {factorial(number)}")  # e.g., "The factorial of 5 is 120"
    except ValueError:
        # Handle invalid input (non-integer)
        print("Please enter a valid integer.")  # Error message

main()  # Call the main function

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires checking if two strings are anagrams of each other.
# Anagrams are words or phrases formed by rearranging the letters of another
# word or phrase, using all the original letters exactly once. For example,
# "listen" and "silent" are anagrams. The program should ignore case and
# spaces when comparing.
#
# Prérequis Clés :
# - Program must prompt user for two strings
# - Must check if strings are anagrams (same letters, different order)
# - Should ignore case (treat 'A' same as 'a')
# - Should ignore spaces
# - Should display whether strings are anagrams
#
# Exemple d'Entrée/Sortie :
# - "listen" and "silent" → anagrams
# - "hello" and "world" → not anagrams
# - "The Morse Code" and "Here come dots" → anagrams (after normalization)
#
# Algorithm: Normalize strings (lowercase, remove spaces), sort both, compare.
# ============================================================================
"""
Problem: 74
Write a Python program to check if two strings are anagrams of each other. Prompt the user to enter two strings

# EXPLICATION DE LA SOLUTION :
# This solution normalizes both strings by converting to lowercase and removing
# spaces, then sorts the characters of each string. If the sorted character
# lists are equal, the strings are anagrams. This works because anagrams have
# the same characters in different orders.
def are_anagrams():
    # Get two strings from user
    str1 = input("Enter the first string: ")  # e.g., "listen"
    str2 = input("Enter the second string: ")  # e.g., "silent"

    # Normalize strings: remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()  # "Listen" → "listen"
    str2 = str2.replace(" ", "").lower()  # "Silent" → "silent"

    # Sort characters and compare
    if sorted(str1) == sorted(str2):  # sorted("listen") == sorted("silent") → True
        print(f"'{str1}' and '{str2}' are anagrams.")  # Display success message
    else:
        print(f"'{str1}' and '{str2}' are not anagrams.")  # Display failure message

are_anagrams()  # Call the function

# UNRELATED FUNCTION (Palindrome Checker):
# This function checks if a string is a palindrome (reads same forwards and
# backwards). It's not related to the anagram problem but appears in the code.
def pal():
    user = input("type: ")  # Get string from user

    # Check if string equals its reverse
    if user == user[::-1]:  # Compare with reversed string
        return True  # Is palindrome
    return False  # Not palindrome

print(pal())  # Call function and print result

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires determining if a number is prime. A prime number is
# a positive integer greater than 1 that has no positive divisors other than
# 1 and itself. The program should efficiently check for primality using an
# optimized algorithm that avoids checking all divisors.
#
# Prérequis Clés :
# - Program must prompt user for a number
# - Must check if number is prime (only divisible by 1 and itself)
# - Should handle edge cases (1, 2, 3, even numbers, etc.)
# - Should display whether number is prime
#
# Exemple d'Entrée/Sortie :
# - 2, 3, 5, 7, 11, 13 → prime numbers
# - 4, 6, 8, 9, 10 → not prime (divisible by numbers other than 1 and itself)
# - 1 → not prime (by definition)
#
# Algorithm: Use optimized trial division (check up to sqrt(n), skip even numbers).
# ============================================================================
"""
Problem: 75
Write a Python program to check if a number is a prime number. Prompt the user to enter a number.

# EXPLICATION DE LA SOLUTION (Optimized Prime Check):
# This solution uses an optimized algorithm that:
# 1. Handles edge cases (n <= 1, n <= 3)
# 2. Quickly eliminates even numbers and multiples of 3
# 3. Only checks divisors up to sqrt(n) using 6k±1 pattern
# This is much more efficient than checking all numbers up to n.
def is_prime(n):
    # Edge case: numbers <= 1 are not prime
    if n <= 1:
        return False  # 1 and negative numbers are not prime

    # Edge case: 2 and 3 are prime
    if n <= 3:
        return True  # 2 and 3 are prime numbers

    # Quick check: if divisible by 2 or 3, not prime
    if n % 2 == 0 or n % 3 == 0:
        return False  # Even numbers (except 2) and multiples of 3 are not prime

    # Check divisors using 6k±1 pattern (all primes > 3 are of form 6k±1)
    # Only need to check up to sqrt(n)
    i = 5  # Start from 5 (first number of form 6k-1)
    while i * i <= n:  # Check up to sqrt(n)
        # Check if n is divisible by i or i+2 (6k-1 and 6k+1)
        if n % i == 0 or n % (i + 2) == 0:
            return False  # Found a divisor, not prime
        i += 6  # Move to next pair: 6k+5 and 6k+7
    return True  # No divisors found, number is prime

def main():
    try:
        # Get number from user
        number = int(input("Enter a number: "))  # e.g., 17

        # Check if number is prime
        if is_prime(number):
            print(f"{number} is a prime number.")  # Display success message
        else:
            print(f"{number} is not a prime number.")  # Display failure message
    except ValueError:
        # Handle invalid input (non-integer)
        print("Please enter a valid integer.")  # Error message

main()  # Call the main function

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires finding elements that appear in both lists (intersection).
# The program should identify all elements that are present in both input lists,
# regardless of their positions. Duplicates should be handled appropriately
# (typically, each common element appears once in the result).
#
# Prérequis Clés :
# - Program must prompt user for two lists
# - Must find elements present in both lists
# - Should handle duplicates appropriately
# - Should display the common elements
#
# Exemple d'Entrée/Sortie :
# - common_elements(["tree", "house", "car"], ["house", "tree", "sky"]) → ["tree", "house"]
# - common_elements([1, 2, 3], [4, 5, 6]) → [] (no common elements)
# - common_elements([1, 2, 2, 3], [2, 2, 4]) → [2] (duplicates handled)
#
# Algorithm: Can use nested loops, set intersection, or list comprehension.
# ============================================================================
"""
Problem: 76
Write a Python program to find the common elements between two lists. Prompt the user to enter two lists.

# EXPLICATION DE LA SOLUTION (Using Nested Loops):
# This solution uses nested loops to compare each element in the first list
# with each element in the second list. It adds common elements to the result
# only if they haven't been added already (to avoid duplicates). This approach
# preserves order but is less efficient for large lists (O(n×m) complexity).
def common_elements(lst1, lst2):
    result = []  # List to store common elements

    # Compare each element in first list with each element in second list
    for i in lst1:
        for j in lst2:
            # If elements match and not already in result
            if i == j and i not in result:  # Check for match and uniqueness
                result.append(i)  # Add to result
    return result  # Return list of common elements

# CAS DE TEST :
# This test finds common elements between two lists
# Common: "tree" and "house"
lst1 = ["tree", "house", "car", "rose"]
lst2 = ["house", "street", "sky", "tree"]
print(common_elements(lst1, lst2))  # Sortie : ['tree', 'house']

# ALTERNATIVE EXPLICATION DE LA SOLUTION (Using Set Intersection):
# This solution converts both lists to sets and uses set intersection to find
# common elements. This is more efficient (O(n+m) complexity) and automatically
# handles duplicates, but doesn't preserve order and requires hashable elements.
def common_elements(lst1, lst2):
    # Convert lists to sets
    set1 = set(lst1)  # {"tree", "house", "car", "rose"}
    set2 = set(lst2)  # {"house", "street", "sky", "tree"}
    # Find intersection (common elements)
    elements_commmon = set1.intersection(set2)  # {"tree", "house"}

    return elements_commmon  # Return set of common elements

# CAS DE TEST :
# Same approach with different test data
arg1 = ["tree", "grass", "flower"]
arg2 = ["grass", "flower", "river"]
print(common_elements(arg1, arg2))  # Sortie : {'grass', 'flower'}

# INTERACTIVE EXPLICATION DE LA SOLUTION :
# This solution prompts the user for input, converts to sets, and finds
# intersection. It provides user-friendly output messages.
def find_common_elements():
    # Get first list from user
    input1 = input("Enter elements of the first list, separated by spaces: ")
    list1 = input1.split()  # Split into list of strings

    # Get second list from user
    input2 = input("Enter elements of the second list, separated by spaces: ")
    list2 = input2.split()  # Split into list of strings

    # Convert to sets and find intersection
    set1 = set(list1)  # Convert to set
    set2 = set(list2)  # Convert to set
    common_elements = set1.intersection(set2)  # Find common elements

    # Display results
    if common_elements:
        print(f"Common elements between the two lists: {list(common_elements)}")  # Show common elements
    else:
        print("There are no common elements between the two lists.")  # No common elements

find_common_elements()  # Call the function

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires counting the number of uppercase letters in a string.
# The function should iterate through each character in the string and count
# how many are uppercase letters (A-Z). This is useful for text analysis and
# validation tasks.
#
# Prérequis Clés :
# - Function must accept a string as input
# - Must count uppercase letters (A-Z)
# - Should return the count as an integer
# - Should handle mixed case strings
#
# Exemple d'Entrée/Sortie :
# - count_uppercase("Hello World") → 2 (H, W)
# - count_uppercase("HELLO") → 5 (all uppercase)
# - count_uppercase("hello") → 0 (no uppercase)
#
# Algorithm: Iterate through characters, check if uppercase, increment counter.
# ============================================================================
"""
Problem: 77
Write a Python function called `count_uppercase` that takes a string as input and returns the number of uppercase letters in the string.

# EXPLICATION DE LA SOLUTION :
# This solution removes spaces first (which may not be necessary), then
# iterates through each character and checks if it equals its uppercase
# version. If a character equals its uppercase form, it's uppercase. However,
# this approach has a flaw: non-alphabetic characters (like digits, punctuation)
# also equal their "uppercase" form, so they would be incorrectly counted.
def uppercase(string):
    count = 0  # Initialize uppercase counter
    # Remove spaces (may not be necessary for counting uppercase)
    string = string.replace(" ", "")  # "Hello World" → "HelloWorld"

    # Iterate through each character
    for word in string:  # 'word' is actually a character (misleading variable name)
        # Check if character equals its uppercase version
        if word == word.upper():  # 'H' == 'H'? Yes; 'e' == 'E'? No
            count += 1  # Increment counter
    return count  # Return total count

# CAS DE TEST :
# This test counts uppercase letters in "whAtT healin Gmanbe LLike"
# Expected: 4 (A, T, G, L)
# Remarque : The current approach may incorrectly count non-alphabetic characters
sentence = "whAtT healin Gmanbe LLike"
print(uppercase(sentence))  # Sortie : count of uppercase letters

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires converting a decimal (base-10) number to binary (base-2).
# Binary numbers use only 0s and 1s. The program should take a decimal number
# and convert it to its binary representation. For example, 5 in decimal is
# 101 in binary (1×2² + 0×2¹ + 1×2⁰ = 4 + 0 + 1 = 5).
#
# Prérequis Clés :
# - Program must prompt user for a decimal number
# - Must convert decimal to binary representation
# - Should display the binary number
#
# Exemple d'Entrée/Sortie :
# - decimal_to_binary(5) → "101"
# - decimal_to_binary(10) → "1010"
# - decimal_to_binary(0) → "0"
#
# Algorithm: Use built-in bin() function or manual division-by-2 method.
# ============================================================================
"""
Problem: 78
Write a Python program to convert a decimal number to binary. Prompt the user to enter a decimal number.

# EXPLICATION DE LA SOLUTION (Using Built-in Function):
# This solution uses Python's built-in `bin()` function, which converts a decimal
# number to a binary string. The function returns a string starting with "0b",
# so we slice from index 2 to remove the prefix. This is the simplest approach.
def decimal_to_binary():
    # Get decimal number from user
    decimal_number = int(input("Enter a decimal number: "))  # e.g., 5

    # Convert to binary using built-in function
    # bin() returns string like "0b101", so slice from index 2 to remove "0b"
    binary_number = bin(decimal_number)[2:]  # "0b101"[2:] → "101"

    # Display the result
    print(f"The binary representation of {decimal_number} is {binary_number}")  # Prints: "The binary representation of 5 is 101"

decimal_to_binary()  # Call the function

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires sorting a list of numbers in ascending order (from
# smallest to largest). The program should prompt the user for a list of
# numbers, convert them to integers, sort them, and display the sorted result.
# C'est une opération fondamentale list operation.
#
# Prérequis Clés :
# - Program must prompt user for a list of numbers
# - Must sort numbers in ascending order (smallest to largest)
# - Should convert string input to integers
# - Should display the sorted list
#
# Exemple d'Entrée/Sortie :
# - sort([56, 23, 677, 6, 1]) → [1, 6, 23, 56, 677]
# - sort([10, 5, 8, 2]) → [2, 5, 8, 10]
#
# Algorithm: Use Python's sorted() function or list.sort() method.
# ============================================================================
"""
Problem: 79
Write a Python program to sort a list of numbers in ascending order. Prompt the user to enter a list of numbers.

# EXPLICATION DE LA SOLUTION (Interactive Version):
# This solution prompts the user for input, splits it into a list of strings,
# converts each to an integer, and sorts the result. It returns the sorted
# list (though the return value isn't used since main() doesn't print it).
def main():
    result = []  # List to store converted integers
    # Get user input
    user = input("enter list of numbers: ")  # e.g., "56 23 677 6 1"
    user = user.split()  # Split into list: ["56", "23", "677", "6", "1"]

    # Convert each string to integer
    for num in user:
        result.append(int(num))  # [56, 23, 677, 6, 1]
    return sorted(result)  # Return sorted list: [1, 6, 23, 56, 677]

main()  # Call function (return value not printed)

# ALTERNATIVE EXPLICATION DE LA SOLUTION (Function with Parameter):
# This solution accepts a list of numbers as a parameter, making it reusable
# and testable. It uses sorted() to create a new sorted list without modifying
# the original.
def ascending_order_numbers(numbers):
    # sorted() returns a new sorted list (doesn't modify original)
    sort_numbers = sorted(numbers)  # [56, 23, 677, 6, 1] → [1, 6, 23, 56, 677]

    return sort_numbers  # Return sorted list

# CAS DE TEST :
# This test sorts the list [56, 23, 677, 6, 1]
numbers = [56, 23, 677, 6, 1]
print(ascending_order_numbers(numbers))  # Sortie : [1, 6, 23, 56, 677]

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires generating a random integer within a specified range.
# The program should prompt the user for a lower limit and an upper limit,
# then generate and display a random number between those limits (inclusive).
# This is useful for games, simulations, and random sampling.
#
# Prérequis Clés :
# - Program must prompt user for lower and upper limits
# - Must generate a random number within the range [lower, upper] (inclusive)
# - Should display the generated random number
#
# Exemple d'Entrée/Sortie :
# - If user enters lower=1, upper=10, output: random number between 1 and 10
# - If user enters lower=100, upper=200, output: random number between 100 and 200
#
# Algorithm: Use random.randint(lower, upper) which includes both endpoints.
# ============================================================================
"""
Problem: 80
Write a Python program to generate a random number between a given range. Prompt the user to enter the lower and upper limits.

# EXPLICATION DE LA SOLUTION :
# This solution uses Python's `random` module to generate random integers.
# The `random.randint()` function generates a random integer between the lower
# and upper limits, inclusive of both endpoints. This is the standard way to
# generate random integers in a range.
import random

def generate_random_number():
    # Get lower limit from user
    lower_limit = int(input("Enter the lower limit: "))  # e.g., 1
    # Get upper limit from user
    upper_limit = int(input("Enter the upper limit: "))  # e.g., 10

    # Generate random integer between lower and upper (inclusive)
    random_number = random.randint(lower_limit, upper_limit)  # e.g., 7

    # Display the result
    print(f"The random number between {lower_limit} and {upper_limit} is: {random_number}")  # Prints: "The random number between 1 and 10 is: 7"

generate_random_number()  # Call the function

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires calculating the square root of a number. The square
# root of a number n is a value that, when multiplied by itself, equals n.
# For example, the square root of 9 is 3 (3 × 3 = 9). The program should
# prompt the user for a number and calculate its square root.
#
# Prérequis Clés :
# - Program must prompt user for a number
# - Must calculate the square root
# - Should handle floating-point numbers (decimals)
# - Should display the result
#
# Exemple d'Entrée/Sortie :
# - square_root(9) → 3.0
# - square_root(16) → 4.0
# - square_root(2) → 1.414... (approximate)
#
# Algorithm: Use exponentiation (num ** 0.5) or math.sqrt() function.
# ============================================================================
"""
Problem: 81
Write a Python program to find the square root of a number. Prompt the user to enter a number.

# EXPLICATION DE LA SOLUTION (Returns Value):
# This solution prompts the user for a number, converts it to float to handle
# decimals, then calculates the square root using exponentiation (raising to
# the power of 0.5). It returns the result, which is then printed.
def square_root():
    # Get number from user and convert to float
    num = float(input("type num: "))  # e.g., 9.0
    # Calculate square root using exponentiation
    return num ** 0.5  # 9.0 ** 0.5 = 3.0

print(square_root())  # Call function and print result

# ALTERNATIVE EXPLICATION DE LA SOLUTION (Prints Directly):
# This solution is similar but prints the result directly instead of returning
# it. Both approaches are valid, but returning allows for more flexibility.
def square_root():
    # Get number from user
    num = float(input("type num: "))  # e.g., 16.0
    # Calculate and print square root directly
    print(num ** 0.5)  # Prints: 4.0

square_root()  # Call the function

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires calculating the area of a circle. The area of a circle
# is calculated using the formula: Area = π × r², where π (pi) is approximately
# 3.14159 and r is the radius. The program should prompt the user for the radius
# and calculate the area.
#
# Prérequis Clés :
# - Program must prompt user for the radius
# - Must calculate area using formula: π × r²
# - Should handle floating-point numbers (decimals)
# - Should display the area
#
# Exemple d'Entrée/Sortie :
# - If user enters radius=5, area ≈ 78.54 (π × 5² = 25π ≈ 78.54)
# - If user enters radius=10, area ≈ 314.16 (π × 10² = 100π ≈ 314.16)
#
# Formula: Area = π × radius²
# ============================================================================
"""
Problem: 82
Write a Python program to find the area of a circle. Prompt the user to enter the radius.

# EXPLICATION DE LA SOLUTION (Simple Version):
# This solution uses Python's math module to access the pi constant, prompts
# for the radius, calculates the area using the formula, and prints the result.
import math

def circle():
    # Get radius from user
    radius = float(input("type number: "))  # e.g., 5.0
    # Calculate area: π × r²
    area = math.pi * radius ** 2  # math.pi × 5² = 25π ≈ 78.54
    print(area)  # Display the area

circle()  # Call the function

# ALTERNATIVE EXPLICATION DE LA SOLUTION (Formatted Output):
# This solution is similar but provides more user-friendly output with
# formatted decimal places (2 decimal places) and a descriptive message.
def calculate_circle_area():
    # Get radius from user
    radius = float(input("Enter the radius of the circle: "))  # e.g., 10.0
    # Calculate area
    area = math.pi * radius ** 2  # π × 10² = 100π ≈ 314.16
    # Display with formatting (2 decimal places)
    print(f"The area of the circle with radius {radius} is {area:.2f}")  # Prints: "The area of the circle with radius 10.0 is 314.16"

calculate_circle_area()  # Call the function

# ALTERNATIVE EXPLICATION DE LA SOLUTION (Modular Design):
# This solution separates the calculation into a reusable function and uses
# a main() function for the interactive part. This is better for testing and
# reusability. The `if __name__ == "__main__"` check allows the file to be
# imported as a module without running the interactive code.
import math

def calculate_circle_area(radius):
    # Calculate and return area
    return math.pi * radius ** 2  # Returns area value

def main():
    # Get radius from user
    radius = float(input("Enter the radius of the circle: "))
    # Calculate area using function
    area = calculate_circle_area(radius)  # Call calculation function
    # Display result
    print(f"The area of the circle with radius {radius} is {area:.2f}")

# Only run main() if script is executed directly (not imported)
if __name__ == "__main__":
    main()  # Call main function

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires checking if a string is a palindrome using a recursive
# function. However, the current solution doesn't actually use recursion - it
# uses string slicing. A true recursive approach would compare the first and
# last characters, then recursively check the substring. A palindrome reads
# the same forwards and backwards (e.g., "racecar", "level").
#
# Prérequis Clés :
# - Program must prompt user for a string
# - Should check if string is a palindrome (ideally using recursion)
# - Should handle case-insensitivity and spaces
# - Should display whether string is a palindrome
#
# Exemple d'Entrée/Sortie :
# - "racecar" → palindrome
# - "hello" → not palindrome
# - "A man a plan" → palindrome (after normalization)
#
# Remarque : Current solution uses slicing, not true recursion.
# ============================================================================
"""
Problem: 83
Write a Python program to check if a given string is a palindrome using a recursive function. Prompt the user to enter a string.

# EXPLICATION DE LA SOLUTION (Uses Slicing, Not True Recursion):
# This solution normalizes the string and compares it with its reverse using
# slicing. While it works, it doesn't actually use recursion as the problem
# requests. A true recursive solution would compare first/last characters
# and recursively check the middle substring.
def is_palindrome(s):
    # Normalize string: remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()  # "Race Car" → "racecar"
    # Compare string with its reverse using slicing
    return s == s[::-1]  # "racecar" == "racecar" → True

def main():
    # Get string from user
    user_input = input("Enter a string: ")  # e.g., "racecar"

    # Check if palindrome
    if is_palindrome(user_input):
        print(f"{user_input} is a palindrome.")  # Display success message
    else:
        print(f"{user_input} is not a palindrome.")  # Display failure message

# Only run if script is executed directly
if __name__ == "__main__":
    main()  # Call main function

"""
Problem: 84
Write a Python program to check if a string is a pangram. A pangram is a sentence that contains every letter of the alphabet at least once. Prompt the user to enter a sentence.

# Checks if sentence contains all 26 letters of the alphabet
def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sentence = sentence.lower()  # Convert to lowercase for case-insensitive check
    for char in alphabet:
        if char not in sentence:  # If any letter is missing, not a pangram
            return "not pangram"
    return "is pangram"  # All letters found

sentence = input("Enter a sentence: ")
print(is_pangram(sentence))

# Alternative version with same logic
def pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sentence = sentence.lower()
    for char in alphabet:
        if char not in sentence:
            return "not pangram"
    return "pangram"

sentence = "abcdefghijklmnopqrstuvwxyz"
print(pangram(sentence))

"""
Problem: 85
Write a Python program to find the GCD (Greatest Common Divisor) of two numbers. Prompt the user to enter two numbers.

# Euclidean algorithm: repeatedly replace (a, b) with (b, a % b) until b == 0
def gcd(a, b):
    while b != 0:
        a, b = b, a % b  # Tuple unpacking: assigns b to a, and a % b to b simultaneously
    return a

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    result = gcd(num1, num2)
    print(f"The GCD of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()

"""
Problem: 86
Write a Python program to find the LCM (Least Common Multiple) of two numbers. Prompt the user to enter two numbers.

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# LCM formula: LCM(a, b) = |a * b| / GCD(a, b)
def lcm(a, b):
    return abs(a * b) // gcd(a, b)  # abs() handles negative numbers, // is integer division

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    result_lcm = lcm(num1, num2)

    print(f"The LCM of {num1} and {num2} is: {result_lcm}")

if __name__ == "__main__":
    main()

"""
Problem: 87
Write a Python program to reverse a list without using the reverse() function. Prompt the user to enter a list of elements.

# Uses slicing [::-1] to reverse (though this uses built-in slicing)
def reverse_lst():
    user = input("Type a list: ")
    split_lst = user.split()
    reversed_lst = []

    for item in split_lst[::-1]:  # [::-1] reverses the list
        reversed_lst.append(item)
    return " ".join(reversed_lst)

print(reverse_lst())

# Manual reversal using range() with negative step
def reverse_list():
    user_input = input("Enter a list: ")
    elements = user_input.split()
    reversed_elements = []

    # range(start, stop, step): start from last index, go to -1 (exclusive), step -1
    for i in range(len(elements) - 1, -1, -1):
        reversed_elements.append(elements[i])

    return f"Reversed list: {reversed_elements}"

print(reverse_list())

# Same approach, prints directly
def reverse_list():
    user_input = input("Enter list: ")
    elements = user_input.split()
    reversed_elements = []

    for i in range(len(elements) - 1, -1, -1):
        reversed_elements.append(elements[i])

    print("Reversed list:", reversed_elements)

reverse_list()

# Function version that takes list as parameter
def reverse_list(items):
    reverse_items = []

    for item in range(len(items)-1,-1,-1):
        reverse_items.append(items[item])
    return reverse_items

lst = ["apple", "banana", "friend"]
print(reverse_list(lst))

"""
Problem: 88
Write a Python program to find the prime factors of a number. Prompt the user to enter a number.

# Finds all prime factors by repeatedly dividing by smallest possible divisor
def prime_factors(n):
    factors = []
    divisor = 2  # Start with smallest prime
    while n > 1:
        while n % divisor == 0:  # While n is divisible by divisor
            factors.append(divisor)
            n //= divisor  # Integer division: divide n by divisor
        divisor += 1  # Try next divisor

    return factors

def main():
    number = int(input("Enter a number: "))
    if number < 2:
        print("Prime factors are only defined for numbers greater than or equal to 2.")
    else:
        result = prime_factors(number)
        print(f"The prime factors of {number} are: {result}")

if __name__ == "__main__":
    main()

# ============================================================================
# EXPLICATION DU PROBLÈME :
# generate a random password of a given length. Prompt the user to enter the length.
#
# Prérequis Clés :
# - Program must prompt user for input
# - Function must accept appropriate parameters
# - Function must return the expected result
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses iteration to process elements.
# ============================================================================
"""
Problème 89 :
Écrivez un programme Python à générer un aléatoire password de une donnée longueur. demander le utilisateur à saisir la longueur.
"""

import random
import string

# Generates random password using letters, digits, and punctuation
def generate_password(length):
    # Function definition
    characters = string.ascii_letters + string.digits + string.punctuation  # All printable ASCII chars
    # Generator expression: creates random.choice() for each iteration, join() combines into string
    password = ''.join(random.choice(characters) for i in range(length))
        # Joins list elements into string

    return password
        # Returns the result

length = int(input("Enter the length of the password: "))
    # Gets user input
print("Generated password:", generate_password(length))


# ============================================================================
# EXPLICATION DU PROBLÈME :
# count the number of words in a sentence. Prompt the user to enter a sentence.
#
# Prérequis Clés :
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must handle numeric values
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses iteration to process elements.
# ============================================================================
"""
Problem: 90:
Write a Python program to count the number of words in a sentence. Prompt the user to enter a sentence.

# Counts words by splitting on whitespace and counting elements
def count_words(sentence):
    # Function definition
    split_words = sentence.split()  # split() splits on whitespace by default
    count = 0
    for word in split_words:
        # Iterates through each element
        count += 1
    return count
    # Remarque : Could also use len(split_words) instead of loop

words = "Jonathan is the best ever"
print(count_words(words))


# ============================================================================
# EXPLICATION DU PROBLÈME :
# find the largest and smallest elements in a list. Prompt the user to enter a list of numbers without using sorted()."
#
# Prérequis Clés :
# - Program must prompt user for input
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
# - Must handle numeric values
# - Must sort elements in the specified order
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses recursion to solve the problem.
# ============================================================================
"""
Problème 91 :
Écrivez un programme Python à trouver le plus grand et plus petit éléments dans une liste. demander le utilisateur à saisir une liste de nombres sans en utilisant trié()."
"""

# Single-pass algorithm: finds both min and max in one iteration
def largest_smallest(elements):
    # Function definition
    smallest = elements[0]  # Initialize with first element
    largest = elements[0]
    for element in elements:
        # Iterates through each element
        if element < smallest:
            smallest = element
        if element > largest:
            largest = element
    return smallest, largest  # Returns tuple (smallest, largest)

lst = [4, 5, 100, 6, 1, 10]
print(largest_smallest(lst))

"""
Problem: 92
Write a Python program to check if a number is a perfect number. A perfect number is a positive integer that is equal to the sum of its proper divisors. Prompt the user to enter a number.

# BUGGY: This function name says "perfect_square" but checks perfect number incorrectly
def is_perfect_square(num):
    # Function definition
    if num <= 0:
        return False
            # Returns the result
    sum_divisor = 0
    for i in range(1, num + 1):  # Includes num itself (should only check proper divisors)
        if num % i == 0:
            # Checks condition
            sum_divisor += i
            if sum_divisor == num:  # Checks during loop, not at end
                return True
                    # Returns the result
    return False
        # Returns the result
is_perfect_square(6)

# CORRECT: Perfect number = sum of proper divisors (excluding the number itself)
def is_perfect_number(n):
    # Function definition
    if n <= 0:
        return False
            # Returns the result

    sum_of_divisors = 0
    for i in range(1, n):  # Only check divisors less than n (proper divisors)
        if n % i == 0:
            # Checks condition
            sum_of_divisors += i

    return sum_of_divisors == n  # Check if sum equals the number

def main():
    # Function definition
    number = int(input("Enter a number: "))
        # Gets user input

    if is_perfect_number(number):
        print(f"{number} is a perfect number.")
    else:
        print(f"{number} is not a perfect number.")

if __name__ == "__main__":
    # Checks condition
    main()


# ============================================================================
# EXPLICATION DU PROBLÈME :
# find the factorial of a number using a loop. Prompt the user to enter a number.
#
# Prérequis Clés :
# - Program must prompt user for input
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must handle numeric values
# - Must calculate factorial (n! = n × (n-1) × ... × 2 × 1)
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses recursion to solve the problem.
# ============================================================================
"""
Problème 93 :
Écrivez un programme Python à trouver la factorielle de un nombre en utilisant une boucle. demander le utilisateur à saisir un nombre.
"""

# Iterative factorial: multiply all numbers from 1 to n
def factorial():
    # Function definition
    user = int(input("type number: "))
        # Gets user input
    result = 1  # Start with 1 (multiplicative identity)
    for number in range(1, user + 1):  # range(1, n+1) gives 1, 2, 3, ..., n
        result *= number  # Multiply: 1 × 2 × 3 × ... × n

    print(result)

factorial()

# BUGGY: Always multiplies by 1 instead of the number
def factorial():
    # Function definition
    user = int(input("type number: "))
        # Gets user input
    result = 1
    for number in range(1, user + 1):
        # Iterates through each element
        result *= 1  # BUG: Should be result *= number
    return result
        # Returns the result

print(factorial())

"""
Problem: 94
Write a Python program to check if a given number is a power of two.

# Checks if number can be repeatedly divided by 2 until reaching 1
def is_power_of_two(number):
    # Function definition
    if number <= 0:
        return False
            # Returns the result
    while number != 1:
        if number % 2 != 0:  # If not divisible by 2, not a power of 2
            return False
                # Returns the result
        number = number // 2  # Integer division: divide by 2
    return True  # Reached 1, so it's a power of 2

number = int(input("Enter a number: "))
    # Gets user input
if is_power_of_two(number):
    print(f"{number} is a power of two.")
else:
    print(f"{number} is not a power of two.")

"""
Problem: 95
Write a Python program to find the intersection of two lists. Prompt the user to enter two lists.
def get_list(prompt):
    # Function definition
    return input(prompt).split()
        # Gets user input

# Uses set intersection: convert lists to sets, find intersection with & operator
def find_intersection(list1, list2):
    # Function definition
    return list(set(list1) & set(list2))  # & is set intersection operator

def main():
    # Function definition
    list1 = get_list("Enter the first list of elements, separated by spaces: ")
    list2 = get_list("Enter the second list of elements, separated by spaces: ")

    intersection = find_intersection(list1, list2)

    print(f"The intersection of the two lists is: {intersection}")

main()

# Alternative version without helper function
def find_intersection():
    # Function definition
    list1 = input("Enter lst: ").split()
        # Gets user input
    list2 = input("Enter lst: ").split()
        # Gets user input
    intersection = list(set(list1) & set(list2))

    print(f"The intersection of the two lists is: {intersection}")

print(find_intersection())


# ============================================================================
# EXPLICATION DU PROBLÈME :
# remove vowels from a string. Prompt the user to enter a string.
#
# Prérequis Clés :
# - Program must prompt user for input
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with strings
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses recursion to solve the problem.
# ============================================================================
"""
Problème 96 :
Écrivez un programme Python à remove voyelles de une chaîne. demander le utilisateur à saisir une chaîne.
"""

# Prints non-vowel characters directly (doesn't return string)
def remove_vowels():
    # Function definition
    user = input("type string: ")
        # Gets user input
    for char in user:
        # Iterates through each element
        if char not in "aeiou":  # Only checks lowercase vowels
            print(char, end= "")  # end="" prevents newline after each char

remove_vowels()

# Returns string with vowels removed, but joins with newlines (likely bug)
def remove_vowels(string):
    # Function definition
    new_name = []
    for char in string:
        # Iterates through each element
        if char not in "aeiou":
            new_name.append(char)
    return "\n".join(new_name)  # Joins with newlines instead of empty string

name = "Jonathan"
print(remove_vowels(name))

"""
Problem: 97
Write a Python program to convert a binary number to decimal. Prompt the user to enter a binary number.

# Converts binary to decimal: each '1' bit contributes 2^position
def binary_to_decimal(binary):
    # Function definition
    decimal = 0
    power = len(binary) - 1  # Start with highest power (leftmost bit)
    for digit in binary:
        # Iterates through each element
        if digit == '1':
            # Checks condition
            decimal += 2 ** power  # Add 2^power for each '1' bit
        power -= 1  # Decrease power for next position

    return decimal
        # Returns the result

def main():
    # Function definition
    binary_number = input("Enter a binary number: ")
    # all() with generator expression: checks if all bits are '0' or '1'
    if all(bit in '01' for bit in binary_number):
        decimal_number = binary_to_decimal(binary_number)
        print(f"The decimal equivalent of {binary_number} is {decimal_number}.")
    else:
        print("Invalid binary number. Please enter a valid binary number (consisting of 0s and 1s).")

if __name__ == "__main__":
    # Checks condition
    main()

"""
Problem: 98
Write a Python program to find the sum of the digits in a string. Prompt the user to enter a string containing seperate numbers. eg "2", "8" should return 10
    # Returns the result

# Sums space-separated numbers in a string
def digits_string():
    # Function definition
    user = input("Type numbers separated by spaces: ").split()  # Split into list of strings
    total = 0
    for number in user:
        # Iterates through each element
        total += int(number)  # Convert to int and add

    print(total)

digits_string()

# Alternative: converts all to int first, then sums
def digits_string():
    # Function definition
    user = input("type numbers: ").split()
        # Gets user input
    total = 0
    int_number = []
    for number in user:
        # Iterates through each element
        int_number.append(int(number))
    for number in int_number:
        # Iterates through each element
        total += number

    print(total)

digits_string()

"""
Problem: 99
Write a Python program to count the number of uppercase and lowercase letters in a string. Prompt the user to enter a string.

# Counts uppercase and lowercase letters using isupper() method
def upper_lower(string):
    # Function definition
    count_upper = 0
    count_lower = 0
    for char in string:
        # Iterates through each element
        if char.isupper():  # isupper() returns True for uppercase letters
            count_upper += 1
        else:  # Remarque : counts non-uppercase (including digits, spaces, punctuation) as lowercase
            count_lower += 1
    return f"lower = {count_lower} and upper = {count_upper}"
        # Returns the result

string = "Jonathan Noll is the Best"
print(upper_lower(string))

"""
Problem: 100
Write a Python program to find the sum of all prime numbers within a given range. Prompt the user to enter the lower and upper limits.

# Optimized prime check: only tests divisors up to sqrt(num)
def is_prime(num):
    # Function definition
    if num <= 1:
        return False
            # Returns the result
    for i in range(2, int(num**0.5) + 1):  # int(num**0.5) + 1 rounds up sqrt
        if num % i == 0:
            # Checks condition
            return False
                # Returns the result
    return True
        # Returns the result

# Sums all primes in range [lower, upper] inclusive
def sum_of_primes(lower, upper):
    # Function definition
    total = 0
    for num in range(lower, upper + 1):  # range() upper bound is exclusive, so +1
        if is_prime(num):
            total += num
    return total
        # Returns the result

def main():
    # Function definition
    lower_limit = int(input("Enter the lower limit: "))
        # Gets user input
    upper_limit = int(input("Enter the upper limit: "))
        # Gets user input
    prime_sum = sum_of_primes(lower_limit, upper_limit)
    print(f"The sum of all prime numbers between {lower_limit} and {upper_limit} is: {prime_sum}")

if __name__ == "__main__":
    # Checks condition
    main()

"""
Problem: 101
Write a Python program to calculate the power of a number using recursion. Prompt the user to enter a base number and an exponent.

# Recursive power: base^exp = base * base^(exp-1), base case when exp == 0
def power(base, exp):
    # Function definition
    if exp == 0:  # Base case: any number to power 0 is 1
        return 1
            # Returns the result
    return base * power(base, exp - 1)  # Recursive case: multiply base by power(base, exp-1)

base = float(input("Enter the base number: "))
    # Gets user input
exp = int(input("Enter the exponent: "))
    # Gets user input

result = power(base, exp)
print(f"{base} to the power of {exp} is: {result}")


# ============================================================================
# EXPLICATION DU PROBLÈME :
# check if a string is an anagram of another string, ignoring whitespace. Prompt the user to enter two strings.
#
# Prérequis Clés :
# - Program must prompt user for input
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with strings
# - Must check if strings contain same letters in different order
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses recursion to solve the problem.
# ============================================================================
"""
Problème 102 :
Écrivez un programme Python à vérifier si une chaîne est an un anagramme de un autre chaîne, ignoring les espaces. demander le utilisateur à saisir deux strings.
"""

# Checks anagrams by comparing sorted character lists
def is_anagram():
    # Function definition
    string1 = input("type string: ").replace(" ", "")  # Remove spaces
    string2 = input("type string: ").replace(" ", "")
        # Gets user input
    sort1 = sorted(string1)  # sorted() returns list of characters
    sort2 = sorted(string2)
        # Sorts elements in ascending order

    if sort1 == sort2:  # If sorted lists are equal, strings are anagrams
        print("this is anagram")
    else:
        print("this is not anagram")

is_anagram()

# Function version that returns boolean
def is_anagram(string1, string2):
    # Function definition
    string1 = string1.replace(" ", "")
    string2 = string2.replace(" ", "")

    return sorted(string1) == sorted(string2)
        # Sorts elements in ascending order

string1 = "listen"
string2 = "silent"

print(is_anagram(string1, string2))

"""
103
Write a Python program to find the largest and smallest digits in a number. Prompt the user to enter a number.

# Remarque : Problem asks for digits in a number, but solution treats input as list of numbers
def largest_smallest():
    # Function definition
    user = input("type list of numbers: ").split()
        # Gets user input
    int_num = []
    for number in user:
        # Iterates through each element
        int_num.append(int(number))

    max_num = max(int_num)  # Built-in max() function
    min_num = min(int_num)  # Built-in min() function
    print(max_num, min_num)

largest_smallest()

"""
Problem: 104
Write a Python program to check if a number is a perfect square. Prompt the user to enter a number"

import math

# math.isqrt() returns integer square root (floor of sqrt)
user = int((input("enter number: ")))
    # Gets user input

root = math.isqrt(user)  # Integer square root
print(root * root == user)  # Perfect square if root² equals original number

# Function version
def is_perfect_square(num):
    # Function definition
    root = math.isqrt(num)  # math.isqrt() is integer square root function
    return root * root == num  # Check if squaring root gives original number

num = int(input("Enter a number: "))
    # Gets user input

if is_perfect_square(num):
    print(f"{num} is a perfect square.")
else:
    print(f"{num} is not a perfect square.")


# ============================================================================
# EXPLICATION DU PROBLÈME :
# find the sum of all odd numbers in a list. Prompt the user to enter a list of numbers.
#
# Prérequis Clés :
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
# - Must handle numeric values
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses iteration to process elements.
# ============================================================================
"""
Problème 105 :
Écrivez un programme Python à trouver le somme de tous les nombres impairs dans une liste. demander le utilisateur à saisir une liste de nombres.
"""

# Sums all odd numbers (numbers not divisible by 2)
def all_odd_numbers(numbers):
    # Function definition
    count = 0  # Variable name misleading - actually stores sum
    for number in numbers:
        # Iterates through each element
        if number % 2 != 0:  # Check if odd (remainder when divided by 2 is not 0)
            count += number  # Add odd number to sum
    return count
        # Returns the result

lst = [2, 10, 3, 7]
print(all_odd_numbers(lst))


# ============================================================================
# EXPLICATION DU PROBLÈME :
# find the sum of all odd numbers in a list. Prompt the user to enter a list of numbers.
#
# Prérequis Clés :
# - Program must prompt user for input
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
# - Must handle numeric values
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses recursion to solve the problem.
# ============================================================================
"""
Problème 106 :
Écrivez un programme Python à trouver le somme de tous les nombres impairs dans une liste. demander le utilisateur à saisir une liste de nombres.
"""

# Interactive version: converts input to integers, then sums odd numbers
def sum_of_odd_numbers():
    # Function definition
    user_input = input("Enter a list of numbers separated by spaces: ")
        # Gets user input
    split_numbers = user_input.split()
        # Splits string into list of words/elements
    int_numbers = []

    for num in split_numbers:
        # Iterates through each element
        int_numbers.append(int(num))

    odd_sum = 0
    for num in int_numbers:
        # Iterates through each element
        if num % 2 != 0:  # Check if odd
            odd_sum += num

    print("The sum of all odd numbers is:", odd_sum)

sum_of_odd_numbers()

# Alternative: converts and checks in same loop
def sum_of_all_odd():
    # Function definition
    user = input("Enter numbers separated by spaces: ").split()
        # Gets user input
    total = 0
    for number in user:
        # Iterates through each element
        number = int(number)  # Convert to int
        if number % 2 != 0:
            total += number

    print(total)

sum_of_all_odd()


# ============================================================================
# EXPLICATION DU PROBLÈME :
# find the common characters between two strings. Prompt the user to enter two strings.
#
# Prérequis Clés :
# - Program must prompt user for input
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with strings
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses recursion to solve the problem.
# ============================================================================
"""
Problème 107 :
Écrivez un programme Python à trouver le commun caractères entre deux strings. demander le utilisateur à saisir deux strings.
"""

# Finds characters that appear in both strings (preserves order of first occurrence)
def common_char():
    # Function definition
    user_input = input("Type 2 strings separated by a space: ").split()
        # Gets user input
    if len(user_input) != 2:
        print("Please enter exactly two strings.")
        return

    str1, str2 = user_input  # Tuple unpacking: assigns first two elements

    common = []
    for char in str1:
        # Iterates through each element
        if char in str2 and char not in common:  # Check if in both strings and not already added
            common.append(char)

    return common
        # Returns the result

print(common_char())

# Function version with separate inputs
def common_char(string1, string2):
    # Function definition
    characters = []
    for char in string1:
        # Iterates through each element
        if char in string2 and char not in characters:
            characters.append(char)

    return characters
        # Returns the result

name1 = input("Enter the first string: ")
    # Gets user input
name2 = input("Enter the second string: ")
    # Gets user input
print(common_char(name1, name2))

"""
Problem: 108
Write a Python program to remove duplicates from a string using set(). Prompt the user to enter a string
# Uses set to track seen characters, but order not preserved (set is unordered)
def remove_duplicates():
    # Function definition
    user = input("type string: ")
        # Gets user input
    unique_user = set()  # Set to track unique characters

    for char in user:
        # Iterates through each element
        if char not in unique_user:
            unique_user.add(char)

    print("".join(unique_user))  # join() converts set to string (order may vary)

remove_duplicates()

# Preserves order: uses set to check, list to maintain order
def remove_duplicates():
    # Function definition
    user = input("type string: ")
        # Gets user input
    unique_user = set()  # For fast lookup
    result = []  # For maintaining order

    for char in user:
        # Iterates through each element
        if char not in unique_user:
            unique_user.add(char)
            result.append(char)  # Add to list to preserve order

    print("".join(result))  # Join list to get ordered string

remove_duplicates()


"""
Problem: 109
Write a Python program to check if a number is an Armstrong number. An Armstrong number is a number that is equal to the sum of its own digits, each raised to the power of the number of digits. Prompt the user to enter a number.

# Armstrong number: sum of digits each raised to power of number of digits equals the number
# Example: 153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153
def is_armstrong(number):
    # Function definition
    digits = []
    for digit in str(number):  # Convert to string to iterate over digits
        digits.append(int(digit))  # Convert each digit back to int

    power = len(digits)  # Power is number of digits
    total = 0
    for digit in digits:
        # Iterates through each element
        total += digit ** power  # Add digit raised to power

    return total == number  # Check if sum equals original number

number = int(input("Enter a number: "))
    # Gets user input

if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")

print(number)


# ============================================================================
# EXPLICATION DU PROBLÈME :
# find the number of vowels and consonants in a string. Prompt the user to enter a string.
#
# Prérequis Clés :
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with strings
# - Must handle numeric values
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses iteration to process elements.
# ============================================================================
"""
Problème 110 :
Écrivez un programme Python à trouver le nombre de voyelles et consonnes dans une chaîne. demander le utilisateur à saisir une chaîne.
"""

# Counts vowels and consonants (treats non-vowels as consonants, including digits/punctuation)
def vowels_consonates(string):
    # Function definition
    string = string.replace(" ", "")  # Remove spaces
    vowels = "aeiou"  # Only lowercase vowels (case-sensitive)
    count_vowels = 0
    consonates = 0

    for char in string:
        # Iterates through each element
        if char in vowels:
            count_vowels += 1
        if char not in vowels:  # Remarque : counts digits, punctuation as consonants
            consonates += 1
    return f"vowels = {count_vowels}\nconsonates = {consonates}"
        # Returns the result

lst = "Jonathan is there next best thing"
print(vowels_consonates(lst))


# ============================================================================
# EXPLICATION DU PROBLÈME :
# find the second smallest element in a list.
#
# Prérequis Clés :
# - Program must prompt user for input
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses recursion to solve the problem.
# ============================================================================
"""
Problème 111 :
Écrivez un programme Python à trouver le deuxième plus petit élément dans une liste.
"""
# Finds second smallest by sorting and taking index 1
def second_smallest_element():
    # Function definition
    user_input = input("Enter numbers separated by spaces: ")
        # Gets user input
    int_numbers = []
    for num_str in user_input.split():
        # Splits string into list of words/elements
        int_numbers.append(int(num_str))

    sorted_numbers = sorted(int_numbers)  # Sort ascending

    if len(sorted_numbers) >= 2:
        return sorted_numbers[1]  # Second element (index 1)
    else:
        return "List should contain at least two numbers."
            # Returns the result

print(second_smallest_element())

# BUGGY: Uses key=len which sorts by length (for strings), not by value
def second_smallest_element(elements):
    # Function definition
    if len(elements) < 2:
        return None
            # Returns the result

    sorted_elements = sorted(elements, key=len)  # key=len sorts by length, not value

    return sorted_elements[1]  # Returns second shortest, not second smallest

arg = ["Jonathan", "hot", "sand"]
print(second_smallest_element(arg))

"""
Problem: 112
Write a Python program to generate all possible permutations of a given string. Prompt the user to enter a string.

from itertools import permutations  # itertools.permutations generates all arrangements

def generate_permutations(string):
    # Function definition
    result = []
    for p in permutations(string):  # permutations() returns tuples of characters
        result.append(''.join(p))  # join() converts tuple to string
    return result
        # Returns the result

string = input("Enter a string: ")
    # Gets user input
result = generate_permutations(string)
print("Permutations:", result)

# Alternative: using itertools directly
import itertools
string = "abcd"
result = itertools.permutations(string)  # Returns iterator

print(list(result))  # Convert iterator to list

"""
113
Define a function max() that takes two numbers as arguments and returns the largest of them. Use the if then-else construct available in Python. (It is true that Python has the max() function built in, but writing it yourself is nevertheless a good exercise.)

# Custom max function using if-else (returns formatted string, not just the number)
def max_num(num1, num2):
    # Function definition
    if num1 > num2:
        return f"This is max number:  {num1}"  # Returns string, not number
    else:
        return f"This is max number: {num2}"
            # Returns the result

num1 = 10
num2 = 20
print(max_num(num1, num2))

"""
Problem: 114
description": "Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.

# BUGGY: Takes list but initializes with 0 (fails if all numbers are negative)
def max_of_three(lst):
    # Function definition
    largest = 0  # BUG: Should initialize with lst[0] or float('-inf')
    for num in lst:
        # Iterates through each element
        if num > largest:
            largest = num
    return largest
        # Returns the result

lst = [466,45677,3]
max_of_three(lst)

# Uses built-in max() function
def main(a, b, c):
    # Function definition
    return max(a,b,c)  # Built-in max() can take multiple arguments
main(56,8,445)

# Correct: compares all three numbers using if-elif-else
def max_of_three(a, b, c):
    # Function definition
    if a >= b and a >= c:  # Check if a is largest
        return a
            # Returns the result
    elif b >= a and b >= c:  # Check if b is largest
        return b
            # Returns the result
    else:  # Otherwise c is largest
        return c
            # Returns the result

max_of_three()

"""
Problem: 115
Define a function that computes the length of a given list or string. (It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise.)

# Manual length calculation: iterate and count elements
def length_string(string):
    # Function definition
    count = 0
    for char in string:  # Iterate over characters
        count += 1
    return count
        # Returns the result

name = "Jonathan"
print(length_string(name))

# Same logic works for lists (iterates over list elements)
def length_list(string):  # Misleading name - works for lists too
    # Function definition
    count = 0
    for char in string:  # Iterates over elements (works for both strings and lists)
        count += 1
    return count
        # Returns the result

lst = ["list", "it", "all"]
print(length_list(lst))

"""
116
Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.

# Simple version: only checks lowercase vowels (case-sensitive)
def is_vowel(string):
    # Function definition
    return string in "aeiou"  # in operator checks membership

arg1 = "e"
arg2 = "h"
arg3 = "a"
print(is_vowel(arg1))
print(is_vowel(arg2))
print(is_vowel(arg3))

# More robust: validates input length, handles case-insensitivity
def is_vowel(char):
    # Function definition
    vowels = "aeiouAEIOU"
    if len(char) == 1 and char.isalpha():  # isalpha() checks if alphabetic
        return char.lower() in vowels  # Convert to lowercase for case-insensitive check
    else:
        return False
            # Returns the result

print(is_vowel('a'))
print(is_vowel('E'))
print(is_vowel('x'))
print(is_vowel('9'))
print(is_vowel(''))
print(is_vowel('aa'))

"""
Problem: 117
Write a function translate() that will translate a text into 'rövarspråket'' (Swedish for 'robber's language''). That is, double every consonant and place an occurrence of 'o'' in between. For example, translate('this is fun'') should return the string 'tothohisos isos fofunon'.
    # Returns the result

# Rövarspråket: doubles consonants with 'o' between (e.g., 't' → 'tot')
def translate(text):
    # Function definition
    vowels = "aeiouAEIOU"
    translated = ""
    for char in text:
        # Iterates through each element
        if char.isalpha() and char not in vowels:  # Check if consonant
            translated += char + 'o' + char  # Double consonant with 'o' in middle
        else:
            translated += char  # Keep vowels and non-alphabetic as-is
    return translated
        # Returns the result

text = input("Enter a text: ")
    # Gets user input
result = translate(text)
print(result)

"""
Problem: 118
Define a function calculate_sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of numbers. For example, calculate_sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.
    # Returns the result

# Custom sum function: accumulates total starting from 0
def calculate_sum(numbers):
    # Function definition
    total = 0  # Start with 0 (additive identity)
    for number in numbers:
        # Iterates through each element
        total += number
    return total
        # Returns the result

# Custom multiply function: accumulates product starting from 1
def multiply(numbers):
    # Function definition
    result = 1  # Start with 1 (multiplicative identity)
    for number in numbers:
        # Iterates through each element
        result *= number
    return result
        # Returns the result

numbers = [1, 2, 3, 4]
print("Sum:", calculate_sum(numbers))
print("Multiply:", multiply(numbers))

"""
Problem: 119
Define a function reverse() that computes the reversal of a string. For example, reverse('I am testing'') should return the string 'gnitset ma I'.
    # Returns the result

# Manual reversal: prepend each character to build reversed string
def reverse(string):
    # Function definition
    reversed_string = ""
    for char in string:
        # Iterates through each element
        reversed_string = char + reversed_string  # Prepend char (builds from right to left)
    return reversed_string
        # Returns the result

string = input("Enter a string: ")
    # Gets user input
result = reverse(string)
print(result)

"""
Problem: 120
Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards). For example, is_palindrome('radar') should return True.
    # Returns the result

# INEFFICIENT: Loop is unnecessary - comparison doesn't depend on loop variable
def palindromes(string):
    # Function definition
    for char in string:  # Loop doesn't use char variable
        if string == string[::-1]:  # Compares string with reverse (same check every iteration)
            return True
                # Returns the result
    return False
        # Returns the result

string = "radarh"
print(palindromes(string))

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function that Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards). For example, is_palindrome('radar') s.
# hould return True.
#
# Prérequis Clés :
# - Program must prompt user for input
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must check if string reads same forwards and backwards
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses recursion to solve the problem.
# ============================================================================
"""
Problème 121 :
Définissez une fonction is_palindrome() qui recognizes palindromes (c'est-à-dire. words qui look le même written backwards). par exemple, is_palindrome('radar') devrait retourner vrai.
"""
# Checks palindrome by comparing string with its reverse
def is_palindrome(string):
    # Function definition
    if string == string[::-1]:  # [::-1] reverses the string
        return True
            # Returns the result
    return False
        # Returns the result

name = "jojj"
print(is_palindrome(name))

"""
Problem: 122
Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a, and returns True if x is a member of a, False otherwise. (Note that this is exactly what the in operator does, but for the sake of the exercise you should pretend Python did not have this operator.

# Uses built-in 'in' operator (exercise asks to pretend it doesn't exist)
def is_member(lst, x):
    # Function definition
    return x in lst  # in operator checks membership

lst = [2, 5, 6]
x = 2
print(is_member(lst, x))

# Manual implementation: iterate and compare each element
def is_member(x, a):
    # Function definition
    for item in a:
        # Iterates through each element
        if item == x:  # Compare each element
            return True
                # Returns the result
    return False  # Not found

x = input("Enter a value: ")
    # Gets user input
a = input("Enter a list of values (comma-separated): ").split(',')  # split(',') splits on comma

result = is_member(x, a)
print(result)

"""
Problem: 123
Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise, you should (also) write it using two nested forloops.

# Uses nested loops to check all pairs
def overlapping(list1, list2):
    # Function definition
    for item1 in list1:
        # Iterates through each element
        for item2 in list2:
            # Iterates through each element
            if item1 == item2:  # Compare each pair
                return True  # Found common element
    return False  # No common elements

list1 = [1, 2, 3, 4]
list2 = [4, 5, 6, 7]
print(overlapping(list1, list2))

list1 = ['apple', 'banana', 'cherry']
list2 = ['date', 'elderberry', 'fig']
print(overlapping(list1, list2))

# Alternative: uses helper function is_member()
def is_member(element, lst):
    # Function definition
    for item in lst:
        # Iterates through each element
        if element == item:
            # Checks condition
            return True
                # Returns the result
    return False
        # Returns the result

def overlapping(list1, list2):
    # Function definition
    for item1 in list1:
        # Iterates through each element
        if is_member(item1, list2):  # Check if item1 is in list2
            return True
                # Returns the result
    return False
        # Returns the result

list1 = [1, 2, 3, 4]
list2 = [4, 5, 6, 7]
print(overlapping(list1, list2))

list1 = ['apple', 'banana', 'cherry']
list2 = ['date', 'elderberry', 'fig']
print(overlapping(list1, list2))


# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function that Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise. You may use your is.
# _member() function, or the in operator, but for the sake of the exercise, you should (also) write it using two nested forloops.
#
# Prérequis Clés :
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses recursion to solve the problem.
# ============================================================================
"""
Problème 124 :
Définissez une fonction overlapping() qui prend deux listes et retourne vrai si they ont at moins l'une member dans commun, False otherwise. You peut Utilisez your is_member() fonction, ou le dans operator, but pour le sake de le exercise, you devrait (aussi) write it en utilisant deux imbriqué forloops.
"""

# Uses 'in' operator (more efficient than nested loops)
def overlapping(lst1, lst2):
    # Function definition
    for element in lst1:
        # Iterates through each element
        if element in lst2:  # in operator checks membership
            return True
                # Returns the result
    return False
        # Returns the result

lst1 = [2, 4, 6, 8, 10]
lst2 = [99, 66, 66, 16]
print(overlapping(lst1, lst2))

# Uses nested loops (as exercise requires)
def overlapping(lst1, lst2):
    # Function definition
    for i in lst1:
        # Iterates through each element
        for j in lst2:
            # Iterates through each element
            if i == j:  # Compare each pair
                return True
                    # Returns the result
    return False
        # Returns the result

lst1 = [2, 4, 6, 8, 10]
lst2 = [99, 66, 66, 16]
print(overlapping(lst1, lst2))

"""
Problem: 125
Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:

# Prints histogram: each number becomes that many asterisks
def histogram(numbers):
    # Function definition
    for number in numbers:
        # Iterates through each element
        print('*' * number)  # String multiplication: '*' * 4 = '****'

histogram([4, 9, 7])

# Same logic, different variable name
def histogram(numbers):
    # Function definition
    for number in numbers:
        # Iterates through each element
        print('*' * number)

numbers = [4, 9, 7]
histogram(numbers)

# Returns string instead of printing (typo in function name: "histrogram")
def histrogram(numbers):
    # Function definition
    result = ""
    for number in numbers:
        # Iterates through each element
        result += "*" * number + "\n"  # Build string with newlines
    return result
        # Returns the result

numbers = [2, 4, 8]
print(histrogram(numbers))


# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires writing a program that Write a program that maps a list of words into a list of integers representing the lengths of the correponding words..
#
# Prérequis Clés :
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
# - Must handle numeric values
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses iteration to process elements.
# ============================================================================
"""
Problème 126 :
Écrivez un programme qui maps une liste de mots dans une liste d'entiers representing le lengths de le correponding words.
"""

# Maps each word to its length (could use list comprehension: [len(word) for word in words])
def map_words_to_lengths(words):
    # Function definition
    lengths = []
    for word in words:
        # Iterates through each element
        lengths.append(len(word))  # Append length of each word
    return lengths
        # Returns the result

words = ["apple", "banana", "cherry", "date"]
lengths = map_words_to_lengths(words)
print(lengths)


# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function that Write a function find_longest_word() that takes a list of words and returns the length of the longest one..
#
# Prérequis Clés :
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses iteration to process elements.
# ============================================================================
"""
Problème 127 :
Écrivez une fonction find_longest_word() qui prend une liste de mots et retourne la longueur de le plus long l'une.
"""

# BUGGY: Compares strings alphabetically (not by length), returns len of last element checked
def find_longest_word(elements):
    # Function definition
    longest_element = elements[0]
    for element in elements:
        # Iterates through each element
        if element > longest_element:  # String comparison, not length comparison
            longest_element = element
    return len(element)  # BUG: Returns len of last element in loop, not longest

lst = ["jo", "tre", "Jonny", "abracadabr"]
print(find_longest_word(lst))


# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function that Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n..
#
# Prérequis Clés :
# - Program must prompt user for input
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
# - Must handle numeric values
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses recursion to solve the problem.
# ============================================================================
"""
Problème 128 :
Écrivez une fonction filter_long_words() qui prend une liste de mots et un entier n et retourne la liste de mots qui sont longer que n.
"""

# Filters words longer than n (similar to filter() built-in)
def filter_long_words(lst, n):
    # Function definition
    longest_words = []  # Variable name misleading - stores words longer than n
    for word in lst:
        # Iterates through each element
        if len(word) > n:  # Check if word length > n
            longest_words.append(word)
    return longest_words
        # Returns the result

lst = ["three", "threebesthorses" "hours", "Jonathannollthebestintheworld"]  # Remarque : missing comma between strings
n = 6
print(filter_long_words(lst, n))

"""
Problem: 129
A pangram is a sentence that contains all the letters of the English alphabet at least once, for example: The quick brown fox jumps over the lazy dog. Your task here is to write a function to check a sentence to see if it is a pangram or not.

# Checks if sentence contains all 26 letters
def is_pangram(sentence):
    # Function definition
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sentence = sentence.lower()  # Convert to lowercase for case-insensitive check
    for letter in alphabet:
        # Iterates through each element
        if letter not in sentence:  # If any letter missing, not a pangram
            return False
                # Returns the result
    return True  # All letters found

sentence = input("Enter a sentence: ")
    # Gets user input
result = is_pangram(sentence)
print(result)

"""
Problem: 130
Define a simple 'spelling correction' function correct() that takes a string and sees to it that 1) two or more occurrences of the space character is compressed into one, and 2) inserts an extra space after a period if the period is directly followed by a letter. E.g. correct('This is very funny and cool.Indeed!'') should return 'This is very funny and cool. Indeed!'' Astuce : Use regular expressions!
    # Returns the result

import re

# Uses regex for text correction: compresses spaces and adds space after periods
def correct(text):
    # r'\s+' matches one or more whitespace characters, replaces with single space
    text = re.sub(r'\s+', ' ', text)  # re.sub(pattern, replacement, string)
    # r'\.(?=[A-Za-z])' matches period followed by letter (positive lookahead)
    text = re.sub(r'\.(?=[A-Za-z])', '. ', text)  # (?=...) is positive lookahead assertion
    return text
        # Returns the result

text = input("Enter a string: ")
    # Gets user input
result = correct(text)
print(result)


# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function that Using the higher order function reduce(), write a function max_in_list() that takes a list of numbers and returns the largest one. Then ask yourself: .
# why define and call a new function, when I can just as well call the reduce() function directly?
#
# Prérequis Clés :
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
# - Must handle numeric values
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses recursion to solve the problem.
# ============================================================================
"""
Problème 131 :
en utilisant le higher order fonction reduce(), write une fonction max_in_list() qui prend une liste de nombres et retourne le maximum en utilisant reduce().
"""
from functools import reduce  # reduce() applies function cumulatively to items

# Helper function for reduce: returns larger of two numbers
def max_func(a, b):
    # Function definition
    if a > b:
        return a
            # Returns the result
    return b
        # Returns the result

# reduce() applies max_func pairwise: max_func(max_func(max_func(1,5),3),9),2)
def max_in_list(numbers):
    # Function definition
    return reduce(max_func, numbers)  # reduce(function, iterable) reduces list to single value

numbers = [1, 5, 3, 9, 2]
print(max_in_list(numbers))

"""
132
Write a Python program to creat a time table where the user puts a number as a argument.

# Generates multiplication table for given number (1-10)
def time_table(number):
    # Function definition
    result = ""
    for i in range(1, 11):  # range(1, 11) gives 1 to 10
        total = number * i
        result += f"{i} x {number} = {total}\n"  # f-string formatting
    return result
        # Returns the result

lst = 6
print(time_table(lst))

"""
Problem: 133
Write a program to create a time table using 2 for loops to print the full time table from 1 -10, eg 1 x 1 up to 10 x 10"

# Nested loops: outer loop for multiplicand, inner for multiplier
for i in range(1, 11):
    # Iterates through each element
    for j in range(1, 11):
        # Iterates through each element
        print(f"{i} x {j} = {i * j}")  # Prints all combinations 1x1 to 10x10


# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function that find the sum of all numbers in a list. Prompt the user to enter a list of numbers in a input function.
#
# Prérequis Clés :
# - Program must prompt user for input
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
# - Must handle numeric values
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses iteration to process elements.
# ============================================================================
"""
Problème 134 :
Écrivez un programme Python à trouver le somme de tous nombres dans une liste. demander le utilisateur à saisir une liste de nombres dans un entrée fonction
"""

# Converts input to integers and sums them using built-in sum()
def sum_of_all_numbers():
    # Function definition
    user_input = input("Enter a list of numbers separated by spaces: ")
        # Gets user input
    split_numbers = user_input.split()
        # Splits string into list of words/elements
    int_numbers = []

    for num in split_numbers:
        # Iterates through each element
        int_numbers.append(int(num))  # Convert strings to integers
    total_sum = sum(int_numbers)  # Built-in sum() function

    print(total_sum)

sum_of_all_numbers()


# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function that Write a function that takes numbers string "123" and splits the numbers into a string ("1", "2", "3")..
#
# Prérequis Clés :
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with strings
# - Must handle numeric values
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses iteration to process elements.
# ============================================================================
"""
Problème 135 :
Écrivez une fonction qui prend nombres chaîne "123" et divise le nombres dans une chaîne ("1", "2", "3").
"""

# BUGGY: split() on string without spaces returns list with one element; should iterate over string directly
def split_number(numbers):
    # Function definition
    numbers_split = numbers.split()  # split() on "123" returns ["123"] (no spaces to split on)
    number_lst = []
    for number in numbers:  # Iterates over characters in string "123"
        number_lst.append(number)  # Appends each character: "1", "2", "3"
    return number_lst  # Returns ["1", "2", "3"] (works but split() is unnecessary)

arg = "123"
print(split_number(arg))


# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function that Write a function that sorts words in a sentence alphabetically..
#
# Prérequis Clés :
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must sort elements in the specified order
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses iteration to process elements.
# ============================================================================
"""
Problème 136 :
Écrivez une fonction qui trie words dans une phrase alphabetically.
"""

# Splits sentence into words, sorts them, joins back with spaces
def alphabetically_ordered(sentence):
    # Function definition
    return " ".join(sorted(sentence.split()))  # sorted() sorts alphabetically, join() combines with spaces

sentence = "hello caca face"
print(alphabetically_ordered(sentence))

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function that Write a function that sorts numbers (int) from smallest number to biggest number..
#
# Prérequis Clés :
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must handle numeric values
# - Must sort elements in the specified order
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses iteration to process elements.
# ============================================================================
"""
Problem 137:
Write a function that sorts numbers (int) from smallest number to biggest number.
# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function that Write a function that sorts number (int) from biggest number to smallest number..
#
# Prérequis Clés :
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must handle numeric values
# - Must sort elements in the specified order
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses iteration to process elements.
# ============================================================================
"""

def smallest_largest(numbers):
    # Function definition
    return sorted(numbers)
        # Sorts elements in ascending order

numbers = [2, 76, 466, 3, 23]
print(smallest_largest(numbers))

"""
Problème 138 :
Écrivez une fonction qui trie nombre (int) de biggest nombre à plus petit nombre.
"""

# Sorts ascending then reverses to get descending order
def largest_smallest(numbers):  # Function name misleading
    # Function definition
    return sorted(numbers)[::-1]  # [::-1] reverses the sorted list (descending order)

numbers = [2, 76, 466, 3, 23]
print(largest_smallest(numbers))

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function that Write a function using sorted() number int) returning the seconded largest number from that list..
#
# Prérequis Clés :
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
# - Must handle numeric values
# - Must sort elements in the specified order
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses iteration to process elements.
# ============================================================================
"""
Problem 139:
Write a function using sorted() number int) returning the seconded largest number from that list.
    # Sorts elements in ascending order
# Returns second largest by sorting and taking second-to-last element
# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function that Write a function using sorted() number int) returning the fourth largest number from that list..
#
# Prérequis Clés :
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
# - Must handle numeric values
# - Must sort elements in the specified order
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses iteration to process elements.
# ============================================================================
"""

def seconded_largest_number(numbers):  # Typo: "seconded" should be "second"
    # Function definition
    return sorted(numbers)[-2]  # [-2] is second-to-last element (second largest)

numbers = [2, 76, 466, 3, 23]
print(seconded_largest_number(numbers))


"""
Problème 140 :
Écrivez une fonction en utilisant trié() nombre int) returning le fourth plus grand nombre de qui list.
"""

# Returns fourth largest by sorting and taking fourth-to-last element
def fourth_largest_number(numbers):
    # Function definition
    return sorted(numbers)[-4]  # [-4] is fourth-to-last element (fourth largest)

numbers = [2, 76, 466, 3, 23]
print(fourth_largest_number(numbers))

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function that Write a function using sorted() returning the smallest and third largest number from that list..
#
# Prérequis Clés :
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
# - Must handle numeric values
# - Must sort elements in the specified order
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses built-en Python functions for efficiency.
# ============================================================================

"""
Problème 141 :
Écrivez une fonction en utilisant trié() returning le plus petit et troisième plus grand nombre de qui list.
"""

# Returns tuple with smallest (index 0) and third largest (index -3)
def smallest_and_third(numbers):
    # Function definition
    smallest = sorted(numbers)[0]  # First element (smallest)
    third_largest = sorted(numbers)[-3]  # Third from end (third largest)
    return smallest, third_largest  # Returns tuple

numbers = [2, 76, 466, 3, 23]
print(smallest_and_third(numbers))


# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function that Write a function that sorts number from smallest number to biggest number using sorted()..
#
# Prérequis Clés :
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must handle numeric values
# - Must sort elements in the specified order
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses recursion to solve the problem.
# ============================================================================
"""
Problème 142 :
Écrivez une fonction qui trie nombre de plus petit nombre à biggest nombre en utilisant trié().
"""

# [::] is full slice (same as no slice) - unnecessary
def largest_smallest(numbers):  # Function name misleading
    # Function definition
    return sorted(numbers)[::]  # [::] is same as sorted(numbers)

numbers = [2, 76, 466, 3, 23]
print(largest_smallest(numbers))

# Simpler version without unnecessary slice
def smallest_biggest(numbers):
    # Function definition
    return sorted(numbers)  # Returns sorted list

lst = [2, 24, 23, 27, 2]
print(smallest_biggest(lst))


# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function that Write a function with user input that coverts 1 2 3 (int) into a "1" "2" "3" (str)..
#
# Prérequis Clés :
# - Program must prompt user for input
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must handle numeric values
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses iteration to process elements.
# ============================================================================
"""
Problème 143 :
Écrivez une fonction avec utilisateur entrée qui coverts 1 2 3 (int) dans un "1" "2" "3" (str).
"""

# Input is already strings after split(), so no conversion needed
def int_str():
    # Function definition
    user_lst = []
    user = input("type: ")  # e.g., "1 2 3"
    split_str = user.split()  # ["1", "2", "3"] (already strings)
    for word in split_str:
        # Iterates through each element
        user_lst.append(word)  # Appends strings (no conversion)
    print(user_lst)  # Prints list of strings

int_str()


# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function that Write a function that coverts 123 (int) into a "1" "2" "3" (str)..
#
# Prérequis Clés :
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must handle numeric values
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses iteration to process elements.
# ============================================================================
"""
Problème 144 :
Écrivez une fonction qui coverts 123 (int) dans un "1" "2" "3" (str).
"""

# Converts integer to string, then splits into list of digit strings
def int_to_str_list(number):
    # Function definition
    number_str = str(number)  # Convert int to string: 123 → "123"
    digits_as_strings = []
    for digit in number_str:  # Iterate over characters in string
        digits_as_strings.append(digit)  # Each character is already a string
    return digits_as_strings  # Returns ["1", "2", "3"]

number = 123
print(int_to_str_list(number))


# ============================================================================
# EXPLICATION DU PROBLÈME :
# find the common number between two lists. Prompt the user to enter two lists, for this exercise do not use set.
#
# Prérequis Clés :
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
# - Must handle numeric values
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses iteration to process elements.
# ============================================================================
"""
Problème 145 :
Écrivez un programme Python à trouver le commun nombre entre deux listes. demander le utilisateur à saisir deux listes, pour cette exercise N'utilisez pas set.
"""
# Uses nested loops to find common elements (O(n×m) complexity)
def common_numbers(lst1, lst2):
    # Function definition
    result = []
    for i in lst1:
        # Iterates through each element
        for j in lst2:
            # Iterates through each element
            if i == j and i not in result:  # Check if equal and not already added
                result.append(i)
    return result
        # Returns the result

lst1 = [2, 24, 23, 27, 2]
lst2 = [56, 2, 27, 455, 1]
print(common_numbers(lst1, lst2))


# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function that Write a function that sorts numbers as  string from biggest number to smallest number..
#
# Prérequis Clés :
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with strings
# - Must handle numeric values
# - Must sort elements in the specified order
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses iteration to process elements.
# ============================================================================
"""
Problème 146 :
Écrivez une fonction qui trie nombres as chaîne de biggest nombre à plus petit nombre.
"""

# Converts string numbers to int, sorts descending, converts back to strings
def big_small(numbers):
    # Function definition
    number_lst = []
    for number in numbers:
        # Iterates through each element
        number_lst.append(int(number))  # Convert string to int for proper numeric sort

    number_lst = sorted(number_lst)[::-1]  # Sort descending
    shorted_str = []  # Typo: "shorted" should be "sorted"

    for number in number_lst:
        # Iterates through each element
        shorted_str.append(str(number))  # Convert back to strings
    return shorted_str
        # Returns the result

lst = ["4", "67", "6"]
print(big_small(lst))


# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function that Write a function where user types a list of numbers in string and returns a list of numbers from smallest to biggest..
#
# Prérequis Clés :
# - Program must prompt user for input
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
# - Must work with strings
# - Must handle numeric values
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses recursion to solve the problem.
# ============================================================================
"""
Problème 147 :
Écrivez une fonction où utilisateur tapez une liste de nombres dans chaîne et retourne une liste de nombres de plus petit à biggest.
"""

# BUGGY: Sorts strings alphabetically, not numerically (e.g., "10" < "2" as strings)
def type_smallest_biggest():
    # Function definition
    user = input("type number list: ").split()
        # Gets user input
    sort_number = sorted(user)  # String sort: "10" comes before "2"

    print(sort_number)

type_smallest_biggest()

# CORRECT: Converts to int for numeric sort, then back to strings
def small_big():
    # Function definition
    user_string = input("type number followed by spaces: ")
        # Gets user input
    user_split = user_string.split()
        # Splits string into list of words/elements
    int_list = []
    for number in user_split:
        # Iterates through each element
        int_list.append(int(number))  # Convert to int

    int_list.sort()  # Sort numerically
    sorted_str = []
    for number in int_list:
        # Iterates through each element
        sorted_str.append(str(number))  # Convert back to strings
    return " ".join(sorted_str)  # Join with spaces

print(small_big())


# ============================================================================
# EXPLICATION DU PROBLÈME :
# double_elements that takes a list of numbers as input and returns a new list where each element is doubled, the list must be side by side eg 1, 2, 3, 1, 2, 3
#
# Prérequis Clés :
# - Program must prompt user for input
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
# - Must handle numeric values
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses recursion to solve the problem.
# ============================================================================
"""
Problème 148 :
Write un Python fonction appelée `double_elements` qui prend une liste de nombres en entrée et retourne une nouvelle liste où chaque élément est doubled, la liste doit be side by side par exemple 1, 2, 3, 1, 2, 3
"""

# Concatenates list with itself to duplicate all elements
def double_elements(numbers):
    # Function definition
    doubled = numbers + numbers  # List concatenation: [1,2,3] + [1,2,3] = [1,2,3,1,2,3]

    return doubled
        # Returns the result

lst = [2, 4, 6, 8]
print(double_elements(lst))

"""
Problem: 149
Write a Python program to find the common elements between two lists. Prompt the user to enter two lists using 2 for loops.

# Uses nested loops as required (O(n×m) complexity)
def common():
    # Function definition
    lst1 = input("type lst: ").split()
        # Gets user input
    lst2 = input("type lst: ").split()
        # Gets user input
    result = []
    for i in lst1:  # Outer loop
        for j in lst2:  # Inner loop (nested)
            if i == j and i not in result:
                # Checks condition
                result.append(i)
    return result
        # Returns the result

common()

"""
Problem: 150
Write a Python program to find the common elements between two lists. Prompt the user to enter two lists without using for loops.

# Uses set intersection (no explicit for loops, more efficient)
def common():
    # Function definition
    lst1 = input("type lst: ").split()
        # Gets user input
    lst2 = input("type lst: ").split()
        # Gets user input
    set1 = set(lst1)  # Convert to set
    set2 = set(lst2)
    common_element = set1.intersection(set2)  # Set intersection operator finds common elements

    print(common_element)

common()


# ============================================================================
# EXPLICATION DU PROBLÈME :
# find_longest_word that takes a list of words as input and returns the longest word in the list. If there are multiple longest words, return the first one encountered.
#
# Prérequis Clés :
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses iteration to process elements.
# ============================================================================
"""
Problème 151 :
Écrivez une fonction Python appelée find_longest_word qui prend une liste de mots en entrée et retourne le plus long mot dans la liste. si il y un multiple le plus long words, retourner le premier l'une encountered.
"""

# Tracks longest word by comparing lengths
def find_longest_word(words):
    # Function definition
    count = 0  # Tracks length of longest word found
    longest_word = ""
    for word in words:
        # Iterates through each element
        if len(word) > count:  # If current word is longer
            count = len(word)  # Update length
            longest_word = word  # Update word
    return longest_word
        # Returns the result

words = ["tree", "mountain", "do", "Jonathannollfrency"]

print(find_longest_word(words))


# ============================================================================
# EXPLICATION DU PROBLÈME :
# calculate_average that takes a list of numbers as input and returns the average of those numbers without using sum() and len()
#
# Prérequis Clés :
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
# - Must handle numeric values
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses iteration to process elements.
# ============================================================================
"""
Problème 152 :
Write un Python fonction appelée `calculate_average` qui prend une liste de nombres en entrée et retourne le moyenne de ces nombres sans en utilisant sum() et len()
"""

# Manually calculates sum and count, then divides
def average(numbers):
    # Function definition
    length = 0  # Manual length counter
    total = 0  # Manual sum accumulator
    for number in numbers:
        # Iterates through each element
        length += 1  # Count elements
        total += number  # Sum elements
        result = total / length  # Recalculate average each iteration (inefficient but correct)
    return result
        # Returns the result

numbers = [4, 667, 68, 766]
print(average(numbers))


# ============================================================================
# EXPLICATION DU PROBLÈME :
# find the second smallest element in a list.
#
# Prérequis Clés :
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses iteration to process elements.
# ============================================================================
"""
Problème 153 :
Écrivez un programme Python à trouver le deuxième plus petit élément dans une liste.
"""

# BUGGY: Uses key=len which sorts by length (for strings), not by value
def second_smallest_element(lst):
    # Function definition
    sorted_lst = sorted(lst, key=len)  # key=len sorts by length, not value
    if len(sorted_lst) >= 2:
        return sorted_lst[1]  # Returns second shortest, not second smallest
    else:
        return None
            # Returns the result

lst = ["t", "hope", "Jonathan", "it"]
print(second_smallest_element(lst))


# ============================================================================
# EXPLICATION DU PROBLÈME :
# find_second_last_element that takes a list as input and returns the second last element of the list.
#
# Prérequis Clés :
# - Program must prompt user for input
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Direct computation or transformation.
# ============================================================================
"""
Problème 154 :
Écrivez une fonction Python appelée `find_second_last_element` qui prend une liste en entrée et retourne le deuxième dernier élément de la liste.
"""

# Returns second-to-last element using negative indexing
def find_last_element():  # Function name should be find_second_last_element
    # Function definition
    user_input = input("Type list (elements separated by spaces): ").split()
        # Gets user input
    if not user_input:  # Check if list is empty
        return None
            # Returns the result
    return user_input[-2]  # [-2] is second-to-last element

print(find_last_element())


# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function that reverse_number that takes an integer as input and returns the reverse of that number. For example, if the input is 123, La fonction doit retourner 321.
# .
#
# Prérequis Clés :
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must handle numeric values
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses recursion to solve the problem.
# ============================================================================
"""
Problème 155 :
Écrivez une fonction Python appelée reverse_number qui prend un entier en entrée et retourne le reverse de cette nombre. par exemple, si le entrée est 123, la fonction devrait retourner 321.
"""

# Concise version: converts to string, reverses, converts back to int
def reverse_number(number):
    # Function definition
    return int(str(number)[::-1])  # str() → reverse with [::-1] → int()

lst = 456
print(reverse_number(lst))

# Step-by-step version (same logic, more verbose)
def reverse_number(number):
    # Function definition
    str_number = str(number)  # Convert to string
    reversed_str_number = str_number[::-1]  # Reverse string
    reversed_number = int(reversed_str_number)  # Convert back to int

    return reversed_number
        # Returns the result

number = 123
print(reverse_number(number))

# BUGGY: Returns string instead of int
def reverse_number(number):
    # Function definition
    str_number = str(number)[::-1]  # Reversed string
    int_number = str_number  # Still a string (misleading variable name)

    return int_number  # Returns string, not int

lst = 1234
print(reverse_number(lst))


# ============================================================================
# EXPLICATION DU PROBLÈME :
# remove_duplicates that takes a string as input and returns a new string with duplicate characters removed, without maintaining the original order of characters.
#
# Prérequis Clés :
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with strings
# - Must handle numeric values
# - Must remove or handle duplicate elements
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses iteration to process elements.
# ============================================================================
"""
Problème 156 :
Écrivez une fonction Python appelée remove_duplicates qui prend une chaîne en entrée et retourne une nouvelle chaîne avec en double caractères removed, sans maintaining le original order de caractères.
"""

# Remarque : Problem asks for duplicate characters, but solution removes duplicate words
def remove_duplicates(string):
    # Function definition
    split_word = string.split()  # Splits into words (not characters)
    set_word = set(split_word)  # Set removes duplicates (order not preserved)

    return " ".join(set_word)  # Join set (order may vary)

lst = "and here is was and in the"
print(remove_duplicates(lst))


# ============================================================================
# EXPLICATION DU PROBLÈME :
# remove_duplicates that takes a string as input and returns the duplicates removed into a string.
#
# Prérequis Clés :
# - Program must prompt user for input
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with strings
# - Must handle numeric values
# - Must remove or handle duplicate elements
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses recursion to solve the problem.
# ============================================================================
"""
Problème 157 :
Écrivez une fonction Python appelée remove_duplicates qui prend une chaîne en entrée et retourne les doublons removed dans une chaîne.
"""

# Returns list of duplicate words (not string with duplicates removed)
def main(string):
    # Function definition
    lst = []
    duplicates = []
    split_string = string.split()
        # Splits string into list of words/elements
    for word in split_string:
        # Iterates through each element
        if word not in lst:
            lst.append(word)  # Track unique words
        else:
            duplicates.append(word)  # Add to duplicates if seen before
    return duplicates  # Returns duplicates, not string with duplicates removed

string = "so what's happening duplicates duplicates today? It's hot duplicates duplicates."
main(string)

# Returns string of duplicate words (not string with duplicates removed)
def remove_duplicates(string):
    # Function definition
    split_word = string.split()
        # Splits string into list of words/elements
    seen = set()  # Track seen words
    duplicates = set()  # Track duplicate words
    for word in split_word:
        # Iterates through each element
        if word in seen:
            duplicates.add(word)  # Add to duplicates
        else:
            seen.add(word)  # Mark as seen

    return ' '.join(duplicates)  # Returns duplicates, not string with duplicates removed

lst = "and here is was and in the"
print(remove_duplicates(lst))

"""
Problem: 158
Write a Python program to find the largest element in a list. Prompt the user to enter a list of numbers using sorted.

# Sorts list and returns last element (largest)
def largest_element(numbers):
    # Function definition
   sorted_numbers = sorted(numbers)  # Sort ascending
   largest_number = sorted_numbers[-1]  # Last element is largest

   return largest_number
       # Returns the result

numbers = [2, 56, 75, 4566, 3]
print(largest_element(numbers))

# INEFFICIENT: Sorts list in each iteration
def main():
    # Function definition
    result = []
    user = input("type numbers: ").split()
        # Gets user input
    for num in user:
        # Iterates through each element
        result.append(int(num))
        largest_num = sorted(result)[-1]  # BUG: Sorts entire list each iteration (inefficient)
    return largest_num  # Returns largest from final sorted list

main()

"""
Problem: 159
Write a Python program to find the largest element in a list. Prompt the user to enter a list of numbers using max().

def largest_element(numbers):
    # Function definition
   return max(numbers)
       # Returns the result

numbers = [2, 56, 75, 4566, 3]
print(largest_element(numbers))


# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function that Define a function that computes the length of a given list or string. (It is true that Python has the len() function built in, but writing it yourself.
#  is nevertheless a good exercise.)
#
# Prérequis Clés :
# - Program must prompt user for input
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
# - Must work with strings
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses recursion to solve the problem.
# ============================================================================
"""
Problème 160 :
Définissez une fonction qui calcule la longueur de une donnée list ou chaîne. (C'est vrai qui Python une len() fonction construit dans, but writing it yourself est nevertheless un good exercise.)
"""

# Manual length calculation: iterate and count elements
def find_length(string):  # Works for both strings and lists (iterable)
    # Function definition
    count = 0
    for char in string:  # Iterate over elements
        count += 1
    return count
        # Returns the result

arg = "Jonathan"
print(find_length(arg))

"""
Problem: 161
Write a Python program to find the intersection of two lists. Prompt the user to enter two lists using set.

def intersection():
    # Function definition
    lst1 = input("type list: ").split()
        # Gets user input
    lst2 = input("type list: ").split()
        # Gets user input
    sort1 = sorted(lst1)
        # Sorts elements in ascending order
    sort2 = sorted(lst2)
        # Sorts elements in ascending order
    common = []
    for word in sort1:
        # Iterates through each element
        if word in sort2:
            common.append(word)
    print(common)

intersection()

def intersection():
    # Function definition
    lst1 = input("type lst1: ").split()
        # Gets user input
    lst2 = input("type lst2: ").split()
        # Gets user input
    set1 = set(lst1)
    set2 = set(lst2)
    common = set1.intersection(set2)

    print(common)

intersection()

def intersection_two_list(lst1, lst2):
    # Function definition
    set1 = set(lst1)
    set2 = set(lst2)
    result = set1.intersection(set2)

    return result
        # Returns the result

lst1 = ["tree", "car", "house", "garden"]
lst2 = ["car", "boat", "toilet", "tree"]
print(intersection_two_list(lst1, lst2))


# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function that Write a function where user types a list of numbers in string and returns a the third largest number in a list..
#
# Prérequis Clés :
# - Program must prompt user for input
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
# - Must work with strings
# - Must handle numeric values
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses iteration to process elements.
# ============================================================================
"""
Problème 162 :
Écrivez une fonction où utilisateur tapez une liste de nombres dans chaîne et retourne une troisième plus grand nombre dans une liste.
"""

# Finds third largest by sorting and taking third-to-last element
def third_largest():
    # Function definition
    user_string = input("type number followed by spaces: ")  # e.g., "10 5 20 15 8"
    user_split = user_string.split()  # Split into list of strings
    int_list = []
    for number in user_split:
        # Iterates through each element
        int_list.append(int(number))  # Convert strings to integers

    int_list.sort()  # Sort ascending: [5, 8, 10, 15, 20]
    result = int_list[-3]  # [-3] is third-to-last (third largest)

    print(result)

third_largest()


# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function that Write a Python function count_vowels that takes a string as input and returns a dictionary with the counts of each vowel ('a', 'e', 'i', 'o', 'u') in .
# the string. Ignore case, so 'A' and 'a' should be counted as the same vowel using list comprehension.
#
# Prérequis Clés :
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
# - Must work with strings
# - Should handle case sensitivity appropriately
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses recursion to solve the problem.
# ============================================================================
"""
Problème 163 :
Écrivez une fonction Python `count_vowels` qui prend une chaîne en entrée et retourne un dictionnaire avec le compte de chaque voyelle ('a','e','i','o','u') dans la chaîne. Ignore cas, so'A'et'a'devrait be counted as le même voyelle en utilisant List comprehension.
"""

# Remarque : Problem asks for list comprehension, but this solution uses regular loops
def count_vowels(string):
    # Function definition
    vowels = "aeiou"
    result = {}  # Dictionary to store vowel counts
    # Initialize all vowels to 0
    for vowel in vowels:
        # Iterates through each element
        result[vowel] = 0  # Set initial count for each vowel

    string = string.lower()  # Convert to lowercase for case-insensitive counting
    for char in string:
        # Iterates through each element
        if char in vowels:
            result[char] += 1  # Increment count for found vowel

    return result
        # Returns the result

string = "JOnathAn is the best"
print(count_vowels(string))

# Uses dictionary comprehension to initialize (closer to list comprehension requirement)
def count_vowels(sentence):
    # Function definition
    sentence = sentence.lower()
        # Converts to lowercase/uppercase
    vowels = "aeiou"
    # Dictionary comprehension: creates dict with each vowel as key, 0 as initial value
    # Syntax: {key: value for item in iterable} - similar to list comprehension
    vowel_counts = {number: 0 for number in vowels}  # {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    for char in sentence:
        # Iterates through each element
        if char in vowels:
            vowel_counts[char] += 1
    return vowel_counts
        # Returns the result

string = "Jonathan is the best"
print(count_vowels(string))


# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function that Write a Python function count_vowels that takes a string as input and returns a dictionary with the counts of each vowel ('a', 'e', 'i', 'o', 'u') in .
# the string. Ignore case, so 'A' and 'a' should be counted as the same vowel without using list conprehension.
#
# Prérequis Clés :
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
# - Must work with strings
# - Should handle case sensitivity appropriately
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses iteration to process elements.
# ============================================================================
"""
Problème 164 :
Écrivez une fonction Python `count_vowels` qui prend une chaîne en entrée et retourne un dictionnaire avec le compte de chaque voyelle ('a','e','i','o','u') dans la chaîne. Ignore cas, so'A'et'a'devrait be counted as le même voyelle sans en utilisant list conprehension.
"""

def count_vowels(sentence):
    # Function definition
    sentence = sentence.lower()
        # Converts to lowercase/uppercase
    vowels = "aeiou"
    vowel_counts = {}
    for number in vowels:
        # Iterates through each element
        vowel_counts[number] = 0

    for char in sentence:
        # Iterates through each element
        if char in vowels:
            vowel_counts[char] += 1

    return vowel_counts
        # Returns the result

string = "Jonathan is the best"
print(count_vowels(string))


# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function that Write a function that takes numbers integer 123 and splits the numbers into a string ("1", "2", "3")..
#
# Prérequis Clés :
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with strings
# - Must handle numeric values
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses recursion to solve the problem.
# ============================================================================
"""
Problème 165 :
Écrivez une fonction qui prend nombres integer 123 et divise le nombres dans une chaîne ("1", "2", "3").
"""

# Converts int to string, then to list of characters
def intiger_string(number):  # Typo: "intiger" should be "integer"
    # Function definition
    return list(str(number))  # str(123) → "123", list("123") → ["1", "2", "3"]
    # list() constructor converts string (iterable) into list of characters

number = 123
print(intiger_string(number))

# Alternative: returns tuple instead of list
def split_number_int(number):
    # Function definition
    number_str = str(number)  # Convert int to string: 123 → "123"
    result = tuple(number_str)  # tuple() constructor converts string to tuple of characters
    # tuple("123") → ("1", "2", "3") - immutable sequence

    return result
        # Returns the result

number = 123
print(split_number_int(number))


# ============================================================================
# EXPLICATION DU PROBLÈME :
# double_elements that takes a list of strings as input and returns a 2 new list where each element is doubled.
#
# Prérequis Clés :
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
# - Must work with strings
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses iteration to process elements.
# ============================================================================
"""
Problème 166 :
Écrivez une fonction Python appelée `double_elements` qui prend une liste de chaînes en entrée et retourne un 2 new list où chaque élément est doubled.
"""

# Duplicates list by appending all elements twice
def double_elements(lst):
    # Function definition
    doubled = []
    # First loop: append all elements once
    for word in lst:
        # Iterates through each element
        doubled.append(word)
    # Second loop: append all elements again
    for word in lst:
        # Iterates through each element
        doubled.append(word)
    return doubled  # Returns list with all elements duplicated: [a, b, c, a, b, c]
    # Remarque : Could also use lst + lst or lst * 2

lst = ["tree", "house", "car"]
print(double_elements(lst))


# ============================================================================
# EXPLICATION DU PROBLÈME :
# find the largest and smallest elements in a list. Prompt the user to enter a list of numbers using sorted()."
#
# Prérequis Clés :
# - Program must prompt user for input
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
# - Must handle numeric values
# - Must sort elements in the specified order
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses recursion to solve the problem.
# ============================================================================
"""
Problème 167 :
Écrivez un programme Python à trouver le plus grand et plus petit éléments dans une liste. demander le utilisateur à saisir une liste de nombres en utilisant trié()."
"""

# Uses sorted() but then uses min()/max() instead (inefficient - sorts then finds min/max separately)
def main():
    # Function definition
    user = input("type numbers: ").split()  # Get input and split
    # map(int, user) applies int() to each string, sorted() sorts the integers
    # list() converts sorted result to list (sorted already returns list, so redundant)
    lst = list(sorted(map(int, user)))  # map() is higher-order function that applies function to iterable
    smallest_num = min(lst)  # Could use lst[0] since it's sorted
    largest_num = max(lst)  # Could use lst[-1] since it's sorted
    return smallest_num, largest_num  # Returns tuple

main()

# More efficient: uses sorted() and takes first/last elements
def l_s(numbers):
    # Function definition
    sort_number_largest = sorted(numbers)[-1]  # Last element after sorting (largest)
    sort_number_smallest = sorted(numbers)[0]  # First element after sorting (smallest)

    return sort_number_largest, sort_number_smallest  # Returns tuple

numbers = [1, 2, 3, 4, 5]
print(l_s(numbers))


# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function that count_words that takes a string as input and returns a dictionary where the keys are the words in the string and the values are the counts of each wor.
# d. Words are separated by spaces, and the function should be case-insensitive, make the keys alphabetical.
#
# Prérequis Clés :
# - Program must prompt user for input
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with strings
# - Should handle case sensitivity appropriately
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses recursion to solve the problem.
# ============================================================================
"""
Problème 168 :
Écrivez une fonction Python appelée count_words qui prend une chaîne en entrée et retourne un dictionnaire où le clés sont le words dans la chaîne et le valeurs sont le compte de chaque mot. Words sont séparés by spaces, et la fonction devrait be cas-insensitive, make le clés alphabetical.
"""

# Sorts words first, then counts (ensures alphabetical order in result)
def count_words():
    # Function definition
    user = input("type words: ").split()
        # Gets user input
    sort = sorted(user)  # Sort words alphabetically
    result = {}  # Dictionary to store word counts
    for word in sort:
        # Iterates through each element
        word = word.lower()  # Convert to lowercase for case-insensitive counting
        # Check if word already in dictionary
        if word in result:  # Dictionary membership check
            result[word] += 1  # Increment count if word exists
        else:
            result[word] = 1  # Initialize count to 1 if first occurrence
    print(result)

count_words()

# Alternative: counts first, then sorts dictionary by keys
def count_words(string):
    # Function definition
    string = string.lower()  # Case-insensitive: convert entire string to lowercase
    words = string.split()  # Split into words
    word_count = {}  # Dictionary for word frequencies
    for word in words:
        # Iterates through each element
        if word in word_count:
            word_count[word] += 1  # Increment existing count
        else:
            word_count[word] = 1  # Initialize new word count

    # dict(sorted(...)) creates new dictionary from sorted key-value pairs
    # sorted(word_count.items()) sorts (key, value) tuples by key (alphabetically)
    # dict() converts sorted list of tuples back to dictionary
    sorted_word_count = dict(sorted(word_count.items()))  # Sort dictionary by keys
    return sorted_word_count
        # Returns the result

input_string = "This is a test. This test is only a test."
print(count_words(input_string))

"""
Problem: 169
Write a function merge_dictionaries that takes two dictionaries as arguments and returns a new dictionary that contains all the key-value pairs from both dictionaries. If a key is present in both dictionaries, the value from the second dictionary should overwrite the value from the first dictionary.

def merge_dictionaries(dict1, dict2):
    # Function definition
    merged = dict1.copy()
    for key, value in dict2.items():
        # Iterates through each element
        merged[key] = value
    return merged
        # Returns the result

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

result = merge_dictionaries(dict1, dict2)
print(result)

"""
Problem: 170
 Write a function count_characters that takes a string as input and returns a dictionary where the keys are characters in the string and the values are the counts of those characters.

# Counts frequency of each character (including spaces, punctuation, etc.)
def count_characters(string):
    # Function definition
    counts = {}  # Dictionary to store character frequencies
    for char in string:  # Iterate over each character
        # Check if character already in dictionary
        if char in counts:  # Dictionary membership check (O(1) average case)
            counts[char] += 1  # Increment count if character exists
        else:
            counts[char] = 1  # Initialize count to 1 for first occurrence
    return counts
    # Remarque : Could use collections.Counter(string) for more efficient counting

string = input("Enter a string: ")
    # Gets user input
result = count_characters(string)
print(result)

"""
Problem: 171
Write a function invert_dictionary that takes a dictionary as input and returns a new dictionary where the keys are the values from the input dictionary, and the values are lists of keys from the input dictionary that had that value.

# Inverts dictionary: original values become keys, original keys become values in lists
# Handles multiple keys with same value by grouping them in a list
def invert_dictionary(input_dict):
    # Function definition
    inverted = {}  # New dictionary for inverted structure
    # input_dict.items() returns view of (key, value) pairs
    for key, value in input_dict.items():
        # Check if value already exists as key in inverted dict
        if value not in inverted:
            inverted[value] = []  # Initialize empty list for this value
        # Append original key to list (handles multiple keys with same value)
        inverted[value].append(key)  # Add key to list of keys that had this value
    return inverted
    # Example: {'a': 1, 'b': 2, 'c': 1} → {1: ['a', 'c'], 2: ['b']}

input_dict = {'a': 1, 'b': 2, 'c': 1}  # 'a' and 'c' both have value 1
result = invert_dictionary(input_dict)  # Résultat: {1: ['a', 'c'], 2: ['b']}
print(result)

"""
Problem: 172
Write a function filter_by_value that takes a dictionary and a threshold value as input and returns a new dictionary containing only the key-value pairs where the value is greater than the threshold.

# Filters dictionary entries: keeps only key-value pairs where value > threshold
def filter_by_value(input_dict, threshold):
    # Function definition
    filtered = {}  # New dictionary for filtered results
    for key, value in input_dict.items():  # Iterate over all key-value pairs
        if value > threshold:  # Check if value exceeds threshold
            filtered[key] = value  # Add key-value pair to filtered dict
    return filtered
    # Remarque : Could use dictionary comprehension: {k: v for k, v in input_dict.items() if v > threshold}

input_dict = {'a': 5, 'b': 2, 'c': 8}
threshold = 3
result = filter_by_value(input_dict, threshold)  # Résultat: {'a': 5, 'c': 8} (b: 2 is filtered out)
print(result)

# Duplicate problem definition (same as above)
"""
Problem: 172
Write a function filter_by_value that takes a dictionary and a threshold value as input and returns a new dictionary containing only the key-value pairs where the value is greater than the threshold.

def filter_by_value(input_dict, threshold):
    # Function definition
    filtered = {}
    for key, value in input_dict.items():
        # Iterates through each element
        if value > threshold:
            filtered[key] = value
    return filtered
        # Returns the result

input_dict = {'a': 5, 'b': 2, 'c': 8}
threshold = 3
result = filter_by_value(input_dict, threshold)
print(result)

"""
Problem: 173
Write a function combine_lists_to_dict that takes two lists—one for keys and one for values—as input and returns a dictionary where each key-value pair is taken from corresponding elements in the input lists.

def combine_lists_to_dict(keys, values):
    # Function definition
    combined = {}
    for i in range(len(keys)):
        # Iterates through each element
        combined[keys[i]] = values[i]
    return combined
        # Returns the result

keys = ['a', 'b', 'c']
values = [1, 2, 3]
result = combine_lists_to_dict(keys, values)
print(result)

"""
Problem: 174
Write a function max_value_key that takes a dictionary as input and returns the key associated with the maximum value. If the dictionary is empty, the function should return None.
    # Returns the result

# Finds key with maximum value (returns first key if multiple keys have same max value)
def max_value_key(input_dict):
    # Check if dictionary is empty
    if not input_dict:  # Empty dict is falsy in Python
        return None  # Return None for empty dictionary

    # input_dict.values() returns view of all values
    max_value = max(input_dict.values())  # Find maximum value in dictionary

    # Search for key that has this maximum value
    for key, value in input_dict.items():
        # Iterates through each element
        if value == max_value:  # Found key with maximum value
            return key  # Return first key found with max value
    # Remarque : Could use max(input_dict, key=input_dict.get) for one-liner

my_dict = {'a': 10, 'b': 5, 'c': 20, 'd': 15}  # Max value is 20 (key 'c')
print(max_value_key(my_dict))  # Sortie : 'c'

empty_dict = {}
print(max_value_key(empty_dict))  # Sortie : None

"""
Problem: 175
Write a function dict_equal that takes two dictionaries as input and returns True if they are equal (i.e., they have the same keys with the same corresponding values), and False otherwise.

# Compares two dictionaries for equality using == operator
def dict_equal(dict1, dict2):
    # == operator compares dictionaries: checks same keys and same values
    # Dictionaries are equal if they have same key-value pairs (order doesn't matter in Python 3.7+)
    return dict1 == dict2
    # Remarque : In Python 3.7+, dict order is preserved, but == still compares by content, not order

dict1 = {'a': 1, 'b': 2}
dict2 = {'a': 1, 'b': 2}
result = dict_equal(dict1, dict2)  # True: same keys and values
print(result)

"""
Problem: 176
Write a function word_frequency that takes a string as input and returns a dictionary where the keys are words in the string and the values are the counts of those words.

# Counts frequency of each word in string (case-sensitive, preserves word case)
def word_frequency(string):
    # Function definition
    words = string.split()  # Split string into list of words
    result = {}  # Dictionary to store word frequencies
    for word in words:
        # Check if word already in dictionary
        if word in result:  # Word seen before
            result[word] += 1  # Increment count
        else:  # First occurrence of word
            result[word] = 1  # Initialize count to 1
    return result
    # Remarque : collections.Counter(words) provides more efficient word counting

string = "gore why are you here you are gore"
print(word_frequency(string))  # Résultat: {'gore': 2, 'why': 1, 'are': 2, 'you': 2, 'here': 1}

"""
Problem: 177
Write a function merge_list_of_dicts that takes a list of dictionaries as input and returns a single dictionary that merges all dictionaries in the list. If any keys are duplicated across dictionaries, the value from the last dictionary in the list should overwrite the previous ones.

# Merges multiple dictionaries: later dictionaries overwrite earlier ones for duplicate keys
def merge_list_of_dicts(dicts):
    # Function definition
    merged = {}  # Résultat dictionary
    for d in dicts:  # Iterate over each dictionary in list
        # update() adds all key-value pairs from d to merged
        # If key exists, value is overwritten; if new, key-value is added
        merged.update(d)  # dict.update() modifies dict in-place, adding/updating entries
    return merged
    # Remarque : Python 3.9+ supports {**d1, **d2, **d3} or dict unpacking

dicts = [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'a': 5}]
# Merging: {'a': 1, 'b': 2} → {'a': 1, 'b': 3, 'c': 4} → {'a': 5, 'b': 3, 'c': 4}
result = merge_list_of_dicts(dicts)  # Résultat: {'a': 5, 'b': 3, 'c': 4}
print(result)

"""
Problem: 178
Write a function remove_duplicates_from_values that takes a dictionary as input and returns a new dictionary where each key-value pair is preserved, but the values are lists with duplicates removed.

def remove_duplicates_from_values(input_dict):
    # Function definition
    new_dict = {}
    for key, value in input_dict.items():
        # Iterates through each element
        new_dict[key] = list(set(value))
    return new_dict
        # Returns the result

input_dict = {'a': [1, 2, 2, 3], 'b': [3, 4, 4, 5], 'c': [1, 1]}
result = remove_duplicates_from_values(input_dict)
print(result)

"""
Problem: 179
Write a function common_keys_max_values that takes two dictionaries and returns a new dictionary that contains only the keys that are present in both input dictionaries. The value for each key in the new dictionary should be the maximum of the values from the two input dictionaries.

# Finds common keys and takes maximum value for each
def common_keys_max_values(dict1, dict2):
    # Function definition
    common_keys = {}
    # dict1.keys() & dict2.keys() is set intersection of keys
    # & operator finds keys present in both dictionaries
    for key in dict1.keys() & dict2.keys():  # Iterate over common keys only
        # max() compares values from both dicts for this key
        common_keys[key] = max(dict1[key], dict2[key])  # Take maximum value
    return common_keys
    # Example: dict1={'b':2}, dict2={'b':3} → common_keys={'b':3} (max of 2 and 3)

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 1, 'd': 4}  # Common keys: 'b', 'c'
result = common_keys_max_values(dict1, dict2)  # Résultat: {'b': 3, 'c': 3} (max values)
print(result)

"""
Problem: 180
Write a function average_values that takes a list of dictionaries as input and returns a new dictionary. The new dictionary should contain the same keys, and the values should be the average of the values associated with each key across all input dictionaries.

# Calculates average of values for each key across multiple dictionaries
def average_values(dicts):
    # Function definition
    averages = {}  # Stores sum of values for each key
    counts = {}  # Stores count of occurrences for each key
    # First pass: accumulate sums and counts
    for d in dicts:  # Iterate over each dictionary
        for key, value in d.items():  # Iterate over key-value pairs
            if key in averages:  # Key seen before
                averages[key] += value  # Add to sum
                counts[key] += 1  # Increment count
            else:  # First occurrence of key
                averages[key] = value  # Initialize sum
                counts[key] = 1  # Initialize count

    # Second pass: calculate averages by dividing sum by count
    for key in averages:
        # Iterates through each element
        averages[key] /= counts[key]  # Divide sum by count to get average

    return averages
    # Example: [{'a':1}, {'a':3}, {'a':5}] → {'a': 3.0} (average of 1, 3, 5)

dicts = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}, {'a': 5, 'b': 6}]
result = average_values(dicts)  # Résultat: {'a': 3.0, 'b': 4.0} (averages)
print(result)

"""
Problem: 181
Write a function merge_dicts_with_lists that takes a list of dictionaries as input. Each dictionary in the list has keys that are strings and values that are lists of integers. The function should merge these dictionaries into a single dictionary where the keys are preserved, and the values are merged lists containing all unique integers from the input dictionaries for each key.

# Merges dictionaries with list values, combining lists and removing duplicates
def merge_dicts_with_lists(dicts):
    # Function definition
    merged = {}
    for d in dicts:  # Iterate over each dictionary
        for key, value in d.items():  # value is a list of integers
            if key in merged:  # Key already exists
                # BUG: set.update() expects iterable, but value is already a list
                # Should be: merged[key].update(value) works because list is iterable
                merged[key].update(value)  # Add elements from value list to set (removes duplicates)
            else:  # First occurrence of key
                merged[key] = set(value)  # Convert list to set (removes duplicates, allows efficient merging)

    # Convert sets back to lists
    for key in merged:
        # Iterates through each element
        merged[key] = list(merged[key])  # Convert set to list (order may vary)

    return merged
    # Example: [{'a':[1,2]}, {'a':[2,3]}] → {'a': [1, 2, 3]} (duplicates removed)

dicts = [{'a': [1, 2, 3], 'b': [2, 3]}, {'a': [3, 4], 'b': [4, 5], 'c': [6]}, {'c': [7, 8, 6]}]
result = merge_dicts_with_lists(dicts)  # Merges lists, removes duplicates
print(result)

"""
Problem: 182
Write a function group_by_first_letter that takes a list of strings as input and returns a dictionary. The dictionary should group the strings by their first letter. Each key in the dictionary should be a first letter, and the corresponding value should be a list of strings that start with that letter.

# Groups words by their first letter (dictionary with lists as values)
def group_by_first_letter(lst):
    # Function definition
    result = {}  # Dictionary: key = first letter, value = list of words
    for word in lst:
        # Iterates through each element
        first_letter = word[0]  # Get first character using index [0]
        if first_letter not in result:  # First word with this starting letter
            result[first_letter] = [word]  # Initialize list with first word
        else:  # Letter seen before
            result[first_letter].append(word)  # Add word to existing list
    return result
    # Example: ["apple", "banana"] → {'a': ['apple'], 'b': ['banana']}

lst = ["apple", "banana", "orange", "cake"]
print(group_by_first_letter(lst))  # Résultat: {'a': ['apple'], 'b': ['banana'], 'o': ['orange'], 'c': ['cake']}

# BUGGY: Overwrites value instead of appending to list
def main(lst):
    # Function definition
    result = {}
    for word in lst:
        # Iterates through each element
        key = word[0]  # First letter
        value = word  # Entire word
        result[key] = value  # BUG: Overwrites previous value instead of appending to list
    return result  # Returns only last word for each letter

lst = ["tree", "cliff", "mountain", "zoo","dodo", "grassy"]
main(lst)  # Résultat: {'t': 'tree', 'c': 'cliff', 'm': 'mountain', 'z': 'zoo', 'd': 'dodo', 'g': 'grassy'}

# ============================================================================
# EXPLICATION DU PROBLÈME :
# check if a string is an anagram of another string, ignoring whitespace. Prompt the user to enter two strings without using sorted().
#
# Prérequis Clés :
# - Program must prompt user for input
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with strings
# - Must sort elements in the specified order
# - Must check if strings contain same letters in different order
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses iteration to process elements.
# ============================================================================
"""
Problème 183 :
Écrivez un programme Python à vérifier si une chaîne est an un anagramme de un autre chaîne, ignoring les espaces. demander le utilisateur à saisir deux strings sans en utilisant trié().
"""

def is_anagram(string1, string2):
    # Function definition
    string1 = string1.replace(" ", "").lower()
        # Converts to lowercase/uppercase
    string2 = string2.replace(" ", "").lower()
        # Converts to lowercase/uppercase
    if len(string1) != len(string2):
        return False
            # Returns the result

    char_count1 = {}
    char_count2 = {}
    for char in string1:
        # Iterates through each element
        if char in char_count1:
            char_count1[char] += 1
        else:
            char_count1[char] = 1

    for char in string2:
        # Iterates through each element
        if char in char_count2:
            char_count2[char] += 1
        else:
            char_count2[char] = 1
    return char_count1 == char_count2
        # Returns the result

string1 = input("Enter the first string: ")
    # Gets user input
string2 = input("Enter the second string: ")
    # Gets user input

print("Are the strings anagrams?:", is_anagram(string1, string2))


# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function that Write a function that takes numbers integer 123 and return 2..
#
# Prérequis Clés :
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must handle numeric values
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Direct computation or transformation.
# ============================================================================
"""
Problème 184 :
Écrivez une fonction qui prend nombres integer 123 et retourner 2.
"""

# Extracts digit at index 1 (second digit) from integer
def get_second_digit(number):
    # Function definition
    number = str(number)  # Convert to string: 123 → "123"
    list_number = list(number)[1]  # Convert to list and get index 1: ["1","2","3"][1] → "2"

    return list_number  # Returns string "2", not integer 2

number = 123
print(get_second_digit(number))  # Sortie : "2" (string)


# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function that Write a function that takes numbers integer 12345678 and return 2, 4, 8..
#
# Prérequis Clés :
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must handle numeric values
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Direct computation or transformation.
# ============================================================================
"""
Problème 185 :
Écrivez une fonction qui prend nombres integer 12345678 et retourner 2, 4, 8.
"""

# Extracts digits at specific indices using string indexing
def get_indexed_digits(number):
    # Function definition
    number = str(number)  # Convert to string: 12345678 → "12345678"
    num2 = number[1]  # Index 1: second digit "2"
    num4 = number[3]  # Index 3: fourth digit "4"
    num8 = number[-1]  # Index -1: last digit "8" (negative indexing from end)

    return num2, num4, num8  # Returns tuple of strings: ("2", "4", "8")
    # String indexing: positive indices from start (0-based), negative from end (-1 is last)

number = 12345678
print(int(number))  # Sortie : ("2", "4", "8")


# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function that Write a function that takes numbers integer 12346778910 and users indexing to return the number 2, 4, 8.
#
# Prérequis Clés :
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must handle numeric values
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses recursion to solve the problem.
# ============================================================================
"""
Problème 186 :
Écrivez une fonction qui prend nombres integer 12346778910 et users indexing à retourner le nombre 2, 4, 8
"""

# Extracts digits at specified indices from integer
def get_digits(number, indices):
    # Function definition
    number_str = str(number)  # Convert to string for indexing: 12345678910 → "12345678910"
    result = []
    for i in indices:  # Iterate over list of indices
        result.append(number_str[i])  # Extract character at index i
        # String indexing: number_str[1] = "2", number_str[3] = "4", number_str[7] = "8"

    return tuple(result)  # Convert list to tuple: ("2", "4", "8")
    # tuple() creates immutable sequence from iterable

number = 12345678910
indices = [1, 3, 7]  # Indices to extract
print(get_digits(number, indices))  # Sortie : ("2", "4", "8")

"""
Problem: 187
Write a Python function called `double_elements` that takes a list of strings as input and returns a 2 new list where each element is doubled where each element is doubled side by side eg 'tree', 'tree', 'road', 'road', 'slow', 'slow'.

def double_elements(string1):
    # Function definition
    double = []
    for word in string1:
        # Iterates through each element
        double.append(word)
        double.append(word)

    return double
        # Returns the result

string1 = ["tree", "road", "slow"]
print(double_elements(string1))


# ============================================================================
# EXPLICATION DU PROBLÈME :
# get_initials that takes a full name (first and last name jonathan noll) as input and returns  "joNathAn noLL"" of the name in uppercase (NALL in jonathan noll).
#
# Prérequis Clés :
# - Program must prompt user for input
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Should handle case sensitivity appropriately
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses recursion to solve the problem.
# ============================================================================
"""
Problème 188 :
Écrivez une fonction Python appelée get_initials qui prend un full nom (premier et dernier nom jonathan noll) en entrée et retourne "joNathAn noLL"" de le nom en majuscule (NALL dans jonathan noll).
"""

# Uppercases specific characters at hardcoded indices (fragile - assumes fixed name length)
def get_initials(name):
    # Function definition
    name_list = list(name)  # Convert string to list of characters (mutable)
    # Hardcoded indices: uppercase characters at positions 2, 6, 11, 12
    # "jonathan noll" → indices: j(0), o(1), n(2), a(3), t(4), h(5), a(6), n(7), ...
    name_list[2] = name_list[2].upper()  # 'n' → 'N' (index 2)
    name_list[6] = name_list[6].upper()  # 'a' → 'A' (index 6)
    name_list[11] = name_list[11].upper()  # 'l' → 'L' (index 11)
    name_list[12] = name_list[12].upper()  # 'l' → 'L' (index 12)

    return ''.join(name_list)  # join() combines list back into string
    # ''.join() joins with empty string (no separator between characters)

name = "jonathan noll"
print(get_initials(name))  # Sortie : "joNathAn noLL"

# More flexible: uppercases any character in "nall" regardless of position
def get_initials(name):
    # Function definition
    initials = []
    for char in name:
        # Iterates through each element
        if char in "nall":  # Check if character is 'n', 'a', or 'l' (case-sensitive)
            initials.append(char.upper())  # Convert to uppercase
        else:
            initials.append(char)  # Keep as-is
    return ''.join(initials)  # Join list into string

name = "jonathan noll"
print(get_initials(name))  # Sortie : "joNathAn noLL" (uppercases all n, a, l characters)

"""
Problem: 189
Write a Python program to find the sum of the digits in a string. Prompt the user to enter a string containing numbers eg "1234" should return 10.
    # Returns the result

# Sums all digit characters in string (assumes all characters are digits)
def sum_digits():
    # Function definition
    user = list(input("type number: "))  # Convert string to list of characters
    count = 0  # Variable name misleading - actually stores sum
    for number in user:  # 'number' is actually a character (misleading name)
        count += int(number)  # Convert char to int and add: "1"→1, "2"→2, etc.
    print(count)

sum_digits()

# More robust: only sums digit characters, ignores non-digits
def digits_string():
    # Function definition
    user = input("Type a string containing numbers: ")
        # Gets user input
    total = 0
    for char in user:
        # Iterates through each element
        if char.isdigit():  # isdigit() checks if character is a digit (0-9)
            total += int(char)  # Convert digit char to int and add
            # isdigit() returns True for '0'-'9', False for letters, spaces, etc.

    print(total)

digits_string()

"""
Problem: 190
Write a Python program to remove duplicates from a string and maintain the order of characters. Prompt the user to enter a string

# Removes duplicate characters while preserving order of first occurrence
def remove_duplicate():
    # Function definition
    user = input("type string: ")
        # Gets user input
    duplicate = []  # Variable name misleading - stores unique characters
    for char in user:
        # Iterates through each element
        if char not in duplicate:  # Check if character already seen
            duplicate.append(char)  # Add first occurrence only (preserves order)
    print(duplicate)  # Prints list, not string (could use ''.join(duplicate))
    # Remarque : Using list maintains order; set() would be faster but loses order

remove_duplicate()

"""
Problem: 191
Write a Python function called `find_min` that takes a list of numbers as input and returns the minimum number in the list without sorted().
    # Sorts elements in ascending order

# Finds minimum using linear search (single pass, O(n) complexity)
def find_min():
    # Function definition
    user = input("type list: ").split()
        # Gets user input
    user_int = []
    for number in user:
        # Iterates through each element
        user_int.append(int(number))  # Convert strings to integers

    min_number = user_int[0]  # Initialize with first element
    # Compare each number with current minimum
    for number in user_int:
        # Iterates through each element
        if number < min_number:  # If smaller number found
            min_number = number  # Update minimum
    print(min_number)

find_min()


# ============================================================================
# EXPLICATION DU PROBLÈME :
# count_occurrences that takes a list and an element as input and returns the number of times the element appears in the list.
#
# Prérequis Clés :
# - Program must prompt user for input
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
# - Must handle numeric values
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses recursion to solve the problem.
# ============================================================================
"""
Problème 192 :
Écrivez une fonction Python appelée count_occurrences qui prend une liste et un élément en entrée et retourne le nombre de fois élément apparaît dans la liste.
"""

# Counts how many times element appears in list (linear search)
def count_occurrences(lst, element):
    # Function definition
    count = 0
    for item in lst:  # Iterate through all items
        if item == element:  # Compare each item with target element
            count += 1  # Increment counter when match found
    return count
    # Remarque : list.count(element) is built-in method that does this

test_list = [1, 2, 3, 4, 1, 2, 1, 5, 1]
element_to_count = 1
print("Number of occurrences of", element_to_count, ":", count_occurrences(test_list, element_to_count))

# Case-insensitive version for strings
def main():
    # Function definition
    user = input("type element: ").lower()  # Convert input to lowercase
    count = 0
    for word in lst:  # lst must be defined outside function (global variable)
        if word.lower() == user:  # Case-insensitive comparison
            count += 1

    if count == 0:
        # Checks condition
        return "not in lst"  # Return string if not found
    else:
        return count  # Return count

lst = ["Jonathan", "Christopher", "Jeremy", "Jonathan", "bad"]
print(main())

"""
Problem: 193
Write a Python function called `find_min` that takes a list of numbers as user input and returns the minimum number in the list. use sorted().
    # Sorts elements in ascending order

def find_min_num():
    # Function definition
    user = input("type number: ").split()
        # Gets user input
    int_number = []
    for number in user:
        # Iterates through each element
        int_number.append(int(number))

    min_num = sorted(int_number)[0]
        # Sorts elements in ascending order
    print(min_num)

find_min_num()

"""
Problem: 194
Write a Python program to find the largest element in a list. Prompt the user to enter a list of items using max(). Write a list of words.

# Finds longest word using max() with key parameter
def largest_element():
    # Function definition
    user = input("type list: ").split()
    # max() with key=len finds element with maximum length
    # key parameter specifies function to determine comparison value
    largest_word = max(user, key=len)  # key=len compares by length, not alphabetically

    print(largest_word)

largest_element()

"""
Problem: 195
Write a Python program to find the second largest element in a list. Prompt the user to enter a list of items. Write a list of words.

# Finds second longest word by sorting descending and taking index 1
def second_largest_element():
    # Function definition
    user_input = input("Enter a list of words: ").split()
        # Gets user input
    if len(user_input) < 2:  # Edge case: need at least 2 words
        print("The list must contain at least two words.")
        return

    # Sort by length in descending order (longest first)
    sorted_words = sorted(user_input, key=len, reverse=True)  # reverse=True sorts descending
    print(f"The second largest word is: {sorted_words[1]}")  # Index 1 is second longest

second_largest_element()

# Alternative: sorts ascending and takes second-to-last
def second_largest_element():
    # Function definition
    user_input = input("Enter a list of words: ").split()
        # Gets user input
    if len(user_input) < 2:
        print("The list must contain at least two words.")
        return

    sorted_words = sorted(user_input, key=len)  # Sort ascending (shortest first)
    print(f"The second largest word is: {sorted_words[-2]}")  # [-2] is second-to-last (second longest)

second_largest_element()

# Simplified version with less descriptive error message
def second_largest_element():
    # Function definition
    user_input = input("Enter a list of words: ").split()
        # Gets user input
    if len(user_input) < 2:
        print("less then 2")  # Less descriptive error message
        return

    sort = sorted(user_input, key=len)  # Sort ascending
    second_largest = sort[-2]  # Second-to-last element

    print(second_largest)

second_largest_element()

"""
Problem: 196
Write a Python program to find the maximum of three numbers. Prompt the user to enter three numbers. use max().

# Uses built-in max() function (numbers already in list, list() is redundant)
def max_of_three(numbers):
    # Function definition
     result = max(list(numbers))  # list() is unnecessary if numbers is already a list
     return result
     # Remarque : max() can take multiple arguments: max(567, 56, 6) or max(numbers)

three_numbers = [567, 56, 6]
print(max_of_three(three_numbers))

"""
Problem: 197
Write a Python program to find the maximum of three numbers. Enter three numbers in a list. Without using any build in fuctions apart from print().

def max_of_three(numbers):
    # Function definition
    max_number = numbers[0]
    if numbers[1] > max_number:
        max_number = numbers[1]

    if numbers[2] > max_number:
        max_number = numbers[2]

    return max_number
        # Returns the result

three_numbers = [567, 56, 6]
print(max_of_three(three_numbers))

"""
Problem: 198
Write a function that converts centimetets to inches.

# Unit conversion: centimeters to inches (1 cm = 0.3937 inches)
def centimeters_inches():
    # Function definition
    cm = int(input("type centimeters: "))
        # Gets user input
    inches = cm * 0.3937  # Conversion factor: multiply centimeters by 0.3937
    # f-string formatting: embeds variables in string with {variable}
    print(f"{cm} cm = {inches} inches")  # Displays conversion result

centimeters_inches()


# ============================================================================
# EXPLICATION DU PROBLÈME :
# find_min_max that takes a list of numbers as input and returns a tuple containing the minimum and maximum numbers in the list, dont not call the fuction using print(find_min_max). Do not use sort().
#
# Prérequis Clés :
# - Program must prompt user for input
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
# - Must handle numeric values
# - Must sort elements in the specified order
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses recursion to solve the problem.
# ============================================================================
"""
Problème 199 :
Écrivez une fonction Python appelée find_min_max qui prend une liste de nombres en entrée et retourne un tuple contenant le minimum et maximum nombres dans la liste, dont pas call le fuction en utilisant print(find_min_max). N'utilisez pas trier().
"""

def find_min_max():
    # Function definition
    user = input("type list of numbers: ").split()
        # Gets user input
    int_num = []
    for number in user:
        # Iterates through each element
        int_num.append(int(number))

    min_num = min(int_num)
    max_num = max(int_num)

    print(min_num, max_num)

find_min_max()

def find_min_max():
    # Function definition
    user = input("type numbers: ").split()
        # Gets user input
    int_number = []
    for number in user:
        # Iterates through each element
        int_number.append(int(number))

    min_number = int_number[0]
    max_number = int_number[0]

    for number in int_number:
        # Iterates through each element
        if number < min_number:
            min_number = number
        if number > max_number:
            max_number = number
    print(min_number, max_number)
    return min_number, max_number
        # Returns the result

find_min_max()


# ============================================================================
# EXPLICATION DU PROBLÈME :
# find the common number in a lists. for this exercise do not use set.
#
# Prérequis Clés :
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
# - Must handle numeric values
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses iteration to process elements.
# ============================================================================
"""
Problème 200 :
Écrivez un programme Python à trouver le commun nombre dans un listes. pour cette exercise N'utilisez pas set.
"""

# Finds duplicate numbers in a single list (not common between two lists)
# Uses list to track seen numbers (no set as required)
def common_numbers(lst):
    # Function definition
    seen = []  # Track numbers we've seen
    common = []  # Track duplicate numbers
    for number in lst:
        # Check if number was seen before and not already in common list
        if number in seen and number not in common:  # Found duplicate
            common.append(number)  # Add to common (duplicates)
        else:
            seen.append(number)  # Mark as seen (first occurrence)

    return common  # Returns list of numbers that appear more than once
    # Remarque : Problem says "common number in a lists" (singular) - finds duplicates within one list

lst = [43, 2, 45, 567, 666, 2, 45]  # Duplicates: 2 and 45
print(common_numbers(lst))  # Sortie : [2, 45]


# ============================================================================
# EXPLICATION DU PROBLÈME :
# find the common number in a lists. use set().
#
# Prérequis Clés :
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
# - Must handle numeric values
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses recursion to solve the problem.
# ============================================================================
"""
Problème 201 :
Écrivez un programme Python à trouver le commun nombre dans un listes. Utilisez set().
"""

# Finds duplicate numbers in a list using set for tracking (finds numbers appearing more than once)
def common_num(lst):
    # Function definition
    unique = set()  # Set to track unique numbers seen
    commom = []  # Typo: "commom" should be "common"
    for number in lst:
        # Iterates through each element
        if number in unique:  # Number seen before (duplicate found)
            commom.append(number)  # Add to duplicates list
        else:
            unique.add(number)  # Mark as seen (add to set)
    return commom  # Returns list of duplicate numbers

lst = [2, 5, 6, 2, 4, 5]
print(common_num(lst))  # Sortie : [2, 5] (duplicates)

# Alternative: returns set instead of list
def common_numbers(lst):
    # Function definition
    seen = set()  # Track seen numbers
    common = set()  # Track duplicates (set removes duplicate entries in result)
    for number in lst:
        # Iterates through each element
        if number in seen:  # Duplicate found
            common.add(number)  # Add to common set
        else:
            seen.add(number)  # Mark as seen
    # Returns set of duplicate numbers (no duplicates in result itself)
    return common
        # Returns the result

lst = [43, 2, 45, 567, 666, 2, 45, 43]
print(common_numbers(lst))  # Sortie : {2, 45, 43} (set of duplicates)

"""
Problem: 202
Write a function word_frequency that takes a string as input and returns a dictionary where the keys are the characters in the string and the values are the counts of those characters alphabetically.

# Counts character frequency (not word frequency - function name is misleading)
# Sorts characters first to ensure alphabetical order in result
def word_frequency(string):  # Function name says "word" but counts characters
    # Function definition
    string = string.replace(" ", "")  # Remove spaces
    sort_char = sorted(string)  # Sort characters alphabetically
    result = {}  # Dictionary for character counts
    # Iterate over sorted characters (ensures alphabetical order)
    for word in sort_char:  # Variable name 'word' is misleading - it's a character
        if word in result:
            result[word] += 1  # Increment count
        else:
            result[word] = 1  # Initialize count
    return result
    # Remarque : Python 3.7+ preserves insertion order, so sorting first ensures alphabetical keys

string = "gore why are you here you are gore"
print(word_frequency(string))  # Counts characters, not words

"""
Problem: 203
Define a function total() that sums and multiplies (respectively) all the numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.
    # Returns the result

# Calculates both sum and product in single pass, returns as tuple
def total(numbers):
    # Function definition
    total_numbers = 0  # Initialize sum accumulator (additive identity: 0)
    multiply_numbers = 1  # Initialize product accumulator (multiplicative identity: 1)
    for number in numbers:
        # Iterates through each element
        total_numbers += number  # Accumulate sum
        multiply_numbers *= number  # Accumulate product
    return total_numbers, multiply_numbers  # Returns tuple (sum, product)
    # Single-pass algorithm: O(n) time complexity, calculates both simultaneously

lst_numbers = [1, 2, 3, 4]
print(total(lst_numbers))  # Sortie : (10, 24) - tuple of sum and product


# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires writing a program that Write a program that maps a list of words into a list of integers representing the words with the lengths of the correponding words..
#
# Prérequis Clés :
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
# - Must handle numeric values
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses iteration to process elements.
# ============================================================================
"""
Problème 204 :
Écrivez un programme qui maps une liste de mots dans une liste d'entiers representing le words avec le lengths de le correponding words.
"""

# Creates alternating list: word, length, word, length, ...
# Remarque : Problem asks for "integers representing words with lengths" - this interleaves words and lengths
def list_integers(lst):
    # Function definition
    result = []
    for word in lst:
        # Iterates through each element
        result.append(word)  # Add word itself (string)
        result.append(len(word))  # Add length of word (integer)
        # Résultat: ["join", 4, "Jonathan", 8, "tree", 4]
    return result
    # Remarque : Result contains both strings and integers (mixed types)

lst = ["join", "Jonathan", "tree"]
print(list_integers(lst))  # Sortie : ["join", 4, "Jonathan", 8, "tree", 4]


# ============================================================================
# EXPLICATION DU PROBLÈME :
# calculate_average that takes a list of numbers as input and returns the average of those numbers. use len() and sum().
#
# Prérequis Clés :
# - Program must prompt user for input
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
# - Must handle numeric values
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses recursion to solve the problem.
# ============================================================================
"""
Problème 205 :
Écrivez une fonction Python appelée `calculate_average` qui prend une liste de nombres en entrée et retourne le moyenne de ces nombres. Utilisez len() et sum().
"""

# Calculates arithmetic mean: sum of numbers divided by count
def average(lst):
    # Function definition
    sum_lst = sum(lst)  # Built-in sum() adds all numbers
    length = len(lst)  # Built-in len() counts elements
    total = sum_lst / length  # Divide sum by count to get average
    # Remarque : / operator performs floating-point division (returns float even if inputs are int)

    return total
    # Formula: average = sum(numbers) / len(numbers)

lst = [2666, 566, 6777]
print(average(lst))  # Sortie : (2666 + 566 + 6777) / 3 = 10009 / 3 = 3336.333...

"""
Problem: 206
Write a Python program to find the maximum of three numbers. Prompt the user to enter three numbers. do not use max().

# Manual max calculation using if statements (no built-in max())
def max_of_three():
    # Function definition
    user = input("type three numbers: ").split()
        # Gets user input
    int_numbers = []
    for number in user:
        # Iterates through each element
        int_numbers.append(int(number))
    # BUG: len(number) checks length of last string in loop, not length of list
    if len(number) != 3:  # Should be len(int_numbers) != 3
        print("not enough numbers")
        return

    max_number = int_numbers[0]  # Initialize with first number
    # Compare with second number
    if int_numbers[1] > max_number:  # If second is larger
        max_number = int_numbers[1]  # Update maximum
    # Compare with third number
    if int_numbers[2] > max_number:  # If third is larger
        max_number = int_numbers[2]  # Update maximum

    print(max_number)
    # Remarque : Assumes exactly 3 numbers (will error if list has different length)

max_of_three()

"""
Problem: 207
Write a Python program to find the maximum of of list of numbers. Prompt the user to enter three numbers. do not use max().

# Finds maximum using linear search (works for any list length, not just 3)
def max_of_list():
    # Function definition
    user = input("type three numbers: ").split()  # Remarque : says "three" but algorithm works for any length
    if len(user) != 3:  # Validation check
        print("type more numbers")
        return

    int_numbers = []
    for number in user:
        # Iterates through each element
        int_numbers.append(int(number))
    max_number = int_numbers[0]  # Initialize with first element
    # Linear search: compare each element with current maximum
    for number in int_numbers:
        # Iterates through each element
        if number > max_number:  # If current number is larger
            max_number = number  # Update maximum
    # Single-pass algorithm: O(n) time complexity

    print(max_number)

max_of_list()

"""
Problem: 208
Write a Python program to find the maximum of of list of numbers. Prompt the user to enter three numbers. Use max().

# Uses built-in max() function to find maximum
def max_of_list():
    # Function definition
    user = input("type three numbers: ").split()
        # Gets user input
    int_numbers = []
    for number in user:
        # Iterates through each element
        int_numbers.append(int(number))

    max_number = max(int_numbers)  # Built-in max() finds maximum element
    # max() can take any iterable and returns the largest element

    print(max_number)

max_of_list()


# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires writing a program that Write a program that maps a list of words into a list of integers representing the lengths of the correponding words with the word eg ['jonathan', 8, .
# 'horse', 5, 'today', 5 ].
#
# Prérequis Clés :
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
# - Must handle numeric values
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses iteration to process elements.
# ============================================================================
"""
Problème 209 :
Écrivez un programme qui maps une liste de mots dans une liste d'entiers representing le lengths de le correponding words avec le mot par exemple ['jonathan', 8,'horse', 5,'today', 5 ].
"""

# Creates alternating list: word, length, word, length, ...
def list_words(lst):
    # Function definition
    words_lengths = []
    for word in lst:
        # Iterates through each element
        words_lengths.append(word)  # Add word (string)
        words_lengths.append(len(word))  # Add length (integer) using built-in len()
        # Résultat: ["Jonathan", 8, "horse", 5, "today", 5]
    return words_lengths
        # Returns the result

lst = ["Jonathan", "horse", "today"]
print(list_words(lst))


# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires writing a program that Write a program that maps a list of words into a list of integers representing the lengths of the correponding words with the word eg ['jonathan', 8, .
# 'horse', 5, 'today', 5 ]. Do not use len().
#
# Prérequis Clés :
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
# - Must handle numeric values
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses iteration to process elements.
# ============================================================================
"""
Problème 210 :
Écrivez un programme qui maps une liste de mots dans une liste d'entiers representing le lengths de le correponding words avec le mot par exemple ['jonathan', 8,'horse', 5,'today', 5 ]. N'utilisez pas len().
"""

# Same as problem 209, but calculates length manually (no len())
def list_words(lst):
    # Function definition
    words_with_lengths = []
    for word in lst:
        # Iterates through each element
        count = 0  # Manual length counter
        # Count characters by iterating
        for char in word:
            # Iterates through each element
            count += 1  # Increment for each character
        words_with_lengths.append(word)  # Add word
        words_with_lengths.append(count)  # Add manually calculated length

    return words_with_lengths
        # Returns the result

lst = ["Jonathan", "horse", "today"]
print(list_words(lst))


# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires writing a program that Write a program that maps a list of words into a list of integers representing the lengths of the correponding words without using len()..
#
# Prérequis Clés :
# - Program must prompt user for input
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
# - Must handle numeric values
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses recursion to solve the problem.
# ============================================================================
"""
Problème 211 :
Écrivez un programme qui maps une liste de mots dans une liste d'entiers representing le lengths de le correponding words sans en utilisant len().
"""

def length_words(lst):
    # Function definition
    length = []
    for word in lst:
        # Iterates through each element
        count = 0
        for char in word:
            # Iterates through each element
            count += 1
        length.append(count)

    return length
        # Returns the result

lst = ["Jonathan", "chris", "mountain"]
print(length_words(lst))

"""
Problem: 212
Write a Python program to find the intersection of two lists. Prompt the user to enter two lists without using set() and without using intersection().

# Finds common elements using 'in' operator (no set or intersection method)
# Remarque : May include duplicates if lst1 has duplicates
def intersection():
    # Function definition
    lst1 = input("type lst1: ").split()
        # Gets user input
    lst2 = input("type lst2: ").split()
        # Gets user input
    common = []
    for word in lst1:  # Iterate through first list
        if word in lst2:  # Check if word exists in second list (membership test)
            common.append(word)  # Add to common if found
    # Remarque : If lst1 has duplicates, common will also have duplicates
    print(common)

intersection()

"""
Problem: 213
Write a Python program to print the following pattern:\n*\n* *\n* * *\n* * * *\n* * * * *

# Prints right-angled triangle pattern using string multiplication
for i in range(1, 6):  # i = 1, 2, 3, 4, 5
    print('* ' * i)  # String multiplication: '*' * 3 = '***'
    # Prints: "* " (1 time), "* * " (2 times), "* * * " (3 times), etc.

"""
Problem: 214
Write a Python program to print the following number pyramid:\n1\n2 2\n3 3 3\n4 4 4 4\n5 5 5 5 5

# Prints number pyramid: each row repeats the row number
for i in range(1, 6):  # i = 1, 2, 3, 4, 5
    # Convert number to string, add space, multiply by row number
    print((str(i) + ' ') * i)  # str(i) + ' ' creates "1 ", then multiply by i
    # Example: i=3 → "3 " * 3 = "3 3 3 "

"""
Problem: 215
Write a Python program to print a square pattern of stars with a given side length.

# Prints n×n square of stars using nested loops
def square_pattern(n):
    # Function definition
    for i in range(n):  # Outer loop: rows
        for j in range(n):  # Inner loop: columns
            print("*", end=" ")  # Print star with space, end="" prevents newline
        print()  # Print newline after each row
    # Remarque : Function returns None (prints but doesn't return value)
n = 5
print(square_pattern(n))  # Prints square, then prints None

# Interactive version with user input
def print_square_pattern(side_length):
    # Function definition
    for i in range(side_length):  # Rows
        for j in range(side_length):  # Columns
            print("*", end=" ")  # end=" " keeps stars on same line with space
        print()  # Newline after each row completes

side_length = int(input("Enter the side length of the square: "))
    # Gets user input
print_square_pattern(side_length)

"""
Problem: 216
Write a Python program to print a right-angled triangle of numbers:\n1\n1 2\n1 2 3\n1 2 3 4\n1 2 3 4 5

# Prints number triangle using generator expression and join()
for i in range(1, 6):  # i = 1, 2, 3, 4, 5
    # Generator expression: (str(num) for num in range(1, i+1)) creates strings "1", "2", ..., "i"
    # join() combines strings with separator: ' '.join(["1","2"]) → "1 2"
    print(' '.join(str(num) for num in range(1, i + 1)))
    # Example: i=3 → range(1,4) = [1,2,3] → ["1","2","3"] → "1 2 3"

"""
Problem: 217
Write a Python program to print an inverted pyramid pattern:\n* * * * *\n* * * *\n* * *\n* *\n*",

# Prints inverted pyramid: decreasing number of stars per row
for i in range(5, 0, -1):  # range(5, 0, -1) = [5, 4, 3, 2, 1] (negative step)
    # Negative step: start=5, stop=0 (exclusive), step=-1 (counts backwards)
    for j in range(i):  # Print i stars in this row
        print('*', end=' ')  # Print star with space
    print()  # Newline after each row

"""
Problem: 218
Write a Python program to print a checkerboard pattern of given size.

# Prints checkerboard: alternating pattern based on sum of row and column indices
def print_checkerboard(size):
    # Function definition
    for i in range(size):  # Rows
        for j in range(size):  # Columns
            # Checkerboard pattern: if (row + col) is even, print '*', else print space
            # (i + j) % 2 == 0: even sum → '*', odd sum → ' '
            if (i + j) % 2 == 0:  # Even sum: (0,0), (0,2), (1,1), (2,0), etc.
                print('*', end=' ')
            else:  # Odd sum: (0,1), (1,0), (1,2), etc.
                print(' ', end=' ')
        print()  # Newline after each row

size = int(input("Enter the size of the checkerboard: "))
    # Gets user input
print_checkerboard(size)

"""
Problem: 219
Write a Python program to print Floyd's Triangle.\n1\n2 3\n4 5 6\n7 8 9 10

# Floyd's Triangle: consecutive numbers in rows of increasing length
def print_floyds_triangle(rows):
    # Function definition
    num = 1  # Counter for consecutive numbers
    for i in range(1, rows + 1):  # i = 1, 2, 3, 4 (row number)
        for j in range(i):  # Print i numbers in row i
            print(num, end=' ')  # Print current number
            num += 1  # Increment to next number
        print()  # Newline after each row
    # Pattern: row 1 has 1 number, row 2 has 2 numbers, row 3 has 3 numbers, etc.

rows = 4
print_floyds_triangle(rows)

"""
220
Write a Python program to print a diamond pattern of stars for a given number of rows.\nFor example, for 3 rows:\n  *\n ***\n*****\n ***\n

# Prints diamond: upper triangle + lower triangle (inverted)
def print_diamond(rows):
    # Upper triangle: increasing stars
    for i in range(rows):  # i = 0, 1, 2, ..., rows-1
        # Print leading spaces (decreases as i increases)
        for j in range(rows - i - 1):  # Spaces: rows-1, rows-2, ..., 0
            print(" ", end="")  # Print space without newline

        # Print stars: 1, 3, 5, 7, ... (2*i + 1 stars)
        for k in range(2 * i + 1):  # 2*0+1=1, 2*1+1=3, 2*2+1=5
            print("*", end="")
        print()  # Newline after row

    # Lower triangle: decreasing stars (inverted upper triangle)
    for i in range(rows - 2, -1, -1):  # i = rows-2, rows-3, ..., 0 (backwards)
        for j in range(rows - i - 1):  # Leading spaces
            print(" ", end="")

        # BUG: Missing closing parenthesis in range()
        for k in range(2 * i + 1):  # Should have closing )
            print("*", end="")  # Syntax error: missing closing parenthesis
        print()

rows = 3
print_diamond(rows)

"""
Problem: 221
Write a Python program to print a hollow square pattern of stars with a given side length.\nFor example, for side length 5:\n*****\n*   *\n*   *\n*   *\n*****

# Prints hollow square: filled top/bottom rows, hollow middle rows
def print_hollow_square(side_length):
    # Function definition
    for i in range(side_length):  # Rows
        if i == 0 or i == side_length - 1:  # First or last row
            print('*' * side_length)  # Print full row of stars
        else:  # Middle rows
            # Print: star + spaces + star
            # (side_length - 2) spaces in middle
            print('*' + ' ' * (side_length - 2) + '*')  # Hollow row

side_length = 5
print_hollow_square(side_length)

"""
Problem: 222
Write a Python program to print a reverse pyramid pattern of numbers:\n1 2 3 4 5\n1 2 3 4\n1 2 3\n1 2\n1"

# Prints inverted number pyramid: decreasing numbers per row
def print_reverse_pyramid(rows):
    # Function definition
    for i in range(rows, 0, -1):  # i = 5, 4, 3, 2, 1 (backwards)
        for j in range(1, i + 1):  # Print numbers 1 to i
            print(j, end=' ')  # Print number with space
        print()  # Newline after each row
    # Pattern: row 1 prints 1-5, row 2 prints 1-4, ..., row 5 prints 1

rows = 5
print_reverse_pyramid(rows)

"""
223
Write a Python program to print a mirrored right-angled triangle of stars:\n    *\n   **\n  ***\n ****\n*****

# Prints right-angled triangle aligned to the right (with leading spaces)
def mirrored_right_angled_triangle(rows):
    # Function definition
    for i in range(1, rows+1):  # i = 1, 2, 3, 4, 5
        # Print leading spaces (decreases as i increases)
        for j in range(rows-i):  # Spaces: 4, 3, 2, 1, 0
            print(" ", end="")  # Print space without newline

        # Print stars: 1, 2, 3, 4, 5 stars
        for k in range(i):
            # Iterates through each element
            print("*", end=" ")  # Print star with space
        print()  # Newline after row

rows = 5
mirrored_right_angled_triangle(rows)

"""
Problem: 224
description": "Write a Python program to print a triangle pattern of letters:\nA\nB B\nC C C\nD D D D\nE E E E E"

# Prints letter triangle: each row repeats a letter (A, B, C, D, E)
def triangle_pattern(rows):
    # Function definition
    for i in range(rows):  # i = 0, 1, 2, 3, 4
        # chr(65 + i): converts ASCII code to character
        # chr(65) = 'A', chr(66) = 'B', chr(67) = 'C', etc.
        letter = chr(65 + i)  # Get letter for current row
        for j in range(i + 1):  # Print letter (i+1) times
            print(letter, end=" ")  # Print letter with space
        print()  # Newline after row

rows = 5
triangle_pattern(rows)

def triangle_pattern(rows):
    # Function definition
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for i in range(rows):
        # Iterates through each element
        letter = letters[i]
        for j in range(i + 1):
            # Iterates through each element

            print(letter, end=" ")

        print()

rows = 5
triangle_pattern(rows)

"""
Problem: 225
Write a Python program to print a square pattern of numbers:\n1 2 3 4 5\n1 2 3 4 5\n1 2 3 4 5\n1 2 3 4 5\n1 2 3 4 5

# Prints square: same numbers (1 to size) in each row
r = 5 # r = row
c = 5 # c = column

# BUG: Variable 'n' reused in nested loops (outer loop variable overwritten)
for n in range(r): # n = number (outer loop: rows)
    for n in range(1, c + 1):  # BUG: 'n' reused, overwrites outer loop variable
        print(n, end = " ")  # Prints 1, 2, 3, 4, 5
    print()  # Newline after each row

# Correct version with different variable names
def print_square_pattern(size):
    # Function definition
    for i in range(size):  # Rows
        for j in range(1, size + 1):  # Columns: numbers 1 to size
            print(j, end=' ')  # Print number with space
        print()  # Newline after row

size = 5
print_square_pattern(size)

"""
Problem: 226
Write a Python program to print a hollow right-angled triangle of stars:\n*\n* *\n*  *\n*   *\n*****

# Prints hollow triangle: first and last row filled, middle rows hollow
def print_hollow_right_triangle(height):
    # Function definition
    for i in range(height):  # i = 0, 1, 2, 3, 4
        if i == height - 1:  # Last row (i = 4 for height=5)
            print('*' * (i + 1))  # Print full row of stars (5 stars)
        else:  # Middle rows (i = 0, 1, 2, 3)
            # Print: star + spaces + star
            # i spaces in middle (0, 1, 2, 3 spaces)
            print('*' + ' ' * i + '*')  # Hollow row: "*", "* *", "*  *", "*   *"

height = 5
print_hollow_right_triangle(height)

# Duplicate problem definition (same solution)
"""
Problem: 226
Write a Python program to print a hollow right-angled triangle of stars:\n*\n* *\n*  *\n*   *\n*****

def print_hollow_right_triangle(height):
    # Function definition
    for i in range(height):
        # Iterates through each element
        if i == height - 1:
            # Checks condition
            print('*' * (i + 1))
        else:
            print('*' + ' ' * i + '*')

height = 5
print_hollow_right_triangle(height)

"""
Problem: 227
Write a Python program to print a zigzag pattern of stars for a given number of rows.\nFor example, for 5 rows:\n*   *   *\n * * * *\n  *   *\n * * * *\n*   *   *

# Prints zigzag: alternating pattern based on row and column parity
def print_zigzag(rows):
    # Function definition
    for i in range(rows):  # Rows
        for j in range(rows):  # Columns
            # Complex condition: checks row parity and column position
            # Even rows (i%2==0): stars at positions divisible by (rows-1)
            # Odd rows (i%2==1): stars at positions where (j % (rows-1) == 1)
            if (i % 2 == 0 and j % (rows - 1) == 0) or (i % 2 == 1 and j % (rows - 1) == 1):
                # Checks condition
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

rows = 5
print_zigzag(rows)

"""
Problem: 228
Write a Python program to print a cross pattern of stars for a given odd number of rows.\nFor example, for 5 rows:\n*   *\n * *\n  *\n * *\n*   *"

# Prints X pattern (cross): stars on main diagonal and anti-diagonal
def print_cross(rows):
    # Function definition
    for i in range(rows):  # Rows
        for j in range(rows):  # Columns
            # Main diagonal: j == i (top-left to bottom-right)
            # Anti-diagonal: j == (rows - 1 - i) (top-right to bottom-left)
            if j == i or j == (rows - 1 - i):  # On either diagonal
                print('*', end='')  # Print star
            else:
                print(' ', end='')  # Print space
        print()  # Newline after row
    # Example: 5x5 grid, stars at (0,0), (0,4), (1,1), (1,3), (2,2), (3,1), (3,3), (4,0), (4,4)

rows = 5
print_cross(rows)

"""
Problem: 229
Write a Python program to print an hourglass pattern of stars:\n*****\n ***\n  *\n ***\n*****

# Prints hourglass: decreasing then increasing stars with spaces
# Remarque : Current implementation may not match expected pattern exactly
def print_hourglass(rows):
    # Function definition
    for i in range(rows):  # i = 0, 1, 2, 3
        # Leading spaces: 0, 1, 2, 3 spaces
        # Stars: (rows - i*2) = 4, 2, 0, -2 (negative for i=3, 4)
        print(' ' * i + '*' * (rows - i * 2))  # May produce incorrect pattern for some rows
    # Remarque : For rows=4, this prints: "****", " **", "", "**" (may need adjustment)

rows = 4
print_hourglass(rows)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# count_occurrences that takes a list of elements as input and returns the number of times the elements appears in the list.
#
# Prérequis Clés :
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
# - Must handle numeric values
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses iteration to process elements.
# ============================================================================
"""
Problème 230 :
Écrivez une fonction Python appelée count_occurrences qui prend une liste d'éléments en entrée et retourne le nombre de fois éléments apparaît dans la liste.
"""

# Counts frequency of each element in list (returns dictionary)
def count_occurrences(lst):
    # Function definition
    result = {}  # Dictionary: element → count
    for word in lst:  # Iterate over all elements
        if word in result:  # Element seen before
            result[word] += 1  # Increment count
        else:  # First occurrence
            result[word] = 1  # Initialize count to 1
    # Returns dictionary with frequency of each element
    return result
    # Remarque : collections.Counter(lst) provides built-in alternative

lst = ["tom", "fred", "tom", "chris", "fred"]
print(count_occurrences(lst))  # Sortie : {'tom': 2, 'fred': 2, 'chris': 1}


# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function that find the sum of all odd numbers in a list. Prompt the user to enter a list of numbers. Write the function as sort as possible..
#
# Prérequis Clés :
# - Program must prompt user for input
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
# - Must handle numeric values
# - Must sort elements in the specified order
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses iteration to process elements.
# ============================================================================
"""
Problème 231 :
Écrivez un programme Python à trouver le somme de tous les nombres impairs dans une liste. demander le utilisateur à saisir une liste de nombres. Write la fonction as trier as possible.
"""

# Sums odd numbers (concise version)
def sum_of_odd():
    # Function definition
    user = input("type numbers: ").split()
        # Gets user input
    count = 0  # Variable name misleading - stores sum
    for number in user:
        # Iterates through each element
        number = int(number)  # Convert to int
        if number % 2 != 0:  # Check if odd
            count += number  # Add odd number to sum
    print(count)

sum_of_odd()


# ============================================================================
# EXPLICATION DU PROBLÈME :
# remove vowels from a string. Prompt the user to enter a string. Do not use append().
#
# Prérequis Clés :
# - Program must prompt user for input
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with strings
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses iteration to process elements.
# ============================================================================
"""
Problème 232 :
Écrivez un programme Python à remove voyelles de une chaîne. demander le utilisateur à saisir une chaîne. N'utilisez pas append().
"""

# Removes vowels by printing non-vowel characters directly (no append())
def remove_vowels():
    # Function definition
    user = input("type string: ")
        # Gets user input
    for char in user:
        # Iterates through each element
        if char not in "aeiou":  # Only checks lowercase vowels (case-sensitive)
            print(char, end= "")  # Print char without newline (end="" prevents newline)
    # Remarque : Doesn't return string, just prints (could build string with += instead of append)

remove_vowels()


# ============================================================================
# EXPLICATION DU PROBLÈME :
# find_min that takes a list of numbers as input and returns the minimum number in the list. Do not use min().
#
# Prérequis Clés :
# - Program must prompt user for input
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
# - Must handle numeric values
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses recursion to solve the problem.
# ============================================================================
"""
Problème 233 :
Écrivez une fonction Python appelée `find_min` qui prend une liste de nombres en entrée et retourne le minimum nombre dans la liste. N'utilisez pas min().
"""

def find_min(lst):
    # Function definition
    min_num = lst[0]
    for number in lst:
        # Iterates through each element
        if number < min_num:
            min_num = number
    return min_num
        # Returns the result

lst = [13, 566, 1]
print(find_min(lst))

"""
Problem: 234
Write a Python program to print a square pattern of stars with a given side length. Use a while loop.

# Prints square using while loop (hardcoded size 5)
i = 1  # Loop counter

while (i < 6):  # Loop 5 times (i = 1, 2, 3, 4, 5)
    print("* " * 5)  # Print 5 stars with spaces (hardcoded, not using variable)
    i += 1  # Increment counter
    # Remarque : Could use i in condition: while i <= 5, or use range() in for loop

"""
Problem: 235
Write a Python program that prints a increasing triangle pattern of stars.

def increasing_triangle():
    # Function definition
    n = 5

    for i in range(n):
        # Iterates through each element
        for i in range(i+1):
            # Iterates through each element
            print("*", end=" ")
        print()

print(increasing_triangle())

"""
Problem: 236
Write a Python program that prints a decreasing triangle pattern of stars.

# Prints inverted triangle: decreasing stars per row
def decreasing_triangle():
    # Function definition
    n = 5
    for i in range(n):  # i = 0, 1, 2, 3, 4
        # range(i, n): starts from i, goes to n-1
        # i=0: range(0,5) = 5 stars, i=1: range(1,5) = 4 stars, etc.
        for j in range(i, n):  # Print (n-i) stars
            print("*", end=" ")
        print()

print(increasing_triangle())  # BUG: Calls wrong function (should be decreasing_triangle())

"""
Problem: 237
Write a Python program that prints a right triangle pattern of stars.

# Simple version using string multiplication
for i in range(1, 6):  # i = 1, 2, 3, 4, 5
    # ("*" + " ") creates "* ", multiply by i
    print((("*") + " ")* i)  # Prints: "* ", "* * ", "* * * ", etc.

# Function version with parameter
def right_triangle(n):
    # Function definition
    for i in range(1, n + 1):  # Rows: 1 to n
        for j in range(i):  # Print i stars
            print("*", end=" ")  # Print star with space
        print()  # Newline after row

number = 5
right_triangle(number)


"""
Problem: 238
Write a Python program that prints a left triangle pattern of stars.

def left_triangle():
    # Function definition
    n = 5
    for i in range(n):
        # Iterates through each element
        for i in range(i, n):
            # Iterates through each element
            print(" ", end=" ")
    for i in range(n):
        # Iterates through each element
        for i in range(i + 1):
            # Iterates through each element
            print("*", end=" ")
        print()

print(increasing_triangle())

"""
Problem: 239
Write a Python program that prints a hill pattern of stars.

# Prints pyramid/hill: increasing stars with centered alignment
def print_hill_pattern(rows):
    # Function definition
    for i in range(rows):  # i = 0, 1, 2, 3, 4
        # Leading spaces: decreases as i increases (4, 3, 2, 1, 0)
        # Stars: 1, 3, 5, 7, 9 (2*i + 1)
        print(' ' * (rows - i - 1) + '*' * (2 * i + 1))
        # Example: i=2 → "  " + "*****" = "  *****" (centered)

rows = 5
print_hill_pattern(rows)

"""
Problem: 240
Write a Python program that prints a reverse hill pattern of stars.

# Prints inverted pyramid: decreasing stars with centered alignment
def print_reverse_hill_pattern(rows):
    # Function definition
    for i in range(rows):  # i = 0, 1, 2, 3, 4
        # Leading spaces: increases as i increases (0, 1, 2, 3, 4)
        # Stars: 9, 7, 5, 3, 1 (2*(rows-i) - 1)
        print(' ' * i + '*' * (2 * (rows - i) - 1))
        # Example: i=1, rows=5 → " " + "*******" = " *******" (centered)

rows = 5
print_reverse_hill_pattern(rows)
"""
Problem: 241
Write a Python program to print the index and value of each element in a list using `enumerate()`

# enumerate() returns (index, value) pairs - useful for accessing both index and element
def enumerate_lst(lst):
    # enumerate(lst) returns iterator of (index, value) tuples
    # Unpacking: index gets the index, word gets the value
    for index, word in enumerate(lst):  # enumerate() provides index-value pairs
        # f-string: embeds variables in string using {variable}
        print(f"index {index} name {word}")  # Prints: "index 0 name Jon", etc.
    # Remarque : Function returns None (prints but doesn't return value)


lst = ["Jon", "Chris", "Nathan"]
print(enumerate_lst(lst))  # Prints indices/values, then prints None

"""
Problem: 242
Write a Python program to create a list of tuples where each tuple contains the index and the value from a given list using `enumerate()`.

# Creates list of (index, value) tuples using enumerate()
def enumerate_lst(lst):
    # Function definition
    result = []
    # enumerate() returns (index, value) pairs: (0, "Jon"), (1, "Chris"), (2, "Nathan")
    for index, word in enumerate(lst):
        # Iterates through each element
        result.append((index, word))  # Append tuple (index, word) to list
        # Tuple syntax: (a, b) creates immutable pair
    return result  # Retourne : [(0, "Jon"), (1, "Chris"), (2, "Nathan")]

lst = ("Jon", "Chris", "Nathan")  # Remarque : tuple input (works with any iterable)
print(enumerate_lst(lst))

"""
Problem: 243
Write a Python program to find the index of the first occurrence of a specific value in a list using `enumerate()`.

def enumerate_lst(lst, target):
    # Function definition
    for index, word in enumerate(lst):
        # Iterates through each element
        if word == target:
            # Checks condition
            return word, index
                # Returns the result
    return -1
        # Returns the result

target = "Chris"
lst = ["Jon", "Chris", "Nathan"]
print(enumerate_lst(lst, target))

"""
Problem: 244
Write a Python program to print the index and value of each element in a list starting from index 1 using `enumerate()`

# enumerate() with start parameter: customizes starting index
def enumerate_lst(lst):
    # enumerate(lst, start=1): starts counting from 1 instead of 0
    # Retourne : (1, "Jon"), (2, "Chris"), (3, "Nathan")
    for index, word in enumerate(lst, start=1):  # start parameter sets initial index
        print(f"Index {index}, Name {word}")  # Prints: "Index 1, Name Jon", etc.
    # Remarque : start parameter doesn't change list indexing, just the counter value

lst = ["Jon", "Chris", "Nathan"]
enumerate_lst(lst)


"""
Problem: 245
Write a Python program to create a dictionary where keys are the indexes and values are the corresponding elements from a list using `enumerate()`.

# Creates dictionary mapping index → value using enumerate()
def enumerate_lst(lst):
    # Function definition
    result = {}  # Dictionary: index → value
    # enumerate() provides (index, value) pairs
    for index, word in enumerate(lst):
        # Iterates through each element
        result[index] = word  # Assign value to index key
    # Résultat: {0: "Jon", 1: "Chris", 2: "Nathan"}
    print(result)
    # Remarque : dict(enumerate(lst)) is more concise alternative

lst = ["Jon", "Chris", "Nathan"]
enumerate_lst(lst)

"""
Problem: 246
Write a Python program to filter and print elements of a list that are at even indexes using `enumerate()`

# BUGGY: Filters odd indexes instead of even indexes
def enumerate_lst(lst):
    # Function definition
    for index, word in enumerate(lst):
        # BUG: index % 2 != 0 checks for ODD indexes, not even
        # Should be: index % 2 == 0 for even indexes
        if index % 2 != 0:  # This filters odd indexes (1, 3, 5, ...)
            print(index, word)  # Prints elements at odd positions

lst = ["Jon", "Chris", "Nathan", "hot", "class", "shirt", "beach", "app", " board", "hit"]
enumerate_lst(lst)  # Prints: 1 Chris, 3 hot, 5 shirt, 7 app, 9 hit (odd indexes)

"""
Problem: 247
Write a Python program to print the index and value of each element in a list using a `for` loop with `enumerate()`.

def enumerate_lst(lst):
    # Function definition
    for index, word in enumerate(lst):
        # Iterates through each element
        print(f"index {index} name {word}")

lst = ["Jon", "Chris", "Nathan", "Sam", "Rachel"]
enumerate_lst(lst)

"""
Problem: 248
Write a Python program to replace each element in a list with its index using `enumerate()`

# Replaces list elements with their indices (modifies original list)
def replace_with_index(lst):
    # enumerate() provides index-value pairs
    # _ (underscore) discards the value since we only need the index
    for index, _ in enumerate(lst):  # _ is conventional name for unused variable
        lst[index] = index  # Replace element at index with index value itself
    return lst  # Returns modified list: [0, 1, 2, 3, 4]
    # Remarque : Modifies list in-place (mutates original list)

lst = ["Jon", "Chris", "Nathan", "Sam", "Rachel"]
print(replace_with_index(lst))  # Sortie : [0, 1, 2, 3, 4]

"""
Problem: 249
Write a Python program to print the index and values from two lists of equal length side by side using `enumerate()`.

# Uses enumerate() on one list, accesses corresponding element from second list
def enumerate_lst(lst1, lst2):
    # enumerate() provides index from lst1, use same index to access lst2
    for index, word in enumerate(lst1):  # Get index and value from lst1
        # Use same index to access corresponding element in lst2
        print(f"index {index}: {word} and {lst2[index]}")  # Prints both values side by side
    # Remarque : Assumes lists have same length (will error if lst2 is shorter)

lst1 = ["Jon", "Chris", "Nathan", "Tom", "Sam", "Rose", "Bliss", "Hurt"]
lst2 = ["Jonny", "Christopher", "Jhovian", "Tom", "Zack", "Rose", "Brad", "Michael"]

enumerate_lst(lst1, lst2)

"""
Problem: 250
Write a Python program to calculate the sum of elements in a list that are located at odd indexes using `enumerate()`.

# Sums elements at odd-indexed positions (1, 3, 5, ...) using enumerate()
def sum_odd_indexed_elements(lst):
    # Function definition
    total = 0
    # enumerate() provides (index, value) pairs
    for index, value in enumerate(lst):
        # Iterates through each element
        if index % 2 != 0:  # Check if index is odd (1, 3, 5, ...)
            total += value  # Add value to sum
    return total
    # Example: [1, 2, 3, 4, 5, 6] → sum of indices 1,3,5 → 2+4+6 = 12

lst = [1, 2, 3, 4, 5, 6]
result = sum_odd_indexed_elements(lst)  # Sums elements at indices 1, 3, 5: 2+4+6 = 12
print(result)

"""
Problem: 251
Write a Python program to pair elements from two lists of equal length using `zip()`.

# zip() pairs corresponding elements from multiple iterables
def pair_elements(lst1, lst2):
    # zip(lst1, lst2) returns iterator of tuples: ("Jon", "A"), ("Chris", "B"), ...
    # list() converts iterator to list
    paired = list(zip(lst1, lst2))  # zip() pairs elements at same index
    return paired  # Retourne : [("Jon", "A"), ("Chris", "B"), ("Nathan", "C"), ("Sam", "D")]
    # zip() stops when shortest iterable is exhausted

lst1 = ["Jon", "Chris", "Nathan", "Sam"]
lst2 = ["A", "B", "C", "D"]

print(pair_elements(lst1, lst2))


"""
Problem: 252
Write a Python program to find the sum of corresponding elements from two lists using `zip()`.

def sum_of_2_lst(lst1, lst2):
    # Function definition
    summed_list = []
    for x, y in zip(lst1, lst2):
        # Iterates through each element
        summed_list.append(x + y)
    return summed_list
        # Returns the result

lst1 = [2, 4, 6, 8]
lst2 = [2, 4, 6, 8]

print(sum_of_2_lst(lst1, lst2))

"""
Problem: 253
Write a Python function to sort a list of tuples by the second element in each tuple using the key parameter.

# Sorts tuples by second element using key parameter with lambda function
def sort_tuples_by_second(tuples_list):
    # sorted() with key parameter: specifies what to compare
    # lambda x: x[1] is anonymous function that returns second element of tuple
    # lambda syntax: lambda arguments: expression
    return sorted(tuples_list, key=lambda x: x[1])  # Sort by x[1] (second element)
    # Résultat: sorted by second element: [(5,1), (3,2), (1,3)]

tuples_list = [(1, 3), (3, 2), (5, 1)]
result = sort_tuples_by_second(tuples_list)  # Sorted by second element: 3, 2, 1
print(result)

"""
Problem: 254
Write a Python program to create a dictionary from two lists, one for keys and one for values, using `zip()`.

# Creates dictionary from two lists using zip() to pair keys and values
def dic_lst(lst1, lst2):
    # Function definition
    result = {}
    # zip() pairs corresponding elements: (1, "Ron"), (2, "break"), ...
    for x, y in zip(lst1, lst2):  # x from lst1 (key), y from lst2 (value)
        result[x] = y  # Assign value y to key x
    return result  # Retourne : {1: "Ron", 2: "break", 3: "tree", 4: "son"}
    # Remarque : dict(zip(lst1, lst2)) is more concise alternative

lst1 = [1, 2, 3, 4]
lst2 = ["Ron", "break", "tree", "son"]
print(dic_lst(lst1, lst2))

"""
Problem: 255
Write a Python program to combine three lists into a list of tuples using `zip()`.
# zip() can combine multiple iterables (not just two)
def combine_3_lst(lst1, lst2, lst3):
    # Function definition
    result = []
    # zip() can take multiple arguments: pairs elements from all iterables
    # zip(lst1, lst2, lst3) returns: ("Sam", "Sammy", "Son"), ("Nike", "Mikey", "monkey"), ...
    for x, y, z in zip(lst1, lst2, lst3):  # Unpack three elements from zip()
         result.append((x, y, z))  # Append tuple of three elements

    return result  # Retourne : [("Sam", "Sammy", "Son"), ("Nike", "Mikey", "monkey"), ...]

lst1 = ["Sam", "Nike", "system"]
lst2 = ["Sammy", "Mikey", "Steven"]
lst3 = ["Son", "monkey", "star"]
print(combine_3_lst(lst1, lst2, lst3))

"""
Problem: 256
Write a Python program to transpose a 2D matrix (list of lists) using `zip()`.

# Transposes matrix: rows become columns, columns become rows
def transpose_matrix(matrix):
    # *matrix unpacks matrix rows as separate arguments to zip()
    # zip(*matrix) pairs elements at same column index across rows
    # zip([1,2,3], [4,5,6], [7,8,9]) → (1,4,7), (2,5,8), (3,6,9)
    transposed = zip(*matrix)  # * operator unpacks iterable as arguments
    result = []
    for row in transposed:  # Each row is a tuple from zip()
        result.append(list(row))  # Convert tuple to list

    return result  # Retourne : [[1,4,7], [2,5,8], [3,6,9]]
    # Remarque : list(zip(*matrix)) is more concise but returns list of tuples
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(transpose_matrix(matrix))

"""
Problem: 257
Write a Python program to unzip a list of tuples into individual lists using `zip()`.

# Unzips list of tuples: separates tuple elements into separate lists
def list_tuples(lst):
    # *lst unpacks list of tuples as separate arguments to zip()
    # zip(*[(1,2,3), (4,5,6), (7,8,9)]) → zip((1,2,3), (4,5,6), (7,8,9))
    # → (1,4,7), (2,5,8), (3,6,9) - groups elements by position
    unzipped = zip(*lst)  # Unzip: groups elements at same index
    result = []
    for x in unzipped:  # Each x is a tuple of elements at same position
        result.append(list(x))  # Convert tuple to list
    # Retourne : [[1,4,7], [2,5,8], [3,6,9]] - transposed/unzipped
    # Remarque : Function doesn't return result (missing return statement)


lst = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
print(list_tuples(lst))  # Prints None (function doesn't return)

"""
Problem: 258
Write a Python program to unzip a list of tuples into individual lists using `zip()`.

def individualists(lst):
    # Function definition
    result = []
    for num in zip(*lst):
        # Iterates through each element
        result.append(list(num))

    return result
        # Returns the result

lst = [(1, 2, 3), (4, 5, 6)]
print(individualists(lst))

"""
Problem: 259
Write a Python program to find the element-wise maximum of two lists using `zip()`.

# Element-wise maximum: compares corresponding elements, takes larger
def maxium_element_wise(lst1, lst2):  # Typo: "maxium" should be "maximum"
    # Function definition
    result = []
    # zip() pairs: (2,7), (4,8), (6,9)
    for x, y in zip(lst1, lst2):
        # Iterates through each element
        result.append(max(x, y))  # max() compares two values, returns larger
    return result  # Retourne : [7, 8, 9] (maximum of each pair)

lst1 = [2, 4, 6]
lst2 = [7, 8, 9]
print(maxium_element_wise(lst1, lst2))

"""
Problem: 260
Write a Python program to concatenate corresponding strings from two lists using `zip()`

# Element-wise string concatenation: joins corresponding strings
def concatenate(lst1, lst2):
    # Function definition
    result = []
    # zip() pairs: ("fruite", "orange"), ("apple", "banana"), ("tomato", "carrot")
    for x, y in zip(lst1, lst2):
        # f-string: embeds variables in string, concatenates with space
        result.append(f"{x} {y}")  # f"{x} {y}" creates "x y"
    return result  # Retourne : ["fruite orange", "apple banana", "tomato carrot"]

lst1 = ["fruite", "apple", "tomato"]  # Typo: "fruite" should be "fruit"
lst2 = ["orange", "banana", "carrot"]
print(concatenate(lst1, lst2))

"""
Problem: 261
Write a Python program to combine two lists into a list of dictionaries using `zip()`. Each dictionary should have keys 'a' and 'b'.

# Creates list of dictionaries from two lists using zip()
def combine_to_dict(lst1, lst2):
    # Function definition
    result = []
    # zip() pairs: (1, "one"), (2, "two"), (3, "three")
    for x, y in zip(lst1, lst2):
        # Dictionary literal: {'a': x, 'b': y} creates dict with keys 'a' and 'b'
        result.append({'a': x, 'b': y})  # Append dictionary to list

    return result  # Retourne : [{'a':1, 'b':'one'}, {'a':2, 'b':'two'}, {'a':3, 'b':'three'}]

lst1 = [1, 2, 3]
lst2 = ['one', 'two', 'three']
print(combine_to_dict(lst1, lst2))


"""
Problem: 262
Write a Python program to filter pairs of elements from two lists where the first element is greater than the second using `zip()`.

# Filters pairs where first element > second element
def filter_pairs(lst1, lst2):
    # Function definition
    result = []
    # zip() pairs: (5,4), (8,7), (3,6), (10,2)
    for x, y in zip(lst1, lst2):
        # Iterates through each element
        if x > y:  # Condition: first element greater than second
            result.append((x, y))  # Append tuple if condition met

    return result  # Retourne : [(5,4), (8,7), (10,2)] (pairs where x > y)

lst1 = [5, 8, 3, 10]
lst2 = [4, 7, 6, 2]
print(filter_pairs(lst1, lst2))

"""
Problem: 263
Write a Python program to filter pairs of elements from two lists where the first element is lesser than the second using `zip()`.

# Filters pairs where first element < second element
def filter_pairs(lst1, lst2):
    # Function definition
    result = []
    # zip() pairs: (5,4), (8,7), (3,6), (10,2)
    for x, y in zip(lst1, lst2):
        # Iterates through each element
        if x < y:  # Check if first element is less than second
            result.append((x, y))  # Add tuple if condition met

    return result  # Retourne : [(3,6)] - only pair where x < y

lst1 = [5, 8, 3, 10]
lst2 = [4, 7, 6, 2]
print(filter_pairs(lst1, lst2))

"""
Problem: 264
Write a Python program to add corresponding elements of nested lists using `zip()`.
lst1 = [[1, 2, 3], [4, 5, 6]]
lst2 = [[7, 8, 9], [10, 11, 12]]
result:
[[8, 10, 12], [14, 16, 18]]

# Element-wise addition of nested lists: uses zip() twice (outer and inner)
def add_nested_lists(lst1, lst2):
    # Function definition
    result = []
    # Outer zip(): pairs corresponding sublists
    # zip([[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]) → ([1,2,3], [7,8,9]), ([4,5,6], [10,11,12])
    for sublist1, sublist2 in zip(lst1, lst2):
        # Iterates through each element
        added_sublist = []
        # Inner zip(): pairs elements within each sublist
        # zip([1,2,3], [7,8,9]) → (1,7), (2,8), (3,9)
        for x, y in zip(sublist1, sublist2):
            # Iterates through each element
            added_sublist.append(x + y)  # Add corresponding elements
        result.append(added_sublist)  # Append summed sublist
    return result  # Retourne : [[8,10,12], [14,16,18]]

    return result
        # Returns the result

lst1 = [[1, 2, 3], [4, 5, 6]]
lst2 = [[7, 8, 9], [10, 11, 12]]
print(add_nested_lists(lst1, lst2))

"""
Problem: 265
Write a Python program to calculate the Euclidean distance between two points in 2D space using `zip()`.

# Euclidean distance: sqrt(sum of squared differences)
import math

def euclidean_distance(point1, point2):
    # Function definition
    distance_squared = 0
    # zip() pairs corresponding coordinates: (3,6), (4,8)
    for x1, x2 in zip(point1, point2):
        # Calculate squared difference for each dimension
        distance_squared += (x1 - x2) ** 2  # (x1-x2)², sum all dimensions

    # Square root of sum of squared differences
    return math.sqrt(distance_squared)  # sqrt((3-6)² + (4-8)²) = sqrt(9+16) = 5
    # Formula: √[(x₁-x₂)² + (y₁-y₂)²]

point1 = (3, 4)
point2 = (6, 8)
print(euclidean_distance(point1, point2))  # Sortie : 5.0

"""
Problem: 266
Write a Python program to interleave two lists into a single list using `zip()`.

# Interleaves two lists: alternates elements from each list
def interleave(lst1, lst2):
    # Function definition
    result = []
    # zip() pairs: ("crissy", "spotty"), ("missy", "motty"), ("sissy", "hotty")
    for x, y in zip(lst1, lst2):
        # Iterates through each element
        result.append(x)  # Add element from first list
        result.append(y)  # Add element from second list (alternating)
    return result  # Retourne : ["crissy", "spotty", "missy", "motty", "sissy", "hotty"]
    # Pattern: [lst1[0], lst2[0], lst1[1], lst2[1], ...]

lst1 = ["crissy", "missy", "sissy"]
lst2 = ["spotty", "motty", "hotty"]
print(interleave(lst1, lst2))

"""
Problem: 267
Write a Python program to multiply corresponding elements of two lists using `zip()`.

# Element-wise multiplication: multiplies corresponding elements from two lists
def multiply_2_lst(lst1, lst2):
    # Function definition
    result = []
    # zip() pairs corresponding elements: (2,3), (4,6), (6,9)
    # zip() iterates through both lists simultaneously, pairing elements at the same index
    for x, y in zip(lst1, lst2):
        # Multiply corresponding elements and append to result
        result.append(x * y)  # 2*3=6, 4*6=24, 6*9=54
    return result  # Retourne : [6, 24, 54]
    # zip() stops when the shortest list is exhausted

lst1 = [2, 4, 6]
lst2 = [3, 6, 9]
print(multiply_2_lst(lst1, lst2))  # Sortie : [6, 24, 54]

"""
Problem: 268
Write a Python program to calculate the dot product of two vectors represented as lists using `zip()`.

# Dot product: sum of element-wise products
def dot_product(vector1, vector2):
    # Function definition
    result = 0  # Accumulator for sum
    # zip() pairs: (1,4), (2,5), (3,6)
    for x, y in zip(vector1, vector2):
        # Iterates through each element
        result += x * y  # Multiply and accumulate: 1*4 + 2*5 + 3*6
    return result  # Retourne : 4 + 10 + 18 = 32
    # Dot product formula: Σ(xᵢ × yᵢ) for all i

vector1 = [1, 2, 3]
vector2 = [4, 5, 6]
print(dot_product(vector1, vector2))  # Sortie : 32

"""
Problem: 269
Write a Python program to filter out all even numbers from a list using `filter()`.

# Function name misleading - actually filters OUT even numbers (keeps odd numbers)
def is_odd(x):
    # Modulo operator % returns remainder after division
    # x % 2 != 0 means x is not divisible by 2 (i.e., odd number)
    return x % 2 != 0  # Returns True for odd numbers (1, 3, 5, ...)

def filter_even_numbers(lst):  # Name suggests keeping evens, but actually removes them
    # filter() is a higher-order function that takes a predicate function and an iterable
    # filter(is_odd, lst) keeps only elements where is_odd returns True (odd numbers)
    # filter() returns an iterator, so list() converts it to a list
    return list(filter(is_odd, lst))  # Retourne : [1, 3, 5] (odd numbers only)
    # filter() applies is_odd to each element and keeps those that return True

lst = [1, 2, 3, 4, 5, 6]
result = filter_even_numbers(lst)  # Filters out evens, keeps odds: [1, 3, 5]
print(result)

"""
Problem: 270
Write a Python program to filter out all odd numbers from a list using `filter()`.

# filter() keeps elements where function returns True
def is_even(x):
    # Function definition
    return x % 2 == 0  # Returns True for even numbers

def filter_odd_numbers(lst):  # Function name misleading - filters to keep even numbers
    # filter(is_even, lst) keeps only even numbers (filters out odd numbers)
    return list(filter(is_even, lst))  # filter() returns iterator, convert to list
    # filter() is higher-order function: takes function and iterable

lst = [1, 2, 3, 4, 5, 6]
result = filter_odd_numbers(lst)  # Keeps even numbers: [2, 4, 6]
print(result)

"""
Problem: 271
Write a Python program to filter out all positive numbers from a list using `filter()`.

# Function name misleading - actually filters OUT positive numbers (keeps non-positive)
def is_non_positive(x):
    # Function definition
    return x <= 0  # Returns True for 0 and negative numbers

def filter_positive_numbers(lst):  # Name suggests keeping positives, but actually removes them
    # filter() keeps elements where is_non_positive returns True
    return list(filter(is_non_positive, lst))  # Retourne : [-2, -1, 0] (non-positive numbers)

lst = [-2, -1, 0, 1, 2, 3]
result = filter_positive_numbers(lst)
print(result)￼

"""
Problem: 272
Write a Python program to filter out all negative numbers from a list using `filter()`.

def is_non_negative(x):
    # Function definition
    return x >= 0
        # Returns the result

def filter_negative_numbers(lst):
    # Function definition
    return list(filter(is_non_negative, lst))
        # Returns the result

lst = [-2, -1, 0, 1, 2, 3]
result = filter_negative_numbers(lst)
print(result)

"""
273
Write a Python program to filter out all words from a list that start with a specific letter using `filter()`.

# Filters OUT words starting with given letter (keeps words that don't start with it)
def filter_words_starting_with_letter(words, letter):
    # Function definition
    def starts_with(word):
        # startswith() checks if string begins with given letter
        return not word.startswith(letter)  # Returns True if word does NOT start with letter

    # filter() keeps elements where starts_with returns True (words not starting with letter)
    filtered_words = filter(starts_with, words)
    return list(filtered_words)  # Returns words that don't start with "a": ["banana", "cherry", "blueberry"]

words = ["apple", "banana", "cherry", "apricot", "blueberry"]
letter = "a"
filtered_words = filter_words_starting_with_letter(words, letter)
print(filtered_words)

"""
Problem: 274
Write a Python program to filter out all palindromes from a list of strings using `filter()`.

def is_palindrome(s):
    # Function definition
    return s == s[::-1]
        # Returns the result

def filter_palindromes(lst):
    # Function definition
    return list(filter(is_palindrome, lst))
        # Returns the result

lst = ['madam', 'hello', 'racecar', 'world', 'level']
result = filter_palindromes(lst)
print(result)

"""
275
Write a Python program to filter out all strings from a list that have a specific length using `filter()`.

# Filters strings with specific length (keeps them)
def filter_by_length(strings, length):
    # Function definition
    def check_length(s):
        # Function definition
        return len(s) == length  # Returns True if string length matches
    # filter() keeps elements where check_length returns True
    return list(filter(check_length, strings))  # Returns strings with length 5: ["apple", "date"]

strings = ["apple", "banana", "cherry", "date", "fig"]
length = 5
result = filter_by_length(strings, length)
print(result)

# Duplicate la définition de fonction (same logic)
def filter_by_length(strings, length):
    # Function definition

    def has_length(s):
        # Function definition
        return len(s) == length
            # Returns the result

    filtered_strings = filter(has_length, strings)

    return list(filtered_strings)
        # Returns the result

strings = ["apple", "banana", "cherry", "date", "fig"]
length = 5
result = filter_by_length(strings, length)

print(result)

"""
Problem: 276
Write a Python program to filter out all numbers from a list that are divisible by a given number using `filter()`.

# Filters numbers divisible by divisor (keeps them)
def filter_divisible(numbers, divisor):
    # Nested function can access outer scope variable 'divisor' (closure)
    def is_divisible(n):
        # Function definition
        return n % divisor == 0  # Returns True if n is divisible by divisor
    # filter() keeps elements where is_divisible returns True
    return list(filter(is_divisible, numbers))  # Retourne : [10, 15, 20, 25, 30, 35, 40] (all divisible by 5)

numbers = [10, 15, 20, 25, 30, 35, 40]
divisor = 5
result = filter_divisible(numbers, divisor)
print(result)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# filter out all numbers from a list that are divisible by a given number using filter().
#
# Prérequis Clés :
# - Program must prompt user for input
# - Function must accept appropriate parameters
# - Function must return the expected result
# - Must work with lists
# - Must handle numeric values
#
# Exemple d'Entrée/Sortie :
# - (See test cases in the code below for specific examples)
#
# Algorithm: Uses recursion to solve the problem.
# ============================================================================
"""
Problème 277 :
Écrivez un programme Python à filtrer out tous nombres de une liste qui sont divisible by une donnée nombre en utilisant `filtrer()`.
"""

def is_not_divisible(num, divisor):
    # Function definition
    return num % divisor != 0
        # Returns the result

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
divisor = 3

filtered_numbers = list(filter(is_not_divisible, numbers))
print(filtered_numbers)  # Sortie : [1, 2, 5, 7, 8, 10]

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires filtering out empty strings from a list, keeping only
# non-empty strings. The function should use Python's built-in `filter()` function
# to create a new list containing only strings that have at least one character.
# This is une opération courante data cleaning operation when processing text data.
#
# Prérequis Clés :
# - Function must accept a list of strings as input
# - Function must use `filter()` to remove empty strings
# - Function must return a new list with only non-empty strings
# - Empty strings ("") should be removed from the result
#
# Exemple d'Entrée/Sortie :
# - filter_non_empty(["apple", "", "banana", "", "cherry"]) should return ["apple", "banana", "cherry"]
# - filter_non_empty(["", "", ""]) should return [] (all empty)
# - filter_non_empty(["hello", "world"]) should return ["hello", "world"] (no empty strings)
#
# The `filter()` function takes a predicate function and an iterable, returning
# an iterator of elements for which the predicate returns True.
# ============================================================================
"""
Problem: 278
Write a Python program to filter out all non-empty strings from a list using `filter()`.

# EXPLICATION DE LA SOLUTION :
# This solution uses a nested helper function `is_non_empty()` that checks if a
# string is not empty. The `filter()` function applies this predicate to each
# element in the list, keeping only those strings where `is_non_empty()` returns True.
# The result is converted to a list using `list()` since `filter()` returns an iterator.
def filter_non_empty(strings):
    # Function definition
    def is_non_empty(s):
        # Function definition
        return s != ""  # Returns True if string is not empty
    # filter() keeps elements where is_non_empty returns True
    return list(filter(is_non_empty, strings))  # Retourne : ["apple", "banana", "cherry", "date"]

strings = ["apple", "", "banana", "", "cherry", "date", ""]
result = filter_non_empty(strings)
print(result)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem asks us to filter a list of numbers to keep only prime numbers.
# A prime number is a natural number greater than 1 that has no positive divisors
# other than 1 and itself. The function should use `filter()` to create a new list
# containing only the prime numbers from the input list.
#
# Prérequis Clés :
# - Function must accept a list of numbers as input
# - Function must use `filter()` to keep only prime numbers
# - Function must return a new list with only prime numbers
# - Must correctly identify prime numbers (numbers > 1 with no divisors other than 1 and itself)
#
# Exemple d'Entrée/Sortie :
# - filter_prime([2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) should return [2, 3, 5, 7, 11]
# - filter_prime([1, 2, 3, 4]) should return [2, 3] (1 is not prime)
# - filter_prime([10, 12, 14, 15]) should return [] (no primes)
#
# Algorithm: Check if a number is prime by testing divisibility from 2 to sqrt(n).
# ============================================================================
"""
Problem: 279
Write a Python program to filter out all prime numbers from a list using `filter()`.

# EXPLICATION DE LA SOLUTION :
# This solution uses a nested helper function `is_prime()` that implements the
# standard prime checking algorithm. For efficiency, it only checks divisors up
# to the square root of the number. The `filter()` function applies this predicate
# to keep only prime numbers from the input list.
def filter_prime(numbers):
    # Function definition
    def is_prime(n):
        # Function definition
        if n < 2:
            return False
                # Returns the result
        for i in range(2, int(n**0.5) + 1):
            # Iterates through each element
            if n % i == 0:
                # Checks condition
                return False
                    # Returns the result
        return True
            # Returns the result
    return list(filter(is_prime, numbers))
        # Returns the result
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17]
result = filter_prime(numbers)
print(result)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires filtering out floating-point numbers from a list, keeping
# only non-float elements (integers, strings, etc.). The function should use
# `filter()` to create a new list that excludes any elements of type float.
# This is useful when you need to separate numeric types or clean mixed-type data.
#
# Prérequis Clés :
# - Function must accept a list of mixed-type elements as input
# - Function must use `filter()` to remove float elements
# - Function must return a new list with only non-float elements
# - Must correctly identify float types using isinstance()
#
# Exemple d'Entrée/Sortie :
# - filter_floats([1, 2.5, "apple", 3.7, 10]) should return [1, "apple", 10]
# - filter_floats([1.0, 2.0, 3.0]) should return [] (all floats)
# - filter_floats([1, 2, 3, "test"]) should return [1, 2, 3, "test"] (no floats)
#
# Remarque : isinstance(x, float) checks if x is of type float, including 4.0.
# ============================================================================
"""
Problem: 280
Write a Python program to filter out all floating-point numbers from a list using `filter()`.

# EXPLICATION DE LA SOLUTION :
# This solution uses a nested helper function `is_not_float()` that checks if an
# element is NOT a float using isinstance(). The `filter()` function applies this
# predicate to keep only non-float elements. Note that 4.0 is considered a float
# even though it represents a whole number.
def filter_floats(items):
    # Function definition
    def is_not_float(x):
        # isinstance(x, float) checks if x is a float type
        return not isinstance(x, float)  # Returns True if x is NOT a float
    # filter() keeps elements where is_not_float returns True
    return list(filter(is_not_float, items))  # Retourne : [1, "apple", 10, 7] (non-floats)
    # Remarque : 4.0 is a float, so it's filtered out

items = [1, 2.5, "apple", 3.7, 10, 8.9, 7, 4.0]
result = filter_floats(items)
print(result)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires filtering out uppercase strings from a list, keeping only
# strings that are not entirely uppercase (lowercase or mixed case). The function
# should use `filter()` to create a new list containing only non-uppercase strings.
# This is useful for text processing when you want to exclude all-caps text.
#
# Prérequis Clés :
# - Function must accept a list of strings as input
# - Function must use `filter()` to remove uppercase strings
# - Function must return a new list with only non-uppercase strings
# - Must use string method .isupper() to check if all characters are uppercase
#
# Exemple d'Entrée/Sortie :
# - filter_uppercase(["HELLO", "world", "PYTHON", "code"]) should return ["world", "code"]
# - filter_uppercase(["hello", "world"]) should return ["hello", "world"] (no uppercase)
# - filter_uppercase(["HELLO", "WORLD"]) should return [] (all uppercase)
#
# Remarque : .isupper() returns True only if all characters are uppercase and string has at least one character.
# ============================================================================
"""
Problem: 281
Write a Python program to filter out all uppercase strings from a list using `filter()`.

# EXPLICATION DE LA SOLUTION :
# This solution uses a nested helper function `is_not_uppercase()` that checks if
# a string is NOT entirely uppercase using the .isupper() method. The `filter()`
# function applies this predicate to keep only strings that contain lowercase or
# mixed-case characters. filter() returns an iterator, so list() converts it to a list.
def filter_uppercase(strings):
    # Function definition
    def is_not_uppercase(s):
        # isupper() returns True if all characters in string are uppercase and string has at least one character
        # not s.isupper() returns True if string is NOT all uppercase (i.e., has lowercase or mixed case)
        return not s.isupper()  # Returns True for "world", "code", "example" (non-uppercase)
    # filter() keeps elements where is_not_uppercase returns True
    # filter() is a higher-order function that applies the predicate to each element
    return list(filter(is_not_uppercase, strings))  # Retourne : ["world", "code", "example"]
    # filter() returns an iterator, so list() converts it to a list

strings = ["HELLO", "world", "PYTHON", "code", "CHATGPT", "example"]
result = filter_uppercase(strings)  # Filters out "HELLO", "PYTHON", "CHATGPT"
print(result)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem is similar to problem 281 - it requires filtering out uppercase
# strings from a list, keeping only strings that are not entirely uppercase.
# The function should use `filter()` to create a new list with non-uppercase strings.
# Cela démontre the same concept with a different implementation.
#
# Prérequis Clés :
# - Function must accept a list of strings as input
# - Function must use `filter()` to remove uppercase strings
# - Function must return a new list with only non-uppercase strings
# - Must correctly identify uppercase strings using .isupper()
#
# Exemple d'Entrée/Sortie :
# - filter_uppercase_again(["HELLO", "WORLD", "python", "CHATGPT"]) should return ["python"]
# - filter_uppercase_again(["hello", "world"]) should return ["hello", "world"]
# - filter_uppercase_again(["HELLO", "WORLD"]) should return [] (all uppercase)
#
# This is a duplicate exercise to reinforce the filtering concept.
# ============================================================================
"""
Problem: 282
Write a Python program to filter out all uppercase strings from a list using `filter()`.

# EXPLICATION DE LA SOLUTION :
# This solution is functionally identical to problem 281, using the same approach
# with a nested helper function and filter(). It demonstrates the same filtering
# pattern with different variable names. filter() is lazy and returns an iterator,
# so list() forces evaluation and creates the final list.
def filter_uppercase_again(strings):
    # Function definition
    def is_not_uppercase(s):
        # isupper() checks if all characters are uppercase
        # not s.isupper() returns True for strings that are not all uppercase
        return not s.isupper()  # True for "python", "openai", "example"
    # filter() applies is_not_uppercase to each string and keeps those returning True
    return list(filter(is_not_uppercase, strings))  # Retourne : ["python", "openai", "example"]
    # filter() is lazy - returns iterator, list() forces evaluation

strings = ["HELLO", "WORLD", "python", "CHATGPT", "openai", "example"]
result = filter_uppercase_again(strings)  # Removes "HELLO", "WORLD", "CHATGPT"
print(result)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires filtering out None values from a list, keeping only
# elements that are not None. The function should use `filter()` to create a
# new list containing only non-None values. This is une opération courante data cleaning
# operation when dealing with optional or missing data.
#
# Prérequis Clés :
# - Function must accept a list of mixed-type elements as input
# - Function must use `filter()` to remove None values
# - Function must return a new list with only non-None elements
# - Must use identity check (is not None) rather than equality check
#
# Exemple d'Entrée/Sortie :
# - filter_non_none([1, None, "example", None, 3.14]) should return [1, "example", 3.14]
# - filter_non_none([None, None, None]) should return [] (all None)
# - filter_non_none([1, 2, 3]) should return [1, 2, 3] (no None values)
#
# Remarque : Use 'is not None' for identity check, not '!= None'. Empty string "" is not None.
# ============================================================================
"""
Problem: 283
Write a Python program to filter out all non-None values from a list using `filter()`.

# EXPLICATION DE LA SOLUTION :
# This solution uses a nested helper function `is_not_none()` that checks if an
# element is not None using the 'is' operator. The 'is' operator checks for object
# identity (same object in memory), which is the correct way to check for None.
# The `filter()` function applies this predicate to keep only non-None elements.
# Note that empty string "" is not None, so it will be kept in the result.
def filter_non_none(items):
    # Function definition
    def is_not_none(x):
        # 'is' operator checks for identity (same object in memory)
        # 'is not None' returns True if x is not the None object
        # Remarque : 'is' is different from '==' - 'is' checks identity, '==' checks equality
        return x is not None  # Returns True for 1, "example", 3.14, "" (all non-None)
    # filter() keeps elements where is_not_none returns True
    return list(filter(is_not_none, items))  # Retourne : [1, "example", 3.14, ""]
    # Remarque : Empty string "" is not None, so it's kept

items = [1, None, "example", None, 3.14, "", None]
result = filter_non_none(items)  # Removes all None values
print(result)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires filtering out elements from a list that contain a specific
# substring, keeping only elements that do NOT contain that substring. The function
# should use `filter()` to create a new list with elements that don't contain the
# specified substring. This is useful for text filtering and data cleaning.
#
# Prérequis Clés :
# - Function must accept a list of strings and a substring as input
# - Function must use `filter()` to remove elements containing the substring
# - Function must return a new list with only elements that don't contain the substring
# - Must use the 'in' operator to check for substring presence
#
# Exemple d'Entrée/Sortie :
# - filter_by_substring(["apple", "banana", "cherry", "pineapple"], "apple") should return ["banana", "cherry"]
# - filter_by_substring(["hello", "world"], "x") should return ["hello", "world"] (no matches)
# - filter_by_substring(["test", "testing", "tested"], "test") should return [] (all contain "test")
#
# The nested function can access the outer scope variable 'substring' (closure).
# ============================================================================
"""
Problem: 284
Write a Python program to filter out all elements from a list that contain a specific substring using `filter()`.

# EXPLICATION DE LA SOLUTION :
# This solution uses a nested helper function `does_not_contain_substring()` that
# checks if a string does NOT contain the specified substring using the 'in' operator.
# The nested function can access the outer scope variable 'substring' through closure.
# The `filter()` function applies this predicate to keep only elements that don't
# contain the substring. Cela démontre how closures work en Python.
def filter_by_substring(items, substring):
    # Function definition
    def does_not_contain_substring(s):
        # 'in' operator checks if substring exists within string s
        # substring not in s returns True if substring is NOT found in s
        return substring not in s  # Returns True for "banana", "cherry", "grape"
    # filter() keeps elements where does_not_contain_substring returns True
    # Nested function can access outer scope variable 'substring' (closure)
    return list(filter(does_not_contain_substring, items))  # Retourne : ["banana", "cherry", "grape"]
    # filter() applies predicate to each item and keeps those that don't contain "apple"

items = ["apple", "banana", "cherry", "pineapple", "grape"]
substring = "apple"
result = filter_by_substring(items, substring)  # Removes "apple" and "pineapple"
print(result)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires printing numbers from 1 to 10 (inclusive) using a while loop.
# The function should use a while loop to iterate and print each number sequentially.
# Cela démontre basic loop control and iteration patterns en Python.
#
# Prérequis Clés :
# - Function must use a while loop (not a for loop)
# - Function must print numbers from 1 to 10
# - Each number should be printed on a separate line
# - Must properly initialize and increment the counter variable
#
# Exemple d'Entrée/Sortie :
# - print_1_to_10() should print: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 (each on new line)
#
# Algorithm: Initialize counter to 1, loop while counter <= 10, print and increment.
# ============================================================================
"""
Problem: 285
Write a Python program to print numbers from 1 to 10 using a `while` loop.

# EXPLICATION DE LA SOLUTION :
# This solution initializes a counter variable i to 1, then uses a while loop that
# continues as long as i is less than or equal to 10. Inside the loop, it prints
# the current value of i and then increments it by 1. The loop terminates when i
# becomes 11, at which point the condition i <= 10 becomes False.
def print_1_to_10():
    # Function definition
    i = 1  # Initialize counter variable to 1
    # while loop continues as long as condition is True
    while i <= 10:  # Loop executes while i is less than or equal to 10
        print(i)  # Print current value of i
        i += 1  # Increment i by 1 (equivalent to i = i + 1)
        # Loop continues: i=1, print 1, i=2, print 2, ..., i=10, print 10, i=11, exit loop
    # After loop, i = 11 (condition i <= 10 is False)

print_1_to_10()  # Sortie : 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 (each on new line)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires calculating the sum of the first 10 natural numbers
# (1 + 2 + 3 + ... + 10 = 55) using a while loop. The function should iterate
# through numbers 1 to 10 and accumulate their sum, then return the total.
# Cela démontre accumulator patterns and loop-based summation.
#
# Prérequis Clés :
# - Function must use a while loop (not a for loop or built-in sum())
# - Function must calculate sum of numbers 1 through 10
# - Function must return the sum (55)
# - Must properly initialize accumulator and counter variables
#
# Exemple d'Entrée/Sortie :
# - sum_first_10_natural_numbers() should return 55
#
# Algorithm: Initialize total to 0, counter to 1, loop while counter <= 10,
# add counter to total, increment counter, return total.
# ============================================================================
"""
Problem: 286
Write a Python program to find the sum of the first 10 natural numbers using a `while` loop.

# EXPLICATION DE LA SOLUTION :
# This solution uses an accumulator pattern with a while loop. It initializes
# a total variable to 0 and a counter i to 1. The while loop continues while
# i <= 10, adding i to the total and incrementing i in each iteration. After
# the loop completes, it returns the accumulated sum (1+2+3+...+10 = 55).
def sum_first_10_natural_numbers():
    # Function definition
    i = 1
    total = 0
    while i <= 10:
        total += i
        i += 1
    return total
        # Returns the result

result = sum_first_10_natural_numbers()
print(result)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires printing all even numbers between 1 and 20 (inclusive)
# using a while loop. Even numbers are integers divisible by 2 (2, 4, 6, 8, 10,
# 12, 14, 16, 18, 20). The function should iterate through the range and print
# only numbers that satisfy the even condition.
#
# Prérequis Clés :
# - Function must use a while loop
# - Function must print only even numbers from 1 to 20
# - Must use modulo operator (%) to check if a number is even
# - Each even number should be printed on a separate line
#
# Exemple d'Entrée/Sortie :
# - print_even_numbers() should print: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20
#
# Algorithm: Loop from 1 to 20, check if i % 2 == 0, print if even, increment counter.
# ============================================================================
"""
Problem: 287
Write a Python program to print all even numbers between 1 and 20 using a `while` loop.

# EXPLICATION DE LA SOLUTION :
# This solution uses a while loop that iterates from 1 to 20. Inside the loop,
# it checks if the current number is even using the modulo operator (i % 2 == 0).
# If the number is even, it prints it. The counter is incremented regardless of
# whether the number was printed, ensuring the loop progresses through all numbers.
def print_even_numbers():
    # Function definition
    i = 1  # Initialize counter to 1
    while i <= 20:  # Loop from 1 to 20
        # Modulo operator % returns remainder after division
        # i % 2 == 0 means i is divisible by 2 (even number)
        if i % 2 == 0:  # Check if current number is even
            print(i)  # Print only if even: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20
        i += 1  # Increment counter regardless of whether number was printed
        # Loop continues: i=1 (odd, skip), i=2 (even, print), i=3 (odd, skip), ...

print_even_numbers()  # Sortie : 2, 4, 6, 8, 10, 12, 14, 16, 18, 20 (each on new line)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires printing all odd numbers between 1 and 20 (inclusive)
# using a while loop. Odd numbers are integers not divisible by 2 (1, 3, 5, 7, 9,
# 11, 13, 15, 17, 19). The function should iterate through the range and print
# only numbers that satisfy the odd condition.
#
# Prérequis Clés :
# - Function must use a while loop
# - Function must print only odd numbers from 1 to 20
# - Must use modulo operator (%) to check if a number is odd
# - Each odd number should be printed on a separate line
#
# Exemple d'Entrée/Sortie :
# - print_odd_numbers() should print: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19
#
# Algorithm: Loop from 1 to 20, check if i % 2 != 0, print if odd, increment counter.
# ============================================================================
"""
Problem: 288
Write a Python program to print all odd numbers between 1 and 20 using a `while` loop.

# EXPLICATION DE LA SOLUTION :
# This solution uses a while loop that iterates from 1 to 20. Inside the loop,
# it checks if the current number is odd using the modulo operator (i % 2 != 0).
# If the number is odd, it prints it. The counter is incremented regardless of
# whether the number was printed, ensuring the loop progresses through all numbers.
def print_odd_numbers():
    # Function definition
    i = 1
    while i <= 20:
        if i % 2 != 0:
            print(i)
        i += 1
print_odd_numbers()

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires calculating the sum of all digits in a given number.
# For example, the sum of digits in 1234 is 1+2+3+4 = 10. The function should
# extract each digit from the number and add them together using a while loop.
# Cela démontre digit extraction using modulo and integer division operations.
#
# Prérequis Clés :
# - Function must accept a number as input
# - Function must use a while loop to extract digits
# - Function must return the sum of all digits
# - Must handle both positive and negative numbers (typically work with absolute value)
#
# Exemple d'Entrée/Sortie :
# - sum_of_digits(1234) should return 10 (1+2+3+4)
# - sum_of_digits(567) should return 18 (5+6+7)
# - sum_of_digits(9) should return 9
#
# Algorithm: Extract last digit using n % 10, add to sum, remove last digit using n // 10, repeat.
# ============================================================================
"""
Problem: 289
Write a Python program to find the sum of the digits of a given number using a `while` loop.

# EXPLICATION DE LA SOLUTION :
# This solution extracts each digit from the number using modulo (%) to get the
# last digit and integer division (//) to remove it. The while loop continues
# until the number becomes 0, accumulating the sum of all extracted digits.
# Extracts each digit and sums them using modulo and integer division
def sum_of_digits(number):
    # Function definition
    total = 0  # Initialize accumulator for sum of digits
    # Continue while number has digits remaining (number > 0)
    while number > 0:
        # Modulo 10 extracts the rightmost digit
        # 12345 % 10 = 5, 1234 % 10 = 4, 123 % 10 = 3, etc.
        digit = number % 10  # Get last digit: 5, then 4, then 3, then 2, then 1
        total += digit  # Add digit to total: 0+5=5, 5+4=9, 9+3=12, 12+2=14, 14+1=15
        # Integer division by 10 removes the rightmost digit
        # 12345 // 10 = 1234, 1234 // 10 = 123, 123 // 10 = 12, etc.
        number //= 10  # Remove last digit: 12345→1234→123→12→1→0
        # When number becomes 0, loop exits
    return total  # Retourne : 15 (sum of digits 1+2+3+4+5)

number = 12345
result = sum_of_digits(number)
print(f"The sum of the digits of {number} is: {result}")  # Sortie : "The sum of the digits of 12345 is: 15"

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires reversing a number (despite the problem description mentioning
# "sum of digits", the code actually reverses the number). For example, 12345 should
# become 54321. The function should extract digits from the original number and
# construct the reversed number using a while loop. Cela démontre digit
# manipulation and number construction.
#
# Prérequis Clés :
# - Function must accept a number as input
# - Function must use a while loop to reverse the number
# - Function must return the reversed number
# - Must extract digits and reconstruct number in reverse order
#
# Exemple d'Entrée/Sortie :
# - reverse_number(12345) should return 54321
# - reverse_number(567) should return 765
# - reverse_number(9) should return 9
#
# Algorithm: Extract last digit using n % 10, append to reversed number (reversed_num * 10 + digit),
# remove last digit using n // 10, repeat until n becomes 0.
# ============================================================================
"""
Problem: 290
Write a Python program to find the sum of the digits of a given number using a `while` loop.

# EXPLICATION DE LA SOLUTION :
# Remarque : Despite the problem description, this code actually reverses the number.
# This solution extracts each digit from the number and builds the reversed number
# by multiplying the current reversed number by 10 and adding the extracted digit.
# The while loop continues until the original number becomes 0.
# Reverses a number by extracting digits and building reversed number
def reverse_number(n):
    # Function definition
    reversed_num = 0  # Initialize reversed number to 0
    # Continue while n has digits remaining
    while n > 0:
        # Build reversed number: multiply by 10 to shift left, add last digit
        # reversed_num * 10 shifts existing digits left, n % 10 gets last digit
        # Example: n=123, reversed_num=0*10+3=3, then 3*10+2=32, then 32*10+1=321
        reversed_num = reversed_num * 10 + n % 10  # Append last digit of n to reversed_num
        # Integer division removes last digit
        n = n // 10  # Remove last digit: 123→12→1→0
    return reversed_num  # Returns reversed number: 12345 → 54321

# Example usage
num = int(input("Enter a number: "))
    # Gets user input
print("Reversed number:", reverse_number(num))

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires calculating the factorial of a given number using a while loop.
# The factorial of n (written as n!) is the product of all positive integers from
# 1 to n. For example, 5! = 5 × 4 × 3 × 2 × 1 = 120. By definition, 0! = 1.
# The function should use a while loop to multiply numbers from n down to 1.
#
# Prérequis Clés :
# - Function must accept a number as input
# - Function must use a while loop to calculate factorial
# - Function must return the factorial result
# - Must handle edge case: 0! = 1
#
# Exemple d'Entrée/Sortie :
# - factorial(5) should return 120 (5×4×3×2×1)
# - factorial(0) should return 1
# - factorial(3) should return 6 (3×2×1)
#
# Algorithm: Initialize result to 1, loop while number > 1, multiply result by number, decrement number.
# ============================================================================
"""
Problem: 291
Write a Python program to find the factorial of a given number using a `while` loop.

# EXPLICATION DE LA SOLUTION :
# This solution uses a while loop to calculate the factorial by multiplying numbers
# from the given number down to 1. It initializes result to 1, then multiplies it
# by the current number in each iteration while decrementing the number. The loop
# continues while number > 1, which correctly handles the case where number is 0
# or 1 (result remains 1).
def factorial(number):
    # Function definition
    result = 1
    while number > 1:
        result *= number
        number -= 1
    return result
        # Returns the result

# Example usage
number_to_calculate = 5
result = factorial(number_to_calculate)
print(f"The factorial of {number_to_calculate} is: {result}")

# Additional test cases
test_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in test_numbers:
    # Iterates through each element
    print(f"The factorial of {num} is: {factorial(num)}")

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires printing the multiplication table of a given number using
# a while loop. A multiplication table shows the product of the number with each
# integer from 1 to 10 (or another range). For example, the table for 5 would show:
# 5 × 1 = 5, 5 × 2 = 10, 5 × 3 = 15, ..., 5 × 10 = 50.
#
# Prérequis Clés :
# - Function must accept a number as input
# - Function must use a while loop to generate the table
# - Function must print each multiplication result
# - Typically prints table from 1 to 10
#
# Exemple d'Entrée/Sortie :
# - multiplication_table(5) should print: 5×1=5, 5×2=10, ..., 5×10=50
# - multiplication_table(3) should print: 3×1=3, 3×2=6, ..., 3×10=30
#
# Algorithm: Initialize counter to 1, loop while counter <= 10, print number × counter, increment counter.
# ============================================================================
"""
Problem: 292
Write a Python program to print the multiplication table of a given number using a `while` loop.

# EXPLICATION DE LA SOLUTION :
# This solution uses a while loop that iterates from 1 to 10. In each iteration,
# it prints the multiplication of the given number with the current counter value
# in a formatted string. The counter is incremented after each print statement,
# ensuring all multiplications from 1 to 10 are displayed.
def multiplication_table(number):
    # Function definition
    i = 1
    while i <= 10:
        print(f"{number} x {i} = {number * i}")
        i += 1

# Example usage
number_to_multiply = 5
print(f"Multiplication table for {number_to_multiply}:")
multiplication_table(number_to_multiply)

# Additional test cases
print("\nMultiplication tables for numbers 1 to 5:")
for num in range(1, 6):
    # Iterates through each element
    print(f"\nMultiplication table for {num}:")
    multiplication_table(num)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires checking if a given number is prime using a while loop.
# A prime number is a natural number greater than 1 that has no positive divisors
# other than 1 and itself. La fonction doit retourner True if the number is prime,
# and False otherwise. C'est une opération fondamentale number theory problem.
#
# Prérequis Clés :
# - Function must accept a number as input
# - Function must use a while loop to check for divisors
# - Function must return True if prime, False otherwise
# - Numbers less than 2 are not prime
# - Must check divisors efficiently (up to sqrt(n))
#
# Exemple d'Entrée/Sortie :
# - is_prime(7) should return True
# - is_prime(10) should return False (divisible by 2 and 5)
# - is_prime(1) should return False (not prime by definition)
#
# Algorithm: Check if number < 2, then check divisibility from 2 to sqrt(number).
# ============================================================================
"""
Problem: 293
Write a Python program to check if a given number is prime using a `while` loop.

# EXPLICATION DE LA SOLUTION :
# This solution first checks if the number is less than 2 (not prime). Then it uses
# a while loop to check for divisors from 2 up to the square root of the number.
# The condition `i * i <= number` is equivalent to `i <= sqrt(number)` but avoids
# importing math. If any divisor is found, it returns False immediately. If no
# divisors are found, the number is prime and returns True.
def is_prime(number):
    # Function definition
    if number < 2:
        return False
            # Returns the result
    i = 2
    while i * i <= number:
        if number % i == 0:
            # Checks condition
            return False
                # Returns the result
        i += 1
    return True
        # Returns the result

# Example usage
test_numbers = [1, 2, 3, 4, 5, 10, 13, 17, 20, 23, 24, 29]

print("Prime number check:")
for num in test_numbers:
    # Iterates through each element
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires counting the number of digits in a given number using
# a while loop. For example, 12345 has 5 digits, and 9 has 1 digit. The function
# should repeatedly divide the number by 10 (using integer division) until it
# becomes 0, counting how many divisions were needed.
#
# Prérequis Clés :
# - Function must accept a number as input
# - Function must use a while loop to count digits
# - Function must return the count of digits
# - Must handle edge case: 0 has 1 digit (or handle separately)
#
# Exemple d'Entrée/Sortie :
# - count_digits(12345) should return 5
# - count_digits(9) should return 1
# - count_digits(100) should return 3
#
# Algorithm: Initialize count to 0, loop while number > 0, divide by 10, increment count.
# ============================================================================
"""
Problem: 294
Write a Python program to count the number of digits in a given number using a `while` loop.

# EXPLICATION DE LA SOLUTION :
# This solution uses a while loop that continues while the number is greater than 0.
# In each iteration, it divides the number by 10 using integer division (//=) to
# remove the rightmost digit, and increments a counter. The loop continues until
# the number becomes 0, at which point the counter contains the total number of digits.
# Remarque : This doesn't handle 0 correctly (would return 0), but the test cases show
# handling for negative numbers by using absolute value.
def count_digits(number):
    # Function definition
    count = 0
    while number > 0:
        number //= 10
        count += 1
    return count
        # Returns the result

# Example usage
test_numbers = [0, 5, 123, 987654321, 1000000000, -456]

print("Counting digits:")
for num in test_numbers:
    # Iterates through each element
    if num < 0:
        print(f"The number of digits in {num} is {count_digits(-num)} (ignoring the negative sign).")
    else:
        print(f"The number of digits in {num} is {count_digits(num)}.")

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires finding the Greatest Common Divisor (GCD) of two numbers
# using a while loop. The GCD is the largest positive integer that divides both
# numbers without leaving a remainder. For example, GCD(56, 98) = 14. This problem
# is typically solved using the Euclidean algorithm, which is one of the oldest
# algorithms still in use today.
#
# Prérequis Clés :
# - Function must accept two numbers as input
# - Function must use a while loop to calculate GCD
# - Function must return the GCD
# - Must implement Euclidean algorithm efficiently
#
# Exemple d'Entrée/Sortie :
# - gcd(56, 98) should return 14
# - gcd(48, 18) should return 6
# - gcd(17, 13) should return 1 (co-prime numbers)
#
# Algorithm: Euclidean algorithm - repeatedly replace (a, b) with (b, a % b) until b becomes 0.
# ============================================================================
"""
Problem: 295
Write a Python program to find the GCD (Greatest Common Divisor) of two numbers using a `while` loop.

# EXPLICATION DE LA SOLUTION :
# This solution implements the Euclidean algorithm using a while loop. The algorithm
# works by repeatedly replacing the pair (a, b) with (b, a % b) until b becomes 0.
# At that point, a contains the GCD. The condition `while b:` continues as long as
# b is non-zero. This is an efficient O(log(min(a, b))) algorithm for finding GCD.
def gcd(a, b):
    # Function definition
    while b:
        a, b = b, a % b
    return a
        # Returns the result

# Example usage
num1 = 56
num2 = 98

result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {result}.")

# Additional test cases
test_cases = [(48, 18), (101, 103), (56, 0), (0, 34), (0, 0)]

print("Testing additional cases:")
for case in test_cases:
    # Iterates through each element
    a, b = case
    result = gcd(a, b)
    print(f"The GCD of {a} and {b} is {result}.")

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires printing the Fibonacci sequence up to N terms using a while loop.
# The Fibonacci sequence is a series of numbers where each number is the sum of the
# two preceding ones, starting from 0 and 1: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# The function should generate and print the first N terms of this sequence.
#
# Prérequis Clés :
# - Function must accept N (number of terms) as input
# - Function must use a while loop to generate the sequence
# - Function must print each term of the Fibonacci sequence
# - Sequence starts with 0 and 1
#
# Exemple d'Entrée/Sortie :
# - fibonacci_sequence(10) should print: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# - fibonacci_sequence(5) should print: 0, 1, 1, 2, 3
#
# Algorithm: Initialize a=0, b=1, loop N times, print a, update (a, b) = (b, a+b).
# ============================================================================
"""
Problem: 296
Write a Python program to print the Fibonacci sequence up to N terms using a `while` loop.

# EXPLICATION DE LA SOLUTION :
# This solution uses two variables a and b to track the current and next Fibonacci
# numbers. It initializes them to 0 and 1 (the first two terms), then uses a while
# loop to print N terms. In each iteration, it prints the current value a, then
# updates the pair (a, b) to (b, a+b) to generate the next term. A counter ensures
# exactly N terms are printed.
def fibonacci_sequence(n):
    # Function definition
    a, b = 0, 1
    count = 0
    while count < n:
        print(a)
        a, b = b, a + b
        count += 1
# Example usage
terms = 10
print(f"Fibonacci sequence up to {terms} terms:")
fibonacci_sequence(terms)

# Additional test case
additional_terms = 15
print(f"\nFibonacci sequence up to {additional_terms} terms:")
fibonacci_sequence(additional_terms)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires finding the sum of all elements in a list using a while loop.
# The function should iterate through each element in the list and accumulate their
# sum, then return the total. Cela démontre list traversal and accumulator
# patterns using a while loop instead of a for loop.
#
# Prérequis Clés :
# - Function must accept a list of numbers as input
# - Function must use a while loop to iterate through the list
# - Function must return the sum of all elements
# - Must use index-based access to traverse the list
#
# Exemple d'Entrée/Sortie :
# - sum_elements([1, 2, 3, 4, 5]) should return 15
# - sum_elements([10, 20, 30]) should return 60
# - sum_elements([]) should return 0 (empty list)
#
# Algorithm: Initialize total to 0, index to 0, loop while index < len(lst), add lst[index] to total, increment index.
# ============================================================================
"""
Problem: 297
description": "Write a Python program to find the sum of all elements in a list using a `while` loop.

# EXPLICATION DE LA SOLUTION :
# This solution uses an index-based approach with a while loop. It initializes a
# total variable to 0 and an index variable to 0. The while loop continues while
# the index is less than the length of the list. In each iteration, it adds the
# element at the current index to the total and increments the index. This approach
# manually manages the index, unlike a for loop which handles iteration automatically.
def sum_elements(lst):
    # Function definition
    total = 0
    index = 0

    while index < len(lst):
        total += lst[index]
        index += 1

    return total
        # Returns the result

lst = [1, 2, 3, 4, 5]
print(sum_elements(lst))

"""
Problem: 298
Write a Python program to find the largest element in a list using a `while` loop.

def main(lst):
    # Function definition
    i = 0
    while i < len(lst):
        return max(lst, key=len)
            # Returns the result
        i += 1

lst = ["tree", "cliff", "mountain", "tree","tree", "grassy"]
main(lst)

# CORRECT EXPLICATION DE LA SOLUTION :
# This solution correctly implements the maximum finding algorithm. It initializes
# largest to the first element, then uses a while loop to iterate through the
# remaining elements (starting from index 1). In each iteration, it compares the
# current element with the largest value found so far and updates largest if the
# current element is greater. This is the standard linear search for maximum.
def find_largest_element(numbers):
    # Function definition
    i = 1
    largest = numbers[0]
    while i < len(numbers):
        if numbers[i] > largest:
            largest = numbers[i]
        i += 1
    return largest
        # Returns the result

# Example usage
numbers_list = [5, 12, 3, 8, 20, 15]
largest_number = find_largest_element(numbers_list)
print(f"The largest element in the list is: {largest_number}")

# Additional test case
additional_numbers_list = [-1, -5, -3, -8]
largest_number_in_negative = find_largest_element(additional_numbers_list)
print(f"The largest element in the list of negatives is: {largest_number_in_negative}")

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires finding the smallest element in a list using a while loop.
# The function should iterate through all elements in the list and keep track of
# the minimum value encountered, then return it. Cela démontre the "minimum
# finding" algorithm pattern using a while loop, which is the complement of finding
# the maximum.
#
# Prérequis Clés :
# - Function must accept a list of comparable elements as input
# - Function must use a while loop to iterate through the list
# - Function must return the smallest element
# - Must handle edge case: empty list (should return None or raise error)
#
# Exemple d'Entrée/Sortie :
# - smallest_element([5, 12, 3, 8, 20, 15]) should return 3
# - smallest_element([-1, -5, -3, -8]) should return -8
# - smallest_element([42]) should return 42
#
# Algorithm: Initialize smallest to first element, loop through remaining elements,
# update smallest if current element is smaller.
# ============================================================================
"""
Problem: 299
Write a Python program to find the smallest element in a list using a `while` loop.

# EXPLICATION DE LA SOLUTION :
# This solution first checks if the list is empty and returns None if so. Otherwise,
# it initializes smallest to the first element, then uses a while loop to iterate
# through the remaining elements (starting from index 1). In each iteration, it
# compares the current element with the smallest value found so far and updates
# smallest if the current element is smaller. This is the standard linear search for minimum.
def smallest_element(lst):
    # Function definition
    if not lst:
        return None
            # Returns the result

    smallest_word = lst[0]
    i = 1

    while i < len(lst):
        if lst[i] < smallest_word:
            smallest_word = lst[i]
        i += 1

    return smallest_word
        # Returns the result

lst = ["hot", "hotty", "hotties"]
print(smallest_element(lst))

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires removing all occurrences of a specific element from a list
# using a while loop. The function should modify the list in-place (or return a
# new list) by removing every instance of the specified element. Cela démontre
# list modification and careful index management when modifying a list during iteration.
#
# Prérequis Clés :
# - Function must accept a list and an element to remove as input
# - Function must use a while loop to iterate through the list
# - Function must remove all occurrences of the specified element
# - Must handle index management correctly when removing elements (don't increment index when removing)
#
# Exemple d'Entrée/Sortie :
# - remove_all_occurrences([1, 2, 3, 2, 4, 2], 2) should return [1, 3, 4]
# - remove_all_occurrences([5, 5, 5], 5) should return []
# - remove_all_occurrences([1, 2, 3], 4) should return [1, 2, 3] (no change)
#
# Algorithm: Loop through list, if element matches, remove it (don't increment index),
# otherwise increment index. This avoids skipping elements after removal.
# ============================================================================
"""
Problem: 300
Write a Python program to remove all occurrences of a specific element from a list using a `while` loop.

# EXPLICATION DE LA SOLUTION :
# This solution uses a while loop with careful index management. When an element
# matches the target, it removes it using pop(i), which shifts all subsequent
# elements left. The key insight is to NOT increment the index when removing an
# element, because the next element has moved into the current position. Only
# increment the index when the element doesn't match (and thus wasn't removed).
# This ensures all occurrences are removed without skipping any elements.
def remove_all_occurrences(lst, element):
    # Function definition
    i = 0
    while i < len(lst):
        if lst[i] == element:
            # Checks condition
            lst.pop(i)
        else:
            i += 1
    return lst
        # Returns the result

# Example usage
numbers_list = [1, 2, 3, 4, 3, 5, 3, 6]
element_to_remove = 3
updated_list = remove_all_occurrences(numbers_list, element_to_remove)
print(f"Updated list after removing {element_to_remove}: {updated_list}")

# Additional test case
fruits_list = ['apple', 'banana', 'cherry', 'banana', 'date']
fruit_to_remove = 'banana'
updated_fruits_list = remove_all_occurrences(fruits_list, fruit_to_remove)
print(f"Updated fruits list after removing '{fruit_to_remove}': {updated_fruits_list}")

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires checking if a given string is a palindrome using a while loop.
# A palindrome is a string that reads the same forwards and backwards (e.g., "radar",
# "level", "racecar"). The function should compare characters from both ends of the
# string, moving inward, and return True if all pairs match, False otherwise.
#
# Prérequis Clés :
# - Function must accept a string as input
# - Function must use a while loop to check characters
# - Function must return True if palindrome, False otherwise
# - Must compare characters from both ends simultaneously
#
# Exemple d'Entrée/Sortie :
# - is_palindrome("radar") should return True
# - is_palindrome("hello") should return False
# - is_palindrome("level") should return True
#
# Algorithm: Use two pointers (i from start, j from end), compare s[i] and s[j],
# move pointers inward until they meet or mismatch is found.
# ============================================================================
"""
Problem: 301
Write a Python program to check if a given string is a palindrome using a `while` loop.

# EXPLICATION DE LA SOLUTION :
# This solution uses two pointers: i starting from the beginning (0) and j starting
# from the end (len(s) - 1). The while loop continues while i < j, comparing characters
# at both positions. If any pair doesn't match, it returns False immediately. If all
# pairs match, the pointers meet in the middle and the function returns True. This
# is an efficient O(n) solution that only checks each character once.
def is_palindrome(s):
    # Function definition
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
                # Returns the result
        i += 1
        j -= 1
    return True
        # Returns the result

# Example usage
test_string_1 = "radar"
test_string_2 = "hello"
test_string_3 = "level"
test_string_4 = "world"

result_1 = is_palindrome(test_string_1)
result_2 = is_palindrome(test_string_2)
result_3 = is_palindrome(test_string_3)
result_4 = is_palindrome(test_string_4)

print(f'Is "{test_string_1}" a palindrome? {result_1}')
print(f'Is "{test_string_2}" a palindrome? {result_2}')
print(f'Is "{test_string_3}" a palindrome? {result_3}')
print(f'Is "{test_string_4}" a palindrome? {result_4}')

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires counting the number of vowels in a given string using a while loop.
# Vowels in English are typically 'a', 'e', 'i', 'o', 'u' (and sometimes 'y'), and
# the function should count both uppercase and lowercase versions. The function should
# iterate through each character in the string and count how many are vowels.
#
# Prérequis Clés :
# - Function must accept a string as input
# - Function must use a while loop to iterate through characters
# - Function must return the count of vowels
# - Must handle both uppercase and lowercase vowels
#
# Exemple d'Entrée/Sortie :
# - count_vowels("Hello, World!") should return 3 (e, o, o)
# - count_vowels("Python programming") should return 4 (o, o, a, i)
# - count_vowels("AEIOU") should return 5
#
# Algorithm: Initialize count to 0, loop through each character, check if character
# is in vowels string, increment count if vowel, return count.
# ============================================================================
"""
Problem: 302
Write a Python program to count the number of vowels in a given string using a `while` loop.

# EXPLICATION DE LA SOLUTION :
# This solution defines a string containing all vowels (both uppercase and lowercase),
# then uses a while loop to iterate through each character in the input string. For
# each character, it checks if it's in the vowels string using the 'in' operator. If
# it is a vowel, the count is incremented. After processing all characters, it returns
# the total count of vowels found.
def count_vowels(s):
    # Function definition
    vowels = "aeiouAEIOU"
    count = 0
    i = 0
    while i < len(s):
        if s[i] in vowels:
            count += 1
        i += 1
    return count
        # Returns the result

# Example usage
test_string_1 = "Hello, World!"
test_string_2 = "Python programming"
test_string_3 = "Count the vowels"
test_string_4 = "AEIOU and sometimes Y"

result_1 = count_vowels(test_string_1)
result_2 = count_vowels(test_string_2)
result_3 = count_vowels(test_string_3)
result_4 = count_vowels(test_string_4)

print(f'Number of vowels in "{test_string_1}": {result_1}')
print(f'Number of vowels in "{test_string_2}": {result_2}')
print(f'Number of vowels in "{test_string_3}": {result_3}')
print(f'Number of vowels in "{test_string_4}": {result_4}')

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires printing each character of a given string on a separate
# line using a while loop. The function should iterate through the string character
# by character and print each one. Cela démontre basic string iteration and
# character access using index-based traversal.
#
# Prérequis Clés :
# - Function must accept a string as input
# - Function must use a while loop to iterate through characters
# - Function must print each character on a separate line
# - Must use index-based access to get each character
#
# Exemple d'Entrée/Sortie :
# - print_each_character("Hello") should print: H, e, l, l, o (each on new line)
# - print_each_character("Python") should print: P, y, t, h, o, n
#
# Algorithm: Initialize index to 0, loop while index < len(s), print s[index], increment index.
# ============================================================================
"""
Problem: 303
Write a Python program to print each character of a given string using a `while` loop.

# EXPLICATION DE LA SOLUTION :
# This solution uses a while loop with an index variable to iterate through the string.
# It initializes i to 0 and continues looping while i is less than the length of the
# string. In each iteration, it prints the character at index i and increments i.
# This is a straightforward index-based iteration pattern.
def print_each_character(s):
    # Function definition
    i = 0
    while i < len(s):
        print(s[i])
        i += 1

# Example usage
test_string_1 = "Hello, World!"
test_string_2 = "Python"
test_string_3 = "While loop example"

print("Characters in test_string_1:")
print_each_character(test_string_1)

print("\nCharacters in test_string_2:")
print_each_character(test_string_2)

print("\nCharacters in test_string_3:")
print_each_character(test_string_3)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a program that repeatedly prompts the user for
# input until a specific condition is met using a while loop. Cela démontre
# input validation and the use of infinite loops with break statements. The loop
# should continue asking until the user provides valid input that satisfies the condition.
#
# Prérequis Clés :
# - Function must use a while loop (typically while True for infinite loop)
# - Function must prompt user for input repeatedly
# - Function must check if input meets condition
# - Function must break out of loop when condition is met
#
# Exemple d'Entrée/Sortie :
# - User enters 5, then 8, then 15 → loop continues until number > 10 is entered
# - This pattern is common for input validation
#
# Algorithm: Use while True loop, get input, check condition, break if condition met.
# ============================================================================
"""
Problem: 304
Write a Python program to repeatedly ask for user input until a specific condition is met using a `while` loop.

# EXPLICATION DE LA SOLUTION :
# This solution uses an infinite while loop (while True) that continues until a
# break statement is executed. Inside the loop, it prompts the user for input and
# converts it to an integer. If the number is greater than 10, it breaks out of the
# loop. Otherwise, the loop continues and prompts again. This is une opération courante pattern
# for input validation.
def ask_until_condition():
    # Function definition
    while True:
        user_input = input("Enter a number greater than 10: ")
            # Gets user input
        if int(user_input) > 10:
            break

ask_until_condition()

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires sorting a list of dates by their month using the `sorted()`
# function with a `key` parameter. The dates should be ordered from January (month 1)
# to December (month 12), regardless of the year or day. Cela démontre custom
# sorting using the key parameter to extract a specific attribute for comparison.
#
# Prérequis Clés :
# - Function must accept a list of date objects as input
# - Function must use `sorted()` with a `key` parameter
# - Function must sort dates by month (1-12)
# - Must return a new sorted list
#
# Exemple d'Entrée/Sortie :
# - sort_dates_by_month([Jan 15, Mar 20, May 10, Sep 25, Jun 1]) should return
#   dates sorted: Jan, Mar, May, Jun, Sep
#
# Algorithm: Use sorted() with key=lambda date: date.month to extract month attribute.
# ============================================================================
"""
305
description": "Write a Python program to sort a list of dates by month using `sorted()` with the `key` parameter.
    # Sorts elements in ascending order

from datetime import datetime

# EXPLICATION DE LA SOLUTION :
# This solution uses the `sorted()` function with a lambda function as the key parameter.
# The lambda function extracts the month attribute from each date object (date.month),
# which returns an integer from 1 to 12. The sorted() function then sorts the dates
# based on these month values, resulting in dates ordered from January to December.
def sort_dates_by_month(dates):
    # Function definition
    return sorted(dates, key=lambda date: date.month)
        # Sorts elements in ascending order

def print_sorted_dates(sorted_dates):
    # Function definition
    for date in sorted_dates:
        # Iterates through each element
        print(date.strftime("%B"))

def main():
    # Function definition
    dates = [
        datetime(2022, 1, 15),
        datetime(2022, 3, 20),
        datetime(2022, 5, 10),
        datetime(2022, 9, 25),
        datetime(2022, 6, 1)
    ]

    sorted_dates = sort_dates_by_month(dates)
    print_sorted_dates(sorted_dates)

main()


# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires sorting a list of integers based on the sum of their digits
# using the `sorted()` function with a `key` parameter. For example, 123 (sum=6)
# should come before 45 (sum=9) when sorted. Cela démontre custom sorting where
# the comparison is based on a computed value rather than the original value.
#
# Prérequis Clés :
# - Function must accept a list of integers as input
# - Function must use `sorted()` with a `key` parameter
# - Function must sort by sum of digits (not the number itself)
# - Must calculate sum of digits for each number
#
# Exemple d'Entrée/Sortie :
# - sort_by_digit_sum([123, 45, 67, 9]) should return [9, 123, 45, 67]
#   (sums: 9→9, 123→6, 45→9, 67→13, sorted by sum: 6, 9, 9, 13)
#
# Algorithm: Define helper function to calculate digit sum, use sorted() with key
# parameter pointing to the helper function.
# ============================================================================
"""
306
Write a Python program to sort a list of integers by the sum of their digits using `sorted()` with the `key` parameter.
    # Sorts elements in ascending order

# EXPLICATION DE LA SOLUTION :
# This solution first defines a helper function `sum_of_digits()` that calculates
# the sum of digits in a number by repeatedly extracting the last digit using modulo
# and removing it using integer division. The main function then uses `sorted()` with
# this helper function as the key parameter, which sorts the numbers based on their
# digit sums rather than their actual values.
def sum_of_digits(n):
    # Function definition
    total = 0
    for digit in str(n):
        # Iterates through each element
        total += int(digit)
    return total
        # Returns the result

def integers_lst(lst):
    # Function definition
    sorted_lst = sorted(lst, key=sum_of_digits)
        # Sorts elements in ascending order
    return sorted_lst
        # Returns the result

lst = [4, 56, 56, 36, 123]
print(integers_lst(lst))

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires finding both the minimum and maximum numbers in a list
# without using built-in functions like sort(), max(), or min(). The function should
# manually iterate through the list to find these values and return them as a tuple.
# Cela démontre manual implementation of min/max finding algorithms.
#
# Prérequis Clés :
# - Function must accept a list of numbers as input
# - Function must return a tuple (min, max)
# - Cannot use sort(), max(), or min() functions
# - Must manually find minimum and maximum through iteration
#
# Exemple d'Entrée/Sortie :
# - find_min_max([5, 2, 8, 1, 9]) should return (1, 9)
# - find_min_max([10, 20, 30]) should return (10, 30)
#
# Algorithm: Initialize min and max to first element, iterate through list,
# update min if current < min, update max if current > max.
# ============================================================================
"""
Problème 307 :
Écrivez une fonction Python appelée find_min_max qui prend une liste de nombres en entrée et retourne un tuple contenant le minimum et maximum nombres dans la liste, dont pas call le fuction en utilisant print(find_min_max). N'utilisez pas trier() ou max() ou min().
"""

# EXPLICATION DE LA SOLUTION :
# Remarque : The provided solution has a bug - it initializes min_num to the last element
# and max_num to the first element, which is incorrect. A correct implementation
# would initialize both to the first element, then iterate through the list comparing
# each element to update min and max accordingly. The solution also doesn't return
# a tuple as required, but prints the values instead.
def find_min_max():
    # Function definition
    user = input("type list of numbers: ").split()
        # Gets user input

    int_num = []
    for number in user:
        # Iterates through each element
        int_num.append(int(number))

    min_num = int_num[-1]
    max_num = int_num[0]

    print(min_num, max_num)

find_min_max()

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires grouping strings by their first letter into a dictionary.
# La fonction doit prendre a list of strings and create a dictionary where each
# key is a first letter and the value is a list of all strings starting with that
# letter. Cela démontre dictionary grouping and data organization patterns.
#
# Prérequis Clés :
# - Function must accept a list of strings as input
# - Function must return a dictionary
# - Dictionary keys should be first letters (characters)
# - Dictionary values should be lists of strings starting with that letter
#
# Exemple d'Entrée/Sortie :
# - group_by_first_letter(["apple", "banana", "apricot", "cherry"]) should return
#   {'a': ['apple', 'apricot'], 'b': ['banana'], 'c': ['cherry']}
#
# Algorithm: Iterate through strings, extract first letter, add to dictionary list
# for that letter (create list if key doesn't exist).
# ============================================================================
"""
Problem: 308
Write a function group_by_first_letter that takes a list of strings as input and returns a dictionary. The dictionary should group the strings by their first letter. Each key in the dictionary should be a first letter, and the corresponding value should be a list of strings that start with that letter. User should type list as input():
    # Gets user input

# EXPLICATION DE LA SOLUTION :
# This solution iterates through each word in the list and extracts the first letter
# using word[0]. It then checks if that letter already exists as a key in the result
# dictionary. If not, it creates a new list with that word. If the key exists, it
# appends the word to the existing list. This creates a grouping of all words by their
# first letter. The solution uses input() to get the list from the user.
def group_by_first_letter():
    # Function definition
    lst = input("type word list: ").split()
        # Gets user input

    result = {}
    for word in lst:
        # Iterates through each element
        first_letter = word[0]
        if first_letter not in result:
            result[first_letter] = [word]
        else:
            result[first_letter].append(word)

    print(result)

group_by_first_letter()

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires printing an increasing triangle pattern using asterisks (*).
# An increasing triangle has one star on the first row, two stars on the second row,
# three stars on the third row, and so on. The triangle should have n rows total.
# Cela démontre nested loops and pattern printing.
#
# Prérequis Clés :
# - Function must accept n (number of rows) as input
# - Function must print an increasing triangle pattern
# - First row: 1 star, second row: 2 stars, ..., nth row: n stars
# - Must use nested loops (typically for loops)
#
# Exemple d'Entrée/Sortie :
# - increasing_triangle(5) should print:
#   *
#   * *
#   * * *
#   * * * *
#   * * * * *
#
# Algorithm: Outer loop for rows (1 to n), inner loop for stars (1 to current row).
# ============================================================================
"""
Proplem: 309
Write a increasing triangle using *

# EXPLICATION DE LA SOLUTION :
# This solution uses nested for loops to print the triangle. The outer loop iterates
# through each row from 0 to n-1. The inner loop prints stars for the current row,
# with the number of stars equal to i+1 (so row 0 has 1 star, row 1 has 2 stars, etc.).
# The end=" " parameter in print() keeps stars on the same line, and the outer print()
# moves to the next line after each row is complete.
def increasing_triangle(n):
    # Function definition
    for i in range(n):
        # Iterates through each element
        for j in range(i+1):
            # Iterates through each element
            print("*", end=" ")
        print()

rows = 5
increasing_triangle(rows)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires finding the longest word in a list of words. The function
# should iterate through the list and return the word with the maximum length. If
# multiple words have the same maximum length, it should return the first one
# encountered. Cela démontre finding maximum based on a property (length).
#
# Prérequis Clés :
# - Function must accept a list of words (strings) as input
# - Function must return the longest word
# - If multiple words have same length, return the first one
# - Cannot use sorted() function
#
# Exemple d'Entrée/Sortie :
# - find_longest_word(["Jonathan", "noll"]) should return "Jonathan"
# - find_longest_word(["cat", "dog", "bird"]) should return "bird"
#
# Algorithm: Initialize longest to empty string and count to 0, iterate through
# words, compare length to count, update if longer.
# ============================================================================
"""
Problem: 310
Write a Python function called find_longest_word that takes a list of words as input and returns the longest word in the list. If there are multiple longest words, return the first one encountered. Do not use sorted().
    # Sorts elements in ascending order

# EXPLICATION DE LA SOLUTION :
# This solution uses a linear search approach. It initializes longest_word to an
# empty string and count to 0. It then iterates through each word in the list,
# comparing the length of each word to the current maximum length (count). If a
# word is longer, it updates both the count and longest_word. This ensures the
# first longest word encountered is returned if there are ties.
def find_longest_word(lst):
    # Function definition
    longest_word = ""
    count = 0

    for word in lst:
        # Iterates through each element
        if len(word) > count:
            count = len(word)
            longest_word = word
    return longest_word
        # Returns the result

lst = ["Jonathan", "noll"]
print(find_longest_word(lst))

def main(lst):
    # Function definition
    return max(lst, key=len)
        # Returns the result

lst = ["tree", "cliff", "mountain", "tree","tree", "grassy"]
main(lst)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires finding the longest word in a list without using sorted()
# or len() functions. The function must manually calculate the length of each word
# by counting characters, then compare to find the maximum. Cela démontre manual
# length calculation and maximum finding without built-in functions.
#
# Prérequis Clés :
# - Function must accept a list of words as input
# - Function must return the longest word
# - Cannot use sorted() or len() functions
# - Must manually count characters to determine length
#
# Exemple d'Entrée/Sortie :
# - find_longest_word(["Jonathan", "noll", "it"]) should return "Jonathan"
# - find_longest_word(["cat", "dog"]) should return "cat" or "dog" (both length 3)
#
# Algorithm: For each word, count characters manually, compare to max_length,
# update if longer.
# ============================================================================
"""
Problem: 311
Write a Python function called find_longest_word that takes a list of words as input and returns the longest word in the list. If there are multiple longest words, return the first one encountered. Do not use sorted()and len().
    # Sorts elements in ascending order

# EXPLICATION DE LA SOLUTION :
# This solution manually calculates the length of each word by iterating through
# its characters and counting them (current_length). It then compares this manually
# calculated length to the maximum length found so far (max_length). If the current
# word is longer, it updates both max_length and longest_word. This approach avoids
# using the built-in len() function by manually counting characters.
def find_longest_word(lst):
    # Function definition
    longest_word = ""
    max_length = 0

    for word in lst:
        # Iterates through each element
        current_length = 0
        for char in word:
            # Iterates through each element
            current_length += 1
        if current_length > max_length:
            max_length = current_length
            longest_word = word

    return longest_word
        # Returns the result

lst = ["Jonathan", "noll", "it"]
print(find_longest_word(lst))

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires finding the second largest number in a list of numbers.
# The function should prompt the user for input, process the list, and return
# the second largest value. The constraint is not to use a for loop, so the
# solution typically uses sorting or other built-in functions.
#
# Prérequis Clés :
# - Function must prompt user for input (list of numbers)
# - Function must find the second largest number
# - Cannot use a for loop
# - Must handle the case where list has fewer than 2 elements
#
# Exemple d'Entrée/Sortie :
# - second_largest_number() with input "5 2 8 1 9" should return 8
# - second_largest_number() with input "10 20 30" should return 20
#
# Algorithm: Sort the list and return the second-to-last element (index -2).
# ============================================================================
"""
Problem: 312
Write a Python program to find the second largest number in a list. Prompt the user to enter a list of numbers, do not use a for loop.

# EXPLICATION DE LA SOLUTION :
# This solution gets user input, splits it into a list of strings, converts them
# to integers using map(), sorts the list in ascending order, and returns the element
# at index -2 (second to last, which is the second largest). Sorting places the
# largest elements at the end, so index -2 gives the second largest.
def second_largest_number():
    # Function definition
    user = input("Type numbers separated by spaces: ").split()
        # Gets user input
    user_int = list(map(int, user))
    user_int.sort()
    second_largest = user_int[-2]

    print(second_largest)

second_largest_number()

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires converting all strings in a list to uppercase using the
# `map()` function. The `map()` function applies a transformation function to each
# element in an iterable and returns an iterator. Cela démontre functional
# programming patterns and the use of map() for list transformations.
#
# Prérequis Clés :
# - Function must accept a list of strings as input
# - Function must use `map()` to transform strings
# - Function must return a new list with all strings in uppercase
# - Must convert each string using .upper() method
#
# Exemple d'Entrée/Sortie :
# - convert_to_uppercase(["hello", "world", "python"]) should return ["HELLO", "WORLD", "PYTHON"]
# - convert_to_uppercase(["Hello", "World"]) should return ["HELLO", "WORLD"]
#
# Algorithm: Define helper function that calls .upper(), use map() to apply to each string.
# ============================================================================
"""
Problem: 313
Write a Python program to convert a list of strings to uppercase using `map()`.

# EXPLICATION DE LA SOLUTION :
# This solution defines a helper function `to_uppercase()` that takes a string
# and returns its uppercase version using the .upper() method. The main function
# then uses `map()` to apply this transformation function to each string in the
# input list. Since map() returns an iterator, list() is used to convert it to
# a list. This is a functional programming approach to list transformation.
def convert_to_uppercase(strings):
    # Function definition
    def to_uppercase(s):
        # Function definition
        return s.upper()
            # Converts to lowercase/uppercase
    return list(map(to_uppercase, strings))
        # Returns the result

# Example usage
strings = ["hello", "world", "python", "programming"]
uppercase_strings = convert_to_uppercase(strings)
print("Original list:", strings)
print("Uppercase list:", uppercase_strings)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires converting a list of string representations of numbers
# to a list of actual integers using the `map()` function. For example, ["1", "2", "3"]
# should become [1, 2, 3]. This is une opération courante data type conversion task.
#
# Prérequis Clés :
# - Function must accept a list of numeric strings as input
# - Function must use `map()` to convert strings to integers
# - Function must return a new list of integers
# - Must use int() function for conversion
#
# Exemple d'Entrée/Sortie :
# - convert_to_integers(["1", "2", "3", "4", "5"]) should return [1, 2, 3, 4, 5]
# - convert_to_integers(["10", "20", "30"]) should return [10, 20, 30]
#
# Algorithm: Define helper function that calls int(), use map() to apply to each string.
# ============================================================================
"""
Problem: 314
Write a Python program to convert a list of strings representing numbers to a list of integers using `map()`.

# EXPLICATION DE LA SOLUTION :
# This solution defines a helper function `to_integer()` that takes a string and
# converts it to an integer using the int() function. The main function then uses
# `map()` to apply this conversion function to each string in the input list. The
# result is converted to a list using list() since map() returns an iterator. This
# is a clean functional approach to type conversion.
def convert_to_integers(strings):
    # Function definition
    def to_integer(s):
        # Function definition
        return int(s)
            # Returns the result
    return list(map(to_integer, strings))
        # Returns the result

# Example usage
string_numbers = ["1", "2", "3", "4", "5"]
integer_numbers = convert_to_integers(string_numbers)
print("Original list of strings:", string_numbers)
print("Converted list of integers:", integer_numbers)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires squaring each number in a list using the `map()` function.
# La fonction doit prendre a list of numbers and return a new list where each
# number has been squared (multiplied by itself). Cela démontre using map()
# for mathematical transformations.
#
# Prérequis Clés :
# - Function must accept a list of numbers as input
# - Function must use `map()` to square each number
# - Function must return a new list with squared values
# - Must calculate x * x (or x ** 2) for each number
#
# Exemple d'Entrée/Sortie :
# - square_numbers([1, 2, 3, 4, 5]) should return [1, 4, 9, 16, 25]
# - square_numbers([10, 20, 30]) should return [100, 400, 900]
#
# Algorithm: Define helper function that returns x * x, use map() to apply to each number.
# ============================================================================
"""
Problem: 315
Write a Python program to square each number in a list using `map()`.

# EXPLICATION DE LA SOLUTION :
# This solution defines a helper function `square()` that takes a number and returns
# its square (x * x). The main function then uses `map()` to apply this squaring
# function to each number in the input list. The result is converted to a list using
# list() since map() returns an iterator. This is an efficient way to transform
# all elements in a list with a single operation.
def square_numbers(numbers):
    # Function definition
    def square(x):
        # Function definition
        return x * x
            # Returns the result
    return list(map(square, numbers))
        # Returns the result

# Example usage
original_numbers = [1, 2, 3, 4, 5]
squared_numbers = square_numbers(original_numbers)
print("Original list of numbers:", original_numbers)
print("Squared list of numbers:", squared_numbers)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires finding the length of each string in a list using the
# `map()` function. La fonction doit prendre a list of strings and return a new
# list containing the length of each corresponding string. Cela démontre
# using map() to extract properties from elements.
#
# Prérequis Clés :
# - Function must accept a list of strings as input
# - Function must use `map()` to find lengths
# - Function must return a new list of integers (lengths)
# - Must use len() function for each string
#
# Exemple d'Entrée/Sortie :
# - string_lengths(["apple", "banana", "cherry"]) should return [5, 6, 6]
# - string_lengths(["hi", "hello", "world"]) should return [2, 5, 5]
#
# Algorithm: Define helper function that calls len(), use map() to apply to each string.
# ============================================================================
"""
Problem: 316
Write a Python program to find the length of each string in a list using `map()`.

# EXPLICATION DE LA SOLUTION :
# This solution defines a helper function `length()` that takes a string and returns
# its length using the len() function. The main function then uses `map()` to apply
# this length function to each string in the input list. The result is converted
# to a list using list() since map() returns an iterator. This creates a parallel
# list of lengths corresponding to each string.
def string_lengths(strings):
    # Function definition
    def length(s):
        # Function definition
        return len(s)
            # Returns the result
    return list(map(length, strings))
        # Returns the result

# Example usage
string_list = ["apple", "banana", "cherry", "date"]
lengths = string_lengths(string_list)
print("Original list of strings:", string_list)
print("Lengths of each string:", lengths)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires converting a list of temperatures from Fahrenheit to
# Celsius using the `map()` function. The conversion formula is: C = (F - 32) × 5/9.
# La fonction doit prendre a list of Fahrenheit temperatures and return a new list
# with the corresponding Celsius temperatures.
#
# Prérequis Clés :
# - Function must accept a list of Fahrenheit temperatures as input
# - Function must use `map()` to convert temperatures
# - Function must return a new list of Celsius temperatures
# - Must apply the conversion formula: (F - 32) * 5 / 9
#
# Exemple d'Entrée/Sortie :
# - fahrenheit_to_celsius([32, 68, 100, 212]) should return [0.0, 20.0, 37.78, 100.0]
# - fahrenheit_to_celsius([0, 32, 100]) should return [-17.78, 0.0, 37.78]
#
# Algorithm: Define helper function with conversion formula, use map() to apply to each temperature.
# ============================================================================
"""
Problem: 317
Write a Python program to convert a list of temperatures from Fahrenheit to Celsius using `map()`.

# EXPLICATION DE LA SOLUTION :
# This solution defines a helper function `to_celsius()` that takes a Fahrenheit
# temperature and converts it to Celsius using the formula (f - 32) * 5 / 9. The
# main function then uses `map()` to apply this conversion function to each temperature
# in the input list. The result is converted to a list using list() since map()
# returns an iterator. This efficiently converts all temperatures in one operation.
def fahrenheit_to_celsius(temperatures):
    # Function definition
    def to_celsius(f):
        # Function definition
        return (f - 32) * 5 / 9
            # Returns the result
    return list(map(to_celsius, temperatures))
        # Returns the result

# Example usage
fahrenheit_temps = [32, 68, 100, 212]  # Sample temperatures in Fahrenheit
celsius_temps = fahrenheit_to_celsius(fahrenheit_temps)
print("Temperatures in Fahrenheit:", fahrenheit_temps)
print("Temperatures in Celsius:", celsius_temps)


# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires adding 5 to each number in a list using the `map()` function.
# La fonction doit prendre a list of numbers and return a new list where each number
# has been increased by 5. Cela démontre using map() for simple arithmetic
# transformations on list elements.
#
# Prérequis Clés :
# - Function must accept a list of numbers as input
# - Function must use `map()` to add 5 to each number
# - Function must return a new list with incremented values
# - Must add 5 to each element: x + 5
#
# Exemple d'Entrée/Sortie :
# - add_five([1, 2, 3, 4]) should return [6, 7, 8, 9]
# - add_five([10, 20, 30]) should return [15, 25, 35]
#
# Algorithm: Define helper function that returns x + 5, use map() to apply to each number.
# ============================================================================
"""
Problem: 319
Write a Python program to add 5 to each number in a list using `map()`.

# EXPLICATION DE LA SOLUTION :
# This solution defines a helper function `add_five_to_number()` that takes a number
# and returns it plus 5. The main function `add_five()` then uses `map()` to apply
# this transformation to each number in the input list. The result is converted
# to a list using list() since map() returns an iterator. This efficiently adds
# 5 to all elements in one operation.
def add_five_to_number(x):
    # Function definition
    return x + 5
        # Returns the result

def add_five(lst):
    # Function definition
    return list(map(add_five_to_number, lst))
        # Returns the result

lst = [1, 2, 3, 4]
print(add_five(lst))

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires computing the square root of each number in a list using
# the `map()` function. La fonction doit prendre a list of numbers and return a
# new list containing the square root of each number. Cela démontre using
# map() with mathematical functions.
#
# Prérequis Clés :
# - Function must accept a list of numbers as input
# - Function must use `map()` to compute square roots
# - Function must return a new list with square root values
# - Must use math.sqrt() or ** 0.5 for square root calculation
#
# Exemple d'Entrée/Sortie :
# - square_roots([1, 4, 9, 16, 25]) should return [1.0, 2.0, 3.0, 4.0, 5.0]
# - square_roots([16, 64, 100]) should return [4.0, 8.0, 10.0]
#
# Algorithm: Define helper function using math.sqrt(), use map() to apply to each number.
# ============================================================================
"""
Problem: 320
Write a Python program to compute the square root of each number in a list using `map()`.

# EXPLICATION DE LA SOLUTION (First version - incorrect):
# Remarque : The first solution has a bug - it computes the square (x ** 2) instead of
# the square root. The function name is also misspelled as "sqaure_root".
def main(lst):
    # Function definition
    def sqaure_root(num):
        # Function definition
        return num ** 2
            # Returns the result
    return list(map(sqaure_root, lst))
        # Returns the result

lst = [567, 4, 1, 57]
main(lst)

# CORRECT EXPLICATION DE LA SOLUTION :
# This solution correctly computes square roots using the math.sqrt() function.
# It defines a helper function `square_root()` that takes a number and returns
# its square root using math.sqrt(). The main function then uses `map()` to apply
# this function to each number in the input list. The result is converted to a
# list using list() since map() returns an iterator.
import math
def square_roots(numbers):
    # Function definition
    def square_root(x):
        # Function definition
        return math.sqrt(x)
            # Returns the result
    return list(map(square_root, numbers))
        # Returns the result

# Example usage
number_list = [1, 4, 9, 16, 25]
roots = square_roots(number_list)
print("Original numbers:", number_list)
print("Square roots:", roots)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires converting a list of strings to a list of their lengths
# using the `map()` function. This is similar to problem 316, where we find the
# length of each string. La fonction doit retourner a new list containing integers
# representing the length of each corresponding string.
#
# Prérequis Clés :
# - Function must accept a list of strings as input
# - Function must use `map()` to find lengths
# - Function must return a new list of integers (lengths)
# - Must use len() function for each string
#
# Exemple d'Entrée/Sortie :
# - lengths_of_strings(["apple", "banana", "cherry"]) should return [5, 6, 6]
# - lengths_of_strings(["hi", "hello"]) should return [2, 5]
#
# Algorithm: Define helper function that calls len(), use map() to apply to each string.
# ============================================================================
"""
Problem: 321
Write a Python program to convert a list of strings to a list of their lengths using `map()`.

# EXPLICATION DE LA SOLUTION :
# This solution defines a helper function `length()` that takes a string and returns
# its length using the len() function. The main function then uses `map()` to apply
# this length function to each string in the input list. The result is converted
# to a list using list() since map() returns an iterator. This creates a parallel
# list of lengths corresponding to each string.
def lengths_of_strings(strings):
    # Function definition
    def length(s):
        # Function definition
        return len(s)
            # Returns the result
    return list(map(length, strings))
        # Returns the result

# Example usage
string_list = ["apple", "banana", "cherry", "date"]
lengths = lengths_of_strings(string_list)
print("Original strings:", string_list)
print("Lengths of strings:", lengths)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires normalizing a list of scores to a range of 0 to 1 using
# the `map()` function. Normalization scales values so the minimum becomes 0 and
# the maximum becomes 1, with all other values proportionally scaled. The formula
# is: normalized = (value - min) / (max - min).
#
# Prérequis Clés :
# - Function must accept a list of scores as input
# - Function must use `map()` to normalize scores
# - Function must return a new list with normalized values (0 to 1 range)
# - Must apply normalization formula: (score - min) / (max - min)
#
# Exemple d'Entrée/Sortie :
# - normalize_scores([50, 60, 70, 80, 90]) should return [0.0, 0.25, 0.5, 0.75, 1.0]
# - normalize_scores([10, 20, 30]) should return [0.0, 0.5, 1.0]
#
# Algorithm: Find min and max, define helper function with normalization formula,
# use map() to apply to each score.
# ============================================================================
"""
Problem: 322
Write a Python program to normalize a list of scores to a range of 0 to 1 using `map()`.

# EXPLICATION DE LA SOLUTION :
# This solution defines a helper function `normalize()` that takes a score and
# normalizes it using the formula (score - min_score) / (max_score - min_score).
# Note that min() and max() are called inside the helper function for each score,
# which is inefficient (they should be calculated once outside). The main function
# uses `map()` to apply this normalization to each score. The result is converted
# to a list using list() since map() returns an iterator.
def normalize_scores(scores):
    # Function definition
    def normalize(score):
        # Function definition
        min_score = min(scores)
        max_score = max(scores)
        return (score - min_score) / (max_score - min_score)
            # Returns the result
    return list(map(normalize, scores))
        # Returns the result

# Example usage
score_list = [50, 60, 70, 80, 90]
normalized_scores = normalize_scores(score_list)
print("Original scores:", score_list)
print("Normalized scores:", normalized_scores)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires reversing each string in a list using the `map()` function.
# La fonction doit prendre a list of strings and return a new list where each
# string has been reversed. For example, "hello" becomes "olleh". Cela démontre
# using map() with string slicing operations.
#
# Prérequis Clés :
# - Function must accept a list of strings as input
# - Function must use `map()` to reverse strings
# - Function must return a new list with reversed strings
# - Must reverse each string (e.g., using slicing [::-1])
#
# Exemple d'Entrée/Sortie :
# - reverse_strings(["hello", "world", "python"]) should return ["olleh", "dlrow", "nohtyp"]
# - reverse_strings(["abc", "def"]) should return ["cba", "fed"]
#
# Algorithm: Define helper function using string slicing [::-1], use map() to apply to each string.
# ============================================================================
"""
Problem: 323
Write a Python program to reverse each string in a list using `map()`.

# EXPLICATION DE LA SOLUTION :
# This solution defines a helper function `reverse()` that takes a string and returns
# its reverse using string slicing [::-1], which creates a reversed copy of the string.
# The main function then uses `map()` to apply this reversal function to each string in
# the input list. The result is converted to a list using list() since map() returns
# an iterator. This efficiently reverses all strings in one operation.
def reverse_strings(strings):
    # Function definition
    def reverse(s):
        # Function definition
        return s[::-1]
            # Returns the result
    return list(map(reverse, strings))
        # Returns the result

# Example usage
string_list = ["hello", "world", "python", "programming"]
reversed_strings = reverse_strings(string_list)
print("Original strings:", string_list)
print("Reversed strings:", reversed_strings)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires doubling each number in a list using the `map()` function.
# La fonction doit prendre a list of numbers and return a new list where each number
# has been multiplied by 2. This is similar to problem 315 (squaring) but simpler.
#
# Prérequis Clés :
# - Function must accept a list of numbers as input
# - Function must use `map()` to double each number
# - Function must return a new list with doubled values
# - Must multiply each number by 2: x * 2
#
# Exemple d'Entrée/Sortie :
# - double_numbers([1, 2, 3, 4, 5]) should return [2, 4, 6, 8, 10]
# - double_numbers([10, 20, 30]) should return [20, 40, 60]
#
# Algorithm: Define helper function that returns x * 2, use map() to apply to each number.
# ============================================================================
"""
Problem: 324
Write a Python program to double each number in a list using `map()`.

# EXPLICATION DE LA SOLUTION :
# This solution defines a helper function `double()` that takes a number and returns
# it multiplied by 2. The main function then uses `map()` to apply this doubling
# function to each number in the input list. The result is converted to a list using
# list() since map() returns an iterator. This efficiently doubles all elements in one operation.
def double_numbers(numbers):
    # Function definition
    def double(x):
        # Function definition
        return x * 2
            # Returns the result
    return list(map(double, numbers))
        # Returns the result

# Example usage
number_list = [1, 2, 3, 4, 5]
doubled_numbers = double_numbers(number_list)
print("Original numbers:", number_list)
print("Doubled numbers:", doubled_numbers)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires removing leading and trailing whitespace from each string
# in a list using the `map()` function. The function should use the .strip() method
# to clean up strings that may have extra spaces at the beginning or end. This is
# une opération courante data cleaning operation.
#
# Prérequis Clés :
# - Function must accept a list of strings as input
# - Function must use `map()` to strip whitespace
# - Function must return a new list with stripped strings
# - Must use .strip() method to remove leading/trailing whitespace
#
# Exemple d'Entrée/Sortie :
# - strip_whitespace(["  Hello  ", "  World  "]) should return ["Hello", "World"]
# - strip_whitespace(["  python  ", "  programming  "]) should return ["python", "programming"]
#
# Algorithm: Define helper function that calls .strip(), use map() to apply to each string.
# ============================================================================
"""
Problem: 325
Write a Python program to remove leading and trailing whitespace from each string in a list using `map()`.

# EXPLICATION DE LA SOLUTION :
# This solution defines a helper function `strip()` that takes a string and returns
# its stripped version using the .strip() method, which removes leading and trailing
# whitespace. The main function then uses `map()` to apply this stripping function
# to each string in the input list. The result is converted to a list using list()
# since map() returns an iterator. This efficiently cleans all strings in one operation.
def strip_whitespace(strings):
    # Function definition
    def strip(s):
        # Function definition
        return s.strip()
            # Returns the result
    return list(map(strip, strings))
# Example usage
string_list = ["  Hello  ", "  World  ", "  Python  ", "  Programming  "]
stripped_strings = strip_whitespace(string_list)
print("Original strings:", string_list)
print("Stripped strings:", stripped_strings)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a list of tuples where each tuple contains a number
# and its square using the `map()` function. For example, [1, 2, 3] should become
# [(1, 1), (2, 4), (3, 9)]. Cela démontre using map() to create structured data.
#
# Prérequis Clés :
# - Function must accept a list of numbers as input
# - Function must use `map()` to create tuples
# - Function must return a new list of tuples (number, square)
# - Each tuple must contain (x, x * x)
#
# Exemple d'Entrée/Sortie :
# - number_and_square([1, 2, 3, 4, 5]) should return [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
# - number_and_square([10, 20]) should return [(10, 100), (20, 400)]
#
# Algorithm: Define helper function that returns (x, x*x), use map() to apply to each number.
# ============================================================================
"""
Problem: 326
Write a Python program to create a list of tuples where each tuple contains a number and its square using `map()`.

# EXPLICATION DE LA SOLUTION :
# This solution defines a helper function `create_tuple()` that takes a number and
# returns a tuple containing the number and its square (x, x * x). The main function
# then uses `map()` to apply this tuple creation function to each number in the input
# list. The result is converted to a list using list() since map() returns an iterator.
# This efficiently creates structured tuples for all numbers in one operation.
def number_and_square(numbers):
    # Function definition
    def create_tuple(x):
        # Function definition
        return (x, x * x)
            # Returns the result
    return list(map(create_tuple, numbers))
        # Returns the result

# Example usage
numbers_list = [1, 2, 3, 4, 5]
squared_tuples = number_and_square(numbers_list)
print("Numbers and their squares:", squared_tuples)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires converting a list of strings to title case using the `map()`
# function. Title case capitalizes the first letter of each word and lowercases the
# rest. For example, "hello world" becomes "Hello World". Cela démontre using
# map() with string formatting methods.
#
# Prérequis Clés :
# - Function must accept a list of strings as input
# - Function must use `map()` to convert to title case
# - Function must return a new list with title-cased strings
# - Must use .title() method for conversion
#
# Exemple d'Entrée/Sortie :
# - to_title_case(["hello world", "python programming"]) should return ["Hello World", "Python Programming"]
# - to_title_case(["hello", "world"]) should return ["Hello", "World"]
#
# Algorithm: Define helper function that calls .title(), use map() to apply to each string.
# ============================================================================
"""
Problem: 327
Write a Python program to convert a list of strings to title case using `map()`.

# EXPLICATION DE LA SOLUTION :
# This solution defines a helper function `title_case()` that takes a string and
# returns its title-cased version using the .title() method, which capitalizes the
# first letter of each word. The main function then uses `map()` to apply this
# transformation to each string in the input list. The result is converted to a
# list using list() since map() returns an iterator. This efficiently formats all
# strings in one operation.
def to_title_case(strings):
    # Function definition
    def title_case(s):
        # Function definition
        return s.title()
            # Returns the result
    return list(map(title_case, strings))
        # Returns the result

# Example usage
words = ["hello world", "python programming", "enumerate function"]
result = to_title_case(words)
print(result)  # ['Hello World', 'Python Programming', 'Enumerate Function']

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires finding the second largest number in a list with constraints:
# no for loop and no map(). The function should prompt the user for input and handle
# the case where there might be duplicate numbers. The solution typically uses sorting
# and set operations to find unique values, then selects the second largest.
#
# Prérequis Clés :
# - Function must prompt user for input (list of numbers)
# - Function must find the second largest number
# - Cannot use a for loop
# - Cannot use map()
# - Should handle duplicate numbers (typically by using set to get unique values)
#
# Exemple d'Entrée/Sortie :
# - second_largest_number() with input "5 2 8 1 9 8" should return 8 (second largest)
# - second_largest_number() with input "10 20 30" should return 20
#
# Algorithm: Get input, convert to integers, use set to get unique values, sort, return [-2].
# ============================================================================
"""
Problem: 328
Write a Python program to find the second largest number in a list. Prompt the user to enter a list of numbers, do not use a for loop, do not use map().

# EXPLICATION DE LA SOLUTION :
# This solution gets user input, splits it, and converts to integers. Remarque : The
# solution uses a for loop to convert strings to integers, which violates the
# constraint. A better approach would use list comprehension or other methods. It
# then uses set() to get unique numbers, converts back to list, sorts, and returns
# the second-to-last element (index -2). It also handles the edge case where there
# aren't enough unique numbers.
def second_largest_number():
    # Function definition
    user_input = input("Type numbers separated by spaces: ").split()
        # Gets user input

    user_int = []
    for num in user_input:
        # Iterates through each element
        user_int.append(int(num))

    unique_numbers = set(user_int)
    unique_numbers = list(unique_numbers)
    unique_numbers.sort()

    if len(unique_numbers) > 1:
        second_largest = unique_numbers[-2]
    else:
        second_largest = "Not enough unique numbers"

    print(second_largest)

second_largest_number()

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires sorting a list of numeric strings from smallest to biggest
# (ascending order) without using a for loop. La fonction doit prendre a list of
# string representations of numbers and return them sorted numerically. This
# demonstrates sorting with a key function to handle string-to-number conversion.
#
# Prérequis Clés :
# - Function must accept a list of numeric strings as input
# - Function must return a sorted list (smallest to biggest)
# - Cannot use a for loop
# - Must sort numerically (not alphabetically)
#
# Exemple d'Entrée/Sortie :
# - list_string(["377", "55", "44"]) should return ["44", "55", "377"]
# - list_string(["10", "2", "100"]) should return ["2", "10", "100"]
#
# Algorithm: Use sorted() with key=int to convert strings to integers for comparison.
# ============================================================================
"""
Problème 329 :
Écrivez une fonction où utilisateur tapez une liste de nombres dans chaîne et retourne une liste de nombres de plus petit à biggest. N'utilisez pas un pour loop.
"""

# EXPLICATION DE LA SOLUTION :
# This solution uses the `sorted()` function with a `key=int` parameter. The key
# parameter converts each string to an integer for comparison purposes, ensuring
# numerical sorting rather than alphabetical sorting. This allows "44" to come
# before "377" even though alphabetically "3" comes before "4". The sorted() function
# returns a new sorted list without modifying the original.
def list_string(numbers):
    # Function definition
    sort = sorted(numbers, key=int)
        # Sorts elements in ascending order
    return sort
        # Returns the result

lst = ["377", "55", "44"]
print(list_string(lst))

def type_smallest_biggest():
    # Function definition
    user = input("type number list: ").split()
        # Gets user input
    sort_number = sorted(user, key=int)
        # Sorts elements in ascending order

    print(sort_number)

type_smallest_biggest()

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires sorting a list of numeric strings from biggest to smallest
# (descending order) without using a for loop. This is the reverse of problem 329.
# La fonction doit prendre a list of string representations of numbers and return
# them sorted in descending numerical order.
#
# Prérequis Clés :
# - Function must accept a list of numeric strings as input
# - Function must return a sorted list (biggest to smallest)
# - Cannot use a for loop
# - Must sort numerically in descending order
#
# Exemple d'Entrée/Sortie :
# - list_of_string_numbers(["44", "66", "3", "477"]) should return ["477", "66", "44", "3"]
# - list_of_string_numbers(["10", "2", "100"]) should return ["100", "10", "2"]
#
# Algorithm: Use sorted() with key=int and reverse=True, or use [::-1] to reverse sorted list.
# ============================================================================
"""
Problème 330 :
Écrivez une fonction où utilisateur tapez une liste de nombres dans chaîne et retourne une liste de nombres de biggest à plus petit. N'utilisez pas un pour loop.
"""

# EXPLICATION DE LA SOLUTION :
# This solution uses `sorted()` with `key=int` to sort numerically, then reverses
# the result using slicing [::-1] to get descending order. Alternatively, the second
# solution uses `sorted()` with both `key=int` and `reverse=True` parameters. Both
# approaches correctly sort the numeric strings from largest to smallest. Remarque : The
# second solution uses map() which might violate constraints depending on interpretation.
def list_of_string_numbers(n):
    # Function definition
    sort = sorted(n, key=int)[::-1]
        # Sorts elements in ascending order

    return sort
        # Returns the result

numbers = ["44", "66", "3", "477"]
print(list_of_string_numbers(numbers))

def type_biggest_smallest():
    # Function definition
    user = input("Type numbers: ").split()
        # Gets user input
    int_list = list(map(int, user))
    sorted_list = sorted(int_list, reverse=True)
        # Sorts elements in ascending order

    print(sorted_list)

type_biggest_smallest()

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires printing both the index and element of each item in a list
# using the `enumerate()` function. The enumerate() function returns pairs of
# (index, value) for each element, making it easy to access both simultaneously.
# This is une opération courante pattern when you need both position and value information.
#
# Prérequis Clés :
# - Function must accept a list as input
# - Function must use `enumerate()` to get index-element pairs
# - Function must print both index and element for each item
# - Should format output clearly (e.g., "Index: 0, Element: apple")
#
# Exemple d'Entrée/Sortie :
# - print_index_and_element(['apple', 'banana', 'cherry']) should print:
#   Index: 0, Element: apple
#   Index: 1, Element: banana
#   Index: 2, Element: cherry
#
# Algorithm: Use enumerate() in a for loop to get (index, element) pairs, print both.
# ============================================================================
"""
Problem: 331
Write a Python program to print the index and element of each item in a list using `enumerate()`.

# EXPLICATION DE LA SOLUTION :
# This solution uses a for loop with `enumerate()` to iterate through the list.
# The enumerate() function automatically provides both the index (starting from 0)
# and the element value for each iteration. The formatted string prints both values
# in a clear, readable format. This is more Pythonic than manually managing an index
# counter with range(len(lst)).
def print_index_and_element(lst):
    # Function definition
    for index, element in enumerate(lst):
        # Iterates through each element
        print(f"Index: {index}, Element: {element}")

# Example usage
lst = ['apple', 'banana', 'cherry']
print_index_and_element(lst)
# Sortie :
# Index: 0, Element: apple
# Index: 1, Element: banana
# Index: 2, Element: cherry

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a list of tuples where each tuple contains an index
# and its corresponding element from a list using `enumerate()`. For example, ['apple',
# 'banana'] should become [(0, 'apple'), (1, 'banana')]. Cela démontre using
# enumerate() to create structured data pairs.
#
# Prérequis Clés :
# - Function must accept a list as input
# - Function must use `enumerate()` to get index-element pairs
# - Function must return a list of tuples (index, element)
# - Each tuple should contain (index, corresponding_element)
#
# Exemple d'Entrée/Sortie :
# - create_index_element_tuples(['apple', 'banana', 'cherry']) should return
#   [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
#
# Algorithm: Use enumerate() in a for loop, append (index, element) tuples to result list.
# ============================================================================
"""
Problem: 332
Write a Python program to create a list of tuples where each tuple contains an index and the corresponding element from a list using `enumerate()`.

# EXPLICATION DE LA SOLUTION :
# This solution uses a for loop with `enumerate()` to iterate through the list,
# getting both index and element for each iteration. It appends a tuple (index, element)
# to a result list for each item. The enumerate() function makes this straightforward
# by providing both values simultaneously, avoiding the need to manually track indices.
def create_index_element_tuples(lst):
    # Function definition
    result = []
    for index, element in enumerate(lst):
        # Iterates through each element
        result.append((index, element))
    return result
        # Returns the result

# Example usage
lst = ['apple', 'banana', 'cherry']
result = create_index_element_tuples(lst)
print(result)  # [(0, 'apple'), (1, 'banana'), (2, 'cherry')]

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires printing each element in a list along with its index using
# `enumerate()`. This is similar to problem 331 but with a simpler output format.
# The function should display both the index and the element value for each string.
#
# Prérequis Clés :
# - Function must accept a list of strings as input
# - Function must use `enumerate()` to get index-element pairs
# - Function must print both index and element for each item
# - Output format should be simple (e.g., "0 apple", "1 banana")
#
# Exemple d'Entrée/Sortie :
# - print_with_index(["apple", "banana", "cherry"]) should print:
#   0 apple
#   1 banana
#   2 cherry
#
# Algorithm: Use enumerate() in a for loop, print index and value.
# ============================================================================
"""
Problem: 333
Write a Python program to print each element with its index in a list of strings using `enumerate()`.

# EXPLICATION DE LA SOLUTION :
# This solution uses a for loop with `enumerate()` to iterate through the list of
# strings. For each iteration, it prints both the index and the value separated by
# a space. This is a simple and direct use of enumerate() to display index-value pairs.
def print_with_index(strings):
    # Function definition
    for index, value in enumerate(strings):
        # Iterates through each element
        print(index, value)

strings = ["apple", "banana", "cherry", "date", "fig"]
print_with_index(strings)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a dictionary from a list where the keys are the
# indexes and the values are the corresponding elements using `enumerate()`. This
# converts a list into a dictionary mapping positions to values. This is useful
# when you need dictionary-style access to list elements.
#
# Prérequis Clés :
# - Function must accept a list as input
# - Function must use `enumerate()` to get index-element pairs
# - Function must return a dictionary
# - Dictionary keys should be indexes (integers), values should be elements
#
# Exemple d'Entrée/Sortie :
# - list_to_dict(['apple', 'banana', 'cherry']) should return {0: 'apple', 1: 'banana', 2: 'cherry'}
#
# Algorithm: Use enumerate() in a for loop, assign result[index] = element for each item.
# ============================================================================
"""
Problem: 334
Write a Python program to generate a dictionary where keys are indexes and values are elements from a list using `enumerate()`.

# EXPLICATION DE LA SOLUTION :
# This solution initializes an empty dictionary, then uses a for loop with `enumerate()`
# to iterate through the list. For each iteration, it assigns the element to the
# dictionary using the index as the key: result[index] = element. This creates a
# mapping from positions to values. Remarque : dict(enumerate(lst)) is a more concise
# alternative that achieves the same result.
def list_to_dict(lst):
    # Function definition
    result = {}
    for index, element in enumerate(lst):
        # Iterates through each element
        result[index] = element
    return result
        # Returns the result

# Example usage
lst = ['apple', 'banana', 'cherry']
result = list_to_dict(lst)
print(result)  # {0: 'apple', 1: 'banana', 2: 'cherry'}

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires finding the index of a specific element in a list using
# `enumerate()`. The function should search through the list and return the index
# of the first occurrence of the target element. If the element is not found, it
# should return -1 (or None). Cela démontre using enumerate() for searching.
#
# Prérequis Clés :
# - Function must accept a list and a target element as input
# - Function must use `enumerate()` to search
# - Function must return the index of the element (or -1 if not found)
# - Should return the first occurrence if element appears multiple times
#
# Exemple d'Entrée/Sortie :
# - find_index(['apple', 'banana', 'cherry'], 'banana') should return 1
# - find_index(['apple', 'banana', 'cherry'], 'grape') should return -1
#
# Algorithm: Use enumerate() in a for loop, check if value == element, return index when found.
# ============================================================================
"""
Problem: 335
Write a Python program to find the index of a specific element in a list using `enumerate()`.

# EXPLICATION DE LA SOLUTION :
# This solution uses a for loop with `enumerate()` to iterate through the list.
# For each iteration, it checks if the current value matches the target element.
# If a match is found, it immediately returns the index. If the loop completes
# without finding a match, it returns -1 to indicate the element was not found.
# This is a linear search implementation using enumerate().
def find_index(lst, element):
    # Function definition
    for index, value in enumerate(lst):
        # Iterates through each element
        if value == element:
            # Checks condition
            return index
                # Returns the result
    return -1
        # Returns the result

# Example usage
lst = ['apple', 'banana', 'cherry']
index = find_index(lst, 'banana')
print(index)  # 1

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires printing each element with its index separated by a colon
# using `enumerate()`. This is similar to problems 331 and 333 but with a specific
# formatting requirement (colon separator). The output should be in the format
# "index: element".
#
# Prérequis Clés :
# - Function must accept a list as input
# - Function must use `enumerate()` to get index-element pairs
# - Function must print in format "index: element" (colon separator)
# - Each line should show one index-element pair
#
# Exemple d'Entrée/Sortie :
# - print_index_and_element_with_colon(['apple', 'banana', 'cherry']) should print:
#   0: apple
#   1: banana
#   2: cherry
#
# Algorithm: Use enumerate() in a for loop, print formatted string with colon separator.
# ============================================================================
"""
Problem: 336
Write a Python program to print each element of a list with its index separated by a colon using `enumerate()`.

# EXPLICATION DE LA SOLUTION :
# This solution uses a for loop with `enumerate()` to iterate through the list.
# For each iteration, it prints a formatted string using an f-string that includes
# both the index and element separated by a colon. This creates a clean, readable
# output format showing the position and value of each element.
def print_index_and_element_with_colon(lst):
    # Function definition
    for index, element in enumerate(lst):
        # Iterates through each element
        print(f"{index}: {element}")

# Example usage
lst = ['apple', 'banana', 'cherry']
print_index_and_element_with_colon(lst)
# Sortie :
# 0: apple
# 1: banana
# 2: cherry

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a list of strings where each string includes its
# index with a custom prefix using `enumerate()`. For example, with prefix "Item ",
# ['apple', 'banana'] should become ['Item 0: apple', 'Item 1: banana']. This
# demonstrates custom string formatting with enumerate().
#
# Prérequis Clés :
# - Function must accept a list and a prefix string as input
# - Function must use `enumerate()` to get index-element pairs
# - Function must return a list of formatted strings
# - Each string should include prefix, index, and element
#
# Exemple d'Entrée/Sortie :
# - create_indexed_strings(['apple', 'banana'], "Item ") should return
#   ['Item 0: apple', 'Item 1: banana']
#
# Algorithm: Use enumerate() in a for loop, format string with prefix, index, and element.
# ============================================================================
"""
Problem: 337
Write a Python program to create a list of strings where each string includes its index with a custom prefix using `enumerate()`.

# EXPLICATION DE LA SOLUTION :
# This solution initializes an empty result list, then uses a for loop with
# `enumerate()` to iterate through the input list. For each iteration, it creates
# a formatted string that combines the prefix, index, and element using an f-string.
# This formatted string is appended to the result list. This allows for customizable
# labeling of list elements with their positions.
def create_indexed_strings(lst, prefix):
    # Function definition
    result = []
    for index, element in enumerate(lst):
        # Iterates through each element
        result.append(f"{prefix}{index}: {element}")
    return result
        # Returns the result

# Example usage
lst = ['apple', 'banana', 'cherry']
result = create_indexed_strings(lst, "Item ")
print(result)  # ['Item 0: apple', 'Item 1: banana', 'Item 2: cherry']

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires modifying elements in a list based on their index using
# `enumerate()`. The function should use the index information to transform each
# element. Cela démontre how enumerate() can be used for index-based modifications,
# such as multiplying by index, adding index, or other transformations.
#
# Prérequis Clés :
# - Function must accept a list as input
# - Function must use `enumerate()` to access both index and element
# - Function must modify elements based on their index
# - Modifications should use the index value in some way
#
# Exemple d'Entrée/Sortie :
# - modify_elements([10, 20, 30]) might return [0, 20, 60] (multiply by index)
# - The specific modification depends on the implementation
#
# Algorithm: Use enumerate() in a for loop, modify lst[index] based on index value.
# ============================================================================
"""
Problem: 338
Write a Python program to modify elements in a list based on their index using `enumerate()`.

# EXPLICATION DE LA SOLUTION :
# This solution uses a for loop with `enumerate()` to iterate through the list.
# For each iteration, it accesses both the index and element, then modifies the
# list element at that index position. The modification uses the index value in
# some way (e.g., multiplying the element by its index). Since lists are mutable,
# the modifications are made in-place. Remarque : The specific modification pattern
# depends on the problem requirements.
def modify_elements(lst):
    # Function definition
    for index, element in enumerate(lst):
        # Iterates through each element
        if index % 2 == 0:  # Modify elements at even indices
            lst[index] = element.upper()
                # Converts to lowercase/uppercase
    return lst
        # Returns the result

# Example usage
lst = ['apple', 'banana', 'cherry', 'date']
result = modify_elements(lst)
print(result)  # ['APPLE', 'banana', 'CHERRY', 'date']

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires computing the sum of elements in a list where each element
# is multiplied by its index using `enumerate()`. For example, [2, 4, 6, 8] would
# calculate: 0*2 + 1*4 + 2*6 + 3*8 = 0 + 4 + 12 + 24 = 40. Cela démontre
# using enumerate() for weighted summation based on position.
#
# Prérequis Clés :
# - Function must accept a list of numbers as input
# - Function must use `enumerate()` to get index-element pairs
# - Function must return the sum of (index * element) for all elements
# - Must multiply each element by its index before summing
#
# Exemple d'Entrée/Sortie :
# - sum_of_elements([2, 4, 6, 8]) should return 40 (0*2 + 1*4 + 2*6 + 3*8)
# - sum_of_elements([1, 2, 3]) should return 8 (0*1 + 1*2 + 2*3)
#
# Algorithm: Use enumerate() in a for loop, accumulate sum of (index * element).
# ============================================================================
"""
339
Write a Python program to compute the sum of elements in a list where each element is multiplied by its index using `enumerate()`.

# EXPLICATION DE LA SOLUTION :
# This solution initializes a total_sum variable to 0, then uses a for loop with
# `enumerate()` to iterate through the list. For each iteration, it multiplies
# the index (i) by the element (num) and adds the result to the total_sum.
# This accumulates the weighted sum where each element is weighted by its position
# in the list. The function returns the final sum.
def sum_of_elements(lst):
    # Function definition
    total_sum = 0

    for i, num in enumerate(lst):
        # Iterates through each element
        total_sum += i * num
    return total_sum
        # Returns the result

lst = [2, 4, 6, 8]
print(sum_of_elements(lst))

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires printing only the elements that are located at odd indexes
# (1, 3, 5, ...) in a list using `enumerate()`. The function should skip elements
# at even indexes (0, 2, 4, ...) and only print those at odd positions. This
# demonstrates conditional filtering with enumerate().
#
# Prérequis Clés :
# - Function must accept a list as input
# - Function must use `enumerate()` to get index-element pairs
# - Function must print only elements at odd indexes
# - Must check if index % 2 != 0 (odd index)
#
# Exemple d'Entrée/Sortie :
# - print_odd_index_elements(['apple', 'banana', 'cherry', 'date']) should print:
#   banana
#   date
#
# Algorithm: Use enumerate() in a for loop, check if index % 2 != 0, print if odd.
# ============================================================================
"""
Problem: 340
Write a Python program to print elements from a list that are located at odd indexes using `enumerate()`.

# EXPLICATION DE LA SOLUTION :
# This solution uses a for loop with `enumerate()` to iterate through the list.
# For each iteration, it checks if the index is odd using the condition index % 2 != 0.
# If the index is odd (1, 3, 5, ...), it prints the corresponding element. This
# effectively filters and prints only elements at odd positions in the list.
def print_odd_index_elements(lst):
    # Function definition
    for index, element in enumerate(lst):
        # Iterates through each element
        if index % 2 != 0:
            print(element)

# Example usage
lst = ['apple', 'banana', 'cherry', 'date']
print_odd_index_elements(lst)
# Sortie :
# banana
# date

"""
Problem: 341
Write a Python program to create a list of tuples where each tuple contains an index and element from a list, but only if the element starts with a vowel, using `enumerate()`.

def index_element_if_vowel(lst):
    # Function definition
    result = []
    vowels = 'aeiouAEIOU'
    for index, element in enumerate(lst):
        # Iterates through each element
        if element[0] in vowels:
            result.append((index, element))
    return result
        # Returns the result

# Example usage
lst = ['apple', 'banana', 'orange', 'grape']
result = index_element_if_vowel(lst)
print(result)  # [(0, 'apple'), (2, 'orange')]

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires finding both the maximum element in a list and its index
# using `enumerate()`. La fonction doit retourner both the index and the maximum
# value. This is useful when you need to know not just the maximum value, but also
# where it appears in the list.
#
# Prérequis Clés :
# - Function must accept a list as input
# - Function must use `enumerate()` to get index-element pairs
# - Function must return both the index and maximum element
# - Should return the first occurrence if maximum appears multiple times
#
# Exemple d'Entrée/Sortie :
# - find_max_and_index([10, 20, 30, 25]) should return (2, 30)
# - find_max_and_index([5, 3, 8, 8]) should return (2, 8) (first occurrence)
#
# Algorithm: Initialize max to first element, use enumerate() to iterate, update max and index when larger element found.
# ============================================================================
"""
Problem: 342
Write a Python program to find the maximum element in a list and its index using `enumerate()`.

# EXPLICATION DE LA SOLUTION :
# This solution initializes max_element to the first element and max_index to 0.
# It then uses a for loop with `enumerate()` to iterate through the list. For each
# iteration, it compares the current element with the current maximum. If a larger
# element is found, it updates both max_element and max_index. This tracks both
# the maximum value and its position simultaneously. The function returns a tuple
# (max_index, max_element).
def find_max_and_index(lst):
    # Function definition
    max_element = lst[0]
    max_index = 0
    for index, element in enumerate(lst):
        # Iterates through each element
        if element > max_element:
            max_element = element
            max_index = index
    return max_index, max_element
        # Returns the result

# Example usage
lst = [10, 20, 30, 25]
index, max_element = find_max_and_index(lst)
print(f"Max element: {max_element}, Index: {index}")
# Sortie : Max element: 30, Index: 2

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a list of tuples with (index, element) pairs,
# but excluding the first N elements using `enumerate()`. For example, if n=2,
# skip the first 2 elements and only include tuples starting from index 2. This
# demonstrates conditional filtering based on index position.
#
# Prérequis Clés :
# - Function must accept a list and an integer n as input
# - Function must use `enumerate()` to get index-element pairs
# - Function must return a list of tuples (index, element)
# - Must exclude elements where index < n
# - Only include elements where index >= n
#
# Exemple d'Entrée/Sortie :
# - index_and_element_excluding_first_n(['apple', 'banana', 'cherry', 'date'], 2)
#   should return [(2, 'cherry'), (3, 'date')]
#
# Algorithm: Use enumerate() in a for loop, check if index >= n, append tuple if true.
# ============================================================================
"""
Problem: 343
Write a Python program to create a list of tuples with index and element, but exclude the first N elements using `enumerate()`.

# EXPLICATION DE LA SOLUTION :
# This solution initializes an empty result list, then uses a for loop with
# `enumerate()` to iterate through the input list. For each iteration, it checks
# if the index is greater than or equal to n. If the condition is true (meaning
# we've skipped the first n elements), it appends a tuple (index, element) to
# the result list. This creates a filtered list that excludes the first n elements.
def index_and_element_excluding_first_n(lst, n):
    # Function definition
    result = []
    for index, element in enumerate(lst):
        # Iterates through each element
        if index >= n:
            result.append((index, element))
    return result
        # Returns the result

# Example usage
lst = ['apple', 'banana', 'cherry', 'date', 'elderberry']
result = index_and_element_excluding_first_n(lst, 2)
print(result)  # [(2, 'cherry'), (3, 'date'), (4, 'elderberry')]

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires printing each number in a list along with its index squared
# using `enumerate()`. For example, for index 2 and number 5, it should print
# something like "Index squared: 4, Number: 5". Cela démontre using enumerate()
# to display both the original index and a computed value (index squared).
#
# Prérequis Clés :
# - Function must accept a list of numbers as input
# - Function must use `enumerate()` to get index-element pairs
# - Function must print both the squared index and the number
# - Must calculate index squared (index ** 2 or index * index)
#
# Exemple d'Entrée/Sortie :
# - print_index_squared([10, 20, 30]) should print:
#   Index squared: 0, Number: 10
#   Index squared: 1, Number: 20
#   Index squared: 4, Number: 30
#
# Algorithm: Use enumerate() in a for loop, calculate index**2, print both values.
# ============================================================================
"""
Problem: 344
Write a Python program to print each number in a list along with its index squared using `enumerate()`.

# EXPLICATION DE LA SOLUTION :
# This solution uses a for loop with `enumerate()` to iterate through the list
# of numbers. For each iteration, it calculates the square of the index (index ** 2)
# and prints both the squared index and the corresponding number. Cela démontre
# how enumerate() can be used to access the index for computations while also
# accessing the element value.
def print_index_squared(numbers):
    # Function definition
    for index, number in enumerate(numbers):
        # Iterates through each element
        print(f"Index: {index}, Squared: {number ** 2}")

lst = [1, 2, 3, 4, 5]
print_index_squared(lst)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires replacing elements in a list based on whether their index
# is even or odd using `enumerate()`. Even-indexed elements (0, 2, 4, ...) should
# be replaced with 'Even', and odd-indexed elements (1, 3, 5, ...) should be
# replaced with 'Odd'. Cela démontre in-place list modification with enumerate().
#
# Prérequis Clés :
# - Function must accept a list as input
# - Function must use `enumerate()` to get index-element pairs
# - Function must modify the list in-place
# - Even indexes (index % 2 == 0) → replace with 'Even'
# - Odd indexes (index % 2 != 0) → replace with 'Odd'
#
# Exemple d'Entrée/Sortie :
# - replace_based_on_index(['a', 'b', 'c', 'd', 'e']) should return ['Even', 'Odd', 'Even', 'Odd', 'Even']
#
# Algorithm: Use enumerate() in a for loop, check index % 2, replace lst[index] accordingly.
# ============================================================================
"""
Problem: 345
Write a Python program to replace elements in a list based on their index using `enumerate()`. For example, replace even indexed elements with 'Even' and odd indexed elements with 'Odd'.

# EXPLICATION DE LA SOLUTION :
# This solution uses a for loop with `enumerate()` to iterate through the list.
# For each iteration, it checks if the index is even (index % 2 == 0). If even,
# it replaces the element at that index with 'Even'. If odd, it replaces with 'Odd'.
# Since lists are mutable, the modifications are made in-place. The function returns
# the modified list.
def replace_based_on_index(lst):
    # Function definition
    for index, element in enumerate(lst):
        # Iterates through each element
        if index % 2 == 0:
            # Checks condition
            lst[index] = 'Even'
        else:
            lst[index] = 'Odd'
    return lst
        # Returns the result

lst = ['a', 'b', 'c', 'd', 'e']
result = replace_based_on_index(lst)
print(result)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function with a nested function. The outer
# function `sum_of_squares()` should contain an inner function `square()` that
# squares a number. The outer function should use this nested function to calculate
# the sum of squares of two numbers. Cela démontre nested la définition de fonctions
# and function scope en Python.
#
# Prérequis Clés :
# - Function must define a nested function `square()` inside `sum_of_squares()`
# - The nested `square()` function should square a number (x * x)
# - The outer function should return square(a) + square(b)
# - Must demonstrate nested la définition de fonction and usage
#
# Exemple d'Entrée/Sortie :
# - sum_of_squares(3, 4) should return 25 (3² + 4² = 9 + 16)
# - sum_of_squares(5, 12) should return 169 (5² + 12² = 25 + 144)
#
# Algorithm: Define nested square() function, call it twice in outer function, return sum.
# ============================================================================
"""
Problem: 346
Write a Python program that defines a function `sum_of_squares()` which contains a nested function `square()` that squares a number. The `sum_of_squares()` function should sum the squares of two numbers.

# EXPLICATION DE LA SOLUTION :
# This solution defines a nested function `square()` inside the outer function
# `sum_of_squares()`. The nested function takes a number x and returns x * x.
# The outer function then calls this nested function twice - once for each parameter
# (a and b) - and returns the sum of the two squared values. Cela démontre
# how nested functions can encapsulate helper logic within a larger function.
def sum_of_squares(a, b):
    # Function definition
    def square(x):
        # Function definition
        return x * x
            # Returns the result
    return square(a) + square(b)
        # Returns the result

result = sum_of_squares(3, 4)
print(result)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function with a nested function that handles
# user input. The outer function `greet()` should contain an inner function
# `get_name()` that prompts the user for their name. The outer function should
# use this nested function to get the name and return a greeting message. This
# demonstrates nested functions for organizing code and separating concerns.
#
# Prérequis Clés :
# - Function must define a nested function `get_name()` inside `greet()`
# - The nested `get_name()` function should prompt user for input
# - The outer function should call get_name() and return a greeting string
# - Must demonstrate nested function for input handling
#
# Exemple d'Entrée/Sortie :
# - greet() with input "Alice" should return "Hello, Alice!"
# - greet() with input "Bob" should return "Hello, Bob!"
#
# Algorithm: Define nested get_name() that returns input(), call it in outer function, return formatted greeting.
# ============================================================================
"""
Problem: 347
Write a Python program that defines a function `greet()` which contains a nested function `get_name()` to prompt the user for their name. The `greet()` function should return a greeting message using the name.
    # Returns the result

# EXPLICATION DE LA SOLUTION :
# This solution defines a nested function `get_name()` inside the outer function
# `greet()`. The nested function prompts the user for their name using input()
# and returns the entered name. The outer function calls this nested function
# to get the name, then returns a formatted greeting string using an f-string.
# Cela démontre how nested functions can encapsulate input/output operations.
def greet():
    # Function definition
    def get_name():
        # Function definition
        return input("What is your name? ")
            # Gets user input
    name = get_name()
    return f"Hello, {name}!"
        # Returns the result

result = greet()
print(result)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function with a nested recursive function to
# calculate factorial. The outer function `factorial()` should contain an inner
# recursive function `inner_factorial()` that implements the factorial algorithm.
# The outer function should call the nested function to compute the result. This
# demonstrates nested functions with recursion.
#
# Prérequis Clés :
# - Function must define a nested recursive function `inner_factorial()` inside `factorial()`
# - The nested function should implement factorial recursively (n! = n * (n-1)!)
# - Base case: 0! = 1
# - The outer function should call the nested function and return the result
#
# Exemple d'Entrée/Sortie :
# - factorial(5) should return 120 (5! = 5 × 4 × 3 × 2 × 1)
# - factorial(0) should return 1
#
# Algorithm: Define nested recursive function with base case (x == 0 returns 1),
# recursive case (x * inner_factorial(x-1)), call from outer function.
# ============================================================================
"""
Problem: 348
Write a Python program that defines a function `factorial()` which contains a nested recursive function `inner_factorial()` to calculate the factorial of a number.

# EXPLICATION DE LA SOLUTION :
# This solution defines a nested recursive function `inner_factorial()` inside the
# outer function `factorial()`. The nested function implements the factorial algorithm
# recursively: if x is 0, it returns 1 (base case); otherwise, it returns x multiplied
# by the factorial of x-1 (recursive case). The outer function simply calls the nested
# function with the input n and returns the result. Cela démontre recursion within
# a nested function structure.
def factorial(n):
    # Function definition
    def inner_factorial(x):
        # Function definition
        if x == 0:
            # Checks condition
            return 1
                # Returns the result
        else:
            return x * inner_factorial(x - 1)
                # Returns the result
    return inner_factorial(n)
        # Returns the result

result = factorial(5)
print(result)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function that returns a nested function (closure).
# The outer function `add_prefix()` should accept a prefix and return a nested
# function `prefix_string()` that adds that prefix to any string. Cela démontre
# closures - functions that remember variables from their enclosing scope. The
# returned function can then be called with a string to add the prefix.
#
# Prérequis Clés :
# - Function must define a nested function `prefix_string()` inside `add_prefix()`
# - The nested function should accept a string and add the prefix to it
# - The outer function should return the nested function (closure)
# - The returned function should remember the prefix from the outer scope
#
# Exemple d'Entrée/Sortie :
# - add_prefix("Hello ")("World") should return "Hello World"
# - add_prefix("Mr. ")("Smith") should return "Mr. Smith"
#
# Algorithm: Define nested function that uses prefix from outer scope, return nested function.
# ============================================================================
"""
Problem: 349
Write a Python program that defines a function `add_prefix()` which contains a nested function `prefix_string()` that adds a given prefix to a string. The `add_prefix()` function should return the prefixed string.
    # Returns the result

# EXPLICATION DE LA SOLUTION :
# This solution defines a nested function `prefix_string()` inside the outer function
# `add_prefix()`. The nested function takes a string and concatenates it with the
# prefix from the outer function's scope. The outer function returns this nested
# function, creating a closure that "remembers" the prefix value. When the returned
# function is called with a string, it adds the remembered prefix to that string.
# This is a closure pattern en Python.
def add_prefix(prefix):
    # Function definition

    def prefix_string(string):
        # Function definition

        return prefix + string
            # Returns the result


    return prefix_string
        # Returns the result

prefix_func = add_prefix("pre-")
result = prefix_func("fix")
print(result)

def add_prefix(prefix):
    # Function definition

    def prefix_string(string):
        # Function definition
        return prefix + string
            # Returns the result

    return prefix_string
        # Returns the result

prefix_func = add_prefix("pre-")

result1 = prefix_func("fix")
result2 = prefix_func("view")
result3 = prefix_func("dict")

print(result1)  # Sortie : "pre-fix"
print(result2)  # Sortie : "pre-view"
print(result3)  # Sortie : "pre-dict"

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function with a nested function to check if
# a number is even. The outer function `check_even()` should contain an inner
# function `is_even()` that checks if a number is even (divisible by 2). The outer
# function should use this nested function to check the input number. Cela démontre
# nested functions for organizing helper logic.
#
# Prérequis Clés :
# - Function must define a nested function `is_even()` inside `check_even()`
# - The nested function should check if a number is even (x % 2 == 0)
# - The outer function should call the nested function and return the result
# - Must demonstrate nested function for conditional checking
#
# Exemple d'Entrée/Sortie :
# - check_even(10) should return True
# - check_even(7) should return False
#
# Algorithm: Define nested is_even() that returns x % 2 == 0, call it in outer function.
# ============================================================================
"""
Problem: 350
Write a Python program that defines a function `check_even()` which contains a nested function `is_even()` that checks if a number is even. The `check_even()` function should return whether the number is even.
    # Returns the result

# EXPLICATION DE LA SOLUTION :
# This solution defines a nested function `is_even()` inside the outer function
# `check_even()`. The nested function takes a number x and returns True if x % 2 == 0
# (even) or False otherwise. The outer function calls this nested function with the
# input number and returns the result. Cela démontre how nested functions can
# encapsulate helper logic for condition checking.
def check_even(num):
    # Function definition
    def is_even(x):
        # Function definition
        return x % 2 == 0
            # Returns the result
    return is_even(num)
        # Returns the result

result = check_even(10)
print(result)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function with a nested function to calculate
# exponentiation. The outer function `power()` should contain an inner function
# `calculate_power()` that raises a number to a given power. The outer function
# should use this nested function to compute base^exponent. Cela démontre
# nested functions for mathematical operations.
#
# Prérequis Clés :
# - Function must define a nested function `calculate_power()` inside `power()`
# - The nested function should calculate b ** e (base to the power of exponent)
# - The outer function should call the nested function and return the result
# - Must demonstrate nested function for mathematical computation
#
# Exemple d'Entrée/Sortie :
# - power(2, 3) should return 8 (2³)
# - power(5, 2) should return 25 (5²)
#
# Algorithm: Define nested calculate_power() that returns b ** e, call it in outer function.
# ============================================================================
"""
Problem: 351
Write a Python program that defines a function `power()` which contains a nested function `calculate_power()` that raises a number to a given power. The `power()` function should return the result.
    # Returns the result

# EXPLICATION DE LA SOLUTION :
# This solution defines a nested function `calculate_power()` inside the outer
# function `power()`. The nested function takes two parameters (b for base, e for
# exponent) and returns b ** e using Python's exponentiation operator. The outer
# function calls this nested function with the input base and exponent, then returns
# the result. Cela démontre how nested functions can encapsulate mathematical
# operations.
def power(base, exponent):
    # Function definition
    def calculate_power(b, e):
        # Function definition
        return b ** e
            # Returns the result
    return calculate_power(base, exponent)
        # Returns the result

result = power(2, 3)
print(result)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function with a nested function to calculate
# the area of a circle. The outer function `area_circle()` should contain an
# inner function `calculate_area()` that computes the area using the formula
# π × r². The outer function should use this nested function to compute the area
# for the given radius. Cela démontre nested functions for geometric calculations.
#
# Prérequis Clés :
# - Function must define a nested function `calculate_area()` inside `area_circle()`
# - The nested function should calculate area = π × r²
# - The outer function should call the nested function and return the result
# - Must use π (approximately 3.14159) in the calculation
#
# Exemple d'Entrée/Sortie :
# - area_circle(5) should return approximately 78.54 (π × 5²)
# - area_circle(10) should return approximately 314.159 (π × 10²)
#
# Algorithm: Define nested calculate_area() with formula π × r², call it in outer function.
# ============================================================================
"""
Problem: 352
Write a Python program that defines a function `area_circle()` which contains a nested function `calculate_area()` that computes the area of a circle given its radius. The `area_circle()` function should return the area.
    # Returns the result

# EXPLICATION DE LA SOLUTION :
# This solution defines a nested function `calculate_area()` inside the outer
# function `area_circle()`. The nested function takes a radius r and calculates
# the area using the formula 3.14159 * r * r (π × r²). The outer function calls
# this nested function with the input radius and returns the result. Cela démontre
# how nested functions can encapsulate geometric calculations. Remarque : Using math.pi
# would be more accurate than the hardcoded value.
def area_circle(radius):
    # Function definition
    def calculate_area(r):
        # Function definition
        return 3.14159 * r * r
            # Returns the result
    return calculate_area(radius)
        # Returns the result

result = area_circle(5)
print(result)

def main():
    # Function definition
    def inner(radius):
        # Function definition
        return  3.14159 * radius * radius
            # Returns the result
    return inner(n)
        # Returns the result
n = 6
main()

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function with a nested function to capitalize
# words in a sentence. The outer function `capitalize_words()` should contain an
# inner function `capitalize()` that capitalizes a single word. The outer function
# should split the sentence into words, apply the nested function to each word,
# and join them back. Cela démontre nested functions for string processing.
#
# Prérequis Clés :
# - Function must define a nested function `capitalize()` inside `capitalize_words()`
# - The nested function should capitalize a word (first letter uppercase)
# - The outer function should split sentence, apply capitalize to each word, join back
# - Must use .split() and .join() for string manipulation
#
# Exemple d'Entrée/Sortie :
# - capitalize_words("hello world from python") should return "Hello World From Python"
# - capitalize_words("python programming") should return "Python Programming"
#
# Algorithm: Define nested capitalize() using .capitalize(), split sentence, map capitalize, join.
# ============================================================================
"""
Problem: 353
Write a Python program that defines a function `capitalize_words()` which contains a nested function `capitalize()` that capitalizes a word. The `capitalize_words()` function should return a string with each word capitalized.
    # Returns the result

# EXPLICATION DE LA SOLUTION :
# This solution defines a nested function `capitalize()` inside the outer function
# `capitalize_words()`. The nested function takes a word and returns its capitalized
# version using the .capitalize() method. The outer function splits the input sentence
# into words, iterates through each word, applies the nested capitalize function, and
# collects the results. Finally, it joins the capitalized words back into a single
# string with spaces. Cela démontre nested functions for text processing.
def capitalize_words(sentence):
    # Function definition
    def capitalize(word):
        # Function definition
        return word.capitalize()
            # Returns the result
    words = sentence.split()
        # Splits string into list of words/elements
    capitalized_words = []
    for word in words:
        # Iterates through each element
        capitalized_words.append(capitalize(word))
    return ' '.join(capitalized_words)
        # Joins list elements into string

result = capitalize_words("hello world from python")
print(result)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function with a nested function to check if
# a string is a palindrome. The outer function `is_palindrome()` should contain
# an inner function `reverse_string()` that reverses a string. The outer function
# should use this nested function to reverse the word and compare it with the
# original to determine if it's a palindrome. Cela démontre nested functions
# for string manipulation and comparison.
#
# Prérequis Clés :
# - Function must define a nested function `reverse_string()` inside `is_palindrome()`
# - The nested function should reverse a string (e.g., using slicing [::-1])
# - The outer function should compare word with its reverse
# - Must return True if palindrome, False otherwise
#
# Exemple d'Entrée/Sortie :
# - is_palindrome("radar") should return True
# - is_palindrome("hello") should return False
#
# Algorithm: Define nested reverse_string() using [::-1], compare word with reverse_string(word).
# ============================================================================
"""
Problem: 354
Write a Python program that defines a function `is_palindrome()` which contains a nested function `reverse_string()` that checks if a string is a palindrome.

# EXPLICATION DE LA SOLUTION :
# This solution defines a nested function `reverse_string()` inside the outer
# function `is_palindrome()`. The nested function takes a string s and returns
# its reverse using string slicing [::-1]. The outer function calls this nested
# function to reverse the input word, then compares the original word with its
# reverse. If they are equal, it returns True (palindrome); otherwise, it returns
# False. Cela démontre nested functions for string operations and comparisons.
def is_palindrome(word):
    # Function definition
    def reverse_string(s):
        # Function definition
        return s[::-1]
            # Returns the result
    return word == reverse_string(word)
        # Returns the result

result = is_palindrome("radar")
print(result)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function with a nested function to concatenate
# two strings. The outer function `concatenate_strings()` should contain an inner
# function `join_strings()` that concatenates two strings. The outer function
# should use this nested function to join the input strings. Cela démontre
# nested functions for string operations.
#
# Prérequis Clés :
# - Function must define a nested function `join_strings()` inside `concatenate_strings()`
# - The nested function should concatenate two strings (s1 + s2)
# - The outer function should call the nested function and return the result
# - Must demonstrate nested function for string concatenation
#
# Exemple d'Entrée/Sortie :
# - concatenate_strings("Hello, ", "world!") should return "Hello, world!"
# - concatenate_strings("Python", "Programming") should return "PythonProgramming"
#
# Algorithm: Define nested join_strings() that returns s1 + s2, call it in outer function.
# ============================================================================
"""
Problem: 355
Write a Python program that defines a function `concatenate_strings()` which contains a nested function `join_strings()` that concatenates two strings.

# EXPLICATION DE LA SOLUTION :
# This solution defines a nested function `join_strings()` inside the outer
# function `concatenate_strings()`. The nested function takes two strings s1 and
# s2 and returns their concatenation using the + operator. The outer function
# calls this nested function with the input strings and returns the result. This
# demonstrates how nested functions can encapsulate string operations.
def concatenate_strings(str1, str2):
    # Function definition
    def join_strings(s1, s2):
        # Function definition
        return s1 + s2
            # Returns the result
    return join_strings(str1, str2)
        # Returns the result

result = concatenate_strings("Hello, ", "world!")
print(result)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function with a nested recursive function to
# generate the Fibonacci sequence. The outer function `fibonacci()` should contain
# an inner recursive function `fib()` that calculates Fibonacci numbers. The outer
# function should use this nested function to generate a list of the first n
# Fibonacci numbers. Cela démontre nested functions with recursion.
#
# Prérequis Clés :
# - Function must define a nested recursive function `fib()` inside `fibonacci()`
# - The nested function should implement Fibonacci recursively (fib(n) = fib(n-1) + fib(n-2))
# - Base cases: fib(0) = 0, fib(1) = 1
# - The outer function should return a list of first n Fibonacci numbers
#
# Exemple d'Entrée/Sortie :
# - fibonacci(10) should return [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# - fibonacci(5) should return [0, 1, 1, 2, 3]
#
# Algorithm: Define nested recursive fib() with base cases, use list comprehension to generate sequence.
# ============================================================================
"""
Problem: 356
Write a Python program that defines a function `fibonacci()` which contains a nested recursive function `fib()` to generate the Fibonacci sequence up to a given number of terms.

# EXPLICATION DE LA SOLUTION :
# This solution defines a nested recursive function `fib()` inside the outer
# function `fibonacci()`. The nested function implements the Fibonacci algorithm
# recursively: if x <= 1, it returns x (base cases); otherwise, it returns
# fib(x-1) + fib(x-2) (recursive case). The outer function uses a list comprehension
# to generate the first n Fibonacci numbers by calling fib(i) for i in range(n).
# Cela démontre recursion within a nested function structure.
def fibonacci(n):
    # Function definition
    def fib(x):
        # Function definition
        if x <= 1:
            return x
                # Returns the result
        else:
            return fib(x - 1) + fib(x - 2)
                # Returns the result
    return [fib(i) for i in range(n)]
        # Returns the result

result = fibonacci(10)
print(result)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function with a nested function to convert
# a string to uppercase. The outer function `to_uppercase()` should contain an
# inner function `convert()` that converts a string to uppercase. The outer
# function should use this nested function to transform the input string. This
# demonstrates nested functions for string transformations.
#
# Prérequis Clés :
# - Function must define a nested function `convert()` inside `to_uppercase()`
# - The nested function should convert a string to uppercase using .upper()
# - The outer function should call the nested function and return the result
# - Must demonstrate nested function for string case conversion
#
# Exemple d'Entrée/Sortie :
# - to_uppercase("hello world") should return "HELLO WORLD"
# - to_uppercase("Python") should return "PYTHON"
#
# Algorithm: Define nested convert() that returns s.upper(), call it in outer function.
# ============================================================================
"""
Problem: 357
Write a Python program that defines a function `to_uppercase()` which contains a nested function `convert()` that converts a string to uppercase.

# EXPLICATION DE LA SOLUTION :
# This solution defines a nested function `convert()` inside the outer function
# `to_uppercase()`. The nested function takes a string s and returns its uppercase
# version using the .upper() method. The outer function calls this nested function
# with the input string and returns the result. Cela démontre how nested
# functions can encapsulate string transformation operations.
def to_uppercase(string):
    # Function definition
    def convert(s):
        # Function definition
        return s.upper()
            # Converts to lowercase/uppercase
    return convert(string)
        # Returns the result

result = to_uppercase("hello world")
print(result)

"""
Problem: 358
Write a Python program that defines a function `find_largest()` which contains a nested function `compare()` that compares two numbers and returns the larger one.

def find_largest(a, b):
    # Function definition
    def compare(x, y):
        # Function definition
        if x > y:
            return x
                # Returns the result
        else:
            return y
                # Returns the result
    return compare(a, b)
        # Returns the result

result = find_largest(10, 20)
print(result)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function with multiple nested functions to
# implement a calculator. The outer function `calculator()` should contain
# nested functions for basic arithmetic operations: `add()`, `subtract()`,
# `multiply()`, and `divide()`. The outer function should use these nested
# functions based on the operation parameter. Cela démontre multiple nested
# functions and conditional logic.
#
# Prérequis Clés :
# - Function must define nested functions: add(), subtract(), multiply(), divide()
# - Each nested function should perform its respective arithmetic operation
# - The outer function should select and call the appropriate nested function
# - Must handle division by zero (return error message)
# - Must handle invalid operations
#
# Exemple d'Entrée/Sortie :
# - calculator('add', 5, 3) should return 8
# - calculator('multiply', 4, 7) should return 28
# - calculator('divide', 10, 0) should return "Cannot divide by zero"
#
# Algorithm: Define nested functions for each operation, use if/elif to select operation.
# ============================================================================
"""
Problem: 359
Write a Python program that defines a function `calculator()` which contains nested functions for `add()`, `subtract()`, `multiply()`, and `divide()`. The `calculator()` function should perform the selected operation.

# EXPLICATION DE LA SOLUTION :
# This solution defines four nested functions inside the outer function `calculator()`:
# `add()`, `subtract()`, `multiply()`, and `divide()`. Each nested function performs
# its respective arithmetic operation. The `divide()` function includes error handling
# for division by zero. The outer function uses if/elif statements to select and call
# the appropriate nested function based on the operation parameter. Cela démontre
# how multiple nested functions can organize related operations within a single function.
def calculator(operation, a, b):
    # Function definition
    def add(x, y):
        # Function definition
        return x + y
            # Returns the result

    def subtract(x, y):
        # Function definition
        return x - y
            # Returns the result

    def multiply(x, y):
        # Function definition
        return x * y
            # Returns the result

    def divide(x, y):
        # Function definition
        if y != 0:
            return x / y
                # Returns the result
        else:
            return "Cannot divide by zero"
                # Returns the result

    if operation == 'add':
        # Checks condition
        return add(a, b)
            # Returns the result
    elif operation == 'subtract':
        return subtract(a, b)
            # Returns the result
    elif operation == 'multiply':
        return multiply(a, b)
            # Returns the result
    elif operation == 'divide':
        return divide(a, b)
            # Returns the result
    else:
        return "Invalid operation"
            # Returns the result

result = calculator('add', 5, 3)
print(result)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function with a nested function to check if
# a number is prime. The outer function `is_prime()` should contain an inner
# function `check_divisibility()` that checks if a number is prime by testing
# for divisors. The outer function should use this nested function to determine
# primality. Cela démontre nested functions for mathematical validation.
#
# Prérequis Clés :
# - Function must define a nested function `check_divisibility()` inside `is_prime()`
# - The nested function should check for divisors from 2 to sqrt(n)
# - Numbers < 2 are not prime
# - The outer function should handle edge cases and call the nested function
#
# Exemple d'Entrée/Sortie :
# - is_prime(7) should return True
# - is_prime(10) should return False
# - is_prime(1) should return False
#
# Algorithm: Check if n < 2, define nested function that checks divisors up to sqrt(n).
# ============================================================================
"""
Problem: 360
Write a Python program that defines a function `is_prime()` which contains a nested function `check_divisibility()` to check if a number is prime.

# EXPLICATION DE LA SOLUTION :
# This solution first checks if the number is less than 2 (not prime). Then it
# defines a nested function `check_divisibility()` that tests for divisors from
# 2 up to the square root of the number. If any divisor is found, it returns
# False; otherwise, it returns True. The outer function calls this nested
# function with the input number and returns the result. Cela démontre
# nested functions for complex mathematical checks.
def is_prime(n):
    # Function definition
    def check_divisibility(x):
        # Function definition
        if x < 2:
            return False
                # Returns the result
        for i in range(2, int(x ** 0.5) + 1):
            # Iterates through each element
            if x % i == 0:
                # Checks condition
                return False
                    # Returns the result
        return True
            # Returns the result
    return check_divisibility(n)
        # Returns the result

result = is_prime(7)
print(result)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function with a nested function to count vowels
# in a string. The outer function `count_vowels()` should contain an inner function
# `is_vowel()` that checks if a character is a vowel. The outer function should
# iterate through the string and use the nested function to count vowels. This
# demonstrates nested functions for character classification.
#
# Prérequis Clés :
# - Function must define a nested function `is_vowel()` inside `count_vowels()`
# - The nested function should check if a character is a vowel (a, e, i, o, u)
# - The outer function should iterate through string and count vowels
# - Must handle both uppercase and lowercase vowels
#
# Exemple d'Entrée/Sortie :
# - count_vowels("Hello World") should return 3 (e, o, o)
# - count_vowels("Python") should return 1 (o)
#
# Algorithm: Define nested is_vowel() that checks char in 'aeiouAEIOU', iterate and count.
# ============================================================================
"""
Problem: 361
Write a Python program that defines a function `count_vowels()` which contains a nested function `is_vowel()` to count the number of vowels in a string.

# EXPLICATION DE LA SOLUTION :
# This solution defines a nested function `is_vowel()` inside the outer function
# `count_vowels()`. The nested function takes a character and returns True if it's
# in the string 'aeiouAEIOU' (a vowel). The outer function initializes a count
# to 0, then iterates through each character in the string. For each character,
# it calls the nested function, and if it returns True, it increments the count.
# Cela démontre how nested functions can encapsulate character classification logic.
def count_vowels(string):
    # Function definition
    def is_vowel(char):
        # Function definition
        return char in 'aeiouAEIOU'
            # Returns the result

    count = 0
    for char in string:
        # Iterates through each element
        if is_vowel(char):
            count += 1
    return count
        # Returns the result

result = count_vowels("Hello World")
print(result)

"""
Problem: 362
Write a Python program that defines a function `calculate_average()` which contains a nested function `sum_numbers()` to calculate the average of a list of numbers.

def calculate_average(numbers):
    # Function definition
    def sum_numbers(nums):
        # Function definition
        total = 0
        for num in nums:
            # Iterates through each element
            total += num
        return total
            # Returns the result

    return sum_numbers(numbers) / len(numbers)
        # Returns the result

result = calculate_average([1, 2, 3, 4, 5])
print(result)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function with a nested function to reverse
# a string. The outer function `reverse_string()` should contain an inner
# function `reverse()` that reverses a string. The function can either return
# the nested function (closure) or call it directly. Cela démontre nested
# functions for string manipulation, including closure patterns.
#
# Prérequis Clés :
# - Function must define a nested function `reverse()` inside `reverse_string()`
# - The nested function should reverse a string (e.g., using slicing [::-1])
# - The outer function should either return the nested function or call it
# - Must demonstrate nested function for string reversal
#
# Exemple d'Entrée/Sortie :
# - reverse_string("Hello") should return "olleH" (if calling directly)
# - Or return a function that can reverse strings (closure pattern)
#
# Algorithm: Define nested reverse() using [::-1] or manual reversal, return or call it.
# ============================================================================
"""
Problem: 363
Write a Python program that defines a function `reverse_string()` which contains a nested function `reverse()` that reverses a given string.

# EXPLICATION DE LA SOLUTION (First version - closure pattern):
# This first solution returns the nested function itself, creating a closure.
# The nested function `reverse()` uses string slicing [::-1] to reverse a string.
# When the outer function is called, it returns the nested function, which can
# then be called with a string argument to reverse it. Cela démontre the
# closure pattern where a function returns another function.
def reverse_string():
    # Function definition
    def reverse(s):
        # Function definition
        return s[::-1]
            # Returns the result
    return reverse
        # Returns the result

# Example usage
reverse_func = reverse_string()
print(reverse_func("Hello, World!"))

def reverse_string(string):
    # Function definition
    def reverse(s):
        # Function definition
        reversed_str = ''
        for char in s:
            # Iterates through each element
            reversed_str = char + reversed_str
        return reversed_str
            # Returns the result
    return reverse(string)
        # Returns the result

result = reverse_string("Hello")
print(result)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function with a nested function to check if
# a list is sorted in ascending order. The outer function `is_sorted()` should
# contain an inner function `compare_elements()` that checks if adjacent elements
# are in the correct order. The outer function should use this nested function
# to verify the list is sorted. Cela démontre nested functions for validation.
#
# Prérequis Clés :
# - Function must define a nested function `compare_elements()` inside `is_sorted()`
# - The nested function should check if list is sorted (each element <= next)
# - The outer function should call the nested function and return the result
# - Must return True if sorted, False otherwise
#
# Exemple d'Entrée/Sortie :
# - is_sorted([1, 2, 3, 4, 5]) should return True
# - is_sorted([5, 2, 3, 1]) should return False
#
# Algorithm: Define nested function that checks lst[i] <= lst[i+1] for all i, return result.
# ============================================================================
"""
Problem: 364
Write a Python program that defines a function `is_sorted()` which contains a nested function `compare_elements()` to check if a list is sorted in ascending order.
    # Sorts elements in ascending order

# EXPLICATION DE LA SOLUTION :
# This solution defines a nested function `compare_elements()` inside the outer
# function `is_sorted()`. The nested function iterates through the list and
# checks if each element is less than or equal to the next element. If any
# element is greater than the next, it returns False immediately. If all elements
# are in order, it returns True. The outer function calls this nested function
# and returns the result. Cela démontre nested functions for list validation.
def is_sorted(lst):
    # Function definition
    def compare_elements():
        # Function definition
        for i in range(len(lst) - 1):
            # Iterates through each element
            if lst[i] > lst[i + 1]:
                return False
                    # Returns the result
        return True
            # Returns the result
    return compare_elements()
        # Returns the result

result = is_sorted([1, 2, 3, 4, 5])
    # Sorts elements in ascending order
print(result)

def is_sorted():
    # Function definition
    return compare_elements(lst)
        # Returns the result

def compare_elements(lst):
    # Function definition
    if lst == sorted(lst):
        # Sorts elements in ascending order
        return True
            # Returns the result
    return False
        # Returns the result

lst = [1,2,3,4,5]
is_sorted()
    # Sorts elements in ascending order

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function with a nested function to generate
# a list of squares. The outer function `generate_squares()` should contain an
# inner function `square()` that squares a number. The outer function should use
# this nested function to generate squares of numbers from 1 to n. Cela démontre
# nested functions for list generation.
#
# Prérequis Clés :
# - Function must define a nested function `square()` inside `generate_squares()`
# - The nested function should square a number (x * x)
# - The outer function should generate squares from 1 to n
# - Must return a list of squared values
#
# Exemple d'Entrée/Sortie :
# - generate_squares(5) should return [1, 4, 9, 16, 25]
# - generate_squares(3) should return [1, 4, 9]
#
# Algorithm: Define nested square() that returns x*x, iterate 1 to n, call square(), append to list.
# ============================================================================
"""
Problem: 365
Write a Python program that defines a function `generate_squares()` which contains a nested function `square()` to generate a list of squares of numbers from 1 to n.

# EXPLICATION DE LA SOLUTION :
# This solution defines a nested function `square()` inside the outer function
# `generate_squares()`. The nested function takes a number x and returns x * x.
# The outer function initializes an empty list, then iterates from 1 to n (inclusive).
# For each number, it calls the nested square function and appends the result to
# the list. Cela démontre how nested functions can be used in list generation
# and transformation operations.
def generate_squares(n):
    # Function definition
    def square(x):
        # Function definition
        return x * x
            # Returns the result
    squares = []
    for i in range(1, n + 1):
        # Iterates through each element
        squares.append(square(i))
    return squares
        # Returns the result

result = generate_squares(5)
print(result)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function with a nested helper function to
# add two numbers. The outer function `sum_of_two()` should contain an inner
# helper function `add()` that adds two numbers. The outer function should call
# this nested helper function and return the result. Cela démontre nested
# functions as helper functions for simple operations.
#
# Prérequis Clés :
# - Function must define a nested helper function `add()` inside `sum_of_two()`
# - The nested function should add two numbers (x + y)
# - The outer function should call the nested function and return the result
# - Must demonstrate nested function as helper
#
# Exemple d'Entrée/Sortie :
# - sum_of_two(3, 5) should return 8
# - sum_of_two(10, 20) should return 30
#
# Algorithm: Define nested add() that returns x + y, call it in outer function.
# ============================================================================
"""
Problem: 366
Write a Python program that defines a main function `sum_of_two()` and a helper function `add(a, b)` that adds two numbers together. The `sum_of_two()` function should call the helper function and return the result.
    # Returns the result

# EXPLICATION DE LA SOLUTION :
# This solution defines a nested helper function `add()` inside the outer function
# `sum_of_two()`. The nested function takes two numbers x and y and returns their
# sum. The outer function calls this nested helper function with the input numbers
# and returns the result. Cela démontre how nested functions can serve as
# helper functions to organize and encapsulate simple operations.
def sum_of_two(a, b):
    # Function definition
    def add(x, y):
        # Function definition
        return x + y
            # Returns the result
    return add(a, b)
        # Returns the result

result = sum_of_two(3, 5)
print(result)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function with a nested function to check if
# a number is even or odd. The outer function `even_or_odd()` should contain an
# inner function `is_even()` that checks if a number is even. The outer function
# should use this nested function to determine and print whether the number is
# even or odd. Cela démontre nested functions for conditional logic and output.
#
# Prérequis Clés :
# - Function must define a nested function `is_even()` inside `even_or_odd()`
# - The nested function should check if a number is even (x % 2 == 0)
# - The outer function should use the nested function and print the result
# - Must print "is even" or "is odd" based on the check
#
# Exemple d'Entrée/Sortie :
# - even_or_odd(10) should print "10 is even"
# - even_or_odd(7) should print "7 is odd"
#
# Algorithm: Define nested is_even() that returns x % 2 == 0, use it to print result.
# ============================================================================
"""
Problem: 367
Write a Python program that defines a main function `even_or_odd()` and a nested function `is_even(n)` that checks if a number is even. The `even_or_odd()` function should use the helper function to print whether the number is even or odd.

# EXPLICATION DE LA SOLUTION :
# This solution defines a nested function `is_even()` inside the outer function
# `even_or_odd()`. The nested function takes a number x and returns True if x % 2 == 0
# (even) or False otherwise. The outer function calls this nested function with the
# input number. If it returns True, it prints that the number is even; otherwise,
# it prints that the number is odd. Cela démontre nested functions for
# conditional logic and formatted output.
def even_or_odd(n):
    # Function definition
    def is_even(x):
        # Function definition
        return x % 2 == 0
            # Returns the result
    if is_even(n):
        print(f"{n} is even")
    else:
        print(f"{n} is odd")

even_or_odd(10)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function with a nested helper function to
# convert temperature from Celsius to Fahrenheit. The outer function `convert_temperature()`
# should contain an inner helper function `celsius_to_fahrenheit()` that performs
# the conversion using the formula: F = (C × 9/5) + 32. The outer function should
# call this nested helper function and return the result. Cela démontre nested
# functions for unit conversion.
#
# Prérequis Clés :
# - Function must define a nested helper function `celsius_to_fahrenheit()` inside `convert_temperature()`
# - The nested function should convert Celsius to Fahrenheit: (c * 9/5) + 32
# - The outer function should call the nested function and return the result
# - Must demonstrate nested function for temperature conversion
#
# Exemple d'Entrée/Sortie :
# - convert_temperature(25) should return 77.0 (25°C = 77°F)
# - convert_temperature(0) should return 32.0 (0°C = 32°F)
#
# Algorithm: Define nested celsius_to_fahrenheit() with conversion formula, call it in outer function.
# ============================================================================
"""
Problem: 368
Write a Python program that defines a main function `convert_temperature()` and a helper function `celsius_to_fahrenheit(c)` that converts a temperature from Celsius to Fahrenheit. The `convert_temperature()` function should use the helper function to return the converted temperature.
    # Returns the result

# EXPLICATION DE LA SOLUTION :
# This solution defines a nested helper function `celsius_to_fahrenheit()` inside
# the outer function `convert_temperature()`. The nested function takes a Celsius
# temperature c and converts it to Fahrenheit using the formula (c * 9/5) + 32.
# The outer function calls this nested helper function with the input Celsius
# temperature and returns the result. Cela démontre how nested functions can
# encapsulate conversion logic.
def convert_temperature(celsius):
    # Function definition
    def celsius_to_fahrenheit(c):
        # Function definition
        return (c * 9/5) + 32
            # Returns the result
    return celsius_to_fahrenheit(celsius)
        # Returns the result

result = convert_temperature(25)
print(result)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function with a nested helper function to
# calculate the area of a rectangle. The outer function `rectangle_area()` should
# contain an inner helper function `calculate_area()` that calculates area using
# the formula: area = length × width. The outer function should call this nested
# helper function and return the result. Cela démontre nested functions for
# geometric calculations.
#
# Prérequis Clés :
# - Function must define a nested helper function `calculate_area()` inside `rectangle_area()`
# - The nested function should calculate area = length × width
# - The outer function should call the nested function and return the result
# - Must demonstrate nested function for area calculation
#
# Exemple d'Entrée/Sortie :
# - rectangle_area(5, 4) should return 20
# - rectangle_area(10, 3) should return 30
#
# Algorithm: Define nested calculate_area() that returns l * w, call it in outer function.
# ============================================================================
"""
Problem: 369
Write a Python program that defines a main function `rectangle_area()` and a helper function `calculate_area(length, width)` that calculates the area of a rectangle. The `rectangle_area()` function should use the helper function to return the area.
    # Returns the result

# EXPLICATION DE LA SOLUTION :
# This solution defines a nested helper function `calculate_area()` inside the
# outer function `rectangle_area()`. The nested function takes length l and width
# w and returns their product (l * w), which is the area of a rectangle. The outer
# function calls this nested helper function with the input length and width, then
# returns the result. Cela démontre how nested functions can encapsulate
# geometric calculation logic.
def rectangle_area(length, width):
    # Function definition
    def calculate_area(l, w):
        # Function definition
        return l * w
            # Returns the result
    return calculate_area(length, width)
        # Returns the result

result = rectangle_area(5, 10)
print(result)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function with a nested helper function to
# check if a number is prime. The outer function `check_prime()` should contain
# an inner helper function `is_prime()` that checks for primality by testing
# divisors. The outer function should call this nested helper function and return
# the result. Cela démontre nested functions for mathematical validation.
#
# Prérequis Clés :
# - Function must define a nested helper function `is_prime()` inside `check_prime()`
# - The nested function should check for divisors from 2 to sqrt(n)
# - Numbers < 2 are not prime
# - The outer function should call the nested function and return the result
#
# Exemple d'Entrée/Sortie :
# - check_prime(11) should return True
# - check_prime(10) should return False
#
# Algorithm: Define nested is_prime() that checks divisors, call it in outer function.
# ============================================================================
"""
Problem: 370
Write a Python program that defines a main function `check_prime()` and a helper function `is_prime(n)` that checks if a number is prime. The `check_prime()` function should use the helper function to return whether the number is prime.
    # Returns the result

# EXPLICATION DE LA SOLUTION :
# This solution defines a nested helper function `is_prime()` inside the outer
# function `check_prime()`. The nested function first checks if the number is less
# than 2 (not prime), then tests for divisors from 2 up to the square root of the
# number. If any divisor is found, it returns False; otherwise, it returns True.
# The outer function calls this nested helper function with the input number and
# returns the result. Cela démontre nested functions for prime number validation.
def check_prime(n):
    # Function definition
    def is_prime(num):
        # Function definition
        if num < 2:
            return False
                # Returns the result
        for i in range(2, int(num ** 0.5) + 1):
            # Iterates through each element
            if num % i == 0:
                # Checks condition
                return False
                    # Returns the result
        return True
            # Returns the result
    return is_prime(n)
        # Returns the result

result = check_prime(11)
print(result)

"""
Problem: 371
Write a Python program that defines a main function `find_minimum()` and a helper function `min_of_three(a, b, c)` that returns the minimum of three numbers. The `find_minimum()` function should use the helper function to return the minimum value.
    # Returns the result

def find_minimum(a, b, c):
    # Function definition
    def min_of_three(x, y, z):
        # Function definition
        return min(x, y, z)
            # Returns the result
    return min_of_three(a, b, c)
        # Returns the result

result = find_minimum(5, 3, 8)
print(result)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function with a helper function to greet a user.
# The outer function `greet_user()` should call a helper function `get_name()` that
# prompts the user for their name. The outer function should then use this name to
# print a greeting message. Remarque : The helper function is defined outside in this
# solution, but it could be nested. Cela démontre function composition for
# user interaction.
#
# Prérequis Clés :
# - Function must define or use a helper function `get_name()`
# - The helper function should prompt user for input
# - The outer function should use the helper function and print a greeting
# - Must demonstrate function composition for user interaction
#
# Exemple d'Entrée/Sortie :
# - greet_user() with input "Alice" should print "Hello, Alice! Welcome!"
#
# Algorithm: Define get_name() that returns input(), call it in greet_user(), print greeting.
# ============================================================================
"""
372
Write a Python program that defines a main function `greet_user()` and a helper function `get_name()` that prompts the user for their name. The `greet_user()` function should use the helper function to print a greeting message.

# EXPLICATION DE LA SOLUTION :
# This solution defines a helper function `get_name()` that prompts the user for
# their name using input() and returns it. The outer function `greet_user()` calls
# this helper function to get the name, then prints a formatted greeting message.
# Remarque : In this implementation, the helper function is defined outside the main
# function, but it could be nested inside for better encapsulation. Cela démontre
# function composition for user interaction and output formatting.
def greet_user():
    # Function definition
    name = get_name()
    print(f"Hello, {name}! Welcome!")


def get_name():
    # Function definition
    name = input("Type your name: ")
        # Gets user input
    return name
        # Returns the result

greet_user()

"""
Problem: 373
Write a Python program that defines a main function `calculate_factorial()` and a helper function `factorial(n)` that calculates the factorial of a number. The `calculate_factorial()` function should use the helper function to return the factorial.
    # Returns the result

def calculate_factorial(n):
    # Function definition
    def factorial(num):
        # Function definition
        if num == 0 or num == 1:
            # Checks condition
            return 1
                # Returns the result
        result = 1
        for i in range(2, num + 1):
            # Iterates through each element
            result *= i
        return result
            # Returns the result
    return factorial(n)
        # Returns the result

result = calculate_factorial(5)
print(result)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function with a nested helper function to
# capitalize words in a sentence. The outer function `capitalize_words()` should
# contain an inner helper function `capitalize()` that capitalizes the first
# letter of a word. The outer function should split the sentence, apply the
# helper function to each word, and join them back. Cela démontre nested
# functions for string processing.
#
# Prérequis Clés :
# - Function must define a nested helper function `capitalize()` inside `capitalize_words()`
# - The nested function should capitalize first letter (word[0].upper() + word[1:])
# - The outer function should split sentence, apply capitalize to each word, join back
# - Must use .split() and .join() for string manipulation
#
# Exemple d'Entrée/Sortie :
# - capitalize_words("hello world from python") should return "Hello World From Python"
#
# Algorithm: Define nested capitalize() using word[0].upper() + word[1:], split, map, join.
# ============================================================================
"""
Problem: 374
Write a Python program that defines a main function `capitalize_words()` and a helper function `capitalize(word)` that capitalizes the first letter of a word. The `capitalize_words()` function should use the helper function to capitalize each word in a sentence.

# EXPLICATION DE LA SOLUTION :
# This solution defines a nested helper function `capitalize()` inside the outer
# function `capitalize_words()`. The nested function takes a word and capitalizes
# its first letter by using word[0].upper() for the first character and word[1:]
# for the rest. The outer function splits the sentence into words, applies the
# nested capitalize function to each word, collects the results, and joins them
# back into a single string. Cela démontre nested functions for text processing.
def capitalize_words(sentence):
    # Function definition
    def capitalize(word):
        # Function definition
        return word[0].upper() + word[1:]
            # Converts to lowercase/uppercase

    words = sentence.split()
        # Splits string into list of words/elements
    capitalized_words = []
    for word in words:
        # Iterates through each element
        capitalized_words.append(capitalize(word))
    return ' '.join(capitalized_words)
        # Joins list elements into string

result = capitalize_words("hello world from python")
print(result)

"""
Problem: 375
Write a Python program that defines a main function `find_largest()` and a helper function `max_in_list(lst)` that returns the largest number in a list. The `find_largest()` function should use the helper function to find and return the largest number.
    # Returns the result

def max_in_list(lst):
    # Function definition
    return max(lst)
        # Returns the result

def find_largest():
    # Function definition
    largest = max_in_list(lst)
    return largest
        # Returns the result

lst = [12, 45, 7, 23, 67756, 89, 34]
print(find_largest())

def max_in_list(lst):
    # Function definition
    if not lst:
        return None
            # Returns the result
    return max(lst)
        # Returns the result

def find_largest():
    # Function definition
    numbers = [12, 45, 7, 23, 56, 89, 34]
    largest = max_in_list(numbers)
    return largest
        # Returns the result

print(find_largest())

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function with a nested helper function to
# reverse a string. The outer function `reverse_string()` should contain an
# inner helper function `reverse()` that reverses a string. The outer function
# should call this nested helper function and return the result. Cela démontre
# nested functions for string manipulation.
#
# Prérequis Clés :
# - Function must define a nested helper function `reverse()` inside `reverse_string()`
# - The nested function should reverse a string (manually or using slicing)
# - The outer function should call the nested function and return the result
# - Must demonstrate nested function for string reversal
#
# Exemple d'Entrée/Sortie :
# - reverse_string("hello") should return "olleh"
# - reverse_string("Python") should return "nohtyP"
#
# Algorithm: Define nested reverse() that manually reverses string, call it in outer function.
# ============================================================================
"""
Problem: 376
Write a Python program that defines a main function `reverse_string()` and a helper function `reverse(s)` that reverses a given string. The `reverse_string()` function should use the helper function to return the reversed string.
    # Returns the result

# EXPLICATION DE LA SOLUTION :
# This solution defines a nested helper function `reverse()` inside the outer
# function `reverse_string()`. The nested function manually reverses a string
# by iterating through each character and prepending it to a result string.
# The outer function calls this nested helper function with the input string
# and returns the result. Cela démontre nested functions for string
# manipulation with manual implementation.
def reverse_string(s):
    # Function definition
    def reverse(s):
        # Function definition
        reversed_str = ''
        for char in s:
            # Iterates through each element
            reversed_str = char + reversed_str
        return reversed_str
            # Returns the result
    return reverse(s)
        # Returns the result

result = reverse_string("hello")
print(result)

"""
Problem: 377
Write a Python program that defines a main function `calculate_average()` and a helper function `average(lst)` that calculates the average of a list of numbers. The `calculate_average()` function should use the helper function to return the average.
    # Returns the result

def calculate_average(lst):
    # Function definition
    def average(lst):
        # Function definition
        total = 0
        for num in lst:
            # Iterates through each element
            total += num
        return total / len(lst)
            # Returns the result

    return average(lst)
        # Returns the result

result = calculate_average([10, 20, 30, 40])
print(result)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function with a nested helper function to
# check if a string is a palindrome. The outer function `check_palindrome()`
# should contain an inner helper function `is_palindrome()` that checks if a
# string reads the same forwards and backwards. The outer function should call
# this nested helper function and return the result. Cela démontre nested
# functions for string validation.
#
# Prérequis Clés :
# - Function must define a nested helper function `is_palindrome()` inside `check_palindrome()`
# - The nested function should check if string equals its reverse
# - The outer function should call the nested function and return the result
# - Must return True if palindrome, False otherwise
#
# Exemple d'Entrée/Sortie :
# - check_palindrome("racecar") should return True
# - check_palindrome("hello") should return False
#
# Algorithm: Define nested is_palindrome() that checks s == s[::-1], call it in outer function.
# ============================================================================
"""
Problem: 378
Write a Python program that defines a main function `check_palindrome()` and a helper function `is_palindrome(s)` that checks if a string is a palindrome. The `check_palindrome()` function should use the helper function to return whether the string is a palindrome.
    # Returns the result

# EXPLICATION DE LA SOLUTION :
# This solution defines a nested helper function `is_palindrome()` inside the
# outer function `check_palindrome()`. The nested function checks if a string
# is equal to its reverse by comparing s with s[::-1] (string slicing to reverse).
# If they are equal, the string is a palindrome. The outer function calls this
# nested helper function with the input string and returns the result. This
# demonstrates nested functions for string validation operations.
def check_palindrome(s):
    # Function definition
    def is_palindrome(s):
        # Function definition
        return s == s[::-1]
            # Returns the result

    return is_palindrome(s)
        # Returns the result

result = check_palindrome("racecar")
print(result)

"""
Problem: 379
Write a Python program to find the number closest to zero in a list of numbers using the `key` parameter in the `min()` function.

def closest_to_zero(numbers):
    # Function definition
    closest = numbers[0]
    for num in numbers:
        # Iterates through each element
        if abs(num) < abs(closest):
            closest = num
    return closest
        # Returns the result

result = closest_to_zero([-5, 2, 3, -1, 0, -7])
print(result)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires creating a function with a nested helper function to
# check if a list is sorted in ascending order. The outer function `check_sorted()`
# should contain an inner helper function `is_sorted()` that verifies the list
# is sorted. The outer function should call this nested helper function and return
# the result. Cela démontre nested functions for list validation.
#
# Prérequis Clés :
# - Function must define a nested helper function `is_sorted()` inside `check_sorted()`
# - The nested function should check if each element <= next element
# - The outer function should call the nested function and return the result
# - Must return True if sorted, False otherwise
#
# Exemple d'Entrée/Sortie :
# - check_sorted([1, 2, 3, 4, 5]) should return True
# - check_sorted([5, 2, 3, 1]) should return False
#
# Algorithm: Define nested is_sorted() that checks lst[i] <= lst[i+1] for all i, call it.
# ============================================================================
"""
Problem: 380
Write a Python program that defines a main function `check_sorted()` and a helper function `is_sorted(lst)` that checks if a list is sorted in ascending order. The `check_sorted()` function should use the helper function to return whether the list is sorted.
    # Sorts elements in ascending order

# EXPLICATION DE LA SOLUTION :
# This solution defines a nested helper function `is_sorted()` inside the outer
# function `check_sorted()`. The nested function iterates through the list and
# checks if each element is less than or equal to the next element. If any element
# is greater than the next, it returns False immediately. If all elements are in
# order, it returns True. The outer function calls this nested helper function
# and returns the result. Cela démontre nested functions for list validation.
def check_sorted(lst):
    # Function definition
    def is_sorted(lst):
        # Function definition
        for i in range(len(lst) - 1):
            # Iterates through each element
            if lst[i] > lst[i + 1]:
                return False
                    # Returns the result
        return True
            # Returns the result

    return is_sorted(lst)
        # Sorts elements in ascending order

result = check_sorted([1, 2, 3, 4])
    # Sorts elements in ascending order
print(result)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires converting a list of numeric strings to a list of integers
# without using a for loop. The function should prompt the user for input, split
# the input into a list of strings, and convert them to integers. Cela démontre
# using map() function to transform list elements without explicit loops.
#
# Prérequis Clés :
# - Function must prompt user for input (list of numbers as strings)
# - Function must convert strings to integers
# - Cannot use a for loop
# - Must return a list of integers
#
# Exemple d'Entrée/Sortie :
# - convert_to_integers(["10", "20", "30", "40"]) should return [10, 20, 30, 40]
# - User input "1 2 3 4" should become [1, 2, 3, 4]
#
# Algorithm: Use map(int, strings) to convert each string to integer, convert to list.
# ============================================================================
"""
Problème 381 :
Écrivez une fonction où utilisateur tapez une liste de nombres dans chaîne et retourne une liste de nombres dans integer. N'utilisez pas un pour loop.
"""

# EXPLICATION DE LA SOLUTION :
# This solution uses the `map()` function to convert each string to an integer
# without using a for loop. The map(int, user) applies the int() function to
# each element in the user input list, and list() converts the map iterator to
# a list. This is a functional programming approach that avoids explicit loops.
# The solution also shows a function version that takes a list of strings directly.
user = input("type numbers: ").split()
    # Gets user input

print(list(map(int, user)))


def convert_to_integers(strings):
    # Function definition
    return list(map(int, strings))
        # Returns the result

numbers_in_strings = ["10", "20", "30", "40"]

print(convert_to_integers(numbers_in_strings))

"""
Problem: 382
Write a Python program to sort a list of strings by their length using the `key` parameter in the `sorted()` function.
    # Sorts elements in ascending order

def sort_strings_by_length(strings):
    # Function definition
    sorted_strings = sorted(strings, key=len)
        # Sorts elements in ascending order
    return sorted_strings
        # Returns the result

result = sort_strings_by_length(["apple", "fig", "banana", "kiwi"])
print(result)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem is similar to problem 382 - it requires sorting a list of strings
# by their length using the `key` parameter in the `sorted()` function. This is
# a duplicate exercise to reinforce the concept of sorting by a key function.
#
# Prérequis Clés :
# - Function must accept a list of strings as input
# - Function must use `sorted()` with a `key` parameter
# - Function must sort by string length (shortest to longest)
# - Must return a new sorted list
#
# Exemple d'Entrée/Sortie :
# - length_strings(["Jonathan", "chris", "mimi"]) should return
#   ["mimi", "chris", "Jonathan"] (sorted by length: 4, 5, 8)
#
# Algorithm: Use sorted() with key=len to sort by string length.
# ============================================================================
"""
383
Write a Python program to sort a list of strings by their length using the `key` parameter in the `sorted()` function.
    # Sorts elements in ascending order

# EXPLICATION DE LA SOLUTION :
# This solution uses the `sorted()` function with `key=len` to sort the strings
# by their length. This is functionally identical to problem 382, demonstrating
# the same sorting pattern with different variable names. The len function serves
# as the key, allowing sorted() to compare strings based on length rather than
# alphabetical order.
def length_strings(lst):
    # Function definition
    sort = sorted(lst, key=len)
        # Sorts elements in ascending order
    return sort
        # Returns the result

lst = ["Jonathan", "chris", "mimi"]
print(length_strings(lst))

"""
Problem: 384
Write a Python program to sort a list of tuples based on the second element using the `key` parameter in the `sorted()` function.
    # Sorts elements in ascending order

def sort_tuples_by_second(tuples):
    # Function definition
    sorted_tuples = sorted(tuples, key=lambda x: x[1])
        # Sorts elements in ascending order
    return sorted_tuples
        # Returns the result

result = sort_tuples_by_second([(1, 3), (2, 1), (3, 2)])
print(result)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires sorting a list of dictionaries based on the value of a
# specific key using the `key` parameter in the `sorted()` function. For example,
# sorting by "age" would order dictionaries by their age values. Cela démontre
# using lambda functions to extract dictionary values for sorting.
#
# Prérequis Clés :
# - Function must accept a list of dictionaries and a key name as input
# - Function must use `sorted()` with a `key` parameter
# - Function must sort by the value of the specified key in each dictionary
# - Must return a new sorted list
#
# Exemple d'Entrée/Sortie :
# - sort_dicts_by_key([{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}], "age")
#   should return [{"name": "Bob", "age": 25}, {"name": "Alice", "age": 30}]
#
# Algorithm: Use sorted() with key=lambda x: x[key_name] to sort by dictionary value.
# ============================================================================
"""
Problem: 385
Write a Python program to sort a list of dictionaries based on the value of a specific key using the `key` parameter in the `sorted()` function.
    # Sorts elements in ascending order

# EXPLICATION DE LA SOLUTION :
# This solution uses the `sorted()` function with a lambda function as the key
# parameter. The lambda function `lambda x: x[key_name]` extracts the value
# associated with the specified key_name from each dictionary. The sorted()
# function then compares dictionaries based on these extracted values, resulting
# in dictionaries sorted by the specified key's value in ascending order. This
# demonstrates custom sorting of complex data structures.
def sort_dicts_by_key(dicts, key_name):
    # Function definition
    sorted_dicts = sorted(dicts, key=lambda x: x[key_name])
        # Sorts elements in ascending order
    return sorted_dicts
        # Returns the result

result = sort_dicts_by_key([{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}], "age")
print(result)

# ============================================================================
# EXPLICATION DU PROBLÈME :
# This problem requires finding the longest word in a list using the `key`
# parameter. The function should use max() with key=len to find the word with
# the maximum length. Cela démontre using the key parameter with max() for
# finding maximum based on a property rather than value.
#
# Prérequis Clés :
# - Function must accept a list of words as input
# - Function must use `max()` with a `key` parameter (or manual implementation)
# - Function must return the longest word
# - Should use key=len to compare by length
#
# Exemple d'Entrée/Sortie :
# - longest_word(["apple", "banana", "cherry", "date"]) should return "banana"
# - longest_word(["hi", "hello", "world"]) should return "hello" or "world"
#
# Algorithm: Use max() with key=len to find word with maximum length.
# ============================================================================
"""
Problem: 386
Write a Python program to find the longest word in a list of words using the `key` parameter.

# EXPLICATION DE LA SOLUTION :
# Remarque : The provided solution doesn't use max() with key parameter as required.
# A correct implementation would use: max(words, key=len). The current solution
# manually iterates through the list and compares lengths, which works but doesn't
# follow the requirement to use the key parameter. The key parameter allows max()
# to compare words based on their length rather than alphabetically.
def longest_word(words):
    # Function definition
    longest = ""
    for word in words:
        # Iterates through each element
        if len(word) > len(longest):
            longest = word
    return longest
        # Returns the result

result = longest_word(["apple", "banana", "cherry", "date"])
print(result)

"""
Problem: 387
Write a Python program to sort a list of numbers based on their absolute value using the `key` parameter in the `sorted()` function.
    # Sorts elements in ascending order

def sort_by_absolute_value(numbers):
    # Function definition
    sorted_numbers = sorted(numbers, key=abs)
        # Sorts elements in ascending order
    return sorted_numbers
        # Returns the result

result = sort_by_absolute_value([-2, -3, 1, 5, -4])
print(result)

"""
Problem: 388
Write a Python program to sort a list of strings by the last character of each string using the `key` parameter in the `sorted()` function.
    # Sorts elements in ascending order

def sort_strings_by_last_character(strings):
    # Function definition
    sorted_strings = sorted(strings, key=lambda x: x[-1])
        # Sorts elements in ascending order
    return sorted_strings
        # Returns the result

result = sort_strings_by_last_character(["banana", "apple", "grape", "kiwi"])
print(result)

def main(lst):
    # Function definition
    def inner(word):
        # Function definition
        return word[-1]
            # Returns the result
    return list(sorted(lst, key=inner))
        # Sorts elements in ascending order

lst = ["treez", "cliff", "mountain", "tree","tree", "grassya"]
main(lst)

"""
Problem: 389
Write a Python program to find the earliest date in a list of date strings (in 'YYYY-MM-DD' format) using the `key` parameter in the `min()` function.

def earliest_date(dates):
    # Function definition
    earliest = min(dates)
    return earliest
        # Returns the result

result = earliest_date(["2023-10-01", "2024-01-15", "2022-12-31"])
print(result)

"""
Problem: 390
Write a Python program to sort a list of names by surname using the `key` parameter in the `sorted()` function.
    # Sorts elements in ascending order

def get_surname(name):
    # Function definition
    return name.split()[-1]
        # Splits string into list of words/elements

names = [
    "John Doe",
    "Jane Smith",
    "Alice Johnson",
    "Bob Brown",
    "Charlie Davis"
]

sorted_names = sorted(names, key=get_surname)
    # Sorts elements in ascending order

print(sorted_names)

"""
Problem: 391
Write a Python program to sort a list of strings alphabetically, ignoring case, using the `key` parameter in the `sorted()` function.
    # Sorts elements in ascending order

def sort_strings_alphabetically(strings):
    # Function definition
    return sorted(strings, key=str.lower)
        # Sorts elements in ascending order

strings = ["banana", "Apple", "cherry", "Date", "fig", "Grape"]
sorted_strings = sort_strings_alphabetically(strings)
print(sorted_strings)

"""
Problem: 392
Write a Python program to find the word with the highest Scrabble score in a list of words using the `key` parameter.

def scrabble_score(word):
    # Function definition
    score_chart = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1,
        'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
    }
    total_score = 0
    for letter in word.upper():
        # Converts to lowercase/uppercase
        total_score += score_chart.get(letter, 0)
    return total_score
        # Returns the result

def find_highest_scrabble_word(words):
    # Function definition
    highest_word = max(words, key=scrabble_score)
    return highest_word
        # Returns the result

result = find_highest_scrabble_word(["hello", "world", "python", "scrabble"])
print(result)

"""
Problem: 393
Write a Python program to sort a list of complex numbers by their magnitude using the `key` parameter in the `sorted()` function.
    # Sorts elements in ascending order

def sort_complex_numbers(complex_numbers):
    # Function definition
    def get_magnitude(c):
        # Function definition
        return abs(c)
            # Returns the result

    sorted_numbers = sorted(complex_numbers, key=get_magnitude)
        # Sorts elements in ascending order
    return sorted_numbers
        # Returns the result

result = sort_complex_numbers([3 + 4j, 1 + 1j, 0 + 2j, 5 + 0j])
print(result)

"""
Problem: 394
Write a Python program to find the file with the largest size in a list of file paths using the `key` parameter and `os.path.getsize`.

import os

def find_largest_file(file_paths):
    # Function definition
    def get_file_size(file_path):
        # Function definition
        return os.path.getsize(file_path)
            # Returns the result

    largest_file = max(file_paths, key=get_file_size)
    return largest_file
        # Returns the result

# Remarque : Update the file paths according to your file system.
# result = find_largest_file(["path/to/file1.txt", "path/to/file2.txt"])
# print(result)  # Uncomment and use real file paths to test.

"""
Problem: 395
Write a Python program to sort a list of fractions (using the `fractions.Fraction` class) by their value using the `key` parameter in the `sorted()` function.
    # Sorts elements in ascending order

from fractions import Fraction

def sort_fractions(fractions):
    # Function definition
    def get_fraction_value(frac):
        # Function definition
        return float(frac)
            # Returns the result

    sorted_fractions = sorted(fractions, key=get_fraction_value)
        # Sorts elements in ascending order
    return sorted_fractions
        # Returns the result

result = sort_fractions([Fraction(1, 2), Fraction(1, 3), Fraction(2, 3), Fraction(1, 4)])
print(result)

"""
Problem: 396
Write a Python program to sort a list of tuples based on the sum of their elements using the `key` parameter in the `sorted()` function.
    # Sorts elements in ascending order

def sort_tuples_by_sum(tuples):
    # Function definition
    def get_sum(tup):
        # Function definition
        return sum(tup)
            # Returns the result

    sorted_tuples = sorted(tuples, key=get_sum)
        # Sorts elements in ascending order
    return sorted_tuples
        # Returns the result

result = sort_tuples_by_sum([(1, 2), (3, 4), (1, 1), (2, 2)])
print(result)

def main(lst_tuples):
    # Function definition
    def inner(tup):
        # Function definition
        return tup[0] + tup[1]
            # Returns the result
    return list(sorted(lst_tuples, key=inner))
        # Sorts elements in ascending order

lst_tuples = [(1,64),(7,3),(2,9)]
print(main(lst_tuples))

"""
Problem: 397
Write a Python program to find the number closest to zero in a list of numbers using the `key` parameter in the `min()` function.

def closest_to_zero(numbers):
    # Function definition
    closest = min(numbers, key=abs)
    return closest
        # Returns the result

result = closest_to_zero([-5, 2, 3, -1, 0, -7])
print(result)

"""
Problem: 398
Write a Python program to sort a list of 2D points (tuples) by their distance from the origin using the `key` parameter in the `sorted()` function.
    # Sorts elements in ascending order

def sort_points_by_distance(points):
    # Function definition
    def get_distance(point):
        # Function definition
        return (point[0]**2 + point[1]**2)**0.5
            # Returns the result

    sorted_points = sorted(points, key=get_distance)
        # Sorts elements in ascending order
    return sorted_points
        # Returns the result

result = sort_points_by_distance([(3, 4), (1, 1), (0, 2), (5, 0)])
print(result)

"""
Problem: 399
Write a Python program to sort a list of words by the number of distinct letters in each word using the `key` parameter in the `sorted()` function.
    # Sorts elements in ascending order

def sort_words_by_distinct_letters(words):
    # Function definition
    def distinct_letter_count(word):
        # Function definition
        return len(set(word))
            # Returns the result

    sorted_words = sorted(words, key=distinct_letter_count)
        # Sorts elements in ascending order
    return sorted_words
        # Returns the result

result = sort_words_by_distinct_letters(["apple", "banana", "cherry", "date"])
print(result)

"""
Problem: 400
Write a Python program to find the word with the highest sum of ASCII values of its characters in a list of words using the `key` parameter.

def main(lst):
    # Function definition
    def inner(word):
        # Function definition
        count = 0
        for char in word:
            # Iterates through each element
            count += ord(char)
        return count
            # Returns the result
    return max(lst, key=inner)
        # Returns the result

lst = ["aa", "bb", "cc", "dg","uu", "ak"]
main(lst)

def ascii_value(word):
    # Function definition
    total_value = 0
    for char in word:
        # Iterates through each element
        total_value += ord(char)
    return total_value
        # Returns the result

def find_highest_ascii_word(words):
    # Function definition
    highest_word = max(words, key=ascii_value)
    return highest_word
        # Returns the result

result = find_highest_ascii_word(["hello", "world", "python", "scrabble"])
print(result)


"""
Problem: 401
Write a Python program to sort a list of strings by the number of vowels in each string using the `key` parameter in the `sorted()` function."
    # Sorts elements in ascending order

def count_vowels(s):
    # Function definition
    vowels = "aeiou"
    count = 0
    s = s.lower()
        # Converts to lowercase/uppercase

    for char in s:
        # Iterates through each element
        if char in vowels:
            count += 1
    return count
        # Returns the result

def sort_by_vowel_count(strings):
    # Function definition
    return sorted(strings, key=count_vowels)
        # Sorts elements in ascending order

strings = ["apple", "banana", "cherry", "date", "fig", "grape"]
sorted_strings = sort_by_vowel_count(strings)
print(sorted_strings)

"""
Problème 402 :
Écrivez une fonction où utilisateur transforms une liste d'entiers dans une liste de chaînes. N'utilisez pas un pour loop.
"""

def convert_to_integers(integers):
    # Function definition
    return list(map(str, integers))
        # Returns the result

numbers = [4, 24, 66, 25]
print(convert_to_integers(numbers))

"""
Problem: 403
Write a Python program to add 5 to each number in a list. Do not use map().

def add_five(lst):
    # Function definition
    result = []

    for number in lst:
        # Iterates through each element
        result.append(number + 5)
    return result
        # Returns the result

lst = [1, 2, 3, 4, 5]
print(add_five(lst))

"""
Problème 404 :
Écrivez une fonction Python appelée `find_min` qui prend une liste de nombres en entrée et retourne le minimum nombre dans la liste. N'utilisez pas min().
"""

def find_min(numbers):
    # Function definition
    min_num = numbers[0]

    for number in numbers:
        # Iterates through each element
        if number < min_num:
            min_num = number
    return min_num
        # Returns the result

lst = [2, 6, 1, 189]
print(find_min(lst))

def main(user):
    # Function definition
    int_lst = []
    for num in user:
        # Iterates through each element
        int_lst.append(int(num))
    min_num = int_lst[0]
    for num in int_lst:
        # Iterates through each element
        if num < min_num:
            min_num = num
    return min_num
        # Returns the result

user = input("type lst of number: ").split()
    # Gets user input
main(user)

"""
Problem: 405
Write a function that converts centimetets to inches. Type a integer as argument.

def converts(cm):
    # Function definition

    inch = cm * 0.39
    print(inch)

number = 5
print(converts(number))

"""
Problem: 406
Write a Python program to reverse a list use the reverse() function. Prompt the user to enter a list of elements.

def reverse(lst):
    # Function definition
    lst.reverse()
    return lst
        # Returns the result

lst = [1, 2, 3, 4]
print(reverse(lst))

"""
Problème 407 :
Écrivez une fonction Python appelée `calculate_average` qui prend une liste de nombres en entrée et retourne le moyenne de ces nombres. N'utilisez pas sum() et len().
"""

def calculate_average(lst):
    # Function definition
    length_num = 0
    for number in lst:
        # Iterates through each element
        length_num += 1

    add_num = 0
    for number in lst:
        # Iterates through each element
        add_num += number

    total = add_num / length_num
    return total
        # Returns the result

lst = [23, 56, 33]
print(calculate_average(lst))

"""
Problème 408 :
Écrivez une fonction Python appelée remove_duplicates qui prend une chaîne en entrée et retourne une nouvelle chaîne avec en double caractères removed, avec maintaining le original order de caractères.
"""

def remove_duplicates(lst):
    # Function definition
    lst = lst.split()
        # Splits string into list of words/elements
    unique = []
    commom = []

    for word in lst:
        # Iterates through each element
        if word in unique:
            commom.append(word)
        else:
            unique.append(word)
    return unique
        # Returns the result

lst = " what is you is going is to do"
print(remove_duplicates(lst))

"""
Problème 409 :
Écrivez un programme qui maps une liste de mots dans une liste d'entiers representing le lengths de le correponding words sans en utilisant len(). Utilisez un dictionnaire.
"""

def len_words(lst):
    # Function definition
    result = {}

    for word in lst:
        # Iterates through each element
        count = 0
        for char in word:
            # Iterates through each element
            count += 1
        result[word] = count
    return result
        # Returns the result

lst = ["Jonathan", "Chris", "Jeremy"]
print(len_words(lst))

"""
Problem: 410
Write a Python program to determine the len of a string in a list. Do not use filter(). For example if the len is 3 and the list is ["jon", "chris", "tom", "Jeremy"] the result should be ["jon", "tom"].
def filter_string(lst):
    # Function definition
    result = []
    for word in lst:
        # Iterates through each element
        if len(word) == 3:
            # Checks condition
            result.append(word)
    return result
        # Returns the result

lst = ["jon", "chris", "tom", "Jeremy"]
print(filter_string(lst))

"""
Problem: 411
Write a Python function called calculate_sum that takes two numbers as arguments. Inside this function, define a nested function that returns their sum."
def calculate_sum(a, b):
    # Function definition

    def inner_sum(x, y):
        # Function definition
        return x + y
            # Returns the result

    return inner_sum(a, b)
        # Returns the result

result = calculate_sum(7, 3)
print(result)

"""
Problem: 412
Write a Python function called calculate_product that takes two numbers as arguments. Inside this function, define a nested function that returns their product.

def calculate_product(a, b):
    # Function definition
    def product():
        # Function definition
        return a * b
            # Returns the result
    return product()
        # Returns the result

result = calculate_product(3, 5)
print(result)

"""
Problem: 413
Write a Python function called calculate_difference that takes two numbers as arguments. Inside this function, define a nested function that returns their difference.

def calculate_difference(a, b):
    # Function definition
    def difference():
        # Function definition
        return a - b
            # Returns the result
    return difference()
        # Returns the result

result = calculate_difference(10, 3)
print(result)

"""
Problem: 414
Write a Python function called calculate_quotient that takes two numbers as arguments. Inside this function, define a nested function that returns their quotient.

def calculate_quotient(a, b):
    # Function definition
    def quotient():
        # Function definition
        return a / b
            # Returns the result
    return quotient()
        # Returns the result

result = calculate_quotient(10, 2)
print(result)


"""
Problem: 415
Write a Python function area_of_rectangle that calculates the area of a rectangle given its length and width. Use a nested function to calculate the area.

def area_of_rectangle(length, width):
    # Function definition
    def area():
        # Function definition
        return length * width
            # Returns the result
    return area()
        # Returns the result

result = area_of_rectangle(5, 4)
print(result)

"""
Problem: 416
Write a Python function perimeter_of_square that calculates the perimeter of a square given its side length. Use a nested function to calculate the perimeter.

def perimeter_of_square(side_length):
    # Function definition
    def perimeter():
        # Function definition
        return 4 * side_length
            # Returns the result
    return perimeter()
        # Returns the result

result = perimeter_of_square(5)
print(result)

"""
Problem: 417
Write a Python function called fahrenheit_to_celsius that takes a temperature in Fahrenheit and converts it to Celsius. Use a nested function to do the conversion.

def fahrenheit_to_celsius(fahrenheit):
    # Function definition
    def convert():
        # Function definition
        return (fahrenheit - 32) * 5 / 9
            # Returns the result
    return convert()
        # Returns the result

result = fahrenheit_to_celsius(68)
print(result)

"""
Problem: 418
Write a Python function called celsius_to_fahrenheit that takes a temperature in Celsius and converts it to Fahrenheit. Use a nested function to do the conversion.

def celsius_to_fahrenheit(celsius):
    # Function definition
    def convert():
        # Function definition
        return (celsius * 9 / 5) + 32
            # Returns the result
    return convert()
        # Returns the result

result = celsius_to_fahrenheit(20)
print(result)

"""
Problem: 419
Write a Python function called even_or_odd that takes a number and returns whether it’s even or odd. Use a nested function to check this condition.

def even_or_odd(number):
    # Function definition
    def check():
        # Function definition
        if number % 2 == 0:
            # Checks condition
            return "Even"
                # Returns the result
        else:
            return "Odd"
                # Returns the result
    return check()
        # Returns the result

result = even_or_odd(7)
print(result)

"""
Problem: 420
Write a Python function called is_prime that checks if a number is prime. Use a nested function to iterate and check divisibility of numbers.

def is_prime(number):
    # Function definition
    def check_divisibility(n):
        # Function definition
        for i in range(2, int(n**0.5) + 1):
            # Iterates through each element
            if n % i == 0:
                # Checks condition
                return False
                    # Returns the result
        return True
            # Returns the result

    if number < 2:
        return False
            # Returns the result
    return check_divisibility(number)
        # Returns the result

result = is_prime(29)
print(result)

"""
Problem: 421
Write a Python function called list_sum that takes a list of numbers and returns the sum. Inside it, define a nested function that adds the elements.

def list_sum(numbers):
    # Function definition
    def add_elements():
        # Function definition
        total = 0
        for number in numbers:
            # Iterates through each element
            total += number
        return total
            # Returns the result
    return add_elements()
        # Returns the result

result = list_sum([1, 2, 3, 4])
print(result)

"""
Problem: 422
Write a Python function called list_product that takes a list of numbers and returns the product of all elements. Use a nested function to compute the product.

def list_product(numbers):
    # Function definition
    def multiply_elements():
        # Function definition
        product = 1
        for number in numbers:
            # Iterates through each element
            product *= number
        return product
            # Returns the result
    return multiply_elements()
        # Returns the result

result = list_product([1, 2, 3, 4])
print(result)

"""
Problem: 423
Write a Python function greater_than that takes two numbers and returns True if the first is greater than the second. Use a nested function for comparison.

def greater_than(a, b):
    # Function definition
    def compare():
        # Function definition
        return a > b
            # Returns the result
    return compare()
        # Returns the result

result = greater_than(10, 5)
print(result)

"""
Problem: 424
Write a Python function string_length that takes a string and returns its length. Use a nested function that calculates and returns the length.

def string_length(s):
    # Function definition
    def calculate_length():
        # Function definition
        length = 0
        for char in s:
            # Iterates through each element
            length += 1
        return length
            # Returns the result
    return calculate_length()
        # Returns the result

result = string_length("Hello, World!")
print(result)

"""
Problem: 425
Write a Python function first_and_last that takes a string and returns its first and last characters using a nested function.

def first_and_last(s):
    # Function definition
    def get_first_last():
        # Function definition
        if len(s) > 0:
            return s[0], s[-1]
                # Returns the result
        else:
            return None, None
                # Returns the result
    return get_first_last()
        # Returns the result

result = first_and_last("Hello")
print(result)

"""
Problem: 426
Write a Python function count_vowels that takes a string and counts the number of vowels using a nested function.

def count_vowels(s):
    # Function definition
    def is_vowel(char):
        # Function definition
        return char.lower() in 'aeiou'
            # Converts to lowercase/uppercase

    count = 0
    for char in s:
        # Iterates through each element
        if is_vowel(char):
            count += 1
    return count
        # Returns the result

result = count_vowels("Hello, World!")
print(result)

"""
Problem: 427
Write a Python function reverse_string that takes a string and returns its reverse using a nested function.

def reverse_string(s):
    # Function definition
    def reverse():
        # Function definition
        reversed_s = ""
        for char in s:
            # Iterates through each element
            reversed_s = char + reversed_s
        return reversed_s
            # Returns the result
    return reverse()
        # Returns the result

result = reverse_string("Hello")
print(result)

"""
Problem: 428
Write a Python function is_palindrome that takes a string and checks if it’s a palindrome using a nested function.

def is_palindrome(s):
    # Function definition
    def check():
        # Function definition
        return s == s[::-1]
            # Returns the result
    return check()
        # Returns the result

result = is_palindrome("racecar")
print(result)

"""
Problem: 429
Write a Python function multiply_by_n that takes a number n and returns another function that multiplies a given number by n.

def multiply_by_n(n):
    # Function definition
    def multiply(x):
        # Function definition
        return n * x
            # Returns the result
    return multiply
        # Returns the result

multiply_by_3 = multiply_by_n(3)
result = multiply_by_3(5)
print(result)

"""
Problem: 430
Write a Python function add_tax that takes a price and returns the price after applying a tax percentage using a nested function.

def add_tax(price):
    # Function definition
    def calculate_tax():
        # Function definition
        tax_rate = 0.15
        return price + (price * tax_rate)
            # Returns the result
    return calculate_tax()
        # Returns the result

result = add_tax(100)
print(result)

"""
Problem: 431
Write a Python function greet_person that takes a name and returns a greeting using a nested function.

def greet_person(name):
    # Function definition
    def greeting():
        # Function definition
        return f"Hello, {name}!"
            # Returns the result
    return greeting()
        # Returns the result

result = greet_person("Alice")
print(result)

"""
Problem: 432
Write a Python function factorial that calculates the factorial of a number using a nested recursive function.

def factorial(n):
    # Function definition
    def calc_factorial(num):
        # Function definition
        if num == 0 or num == 1:
            # Checks condition
            return 1
                # Returns the result
        else:
            return num * calc_factorial(num - 1)
                # Returns the result

    return calc_factorial(n)
        # Returns the result

result = factorial(5)
print(result)

"""
Problem: 433
Write a Python function exponent that calculates the result of raising a number to a power using a nested function.

def exponent(base, power):
    # Function definition
    def calculate():
        # Function definition
        result = 1
        for _ in range(power):
            # Iterates through each element
            result *= base
        return result
            # Returns the result
    return calculate()
        # Returns the result

result = exponent(2, 3)
print(result)

"""
Problem: 434
Write a Python function gcd that calculates the greatest common divisor of two numbers using a nested function.

def gcd(a, b):
    # Function definition
    def calculate_gcd(x, y):
        # Function definition
        while y != 0:
            (x, y) = (y, x % y)
        return x
            # Returns the result
    return calculate_gcd(a, b)
        # Returns the result

result = gcd(48, 18)
print(result)

"""
Problem: 435
Write a Python function lcm that calculates the least common multiple of two numbers using a nested function.

def lcm(a, b):
    # Function definition
    def calculate_lcm(x, y):
        # Function definition
        return abs(x * y) // gcd(x, y)
            # Returns the result

    def gcd(x, y):
        # Function definition
        while y != 0:
            (x, y) = (y, x % y)
        return x
            # Returns the result

    return calculate_lcm(a, b)
        # Returns the result

result = lcm(4, 5)
print(result)


"""
Problem: 436
Write a Python function square_of_number that returns the square of a number using a nested function.

def square_of_number(n):
    # Function definition
    def square():
        # Function definition
        return n * n
            # Returns the result
    return square()
        # Returns the result

result = square_of_number(5)
print(result)

"""
Problem: 437
Write a Python function cube_of_number that returns the cube of a number using a nested function.

def cube_of_number(n):
    # Function definition
    def cube():
        # Function definition
        return n * n * n
            # Returns the result
    return cube()
        # Returns the result

result = cube_of_number(3)
print(result)

"""
Problem: 438
Write a Python function sort_list_descending that takes a list and sorts it in descending order using a nested function.

def sort_list_descending(lst):
    # Function definition
    def sort():
        # Function definition
        sorted_list = []
        while lst:
            maximum = lst[0]
            for item in lst:
                # Iterates through each element
                if item > maximum:
                    maximum = item
            sorted_list.append(maximum)
            lst.remove(maximum)
        return sorted_list
            # Returns the result
    return sort()
        # Returns the result

result = sort_list_descending([4, 1, 3, 2])
print(result)

"""
Problem: 439
Write a Python function max_of_three that takes three numbers and returns the maximum using a nested function.

def max_of_three(a, b, c):
    # Function definition
    def find_max():
        # Function definition
        max_value = a
        if b > max_value:
            max_value = b
        if c > max_value:
            max_value = c
        return max_value
            # Returns the result
    return find_max()
        # Returns the result

result = max_of_three(10, 20, 15)
print(result)

"""
Problem: 440
Write a Python function average_of_list that calculates the average of a list of numbers using a nested function. Do not use sum() and len()

def average_of_list(lst):
    # Function definition
    def calculate_average():
        # Function definition
        total = 0
        count = 0
        for number in lst:
            # Iterates through each element
            total += number
            count += 1
        return total / count if count != 0 else 0
            # Returns the result
    return calculate_average()
        # Returns the result

result = average_of_list([10, 20, 30, 40])
print(result)

"""
Problem: 441
Write a Python function average_of_list that calculates the average of a list of numbers using a nested function.

def average_of_list(lst):
    # Function definition
    def calculate_average():
        # Function definition
        total = 0
        count = 0
        for number in lst:
            # Iterates through each element
            total += number
            count += 1
        return total / count if count != 0 else 0
            # Returns the result
    return calculate_average()
        # Returns the result

result = average_of_list([5, 15, 25])
print(result)

"""
Problem: 442
Write a Python function is_uppercase that checks if all characters in a string are uppercase using a nested function.

def is_uppercase(s):
    # Function definition
    def check():
        # Function definition
        for char in s:
            # Iterates through each element
            if not char.isupper():
                return False
                    # Returns the result
        return True
            # Returns the result
    return check()
        # Returns the result

result = is_uppercase("HELLO")
print(result)

"""
Problem: 443
Write a Python function is_lowercase that checks if all characters in a string are lowercase using a nested function.

def is_lowercase(s):
    # Function definition
    def check():
        # Function definition
        for char in s:
            # Iterates through each element
            if not char.islower():
                return False
                    # Returns the result
        return True
            # Returns the result
    return check()
        # Returns the result

result = is_lowercase("hello")
print(result)

"""
Problem: 444
Write a Python function string_contains_digit that checks if a string contains a digit using a nested function.

def string_contains_digit(string):
    # Function definition

    def contains_digit(x):
        # Function definition
        for char in x:
            # Iterates through each element
            if char.isdigit():
                return True
                    # Returns the result
        return False
            # Returns the result

    return contains_digit(string)
        # Returns the result

string = "jonathan5"
print(string_contains_digit(string))

"""
Problem: 445
Write a Python function string_contains_letter that checks if a string contains a letter using a nested function.

def string_contains_letter(string):
    # Function definition

    def contains_letter(x):
        # Function definition
        for char in x:
            # Iterates through each element
            if char.isalpha():
                return True
                    # Returns the result
        return False
            # Returns the result

    return contains_letter(string)
        # Returns the result

string = "123455g"
print(string_contains_letter(string))

"""
Problem: 446
Write a Python function calculate_average that takes three numbers and returns their average using a nested function.

def average_of_list(lst):
    # Function definition

    def average(x):
        # Function definition
        for number in x:
            # Iterates through each element
            count_len = len(x)
            add_num = sum(x)
            total = add_num / count_len

        return total
            # Returns the result

    return average(lst)
        # Returns the result

lst = [34, 67, 667]
print(average_of_list(lst))

"""
Problem: 447
Write a Python function check_multiple_of_n that takes two numbers and checks if the first is a multiple of the second using a nested function.

def check_multiple_of_n(num1, num2):
    # Function definition

    def is_multiple(x, y):
        # Function definition
        return x % y == 0
            # Returns the result

    return is_multiple(num1, num2)
        # Returns the result

print(check_multiple_of_n(10, 2))
print(check_multiple_of_n(10, 3))

"""
Problem: 448
Write a Python function longest_string that takes a list of strings and returns the longest one using a nested function.

def longest_string(lst):
    # Function definition

    def longest(x):
        # Function definition
        longest_word = x[0]
        for word in x:
            # Iterates through each element
            if word > longest_word:
                longest_word = word
        return longest_word
            # Returns the result

    return longest(lst)
        # Returns the result

lst = ["jon", "zonathan", "mimi"]
print(longest_string(lst))


def longest_string(lst):
    # Function definition

    def find_longest(strings):
        # Function definition
        return max(strings, key=len)
            # Returns the result

    return find_longest(lst)
        # Returns the result

lst = ["jon", "zonathan", "mimi"]
print(longest_string(lst))

"""
Problem: 449
Write a Python function shortest_string that takes a list of strings and returns the shortest one using a nested function.

def shortest_string(lst):
    # Function definition

    def shortest(x):
        # Function definition
        return min(x, key=len)
            # Returns the result

    return shortest(lst)
        # Returns the result

lst = ["chris", "tit", "mountain"]
print(shortest_string(lst))

"""
Problem: 450
Write a Python function remove_duplicates that takes a list and removes duplicates using a nested function.

def remove_duplicates(lst):
    # Function definition

    def duplicates_removed(x):
        # Function definition
        unique = set()

        for word in x:
            # Iterates through each element
            unique.add(word)
        return unique
            # Returns the result

    return duplicates_removed(lst)
        # Returns the result

lst = ["not", "not", "today", "today"]
print(remove_duplicates(lst))

"""
Problem: 451
Write a Python function fibonacci that generates the nth Fibonacci number using a nested recursive function.

def fibonacci(n):
    # Function definition

    def fib_recursive(n):
        # Function definition
        if n <= 1:
            return n
                # Returns the result
        else:
            return fib_recursive(n - 1) + fib_recursive(n - 2)
                # Returns the result

    return fib_recursive(n)
        # Returns the result

n = 10
print(fibonacci(n))

"""
Problem: 452
Write a Python function called calculate_sum that takes two numbers as arguments. Inside this function, define a nested function that returns their sum and another function that returns the multiplication."
def calculate_sum(a, b):
    # Function definition

    def inner_sum(x, y):
        # Function definition
        return x + y
            # Returns the result

    def inner_mult(x, y):
        # Function definition
        return x * y
            # Returns the result

    return inner_sum(a, b), inner_mult(a, b)
        # Returns the result

print(calculate_sum(7, 3))


"""
Problem: 453
Write a Python function called calculate_integers that takes two numbers as arguments. Inside this function, define nested functions that returns their product, sum and division.

def calculate_integers(a, b):
    # Function definition

    def product(x, y):
        # Function definition
        return x * y
            # Returns the result

    def sum_int(x, y):
        # Function definition
        return x + y
            # Returns the result

    def division(x, y):
        # Function definition
        return x / y
            # Returns the result

    return product(a, b), sum_int(a, b), division(a, b)
        # Returns the result

print(calculate_integers(10, 5))

"""
Problem: 455
Write a Python function average_of_list that calculates the average of a list of numbers using a nested function. Use len() and sum().

def average_of_list(lst):
    # Function definition

    def average(x):
        # Function definition
        for number in x:
            # Iterates through each element
            count_len = len(x)
            add_num = sum(x)
            total = add_num / count_len

        return total
            # Returns the result

    return average(lst)
        # Returns the result

lst = [34, 67, 667]
print(average_of_list(lst))

"""
Problem: 456
Write a Python function that sorts a list of strings by their length using the key parameter.

def len_lst(lst):
    # Function definition
    sort = sorted(lst, key=len)
        # Sorts elements in ascending order

    return sort
        # Returns the result

lst = ["Jonathan", "chris", "Jeremy"]
print(len_lst(lst))

"""
Problem: 457
Write a Python function to find the minimum string by its length using the min() function with the key parameter.

def min_len(lst):
    # Function definition
    min_string = min(lst, key=len)

    return min_string
        # Returns the result

lst = ["truck", "is", "Bethany"]
print(min_len(lst))

"""
Problem: 458
Write a Python function to find the maximum string alphabetically using the key parameter.
def max_string_alpha(lst):
    # Function definition

    def max_string(x):
        # Function definition
        return len(x)
            # Returns the result

    return max(lst, key=max_string)
        # Returns the result

lst = ["hippopotamus", "giraffe", "monkey"]
print(max_string_alpha(lst))

"""
Problem: 459
Write a Python function to sort a list of dictionaries by the value associated with a specific key using the key parameter.

from operator import itemgetter

def sort_dicts_by_key(dict_list, sort_key):
    # Use itemgetter
    return sorted(dict_list, key=itemgetter(sort_key))
        # Sorts elements in ascending order

dict_list = [
    {'name': 'John', 'age': 30},
    {'name': 'Jane', 'age': 25},
    {'name': 'Doe', 'age': 35}
]

sorted_list = sort_dicts_by_key(dict_list, 'age')
print(sorted_list)

"""
Problem: 460
Write a Python function to sort a list of integers by their absolute value using the key parameter.

def sort_by_absolute_value(lst):
    # Function definition
    return sorted(lst, key=abs)
        # Sorts elements in ascending order

lst = [3, -1, -4, 2, 0]
sorted_lst = sort_by_absolute_value(lst)
print(sorted_lst)

"""
Problem: 461
Write a Python function that sorts a list of words by the number of vowels they contain using the key parameter.

def sort_words_by_vowel_count(lst):
    # Function definition

    def count_vowels(word):
        # Function definition
        vowels = 'aeiou'
        count = 0
        for char in word:
            # Iterates through each element
            if char in vowels:
                count += 1
        return count
            # Returns the result

    return sorted(lst, key=count_vowels)
        # Sorts elements in ascending order

lst = ["apple", "banana", "cherry", "date"]
print(sort_words_by_vowel_count(lst))

"""
Problem: 462
Write a Python function to find the longest word in a list using the max() function with the key parameter.

def longest_word(lst):
    # Function definition
    longest_w = max(lst, key=len)

    return longest_w
        # Returns the result

lst = ["cheater", "lepard", "lion"]
print(longest_word(lst))

"""
Problem: 463
Write a Python function to sort a list of tuples by the sum of the elements in each tuple using the key parameter.

def sum_of_tuple(lst):
    # Function definition

    return sorted(lst, key=sum)
        # Sorts elements in ascending order

lst = [(9, 9, 9), (5, 5, 5), (8, 8, 8)]
print(sum_of_tuple(lst))

"""
Problem: 464
Write a Python function to sort a list of strings by the last character of each string using the key parameter.

def list_of_strings_lst(lst):
    # Function definition

    def last_char(s):
        # Function definition
        return s[-1]
            # Returns the result

    return sorted(lst, key=last_char)
        # Sorts elements in ascending order

lst = ["car", "side", "beach"]
print(list_of_strings_lst(lst))

"""
Problem: 465
Write a Python function to sort a list of strings by the number of uppercase letters in each string using the key parameter.

def sort_number_uppercases(lst):
    # Function definition

    def uppercase_count(x):
        # Function definition
        count = 0
        for char in x:
            # Iterates through each element
            if char.isupper():
                count += 1
        return count
            # Returns the result

    return sorted(lst,
        # Sorts elements in ascending order
    key=uppercase_count)

lst = ["SNSKEYHG", "SlIppery", "SNAKEGG"]
print(sort_number_uppercases(lst))

"""
Problem: 466
Write a Python function to find the tuple with the largest product of its elements using the key parameter.

def tuple_largest_product(lst):
    # Function definition

    def product(x):
        # Function definition
        count = 1
        for number in x:
            # Iterates through each element
            count *= number
        return count
            # Returns the result

    return max(lst, key=product)
        # Returns the result

lst = [(2, 2, 2), (4, 4, 4)]
print(tuple_largest_product(lst))

"""
Problem: 467
Write a Python function to sort a list of floating-point numbers by their rounded value using the key parameter.

def floating_point(numbers):
    # Function definition
    return sorted(numbers, key=round)
        # Sorts elements in ascending order

numbers = [3.7, 3.3, 2.7, 1.2, 35.4, 677.9]
print(floating_point(numbers))

"""
Problem: 468
Write a Python function to sort a list of tuples based on the first element in descending order using the key parameter.

def first_element_decending_order(lst):
    # Function definition
    def first_element(x):
        # Function definition
        return x[0]
            # Returns the result

    return sorted(lst, key=first_element, reverse=True)
        # Sorts elements in ascending order

lst = [("see", "sea", "saw"), ("zoat", "zite", "zank")]
print(first_element_decending_order(lst))

"""
Problem: 469
Write a Python function that sorts a list of words by the number of consonants using the key parameter.

def number_of_consonants(lst):
    # Function definition

    def consonants(word):
        # Function definition

        consonants_set = "bcdfghjklmnpqrstvwxyz"

        count = 0

        for char in word.lower():
            # Converts to lowercase/uppercase
            if char in consonants_set:
                count += 1
        return count
            # Returns the result

    return sorted(lst, key=consonants)
        # Sorts elements in ascending order

lst = ["zzzzzzzzz", "yyyyyy", "bbb"]
print(number_of_consonants(lst))

"""
Problem: 470
Write a Python function to find the shortest string in a list using the min() function with the key parameter.

def min_string(lst):
    # Function definition
    return min(lst, key=len)
        # Returns the result

lst = ["down", "up"]
print(min_string(lst))

"""
Problem: 471
Write a Python function to sort a list of dictionaries by the length of the value associated with a specific key using the key parameter.

def length_of_value(lst, key):
    # Function definition

    def length_function(x):
        # Function definition
        return len(x.get(key, ""))
            # Returns the result

    return sorted(lst, key=length_function)
        # Sorts elements in ascending order

lst = [{"a": "tree", "b": "bushen"}, {"a": "tin", "b": "bash"}, {"a": "tumb", "b": "bat"}]
sorted_lst = length_of_value(lst, "b")
print(sorted_lst)

"""
Problem: 472
Write a Python function to find the person with the longest name in a list of dictionaries containing ‘name’ as a key using the max() function with the key parameter.

def find_person(lst_dict, key):
    # Function definition

    def longest_name(d):
        # Function definition
        return len(d.get(key, ""))
            # Returns the result

    return max(lst_dict, key=longest_name)
        # Returns the result

lst_dict = [{"name": "Beth"}, {"name": "Brett"}, {"name": "Jhonivan"}, {"name": "Jonathan"}]
key = "name"

print(find_person(lst_dict, key))

"""
Problem: 473
Write a Python function that sorts a list of integers by their remainder when divided by a given number using the key parameter.

def main(lst, divisor):
    # Function definition

    def inner(num):
        # Function definition
        return num % divisor
            # Returns the result
    return sorted(lst, key=inner)
        # Sorts elements in ascending order

lst = [677, 34, 9, 2, 67]
divisor = 5
main(lst, divisor)

def remainder_key(x, divisor):
    # Function definition
    return x % divisor
        # Returns the result

def sort_by_remainder(lst, divisor):
    # Function definition

    def key_func(x):
        # Function definition
        return remainder_key(x, divisor)
            # Returns the result

    return sorted(lst, key=key_func)
        # Sorts elements in ascending order

lst = [10, 23, 4, 7, 15]
divisor = 5
print(sort_by_remainder(lst, divisor))

"""
Problem: 474
Write a Python function to sort a list of dates by the year using the key parameter.

from datetime import datetime

def year_key(date):
    # Function definition
    return date.year
        # Returns the result

def sort_by_year(dates):
    # Function definition

    date_objects = []

    for date in dates:
        # Iterates through each element
        date_objects.append(datetime.strptime(date, "%d.%m.%Y"))

    sorted_dates = sorted(date_objects, key=year_key)
        # Sorts elements in ascending order

    sorted_date_strings = []
    for date in sorted_dates:
        # Iterates through each element
        sorted_date_strings.append(date.strftime("%d.%m.%Y"))

    return sorted_date_strings
        # Returns the result

dates = ["01.02.1908", "12.11.1955", "23.04.1989", "07.07.1967"]
sorted_dates = sort_by_year(dates)
print(sorted_dates)

"""
Problem: 475
Write a Python function to sort a list of names by the number of times the letter ‘a’ appears in each name using the key parameter.

def sort_by_a_count(names):
    # Function definition

    def count_a(name):
        # Function definition

        return name.lower().count('a')
            # Converts to lowercase/uppercase

    return sorted(names, key=count_a)
        # Sorts elements in ascending order

names = ["Anna", "Alice", "Bob", "Amanda", "Ava"]
sorted_names = sort_by_a_count(names)
print(sorted_names)

"""
Problem: 476
Write a Python function to sort a list of numbers by their square using the key parameter.

def sort_sqaure(lst):
    # Function definition

    def sqaured(x):
        # Function definition
        return x * x
            # Returns the result

    return sorted(lst, key=sqaured)
        # Sorts elements in ascending order


lst = [9, 5, 4, 1 ]
print(sort_sqaure(lst))

"""
Problem: 477
Write a Python function to find the list element closest to a target value using the key parameter.

def closest_to_target(lst, target):
    # Function definition

    def difference_from_target(x):
        # Function definition
        return abs(x - target)
            # Returns the result

    return min(lst, key=difference_from_target)
        # Returns the result

lst = [10, 22, 14, 3, 8]
target = 7
closest_value = closest_to_target(lst, target)
print(closest_value)

"""
Problem: 478
Write a Python function that sorts a list of tuples based on the length of the first element in each tuple using the key parameter.

def length_of_first_element(lst):
    # Function definition

    def length_of_first(x):
        # Function definition
        return len(x[0])
            # Returns the result

    return sorted(lst, key=length_of_first)
        # Sorts elements in ascending order

lst = [("initiate", "love", "seat"), ("sweet", "beat", "hell")]
sorted_list = length_of_first_element(lst)
print(sorted_list)



"""
Problem: 479
Write a Python function to sort a list of strings by the number of spaces they contain using the key parameter.

def number_of_spaces(lst):
    # Function definition

    def spaces_count(x):
        # Function definition
        return x.count(" ")
            # Returns the result

    return sorted(lst, key=spaces_count)
        # Sorts elements in ascending order

lst = ["what is happening", "why all the hate in your brain", "stop it"]
print(number_of_spaces(lst))

"""
Problem: 480
Write a Python function that finds the word with the most vowels in a list using the max() function with the key parameter.

def most_vowels(lst):
    # Function definition

    def count_vowels(word):
        # Function definition
        vowels = "aeiou"

        count = 0
        for char in word:
            # Iterates through each element
            if char in vowels:
                count += 1
        return count
            # Returns the result

    return max(lst, key=count_vowels)
        # Returns the result

lst = ["aamost", "Aaron", "bible", "buttom", "aeiouthian"]
print(most_vowels(lst))

"""
Problem: 481
Write a Python function to sort a list of integers by the number of digits they contain using the key parameter.

def sort_lst_integers(lst):
    # Function definition

    def count_digits(n):
        # Function definition
        return len(str(abs(n)))
            # Returns the result
    return sorted(lst, key=count_digits)
        # Sorts elements in ascending order

lst = [456, 56, 8, 788, 89, 1]
print(sort_lst_integers(lst))

"""
Problem: 482
Write a Python function that sorts a list of tuples by the difference between their elements using the key parameter.

def sort_tuples_by_difference(lst):
    # Function definition

    def difference(tup):
        # Function definition
        return abs(tup[0] - tup[1])
            # Returns the result

    return sorted(lst, key=difference)
        # Sorts elements in ascending order

lst = [(3, 8), (1, 7), (5, 5), (9, 2), (6, 10)]

print(sort_tuples_by_difference(lst))

"""
Problem: 483
Write a Python function to sort a list of strings by the ASCII value of their first character using the key parameter.

def sort_strings_by_ascii(lst):
    # Function definition

    def ascii_value(s):
        # Function definition
        return ord(s[0])
            # Returns the result

    return sorted(lst, key=ascii_value)
        # Sorts elements in ascending order

lst = ["banana", "apple", "cherry", "date", "elderberry"]
print(sort_strings_by_ascii(lst))

"""
Problem: 484
Write a Python function to sort a list of lists by the sum of the elements in each sublist using the key parameter.

def sort_lists_by_sum(lst):
    # Function definition

    def sum_of_elements(sublist):
        # Function definition
        return sum(sublist)
            # Returns the result

    return sorted(lst, key=sum_of_elements)
        # Sorts elements in ascending order

lst = [[3, 4], [1, 2, 3], [10], [5, 1, 1]]

print(sort_lists_by_sum(lst))

"""
Problem: 485
Write a Python function to find the word with the fewest consonants in a list using the min() function with the key parameter.

def number_of_consonants(lst):
    # Function definition

    def consonants(word):
        # Function definition

        consonants_set = "bcdfghjklmnpqrstvwxyz"

        count = 0

        for char in word.lower():
            # Converts to lowercase/uppercase
            if char in consonants_set:
                count += 1
        return count
            # Returns the result

    return min(lst, key=consonants)
        # Returns the result

lst = ["zzzzzzzzz", "yyyyyy", "bbb"]
print(number_of_consonants(lst))


"""
Problem: 486
Write a Python function that sorts a list of file names by their file extension using the key parameter.

def sort_files_by_extension(lst):
    # Function definition

    def file_extension(filename):
        # Function definition
        return filename.split('.')[-1]
            # Returns the result

    return sorted(lst, key=file_extension)
        # Sorts elements in ascending order

lst = ["document.txt", "photo.jpeg", "music.mp3", "video.mp4", "archive.zip"]

print(sort_files_by_extension(lst))

"""
Problem: 487
Write a Python function to sort a list of numbers by the square root of each number using the key parameter.

def sqaure_numbers_lst(lst):
    # Function definition

    def sqaure(n):
        # Function definition
        return n * n
            # Returns the result

    return sorted(lst, key=sqaure)
        # Sorts elements in ascending order

lst = [12, 46, 2, 10]
print(sqaure_numbers_lst(lst))

"""
Problem: 488
Write a Python function to sort a list of words by the number of distinct letters in each word using the key parameter.

def sort_words_by_distinct_letters(words):
    # Function definition

    def distinct_letter_count(word):
        # Function definition
        return len(set(word))
            # Returns the result

    return sorted(words, key=distinct_letter_count)
        # Sorts elements in ascending order

words = ["apple", "banana", "cherry", "orange"]
print(sort_words_by_distinct_letters(words))

"""
Problem: 489
Write a Python function that sorts a list of strings by the second letter in each string using the key parameter.

def sort_second_letter(lst):
    # Function definition

    def second_letter(x):
        # Function definition
        return x[1]
            # Returns the result

    return sorted(lst, key=second_letter)
        # Sorts elements in ascending order

lst = ["mountain", "law", "lebany"]
print(sort_second_letter(lst))

"""
Problem: 490
Write a Python function to sort a list of people by their age stored in a dictionary using the key parameter.

def people_age(dic):
    # Function definition

    def sort_age(person):
        # Function definition
        return dic[person]
            # Returns the result

    return sorted(dic, key=sort_age)
        # Sorts elements in ascending order

dic = {"Sam": 27, "Tom": 56, "Chantelle": 18}
print(people_age(dic))

"""
Problem: 491
Write a Python function that sorts a list of numbers by their binary representation using the key parameter.

def sort_by_binary_representation(lst):
    # Function definition

    def binary_representation(x):
        # Function definition
        return bin(x)
            # Returns the result

    return sorted(lst, key=binary_representation)
        # Sorts elements in ascending order

lst = [5, 3, 8, 1, 12]

print(sort_by_binary_representation(lst))

"""
Problem: 492
Write a Python function to find the person with the shortest name in a list of dictionaries using the min() function with the key parameter.

def sort_keys_by_value(dic):
    # Function definition

    def get_value(key):
        # Function definition
        return dic[key]
            # Returns the result

    return sorted(dic.keys(), key=get_value)
        # Sorts elements in ascending order

dic = {"Sam": 27, "Tommy": 56, "Chantelle": 18}
print(sort_keys_by_value(dic))

"""
Problem: 493
Write a Python function to sort a list of fractions by their decimal value using the key parameter.

from fractions import Fraction

def sort_fractions_by_decimal(fractions):
    # Function definition

    def decimal_value(fraction):
        # Function definition
        return float(fraction)
            # Returns the result

    return sorted(fractions, key=decimal_value)
        # Sorts elements in ascending order

fractions = [Fraction(1, 3), Fraction(3, 4), Fraction(2, 5), Fraction(7, 10)]

print(sort_fractions_by_decimal(fractions))

"""
Problem: 494
Write a Python function to find the longest string that ends with a specific letter using the max() function with the key parameter.

def longest_string_letter(lst, letter):
    # Function definition

    def longest_letter(s):
        # Function definition
        return len(s) if s.endswith(letter) else -1
            # Returns the result

    return max(lst, key=longest_letter)
        # Returns the result

lst = ["Jonathan", "Nathan", "Sarah", "Martha"]

print(longest_string_letter(lst, 'n'))
print(longest_string_letter(lst, 'a'))

def longest_string(string, letter):
    # Function definition

    words = string.split()
        # Splits string into list of words/elements

    def letter_ends(word):
        # Function definition
        if word.endswith(letter):
            return len(word)
                # Returns the result
        else:
            return 0
                # Returns the result

    longest = None
    max_length = 0

    for word in words:
        # Iterates through each element
        length = letter_ends(word)
        if length > max_length:
            max_length = length
            longest = word

    return longest
        # Returns the result

input_string = "Jonathan nathan Natas"
letter = "a"
print(longest_string(input_string, letter))

"""
Problem: 495
Create a base class Animal with a method speak() and a derived class Dog that overrides the speak() method to print “Bark”.

class Animal:
    def speak(self):
        # Function definition
        return "Animal sound"
            # Returns the result

class Dog(Animal):
    def speak(self):
        # Function definition
        return "Bark"
            # Returns the result

class Cat(Animal):
    def speak(self):
        # Function definition
        return "Meow"
            # Returns the result

dog = Dog()
cat = Cat()
print(dog.speak())
print(cat.speak())

"""
Problem: 496
Create a base class Vehicle with attributes speed and color. Create a derived class Car that adds the model attribute.

class Vehicle:
    def __init__(self, speed, color):
        # Function definition
        self.speed = speed
        self.color = color

class Car(Vehicle):
    def __init__(self, speed, color, model):
        # Function definition

        super().__init__(speed, color)

        self.model = model

my_car = Car(120, "Red", "Toyota")
print(f"Car Model: {my_car.model}, Speed: {my_car.speed}, Color: {my_car.color}")

"""
Problem: 497
Create a base class Person with a method introduce(). Create a derived class Student that overrides the introduce() method to include the student’s grade.
class Person:
    def __init__(self, name):
        # Function definition
        self.name = name

    def introduce(self):
        # Function definition
        return f"Hello, my name is {self.name}."
            # Returns the result

class Student(Person):
    def __init__(self, name, grade):
        # Function definition

        super().__init__(name)

        self.grade = grade

    def introduce(self):
        # Function definition
        return f"Hello, my name is {self.name} and I am in grade {self.grade}."
            # Returns the result

person = Person("Alice")
print(person.introduce())

student = Student("Bob", 10)
print(student.introduce())

"""
Problem: 498
Create a base class Shape with a method area(). Create a derived class Rectangle that calculates the area.

class Shape:
    def area(self):
        # Function definition

        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        # Function definition
        self.length = length
        self.width = width

    def area(self):
        # Function definition
        return self.length * self.width
            # Returns the result

rectangle = Rectangle(5, 3)
print(f"Area of the rectangle: {rectangle.area()}")

"""
Problem: 499
Create a base class Appliance with attributes brand and power. Create a derived class WashingMachine that adds a method wash_clothes().

class Appliance:
    def __init__(self, brand, power):
        # Function definition
        self.brand = brand
        self.power = power

class WashingMachine(Appliance):
    def __init__(self, brand, power):
        # Function definition
        super().__init__(brand, power)

    def wash_clothes(self):
        # Function definition
        return f"The {self.brand} washing machine is washing clothes with {self.power} watts of power."
            # Returns the result

washing_machine = WashingMachine("LG", 1500)
print(washing_machine.wash_clothes())

"""
Problem: 500
Create a base class Employee with attributes name and salary. Create a derived class Manager that adds a method assign_task().

class Employee:
    def __init__(self, name, salary):
        # Function definition
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary):
        # Function definition

        super().__init__(name, salary)

    def assign_task(self, task):
        # Function definition
        return f"Manager {self.name} has assigned the task: {task}."
            # Returns the result

manager = Manager("John Doe", 75000)
print(manager.assign_task("Prepare a project report"))




























