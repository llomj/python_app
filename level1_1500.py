

"""
Problem: 1001
Write a Python program to reverse a list using slicing.
"""

numbers = [1, 2, 3, 4, 5]
reversed_list = numbers[::-1]
print(reversed_list)  # Expected output: [5, 4, 3, 2, 1]


"""
Problem: 1002
Write a Python program to extract every third element from a list.
"""

numbers = [10, 20, 30, 40, 50, 60, 70, 80]
sliced_list = numbers[::3]
print(sliced_list)  # Expected output: [10, 40, 70]


"""
Problem: 1003
Write a Python program to extract every second character from a string in reverse order.
"""

text = "abcdefghij"
sliced_text = text[::-2]
print(sliced_text)  # Expected output: jhfdb


"""
Problem: 1004
Write a Python program to slice the middle three characters from a string with an odd length.
"""

text = "abcdefg"
middle_index = len(text) // 2
sliced_text = text[middle_index - 1: middle_index + 2]
print(sliced_text)  # Expected output: cde


"""
Problem: 1005
Write a Python program to remove the first and last characters from a string using slicing.
"""

text = "Python"
sliced_text = text[1:-1]
print(sliced_text)  # Expected output: ytho


"""
Problem: 1006
Write a Python program to get the first half of a string using slicing.
"""

text = "abcdefgh"
sliced_text = text[:len(text) // 2]
print(sliced_text)  # Expected output: abcd


"""
Problem: 1007
Write a Python program to get the second half of a string using slicing.
"""

text = "abcdefgh"
sliced_text = text[len(text) // 2:]
print(sliced_text)  # Expected output: efgh


"""
Problem: 1008
Write a Python program to extract the middle two characters from an even-length string.
"""

text = "abcdef"
middle_index = len(text) // 2
sliced_text = text[middle_index - 1: middle_index + 1]
print(sliced_text)  # Expected output: cd


"""
Problem: 1009
Write a Python program to remove the first three elements from a list using slicing.
"""

numbers = [1, 2, 3, 4, 5, 6]
sliced_list = numbers[3:]
print(sliced_list)  # Expected output: [4, 5, 6]


"""
Problem: 1010
Write a Python program to remove the last two elements from a tuple using slicing.
"""

numbers = (10, 20, 30, 40, 50)
sliced_tuple = numbers[:-2]
print(sliced_tuple)  # Expected output: (10, 20, 30)


"""
Problem: 1011
Write a Python program to slice every alternate element from a list.
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
sliced_list = numbers[::2]
print(sliced_list)  # Expected output: [1, 3, 5, 7]


"""
Problem: 1012
Write a Python program to extract a substring from index 3 to 7 using slicing.
"""

text = "PythonProgramming"
sliced_text = text[3:8]
print(sliced_text)  # Expected output: honPr


"""
Problem: 1013
Write a Python program to extract a tuple slice from index 2 to 5.
"""

numbers = (100, 200, 300, 400, 500, 600)
sliced_tuple = numbers[2:6]
print(sliced_tuple)  # Expected output: (300, 400, 500, 600)


"""
Problem: 1014
Write a Python program to check if a string is a palindrome using slicing.
"""

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))  # Expected output: True
print(is_palindrome("hello"))  # Expected output: False


"""
Problem: 1015
Write a Python program to extract the last three characters of a string using slicing.
"""

text = "Programming"
sliced_text = text[-3:]
print(sliced_text)  # Expected output: ing


"""
Problem: 1016
Write a Python program to extract the first five elements of a list using slicing.
"""

numbers = [10, 20, 30, 40, 50, 60, 70]
sliced_list = numbers[:5]
print(sliced_list)  # Expected output: [10, 20, 30, 40, 50]


"""
Problem: 1017
Write a Python program to extract all but the last three elements from a tuple using slicing.
"""

numbers = (5, 10, 15, 20, 25, 30, 35)
sliced_tuple = numbers[:-3]
print(sliced_tuple)  # Expected output: (5, 10, 15, 20)


"""
Problem: 1018
Write a Python program to extract a string without its first and last two characters.
"""

text = "HelloWorld"
sliced_text = text[2:-2]
print(sliced_text)  # Expected output: lloWor

"""
Problem: 1019
Write a Python program to create a list of squares of numbers from 1 to 10 using list comprehension.
"""

squares = [x ** 2 for x in range(1, 11)]
print(squares)  # Expected output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


"""
Problem: 1020
Write a Python program to create a list of even numbers from 1 to 20 using list comprehension.
"""

evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)  # Expected output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


"""
Problem: 1021
Write a Python program to create a list of numbers from 1 to 50 that are divisible by 5 using list comprehension.
"""

div_by_5 = [x for x in range(1, 51) if x % 5 == 0]
print(div_by_5)  # Expected output: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]


"""
Problem: 1022
Write a Python program to create a list of the first letter of each word in a given sentence using list comprehension.
"""

sentence = "Python is a powerful programming language"
first_letters = [word[0] for word in sentence.split()]
print(first_letters)  # Expected output: ['P', 'i', 'a', 'p', 'p', 'l']


"""
Problem: 1023
Write a Python program to create a list of words with more than three letters from a sentence using list comprehension.
"""

sentence = "The sun is bright today"
long_words = [word for word in sentence.split() if len(word) > 3]
print(long_words)  # Expected output: ['bright', 'today']


"""
Problem: 1024
Write a Python program to generate a list of tuples containing a number and its square for numbers from 1 to 10. List comprehension.
"""

squares_tuples = [(x, x**2) for x in range(1, 11)]
print(squares_tuples)  # Expected output: [(1, 1), (2, 4), ..., (10, 100)]


"""
Problem: 1025
Write a Python program to create a new list where every element from an existing list is doubled. List comprehension.
"""

numbers = [3, 5, 7, 9]
doubled = [x * 2 for x in numbers]
print(doubled)  # Expected output: [6, 10, 14, 18]


"""
Problem: 1026
Write a Python program to create a list of numbers from 1 to 100 that are either divisible by 3 or 7. List comprehension.
"""

div_by_3_or_7 = [x for x in range(1, 101) if x % 3 == 0 or x % 7 == 0]
print(div_by_3_or_7)


"""
Problem: 1027
Write a Python program to convert a list of strings to uppercase using list comprehension.
"""

words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(upper_words)  # Expected output: ['HELLO', 'WORLD', 'PYTHON']


"""
Problem: 1028
Write a Python program to flatten a nested list using list comprehension.
"""

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for sublist in nested_list for num in sublist]
print(flattened)  # Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9]


"""
Problem: 1029
Write a Python program to create a list of vowels from a given string using list comprehension.
"""

text = "List Comprehension is Powerful"
vowels = [char for char in text if char.lower() in "aeiou"]
print(vowels)  # Expected output: ['i', 'o', 'e', 'e', 'i', 'o', 'i', 'o', 'e']


"""
Problem: 1030
Write a Python program to extract only numeric values from a mixed list. List comprehension.
"""

mixed_list = [10, "apple", 15.5, "banana", 30, "42"]
numbers = [x for x in mixed_list if isinstance(x, (int, float))]
print(numbers)  # Expected output: [10, 15.5, 30]


"""
Problem: 1031
Write a Python program to generate a list of first 10 Fibonacci numbers using list comprehension.
"""

fib = [0, 1]
[fib.append(fib[-1] + fib[-2]) for _ in range(8)]
print(fib)  # Expected output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


"""
Problem: 1032
Write a Python program to create a list of prime numbers up to 50 using list comprehension.
"""

primes = [x for x in range(2, 51) if all(x % y != 0 for y in range(2, int(x**0.5) + 1))]
print(primes)


"""
Problem: 1033
Write a Python program to generate a list of all words in a sentence that end with a vowel. List comprehension.
"""

sentence = "The apple is on the tree"
vowel_ending_words = [word for word in sentence.split() if word[-1].lower() in "aeiou"]
print(vowel_ending_words)  # Expected output: ['The', 'apple', 'is', 'tree']


"""
Problem: 1034
Write a Python program to create a list of lowercase characters from a given string. List comprehension.
"""

text = "Python List Comprehension"
lower_chars = [char for char in text if char.islower()]
print(lower_chars)  # Expected output: ['y', 't', 'h', 'o', 'n', 'i', 's', 't', 'o', 'm', 'p', 'r', 'e', 'h', 'e', 'n', 's', 'i', 'o', 'n']


"""
Problem: 1035
Write a Python program to create a list of words with their lengths from a given sentence. List comprehension.
"""

sentence = "List comprehension makes Python concise"
word_lengths = [(word, len(word)) for word in sentence.split()]
print(word_lengths)  # Expected output: [('List', 4), ('comprehension', 13), ('makes', 5), ('Python', 6), ('concise', 7)]


"""
Problem: 1036
Write a Python program to remove duplicates from a list using list comprehension.
"""

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(dict.fromkeys(numbers))
print(unique_numbers)  # Expected output: [1, 2, 3, 4, 5]


"""
Problem: 1037
Write a Python program to filter words containing the letter 'p' from a given list. List comprehension.
"""

words = ["apple", "banana", "grape", "cherry", "peach"]
filtered_words = [word for word in words if "p" in word]
print(filtered_words)  # Expected output: ['apple', 'grape', 'peach']

"""
Problem: 1038
Write a Python recursive function to calculate the factorial of a given number.
"""

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

print(factorial(5))  # Expected output: 120


"""
Problem: 1039
Write a Python recursive function to calculate the sum of all numbers from 1 to n.
"""

def sum_n(n):
    return n if n == 1 else n + sum_n(n - 1)

print(sum_n(10))  # Expected output: 55


"""
Problem: 1040
Write a Python recursive function to compute the nth Fibonacci number.
"""

def fibonacci(n):
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # Expected output: 8


"""
Problem: 1041
Write a Python recursive function to reverse a string.
"""

def reverse_string(s):
    return s if len(s) == 0 else s[-1] + reverse_string(s[:-1])

print(reverse_string("hello"))  # Expected output: olleh


"""
Problem: 1042
Write a Python recursive function to count the number of digits in a given number.
"""

def count_digits(n):
    return 1 if n < 10 else 1 + count_digits(n // 10)

print(count_digits(12345))  # Expected output: 5


"""
Problem: 1043
Write a Python recursive function to find the greatest common divisor (GCD) of two numbers.
"""

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

print(gcd(48, 18))  # Expected output: 6


"""
Problem: 1044
Write a Python recursive function to find the sum of elements in a list.
"""

def list_sum(lst):
    return 0 if not lst else lst[0] + list_sum(lst[1:])

print(list_sum([1, 2, 3, 4, 5]))  # Expected output: 15


"""
Problem: 1045
Write a Python recursive function to check if a number is a palindrome.
"""

def is_palindrome(n, temp=None):
    if temp is None:
        temp = str(n)
    return True if len(temp) <= 1 else temp[0] == temp[-1] and is_palindrome(n, temp[1:-1])

print(is_palindrome(121))  # Expected output: True
print(is_palindrome(123))  # Expected output: False


"""
Problem: 1046
Write a Python recursive function to find the power of a number.
"""

def power(x, n):
    return 1 if n == 0 else x * power(x, n - 1)

print(power(2, 3))  # Expected output: 8


"""
Problem: 1047
Write a Python recursive function to compute the product of two numbers.
"""

def multiply(a, b):
    return 0 if b == 0 else a + multiply(a, b - 1)

print(multiply(5, 4))  # Expected output: 20


"""
Problem: 1048
Write a Python recursive function to print numbers from 1 to n.
"""

def print_numbers(n):
    if n > 0:
        print_numbers(n - 1)
        print(n)

print_numbers(5)  
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

def print_reverse(n):
    if n > 0:
        print(n)
        print_reverse(n - 1)

print_reverse(5)  
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

def is_sorted(lst):
    return True if len(lst) <= 1 else lst[0] <= lst[1] and is_sorted(lst[1:])

print(is_sorted([1, 2, 3, 4, 5]))  # Expected output: True
print(is_sorted([5, 3, 1]))  # Expected output: False


"""
Problem: 1051
Write a Python recursive function to count the occurrences of a character in a string.
"""

def char_count(s, c):
    return 0 if not s else (1 if s[0] == c else 0) + char_count(s[1:], c)

print(char_count("banana", "a"))  # Expected output: 3


"""
Problem: 1052
Write a Python recursive function to generate all binary strings of length n.
"""

def binary_strings(n, s=""):
    if n == 0:
        print(s)
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


"""
Problem: 1053
Write a Python recursive function to compute the sum of digits of a number.
"""

def sum_of_digits(n):
    if n == 0:
        return 0
    # Recursive case: add the last digit to the sum of the remaining digits
    else:
        return n % 10 + sum_of_digits(n // 10)

string = 1244
print(sum_of_digits(string))  # Output: 11

def sum_of_digits(n):
    return n if n < 10 else (n % 10) + sum_of_digits(n // 10)

print(sum_of_digits(1234))  # Expected output: 10


"""
Problem: 1054
Write a Python recursive function to calculate the nth triangular number.
"""

def triangular_number(n):
    return 0 if n == 0 else n + triangular_number(n - 1)

print(triangular_number(5))  # Expected output: 15


"""
Problem: 1055
Write a Python recursive function to remove duplicates from a string.
"""

def remove_duplicates(s, seen=""):
    return "" if not s else (remove_duplicates(s[1:], seen) if s[0] in seen else s[0] + remove_duplicates(s[1:], seen + s[0]))

print(remove_duplicates("banana"))  # Expected output: ban


"""
Problem: 1056
Write a Python recursive function to generate all permutations of a given string.
"""

def permutations(s, prefix=""):
    if not s:
        print(prefix)
    else:
        for i in range(len(s)):
            permutations(s[:i] + s[i+1:], prefix + s[i])

permutations("abc")  
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

def longest_string(words):
    return max(words, key=lambda word: len(word))

result = longest_string(["apple", "banana", "cherry"])
print(result)

"""
Problem: 1058
Write a Python program to check if a number is even using a lambda function.
"""

is_even = lambda x: x % 2 == 0

result = is_even(4)
print(result)

"""
Problem: 1059
Write a Python program to calculate the square root of all elements in a list using a lambda function.
"""

import math

def square_roots(numbers):
    return list(map(lambda x: math.sqrt(x), numbers))

result = square_roots([4, 9, 16])
print(result)

"""
Problem: 1060
Write a Python program to check if a string contains any digits using a lambda function.
"""

contains_digits = lambda s: any(map(str.isdigit, s))

result = contains_digits("hello123")
print(result)

"""
Problem: 1061
Write a Python program to sort a list of tuples based on the first element in descending order using a lambda expression.
"""

def sort_by_first_element_desc(tuples):
    return sorted(tuples, key=lambda x: x[0], reverse=True)

result = sort_by_first_element_desc([(3, "apple"), (1, "banana"), (2, "cherry")])
print(result)

"""
Problem: 1062
Write a Python program to filter out words that are shorter than a given length using the `filter()` function with a lambda expression.
"""

def filter_short_words(words, length):
    return list(filter(lambda word: len(word) >= length, words))

result = filter_short_words(["apple", "banana", "cherry", "date"], 6)
print(result)

"""
Problem: 1063
Write a Python program to double all elements in a list using a lambda function.
"""

def double_elements(numbers):
    return list(map(lambda x: x * 2, numbers))

result = double_elements([1, 2, 3, 4])
print(result)

"""
Problem: 1064
Write a Python program to check if a number is divisible by 3 using a lambda function.
"""

is_divisible_by_3 = lambda x: x % 3 == 0

result = is_divisible_by_3(9)
print(result)

"""
Problem: 1065
Write a Python program to find the second largest number in a list using a lambda function.
"""

second_largest = lambda numbers: sorted(set(numbers))[-2]

result = second_largest([10, 20, 30, 40, 50])
print(result)

"""
Problem: 1066
Write a Python program to map a list of numbers into their cubes using a lambda function.
"""

def cube_elements(numbers):
    return list(map(lambda x: x ** 3, numbers))

result = cube_elements([1, 2, 3, 4])
print(result)

"""
Problem: 1067
Write a Python program to sort a list of words by their lengths using the `sorted()` function with a lambda expression.
"""

def sort_by_length(words):
    return sorted(words, key=lambda word: len(word))

result = sort_by_length(["apple", "banana", "kiwi", "cherry"])
print(result)

"""
Problem: 1068
Write a Python program to check if a number is odd using a lambda function.
"""

is_odd = lambda x: x % 2 != 0

result = is_odd(5)
print(result)

"""
Problem: 1069
Write a Python program to find the sum of all elements in a list using the `reduce()` function with a lambda expression.
"""

from functools import reduce

def sum_of_elements(numbers):
    return reduce(lambda x, y: x + y, numbers)

result = sum_of_elements([1, 2, 3, 4])
print(result)

"""
Problem: 1070
Write a Python program to check if a string ends with a vowel using a lambda function.
"""

ends_with_vowel = lambda s: s[-1].lower() in 'aeiou'

result = ends_with_vowel("hello")
print(result)

"""
Problem: 1071
Write a Python program to find the smallest number in a list using the `min()` function with a lambda expression.
"""

# Define a list of numbers
numbers = [12, 45, 7, 23, 56, 89, 34]

# Use the min() function with a lambda expression to find the smallest number
smallest_number = min(numbers, key=lambda x: x)

# Print the result
print("The smallest number in the list is:", smallest_number)

"""
Problem: 1072
Write a Python program to check if a string contains only alphabetic characters using a lambda function.
"""

is_alpha = lambda s: s.isalpha()

result = is_alpha("hello")
print(result)

"""
Problem: 1073
Write a Python program to convert all integers in a list to strings using a lambda function.
"""

def convert_to_strings(numbers):
    return list(map(lambda x: str(x), numbers))

result = convert_to_strings([1, 2, 3, 4])
print(result)

"""
Problem: 1074
Write a Python program to find the sum of all even numbers in a list using a lambda expression.
"""

def sum_of_even(numbers):
    return sum(filter(lambda x: x % 2 == 0, numbers))

result = sum_of_even([1, 2, 3, 4, 5, 6])
print(result)

"""
Problem: 1075
Write a Python program to remove all whitespace from a string using a lambda function.
"""

string = "i'm going for a walk"
result = lambda char: char.replace(" ", "")

result(string)

remove_whitespace = lambda s: ''.join(s.split())

result = remove_whitespace("hello world")
print(result)

"""
Problem: 1076
Write a Python program to count the number of even numbers in a list using a lambda function.
"""

count_even = lambda numbers: len(list(filter(lambda x: x % 2 == 0, numbers)))

result = count_even([1, 2, 3, 4, 5, 6])
print(result)

"""
Problem: 1077
Write a Python program to find the product of all odd numbers in a list using a lambda function.
"""

from functools import reduce

product_of_odds = lambda numbers: reduce(lambda x, y: x * y, filter(lambda x: x % 2 != 0, numbers))

result = product_of_odds([1, 2, 3, 4, 5])
print(result)

"""
Problem: 1078
Write a Python program to check if a number is prime using a lambda function.
"""

is_prime = lambda n: all(n % i != 0 for i in range(2, int(n ** 0.5) + 1)) if n > 1 else False

result = is_prime(7)
print(result)

"""
Problem: 1079
Write a Python program to create a list of tuples (number, square root) for each number in a given list using a lambda function.
"""

import math

def create_square_root_tuples(numbers):
    return list(map(lambda x: (x, math.sqrt(x)), numbers))

result = create_square_root_tuples([4, 9, 16])
print(result)

"""
Problem: 1080
Write a Python program to check if a string contains any uppercase letters using a lambda function.
"""

contains_uppercase = lambda s: any(map(str.isupper, s))

result = contains_uppercase("Hello")
print(result)

"""
Problem: 1081
Write a Python program to find the average of odd numbers in a list using a lambda function.
"""

def average_of_odds(lst):
    odd = list(filter(lambda num: num % 2 !=0, lst))
    total = sum(odd)
    count = len(odd)
    average = total / count
    return average
lst = [1,2,3,4,5,6,7,8,9]

average_of_odds(lst)

def average_of_odds(numbers):
    odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
    return sum(odd_numbers) / len(odd_numbers) if odd_numbers else 0

result = average_of_odds([1, 2, 3, 4, 5])
print(result)

"""
Problem: 1082
Write a Python program to create a list of squares for all odd numbers in a list using a lambda function.
"""

def square_odd_numbers(numbers):
    return list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, numbers)))

result = square_odd_numbers([1, 2, 3, 4, 5])
print(result)

"""
Problem: 1083
Write a Python program to check if a list contains any negative numbers using a lambda function.
"""

contains_negative = lambda numbers: any(map(lambda x: x < 0, numbers))

result = contains_negative([1, -2, 3, 4])
print(result)

"""
Problem: 1084
Write a Python program to create a list of tuples where the first element is the original number and the second element is its cube using a lambda function.
"""

def create_cube_tuples(numbers):
    return list(map(lambda x: (x, x**3), numbers))

result = create_cube_tuples([1, 2, 3])
print(result)

"""
Problem: 1085
Write a Python program to filter out numbers greater than a given value using a lambda function.
"""

def filter_greater_than(numbers, value):
    return list(filter(lambda x: x <= value, numbers))

result = filter_greater_than([1, 2, 3, 4, 5], 3)
print(result)

"""
Problem: 1086
Write a Python program to convert a list of strings to their lengths using a lambda function.
"""

def convert_to_lengths(strings):
    return list(map(lambda x: len(x), strings))

result = convert_to_lengths(["apple", "banana", "cherry"])
print(result)

"""
Problem: 1087
Write a Python program to check if a number is a perfect square using a lambda function.
"""

is_perfect_square = lambda x: int(x**0.5) ** 2 == x

result = is_perfect_square(16)
print(result)

"""
Problem: 1088
Write a Python program to find the sum of the cubes of all numbers in a list using a lambda function.
"""

def sum_of_cubes(numbers):
    return sum(map(lambda x: x**3, numbers))

result = sum_of_cubes([1, 2, 3])
print(result)

"""
Problem: 1089
Write a Python program to remove all elements greater than a specific value in a list using a lambda function.
"""

def remove_elements_greater_than(numbers, value):
    return list(filter(lambda x: x <= value, numbers))

result = remove_elements_greater_than([1, 2, 3, 4, 5], 3)
print(result)

"""
Problem: 1090
Write a Python program to check if all elements in a list are positive using a lambda function.
"""

all_positive = lambda numbers: all(map(lambda x: x > 0, numbers))

result = all_positive([1, 2, 3, 4])
print(result)

"""
Problem: 1091
Write a Python program to create a generator that yields the square of each number in a given range.
"""

def square_generator(n):
    for i in range(n):
        yield i**2

result = list(square_generator(5))
print(result)

"""
Problem: 1092
Write a Python program to create a generator that yields Fibonacci numbers up to a given number.
"""

def fibonacci_generator(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

result = list(fibonacci_generator(20))
print(result)

"""
Problem: 1093
Write a Python program to create a generator that yields the characters of a string one by one.
"""

def char_generator(s):
    for char in s:
        yield char

result = list(char_generator("hello"))
print(result)

"""
Problem: 1094
Write a Python program to create a generator that yields numbers from 1 to n with a step of 2.
"""

def step_generator(n):
    for i in range(1, n, 2):
        yield i

result = list(step_generator(10))
print(result)

"""
Problem: 1095
Write a Python program to create a generator that yields even numbers from 1 to n.
"""

def even_number_generator(n):
    for i in range(2, n+1, 2):
        yield i

result = list(even_number_generator(10))
print(result)

"""
Problem: 1096
Write a Python program to create a generator that yields squares of even numbers from 1 to n.
"""

def square_even_generator(n):
    for i in range(2, n+1, 2):
        yield i**2

result = list(square_even_generator(10))
print(result)

"""
Problem: 1097
Write a Python program to create a generator that yields the first n prime numbers.
"""

def prime_generator(n):
    primes = []
    num = 2
    while len(primes) < n:
        if all(num % p != 0 for p in primes):
            primes.append(num)
        num += 1
    yield from primes

result = list(prime_generator(5))
print(result)

"""
Problem: 1098
Write a Python program to create a generator that yields the sum of consecutive pairs from a given list.
"""

def consecutive_pair_sum(lst):
    for i in range(len(lst)-1):
        yield lst[i] + lst[i+1]

result = list(consecutive_pair_sum([1, 2, 3, 4, 5]))
print(result)

"""
Problem: 1099
Write a Python program to create a generator that yields the factorial of each number from 1 to n.
"""

def factorial_generator(n):
    def factorial(x):
        result = 1
        for i in range(1, x+1):
            result *= i
        return result
    for i in range(1, n+1):
        yield factorial(i)

result = list(factorial_generator(5))
print(result)

"""
Problem: 1100
Write a Python program to create a generator that yields numbers divisible by 3 and 5 from 1 to n.
"""

def divisible_by_3_and_5_generator(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            yield i

result = list(divisible_by_3_and_5_generator(50))
print(result)

"""
Problem: 1101
Write a Python program to create a generator that filters out the odd numbers from a list.
"""

def odd_filter_generator(lst):
    for num in lst:
        if num % 2 == 0:
            yield num

result = list(odd_filter_generator([1, 2, 3, 4, 5, 6]))
print(result)

"""
Problem: 1102
Write a Python program to create a generator that yields the cumulative sum of a given list of numbers.
"""

def cumulative_sum_generator(lst):
    total = 0
    for num in lst:
        total += num
        yield total

result = list(cumulative_sum_generator([1, 2, 3, 4, 5]))
print(result)

"""
Problem: 1103
Write a Python program to create a generator that yields the n-th power of each number from 1 to n.
"""

def power_generator(n, power):
    for i in range(1, n+1):
        yield i**power

result = list(power_generator(5, 3))
print(result)

"""
Problem: 1104
Write a Python program to create a generator that yields each word in a sentence.
"""

def word_generator(sentence):
    words = sentence.split()
    for word in words:
        yield word

result = list(word_generator("This is a test sentence"))
print(result)

"""
Problem: 1105
Write a Python program to create a generator that yields numbers that are squares of integers up to n.
"""

def square_number_generator(n):
    for i in range(1, n+1):
        yield i**2

result = list(square_number_generator(5))
print(result)

"""
Problem: 1106
Write a Python program to create a generator that yields the squares of odd numbers from 1 to n.
"""

def main(n):
    for num in range(1, n+1):
        if num % 2 != 0:
            yield num ** 2

n = 10
result = list(main(n))
print(result)

def square_odd_number_generator(n):
    for i in range(1, n+1, 2):
        yield i**2

result = list(square_odd_number_generator(10))
print(result)

"""
Problem: 1107
Write a Python program to create a generator that yields the elements of a given list in reverse order.
"""

def reverse_list_generator(lst):
    for i in range(len(lst)-1, -1, -1):
        yield lst[i]

result = list(reverse_list_generator([1, 2, 3, 4, 5]))
print(result)

"""
Problem: 1108
Write a Python program to create a generator that yields multiples of a given number up to n.
"""

def multiple_generator(n, multiple):
    for i in range(multiple, n+1, multiple):
        yield i

result = list(multiple_generator(20, 3))
print(result)

"""
Problem: 1109
Write a Python program to create a generator that yields all the uppercase letters in a string.
"""

def uppercase_generator(s):
    for char in s:
        if char.isupper():
            yield char

result = list(uppercase_generator("Hello World"))
print(result)

"""
Problem: 1110
Write a Python program to create a generator that yields the differences between consecutive elements of a list.
"""

def consecutive_diff_generator(lst):
    for i in range(len(lst)-1):
        yield lst[i+1] - lst[i]

result = list(consecutive_diff_generator([1, 3, 6, 10]))
print(result)

"""
Problem: 1111
Write a Python program to create a generator that yields numbers greater than a given value in a list.
"""

def greater_than_generator(lst, value):
    for num in lst:
        if num > value:
            yield num

result = list(greater_than_generator([1, 2, 3, 4, 5, 6], 3))
print(result)

"""
Problem: 1112
Write a Python program to create a generator that yields the sum of each element with its index from a list.
"""

def sum_with_index_generator(lst):
    for index, num in enumerate(lst):
        yield num + index

result = list(sum_with_index_generator([10, 20, 30, 40]))
print(result)

"""
Problem: 1113
Write a Python program to create a generator that yields all palindromes from a list of strings. 
"""

def palindrome_generator(lst):
    for word in lst:
        if word == word[::-1]:
            yield word

result = list(palindrome_generator(["madam", "apple", "racecar", "banana"]))
print(result)

"""
Problem: 1114
Write a Python program to create a generator that yields the product of elements in pairs from a given list.
"""

def pair_product_generator(lst):
    for i in range(len(lst)-1):
        yield lst[i] * lst[i+1]

result = list(pair_product_generator([1, 2, 3, 4]))
print(result)

"""
Problem: 1115
Write a Python program to create a generator that yields elements from a list that are greater than the previous element. 
"""

def greater_than_previous_generator(lst):
    for i in range(1, len(lst)):
        if lst[i] > lst[i-1]:
            yield lst[i]

result = list(greater_than_previous_generator([1, 2, 1, 4, 3]))
print(result)

"""
Problem: 1116
Write a Python program to create a generator that yields all numbers in a list that are divisible by a given number.
"""

def divisible_by_generator(lst, divisor):
    for num in lst:
        if num % divisor == 0:
            yield num

result = list(divisible_by_generator([10, 15, 20, 25, 30], 5))
print(result)

"""
Problem: 1117
Write a Python program to create a generator that yields the first n even Fibonacci numbers.
"""

def even_fibonacci_generator(n):
    a, b = 0, 2
    count = 0
    while count < n:
        yield a
        a, b = b, 4 * b + a
        count += 1

result = list(even_fibonacci_generator(5))
print(result)

"""
Problem: 1118
Write a Python program to create a generator that yields all the even-indexed elements of a list.
"""

def even_index_generator(lst):
    for i in range(0, len(lst), 2):
        yield lst[i]

result = list(even_index_generator([1, 2, 3, 4, 5, 6]))
print(result)

"""
Problem: 1119
Write a Python program to create a generator that yields each word in a sentence, but only those with an even number of characters. 
"""

def even_length_word_generator(sentence):
    words = sentence.split()
    for word in words:
        if len(word) % 2 == 0:
            yield word

result = list(even_length_word_generator("This is a simple test sentence"))
print(result)

"""
Problem: 1120
Write a Python program to check if a number is positive, negative, or zero. Control flow.
"""

def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

result = check_number(5)
print(result)

"""
Problem: 1121
Write a Python program to find the largest of three numbers. Control flow.
"""

def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

result = largest_of_three(10, 20, 15)
print(result)

"""
Problem: 1122
Write a Python program to check if a given year is a leap year. Control flow.
"""

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

result = is_leap_year(2024)
print(result)

"""
Problem: 1123
Write a Python program to check if a number is even or odd. Control flow.
"""

def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

result = check_even_odd(7)
print(result)

"""
Problem: 1124
Write a Python program to check if a number is divisible by both 3 and 5. Control flow.
"""

def divisible_by_3_and_5(n):
    if n % 3 == 0 and n % 5 == 0:
        return True
    else:
        return False

result = divisible_by_3_and_5(15)
print(result)

"""
Problem: 1125
Write a Python program to print all numbers from 1 to n that are divisible by 7. Control flow.
"""

def divisible_by_7(n):
    for i in range(1, n+1):
        if i % 7 == 0:
            print(i)

divisible_by_7(50)

"""
Problem: 1126
Write a Python program to check if a given number is a prime number. Control flow.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

result = is_prime(11)
print(result)

"""
Problem: 1127
Write a Python program to find the factorial of a number using recursion. Control flow.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

result = factorial(5)
print(result)

"""
Problem: 1128
Write a Python program to check if a string is a palindrome. Control flow.
"""

def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

result = is_palindrome("madam")
print(result)

"""
Problem: 1129
Write a Python program to count the number of vowels in a given string. Control flow.
"""

def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s:
        if char.lower() in vowels:
            count += 1
    return count

result = count_vowels("Hello World")
print(result)

"""
Problem: 1130
Write a Python program to check if a number is a perfect number. Control flow.
"""

def is_perfect_number(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    if sum(divisors) == n:
        return True
    else:
        return False

result = is_perfect_number(6)
print(result)

"""
Problem: 1131
Write a Python program to check if a number is Armstrong number. Control flow.
"""

def is_armstrong(n):
    num_str = str(n)
    length = len(num_str)
    total = sum(int(digit) ** length for digit in num_str)
    if total == n:
        return True
    else:
        return False

result = is_armstrong(153)
print(result)

"""
Problem: 1132
Write a Python program to print all the prime numbers less than or equal to n. Control flow.
"""

def prime_numbers_up_to_n(n):
    primes = []
    for num in range(2, n+1):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            primes.append(num)
    return primes

result = prime_numbers_up_to_n(20)
print(result)

"""
Problem: 1133
Write a Python program to check if a number is an even number and greater than 10. Control flow.
"""

def even_and_greater_than_10(n):
    if n % 2 == 0 and n > 10:
        return True
    else:
        return False

result = even_and_greater_than_10(12)
print(result)

"""
Problem: 1134
Write a Python program to find all the divisors of a number. Control flow.
"""

n = 20

for i in range(1, n + 1):
    if n % i == 0:
        print(i)

def find_divisors(n):
    divisors = [i for i in range(1, n+1) if n % i == 0]
    return divisors

result = find_divisors(12)
print(result)

"""
Problem: 1135
Write a Python program to print the multiplication table of a number up to 10. Control flow.
"""

def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

multiplication_table(7)

"""
Problem: 1136
Write a Python program to check if a number is a perfect square. Control flow.
"""

def is_perfect_square(n):
    return int(n**0.5) ** 2 == n

result = is_perfect_square(25)
print(result)

"""
Problem: 1137
Write a Python program to check if a number is a power of 2. Control flow.
"""

def is_power_of_2(n):
    return n > 0 and (n & (n - 1)) == 0

result = is_power_of_2(16)
print(result)

"""
Problem: 1138
Write a Python program to find the second largest number in a list. Control flow.
"""

def second_largest(lst):
    lst = sorted(set(lst), reverse=True)
    return lst[1] if len(lst) > 1 else None

result = second_largest([10, 20, 4, 45, 99])
print(result)

"""
Problem: 1139
Write a Python program to check if a given number is a power of 3. Control flow.
"""

def is_power_of_3(n):
    while n % 3 == 0 and n > 0:
        n //= 3
    return n == 1

result = is_power_of_3(27)
print(result)

"""
Problem: 1140
Write a Python program to print Fibonacci numbers up to n. Control flow.
"""

def fibonacci_up_to_n(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b

fibonacci_up_to_n(20)

"""
Problem: 1141
Write a Python program to count the occurrences of a specific element in a list. Control flow.
"""

def count_occurrences(lst, element):
    return lst.count(element)

result = count_occurrences([1, 2, 2, 3, 4, 2], 2)
print(result)

"""
Problem: 1142
Write a Python program to check if a given number is a perfect square and an Armstrong number. Control flow.
"""

def is_perfect_square_and_armstrong(n):
    if is_perfect_square(n) and is_armstrong(n):
        return True
    else:
        return False

result = is_perfect_square_and_armstrong(153)
print(result)

"""
Problem: 1143
Write a Python program to find all numbers in a given range that are divisible by 7 and 11. Control flow.
"""

def divisible_by_7_and_11(start, end):
    return [num for num in range(start, end+1) if num % 7 == 0 and num % 11 == 0]

result = divisible_by_7_and_11(1, 100)
print(result)

"""
Problem: 1144
Write a Python program to print the factorial of a number using a while loop. Control flow.
"""

def factorial_while(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

result = factorial_while(5)
print(result)

"""
Problem: 1145
Write a Python program to print a list of numbers in reverse order. Control flow.
"""

def reverse_list(lst):
    return lst[::-1]

result = reverse_list([1, 2, 3, 4, 5])
print(result)

"""
Problem: 1146
Write a Python program to check if a number is divisible by 5 or 10. Control flow.
"""

def divisible_by_5_or_10(n):
    if n % 5 == 0 or n % 10 == 0:
        return True
    else:
        return False

result = divisible_by_5_or_10(50)
print(result)

"""
Problem: 1147
Write a Python program to check if a number is divisible by any number in a given list. Control flow.
"""

def divisible_by_any_number(n, lst):
    for num in lst:
        if n % num == 0:
            return True
    return False

result = divisible_by_any_number(10, [3, 5, 7])
print(result)

"""
Problem: 1148
Write a Python program to demonstrate variable scope in a function. Scope.
"""

def outer_function():
    x = 10  # Local variable
    def inner_function():
        print(x)  # Accessing the outer function's variable
    inner_function()

outer_function()

"""
Problem: 1149
Write a Python program to show the difference between global and local variables. Scope.
"""

x = 20  # Global variable

def test_scope():
    x = 10  # Local variable
    print(f"Local variable: {x}")

test_scope()
print(f"Global variable: {x}")

"""
Problem: 1150
Write a Python program to demonstrate the use of the `global` keyword. Scope.
"""

def modify_global_variable():
    global x
    x = 30  # Modifies the global variable

x = 10
modify_global_variable()
print(x)

"""
Problem: 1151
Write a Python program to demonstrate the use of `nonlocal` keyword. Scope.
"""

def outer_function():
    x = 10
    def inner_function():
        nonlocal x
        x = 20  # Modifies the variable in the outer function's scope
    inner_function()
    print(x)

outer_function()

"""
Problem: 1152
Write a Python program to demonstrate variable shadowing. Scope.
"""

x = 100  # Global variable

def shadowing_example():
    x = 50  # Local variable, shadows the global variable
    print(f"Local x: {x}")

shadowing_example()
print(f"Global x: {x}")

"""
Problem: 1153
Write a Python program to demonstrate the use of function arguments as local variables. Scope.
"""

def example_function(a, b):
    c = a + b  # c is a local variable
    print(f"The sum of {a} and {b} is {c}")

example_function(5, 7)

"""
Problem: 1154
Write a Python program to demonstrate how to pass a variable as a default argument. Scope.
"""

def greet(name="John"):
    print(f"Hello, {name}!")

greet()  # Uses default value
greet("Alice")  # Uses passed argument

"""
Problem: 1155
Write a Python program to show the use of mutable and immutable types in functions. Scope.
"""

def modify_list(lst):
    lst.append(4)  # List is mutable, so it is modified
    print(f"Modified list: {lst}")

my_list = [1, 2, 3]
modify_list(my_list)
print(f"Original list: {my_list}")

def modify_integer(n):
    n += 1  # Integer is immutable, so it cannot be modified
    print(f"Modified integer: {n}")

my_int = 5
modify_integer(my_int)
print(f"Original integer: {my_int}")

"""
Problem: 1156
Write a Python program to demonstrate the scope of variables in a loop. Scope.
"""

def loop_scope():
    for i in range(3):
        x = i
        print(f"Inside loop: {x}")
    # x is accessible here after the loop ends
    print(f"Outside loop: {x}")

loop_scope()

"""
Problem: 1157
Write a Python program to check if a variable is defined. Scope.
"""

def check_variable():
    try:
        print(x)
    except NameError:
        print("x is not defined")

check_variable()

"""
Problem: 1158
Write a Python program to demonstrate the scope of variables in nested functions. Scope.
"""

def outer_function():
    x = 10  # Local variable in outer function
    def inner_function():
        y = 20  # Local variable in inner function
        print(f"Inner function: x = {x}, y = {y}")
    inner_function()
    print(f"Outer function: x = {x}")

outer_function()

"""
Problem: 1159
Write a Python program to demonstrate how to return a variable from a function. Scope.
"""

def add_numbers(a, b):
    sum_result = a + b
    return sum_result

result = add_numbers(3, 5)
print(f"The sum is {result}")

"""
Problem: 1160
Write a Python program to explain how default mutable arguments work in functions. Scope.
"""

def append_to_list(n, default_list=[]):
    default_list.append(n)
    return default_list

# Test the function
print(append_to_list(1))  # [1]
print(append_to_list(2))  # [1, 2]
print(append_to_list(3))  # [1, 2, 3]


def append_to_list(lst=None):
    if lst is None:
        lst = []
    lst.append(1)
    return lst

print(append_to_list())  # Returns [1]
print(append_to_list())  # Returns [1], new list is created each time

"""
Problem: 1161
Write a Python program to demonstrate the use of variables in list comprehensions. Scope.
"""

def square_numbers(lst):
    return [x**2 for x in lst]

numbers = [1, 2, 3, 4]
result = square_numbers(numbers)
print(f"Squares: {result}")

"""
Problem: 1162
Write a Python program to show the effect of reusing the same variable in a function. Scope.
"""

def reuse_variable():
    x = 5
    x = x * 2  # Reuses the variable
    print(f"New value of x: {x}")

reuse_variable()

"""
Problem: 1163
Write a Python program to demonstrate variable scope in different functions. Scope.
"""

x = 50  # Global variable

def function_one():
    print(f"Function One: {x}")

def function_two():
    x = 40
    print(f"Function Two: {x}")

function_one()
function_two()

"""
Problem: 1164
Write a Python program to demonstrate the use of `global` for modifying variables in different functions. Scope.
"""

x = 10  # Global variable

def function_one():
    global x
    x += 5

def function_two():
    global x
    x -= 3

function_one()
function_two()
print(f"Global variable x: {x}")

"""
Problem: 1165
Write a Python program to show how variable values are changed in nested functions. Scope.
"""

def outer_function():
    x = 15  # Local variable in outer function
    def inner_function():
        nonlocal x
        x += 10  # Modifies x in the outer function's scope
        print(f"Inner function: x = {x}")
    inner_function()
    print(f"Outer function: x = {x}")

outer_function()

"""
Problem: 1166
Write a Python program to demonstrate the use of variable arguments in functions. Scope.
"""

def print_arguments(*args):
    for arg in args:
        print(arg)

print_arguments(1, 2, 3, "hello", [1, 2, 3])

"""
Problem: 1167
Write a Python program to show how the scope of a variable changes in a for loop. Scope.

"""

def loop_variable_scope():
    for i in range(3):
        y = i  # Local variable in the loop
        print(f"In the loop: y = {y}")
    print(f"After the loop: y = {y}")  # y still exists outside the loop

loop_variable_scope()

"""
Problem: 1168
Write a Python program to show the behavior of variables in global scope inside functions. Scope.
"""

def global_inside_function():
    print(f"Global variable x inside function: {x}")

x = 10  # Global variable
global_inside_function()

"""
Problem: 1169
Write a Python program to explain the difference between mutable and immutable variables in terms of scope. Scope.
"""

def test_mutability():
    mutable = [1, 2, 3]  # Mutable variable (list)
    immutable = 10  # Immutable variable (integer)
    
    mutable[0] = 100  # Modifies the mutable variable
    immutable = 20  # This does not change the original variable
    
    print(f"Mutable variable: {mutable}")
    print(f"Immutable variable: {immutable}")

test_mutability()

"""
Problem: 1170
Write a Python program to show the behavior of variables declared in a list comprehension. Scope.
"""

def list_comprehension_variable_scope():
    lst = [x**2 for x in range(5)]
    print(f"List comprehension result: {lst}")

list_comprehension_variable_scope()

"""
Problem: 1171
Write a Python program to show that function arguments can be variables with different scopes. Scope.
"""

def print_variable_in_function(x):
    y = x * 2  # Local variable inside function
    print(f"Function variable y: {y}")

z = 10  # Global variable
print_variable_in_function(z)

"""
Problem: 1172
Write a Python program to show that a variable in a for loop can be accessed outside the loop. Scope.
"""

def for_loop_variable_scope():
    for i in range(3):
        x = i
        print(f"In the loop: x = {x}")
    print(f"Outside the loop: x = {x}")

for_loop_variable_scope()

"""
Problem: 1173
Write a Python program to demonstrate the impact of changing a global variable inside a function. Scope.
"""

x = 100

def change_global_variable():
    global x
    x = 50

change_global_variable()
print(f"Global x after modification: {x}")

"""
Problem: 1174
Write a Python program to demonstrate variable accessibility within different levels of nested functions. Scope.
"""

def outer_function():
    x = 5
    def middle_function():
        y = 10
        def inner_function():
            z = 15
            print(f"Inner function: x = {x}, y = {y}, z = {z}")
        inner_function()
    middle_function()

outer_function()

"""
Problem: 1175
Write a Python program to demonstrate how function arguments can access global variables. Scope.
"""

x = 100

def print_global_variable(x):
    print(f"Global x inside function: {x}")

print_global_variable(x)

"""
Problem: 1176
Write a Python program to demonstrate the scope of variables in a recursive function. Scope.
"""

def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

result = factorial_recursive(5)
print(f"Factorial: {result}")

"""
Problem: 1177
Write a Python program to import the `math` module and calculate the square root of a number. Module.
"""

import math

def calculate_square_root(number):
    return math.sqrt(number)

result = calculate_square_root(16)
print(f"The square root of 16 is {result}")

"""
Problem: 1178
Write a Python program to use the `random` module to generate a random number between 1 and 100. Module.
"""

import random

def generate_random_number():
    return random.randint(1, 100)

random_number = generate_random_number()
print(f"Random number between 1 and 100: {random_number}")

"""
Problem: 1179
Write a Python program to use the `datetime` module to get the current date and time. Module.
"""

import datetime

def current_datetime():
    return datetime.datetime.now()

now = current_datetime()
print(f"Current date and time: {now}")

"""
Problem: 1180
Write a Python program to use the `os` module to get the current working directory. Module.
"""

import os

def current_working_directory():
    return os.getcwd()

cwd = current_working_directory()
print(f"Current working directory: {cwd}")

"""
Problem: 1181
Write a Python program to use the `sys` module to get the Python version. Module.
"""

import sys

def python_version():
    return sys.version

version = python_version()
print(f"Python version: {version}")

"""
Problem: 1182
Write a Python program to use the `json` module to convert a Python dictionary to a JSON string. Module.
"""

import json

def dict_to_json():
    sample_dict = {"name": "Alice", "age": 30}
    return json.dumps(sample_dict)

json_str = dict_to_json()
print(f"JSON string: {json_str}")

"""
Problem: 1183
Write a Python program to use the `re` module to check if a string contains a number. Module.
"""

import re

def contains_number(string):
    return bool(re.search(r'\d', string))

result = contains_number("Hello123")
print(f"Does the string contain a number? {result}")

"""
Problem: 1184
Write a Python program to use the `os` module to list all files in a directory. Module.
"""

import os

def list_files(directory):
    return os.listdir(directory)

files = list_files(".")
print(f"Files in the current directory: {files}")

"""
Problem: 1185
Write a Python program to use the `math` module to calculate the factorial of a number. Module.
"""

import math

def calculate_factorial(number):
    return math.factorial(number)

factorial_result = calculate_factorial(5)
print(f"The factorial of 5 is {factorial_result}")

"""
Problem: 1186
Write a Python program to use the `time` module to measure the execution time of a block of code. Module.
"""

import time

def measure_time():
    start_time = time.time()
    sum(range(1000000))
    end_time = time.time()
    return end_time - start_time

execution_time = measure_time()
print(f"Execution time: {execution_time} seconds")

"""
Problem: 1187
Write a Python program to use the `calendar` module to check if a year is a leap year. Module.
"""

import calendar

def is_leap_year(year):
    return calendar.isleap(year)

result = is_leap_year(2024)
print(f"Is 2024 a leap year? {result}")

"""
Problem: 1188
Write a Python program to use the `math` module to find the value of pi. Module.
"""

import math

def get_pi_value():
    return math.pi

pi_value = get_pi_value()
print(f"The value of pi is {pi_value}")

"""
Problem: 1189
Write a Python program to use the `random` module to shuffle a list of numbers. Module.
"""

import random

def shuffle_list(lst):
    random.shuffle(lst)
    return lst

numbers = [1, 2, 3, 4, 5]
shuffled_numbers = shuffle_list(numbers)
print(f"Shuffled list: {shuffled_numbers}")

"""
Problem: 1190
Write a Python program to use the `collections` module to count the occurrences of elements in a list. Module.
"""

import collections

def count_occurrences(lst):
    return collections.Counter(lst)

numbers = [1, 2, 2, 3, 3, 3]
occurrences = count_occurrences(numbers)
print(f"Occurrences: {occurrences}")

"""
Problem: 1191
Write a Python program to use the `math` module to calculate the greatest common divisor (GCD) of two numbers. Module.
"""

import math

def calculate_gcd(a, b):
    return math.gcd(a, b)

gcd_result = calculate_gcd(48, 180)
print(f"The GCD of 48 and 180 is {gcd_result}")

"""
Problem: 1192
Write a Python program to use the `os` module to rename a file. Module.
"""

import os

def rename_file(old_name, new_name):
    os.rename(old_name, new_name)

# Uncomment the following lines to test the rename_file function:
rename_file("old_file.txt", "new_file.txt")

"""
Problem: 1193
Write a Python program to use the `datetime` module to format the current date. Module.
"""

import datetime

def format_current_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")

formatted_date = format_current_date()
print(f"Formatted current date: {formatted_date}")

"""
Problem: 1194
Write a Python program to use the `json` module to parse a JSON string into a Python dictionary. Module.
"""

import json

def json_to_dict(json_str):
    return json.loads(json_str)

json_str = '{"name": "Bob", "age": 25}'
parsed_dict = json_to_dict(json_str)
print(f"Parsed dictionary: {parsed_dict}")

"""
Problem: 1195
Write a Python program to use the `random` module to select a random element from a list. Module.
"""

import random

def select_random_element(lst):
    return random.choice(lst)

elements = [10, 20, 30, 40]
random_element = select_random_element(elements)
print(f"Random element: {random_element}")

"""
Problem: 1196
Write a Python program to use the `math` module to round a floating-point number to the nearest integer. Module.
"""

import math

def round_number(number):
    return round(number)

rounded_value = round_number(7.5)
print(f"Rounded value of 7.5: {rounded_value}")

"""
Problem: 1197
Write a Python program to create a dictionary and access its value using a key. Dictionary operations.
"""

def access_value():
    sample_dict = {"name": "Alice", "age": 30}
    return sample_dict["name"]

result = access_value()
print(f"Value accessed: {result}")

"""
Problem: 1198
Write a Python program to add a key-value pair to an existing dictionary. Dictionary operations.
"""

def add_key_value():
    sample_dict = {"name": "Alice", "age": 30}
    sample_dict["city"] = "New York"
    return sample_dict

updated_dict = add_key_value()
print(f"Updated dictionary: {updated_dict}")

"""
Problem: 1199
Write a Python program to remove a key-value pair from a dictionary. Dictionary operations.
"""

def remove_key():
    sample_dict = {"name": "Alice", "age": 30, "city": "New York"}
    del sample_dict["city"]
    return sample_dict

updated_dict = remove_key()
print(f"Dictionary after removal: {updated_dict}")

"""
Problem: 1200
Write a Python program to get all the keys from a dictionary. Dictionary operations.
"""

def get_keys():
    sample_dict = {"name": "Alice", "age": 30, "city": "New York"}
    return sample_dict.keys()

keys = get_keys()
print(f"Keys in dictionary: {keys}")

"""
Problem: 1201
Write a Python program to get all the values from a dictionary. Dictionary operations.
"""

def get_values():
    sample_dict = {"name": "Alice", "age": 30, "city": "New York"}
    return sample_dict.values()

values = get_values()
print(f"Values in dictionary: {values}")

"""
Problem: 1202
Write a Python program to check if a key exists in a dictionary. Dictionary operations.
"""

def check_key():
    sample_dict = {"name": "Alice", "age": 30, "city": "New York"}
    return "age" in sample_dict

result = check_key()
print(f"Key exists: {result}")

"""
Problem: 1203
Write a Python program to get the value associated with a key, or return a default value if the key doesn't exist. Dictionary operations.
"""

def get_value(dictionary, key, default=None):
    
    return dictionary.get(key, default)

# Example usage:
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(get_value(my_dict, 'a'))  # Output: 1
print(get_value(my_dict, 'd', 'not found'))  # Output: not found

def get_value_or_default():
    sample_dict = {"name": "Alice", "age": 30}
    return sample_dict.get("city", "Unknown")

result = get_value_or_default()
print(f"Value: {result}")

"""
Problem: 1204
Write a Python program to clear all items from a dictionary. Dictionary operations.
"""

def clear_dict():
    sample_dict = {"name": "Alice", "age": 30, "city": "New York"}
    sample_dict.clear()
    return sample_dict

updated_dict = clear_dict()
print(f"Dictionary after clearing: {updated_dict}")

"""
Problem: 1205
Write a Python program to copy a dictionary. Dictionary operations.
"""

def copy_dict():
    sample_dict = {"name": "Alice", "age": 30}
    return sample_dict.copy()

copied_dict = copy_dict()
print(f"Copied dictionary: {copied_dict}")

"""
Problem: 1206
Write a Python program to merge two dictionaries. Dictionary operations.
"""

def merge_dicts():
    dict1 = {"name": "Alice", "age": 30}
    dict2 = {"city": "New York", "job": "Engineer"}
    dict1.update(dict2)
    return dict1

merged_dict = merge_dicts()
print(f"Merged dictionary: {merged_dict}")

"""
Problem: 1207
Write a Python program to iterate through all key-value pairs in a dictionary. Dictionary operations.
"""

def iterate_dict():
    sample_dict = {"name": "Alice", "age": 30, "city": "New York"}
    for key, value in sample_dict.items():
        print(f"{key}: {value}")

iterate_dict()

"""
Problem: 1208
Write a Python program to find the length of a dictionary. Dictionary operations.
"""

def dict_length():
    sample_dict = {"name": "Alice", "age": 30, "city": "New York"}
    return len(sample_dict)

length = dict_length()
print(f"Length of dictionary: {length}")

"""
Problem: 1209
Write a Python program to reverse the keys and values in a dictionary. Dictionary operations.
"""

def reverse_dict():
    sample_dict = {"name": "Alice", "age": 30, "city": "New York"}
    return {v: k for k, v in sample_dict.items()}

reversed_dict = reverse_dict()
print(f"Reversed dictionary: {reversed_dict}")

"""
Problem: 1210
Write a Python program to create a dictionary from two lists, one for keys and one for values. Dictionary operations.
"""

def create_dict_from_lists():
    keys = ["name", "age", "city"]
    values = ["Alice", 30, "New York"]
    return dict(zip(keys, values))

created_dict = create_dict_from_lists()
print(f"Created dictionary: {created_dict}")

"""
Problem: 1211
Write a Python program to get the sum of all values in a dictionary. Dictionary operations.
"""

def sum_values():
    sample_dict = {"a": 10, "b": 20, "c": 30}
    return sum(sample_dict.values())

total = sum_values()
print(f"Sum of values: {total}")

"""
Problem: 1212
Write a Python program to filter a dictionary based on a condition. Dictionary operations.
"""

def filter_dict():
    sample_dict = {"name": "Alice", "age": 30, "city": "New York"}
    return {key: value for key, value in sample_dict.items() if isinstance(value, str)}

filtered_dict = filter_dict()
print(f"Filtered dictionary: {filtered_dict}")

"""
Problem: 1213
Write a Python program to find the maximum value in a dictionary. Dictionary operations.
"""

def max_value():
    sample_dict = {"a": 10, "b": 20, "c": 30}
    return max(sample_dict.values())

max_val = max_value()
print(f"Maximum value: {max_val}")

"""
Problem: 1214
Write a Python program to check if a dictionary is empty. Dictionary operations.
"""

def is_dict_empty():
    sample_dict = {}
    return len(sample_dict) == 0

result = is_dict_empty()
print(f"Is dictionary empty? {result}")

"""
Problem: 1215
Write a Python program to remove all occurrences of a value in a dictionary. Dictionary operations.
"""

def remove_value():
    sample_dict = {"a": 10, "b": 20, "c": 10}
    sample_dict = {k: v for k, v in sample_dict.items() if v != 10}
    return sample_dict

updated_dict = remove_value()
print(f"Dictionary after removal: {updated_dict}")

"""
Problem: 1216
Write a Python program to find the key associated with a given value in a dictionary. Dictionary operations.
"""

def find_key_by_value():
    sample_dict = {"a": 10, "b": 20, "c": 30}
    return [k for k, v in sample_dict.items() if v == 20]

key = find_key_by_value()
print(f"Key for value 20: {key}")

"""
Problem: 1217
Write a Python program to create a dictionary with default values using `defaultdict`. Dictionary operations.
"""

from collections import defaultdict

def create_defaultdict():
    sample_dict = defaultdict(int)
    sample_dict["a"] += 1
    sample_dict["b"] += 2
    return dict(sample_dict)

default_dict = create_defaultdict()
print(f"Default dictionary: {default_dict}")

"""
Problem: 1218
Write a Python program to get the first key-value pair from a dictionary. Dictionary operations.
"""

def first_key_value():
    sample_dict = {"a": 10, "b": 20, "c": 30}
    first_item = list(sample_dict.items())[0]
    return first_item

first_item = first_key_value()
print(f"First key-value pair: {first_item}")

"""
Problem: 1219
Write a Python program to merge multiple dictionaries into one. Dictionary operations.
"""

def merge_multiple_dicts():
    dict1 = {"a": 10, "b": 20}
    dict2 = {"c": 30, "d": 40}
    dict3 = {"e": 50}
    merged_dict = {**dict1, **dict2, **dict3}
    return merged_dict

merged_dict = merge_multiple_dicts()
print(f"Merged dictionary: {merged_dict}")

"""
Problem: 1220
Write a Python program to convert a list of tuples into a dictionary. Dictionary operations.
"""

def list_to_dict():
    sample_list = [("a", 1), ("b", 2), ("c", 3)]
    return dict(sample_list)

converted_dict = list_to_dict()
print(f"Converted dictionary: {converted_dict}")

"""
Problem: 1221
Write a Python program to create a Path object using the `pathlib` module.
"""

from pathlib import Path

def create_path():
    p = Path("example_directory")
    return p

path = create_path()
print(f"Created path: {path}")

"""
Problem: 1222
Write a Python program to check if a path exists using `pathlib`.
"""

from pathlib import Path

def check_path_exists():
    p = Path("example_directory")
    return p.exists()

exists = check_path_exists()
print(f"Path exists: {exists}")

"""
Problem: 1223
Write a Python program to check if a path is a file using `pathlib`.
"""

from pathlib import Path

def check_if_file():
    p = Path("example_file.txt")
    return p.is_file()

is_file = check_if_file()
print(f"Is it a file? {is_file}")

"""
Problem: 1224
Write a Python program to check if a path is a directory using `pathlib`.
"""

from pathlib import Path

def check_if_directory():
    p = Path("example_directory")
    return p.is_dir()

is_directory = check_if_directory()
print(f"Is it a directory? {is_directory}")

"""
Problem: 1225
Write a Python program to get the file name from a path using `pathlib`.
"""

from pathlib import Path

def get_file_name():
    p = Path("example_directory/example_file.txt")
    return p.name

file_name = get_file_name()
print(f"File name: {file_name}")

"""
Problem: 1226
Write a Python program to get the parent directory of a path using `pathlib`.
"""

from pathlib import Path

def get_parent_directory():
    p = Path("example_directory/example_file.txt")
    return p.parent

parent_directory = get_parent_directory()
print(f"Parent directory: {parent_directory}")

"""
Problem: 1227
Write a Python program to join two paths using `pathlib`.
"""

from pathlib import Path

def join_paths():
    p1 = Path("example_directory")
    p2 = "example_file.txt"
    return p1 / p2

joined_path = join_paths()
print(f"Joined path: {joined_path}")

"""
Problem: 1228
Write a Python program to get the file extension of a path using `pathlib`.
"""

from pathlib import Path

def get_file_extension():
    p = Path("example_file.txt")
    return p.suffix

file_extension = get_file_extension()
print(f"File extension: {file_extension}")

"""
Problem: 1229
Write a Python program to get the size of a file using `pathlib`.
"""

from pathlib import Path

def get_file_size():
    p = Path("example_file.txt")
    return p.stat().st_size

file_size = get_file_size()
print(f"File size: {file_size} bytes")

"""
Problem: 1230
Write a Python program to rename a file using `pathlib`.
"""

from pathlib import Path

def rename_file():
    old_path = Path("old_file.txt")
    new_path = Path("new_file.txt")
    old_path.rename(new_path)
    return new_path

renamed_file = rename_file()
print(f"Renamed file: {renamed_file}")

"""
Problem: 1231
Write a Python program to create a new directory using `pathlib`.
"""

from pathlib import Path

def create_directory():
    p = Path("new_directory")
    p.mkdir(parents=True, exist_ok=True)
    return p

created_directory = create_directory()
print(f"Created directory: {created_directory}")

"""
Problem: 1232
Write a Python program to remove a directory using `pathlib`.
"""

from pathlib import Path

def remove_directory():
    p = Path("new_directory")
    p.rmdir()
    return f"Directory {p} removed"

removed_directory = remove_directory()
print(removed_directory)

"""
Problem: 1233
Write a Python program to remove a file using `pathlib`.
"""

from pathlib import Path

def remove_file():
    p = Path("example_file.txt")
    p.unlink()
    return f"File {p} removed"

removed_file = remove_file()
print(removed_file)

"""
Problem: 1234
Write a Python program to get the absolute path of a file using `pathlib`.
"""

from pathlib import Path

def get_absolute_path():
    p = Path("example_file.txt")
    return p.resolve()

absolute_path = get_absolute_path()
print(f"Absolute path: {absolute_path}")

"""
Problem: 1235
Write a Python program to check if a path is a symbolic link using `pathlib`.
"""

from pathlib import Path

def check_if_symlink():
    p = Path("example_symlink")
    return p.is_symlink()

is_symlink = check_if_symlink()
print(f"Is it a symbolic link? {is_symlink}")

"""
Problem: 1236
Write a Python program to create a symbolic link using `pathlib`.
"""

from pathlib import Path

def create_symlink():
    target = Path("example_file.txt")
    symlink = Path("example_symlink")
    symlink.symlink_to(target)
    return symlink

symlink = create_symlink()
print(f"Created symlink: {symlink}")

"""
Problem: 1237
Write a Python program to check if a path is a directory and if it contains files using `pathlib`.
"""

from pathlib import Path

def check_directory_and_files():
    p = Path("example_directory")
    if p.is_dir():
        return [file.name for file in p.iterdir()]
    return []

directory_files = check_directory_and_files()
print(f"Files in directory: {directory_files}")

"""
Problem: 1238
Write a Python program to get the last modified time of a file using `pathlib`.
"""

from pathlib import Path
import time

def get_last_modified_time():
    p = Path("example_file.txt")
    timestamp = p.stat().st_mtime
    return time.ctime(timestamp)

last_modified_time = get_last_modified_time()
print(f"Last modified time: {last_modified_time}")

"""
Problem: 1239
Write a Python program to get the directory name from a path using `pathlib`.
"""

from pathlib import Path

def get_directory_name():
    p = Path("example_directory/example_file.txt")
    return p.parent.name

directory_name = get_directory_name()
print(f"Directory name: {directory_name}")

"""
Problem: 1240
Write a Python program to check if a path is empty (no files) using `pathlib`.
"""

from pathlib import Path

def check_if_empty():
    p = Path("example_directory")
    return len(list(p.iterdir())) == 0

is_empty = check_if_empty()
print(f"Is directory empty? {is_empty}")

"""
Problem: 1241
Write a Python program to iterate over all files in a directory using `pathlib`.
"""

from pathlib import Path

def iterate_files():
    p = Path("example_directory")
    return [file.name for file in p.iterdir() if file.is_file()]

files_in_directory = iterate_files()
print(f"Files in directory: {files_in_directory}")

"""
Problem: 1242
Write a Python program to find the path to the parent directory using `pathlib`.
"""

from pathlib import Path

def get_parent_directory():
    p = Path("example_directory/example_file.txt")
    return p.parent.parent

parent_directory = get_parent_directory()
print(f"Parent directory: {parent_directory}")

"""
Problem: 1243
Write a Python program to check if a file has a certain extension using `pathlib`.
"""

from pathlib import Path

def check_file_extension():
    p = Path("example_file.txt")
    return p.suffix == ".txt"

has_extension = check_file_extension()
print(f"Has .txt extension? {has_extension}")

"""
Problem: 1244
Write a Python program to get the file size using `pathlib` in human-readable format.
"""

from pathlib import Path

def get_human_readable_size():
    p = Path("example_file.txt")
    size_in_bytes = p.stat().st_size
    return f"{size_in_bytes / 1024:.2f} KB"

size = get_human_readable_size()
print(f"File size: {size}")

"""
Problem: 1245
Write a Python program to change the current working directory using `pathlib`.
"""

from pathlib import Path

def change_working_directory():
    p = Path("example_directory")
    p.chdir()
    return f"Changed working directory to: {p}"

changed_directory = change_working_directory()
print(changed_directory)

"""
Problem: 1246
Write a Python program to check if two conditions are true using the `and` operator.
"""

def check_conditions():
    a = 5
    b = 10
    return a > 3 and b < 15

result = check_conditions()
print(f"Both conditions are true: {result}")

"""
Problem: 1247
Write a Python program to check if a number is between 10 and 20 (both inclusive) using the `and` operator.
"""

def check_range():
    num = 15
    return num >= 10 and num <= 20

result = check_range()
print(f"Number is between 10 and 20: {result}")

"""
Problem: 1248
Write a Python program to check if a string is non-empty and contains a specific character using the `and` operator.
"""

def check_string():
    text = "hello"
    return len(text) > 0 and "e" in text

result = check_string()
print(f"String is non-empty and contains 'e': {result}")

"""
Problem: 1249
Write a Python program to check if a number is divisible by both 3 and 5 using the `and` operator.
"""

def main(number):
    return True if number % 3 == 0 and number % 5 == 0 else False
    
number = 15
main(number)

def check_divisibility():
    num = 15
    return num % 3 == 0 and num % 5 == 0

result = check_divisibility()
print(f"Number is divisible by both 3 and 5: {result}")

def main(number):
    return number % 3 == 0 and number % 5 == 0
    
number = 15
main(number)

"""
Problem: 1250
Write a Python program to check if a list is non-empty and the first element is greater than 5 using the `and` operator.
"""

def check_list():
    lst = [6, 2, 8]
    return len(lst) > 0 and lst[0] > 5

result = check_list()
print(f"List is non-empty and first element is greater than 5: {result}")

"""
Problem: 1251
Write a Python program to check if a year is a leap year using the `and` operator.
"""

def check_leap_year():
    year = 2024
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

result = check_leap_year()
print(f"Year is a leap year: {result}")

"""
Problem: 1252
Write a Python program to check if a number is positive, even, and divisible by 4 using the `and` operator.
"""

def check_number():
    num = 8
    return num > 0 and num % 2 == 0 and num % 4 == 0

result = check_number()
print(f"Number is positive, even, and divisible by 4: {result}")

"""
Problem: 1253
Write a Python program to check if a list contains exactly three elements, and the first element is greater than 5 using the `and` operator.
"""

def check_list_conditions():
    lst = [6, 2, 8]
    return len(lst) == 3 and lst[0] > 5

result = check_list_conditions()
print(f"List has three elements and first is greater than 5: {result}")

"""
Problem: 1254
Write a Python program to check if a string is lowercase and its length is greater than 3 using the `and` operator.
"""

def check_string_conditions():
    text = "hello"
    return text.islower() and len(text) > 3

result = check_string_conditions()
print(f"String is lowercase and its length is greater than 3: {result}")

"""
Problem: 1255
Write a Python program to check if a number is greater than 10 and less than 50 using the `and` operator.
"""

def check_range_conditions():
    num = 30
    return num > 10 and num < 50

result = check_range_conditions()
print(f"Number is between 10 and 50: {result}")

"""
Problem: 1256
Write a Python program to check if a number is both a multiple of 7 and 11 using the `and` operator.
"""

def check_multiples():
    num = 77
    return num % 7 == 0 and num % 11 == 0

result = check_multiples()
print(f"Number is a multiple of both 7 and 11: {result}")

"""
Problem: 1257
Write a Python program to check if a person is eligible to vote, meaning the age is greater than 18 and they are a citizen, using the `and` operator.
"""

def check_voting_eligibility():
    age = 20
    is_citizen = True
    return age > 18 and is_citizen

result = check_voting_eligibility()
print(f"Person is eligible to vote: {result}")

"""
Problem: 1258
Write a Python program to check if a number is divisible by 2, 3, and 5 using the `and` operator.
"""

def check_divisibility_all():
    num = 30
    return num % 2 == 0 and num % 3 == 0 and num % 5 == 0

result = check_divisibility_all()
print(f"Number is divisible by 2, 3, and 5: {result}")

"""
Problem: 1259
Write a Python program to check if a dictionary contains a specific key and the value is greater than a specified number using the `and` operator.
"""

def check_dict_conditions():
    sample_dict = {"age": 30, "city": "New York"}
    return "age" in sample_dict and sample_dict["age"] > 25

result = check_dict_conditions()
print(f"Dictionary contains 'age' and its value is greater than 25: {result}")

"""
Problem: 1260
Write a Python program to check if a string is not empty and its length is an even number using the `and` operator.
"""

def check_string_length():
    text = "hello"
    return len(text) > 0 and len(text) % 2 == 0

result = check_string_length()
print(f"String is not empty and its length is even: {result}")

"""
Problem: 1261
Write a Python program to check if a number is within the range of 20 to 100 (inclusive) using the `and` operator.
"""

def check_range_inclusive():
    num = 50
    return num >= 20 and num <= 100

result = check_range_inclusive()
print(f"Number is between 20 and 100 (inclusive): {result}")

"""
Problem: 1262
Write a Python program to check if a number is divisible by both 2 and 7 using the `and` operator.
"""

def check_divisible_by_2_and_7():
    num = 14
    return num % 2 == 0 and num % 7 == 0

result = check_divisible_by_2_and_7()
print(f"Number is divisible by both 2 and 7: {result}")

"""
Problem: 1263
Write a Python program to check if a number is negative and divisible by 5 using the `and` operator.
"""

def check_negative_and_divisible():
    num = -25
    return num < 0 and num % 5 == 0

result = check_negative_and_divisible()
print(f"Number is negative and divisible by 5: {result}")

"""
Problem: 1264
Write a Python program to check if a string contains only digits and its length is greater than 5 using the `and` operator.
"""

def check_digit_string():
    text = "123456"
    return text.isdigit() and len(text) > 5

result = check_digit_string()
print(f"String contains only digits and its length is greater than 5: {result}")

"""
Problem: 1265
Write a Python program to check if a number is a prime number and greater than 10 using the `and` operator.
"""

def check_prime_and_greater_than_10():
    num = 13
    return num > 10 and all(num % i != 0 for i in range(2, num))

result = check_prime_and_greater_than_10()
print(f"Number is prime and greater than 10: {result}")

"""
Problem: 1266
Write a Python program to check if a number is odd and greater than 0 using the `and` operator.
"""

def check_odd_and_positive():
    num = 7
    return num % 2 != 0 and num > 0

result = check_odd_and_positive()
print(f"Number is odd and positive: {result}")

"""
Problem: 1267
Write a Python program to check if a file exists and its size is greater than 100 KB using the `and` operator.
"""

from pathlib import Path

def check_file_exists_and_size():
    p = Path("example_file.txt")
    return p.exists() and p.stat().st_size > 100 * 1024

result = check_file_exists_and_size()
print(f"File exists and its size is greater than 100 KB: {result}")

"""
Problem: 1268
Write a Python program to check if a list contains exactly 5 elements and the last element is greater than 10 using the `and` operator.
"""

def check_list_length_and_last_element():
    lst = [1, 2, 3, 4, 12]
    return len(lst) == 5 and lst[-1] > 10

result = check_list_length_and_last_element()
print(f"List contains exactly 5 elements and last element is greater than 10: {result}")

"""
Problem: 1269
Write a Python program to check if a number is between 1 and 10 (inclusive) and is odd using the `and` operator.
"""

def check_range_and_odd():
    num = 7
    return num >= 1 and num <= 10 and num % 2 != 0

result = check_range_and_odd()
print(f"Number is between 1 and 10 and odd: {result}")

"""
Problem: 1270
Write a Python program to check if at least one of two conditions is true using the `or` operator.
"""

def check_conditions():
    a = 5
    b = 10
    return a > 10 or b < 15

result = check_conditions()
print(f"At least one condition is true: {result}")

"""
Problem: 1271
Write a Python program to check if a number is either less than 10 or greater than 20 using the `or` operator.
"""

def check_range():
    num = 5
    return num < 10 or num > 20

result = check_range()
print(f"Number is either less than 10 or greater than 20: {result}")

"""
Problem: 1272
Write a Python program to check if a string is empty or contains a specific character using the `or` operator.
"""

def check_string():
    text = "hello"
    return len(text) == 0 or "e" in text

result = check_string()
print(f"String is empty or contains 'e': {result}")

"""
Problem: 1273
Write a Python program to check if a number is divisible by 3 or 5 using the `or` operator.
"""

def check_divisibility():
    num = 9
    return num % 3 == 0 or num % 5 == 0

result = check_divisibility()
print(f"Number is divisible by 3 or 5: {result}")

"""
Problem: 1274
Write a Python program to check if a list is empty or its first element is greater than 5 using the `or` operator.
"""

def check_list():
    lst = [6, 2, 8]
    return len(lst) == 0 or lst[0] > 5

result = check_list()
print(f"List is empty or its first element is greater than 5: {result}")

"""
Problem: 1275
Write a Python program to check if a year is a leap year or divisible by 100 using the `or` operator.
"""

def check_leap_year():
    year = 2024
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

result = check_leap_year()
print(f"Year is a leap year or divisible by 100: {result}")

"""
Problem: 1276
Write a Python program to check if a number is positive or divisible by 7 using the `or` operator.
"""

def check_number():
    num = 10
    return num > 0 or num % 7 == 0

result = check_number()
print(f"Number is positive or divisible by 7: {result}")

"""
Problem: 1277
Write a Python program to check if a string is lowercase or its length is greater than 3 using the `or` operator.
"""

def check_string_conditions():
    text = "HELLO"
    return text.islower() or len(text) > 3

result = check_string_conditions()
print(f"String is lowercase or its length is greater than 3: {result}")

"""
Problem: 1278
Write a Python program to check if a number is between 10 and 50 or divisible by 7 using the `or` operator.
"""

def check_conditions():
    num = 30
    return (num >= 10 and num <= 50) or num % 7 == 0

result = check_conditions()
print(f"Number is between 10 and 50 or divisible by 7: {result}")

"""
Problem: 1279
Write a Python program to check if a number is a multiple of 7 or 11 using the `or` operator.
"""

def check_multiples():
    num = 77
    return num % 7 == 0 or num % 11 == 0

result = check_multiples()
print(f"Number is a multiple of 7 or 11: {result}")

"""
Problem: 1280
Write a Python program to check if a person is eligible to vote, meaning the age is greater than 18 or they are a citizen, using the `or` operator.
"""

def check_voting_eligibility():
    age = 17
    is_citizen = True
    return age > 18 or is_citizen

result = check_voting_eligibility()
print(f"Person is eligible to vote: {result}")

"""
Problem: 1281
Write a Python program to check if a number is divisible by 2 or 3 using the `or` operator.
"""

def check_divisibility_all():
    num = 9
    return num % 2 == 0 or num % 3 == 0

result = check_divisibility_all()
print(f"Number is divisible by 2 or 3: {result}")

"""
Problem: 1282
Write a Python program to check if a dictionary contains a specific key or if the value is greater than a specified number using the `or` operator.
"""

def check_dict_conditions():
    sample_dict = {"age": 20, "city": "New York"}
    return "name" in sample_dict or sample_dict["age"] > 25

result = check_dict_conditions()
print(f"Dictionary contains 'name' or age is greater than 25: {result}")

"""
Problem: 1283
Write a Python program to check if a string is empty or contains a number using the `or` operator.
"""

def check_string_empty_or_number():
    text = "hello123"
    return len(text) == 0 or any(char.isdigit() for char in text)

result = check_string_empty_or_number()
print(f"String is empty or contains a number: {result}")

"""
Problem: 1284
Write a Python program to check if a number is either negative or divisible by 3 using the `or` operator.
"""

def check_negative_or_divisible_by_3():
    num = -15
    return num < 0 or num % 3 == 0

result = check_negative_or_divisible_by_3()
print(f"Number is negative or divisible by 3: {result}")

"""
Problem: 1285
Write a Python program to check if a list is empty or contains more than 5 elements using the `or` operator.
"""

def check_list_conditions():
    lst = [1, 2, 3]
    return len(lst) == 0 or len(lst) > 5

result = check_list_conditions()
print(f"List is empty or contains more than 5 elements: {result}")

"""
Problem: 1286
Write a Python program to check if a number is a perfect square or a perfect cube using the `or` operator.
"""

import math

def check_perfect_square_or_cube():
    num = 16
    return math.isqrt(num) ** 2 == num or round(num ** (1 / 3)) ** 3 == num

result = check_perfect_square_or_cube()
print(f"Number is a perfect square or cube: {result}")

"""
Problem: 1287
Write a Python program to check if a string contains only letters or only digits using the `or` operator.
"""

def check_string_type():
    text = "1234"
    return text.isalpha() or text.isdigit()

result = check_string_type()
print(f"String contains only letters or digits: {result}")

"""
Problem: 1288
Write a Python program to check if a list contains exactly 3 elements or its sum is greater than 50 using the `or` operator.
"""

def check_list_conditions():
    lst = [6, 2, 8]
    return len(lst) == 3 or sum(lst) > 50

result = check_list_conditions()
print(f"List has exactly 3 elements or its sum is greater than 50: {result}")

"""
Problem: 1289
Write a Python program to check if a number is divisible by 2 or 5 using the `or` operator.
"""

def check_divisible_by_2_or_5():
    num = 10
    return num % 2 == 0 or num % 5 == 0

result = check_divisible_by_2_or_5()
print(f"Number is divisible by 2 or 5: {result}")

"""
Problem: 1290
Write a Python program to check if a file exists or if it is writable using the `or` operator.
"""

from pathlib import Path

def check_file_conditions():
    p = Path("example_file.txt")
    return p.exists() or p.is_file()

result = check_file_conditions()
print(f"File exists or is a file: {result}")

"""
Problem: 1291
Write a Python program to check if a number is greater than 100 or less than 10 using the `or` operator.
"""

def check_number():
    num = 5
    return num > 100 or num < 10

result = check_number()
print(f"Number is greater than 100 or less than 10: {result}")

"""
Problem: 1292
Write a Python program to check if a string is uppercase or its length is even using the `or` operator.
"""

def check_string_conditions():
    text = "HELLO"
    return text.isupper() or len(text) % 2 == 0

result = check_string_conditions()
print(f"String is uppercase or its length is even: {result}")

"""
Problem: 1293
Write a Python program to check if a list is non-empty or its last element is greater than 10 using the `or` operator.
"""

def check_list_conditions():
    lst = [6, 2, 8]
    return len(lst) > 0 or lst[-1] > 10

result = check_list_conditions()
print(f"List is non-empty or its last element is greater than 10: {result}")

"""
Problem: 1294
Write a Python program to check if a number is even or divisible by 3 using the `or` operator.
"""

def check_even_or_divisible_by_3():
    num = 8
    return num % 2 == 0 or num % 3 == 0

result = check_even_or_divisible_by_3()
print(f"Number is even or divisible by 3: {result}")

"""
Problem: 1295
Write a Python program to check if a string is not empty or contains the character 'a' using the `or` operator.
"""

def check_string():
    text = "apple"
    return len(text) > 0 or "a" in text

result = check_string()
print(f"String is not empty or contains 'a': {result}")

""" 
Problem: 1296
Write a Python program to extract all words starting with a capital letter.
"""

s = "Hello World, this is Python."
words = re.findall(r"\b[A-Z][a-z]*\b", s)
print(words)  # Expected output: ['Hello', 'World', 'Python']


""" 
Problem: 1297
Write a Python program to split a string by commas and optional whitespace.
"""

s = "apple, banana ,cherry , grape"
items = re.split(r"\s*,\s*", s)
print(items)  # Expected output: ['apple', 'banana', 'cherry', 'grape']


""" 
Problem: 1298
Write a Python program to check if a password contains at least one digit, one uppercase, and one lowercase letter.
"""

password = "Password123"
match = bool(re.search(r"[A-Z]", password) and re.search(r"[a-z]", password) and re.search(r"\d", password))
print(match)  # Expected output: True


""" 
Problem: 1299
Write a Python program to find all email addresses in a text.
"""

text = "Send to alice@example.com and bob99@domain.co.uk"
emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
print(emails)  # Expected output: ['alice@example.com', 'bob99@domain.co.uk']


""" 
Problem: 1300
Write a Python program to extract hashtags from a tweet.
"""

tweet = "Loving the #Python #coding journey!"
hashtags = re.findall(r"#\w+", tweet)
print(hashtags)  # Expected output: ['#Python', '#coding']


""" 
Problem: 1301
Write a Python program to extract domain names from URLs.
"""

text = "Visit us at https://example.com or http://test.org"
domains = re.findall(r"https?://([\w.-]+)", text)
print(domains)  # Expected output: ['example.com', 'test.org']


""" 
Problem: 1302
Write a Python program to validate if a string is a valid IPv4 address.
"""

ip = "192.168.1.1"
pattern = r"^(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(?!$)){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$"
match = bool(re.fullmatch(pattern, ip))
print(match)  # Expected output: True


""" 
Problem: 1303
Write a Python program to remove all punctuation from a string.
"""

text = "Hello, world! Python is great."
clean = re.sub(r"[^\w\s]", "", text)
print(clean)  # Expected output: Hello world Python is great


""" 
Problem: 1304
Write a Python program to match a string that starts with a vowel.
"""

s = "apple"
match = bool(re.match(r"^[aeiouAEIOU]", s))
print(match)  # Expected output: True


""" 
Problem: 1305
Write a Python program to extract all valid dates in the format YYYY-MM-DD.
"""

text = "Events: 2024-06-01, 2025-07-04, 99-01-01"
dates = re.findall(r"\b\d{4}-\d{2}-\d{2}\b", text)
print(dates)  # Expected output: ['2024-06-01', '2025-07-04']


""" 
Problem: 1306
Write a Python program to validate a hexadecimal color code.
"""

color = "#1a2b3c"
match = bool(re.fullmatch(r"#([A-Fa-f0-9]{6})", color))
print(match)  # Expected output: True


""" 
Problem: 1307
Write a Python program to extract all words that end with 'ing'.
"""

text = "I am running and jumping while singing."
words = re.findall(r"\b\w+ing\b", text)
print(words)  # Expected output: ['running', 'jumping', 'singing']


""" 
Problem: 1308
Write a Python program to extract the file extension from a filename.
"""

filename = "document.pdf"
ext = re.search(r"\.(\w+)$", filename).group(1)
print(ext)  # Expected output: pdf


""" 
Problem: 1309
Write a Python program to find duplicated words in a sentence.
"""

text = "This is is a test test string"
duplicates = re.findall(r"\b(\w+)\s+\1\b", text)
print(duplicates)  # Expected output: ['is', 'test']

""" 
Problem: 1310
Write a Python program to extract all capitalized words from a paragraph.
"""

text = "Alice and Bob went to New York City on Monday."
capitalized = re.findall(r"\b[A-Z][a-z]*\b", text)
print(capitalized)  # Expected: ['Alice', 'Bob', 'New', 'York', 'City', 'Monday']


""" 
Problem: 1311
Write a Python program to validate a time in 24-hour format (HH:MM).
"""

time = "23:59"
match = bool(re.fullmatch(r"([01]\d|2[0-3]):[0-5]\d", time))
print(match)  # Expected: True


""" 
Problem: 1312
Write a Python program to extract all integers and floats from a string.
"""

text = "The temperature is 21.5C, and humidity is 60% with 0.25 inches rain."
numbers = re.findall(r"\d+\.\d+|\d+", text)
print(numbers)  # Expected: ['21.5', '60', '0.25']


""" 
Problem: 1313
Write a Python program to remove leading zeros from an IP address.
"""

ip = "192.168.001.001"
clean_ip = re.sub(r"\b0+(\d)", r"\1", ip)
print(clean_ip)  # Expected: 192.168.1.1


""" 
Problem: 1314
Write a Python program to check if a string is a valid slug (only lowercase letters, numbers, hyphens).
"""

slug = "python-tips-101"
match = bool(re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", slug))
print(match)  # Expected: True


""" 
Problem: 1315
Write a Python program to extract content inside parentheses.
"""

text = "This is a sample (with content) and (another one)."
content = re.findall(r"\((.*?)\)", text)
print(content)  # Expected: ['with content', 'another one']


""" 
Problem: 1316
Write a Python program to match all valid HTML tags in a string.
"""

html = "<div><p>Hello</p></div>"
tags = re.findall(r"<[^>]+>", html)
print(tags)  # Expected: ['<div>', '<p>', '</p>', '</div>']


""" 
Problem: 1317
Write a Python program to validate if a string is a US ZIP code (5 digits).
"""

zip_code = "12345"
match = bool(re.fullmatch(r"\d{5}", zip_code))
print(match)  # Expected: True


""" 
Problem: 1318
Write a Python program to find all abbreviations like "U.S.A." in a string.
"""

text = "Some examples: U.S.A. and E.U."
abbreviations = re.findall(r"(?:[A-Z]\.){2,}", text)
print(abbreviations)  # Expected: ['U.S.A.', 'E.U.']


""" 
Problem: 1319
Write a Python program to count how many times a word appears in a case-insensitive way.
"""

text = "Python is great. I love python because PYTHON is powerful."
count = len(re.findall(r"\bpython\b", text, re.IGNORECASE))
print(count)  # Expected: 3


""" 
Problem: 1320
Write a Python program to replace duplicate spaces with a single space.
"""

text = "This    is  a    spaced   sentence."
clean = re.sub(r"\s{2,}", " ", text)
print(clean)  # Expected: "This is a spaced sentence."


""" 
Problem: 1321
Write a Python program to validate a MAC address (e.g., 00:1A:2B:3C:4D:5E).
"""

mac = "00:1A:2B:3C:4D:5E"
match = bool(re.fullmatch(r"([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}", mac))
print(match)  # Expected: True


""" 
Problem: 1322
Write a Python program to extract the username from an email address.
"""
import re
email = "john.doe@example.com"
username = re.match(r"([^@]+)", email).group(1)
print(username)  # Expected: john.doe


""" 
Problem: 1323
Write a Python program to insert commas into a numeric string every three digits.
"""

num = "1000000"
formatted = re.sub(r"(?<=\d)(?=(\d{3})+$)", ",", num)
print(formatted)  # Expected: 1,000,000


""" 
Problem: 1324
Write a Python program to extract all valid Twitter handles from a string.
"""

text = "Follow @python, @realpython, and @openai!"
handles = re.findall(r"@\w+", text)
print(handles)  # Expected: ['@python', '@realpython', '@openai']


""" 
Problem: 1325
Write a Python program to check if a string contains any emoji.
"""

emoji_text = "I love 🍕 and 🐍"
match = bool(re.search(r"[\U0001F600-\U0001F64F]", emoji_text))
print(match)  # Expected: True


""" 
Problem: 1326
Write a Python program to extract time values in 12-hour format with AM/PM.
"""

text = "Meeting at 02:30 PM and dinner at 07:45 AM."
times = re.findall(r"\b\d{2}:\d{2} [AP]M\b", text)
print(times)  # Expected: ['02:30 PM', '07:45 AM']


""" 
Problem: 1327
Write a Python program to extract prices with a dollar sign.
"""

text = "Items: $20.99, $3.50, $100"
prices = re.findall(r"\$\d+(\.\d{2})?", text)
print(prices)  # Expected: ['$20.99', '$3.50', '$100']


""" 
Problem: 1328
Write a Python program to detect duplicate characters in a string using regex.
"""

s = "programming"
duplicates = re.findall(r"(\w)(?=.*\1)", s)
print(set(duplicates))  # Expected: {'r', 'g', 'm'}


""" 
Problem: 1329
Write a Python program to validate a hexadecimal number (e.g., 0x1A3F).
"""

hex_num = "0x1A3F"
match = bool(re.fullmatch(r"0x[0-9A-Fa-f]+", hex_num))
print(match)  # Expected: True


""" 
Problem: 1330
Write a Python program to extract quoted strings (single or double quotes).
"""
import re

text = "'Hello', she said. \"How are you?\""
quotes = re.findall(r"(['\"])(.*?)\1", text)
print([q[1] for q in quotes])  # Expected: ['Hello', 'How are you?']


""" 
Problem: 1331
Write a Python program to check if a variable is an integer using isinstance().
"""

x = 10
print(isinstance(x, int))  # Expected: True


""" 
Problem: 1332
Write a Python program to check if a variable is a string using isinstance().
"""

x = "hello"
print(isinstance(x, str))  # Expected: True


""" 
Problem: 1333
Write a Python program to check if a variable is a float using isinstance().
"""

x = 3.14
print(isinstance(x, float))  # Expected: True


""" 
Problem: 1334
Write a Python program to check if a variable is a list using isinstance().
"""

x = [1, 2, 3]
print(isinstance(x, list))  # Expected: True


""" 
Problem: 1335
Write a Python program to check if a variable is a dictionary using isinstance().
"""

x = {"a": 1}
print(isinstance(x, dict))  # Expected: True


""" 
Problem: 1336
Write a Python program to check if a variable is either int or float using isinstance().
"""

x = 10.0
print(isinstance(x, (int, float)))  # Expected: True


""" 
Problem: 1337
Write a Python program to check if each element in a list is a string.
"""

lst = ["apple", "banana", "cherry"]
result = all(isinstance(item, str) for item in lst)
print(result)  # Expected: True


""" 
Problem: 1338
Write a Python program to filter only integers from a mixed list using isinstance().
"""

items = [1, "a", 3.5, 4, "b"]
ints = [x for x in items if isinstance(x, int)]
print(ints)  # Expected: [1, 4]


""" 
Problem: 1339
Write a Python program to filter only strings from a mixed list using isinstance().
"""

items = [1, "apple", 2.5, "banana"]
strings = [x for x in items if isinstance(x, str)]
print(strings)  # Expected: ['apple', 'banana']


""" 
Problem: 1340
Write a Python program to check if an object is a boolean using isinstance().
"""

x = True
print(isinstance(x, bool))  # Expected: True


""" 
Problem: 1341
Write a Python program to check if a variable is a tuple using isinstance().
"""

x = (1, 2, 3)
print(isinstance(x, tuple))  # Expected: True


""" 
Problem: 1342
Write a Python program to check if an object is not a string using isinstance().
"""

x = 42
print(not isinstance(x, str))  # Expected: True


""" 
Problem: 1343
Write a Python program to define a function that accepts only strings using isinstance().
"""

def greet(name):
    if not isinstance(name, str):
        return "Invalid input"
    return f"Hello, {name}!"

print(greet("Alice"))  # Expected: Hello, Alice!
print(greet(123))      # Expected: Invalid input


""" 
Problem: 1344
Write a Python program to check if all elements in a nested list are lists.
"""

nested = [[1, 2], [3, 4]]
result = all(isinstance(sub, list) for sub in nested)
print(result)  # Expected: True


""" 
Problem: 1345
Write a Python program to separate strings and numbers from a list.
"""

mixed = [1, "one", 2, "two", 3, "three"]
nums = [x for x in mixed if isinstance(x, int)]
words = [x for x in mixed if isinstance(x, str)]
print(nums)   # Expected: [1, 2, 3]
print(words)  # Expected: ['one', 'two', 'three']


""" 
Problem: 1346
Write a Python program to validate argument types in a function.
"""

def multiply(a, b):
    if not all(isinstance(x, (int, float)) for x in (a, b)):
        return "Invalid input"
    return a * b

print(multiply(2, 3))     # Expected: 6
print(multiply(2, "x"))   # Expected: Invalid input


""" 
Problem: 1347
Write a Python program to check if a variable is a set using isinstance().
"""

x = {1, 2, 3}
print(isinstance(x, set))  # Expected: True


""" 
Problem: 1348
Write a Python program to validate that dictionary keys are all strings.
"""

d = {"a": 1, "b": 2}
result = all(isinstance(k, str) for k in d.keys())
print(result)  # Expected: True


""" 
Problem: 1349
Write a Python program to validate that dictionary values are all integers.
"""

d = {"x": 1, "y": 2}
result = all(isinstance(v, int) for v in d.values())
print(result)  # Expected: True


""" 
Problem: 1350
Write a Python program to check if an object is a file-like object (has read method).
"""

class FakeFile:
    def read(self):
        pass

f = FakeFile()
print(hasattr(f, "read") and callable(f.read))  # Expected: True

""" 
Problem: 1351
Write a Python program to remove a key from a dictionary using pop() and print the updated dictionary.
"""
d = {"a": 1, "b": 2, "c": 3}
d.pop("b")
print(d)  # Expected: {'a': 1, 'c': 3}


""" 
Problem: 1352
Write a Python program to use pop() to retrieve the value of a key from a dictionary.
"""
d = {"a": 10, "b": 20}
value = d.pop("a")
print(value)  # Expected: 10


""" 
Problem: 1353
Write a Python program to use pop() on a list to remove the last item.
"""
lst = [1, 2, 3, 4]
lst.pop()
print(lst)  # Expected: [1, 2, 3]


""" 
Problem: 1354
Write a Python program to remove a specific index from a list using pop().
"""
lst = [10, 20, 30, 40]
lst.pop(1)
print(lst)  # Expected: [10, 30, 40]


""" 
Problem: 1355
Write a Python program to capture and print the element removed using pop() from a list.
"""
lst = [5, 6, 7]
removed = lst.pop()
print(removed)  # Expected: 7


""" 
Problem: 1356
Write a Python program to remove all elements from a list using pop() in a loop.
"""
lst = [1, 2, 3]
while lst:
    print(lst.pop())  # Expected: 3, 2, 1 (on separate lines)


""" 
Problem: 1357
Write a Python program to handle IndexError when popping from an empty list.
"""
lst = []
try:
    lst.pop()
except IndexError:
    print("List is empty")  # Expected: "List is empty"


""" 
Problem: 1358
Write a Python program to use pop() with dictionaries and provide a default return value if the key doesn't exist.
"""
d = {"x": 5}
val = d.pop("y", "Not Found")
print(val)  # Expected: "Not Found"


""" 
Problem: 1359
Write a Python program to safely remove a key from a dictionary using pop() inside a try block.
"""
d = {"a": 100}
try:
    print(d.pop("b"))
except KeyError:
    print("Key not found")  # Expected: "Key not found"


""" 
Problem: 1360
Write a Python program to remove keys one by one using pop() until the dictionary is empty.
"""
d = {"k1": 1, "k2": 2}
while d:
    print(d.popitem())  # Expected: tuple key-value pairs


""" 
Problem: 1361
Write a Python program to pop elements from a stack represented by a list.
"""
stack = [1, 2, 3]
print(stack.pop())  # Expected: 3


""" 
Problem: 1362
Write a Python program to simulate queue dequeue using pop(0).
"""
queue = [10, 20, 30]
print(queue.pop(0))  # Expected: 10


""" 
Problem: 1363
Write a Python program to remove the last element from a list using pop() and store it.
"""
numbers = [4, 5, 6]
last = numbers.pop()
print(last)  # Expected: 6


""" 
Problem: 1364
Write a Python program to demonstrate the use of pop() on a string key in a dictionary.
"""
d = {"name": "Alice", "age": 30}
print(d.pop("name"))  # Expected: "Alice"


""" 
Problem: 1365
Write a Python program to pop multiple elements from the end of a list using a loop.
"""
lst = [1, 2, 3, 4, 5]
for _ in range(3):
    lst.pop()
print(lst)  # Expected: [1, 2]


""" 
Problem: 1366
Write a Python program to pop and sum the last two numbers from a list.
"""
lst = [100, 200, 300]
sum_last_two = lst.pop() + lst.pop()
print(sum_last_two)  # Expected: 500


""" 
Problem: 1367
Write a Python program to use pop() in a function that removes a key from a given dictionary.
"""
def remove_key(d, key):
    return d.pop(key, None)

print(remove_key({"a": 1, "b": 2}, "a"))  # Expected: 1


""" 
Problem: 1368
Write a Python program to pop an element from a list and append it to another list.
"""
src = [9, 8, 7]
dst = []
dst.append(src.pop())
print(dst)  # Expected: [7]


""" 
Problem: 1369
Write a Python program to implement a basic undo feature using pop() on a list of actions.
"""
actions = ["type", "edit", "save"]
undo = actions.pop()
print(undo)  # Expected: "save"


""" 
Problem: 1370
Write a Python program to pop elements from a nested list.
"""
nested = [[1, 2], [3, 4], [5, 6]]
last_sublist = nested.pop()
print(last_sublist)  # Expected: [5, 6]

""" 
Problem: 1371  
Write a Python program with a function that accepts arbitrary keyword arguments and prints them.
"""
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1, b=2)  # Expected: {'a': 1, 'b': 2}


""" 
Problem: 1372  
Write a Python function that prints each key-value pair in **kwargs on a separate line.
"""
def display_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_kwargs(name="Alice", age=30)
# Expected:
# name: Alice
# age: 30


""" 
Problem: 1373  
Write a Python program to count the number of keyword arguments passed to a function.
"""
def count_kwargs(**kwargs):
    print(len(kwargs))

count_kwargs(a=1, b=2, c=3)  # Expected: 3


""" 
Problem: 1374  
Write a Python function that returns the keys of **kwargs as a list.
"""
def kwargs_keys(**kwargs):
    return list(kwargs.keys())

print(kwargs_keys(x=10, y=20))  # Expected: ['x', 'y']


""" 
Problem: 1375  
Write a Python function that returns the values of **kwargs as a list.
"""
def kwargs_values(**kwargs):
    return list(kwargs.values())

print(kwargs_values(x=10, y=20))  # Expected: [10, 20]


""" 
Problem: 1376  
Write a Python function that returns True if 'id' is in **kwargs.
"""
def has_id(**kwargs):
    return 'id' in kwargs

print(has_id(name="A", id=123))  # Expected: True


""" 
Problem: 1377  
Write a Python function that returns the value of a keyword argument 'name' if it exists, else return 'Unknown'.
"""
def get_name(**kwargs):
    return kwargs.get('name', 'Unknown')

print(get_name(age=22))  # Expected: "Unknown"


""" 
Problem: 1378  
Write a Python function that sums all numeric values in **kwargs.
"""
def sum_kwargs(**kwargs):
    return sum(v for v in kwargs.values() if isinstance(v, (int, float)))

print(sum_kwargs(a=10, b=5.5, c="x"))  # Expected: 15.5


""" 
Problem: 1379  
Write a Python function that filters and returns keyword arguments where values are strings.
"""
def string_kwargs(**kwargs):
    return {k: v for k, v in kwargs.items() if isinstance(v, str)}

print(string_kwargs(a="hi", b=2, c="hello"))  # Expected: {'a': 'hi', 'c': 'hello'}


""" 
Problem: 1380  
Write a Python function that prints a formatted string from **kwargs using name and age keys.
"""
def greet(**kwargs):
    print(f"Hello {kwargs.get('name', 'Guest')}, age {kwargs.get('age', 'N/A')}")

greet(name="Bob", age=40)  # Expected: Hello Bob, age 40


""" 
Problem: 1381  
Write a Python function that updates a dictionary with keyword arguments.
"""
def update_dict(base, **kwargs):
    base.update(kwargs)
    return base

print(update_dict({'x': 1}, y=2, z=3))  # Expected: {'x': 1, 'y': 2, 'z': 3}


""" 
Problem: 1382  
Write a Python function that merges two dictionaries using **kwargs.
"""
def merge_dicts(d1, **kwargs):
    merged = d1.copy()
    merged.update(kwargs)
    return merged

print(merge_dicts({'a': 1}, b=2))  # Expected: {'a': 1, 'b': 2}


""" 
Problem: 1383  
Write a Python function that prints only the keyword arguments with even integer values.
"""
def even_kwargs(**kwargs):
    for k, v in kwargs.items():
        if isinstance(v, int) and v % 2 == 0:
            print(f"{k}: {v}")

even_kwargs(a=1, b=2, c=4)
# Expected:
# b: 2
# c: 4


""" 
Problem: 1384  
Write a Python function that accepts any number of keyword arguments and prints them sorted by key.
"""
def sorted_kwargs(**kwargs):
    for k in sorted(kwargs.keys()):
        print(f"{k}: {kwargs[k]}")

sorted_kwargs(z=9, a=1, m=5)
# Expected:
# a: 1
# m: 5
# z: 9


""" 
Problem: 1385  
Write a Python function that prints the number of string values in **kwargs.
"""
def count_strings(**kwargs):
    print(sum(1 for v in kwargs.values() if isinstance(v, str)))

count_strings(a="one", b=2, c="three")  # Expected: 2


""" 
Problem: 1386  
Write a Python function that prints whether each value in **kwargs is truthy or falsy.
"""
def check_truthy(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {'Truthy' if v else 'Falsy'}")

check_truthy(a=0, b="hello", c=[])  
# Expected:
# a: Falsy
# b: Truthy
# c: Falsy


""" 
Problem: 1387  
Write a Python function that prints all key-value pairs in **kwargs where the key starts with 'a'.
"""
def starts_with_a(**kwargs):
    for k, v in kwargs.items():
        if k.startswith('a'):
            print(f"{k}: {v}")

starts_with_a(apple=1, banana=2, ant=3)
# Expected:
# apple: 1
# ant: 3


""" 
Problem: 1388  
Write a Python function that returns a reversed dictionary built from **kwargs.
"""
def reverse_kwargs(**kwargs):
    return {v: k for k, v in kwargs.items()}

print(reverse_kwargs(a=1, b=2))  # Expected: {1: 'a', 2: 'b'}


""" 
Problem: 1389  
Write a Python function that returns the longest key in **kwargs.
"""
def longest_key(**kwargs):
    return max(kwargs, key=len)

print(longest_key(short=1, muchlonger=2))  # Expected: 'muchlonger'


""" 
Problem: 1390  
Write a Python function that creates a string from **kwargs as key=value pairs joined by commas.
"""
def stringify_kwargs(**kwargs):
    return ', '.join(f"{k}={v}" for k, v in kwargs.items())

print(stringify_kwargs(x=10, y=20))  # Expected: "x=10, y=20"


""" 
Problem: 1391  
Write a Python function that checks if all values in **kwargs are integers.
"""
def all_ints(**kwargs):
    return all(isinstance(v, int) for v in kwargs.values())

print(all_ints(a=1, b=2))  # Expected: True


""" 
Problem: 1392  
Write a Python function that finds and returns the maximum numeric value in **kwargs.
"""
def max_numeric(**kwargs):
    nums = [v for v in kwargs.values() if isinstance(v, (int, float))]
    return max(nums) if nums else None

print(max_numeric(a=1, b=3.5, c="x"))  # Expected: 3.5


""" 
Problem: 1393  
Write a Python function that counts the keyword arguments whose value is None.
"""
def count_none(**kwargs):
    return sum(1 for v in kwargs.values() if v is None)

print(count_none(a=None, b=1, c=None))  # Expected: 2


""" 
Problem: 1394  
Write a Python function that prints the types of values in **kwargs.
"""
def print_types(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {type(v).__name__}")

print_types(a=1, b="str", c=3.14)
# Expected:
# a: int
# b: str
# c: float


""" 
Problem: 1395  
Write a Python function that creates a list of key-value pairs (tuples) from **kwargs.
"""
def kv_pairs(**kwargs):
    return list(kwargs.items())

print(kv_pairs(a=1, b=2))  # Expected: [('a', 1), ('b', 2)]


""" 
Problem: 1396  
Write a Python function that filters out keyword arguments with falsy values.
"""
def remove_falsy(**kwargs):
    return {k: v for k, v in kwargs.items() if v}

print(remove_falsy(a=0, b=1, c=""))  # Expected: {'b': 1}


""" 
Problem: 1397  
Write a Python function that returns True if at least one value in **kwargs is a list.
"""
def has_list(**kwargs):
    return any(isinstance(v, list) for v in kwargs.values())

print(has_list(a=[1,2], b="x"))  # Expected: True


""" 
Problem: 1398  
Write a Python function that prints whether the number of keyword arguments is even or odd.
"""
def even_or_odd_kwargs(**kwargs):
    print("Even" if len(kwargs) % 2 == 0 else "Odd")

even_or_odd_kwargs(a=1, b=2, c=3)  # Expected: Odd


""" 
Problem: 1399  
Write a Python function that accepts **kwargs and renames any keys that start with 'temp_' by removing the prefix.
"""
def clean_temp_keys(**kwargs):
    return {k[5:] if k.startswith('temp_') else k: v for k, v in kwargs.items()}

print(clean_temp_keys(temp_x=1, y=2))  # Expected: {'x': 1, 'y': 2}


""" 
Problem: 1400  
Write a Python function that accepts **kwargs and returns only those key-value pairs where the key is uppercase.
"""
def uppercase_keys_only(**kwargs):
    return {k: v for k, v in kwargs.items() if k.isupper()}

print(uppercase_keys_only(AGE=30, name="Ann"))  # Expected: {'AGE': 30}

""" 
Problem: 1402  
Write a Pythonic way to use `enumerate()` to get both index and value from a list.
"""
fruits = ['apple', 'banana', 'cherry']
for index, value in enumerate(fruits):
    print(f"{index}: {value}")  # Expected: 0: apple, 1: banana, 2: cherry


""" 
Problem: 1403  
Write a Pythonic way to use `zip()` to combine two lists into a list of tuples.
"""
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
combined = list(zip(names, ages))
print(combined)  # Expected: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]


""" 
Problem: 1404  
Write a Pythonic way to use a dictionary comprehension to swap keys and values.
"""
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in original.items()}
print(swapped)  # Expected: {1: 'a', 2: 'b', 3: 'c'}


""" 
Problem: 1405  
Write a Pythonic way to use `all()` to check if all elements in a list satisfy a condition.
"""
numbers = [2, 4, 6, 8]
all_even = all(x % 2 == 0 for x in numbers)
print(all_even)  # Expected: True


""" 
Problem: 1406  
Write a Pythonic way to flatten a list of lists using a list comprehension.
"""
nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flattened = [item for sublist in nested for item in sublist]
print(flattened)  # Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9]


""" 
Problem: 1407  
Write a Pythonic way to use `map()` to convert a list of strings to uppercase.
"""
words = ['hello', 'world', 'python']
uppercase_words = list(map(str.upper, words))
print(uppercase_words)  # Expected: ['HELLO', 'WORLD', 'PYTHON']


""" 
Problem: 1408  
Write a Pythonic way to use `filter()` with a lambda to get even numbers from a list.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Expected: [2, 4, 6, 8, 10]


""" 
Problem: 1409  
Write a Pythonic way to use `set()` to remove duplicates from a list while preserving order using dict.fromkeys().
"""
items = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique_ordered = list(dict.fromkeys(items))
print(unique_ordered)  # Expected: [1, 2, 3, 4, 5]


""" 
Problem: 1410  
Write a Pythonic way to use `str.join()` to concatenate a list of strings with a separator.
"""
words = ['Python', 'is', 'great']
sentence = ' '.join(words)
print(sentence)  # Expected: Python is great


""" 
Problem: 1411  
Write a Pythonic way to use list slicing to reverse a string.
"""
text = "Python"
reversed_text = text[::-1]
print(reversed_text)  # Expected: nohtyP


""" 
Problem: 1412  
Write a Pythonic way to use `collections.Counter` to count character frequencies in a string.
"""
from collections import Counter
text = "hello world"
char_counts = Counter(text)
print(char_counts)  # Expected: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})


""" 
Problem: 1413  
Write a Pythonic way to use `itertools.chain()` to combine multiple lists into one.
"""
from itertools import chain
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
combined = list(chain(list1, list2, list3))
print(combined)  # Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9]


""" 
Problem: 1414  
Write a Pythonic way to use `str.split()` and list comprehension to capitalize each word.
"""
text = "hello world python"
capitalized = ' '.join(word.capitalize() for word in text.split())
print(capitalized)  # Expected: Hello World Python


""" 
Problem: 1415  
Write a Pythonic way to use `zip()` with `*` to transpose a list of lists.
"""
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = list(zip(*matrix))
print(transposed)  # Expected: [(1, 4, 7), (2, 5, 8), (3, 6, 9)]


""" 
Problem: 1416  
Write a Pythonic way to use `dict.get()` with a default value to safely access dictionary keys.
"""
data = {'name': 'Alice', 'age': 30}
name = data.get('name', 'Unknown')
city = data.get('city', 'Unknown')
print(name, city)  # Expected: Alice Unknown


""" 
Problem: 1417  
Write a Pythonic way to use `collections.defaultdict` to group items by a key.
"""
from collections import defaultdict
items = [('fruit', 'apple'), ('fruit', 'banana'), ('vegetable', 'carrot'), ('fruit', 'cherry')]
grouped = defaultdict(list)
for category, item in items:
    grouped[category].append(item)
print(dict(grouped))  # Expected: {'fruit': ['apple', 'banana', 'cherry'], 'vegetable': ['carrot']}


""" 
Problem: 1418  
Write a Pythonic way to use `itertools.groupby()` to group consecutive identical elements.
"""
from itertools import groupby
data = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4]
grouped = {k: list(g) for k, g in groupby(data)}
print(grouped)  # Expected: {1: [1, 1, 1], 2: [2, 2], 3: [3, 3, 3, 3], 4: [4]}


""" 
Problem: 1419  
Write a Pythonic way to use `str.maketrans()` and `str.translate()` to replace multiple characters.
"""
text = "hello world"
translation = str.maketrans('lo', '12')
result = text.translate(translation)
print(result)  # Expected: he112 w2r1d


""" 
Problem: 1420  
Write a Pythonic way to use `frozenset()` to create an immutable set for use as a dictionary key.
"""
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([4, 5, 6])
mapping = {fs1: 'first', fs2: 'second'}
print(mapping[fs1])  # Expected: first


""" 
Problem: 1421  
Write a Pythonic way to use `itertools.combinations()` to generate all pairs from a list.
"""
from itertools import combinations
items = ['a', 'b', 'c', 'd']
pairs = list(combinations(items, 2))
print(pairs)  # Expected: [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')]


""" 
Problem: 1422  
Write a Pythonic way to use `collections.deque` to implement a queue with append and popleft.
"""
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
first = queue.popleft()
print(first, list(queue))  # Expected: 1 [2, 3]


""" 
Problem: 1423  
Write a Pythonic way to use `str.partition()` to split a string at the first occurrence of a delimiter.
"""
text = "hello:world:python"
before, sep, after = text.partition(':')
print(before, after)  # Expected: hello world:python


""" 
Problem: 1424  
Write a Pythonic way to use `operator.itemgetter()` to sort a list of dictionaries by a key.
"""
from operator import itemgetter
people = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
sorted_people = sorted(people, key=itemgetter('age'))
print(sorted_people)  # Expected: [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]


""" 
Problem: 1425  
Write a Pythonic way to use `contextlib.suppress()` to ignore specific exceptions.
"""
from contextlib import suppress
with suppress(ValueError, ZeroDivisionError):
    result = int("not a number")  # This would raise ValueError, but it's suppressed
    print("This won't print")
print("Continues after exception")  # Expected: Continues after exception


""" 
Problem: 1426  
Write a Pythonic way to check if any item in a list is true.
"""
lst = [0, False, 5]
print(any(lst))  # Expected: True


""" 
Problem: 1427  
Write a Pythonic way to use a generator expression to calculate the sum of squares.
"""
lst = [1, 2, 3]
total = sum(x**2 for x in lst)
print(total)  # Expected: 14


""" 
Problem: 1428  
Write a Pythonic program to get the intersection of two sets.
"""
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)  # Expected: {2, 3}


""" 
Problem: 1429  
Write a Pythonic program to get the union of two sets.
"""
print(a | b)  # Expected: {1, 2, 3, 4}


""" 
Problem: 1430  
Write a Pythonic way to check if a string contains only digits.
"""
s = "12345"
print(s.isdigit())  # Expected: True


""" 
Problem: 1431  
Write a Pythonic one-liner to reverse a list.
"""
lst = [1, 2, 3]
print(lst[::-1])  # Expected: [3, 2, 1]


""" 
Problem: 1432  
Write a Pythonic way to zip dictionary keys and values into a list of tuples.
"""
d = {'a': 1, 'b': 2}
zipped = list(zip(d.keys(), d.values()))
print(zipped)  # Expected: [('a', 1), ('b', 2)]


""" 
Problem: 1433  
Write a Pythonic way to initialize a dictionary with default integer values.
"""
from collections import defaultdict
d = defaultdict(int)
d["x"] += 1
print(d["x"])  # Expected: 1


""" 
Problem: 1434  
Write a Pythonic program to group elements by length from a list of words.
"""
words = ["hi", "hello", "yes", "no"]
from collections import defaultdict
grouped = defaultdict(list)
for word in words:
    grouped[len(word)].append(word)
print(dict(grouped))  # Expected: {2: ['hi', 'no'], 5: ['hello'], 3: ['yes']}


""" 
Problem: 1435  
Write a Pythonic program to sort a list of tuples by the second item.
"""
lst = [(1, 3), (2, 1), (4, 2)]
sorted_lst = sorted(lst, key=lambda x: x[1])
print(sorted_lst)  # Expected: [(2, 1), (4, 2), (1, 3)]


""" 
Problem: 1436  
Write a Pythonic way to use a context manager to read a file.
"""
# Simulated context manager example
with open("temp.txt", "w") as f:
    f.write("Hello")
with open("temp.txt") as f:
    print(f.read())  # Expected: "Hello"


""" 
Problem: 1437  
Write a Pythonic one-liner to find the maximum item in a list.
"""
lst = [1, 5, 2]
print(max(lst))  # Expected: 5


""" 
Problem: 1438  
Write a Pythonic way to assign multiple variables from a list.
"""
lst = [1, 2, 3]
a, b, c = lst
print(a, b, c)  # Expected: 1 2 3


""" 
Problem: 1439  
Write a Pythonic way to create a dictionary from two lists.
"""
keys = ['a', 'b']
values = [1, 2]
d = dict(zip(keys, values))
print(d)  # Expected: {'a': 1, 'b': 2}


""" 
Problem: 1440  
Write a Pythonic way to remove a key from a dictionary if it exists.
"""
d = {'a': 1, 'b': 2}
d.pop('b', None)
print(d)  # Expected: {'a': 1}


""" 
Problem: 1441  
Write a Pythonic way to check if a variable is None.
"""
x = None
print(x is None)  # Expected: True


""" 
Problem: 1442  
Write a Pythonic way to handle a missing dictionary key using try-except.
"""
d = {'a': 1}
try:
    print(d['b'])
except KeyError:
    print("Key not found")  # Expected: Key not found


""" 
Problem: 1443  
Write a Pythonic way to unpack a tuple into variables.
"""
t = (1, 2)
x, y = t
print(x, y)  # Expected: 1 2


""" 
Problem: 1444  
Write a Pythonic one-liner to check if a list contains duplicates.
"""
lst = [1, 2, 2]
print(len(lst) != len(set(lst)))  # Expected: True


""" 
Problem: 1445  
Write a Pythonic program to count character frequencies in a string.
"""
s = "banana"
freq = Counter(s)
print(freq)  # Expected: {'b': 1, 'a': 3, 'n': 2}


""" 
Problem: 1446  
Write a Pythonic one-liner to filter out negative numbers from a list.
"""
lst = [1, -2, 3, -4]
print([x for x in lst if x >= 0])  # Expected: [1, 3]


""" 
Problem: 1447  
Write a Pythonic way to test if a list has at least one even number.
"""
lst = [1, 3, 4]
print(any(x % 2 == 0 for x in lst))  # Expected: True


""" 
Problem: 1448  
Write a Pythonic way to get the index of an item in a list.
"""
lst = ['a', 'b', 'c']
print(lst.index('b'))  # Expected: 1


""" 
Problem: 1449  
Write a Pythonic way to filter dictionary items with values > 10.
"""
d = {'a': 5, 'b': 15}
filtered = {k: v for k, v in d.items() if v > 10}
print(filtered)  # Expected: {'b': 15}


""" 
Problem: 1450  
Write a Pythonic program to invert a dictionary (keys become values, values become keys).
"""
d = {'a': 1, 'b': 2}
inverted = {v: k for k, v in d.items()}
print(inverted)  # Expected: {1: 'a', 2: 'b'}

""" 
Problem: 1451  
Write a Python program using `all()` to check if all numbers in a list are positive.
"""
lst = [1, 2, 3, 4]
print(all(x > 0 for x in lst))  # Expected: True


""" 
Problem: 1452  
Use `all()` to determine if all characters in a string are lowercase.
"""
s = "hello"
print(all(c.islower() for c in s))  # Expected: True


""" 
Problem: 1453  
Write a Pythonic way to use `all()` to check if all elements in a list are even.
"""
lst = [2, 4, 6]
print(all(x % 2 == 0 for x in lst))  # Expected: True


""" 
Problem: 1454  
Check if all items in a dictionary have non-empty values using `all()`.
"""
d = {"a": 1, "b": "hello", "c": [1]}
print(all(bool(v) for v in d.values()))  # Expected: True


""" 
Problem: 1455  
Use `all()` to check if all items in a set are greater than 10.
"""
s = {11, 12, 13}
print(all(x > 10 for x in s))  # Expected: True


""" 
Problem: 1456  
Use `all()` to validate that all lines in a list start with a capital letter.
"""
lines = ["Hello", "World", "Python"]
print(all(line[0].isupper() for line in lines))  # Expected: True


""" 
Problem: 1457  
Use `all()` to check if all elements in a matrix row are equal.
"""
row = [5, 5, 5]
print(all(x == row[0] for x in row))  # Expected: True


""" 
Problem: 1458  
Use `all()` to check if all values in a list are strings.
"""
lst = ["a", "b", "c"]
print(all(isinstance(x, str) for x in lst))  # Expected: True


""" 
Problem: 1459  
Write a Python program that uses `all()` to check if all keys in a dictionary are strings.
"""
d = {"a": 1, "b": 2}
print(all(isinstance(k, str) for k in d.keys()))  # Expected: True


""" 
Problem: 1460  
Use `all()` to verify that all files have a ".txt" extension.
"""
files = ["doc1.txt", "doc2.txt"]
print(all(f.endswith(".txt") for f in files))  # Expected: True


""" 
Problem: 1461  
Use `all()` to check if all numbers in a list are within a certain range.
"""
nums = [5, 6, 7]
print(all(1 <= x <= 10 for x in nums))  # Expected: True


""" 
Problem: 1462  
Check if all sublists in a 2D list are non-empty using `all()`.
"""
matrix = [[1], [2], [3]]
print(all(len(sublist) > 0 for sublist in matrix))  # Expected: True


""" 
Problem: 1463  
Use `all()` to confirm all booleans in a list are True.
"""
flags = [True, True, True]
print(all(flags))  # Expected: True


""" 
Problem: 1464  
Use `all()` to verify all words in a list contain the letter "a".
"""
words = ["apple", "banana", "grape"]
print(all("a" in word for word in words))  # Expected: True


""" 
Problem: 1465  
Write a Python program using `all()` to check if a list of numbers is strictly increasing.
"""
nums = [1, 2, 3, 4]
print(all(x < y for x, y in zip(nums, nums[1:])))  # Expected: True


""" 
Problem: 1466  
Check if all environment variables in a list are defined (non-empty strings).
"""
envs = ["PATH", "HOME", "USER"]
print(all(isinstance(env, str) and env for env in envs))  # Expected: True


""" 
Problem: 1467  
Use `all()` to ensure all items in a tuple are of the same type.
"""
t = (1, 2, 3)
print(all(type(x) == type(t[0]) for x in t))  # Expected: True


""" 
Problem: 1468  
Check if all numbers in a list are prime using `all()` and a helper function.
"""
def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1))

lst = [2, 3, 5, 7]
print(all(is_prime(x) for x in lst))  # Expected: True


""" 
Problem: 1469  
Use `all()` to confirm all values in a list are not None.
"""
lst = [1, 2, 3]
print(all(x is not None for x in lst))  # Expected: True


""" 
Problem: 1470  
Use `all()` to verify that all passwords in a list are at least 8 characters long.
"""
passwords = ["abcdefgh", "12345678", "password"]
print(all(len(p) >= 8 for p in passwords))  # Expected: True

""" 
Problem: 1471  
Write a Python program to check if a variable is `None` using `is`.
"""
x = None
print(x is None)  # Expected: True


""" 
Problem: 1472  
Check if two variables point to the same list object using `is`.
"""
a = []
b = a
print(a is b)  # Expected: True


""" 
Problem: 1473  
Check if two separately created lists are not the same object using `is`.
"""
a = []
b = []
print(a is not b)  # Expected: True


""" 
Problem: 1474  
Use `is` to check if a variable is exactly `True`.
"""
flag = True
print(flag is True)  # Expected: True


""" 
Problem: 1475  
Use `is` to check identity of two strings (interned strings).
"""
s1 = "hello"
s2 = "hello"
print(s1 is s2)  # Expected: True (implementation detail in CPython)


""" 
Problem: 1476  
Use `is` to check identity of small integers.
"""
a = 100
b = 100
print(a is b)  # Expected: True (due to integer caching)


""" 
Problem: 1477  
Check if a function return value is `None` using `is`.
"""
def do_nothing():
    pass

print(do_nothing() is None)  # Expected: True


""" 
Problem: 1478  
Use `is` to check if a class attribute is shared.
"""
class A:
    x = []

a1 = A()
a2 = A()
print(a1.x is a2.x)  # Expected: True


""" 
Problem: 1479  
Use `is` to check if an object is the same before and after a function call.
"""
def identity(x):
    return x

obj = []
print(obj is identity(obj))  # Expected: True


""" 
Problem: 1480  
Use `is` to compare with built-in singleton `Ellipsis`.
"""
x = ...
print(x is Ellipsis)  # Expected: True


""" 
Problem: 1481  
Check if two instances of a class are not the same object.
"""
class X:
    pass

x1 = X()
x2 = X()
print(x1 is not x2)  # Expected: True


""" 
Problem: 1482  
Check identity of two variables referencing the same dictionary.
"""
d1 = {"a": 1}
d2 = d1
print(d1 is d2)  # Expected: True


""" 
Problem: 1483  
Use `is` in an assertion to verify object identity.
"""
a = b = object()
assert a is b
print("Assertion passed")  # Expected: Assertion passed

""" 
Problem: 1484  
Compare identity of two Boolean values using `is`.
"""
x = (2 < 3)
y = True
print(x is y)  # Expected: True


""" 
Problem: 1485  
Use `is not` to verify a function argument is not None.
"""
def greet(name):
    if name is not None:
        print(f"Hello, {name}!")

greet("Alice")  # Expected: Hello, Alice!


""" 
Problem: 1486  
Use `is` to test if a global constant is unchanged.
"""
SENTINEL = object()
def check(x):
    return x is SENTINEL

value = SENTINEL
print(check(value))  # Expected: True


""" 
Problem: 1487  
Check that changing a variable makes it no longer the same object.
"""
a = [1, 2]
b = a
a = [1, 2]
print(a is b)  # Expected: False


""" 
Problem: 1488  
Use `is` to compare with a constant declared elsewhere.
"""
NONE_CONST = None
x = None
print(x is NONE_CONST)  # Expected: True


""" 
Problem: 1489  
Use `is` with `not` to check that a value is not `False`.
"""
value = "some text"
print(value is not False)  # Expected: True


""" 
Problem: 1490  
Show that identity and equality are not always the same.
"""
a = [1]
b = [1]
print(a == b)   # Expected: True
print(a is b)   # Expected: False

""" 
Problem: 1491  
Use `default=` with the `max()` function to return a default when the list is empty.
"""
nums = []
print(max(nums, default=0))  # Expected: 0


""" 
Problem: 1492  
Use `default=` with the `min()` function to avoid an error on an empty sequence.
"""
values = []
print(min(values, default=-1))  # Expected: -1


""" 
Problem: 1493  
Use `default=` in `max()` to safely get the longest word from a list.
"""
words = []
print(max(words, key=len, default="None"))  # Expected: "None"


""" 
Problem: 1494  
Use `default=` with `next()` to get the first even number or -1.
"""
lst = [1, 3, 5]
print(next((x for x in lst if x % 2 == 0), default=-1))  # Expected: -1


""" 
Problem: 1495  
Use `default=` in `next()` to safely access an item in a generator.
"""
gen = (x for x in range(5) if x > 10)
print(next(gen, default="No item"))  # Expected: "No item"


""" 
Problem: 1496  
Use `default=` with `max()` on a filtered list to handle no matches.
"""
nums = [1, 3, 5]
print(max((x for x in nums if x % 2 == 0), default=None))  # Expected: None


""" 
Problem: 1497  
Use `default=` in `min()` to get a fallback value when no condition matches.
"""
nums = [1, 3, 5]
print(min((x for x in nums if x % 2 == 0), default=-1))  # Expected: -1


""" 
Problem: 1498  
Use `default=` with `next()` to find the first name starting with "Z".
"""
names = ["Alice", "Bob"]
print(next((name for name in names if name.startswith("Z")), default="Not found"))  # Expected: "Not found"


""" 
Problem: 1499  
Use `default=` with `max()` to find the max in a sublist or return a placeholder.
"""
data = []
print(max(data, default="empty"))  # Expected: "empty"


""" 
Problem: 1500  
Use `default=` in `next()` to handle an empty comprehension.
"""
print(next((x for x in []), default="Empty"))  # Expected: "Empty"






