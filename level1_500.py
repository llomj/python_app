#function problems level 1 (chatGPT￼) 

"""
Problem 1:
Write a Python function called `add_numbers` that takes two numbers as parameters and returns their sum.
"""

def add_number(a, b):
    return a + b
    
print(add_number(5, 5))  # Output: 10
    
def add_num(a, b):
    result = a + b
    return result
    
print(add_num(5, 5))  # Output: 10

"""
Problem 2:
Write a Python function called `multiply_numbers` that takes two numbers as parameters and returns their product.
"""

def multiply_numbers(a, b):
    return a * b
    
print(multiply_numbers(5, 5))  # Output: 25

"""
Problem 3:
Write a Python function called `find_max` that takes a list of numbers as input and returns the maximum number in the list.
"""

def find_max(number):
    return max(number)

result = [2, 67, 300]    
print(find_max(result))  # Output: 300
        
def find_max(numbers):
    max_number = numbers[0]
    
    for num in numbers:
        if num > max_number:
            max_number = num  # Update max_number to the new maximum
    return max_number
    
numbers_list = [5, 100, 3, 8, 15]
print("The maximum number in the list is:", find_max(numbers_list))  # Output: The maximum number in the list is: 100

"""
Problem 4:
Write a Python function called `calculate_average` that takes a list of numbers as input and returns the average of those numbers. Use sum() and len().
"""

def calculate_average(number):
    result = sum(number) / len(number)
    return result
    
lst = [1, 67, 888]
print(calculate_average(lst))  # Output: 318.6666666666667
    
def cal_average(number):
    result = sum(number) / len(number)
    
    return result  # Return the average
    
lst = [44,67,54]    
print(cal_average(lst))  # Output: 55.0

"""
Problem 5:
Write a Python function called `count_vowels` that takes a string as input and returns the count of vowels (a, e, i, o, u) in the string. Ignore case sensitivity.
"""

def count_vowels(string):
    count = 0
    
    for char in string:
        if char in "aeiou":
            count += 1  # Increment counter if vowel found
    return count
    
result = "Jonathan"
print(count_vowels(result))  # Output: 3

"""
Problem 6:
Write a Python function called `reverse_string` that takes a string as input and returns the reverse of that string.
"""
    
def reverse_string(string):
    string = string[::-1]
    
    return string  # Return the reversed string
    
result = "Jonathan"
print(reverse_string(result))  # Output: nahtanoJ
    
"""
Problem 7:
Write a Python function called `is_even` that takes an integer as input and returns True if the number is even, and False otherwise.
"""

def is_even(number):
    return number % 2 == 0
               
result = 10        
print(is_even(result))  # Output: True

"""
Problem 8:
Write a Python function called `calculate_square` that takes a number as input and returns the square of that number.
"""

def cal_square(number):
    return number ** number
       
lst = 9
print(cal_square(lst))  # Output: 387420489 (incorrect - should be 81)

def calculate_sqaure(number):
    square = number * number
    
    return square  # Return the squared value
    
print(calculate_sqaure(6))  # Output: 36

"""
Problem 9:
Write a Python function called `greet_user` that takes a string `name` as input and prints a greeting message in the format "Hello, [name]!".
"""

def greet_user(string):
    return f"hello {string}"  # Returns formatted greeting string
        
print(greet_user("Jonathan"))  # Output: hello Jonathan

"""
Problem 10:
Write a Python function called `square_list` that takes a list of numbers as input and returns a new list with each number squared.
"""

def square_lst(numbers):
    squared_numbers = []
    
    for number in numbers:
        squared_numbers.append(number ** 2)
    return squared_numbers
    
result = [2, 4, 5, 6]
print(square_lst(result))  # Output: [4, 16, 25, 36]

"""
Problem 11:
Write a Python function called `convert_to_uppercase` that takes a string as input and returns the string with all its characters converted to uppercase.
"""

def covert_uppercase(string):
    return string.upper()  # Returns uppercase version of the string
    
print(covert_uppercase("Jonathan"))  # Output: JONATHAN

"""
Problem 12:
Write a Python function called `calculate_sum` that takes a list of numbers as input and returns the sum of all the numbers in the list.
"""

def calculate_sum(number):
    return sum(number)

lst = [1, 56, 778]    
print(calculate_sum(lst))  # Output: 835

def cal_sum(numbers):
    count = 0
    
    for number in numbers:
        count += number  # Add current number to the running total
    return count  # Return the final sum
    
lst = [1, 56, 778]
print(cal_sum(lst))  # Output: 835

"""
Problem 13:
Write a Python function called `is_odd` that takes an integer as input and returns True if the number is odd, and False otherwise.
"""

def is_odd(number):
    return number % 2 == 0  # This returns True for even numbers (WRONG!)

print(is_odd(10))  # Output: True (INCORRECT - 10 is even, not odd!)

"""
Problem 14:
Write a Python function called `concatenate_strings` that takes two strings as input and returns a new string that is the concatenation of the two input strings.
"""

def concatenate_strings(string1, string2):
    concatenate = string1 + string2  # Join string1 and string2
    return concatenate  # Return the concatenated string
       
lst1 = "Jonathan"
lst2 = "moll"
print(concatenate_strings(lst1, lst2))  # Output: Jonathanmoll

def concatenate_string(string1, string2):
    return string1 + string2  # Returns string1 followed by string2
    
print(concatenate_string("Jonathan", "moll"))  # Output: Jonathanmoll

"""
Problem 15:
Write a Python function called `find_length` that takes a string as input and returns the length of that string.
"""

def find_length(string):
    return len(string)

print(find_length("Jonathan"))  # Output: 8

def find_len(string):
    count = 0
    
    for char in string:
        count += 1  # Increment counter for each character found
    return count
        
print(find_len("Jonathan"))  # Output: 8

"""
Problem 16:
Write a Python function called `is_palindrome` that takes a string as input and returns True if the string is a palindrome (reads the same forwards and backwards), and False otherwise.
"""

def is_palindrome(string):
    string = string.replace(" ", "").lower()  # Remove spaces, convert to lowercase
    
    return string == string[::-1]  # Returns True if palindrome, False otherwise
    
# Normalized: "tom", Reversed: "mot"
print(is_palindrome("tom"))  # Output: False

"""
Problem 17:
Write a Python function called `count_words` that takes a string as input and returns the number of words in the string. Assume that words are separated by spaces.
"""

def count_words(string):
    words = string.split()
    word_count = 0  # Initialize counter
    
    for word in words:
        word_count += 1  # Count each word
    
    return word_count

example_string = "This is an example sentence."
print(count_words(example_string))  # Output: 5

def count_words(string):
    words = string.split()  # Split string into list of words
    return len(words)  # Return the length of the list (word count)

example_string = "This is an example sentence."
print(count_words(example_string))  # Output: 5

def count_words(string):
    count = 0  # Initialize counter
    for char in string:
        if char == char.replace(" ",""):  # This condition is always True
            count += 1  # Increments for every character
    return count  # Returns character count, not word count (WRONG!)
               
arg = "hello you cunt"
print(count_words(arg))  # Output: 15 (INCORRECT - should be 3 words!)

"""
Problem 18:
Write a Python function called `find_min` that takes a list of numbers as an input argument and returns the minimum number in the list.
"""

def find_min():
    user = input("type number: ").split()
    int_number = []  # List to store converted integers
    for number in user:
        int_number.append(int(number))
        
    min_num = sorted(int_number)[0]
    for number in int_number:
        if min_num < 0:  # BUG: This condition is wrong
            min_num = number
    print(min_num)  # Print the result
    
find_min()  # Call the function

def find_min(numbers):
    return min(numbers)

lst = [1, 56, 68]
print(find_min(lst))  # Output: 1

def find_minimum(numbers):
    min_number = numbers[0]
    
    for number in numbers:
        if number < min_number:
            min_number = number  # Update min_number to the new minimum
    return min_number  # Return the minimum value found
    
min_number = [45, 6, 1]
print(find_minimum(min_number))  # Output: 1
        
"""
Problem 19:
Write a Python function called `is_even_index_sum` that takes a list of numbers as input and returns True if the sum of the numbers at even indices is even, and False otherwise. Assume that the first index is considered as index 0.
"""

def is_even_index_sum(numbers):
    even_index_sum = 0
    
    for i in range(len(numbers)):
        if i % 2 == 0:
            even_index_sum += numbers[i]  # Add element at even index to sum
    
    return even_index_sum % 2 == 0  # Returns True if sum is even, False if odd

# Even indices: 0 (100), 2 (300)
# Sum: 100 + 300 = 400
lst = [100, 200, 300, 400]
print(is_even_index_sum(lst))  # Output: True

"""
Problem 20:
Write a Python function called `double_elements` that takes a list of numbers as input and returns a new list where each element is doubled.
"""

def double_elements(elements):
    doubled = []
    
    for element in elements:
        doubled.append(element)  # Add element once
        doubled.append(element)  # Add element again (duplication, not doubling!)
        
    return doubled  # Returns list with duplicated elements

lst = ["tree", "shop", "car"]
print(double_elements(lst))  # Output: ['tree', 'tree', 'shop', 'shop', 'car', 'car']

def double_elements(numbers):
    doubled_numbers = []
    
    for num in numbers:
        doubled_numbers.append(num * 2)  # Multiply by 2 and append
    
    return doubled_numbers  # Return list with doubled values

numbers_list = [1, 2, 3, 4, 5]
print("The list with doubled elements is:", double_elements(numbers_list))  # Output: [2, 4, 6, 8, 10]
    
"""
Problem 21:
Write a Python function called `is_all_positive` that takes a list of numbers as input and returns True if all the numbers in the list are positive (greater than zero), and False otherwise.
"""

def is_all_positive(numbers):
    for number in numbers:
        if number <= 0:
            return False  # Found a non-positive number, return False immediately
    return True  # All numbers passed the positive check
              
lst = [0, 6, 8]
print(is_all_positive(lst))  # Output: False

"""
Problem 22:
Write a Python function called `find_average` that takes a list of numbers as input and returns the average of those numbers.
"""

def find_average(numbers):
    total_average = sum(numbers) / len(numbers)
    return total_average
    
lst = [4, 67, 77,]
print(find_average(lst))  # Output: 49.333333333333336

def find_average_lst(numbers):
    total = 0
    count = 0  # Initialize counter
    
    for number in numbers:
        total += number  # Add to running total
        count += 1  # Increment counter
        
    if count > 0:
        average = total / count  # Calculate average
    return average  # BUG: 'average' might not be defined if count == 0
        
lst = [1, 56, 66]
print(find_average_lst(lst))  # Output: 41.0

def find_average_lst(numbers):
    total = 0
    count = 0  # Initialize counter
    
    for number in numbers:
        total += number  # Add to running total
        count += 1  # Increment counter
        
    average = total / count  # Could cause ZeroDivisionError if list is empty
    return average  # Return the average
        
lst = [1, 56, 66]
print(find_average_lst(lst))  # Output: 41.0

"""
Problem 23:
Write a Python function called `contains_negative` that takes a list of numbers as input and returns True if the list contains any negative number, and False otherwise.
"""

def contains_negative(numbers):
    for number in numbers:
        if number <= 0:  # This incorrectly treats 0 as negative
            return True  # Return True immediately if found
    return False  # Return False if no negative numbers found

lst = [5, -9]    
print(contains_negative(lst))  # Output: True (correct for this case, but buggy logic)

"""
Problem 24:
Write a Python function called `find_last_element` that takes a list if numbers and returns the last number of the list.
"""

def find_last_element(string):
    return string[-1]
    
lst = [1, 45, 66]
print(find_last_element(lst))  # Output: 66

def find_element(elements):
    last = elements[-1]
    
    for element in elements:
        if element == last:
            return last  # Return the last element
    
lst = [1,5]
print(find_element(lst))  # Output: 5

"""
Problem 25:
Write a Python function called `multiply_elements` that takes a list of numbers as input and returns the product of all the numbers in the list.
"""

def multiply_elements(numbers):
    count = 1
    
    for i in range(len(numbers)):
        count *= numbers[i]  # Multiply current element with running product
    return count  # Return the final product
        
arg = [2, 4, 2]
print(multiply_elements(arg))  # Output: 16

def multiply_elements(numbers):
    count = 1
    
    for number in numbers:
        count *= number  # Multiply each number with running product
    return count  # Return the final product
    
lst = [100, 200, 900]
print(multiply_elements(lst))  # Output: 18000000

def multiply_elements(numbers):
    count = 1  # Initialize to 1
    
    for number in numbers:
        count *= number
    
    for number in numbers:
        count *= number
    
    return count  # Returns squared product (INCORRECT!)

arg = [2, 4, 2]
print(multiply_elements(arg))  # Output: 256 (INCORRECT - should be 16)
        
"""
Problem 26:
Write a Python function called `has_duplicates` that takes a list as input and returns True if the list contains any duplicate elements, and False otherwise.
"""

def has_duplicates(lst):
    unique = set()  # Set to track elements we've seen
    common = []
    
    for word in lst:
        if word in unique:
            common.append(word)  # Add to common list (optional)
            return True  # Found duplicate, return True immediately
        else:
            unique.add(word)  # Add to set of seen elements
    return False  # No duplicates found, return False
                
lst = ["it", "was", "itt"]
print(has_duplicates(lst))  # Output: False

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

"""
Problem 27:
Write a Python function called `count_occurrences` that takes a list and an element as input and returns the number of times the element appears in the list.
"""

def count_occurrences(elements, target):
    count = 0  # Initialize counter
    word = ""  # Variable to store the target word
    
    for element in elements:
        if element == target:
            word = element  # Store the matching element
            count += 1  # Increment counter
    return f"The word {word} occures {count} times"
               
elements = ["tree", "house", "tree", "car"]
target = "tree"
print(count_occurrences(elements, target))  # Output: The word tree occures 2 times

def count_occurrences(elements, target):
    count = 0  # Initialize counter
    
    for element in elements:
        if element == target:
            count += 1  # Increment for each match
    return count  # Return the count as an integer

list_elements = [1, 2, 3, 4, 5, 2, 2, 3]
target_element = 2

print(f"The element {target_element} appears {count_occurrences(list_elements, target_element)} times in the list.")  # Output: The element 2 appears 3 times in the list.
    
"""
Problem 28:
Write a Python function called `remove_vowels` that takes a string as input and returns a new string with all the vowels (a, e, i, o, u) removed.
"""

def remove_vowels(string):
    vowels = "aeiouAEIOU"  # Define vowels (both cases)
    result = ""
    
    for char in string:
        if char not in vowels:
            result += char  # Append non-vowel character
    return result  # Return string with vowels removed

# Original: J-o-n-a-t-h-a-n
# Vowels removed: o, a, a
lst = "Jonathan"
print(remove_vowels(lst))  # Output: Jnthn

def remove_vowels(string):
    vowels = "aeiou"  # Only lowercase vowels (missing uppercase)
    vowels_removed = []  # List to collect non-vowel characters
    
    for char in string:
        if char not in vowels:
            vowels_removed.append(char)  # Add to list
    return "".join(vowels_removed)  # Join list into string
            
lst = "Jonathan"
print(remove_vowels(lst))  # Output: Jnthn

"""
Problem 29:
Write a Python function called `capitalize_words` that takes a string as input and returns a new string with the first letter of each word capitalized. Assume that words are separated by spaces.
"""

def capitalize_words(sentence):
    words = sentence.split()  
    capitalized_words = []  # List to store capitalized words
    
    for word in words:
        capitalized_words.append(word.capitalize())  
    
    return ' '.join(capitalized_words) 

input_sentence = "hello world! this is a test."
print("Capitalized sentence:", capitalize_words(input_sentence))  # Hello World! This Is A Test.

"""
Problem 30:
Write a Python function called remove_spaces that takes a string as input and returns a new string with all spaces removed.
"""

def remove_spaces(sentence):
    return sentence.replace(" ", "")  # Returns string with spaces removed
    
arg = "suck me duck Jonathan"
print(remove_spaces(arg))  # Output: suckmeduckJonathan

def remove_space(string):
    space_removed = string.replace(" ", "")
    return space_removed  # Return string without spaces
    
lst = "what just happened" 
print(remove_space(lst))  # Output: whatjusthappened

def remove_spaces(sentence):
    split_word = sentence.split()
    result = []  # List to store words
    
    for word in split_word:
        result.append(word)  # Add word to list
    return "".join(result)  # Join words with no separator
    
arg = "suck me duck Jonathan"
print(remove_spaces(arg))  # Output: suckmeduckJonathan

"""
Problem 31:
Write a Python function called get_initials that takes a full name (first and last name) as input and returns the initials of the name in uppercase. For example, if the input is “John Doe”, the function should return “J.D.”.
"""

def get_initials(full_name):
    parts = full_name.split()
    
    initials = []
    
    for part in parts:
        initials.append(part[0].upper())  # Add uppercase first letter to list
        
    return '.'.join(initials) 

lst = "Jonathan moll"
print(get_initials(lst))  # Output: "J.M."

def get_initials(fullname):
    string = fullname.split()
    
    initials = f"{string[0][0].upper()}.{string[1][0].upper()}"
    return initials

string = "jonathan koll"
print(get_initials(string))  # Output: J.K

"""
Problem 32:
Write a Python function called reverse_words that takes a string as input and returns a new string with the words reversed. For example, if the input is “hello world”, the function should return “world hello”.
"""
def reverse_word(string):
    seperate = string.split()
    return seperate[::-1]
    
lst = "hello world"
print(reverse_word(lst))

def reverse_words(words):
    words = words.split()
    
    reversed_words = words[::-1]
    
    reversed_sentence = " ".join(reversed_words)
    
    return reversed_sentence

lst = "Jonathan moll"
print(reverse_words(lst))  # Output: moll Jonathan 

"""
Problem 33:
Write a Python function called `remove_duplicates` that takes a list as input and returns a new list with duplicate elements removed, while maintaining the original order of elements.
"""

def remove_duplicates(input_list):
    return list(set(input_list))  # Returns unique elements

input_list = [1, 2, 3, 1, 4, 2, 5]
print("List with duplicates removed:", remove_duplicates(input_list))  # Output: [1, 2, 3, 4, 5]

def remove_duplicates(input_list):
    unique_elements = []  # List to store unique elements in order
    
    for element in input_list:
        if element not in unique_elements:
            unique_elements.append(element)  # Add first occurrence
    return unique_elements  # Return list with duplicates removed, order preserved

input_list = [1, 2, 3, 1, 4, 2, 5]
print("List with duplicates removed:", remove_duplicates(input_list))  # Output: [1, 2, 3, 4, 5]
    
"""
Problem 34:
Write a Python function called find_longest_word that takes a string of words as input and returns the longest word in the list. If there are multiple longest words, return the first one encountered.
"""

def main(lst):
    return max(lst, key=len)
    
lst = ["tree", "cliff", "mountain", "tree","tree", "grassy"]
main(lst)  # Returns: "mountain"

def main(lst):
    largest_len = 0  # Track the length of the longest word found
    largest_word = ""  # Track the longest word itself
    
    for word in lst:
        if len(word) > largest_len:
            largest_len = len(word)  # Update the length
            largest_word = word  # Update the word
    return largest_word  # Return the longest word
        
lst = ["tree", "cliff", "mountain", "tree","tree", "grassy"]
main(lst)  # Returns: "mountain"

def find_longest_word(words):
    word_list = words.split()  # e.g., ["why", "dont", "you", "call", "Jonathan"]

    return max(word_list, key=len)  # Returns "Jonathan"

input_string = "why dont you call Jonathan"
print("Longest word:", find_longest_word(input_string))  # Output: Longest word: Jonathan

def find_longest_word(words):
    split_word = words.split()  # e.g., ["why", "dont", "Jonathanthebest", "finds", "top"]
    count = 0  # Track the length of the longest word
    longest_word = ""  # Track the longest word itself
    
    for word in split_word:
        if len(word) > count:
            count = len(word)  # Update length
            longest_word = word  # Update word
    return longest_word  # Return the longest word

input_string = "why dont Jonathanthebest finds top"
print("Longest word:", find_longest_word(input_string))  # Output: Longest word: Jonathanthebest

"""
Problem 35:
Write a Python function called find_vowels that takes a string as input and returns a list of vowels (a, e, i, o, u) present in the string. Ignore case sensitivity, meaning consider both uppercase and lowercase vowels.
"""

def find_vowels(string):
    vowels = "aeiou"  # Only lowercase vowels (missing uppercase)
    return_vowels = []  # List to store found vowels
    
    for char in string:
        if char in vowels:
            return_vowels += char  # Add vowel to list
    return return_vowels  # Return list of vowels found
            
lst = "Jonathan"
print(find_vowels(lst))  # Output: ['o', 'a', 'a']

def find_vowels(string):
    vowels = "aeiouAEIOU"  # Both lowercase and uppercase vowels
    vowel_list = []  # List to store found vowels
    
    for char in string:
        if char in vowels:
            vowel_list.append(char)  # Add vowel to list
    return vowel_list  # Return list of all vowels found

lst = "Jonathan"
print(find_vowels(lst))  # Output: ['o', 'a', 'a']

"""
Problem 36:
Write a Python function called `reverse_number` that takes an integer as input and returns the reverse of that number. For example, if the input is 123, the function should return 321.
"""

def reverse_number(number):
    return int(str(number)[::-1])  # Returns reversed number
    
number = 123
print(reverse_number(number))  # Output: 321

"""
Problem 37:
Write a Python function called remove_duplicates that takes a string as input and returns a new string with duplicate characters removed, while maintaining the original order of characters.
"""

def remove_duplicate(strings):
    return list(set(strings))  # Returns list, not string, and order may be lost
       
lst = "Jonathan"
print(remove_duplicate(lst))  # Output: ['J', 'o', 'n', 'a', 't', 'h'] (order may vary)

def remove_duplicates(string):
    unique_chars = []  # List to store unique characters in order
    
    for char in string:
        if char not in unique_chars:
            unique_chars.append(char)  # Add first occurrence
    return "".join(unique_chars)  # Return string with duplicates removed, order preserved

input_string = "Jonathan"
print(remove_duplicates(input_string))  # Output: Jonath

def remove_dupicates(numbers):
    duplicates = []  # List to store unique elements (note: variable name is misleading)
    
    for number in numbers:
        if number not in duplicates:
            duplicates.append(number)  # Add first occurrence
    return duplicates  # Return list with duplicates removed, order preserved
                 
lst = [3, 2, 2]
print(remove_dupicates(lst))  # Output: [3, 2]

"""
Problem: 38
Write a Python function called `sum_of_list` that takes a list of numbers as input and returns the sum of all the numbers in the list.
"""

def sum_of_list():
    user = input("type numbers: ").split()  # e.g., "1 2 3" → ["1", "2", "3"]
    int_number = []  # List to store converted integers
    
    for number in user:
        int_number.append(int(number))  # Convert "1" → 1, etc.
    
    count = 0
    for number in int_number:
        count += number  # Add current number to running total
    print(count)  # Print the result
    
sum_of_list()  # Call the function

"""
Problem 39:
Write a Python function called sum_of_list that takes a list of numbers as input and returns the sum of all the numbers in the list.
"""        

def sum_of_list(numbers):
    count = 0
    
    for number in numbers:
        count += number  # Add current number to running total
    return count  # Return the final sum

lst = [2, 2, 2]
print(sum_of_list(lst))  # Output: 6

"""
Problem 40:
Write a Python function called find_min_max that takes a list of numbers as input and returns a tuple containing the minimum and maximum numbers in the list.
"""

def find_min_max(numbers):
    min_number = numbers[0]  # Start with first element as minimum
    max_number = numbers[0]  # Start with first element as maximum
    
    for number in numbers:
        if number < min_number:
            min_number = number  # Found a new minimum
        if number > max_number:
            max_number = number  # Found a new maximum
    return min_number, max_number  # Returns (min, max)
       
# Minimum: 2, Maximum: 222
lst = [10, 90, 45, 55, 222, 2]
print(find_min_max(lst))  # Output: (2, 222)

"""
Problem 41:
Write a Python function called `count_occurrences` that takes a list and an element as input and returns the number of times the element appears in the list.
Did you complete the exercise? (y/n)
"""

def count_occurrences():
    user = input("type lst: ").split()  # e.g., ["Tom", "Jerry", "Tom"]
    count = 0  # Initialize counter
    
    for word in user:
        if word == "Tom":  # Only counts "Tom", not a general element
            count += 1  # Increment counter
    return count  # Return count
            
count_occurrences()  # Prompts user for input

"""
Problem 42:
Write a Python function called `table` that takes an integer `x` as input and prints the multiplication table for `x` from 0 to 10 (inclusive). Each line should show the multiplication of `x` with the number from 0 to 10 in the format `x * number = total`." 
"""

def table(x):
    result = ""
    
    for i in range(1, 11):  # Should be range(11) to include 0
        result += f"{i} x {x} = {i*x}\n"  # e.g., "1 x 6 = 6\n"
    return result  # Return the complete table as a string

# Output: "1 x 6 = 6\n2 x 6 = 12\n...10 x 6 = 60\n"
print(table(6))  # Prints the multiplication table

def table(x):
    for i in range(1, 11):  # Should be range(11) to include 0
        print(f"{i} x {x} = {i*x}")  # Directly prints each line
        
table(6)  # Calls function and prints table

def table(x):
    result = []  # List to store formatted lines
    
    for number in range(11):  # range(11) = 0, 1, 2, ..., 10
        total = number * x  # Calculate product
        result.append(f"{x} x {number} = {total}")  # e.g., "9 x 0 = 0"
    return "\n".join(result)  # Returns complete table as string

print(table(9))  # Prints the complete multiplication table

for j in range(1, 11):  # Outer loop: multiplier (1 to 10)
    for i in range(1, 11):  # Inner loop: multiplicand (1 to 10)
        product = j * i  # Calculate product
        print(f"{j} x {i} = {product}")  # Print each multiplication
    print("-" * 10)  # Separator between tables

"""
Problem 43:
Write a Python function called square_elements that takes a list of numbers as input and returns a new list with each element squared.
"""

def square_elements(numbers):
    squared_list = []
    
    for number in numbers:
        squared_list.append(number ** number)
    return squared_list  # Returns incorrect results
               
lst = [2, 3, 4, 5, 6]
print(square_elements(lst))  # Output: [4, 27, 256, 3125, 46656] (INCORRECT!)

"""
Problem 44:
Write a Python function called count_uppercase that takes a string as input and returns the number of uppercase letters in the string.
"""

def count_uppercase(string):
    count = 0  # Initialize counter
    
    for char in string:
        if char.isupper():
            count += 1  # Increment counter for uppercase letter
    return count
                   
lst = "Jonathan Moll"
print(count_uppercase(lst))  # Output: 2

def count_uppercase(string):
    count = 0  # Initialize counter
    string = string.replace(" ", "")
    
    for char in string:
        if char == char.upper():
            count += 1  # Increments for uppercase, numbers, and symbols
    return count  # May return incorrect count if string has numbers/symbols
    
string = "Jonah Is Tbe Best"
print(count_uppercase(string))  # Output: 4
    
"""
Problem 45:
Write a Python function called remove_spaces that takes a string as input and returns the string with all spaces removed.
"""

def remove_spaces(string):
    return string.replace(" ", "")  # Returns string with spaces removed
    
lst = "what happening boss man"
print(remove_spaces(lst))  # Output: whathappeningbossman
    
def remove_spaces(string):
    string_removed = []  # List to collect non-space characters
    
    for char in string:
        if char != " ":  # Check if character is not a space
            string_removed.append(char)  # Add non-space character to list
    return "".join(string_removed)  # Return string without spaces
                
lst = "what happening boss man"
print(remove_spaces(lst))  # Output: whathappeningbossman

"""
Problem 46:
Write a Python function called merge_lists that takes two sorted lists as input and returns a new sorted list containing all the elements from both input lists.
"""

def merge_lists():
    lst1 = sorted(input("Type the first sorted list: ").split())  # Sorts again
    lst2 = sorted(input("Type the second sorted list: ").split())  # Sorts again
    
    merged_list = sorted(lst1 + lst2)  # Concatenate and sort
    
    print(merged_list)  # Print the merged and sorted list

merge_lists()  # Call the function

"""
Problem 47:
Write a Python function called find_index that takes a list of numbers and a target number as input, and returns the index of the target number in the list. If the target number is not found in the list, the function should return -1.
"""

def find_index(numbers, target):
    for index, num in enumerate(numbers):
        if num == target:
            return index  # Return index immediately when found
    return -1  # Target not found

numbers = [1, 3, 5, 7, 9]
target = 5
print("Index of", target, "in nums:", find_index(numbers, target))  # Output: Index of 5 in nums: 2

target = 6
print("Index of", target, "in nums:", find_index(numbers, target))  # Output: Index of 6 in nums: -1

"""
Problem 48:
Write a Python function called sum_even_indices that takes a list of numbers as input and returns the sum of the elements at even indices (0-based) in the list.
"""

def sum_even_indices(nums):
    total = 0
    
    for i in range(len(nums)):
        if i % 2 == 0:  # i % 2 == 0 means index is even
            total += nums[i]  # Add element at even index to sum
    return total  # Return the total sum

# Even indices: 0 (1), 2 (3), 4 (5)
numbers = [1, 2, 3, 4, 5, 6]
print("Sum of elements at even indices:", sum_even_indices(numbers))  # Output: Sum of elements at even indices: 9

def sum_even_indices(nums):
    return sum(nums[i] for i in range(len(nums)) if i % 2 == 0)  # One-liner version

numbers = [1, 2, 3, 4, 5, 6]
print("Sum of elements at even indices:", sum_even_indices(numbers))  # Output: Sum of elements at even indices: 9

"""
Problem 49:
Write a Python function called remove_duplicates_case_insensitive that takes a list of strings as input and returns a new list with duplicate strings removed, ignoring case sensitivity. For example, “hello” and “HELLO” should be considered the same. Do not use set().
"""

def remove_duplicates(lst):
    unique = set()
    common = []
    for word in lst:
        word_lower = word.lower()
        if word_lower not in unique:
            common.append(word_lower)
            unique.add(word_lower)
    return common
            
lst = ["not", "not", "hot", "hot"]
print(remove_duplicates(lst))

def remove_duplicates(lst):
    unique = set()
    for word in lst:
        word_lower = word.lower()
        if word_lower not in unique:
            unique.add(word_lower)
    return unique
            
lst = ["not", "not", "hot", "hot", "cold"]
print(remove_duplicates(lst))

def remove_duplicates(strings):
    unique_strings = []
    for string in strings:
        if string.lower() not in map(str.lower, unique_strings):
            unique_strings.append(string)
    return unique_strings

input_strings = ["Hello", "HELLO", "world", "World", "Python", "python"]
print("List with case-insensitive duplicates removed:", remove_duplicates(input_strings))

"""
Problem 50:
Write a Python function called is_palindrome that takes a string as input and returns True if the string is a palindrome (reads the same forwards and backwards), and False otherwise.
"""

def is_palindrome(s):
    return s == s[::-1]  # One-liner palindrome check

input_string = "racecar"
print("Is", input_string, "a palindrome?", is_palindrome(input_string))  # Output: Is racecar a palindrome? True

input_string = "hello"
print("Is", input_string, "a palindrome?", is_palindrome(input_string))  # Output: Is hello a palindrome? False

"""
Problem 51:
Write a Python function called `factorial` that takes a non-negative integer as input and returns its factorial. The factorial of a number `n` is the product of all positive integers less than or equal to `n` (n!). For example, `factorial(5)` should return `120` (since 5 * 4 * 3 * 2 * 1 = 120).
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):  # range(1, n+1) = 1, 2, 3, ..., n
            result *= i  # Multiply: result = 1 × 2 × 3 × ... × n
        return result  # Return the factorial

print(factorial(0))  # Output: 1

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)  # Calls itself with n-1

print(factorial(5))  # Output: 120

def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1  # Initialize result
        for i in range(n, 0, -1):  # range(n, 0, -1) = n, n-1, ..., 2, 1
            result *= i  # Multiply: result = n × (n-1) × ... × 2 × 1
        return result  # Return the factorial

print(factorial(5))  # Output: 120 

"""
Problem 52:
Write a Python function called is_anagram that takes two strings as input and returns True if they are anagrams of each other, and False otherwise. Two strings are anagrams if they can be rearranged to form the same word (e.g., “listen” and “silent”).
"""

def main():
    string1 = input("type string: ").lower()  # e.g., "Listen" → "listen"
    string2 = input("type string: ").lower()  # e.g., "Silent" → "silent"
    
    sorted1 = sorted(string1)
    sorted2 = sorted(string2)
    
    if sorted1 == sorted2:
        return True  # Strings are anagrams
    return False  # Strings are not anagrams

main()

def is_anagram(str1, str2):
    str1 = str1.lower()  # "Listen" → "listen"
    str2 = str2.lower()  # "Silent" → "silent"
    
    return sorted(str1) == sorted(str2)  # Returns True if anagrams, False otherwise

print(is_anagram("listen", "silent"))  # Output: True

print(is_anagram("hello", "world"))  # Output: False

print(is_anagram("Triangle", "Integral"))  # Output: True

def is_anagram(lst1, lst2):
    sorted_lst1 = sorted(lst1)  # "qwer" → ['e', 'q', 'r', 'w']
    sorted_lst2 = sorted(lst2)  # "rewq" → ['e', 'q', 'r', 'w']
    
    if sorted_lst1 == sorted_lst2:
        return True  # Strings are anagrams
    return False  # Strings are not anagrams
           
lst1 = "qwer"
lst2 = "rewq"
print(is_anagram(lst1, lst2))  # Output: True

"""
Problem 53:
Write a Python function called count_words that takes a string as input and returns a dictionary where the keys are the words in the string and the values are the counts of each word. Words are separated by spaces, and the function should be case-insensitive.
"""

def count_words(s):
    s = s.lower()
    words = s.split()  # ["this", "is", "a", "test", "this", "test", ...]
    word_count = {}  # Dictionary to store word frequencies
    
    for word in words:
        if word in word_count:
            word_count[word] += 1  # Increment count if word exists
        else:
            word_count[word] = 1
    return word_count  # Return dictionary with word counts

input_string = "This is a test. This test is only a test."
print(count_words(input_string))  # Output: {'this': 2, 'is': 2, 'a': 2, 'test.': 2, 'only': 1}

"""
Problem 54:
Write a Python function called fibonacci that takes an integer n as input and returns a list containing the first n numbers of the Fibonacci sequence. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two numbers.
"""

def fibonacci(n):
    if n <= 0:
        return []  # No Fibonacci numbers to generate
    elif n == 1:
        return [0]  # First Fibonacci number
    elif n == 2:
        return [0, 1]  # First two Fibonacci numbers

    fib_sequence = [0, 1]  # Start with base values

    for i in range(2, n):  # range(2, n) = 2, 3, 4, ..., n-1
        next_number = fib_sequence[-1] + fib_sequence[-2]  # Sum last two
        fib_sequence.append(next_number)  # Add to sequence

    return fib_sequence  # Return complete Fibonacci sequence

print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

"""
Problem 55:
Write a Python program to calculate the area of a rectangle. Prompt the user to enter the length and width.
"""

def area_rectangle():
    length = float(input("type length: "))  # e.g., 5.0
    width = float(input("type width: "))  # e.g., 3.0
    area = length * width  # e.g., 5.0 × 3.0 = 15.0
    
    print(area)  # Prints the area
    
area_rectangle()  # Call the function

"""
Problem: 56
Write a Python program to check if a given number is even or odd. Prompt the user to enter a number.
"""

def even_odd():
    user = int(input("type number: "))  # e.g., 4 or 7
    
    if user % 2 == 0:  # If remainder is 0, number is even
        print("Number is even")  # Display even message
    else:  # If remainder is not 0 (i.e., 1), number is odd
        print("Number is odd")  # Display odd message
   
even_odd()  # Call the function

"""
Problem 57
Write a Python program to print the Fibonacci series up to a given number. Prompt the user to enter the limit using a while loop.
"""

def fibonacci_series():
    limit = int(input("Enter the limit: "))  # e.g., 10
    a, b = 0, 1  # a=0 (first), b=1 (second)
    
    while a <= limit:  # Loop until a exceeds limit
        print(a, end=' ')  # Prints: 0, then 1, then 1, then 2, etc.
        a, b = b, a + b  # Tuple assignment: a=1,b=1 → a=1,b=2 → a=2,b=3, etc.
        
fibonacci_series()  # Call the function

"""
Problem: 58
Write a Python program to find the maximum of three numbers. Prompt the user to enter three numbers."
"""

def max_number():
    user = input("type 3 numbers: ").split()  # e.g., "10 20 15" → ["10", "20", "15"]
    int_number = []  # List to store converted integers
    
    for number in user:
        int_number.append(int(number))  # ["10", "20", "15"] → [10, 20, 15]
    
    max_num = int_number[0]  # Assume first number is maximum (10)
    
    for number in int_number:
        if number > max_num:  # 20 > 10, so max_num = 20; 15 > 20? No
            max_num = number  # Update maximum
    print(max_num)  # Print the maximum number (20)
           
max_number()  # Call the function

"""
Problem 59:
Write a Python program to reverse a string. Prompt the user to enter a string.
"""

def reverse_string():
    user = input("type string: ")  # e.g., "hello"
    user = user[::-1]  # "hello" → "olleh"
    
    print(user)  # Prints: olleh
    
reverse_string()  # Call the function

def reverse_string(string):
    return string[::-1]  # Returns reversed string
            
lst = "Jonathan"
print(reverse_string(lst))  # Output: nahtanoJ

"""
Problem: 60
Write a Python program to check if a given string is a palindrome. Prompt the user to enter a string.
"""

def is_palindrome():
    user = input("type word: ").lower().replace(" ", "")  # "Race Car" → "racecar"
    
    return user == user[::-1]  # "racecar" == "racecar" → True
        
print(is_palindrome())  # Call function and print result

"""
Problem: 61
Write a Python program to count the number of vowels in a given string. Prompt the user to enter a string.
"""

def count_vowels():
    user = input("type string: ").lower()  # "Hello" → "hello"
    vowels = "aeiou"  # String containing all vowels
    count = 0
    
    for char in user:
        if char in vowels:  # If char is 'a', 'e', 'i', 'o', or 'u'
            count += 1  # Increment counter
    print(count)  # Display the total count
    
count_vowels()  # Call the function

"""
Problem: 62
Write a Python program to calculate the factorial of a number. Prompt the user to enter a number.
"""

def factorial():
    result = 1  # Initialize result
    for i in range(1, 6):
        result *= i  # Multiply: 1 × 2 × 3 × 4 × 5 = 120
        
    print(f"{result}")  # Always prints 120

factorial()  # Call the function
 
def factorial():
    number = int(input("Enter a number: "))  # e.g., 5
    result = 1
    
    for i in range(1, number + 1):  # range(1, 6) = 1, 2, 3, 4, 5
        result *= i  # Multiply: 1 × 2 × 3 × 4 × 5 = 120
        
    print(f"The factorial of {number} is {result}")  # Prints: The factorial of 5 is 120

factorial()  # Call the function

"""
Problem: 63
Write a Python program to calculate the sum of all numbers from 1 to a given number. Prompt the user to enter a number.
"""

def sum_of_all_numbers():
    user = input("type numbers: ").split()  # "1 2 3 4 5" → ["1", "2", "3", "4", "5"]
    int_user = []  # List to store converted integers
    
    for number in user:
        int_user.append(int(number))  # ["1", "2", ...] → [1, 2, 3, 4, 5]
        
    count = 0
    
    for number in int_user:
        count += number  # Add each number: 1+2+3+4+5 = 15
    print(count)  # Display the sum

sum_of_all_numbers()  # Call the function

"""
Problem: 64
Write a Python program to find the largest element in a list. Prompt the user to enter a list of numbers.
"""

def find_largest():
    user = input("type number: ").split()  # "2 56 75 4566 3" → ["2", "56", ...]
    int_number = []  # List to store converted integers
    
    for number in user:
        int_number.append(int(number))  # [2, 56, 75, 4566, 3]
    
    sort = sorted(int_number)  # [2, 3, 56, 75, 4566]
    largest = sort[-1]  # 4566
    
    print(largest)  # Display the largest number

find_largest()  # Call the function

def find_largest():
    user = input("type number: ").split()
    int_number = []
    for number in user:
        int_number.append(int(number))
    
    sort = sorted(int_number, reverse=True)  # [4566, 75, 56, 3, 2]
    largest = sort[0]  # 4566
    
    print(largest)  # Display the largest number
    
find_largest()  # Call the function

def largest_element(numbers):
    return max(numbers)
                
numbers = [2, 56, 75, 4566, 3]
print(largest_element(numbers))  # Output: 4566

def largest_element(numbers):
    largest = numbers[0]  # Assume first is largest
    
    for number in numbers:
        if number > largest:  # 56 > 2, so largest = 56; 75 > 56, so largest = 75, etc.
            largest = number  # Update maximum
    return largest  # Return the largest number
                
numbers = [2, 56, 75, 4566, 3]
print(largest_element(numbers))  # Output: 4566

"""
Problem: 65
Write a Python program to find the largest element in a list (do not use numbers).
"""

def main(lst):
    return max(lst, key=len)
    
lst = ["tree", "cliff", "mountain", "tree","tree", "grassy"]
main(lst)  # Returns: "mountain"

def largest_elememt(lst):
    count = 0  # Track the length of the longest string found
    largest = ""  # Track the longest string itself
    
    for word in lst:
        if len(word) > count:  # Compare lengths
            count = len(word)  # Update the length
            largest = word  # Update the word
    return largest  # Return the longest string
            
lst = ["house", "counter", "if"]
print(largest_elememt(lst))  # Output: counter

def largest_elememt(lst):
    lst = sorted(lst, key=len)  # ["if", "house", "counter"]
     
    return lst[-1]  # Returns "counter"
    
lst = ["house", "counter", "if"]
print(largest_elememt(lst))  # Output: counter
    
"""
Problem 66:
Write a Python program to remove duplicates from a list. Prompt the user to enter a list of elements.
"""

def remove_duplicates(elements):
    duplicates = []  # List to store unique elements (misleading variable name)
    
    for element in elements:
        if element in duplicates:
            return duplicates  # Returns partial list with first duplicate found
        duplicates.append(element)  # Add first occurrence
    return None  # Returns None if no duplicates found
            
lst = ["tree", "kiss", "tree"]
print(remove_duplicates(lst))  # Output: ['tree'] (INCORRECT!)

"""
Problem: 67
Write a Python program to check if a given year is a leap year. Prompt the user to enter a year.
"""

def is_leap_year():
    year = int(input("Enter a year: "))  # e.g., 2000
    
    # Check leap year conditions:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True  # Return True for leap year
    else:
        return False  # Return False for non-leap year

print(is_leap_year())  # Prompts user and prints result

"""
Problem: 68
Write a Python program to find the length of a string without using the built-in len() function. Prompt the user to enter a string.
"""

def length_string():
    user = input("entre string: ").replace(" ", "")  # "hello world" → "helloworld"
    count = 0

    for char in user:
        count += 1  # Increment counter for each character
    print(count)  # Display the total count
             
length_string()  # Call the function

"""
Promblem: 69
Write a Python program to check if a string is a palindrome without using any built-in functions. Prompt the user to enter a string.
"""

def palindrome(string):
    if string == string[::-1]:  # "juju" == "ujuj"? No
        return True  # Return True if palindrome
    return False  # Return False if not palindrome
       
word = "juju"
print(palindrome(word))  # Output: False

"""
Problem: 70
Write a Python program to count the occurrences of each word in a given sentence. Prompt the user to enter a sentence.
"""

def count_each_word(sentence):
    count = 0  # Counter for total words (WRONG - should count per word)
    split_word = sentence.split()  # "Jonathan is the best" → ["Jonathan", "is", "the", "best"]
    
    for word in split_word:
        count += 1  # Increments for each word: 1, 2, 3, 4
    return count  # Returns 4 (total words, not per-word occurrences)
       
lst = "Jonathan is the best"
print(count_each_word(lst))  # Output: 4 (WRONG - should be a dictionary!)

"""
Problem: 71
Write a Python program to find the second largest number in a list. Prompt the user to enter a list of numbers.
"""

def sec_lar():
    numbers = list(map(int, input("type: ").split()))  # "56 700 1 57 78 787 5 88" → [56, 700, ...]
    unique_numbers = list(set(numbers))  # Removes duplicates
    unique_numbers.sort()  # Sorts the unique numbers
    
    print(unique_numbers[-2])  # Prints the second largest

sec_lar()  # Call the function

def second_largest_number(numbers):
    sorted_numbers = sorted(numbers, reverse=True)  # [787, 700, 88, 78, 57, 56, 5, 1]
    
    if len(sorted_numbers) > 1:
        return sorted_numbers[1]  # Return second element (700)
    else:
        return None  # Return None if list too short
        
arg = [56, 700, 1, 57, 78, 787, 5, 88]
print(second_largest_number(arg))  # Output: 700

def second_largest_number(numbers):
    sorted_numbers = sorted(numbers, reverse=True)  # Sort descending
    
    for number in sorted_numbers:
        return sorted_numbers[1]  # Always returns second element immediately
    return None  # Unreachable if list is non-empty
        
arg = [56, 700, 1, 57, 78, 787, 5, 88]
print(second_largest_number(arg))  # Output: 700

def second_largest_number(numbers):
    sorted_numbers = sorted(numbers)  # [1, 5, 56, 57, 78, 88, 700, 787]
    
    for number in sorted_numbers:
        return sorted_numbers[-2]  # Returns 700
    return None  # Unreachable
        
arg = [56, 700, 1, 57, 78, 787, 5, 88]
print(second_largest_number(arg))  # Output: 700

"""
Problem: 72
Write a Python program to check if a given string is a valid email address. Prompt the user to enter an email address.
"""

import re

def is_valid_email(email):
    """
    Checks if the given email address is valid.
    
    Args:
        email (str): The email address to be validated.
    
    Returns:
        bool: True if the email address is valid, False otherwise.
    """
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
    if re.match(pattern, email):  # re.match checks from start of string
        return True  # Email matches pattern
    else:
        return False  # Email doesn't match pattern

def main():
    email = input("Enter an email address: ")  # e.g., "user@example.com"
    
    if is_valid_email(email):
        print("Email address is valid.")  # Display success message
    else:
        print("Email address is invalid.")  # Display error message

main()  # Call the main function

def is_valid_email():
    email = input("Enter an email address: ")
    
    if '@' not in email or '.' not in email:
        return False  # Missing required symbols
    
    local, domain = email.split('@', 1)  # Split at first @ only
    
    if not local:
        return False  # Local part is empty
    
    if '.' not in domain or domain.startswith('.') or domain.endswith('.'):
        return False  # Domain must have dot, not start/end with dot
    
    domain_parts = domain.split('.')  # Split domain by dots
    if any(not part for part in domain_parts):  # Check if any part is empty
        return False  # Empty domain part found
    
    return True  # All validations passed

print(is_valid_email())  # Call function and print result

"""
Problem: 73
Write a Python program to find the factorial of a number using recursion. Prompt the user to enter a number."
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1  # Stop recursion, return 1
    else:
        return n * factorial(n - 1)  # Call function with n-1
        #          = 5 × 4 × factorial(3)
        #          = 5 × 4 × 3 × factorial(2)
        #          = 5 × 4 × 3 × 2 × 1 = 120

def main():
    try:
        number = int(input("Enter a number: "))  # e.g., 5
        
        if number < 0:
            print("Factorial is not defined for negative numbers.")  # Error message
        else:
            print(f"The factorial of {number} is {factorial(number)}")  # e.g., "The factorial of 5 is 120"
    except ValueError:
        print("Please enter a valid integer.")  # Error message

main()  # Call the main function

"""
Problem: 74
Write a Python program to check if two strings are anagrams of each other. Prompt the user to enter two strings
"""

def are_anagrams():
    str1 = input("Enter the first string: ")  # e.g., "listen"
    str2 = input("Enter the second string: ")  # e.g., "silent"
    
    str1 = str1.replace(" ", "").lower()  # "Listen" → "listen"
    str2 = str2.replace(" ", "").lower()  # "Silent" → "silent"
    
    if sorted(str1) == sorted(str2):  # sorted("listen") == sorted("silent") → True
        print(f"'{str1}' and '{str2}' are anagrams.")  # Display success message
    else:
        print(f"'{str1}' and '{str2}' are not anagrams.")  # Display failure message

are_anagrams()  # Call the function

def pal():
    user = input("type: ")  # Get string from user
  
    if user == user[::-1]:  # Compare with reversed string
        return True  # Is palindrome
    return False  # Not palindrome
 
print(pal())  # Call function and print result

"""
Problem: 75
Write a Python program to check if a number is a prime number. Prompt the user to enter a number.
"""

def is_prime(n):
    if n <= 1:
        return False  # 1 and negative numbers are not prime
    
    if n <= 3:
        return True  # 2 and 3 are prime numbers
    
    if n % 2 == 0 or n % 3 == 0:
        return False  # Even numbers (except 2) and multiples of 3 are not prime
    
    i = 5  # Start from 5 (first number of form 6k-1)
    while i * i <= n:  # Check up to sqrt(n)
        if n % i == 0 or n % (i + 2) == 0:
            return False  # Found a divisor, not prime
        i += 6  # Move to next pair: 6k+5 and 6k+7
    return True  # No divisors found, number is prime

def main():
    try:
        number = int(input("Enter a number: "))  # e.g., 17
        
        if is_prime(number):
            print(f"{number} is a prime number.")  # Display success message
        else:
            print(f"{number} is not a prime number.")  # Display failure message
    except ValueError:
        print("Please enter a valid integer.")  # Error message

main()  # Call the main function

"""
Problem: 76
Write a Python program to find the common elements between two lists. Prompt the user to enter two lists.
"""

def common_elements(lst1, lst2):
    result = []  # List to store common elements
    
    for i in lst1:
        for j in lst2:
            if i == j and i not in result:  # Check for match and uniqueness
                result.append(i)  # Add to result
    return result  # Return list of common elements
    
lst1 = ["tree", "house", "car", "rose"]
lst2 = ["house", "street", "sky", "tree"]
print(common_elements(lst1, lst2))  # Output: ['tree', 'house']

def common_elements(lst1, lst2):
    set1 = set(lst1)  # {"tree", "house", "car", "rose"}
    set2 = set(lst2)  # {"house", "street", "sky", "tree"}
    elements_commmon = set1.intersection(set2)  # {"tree", "house"}

    return elements_commmon  # Return set of common elements
        
arg1 = ["tree", "grass", "flower"]
arg2 = ["grass", "flower", "river"]
print(common_elements(arg1, arg2))  # Output: {'grass', 'flower'}
    
def find_common_elements():
    input1 = input("Enter elements of the first list, separated by spaces: ")
    list1 = input1.split()  # Split into list of strings
    
    input2 = input("Enter elements of the second list, separated by spaces: ")
    list2 = input2.split()  # Split into list of strings
    
    set1 = set(list1)  # Convert to set
    set2 = set(list2)  # Convert to set
    common_elements = set1.intersection(set2)  # Find common elements
    
    if common_elements:
        print(f"Common elements between the two lists: {list(common_elements)}")  # Show common elements
    else:
        print("There are no common elements between the two lists.")  # No common elements

find_common_elements()  # Call the function

"""
Problem: 77
Write a Python function called `count_uppercase` that takes a string as input and returns the number of uppercase letters in the string.
"""

def uppercase(string):
    count = 0
    string = string.replace(" ", "")  # "Hello World" → "HelloWorld"
    
    for word in string:  # 'word' is actually a character (misleading variable name)
        if word == word.upper():  # 'H' == 'H'? Yes; 'e' == 'E'? No
            count += 1  # Increment counter
    return count  # Return total count
        
sentence = "whAtT healin Gmanbe LLike"
print(uppercase(sentence))  # Output: count of uppercase letters

"""
Problem: 78
Write a Python program to convert a decimal number to binary. Prompt the user to enter a decimal number.
"""

def decimal_to_binary():
    decimal_number = int(input("Enter a decimal number: "))  # e.g., 5
    
    binary_number = bin(decimal_number)[2:]  # "0b101"[2:] → "101"
    
    print(f"The binary representation of {decimal_number} is {binary_number}")  # Prints: "The binary representation of 5 is 101"

decimal_to_binary()  # Call the function

"""
Problem: 79
Write a Python program to sort a list of numbers in ascending order. Prompt the user to enter a list of numbers.
"""

def main():
    result = []  # List to store converted integers
    user = input("enter list of numbers: ")  # e.g., "56 23 677 6 1"
    user = user.split()  # Split into list: ["56", "23", "677", "6", "1"]
    
    for num in user:
        result.append(int(num))  # [56, 23, 677, 6, 1]
    return sorted(result)  # Return sorted list: [1, 6, 23, 56, 677]
    
main()  # Call function (return value not printed)

def ascending_order_numbers(numbers):
    sort_numbers = sorted(numbers)  # [56, 23, 677, 6, 1] → [1, 6, 23, 56, 677]
    
    return sort_numbers  # Return sorted list
    
numbers = [56, 23, 677, 6, 1]
print(ascending_order_numbers(numbers))  # Output: [1, 6, 23, 56, 677]

"""
Problem: 80
Write a Python program to generate a random number between a given range. Prompt the user to enter the lower and upper limits.
"""

import random

def generate_random_number():
    lower_limit = int(input("Enter the lower limit: "))  # e.g., 1
    upper_limit = int(input("Enter the upper limit: "))  # e.g., 10
    
    random_number = random.randint(lower_limit, upper_limit)  # e.g., 7
    
    print(f"The random number between {lower_limit} and {upper_limit} is: {random_number}")  # Prints: "The random number between 1 and 10 is: 7"

generate_random_number()  # Call the function
    
"""
Problem: 81
Write a Python program to find the square root of a number. Prompt the user to enter a number.
"""

def square_root():
    num = float(input("type num: "))  # e.g., 9.0
    return num ** 0.5  # 9.0 ** 0.5 = 3.0
    
print(square_root())  # Call function and print result

def square_root():
    num = float(input("type num: "))  # e.g., 16.0
    print(num ** 0.5)  # Prints: 4.0
    
square_root()  # Call the function

"""
Problem: 82
Write a Python program to find the area of a circle. Prompt the user to enter the radius.
"""

import math

def circle():
    radius = float(input("type number: "))  # e.g., 5.0
    area = math.pi * radius ** 2  # math.pi × 5² = 25π ≈ 78.54
    print(area)  # Display the area
    
circle()  # Call the function

def calculate_circle_area():
    radius = float(input("Enter the radius of the circle: "))  # e.g., 10.0
    area = math.pi * radius ** 2  # π × 10² = 100π ≈ 314.16
    print(f"The area of the circle with radius {radius} is {area:.2f}")  # Prints: "The area of the circle with radius 10.0 is 314.16"

calculate_circle_area()  # Call the function

import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2  # Returns area value

def main():
    radius = float(input("Enter the radius of the circle: "))
    area = calculate_circle_area(radius)  # Call calculation function
    print(f"The area of the circle with radius {radius} is {area:.2f}")

if __name__ == "__main__":
    main()  # Call main function

"""
Problem: 83
Write a Python program to check if a given string is a palindrome using a recursive function. Prompt the user to enter a string.
"""

def is_palindrome(s):
    s = s.replace(" ", "").lower()  # "Race Car" → "racecar"
    return s == s[::-1]  # "racecar" == "racecar" → True

def main():
    user_input = input("Enter a string: ")  # e.g., "racecar"
    
    if is_palindrome(user_input):
        print(f"{user_input} is a palindrome.")  # Display success message
    else:
        print(f"{user_input} is not a palindrome.")  # Display failure message

if __name__ == "__main__":
    main()  # Call main function

"""
Problem: 84
Write a Python program to check if a string is a pangram. A pangram is a sentence that contains every letter of the alphabet at least once. Prompt the user to enter a sentence.
"""

def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sentence = sentence.lower()  # Convert to lowercase for case-insensitive check
    for char in alphabet:
        if char not in sentence:  # If any letter is missing, not a pangram
            return "not pangram"
    return "is pangram"  # All letters found
   
sentence = input("Enter a sentence: ")
print(is_pangram(sentence))

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
"""

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
"""

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

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
"""

def reverse_lst():
    user = input("Type a list: ")
    split_lst = user.split()    
    reversed_lst = []
    
    for item in split_lst[::-1]:  # [::-1] reverses the list
        reversed_lst.append(item)
    return " ".join(reversed_lst)

print(reverse_lst())

def reverse_list():
    user_input = input("Enter a list: ")
    elements = user_input.split()
    reversed_elements = []
    
    for i in range(len(elements) - 1, -1, -1):
        reversed_elements.append(elements[i])

    return f"Reversed list: {reversed_elements}"

print(reverse_list())

def reverse_list():
    user_input = input("Enter list: ")
    elements = user_input.split()
    reversed_elements = []
    
    for i in range(len(elements) - 1, -1, -1):
        reversed_elements.append(elements[i])

    print("Reversed list:", reversed_elements)

reverse_list()

def reverse_list(items):
    reverse_items = []
    
    for item in range(len(items)-1,-1,-1):
        reverse_items.append(items[item])
    return reverse_items
        
lst = ["apple", "banana", "cunt"]
print(reverse_list(lst))

"""
Problem: 88
Write a Python program to find the prime factors of a number. Prompt the user to enter a number.
"""

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

"""
Problem 89:
Write a Python program to generate a random password of a given length. Prompt the user to enter the length.
"""

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation  # All printable ASCII chars
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

length = int(input("Enter the length of the password: "))
print("Generated password:", generate_password(length))

"""
Problem: 90:
Write a Python program to count the number of words in a sentence. Prompt the user to enter a sentence.
"""

def count_words(sentence):
    split_words = sentence.split()  # split() splits on whitespace by default
    
    count = 0
    for word in split_words:
        count += 1  # Count each word
    return count  # Return total word count
                   
words = "Jonathan is the best ever"
print(count_words(words))  # Output: 5

"""
Problem 91:
Write a Python program to find the largest and smallest elements in a list. Prompt the user to enter a list of numbers without using sorted()."
"""

def largest_smallest(elements):
    smallest = elements[0]  # Start with first element as minimum
    largest = elements[0]   # Start with first element as maximum
    
    for element in elements:
        if element < smallest:
            smallest = element  # Found a new minimum
        if element > largest:
            largest = element  # Found a new maximum
    
    return smallest, largest  # Returns tuple (smallest, largest)
    
# Smallest: 1, Largest: 100
lst = [4, 5, 100, 6, 1, 10]
print(largest_smallest(lst))  # Output: (1, 100)

"""
Problem: 92
Write a Python program to check if a number is a perfect number. A perfect number is a positive integer that is equal to the sum of its proper divisors. Prompt the user to enter a number.
"""

def is_perfect_square(num):
    if num <= 0:
        return False
    sum_divisor = 0
    for i in range(1, num + 1):  # Includes num itself (should only check proper divisors)
        if num % i == 0:
            sum_divisor += i
            if sum_divisor == num:  # Checks during loop, not at end
                return True
    return False
is_perfect_square(6)

def is_perfect_number(n):
    if n <= 0:
        return False
    
    sum_of_divisors = 0
    for i in range(1, n):  # Only check divisors less than n (proper divisors)
        if n % i == 0:
            sum_of_divisors += i
    
    return sum_of_divisors == n  # Check if sum equals the number

def main():
    number = int(input("Enter a number: "))
    
    if is_perfect_number(number):
        print(f"{number} is a perfect number.")
    else:
        print(f"{number} is not a perfect number.")

if __name__ == "__main__":
    main()

"""
Problem 93:
Write a Python program to find the factorial of a number using a loop. Prompt the user to enter a number.
"""

def factorial():
    user = int(input("type number: "))
    result = 1  # Start with 1 (multiplicative identity)
    for number in range(1, user + 1):  # range(1, n+1) gives 1, 2, 3, ..., n
        result *= number  # Multiply: 1 × 2 × 3 × ... × n
    
    print(result)
           
factorial()

def factorial():
    user = int(input("type number: "))
    result = 1
    for number in range(1, user + 1):
        result *= 1  # BUG: Should be result *= number
    return result

print(factorial())

"""
Problem: 94
Write a Python program to check if a given number is a power of two.
"""

def is_power_of_two(number):
    if number <= 0:
        return False
    while number != 1:
        if number % 2 != 0:  # If not divisible by 2, not a power of 2
            return False
        number = number // 2  # Integer division: divide by 2
    return True  # Reached 1, so it's a power of 2

number = int(input("Enter a number: "))
if is_power_of_two(number):
    print(f"{number} is a power of two.")
else:
    print(f"{number} is not a power of two.")

"""
Problem: 95
Write a Python program to find the intersection of two lists. Prompt the user to enter two lists.
"""
def get_list(prompt):
    return input(prompt).split()

def find_intersection(list1, list2):
    return list(set(list1) & set(list2))  # & is set intersection operator

def main():
    list1 = get_list("Enter the first list of elements, separated by spaces: ")
    list2 = get_list("Enter the second list of elements, separated by spaces: ")

    intersection = find_intersection(list1, list2)

    print(f"The intersection of the two lists is: {intersection}")

main()

def find_intersection():
    list1 = input("Enter lst: ").split()
    list2 = input("Enter lst: ").split()
    intersection = list(set(list1) & set(list2))

    print(f"The intersection of the two lists is: {intersection}")
    
print(find_intersection())

"""
Problem 96:
Write a Python program to remove vowels from a string. Prompt the user to enter a string.
"""

def remove_vowels():
    user = input("type string: ")
    for char in user:
        if char not in "aeiou":  # Only checks lowercase vowels
            print(char, end= "")  # end="" prevents newline after each char
            
remove_vowels()

def remove_vowels(string):
    new_name = []
    for char in string:
        if char not in "aeiou":
            new_name.append(char)
    return "\n".join(new_name)  # Joins with newlines instead of empty string
               
name = "Jonathan" 
print(remove_vowels(name))

"""
Problem: 97
Write a Python program to convert a binary number to decimal. Prompt the user to enter a binary number.
"""

def binary_to_decimal(binary):
    decimal = 0
    power = len(binary) - 1  # Start with highest power (leftmost bit)
    for digit in binary:
        if digit == '1':
            decimal += 2 ** power  # Add 2^power for each '1' bit
        power -= 1  # Decrease power for next position
    
    return decimal

def main():
    binary_number = input("Enter a binary number: ")
    if all(bit in '01' for bit in binary_number):
        decimal_number = binary_to_decimal(binary_number)
        print(f"The decimal equivalent of {binary_number} is {decimal_number}.")
    else:
        print("Invalid binary number. Please enter a valid binary number (consisting of 0s and 1s).")

if __name__ == "__main__":
    main()

"""
Problem: 98
Write a Python program to find the sum of the digits in a string. Prompt the user to enter a string containing seperate numbers. eg "2", "8" should return 10
"""

def digits_string():
    user = input("Type numbers separated by spaces: ").split()  # Split into list of strings
    total = 0
    for number in user:
        total += int(number)  # Convert to int and add
        
    print(total)
    
digits_string()

def digits_string():
    user = input("type numbers: ").split()
    total = 0
    int_number = []
    for number in user:
        int_number.append(int(number))
    for number in int_number:
        total += number
        
    print(total)
    
digits_string()

"""
Problem: 99
Write a Python program to count the number of uppercase and lowercase letters in a string. Prompt the user to enter a string.
"""

def upper_lower(string):
    count_upper = 0
    count_lower = 0
    for char in string:
        if char.isupper():  # isupper() returns True for uppercase letters
            count_upper += 1
        else:  # Note: counts non-uppercase (including digits, spaces, punctuation) as lowercase
            count_lower += 1
    return f"lower = {count_lower} and upper = {count_upper}"
            
string = "Jonathan Moll is the Best"
print(upper_lower(string))

"""
Problem: 100
Write a Python program to find the sum of all prime numbers within a given range. Prompt the user to enter the lower and upper limits.
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):  # int(num**0.5) + 1 rounds up sqrt
        if num % i == 0:
            return False
    return True

def sum_of_primes(lower, upper):
    total = 0
    for num in range(lower, upper + 1):  # range() upper bound is exclusive, so +1
        if is_prime(num):
            total += num
    return total

def main():
    lower_limit = int(input("Enter the lower limit: "))
    upper_limit = int(input("Enter the upper limit: "))
    prime_sum = sum_of_primes(lower_limit, upper_limit)
    print(f"The sum of all prime numbers between {lower_limit} and {upper_limit} is: {prime_sum}")

if __name__ == "__main__":
    main()

"""
Problem: 101
Write a Python program to calculate the power of a number using recursion. Prompt the user to enter a base number and an exponent.
"""

def power(base, exp):
    if exp == 0:  # Base case: any number to power 0 is 1
        return 1
    return base * power(base, exp - 1)  # Recursive case: multiply base by power(base, exp-1)

base = float(input("Enter the base number: "))
exp = int(input("Enter the exponent: "))

result = power(base, exp)
print(f"{base} to the power of {exp} is: {result}")

"""
Problem 102:
Write a Python program to check if a string is an anagram of another string, ignoring whitespace. Prompt the user to enter two strings.
"""

def is_anagram():
    string1 = input("type string: ").replace(" ", "")  # Remove spaces
    string2 = input("type string: ").replace(" ", "")
    sort1 = sorted(string1)  # sorted() returns list of characters
    sort2 = sorted(string2)
    
    if sort1 == sort2:  # If sorted lists are equal, strings are anagrams
        print("this is anagram")
    else:
        print("this is not anagram")
    
is_anagram()
        
def is_anagram(string1, string2):
    string1 = string1.replace(" ", "")
    string2 = string2.replace(" ", "")
    
    return sorted(string1) == sorted(string2)
    
string1 = "listen"
string2 = "silent"

print(is_anagram(string1, string2))

"""
103
Write a Python program to find the largest and smallest digits in a number. Prompt the user to enter a number.
"""

def largest_smallest():
    user = input("type list of numbers: ").split()
    int_num = []
    for number in user:
        int_num.append(int(number))
        
    max_num = max(int_num)  # Built-in max() function
    min_num = min(int_num)  # Built-in min() function
    print(max_num, min_num)
        
largest_smallest()

"""
Problem: 104
Write a Python program to check if a number is a perfect square. Prompt the user to enter a number"
"""

import math

user = int((input("enter number: ")))

root = math.isqrt(user)  # Integer square root
print(root * root == user)  # Perfect square if root² equals original number

def is_perfect_square(num):
    root = math.isqrt(num)  # math.isqrt() is integer square root function
    return root * root == num  # Check if squaring root gives original number

num = int(input("Enter a number: "))

if is_perfect_square(num):
    print(f"{num} is a perfect square.")
else:
    print(f"{num} is not a perfect square.")
 
"""
Problem 105:
Write a Python program to find the sum of all odd numbers in a list. Prompt the user to enter a list of numbers.
"""

def all_odd_numbers(numbers):
    count = 0
    for number in numbers:
        if number % 2 != 0:  # Check if odd (remainder when divided by 2 is not 0)
            count += number  # Add odd number to sum
    return count

lst = [2, 10, 3, 7]    
print(all_odd_numbers(lst))

"""
Problem 106:
Write a Python program to find the sum of all odd numbers in a list. Prompt the user to enter a list of numbers.
"""

def sum_of_odd_numbers():
    user_input = input("Enter a list of numbers separated by spaces: ")
    split_numbers = user_input.split()
    int_numbers = []
    
    for num in split_numbers:
        int_numbers.append(int(num))
    
    odd_sum = 0
    for num in int_numbers:
        if num % 2 != 0:  # Check if odd
            odd_sum += num
    
    print("The sum of all odd numbers is:", odd_sum)

sum_of_odd_numbers()

def sum_of_all_odd():
    user = input("Enter numbers separated by spaces: ").split()
    total = 0
    for number in user:
        number = int(number)  # Convert to int
        if number % 2 != 0:
            total += number
    
    print(total)
            
sum_of_all_odd()

"""
Problem 107:
Write a Python program to find the common characters between two strings. Prompt the user to enter two strings.
"""

def common_char():
    user_input = input("Type 2 strings separated by a space: ").split()
    if len(user_input) != 2:
        print("Please enter exactly two strings.")
        return
    
    str1, str2 = user_input  # Tuple unpacking: assigns first two elements
    
    common = []
    for char in str1:
        if char in str2 and char not in common:  # Check if in both strings and not already added
            common.append(char)
    
    return common

print(common_char())

def common_char(string1, string2):
    characters = []
    for char in string1:
        if char in string2 and char not in characters:
            characters.append(char)
    
    return characters
    
name1 = input("Enter the first string: ")
name2 = input("Enter the second string: ")
print(common_char(name1, name2))

"""
Problem: 108
Write a Python program to remove duplicates from a string using set(). Prompt the user to enter a string 
"""
def remove_duplicates():
    user = input("type string: ")
    unique_user = set()  # Set to track unique characters
    
    for char in user:
        if char not in unique_user:
            unique_user.add(char)
            
    print("".join(unique_user))  # join() converts set to string (order may vary)
            
remove_duplicates()

def remove_duplicates():
    user = input("type string: ")
    unique_user = set()  # For fast lookup
    result = []  # For maintaining order
    
    for char in user:
        if char not in unique_user:
            unique_user.add(char)
            result.append(char)  # Add to list to preserve order
            
    print("".join(result))  # Join list to get ordered string
            
remove_duplicates()

"""
Problem: 109
Write a Python program to check if a number is an Armstrong number. An Armstrong number is a number that is equal to the sum of its own digits, each raised to the power of the number of digits. Prompt the user to enter a number.
"""

def is_armstrong(number):
    digits = []
    for digit in str(number):  # Convert to string to iterate over digits
        digits.append(int(digit))  # Convert each digit back to int
    
    power = len(digits)  # Power is number of digits
    total = 0
    for digit in digits:
        total += digit ** power  # Add digit raised to power
        
    return total == number  # Check if sum equals original number

number = int(input("Enter a number: "))

if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")

print(number)

"""
Problem 110:
Write a Python program to find the number of vowels and consonants in a string. Prompt the user to enter a string.
"""

def vowels_consonates(string):
    string = string.replace(" ", "")  # Remove spaces
    vowels = "aeiou"  # Only lowercase vowels (case-sensitive)
    count_vowels = 0
    consonates = 0
    
    for char in string:
        if char in vowels:
            count_vowels += 1
        if char not in vowels:  # Note: counts digits, punctuation as consonants
            consonates += 1
    return f"vowels = {count_vowels}\nconsonates = {consonates}"
            
lst = "Jonathan is there next best thing"
print(vowels_consonates(lst))

"""
Problem 111:
Write a Python program to find the second smallest element in a list.
"""
def second_smallest_element():
    user_input = input("Enter numbers separated by spaces: ")
    int_numbers = []
    for num_str in user_input.split():
        int_numbers.append(int(num_str))

    sorted_numbers = sorted(int_numbers)  # Sort ascending
    
    if len(sorted_numbers) >= 2:
        return sorted_numbers[1]  # Second element (index 1)
    else:
        return "List should contain at least two numbers."

print(second_smallest_element())

def second_smallest_element(elements):
    if len(elements) < 2:
        return None
        
    sorted_elements = sorted(elements, key=len)  # key=len sorts by length, not value
    
    return sorted_elements[1]  # Returns second shortest, not second smallest

arg = ["Jonathan", "hot", "sand"]
print(second_smallest_element(arg))

"""
Problem: 112
Write a Python program to generate all possible permutations of a given string. Prompt the user to enter a string.
"""

from itertools import permutations  # itertools.permutations generates all arrangements

def generate_permutations(string):
    result = []
    for p in permutations(string):  # permutations() returns tuples of characters
        result.append(''.join(p))  # join() converts tuple to string
    return result

string = input("Enter a string: ")
result = generate_permutations(string)
print("Permutations:", result)

import itertools
string = "abcd"
result = itertools.permutations(string)  # Returns iterator

print(list(result))  # Convert iterator to list

"""
113
Define a function max() that takes two numbers as arguments and returns the largest of them. Use the if then-else construct available in Python. (It is true that Python has the max() function built in, but writing it yourself is nevertheless a good exercise.)
"""

def max_num(num1, num2):
    if num1 > num2:
        return f"This is max number:  {num1}"  # Returns string, not number
    else:
        return f"This is max number: {num2}"
    
num1 = 10
num2 = 20
print(max_num(num1, num2))

"""
Problem: 114
description": "Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.
"""

def max_of_three(lst):
    largest = 0
    for num in lst:
        if num > largest:
            largest = num
    return largest

lst = [466,45677,3]
max_of_three(lst)

def main(a, b, c):
    return max(a,b,c)  # Built-in max() can take multiple arguments
main(56,8,445)

def max_of_three(a, b, c):
    if a >= b and a >= c:  # Check if a is largest
        return a
    elif b >= a and b >= c:  # Check if b is largest
        return b
    else:  # Otherwise c is largest
        return c
        
max_of_three()

"""
Problem: 115
Define a function that computes the length of a given list or string. (It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise.)
"""

def length_string(string):
    count = 0
    for char in string:  # Iterate over characters
        count += 1
    return count
    
name = "Jonathan"
print(length_string(name))

def length_list(string):  # Misleading name - works for lists too
    count = 0
    for char in string:  # Iterates over elements (works for both strings and lists)
        count += 1
    return count
    
lst = ["list", "it", "all"]
print(length_list(lst))

"""
116
Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.
"""

def is_vowel(string):
    return string in "aeiou"  # in operator checks membership

arg1 = "e"
arg2 = "h"
arg3 = "a"
print(is_vowel(arg1))
print(is_vowel(arg2))
print(is_vowel(arg3))

def is_vowel(char):
    vowels = "aeiouAEIOU"
    if len(char) == 1 and char.isalpha():  # isalpha() checks if alphabetic
        return char.lower() in vowels  # Convert to lowercase for case-insensitive check
    else:
        return False
        
print(is_vowel('a'))  
print(is_vowel('E')) 
print(is_vowel('x')) 
print(is_vowel('9')) 
print(is_vowel(''))  
print(is_vowel('aa')) 

"""
Problem: 117
Write a function translate() that will translate a text into 'rövarspråket'' (Swedish for 'robber's language''). That is, double every consonant and place an occurrence of 'o'' in between. For example, translate('this is fun'') should return the string 'tothohisos isos fofunon'.
"""

def translate(text):
    vowels = "aeiouAEIOU"
    translated = ""
    for char in text:
        if char.isalpha() and char not in vowels:  # Check if consonant
            translated += char + 'o' + char  # Double consonant with 'o' in middle
        else:
            translated += char  # Keep vowels and non-alphabetic as-is
    return translated

text = input("Enter a text: ")
result = translate(text)
print(result)

"""
Problem: 118
Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.
"""

def sum(numbers):
    total = 0  # Start with 0 (additive identity)
    for number in numbers:
        total += number
    return total

def multiply(numbers):
    result = 1  # Start with 1 (multiplicative identity)
    for number in numbers:
        result *= number
    return result

numbers = [1, 2, 3, 4]
print("Sum:", sum(numbers)) 
print("Multiply:", multiply(numbers))

"""
Problem: 119
Define a function reverse() that computes the reversal of a string. For example, reverse('I am testing'') should return the string 'gnitset ma I'.
"""

def reverse(string):
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string  # Prepend char (builds from right to left)
    return reversed_string

string = input("Enter a string: ")
result = reverse(string)
print(result)

"""
Problem: 120
Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards). For example, is_palindrome('radar') should return True.
"""

def palindromes(string):
    for char in string:  # Loop doesn't use char variable
        if string == string[::-1]:  # Compares string with reverse (same check every iteration)
            return True
    return False

string = "radarh"
print(palindromes(string))

"""
Problem 121:
Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards). For example, is_palindrome('radar') should return True.
"""
def is_palindrome(string):
    if string == string[::-1]:  # [::-1] reverses the string
        return True
    return False
     
name = "jojj"
print(is_palindrome(name))

"""
Problem: 122
Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a, and returns True if x is a member of a, False otherwise. (Note that this is exactly what the in operator does, but for the sake of the exercise you should pretend Python did not have this operator.
"""

def is_member(lst, x):
    return x in lst  # in operator checks membership

lst = [2, 5, 6]
x = 2
print(is_member(lst, x))

def is_member(x, a):
    for item in a:
        if item == x:  # Compare each element
            return True
    return False  # Not found

x = input("Enter a value: ")
a = input("Enter a list of values (comma-separated): ").split(',')  # split(',') splits on comma

result = is_member(x, a)
print(result)

"""
Problem: 123
Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise, you should (also) write it using two nested forloops.
"""

def overlapping(list1, list2):
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:  # Compare each pair
                return True  # Found common element
    return False  # No common elements
    
list1 = [1, 2, 3, 4]
list2 = [4, 5, 6, 7]
print(overlapping(list1, list2))  

list1 = ['apple', 'banana', 'cherry']
list2 = ['date', 'elderberry', 'fig']
print(overlapping(list1, list2)) 
 
def is_member(element, lst):
    for item in lst:
        if element == item:
            return True
    return False

def overlapping(list1, list2):
    for item1 in list1:
        if is_member(item1, list2):  # Check if item1 is in list2
            return True
    return False

list1 = [1, 2, 3, 4]
list2 = [4, 5, 6, 7]
print(overlapping(list1, list2))

list1 = ['apple', 'banana', 'cherry']
list2 = ['date', 'elderberry', 'fig']
print(overlapping(list1, list2))

"""
Problem 124:
Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise, you should (also) write it using two nested forloops.
"""

def overlapping(lst1, lst2):
    for element in lst1:
        if element in lst2:  # in operator checks membership
            return True
    return False
    
lst1 = [2, 4, 6, 8, 10]
lst2 = [99, 66, 66, 16]
print(overlapping(lst1, lst2))

def overlapping(lst1, lst2):
    for i in lst1:
        for j in lst2:
            if i == j:  # Compare each pair
                return True
    return False
    
lst1 = [2, 4, 6, 8, 10]
lst2 = [99, 66, 66, 16]
print(overlapping(lst1, lst2))

"""
Problem: 125
Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:
"""

def histogram(numbers):
    for number in numbers:
        print('*' * number)  # String multiplication: '*' * 4 = '****'

histogram([4, 9, 7])

def histogram(numbers):
    for number in numbers:
        print('*' * number)
        
numbers = [4, 9, 7]
histogram(numbers)

def histrogram(numbers):
    result = ""
    for number in numbers:
        result += "*" * number + "\n"  # Build string with newlines
    return result
    
numbers = [2, 4, 8]
print(histrogram(numbers))

"""
Problem 126:
Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.
"""

def map_words_to_lengths(words):
    lengths = []
    for word in words:
        lengths.append(len(word))  # Append length of each word
    return lengths

words = ["apple", "banana", "cherry", "date"]
lengths = map_words_to_lengths(words)
print(lengths) 

"""
Problem 127:
Write a function find_longest_word() that takes a list of words and returns the length of the longest one.
"""

def find_longest_word(elements):
    longest_element = elements[0]
    for element in elements:
        if element > longest_element:  # String comparison, not length comparison
            longest_element = element
    return len(element)  # BUG: Returns len of last element in loop, not longest
               
lst = ["jo", "tre", "Jonny", "abracadabr"] 
print(find_longest_word(lst))

"""
Problem 128:
Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.
"""

def filter_long_words(lst, n):
    longest_words = []
    for word in lst:
        if len(word) > n:  # Check if word length > n
            longest_words.append(word)
    return longest_words
           
lst = ["three", "threebesthorses" "hours", "Jonathanmollthebestintheworld"]  # Note: missing comma between strings
n = 6
print(filter_long_words(lst, n))

"""
Problem: 129
A pangram is a sentence that contains all the letters of the English alphabet at least once, for example: The quick brown fox jumps over the lazy dog. Your task here is to write a function to check a sentence to see if it is a pangram or not.
"""

def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sentence = sentence.lower()  # Convert to lowercase for case-insensitive check
    for letter in alphabet:
        if letter not in sentence:  # If any letter missing, not a pangram
            return False
    return True  # All letters found

sentence = input("Enter a sentence: ")
result = is_pangram(sentence)
print(result)

"""
Problem: 130
Define a simple 'spelling correction' function correct() that takes a string and sees to it that 1) two or more occurrences of the space character is compressed into one, and 2) inserts an extra space after a period if the period is directly followed by a letter. E.g. correct('This is very funny and cool.Indeed!'') should return 'This is very funny and cool. Indeed!'' Tip: Use regular expressions!
"""

import re

def correct(text):
    text = re.sub(r'\s+', ' ', text)  # re.sub(pattern, replacement, string)
    text = re.sub(r'\.(?=[A-Za-z])', '. ', text)  # (?=...) is positive lookahead assertion
    return text

text = input("Enter a string: ")
result = correct(text)
print(result)

"""
Problem 131:
Using the higher order function reduce(), write a function max_in_list() that takes a list of numbers and returns the largest one. Then ask yourself: why define and call a new function, when I can just as well call the reduce() function directly?
"""
from functools import reduce  # reduce() applies function cumulatively to items

def max_func(a, b):
    if a > b:
        return a
    return b

def max_in_list(numbers):
    return reduce(max_func, numbers)  # reduce(function, iterable) reduces list to single value
    
numbers = [1, 5, 3, 9, 2]
print(max_in_list(numbers))

"""
132
Write a Python program to creat a time table where the user puts a number as a argument.
"""

def time_table(number):
    result = ""
    for i in range(1, 11):  # range(1, 11) gives 1 to 10
        total = number * i
        result += f"{i} x {number} = {total}\n"  # f-string formatting
    return result
        
lst = 6
print(time_table(lst))

"""
Problem: 133
Write a program to create a time table using 2 for loops to print the full time table from 1 -10, eg 1 x 1 up to 10 x 10"
"""

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")  # Prints all combinations 1x1 to 10x10

"""
Problem 134:
Write a Python program to find the sum of all numbers in a list. Prompt the user to enter a list of numbers in a input function
"""

def sum_of_all_numbers():
    user_input = input("Enter a list of numbers separated by spaces: ")
    split_numbers = user_input.split()
    int_numbers = []
    
    for num in split_numbers:
        int_numbers.append(int(num))  # Convert strings to integers
    total_sum = sum(int_numbers)  # Built-in sum() function
    
    print(total_sum)

sum_of_all_numbers()

"""
Problem 135:
Write a function that takes numbers string "123" and splits the numbers into a string ("1", "2", "3").
"""

def split_number(numbers):
    numbers_split = numbers.split()  # split() on "123" returns ["123"] (no spaces to split on)
    number_lst = []
    for number in numbers:  # Iterates over characters in string "123"
        number_lst.append(number)  # Appends each character: "1", "2", "3"
    return number_lst  # Returns ["1", "2", "3"] (works but split() is unnecessary)
        
arg = "123"
print(split_number(arg))

"""
Problem 136:
Write a function that sorts words in a sentence alphabetically.
"""

def alphabetically_ordered(sentence):
    return " ".join(sorted(sentence.split()))  # sorted() sorts alphabetically, join() combines with spaces

sentence = "hello caca face"
print(alphabetically_ordered(sentence))

"""
Problem 137:
Write a function that sorts numbers (int) from smallest number to biggest number.
"""

def smallest_largest(numbers):
    return sorted(numbers)
        
numbers = [2, 76, 466, 3, 23]
print(smallest_largest(numbers)) 

"""
Problem 138:
Write a function that sorts number (int) from biggest number to smallest number.
"""

def largest_smallest(numbers):  # Function name misleading
    return sorted(numbers)[::-1]  # [::-1] reverses the sorted list (descending order)
        
numbers = [2, 76, 466, 3, 23]
print(largest_smallest(numbers)) 

"""
Problem 139:
Write a function using sorted() number int) returning the seconded largest number from that list.
"""

def seconded_largest_number(numbers):  # Typo: "seconded" should be "second"
    return sorted(numbers)[-2]  # [-2] is second-to-last element (second largest)
        
numbers = [2, 76, 466, 3, 23]
print(seconded_largest_number(numbers)) 

"""
Problem 140:
Write a function using sorted() number int) returning the fourth largest number from that list.
"""

def fourth_largest_number(numbers):
    return sorted(numbers)[-4]  # [-4] is fourth-to-last element (fourth largest)
        
numbers = [2, 76, 466, 3, 23]
print(fourth_largest_number(numbers)) 

"""
Problem 141:
Write a function using sorted() returning the smallest and third largest number from that list.
"""

def smallest_and_third(numbers):
    smallest = sorted(numbers)[0]  # First element (smallest)
    third_largest = sorted(numbers)[-3]  # Third from end (third largest)
    return smallest, third_largest  # Returns tuple

numbers = [2, 76, 466, 3, 23]
print(smallest_and_third(numbers)) 

"""
Problem 142:
Write a function that sorts number from smallest number to biggest number using sorted().
"""

def largest_smallest(numbers):  # Function name misleading
    return sorted(numbers)[::]  # [::] is same as sorted(numbers)
        
numbers = [2, 76, 466, 3, 23]
print(largest_smallest(numbers)) 

def smallest_biggest(numbers):
    return sorted(numbers)  # Returns sorted list
    
lst = [2, 24, 23, 27, 2]
print(smallest_biggest(lst))

"""
Problem 143:
Write a function with user input that coverts 1 2 3 (int) into a "1" "2" "3" (str).
"""

def int_str():
    user_lst = []
    user = input("type: ")  # e.g., "1 2 3"
    split_str = user.split()  # ["1", "2", "3"] (already strings)
    for word in split_str:
        user_lst.append(word)  # Appends strings (no conversion)
    print(user_lst)  # Prints list of strings
    
int_str()

"""
Problem 144:
Write a function that coverts 123 (int) into a "1" "2" "3" (str).
"""

def int_to_str_list(number):
    number_str = str(number)  # Convert int to string: 123 → "123"
    digits_as_strings = []
    for digit in number_str:  # Iterate over characters in string
        digits_as_strings.append(digit)  # Each character is already a string
    return digits_as_strings  # Returns ["1", "2", "3"]

number = 123
print(int_to_str_list(number)) 

"""
Problem 145:
Write a Python program to find the common number between two lists. Prompt the user to enter two lists, for this exercise do not use set.
"""
def common_numbers(lst1, lst2):
    result = []
    for i in lst1:
        for j in lst2:
            if i == j and i not in result:  # Check if equal and not already added
                result.append(i)
    return result

lst1 = [2, 24, 23, 27, 2]
lst2 = [56, 2, 27, 455, 1]
print(common_numbers(lst1, lst2))

"""
Problem 146:
Write a function that sorts numbers as  string from biggest number to smallest number.
"""

def big_small(numbers):
    number_lst = []
    for number in numbers:
        number_lst.append(int(number))  # Convert string to int for proper numeric sort
              
    number_lst = sorted(number_lst)[::-1]  # Sort descending
    shorted_str = []  # Typo: "shorted" should be "sorted"
    
    for number in number_lst:
        shorted_str.append(str(number))  # Convert back to strings
    return shorted_str
           
lst = ["4", "67", "6"]
print(big_small(lst))

"""
Problem 147:
Write a function where user types a list of numbers in string and returns a list of numbers from smallest to biggest.
"""

def type_smallest_biggest():
    user = input("type number list: ").split()
    sort_number = sorted(user)  # String sort: "10" comes before "2"
       
    print(sort_number)
    
type_smallest_biggest()

def small_big():
    user_string = input("type number followed by spaces: ")
    user_split = user_string.split()
    int_list = []
    for number in user_split:
        int_list.append(int(number))  # Convert to int
    
    int_list.sort()  # Sort numerically
    sorted_str = []
    for number in int_list:
        sorted_str.append(str(number))  # Convert back to strings
    return " ".join(sorted_str)  # Join with spaces
    
print(small_big())

"""
Problem 148:
Write a Python function called `double_elements` that takes a list of numbers as input and returns a new list where each element is doubled, the list must be side by side eg 1, 2, 3, 1, 2, 3
"""

def double_elements(numbers):
    doubled = numbers + numbers  # List concatenation: [1,2,3] + [1,2,3] = [1,2,3,1,2,3]
    
    return doubled

lst = [2, 4, 6, 8]
print(double_elements(lst))

"""
Problem: 149
Write a Python program to find the common elements between two lists. Prompt the user to enter two lists using 2 for loops.
"""

def common():
    lst1 = input("type lst: ").split()
    lst2 = input("type lst: ").split()
    result = []
    for i in lst1:  # Outer loop
        for j in lst2:  # Inner loop (nested)
            if i == j and i not in result:
                result.append(i)
    return result
    
common()

"""
Problem: 150
Write a Python program to find the common elements between two lists. Prompt the user to enter two lists without using for loops.
"""

def common():
    lst1 = input("type lst: ").split()
    lst2 = input("type lst: ").split()
    set1 = set(lst1)  # Convert to set
    set2 = set(lst2)
    common_element = set1.intersection(set2)  # Set intersection operator finds common elements
        
    print(common_element)
    
common()

"""
Problem 151:
Write a Python function called find_longest_word that takes a list of words as input and returns the longest word in the list. If there are multiple longest words, return the first one encountered.
"""

def find_longest_word(words):
    count = 0  # Tracks length of longest word found
    longest_word = ""
    for word in words:
        if len(word) > count:  # If current word is longer
            count = len(word)  # Update length
            longest_word = word  # Update word
    return longest_word

words = ["tree", "mountain", "do", "Jonathanmollfrency"]
    
print(find_longest_word(words))

"""
Problem 152:
Write a Python function called `calculate_average` that takes a list of numbers as input and returns the average of those numbers without using sum() and len()
"""

def average(numbers):
    length = 0  # Manual length counter
    total = 0  # Manual sum accumulator
    for number in numbers:
        length += 1  # Count elements
        total += number  # Sum elements
        result = total / length
    return result
    
numbers = [4, 667, 68, 766]
print(average(numbers))

"""
Problem 153:
Write a Python program to find the second smallest element in a list.
"""

def second_smallest_element(lst):
    sorted_lst = sorted(lst, key=len)  # key=len sorts by length, not value
    if len(sorted_lst) >= 2:
        return sorted_lst[1]  # Returns second shortest, not second smallest
    else:
        return None
           
lst = ["t", "hope", "Jonathan", "it"]
print(second_smallest_element(lst))

"""
Problem 154:
Write a Python function called `find_second_last_element` that takes a list as input and returns the second last element of the list.
"""

def find_last_element():  # Function name should be find_second_last_element
    user_input = input("Type list (elements separated by spaces): ").split()
    if not user_input:  # Check if list is empty
        return None  
    return user_input[-2]  # [-2] is second-to-last element

print(find_last_element())

"""
Problem 155:
Write a Python function called reverse_number that takes an integer as input and returns the reverse of that number. For example, if the input is 123, the function should return 321.
"""

def reverse_number(number):
    return int(str(number)[::-1])  # str() → reverse with [::-1] → int()

lst = 456
print(reverse_number(lst))

def reverse_number(number):
    str_number = str(number)  # Convert to string
    reversed_str_number = str_number[::-1]  # Reverse string
    reversed_number = int(reversed_str_number)  # Convert back to int
   
    return reversed_number
    
number = 123
print(reverse_number(number)) 

def reverse_number(number):
    str_number = str(number)[::-1]  # Reversed string
    int_number = str_number  # Still a string (misleading variable name)
    
    return int_number  # Returns string, not int
             
lst = 1234
print(reverse_number(lst))

"""
Problem 156:
Write a Python function called remove_duplicates that takes a string as input and returns a new string with duplicate characters removed, without maintaining the original order of characters.
"""

def remove_duplicates(string):
    split_word = string.split()  # Splits into words (not characters)
    set_word = set(split_word)  # Set removes duplicates (order not preserved)
    
    return " ".join(set_word)  # Join set (order may vary)
    
lst = "and here is was and in the"
print(remove_duplicates(lst))

"""
Problem 157:
Write a Python function called remove_duplicates that takes a string as input and returns the duplicates removed into a string.
"""

def main(string):
    lst = []
    duplicates = []
    split_string = string.split()
    for word in split_string:
        if word not in lst:
            lst.append(word)  # Track unique words
        else:
            duplicates.append(word)  # Add to duplicates if seen before
    return duplicates  # Returns duplicates, not string with duplicates removed
        
string = "so what's happening duplicates duplicates today? It's hot duplicates duplicates."
main(string)

def remove_duplicates(string):
    split_word = string.split()
    seen = set()  # Track seen words
    duplicates = set()  # Track duplicate words
    for word in split_word:
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
"""
    
def largest_element(numbers):
   sorted_numbers = sorted(numbers)  # Sort ascending
   largest_number = sorted_numbers[-1]  # Last element is largest
   
   return largest_number
                
numbers = [2, 56, 75, 4566, 3]
print(largest_element(numbers))      

def main():
    result = []
    user = input("type numbers: ").split()
    for num in user:
        result.append(int(num))
        largest_num = sorted(result)[-1]  # BUG: Sorts entire list each iteration (inefficient)
    return largest_num  # Returns largest from final sorted list

main()

"""
Problem: 159
Write a Python program to find the largest element in a list. Prompt the user to enter a list of numbers using max().
"""

def largest_element(numbers):
   return max(numbers)
                
numbers = [2, 56, 75, 4566, 3]
print(largest_element(numbers))   

"""
Problem 160:
Define a function that computes the length of a given list or string. (It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise.)
"""

def find_length(string):  # Works for both strings and lists (iterable)
    count = 0
    for char in string:  # Iterate over elements
        count += 1
    return count
    
arg = "Jonathan"
print(find_length(arg))

"""
Problem: 161
Write a Python program to find the intersection of two lists. Prompt the user to enter two lists using set.
"""

def intersection():
    lst1 = input("type list: ").split()
    lst2 = input("type list: ").split()
    sort1 = sorted(lst1)
    sort2 = sorted(lst2)
    common = []
    for word in sort1:
        if word in sort2:
            common.append(word)
    print(common)
    
intersection()

def intersection():
    lst1 = input("type lst1: ").split()
    lst2 = input("type lst2: ").split()
    set1 = set(lst1)
    set2 = set(lst2)
    common = set1.intersection(set2)
    
    print(common)
    
intersection()

def intersection_two_list(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    result = set1.intersection(set2)
    
    return result
                   
lst1 = ["tree", "car", "house", "garden"]
lst2 = ["car", "boat", "toilet", "tree"]
print(intersection_two_list(lst1, lst2))

"""
Problem 162:
Write a function where user types a list of numbers in string and returns a the third largest number in a list.
"""

def third_largest():
    user_string = input("type number followed by spaces: ")  # e.g., "10 5 20 15 8"
    user_split = user_string.split()  # Split into list of strings
    int_list = []
    for number in user_split:
        int_list.append(int(number))  # Convert strings to integers
    
    int_list.sort()  # Sort ascending: [5, 8, 10, 15, 20]
    result = int_list[-3]  # [-3] is third-to-last (third largest)
    
    print(result)
    
third_largest()

"""
Problem 163:
Write a Python function `count_vowels` that takes a string as input and returns a dictionary with the counts of each vowel ('a', 'e', 'i', 'o', 'u') in the string. Ignore case, so 'A' and 'a' should be counted as the same vowel using list comprehension.
"""

def count_vowels(string):
    vowels = "aeiou"
    result = {}  # Dictionary to store vowel counts
    for vowel in vowels:
        result[vowel] = 0  # Set initial count for each vowel
    
    string = string.lower()  # Convert to lowercase for case-insensitive counting
    for char in string:
        if char in vowels:
            result[char] += 1  # Increment count for found vowel
    
    return result

string = "JOnathAn is the best"
print(count_vowels(string))

def count_vowels(sentence):
    sentence = sentence.lower()
    vowels = "aeiou"
    vowel_counts = {number: 0 for number in vowels}  # {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    for char in sentence:
        if char in vowels:
            vowel_counts[char] += 1
    return vowel_counts
    
string = "Jonathan is the best"    
print(count_vowels(string))

"""
Problem 164:
Write a Python function `count_vowels` that takes a string as input and returns a dictionary with the counts of each vowel ('a', 'e', 'i', 'o', 'u') in the string. Ignore case, so 'A' and 'a' should be counted as the same vowel without using list conprehension.
"""

def count_vowels(sentence):
    sentence = sentence.lower()
    vowels = "aeiou"
    vowel_counts = {}
    for number in vowels:
        vowel_counts[number] = 0
    
    for char in sentence:
        if char in vowels:
            vowel_counts[char] += 1
    
    return vowel_counts

string = "Jonathan is the best"
print(count_vowels(string))

"""
Problem 165:
Write a function that takes numbers integer 123 and splits the numbers into a string ("1", "2", "3").
"""

def intiger_string(number):  # Typo: "intiger" should be "integer"
    return list(str(number))  # str(123) → "123", list("123") → ["1", "2", "3"]
    
number = 123
print(intiger_string(number))

def split_number_int(number):
    number_str = str(number)  # Convert int to string: 123 → "123"
    result = tuple(number_str)  # tuple() constructor converts string to tuple of characters
    
    return result

number = 123
print(split_number_int(number))

"""
Problem 166:
Write a Python function called `double_elements` that takes a list of strings as input and returns a 2 new list where each element is doubled.
"""

def double_elements(lst):
    doubled = []
    for word in lst:
        doubled.append(word)
    for word in lst:
        doubled.append(word)
    return doubled  # Returns list with all elements duplicated: [a, b, c, a, b, c]
    
lst = ["tree", "house", "car"]
print(double_elements(lst))

"""
Problem 167:
Write a Python program to find the largest and smallest elements in a list. Prompt the user to enter a list of numbers using sorted()."
"""

def main():
    user = input("type numbers: ").split()  # Get input and split
    lst = list(sorted(map(int, user)))  # map() is higher-order function that applies function to iterable
    smallest_num = min(lst)  # Could use lst[0] since it's sorted
    largest_num = max(lst)  # Could use lst[-1] since it's sorted
    return smallest_num, largest_num  # Returns tuple
    
main()

def l_s(numbers):
    sort_number_largest = sorted(numbers)[-1]  # Last element after sorting (largest)
    sort_number_smallest = sorted(numbers)[0]  # First element after sorting (smallest)
    
    return sort_number_largest, sort_number_smallest  # Returns tuple
       
numbers = [1, 2, 3, 4, 5]
print(l_s(numbers))

"""
Problem 168:
Write a Python function called count_words that takes a string as input and returns a dictionary where the keys are the words in the string and the values are the counts of each word. Words are separated by spaces, and the function should be case-insensitive, make the keys alphabetical.
"""

def count_words():
    user = input("type words: ").split()
    sort = sorted(user)  # Sort words alphabetically
    result = {}  # Dictionary to store word counts
    for word in sort:
        word = word.lower()  # Convert to lowercase for case-insensitive counting
        if word in result:  # Dictionary membership check
            result[word] += 1  # Increment count if word exists
        else:
            result[word] = 1
    print(result)
    
count_words()

def count_words(string):
    string = string.lower()  # Case-insensitive: convert entire string to lowercase
    words = string.split()  # Split into words
    word_count = {}  # Dictionary for word frequencies
    for word in words:
        if word in word_count:
            word_count[word] += 1  # Increment existing count
        else:
            word_count[word] = 1
    
    sorted_word_count = dict(sorted(word_count.items()))  # Sort dictionary by keys
    return sorted_word_count

input_string = "This is a test. This test is only a test."
print(count_words(input_string))

"""
Problem: 169
Write a function merge_dictionaries that takes two dictionaries as arguments and returns a new dictionary that contains all the key-value pairs from both dictionaries. If a key is present in both dictionaries, the value from the second dictionary should overwrite the value from the first dictionary.
"""

def merge_dictionaries(dict1, dict2):
    merged = dict1.copy()
    for key, value in dict2.items():
        merged[key] = value
    return merged

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

result = merge_dictionaries(dict1, dict2)
print(result)

"""
Problem: 170
 Write a function count_characters that takes a string as input and returns a dictionary where the keys are characters in the string and the values are the counts of those characters.
"""

def count_characters(string):
    counts = {}  # Dictionary to store character frequencies
    for char in string:  # Iterate over each character
        if char in counts:  # Dictionary membership check (O(1) average case)
            counts[char] += 1  # Increment count if character exists
        else:
            counts[char] = 1
    return counts

string = input("Enter a string: ")
result = count_characters(string)
print(result)

"""
Problem: 171
Write a function invert_dictionary that takes a dictionary as input and returns a new dictionary where the keys are the values from the input dictionary, and the values are lists of keys from the input dictionary that had that value.
"""

def invert_dictionary(input_dict):
    inverted = {}  # New dictionary for inverted structure
    for key, value in input_dict.items():
        if value not in inverted:
            inverted[value] = []
        inverted[value].append(key)  # Add key to list of keys that had this value
    return inverted

input_dict = {'a': 1, 'b': 2, 'c': 1}  # 'a' and 'c' both have value 1
result = invert_dictionary(input_dict)  # Result: {1: ['a', 'c'], 2: ['b']}
print(result)

"""
Problem: 172
Write a function filter_by_value that takes a dictionary and a threshold value as input and returns a new dictionary containing only the key-value pairs where the value is greater than the threshold.
"""

def filter_by_value(input_dict, threshold):
    filtered = {}  # New dictionary for filtered results
    for key, value in input_dict.items():  # Iterate over all key-value pairs
        if value > threshold:  # Check if value exceeds threshold
            filtered[key] = value  # Add key-value pair to filtered dict
    return filtered

input_dict = {'a': 5, 'b': 2, 'c': 8}
threshold = 3
result = filter_by_value(input_dict, threshold)  # Result: {'a': 5, 'c': 8} (b: 2 is filtered out)
print(result)

"""
Problem: 172
Write a function filter_by_value that takes a dictionary and a threshold value as input and returns a new dictionary containing only the key-value pairs where the value is greater than the threshold.
"""

def filter_by_value(input_dict, threshold):
    filtered = {}
    for key, value in input_dict.items():
        if value > threshold:
            filtered[key] = value
    return filtered

input_dict = {'a': 5, 'b': 2, 'c': 8}
threshold = 3
result = filter_by_value(input_dict, threshold)
print(result)

"""
Problem: 173
Write a function combine_lists_to_dict that takes two lists—one for keys and one for values—as input and returns a dictionary where each key-value pair is taken from corresponding elements in the input lists.
"""

def combine_lists_to_dict(keys, values):
    combined = {}
    for i in range(len(keys)):
        combined[keys[i]] = values[i]
    return combined

keys = ['a', 'b', 'c']
values = [1, 2, 3]
result = combine_lists_to_dict(keys, values)
print(result)

"""
Problem: 174
Write a function max_value_key that takes a dictionary as input and returns the key associated with the maximum value. If the dictionary is empty, the function should return None.
"""

def max_value_key(input_dict):
    if not input_dict:  # Empty dict is falsy in Python
        return None  # Return None for empty dictionary
    
    max_value = max(input_dict.values())  # Find maximum value in dictionary
    
    for key, value in input_dict.items():
        if value == max_value:  # Found key with maximum value
            return key  # Return first key found with max value

my_dict = {'a': 10, 'b': 5, 'c': 20, 'd': 15}  # Max value is 20 (key 'c')
print(max_value_key(my_dict))  # Output: 'c'

empty_dict = {}
print(max_value_key(empty_dict))  # Output: None

"""
Problem: 175
Write a function dict_equal that takes two dictionaries as input and returns True if they are equal (i.e., they have the same keys with the same corresponding values), and False otherwise.
"""

def dict_equal(dict1, dict2):
    return dict1 == dict2

dict1 = {'a': 1, 'b': 2}
dict2 = {'a': 1, 'b': 2}
result = dict_equal(dict1, dict2)  # True: same keys and values
print(result)

"""
Problem: 176
Write a function word_frequency that takes a string as input and returns a dictionary where the keys are words in the string and the values are the counts of those words.
"""

def word_frequency(string):
    words = string.split()  # Split string into list of words
    result = {}  # Dictionary to store word frequencies
    for word in words:
        if word in result:  # Word seen before
            result[word] += 1  # Increment count
        else:  # First occurrence of word
            result[word] = 1
    return result
            
string = "gore why are you here you are gore"
print(word_frequency(string))  # Result: {'gore': 2, 'why': 1, 'are': 2, 'you': 2, 'here': 1}

"""
Problem: 177
Write a function merge_list_of_dicts that takes a list of dictionaries as input and returns a single dictionary that merges all dictionaries in the list. If any keys are duplicated across dictionaries, the value from the last dictionary in the list should overwrite the previous ones.
"""

def merge_list_of_dicts(dicts):
    merged = {}  # Result dictionary
    for d in dicts:  # Iterate over each dictionary in list
        merged.update(d)  # dict.update() modifies dict in-place, adding/updating entries
    return merged

dicts = [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'a': 5}]
result = merge_list_of_dicts(dicts)  # Result: {'a': 5, 'b': 3, 'c': 4}
print(result)

"""
Problem: 178
Write a function remove_duplicates_from_values that takes a dictionary as input and returns a new dictionary where each key-value pair is preserved, but the values are lists with duplicates removed.
"""

def remove_duplicates_from_values(input_dict):
    new_dict = {}
    for key, value in input_dict.items():
        new_dict[key] = list(set(value))
    return new_dict

input_dict = {'a': [1, 2, 2, 3], 'b': [3, 4, 4, 5], 'c': [1, 1]}
result = remove_duplicates_from_values(input_dict)
print(result)

"""
Problem: 179
Write a function common_keys_max_values that takes two dictionaries and returns a new dictionary that contains only the keys that are present in both input dictionaries. The value for each key in the new dictionary should be the maximum of the values from the two input dictionaries.
"""

def common_keys_max_values(dict1, dict2):
    common_keys = {}
    for key in dict1.keys() & dict2.keys():  # Iterate over common keys only
        common_keys[key] = max(dict1[key], dict2[key])  # Take maximum value
    return common_keys

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 1, 'd': 4}  # Common keys: 'b', 'c'
result = common_keys_max_values(dict1, dict2)  # Result: {'b': 3, 'c': 3} (max values)
print(result)

"""
Problem: 180
Write a function average_values that takes a list of dictionaries as input and returns a new dictionary. The new dictionary should contain the same keys, and the values should be the average of the values associated with each key across all input dictionaries.
"""

def average_values(dicts):
    averages = {}
    counts = {}
    for d in dicts:  # Iterate over each dictionary
        for key, value in d.items():  # Iterate over key-value pairs
            if key in averages:  # Key seen before
                averages[key] += value  # Add to sum
                counts[key] += 1  # Increment count
            else:  # First occurrence of key
                averages[key] = value  # Initialize sum
                counts[key] = 1  # Initialize count
    
    for key in averages:
        averages[key] /= counts[key]  # Divide sum by count to get average
    
    return averages

dicts = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}, {'a': 5, 'b': 6}]
result = average_values(dicts)  # Result: {'a': 3.0, 'b': 4.0} (averages)
print(result)

"""
Problem: 181
Write a function merge_dicts_with_lists that takes a list of dictionaries as input. Each dictionary in the list has keys that are strings and values that are lists of integers. The function should merge these dictionaries into a single dictionary where the keys are preserved, and the values are merged lists containing all unique integers from the input dictionaries for each key.
"""

def merge_dicts_with_lists(dicts):
    merged = {}
    for d in dicts:  # Iterate over each dictionary
        for key, value in d.items():  # value is a list of integers
            if key in merged:  # Key already exists
                merged[key].update(value)  # Add elements from value list to set (removes duplicates)
            else:  # First occurrence of key
                merged[key] = set(value)  # Convert list to set (removes duplicates, allows efficient merging)
    
    for key in merged:
        merged[key] = list(merged[key])  # Convert set to list (order may vary)
    
    return merged

dicts = [{'a': [1, 2, 3], 'b': [2, 3]}, {'a': [3, 4], 'b': [4, 5], 'c': [6]}, {'c': [7, 8, 6]}]
result = merge_dicts_with_lists(dicts)  # Merges lists, removes duplicates
print(result)

"""
Problem: 182
Write a function group_by_first_letter that takes a list of strings as input and returns a dictionary. The dictionary should group the strings by their first letter. Each key in the dictionary should be a first letter, and the corresponding value should be a list of strings that start with that letter.
"""

def group_by_first_letter(lst):
    result = {}  # Dictionary: key = first letter, value = list of words
    for word in lst:
        first_letter = word[0]  # Get first character using index [0]
        if first_letter not in result:  # First word with this starting letter
            result[first_letter] = [word]
        else:  # Letter seen before
            result[first_letter].append(word)  # Add word to existing list
    return result

lst = ["apple", "banana", "orange", "cake"]
print(group_by_first_letter(lst))  # Result: {'a': ['apple'], 'b': ['banana'], 'o': ['orange'], 'c': ['cake']}

def main(lst):
    result = {}
    for word in lst:
        key = word[0]  # First letter
        value = word  # Entire word
        result[key] = value  # BUG: Overwrites previous value instead of appending to list
    return result  # Returns only last word for each letter
        
lst = ["tree", "cliff", "mountain", "zoo","dodo", "grassy"]
main(lst)  # Result: {'t': 'tree', 'c': 'cliff', 'm': 'mountain', 'z': 'zoo', 'd': 'dodo', 'g': 'grassy'}

"""
Problem 183:
Write a Python program to check if a string is an anagram of another string, ignoring whitespace. Prompt the user to enter two strings without using sorted().
"""
        
def is_anagram(string1, string2):
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()
    if len(string1) != len(string2):
        return False
        
    char_count1 = {}
    char_count2 = {}
    for char in string1:
        if char in char_count1:
            char_count1[char] += 1
        else:
            char_count1[char] = 1

    for char in string2:
        if char in char_count2:
            char_count2[char] += 1
        else:
            char_count2[char] = 1
    return char_count1 == char_count2

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

print("Are the strings anagrams?:", is_anagram(string1, string2))

"""
Problem 184:
Write a function that takes numbers integer 123 and return 2.
"""

def int(number):  # Should use different name like get_digit or extract_digit
    number = str(number)  # Convert to string: 123 → "123"
    list_number = list(number)[1]  # Convert to list and get index 1: ["1","2","3"][1] → "2"
    
    return list_number  # Returns string "2", not integer 2
        
number = 123
print(int(number))  # Output: "2" (string)

"""
Problem 185:
Write a function that takes numbers integer 12345678 and return 2, 4, 8.
"""

def int(number):  # Should use different name
    number = str(number)  # Convert to string: 12345678 → "12345678"
    num2 = number[1]  # Index 1: second digit "2"
    num4 = number[3]  # Index 3: fourth digit "4"
    num8 = number[-1]  # Index -1: last digit "8" (negative indexing from end)
    
    return num2, num4, num8  # Returns tuple of strings: ("2", "4", "8")
        
number = 12345678
print(int(number))  # Output: ("2", "4", "8")

"""
Problem 186:
Write a function that takes numbers integer 12346778910 and users indexing to return the number 2, 4, 8
"""

def get_digits(number, indices):
    number_str = str(number)  # Convert to string for indexing: 12345678910 → "12345678910"
    result = []
    for i in indices:  # Iterate over list of indices
        result.append(number_str[i])  # Extract character at index i

    return tuple(result)  # Convert list to tuple: ("2", "4", "8")

number = 12345678910
indices = [1, 3, 7]  # Indices to extract
print(get_digits(number, indices))  # Output: ("2", "4", "8")  

"""
Problem: 187
Write a Python function called `double_elements` that takes a list of strings as input and returns a 2 new list where each element is doubled where each element is doubled side by side eg 'tree', 'tree', 'road', 'road', 'slow', 'slow'.
"""

def double_elements(string1):
    double = []
    for word in string1:
        double.append(word)
        double.append(word)
    
    return double
            
string1 = ["tree", "road", "slow"]
print(double_elements(string1))    

"""
Problem 188:
Write a Python function called get_initials that takes a full name (first and last name jonathan moll) as input and returns  "joNathAn moLL"" of the name in uppercase (NALL in jonathan moll).
"""

def get_initials(name):
    name_list = list(name)  # Convert string to list of characters (mutable)
    name_list[2] = name_list[2].upper()  # 'n' → 'N' (index 2)
    name_list[6] = name_list[6].upper()  # 'a' → 'A' (index 6)
    name_list[11] = name_list[11].upper()  # 'l' → 'L' (index 11)
    name_list[12] = name_list[12].upper()  # 'l' → 'L' (index 12)
    
    return ''.join(name_list)  # join() combines list back into string

name = "jonathan moll"
print(get_initials(name))  # Output: "joNathAn moLL"

def get_initials(name):
    initials = []
    for char in name:
        if char in "nall":  # Check if character is 'n', 'a', or 'l' (case-sensitive)
            initials.append(char.upper())  # Convert to uppercase
        else:
            initials.append(char)  # Keep as-is
    return ''.join(initials)  # Join list into string

name = "jonathan moll"
print(get_initials(name))  # Output: "joNathAn moLL" (uppercases all n, a, l characters)

"""
Problem: 189
Write a Python program to find the sum of the digits in a string. Prompt the user to enter a string containing numbers eg "1234" should return 10.
"""

def sum_digits():
    user = list(input("type number: "))  # Convert string to list of characters
    count = 0
    for number in user:  # 'number' is actually a character (misleading name)
        count += int(number)  # Convert char to int and add: "1"→1, "2"→2, etc.
    print(count)
                
sum_digits()

def digits_string():
    user = input("Type a string containing numbers: ")
    total = 0
    for char in user:
        if char.isdigit():  # isdigit() checks if character is a digit (0-9)
            total += int(char)  # Convert digit char to int and add
            
    print(total)
    
digits_string()

"""
Problem: 190
Write a Python program to remove duplicates from a string and maintain the order of characters. Prompt the user to enter a string
"""

def remove_duplicate():
    user = input("type string: ")
    duplicate = []
    for char in user:
        if char not in duplicate:  # Check if character already seen
            duplicate.append(char)  # Add first occurrence only (preserves order)
    print(duplicate)  # Prints list, not string (could use ''.join(duplicate))
    
remove_duplicate()

"""
Problem: 191
Write a Python function called `find_min` that takes a list of numbers as input and returns the minimum number in the list without sorted().
"""

def find_min():
    user = input("type list: ").split()
    user_int = []
    for number in user:
        user_int.append(int(number))  # Convert strings to integers
    
    min_number = user_int[0]
    for number in user_int:
        if number < min_number:  # If smaller number found
            min_number = number  # Update minimum
    print(min_number)
    
find_min()

"""
Problem 192:
Write a Python function called count_occurrences that takes a list and an element as input and returns the number of times the element appears in the list.
"""

def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:  # Compare each item with target element
            count += 1  # Increment counter when match found
    return count

test_list = [1, 2, 3, 4, 1, 2, 1, 5, 1]
element_to_count = 1
print("Number of occurrences of", element_to_count, ":", count_occurrences(test_list, element_to_count))

def main():
    user = input("type element: ").lower()  # Convert input to lowercase
    count = 0
    for word in lst:  # lst must be defined outside function (global variable)
        if word.lower() == user:  # Case-insensitive comparison
            count += 1
            
    if count == 0:
        return "not in lst"  # Return string if not found
    else:
        return count  # Return count
               
lst = ["Jonathan", "Christopher", "Jeremy", "Jonathan", "bad"]
print(main())

"""
Problem: 193
Write a Python function called `find_min` that takes a list of numbers as user input and returns the minimum number in the list. use sorted().
"""

def find_min_num():
    user = input("type number: ").split()
    int_number = []
    for number in user:
        int_number.append(int(number))
    
    min_num = sorted(int_number)[0]
    print(min_num)
                  
find_min_num()

"""
Problem: 194
Write a Python program to find the largest element in a list. Prompt the user to enter a list of items using max(). Write a list of words.
"""

def largest_element():
    user = input("type list: ").split()
    largest_word = max(user, key=len)  # key=len compares by length, not alphabetically
    
    print(largest_word)
           
largest_element()

"""
Problem: 195
Write a Python program to find the second largest element in a list. Prompt the user to enter a list of items. Write a list of words.
"""

def second_largest_element():
    user_input = input("Enter a list of words: ").split()
    if len(user_input) < 2:  # Edge case: need at least 2 words
        print("The list must contain at least two words.")
        return

    sorted_words = sorted(user_input, key=len, reverse=True)  # reverse=True sorts descending
    print(f"The second largest word is: {sorted_words[1]}")  # Index 1 is second longest

second_largest_element()

def second_largest_element():
    user_input = input("Enter a list of words: ").split()
    if len(user_input) < 2:
        print("The list must contain at least two words.")
        return

    sorted_words = sorted(user_input, key=len)  # Sort ascending (shortest first)
    print(f"The second largest word is: {sorted_words[-2]}")  # [-2] is second-to-last (second longest)

second_largest_element()

def second_largest_element():
    user_input = input("Enter a list of words: ").split()
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
"""

def max_of_three(numbers):
     result = max(list(numbers))  # list() is unnecessary if numbers is already a list
     return result
        
three_numbers = [567, 56, 6]    
print(max_of_three(three_numbers))

"""
Problem: 197
Write a Python program to find the maximum of three numbers. Enter three numbers in a list. Without using any build in fuctions apart from print().
"""

def max_of_three(numbers):
    max_number = numbers[0]
    if numbers[1] > max_number:
        max_number = numbers[1]
        
    if numbers[2] > max_number:
        max_number = numbers[2]
        
    return max_number

three_numbers = [567, 56, 6]
print(max_of_three(three_numbers))

"""
Problem: 198
Write a function that converts centimetets to inches.
"""

def centimeters_inches():
    cm = int(input("type centimeters: "))
    inches = cm * 0.3937  # Conversion factor: multiply centimeters by 0.3937
    print(f"{cm} cm = {inches} inches")  # Displays conversion result
    
centimeters_inches()

"""
Problem 199:
Write a Python function called find_min_max that takes a list of numbers as input and returns a tuple containing the minimum and maximum numbers in the list, dont not call the fuction using print(find_min_max). Do not use sort().
"""

def find_min_max():
    user = input("type list of numbers: ").split()
    int_num = []
    for number in user:
        int_num.append(int(number))
    
    min_num = min(int_num)
    max_num = max(int_num)
    
    print(min_num, max_num)
       
find_min_max()

def find_min_max():
    user = input("type numbers: ").split()
    int_number = []
    for number in user:
        int_number.append(int(number))

    min_number = int_number[0]
    max_number = int_number[0]
    
    for number in int_number:
        if number < min_number:
            min_number = number
        if number > max_number:
            max_number = number
    print(min_number, max_number)
    return min_number, max_number

find_min_max()

"""
Problem 200:
Write a Python program to find the common number in a lists. for this exercise do not use set.
"""

def common_numbers(lst):
    seen = []  # Track numbers we've seen
    common = []  # Track duplicate numbers
    for number in lst:
        if number in seen and number not in common:  # Found duplicate
            common.append(number)  # Add to common (duplicates)
        else:
            seen.append(number)  # Mark as seen (first occurrence)
    
    return common  # Returns list of numbers that appear more than once

lst = [43, 2, 45, 567, 666, 2, 45]  # Duplicates: 2 and 45
print(common_numbers(lst))  # Output: [2, 45]

"""
Problem 201:
Write a Python program to find the common number in a lists. use set().
"""

def common_num(lst):
    unique = set()  # Set to track unique numbers seen
    commom = []  # Typo: "commom" should be "common"
    for number in lst:
        if number in unique:  # Number seen before (duplicate found)
            commom.append(number)  # Add to duplicates list
        else:
            unique.add(number)  # Mark as seen (add to set)
    return commom  # Returns list of duplicate numbers
    
lst = [2, 5, 6, 2, 4, 5]
print(common_num(lst))  # Output: [2, 5] (duplicates)

def common_numbers(lst):
    seen = set()  # Track seen numbers
    common = set()  # Track duplicates (set removes duplicate entries in result)
    for number in lst:
        if number in seen:  # Duplicate found
            common.add(number)  # Add to common set
        else:
            seen.add(number)  # Mark as seen
    return common

lst = [43, 2, 45, 567, 666, 2, 45, 43]
print(common_numbers(lst))  # Output: {2, 45, 43} (set of duplicates)

"""
Problem: 202
Write a function word_frequency that takes a string as input and returns a dictionary where the keys are the characters in the string and the values are the counts of those characters alphabetically.
"""

def word_frequency(string):  # Function name says "word" but counts characters
    string = string.replace(" ", "")  # Remove spaces
    sort_char = sorted(string)  # Sort characters alphabetically
    result = {}  # Dictionary for character counts
    for word in sort_char:  # Variable name 'word' is misleading - it's a character
        if word in result:
            result[word] += 1  # Increment count
        else:
            result[word] = 1  # Initialize count
    return result
            
string = "gore why are you here you are gore"
print(word_frequency(string))  # Counts characters, not words

"""
Problem: 203
Define a function total() that sums and multiplies (respectively) all the numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.
"""

def total(numbers):
    total_numbers = 0
    multiply_numbers = 1
    for number in numbers:
        total_numbers += number  # Accumulate sum
        multiply_numbers *= number  # Accumulate product
    return total_numbers, multiply_numbers  # Returns tuple (sum, product)
            
lst_numbers = [1, 2, 3, 4]
print(total(lst_numbers))  # Output: (10, 24) - tuple of sum and product

"""
Problem 204:
Write a program that maps a list of words into a list of integers representing the words with the lengths of the correponding words.
"""

def list_integers(lst):
    result = []
    for word in lst:
        result.append(word)  # Add word itself (string)
        result.append(len(word))  # Add length of word (integer)
    return result
    
lst = ["join", "Jonathan", "tree"]
print(list_integers(lst))  # Output: ["join", 4, "Jonathan", 8, "tree", 4]

"""
Problem 205:
Write a Python function called `calculate_average` that takes a list of numbers as input and returns the average of those numbers. use len() and sum().
"""

def average(lst):
    sum_lst = sum(lst)  # Built-in sum() adds all numbers
    length = len(lst)  # Built-in len() counts elements
    total = sum_lst / length  # Divide sum by count to get average
    
    return total
               
lst = [2666, 566, 6777]
print(average(lst))  # Output: (2666 + 566 + 6777) / 3 = 10009 / 3 = 3336.333...
    
"""
Problem: 206
Write a Python program to find the maximum of three numbers. Prompt the user to enter three numbers. do not use max().
"""

def max_of_three():
    user = input("type three numbers: ").split()
    int_numbers = []
    for number in user:
        int_numbers.append(int(number))
    if len(number) != 3:  # Should be len(int_numbers) != 3
        print("not enough numbers")
        return
        
    max_number = int_numbers[0]
    if int_numbers[1] > max_number:  # If second is larger
        max_number = int_numbers[1]  # Update maximum
    if int_numbers[2] > max_number:  # If third is larger
        max_number = int_numbers[2]  # Update maximum
        
    print(max_number)
    
max_of_three()

"""
Problem: 207
Write a Python program to find the maximum of of list of numbers. Prompt the user to enter three numbers. do not use max().
"""

def max_of_list():
    user = input("type three numbers: ").split()  # Note: says "three" but algorithm works for any length
    if len(user) != 3:  # Validation check
        print("type more numbers")
        return
    
    int_numbers = []
    for number in user:
        int_numbers.append(int(number))
    max_number = int_numbers[0]
    for number in int_numbers:
        if number > max_number:  # If current number is larger
            max_number = number  # Update maximum
            
    print(max_number)
           
max_of_list()

"""
Problem: 208
Write a Python program to find the maximum of of list of numbers. Prompt the user to enter three numbers. Use max().
"""

def max_of_list():
    user = input("type three numbers: ").split()
    int_numbers = []
    for number in user:
        int_numbers.append(int(number))
    
    max_number = max(int_numbers)  # Built-in max() finds maximum element
                   
    print(max_number)
           
max_of_list()

"""
Problem 209:
Write a program that maps a list of words into a list of integers representing the lengths of the correponding words with the word eg ['jonathan', 8, 'horse', 5, 'today', 5 ].
"""

def list_words(lst):
    words_lengths = []
    for word in lst:
        words_lengths.append(word)  # Add word (string)
        words_lengths.append(len(word))  # Add length (integer) using built-in len()
    return words_lengths
        
lst = ["Jonathan", "horse", "today"]
print(list_words(lst))

"""
Problem 210:
Write a program that maps a list of words into a list of integers representing the lengths of the correponding words with the word eg ['jonathan', 8, 'horse', 5, 'today', 5 ]. Do not use len().
"""

def list_words(lst):
    words_with_lengths = []
    for word in lst:
        count = 0  # Manual length counter
        for char in word:
            count += 1  # Increment for each character
        words_with_lengths.append(word)  # Add word
        words_with_lengths.append(count)
    
    return words_with_lengths

lst = ["Jonathan", "horse", "today"]
print(list_words(lst))

"""
Problem 211:
Write a program that maps a list of words into a list of integers representing the lengths of the correponding words without using len().
"""

def length_words(lst):
    length = []
    for word in lst:
        count = 0
        for char in word:
            count += 1
        length.append(count)
    
    return length
    
lst = ["Jonathan", "chris", "mountain"]
print(length_words(lst))

"""
Problem: 212
Write a Python program to find the intersection of two lists. Prompt the user to enter two lists without using set() and without using intersection().
"""

def intersection():
    lst1 = input("type lst1: ").split()
    lst2 = input("type lst2: ").split()
    common = []
    for word in lst1:
        if word in lst2:  # Check if word exists in second list (membership test)
            common.append(word)  # Add to common if found
    print(common)
    
intersection()

"""
Problem: 213
Write a Python program to print the following pattern:\n*\n* *\n* * *\n* * * *\n* * * * *
"""

for i in range(1, 6):  # i = 1, 2, 3, 4, 5
    print('* ' * i)  # String multiplication: '*' * 3 = '***'
    
"""
Problem: 214
Write a Python program to print the following number pyramid:\n1\n2 2\n3 3 3\n4 4 4 4\n5 5 5 5 5
"""

for i in range(1, 6):  # i = 1, 2, 3, 4, 5
    print((str(i) + ' ') * i)
    # Example: i=3 → "3 " * 3 = "3 3 3 "

"""
Problem: 215
Write a Python program to print a square pattern of stars with a given side length.
"""

def square_pattern(n):
    for i in range(n):  # Outer loop: rows
        for j in range(n):  # Inner loop: columns
            print("*", end=" ")  # Print star with space, end="" prevents newline
        print()  # Print newline after each row
n = 5    
print(square_pattern(n))  # Prints square, then prints None

def print_square_pattern(side_length):
    for i in range(side_length):  # Rows
        for j in range(side_length):  # Columns
            print("*", end=" ")  # end=" " keeps stars on same line with space
        print()  # Newline after each row completes

side_length = int(input("Enter the side length of the square: "))
print_square_pattern(side_length)

"""
Problem: 216
Write a Python program to print a right-angled triangle of numbers:\n1\n1 2\n1 2 3\n1 2 3 4\n1 2 3 4 5
"""

for i in range(1, 6):  # i = 1, 2, 3, 4, 5
    print(' '.join(str(num) for num in range(1, i + 1)))

"""
Problem: 217
Write a Python program to print an inverted pyramid pattern:\n* * * * *\n* * * *\n* * *\n* *\n*",
"""

for i in range(5, 0, -1):  # range(5, 0, -1) = [5, 4, 3, 2, 1] (negative step)
    for j in range(i):  # Print i stars in this row
        print('*', end=' ')  # Print star with space
    print()  # Newline after each row 

"""
Problem: 218
Write a Python program to print a checkerboard pattern of given size.
"""

def print_checkerboard(size):
    for i in range(size):  # Rows
        for j in range(size):  # Columns
            if (i + j) % 2 == 0:  # Even sum: (0,0), (0,2), (1,1), (2,0), etc.
                print('*', end=' ')
            else:  # Odd sum: (0,1), (1,0), (1,2), etc.
                print(' ', end=' ')
        print()  # Newline after each row

size = int(input("Enter the size of the checkerboard: "))
print_checkerboard(size)

"""
Problem: 219
Write a Python program to print Floyd's Triangle.\n1\n2 3\n4 5 6\n7 8 9 10
"""

def print_floyds_triangle(rows):
    num = 1  # Counter for consecutive numbers
    for i in range(1, rows + 1):  # i = 1, 2, 3, 4 (row number)
        for j in range(i):  # Print i numbers in row i
            print(num, end=' ')  # Print current number
            num += 1  # Increment to next number
        print()  # Newline after each row

rows = 4
print_floyds_triangle(rows)

"""
220
Write a Python program to print a diamond pattern of stars for a given number of rows.\nFor example, for 3 rows:\n  *\n ***\n*****\n ***\n  
"""

def print_diamond(rows):
    for i in range(rows):  # i = 0, 1, 2, ..., rows-1
        for j in range(rows - i - 1):  # Spaces: rows-1, rows-2, ..., 0
            print(" ", end="")  # Print space without newline
        
        for k in range(2 * i + 1):  # 2*0+1=1, 2*1+1=3, 2*2+1=5
            print("*", end="")
        print()  # Newline after row

    for i in range(rows - 2, -1, -1):  # i = rows-2, rows-3, ..., 0 (backwards)
        for j in range(rows - i - 1):  # Leading spaces
            print(" ", end="")
            
        for k in range(2 * i + 1):  # Should have closing )
            print("*", end="")  # Syntax error: missing closing parenthesis
        print()

rows = 3
print_diamond(rows)

"""
Problem: 221
Write a Python program to print a hollow square pattern of stars with a given side length.\nFor example, for side length 5:\n*****\n*   *\n*   *\n*   *\n*****
"""

def print_hollow_square(side_length):
    for i in range(side_length):  # Rows
        if i == 0 or i == side_length - 1:  # First or last row
            print('*' * side_length)  # Print full row of stars
        else:  # Middle rows
            # Print: star + spaces + star
            print('*' + ' ' * (side_length - 2) + '*')  # Hollow row

side_length = 5
print_hollow_square(side_length)

"""
Problem: 222
Write a Python program to print a reverse pyramid pattern of numbers:\n1 2 3 4 5\n1 2 3 4\n1 2 3\n1 2\n1"
"""

def print_reverse_pyramid(rows):
    for i in range(rows, 0, -1):  # i = 5, 4, 3, 2, 1 (backwards)
        for j in range(1, i + 1):  # Print numbers 1 to i
            print(j, end=' ')  # Print number with space
        print()  # Newline after each row

rows = 5
print_reverse_pyramid(rows)

"""
223
Write a Python program to print a mirrored right-angled triangle of stars:\n    *\n   **\n  ***\n ****\n*****
"""

def mirrored_right_angled_triangle(rows):
    for i in range(1, rows+1):  # i = 1, 2, 3, 4, 5
        for j in range(rows-i):  # Spaces: 4, 3, 2, 1, 0
            print(" ", end="")  # Print space without newline
            
        for k in range(i):
            print("*", end=" ")  # Print star with space
        print()  # Newline after row

rows = 5
mirrored_right_angled_triangle(rows)

"""
Problem: 224
description": "Write a Python program to print a triangle pattern of letters:\nA\nB B\nC C C\nD D D D\nE E E E E"
"""

def triangle_pattern(rows):
    for i in range(rows):  # i = 0, 1, 2, 3, 4
        letter = chr(65 + i)  # Get letter for current row
        for j in range(i + 1):  # Print letter (i+1) times
            print(letter, end=" ")  # Print letter with space
        print()  # Newline after row

rows = 5
triangle_pattern(rows)

def triangle_pattern(rows):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    for i in range(rows):
        letter = letters[i]
        for j in range(i + 1):
            
            print(letter, end=" ")
            
        print()

rows = 5
triangle_pattern(rows)

"""
Problem: 225
Write a Python program to print a square pattern of numbers:\n1 2 3 4 5\n1 2 3 4 5\n1 2 3 4 5\n1 2 3 4 5\n1 2 3 4 5
"""

r = 5 # r = row
c = 5 # c = column

for n in range(r): # n = number (outer loop: rows)
    for n in range(1, c + 1):  # BUG: 'n' reused, overwrites outer loop variable
        print(n, end = " ")  # Prints 1, 2, 3, 4, 5
    print()  # Newline after each row

def print_square_pattern(size):
    for i in range(size):  # Rows
        for j in range(1, size + 1):  # Columns: numbers 1 to size
            print(j, end=' ')  # Print number with space
        print()  # Newline after row

size = 5
print_square_pattern(size)

"""
Problem: 226
Write a Python program to print a hollow right-angled triangle of stars:\n*\n* *\n*  *\n*   *\n*****
"""

def print_hollow_right_triangle(height):
    for i in range(height):  # i = 0, 1, 2, 3, 4
        if i == height - 1:  # Last row (i = 4 for height=5)
            print('*' * (i + 1))  # Print full row of stars (5 stars)
        else:  # Middle rows (i = 0, 1, 2, 3)
            # Print: star + spaces + star
            print('*' + ' ' * i + '*')  # Hollow row: "*", "* *", "*  *", "*   *"

height = 5
print_hollow_right_triangle(height)

"""
Problem: 226
Write a Python program to print a hollow right-angled triangle of stars:\n*\n* *\n*  *\n*   *\n*****
"""

def print_hollow_right_triangle(height):
    for i in range(height):
        if i == height - 1:
            print('*' * (i + 1))
        else:
            print('*' + ' ' * i + '*')

height = 5
print_hollow_right_triangle(height)

"""
Problem: 227
Write a Python program to print a zigzag pattern of stars for a given number of rows.\nFor example, for 5 rows:\n*   *   *\n * * * *\n  *   *\n * * * *\n*   *   *
"""

def print_zigzag(rows):
    for i in range(rows):  # Rows
        for j in range(rows):  # Columns
            if (i % 2 == 0 and j % (rows - 1) == 0) or (i % 2 == 1 and j % (rows - 1) == 1):
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

rows = 5
print_zigzag(rows)

"""
Problem: 228
Write a Python program to print a cross pattern of stars for a given odd number of rows.\nFor example, for 5 rows:\n*   *\n * *\n  *\n * *\n*   *"
"""

def print_cross(rows):
    for i in range(rows):  # Rows
        for j in range(rows):  # Columns
            if j == i or j == (rows - 1 - i):  # On either diagonal
                print('*', end='')  # Print star
            else:
                print(' ', end='')  # Print space
        print()  # Newline after row

rows = 5
print_cross(rows)

"""
Problem: 229
Write a Python program to print an hourglass pattern of stars:\n*****\n ***\n  *\n ***\n*****
"""

def print_hourglass(rows):
    for i in range(rows):  # i = 0, 1, 2, 3
        print(' ' * i + '*' * (rows - i * 2))  # May produce incorrect pattern for some rows

rows = 4
print_hourglass(rows)

"""
Problem 230:
Write a Python function called count_occurrences that takes a list of elements as input and returns the number of times the elements appears in the list.
"""

def count_occurrences(lst):
    result = {}  # Dictionary: element → count
    for word in lst:  # Iterate over all elements
        if word in result:  # Element seen before
            result[word] += 1  # Increment count
        else:  # First occurrence
            result[word] = 1
    return result

lst = ["tom", "fred", "tom", "chris", "fred"]
print(count_occurrences(lst))  # Output: {'tom': 2, 'fred': 2, 'chris': 1}

"""
Problem 231:
Write a Python program to find the sum of all odd numbers in a list. Prompt the user to enter a list of numbers. Write the function as sort as possible.
"""

def sum_of_odd():
    user = input("type numbers: ").split()
    count = 0
    for number in user:
        number = int(number)  # Convert to int
        if number % 2 != 0:  # Check if odd
            count += number  # Add odd number to sum
    print(count)
            
sum_of_odd()

"""
Problem 232:
Write a Python program to remove vowels from a string. Prompt the user to enter a string. Do not use append().
"""

def remove_vowels():
    user = input("type string: ")
    for char in user:
        if char not in "aeiou":  # Only checks lowercase vowels (case-sensitive)
            print(char, end= "")  # Print char without newline (end="" prevents newline)
            
remove_vowels()

"""
Problem 233:
Write a Python function called `find_min` that takes a list of numbers as input and returns the minimum number in the list. Do not use min().
"""

def find_min(lst):
    min_num = lst[0]
    for number in lst:
        if number < min_num:
            min_num = number
    return min_num
            
lst = [13, 566, 1]
print(find_min(lst))

"""
Problem: 234
Write a Python program to print a square pattern of stars with a given side length. Use a while loop.
"""

i = 1  # Loop counter

while (i < 6):  # Loop 5 times (i = 1, 2, 3, 4, 5)
    print("* " * 5)  # Print 5 stars with spaces (hardcoded, not using variable)
    i += 1  # Increment counter

"""
Problem: 235
Write a Python program that prints a increasing triangle pattern of stars.
"""

def increasing_triangle():
    n = 5
    
    for i in range(n):
        for i in range(i+1):
            print("*", end=" ")
        print()

print(increasing_triangle())

"""
Problem: 236
Write a Python program that prints a decreasing triangle pattern of stars.
"""

def decreasing_triangle():
    n = 5
    for i in range(n):  # i = 0, 1, 2, 3, 4
        for j in range(i, n):  # Print (n-i) stars
            print("*", end=" ")
        print()

print(increasing_triangle())  # BUG: Calls wrong function (should be decreasing_triangle())

"""
Problem: 237
Write a Python program that prints a right triangle pattern of stars.
"""

for i in range(1, 6):  # i = 1, 2, 3, 4, 5
    print((("*") + " ")* i)  # Prints: "* ", "* * ", "* * * ", etc.

def right_triangle(n): 
    for i in range(1, n + 1):  # Rows: 1 to n
        for j in range(i):  # Print i stars
            print("*", end=" ")  # Print star with space
        print()  # Newline after row

number = 5
right_triangle(number)

"""
Problem: 238
Write a Python program that prints a left triangle pattern of stars.
"""

def left_triangle():
    n = 5
    for i in range(n):
        for i in range(i, n):
            print(" ", end=" ")
    for i in range(n):
        for i in range(i + 1):
            print("*", end=" ")
        print()

print(increasing_triangle())

"""
Problem: 239
Write a Python program that prints a hill pattern of stars.
"""

def print_hill_pattern(rows):
    for i in range(rows):  # i = 0, 1, 2, 3, 4
        print(' ' * (rows - i - 1) + '*' * (2 * i + 1))

rows = 5
print_hill_pattern(rows)

"""
Problem: 240
Write a Python program that prints a reverse hill pattern of stars.
"""

def print_reverse_hill_pattern(rows):
    for i in range(rows):  # i = 0, 1, 2, 3, 4
        print(' ' * i + '*' * (2 * (rows - i) - 1))

rows = 5
print_reverse_hill_pattern(rows)
"""
Problem: 241
Write a Python program to print the index and value of each element in a list using `enumerate()`
"""

def enumerate_lst(lst):
    for index, word in enumerate(lst):  # enumerate() provides index-value pairs
        print(f"index {index} name {word}")  # Prints: "index 0 name Jon", etc.
    
    
lst = ["Jon", "Chris", "Nathan"]
print(enumerate_lst(lst))  # Prints indices/values, then prints None 

"""
Problem: 242
Write a Python program to create a list of tuples where each tuple contains the index and the value from a given list using `enumerate()`.
"""

def enumerate_lst(lst):
    result = []
    for index, word in enumerate(lst):
        result.append((index, word))  # Append tuple (index, word) to list
    return result  # Returns: [(0, "Jon"), (1, "Chris"), (2, "Nathan")]
    
lst = ("Jon", "Chris", "Nathan")  # Note: tuple input (works with any iterable)
print(enumerate_lst(lst)) 

"""
Problem: 243
Write a Python program to find the index of the first occurrence of a specific value in a list using `enumerate()`.
"""

def enumerate_lst(lst, target):
    for index, word in enumerate(lst):
        if word == target:
            return word, index 
    return -1
        
target = "Chris"    
lst = ["Jon", "Chris", "Nathan"]
print(enumerate_lst(lst, target)) 

"""
Problem: 244
Write a Python program to print the index and value of each element in a list starting from index 1 using `enumerate()`
"""

def enumerate_lst(lst):
    for index, word in enumerate(lst, start=1):  # start parameter sets initial index
        print(f"Index {index}, Name {word}")  # Prints: "Index 1, Name Jon", etc.

lst = ["Jon", "Chris", "Nathan"]
enumerate_lst(lst)

"""
Problem: 245
Write a Python program to create a dictionary where keys are the indexes and values are the corresponding elements from a list using `enumerate()`.
"""

def enumerate_lst(lst):
    result = {}  # Dictionary: index → value
    for index, word in enumerate(lst):
        result[index] = word  # Assign value to index key
    print(result)
    
lst = ["Jon", "Chris", "Nathan"]
enumerate_lst(lst)

"""
Problem: 246
Write a Python program to filter and print elements of a list that are at even indexes using `enumerate()`
"""

def enumerate_lst(lst):
    for index, word in enumerate(lst):
        if index % 2 != 0:  # This filters odd indexes (1, 3, 5, ...)
            print(index, word)  # Prints elements at odd positions
        
lst = ["Jon", "Chris", "Nathan", "hot", "class", "shirt", "beach", "app", " board", "hit"]
enumerate_lst(lst)  # Prints: 1 Chris, 3 hot, 5 shirt, 7 app, 9 hit (odd indexes)

"""
Problem: 247
Write a Python program to print the index and value of each element in a list using a `for` loop with `enumerate()`.
"""

def enumerate_lst(lst):
    for index, word in enumerate(lst):
        print(f"index {index} name {word}")
    
lst = ["Jon", "Chris", "Nathan", "Sam", "Rachel"]
enumerate_lst(lst)

"""
Problem: 248
Write a Python program to replace each element in a list with its index using `enumerate()`
"""

def replace_with_index(lst):
    for index, _ in enumerate(lst):  # _ is conventional name for unused variable
        lst[index] = index  # Replace element at index with index value itself
    return lst  # Returns modified list: [0, 1, 2, 3, 4]

lst = ["Jon", "Chris", "Nathan", "Sam", "Rachel"]
print(replace_with_index(lst))  # Output: [0, 1, 2, 3, 4] 

"""
Problem: 249
Write a Python program to print the index and values from two lists of equal length side by side using `enumerate()`.
"""

def enumerate_lst(lst1, lst2):
    for index, word in enumerate(lst1):  # Get index and value from lst1
        print(f"index {index}: {word} and {lst2[index]}")  # Prints both values side by side
    
lst1 = ["Jon", "Chris", "Nathan", "Tom", "Sam", "Rose", "Bliss", "Hurt"]
lst2 = ["Jonny", "Christopher", "Jhovian", "Tom", "Zack", "Rose", "Brad", "Michael"]

enumerate_lst(lst1, lst2)

"""
Problem: 250
Write a Python program to calculate the sum of elements in a list that are located at odd indexes using `enumerate()`.
"""

def sum_odd_indexed_elements(lst):
    total = 0
    for index, value in enumerate(lst):
        if index % 2 != 0:  # Check if index is odd (1, 3, 5, ...)
            total += value  # Add value to sum
    return total

lst = [1, 2, 3, 4, 5, 6]
result = sum_odd_indexed_elements(lst)  # Sums elements at indices 1, 3, 5: 2+4+6 = 12
print(result)

"""
Problem: 251
Write a Python program to pair elements from two lists of equal length using `zip()`.
"""

def pair_elements(lst1, lst2):
    paired = list(zip(lst1, lst2))  # zip() pairs elements at same index
    return paired  # Returns: [("Jon", "A"), ("Chris", "B"), ("Nathan", "C"), ("Sam", "D")]

lst1 = ["Jon", "Chris", "Nathan", "Sam"]
lst2 = ["A", "B", "C", "D"]

print(pair_elements(lst1, lst2))

"""
Problem: 252
Write a Python program to find the sum of corresponding elements from two lists using `zip()`.
"""

def sum_of_2_lst(lst1, lst2):
    summed_list = []
    for x, y in zip(lst1, lst2):
        summed_list.append(x + y)
    return summed_list

lst1 = [2, 4, 6, 8]
lst2 = [2, 4, 6, 8]

print(sum_of_2_lst(lst1, lst2))

"""
Problem: 253
Write a Python function to sort a list of tuples by the second element in each tuple using the key parameter.
"""

def sort_tuples_by_second(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1])  # Sort by x[1] (second element)

tuples_list = [(1, 3), (3, 2), (5, 1)]
result = sort_tuples_by_second(tuples_list)  # Sorted by second element: 3, 2, 1
print(result)

"""
Problem: 254
Write a Python program to create a dictionary from two lists, one for keys and one for values, using `zip()`.
"""

def dic_lst(lst1, lst2):
    result = {}
    for x, y in zip(lst1, lst2):  # x from lst1 (key), y from lst2 (value)
        result[x] = y  # Assign value y to key x
    return result  # Returns: {1: "Ron", 2: "break", 3: "tree", 4: "son"}
    
lst1 = [1, 2, 3, 4]
lst2 = ["Ron", "break", "tree", "son"]
print(dic_lst(lst1, lst2))

"""
Problem: 255
Write a Python program to combine three lists into a list of tuples using `zip()`.
"""
def combine_3_lst(lst1, lst2, lst3):
    result = []
    for x, y, z in zip(lst1, lst2, lst3):  # Unpack three elements from zip()
         result.append((x, y, z))  # Append tuple of three elements
         
    return result  # Returns: [("Sam", "Sammy", "Son"), ("Nike", "Mikey", "monkey"), ...]
     
lst1 = ["Sam", "Nike", "system"]
lst2 = ["Sammy", "Mikey", "Steven"]
lst3 = ["Son", "monkey", "star"]
print(combine_3_lst(lst1, lst2, lst3))

"""
Problem: 256
Write a Python program to transpose a 2D matrix (list of lists) using `zip()`.
"""

def transpose_matrix(matrix):
    transposed = zip(*matrix)  # * operator unpacks iterable as arguments
    result = []
    for row in transposed:  # Each row is a tuple from zip()
        result.append(list(row))  # Convert tuple to list
    
    return result  # Returns: [[1,4,7], [2,5,8], [3,6,9]]
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(transpose_matrix(matrix))

"""
Problem: 257
Write a Python program to unzip a list of tuples into individual lists using `zip()`.
"""

def list_tuples(lst):
    unzipped = zip(*lst)  # Unzip: groups elements at same index
    result = []
    for x in unzipped:  # Each x is a tuple of elements at same position
        result.append(list(x))  # Convert tuple to list
    
    
lst = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
print(list_tuples(lst))  # Prints None (function doesn't return)

"""
Problem: 258
Write a Python program to unzip a list of tuples into individual lists using `zip()`.
"""

def individualists(lst):
    result = []
    for num in zip(*lst):
        result.append(list(num))
        
    return result

lst = [(1, 2, 3), (4, 5, 6)]
print(individualists(lst))

"""
Problem: 259
Write a Python program to find the element-wise maximum of two lists using `zip()`.
"""

def maxium_element_wise(lst1, lst2):  # Typo: "maxium" should be "maximum"
    result = []
    for x, y in zip(lst1, lst2):
        result.append(max(x, y))  # max() compares two values, returns larger
    return result  # Returns: [7, 8, 9] (maximum of each pair)
    
lst1 = [2, 4, 6]
lst2 = [7, 8, 9]
print(maxium_element_wise(lst1, lst2))

"""
Problem: 260
Write a Python program to concatenate corresponding strings from two lists using `zip()`
"""

def concatenate(lst1, lst2):
    result = []
    for x, y in zip(lst1, lst2):
        result.append(f"{x} {y}")
    return result  # Returns: ["fruite orange", "apple banana", "tomato carrot"]
    
lst1 = ["fruite", "apple", "tomato"]  # Typo: "fruite" should be "fruit"
lst2 = ["orange", "banana", "carrot"]
print(concatenate(lst1, lst2))

"""
Problem: 261
Write a Python program to combine two lists into a list of dictionaries using `zip()`. Each dictionary should have keys 'a' and 'b'.
"""

def combine_to_dict(lst1, lst2):
    result = []
    for x, y in zip(lst1, lst2):
        result.append({'a': x, 'b': y})  # Append dictionary to list
    
    return result  # Returns: [{'a':1, 'b':'one'}, {'a':2, 'b':'two'}, {'a':3, 'b':'three'}]

lst1 = [1, 2, 3]
lst2 = ['one', 'two', 'three']
print(combine_to_dict(lst1, lst2))

"""
Problem: 262
Write a Python program to filter pairs of elements from two lists where the first element is greater than the second using `zip()`.
"""

def filter_pairs(lst1, lst2):
    result = []
    for x, y in zip(lst1, lst2):
        if x > y:  # Condition: first element greater than second
            result.append((x, y))  # Append tuple if condition met
    
    return result  # Returns: [(5,4), (8,7), (10,2)] (pairs where x > y)

lst1 = [5, 8, 3, 10]
lst2 = [4, 7, 6, 2]
print(filter_pairs(lst1, lst2))

"""
Problem: 263
Write a Python program to filter pairs of elements from two lists where the first element is lesser than the second using `zip()`.
"""

def filter_pairs(lst1, lst2):
    result = []
    for x, y in zip(lst1, lst2):
        if x < y:  # Check if first element is less than second
            result.append((x, y))  # Add tuple if condition met
    
    return result  # Returns: [(3,6)] - only pair where x < y

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
"""

def add_nested_lists(lst1, lst2):
    result = []
    for sublist1, sublist2 in zip(lst1, lst2):
        added_sublist = []
        for x, y in zip(sublist1, sublist2):
            added_sublist.append(x + y)  # Add corresponding elements
        result.append(added_sublist)  # Append summed sublist
    return result  # Returns: [[8,10,12], [14,16,18]]
    
    return result

lst1 = [[1, 2, 3], [4, 5, 6]]
lst2 = [[7, 8, 9], [10, 11, 12]]
print(add_nested_lists(lst1, lst2))

"""
Problem: 265
Write a Python program to calculate the Euclidean distance between two points in 2D space using `zip()`.
"""

import math

def euclidean_distance(point1, point2):
    distance_squared = 0
    for x1, x2 in zip(point1, point2):
        distance_squared += (x1 - x2) ** 2  # (x1-x2)², sum all dimensions
        
    return math.sqrt(distance_squared)  # sqrt((3-6)² + (4-8)²) = sqrt(9+16) = 5

point1 = (3, 4)
point2 = (6, 8)
print(euclidean_distance(point1, point2))  # Output: 5.0

"""
Problem: 266
Write a Python program to interleave two lists into a single list using `zip()`.
"""

def interleave(lst1, lst2):
    result = []
    for x, y in zip(lst1, lst2):
        result.append(x)  # Add element from first list
        result.append(y)  # Add element from second list (alternating)
    return result  # Returns: ["crissy", "spotty", "missy", "motty", "sissy", "hotty"]
        
lst1 = ["crissy", "missy", "sissy"]
lst2 = ["spotty", "motty", "hotty"]
print(interleave(lst1, lst2))

"""
Problem: 267
Write a Python program to multiply corresponding elements of two lists using `zip()`.
"""

def multiply_2_lst(lst1, lst2):
    result = []
    for x, y in zip(lst1, lst2):
        result.append(x * y)  # 2*3=6, 4*6=24, 6*9=54
    return result  # Returns: [6, 24, 54]
            
lst1 = [2, 4, 6]
lst2 = [3, 6, 9]
print(multiply_2_lst(lst1, lst2))  # Output: [6, 24, 54]

"""
Problem: 268
Write a Python program to calculate the dot product of two vectors represented as lists using `zip()`.
"""

def dot_product(vector1, vector2):
    result = 0  # Accumulator for sum
    for x, y in zip(vector1, vector2):
        result += x * y  # Multiply and accumulate: 1*4 + 2*5 + 3*6
    return result  # Returns: 4 + 10 + 18 = 32
    
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]
print(dot_product(vector1, vector2))  # Output: 32

"""
Problem: 269
Write a Python program to filter out all even numbers from a list using `filter()`.
"""

def is_odd(x):
    return x % 2 != 0  # Returns True for odd numbers (1, 3, 5, ...)

def filter_even_numbers(lst):  # Name suggests keeping evens, but actually removes them
    return list(filter(is_odd, lst))  # Returns: [1, 3, 5] (odd numbers only)

lst = [1, 2, 3, 4, 5, 6]
result = filter_even_numbers(lst)  # Filters out evens, keeps odds: [1, 3, 5]
print(result)

"""
Problem: 270
Write a Python program to filter out all odd numbers from a list using `filter()`.
"""

def is_even(x):
    return x % 2 == 0  # Returns True for even numbers

def filter_odd_numbers(lst):  # Function name misleading - filters to keep even numbers
    return list(filter(is_even, lst))  # filter() returns iterator, convert to list

lst = [1, 2, 3, 4, 5, 6]
result = filter_odd_numbers(lst)  # Keeps even numbers: [2, 4, 6]
print(result)

"""
Problem: 271
Write a Python program to filter out all positive numbers from a list using `filter()`.
"""

def is_non_positive(x):
    return x <= 0  # Returns True for 0 and negative numbers

def filter_positive_numbers(lst):  # Name suggests keeping positives, but actually removes them
    return list(filter(is_non_positive, lst))  # Returns: [-2, -1, 0] (non-positive numbers)

lst = [-2, -1, 0, 1, 2, 3]
result = filter_positive_numbers(lst)
print(result)￼

"""
Problem: 272
Write a Python program to filter out all negative numbers from a list using `filter()`.

"""
def is_non_negative(x):
    return x >= 0

def filter_negative_numbers(lst):
    return list(filter(is_non_negative, lst))

lst = [-2, -1, 0, 1, 2, 3]
result = filter_negative_numbers(lst)
print(result)

"""
273
Write a Python program to filter out all words from a list that start with a specific letter using `filter()`.
"""

def filter_words_starting_with_letter(words, letter):
    def starts_with(word):
        return not word.startswith(letter)  # Returns True if word does NOT start with letter

    filtered_words = filter(starts_with, words)
    return list(filtered_words)  # Returns words that don't start with "a": ["banana", "cherry", "blueberry"]

words = ["apple", "banana", "cherry", "apricot", "blueberry"]
letter = "a"
filtered_words = filter_words_starting_with_letter(words, letter)
print(filtered_words)

"""
Problem: 274
Write a Python program to filter out all palindromes from a list of strings using `filter()`.
"""

def is_palindrome(s):
    return s == s[::-1]

def filter_palindromes(lst):
    return list(filter(is_palindrome, lst))

lst = ['madam', 'hello', 'racecar', 'world', 'level']
result = filter_palindromes(lst)
print(result)

"""
275
Write a Python program to filter out all strings from a list that have a specific length using `filter()`.
"""

def filter_by_length(strings, length):
    def check_length(s):
        return len(s) == length  # Returns True if string length matches
    return list(filter(check_length, strings))  # Returns strings with length 5: ["apple", "date"]

strings = ["apple", "banana", "cherry", "date", "fig"]
length = 5
result = filter_by_length(strings, length)
print(result)

def filter_by_length(strings, length):
    
    def has_length(s):
        return len(s) == length

    filtered_strings = filter(has_length, strings)

    return list(filtered_strings)

strings = ["apple", "banana", "cherry", "date", "fig"]
length = 5
result = filter_by_length(strings, length)

print(result) 

"""
Problem: 276
Write a Python program to filter out all numbers from a list that are divisible by a given number using `filter()`.
"""

def filter_divisible(numbers, divisor):
    def is_divisible(n):
        return n % divisor == 0  # Returns True if n is divisible by divisor
    return list(filter(is_divisible, numbers))  # Returns: [10, 15, 20, 25, 30, 35, 40] (all divisible by 5)

numbers = [10, 15, 20, 25, 30, 35, 40]
divisor = 5
result = filter_divisible(numbers, divisor)
print(result)

"""
Problem 277:
Write a Python program to filter out all numbers from a list that are divisible by a given number using `filter()`.
Did you complete the exercise? (y/n)
"""

def is_not_divisible(num, divisor):
    return num % divisor != 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
divisor = 3

filtered_numbers = list(filter(is_not_divisible, numbers))
print(filtered_numbers)  # Output: [1, 2, 5, 7, 8, 10]

"""
Problem: 278
Write a Python program to filter out all non-empty strings from a list using `filter()`.
"""

def filter_non_empty(strings):
    def is_non_empty(s):
        return s != ""  # Returns True if string is not empty
    return list(filter(is_non_empty, strings))  # Returns: ["apple", "banana", "cherry", "date"]

strings = ["apple", "", "banana", "", "cherry", "date", ""]
result = filter_non_empty(strings)
print(result)

"""
Problem: 279
Write a Python program to filter out all prime numbers from a list using `filter()`.
"""

def filter_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    return list(filter(is_prime, numbers))
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17]
result = filter_prime(numbers)
print(result)

"""
Problem: 280
Write a Python program to filter out all floating-point numbers from a list using `filter()`.
"""

def filter_floats(items):
    def is_not_float(x):
        return not isinstance(x, float)  # Returns True if x is NOT a float
    return list(filter(is_not_float, items))  # Returns: [1, "apple", 10, 7] (non-floats)

items = [1, 2.5, "apple", 3.7, 10, 8.9, 7, 4.0]
result = filter_floats(items)
print(result)

"""
Problem: 281
Write a Python program to filter out all uppercase strings from a list using `filter()`.
"""

def filter_uppercase(strings):
    def is_not_uppercase(s):
        return not s.isupper()  # Returns True for "world", "code", "example" (non-uppercase)
    return list(filter(is_not_uppercase, strings))  # Returns: ["world", "code", "example"]

strings = ["HELLO", "world", "PYTHON", "code", "CHATGPT", "example"]
result = filter_uppercase(strings)  # Filters out "HELLO", "PYTHON", "CHATGPT"
print(result)

"""
Problem: 282
Write a Python program to filter out all uppercase strings from a list using `filter()`.
"""

def filter_uppercase_again(strings):
    def is_not_uppercase(s):
        return not s.isupper()  # True for "python", "openai", "example"
    return list(filter(is_not_uppercase, strings))  # Returns: ["python", "openai", "example"]

strings = ["HELLO", "WORLD", "python", "CHATGPT", "openai", "example"]
result = filter_uppercase_again(strings)  # Removes "HELLO", "WORLD", "CHATGPT"
print(result)

"""
Problem: 283
Write a Python program to filter out all non-None values from a list using `filter()`.
"""

def filter_non_none(items):
    def is_not_none(x):
        return x is not None  # Returns True for 1, "example", 3.14, "" (all non-None)
    return list(filter(is_not_none, items))  # Returns: [1, "example", 3.14, ""]

items = [1, None, "example", None, 3.14, "", None]
result = filter_non_none(items)  # Removes all None values
print(result)

"""
Problem: 284
Write a Python program to filter out all elements from a list that contain a specific substring using `filter()`.
"""

def filter_by_substring(items, substring):
    def does_not_contain_substring(s):
        return substring not in s  # Returns True for "banana", "cherry", "grape"
    return list(filter(does_not_contain_substring, items))  # Returns: ["banana", "cherry", "grape"]

items = ["apple", "banana", "cherry", "pineapple", "grape"]
substring = "apple"
result = filter_by_substring(items, substring)  # Removes "apple" and "pineapple"
print(result)

"""
Problem: 285
Write a Python program to print numbers from 1 to 10 using a `while` loop.
"""

def print_1_to_10():
    i = 1
    while i <= 10:  # Loop executes while i is less than or equal to 10
        print(i)  # Print current value of i
        i += 1  # Increment i by 1 (equivalent to i = i + 1)
        
print_1_to_10()  # Output: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 (each on new line)

"""
Problem: 286
Write a Python program to find the sum of the first 10 natural numbers using a `while` loop.
"""

def sum_first_10_natural_numbers():
    i = 1
    total = 0
    while i <= 10:
        total += i
        i += 1
    return total

result = sum_first_10_natural_numbers()
print(result)

"""
Problem: 287
Write a Python program to print all even numbers between 1 and 20 using a `while` loop.
"""

def print_even_numbers():
    i = 1
    while i <= 20:  # Loop from 1 to 20
        if i % 2 == 0:  # Check if current number is even
            print(i)  # Print only if even: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20
        i += 1  # Increment counter regardless of whether number was printed

print_even_numbers()  # Output: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20 (each on new line)

"""
Problem: 288
Write a Python program to print all odd numbers between 1 and 20 using a `while` loop.
"""

def print_odd_numbers():
    i = 1
    while i <= 20:
        if i % 2 != 0:
            print(i)
        i += 1
print_odd_numbers()

"""
Problem: 289
Write a Python program to find the sum of the digits of a given number using a `while` loop.
"""
def sum_of_digits(number):
    total = 0
    while number > 0:
        digit = number % 10  # Get last digit: 5, then 4, then 3, then 2, then 1
        total += digit  # Add digit to total: 0+5=5, 5+4=9, 9+3=12, 12+2=14, 14+1=15
        number //= 10  # Remove last digit: 12345→1234→123→12→1→0
    return total  # Returns: 15 (sum of digits 1+2+3+4+5)

number = 12345
result = sum_of_digits(number)
print(f"The sum of the digits of {number} is: {result}")  # Output: "The sum of the digits of 12345 is: 15"

"""
Problem: 290
Write a Python program to find the sum of the digits of a given number using a `while` loop.
"""

def reverse_number(n):
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10  # Append last digit of n to reversed_num
        n = n // 10  # Remove last digit: 123→12→1→0
    return reversed_num  # Returns reversed number: 12345 → 54321

num = int(input("Enter a number: "))
print("Reversed number:", reverse_number(num))

"""
Problem: 291
Write a Python program to find the factorial of a given number using a `while` loop.
"""

def factorial(number):
    result = 1
    while number > 1:
        result *= number
        number -= 1
    return result

number_to_calculate = 5
result = factorial(number_to_calculate)
print(f"The factorial of {number_to_calculate} is: {result}")

test_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in test_numbers:
    print(f"The factorial of {num} is: {factorial(num)}")

"""
Problem: 292
Write a Python program to print the multiplication table of a given number using a `while` loop.
"""

def multiplication_table(number):
    i = 1
    while i <= 10:
        print(f"{number} x {i} = {number * i}")
        i += 1

number_to_multiply = 5
print(f"Multiplication table for {number_to_multiply}:")
multiplication_table(number_to_multiply)

print("\nMultiplication tables for numbers 1 to 5:")
for num in range(1, 6):
    print(f"\nMultiplication table for {num}:")
    multiplication_table(num)

"""
Problem: 293
Write a Python program to check if a given number is prime using a `while` loop.
"""

def is_prime(number):
    if number < 2:
        return False
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    return True

test_numbers = [1, 2, 3, 4, 5, 10, 13, 17, 20, 23, 24, 29]

print("Prime number check:")
for num in test_numbers:
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
    
"""
Problem: 294
Write a Python program to count the number of digits in a given number using a `while` loop.
"""

def count_digits(number):
    count = 0
    while number > 0:
        number //= 10
        count += 1
    return count

test_numbers = [0, 5, 123, 987654321, 1000000000, -456]

print("Counting digits:")
for num in test_numbers:
    if num < 0:
        print(f"The number of digits in {num} is {count_digits(-num)} (ignoring the negative sign).")
    else:
        print(f"The number of digits in {num} is {count_digits(num)}.")

"""
Problem: 295
Write a Python program to find the GCD (Greatest Common Divisor) of two numbers using a `while` loop.
"""

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = 56
num2 = 98

result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {result}.")

test_cases = [(48, 18), (101, 103), (56, 0), (0, 34), (0, 0)]

print("Testing additional cases:")
for case in test_cases:
    a, b = case
    result = gcd(a, b)
    print(f"The GCD of {a} and {b} is {result}.")

"""
Problem: 296
Write a Python program to print the Fibonacci sequence up to N terms using a `while` loop.
"""

def fibonacci_sequence(n):
    a, b = 0, 1
    count = 0
    while count < n:
        print(a)
        a, b = b, a + b
        count += 1
terms = 10
print(f"Fibonacci sequence up to {terms} terms:")
fibonacci_sequence(terms)

additional_terms = 15
print(f"\nFibonacci sequence up to {additional_terms} terms:")
fibonacci_sequence(additional_terms)

"""
Problem: 297
description": "Write a Python program to find the sum of all elements in a list using a `while` loop.
"""

def sum_elements(lst):
    total = 0
    index = 0
    
    while index < len(lst):
        total += lst[index]
        index += 1
        
    return total

lst = [1, 2, 3, 4, 5]
print(sum_elements(lst))

"""
Problem: 298
Write a Python program to find the largest element in a list using a `while` loop.
"""

def main(lst):
    i = 0
    while i < len(lst):
        return max(lst, key=len)
        i += 1
        
lst = ["tree", "cliff", "mountain", "tree","tree", "grassy"]
main(lst)

def find_largest_element(numbers):
    i = 1
    largest = numbers[0]
    while i < len(numbers):
        if numbers[i] > largest:
            largest = numbers[i]
        i += 1
    return largest

numbers_list = [5, 12, 3, 8, 20, 15]
largest_number = find_largest_element(numbers_list)
print(f"The largest element in the list is: {largest_number}")

additional_numbers_list = [-1, -5, -3, -8]
largest_number_in_negative = find_largest_element(additional_numbers_list)
print(f"The largest element in the list of negatives is: {largest_number_in_negative}")

"""
Problem: 299
Write a Python program to find the smallest element in a list using a `while` loop.
"""

def smallest_element(lst):
    if not lst:
        return None

    smallest_word = lst[0]
    i = 1 

    while i < len(lst):
        if lst[i] < smallest_word:
            smallest_word = lst[i] 
        i += 1  

    return smallest_word

lst = ["hot", "hotty", "hotties"]
print(smallest_element(lst))

"""
Problem: 300
Write a Python program to remove all occurrences of a specific element from a list using a `while` loop.
"""

def remove_all_occurrences(lst, element):
    i = 0
    while i < len(lst):
        if lst[i] == element:
            lst.pop(i)
        else:
            i += 1
    return lst

numbers_list = [1, 2, 3, 4, 3, 5, 3, 6]
element_to_remove = 3
updated_list = remove_all_occurrences(numbers_list, element_to_remove)
print(f"Updated list after removing {element_to_remove}: {updated_list}")

fruits_list = ['apple', 'banana', 'cherry', 'banana', 'date']
fruit_to_remove = 'banana'
updated_fruits_list = remove_all_occurrences(fruits_list, fruit_to_remove)
print(f"Updated fruits list after removing '{fruit_to_remove}': {updated_fruits_list}")

"""
Problem: 301
Write a Python program to check if a given string is a palindrome using a `while` loop.
"""

def is_palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

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

"""
Problem: 302
Write a Python program to count the number of vowels in a given string using a `while` loop.
"""

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    i = 0
    while i < len(s):
        if s[i] in vowels:
            count += 1
        i += 1
    return count

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

"""
Problem: 303
Write a Python program to print each character of a given string using a `while` loop.
"""

def print_each_character(s):
    i = 0
    while i < len(s):
        print(s[i])
        i += 1

test_string_1 = "Hello, World!"
test_string_2 = "Python"
test_string_3 = "While loop example"

print("Characters in test_string_1:")
print_each_character(test_string_1)

print("\nCharacters in test_string_2:")
print_each_character(test_string_2)

print("\nCharacters in test_string_3:")
print_each_character(test_string_3)

"""
Problem: 304
Write a Python program to repeatedly ask for user input until a specific condition is met using a `while` loop.
"""

def ask_until_condition():
    while True:
        user_input = input("Enter a number greater than 10: ")
        if int(user_input) > 10:
            break
            
ask_until_condition()

"""
305
description": "Write a Python program to sort a list of dates by month using `sorted()` with the `key` parameter.
"""

from datetime import datetime

def sort_dates_by_month(dates):
    return sorted(dates, key=lambda date: date.month)

def print_sorted_dates(sorted_dates):
    for date in sorted_dates:
        print(date.strftime("%B"))

def main():
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

"""
306
Write a Python program to sort a list of integers by the sum of their digits using `sorted()` with the `key` parameter.
"""

def sum_of_digits(n):
    total = 0
    for digit in str(n): 
        total += int(digit)
    return total

def integers_lst(lst):
    sorted_lst = sorted(lst, key=sum_of_digits)
    return sorted_lst

lst = [4, 56, 56, 36, 123]
print(integers_lst(lst))

"""
Problem 307:
Write a Python function called find_min_max that takes a list of numbers as input and returns a tuple containing the minimum and maximum numbers in the list, dont not call the fuction using print(find_min_max). Do not use sort() or max() or min().
"""

def find_min_max():
    user = input("type list of numbers: ").split()

    int_num = []
    for number in user:
        int_num.append(int(number))
    
    min_num = int_num[-1]
    max_num = int_num[0]
    
    print(min_num, max_num)
           
find_min_max()

"""
Problem: 308
Write a function group_by_first_letter that takes a list of strings as input and returns a dictionary. The dictionary should group the strings by their first letter. Each key in the dictionary should be a first letter, and the corresponding value should be a list of strings that start with that letter. User should type list as input():
"""

def group_by_first_letter():
    lst = input("type word list: ").split()
    
    result = {}
    for word in lst:
        first_letter = word[0]
        if first_letter not in result:
            result[first_letter] = [word]
        else:
            result[first_letter].append(word)
            
    print(result)
        
group_by_first_letter()

"""
Proplem: 309
Write a increasing triangle using *
"""

def increasing_triangle(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end=" ")
        print()
            
rows = 5
increasing_triangle(rows)

"""
Problem: 310
Write a Python function called find_longest_word that takes a list of words as input and returns the longest word in the list. If there are multiple longest words, return the first one encountered. Do not use sorted().
"""

def find_longest_word(lst):
    longest_word = ""
    count = 0
    
    for word in lst:
        if len(word) > count:
            count = len(word)
            longest_word = word
    return longest_word

lst = ["Jonathan", "noll"]    
print(find_longest_word(lst))

def main(lst):
    return max(lst, key=len)
    
lst = ["tree", "cliff", "mountain", "tree","tree", "grassy"]
main(lst)

"""
Problem: 311
Write a Python function called find_longest_word that takes a list of words as input and returns the longest word in the list. If there are multiple longest words, return the first one encountered. Do not use sorted()and len().
"""

def find_longest_word(lst):
    longest_word = ""
    max_length = 0
    
    for word in lst:
        current_length = 0
        for char in word:
            current_length += 1
        if current_length > max_length:
            max_length = current_length 
            longest_word = word
            
    return longest_word
    
lst = ["Jonathan", "noll", "it"]    
print(find_longest_word(lst))

"""
Problem: 312
Write a Python program to find the second largest number in a list. Prompt the user to enter a list of numbers, do not use a for loop.
"""

def second_largest_number():
    user = input("Type numbers separated by spaces: ").split()
    user_int = list(map(int, user))
    user_int.sort()  
    second_largest = user_int[-2]  

    print(second_largest)

second_largest_number()

"""
Problem: 313
Write a Python program to convert a list of strings to uppercase using `map()`.
"""

def convert_to_uppercase(strings):
    def to_uppercase(s):
        return s.upper()
    return list(map(to_uppercase, strings))

strings = ["hello", "world", "python", "programming"]
uppercase_strings = convert_to_uppercase(strings)
print("Original list:", strings)
print("Uppercase list:", uppercase_strings)

"""
Problem: 314
Write a Python program to convert a list of strings representing numbers to a list of integers using `map()`.
"""

def convert_to_integers(strings):
    def to_integer(s):
        return int(s)
    return list(map(to_integer, strings))

string_numbers = ["1", "2", "3", "4", "5"]
integer_numbers = convert_to_integers(string_numbers)
print("Original list of strings:", string_numbers)
print("Converted list of integers:", integer_numbers)

"""
Problem: 315
Write a Python program to square each number in a list using `map()`.
"""

def square_numbers(numbers):
    def square(x):
        return x * x
    return list(map(square, numbers))

original_numbers = [1, 2, 3, 4, 5]
squared_numbers = square_numbers(original_numbers)
print("Original list of numbers:", original_numbers)
print("Squared list of numbers:", squared_numbers)

"""
Problem: 316
Write a Python program to find the length of each string in a list using `map()`.
"""

def string_lengths(strings):
    def length(s):
        return len(s)
    return list(map(length, strings))

string_list = ["apple", "banana", "cherry", "date"]
lengths = string_lengths(string_list)
print("Original list of strings:", string_list)
print("Lengths of each string:", lengths)

"""
Problem: 317
Write a Python program to convert a list of temperatures from Fahrenheit to Celsius using `map()`.
"""

def fahrenheit_to_celsius(temperatures):
    def to_celsius(f):
        return (f - 32) * 5 / 9
    return list(map(to_celsius, temperatures))

fahrenheit_temps = [32, 68, 100, 212]  # Sample temperatures in Fahrenheit
celsius_temps = fahrenheit_to_celsius(fahrenheit_temps)
print("Temperatures in Fahrenheit:", fahrenheit_temps)
print("Temperatures in Celsius:", celsius_temps)

"""
Problem: 319
Write a Python program to add 5 to each number in a list using `map()`.
"""

def add_five_to_number(x):
    return x + 5

def add_five(lst):
    return list(map(add_five_to_number, lst))

lst = [1, 2, 3, 4]
print(add_five(lst))

"""
Problem: 320
Write a Python program to compute the square root of each number in a list using `map()`.
"""

def main(lst):
    def sqaure_root(num):
        return num ** 2
    return list(map(sqaure_root, lst))
    
lst = [567, 4, 1, 57]
main(lst)

import math
def square_roots(numbers):
    def square_root(x):
        return math.sqrt(x)
    return list(map(square_root, numbers))

number_list = [1, 4, 9, 16, 25]
roots = square_roots(number_list)
print("Original numbers:", number_list)
print("Square roots:", roots)

"""
Problem: 321
Write a Python program to convert a list of strings to a list of their lengths using `map()`.
"""

def lengths_of_strings(strings):
    def length(s):
        return len(s)
    return list(map(length, strings))

string_list = ["apple", "banana", "cherry", "date"]
lengths = lengths_of_strings(string_list)
print("Original strings:", string_list)
print("Lengths of strings:", lengths)

"""
Problem: 322
Write a Python program to normalize a list of scores to a range of 0 to 1 using `map()`.
"""

def normalize_scores(scores):
    def normalize(score):
        min_score = min(scores)
        max_score = max(scores)
        return (score - min_score) / (max_score - min_score)
    return list(map(normalize, scores))

score_list = [50, 60, 70, 80, 90]
normalized_scores = normalize_scores(score_list)
print("Original scores:", score_list)
print("Normalized scores:", normalized_scores)

"""
Problem: 323
Write a Python program to reverse each string in a list using `map()`.
"""

def reverse_strings(strings):
    def reverse(s):
        return s[::-1]
    return list(map(reverse, strings))

string_list = ["hello", "world", "python", "programming"]
reversed_strings = reverse_strings(string_list)
print("Original strings:", string_list)
print("Reversed strings:", reversed_strings)

"""
Problem: 324
Write a Python program to double each number in a list using `map()`.
"""

def double_numbers(numbers):
    def double(x):
        return x * 2
    return list(map(double, numbers))

number_list = [1, 2, 3, 4, 5]
doubled_numbers = double_numbers(number_list)
print("Original numbers:", number_list)
print("Doubled numbers:", doubled_numbers)

"""
Problem: 325
Write a Python program to remove leading and trailing whitespace from each string in a list using `map()`.
"""

def strip_whitespace(strings):
    def strip(s):
        return s.strip()
    return list(map(strip, strings))
string_list = ["  Hello  ", "  World  ", "  Python  ", "  Programming  "]
stripped_strings = strip_whitespace(string_list)
print("Original strings:", string_list)
print("Stripped strings:", stripped_strings)
    
"""
Problem: 326
Write a Python program to create a list of tuples where each tuple contains a number and its square using `map()`.
"""

def number_and_square(numbers):
    def create_tuple(x):
        return (x, x * x)
    return list(map(create_tuple, numbers))

numbers_list = [1, 2, 3, 4, 5]
squared_tuples = number_and_square(numbers_list)
print("Numbers and their squares:", squared_tuples)

"""
Problem: 327
Write a Python program to convert a list of strings to title case using `map()`.
"""

def to_title_case(strings):
    def title_case(s):
        return s.title()
    return list(map(title_case, strings))

words = ["hello world", "python programming", "enumerate function"]
result = to_title_case(words)
print(result)  # ['Hello World', 'Python Programming', 'Enumerate Function']

"""
Problem: 328
Write a Python program to find the second largest number in a list. Prompt the user to enter a list of numbers, do not use a for loop, do not use map().
"""

def second_largest_number():
    user_input = input("Type numbers separated by spaces: ").split()

    user_int = []
    for num in user_input:
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

"""
Problem 329:
Write a function where user types a list of numbers in string and returns a list of numbers from smallest to biggest. Do not use a for loop.
"""

def list_string(numbers):
    sort = sorted(numbers, key=int)
    return sort
   
lst = ["377", "55", "44"]
print(list_string(lst))

def type_smallest_biggest():
    user = input("type number list: ").split()
    sort_number = sorted(user, key=int)
       
    print(sort_number)
    
type_smallest_biggest()

"""
Problem 330:
Write a function where user types a list of numbers in string and returns a list of numbers from biggest to smallest. Do not use a for loop.
"""

def list_of_string_numbers(n):
    sort = sorted(n, key=int)[::-1]
    
    return sort
        
numbers = ["44", "66", "3", "477"]
print(list_of_string_numbers(numbers))

def type_biggest_smallest():
    user = input("Type numbers: ").split()
    int_list = list(map(int, user))
    sorted_list = sorted(int_list, reverse=True)
    
    print(sorted_list)

type_biggest_smallest()

"""
Problem: 331
Write a Python program to print the index and element of each item in a list using `enumerate()`.
"""

def print_index_and_element(lst):
    for index, element in enumerate(lst):
        print(f"Index: {index}, Element: {element}")

lst = ['apple', 'banana', 'cherry']
print_index_and_element(lst)
# Output:
# Index: 0, Element: apple
# Index: 1, Element: banana
# Index: 2, Element: cherry

"""
Problem: 332
Write a Python program to create a list of tuples where each tuple contains an index and the corresponding element from a list using `enumerate()`.
"""

def create_index_element_tuples(lst):
    result = []
    for index, element in enumerate(lst):
        result.append((index, element))
    return result

lst = ['apple', 'banana', 'cherry']
result = create_index_element_tuples(lst)
print(result)  # [(0, 'apple'), (1, 'banana'), (2, 'cherry')]

"""
Problem: 333
Write a Python program to print each element with its index in a list of strings using `enumerate()`.
"""

def print_with_index(strings):
    for index, value in enumerate(strings):
        print(index, value)

strings = ["apple", "banana", "cherry", "date", "fig"]
print_with_index(strings)

"""
Problem: 334
Write a Python program to generate a dictionary where keys are indexes and values are elements from a list using `enumerate()`.
"""

def list_to_dict(lst):
    result = {}
    for index, element in enumerate(lst):
        result[index] = element
    return result

lst = ['apple', 'banana', 'cherry']
result = list_to_dict(lst)
print(result)  # {0: 'apple', 1: 'banana', 2: 'cherry'}

"""
Problem: 335
Write a Python program to find the index of a specific element in a list using `enumerate()`.
"""

def find_index(lst, element):
    for index, value in enumerate(lst):
        if value == element:
            return index
    return -1

lst = ['apple', 'banana', 'cherry']
index = find_index(lst, 'banana')
print(index)  # 1

"""
Problem: 336
Write a Python program to print each element of a list with its index separated by a colon using `enumerate()`.
"""

def print_index_and_element_with_colon(lst):
    for index, element in enumerate(lst):
        print(f"{index}: {element}")

lst = ['apple', 'banana', 'cherry']
print_index_and_element_with_colon(lst)
# Output:
# 0: apple
# 1: banana
# 2: cherry

"""
Problem: 337
Write a Python program to create a list of strings where each string includes its index with a custom prefix using `enumerate()`.
"""

def create_indexed_strings(lst, prefix):
    result = []
    for index, element in enumerate(lst):
        result.append(f"{prefix}{index}: {element}")
    return result

lst = ['apple', 'banana', 'cherry']
result = create_indexed_strings(lst, "Item ")
print(result)  # ['Item 0: apple', 'Item 1: banana', 'Item 2: cherry']

"""
Problem: 338
Write a Python program to modify elements in a list based on their index using `enumerate()`.
"""

def modify_elements(lst):
    for index, element in enumerate(lst):
        if index % 2 == 0:  # Modify elements at even indices
            lst[index] = element.upper()
    return lst

lst = ['apple', 'banana', 'cherry', 'date']
result = modify_elements(lst)
print(result)  # ['APPLE', 'banana', 'CHERRY', 'date']

"""
339
Write a Python program to compute the sum of elements in a list where each element is multiplied by its index using `enumerate()`.
"""

def sum_of_elements(lst):
    total_sum = 0
    
    for i, num in enumerate(lst):
        total_sum += i * num  
    return total_sum

lst = [2, 4, 6, 8]
print(sum_of_elements(lst))

"""
Problem: 340
Write a Python program to print elements from a list that are located at odd indexes using `enumerate()`.
"""

def print_odd_index_elements(lst):
    for index, element in enumerate(lst):
        if index % 2 != 0:
            print(element)

lst = ['apple', 'banana', 'cherry', 'date']
print_odd_index_elements(lst)
# Output:
# banana
# date

"""
Problem: 341
Write a Python program to create a list of tuples where each tuple contains an index and element from a list, but only if the element starts with a vowel, using `enumerate()`.
"""

def index_element_if_vowel(lst):
    result = []
    vowels = 'aeiouAEIOU'
    for index, element in enumerate(lst):
        if element[0] in vowels:
            result.append((index, element))
    return result

lst = ['apple', 'banana', 'orange', 'grape']
result = index_element_if_vowel(lst)
print(result)  # [(0, 'apple'), (2, 'orange')]

"""
Problem: 342
Write a Python program to find the maximum element in a list and its index using `enumerate()`.
"""

def find_max_and_index(lst):
    max_element = lst[0]
    max_index = 0
    for index, element in enumerate(lst):
        if element > max_element:
            max_element = element
            max_index = index
    return max_index, max_element

lst = [10, 20, 30, 25]
index, max_element = find_max_and_index(lst)
print(f"Max element: {max_element}, Index: {index}")
# Output: Max element: 30, Index: 2

"""
Problem: 343
Write a Python program to create a list of tuples with index and element, but exclude the first N elements using `enumerate()`.
"""

def index_and_element_excluding_first_n(lst, n):
    result = []
    for index, element in enumerate(lst):
        if index >= n:
            result.append((index, element))
    return result

lst = ['apple', 'banana', 'cherry', 'date', 'elderberry']
result = index_and_element_excluding_first_n(lst, 2)
print(result)  # [(2, 'cherry'), (3, 'date'), (4, 'elderberry')]

"""
Problem: 344
Write a Python program to print each number in a list along with its index squared using `enumerate()`.
"""

def print_index_squared(numbers):
    for index, number in enumerate(numbers):
        print(f"Index: {index}, Squared: {number ** 2}")

lst = [1, 2, 3, 4, 5]
print_index_squared(lst)

"""
Problem: 345
Write a Python program to replace elements in a list based on their index using `enumerate()`. For example, replace even indexed elements with 'Even' and odd indexed elements with 'Odd'.
"""

def replace_based_on_index(lst):
    for index, element in enumerate(lst):
        if index % 2 == 0:
            lst[index] = 'Even'
        else:
            lst[index] = 'Odd'
    return lst

lst = ['a', 'b', 'c', 'd', 'e']
result = replace_based_on_index(lst)
print(result)

"""
Problem: 346
Write a Python program that defines a function `sum_of_squares()` which contains a nested function `square()` that squares a number. The `sum_of_squares()` function should sum the squares of two numbers.
"""

def sum_of_squares(a, b):
    def square(x):
        return x * x
    return square(a) + square(b)

result = sum_of_squares(3, 4)
print(result)

"""
Problem: 347
Write a Python program that defines a function `greet()` which contains a nested function `get_name()` to prompt the user for their name. The `greet()` function should return a greeting message using the name.
"""

def greet():
    def get_name():
        return input("What is your name? ")
    name = get_name()
    return f"Hello, {name}!"

result = greet()
print(result)

"""
Problem: 348
Write a Python program that defines a function `factorial()` which contains a nested recursive function `inner_factorial()` to calculate the factorial of a number.
"""

def factorial(n):
    def inner_factorial(x):
        if x == 0:
            return 1
        else:
            return x * inner_factorial(x - 1)
    return inner_factorial(n)

result = factorial(5)
print(result)

"""
Problem: 349
Write a Python program that defines a function `add_prefix()` which contains a nested function `prefix_string()` that adds a given prefix to a string. The `add_prefix()` function should return the prefixed string.
"""

def add_prefix(prefix):
    
    def prefix_string(string):
    
        return prefix + string
    

    return prefix_string

prefix_func = add_prefix("pre-")
result = prefix_func("fix") 
print(result)

def add_prefix(prefix):
    
    def prefix_string(string):
        return prefix + string
    
    return prefix_string

prefix_func = add_prefix("pre-")

result1 = prefix_func("fix")
result2 = prefix_func("view")
result3 = prefix_func("dict")

print(result1)  # Output: "pre-fix"
print(result2)  # Output: "pre-view"
print(result3)  # Output: "pre-dict"

"""
Problem: 350
Write a Python program that defines a function `check_even()` which contains a nested function `is_even()` that checks if a number is even. The `check_even()` function should return whether the number is even.
"""

def check_even(num):
    def is_even(x):
        return x % 2 == 0
    return is_even(num)

result = check_even(10)
print(result)

"""
Problem: 351
Write a Python program that defines a function `power()` which contains a nested function `calculate_power()` that raises a number to a given power. The `power()` function should return the result.
"""

def power(base, exponent):
    def calculate_power(b, e):
        return b ** e
    return calculate_power(base, exponent)

result = power(2, 3)
print(result)

"""
Problem: 352
Write a Python program that defines a function `area_circle()` which contains a nested function `calculate_area()` that computes the area of a circle given its radius. The `area_circle()` function should return the area.
"""

def area_circle(radius):
    def calculate_area(r):
        return 3.14159 * r * r
    return calculate_area(radius)

result = area_circle(5)
print(result)

def main():
    def inner(radius):
        return  3.14159 * radius * radius
    return inner(n)
n = 6
main()

"""
Problem: 353
Write a Python program that defines a function `capitalize_words()` which contains a nested function `capitalize()` that capitalizes a word. The `capitalize_words()` function should return a string with each word capitalized.
"""

def capitalize_words(sentence):
    def capitalize(word):
        return word.capitalize()
    words = sentence.split()
    capitalized_words = []
    for word in words:
        capitalized_words.append(capitalize(word))
    return ' '.join(capitalized_words)

result = capitalize_words("hello world from python")
print(result)

"""
Problem: 354
Write a Python program that defines a function `is_palindrome()` which contains a nested function `reverse_string()` that checks if a string is a palindrome.
"""

def is_palindrome(word):
    def reverse_string(s):
        return s[::-1]
    return word == reverse_string(word)

result = is_palindrome("radar")
print(result)

"""
Problem: 355
Write a Python program that defines a function `concatenate_strings()` which contains a nested function `join_strings()` that concatenates two strings.
"""

def concatenate_strings(str1, str2):
    def join_strings(s1, s2):
        return s1 + s2
    return join_strings(str1, str2)

result = concatenate_strings("Hello, ", "world!")
print(result)

"""
Problem: 356
Write a Python program that defines a function `fibonacci()` which contains a nested recursive function `fib()` to generate the Fibonacci sequence up to a given number of terms.
"""

def fibonacci(n):
    def fib(x):
        if x <= 1:
            return x
        else:
            return fib(x - 1) + fib(x - 2)
    return [fib(i) for i in range(n)]

result = fibonacci(10)
print(result)

"""
Problem: 357
Write a Python program that defines a function `to_uppercase()` which contains a nested function `convert()` that converts a string to uppercase.
"""

def to_uppercase(string):
    def convert(s):
        return s.upper()
    return convert(string)

result = to_uppercase("hello world")
print(result)

"""
Problem: 358
Write a Python program that defines a function `find_largest()` which contains a nested function `compare()` that compares two numbers and returns the larger one.
"""

def find_largest(a, b):
    def compare(x, y):
        if x > y:
            return x
        else:
            return y
    return compare(a, b)

result = find_largest(10, 20)
print(result)

"""
Problem: 359
Write a Python program that defines a function `calculator()` which contains nested functions for `add()`, `subtract()`, `multiply()`, and `divide()`. The `calculator()` function should perform the selected operation.
"""

def calculator(operation, a, b):
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero"

    if operation == 'add':
        return add(a, b)
    elif operation == 'subtract':
        return subtract(a, b)
    elif operation == 'multiply':
        return multiply(a, b)
    elif operation == 'divide':
        return divide(a, b)
    else:
        return "Invalid operation"

result = calculator('add', 5, 3)
print(result)

"""
Problem: 360
Write a Python program that defines a function `is_prime()` which contains a nested function `check_divisibility()` to check if a number is prime.
"""

def is_prime(n):
    def check_divisibility(x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True
    return check_divisibility(n)

result = is_prime(7)
print(result)

"""
Problem: 361
Write a Python program that defines a function `count_vowels()` which contains a nested function `is_vowel()` to count the number of vowels in a string.
"""

def count_vowels(string):
    def is_vowel(char):
        return char in 'aeiouAEIOU'

    count = 0
    for char in string:
        if is_vowel(char):
            count += 1
    return count

result = count_vowels("Hello World")
print(result)

"""
Problem: 362
Write a Python program that defines a function `calculate_average()` which contains a nested function `sum_numbers()` to calculate the average of a list of numbers.
"""

def calculate_average(numbers):
    def sum_numbers(nums):
        total = 0
        for num in nums:
            total += num
        return total

    return sum_numbers(numbers) / len(numbers)

result = calculate_average([1, 2, 3, 4, 5])
print(result)

"""
Problem: 363
Write a Python program that defines a function `reverse_string()` which contains a nested function `reverse()` that reverses a given string.
"""

def reverse_string():
    def reverse(s):
        return s[::-1]
    return reverse

reverse_func = reverse_string()
print(reverse_func("Hello, World!"))  

def reverse_string(string):
    def reverse(s):
        reversed_str = ''
        for char in s:
            reversed_str = char + reversed_str
        return reversed_str
    return reverse(string)

result = reverse_string("Hello")
print(result)

"""
Problem: 364
Write a Python program that defines a function `is_sorted()` which contains a nested function `compare_elements()` to check if a list is sorted in ascending order.
"""

def is_sorted(lst):
    def compare_elements():
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                return False
        return True
    return compare_elements()

result = is_sorted([1, 2, 3, 4, 5])
print(result)

def is_sorted():
    return compare_elements(lst)
    
def compare_elements(lst):
    if lst == sorted(lst):
        return True
    return False

lst = [1,2,3,4,5]
is_sorted()

"""
Problem: 365
Write a Python program that defines a function `generate_squares()` which contains a nested function `square()` to generate a list of squares of numbers from 1 to n.
"""

def generate_squares(n):
    def square(x):
        return x * x
    squares = []
    for i in range(1, n + 1):
        squares.append(square(i))
    return squares

result = generate_squares(5)
print(result)

"""
Problem: 366
Write a Python program that defines a main function `sum_of_two()` and a helper function `add(a, b)` that adds two numbers together. The `sum_of_two()` function should call the helper function and return the result.
"""

def sum_of_two(a, b):
    def add(x, y):
        return x + y
    return add(a, b)

result = sum_of_two(3, 5)
print(result)

"""
Problem: 367
Write a Python program that defines a main function `even_or_odd()` and a nested function `is_even(n)` that checks if a number is even. The `even_or_odd()` function should use the helper function to print whether the number is even or odd.
"""

def even_or_odd(n):
    def is_even(x):
        return x % 2 == 0
    if is_even(n):
        print(f"{n} is even")
    else:
        print(f"{n} is odd")

even_or_odd(10)

"""
Problem: 368
Write a Python program that defines a main function `convert_temperature()` and a helper function `celsius_to_fahrenheit(c)` that converts a temperature from Celsius to Fahrenheit. The `convert_temperature()` function should use the helper function to return the converted temperature.
"""

def convert_temperature(celsius):
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    return celsius_to_fahrenheit(celsius)

result = convert_temperature(25)
print(result)

"""
Problem: 369
Write a Python program that defines a main function `rectangle_area()` and a helper function `calculate_area(length, width)` that calculates the area of a rectangle. The `rectangle_area()` function should use the helper function to return the area.
"""

def rectangle_area(length, width):
    def calculate_area(l, w):
        return l * w
    return calculate_area(length, width)

result = rectangle_area(5, 10)
print(result)

"""
Problem: 370
Write a Python program that defines a main function `check_prime()` and a helper function `is_prime(n)` that checks if a number is prime. The `check_prime()` function should use the helper function to return whether the number is prime.
"""

def check_prime(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    return is_prime(n)

result = check_prime(11)
print(result)

"""
Problem: 371
Write a Python program that defines a main function `find_minimum()` and a helper function `min_of_three(a, b, c)` that returns the minimum of three numbers. The `find_minimum()` function should use the helper function to return the minimum value.
"""

def find_minimum(a, b, c):
    def min_of_three(x, y, z):
        return min(x, y, z)
    return min_of_three(a, b, c)

result = find_minimum(5, 3, 8)
print(result)

"""
372
Write a Python program that defines a main function `greet_user()` and a helper function `get_name()` that prompts the user for their name. The `greet_user()` function should use the helper function to print a greeting message.
"""

def greet_user():
    name = get_name()
    print(f"Hello, {name}! Welcome!")

def get_name():
    name = input("Type your name: ")
    return name

greet_user()

"""
Problem: 373
Write a Python program that defines a main function `calculate_factorial()` and a helper function `factorial(n)` that calculates the factorial of a number. The `calculate_factorial()` function should use the helper function to return the factorial.
"""

def calculate_factorial(n):
    def factorial(num):
        if num == 0 or num == 1:
            return 1
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result
    return factorial(n)

result = calculate_factorial(5)
print(result)

"""
Problem: 374
Write a Python program that defines a main function `capitalize_words()` and a helper function `capitalize(word)` that capitalizes the first letter of a word. The `capitalize_words()` function should use the helper function to capitalize each word in a sentence.
"""

def capitalize_words(sentence):
    def capitalize(word):
        return word[0].upper() + word[1:]

    words = sentence.split()
    capitalized_words = []
    for word in words:
        capitalized_words.append(capitalize(word))
    return ' '.join(capitalized_words)

result = capitalize_words("hello world from python")
print(result)

"""
Problem: 375
Write a Python program that defines a main function `find_largest()` and a helper function `max_in_list(lst)` that returns the largest number in a list. The `find_largest()` function should use the helper function to find and return the largest number.
"""

def max_in_list(lst):
    return max(lst)  

def find_largest():
    largest = max_in_list(lst)
    return largest

lst = [12, 45, 7, 23, 67756, 89, 34]
print(find_largest())  

def max_in_list(lst):
    if not lst:
        return None
    return max(lst)  

def find_largest():
    numbers = [12, 45, 7, 23, 56, 89, 34]
    largest = max_in_list(numbers)
    return largest

print(find_largest())  

"""
Problem: 376
Write a Python program that defines a main function `reverse_string()` and a helper function `reverse(s)` that reverses a given string. The `reverse_string()` function should use the helper function to return the reversed string.
"""

def reverse_string(s):
    def reverse(s):
        reversed_str = ''
        for char in s:
            reversed_str = char + reversed_str
        return reversed_str
    return reverse(s)

result = reverse_string("hello")
print(result)

"""
Problem: 377
Write a Python program that defines a main function `calculate_average()` and a helper function `average(lst)` that calculates the average of a list of numbers. The `calculate_average()` function should use the helper function to return the average.
"""

def calculate_average(lst):
    def average(lst):
        total = 0
        for num in lst:
            total += num
        return total / len(lst)

    return average(lst)

result = calculate_average([10, 20, 30, 40])
print(result)

"""
Problem: 378
Write a Python program that defines a main function `check_palindrome()` and a helper function `is_palindrome(s)` that checks if a string is a palindrome. The `check_palindrome()` function should use the helper function to return whether the string is a palindrome.
"""

def check_palindrome(s):
    def is_palindrome(s):
        return s == s[::-1]

    return is_palindrome(s)

result = check_palindrome("racecar")
print(result)

"""
Problem: 379
Write a Python program to find the number closest to zero in a list of numbers using the `key` parameter in the `min()` function.
"""

def closest_to_zero(numbers):
    closest = numbers[0]
    for num in numbers:
        if abs(num) < abs(closest):
            closest = num
    return closest

result = closest_to_zero([-5, 2, 3, -1, 0, -7])
print(result)

"""
Problem: 380
Write a Python program that defines a main function `check_sorted()` and a helper function `is_sorted(lst)` that checks if a list is sorted in ascending order. The `check_sorted()` function should use the helper function to return whether the list is sorted.
"""

def check_sorted(lst):
    def is_sorted(lst):
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                return False
        return True

    return is_sorted(lst)

result = check_sorted([1, 2, 3, 4])
print(result)

"""
Problem 381:
Write a function where user types a list of numbers in string and returns a list of numbers in integer. Do not use a for loop.
"""

user = input("type numbers: ").split()

print(list(map(int, user)))
    

def convert_to_integers(strings):
    return list(map(int, strings))

numbers_in_strings = ["10", "20", "30", "40"]

print(convert_to_integers(numbers_in_strings))

"""
Problem: 382
Write a Python program to sort a list of strings by their length using the `key` parameter in the `sorted()` function.
"""

def sort_strings_by_length(strings):
    sorted_strings = sorted(strings, key=len)
    return sorted_strings

result = sort_strings_by_length(["apple", "fig", "banana", "kiwi"])
print(result)

"""
383
Write a Python program to sort a list of strings by their length using the `key` parameter in the `sorted()` function.
"""

def length_strings(lst):
    sort = sorted(lst, key=len)
    return sort
    
lst = ["Jonathan", "chris", "mimi"]
print(length_strings(lst))

"""
Problem: 384
Write a Python program to sort a list of tuples based on the second element using the `key` parameter in the `sorted()` function.
"""

def sort_tuples_by_second(tuples):
    sorted_tuples = sorted(tuples, key=lambda x: x[1])
    return sorted_tuples

result = sort_tuples_by_second([(1, 3), (2, 1), (3, 2)])
print(result)

"""
Problem: 385
Write a Python program to sort a list of dictionaries based on the value of a specific key using the `key` parameter in the `sorted()` function.
"""

def sort_dicts_by_key(dicts, key_name):
    sorted_dicts = sorted(dicts, key=lambda x: x[key_name])
    return sorted_dicts

result = sort_dicts_by_key([{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}], "age")
print(result)

"""
Problem: 386
Write a Python program to find the longest word in a list of words using the `key` parameter.
"""

def longest_word(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

result = longest_word(["apple", "banana", "cherry", "date"])
print(result)

"""
Problem: 387
Write a Python program to sort a list of numbers based on their absolute value using the `key` parameter in the `sorted()` function.
"""

def sort_by_absolute_value(numbers):
    sorted_numbers = sorted(numbers, key=abs)
    return sorted_numbers

result = sort_by_absolute_value([-2, -3, 1, 5, -4])
print(result)

"""
Problem: 388
Write a Python program to sort a list of strings by the last character of each string using the `key` parameter in the `sorted()` function.
"""

def sort_strings_by_last_character(strings):
    sorted_strings = sorted(strings, key=lambda x: x[-1])
    return sorted_strings

result = sort_strings_by_last_character(["banana", "apple", "grape", "kiwi"])
print(result)

def main(lst):
    def inner(word):
        return word[-1]
    return list(sorted(lst, key=inner))
    
lst = ["treez", "cliff", "mountain", "tree","tree", "grassya"]
main(lst)

"""
Problem: 389
Write a Python program to find the earliest date in a list of date strings (in 'YYYY-MM-DD' format) using the `key` parameter in the `min()` function.
"""

def earliest_date(dates):
    earliest = min(dates)
    return earliest

result = earliest_date(["2023-10-01", "2024-01-15", "2022-12-31"])
print(result)

"""
Problem: 390
Write a Python program to sort a list of names by surname using the `key` parameter in the `sorted()` function.
"""

def get_surname(name):
    return name.split()[-1]

names = [
    "John Doe",
    "Jane Smith",
    "Alice Johnson",
    "Bob Brown",
    "Charlie Davis"
]

sorted_names = sorted(names, key=get_surname)

print(sorted_names)

"""
Problem: 391
Write a Python program to sort a list of strings alphabetically, ignoring case, using the `key` parameter in the `sorted()` function.
"""

def sort_strings_alphabetically(strings):
    return sorted(strings, key=str.lower)

strings = ["banana", "Apple", "cherry", "Date", "fig", "Grape"]
sorted_strings = sort_strings_alphabetically(strings)
print(sorted_strings)

"""
Problem: 392
Write a Python program to find the word with the highest Scrabble score in a list of words using the `key` parameter.
"""

def scrabble_score(word):
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
        total_score += score_chart.get(letter, 0)
    return total_score

def find_highest_scrabble_word(words):
    highest_word = max(words, key=scrabble_score)
    return highest_word

result = find_highest_scrabble_word(["hello", "world", "python", "scrabble"])
print(result)

"""
Problem: 393
Write a Python program to sort a list of complex numbers by their magnitude using the `key` parameter in the `sorted()` function.
"""

def sort_complex_numbers(complex_numbers):
    def get_magnitude(c):
        return abs(c)

    sorted_numbers = sorted(complex_numbers, key=get_magnitude)
    return sorted_numbers

result = sort_complex_numbers([3 + 4j, 1 + 1j, 0 + 2j, 5 + 0j])
print(result)

"""
Problem: 394
Write a Python program to find the file with the largest size in a list of file paths using the `key` parameter and `os.path.getsize`.
"""

import os

def find_largest_file(file_paths):
    def get_file_size(file_path):
        return os.path.getsize(file_path)

    largest_file = max(file_paths, key=get_file_size)
    return largest_file

"""
Problem: 395
Write a Python program to sort a list of fractions (using the `fractions.Fraction` class) by their value using the `key` parameter in the `sorted()` function.
"""

from fractions import Fraction

def sort_fractions(fractions):
    def get_fraction_value(frac):
        return float(frac)

    sorted_fractions = sorted(fractions, key=get_fraction_value)
    return sorted_fractions

result = sort_fractions([Fraction(1, 2), Fraction(1, 3), Fraction(2, 3), Fraction(1, 4)])
print(result)

"""
Problem: 396
Write a Python program to sort a list of tuples based on the sum of their elements using the `key` parameter in the `sorted()` function.
"""

def sort_tuples_by_sum(tuples):
    def get_sum(tup):
        return sum(tup)

    sorted_tuples = sorted(tuples, key=get_sum)
    return sorted_tuples

result = sort_tuples_by_sum([(1, 2), (3, 4), (1, 1), (2, 2)])
print(result)

def main(lst_tuples):
    def inner(tup):
        return tup[0] + tup[1]
    return list(sorted(lst_tuples, key=inner))
    
lst_tuples = [(1,64),(7,3),(2,9)]
print(main(lst_tuples))

"""
Problem: 397
Write a Python program to find the number closest to zero in a list of numbers using the `key` parameter in the `min()` function.
"""

def closest_to_zero(numbers):
    closest = min(numbers, key=abs)
    return closest

result = closest_to_zero([-5, 2, 3, -1, 0, -7])
print(result)

"""
Problem: 398
Write a Python program to sort a list of 2D points (tuples) by their distance from the origin using the `key` parameter in the `sorted()` function.
"""

def sort_points_by_distance(points):
    def get_distance(point):
        return (point[0]**2 + point[1]**2)**0.5

    sorted_points = sorted(points, key=get_distance)
    return sorted_points

result = sort_points_by_distance([(3, 4), (1, 1), (0, 2), (5, 0)])
print(result)

"""
Problem: 399
Write a Python program to sort a list of words by the number of distinct letters in each word using the `key` parameter in the `sorted()` function.
"""

def sort_words_by_distinct_letters(words):
    def distinct_letter_count(word):
        return len(set(word))

    sorted_words = sorted(words, key=distinct_letter_count)
    return sorted_words

result = sort_words_by_distinct_letters(["apple", "banana", "cherry", "date"])
print(result)

"""
Problem: 400
Write a Python program to find the word with the highest sum of ASCII values of its characters in a list of words using the `key` parameter.
"""

def main(lst):
    def inner(word):
        count = 0
        for char in word:
            count += ord(char)
        return count
    return max(lst, key=inner)

lst = ["aa", "bb", "cc", "dg","uu", "ak"]
main(lst)

def ascii_value(word):
    total_value = 0
    for char in word:
        total_value += ord(char)
    return total_value

def find_highest_ascii_word(words):
    highest_word = max(words, key=ascii_value)
    return highest_word

result = find_highest_ascii_word(["hello", "world", "python", "scrabble"])
print(result)

"""
Problem: 401
Write a Python program to sort a list of strings by the number of vowels in each string using the `key` parameter in the `sorted()` function."
"""

def count_vowels(s):
    vowels = "aeiou"
    count = 0
    s = s.lower() 
    
    for char in s:
        if char in vowels:
            count += 1
    return count

def sort_by_vowel_count(strings):
    return sorted(strings, key=count_vowels)

strings = ["apple", "banana", "cherry", "date", "fig", "grape"]
sorted_strings = sort_by_vowel_count(strings)
print(sorted_strings)

"""
Problem 402:
Write a function where user transforms a list of integers into a list of strings. Do not use a for loop.
"""

def convert_to_integers(integers):
    return list(map(str, integers))

numbers = [4, 24, 66, 25]
print(convert_to_integers(numbers))

"""
Problem: 403
Write a Python program to add 5 to each number in a list. Do not use map().
"""

def add_five(lst):
    result = []
    
    for number in lst:
        result.append(number + 5)
    return result

lst = [1, 2, 3, 4, 5]
print(add_five(lst))

"""
Problem 404:
Write a Python function called `find_min` that takes a list of numbers as input and returns the minimum number in the list. Do not use min().
"""

def find_min(numbers):
    min_num = numbers[0]
    
    for number in numbers:
        if number < min_num:
            min_num = number
    return min_num
    
lst = [2, 6, 1, 189]
print(find_min(lst))

def main(user):
    int_lst = []
    for num in user:
        int_lst.append(int(num))
    min_num = int_lst[0]
    for num in int_lst:
        if num < min_num:
            min_num = num
    return min_num

user = input("type lst of number: ").split()
main(user)

"""
Problem: 405
Write a function that converts centimetets to inches. Type a integer as argument.
"""

def converts(cm):
    
    inch = cm * 0.39
    print(inch)

number = 5
print(converts(number))

"""
Problem: 406
Write a Python program to reverse a list use the reverse() function. Prompt the user to enter a list of elements.
"""

def reverse(lst):
    lst.reverse()
    return lst
    
lst = [1, 2, 3, 4]
print(reverse(lst))

"""
Problem 407:
Write a Python function called `calculate_average` that takes a list of numbers as input and returns the average of those numbers. Do not use sum() and len().
"""

def calculate_average(lst):
    length_num = 0
    for number in lst:
        length_num += 1
        
    add_num = 0
    for number in lst:
        add_num += number
        
    total = add_num / length_num
    return total
           
lst = [23, 56, 33]
print(calculate_average(lst))

"""
Problem 408:
Write a Python function called remove_duplicates that takes a string as input and returns a new string with duplicate characters removed, with maintaining the original order of characters.
"""

def remove_duplicates(lst):
    lst = lst.split()
    unique = []
    commom = []
    
    for word in lst:
        if word in unique:
            commom.append(word)
        else:
            unique.append(word)
    return unique
    
lst = " what is you is going is to do"
print(remove_duplicates(lst))

"""
Problem 409:
Write a program that maps a list of words into a list of integers representing the lengths of the correponding words without using len(). Use a dictionary.
"""

def len_words(lst):
    result = {}
    
    for word in lst:
        count = 0
        for char in word:
            count += 1
        result[word] = count
    return result
               
lst = ["Jonathan", "Chris", "Jeremy"]
print(len_words(lst))

"""
Problem: 410
Write a Python program to determine the len of a string in a list. Do not use filter(). For example if the len is 3 and the list is ["jon", "chris", "tom", "Jeremy"] the result should be ["jon", "tom"].
"""
def filter_string(lst):
    result = []
    for word in lst:
        if len(word) == 3: 
            result.append(word)
    return result
                    
lst = ["jon", "chris", "tom", "Jeremy"]
print(filter_string(lst))

"""
Problem: 411
Write a Python function called calculate_sum that takes two numbers as arguments. Inside this function, define a nested function that returns their sum."
"""
def calculate_sum(a, b):
    
    def inner_sum(x, y):
        return x + y
    
    return inner_sum(a, b)

result = calculate_sum(7, 3)
print(result)

"""
Problem: 412
Write a Python function called calculate_product that takes two numbers as arguments. Inside this function, define a nested function that returns their product.
"""

def calculate_product(a, b):
    def product():
        return a * b
    return product()

result = calculate_product(3, 5)
print(result)

"""
Problem: 413
Write a Python function called calculate_difference that takes two numbers as arguments. Inside this function, define a nested function that returns their difference.
"""

def calculate_difference(a, b):
    def difference():
        return a - b
    return difference()

result = calculate_difference(10, 3)
print(result)

"""
Problem: 414
Write a Python function called calculate_quotient that takes two numbers as arguments. Inside this function, define a nested function that returns their quotient.
"""

def calculate_quotient(a, b):
    def quotient():
        return a / b
    return quotient()

result = calculate_quotient(10, 2)
print(result)

"""
Problem: 415
Write a Python function area_of_rectangle that calculates the area of a rectangle given its length and width. Use a nested function to calculate the area.
"""

def area_of_rectangle(length, width):
    def area():
        return length * width
    return area()

result = area_of_rectangle(5, 4)
print(result)

"""
Problem: 416
Write a Python function perimeter_of_square that calculates the perimeter of a square given its side length. Use a nested function to calculate the perimeter.
"""

def perimeter_of_square(side_length):
    def perimeter():
        return 4 * side_length
    return perimeter()

result = perimeter_of_square(5)
print(result)

"""
Problem: 417
Write a Python function called fahrenheit_to_celsius that takes a temperature in Fahrenheit and converts it to Celsius. Use a nested function to do the conversion.
"""

def fahrenheit_to_celsius(fahrenheit):
    def convert():
        return (fahrenheit - 32) * 5 / 9
    return convert()

result = fahrenheit_to_celsius(68)
print(result)

"""
Problem: 418
Write a Python function called celsius_to_fahrenheit that takes a temperature in Celsius and converts it to Fahrenheit. Use a nested function to do the conversion.
"""

def celsius_to_fahrenheit(celsius):
    def convert():
        return (celsius * 9 / 5) + 32
    return convert()

result = celsius_to_fahrenheit(20)
print(result)

"""
Problem: 419
Write a Python function called even_or_odd that takes a number and returns whether it’s even or odd. Use a nested function to check this condition.
"""

def even_or_odd(number):
    def check():
        if number % 2 == 0:
            return "Even"
        else:
            return "Odd"
    return check()

result = even_or_odd(7)
print(result)

"""
Problem: 420
Write a Python function called is_prime that checks if a number is prime. Use a nested function to iterate and check divisibility of numbers.
"""

def is_prime(number):
    def check_divisibility(n):
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    if number < 2:
        return False
    return check_divisibility(number)

result = is_prime(29)
print(result)

"""
Problem: 421
Write a Python function called list_sum that takes a list of numbers and returns the sum. Inside it, define a nested function that adds the elements.
"""

def list_sum(numbers):
    def add_elements():
        total = 0
        for number in numbers:
            total += number
        return total
    return add_elements()

result = list_sum([1, 2, 3, 4])
print(result)

"""
Problem: 422
Write a Python function called list_product that takes a list of numbers and returns the product of all elements. Use a nested function to compute the product.
"""

def list_product(numbers):
    def multiply_elements():
        product = 1
        for number in numbers:
            product *= number
        return product
    return multiply_elements()

result = list_product([1, 2, 3, 4])
print(result)

"""
Problem: 423
Write a Python function greater_than that takes two numbers and returns True if the first is greater than the second. Use a nested function for comparison.
"""

def greater_than(a, b):
    def compare():
        return a > b
    return compare()

result = greater_than(10, 5)
print(result)

"""
Problem: 424
Write a Python function string_length that takes a string and returns its length. Use a nested function that calculates and returns the length.
"""

def string_length(s):
    def calculate_length():
        length = 0
        for char in s:
            length += 1
        return length
    return calculate_length()

result = string_length("Hello, World!")
print(result)

"""
Problem: 425
Write a Python function first_and_last that takes a string and returns its first and last characters using a nested function.
"""

def first_and_last(s):
    def get_first_last():
        if len(s) > 0:
            return s[0], s[-1]
        else:
            return None, None
    return get_first_last()

result = first_and_last("Hello")
print(result)

"""
Problem: 426
Write a Python function count_vowels that takes a string and counts the number of vowels using a nested function.
"""

def count_vowels(s):
    def is_vowel(char):
        return char.lower() in 'aeiou'

    count = 0
    for char in s:
        if is_vowel(char):
            count += 1
    return count

result = count_vowels("Hello, World!")
print(result)

"""
Problem: 427
Write a Python function reverse_string that takes a string and returns its reverse using a nested function.
"""

def reverse_string(s):
    def reverse():
        reversed_s = ""
        for char in s:
            reversed_s = char + reversed_s
        return reversed_s
    return reverse()

result = reverse_string("Hello")
print(result)

"""
Problem: 428
Write a Python function is_palindrome that takes a string and checks if it’s a palindrome using a nested function.
"""

def is_palindrome(s):
    def check():
        return s == s[::-1]
    return check()

result = is_palindrome("racecar")
print(result)

"""
Problem: 429
Write a Python function multiply_by_n that takes a number n and returns another function that multiplies a given number by n.
"""

def multiply_by_n(n):
    def multiply(x):
        return n * x
    return multiply

multiply_by_3 = multiply_by_n(3)
result = multiply_by_3(5)
print(result)

"""
Problem: 430
Write a Python function add_tax that takes a price and returns the price after applying a tax percentage using a nested function.
"""

def add_tax(price):
    def calculate_tax():
        tax_rate = 0.15
        return price + (price * tax_rate)
    return calculate_tax()

result = add_tax(100)
print(result)

"""
Problem: 431
Write a Python function greet_person that takes a name and returns a greeting using a nested function.
"""

def greet_person(name):
    def greeting():
        return f"Hello, {name}!"
    return greeting()

result = greet_person("Alice")
print(result)

"""
Problem: 432
Write a Python function factorial that calculates the factorial of a number using a nested recursive function.
"""

def factorial(n):
    def calc_factorial(num):
        if num == 0 or num == 1:
            return 1
        else:
            return num * calc_factorial(num - 1)

    return calc_factorial(n)

result = factorial(5)
print(result)

"""
Problem: 433
Write a Python function exponent that calculates the result of raising a number to a power using a nested function.
"""

def exponent(base, power):
    def calculate():
        result = 1
        for _ in range(power):
            result *= base
        return result
    return calculate()

result = exponent(2, 3)
print(result)

"""
Problem: 434
Write a Python function gcd that calculates the greatest common divisor of two numbers using a nested function.
"""

def gcd(a, b):
    def calculate_gcd(x, y):
        while y != 0:
            (x, y) = (y, x % y)
        return x
    return calculate_gcd(a, b)

result = gcd(48, 18)
print(result)

"""
Problem: 435
Write a Python function lcm that calculates the least common multiple of two numbers using a nested function.
"""

def lcm(a, b):
    def calculate_lcm(x, y):
        return abs(x * y) // gcd(x, y)

    def gcd(x, y):
        while y != 0:
            (x, y) = (y, x % y)
        return x

    return calculate_lcm(a, b)

result = lcm(4, 5)
print(result)

"""
Problem: 436
Write a Python function square_of_number that returns the square of a number using a nested function.
"""

def square_of_number(n):
    def square():
        return n * n
    return square()

result = square_of_number(5)
print(result)

"""
Problem: 437
Write a Python function cube_of_number that returns the cube of a number using a nested function.
"""

def cube_of_number(n):
    def cube():
        return n * n * n
    return cube()

result = cube_of_number(3)
print(result)

"""
Problem: 438
Write a Python function sort_list_descending that takes a list and sorts it in descending order using a nested function.
"""

def sort_list_descending(lst):
    def sort():
        sorted_list = []
        while lst:
            maximum = lst[0]
            for item in lst:
                if item > maximum:
                    maximum = item
            sorted_list.append(maximum)
            lst.remove(maximum)
        return sorted_list
    return sort()

result = sort_list_descending([4, 1, 3, 2])
print(result)

"""
Problem: 439
Write a Python function max_of_three that takes three numbers and returns the maximum using a nested function.
"""

def max_of_three(a, b, c):
    def find_max():
        max_value = a
        if b > max_value:
            max_value = b
        if c > max_value:
            max_value = c
        return max_value
    return find_max()

result = max_of_three(10, 20, 15)
print(result)

"""
Problem: 440
Write a Python function average_of_list that calculates the average of a list of numbers using a nested function. Do not use sum() and len()
"""

def average_of_list(lst):
    def calculate_average():
        total = 0
        count = 0
        for number in lst:
            total += number
            count += 1
        return total / count if count != 0 else 0
    return calculate_average()

result = average_of_list([10, 20, 30, 40])
print(result)

"""
Problem: 441
Write a Python function average_of_list that calculates the average of a list of numbers using a nested function.
"""

def average_of_list(lst):
    def calculate_average():
        total = 0
        count = 0
        for number in lst:
            total += number
            count += 1
        return total / count if count != 0 else 0
    return calculate_average()

result = average_of_list([5, 15, 25])
print(result)

"""
Problem: 442
Write a Python function is_uppercase that checks if all characters in a string are uppercase using a nested function.
"""

def is_uppercase(s):
    def check():
        for char in s:
            if not char.isupper():
                return False
        return True
    return check()

result = is_uppercase("HELLO")
print(result)

"""
Problem: 443
Write a Python function is_lowercase that checks if all characters in a string are lowercase using a nested function.
"""

def is_lowercase(s):
    def check():
        for char in s:
            if not char.islower():
                return False
        return True
    return check()

result = is_lowercase("hello")
print(result)

"""
Problem: 444
Write a Python function string_contains_digit that checks if a string contains a digit using a nested function.
"""

def string_contains_digit(string):
    
    def contains_digit(x):
        for char in x:
            if char.isdigit():
                return True
        return False
        
    return contains_digit(string)
        
string = "jonathan5"
print(string_contains_digit(string))

"""
Problem: 445
Write a Python function string_contains_letter that checks if a string contains a letter using a nested function.
"""

def string_contains_letter(string):
    
    def contains_letter(x):
        for char in x:
            if char.isalpha():
                return True
        return False
        
    return contains_letter(string)
        
string = "123455g"
print(string_contains_letter(string))

"""
Problem: 446
Write a Python function calculate_average that takes three numbers and returns their average using a nested function.
"""

def average_of_list(lst):
    
    def average(x):
        for number in x:
            count_len = len(x)
            add_num = sum(x)
            total = add_num / count_len
            
        return total
        
    return average(lst)

lst = [34, 67, 667]
print(average_of_list(lst))

"""
Problem: 447
Write a Python function check_multiple_of_n that takes two numbers and checks if the first is a multiple of the second using a nested function.
"""

def check_multiple_of_n(num1, num2):
    
    def is_multiple(x, y):
        return x % y == 0 
    
    return is_multiple(num1, num2)

print(check_multiple_of_n(10, 2))
print(check_multiple_of_n(10, 3)) 

"""
Problem: 448
Write a Python function longest_string that takes a list of strings and returns the longest one using a nested function.
"""

def longest_string(lst):
    
    def longest(x):
        longest_word = x[0]
        for word in x:
            if word > longest_word:
                longest_word = word
        return longest_word
            
    return longest(lst)
                    
lst = ["jon", "zonathan", "mimi"]
print(longest_string(lst))

def longest_string(lst):

    def find_longest(strings):
        return max(strings, key=len)
    
    return find_longest(lst)
    
lst = ["jon", "zonathan", "mimi"]
print(longest_string(lst))

"""
Problem: 449
Write a Python function shortest_string that takes a list of strings and returns the shortest one using a nested function.
"""

def shortest_string(lst):
    
    def shortest(x):
        return min(x, key=len)
        
    return shortest(lst)
        
lst = ["chris", "tit", "mountain"]
print(shortest_string(lst))

"""
Problem: 450
Write a Python function remove_duplicates that takes a list and removes duplicates using a nested function.
"""

def remove_duplicates(lst):
    
    def duplicates_removed(x):
        unique = set()
        
        for word in x:
            unique.add(word)
        return unique
        
    return duplicates_removed(lst)

lst = ["not", "not", "today", "today"]
print(remove_duplicates(lst))

"""
Problem: 451
Write a Python function fibonacci that generates the nth Fibonacci number using a nested recursive function.
"""

def fibonacci(n):

    def fib_recursive(n):
        if n <= 1:
            return n
        else:
            return fib_recursive(n - 1) + fib_recursive(n - 2)
    
    return fib_recursive(n)

n = 10 
print(fibonacci(n))

"""
Problem: 452
Write a Python function called calculate_sum that takes two numbers as arguments. Inside this function, define a nested function that returns their sum and another function that returns the multiplication."
"""
def calculate_sum(a, b):
    
    def inner_sum(x, y):
        return x + y
    
    def inner_mult(x, y):
        return x * y
    
    return inner_sum(a, b), inner_mult(a, b)

print(calculate_sum(7, 3))

"""
Problem: 453
Write a Python function called calculate_integers that takes two numbers as arguments. Inside this function, define nested functions that returns their product, sum and division.
"""

def calculate_integers(a, b):
    
    def product(x, y):
        return x * y
        
    def sum_int(x, y):
        return x + y
        
    def division(x, y):
        return x / y
        
    return product(a, b), sum_int(a, b), division(a, b)
    
print(calculate_integers(10, 5))

"""
Problem: 455
Write a Python function average_of_list that calculates the average of a list of numbers using a nested function. Use len() and sum().
"""

def average_of_list(lst):
    
    def average(x):
        for number in x:
            count_len = len(x)
            add_num = sum(x)
            total = add_num / count_len
            
        return total
        
    return average(lst)

lst = [34, 67, 667]
print(average_of_list(lst))

"""
Problem: 456
Write a Python function that sorts a list of strings by their length using the key parameter.
"""

def len_lst(lst):
    sort = sorted(lst, key=len)
    
    return sort
    
lst = ["Jonathan", "chris", "Jeremy"]
print(len_lst(lst))

"""
Problem: 457
Write a Python function to find the minimum string by its length using the min() function with the key parameter.
"""

def min_len(lst):
    min_string = min(lst, key=len)
    
    return min_string
    
lst = ["truck", "is", "Bethany"]
print(min_len(lst))

"""
Problem: 458
Write a Python function to find the maximum string alphabetically using the key parameter.
"""
def max_string_alpha(lst):
    
    def max_string(x):
        return len(x)
        
    return max(lst, key=max_string)

lst = ["hippopotamus", "giraffe", "monkey"]
print(max_string_alpha(lst))

"""
Problem: 459
Write a Python function to sort a list of dictionaries by the value associated with a specific key using the key parameter.
"""

from operator import itemgetter

def sort_dicts_by_key(dict_list, sort_key):
    return sorted(dict_list, key=itemgetter(sort_key))

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
"""

def sort_by_absolute_value(lst):
    return sorted(lst, key=abs)

lst = [3, -1, -4, 2, 0]
sorted_lst = sort_by_absolute_value(lst)
print(sorted_lst)

"""
Problem: 461
Write a Python function that sorts a list of words by the number of vowels they contain using the key parameter.
"""

def sort_words_by_vowel_count(lst):
    
    def count_vowels(word):
        vowels = 'aeiou'
        count = 0
        for char in word:
            if char in vowels:
                count += 1
        return count
    
    return sorted(lst, key=count_vowels)

lst = ["apple", "banana", "cherry", "date"]
print(sort_words_by_vowel_count(lst))

"""
Problem: 462
Write a Python function to find the longest word in a list using the max() function with the key parameter.
"""

def longest_word(lst):
    longest_w = max(lst, key=len)
    
    return longest_w
    
lst = ["cheater", "lepard", "lion"]
print(longest_word(lst))
    
"""
Problem: 463
Write a Python function to sort a list of tuples by the sum of the elements in each tuple using the key parameter.
"""

def sum_of_tuple(lst):
    
    return sorted(lst, key=sum)
    
lst = [(9, 9, 9), (5, 5, 5), (8, 8, 8)]
print(sum_of_tuple(lst))

"""
Problem: 464
Write a Python function to sort a list of strings by the last character of each string using the key parameter.
"""

def list_of_strings_lst(lst):
    
    def last_char(s):
        return s[-1]
    
    return sorted(lst, key=last_char)

lst = ["car", "side", "beach"]
print(list_of_strings_lst(lst))

"""
Problem: 465
Write a Python function to sort a list of strings by the number of uppercase letters in each string using the key parameter.
"""

def sort_number_uppercases(lst):
    
    def uppercase_count(x):
        count = 0
        for char in x:
            if char.isupper():
                count += 1
        return count
                
    return sorted(lst,
    key=uppercase_count)

lst = ["SNSKEYHG", "SlIppery", "SNAKEGG"]
print(sort_number_uppercases(lst))

"""
Problem: 466
Write a Python function to find the tuple with the largest product of its elements using the key parameter.
"""

def tuple_largest_product(lst):
    
    def product(x):
        count = 1
        for number in x:
            count *= number
        return count
    
    return max(lst, key=product)

lst = [(2, 2, 2), (4, 4, 4)]
print(tuple_largest_product(lst))

"""
Problem: 467
Write a Python function to sort a list of floating-point numbers by their rounded value using the key parameter.
"""

def floating_point(numbers):
    return sorted(numbers, key=round)
    
numbers = [3.7, 3.3, 2.7, 1.2, 35.4, 677.9]
print(floating_point(numbers))

"""
Problem: 468
Write a Python function to sort a list of tuples based on the first element in descending order using the key parameter.
"""

def first_element_decending_order(lst):
    def first_element(x):
        return x[0] 
    
    return sorted(lst, key=first_element, reverse=True)

lst = [("see", "sea", "saw"), ("zoat", "zite", "zank")]
print(first_element_decending_order(lst))

"""
Problem: 469
Write a Python function that sorts a list of words by the number of consonants using the key parameter.
"""

def number_of_consonants(lst):
    
    def consonants(word):
    
        consonants_set = "bcdfghjklmnpqrstvwxyz"
        
        count = 0

        for char in word.lower():
            if char in consonants_set:
                count += 1
        return count

    return sorted(lst, key=consonants)
    
lst = ["zzzzzzzzz", "yyyyyy", "bbb"]
print(number_of_consonants(lst))

"""
Problem: 470
Write a Python function to find the shortest string in a list using the min() function with the key parameter.
"""

def min_string(lst):
    return min(lst, key=len)
    
lst = ["down", "up"]
print(min_string(lst))

"""
Problem: 471
Write a Python function to sort a list of dictionaries by the length of the value associated with a specific key using the key parameter.
"""

def length_of_value(lst, key):
    
    def length_function(x):
        return len(x.get(key, ""))
        
    return sorted(lst, key=length_function)

lst = [{"a": "tree", "b": "bushen"}, {"a": "tin", "b": "bash"}, {"a": "tumb", "b": "bat"}]
sorted_lst = length_of_value(lst, "b")
print(sorted_lst)

"""
Problem: 472
Write a Python function to find the person with the longest name in a list of dictionaries containing ‘name’ as a key using the max() function with the key parameter.
"""

def find_person(lst_dict, key):

    def longest_name(d):
        return len(d.get(key, ""))

    return max(lst_dict, key=longest_name)

lst_dict = [{"name": "Beth"}, {"name": "Brett"}, {"name": "Jhonivan"}, {"name": "Jonathan"}]
key = "name"

print(find_person(lst_dict, key))

"""
Problem: 473
Write a Python function that sorts a list of integers by their remainder when divided by a given number using the key parameter.
"""

def main(lst, divisor):
    
    def inner(num):
        return num % divisor
    return sorted(lst, key=inner)

lst = [677, 34, 9, 2, 67]
divisor = 5
main(lst, divisor)

def remainder_key(x, divisor):
    return x % divisor

def sort_by_remainder(lst, divisor):

    def key_func(x):
        return remainder_key(x, divisor)
    
    return sorted(lst, key=key_func)

lst = [10, 23, 4, 7, 15]
divisor = 5
print(sort_by_remainder(lst, divisor))

"""
Problem: 474
Write a Python function to sort a list of dates by the year using the key parameter.
"""

from datetime import datetime

def year_key(date):
    return date.year

def sort_by_year(dates):

    date_objects = []
    
    for date in dates:
        date_objects.append(datetime.strptime(date, "%d.%m.%Y"))
    
    sorted_dates = sorted(date_objects, key=year_key)

    sorted_date_strings = []
    for date in sorted_dates:
        sorted_date_strings.append(date.strftime("%d.%m.%Y"))
    
    return sorted_date_strings

dates = ["01.02.1908", "12.11.1955", "23.04.1989", "07.07.1967"]
sorted_dates = sort_by_year(dates)
print(sorted_dates)

"""
Problem: 475
Write a Python function to sort a list of names by the number of times the letter ‘a’ appears in each name using the key parameter.
"""

def sort_by_a_count(names):
    
    def count_a(name):
        
        return name.lower().count('a')
    
    return sorted(names, key=count_a)

names = ["Anna", "Alice", "Bob", "Amanda", "Ava"]
sorted_names = sort_by_a_count(names)
print(sorted_names)

"""
Problem: 476
Write a Python function to sort a list of numbers by their square using the key parameter.
"""

def sort_sqaure(lst):
    
    def sqaured(x):
        return x * x
        
    return sorted(lst, key=sqaured)
        
    
lst = [9, 5, 4, 1 ]
print(sort_sqaure(lst))

"""
Problem: 477
Write a Python function to find the list element closest to a target value using the key parameter.
"""

def closest_to_target(lst, target):

    def difference_from_target(x):
        return abs(x - target)
    
    return min(lst, key=difference_from_target)

lst = [10, 22, 14, 3, 8]
target = 7
closest_value = closest_to_target(lst, target)
print(closest_value)

"""
Problem: 478
Write a Python function that sorts a list of tuples based on the length of the first element in each tuple using the key parameter.
"""

def length_of_first_element(lst):
    
    def length_of_first(x):
        return len(x[0])
        
    return sorted(lst, key=length_of_first)

lst = [("initiate", "love", "seat"), ("sweet", "beat", "hell")]
sorted_list = length_of_first_element(lst)
print(sorted_list)

"""
Problem: 479
Write a Python function to sort a list of strings by the number of spaces they contain using the key parameter.
"""

def number_of_spaces(lst):
    
    def spaces_count(x):
        return x.count(" ")
        
    return sorted(lst, key=spaces_count)
    
lst = ["what is happening", "why all the hate in your brain", "stop it"]
print(number_of_spaces(lst))

"""
Problem: 480
Write a Python function that finds the word with the most vowels in a list using the max() function with the key parameter.
"""

def most_vowels(lst):
    
    def count_vowels(word):
        vowels = "aeiou"
        
        count = 0
        for char in word:
            if char in vowels:
                count += 1
        return count
            
    return max(lst, key=count_vowels)
    
lst = ["aamost", "Aaron", "bible", "buttom", "aeiouthian"]
print(most_vowels(lst))

"""
Problem: 481
Write a Python function to sort a list of integers by the number of digits they contain using the key parameter.
"""

def sort_lst_integers(lst):
    
    def count_digits(n):
        return len(str(abs(n)))
    return sorted(lst, key=count_digits)
        
lst = [456, 56, 8, 788, 89, 1]
print(sort_lst_integers(lst))

"""
Problem: 482
Write a Python function that sorts a list of tuples by the difference between their elements using the key parameter.
"""

def sort_tuples_by_difference(lst):

    def difference(tup):
        return abs(tup[0] - tup[1]) 
    
    return sorted(lst, key=difference)

lst = [(3, 8), (1, 7), (5, 5), (9, 2), (6, 10)]

print(sort_tuples_by_difference(lst))

"""
Problem: 483
Write a Python function to sort a list of strings by the ASCII value of their first character using the key parameter.
"""

def sort_strings_by_ascii(lst):
    
    def ascii_value(s):
        return ord(s[0])
        
    return sorted(lst, key=ascii_value)

lst = ["banana", "apple", "cherry", "date", "elderberry"]
print(sort_strings_by_ascii(lst))

"""
Problem: 484
Write a Python function to sort a list of lists by the sum of the elements in each sublist using the key parameter.
"""

def sort_lists_by_sum(lst):

    def sum_of_elements(sublist):
        return sum(sublist)
        
    return sorted(lst, key=sum_of_elements)

lst = [[3, 4], [1, 2, 3], [10], [5, 1, 1]]

print(sort_lists_by_sum(lst))

"""
Problem: 485
Write a Python function to find the word with the fewest consonants in a list using the min() function with the key parameter.
"""

def number_of_consonants(lst):
    
    def consonants(word):
    
        consonants_set = "bcdfghjklmnpqrstvwxyz"
        
        count = 0

        for char in word.lower():
            if char in consonants_set:
                count += 1
        return count

    return min(lst, key=consonants)
    
lst = ["zzzzzzzzz", "yyyyyy", "bbb"]
print(number_of_consonants(lst))

"""
Problem: 486
Write a Python function that sorts a list of file names by their file extension using the key parameter.
"""

def sort_files_by_extension(lst):
    
    def file_extension(filename):
        return filename.split('.')[-1]
        
    return sorted(lst, key=file_extension)

lst = ["document.txt", "photo.jpeg", "music.mp3", "video.mp4", "archive.zip"]

print(sort_files_by_extension(lst))

"""
Problem: 487
Write a Python function to sort a list of numbers by the square root of each number using the key parameter.
"""

def sqaure_numbers_lst(lst):
    
    def sqaure(n):
        return n * n
        
    return sorted(lst, key=sqaure)
    
lst = [12, 46, 2, 10]
print(sqaure_numbers_lst(lst))

"""
Problem: 488
Write a Python function to sort a list of words by the number of distinct letters in each word using the key parameter.
"""

def sort_words_by_distinct_letters(words):

    def distinct_letter_count(word):
        return len(set(word))
        
    return sorted(words, key=distinct_letter_count)

words = ["apple", "banana", "cherry", "orange"]
print(sort_words_by_distinct_letters(words))

"""
Problem: 489
Write a Python function that sorts a list of strings by the second letter in each string using the key parameter.
"""

def sort_second_letter(lst):
    
    def second_letter(x):
        return x[1]
        
    return sorted(lst, key=second_letter)
    
lst = ["mountain", "law", "lebany"]
print(sort_second_letter(lst))

"""
Problem: 490
Write a Python function to sort a list of people by their age stored in a dictionary using the key parameter.
"""

def people_age(dic):
    
    def sort_age(person):
        return dic[person]
        
    return sorted(dic, key=sort_age)
    
dic = {"Sam": 27, "Tom": 56, "Chantelle": 18}
print(people_age(dic))

"""
Problem: 491
Write a Python function that sorts a list of numbers by their binary representation using the key parameter.
"""

def sort_by_binary_representation(lst):
    
    def binary_representation(x):
        return bin(x)
        
    return sorted(lst, key=binary_representation)

lst = [5, 3, 8, 1, 12]

print(sort_by_binary_representation(lst))

"""
Problem: 492
Write a Python function to find the person with the shortest name in a list of dictionaries using the min() function with the key parameter.
"""

def sort_keys_by_value(dic):

    def get_value(key):
        return dic[key]
        
    return sorted(dic.keys(), key=get_value)
   
dic = {"Sam": 27, "Tommy": 56, "Chantelle": 18}
print(sort_keys_by_value(dic))

"""
Problem: 493
Write a Python function to sort a list of fractions by their decimal value using the key parameter.
"""

from fractions import Fraction

def sort_fractions_by_decimal(fractions):

    def decimal_value(fraction):
        return float(fraction)
        
    return sorted(fractions, key=decimal_value)

fractions = [Fraction(1, 3), Fraction(3, 4), Fraction(2, 5), Fraction(7, 10)]

print(sort_fractions_by_decimal(fractions))

"""
Problem: 494
Write a Python function to find the longest string that ends with a specific letter using the max() function with the key parameter.
"""

def longest_string_letter(lst, letter):
    
    def longest_letter(s):
        return len(s) if s.endswith(letter) else -1
    
    return max(lst, key=longest_letter)

lst = ["Jonathan", "Nathan", "Sarah", "Martha"]

print(longest_string_letter(lst, 'n'))
print(longest_string_letter(lst, 'a'))

def longest_string(string, letter):
    
    words = string.split()

    def letter_ends(word):
        if word.endswith(letter):
            return len(word)
        else:
            return 0
    
    longest = None  
    max_length = 0 

    for word in words:
        length = letter_ends(word)
        if length > max_length:
            max_length = length
            longest = word
    
    return longest

input_string = "Jonathan nathan Natas"
letter = "a"
print(longest_string(input_string, letter))

"""
Problem: 495
Create a base class Animal with a method speak() and a derived class Dog that overrides the speak() method to print “Bark”.
"""

class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return "Bark"
        
class Cat(Animal):
    def speak(self):
        return "Meow"
        
dog = Dog()
cat = Cat()
print(dog.speak())
print(cat.speak())

"""
Problem: 496
Create a base class Vehicle with attributes speed and color. Create a derived class Car that adds the model attribute.
"""

class Vehicle:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

class Car(Vehicle):
    def __init__(self, speed, color, model):

        super().__init__(speed, color)
        
        self.model = model

my_car = Car(120, "Red", "Toyota")
print(f"Car Model: {my_car.model}, Speed: {my_car.speed}, Color: {my_car.color}")

"""
Problem: 497
Create a base class Person with a method introduce(). Create a derived class Student that overrides the introduce() method to include the student’s grade.
"""
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Hello, my name is {self.name}."

class Student(Person):
    def __init__(self, name, grade):
    
        super().__init__(name)
    
        self.grade = grade
        
    def introduce(self):
        return f"Hello, my name is {self.name} and I am in grade {self.grade}."

person = Person("Alice")
print(person.introduce()) 

student = Student("Bob", 10)
print(student.introduce()) 

"""
Problem: 498
Create a base class Shape with a method area(). Create a derived class Rectangle that calculates the area.
"""

class Shape:
    def area(self):

        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rectangle = Rectangle(5, 3)
print(f"Area of the rectangle: {rectangle.area()}") 

"""
Problem: 499
Create a base class Appliance with attributes brand and power. Create a derived class WashingMachine that adds a method wash_clothes().
"""

class Appliance:
    def __init__(self, brand, power):
        self.brand = brand
        self.power = power

class WashingMachine(Appliance):
    def __init__(self, brand, power):
        super().__init__(brand, power)

    def wash_clothes(self):
        return f"The {self.brand} washing machine is washing clothes with {self.power} watts of power."

washing_machine = WashingMachine("LG", 1500)
print(washing_machine.wash_clothes())

"""
Problem: 500
Create a base class Employee with attributes name and salary. Create a derived class Manager that adds a method assign_task().
"""

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary):
    
        super().__init__(name, salary)

    def assign_task(self, task):
        return f"Manager {self.name} has assigned the task: {task}."

manager = Manager("John Doe", 75000)
print(manager.assign_task("Prepare a project report"))

