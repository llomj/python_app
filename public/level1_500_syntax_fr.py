# Syntax documentation
#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: +
# Fonctions intégrées : sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → import operator
#   → return operator.add(a, b)
#   → result = a + b
#   → return result
#   → import operator
#   → return operator.add(a, b)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — add_num, add_number are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(add_number(...))  # add_number() runs first → value goes to print()
#   → print(add_num(...))  # add_num() runs first → value goes to print()
#   → a = ...  # stored in memory
#   → b = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(add_number(...))  # add_number() runs first → value goes to print()
"""
Problème 1 :
Écrivez une fonction Python appelée `add_numbers` qui prend deux nombres comme paramètres et retourne leur somme.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: * >=
# Fonctions intégrées : abs, pow, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return pow(a, b)
#   → return pow(a, b)
#   → return pow(a, b)
#   → return pow(a, b)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only multiply_numbers is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(multiply_numbers(...))  # multiply_numbers() runs first → value goes to print()
#   → print(multiply_numbers(...))  # multiply_numbers() runs first → value goes to print()
#   → print(multiply_numbers(...))  # multiply_numbers() runs first → value goes to print()
#   → a = ...  # stored in memory
#   → b = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(multiply_numbers(...))  # multiply_numbers() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
"""
Problème 2 :
Écrivez une fonction Python appelée `multiply_numbers` qui prend deux nombres comme paramètres et retourne leur produit.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: >
# Fonctions intégrées : max, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → result = number[0]
#   → for item in number:
#   →     if item > result:
#   →         result = item
#   → return result
#   → result = number[0]
#   → for item in number:
#   →     if item > result:
#   →         result = item
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only find_max is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(find_max(...))  # find_max() runs first → value goes to print()
#   → numbers_list = ...  # stored in memory
#   → print('The maximum number in the list is:', find_max(...))
#   → number = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(find_max(...))  # find_max() runs first → value goes to print()
#
# Loop: takes one item from numbers, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 3 :
Écrivez une fonction Python appelée `find_max` qui prend une liste de nombres en entrée et retourne le maximum nombre dans la liste.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: /
# Fonctions intégrées : len, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → total = 0
#   → count = 0
#   → for item in number:
#   →     total += item
#   →     count += 1
#   → return total / count if count else 0
#   → result = sum(number) / len(number)
#   → return result
#   → total = 0
#   → count = 0
#   → for item in number:
#   →     total += item
#   →     count += 1
#   → return total / count if count else 0
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — cal_average, calculate_average are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(calculate_average(...))  # calculate_average() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → print(cal_average(...))  # cal_average() runs first → value goes to print()
#   → number = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(calculate_average(...))  # calculate_average() runs first → value goes to print()
#
# Loop: takes one item from number, runs body, repeats until done
"""
Problème 4 :
Écrivez une fonction Python appelée `calculate_average` qui prend une liste de nombres en entrée et retourne le moyenne de ces nombres. Utilisez sum() et len().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: in
# Fonctions intégrées : len, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return len([char for char in string if char in 'aeiou'])
#   → return len([char for char in string if char in 'aeiou'])
#   → return len([char for char in string if char in 'aeiou'])
#   → return len([char for char in string if char in 'aeiou'])
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_vowels is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(count_vowels(...))  # count_vowels() runs first → value goes to print()
#   → print(count_vowels(...))  # count_vowels() runs first → value goes to print()
#   → print(count_vowels(...))  # count_vowels() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_vowels(...))  # count_vowels() runs first → value goes to print()
#
# Loop: takes one item from string, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 5 :
Écrivez une fonction Python appelée `count_vowels` qui prend une chaîne en entrée et retourne le nombre de voyelles (a, e, i, o, u) dans la chaîne. Ignorez la casse.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: +
# Fonctions intégrées : reversed()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → result = ''
#   → for char in string:
#   →     result = char + result
#   → return result
#   → result = ''
#   → for char in string:
#   →     result = char + result
#   → return result
#   → result = ''
#   → for char in string:
#   →     result = char + result
#   → return result
#   → result = ''
#   → for char in string:
#   →     result = char + result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only reverse_string is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(reverse_string(...))  # reverse_string() runs first → value goes to print()
#   → print(reverse_string(...))  # reverse_string() runs first → value goes to print()
#   → print(reverse_string(...))  # reverse_string() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(reverse_string(...))  # reverse_string() runs first → value goes to print()
#
# Loop: takes one item from string, runs body, repeats until done
"""
Problème 6 :
Écrivez une fonction Python appelée `reverse_string` qui prend une chaîne en entrée et retourne le reverse de cette chaîne.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: % & * // ==
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return number % 2 == 0
#   → return number % 2 == 0
#   → return number % 2 == 0
#   → return number % 2 == 0
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only is_even is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(is_even(...))  # is_even() runs first → value goes to print()
#   → print(is_even(...))  # is_even() runs first → value goes to print()
#   → print(is_even(...))  # is_even() runs first → value goes to print()
#   → number = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_even(...))  # is_even() runs first → value goes to print()
"""
Problème 7 :
Écrivez une fonction Python appelée `is_even` qui prend un entier en entrée et retourne vrai si le nombre est pair, et False sinon.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: **
# Fonctions intégrées : pow()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → import math
#   → return math.pow(number, 2)
#   → square = number ** 2
#   → return square
#   → import math
#   → return math.pow(number, 2)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — cal_square, calculate_square are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(cal_square(...))  # cal_square() runs first → value goes to print()
#   → print(calculate_square(...))  # calculate_square() runs first → value goes to print()
#   → number = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(cal_square(...))  # cal_square() runs first → value goes to print()
"""
Problème 8 :
Écrivez une fonction Python appelée `calculate_square` qui prend un nombre en entrée et retourne le carré de cette nombre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: % +
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return 'hello %s' % string
#   → return 'hello %s' % string
#   → return 'hello %s' % string
#   → return 'hello %s' % string
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only greet_user is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(greet_user(...))  # greet_user() runs first → value goes to print()
#   → print(greet_user(...))  # greet_user() runs first → value goes to print()
#   → print(greet_user(...))  # greet_user() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(greet_user(...))  # greet_user() runs first → value goes to print()
"""
Problème 9 :
Écrivez une fonction Python appelée `greet_user` qui prend une chaîne `name` en entrée et affiche un message de salutation message dans le format "Hello, [nom]!".
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: **
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(lambda number: number ** 2, numbers))
#   → return list(map(lambda number: number ** 2, numbers))
#   → return list(map(lambda number: number ** 2, numbers))
#   → return list(map(lambda number: number ** 2, numbers))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only square_lst is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(square_lst(...))  # square_lst() runs first → value goes to print()
#   → print(square_lst(...))  # square_lst() runs first → value goes to print()
#   → print(square_lst(...))  # square_lst() runs first → value goes to print()
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(square_lst(...))  # square_lst() runs first → value goes to print()
#
# Loop: takes one item from numbers, runs body, repeats until done
"""
Problème 10 :
Écrivez une fonction Python appelée `square_list` qui prend une liste de nombres en entrée et retourne une nouvelle liste avec chaque nombre au carré.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: - <=
# Fonctions intégrées : chr, ord, str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return str(string).upper()
#   → return str(string).upper()
#   → return str(string).upper()
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only covert_uppercase is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(covert_uppercase(...))  # covert_uppercase() runs first → value goes to print()
#   → print(covert_uppercase(...))  # covert_uppercase() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(covert_uppercase(...))  # covert_uppercase() runs first → value goes to print()
#
# Loop: takes one item from string, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 11 :
Écrivez une fonction Python appelée `convert_to_uppercase` qui prend une chaîne en entrée et retourne la chaîne avec tous ses caractères converted à uppercase.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : reduce, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → from functools import reduce
#   → import operator
#   → return reduce(operator.add, number, 0)
#   → count = 0
#   → for number in numbers:
#   →     count += number
#   → return count
#   → from functools import reduce
#   → import operator
#   → return reduce(operator.add, number, 0)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — cal_sum, calculate_sum are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(calculate_sum(...))  # calculate_sum() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → print(cal_sum(...))  # cal_sum() runs first → value goes to print()
#   → number = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(calculate_sum(...))  # calculate_sum() runs first → value goes to print()
#
# Loop: takes one item from numbers, runs body, repeats until done
"""
Problème 12 :
Écrivez une fonction Python appelée `calculate_sum` qui prend une liste de nombres en entrée et retourne le somme de tous le nombres dans la liste.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: % & != ==
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return number % 2 != 0
#   → return number % 2 != 0
#   → return number % 2 != 0
#   → return number % 2 != 0
#   → return number % 2 != 0
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only is_odd is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(is_odd(...))  # is_odd() runs first → value goes to print()
#   → print(is_odd(...))  # is_odd() runs first → value goes to print()
#   → print(is_odd(...))  # is_odd() runs first → value goes to print()
#   → print(is_odd(...))  # is_odd() runs first → value goes to print()
#   → number = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_odd(...))  # is_odd() runs first → value goes to print()
"""
Problème 13 :
Écrivez une fonction Python appelée `is_odd` qui prend un entier en entrée et retourne vrai si le nombre est impair, et False sinon.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: % +
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return '%s%s' % (string1, string2)
#   → return string1 + string2
#   → return '%s%s' % (string1, string2)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — concatenate_string, concatenate_strings are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → print(concatenate_strings(...))  # concatenate_strings() runs first → value goes to print()
#   → print(concatenate_string(...))  # concatenate_string() runs first → value goes to print()
#   → string1 = ...  # stored in memory
#   → string2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(concatenate_strings(...))  # concatenate_strings() runs first → value goes to print()
"""
Problème 14 :
Écrivez une fonction Python appelée `concatenate_strings` qui prend deux strings en entrée et retourne une nouvelle chaîne qui est le concatenation de le deux entrée strings.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : len, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sum((1 for _ in string))
#   → count = 0
#   → for char in string:
#   →     count += 1
#   → return count
#   → return sum((1 for _ in string))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — find_len, find_length are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(find_length(...))  # find_length() runs first → value goes to print()
#   → print(find_len(...))  # find_len() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(find_length(...))  # find_length() runs first → value goes to print()
#
# Loop: takes one item from string, runs body, repeats until done
"""
Problème 15 :
Écrivez une fonction Python appelée `find_length` qui prend une chaîne en entrée et retourne la longueur de cette chaîne.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: + != // ==
# Fonctions intégrées : len, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return string == string[::-1]
#   → return string == string[::-1]
#   → return string == string[::-1]
#   → return string == string[::-1]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only is_palindrome is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(is_palindrome(...))  # is_palindrome() runs first → value goes to print()
#   → print(is_palindrome(...))  # is_palindrome() runs first → value goes to print()
#   → print(is_palindrome(...))  # is_palindrome() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_palindrome(...))  # is_palindrome() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 16 :
Écrivez une fonction Python appelée `is_palindrome` qui prend une chaîne en entrée et retourne vrai si la chaîne est un palindrome (lit le même forwards et backwards), et False sinon.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : len()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return word_count
#   → return word_count
#   → return word_count
#   → return word_count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_words is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → example_string = ...  # stored in memory
#   → print(count_words(...))  # count_words() runs first → value goes to print()
#   → example_string = ...  # stored in memory
#   → print(count_words(...))  # count_words() runs first → value goes to print()
#   → arg = ...  # stored in memory
#   → print(count_words(...))  # count_words() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_words(...))  # count_words() runs first → value goes to print()
#
# Loop: takes one item from words, runs body, repeats until done
"""
Problème 17 :
Écrivez une fonction Python appelée `count_words` qui prend une chaîne en entrée et retourne le nombre de mots dans la chaîne. Supposons que words sont séparés by spaces.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: <
# Fonctions intégrées : input, int, min, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → user = input('type number: ').split()
#   → int_number = []
#   → for number in user:
#   →     int_number.append(int(number))
#   → min_num = sorted(int_number)[0]
#   → for number in int_number:
#   →     if min_num < 0:
#   →         min_num = number
#   → result = min_num
#   → return result
#   → user = input('type number: ').split()
#   → int_number = []
#   → for number in user:
#   →     int_number.append(int(number))
#   → min_num = sorted(int_number)[0]
#   → for number in int_number:
#   →     if min_num < 0:
#   →         min_num = number
#   → result = min_num
#   → return result
#   → min_number = numbers[0]
#   → for number in numbers:
#   →     if number < min_number:
#   →         min_number = number
#   → return min_number
#   → user = input('type number: ').split()
#   → int_number = []
#   → for number in user:
#   →     int_number.append(int(number))
#   → min_num = sorted(int_number)[0]
#   → for number in int_number:
#   →     if min_num < 0:
#   →         min_num = number
#   → result = min_num
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — find_min, find_minimum are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → find_min()  # jumps into find_min(), runs body, returns
#   → lst = ...  # stored in memory
#   → print(find_min(...))  # find_min() runs first → value goes to print()
#   → min_number = ...  # stored in memory
#   → print(find_minimum(...))  # find_minimum() runs first → value goes to print()
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(find_min(...))  # find_min() runs first → value goes to print()
#
# Loop: takes one item from user, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 18 :
Écrivez une fonction Python appelée `find_min` qui prend une liste de nombres comme argument d'entrée et retourne le minimum nombre dans la liste.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: % ==
# Fonctions intégrées : len, range, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return even_index_sum % 2 == 0
#   → return even_index_sum % 2 == 0
#   → return even_index_sum % 2 == 0
#   → return even_index_sum % 2 == 0
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only is_even_index_sum is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(is_even_index_sum(...))  # is_even_index_sum() runs first → value goes to print()
#   → print(is_even_index_sum(...))  # is_even_index_sum() runs first → value goes to print()
#   → print(is_even_index_sum(...))  # is_even_index_sum() runs first → value goes to print()
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_even_index_sum(...))  # is_even_index_sum() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 19 :
Écrivez une fonction Python appelée `is_even_index_sum` qui prend une liste de nombres en entrée et retourne vrai si le somme de le nombres at même les indices est pair, et False sinon. Supposons que le premier index est considéré comme index 0.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: *
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(lambda element: element, elements))
#   → return list(map(lambda element: element, elements))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only double_elements is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(double_elements(...))  # double_elements() runs first → value goes to print()
#   → numbers_list = ...  # stored in memory
#   → print('The list with doubled elements is:', double_elements(...))
#   → elements = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(double_elements(...))  # double_elements() runs first → value goes to print()
#
# Loop: takes one item from elements, runs body, repeats until done
"""
Problème 20 :
Écrivez une fonction Python appelée `double_elements` qui prend une liste de nombres en entrée et retourne une nouvelle liste où chaque élément est doubled.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: > <= and
# Fonctions intégrées : all, len, min()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return False
#   → return False
#   → return False
#   → return False
#   → return False
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only is_all_positive is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(is_all_positive(...))  # is_all_positive() runs first → value goes to print()
#   → print(is_all_positive(...))  # is_all_positive() runs first → value goes to print()
#   → print(is_all_positive(...))  # is_all_positive() runs first → value goes to print()
#   → print(is_all_positive(...))  # is_all_positive() runs first → value goes to print()
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_all_positive(...))  # is_all_positive() runs first → value goes to print()
#
# Loop: takes one item from numbers, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 21 :
Écrivez une fonction Python appelée `is_all_positive` qui prend une liste de nombres en entrée et retourne vrai si tous le nombres dans la liste sont positif (greater que zero), et False sinon.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: / >
# Fonctions intégrées : len, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → total = 0
#   → count = 0
#   → for item in numbers:
#   →     total += item
#   →     count += 1
#   → return total / count if count else 0
#   → total = 0
#   → count = 0
#   → for number in numbers:
#   →     total += number
#   →     count += 1
#   → average = total / count
#   → return average
#   → total = 0
#   → count = 0
#   → for number in numbers:
#   →     total += number
#   →     count += 1
#   → average = total / count
#   → return average
#   → total = 0
#   → count = 0
#   → for item in numbers:
#   →     total += item
#   →     count += 1
#   → return total / count if count else 0
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — find_average, find_average_lst are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(find_average(...))  # find_average() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → print(find_average_lst(...))  # find_average_lst() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → print(find_average_lst(...))  # find_average_lst() runs first → value goes to print()
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(find_average(...))  # find_average() runs first → value goes to print()
#
# Loop: takes one item from numbers, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 22 :
Écrivez une fonction Python appelée `find_average` qui prend une liste de nombres en entrée et retourne le moyenne de ces nombres.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: < > and
# Fonctions intégrées : any, len, min()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return True
#   → return True
#   → return True
#   → return True
#   → return True
#   → return True
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only contains_negative is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(contains_negative(...))  # contains_negative() runs first → value goes to print()
#   → print(contains_negative(...))  # contains_negative() runs first → value goes to print()
#   → print(contains_negative(...))  # contains_negative() runs first → value goes to print()
#   → print(contains_negative(...))  # contains_negative() runs first → value goes to print()
#   → print(contains_negative(...))  # contains_negative() runs first → value goes to print()
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(contains_negative(...))  # contains_negative() runs first → value goes to print()
#
# Loop: takes one item from numbers, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 23 :
Écrivez une fonction Python appelée `contains_negative` qui prend une liste de nombres en entrée et retourne vrai si la liste contient un négatif nombre, et False sinon.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: ==
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return string[-1]
#   → last = elements[-1]
#   → for element in elements:
#   →     if element == last:
#   →         return last
#   → return string[-1]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — find_element, find_last_element are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(find_last_element(...))  # find_last_element() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → print(find_element(...))  # find_element() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(find_last_element(...))  # find_last_element() runs first → value goes to print()
#
# Loop: takes one item from elements, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 24 :
Écrivez une fonction Python appelée `find_last_element` qui prend une liste si nombres et retourne le dernier nombre de la liste.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : len, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return count
#   → return count
#   → return count
#   → return count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only multiply_elements is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → arg = ...  # stored in memory
#   → print(multiply_elements(...))  # multiply_elements() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → print(multiply_elements(...))  # multiply_elements() runs first → value goes to print()
#   → arg = ...  # stored in memory
#   → print(multiply_elements(...))  # multiply_elements() runs first → value goes to print()
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(multiply_elements(...))  # multiply_elements() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
"""
Problème 25 :
Écrivez une fonction Python appelée `multiply_elements` qui prend une liste de nombres en entrée et retourne le produit de tous le nombres dans la liste.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: > != in
# Fonctions intégrées : any, input, len, list, map, set()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(lambda word: word, lst))
#   → return list(map(lambda word: word, lst))
#   → return list(map(lambda word: word, lst))
#   → return list(map(lambda word: word, lst))
#   → return list(map(lambda word: word, lst))
#   → return list(map(lambda word: word, lst))
#   → return list(map(lambda word: word, lst))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only has_duplicates is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(has_duplicates(...))  # has_duplicates() runs first → value goes to print()
#   → has_duplicates()  # jumps into has_duplicates(), runs body, returns
#   → print(has_duplicates(...))  # has_duplicates() runs first → value goes to print()
#   → list_with_duplicates = ...  # stored in memory
#   → list_without_duplicates = ...  # stored in memory
#   → print('Does the list have duplicates?', has_duplicates(...))
#   → print(has_duplicates(...))  # has_duplicates() runs first → value goes to print()
#   → print(has_duplicates(...))  # has_duplicates() runs first → value goes to print()
#   → print(has_duplicates(...))  # has_duplicates() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(has_duplicates(...))  # has_duplicates() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 26 :
Écrivez une fonction Python appelée `has_duplicates` qui prend une liste en entrée et retourne vrai si la liste contient un en double éléments, et False sinon.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: % ==
# Fonctions intégrées : sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return 'The word %s occures %s times' % (word, count)
#   → return 'The word %s occures %s times' % (word, count)
#   → return 'The word %s occures %s times' % (word, count)
#   → return 'The word %s occures %s times' % (word, count)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_occurrences is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → elements = ...  # stored in memory
#   → target = ...  # stored in memory
#   → print(count_occurrences(...))  # count_occurrences() runs first → value goes to print()
#   → list_elements = ...  # stored in memory
#   → target_element = ...  # stored in memory
#   → print(?)
#   → print(count_occurrences(...))  # count_occurrences() runs first → value goes to print()
#   → print(count_occurrences(...))  # count_occurrences() runs first → value goes to print()
#   → elements = ...  # stored in memory
#   → target = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_occurrences(...))  # count_occurrences() runs first → value goes to print()
#
# Loop: takes one item from elements, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 27 :
Écrivez une fonction Python appelée `count_occurrences` qui prend une liste et un élément en entrée et retourne le nombre de fois élément apparaît dans la liste.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: not in
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#   → return result
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only remove_vowels is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(remove_vowels(...))  # remove_vowels() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → print(remove_vowels(...))  # remove_vowels() runs first → value goes to print()
#   → print(remove_vowels(...))  # remove_vowels() runs first → value goes to print()
#   → print(remove_vowels(...))  # remove_vowels() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(remove_vowels(...))  # remove_vowels() runs first → value goes to print()
#
# Loop: takes one item from string, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 28 :
Écrivez une fonction Python appelée `remove_vowels` qui prend une chaîne en entrée et retourne une nouvelle chaîne avec tous la voyelles (a, e, i, o, u) removed.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return ' '.join(capitalized_words)
#   → return ' '.join(capitalized_words)
#   → return ' '.join(capitalized_words)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only capitalize_words is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → input_sentence = ...  # stored in memory
#   → print('Capitalized sentence:', capitalize_words(...))
#   → print(capitalize_words(...))  # capitalize_words() runs first → value goes to print()
#   → print(capitalize_words(...))  # capitalize_words() runs first → value goes to print()
#   → sentence = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(capitalize_words(...))  # capitalize_words() runs first → value goes to print()
#
# Loop: takes one item from words, runs body, repeats until done
"""
Problème 29 :
Écrivez une fonction Python appelée `capitalize_words` qui prend une chaîne en entrée et retourne une nouvelle chaîne avec le premier lettre de chaque mot capitalized. Supposons que words sont séparés by spaces.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: !=
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sentence.replace(' ', '')
#   → space_removed = string.replace(' ', '')
#   → return space_removed
#   → return sentence.replace(' ', '')
#   → return sentence.replace(' ', '')
#   → return sentence.replace(' ', '')
#   → return sentence.replace(' ', '')
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — remove_space, remove_spaces are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → arg = ...  # stored in memory
#   → print(remove_spaces(...))  # remove_spaces() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → print(remove_space(...))  # remove_space() runs first → value goes to print()
#   → arg = ...  # stored in memory
#   → print(remove_spaces(...))  # remove_spaces() runs first → value goes to print()
#   → print(remove_spaces(...))  # remove_spaces() runs first → value goes to print()
#   → print(remove_spaces(...))  # remove_spaces() runs first → value goes to print()
#   → sentence = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(remove_spaces(...))  # remove_spaces() runs first → value goes to print()
#
# Loop: takes one item from split_word, runs body, repeats until done
"""
Problème 30 :
Écrivez une fonction Python appelée remove_spaces qui prend une chaîne en entrée et retourne une nouvelle chaîne avec tous spaces removed.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: +
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return '.'.join((part[0].upper() for part in parts)) + '.'
#   → return '.'.join((part[0].upper() for part in parts)) + '.'
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only get_initials is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(get_initials(...))  # get_initials() runs first → value goes to print()
#   → full_name = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(get_initials(...))  # get_initials() runs first → value goes to print()
"""
Problème 31 :
Écrivez une fonction Python appelée get_initials qui prend un full nom (premier et dernier nom) en entrée et retourne le initials de le nom en majuscule. par exemple, si le entrée est “John Doe”, la fonction devrait retourner “J.D.”.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: +
# Fonctions intégrées : reversed()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → result = ''
#   → for char in seperate:
#   →     result = char + result
#   → return result
#   → words = string.split()
#   → result = []
#   → for word in reversed(words):
#   →     result.append(word)
#   → return ' '.join(result)
#   → words = string.split()
#   → result = []
#   → for word in reversed(words):
#   →     result.append(word)
#   → return ' '.join(result)
#   → words = string.split()
#   → result = []
#   → for word in reversed(words):
#   →     result.append(word)
#   → return ' '.join(result)
#   → result = ''
#   → for char in seperate:
#   →     result = char + result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — reverse_word, reverse_words are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(reverse_word(...))  # reverse_word() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → print(reverse_words(...))  # reverse_words() runs first → value goes to print()
#   → print(reverse_words(...))  # reverse_words() runs first → value goes to print()
#   → print(reverse_words(...))  # reverse_words() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(reverse_word(...))  # reverse_word() runs first → value goes to print()
#
# Loop: takes one item from reversed(...), runs body, repeats until done
"""
Problème 32 :
Écrivez une fonction Python appelée reverse_words qui prend une chaîne en entrée et retourne une nouvelle chaîne avec le words inversé. par exemple, si le entrée est “hello world”, la fonction devrait retourner “world hello”.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: in or not in
# Fonctions intégrées : list, set()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(set(input_list))
#   → return list(set(input_list))
#   → return list(set(input_list))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only remove_duplicates is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → input_list = ...  # stored in memory
#   → print('List with duplicates removed:', remove_duplicates(...))
#   → input_list = ...  # stored in memory
#   → print('List with duplicates removed:', remove_duplicates(...))
#   → print(remove_duplicates(...))  # remove_duplicates() runs first → value goes to print()
#   → print(remove_duplicates(...))  # remove_duplicates() runs first → value goes to print()
#   → input_list = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(remove_duplicates(...))  # remove_duplicates() runs first → value goes to print()
#
# Loop: takes one item from input_list, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 33 :
Écrivez une fonction Python appelée `remove_duplicates` qui prend une liste en entrée et retourne une nouvelle liste avec en double éléments removed, tandis que maintaining le original order d'éléments.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: >
# Fonctions intégrées : len, max()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return max(lst, key=len)
#   → return max(lst, key=len)
#   → return max(lst, key=len)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — find_longest_word, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → main(lst)  # jumps into main(), runs body, returns
#   → lst = ...  # stored in memory
#   → main(lst)  # jumps into main(), runs body, returns
#   → input_string = ...  # stored in memory
#   → print('Longest word:', find_longest_word(...))
#   → input_string = ...  # stored in memory
#   → print('Longest word:', find_longest_word(...))
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(main(...))  # main() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 34 :
Écrivez une fonction Python appelée find_longest_word qui prend une chaîne de mots en entrée et retourne le plus long mot dans la liste. si il y un multiple le plus long words, retourner le premier l'une encountered.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: in
# Fonctions intégrées : filter, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return return_vowels
#   → return return_vowels
#   → return return_vowels
#   → return return_vowels
#   → return return_vowels
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only find_vowels is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(find_vowels(...))  # find_vowels() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → print(find_vowels(...))  # find_vowels() runs first → value goes to print()
#   → print(find_vowels(...))  # find_vowels() runs first → value goes to print()
#   → print(find_vowels(...))  # find_vowels() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(find_vowels(...))  # find_vowels() runs first → value goes to print()
#
# Loop: takes one item from string, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 35 :
Écrivez une fonction Python appelée find_vowels qui prend une chaîne en entrée et retourne une liste de voyelles (a, e, i, o, u) present dans la chaîne. Ignorez la casse, meaning consider les deux uppercase et lowercase voyelles.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: while
# Operators: % * + > >=
# Fonctions intégrées : abs, int, str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return int(str(number)[::-1])
#   → return int(str(number)[::-1])
#   → return int(str(number)[::-1])
#   → return int(str(number)[::-1])
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only reverse_number is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → number = ...  # stored in memory
#   → print(reverse_number(...))  # reverse_number() runs first → value goes to print()
#   → print(reverse_number(...))  # reverse_number() runs first → value goes to print()
#   → print(reverse_number(...))  # reverse_number() runs first → value goes to print()
#   → number = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(reverse_number(...))  # reverse_number() runs first → value goes to print()
#
# Loop: check condition → if True run body → check again
"""
Problème 36 :
Écrivez une fonction Python appelée `reverse_number` qui prend un entier en entrée et retourne le reverse de cette nombre. par exemple, si le entrée est 123, la fonction devrait retourner 321.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: in or not in
# Fonctions intégrées : list, set()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(set(strings))
#   → seen = set()
#   → return ''.join([c for c in string if not (c in seen or seen.add(c))])
#   → duplicates = []
#   → for number in numbers:
#   →     if number not in duplicates:
#   →         duplicates.append(number)
#   → return duplicates
#   → seen = set()
#   → return ''.join([c for c in string if not (c in seen or seen.add(c))])
#   → seen = set()
#   → return ''.join([c for c in string if not (c in seen or seen.add(c))])
#   → return list(set(strings))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — remove_dupicates, remove_duplicate, remove_duplicates are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(remove_duplicate(...))  # remove_duplicate() runs first → value goes to print()
#   → input_string = ...  # stored in memory
#   → print(remove_duplicates(...))  # remove_duplicates() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → print(remove_dupicates(...))  # remove_dupicates() runs first → value goes to print()
#   → print(remove_duplicates(...))  # remove_duplicates() runs first → value goes to print()
#   → print(remove_duplicates(...))  # remove_duplicates() runs first → value goes to print()
#   → strings = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(remove_duplicate(...))  # remove_duplicate() runs first → value goes to print()
#
# Loop: takes one item from string, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 37 :
Écrivez une fonction Python appelée remove_duplicates qui prend une chaîne en entrée et retourne une nouvelle chaîne avec en double caractères removed, tandis que maintaining le original order de caractères.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: +
# Fonctions intégrées : input, int, reduce, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → user = input('type numbers: ').split()
#   → int_number = []
#   → for number in user:
#   →     int_number.append(int(number))
#   → count = 0
#   → for number in int_number:
#   →     count += number
#   → result = count
#   → return result
#   → user = input('type numbers: ').split()
#   → int_number = []
#   → for number in user:
#   →     int_number.append(int(number))
#   → count = 0
#   → for number in int_number:
#   →     count += number
#   → result = count
#   → return result
#   → user = input('type numbers: ').split()
#   → int_number = []
#   → for number in user:
#   →     int_number.append(int(number))
#   → count = 0
#   → for number in int_number:
#   →     count += number
#   → result = count
#   → return result
#   → user = input('type numbers: ').split()
#   → int_number = []
#   → for number in user:
#   →     int_number.append(int(number))
#   → count = 0
#   → for number in int_number:
#   →     count += number
#   → result = count
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sum_of_list is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → sum_of_list()  # jumps into sum_of_list(), runs body, returns
#   → print(sum_of_list(...))  # sum_of_list() runs first → value goes to print()
#   → print(sum_of_list(...))  # sum_of_list() runs first → value goes to print()
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sum_of_list(...))  # sum_of_list() runs first → value goes to print()
#
# Loop: takes one item from user, runs body, repeats until done
"""
Problème 38 :
Écrivez une fonction Python appelée `sum_of_list` qui prend une liste de nombres en entrée et retourne le somme de tous le nombres dans la liste.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: +
# Fonctions intégrées : reduce, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return count
#   → return count
#   → return count
#   → return count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sum_of_list is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(sum_of_list(...))  # sum_of_list() runs first → value goes to print()
#   → print(sum_of_list(...))  # sum_of_list() runs first → value goes to print()
#   → print(sum_of_list(...))  # sum_of_list() runs first → value goes to print()
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sum_of_list(...))  # sum_of_list() runs first → value goes to print()
#
# Loop: takes one item from numbers, runs body, repeats until done
"""
Problème 39 :
Écrivez une fonction Python appelée sum_of_list qui prend une liste de nombres en entrée et retourne le somme de tous le nombres dans la liste.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: < >
# Fonctions intégrées : max, min, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return (min_number, max_number)
#   → return (min_number, max_number)
#   → return (min_number, max_number)
#   → return (min_number, max_number)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only find_min_max is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(find_min_max(...))  # find_min_max() runs first → value goes to print()
#   → print(find_min_max(...))  # find_min_max() runs first → value goes to print()
#   → print(find_min_max(...))  # find_min_max() runs first → value goes to print()
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(find_min_max(...))  # find_min_max() runs first → value goes to print()
#
# Loop: takes one item from numbers, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 40 :
Écrivez une fonction Python appelée find_min_max qui prend une liste de nombres en entrée et retourne un tuple contenant le minimum et maximum nombres dans la liste.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: ==
# Fonctions intégrées : input, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return count
#   → return count
#   → return count
#   → return count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_occurrences is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → count_occurrences()  # jumps into count_occurrences(), runs body, returns
#   → print(count_occurrences(...))  # count_occurrences() runs first → value goes to print()
#   → print(count_occurrences(...))  # count_occurrences() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → target = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_occurrences(...))  # count_occurrences() runs first → value goes to print()
#
# Loop: takes one item from user, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 41 :
Écrivez une fonction Python appelée `count_occurrences` qui prend une liste et un élément en entrée et retourne le nombre de fois élément apparaît dans la liste.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: **
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(lambda number: number ** 2, numbers))
#   → return list(map(lambda number: number ** 2, numbers))
#   → return list(map(lambda number: number ** 2, numbers))
#   → return list(map(lambda number: number ** 2, numbers))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only square_elements is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(square_elements(...))  # square_elements() runs first → value goes to print()
#   → print(square_elements(...))  # square_elements() runs first → value goes to print()
#   → print(square_elements(...))  # square_elements() runs first → value goes to print()
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(square_elements(...))  # square_elements() runs first → value goes to print()
#
# Loop: takes one item from numbers, runs body, repeats until done
"""
Problème 43 :
Écrivez une fonction Python appelée square_elements qui prend une liste de nombres en entrée et retourne une nouvelle liste avec chaque élément au carré.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: ==
# Fonctions intégrées : filter, len, list, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return len([char for char in string if char.isupper()])
#   → return len([char for char in string if char.isupper()])
#   → return len([char for char in string if char.isupper()])
#   → return len([char for char in string if char.isupper()])
#   → return len([char for char in string if char.isupper()])
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_uppercase is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(count_uppercase(...))  # count_uppercase() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → print(count_uppercase(...))  # count_uppercase() runs first → value goes to print()
#   → print(count_uppercase(...))  # count_uppercase() runs first → value goes to print()
#   → print(count_uppercase(...))  # count_uppercase() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_uppercase(...))  # count_uppercase() runs first → value goes to print()
#
# Loop: takes one item from string, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 44 :
Écrivez une fonction Python appelée count_uppercase qui prend une chaîne en entrée et retourne le nombre de uppercase lettre dans la chaîne.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: !=
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return string.replace(' ', '')
#   → return string.replace(' ', '')
#   → return string.replace(' ', '')
#   → return string.replace(' ', '')
#   → return string.replace(' ', '')
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only remove_spaces is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(remove_spaces(...))  # remove_spaces() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → print(remove_spaces(...))  # remove_spaces() runs first → value goes to print()
#   → print(remove_spaces(...))  # remove_spaces() runs first → value goes to print()
#   → print(remove_spaces(...))  # remove_spaces() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(remove_spaces(...))  # remove_spaces() runs first → value goes to print()
#
# Loop: takes one item from string, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 45 :
Écrivez une fonction Python appelée remove_spaces qui prend une chaîne en entrée et retourne la chaîne avec tous spaces removed.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: +
# Fonctions intégrées : input, list, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → lst1 = sorted(input('Type the first sorted list: ').split())
#   → lst2 = sorted(input('Type the second sorted list: ').split())
#   → merged_list = sorted(lst1 + lst2)
#   → result = merged_list
#   → return result
#   → lst1 = sorted(input('Type the first sorted list: ').split())
#   → lst2 = sorted(input('Type the second sorted list: ').split())
#   → merged_list = sorted(lst1 + lst2)
#   → result = merged_list
#   → return result
#   → lst1 = sorted(input('Type the first sorted list: ').split())
#   → lst2 = sorted(input('Type the second sorted list: ').split())
#   → merged_list = sorted(lst1 + lst2)
#   → result = merged_list
#   → return result
#   → lst1 = sorted(input('Type the first sorted list: ').split())
#   → lst2 = sorted(input('Type the second sorted list: ').split())
#   → merged_list = sorted(lst1 + lst2)
#   → result = merged_list
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only merge_lists is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → merge_lists()  # jumps into merge_lists(), runs body, returns
#   → print(merge_lists(...))  # merge_lists() runs first → value goes to print()
#   → print(merge_lists(...))  # merge_lists() runs first → value goes to print()
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(merge_lists(...))  # merge_lists() runs first → value goes to print()
"""
Problème 46 :
Écrivez une fonction Python appelée merge_lists qui prend deux listes triées en entrée et retourne une nouvelle liste triée contenant tous le éléments de les deux entrée listes.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else | try/except
# Operators: ==
# Fonctions intégrées : enumerate()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return index
#   → return index
#   → return index
#   → return index
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only find_index is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → target = ...  # stored in memory
#   → print('Index of', target, 'in nums:', find_index(...))
#   → target = ...  # stored in memory
#   → print('Index of', target, 'in nums:', find_index(...))
#   → print(find_index(...))  # find_index() runs first → value goes to print()
#   → print(find_index(...))  # find_index() runs first → value goes to print()
#   → print(find_index(...))  # find_index() runs first → value goes to print()
#   → numbers = ...  # stored in memory
#   → target = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(find_index(...))  # find_index() runs first → value goes to print()
#
# Loop: takes one item from enumerate(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 47 :
Écrivez une fonction Python appelée find_index qui prend une liste de nombres et une cible nombre en entrée, et retourne le index de le cible nombre dans la liste. si le cible nombre est pas trouvé dans la liste, la fonction devrait retourner -1.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: % ==
# Fonctions intégrées : enumerate, len, range, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return total
#   → return total
#   → return total
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sum_even_indices is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → print('Sum of elements at even indices:', sum_even_indices(...))
#   → numbers = ...  # stored in memory
#   → print('Sum of elements at even indices:', sum_even_indices(...))
#   → print(sum_even_indices(...))  # sum_even_indices() runs first → value goes to print()
#   → print(sum_even_indices(...))  # sum_even_indices() runs first → value goes to print()
#   → nums = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sum_even_indices(...))  # sum_even_indices() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 48 :
Écrivez une fonction Python appelée sum_even_indices qui prend une liste de nombres en entrée et retourne le somme de le éléments at même les indices (0-based) dans la liste.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: and not in
# Fonctions intégrées : list, map, set()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(lambda word: word_lower, lst))
#   → return list(map(lambda word: word_lower, lst))
#   → return list(map(lambda word: word_lower, lst))
#   → return list(map(lambda word: word_lower, lst))
#   → return list(map(lambda word: word_lower, lst))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only remove_duplicates is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(remove_duplicates(...))  # remove_duplicates() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → print(remove_duplicates(...))  # remove_duplicates() runs first → value goes to print()
#   → input_strings = ...  # stored in memory
#   → print('List with case-insensitive duplicates removed:', remove_duplicates(...))
#   → print(remove_duplicates(...))  # remove_duplicates() runs first → value goes to print()
#   → print(remove_duplicates(...))  # remove_duplicates() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(remove_duplicates(...))  # remove_duplicates() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 49 :
Écrivez une fonction Python appelée remove_duplicates_case_insensitive qui prend une liste de chaînes en entrée et retourne une nouvelle liste avec en double strings removed, en ignorant la casse sensitivity. par exemple, “hello” et “HELLO” devrait be considered le même. N'utilisez pas set().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else | while
# Operators: - < != ==
# Fonctions intégrées : len, reversed()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return s == s[::-1]
#   → return s == s[::-1]
#   → return s == s[::-1]
#   → return s == s[::-1]
#   → return s == s[::-1]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only is_palindrome is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → input_string = ...  # stored in memory
#   → print('Is', input_string, 'a palindrome?', is_palindrome(...))
#   → input_string = ...  # stored in memory
#   → print('Is', input_string, 'a palindrome?', is_palindrome(...))
#   → print(is_palindrome(...))  # is_palindrome() runs first → value goes to print()
#   → print(is_palindrome(...))  # is_palindrome() runs first → value goes to print()
#   → print(is_palindrome(...))  # is_palindrome() runs first → value goes to print()
#   → print(is_palindrome(...))  # is_palindrome() runs first → value goes to print()
#   → s = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_palindrome(...))  # is_palindrome() runs first → value goes to print()
#
# Loop: check condition → if True run body → check again
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 50 :
Écrivez une fonction Python appelée is_palindrome qui prend une chaîne en entrée et retourne vrai si la chaîne est un palindrome (lit le même forwards et backwards), et False sinon.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: * + - ==
# Fonctions intégrées : range, reduce()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return 1
#   → return 1
#   → return 1
#   → return 1
#   → return 1
#   → return 1
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only factorial is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(factorial(...))  # factorial() runs first → value goes to print()
#   → print(factorial(...))  # factorial() runs first → value goes to print()
#   → print(factorial(...))  # factorial() runs first → value goes to print()
#   → print(factorial(...))  # factorial() runs first → value goes to print()
#   → print(factorial(...))  # factorial() runs first → value goes to print()
#   → n = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(factorial(...))  # factorial() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 51 :
Écrivez une fonction Python appelée `la factorielle` qui prend un non-négatif integer en entrée et retourne ses la factorielle. la factorielle de un nombre `n` est le produit de tous positif integers less que ou equal à `n` (n!). par exemple, `la factorielle(5)` devrait retourner `120` (since 5 * 4 * 3 * 2 * 1 = 120).
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: != ==
# Fonctions intégrées : Counter, input, len, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return True
#   → str1, str2 = (str1.lower(), str2.lower())
#   → if len(str1) != len(str2):
#   →     return False
#   → for char in str1:
#   →     if str1.count(char) != str2.count(char):
#   →         return False
#   → return True
#   → str1, str2 = (str1.lower(), str2.lower())
#   → if len(str1) != len(str2):
#   →     return False
#   → for char in str1:
#   →     if str1.count(char) != str2.count(char):
#   →         return False
#   → return True
#   → str1, str2 = (str1.lower(), str2.lower())
#   → if len(str1) != len(str2):
#   →     return False
#   → for char in str1:
#   →     if str1.count(char) != str2.count(char):
#   →         return False
#   → return True
#   → str1, str2 = (str1.lower(), str2.lower())
#   → if len(str1) != len(str2):
#   →     return False
#   → for char in str1:
#   →     if str1.count(char) != str2.count(char):
#   →         return False
#   → return True
#   → str1, str2 = (str1.lower(), str2.lower())
#   → if len(str1) != len(str2):
#   →     return False
#   → for char in str1:
#   →     if str1.count(char) != str2.count(char):
#   →         return False
#   → return True
#   → str1, str2 = (str1.lower(), str2.lower())
#   → if len(str1) != len(str2):
#   →     return False
#   → for char in str1:
#   →     if str1.count(char) != str2.count(char):
#   →         return False
#   → return True
#   → str1, str2 = (str1.lower(), str2.lower())
#   → if len(str1) != len(str2):
#   →     return False
#   → for char in str1:
#   →     if str1.count(char) != str2.count(char):
#   →         return False
#   → return True
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — is_anagram, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → main()  # jumps into main(), runs body, returns
#   → print(is_anagram(...))  # is_anagram() runs first → value goes to print()
#   → print(is_anagram(...))  # is_anagram() runs first → value goes to print()
#   → print(is_anagram(...))  # is_anagram() runs first → value goes to print()
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → print(is_anagram(...))  # is_anagram() runs first → value goes to print()
#   → print(is_anagram(...))  # is_anagram() runs first → value goes to print()
#   → print(is_anagram(...))  # is_anagram() runs first → value goes to print()
#   → str1 = ...  # stored in memory
#   → str2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_anagram(...))  # is_anagram() runs first → value goes to print()
#
# Loop: takes one item from str1, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 52 :
Écrivez une fonction Python appelée is_anagram qui prend deux strings en entrée et retourne vrai si they sont anagrams de chaque autre, et False sinon. deux strings sont anagrams si they peut be rearranged à form le même mot (e.g., “listen” et “silent”).
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: + in
# Fonctions intégrées : Counter, dict()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return word_count
#   → return word_count
#   → return word_count
#   → return word_count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_words is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → input_string = ...  # stored in memory
#   → print(count_words(...))  # count_words() runs first → value goes to print()
#   → print(count_words(...))  # count_words() runs first → value goes to print()
#   → print(count_words(...))  # count_words() runs first → value goes to print()
#   → s = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_words(...))  # count_words() runs first → value goes to print()
#
# Loop: takes one item from words, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 53 :
Écrivez une fonction Python appelée count_words qui prend une chaîne en entrée et retourne un dictionnaire où le clés sont le words dans la chaîne et le valeurs sont le compte de chaque mot. Words sont séparés by spaces, et la fonction devrait be cas-insensitive.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: + - <= ==
# Fonctions intégrées : list, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return []
#   → return []
#   → return []
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only fibonacci is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(fibonacci(...))  # fibonacci() runs first → value goes to print()
#   → print(fibonacci(...))  # fibonacci() runs first → value goes to print()
#   → print(list(...))
#   → n = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(fibonacci(...))  # fibonacci() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 54 :
Écrivez une fonction Python appelée fibonacci qui prend un entier n en entrée et retourne une liste contenant les n premiers nombres de la suite de Fibonacci. la suite de Fibonacci commence par 0 et 1, et chaque subsequent nombre est le somme de le précédent deux nombres.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: *
# Fonctions intégrées : float, input()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → length = float(input('Enter length: '))
#   → width = float(input('Enter width: '))
#   → result = length * width
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only area_rectangle is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → area_rectangle()  # jumps into area_rectangle(), runs body, returns
#   → length = ...  # stored in memory
#   → width = ...  # stored in memory
#   → print(length * width)
#   → length = ...  # stored in memory
#   → width = ...  # stored in memory
#   → print(length * width)
"""
Problème 55 :
Écrivez un programme Python à calculate le area de un rectangle. demander le utilisateur à saisir la longueur et width.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else
# Operators: % & ==
# Fonctions intégrées : input, int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return 'Even' if n & 1 == 0 else 'Odd'
#   → return 'Even' if n & 1 == 0 else 'Odd'
#   → return 'Even' if n & 1 == 0 else 'Odd'
#   → return 'Even' if n & 1 == 0 else 'Odd'
#   → return 'Even' if n & 1 == 0 else 'Odd'
#   → return 'Even' if n & 1 == 0 else 'Odd'
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only even_odd is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → even_odd()  # jumps into even_odd(), runs body, returns
#   → print(even_odd(...))  # even_odd() runs first → value goes to print()
#   → print(even_odd(...))  # even_odd() runs first → value goes to print()
#   → print(even_odd(...))  # even_odd() runs first → value goes to print()
#   → print(even_odd(...))  # even_odd() runs first → value goes to print()
#   → n = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(even_odd(...))  # even_odd() runs first → value goes to print()
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 56 :
Écrivez un programme Python à vérifier si une donnée nombre est pair ou impair. demander le utilisateur à saisir un nombre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: while
# Operators: + <=
# Fonctions intégrées : input, int, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → fib = [0, 1]
#   → [fib.append(fib[-1] + fib[-2]) for _ in range(2, n)]
#   → return fib[:n]
#   → fib = [0, 1]
#   → [fib.append(fib[-1] + fib[-2]) for _ in range(2, n)]
#   → return fib[:n]
#   → fib = [0, 1]
#   → [fib.append(fib[-1] + fib[-2]) for _ in range(2, n)]
#   → return fib[:n]
#   → fib = [0, 1]
#   → [fib.append(fib[-1] + fib[-2]) for _ in range(2, n)]
#   → return fib[:n]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only fibonacci_series is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → fibonacci_series()  # jumps into fibonacci_series(), runs body, returns
#   → print(fibonacci_series(...))  # fibonacci_series() runs first → value goes to print()
#   → print(fibonacci_series(...))  # fibonacci_series() runs first → value goes to print()
#   → limit = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(fibonacci_series(...))  # fibonacci_series() runs first → value goes to print()
#
# Loop: check condition → if True run body → check again
"""
Problème 57 :
Écrivez un programme Python à print le Fibonacci series up à une donnée nombre. demander le utilisateur à saisir le limit en utilisant un tandis que loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: > >= and
# Fonctions intégrées : input, int, max, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → user = input('type 3 numbers: ').split()
#   → int_number = []
#   → for number in user:
#   →     int_number.append(int(number))
#   → max_num = int_number[0]
#   → for number in int_number:
#   →     if number > max_num:
#   →         max_num = number
#   → result = max_num
#   → return result
#   → user = input('type 3 numbers: ').split()
#   → int_number = []
#   → for number in user:
#   →     int_number.append(int(number))
#   → max_num = int_number[0]
#   → for number in int_number:
#   →     if number > max_num:
#   →         max_num = number
#   → result = max_num
#   → return result
#   → user = input('type 3 numbers: ').split()
#   → int_number = []
#   → for number in user:
#   →     int_number.append(int(number))
#   → max_num = int_number[0]
#   → for number in int_number:
#   →     if number > max_num:
#   →         max_num = number
#   → result = max_num
#   → return result
#   → user = input('type 3 numbers: ').split()
#   → int_number = []
#   → for number in user:
#   →     int_number.append(int(number))
#   → max_num = int_number[0]
#   → for number in int_number:
#   →     if number > max_num:
#   →         max_num = number
#   → result = max_num
#   → return result
#   → user = input('type 3 numbers: ').split()
#   → int_number = []
#   → for number in user:
#   →     int_number.append(int(number))
#   → max_num = int_number[0]
#   → for number in int_number:
#   →     if number > max_num:
#   →         max_num = number
#   → result = max_num
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only max_number is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → max_number()  # jumps into max_number(), runs body, returns
#   → print(max_number(...))  # max_number() runs first → value goes to print()
#   → print(max_number(...))  # max_number() runs first → value goes to print()
#   → print(max_number(...))  # max_number() runs first → value goes to print()
#   → a = ...  # stored in memory
#   → b = ...  # stored in memory
#   → c = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(max_number(...))  # max_number() runs first → value goes to print()
#
# Loop: takes one item from user, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 58 :
Écrivez un programme Python à trouver le maximum de trois nombres. demander le utilisateur à saisir trois nombres."
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: +
# Fonctions intégrées : input, reversed()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → user = input('type string: ')
#   → user = user[::-1]
#   → result = user
#   → return result
#   → user = input('type string: ')
#   → user = user[::-1]
#   → result = user
#   → return result
#   → user = input('type string: ')
#   → user = user[::-1]
#   → result = user
#   → return result
#   → user = input('type string: ')
#   → user = user[::-1]
#   → result = user
#   → return result
#   → user = input('type string: ')
#   → user = user[::-1]
#   → result = user
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only reverse_string is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → reverse_string()  # jumps into reverse_string(), runs body, returns
#   → lst = ...  # stored in memory
#   → print(reverse_string(...))  # reverse_string() runs first → value goes to print()
#   → print(reverse_string(...))  # reverse_string() runs first → value goes to print()
#   → print(reverse_string(...))  # reverse_string() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(reverse_string(...))  # reverse_string() runs first → value goes to print()
#
# Loop: takes one item from s, runs body, repeats until done
"""
Problème 59 :
Écrivez un programme Python à reverse une chaîne. demander le utilisateur à saisir une chaîne.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else | while
# Operators: + - < != // ==
# Fonctions intégrées : all, input, len, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return user == user[::-1]
#   → return user == user[::-1]
#   → return user == user[::-1]
#   → return user == user[::-1]
#   → return user == user[::-1]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only is_palindrome is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(is_palindrome(...))  # is_palindrome() runs first → value goes to print()
#   → print(is_palindrome(...))  # is_palindrome() runs first → value goes to print()
#   → print(is_palindrome(...))  # is_palindrome() runs first → value goes to print()
#   → print(is_palindrome(...))  # is_palindrome() runs first → value goes to print()
#   → s = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_palindrome(...))  # is_palindrome() runs first → value goes to print()
#
# Loop: check condition → if True run body → check again
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 60 :
Écrivez un programme Python à vérifier si une donnée chaîne est un palindrome. demander le utilisateur à saisir une chaîne.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: in
# Fonctions intégrées : input, len, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → user = input('type string: ').lower()
#   → vowels = 'aeiou'
#   → count = 0
#   → for char in user:
#   →     if char in vowels:
#   →         count += 1
#   → result = count
#   → return result
#   → user = input('type string: ').lower()
#   → vowels = 'aeiou'
#   → count = 0
#   → for char in user:
#   →     if char in vowels:
#   →         count += 1
#   → result = count
#   → return result
#   → user = input('type string: ').lower()
#   → vowels = 'aeiou'
#   → count = 0
#   → for char in user:
#   →     if char in vowels:
#   →         count += 1
#   → result = count
#   → return result
#   → user = input('type string: ').lower()
#   → vowels = 'aeiou'
#   → count = 0
#   → for char in user:
#   →     if char in vowels:
#   →         count += 1
#   → result = count
#   → return result
#   → user = input('type string: ').lower()
#   → vowels = 'aeiou'
#   → count = 0
#   → for char in user:
#   →     if char in vowels:
#   →         count += 1
#   → result = count
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_vowels is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → count_vowels()  # jumps into count_vowels(), runs body, returns
#   → print(count_vowels(...))  # count_vowels() runs first → value goes to print()
#   → print(count_vowels(...))  # count_vowels() runs first → value goes to print()
#   → print(count_vowels(...))  # count_vowels() runs first → value goes to print()
#   → s = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_vowels(...))  # count_vowels() runs first → value goes to print()
#
# Loop: takes one item from user, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 61 :
Écrivez un programme Python à compter le nombre de voyelles dans une donnée chaîne. demander le utilisateur à saisir une chaîne.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: * + - <=
# Fonctions intégrées : fact, input, int, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → result = 1
#   → for i in range(1, 6):
#   →     result *= i
#   → result = f'{result}'
#   → return result
#   → result = 1
#   → for i in range(1, 6):
#   →     result *= i
#   → result = f'{result}'
#   → return result
#   → result = 1
#   → for i in range(1, 6):
#   →     result *= i
#   → result = f'{result}'
#   → return result
#   → result = 1
#   → for i in range(1, 6):
#   →     result *= i
#   → result = f'{result}'
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only factorial is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → factorial()  # jumps into factorial(), runs body, returns
#   → factorial()  # jumps into factorial(), runs body, returns
#   → factorial()  # jumps into factorial(), runs body, returns
#   → factorial()  # jumps into factorial(), runs body, returns
#   → result = ...  # stored in memory
#   → for i in range(...)  # runs body once per item
#   → print(?)
#   → result = ...  # stored in memory
#   → for i in range(...)  # runs body once per item
#   → print(?)
#
# Loop: takes one item from range(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 62 :
Écrivez un programme Python à calculate la factorielle de un nombre. demander le utilisateur à saisir un nombre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: +
# Fonctions intégrées : input, int, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → n = int(input('Enter a number: '))
#   → total = 0
#   → for number in range(1, n + 1):
#   →     total += number
#   → result = total
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sum_of_all_numbers is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → sum_of_all_numbers()  # jumps into sum_of_all_numbers(), runs body, returns
#   → n = ...  # stored in memory
#   → total = ...  # stored in memory
#   → for number in range(...)  # runs body once per item
#   → print(total)
#   → n = ...  # stored in memory
#   → total = ...  # stored in memory
#   → for number in range(...)  # runs body once per item
#   → print(total)
#
# Loop: takes one item from range(...), runs body, repeats until done
"""
Problème 63 :
Écrivez un programme Python à calculate le somme de tous nombres de 1 à une donnée nombre. demander le utilisateur à saisir un nombre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: >
# Fonctions intégrées : input, int, max, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → user = input('type number: ').split()
#   → int_number = []
#   → for number in user:
#   →     int_number.append(int(number))
#   → sort = sorted(int_number)
#   → largest = sort[-1]
#   → result = largest
#   → return result
#   → user = input('type number: ').split()
#   → int_number = []
#   → for number in user:
#   →     int_number.append(int(number))
#   → sort = sorted(int_number)
#   → largest = sort[-1]
#   → result = largest
#   → return result
#   → largest = numbers[0]
#   → for number in numbers:
#   →     if number > largest:
#   →         largest = number
#   → return largest
#   → largest = numbers[0]
#   → for number in numbers:
#   →     if number > largest:
#   →         largest = number
#   → return largest
#   → largest = numbers[0]
#   → for number in numbers:
#   →     if number > largest:
#   →         largest = number
#   → return largest
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — find_largest, largest_element are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → find_largest()  # jumps into find_largest(), runs body, returns
#   → find_largest()  # jumps into find_largest(), runs body, returns
#   → numbers = ...  # stored in memory
#   → print(largest_element(...))  # largest_element() runs first → value goes to print()
#   → numbers = ...  # stored in memory
#   → print(largest_element(...))  # largest_element() runs first → value goes to print()
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(largest_element(...))  # largest_element() runs first → value goes to print()
#
# Loop: takes one item from user, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 64 :
Écrivez un programme Python à trouver le plus grand élément dans une liste. demander le utilisateur à saisir une liste de nombres.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: >
# Fonctions intégrées : len, max, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return max(lst, key=len)
#   → lst = sorted(lst, key=len)
#   → return lst[-1]
#   → lst = sorted(lst, key=len)
#   → return lst[-1]
#   → return max(lst, key=len)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — largest_elememt, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → main(lst)  # jumps into main(), runs body, returns
#   → lst = ...  # stored in memory
#   → print(largest_elememt(...))  # largest_elememt() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → print(largest_elememt(...))  # largest_elememt() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(main(...))  # main() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 65 :
Écrivez un programme Python à trouver le plus grand élément dans une liste (N'utilisez pas nombres).
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: in not in
# Fonctions intégrées : list, map, set()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(lambda element: element, elements))
#   → return list(map(lambda element: element, elements))
#   → return list(map(lambda element: element, elements))
#   → return list(map(lambda element: element, elements))
#   → return list(map(lambda element: element, elements))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only remove_duplicates is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(remove_duplicates(...))  # remove_duplicates() runs first → value goes to print()
#   → print(remove_duplicates(...))  # remove_duplicates() runs first → value goes to print()
#   → print(remove_duplicates(...))  # remove_duplicates() runs first → value goes to print()
#   → print(remove_duplicates(...))  # remove_duplicates() runs first → value goes to print()
#   → elements = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(remove_duplicates(...))  # remove_duplicates() runs first → value goes to print()
#
# Loop: takes one item from elements, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 66 :
Écrivez un programme Python à remove les doublons de une liste. demander le utilisateur à saisir une liste d'éléments.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else
# Operators: % != == or and
# Fonctions intégrées : input, int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return True
#   → return True
#   → return True
#   → return True
#   → return True
#   → return True
#   → return True
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only is_leap_year is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(is_leap_year(...))  # is_leap_year() runs first → value goes to print()
#   → print(is_leap_year(...))  # is_leap_year() runs first → value goes to print()
#   → print(is_leap_year(...))  # is_leap_year() runs first → value goes to print()
#   → print(is_leap_year(...))  # is_leap_year() runs first → value goes to print()
#   → print(is_leap_year(...))  # is_leap_year() runs first → value goes to print()
#   → print(is_leap_year(...))  # is_leap_year() runs first → value goes to print()
#   → year = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_leap_year(...))  # is_leap_year() runs first → value goes to print()
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 67 :
Écrivez un programme Python à vérifier si une donnée year est une année bissextile. demander le utilisateur à saisir un year.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : input()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → text = input('Enter a string: ')
#   → count = 0
#   → for _ in text:
#   →     count += 1
#   → result = count
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only length_string is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → length_string()  # jumps into length_string(), runs body, returns
#   → text = ...  # stored in memory
#   → count = ...  # stored in memory
#   → for _ in text  # runs body once per item
#   → print(count)
#   → text = ...  # stored in memory
#   → count = ...  # stored in memory
#   → for _ in text  # runs body once per item
#   → print(count)
#
# Loop: takes one item from text, runs body, repeats until done
"""
Problème 68 :
Écrivez un programme Python à trouver la longueur de une chaîne sans en utilisant le construit-dans len() fonction. demander le utilisateur à saisir une chaîne.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: +
# Fonctions intégrées : Counter, dict()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return count
#   → return count
#   → return count
#   → return count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_each_word is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(count_each_word(...))  # count_each_word() runs first → value goes to print()
#   → print(count_each_word(...))  # count_each_word() runs first → value goes to print()
#   → print(count_each_word(...))  # count_each_word() runs first → value goes to print()
#   → sentence = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_each_word(...))  # count_each_word() runs first → value goes to print()
#
# Loop: takes one item from split_word, runs body, repeats until done
"""
Problème 70 :
Écrivez un programme Python à compter le occurrences de chaque mot dans une donnée phrase. demander le utilisateur à saisir une phrase.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else
# Operators: <
# Fonctions intégrées : input, len, list, map, set, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return None
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — sec_lar, second_largest_number are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(second_largest_number(...))  # second_largest_number() runs first → value goes to print()
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 71 :
Écrivez un programme Python à trouver le deuxième plus grand nombre dans une liste. demander le utilisateur à saisir une liste de nombres.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : bool()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return bool(re.fullmatch(pattern, email))
#   → return bool(re.fullmatch(pattern, email))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only is_valid_email is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(is_valid_email(...))  # is_valid_email() runs first → value goes to print()
#   → email = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_valid_email(...))  # is_valid_email() runs first → value goes to print()
"""
Problème 72 :
Écrivez un programme Python à vérifier si une donnée chaîne est un valid email address. demander le utilisateur à saisir an email address.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else | try/except
# Operators: * + - < == or
# Fonctions intégrées : input, int, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → number = int(input('Enter a number: '))
#   → print(f'The factorial of {number} is {factorial(number)}')
#   → number = int(input('Enter a number: '))
#   → print(f'The factorial of {number} is {factorial(number)}')
#   → number = int(input('Enter a number: '))
#   → print(f'The factorial of {number} is {factorial(number)}')
#   → return 1
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — factorial, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → main()  # jumps into main(), runs body, returns
#   → main()  # jumps into main(), runs body, returns
#   → main()  # jumps into main(), runs body, returns
#   → n = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(factorial(...))  # factorial() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 73 :
Écrivez un programme Python à trouver la factorielle de un nombre en utilisant recursion. demander le utilisateur à saisir un nombre."
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: ==
# Fonctions intégrées : input, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → first = input('Enter the first string: ').replace(' ', '').lower()
#   → second = input('Enter the second string: ').replace(' ', '').lower()
#   → result = sorted(first) == sorted(second)
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only are_anagrams is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → are_anagrams()  # jumps into are_anagrams(), runs body, returns
#   → first = ...  # stored in memory
#   → second = ...  # stored in memory
#   → print(?)
#   → first = ...  # stored in memory
#   → second = ...  # stored in memory
#   → print(?)
"""
Problème 74 :
Écrivez un programme Python à vérifier si deux strings sont anagrams de chaque autre. demander le utilisateur à saisir deux strings
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else | try/except | while
# Operators: % * + < != ** <= == or
# Fonctions intégrées : all, input, int, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → try:
#   →     number = int(input('Enter a number: '))
#   →     if is_prime(number):
#   →         print(f'{number} is a prime number.')
#   →     else:
#   →         print(f'{number} is not a prime number.')
#   → except ValueError:
#   →     print('Please enter a valid integer.')
#   → return False
#   → return False
#   → return False
#   → return False
#   → return False
#   → return False
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — is_prime, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → main()  # jumps into main(), runs body, returns
#   → print(is_prime(...))  # is_prime() runs first → value goes to print()
#   → print(is_prime(...))  # is_prime() runs first → value goes to print()
#   → print(is_prime(...))  # is_prime() runs first → value goes to print()
#   → print(is_prime(...))  # is_prime() runs first → value goes to print()
#   → print(is_prime(...))  # is_prime() runs first → value goes to print()
#   → n = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_prime(...))  # is_prime() runs first → value goes to print()
#
# Loop: check condition → if True run body → check again
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 75 :
Écrivez un programme Python à vérifier si un nombre est un nombre premier. demander le utilisateur à saisir un nombre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: == in and not in
# Fonctions intégrées : filter, input, list, map, set()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(lambda i: i, lst1))
#   → return list(map(lambda i: i, lst1))
#   → input1 = input('Enter elements of the first list, separated by spaces: ')
#   → list1 = input1.split()
#   → input2 = input('Enter elements of the second list, separated by spaces: ')
#   → list2 = input2.split()
#   → set1 = set(list1)
#   → set2 = set(list2)
#   → common_elements = set1.intersection(set2)
#   → if common_elements:
#   →     print(f'Common elements between the two lists: {list(common_elements)}')
#   → else:
#   →     print('There are no common elements between the two lists.')
#   → return list(map(lambda i: i, lst1))
#   → return list(map(lambda i: i, lst1))
#   → return list(map(lambda i: i, lst1))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — common_elements, find_common_elements are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → print(common_elements(...))  # common_elements() runs first → value goes to print()
#   → arg1 = ...  # stored in memory
#   → arg2 = ...  # stored in memory
#   → print(common_elements(...))  # common_elements() runs first → value goes to print()
#   → find_common_elements()  # jumps into find_common_elements(), runs body, returns
#   → print(common_elements(...))  # common_elements() runs first → value goes to print()
#   → print(common_elements(...))  # common_elements() runs first → value goes to print()
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(common_elements(...))  # common_elements() runs first → value goes to print()
#
# Loop: takes one item from lst1, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 76 :
Écrivez un programme Python à trouver le commun éléments entre deux listes. demander le utilisateur à saisir deux listes.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: ==
# Fonctions intégrées : filter, len, list, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return count
#   → return count
#   → return count
#   → return count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only uppercase is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → sentence = ...  # stored in memory
#   → print(uppercase(...))  # uppercase() runs first → value goes to print()
#   → print(uppercase(...))  # uppercase() runs first → value goes to print()
#   → print(uppercase(...))  # uppercase() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(uppercase(...))  # uppercase() runs first → value goes to print()
#
# Loop: takes one item from string, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 77 :
Écrivez une fonction Python appelée `count_uppercase` qui prend une chaîne en entrée et retourne le nombre de uppercase lettre dans la chaîne.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else | while
# Operators: % + > ==
# Fonctions intégrées : bin, format, input, int, str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → decimal_number = int(input('Enter a decimal number: '))
#   → binary_number = bin(decimal_number)[2:]
#   → result = f'The binary representation of {decimal_number} is {binary_number}'
#   → return result
#   → decimal_number = int(input('Enter a decimal number: '))
#   → binary_number = bin(decimal_number)[2:]
#   → result = f'The binary representation of {decimal_number} is {binary_number}'
#   → return result
#   → decimal_number = int(input('Enter a decimal number: '))
#   → binary_number = bin(decimal_number)[2:]
#   → result = f'The binary representation of {decimal_number} is {binary_number}'
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only decimal_to_binary is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → decimal_to_binary()  # jumps into decimal_to_binary(), runs body, returns
#   → decimal_to_binary()  # jumps into decimal_to_binary(), runs body, returns
#   → decimal_to_binary()  # jumps into decimal_to_binary(), runs body, returns
#   → decimal_number = ...  # stored in memory
#   → binary_number = ...  # stored in memory
#   → print(?)
#   → decimal_number = ...  # stored in memory
#   → binary_number = ...  # stored in memory
#   → print(?)
#
# Loop: check condition → if True run body → check again
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 78 :
Écrivez un programme Python à convert un decimal nombre à binary. demander le utilisateur à saisir un decimal nombre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: + - >
# Fonctions intégrées : input, int, len, range, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sorted(result, reverse=False)
#   → arr = numbers.copy()
#   → n = len(arr)
#   → for i in range(n):
#   →     for j in range(0, n - i - 1):
#   →         if arr[j] > arr[j + 1]:
#   →             arr[j], arr[j + 1] = (arr[j + 1], arr[j])
#   → return arr
#   → arr = numbers.copy()
#   → n = len(arr)
#   → for i in range(n):
#   →     for j in range(0, n - i - 1):
#   →         if arr[j] > arr[j + 1]:
#   →             arr[j], arr[j + 1] = (arr[j + 1], arr[j])
#   → return arr
#   → arr = numbers.copy()
#   → n = len(arr)
#   → for i in range(n):
#   →     for j in range(0, n - i - 1):
#   →         if arr[j] > arr[j + 1]:
#   →             arr[j], arr[j + 1] = (arr[j + 1], arr[j])
#   → return arr
#   → arr = numbers.copy()
#   → n = len(arr)
#   → for i in range(n):
#   →     for j in range(0, n - i - 1):
#   →         if arr[j] > arr[j + 1]:
#   →             arr[j], arr[j + 1] = (arr[j + 1], arr[j])
#   → return arr
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — ascending_order_numbers, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → main()  # jumps into main(), runs body, returns
#   → numbers = ...  # stored in memory
#   → print(ascending_order_numbers(...))  # ascending_order_numbers() runs first → value goes to print()
#   → print(ascending_order_numbers(...))  # ascending_order_numbers() runs first → value goes to print()
#   → print(ascending_order_numbers(...))  # ascending_order_numbers() runs first → value goes to print()
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(ascending_order_numbers(...))  # ascending_order_numbers() runs first → value goes to print()
#
# Loop: takes one item from user, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 79 :
Écrivez un programme Python à trier une liste de nombres dans l'ordre croissant. demander le utilisateur à saisir une liste de nombres.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: +
# Fonctions intégrées : float, input, int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → lower_limit = int(input('Enter the lower limit: '))
#   → upper_limit = int(input('Enter the upper limit: '))
#   → random_number = random.randint(lower_limit, upper_limit)
#   → result = f'The random number between {lower_limit} and {upper_limit} is: {random_number}'
#   → return result
#   → lower_limit = int(input('Enter the lower limit: '))
#   → upper_limit = int(input('Enter the upper limit: '))
#   → random_number = random.randint(lower_limit, upper_limit)
#   → result = f'The random number between {lower_limit} and {upper_limit} is: {random_number}'
#   → return result
#   → lower_limit = int(input('Enter the lower limit: '))
#   → upper_limit = int(input('Enter the upper limit: '))
#   → random_number = random.randint(lower_limit, upper_limit)
#   → result = f'The random number between {lower_limit} and {upper_limit} is: {random_number}'
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only generate_random_number is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → generate_random_number()  # jumps into generate_random_number(), runs body, returns
#   → generate_random_number()  # jumps into generate_random_number(), runs body, returns
#   → generate_random_number()  # jumps into generate_random_number(), runs body, returns
#   → lower_limit = ...  # stored in memory
#   → upper_limit = ...  # stored in memory
#   → random_number = ...  # stored in memory
#   → print(?)
#   → lower_limit = ...  # stored in memory
#   → upper_limit = ...  # stored in memory
#   → random_number = ...  # stored in memory
#   → print(?)
"""
Problème 80 :
Écrivez un programme Python à générer un nombre aléatoire entre une donnée range. demander le utilisateur à saisir le lower et upper limits.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: + / < **
# Fonctions intégrées : float, input, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return num ** 0.5
#   → return num ** 0.5
#   → return num ** 0.5
#   → return num ** 0.5
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only square_root is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(square_root(...))  # square_root() runs first → value goes to print()
#   → square_root()  # jumps into square_root(), runs body, returns
#   → print(square_root(...))  # square_root() runs first → value goes to print()
#   → print(square_root(...))  # square_root() runs first → value goes to print()
#   → num = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → num = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#
# Loop: takes one item from range(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 81 :
Écrivez un programme Python à trouver le carré root de un nombre. demander le utilisateur à saisir un nombre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# Keywords: if/else
# Operators: * ** ==
# Fonctions intégrées : Circle, float, input()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → radius = float(input('type number: '))
#   → area = math.pi * radius ** 2
#   → result = area
#   → return result
#   → return math.pi * radius ** 2
# if ... → only one branch executes based on condition
#   → return math.pi * radius ** 2
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes Circle are defined — methods stored in memory
# def blocks are skipped at runtime — calculate_circle_area, circle, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → circle()  # jumps into circle(), runs body, returns
#   → calculate_circle_area()  # jumps into calculate_circle_area(), runs body, returns
#   → if condition  # evaluates → runs the True branch
#   → calculate_circle_area = ...  # stored in memory
#   → print(?)
#   → circle = ...  # stored in memory
#   → print(?)
#   → radius = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(calculate_circle_area(...))  # calculate_circle_area() runs first → value goes to print()
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 82 :
Écrivez un programme Python à trouver le area de un circle. demander le utilisateur à saisir le radius.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else | while
# Operators: - < != <= ==
# Fonctions intégrées : input, len()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# if ... → only one branch executes based on condition
#   → return s == s[::-1]
#   → return s == s[::-1]
#   → return s == s[::-1]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — is_palindrome, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → if condition  # evaluates → runs the True branch
#   → print(is_palindrome(...))  # is_palindrome() runs first → value goes to print()
#   → print(is_palindrome(...))  # is_palindrome() runs first → value goes to print()
#   → s = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_palindrome(...))  # is_palindrome() runs first → value goes to print()
#
# Loop: check condition → if True run body → check again
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 83 :
Écrivez un programme Python à vérifier si une donnée chaîne est un palindrome en utilisant un recursive fonction. demander le utilisateur à saisir une chaîne.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : set()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return alphabet.issubset(set(sentence.lower()))
#   → return alphabet.issubset(set(sentence.lower()))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — is_pangram, pangram are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(is_pangram(...))  # is_pangram() runs first → value goes to print()
#   → sentence = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_pangram(...))  # is_pangram() runs first → value goes to print()
"""
Problème 84 :
Écrivez un programme Python à vérifier si une chaîne est un pangram. un pangram est une phrase qui contient chaque lettre de le alphabet at moins once. demander le utilisateur à saisir une phrase.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else | while
# Operators: % != ==
# Fonctions intégrées : input, int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# if ... → only one branch executes based on condition
#   → return a
#   → return a
#   → return a
#   → return a
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — gcd, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → if condition  # evaluates → runs the True branch
#   → print(gcd(...))  # gcd() runs first → value goes to print()
#   → print(gcd(...))  # gcd() runs first → value goes to print()
#   → print(gcd(...))  # gcd() runs first → value goes to print()
#   → a = ...  # stored in memory
#   → b = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(gcd(...))  # gcd() runs first → value goes to print()
#
# Loop: check condition → if True run body → check again
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 85 :
Écrivez un programme Python à trouver le GCD (Greatest commun Divisor) des deux nombres. demander le utilisateur à saisir deux nombres.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else | while
# Operators: % * + != // ==
# Fonctions intégrées : abs, input, int, max, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# if ... → only one branch executes based on condition
#   → for i in range(max(a, b), a * b + 1, max(a, b)):
#   →     if i % b == 0:
#   →         return i
#   → for i in range(max(a, b), a * b + 1, max(a, b)):
#   →     if i % b == 0:
#   →         return i
#   → for i in range(max(a, b), a * b + 1, max(a, b)):
#   →     if i % b == 0:
#   →         return i
#   → return a
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — gcd, lcm, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → if condition  # evaluates → runs the True branch
#   → print(lcm(...))  # lcm() runs first → value goes to print()
#   → print(lcm(...))  # lcm() runs first → value goes to print()
#   → print(lcm(...))  # lcm() runs first → value goes to print()
#   → a = ...  # stored in memory
#   → b = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(gcd(...))  # gcd() runs first → value goes to print()
#
# Loop: check condition → if True run body → check again
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 86 :
Écrivez un programme Python à trouver le LCM (moins commun Multiple) des deux nombres. demander le utilisateur à saisir deux nombres.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: -
# Fonctions intégrées : deque, input, len, list, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return ' '.join(reversed_lst)
#   → from collections import deque
#   → d = deque(items)
#   → d.reverse()
#   → return list(d)
#   → from collections import deque
#   → d = deque(items)
#   → d.reverse()
#   → return list(d)
#   → from collections import deque
#   → d = deque(items)
#   → d.reverse()
#   → return list(d)
#   → from collections import deque
#   → d = deque(items)
#   → d.reverse()
#   → return list(d)
#   → from collections import deque
#   → d = deque(items)
#   → d.reverse()
#   → return list(d)
#   → from collections import deque
#   → d = deque(items)
#   → d.reverse()
#   → return list(d)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — reverse_list, reverse_lst are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(reverse_lst(...))  # reverse_lst() runs first → value goes to print()
#   → print(reverse_list(...))  # reverse_list() runs first → value goes to print()
#   → reverse_list()  # jumps into reverse_list(), runs body, returns
#   → lst = ...  # stored in memory
#   → print(reverse_list(...))  # reverse_list() runs first → value goes to print()
#   → print(reverse_list(...))  # reverse_list() runs first → value goes to print()
#   → print(reverse_list(...))  # reverse_list() runs first → value goes to print()
#   → items = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(reverse_list(...))  # reverse_list() runs first → value goes to print()
#
# Loop: takes one item from ?, runs body, repeats until done
"""
Problème 87 :
Écrivez un programme Python à reverse une liste sans en utilisant le reverse() fonction. demander le utilisateur à saisir une liste d'éléments.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else | while
# Operators: % + < > ** // ==
# Fonctions intégrées : input, int, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# if ... → only one branch executes based on condition
#   → return factors
#   → return factors
#   → return factors
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — main, prime_factors are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → if condition  # evaluates → runs the True branch
#   → print(prime_factors(...))  # prime_factors() runs first → value goes to print()
#   → print(prime_factors(...))  # prime_factors() runs first → value goes to print()
#   → n = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(prime_factors(...))  # prime_factors() runs first → value goes to print()
#
# Loop: check condition → if True run body → check again
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 88 :
Écrivez un programme Python à trouver le prime factors de un nombre. demander le utilisateur à saisir un nombre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: * +
# Fonctions intégrées : input, int, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return password
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only generate_password is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → length = ...  # stored in memory
#   → print('Generated password:', generate_password(...))
#   → print('Generated password:', generate_password(...))
#   → print('Generated password:', generate_password(...))
#   → length = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(generate_password(...))  # generate_password() runs first → value goes to print()
"""
Problème 89 :
Écrivez un programme Python à générer un aléatoire password de une donnée longueur. demander le utilisateur à saisir la longueur.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : len, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return count
#   → return count
#   → return count
#   → return count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_words is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → words = ...  # stored in memory
#   → print(count_words(...))  # count_words() runs first → value goes to print()
#   → print(count_words(...))  # count_words() runs first → value goes to print()
#   → print(count_words(...))  # count_words() runs first → value goes to print()
#   → sentence = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_words(...))  # count_words() runs first → value goes to print()
#
# Loop: takes one item from split_words, runs body, repeats until done
"""
Problème 90 :
Écrivez un programme Python à compter le nombre de mots dans une phrase. demander le utilisateur à saisir une phrase.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: < >
# Fonctions intégrées : max, min, reduce()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return (smallest, largest)
#   → return (smallest, largest)
#   → return (smallest, largest)
#   → return (smallest, largest)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only largest_smallest is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(largest_smallest(...))  # largest_smallest() runs first → value goes to print()
#   → print(largest_smallest(...))  # largest_smallest() runs first → value goes to print()
#   → print(largest_smallest(...))  # largest_smallest() runs first → value goes to print()
#   → elements = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(largest_smallest(...))  # largest_smallest() runs first → value goes to print()
#
# Loop: takes one item from elements, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 91 :
Écrivez un programme Python à trouver le plus grand et plus petit éléments dans une liste. demander le utilisateur à saisir une liste de nombres sans en utilisant trié()."
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: % + ** // <= ==
# Fonctions intégrées : input, int, range, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return False
# if ... → only one branch executes based on condition
#   → if n <= 1:
#   →     return False
#   → divisors = {1}
#   → for i in range(2, int(n ** 0.5) + 1):
#   →     if n % i == 0:
#   →         divisors.add(i)
#   →         divisors.add(n // i)
#   → return n == sum(divisors)
#   → if n <= 1:
#   →     return False
#   → divisors = {1}
#   → for i in range(2, int(n ** 0.5) + 1):
#   →     if n % i == 0:
#   →         divisors.add(i)
#   →         divisors.add(n // i)
#   → return n == sum(divisors)
#   → if n <= 1:
#   →     return False
#   → divisors = {1}
#   → for i in range(2, int(n ** 0.5) + 1):
#   →     if n % i == 0:
#   →         divisors.add(i)
#   →         divisors.add(n // i)
#   → return n == sum(divisors)
#   → if n <= 1:
#   →     return False
#   → divisors = {1}
#   → for i in range(2, int(n ** 0.5) + 1):
#   →     if n % i == 0:
#   →         divisors.add(i)
#   →         divisors.add(n // i)
#   → return n == sum(divisors)
#   → return False
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — is_perfect_number, is_perfect_square, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → is_perfect_square(6)  # jumps into is_perfect_square(), runs body, returns
#   → if condition  # evaluates → runs the True branch
#   → print(is_perfect_number(...))  # is_perfect_number() runs first → value goes to print()
#   → print(is_perfect_number(...))  # is_perfect_number() runs first → value goes to print()
#   → print(is_perfect_number(...))  # is_perfect_number() runs first → value goes to print()
#   → print(is_perfect_number(...))  # is_perfect_number() runs first → value goes to print()
#   → num = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_perfect_square(...))  # is_perfect_square() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 92 :
Écrivez un programme Python à vérifier si un nombre est un nombre parfait. un nombre parfait est un positif integer qui est equal à le somme de ses proper divisors. demander le utilisateur à saisir un nombre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: * + - <=
# Fonctions intégrées : input, int, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → user = int(input('type number: '))
#   → result = 1
#   → for number in range(1, user + 1):
#   →     result *= number
#   → result = result
#   → return result
#   → user = int(input('type number: '))
#   → result = 1
#   → for number in range(1, user + 1):
#   →     result *= number
#   → result = result
#   → return result
#   → user = int(input('type number: '))
#   → result = 1
#   → for number in range(1, user + 1):
#   →     result *= number
#   → result = result
#   → return result
#   → user = int(input('type number: '))
#   → result = 1
#   → for number in range(1, user + 1):
#   →     result *= number
#   → result = result
#   → return result
#   → user = int(input('type number: '))
#   → result = 1
#   → for number in range(1, user + 1):
#   →     result *= number
#   → result = result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only factorial is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → factorial()  # jumps into factorial(), runs body, returns
#   → print(factorial(...))  # factorial() runs first → value goes to print()
#   → factorial()  # jumps into factorial(), runs body, returns
#   → n = ...  # stored in memory
#   → print(factorial(...))  # factorial() runs first → value goes to print()
#   → n = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(factorial(...))  # factorial() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 93 :
Écrivez un programme Python à trouver la factorielle de un nombre en utilisant une boucle. demander le utilisateur à saisir un nombre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else | while
# Operators: % & - > != // <= == and
# Fonctions intégrées : input, int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# if ... → only one branch executes based on condition
#   → return False
#   → return False
#   → return False
#   → return False
#   → return False
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only is_power_of_two is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → number = ...  # stored in memory
#   → if condition  # evaluates → runs the True branch
#   → print(is_power_of_two(...))  # is_power_of_two() runs first → value goes to print()
#   → print(is_power_of_two(...))  # is_power_of_two() runs first → value goes to print()
#   → print(is_power_of_two(...))  # is_power_of_two() runs first → value goes to print()
#   → print(is_power_of_two(...))  # is_power_of_two() runs first → value goes to print()
#   → number = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_power_of_two(...))  # is_power_of_two() runs first → value goes to print()
#
# Loop: check condition → if True run body → check again
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 94 :
Écrivez un programme Python à vérifier si une donnée nombre est un power des deux.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: & in
# Fonctions intégrées : filter, input, list, set()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → list1 = get_list('Enter the first list of elements, separated by spaces: ')
#   → list2 = get_list('Enter the second list of elements, separated by spaces: ')
#   → intersection = find_intersection(list1, list2)
#   → print(f'The intersection of the two lists is: {intersection}')
#   → return list(filter(lambda x: x in list2, list1))
#   → return list(filter(lambda x: x in list2, list1))
#   → return list(filter(lambda x: x in list2, list1))
#   → return input(prompt).split()
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — find_intersection, get_list, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → main()  # jumps into main(), runs body, returns
#   → print(find_intersection(...))  # find_intersection() runs first → value goes to print()
#   → print(find_intersection(...))  # find_intersection() runs first → value goes to print()
#   → print(find_intersection(...))  # find_intersection() runs first → value goes to print()
#   → prompt = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(get_list(...))  # get_list() runs first → value goes to print()
"""
Problème 95 :
Écrivez un programme Python à trouver le l'intersection des deux listes. demander le utilisateur à saisir deux listes.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: * - ** == in
# Fonctions intégrées : all, enumerate, input, int, len, reversed, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# if ... → only one branch executes based on condition
#   → return decimal
#   → return decimal
#   → return decimal
#   → return decimal
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — binary_to_decimal, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → if condition  # evaluates → runs the True branch
#   → print(binary_to_decimal(...))  # binary_to_decimal() runs first → value goes to print()
#   → print(binary_to_decimal(...))  # binary_to_decimal() runs first → value goes to print()
#   → print(binary_to_decimal(...))  # binary_to_decimal() runs first → value goes to print()
#   → binary = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(binary_to_decimal(...))  # binary_to_decimal() runs first → value goes to print()
#
# Loop: takes one item from binary, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 97 :
Écrivez un programme Python à convert un binary nombre à decimal. demander le utilisateur à saisir un binary nombre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : input, int, map, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → user = input('Type numbers separated by spaces: ').split()
#   → total = 0
#   → for number in user:
#   →     total += int(number)
#   → result = total
#   → return result
#   → user = input('Type numbers separated by spaces: ').split()
#   → total = 0
#   → for number in user:
#   →     total += int(number)
#   → result = total
#   → return result
#   → user = input('Type numbers separated by spaces: ').split()
#   → total = 0
#   → for number in user:
#   →     total += int(number)
#   → result = total
#   → return result
#   → user = input('Type numbers separated by spaces: ').split()
#   → total = 0
#   → for number in user:
#   →     total += int(number)
#   → result = total
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only digits_string is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → digits_string()  # jumps into digits_string(), runs body, returns
#   → digits_string()  # jumps into digits_string(), runs body, returns
#   → digits_string()  # jumps into digits_string(), runs body, returns
#   → digits_string()  # jumps into digits_string(), runs body, returns
#   → user = ...  # stored in memory
#   → total = ...  # stored in memory
#   → for number in user  # runs body once per item
#   → print(total)
#   → user = ...  # stored in memory
#   → total = ...  # stored in memory
#   → for number in user  # runs body once per item
#   → print(total)
#
# Loop: takes one item from user, runs body, repeats until done
"""
Problème 98 :
Écrivez un programme Python à trouver le somme de les chiffres dans une chaîne. demander le utilisateur à saisir une chaîne contenant séparés nombres. par exemple "2", "8" devrait retourner 10
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: %
# Fonctions intégrées : len, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return 'lower = %s and upper = %s' % (count_lower, count_upper)
#   → return 'lower = %s and upper = %s' % (count_lower, count_upper)
#   → return 'lower = %s and upper = %s' % (count_lower, count_upper)
#   → return 'lower = %s and upper = %s' % (count_lower, count_upper)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only upper_lower is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → string = ...  # stored in memory
#   → print(upper_lower(...))  # upper_lower() runs first → value goes to print()
#   → print(upper_lower(...))  # upper_lower() runs first → value goes to print()
#   → print(upper_lower(...))  # upper_lower() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(upper_lower(...))  # upper_lower() runs first → value goes to print()
#
# Loop: takes one item from string, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 99 :
Écrivez un programme Python à compter le nombre de uppercase et lowercase lettre dans une chaîne. demander le utilisateur à saisir une chaîne.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: % * + > != ** <= == and
# Fonctions intégrées : all, input, int, range, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# if ... → only one branch executes based on condition
#   → sieve = [True] * (upper + 1)
#   → sieve[0] = sieve[1] = False
#   → for i in range(2, int(upper ** 0.5) + 1):
#   →     if sieve[i]:
#   →         for j in range(i * i, upper + 1, i):
#   →             sieve[j] = False
#   → return sum((i for i in range(lower, upper + 1) if sieve[i]))
#   → sieve = [True] * (upper + 1)
#   → sieve[0] = sieve[1] = False
#   → for i in range(2, int(upper ** 0.5) + 1):
#   →     if sieve[i]:
#   →         for j in range(i * i, upper + 1, i):
#   →             sieve[j] = False
#   → return sum((i for i in range(lower, upper + 1) if sieve[i]))
#   → return False
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — is_prime, main, sum_of_primes are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → if condition  # evaluates → runs the True branch
#   → print(sum_of_primes(...))  # sum_of_primes() runs first → value goes to print()
#   → print(sum_of_primes(...))  # sum_of_primes() runs first → value goes to print()
#   → num = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_prime(...))  # is_prime() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 100 :
Écrivez un programme Python à trouver le somme de tous prime nombres dans une donnée range. demander le utilisateur à saisir le lower et upper limits.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: * - ** ==
# Fonctions intégrées : float, input, int, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return 1
#   → return 1
#   → return 1
#   → return 1
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only power is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → base = ...  # stored in memory
#   → exp = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(?)
#   → print(power(...))  # power() runs first → value goes to print()
#   → print(power(...))  # power() runs first → value goes to print()
#   → print(power(...))  # power() runs first → value goes to print()
#   → base = ...  # stored in memory
#   → exp = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(power(...))  # power() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 101 :
Écrivez un programme Python à calculate le power de un nombre en utilisant recursion. demander le utilisateur à saisir un base nombre et an exponent.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: != ==
# Fonctions intégrées : Counter, input, len, set, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → s1, s2 = (string1.replace(' ', '').lower(), string2.replace(' ', '').lower())
#   → if len(s1) != len(s2):
#   →     return False
#   → for char in set(s1):
#   →     if s1.count(char) != s2.count(char):
#   →         return False
#   → return True
#   → s1, s2 = (string1.replace(' ', '').lower(), string2.replace(' ', '').lower())
#   → if len(s1) != len(s2):
#   →     return False
#   → for char in set(s1):
#   →     if s1.count(char) != s2.count(char):
#   →         return False
#   → return True
#   → s1, s2 = (string1.replace(' ', '').lower(), string2.replace(' ', '').lower())
#   → if len(s1) != len(s2):
#   →     return False
#   → for char in set(s1):
#   →     if s1.count(char) != s2.count(char):
#   →         return False
#   → return True
#   → s1, s2 = (string1.replace(' ', '').lower(), string2.replace(' ', '').lower())
#   → if len(s1) != len(s2):
#   →     return False
#   → for char in set(s1):
#   →     if s1.count(char) != s2.count(char):
#   →         return False
#   → return True
#   → s1, s2 = (string1.replace(' ', '').lower(), string2.replace(' ', '').lower())
#   → if len(s1) != len(s2):
#   →     return False
#   → for char in set(s1):
#   →     if s1.count(char) != s2.count(char):
#   →         return False
#   → return True
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only is_anagram is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → is_anagram()  # jumps into is_anagram(), runs body, returns
#   → string1 = ...  # stored in memory
#   → string2 = ...  # stored in memory
#   → print(is_anagram(...))  # is_anagram() runs first → value goes to print()
#   → print(is_anagram(...))  # is_anagram() runs first → value goes to print()
#   → print(is_anagram(...))  # is_anagram() runs first → value goes to print()
#   → string1 = ...  # stored in memory
#   → string2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_anagram(...))  # is_anagram() runs first → value goes to print()
#
# Loop: takes one item from set(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 102 :
Écrivez un programme Python à vérifier si une chaîne est an un anagramme de un autre chaîne, ignoring les espaces. demander le utilisateur à saisir deux strings.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else
# Operators: * < ** ==
# Fonctions intégrées : input, int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# if ... → only one branch executes based on condition
#   → return root * root == num
#   → return root * root == num
#   → return root * root == num
#   → return root * root == num
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only is_perfect_square is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → user = ...  # stored in memory
#   → root = ...  # stored in memory
#   → print(?)
#   → num = ...  # stored in memory
#   → if condition  # evaluates → runs the True branch
#   → print(is_perfect_square(...))  # is_perfect_square() runs first → value goes to print()
#   → print(is_perfect_square(...))  # is_perfect_square() runs first → value goes to print()
#   → print(is_perfect_square(...))  # is_perfect_square() runs first → value goes to print()
#   → num = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_perfect_square(...))  # is_perfect_square() runs first → value goes to print()
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 104 :
Écrivez un programme Python à vérifier si un nombre est un perfect carré. demander le utilisateur à saisir un nombre"
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: % !=
# Fonctions intégrées : filter, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return count
#   → return count
#   → return count
#   → return count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only all_odd_numbers is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(all_odd_numbers(...))  # all_odd_numbers() runs first → value goes to print()
#   → print(all_odd_numbers(...))  # all_odd_numbers() runs first → value goes to print()
#   → print(all_odd_numbers(...))  # all_odd_numbers() runs first → value goes to print()
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(all_odd_numbers(...))  # all_odd_numbers() runs first → value goes to print()
#
# Loop: takes one item from numbers, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 105 :
Écrivez un programme Python à trouver le somme de tous les nombres impairs dans une liste. demander le utilisateur à saisir une liste de nombres.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: % !=
# Fonctions intégrées : filter, input, int, list, map, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → user_input = input('Enter a list of numbers separated by spaces: ')
#   → split_numbers = user_input.split()
#   → int_numbers = []
#   → for num in split_numbers:
#   →     int_numbers.append(int(num))
#   → odd_sum = 0
#   → for num in int_numbers:
#   →     if num % 2 != 0:
#   →         odd_sum += num
#   → result = ('The sum of all odd numbers is:', odd_sum)
#   → return result
#   → numbers = list(map(int, input('Enter numbers: ').split()))
#   → print(sum(filter(lambda x: x % 2 != 0, numbers)))
#   → user_input = input('Enter a list of numbers separated by spaces: ')
#   → split_numbers = user_input.split()
#   → int_numbers = []
#   → for num in split_numbers:
#   →     int_numbers.append(int(num))
#   → odd_sum = 0
#   → for num in int_numbers:
#   →     if num % 2 != 0:
#   →         odd_sum += num
#   → result = ('The sum of all odd numbers is:', odd_sum)
#   → return result
#   → numbers = list(map(int, input('Enter numbers: ').split()))
#   → print(sum(filter(lambda x: x % 2 != 0, numbers)))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — sum_of_all_odd, sum_of_odd_numbers are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → sum_of_odd_numbers()  # jumps into sum_of_odd_numbers(), runs body, returns
#   → sum_of_all_odd()  # jumps into sum_of_all_odd(), runs body, returns
#   → sum_of_odd_numbers()  # jumps into sum_of_odd_numbers(), runs body, returns
#   → sum_of_all_odd()  # jumps into sum_of_all_odd(), runs body, returns
#   → user_input = ...  # stored in memory
#   → split_numbers = ...  # stored in memory
#   → int_numbers = ...  # stored in memory
#   → for num in split_numbers  # runs body once per item
#   → odd_sum = ...  # stored in memory
#   → for num in int_numbers  # runs body once per item
#   → print('The sum of all odd numbers is:', odd_sum)
#   → user_input = ...  # stored in memory
#   → split_numbers = ...  # stored in memory
#   → int_numbers = ...  # stored in memory
#   → for num in split_numbers  # runs body once per item
#   → odd_sum = ...  # stored in memory
#   → for num in int_numbers  # runs body once per item
#   → print('The sum of all odd numbers is:', odd_sum)
#
# Loop: takes one item from split_numbers, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 106 :
Écrivez un programme Python à trouver le somme de tous les nombres impairs dans une liste. demander le utilisateur à saisir une liste de nombres.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: & != in and not in
# Fonctions intégrées : input, len, list, map, set()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(lambda char: char, str1))
#   → return list(map(lambda char: char, str1))
#   → return list(map(lambda char: char, str1))
#   → return list(map(lambda char: char, str1))
#   → return list(map(lambda char: char, str1))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only common_char is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(common_char(...))  # common_char() runs first → value goes to print()
#   → name1 = ...  # stored in memory
#   → name2 = ...  # stored in memory
#   → print(common_char(...))  # common_char() runs first → value goes to print()
#   → print(common_char(...))  # common_char() runs first → value goes to print()
#   → print(common_char(...))  # common_char() runs first → value goes to print()
#   → string1 = ...  # stored in memory
#   → string2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(common_char(...))  # common_char() runs first → value goes to print()
#
# Loop: takes one item from str1, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 107 :
Écrivez un programme Python à trouver le commun caractères entre deux strings. demander le utilisateur à saisir deux strings.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: in or not in
# Fonctions intégrées : input, set()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → user = input('type string: ')
#   → unique_user = set()
#   → for char in user:
#   →     if char not in unique_user:
#   →         unique_user.add(char)
#   → result = ''.join(unique_user)
#   → return result
#   → user = input('type string: ')
#   → unique_user = set()
#   → for char in user:
#   →     if char not in unique_user:
#   →         unique_user.add(char)
#   → result = ''.join(unique_user)
#   → return result
#   → user = input('type string: ')
#   → unique_user = set()
#   → for char in user:
#   →     if char not in unique_user:
#   →         unique_user.add(char)
#   → result = ''.join(unique_user)
#   → return result
#   → user = input('type string: ')
#   → unique_user = set()
#   → for char in user:
#   →     if char not in unique_user:
#   →         unique_user.add(char)
#   → result = ''.join(unique_user)
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only remove_duplicates is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → remove_duplicates()  # jumps into remove_duplicates(), runs body, returns
#   → remove_duplicates()  # jumps into remove_duplicates(), runs body, returns
#   → remove_duplicates()  # jumps into remove_duplicates(), runs body, returns
#   → remove_duplicates()  # jumps into remove_duplicates(), runs body, returns
#   → user = ...  # stored in memory
#   → unique_user = ...  # stored in memory
#   → for char in user  # runs body once per item
#   → print(''.join(...))
#   → user = ...  # stored in memory
#   → unique_user = ...  # stored in memory
#   → for char in user  # runs body once per item
#   → print(''.join(...))
#
# Loop: takes one item from user, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 108 :
Écrivez un programme Python à remove les doublons de une chaîne en utilisant set(). demander le utilisateur à saisir une chaîne
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else | while
# Operators: % > ** ==
# Fonctions intégrées : input, int, len, str, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# if ... → only one branch executes based on condition
#   → return total == number
#   → return total == number
#   → return total == number
#   → return total == number
#   → return total == number
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only is_armstrong is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → number = ...  # stored in memory
#   → if condition  # evaluates → runs the True branch
#   → print(number)
#   → print(is_armstrong(...))  # is_armstrong() runs first → value goes to print()
#   → print(is_armstrong(...))  # is_armstrong() runs first → value goes to print()
#   → print(is_armstrong(...))  # is_armstrong() runs first → value goes to print()
#   → print(is_armstrong(...))  # is_armstrong() runs first → value goes to print()
#   → number = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_armstrong(...))  # is_armstrong() runs first → value goes to print()
#
# Loop: takes one item from str(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 109 :
Écrivez un programme Python à vérifier si un nombre est an un nombre d'Armstrong. An un nombre d'Armstrong est un nombre qui est equal à le somme de ses own les chiffres, chaque raised à le power de le nombre de les chiffres. demander le utilisateur à saisir un nombre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: < >=
# Fonctions intégrées : input, int, len, max, min, set, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sorted_numbers[1]
#   → return sorted_numbers[1]
#   → return sorted_numbers[1]
#   → return sorted_numbers[1]
#   → return sorted_numbers[1]
#   → return sorted_numbers[1]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only second_smallest_element is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(second_smallest_element(...))  # second_smallest_element() runs first → value goes to print()
#   → arg = ...  # stored in memory
#   → print(second_smallest_element(...))  # second_smallest_element() runs first → value goes to print()
#   → print(second_smallest_element(...))  # second_smallest_element() runs first → value goes to print()
#   → print(second_smallest_element(...))  # second_smallest_element() runs first → value goes to print()
#   → print(second_smallest_element(...))  # second_smallest_element() runs first → value goes to print()
#   → elements = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(second_smallest_element(...))  # second_smallest_element() runs first → value goes to print()
#
# Loop: takes one item from user_input.split(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 111 :
Écrivez un programme Python à trouver le deuxième plus petit élément dans une liste.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: +
# Fonctions intégrées : backtrack, input, len, list, permutations, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only generate_permutations is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print('Permutations:', result)
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(list(...))
#   → print(generate_permutations(...))  # generate_permutations() runs first → value goes to print()
#   → print(generate_permutations(...))  # generate_permutations() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(generate_permutations(...))  # generate_permutations() runs first → value goes to print()
#
# Loop: takes one item from permutations(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 112 :
Écrivez un programme Python à générer tous possible permutations de une donnée chaîne.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: > >= and
# Fonctions intégrées : max, reduce, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return largest
#   → return max(a, b, c)
#   → return largest
#   → return largest
#   → return largest
#   → return largest
#   → return largest
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — main, max_of_three are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → max_of_three(lst)  # jumps into max_of_three(), runs body, returns
#   → main(56, 8, 445)  # jumps into main(), runs body, returns
#   → max_of_three()  # jumps into max_of_three(), runs body, returns
#   → print(max_of_three(...))  # max_of_three() runs first → value goes to print()
#   → print(max_of_three(...))  # max_of_three() runs first → value goes to print()
#   → print(max_of_three(...))  # max_of_three() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(max_of_three(...))  # max_of_three() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 114 :
description": "Define une fonction max_of_three() qui prend trois nombres as arguments et retourne le plus grand de them.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: + ==
# Fonctions intégrées : enumerate, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return count
#   → count = 0
#   → for char in string:
#   →     count += 1
#   → return count
#   → return count
#   → return count
#   → return count
#   → return count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — length_list, length_string are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → name = ...  # stored in memory
#   → print(length_string(...))  # length_string() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → print(length_list(...))  # length_list() runs first → value goes to print()
#   → print(length_string(...))  # length_string() runs first → value goes to print()
#   → print(length_string(...))  # length_string() runs first → value goes to print()
#   → print(length_string(...))  # length_string() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(length_string(...))  # length_string() runs first → value goes to print()
#
# Loop: takes one item from string, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 115 :
Définissez une fonction qui calcule la longueur de une donnée list ou chaîne. (C'est vrai qui Python une len() fonction construit dans, but writing it yourself est nevertheless un good exercise.)
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: + and not in
# Fonctions intégrées : input, set()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return translated
#   → return translated
#   → return translated
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only translate is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → text = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(translate(...))  # translate() runs first → value goes to print()
#   → print(translate(...))  # translate() runs first → value goes to print()
#   → text = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(translate(...))  # translate() runs first → value goes to print()
#
# Loop: takes one item from text, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 117 :
Écrivez une fonction translate() qui va translate un text dans'rövarspråket''(suédois pour'robber's language''). C'est, double chaque consonne et place an occurrence de'o''dans entre. par exemple, translate('cette est fun'') devrait retourner la chaîne'tothohisos isos fofunon'.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: * +
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return total
#   → from functools import reduce
#   → return reduce(lambda x, y: x * y, numbers)
#   → return total
#   → from functools import reduce
#   → return reduce(lambda x, y: x * y, numbers)
#   → return total
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — multiply, sum are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → print('Sum:', sum(...))
#   → print('Multiply:', multiply(...))
#   → print(sum(...))  # sum() runs first → value goes to print()
#   → print(multiply(...))  # multiply() runs first → value goes to print()
#   → print(sum(...))  # sum() runs first → value goes to print()
#   → print(multiply(...))  # multiply() runs first → value goes to print()
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sum(...))  # sum() runs first → value goes to print()
#
# Loop: takes one item from numbers, runs body, repeats until done
"""
Problème 118 :
Définissez une fonction calculate_sum() et une fonction multiply() qui sums et multiplie (respectively) tous le nombres dans une liste de nombres. par exemple, calculate_sum([1, 2, 3, 4]) devrait retourner 10, et multiply([1, 2, 3, 4]) devrait retourner 24.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: + <=
# Fonctions intégrées : input, len, reversed()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return reversed_string
#   → return reversed_string
#   → return reversed_string
#   → return reversed_string
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only reverse is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(reverse(...))  # reverse() runs first → value goes to print()
#   → print(reverse(...))  # reverse() runs first → value goes to print()
#   → print(reverse(...))  # reverse() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(reverse(...))  # reverse() runs first → value goes to print()
#
# Loop: takes one item from string, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 119 :
Définissez une fonction reverse() qui calcule le reversal de une chaîne. par exemple, reverse('I am testing'') devrait retourner la chaîne'gnitset ma I'.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else | while
# Operators: + - < != // ==
# Fonctions intégrées : all, len, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return True
#   → return all((string[i] == string[-(i + 1)] for i in range(len(string) // 2)))
#   → return all((string[i] == string[-(i + 1)] for i in range(len(string) // 2)))
#   → return all((string[i] == string[-(i + 1)] for i in range(len(string) // 2)))
#   → return all((string[i] == string[-(i + 1)] for i in range(len(string) // 2)))
#   → return True
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — is_palindrome, palindromes are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → string = ...  # stored in memory
#   → print(palindromes(...))  # palindromes() runs first → value goes to print()
#   → print(is_palindrome(...))  # is_palindrome() runs first → value goes to print()
#   → print(is_palindrome(...))  # is_palindrome() runs first → value goes to print()
#   → print(is_palindrome(...))  # is_palindrome() runs first → value goes to print()
#   → print(is_palindrome(...))  # is_palindrome() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(palindromes(...))  # palindromes() runs first → value goes to print()
#
# Loop: takes one item from string, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 120 :
Définissez une fonction is_palindrome() qui recognizes palindromes (c'est-à-dire. words qui look le même written backwards). par exemple, is_palindrome('radar') devrait retourner vrai.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else | while
# Operators: - < != ==
# Fonctions intégrées : len, reversed()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return True
#   → return True
#   → return True
#   → return True
#   → return True
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only is_palindrome is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → name = ...  # stored in memory
#   → print(is_palindrome(...))  # is_palindrome() runs first → value goes to print()
#   → print(is_palindrome(...))  # is_palindrome() runs first → value goes to print()
#   → print(is_palindrome(...))  # is_palindrome() runs first → value goes to print()
#   → print(is_palindrome(...))  # is_palindrome() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_palindrome(...))  # is_palindrome() runs first → value goes to print()
#
# Loop: check condition → if True run body → check again
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 121 :
Définissez une fonction is_palindrome() qui recognizes palindromes (c'est-à-dire. words qui look le même written backwards). par exemple, is_palindrome('radar') devrait retourner vrai.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: == in or
# Fonctions intégrées : any, input()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return any((element == x for element in lst))
#   → return any((element == x for element in lst))
#   → return any((element == x for element in lst))
#   → return any((element == x for element in lst))
#   → return any((element == x for element in lst))
#   → return any((element == x for element in lst))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only is_member is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → x = ...  # stored in memory
#   → print(is_member(...))  # is_member() runs first → value goes to print()
#   → x = ...  # stored in memory
#   → a = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_member(...))  # is_member() runs first → value goes to print()
#   → print(is_member(...))  # is_member() runs first → value goes to print()
#   → print(is_member(...))  # is_member() runs first → value goes to print()
#   → print(is_member(...))  # is_member() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → x = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_member(...))  # is_member() runs first → value goes to print()
#
# Loop: takes one item from a, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 122 :
Écrivez une fonction is_member() qui prend une valeur (c'est-à-dire. un nombre, chaîne, etc.) x et une liste de valeurs, et retourne vrai si x est un member de a, False otherwise. (Note qui cette est exactly quoi le dans operator fait, but pour le sake de le exercise you devrait pretend Python did pas ont cette operator.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: & == in
# Fonctions intégrées : any, bool, set()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return True
#   → return True
#   → return True
#   → return True
#   → return True
#   → return True
#   → return True
#   → return True
#   → return True
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — is_member, overlapping are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → list1 = ...  # stored in memory
#   → list2 = ...  # stored in memory
#   → print(overlapping(...))  # overlapping() runs first → value goes to print()
#   → list1 = ...  # stored in memory
#   → list2 = ...  # stored in memory
#   → print(overlapping(...))  # overlapping() runs first → value goes to print()
#   → list1 = ...  # stored in memory
#   → list2 = ...  # stored in memory
#   → print(overlapping(...))  # overlapping() runs first → value goes to print()
#   → list1 = ...  # stored in memory
#   → list2 = ...  # stored in memory
#   → print(overlapping(...))  # overlapping() runs first → value goes to print()
#   → print(overlapping(...))  # overlapping() runs first → value goes to print()
#   → print(overlapping(...))  # overlapping() runs first → value goes to print()
#   → print(overlapping(...))  # overlapping() runs first → value goes to print()
#   → print(overlapping(...))  # overlapping() runs first → value goes to print()
#   → list1 = ...  # stored in memory
#   → list2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(overlapping(...))  # overlapping() runs first → value goes to print()
#
# Loop: takes one item from list1, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 123 :
Définissez une fonction overlapping() qui prend deux listes et retourne vrai si they ont at moins l'une member dans commun, False otherwise. You peut Utilisez your is_member() fonction, ou le dans operator, but pour le sake de le exercise, you devrait (aussi) write it en utilisant deux imbriqué forloops.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: & > == in
# Fonctions intégrées : any, len, set()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return True
#   → return True
#   → return True
#   → return True
#   → return True
#   → return True
#   → return True
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only overlapping is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → print(overlapping(...))  # overlapping() runs first → value goes to print()
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → print(overlapping(...))  # overlapping() runs first → value goes to print()
#   → print(overlapping(...))  # overlapping() runs first → value goes to print()
#   → print(overlapping(...))  # overlapping() runs first → value goes to print()
#   → print(overlapping(...))  # overlapping() runs first → value goes to print()
#   → print(overlapping(...))  # overlapping() runs first → value goes to print()
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(overlapping(...))  # overlapping() runs first → value goes to print()
#
# Loop: takes one item from lst1, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 124 :
Définissez une fonction overlapping() qui prend deux listes et retourne vrai si they ont at moins l'une member dans commun, False otherwise. You peut Utilisez your is_member() fonction, ou le dans operator, but pour le sake de le exercise, you devrait (aussi) write it en utilisant deux imbriqué forloops.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : len, list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return lengths
#   → return lengths
#   → return lengths
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only map_words_to_lengths is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → words = ...  # stored in memory
#   → lengths = ...  # stored in memory
#   → print(lengths)
#   → print(map_words_to_lengths(...))  # map_words_to_lengths() runs first → value goes to print()
#   → print(map_words_to_lengths(...))  # map_words_to_lengths() runs first → value goes to print()
#   → words = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(map_words_to_lengths(...))  # map_words_to_lengths() runs first → value goes to print()
#
# Loop: takes one item from words, runs body, repeats until done
"""
Problème 126 :
Écrivez un programme qui maps une liste de mots dans une liste d'entiers representing le lengths de le correponding words.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: >
# Fonctions intégrées : len, max, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sum((1 for _ in element))
#   → return sum((1 for _ in element))
#   → return sum((1 for _ in element))
#   → return sum((1 for _ in element))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only find_longest_word is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(find_longest_word(...))  # find_longest_word() runs first → value goes to print()
#   → print(find_longest_word(...))  # find_longest_word() runs first → value goes to print()
#   → print(find_longest_word(...))  # find_longest_word() runs first → value goes to print()
#   → elements = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(find_longest_word(...))  # find_longest_word() runs first → value goes to print()
#
# Loop: takes one item from elements, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 127 :
Écrivez une fonction find_longest_word() qui prend une liste de mots et retourne la longueur de le plus long l'une.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: >
# Fonctions intégrées : filter, len, list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(lambda word: word, lst))
#   → return list(map(lambda word: word, lst))
#   → return list(map(lambda word: word, lst))
#   → return list(map(lambda word: word, lst))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only filter_long_words is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → n = ...  # stored in memory
#   → print(filter_long_words(...))  # filter_long_words() runs first → value goes to print()
#   → print(filter_long_words(...))  # filter_long_words() runs first → value goes to print()
#   → print(filter_long_words(...))  # filter_long_words() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → n = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(filter_long_words(...))  # filter_long_words() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 128 :
Écrivez une fonction filter_long_words() qui prend une liste de mots et un entier n et retourne la liste de mots qui sont longer que n.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: in not in
# Fonctions intégrées : all, input, set()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return False
#   → return False
#   → return False
#   → return False
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only is_pangram is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → sentence = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_pangram(...))  # is_pangram() runs first → value goes to print()
#   → print(is_pangram(...))  # is_pangram() runs first → value goes to print()
#   → print(is_pangram(...))  # is_pangram() runs first → value goes to print()
#   → sentence = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_pangram(...))  # is_pangram() runs first → value goes to print()
#
# Loop: takes one item from alphabet, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 129 :
un pangram est une phrase qui contient tous le lettre de le anglais alphabet at moins once, par exemple: Le quick brown fox jumps over le lazy dog. Your task here est à write une fonction à check une phrase à see si c'est une pangram ou pas.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : input()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return text
#   → return text
#   → return text
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only correct is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → text = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(correct(...))  # correct() runs first → value goes to print()
#   → print(correct(...))  # correct() runs first → value goes to print()
#   → text = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(correct(...))  # correct() runs first → value goes to print()
"""
Problème 130 :
Define un simple'spelling correction'fonction correct() qui prend une chaîne et sees à it qui 1) deux ou plus occurrences de le space caractère est compressed dans l'une, et 2) inserts an extra space après un period si le period est directly followed by une lettre. E.g. correct('This est très funny et cool.Indeed!'') devrait retourner'This est très funny et cool. Indeed!''Tip: Utilisez regular expressions!
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else
# Operators: >
# Fonctions intégrées : max, reduce()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return max(numbers)
#   → return max(numbers)
#   → return max(numbers)
#   → return a
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — max_func, max_in_list are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → print(max_in_list(...))  # max_in_list() runs first → value goes to print()
#   → print(max_in_list(...))  # max_in_list() runs first → value goes to print()
#   → print(max_in_list(...))  # max_in_list() runs first → value goes to print()
#   → a = ...  # stored in memory
#   → b = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(max_func(...))  # max_func() runs first → value goes to print()
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 131 :
en utilisant le higher order fonction reduce(), write une fonction max_in_list() qui prend une liste de nombres et retourne le maximum en utilisant reduce().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : input, int, list, map, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → user_input = input('Enter a list of numbers separated by spaces: ')
#   → split_numbers = user_input.split()
#   → int_numbers = []
#   → for num in split_numbers:
#   →     int_numbers.append(int(num))
#   → total_sum = sum(int_numbers)
#   → result = total_sum
#   → return result
#   → user_input = input('Enter a list of numbers separated by spaces: ')
#   → split_numbers = user_input.split()
#   → int_numbers = []
#   → for num in split_numbers:
#   →     int_numbers.append(int(num))
#   → total_sum = sum(int_numbers)
#   → result = total_sum
#   → return result
#   → user_input = input('Enter a list of numbers separated by spaces: ')
#   → split_numbers = user_input.split()
#   → int_numbers = []
#   → for num in split_numbers:
#   →     int_numbers.append(int(num))
#   → total_sum = sum(int_numbers)
#   → result = total_sum
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sum_of_all_numbers is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → sum_of_all_numbers()  # jumps into sum_of_all_numbers(), runs body, returns
#   → sum_of_all_numbers()  # jumps into sum_of_all_numbers(), runs body, returns
#   → sum_of_all_numbers()  # jumps into sum_of_all_numbers(), runs body, returns
#   → user_input = ...  # stored in memory
#   → split_numbers = ...  # stored in memory
#   → int_numbers = ...  # stored in memory
#   → for num in split_numbers  # runs body once per item
#   → total_sum = ...  # stored in memory
#   → print(total_sum)
#   → user_input = ...  # stored in memory
#   → split_numbers = ...  # stored in memory
#   → int_numbers = ...  # stored in memory
#   → for num in split_numbers  # runs body once per item
#   → total_sum = ...  # stored in memory
#   → print(total_sum)
#
# Loop: takes one item from split_numbers, runs body, repeats until done
"""
Problème 134 :
Écrivez un programme Python à trouver le somme de tous nombres dans une liste. demander le utilisateur à saisir une liste de nombres dans un entrée fonction
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(lambda number: number, numbers))
#   → return list(map(lambda number: number, numbers))
#   → return list(map(lambda number: number, numbers))
#   → return list(map(lambda number: number, numbers))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only split_number is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → arg = ...  # stored in memory
#   → print(split_number(...))  # split_number() runs first → value goes to print()
#   → print(split_number(...))  # split_number() runs first → value goes to print()
#   → print(split_number(...))  # split_number() runs first → value goes to print()
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(split_number(...))  # split_number() runs first → value goes to print()
#
# Loop: takes one item from numbers, runs body, repeats until done
"""
Problème 135 :
Écrivez une fonction qui prend nombres chaîne "123" et divise le nombres dans une chaîne ("1", "2", "3").
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return ' '.join(sorted(sentence.split()))
#   → return ' '.join(sorted(sentence.split()))
#   → return ' '.join(sorted(sentence.split()))
#   → return ' '.join(sorted(sentence.split()))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only alphabetically_ordered is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → sentence = ...  # stored in memory
#   → print(alphabetically_ordered(...))  # alphabetically_ordered() runs first → value goes to print()
#   → print(alphabetically_ordered(...))  # alphabetically_ordered() runs first → value goes to print()
#   → print(alphabetically_ordered(...))  # alphabetically_ordered() runs first → value goes to print()
#   → sentence = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(alphabetically_ordered(...))  # alphabetically_ordered() runs first → value goes to print()
"""
Problème 136 :
Écrivez une fonction qui trie words dans une phrase alphabetically.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sorted(numbers, reverse=False)
#   → return sorted(numbers, reverse=False)
#   → return sorted(numbers, reverse=False)
#   → return sorted(numbers, reverse=False)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only smallest_largest is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → print(smallest_largest(...))  # smallest_largest() runs first → value goes to print()
#   → print(smallest_largest(...))  # smallest_largest() runs first → value goes to print()
#   → print(smallest_largest(...))  # smallest_largest() runs first → value goes to print()
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(smallest_largest(...))  # smallest_largest() runs first → value goes to print()
"""
Problème 137 :
Écrivez une fonction qui trie nombres (int) de plus petit nombre à biggest nombre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sorted(numbers)[::-1]
#   → return sorted(numbers)[::-1]
#   → return sorted(numbers)[::-1]
#   → return sorted(numbers)[::-1]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only largest_smallest is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → print(largest_smallest(...))  # largest_smallest() runs first → value goes to print()
#   → print(largest_smallest(...))  # largest_smallest() runs first → value goes to print()
#   → print(largest_smallest(...))  # largest_smallest() runs first → value goes to print()
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(largest_smallest(...))  # largest_smallest() runs first → value goes to print()
"""
Problème 138 :
Écrivez une fonction qui trie nombre (int) de biggest nombre à plus petit nombre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : set, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sorted(numbers)[-2]
#   → return sorted(numbers)[-2]
#   → return sorted(numbers)[-2]
#   → return sorted(numbers)[-2]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only seconded_largest_number is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → print(seconded_largest_number(...))  # seconded_largest_number() runs first → value goes to print()
#   → print(seconded_largest_number(...))  # seconded_largest_number() runs first → value goes to print()
#   → print(seconded_largest_number(...))  # seconded_largest_number() runs first → value goes to print()
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(seconded_largest_number(...))  # seconded_largest_number() runs first → value goes to print()
"""
Problème 139 :
Écrivez une fonction en utilisant trié() nombre int) returning le seconded plus grand nombre de qui list.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : set, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sorted(numbers)[-4]
#   → return sorted(numbers)[-4]
#   → return sorted(numbers)[-4]
#   → return sorted(numbers)[-4]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only fourth_largest_number is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → print(fourth_largest_number(...))  # fourth_largest_number() runs first → value goes to print()
#   → print(fourth_largest_number(...))  # fourth_largest_number() runs first → value goes to print()
#   → print(fourth_largest_number(...))  # fourth_largest_number() runs first → value goes to print()
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(fourth_largest_number(...))  # fourth_largest_number() runs first → value goes to print()
"""
Problème 140 :
Écrivez une fonction en utilisant trié() nombre int) returning le fourth plus grand nombre de qui list.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : min, set, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return (smallest, third_largest)
#   → return (smallest, third_largest)
#   → return (smallest, third_largest)
#   → return (smallest, third_largest)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only smallest_and_third is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → print(smallest_and_third(...))  # smallest_and_third() runs first → value goes to print()
#   → print(smallest_and_third(...))  # smallest_and_third() runs first → value goes to print()
#   → print(smallest_and_third(...))  # smallest_and_third() runs first → value goes to print()
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(smallest_and_third(...))  # smallest_and_third() runs first → value goes to print()
"""
Problème 141 :
Écrivez une fonction en utilisant trié() returning le plus petit et troisième plus grand nombre de qui list.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sorted(numbers)[:]
#   → return sorted(numbers, key=int)
#   → return sorted(numbers, key=int)
#   → return sorted(numbers, key=int)
#   → return sorted(numbers)[:]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — largest_smallest, smallest_biggest are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → print(largest_smallest(...))  # largest_smallest() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → print(smallest_biggest(...))  # smallest_biggest() runs first → value goes to print()
#   → print(smallest_biggest(...))  # smallest_biggest() runs first → value goes to print()
#   → print(smallest_biggest(...))  # smallest_biggest() runs first → value goes to print()
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(largest_smallest(...))  # largest_smallest() runs first → value goes to print()
"""
Problème 142 :
Écrivez une fonction qui trie nombre de plus petit nombre à biggest nombre en utilisant trié().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : input()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → user_lst = []
#   → user = input('type: ')
#   → split_str = user.split()
#   → for word in split_str:
#   →     user_lst.append(word)
#   → result = user_lst
#   → return result
#   → user_lst = []
#   → user = input('type: ')
#   → split_str = user.split()
#   → for word in split_str:
#   →     user_lst.append(word)
#   → result = user_lst
#   → return result
#   → user_lst = []
#   → user = input('type: ')
#   → split_str = user.split()
#   → for word in split_str:
#   →     user_lst.append(word)
#   → result = user_lst
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only int_str is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → int_str()  # jumps into int_str(), runs body, returns
#   → int_str()  # jumps into int_str(), runs body, returns
#   → int_str()  # jumps into int_str(), runs body, returns
#   → user_lst = ...  # stored in memory
#   → user = ...  # stored in memory
#   → split_str = ...  # stored in memory
#   → for word in split_str  # runs body once per item
#   → print(user_lst)
#   → user_lst = ...  # stored in memory
#   → user = ...  # stored in memory
#   → split_str = ...  # stored in memory
#   → for word in split_str  # runs body once per item
#   → print(user_lst)
#
# Loop: takes one item from split_str, runs body, repeats until done
"""
Problème 143 :
Écrivez une fonction avec utilisateur entrée qui coverts 1 2 3 (int) dans un "1" "2" "3" (str).
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : list, map, str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(lambda digit: digit, number_str))
#   → return list(map(lambda digit: digit, number_str))
#   → return list(map(lambda digit: digit, number_str))
#   → return list(map(lambda digit: digit, number_str))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only int_to_str_list is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → number = ...  # stored in memory
#   → print(int_to_str_list(...))  # int_to_str_list() runs first → value goes to print()
#   → print(int_to_str_list(...))  # int_to_str_list() runs first → value goes to print()
#   → print(int_to_str_list(...))  # int_to_str_list() runs first → value goes to print()
#   → number = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(int_to_str_list(...))  # int_to_str_list() runs first → value goes to print()
#
# Loop: takes one item from number_str, runs body, repeats until done
"""
Problème 144 :
Écrivez une fonction qui coverts 123 (int) dans un "1" "2" "3" (str).
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: == in and not in
# Fonctions intégrées : filter, list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(lambda i: i, lst1))
#   → return list(map(lambda i: i, lst1))
#   → return list(map(lambda i: i, lst1))
#   → return list(map(lambda i: i, lst1))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only common_numbers is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → print(common_numbers(...))  # common_numbers() runs first → value goes to print()
#   → print(common_numbers(...))  # common_numbers() runs first → value goes to print()
#   → print(common_numbers(...))  # common_numbers() runs first → value goes to print()
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(common_numbers(...))  # common_numbers() runs first → value goes to print()
#
# Loop: takes one item from lst1, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 145 :
Écrivez un programme Python à trouver le commun nombre entre deux listes. demander le utilisateur à saisir deux listes, pour cette exercise N'utilisez pas set.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : int, sorted, str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return shorted_str
#   → return shorted_str
#   → return shorted_str
#   → return shorted_str
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only big_small is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(big_small(...))  # big_small() runs first → value goes to print()
#   → print(big_small(...))  # big_small() runs first → value goes to print()
#   → print(big_small(...))  # big_small() runs first → value goes to print()
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(big_small(...))  # big_small() runs first → value goes to print()
#
# Loop: takes one item from numbers, runs body, repeats until done
"""
Problème 146 :
Écrivez une fonction qui trie nombres as chaîne de biggest nombre à plus petit nombre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : input, int, list, map, sorted, str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → user = input('type number list: ').split()
#   → sort_number = sorted(user)
#   → result = sort_number
#   → return result
#   → nums = list(map(int, input('Enter numbers: ').split()))
#   → nums.sort()
#   → return ' '.join(map(str, nums))
#   → nums = list(map(int, input('Enter numbers: ').split()))
#   → nums.sort()
#   → return ' '.join(map(str, nums))
#   → user = input('type number list: ').split()
#   → sort_number = sorted(user)
#   → result = sort_number
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — small_big, type_smallest_biggest are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → type_smallest_biggest()  # jumps into type_smallest_biggest(), runs body, returns
#   → print(small_big(...))  # small_big() runs first → value goes to print()
#   → print(small_big(...))  # small_big() runs first → value goes to print()
#   → type_smallest_biggest()  # jumps into type_smallest_biggest(), runs body, returns
#   → user = ...  # stored in memory
#   → sort_number = ...  # stored in memory
#   → print(sort_number)
#   → user = ...  # stored in memory
#   → sort_number = ...  # stored in memory
#   → print(sort_number)
#
# Loop: takes one item from user_split, runs body, repeats until done
"""
Problème 147 :
Écrivez une fonction où utilisateur tapez une liste de nombres dans chaîne et retourne une liste de nombres de plus petit à biggest.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: * +
# Fonctions intégrées : sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → import operator
#   → return operator.add(numbers, numbers)
#   → import operator
#   → return operator.add(numbers, numbers)
#   → import operator
#   → return operator.add(numbers, numbers)
#   → import operator
#   → return operator.add(numbers, numbers)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only double_elements is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(double_elements(...))  # double_elements() runs first → value goes to print()
#   → print(double_elements(...))  # double_elements() runs first → value goes to print()
#   → print(double_elements(...))  # double_elements() runs first → value goes to print()
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(double_elements(...))  # double_elements() runs first → value goes to print()
"""
Problème 148 :
Write un Python fonction appelée `double_elements` qui prend une liste de nombres en entrée et retourne une nouvelle liste où chaque élément est doubled, la liste doit be side by side par exemple 1, 2, 3, 1, 2, 3
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: & == in and not in
# Fonctions intégrées : input, list, map, set()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(lambda i: i, lst1))
#   → return list(map(lambda i: i, lst1))
#   → return list(map(lambda i: i, lst1))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only common is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → common()  # jumps into common(), runs body, returns
#   → print(common(...))  # common() runs first → value goes to print()
#   → print(common(...))  # common() runs first → value goes to print()
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → for i in lst1  # runs body once per item
#   → result = ...  # stored in memory
#   → print(result)
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → for i in lst1  # runs body once per item
#   → result = ...  # stored in memory
#   → print(result)
#
# Loop: takes one item from lst1, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 149 :
Écrivez un programme Python à trouver le commun éléments entre deux listes. demander le utilisateur à saisir deux listes en utilisant 2 pour loops.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: &
# Fonctions intégrées : input, list, set()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → lst1 = input('type lst: ').split()
#   → lst2 = input('type lst: ').split()
#   → set1 = set(lst1)
#   → set2 = set(lst2)
#   → common_element = set1.intersection(set2)
#   → result = common_element
#   → return result
#   → lst1 = input('type lst: ').split()
#   → lst2 = input('type lst: ').split()
#   → set1 = set(lst1)
#   → set2 = set(lst2)
#   → common_element = set1.intersection(set2)
#   → result = common_element
#   → return result
#   → lst1 = input('type lst: ').split()
#   → lst2 = input('type lst: ').split()
#   → set1 = set(lst1)
#   → set2 = set(lst2)
#   → common_element = set1.intersection(set2)
#   → result = common_element
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only common is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → common()  # jumps into common(), runs body, returns
#   → common()  # jumps into common(), runs body, returns
#   → common()  # jumps into common(), runs body, returns
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → set1 = ...  # stored in memory
#   → set2 = ...  # stored in memory
#   → common_element = ...  # stored in memory
#   → print(common_element)
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → set1 = ...  # stored in memory
#   → set2 = ...  # stored in memory
#   → common_element = ...  # stored in memory
#   → print(common_element)
"""
Problème 150 :
Écrivez un programme Python à trouver le commun éléments entre deux listes. demander le utilisateur à saisir deux listes sans en utilisant pour loops.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: > >=
# Fonctions intégrées : len, max, reduce, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return longest_word
#   → return longest_word
#   → return longest_word
#   → return longest_word
#   → return longest_word
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only find_longest_word is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → words = ...  # stored in memory
#   → print(find_longest_word(...))  # find_longest_word() runs first → value goes to print()
#   → print(find_longest_word(...))  # find_longest_word() runs first → value goes to print()
#   → print(find_longest_word(...))  # find_longest_word() runs first → value goes to print()
#   → print(find_longest_word(...))  # find_longest_word() runs first → value goes to print()
#   → words = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(find_longest_word(...))  # find_longest_word() runs first → value goes to print()
#
# Loop: takes one item from words, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 151 :
Écrivez une fonction Python appelée find_longest_word qui prend une liste de mots en entrée et retourne le plus long mot dans la liste. si il y un multiple le plus long words, retourner le premier l'une encountered.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: * + /
# Fonctions intégrées : Fraction, float, len, reduce, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → from fractions import Fraction
#   → return float(Fraction(total, length))
#   → from fractions import Fraction
#   → return float(Fraction(total, length))
#   → from fractions import Fraction
#   → return float(Fraction(total, length))
#   → from fractions import Fraction
#   → return float(Fraction(total, length))
#   → from fractions import Fraction
#   → return float(Fraction(total, length))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only average is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → print(average(...))  # average() runs first → value goes to print()
#   → print(average(...))  # average() runs first → value goes to print()
#   → print(average(...))  # average() runs first → value goes to print()
#   → print(average(...))  # average() runs first → value goes to print()
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(average(...))  # average() runs first → value goes to print()
#
# Loop: takes one item from numbers, runs body, repeats until done
"""
Problème 152 :
Write un Python fonction appelée `calculate_average` qui prend une liste de nombres en entrée et retourne le moyenne de ces nombres sans en utilisant sum() et len()
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else
# Operators: >=
# Fonctions intégrées : len, set, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sorted_lst[1]
#   → return sorted_lst[1]
#   → return sorted_lst[1]
#   → return sorted_lst[1]
#   → return sorted_lst[1]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only second_smallest_element is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(second_smallest_element(...))  # second_smallest_element() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → print(second_smallest_element(...))  # second_smallest_element() runs first → value goes to print()
#   → print(second_smallest_element(...))  # second_smallest_element() runs first → value goes to print()
#   → print(second_smallest_element(...))  # second_smallest_element() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(second_smallest_element(...))  # second_smallest_element() runs first → value goes to print()
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 153 :
Écrivez un programme Python à trouver le deuxième plus petit élément dans une liste.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else
# Operators: < >=
# Fonctions intégrées : input, len()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return None
#   → return lst[-2:-1][0] if len(lst) >= 2 else None
#   → return lst[-2:-1][0] if len(lst) >= 2 else None
#   → return lst[-2:-1][0] if len(lst) >= 2 else None
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — find_last_element, find_second_last_element are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(find_last_element(...))  # find_last_element() runs first → value goes to print()
#   → print(find_second_last_element(...))  # find_second_last_element() runs first → value goes to print()
#   → print(find_second_last_element(...))  # find_second_last_element() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(find_second_last_element(...))  # find_second_last_element() runs first → value goes to print()
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 154 :
Écrivez une fonction Python appelée `find_second_last_element` qui prend une liste en entrée et retourne le deuxième dernier élément de la liste.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: while
# Operators: % * + > >=
# Fonctions intégrées : abs, int, str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return int(str(number)[::-1])
#   → return int(str(number)[::-1])
#   → return int(str(number)[::-1])
#   → return int(str(number)[::-1])
#   → return int(str(number)[::-1])
#   → return int(str(number)[::-1])
#   → return int(str(number)[::-1])
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only reverse_number is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(reverse_number(...))  # reverse_number() runs first → value goes to print()
#   → number = ...  # stored in memory
#   → print(reverse_number(...))  # reverse_number() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → print(reverse_number(...))  # reverse_number() runs first → value goes to print()
#   → print(reverse_number(...))  # reverse_number() runs first → value goes to print()
#   → print(reverse_number(...))  # reverse_number() runs first → value goes to print()
#   → print(reverse_number(...))  # reverse_number() runs first → value goes to print()
#   → number = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(reverse_number(...))  # reverse_number() runs first → value goes to print()
#
# Loop: check condition → if True run body → check again
"""
Problème 155 :
Écrivez une fonction Python appelée reverse_number qui prend un entier en entrée et retourne le reverse de cette nombre. par exemple, si le entrée est 123, la fonction devrait retourner 321.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: in or
# Fonctions intégrées : set()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return ' '.join(set_word)
#   → return ' '.join(set_word)
#   → return ' '.join(set_word)
#   → return ' '.join(set_word)
#   → return ' '.join(set_word)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only remove_duplicates is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(remove_duplicates(...))  # remove_duplicates() runs first → value goes to print()
#   → print(remove_duplicates(...))  # remove_duplicates() runs first → value goes to print()
#   → print(remove_duplicates(...))  # remove_duplicates() runs first → value goes to print()
#   → print(remove_duplicates(...))  # remove_duplicates() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(remove_duplicates(...))  # remove_duplicates() runs first → value goes to print()
"""
Problème 156 :
Écrivez une fonction Python appelée remove_duplicates qui prend une chaîne en entrée et retourne une nouvelle chaîne avec en double caractères removed, sans maintaining le original order de caractères.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: >
# Fonctions intégrées : input, int, max, reduce, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return largest_number
#   → result = []
#   → user = input('type numbers: ').split()
#   → for num in user:
#   →     result.append(int(num))
#   →     largest_num = sorted(result)[-1]
#   → return largest_num
#   → return largest_number
#   → return largest_number
#   → return largest_number
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — largest_element, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → print(largest_element(...))  # largest_element() runs first → value goes to print()
#   → main()  # jumps into main(), runs body, returns
#   → print(largest_element(...))  # largest_element() runs first → value goes to print()
#   → print(largest_element(...))  # largest_element() runs first → value goes to print()
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(largest_element(...))  # largest_element() runs first → value goes to print()
#
# Loop: takes one item from user, runs body, repeats until done
"""
Problème 158 :
Écrivez un programme Python à trouver le plus grand élément dans une liste. demander le utilisateur à saisir une liste de nombres en utilisant trié.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: >
# Fonctions intégrées : max, reduce, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → result = numbers[0]
#   → for item in numbers:
#   →     if item > result:
#   →         result = item
#   → return result
#   → result = numbers[0]
#   → for item in numbers:
#   →     if item > result:
#   →         result = item
#   → return result
#   → result = numbers[0]
#   → for item in numbers:
#   →     if item > result:
#   →         result = item
#   → return result
#   → result = numbers[0]
#   → for item in numbers:
#   →     if item > result:
#   →         result = item
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only largest_element is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → print(largest_element(...))  # largest_element() runs first → value goes to print()
#   → print(largest_element(...))  # largest_element() runs first → value goes to print()
#   → print(largest_element(...))  # largest_element() runs first → value goes to print()
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(largest_element(...))  # largest_element() runs first → value goes to print()
#
# Loop: takes one item from numbers, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 159 :
Écrivez un programme Python à trouver le plus grand élément dans une liste. demander le utilisateur à saisir une liste de nombres en utilisant max().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: + ==
# Fonctions intégrées : enumerate, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return count
#   → return count
#   → return count
#   → return count
#   → return count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only find_length is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → arg = ...  # stored in memory
#   → print(find_length(...))  # find_length() runs first → value goes to print()
#   → print(find_length(...))  # find_length() runs first → value goes to print()
#   → print(find_length(...))  # find_length() runs first → value goes to print()
#   → print(find_length(...))  # find_length() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(find_length(...))  # find_length() runs first → value goes to print()
#
# Loop: takes one item from string, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 160 :
Définissez une fonction qui calcule la longueur de une donnée list ou chaîne. (C'est vrai qui Python une len() fonction construit dans, but writing it yourself est nevertheless un good exercise.)
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: & in
# Fonctions intégrées : filter, input, list, set, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → lst1 = input('type list: ').split()
#   → lst2 = input('type list: ').split()
#   → sort1 = sorted(lst1)
#   → sort2 = sorted(lst2)
#   → common = []
#   → for word in sort1:
#   →     if word in sort2:
#   →         common.append(word)
#   → result = common
#   → return result
#   → lst1 = input('type list: ').split()
#   → lst2 = input('type list: ').split()
#   → sort1 = sorted(lst1)
#   → sort2 = sorted(lst2)
#   → common = []
#   → for word in sort1:
#   →     if word in sort2:
#   →         common.append(word)
#   → result = common
#   → return result
#   → return list(filter(lambda x: x in lst2, lst1))
#   → return list(filter(lambda x: x in lst2, lst1))
#   → return list(filter(lambda x: x in lst2, lst1))
#   → return list(filter(lambda x: x in lst2, lst1))
#   → return list(filter(lambda x: x in lst2, lst1))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — intersection, intersection_two_list are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → intersection()  # jumps into intersection(), runs body, returns
#   → intersection()  # jumps into intersection(), runs body, returns
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → print(intersection_two_list(...))  # intersection_two_list() runs first → value goes to print()
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → print(intersection_two_list(...))  # intersection_two_list() runs first → value goes to print()
#   → print(intersection_two_list(...))  # intersection_two_list() runs first → value goes to print()
#   → print(intersection_two_list(...))  # intersection_two_list() runs first → value goes to print()
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(intersection_two_list(...))  # intersection_two_list() runs first → value goes to print()
#
# Loop: takes one item from sort1, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 161 :
Écrivez un programme Python à trouver le l'intersection des deux listes. demander le utilisateur à saisir deux listes en utilisant set.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : input, int, list, map, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → user_string = input('type number followed by spaces: ')
#   → user_split = user_string.split()
#   → int_list = []
#   → for number in user_split:
#   →     int_list.append(int(number))
#   → int_list.sort()
#   → result = int_list[-3]
#   → result = result
#   → return result
#   → user_string = input('type number followed by spaces: ')
#   → user_split = user_string.split()
#   → int_list = []
#   → for number in user_split:
#   →     int_list.append(int(number))
#   → int_list.sort()
#   → result = int_list[-3]
#   → result = result
#   → return result
#   → user_string = input('type number followed by spaces: ')
#   → user_split = user_string.split()
#   → int_list = []
#   → for number in user_split:
#   →     int_list.append(int(number))
#   → int_list.sort()
#   → result = int_list[-3]
#   → result = result
#   → return result
#   → user_string = input('type number followed by spaces: ')
#   → user_split = user_string.split()
#   → int_list = []
#   → for number in user_split:
#   →     int_list.append(int(number))
#   → int_list.sort()
#   → result = int_list[-3]
#   → result = result
#   → return result
#   → user_string = input('type number followed by spaces: ')
#   → user_split = user_string.split()
#   → int_list = []
#   → for number in user_split:
#   →     int_list.append(int(number))
#   → int_list.sort()
#   → result = int_list[-3]
#   → result = result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only third_largest is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → third_largest()  # jumps into third_largest(), runs body, returns
#   → print(third_largest(...))  # third_largest() runs first → value goes to print()
#   → print(third_largest(...))  # third_largest() runs first → value goes to print()
#   → print(third_largest(...))  # third_largest() runs first → value goes to print()
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(third_largest(...))  # third_largest() runs first → value goes to print()
#
# Loop: takes one item from user_split, runs body, repeats until done
"""
Problème 162 :
Écrivez une fonction où utilisateur tapez une liste de nombres dans chaîne et retourne une troisième plus grand nombre dans une liste.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: in
# Fonctions intégrées : Counter()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#   → return result
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_vowels is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → string = ...  # stored in memory
#   → print(count_vowels(...))  # count_vowels() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → print(count_vowels(...))  # count_vowels() runs first → value goes to print()
#   → print(count_vowels(...))  # count_vowels() runs first → value goes to print()
#   → print(count_vowels(...))  # count_vowels() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_vowels(...))  # count_vowels() runs first → value goes to print()
#
# Loop: takes one item from vowels, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 163 :
Écrivez une fonction Python `count_vowels` qui prend une chaîne en entrée et retourne un dictionnaire avec le compte de chaque voyelle ('a','e','i','o','u') dans la chaîne. Ignore cas, so'A'et'a'devrait be counted as le même voyelle en utilisant List comprehension.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: in
# Fonctions intégrées : Counter()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return vowel_counts
#   → return vowel_counts
#   → return vowel_counts
#   → return vowel_counts
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_vowels is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → string = ...  # stored in memory
#   → print(count_vowels(...))  # count_vowels() runs first → value goes to print()
#   → print(count_vowels(...))  # count_vowels() runs first → value goes to print()
#   → print(count_vowels(...))  # count_vowels() runs first → value goes to print()
#   → sentence = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_vowels(...))  # count_vowels() runs first → value goes to print()
#
# Loop: takes one item from vowels, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 164 :
Écrivez une fonction Python `count_vowels` qui prend une chaîne en entrée et retourne un dictionnaire avec le compte de chaque voyelle ('a','e','i','o','u') dans la chaîne. Ignore cas, so'A'et'a'devrait be counted as le même voyelle sans en utilisant list conprehension.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list, map, str, tuple()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(str(number))
#   → return [c for c in str(number)]
#   → return [c for c in str(number)]
#   → return [c for c in str(number)]
#   → return list(str(number))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — intiger_string, split_number_int are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → number = ...  # stored in memory
#   → print(intiger_string(...))  # intiger_string() runs first → value goes to print()
#   → number = ...  # stored in memory
#   → print(split_number_int(...))  # split_number_int() runs first → value goes to print()
#   → print(split_number_int(...))  # split_number_int() runs first → value goes to print()
#   → print(split_number_int(...))  # split_number_int() runs first → value goes to print()
#   → number = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(intiger_string(...))  # intiger_string() runs first → value goes to print()
"""
Problème 165 :
Écrivez une fonction qui prend nombres integer 123 et divise le nombres dans une chaîne ("1", "2", "3").
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: *
# Fonctions intégrées : list, map, zip()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(lambda word: word, lst))
#   → return list(map(lambda word: word, lst))
#   → return list(map(lambda word: word, lst))
#   → return list(map(lambda word: word, lst))
#   → return list(map(lambda word: word, lst))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only double_elements is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(double_elements(...))  # double_elements() runs first → value goes to print()
#   → print(double_elements(...))  # double_elements() runs first → value goes to print()
#   → print(double_elements(...))  # double_elements() runs first → value goes to print()
#   → print(double_elements(...))  # double_elements() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(double_elements(...))  # double_elements() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
"""
Problème 166 :
Écrivez une fonction Python appelée `double_elements` qui prend une liste de chaînes en entrée et retourne un 2 new list où chaque élément est doubled.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: < >
# Fonctions intégrées : input, list, map, max, min, reduce, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return (smallest_num, largest_num)
#   → return (sorted(numbers)[0], sorted(numbers)[-1])
#   → return (sorted(numbers)[0], sorted(numbers)[-1])
#   → return (sorted(numbers)[0], sorted(numbers)[-1])
#   → return (sorted(numbers)[0], sorted(numbers)[-1])
#   → return (sorted(numbers)[0], sorted(numbers)[-1])
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — l_s, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → main()  # jumps into main(), runs body, returns
#   → numbers = ...  # stored in memory
#   → print(l_s(...))  # l_s() runs first → value goes to print()
#   → print(l_s(...))  # l_s() runs first → value goes to print()
#   → print(l_s(...))  # l_s() runs first → value goes to print()
#   → print(l_s(...))  # l_s() runs first → value goes to print()
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(l_s(...))  # l_s() runs first → value goes to print()
"""
Problème 167 :
Écrivez un programme Python à trouver le plus grand et plus petit éléments dans une liste. demander le utilisateur à saisir une liste de nombres en utilisant trié()."
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: + in
# Fonctions intégrées : Counter, dict, input, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → user = input('type words: ').split()
#   → sort = sorted(user)
#   → result = {}
#   → for word in sort:
#   →     word = word.lower()
#   →     if word in result:
#   →         result[word] += 1
#   →     else:
#   →         result[word] = 1
#   → result = result
#   → return result
#   → user = input('type words: ').split()
#   → sort = sorted(user)
#   → result = {}
#   → for word in sort:
#   →     word = word.lower()
#   →     if word in result:
#   →         result[word] += 1
#   →     else:
#   →         result[word] = 1
#   → result = result
#   → return result
#   → user = input('type words: ').split()
#   → sort = sorted(user)
#   → result = {}
#   → for word in sort:
#   →     word = word.lower()
#   →     if word in result:
#   →         result[word] += 1
#   →     else:
#   →         result[word] = 1
#   → result = result
#   → return result
#   → user = input('type words: ').split()
#   → sort = sorted(user)
#   → result = {}
#   → for word in sort:
#   →     word = word.lower()
#   →     if word in result:
#   →         result[word] += 1
#   →     else:
#   →         result[word] = 1
#   → result = result
#   → return result
#   → user = input('type words: ').split()
#   → sort = sorted(user)
#   → result = {}
#   → for word in sort:
#   →     word = word.lower()
#   →     if word in result:
#   →         result[word] += 1
#   →     else:
#   →         result[word] = 1
#   → result = result
#   → return result
#   → user = input('type words: ').split()
#   → sort = sorted(user)
#   → result = {}
#   → for word in sort:
#   →     word = word.lower()
#   →     if word in result:
#   →         result[word] += 1
#   →     else:
#   →         result[word] = 1
#   → result = result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_words is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → count_words()  # jumps into count_words(), runs body, returns
#   → input_string = ...  # stored in memory
#   → print(count_words(...))  # count_words() runs first → value goes to print()
#   → print(count_words(...))  # count_words() runs first → value goes to print()
#   → print(count_words(...))  # count_words() runs first → value goes to print()
#   → print(count_words(...))  # count_words() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_words(...))  # count_words() runs first → value goes to print()
#
# Loop: takes one item from sort, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 168 :
Écrivez une fonction Python appelée count_words qui prend une chaîne en entrée et retourne un dictionnaire où le clés sont le words dans la chaîne et le valeurs sont le compte de chaque mot. Words sont séparés by spaces, et la fonction devrait be cas-insensitive, make le clés alphabetical.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: or
# Fonctions intégrées : dict()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return merged
#   → return merged
#   → return merged
#   → return merged
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only merge_dictionaries is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dict1 = ...  # stored in memory
#   → dict2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(merge_dictionaries(...))  # merge_dictionaries() runs first → value goes to print()
#   → print(merge_dictionaries(...))  # merge_dictionaries() runs first → value goes to print()
#   → print(merge_dictionaries(...))  # merge_dictionaries() runs first → value goes to print()
#   → dict1 = ...  # stored in memory
#   → dict2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(merge_dictionaries(...))  # merge_dictionaries() runs first → value goes to print()
#
# Loop: takes one item from dict2.items(...), runs body, repeats until done
"""
Problème 169 :
Écrivez une fonction merge_dictionaries qui prend deux dictionnaires as arguments et retourne un nouveau dictionnaire qui contient tous les paires clé-valeur de les deux dictionnaires. si une clé est present dans les deux dictionnaires, le valeur de le deuxième dictionnaire devrait overwrite le valeur de le premier dictionnaire.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: + in
# Fonctions intégrées : Counter, dict, input()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return counts
#   → return counts
#   → return counts
#   → return counts
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_characters is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_characters(...))  # count_characters() runs first → value goes to print()
#   → print(count_characters(...))  # count_characters() runs first → value goes to print()
#   → print(count_characters(...))  # count_characters() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_characters(...))  # count_characters() runs first → value goes to print()
#
# Loop: takes one item from string, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 170 :
Écrivez une fonction count_characters qui prend une chaîne en entrée et retourne un dictionnaire où le clés sont caractères dans la chaîne et le valeurs sont le compte de ces caractères.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: == not in
# Fonctions intégrées : defaultdict, dict, set()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return inverted
#   → return inverted
#   → return inverted
#   → return inverted
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only invert_dictionary is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → input_dict = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(invert_dictionary(...))  # invert_dictionary() runs first → value goes to print()
#   → print(invert_dictionary(...))  # invert_dictionary() runs first → value goes to print()
#   → print(invert_dictionary(...))  # invert_dictionary() runs first → value goes to print()
#   → input_dict = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(invert_dictionary(...))  # invert_dictionary() runs first → value goes to print()
#
# Loop: takes one item from input_dict.items(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 171 :
Écrivez une fonction invert_dictionary qui prend un dictionnaire en entrée et retourne un nouveau dictionnaire où le clés sont le valeurs de le entrée dictionnaire, et le valeurs sont listes de clés de le entrée dictionnaire qui had qui valeur.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: >
# Fonctions intégrées : dict, filter()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return filtered
#   → return filtered
#   → return filtered
#   → return filtered
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only filter_by_value is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → input_dict = ...  # stored in memory
#   → threshold = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(filter_by_value(...))  # filter_by_value() runs first → value goes to print()
#   → print(filter_by_value(...))  # filter_by_value() runs first → value goes to print()
#   → print(filter_by_value(...))  # filter_by_value() runs first → value goes to print()
#   → input_dict = ...  # stored in memory
#   → threshold = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(filter_by_value(...))  # filter_by_value() runs first → value goes to print()
#
# Loop: takes one item from input_dict.items(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 172 :
Écrivez une fonction filter_by_value qui prend un dictionnaire et une valeur seuil en entrée et retourne un nouveau dictionnaire contenant seulement les paires clé-valeur où le valeur est greater que le seuil.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : dict, len, range, zip()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return combined
#   → return combined
#   → return combined
#   → return combined
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only combine_lists_to_dict is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → keys = ...  # stored in memory
#   → values = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(combine_lists_to_dict(...))  # combine_lists_to_dict() runs first → value goes to print()
#   → print(combine_lists_to_dict(...))  # combine_lists_to_dict() runs first → value goes to print()
#   → print(combine_lists_to_dict(...))  # combine_lists_to_dict() runs first → value goes to print()
#   → keys = ...  # stored in memory
#   → values = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(combine_lists_to_dict(...))  # combine_lists_to_dict() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
"""
Problème 173 :
Écrivez une fonction combine_lists_to_dict qui prend deux listes—l'une pour clés et l'une pour valeurs—as entrée et retourne un dictionnaire où chaque la paire clé-valeur est taken de corresponding éléments dans le entrée listes.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: == >=
# Fonctions intégrées : max, reduce, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return None
#   → return None
#   → return None
#   → return None
#   → return None
#   → return None
#   → return None
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only max_value_key is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → my_dict = ...  # stored in memory
#   → print(max_value_key(...))  # max_value_key() runs first → value goes to print()
#   → empty_dict = ...  # stored in memory
#   → print(max_value_key(...))  # max_value_key() runs first → value goes to print()
#   → print(max_value_key(...))  # max_value_key() runs first → value goes to print()
#   → print(max_value_key(...))  # max_value_key() runs first → value goes to print()
#   → print(max_value_key(...))  # max_value_key() runs first → value goes to print()
#   → print(max_value_key(...))  # max_value_key() runs first → value goes to print()
#   → input_dict = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(max_value_key(...))  # max_value_key() runs first → value goes to print()
#
# Loop: takes one item from input_dict.items(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 174 :
Écrivez une fonction max_value_key qui prend un dictionnaire en entrée et retourne la clé associated avec le maximum valeur. si le dictionnaire est vide, la fonction devrait retourner None.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: ^ != == or not in
# Fonctions intégrées : all, len, set()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return dict1 == dict2
#   → return dict1 == dict2
#   → return dict1 == dict2
#   → return dict1 == dict2
#   → return dict1 == dict2
#   → return dict1 == dict2
#   → return dict1 == dict2
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only dict_equal is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dict1 = ...  # stored in memory
#   → dict2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(dict_equal(...))  # dict_equal() runs first → value goes to print()
#   → print(dict_equal(...))  # dict_equal() runs first → value goes to print()
#   → print(dict_equal(...))  # dict_equal() runs first → value goes to print()
#   → print(dict_equal(...))  # dict_equal() runs first → value goes to print()
#   → print(dict_equal(...))  # dict_equal() runs first → value goes to print()
#   → print(dict_equal(...))  # dict_equal() runs first → value goes to print()
#   → dict1 = ...  # stored in memory
#   → dict2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(dict_equal(...))  # dict_equal() runs first → value goes to print()
#
# Loop: takes one item from dict1, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 175 :
Écrivez une fonction dict_equal qui prend deux dictionnaires en entrée et retourne vrai si they sont equal (c'est-à-dire., they ont le même clés avec le même corresponding valeurs), et False sinon.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: + in
# Fonctions intégrées : Counter, dict()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only word_frequency is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → string = ...  # stored in memory
#   → print(word_frequency(...))  # word_frequency() runs first → value goes to print()
#   → print(word_frequency(...))  # word_frequency() runs first → value goes to print()
#   → print(word_frequency(...))  # word_frequency() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(word_frequency(...))  # word_frequency() runs first → value goes to print()
#
# Loop: takes one item from words, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 176 :
Écrivez une fonction word_frequency qui prend une chaîne en entrée et retourne un dictionnaire où le clés sont words dans la chaîne et le valeurs sont le compte de ces words.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : reduce()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return merged
#   → return merged
#   → return merged
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only merge_list_of_dicts is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dicts = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(merge_list_of_dicts(...))  # merge_list_of_dicts() runs first → value goes to print()
#   → print(merge_list_of_dicts(...))  # merge_list_of_dicts() runs first → value goes to print()
#   → dicts = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(merge_list_of_dicts(...))  # merge_list_of_dicts() runs first → value goes to print()
#
# Loop: takes one item from dicts, runs body, repeats until done
"""
Problème 177 :
Écrivez une fonction merge_list_of_dicts qui prend une liste de dictionnaires en entrée et retourne un seul dictionnaire qui fusionne tous dictionnaires dans la liste. si un clés sont duplicated across dictionnaires, le valeur de le dernier dictionnaire dans la liste devrait overwrite le précédent ones.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : list, set()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return new_dict
#   → return new_dict
#   → return new_dict
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only remove_duplicates_from_values is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → input_dict = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(remove_duplicates_from_values(...))  # remove_duplicates_from_values() runs first → value goes to print()
#   → print(remove_duplicates_from_values(...))  # remove_duplicates_from_values() runs first → value goes to print()
#   → input_dict = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(remove_duplicates_from_values(...))  # remove_duplicates_from_values() runs first → value goes to print()
#
# Loop: takes one item from input_dict.items(...), runs body, repeats until done
"""
Problème 178 :
Écrivez une fonction remove_duplicates_from_values qui prend un dictionnaire en entrée et retourne un nouveau dictionnaire où chaque la paire clé-valeur est preserved, but le valeurs sont listes avec les doublons removed.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: &
# Fonctions intégrées : max, set()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return common_keys
#   → return common_keys
#   → return common_keys
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only common_keys_max_values is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dict1 = ...  # stored in memory
#   → dict2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(common_keys_max_values(...))  # common_keys_max_values() runs first → value goes to print()
#   → print(common_keys_max_values(...))  # common_keys_max_values() runs first → value goes to print()
#   → dict1 = ...  # stored in memory
#   → dict2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(common_keys_max_values(...))  # common_keys_max_values() runs first → value goes to print()
#
# Loop: takes one item from ?, runs body, repeats until done
"""
Problème 179 :
Écrivez une fonction common_keys_max_values qui prend deux dictionnaires et retourne un nouveau dictionnaire qui contient seulement le clés qui sont present dans les deux entrée dictionnaires. Le valeur pour chaque clé dans le new dictionnaire devrait be le maximum de le valeurs de le deux entrée dictionnaires.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: / in
# Fonctions intégrées : defaultdict, set, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return averages
#   → return averages
#   → return averages
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only average_values is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dicts = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(average_values(...))  # average_values() runs first → value goes to print()
#   → print(average_values(...))  # average_values() runs first → value goes to print()
#   → dicts = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(average_values(...))  # average_values() runs first → value goes to print()
#
# Loop: takes one item from dicts, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 180 :
Écrivez une fonction average_values qui prend une liste de dictionnaires en entrée et retourne un nouveau dictionnaire. Le new dictionnaire devrait contien le même clés, et le valeurs devrait be le moyenne de le valeurs associated avec chaque clé across tous entrée dictionnaires.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: in
# Fonctions intégrées : defaultdict, list, set()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return merged
#   → return merged
#   → return merged
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only merge_dicts_with_lists is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dicts = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(merge_dicts_with_lists(...))  # merge_dicts_with_lists() runs first → value goes to print()
#   → print(merge_dicts_with_lists(...))  # merge_dicts_with_lists() runs first → value goes to print()
#   → dicts = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(merge_dicts_with_lists(...))  # merge_dicts_with_lists() runs first → value goes to print()
#
# Loop: takes one item from dicts, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 181 :
Écrivez une fonction merge_dicts_with_lists qui prend une liste de dictionnaires en entrée. chaque dictionnaire dans la liste des clés qui sont des chaînes et valeurs qui sont listes de integers. la fonction devrait merge ces dictionnaires dans un seul dictionnaire où le clés sont preserved, et le valeurs sont fusionné listes contenant tous unique integers de le entrée dictionnaires pour chaque clé.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: not in
# Fonctions intégrées : defaultdict, dict()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → result = {}
#   → for word in lst:
#   →     key = word[0]
#   →     value = word
#   →     result[key] = value
#   → return result
#   → return result
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — group_by_first_letter, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(group_by_first_letter(...))  # group_by_first_letter() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → main(lst)  # jumps into main(), runs body, returns
#   → print(group_by_first_letter(...))  # group_by_first_letter() runs first → value goes to print()
#   → print(group_by_first_letter(...))  # group_by_first_letter() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(group_by_first_letter(...))  # group_by_first_letter() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 182 :
Écrivez une fonction group_by_first_letter qui prend une liste de chaînes en entrée et retourne un dictionnaire. Le dictionnaire devrait group le strings by leur premier lettre. chaque clé dans le dictionnaire devrait be un premier lettre, et le corresponding valeur devrait be une liste de chaînes qui start avec qui lettre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: != == in
# Fonctions intégrées : Counter, all, input, len, set()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return False
#   → return False
#   → return False
#   → return False
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only is_anagram is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → string1 = ...  # stored in memory
#   → string2 = ...  # stored in memory
#   → print('Are the strings anagrams?:', is_anagram(...))
#   → print(is_anagram(...))  # is_anagram() runs first → value goes to print()
#   → print(is_anagram(...))  # is_anagram() runs first → value goes to print()
#   → print(is_anagram(...))  # is_anagram() runs first → value goes to print()
#   → string1 = ...  # stored in memory
#   → string2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_anagram(...))  # is_anagram() runs first → value goes to print()
#
# Loop: takes one item from string1, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 183 :
Écrivez un programme Python à vérifier si une chaîne est an un anagramme de un autre chaîne, ignoring les espaces. demander le utilisateur à saisir deux strings sans en utilisant trié().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: % //
# Fonctions intégrées : list, str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list_number
#   → return number // 10 % 10
#   → return str(n)[1]
#   → return list_number
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — extract_digit, get_digit, get_second_digit are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → number = ...  # stored in memory
#   → print(int(...))  # int() runs first → value goes to print()
#   → print(extract_digit(...))  # extract_digit() runs first → value goes to print()
#   → print(get_digit(...))  # get_digit() runs first → value goes to print()
#   → number = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(int(...))  # int() runs first → value goes to print()
"""
Problème 184 :
Écrivez une fonction qui prend nombres integer 123 et retourner 2.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : str, tuple()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return (num2, num4, num8)
#   → s = str(number)
#   → return (s[1], s[3], s[-1])
#   → s = str(num)
#   → return tuple((s[i] for i in [1, 3, -1]))
#   → return (num2, num4, num8)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — extract_digits, get_digits, get_indexed_digits are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → number = ...  # stored in memory
#   → print(int(...))  # int() runs first → value goes to print()
#   → print(extract_digits(...))  # extract_digits() runs first → value goes to print()
#   → print(get_digits(...))  # get_digits() runs first → value goes to print()
#   → number = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(int(...))  # int() runs first → value goes to print()
"""
Problème 185 :
Écrivez une fonction qui prend nombres integer 12345678 et retourner 2, 4, 8.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : itemgetter, list, map, str, tuple()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(lambda i: number_str[i], indices))
#   → return list(map(lambda i: number_str[i], indices))
#   → return list(map(lambda i: number_str[i], indices))
#   → return list(map(lambda i: number_str[i], indices))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only get_digits is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → number = ...  # stored in memory
#   → indices = ...  # stored in memory
#   → print(get_digits(...))  # get_digits() runs first → value goes to print()
#   → print(get_digits(...))  # get_digits() runs first → value goes to print()
#   → print(get_digits(...))  # get_digits() runs first → value goes to print()
#   → number = ...  # stored in memory
#   → indices = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(get_digits(...))  # get_digits() runs first → value goes to print()
#
# Loop: takes one item from indices, runs body, repeats until done
"""
Problème 186 :
Écrivez une fonction qui prend nombres integer 12346778910 et users indexing à retourner le nombre 2, 4, 8
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : list, map, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(lambda word: word, string1))
#   → return list(map(lambda word: word, string1))
#   → return list(map(lambda word: word, string1))
#   → return list(map(lambda word: word, string1))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only double_elements is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → string1 = ...  # stored in memory
#   → print(double_elements(...))  # double_elements() runs first → value goes to print()
#   → print(double_elements(...))  # double_elements() runs first → value goes to print()
#   → print(double_elements(...))  # double_elements() runs first → value goes to print()
#   → string1 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(double_elements(...))  # double_elements() runs first → value goes to print()
#
# Loop: takes one item from string1, runs body, repeats until done
"""
Problème 187 :
Écrivez une fonction Python appelée `double_elements` qui prend une liste de chaînes en entrée et retourne un 2 new list où chaque élément est doubled où chaque élément est doubled side by side par exemple'tree','tree','road','road','slow','slow'.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: in
# Fonctions intégrées : list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return ''.join(name_list)
#   → return ''.join(name_list)
#   → return ''.join(name_list)
#   → return ''.join(name_list)
#   → return ''.join(name_list)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only get_initials is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → name = ...  # stored in memory
#   → print(get_initials(...))  # get_initials() runs first → value goes to print()
#   → name = ...  # stored in memory
#   → print(get_initials(...))  # get_initials() runs first → value goes to print()
#   → print(get_initials(...))  # get_initials() runs first → value goes to print()
#   → print(get_initials(...))  # get_initials() runs first → value goes to print()
#   → name = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(get_initials(...))  # get_initials() runs first → value goes to print()
#
# Loop: takes one item from name, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 188 :
Écrivez une fonction Python appelée get_initials qui prend un full nom (premier et dernier nom jonathan noll) en entrée et retourne "joNathAn noLL"" de le nom en majuscule (NALL dans jonathan noll).
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: +
# Fonctions intégrées : filter, input, int, list, reduce, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → user = list(input('type number: '))
#   → count = 0
#   → for number in user:
#   →     count += int(number)
#   → result = count
#   → return result
#   → user = input('Type a string containing numbers: ')
#   → total = 0
#   → for char in user:
#   →     if char.isdigit():
#   →         total += int(char)
#   → print(total)
#   → user = list(input('type number: '))
#   → count = 0
#   → for number in user:
#   →     count += int(number)
#   → result = count
#   → return result
#   → user = list(input('type number: '))
#   → count = 0
#   → for number in user:
#   →     count += int(number)
#   → result = count
#   → return result
#   → user = list(input('type number: '))
#   → count = 0
#   → for number in user:
#   →     count += int(number)
#   → result = count
#   → return result
#   → user = list(input('type number: '))
#   → count = 0
#   → for number in user:
#   →     count += int(number)
#   → result = count
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — digits_string, sum_digits are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → sum_digits()  # jumps into sum_digits(), runs body, returns
#   → digits_string()  # jumps into digits_string(), runs body, returns
#   → print(sum_digits(...))  # sum_digits() runs first → value goes to print()
#   → print(sum_digits(...))  # sum_digits() runs first → value goes to print()
#   → print(sum_digits(...))  # sum_digits() runs first → value goes to print()
#   → s = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sum_digits(...))  # sum_digits() runs first → value goes to print()
#
# Loop: takes one item from user, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 189 :
Écrivez un programme Python à trouver le somme de les chiffres dans une chaîne. demander le utilisateur à saisir une chaîne contenant nombres, par exemple "1234" devrait retourner 10.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: not in
# Fonctions intégrées : input()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → user = input('type string: ')
#   → duplicate = []
#   → for char in user:
#   →     if char not in duplicate:
#   →         duplicate.append(char)
#   → result = duplicate
#   → return result
#   → user = input('type string: ')
#   → duplicate = []
#   → for char in user:
#   →     if char not in duplicate:
#   →         duplicate.append(char)
#   → result = duplicate
#   → return result
#   → user = input('type string: ')
#   → duplicate = []
#   → for char in user:
#   →     if char not in duplicate:
#   →         duplicate.append(char)
#   → result = duplicate
#   → return result
#   → user = input('type string: ')
#   → duplicate = []
#   → for char in user:
#   →     if char not in duplicate:
#   →         duplicate.append(char)
#   → result = duplicate
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only remove_duplicate is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → remove_duplicate()  # jumps into remove_duplicate(), runs body, returns
#   → print(remove_duplicate(...))  # remove_duplicate() runs first → value goes to print()
#   → print(remove_duplicate(...))  # remove_duplicate() runs first → value goes to print()
#   → s = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(remove_duplicate(...))  # remove_duplicate() runs first → value goes to print()
#
# Loop: takes one item from user, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 190 :
Écrivez un programme Python à remove les doublons de une chaîne et maintain le order de caractères. demander le utilisateur à saisir une chaîne
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: <
# Fonctions intégrées : input, int, min, reduce()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → user = input('type list: ').split()
#   → user_int = []
#   → for number in user:
#   →     user_int.append(int(number))
#   → min_number = user_int[0]
#   → for number in user_int:
#   →     if number < min_number:
#   →         min_number = number
#   → result = min_number
#   → return result
#   → user = input('type list: ').split()
#   → user_int = []
#   → for number in user:
#   →     user_int.append(int(number))
#   → min_number = user_int[0]
#   → for number in user_int:
#   →     if number < min_number:
#   →         min_number = number
#   → result = min_number
#   → return result
#   → user = input('type list: ').split()
#   → user_int = []
#   → for number in user:
#   →     user_int.append(int(number))
#   → min_number = user_int[0]
#   → for number in user_int:
#   →     if number < min_number:
#   →         min_number = number
#   → result = min_number
#   → return result
#   → user = input('type list: ').split()
#   → user_int = []
#   → for number in user:
#   →     user_int.append(int(number))
#   → min_number = user_int[0]
#   → for number in user_int:
#   →     if number < min_number:
#   →         min_number = number
#   → result = min_number
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only find_min is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → find_min()  # jumps into find_min(), runs body, returns
#   → print(find_min(...))  # find_min() runs first → value goes to print()
#   → print(find_min(...))  # find_min() runs first → value goes to print()
#   → nums = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(find_min(...))  # find_min() runs first → value goes to print()
#
# Loop: takes one item from user, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 191 :
Écrivez une fonction Python appelée `find_min` qui prend une liste de nombres en entrée et retourne le minimum nombre dans la liste sans trié().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: ==
# Fonctions intégrées : Counter, filter, input, len, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → user = input('type element: ').lower()
#   → count = 0
#   → for word in lst:
#   →     if word.lower() == user:
#   →         count += 1
#   → if count == 0:
#   →     return 'not in lst'
#   → else:
#   →     return count
#   → return count
#   → return count
#   → return count
#   → return count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — count_occurrences, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → test_list = ...  # stored in memory
#   → element_to_count = ...  # stored in memory
#   → print('Number of occurrences of', element_to_count, ':', count_occurrences(...))
#   → lst = ...  # stored in memory
#   → print(main(...))  # main() runs first → value goes to print()
#   → print(count_occurrences(...))  # count_occurrences() runs first → value goes to print()
#   → print(count_occurrences(...))  # count_occurrences() runs first → value goes to print()
#   → print(count_occurrences(...))  # count_occurrences() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → element = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_occurrences(...))  # count_occurrences() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 192 :
Écrivez une fonction Python appelée count_occurrences qui prend une liste et un élément en entrée et retourne le nombre de fois élément apparaît dans la liste.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : input, int, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → user = input('type number: ').split()
#   → int_number = []
#   → for number in user:
#   →     int_number.append(int(number))
#   → min_num = sorted(int_number)[0]
#   → result = min_num
#   → return result
#   → user = input('type number: ').split()
#   → int_number = []
#   → for number in user:
#   →     int_number.append(int(number))
#   → min_num = sorted(int_number)[0]
#   → result = min_num
#   → return result
#   → user = input('type number: ').split()
#   → int_number = []
#   → for number in user:
#   →     int_number.append(int(number))
#   → min_num = sorted(int_number)[0]
#   → result = min_num
#   → return result
#   → user = input('type number: ').split()
#   → int_number = []
#   → for number in user:
#   →     int_number.append(int(number))
#   → min_num = sorted(int_number)[0]
#   → result = min_num
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only find_min_num is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → find_min_num()  # jumps into find_min_num(), runs body, returns
#   → print(find_min_num(...))  # find_min_num() runs first → value goes to print()
#   → print(find_min_num(...))  # find_min_num() runs first → value goes to print()
#   → nums = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(find_min_num(...))  # find_min_num() runs first → value goes to print()
#
# Loop: takes one item from user, runs body, repeats until done
"""
Problème 193 :
Écrivez une fonction Python appelée `find_min` qui prend une liste de nombres as utilisateur entrée et retourne le minimum nombre dans la liste. Utilisez trié().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: >=
# Fonctions intégrées : input, len, max, reduce, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → user = input('type list: ').split()
#   → largest_word = max(user, key=len)
#   → result = largest_word
#   → return result
#   → user = input('type list: ').split()
#   → largest_word = max(user, key=len)
#   → result = largest_word
#   → return result
#   → user = input('type list: ').split()
#   → largest_word = max(user, key=len)
#   → result = largest_word
#   → return result
#   → user = input('type list: ').split()
#   → largest_word = max(user, key=len)
#   → result = largest_word
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only largest_element is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → largest_element()  # jumps into largest_element(), runs body, returns
#   → print(largest_element(...))  # largest_element() runs first → value goes to print()
#   → print(largest_element(...))  # largest_element() runs first → value goes to print()
#   → words = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(largest_element(...))  # largest_element() runs first → value goes to print()
"""
Problème 194 :
Écrivez un programme Python à trouver le plus grand élément dans une liste. demander le utilisateur à saisir une liste d'éléments en utilisant max(). Write une liste de mots.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: < >
# Fonctions intégrées : input, len, nlargest, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → if len(words) < 2:
#   →     return None
#   → first = second = ''
#   → for w in words:
#   →     if len(w) > len(first):
#   →         second = first
#   →         first = w
#   →     elif len(w) > len(second):
#   →         second = w
#   → return second
#   → if len(words) < 2:
#   →     return None
#   → first = second = ''
#   → for w in words:
#   →     if len(w) > len(first):
#   →         second = first
#   →         first = w
#   →     elif len(w) > len(second):
#   →         second = w
#   → return second
#   → if len(words) < 2:
#   →     return None
#   → first = second = ''
#   → for w in words:
#   →     if len(w) > len(first):
#   →         second = first
#   →         first = w
#   →     elif len(w) > len(second):
#   →         second = w
#   → return second
#   → if len(words) < 2:
#   →     return None
#   → first = second = ''
#   → for w in words:
#   →     if len(w) > len(first):
#   →         second = first
#   →         first = w
#   →     elif len(w) > len(second):
#   →         second = w
#   → return second
#   → if len(words) < 2:
#   →     return None
#   → first = second = ''
#   → for w in words:
#   →     if len(w) > len(first):
#   →         second = first
#   →         first = w
#   →     elif len(w) > len(second):
#   →         second = w
#   → return second
#   → if len(words) < 2:
#   →     return None
#   → first = second = ''
#   → for w in words:
#   →     if len(w) > len(first):
#   →         second = first
#   →         first = w
#   →     elif len(w) > len(second):
#   →         second = w
#   → return second
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only second_largest_element is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → second_largest_element()  # jumps into second_largest_element(), runs body, returns
#   → second_largest_element()  # jumps into second_largest_element(), runs body, returns
#   → second_largest_element()  # jumps into second_largest_element(), runs body, returns
#   → print(second_largest_element(...))  # second_largest_element() runs first → value goes to print()
#   → print(second_largest_element(...))  # second_largest_element() runs first → value goes to print()
#   → words = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(second_largest_element(...))  # second_largest_element() runs first → value goes to print()
#
# Loop: takes one item from words, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 195 :
Écrivez un programme Python à trouver le deuxième plus grand élément dans une liste. demander le utilisateur à saisir une liste d'éléments. Write une liste de mots.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: > and
# Fonctions intégrées : list, max, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only max_of_three is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → three_numbers = ...  # stored in memory
#   → print(max_of_three(...))  # max_of_three() runs first → value goes to print()
#   → print(max_of_three(...))  # max_of_three() runs first → value goes to print()
#   → print(max_of_three(...))  # max_of_three() runs first → value goes to print()
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(max_of_three(...))  # max_of_three() runs first → value goes to print()
"""
Problème 196 :
Écrivez un programme Python à trouver le maximum de trois nombres. demander le utilisateur à saisir trois nombres. Utilisez max().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: >
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return max_number
#   → return max_number
#   → return max_number
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only max_of_three is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → three_numbers = ...  # stored in memory
#   → print(max_of_three(...))  # max_of_three() runs first → value goes to print()
#   → print(max_of_three(...))  # max_of_three() runs first → value goes to print()
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(max_of_three(...))  # max_of_three() runs first → value goes to print()
#
# Loop: takes one item from numbers, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 197 :
Écrivez un programme Python à trouver le maximum de trois nombres. saisir trois nombres dans une liste. sans en utilisant un build dans fuctions apart de print().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: *
# Fonctions intégrées : input, int, round()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → cm = int(input('type centimeters: '))
#   → inches = cm * 0.3937
#   → result = f'{cm} cm = {inches} inches'
#   → return result
#   → cm = int(input('type centimeters: '))
#   → inches = cm * 0.3937
#   → result = f'{cm} cm = {inches} inches'
#   → return result
#   → return cm * 0.3937
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — centimeters_inches, cm_to_inches are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → centimeters_inches()  # jumps into centimeters_inches(), runs body, returns
#   → print(?)
#   → print(centimeters_inches(...))  # centimeters_inches() runs first → value goes to print()
#   → cm = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(cm_to_inches(...))  # cm_to_inches() runs first → value goes to print()
"""
Problème 198 :
Écrivez une fonction qui convertit centimetets à inches.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: < >
# Fonctions intégrées : input, int, max, min, reduce, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → user = input('type list of numbers: ').split()
#   → int_num = []
#   → for number in user:
#   →     int_num.append(int(number))
#   → min_num = min(int_num)
#   → max_num = max(int_num)
#   → result = (min_num, max_num)
#   → return result
#   → user = input('type list of numbers: ').split()
#   → int_num = []
#   → for number in user:
#   →     int_num.append(int(number))
#   → min_num = min(int_num)
#   → max_num = max(int_num)
#   → result = (min_num, max_num)
#   → return result
#   → user = input('type list of numbers: ').split()
#   → int_num = []
#   → for number in user:
#   →     int_num.append(int(number))
#   → min_num = min(int_num)
#   → max_num = max(int_num)
#   → result = (min_num, max_num)
#   → return result
#   → user = input('type list of numbers: ').split()
#   → int_num = []
#   → for number in user:
#   →     int_num.append(int(number))
#   → min_num = min(int_num)
#   → max_num = max(int_num)
#   → result = (min_num, max_num)
#   → return result
#   → user = input('type list of numbers: ').split()
#   → int_num = []
#   → for number in user:
#   →     int_num.append(int(number))
#   → min_num = min(int_num)
#   → max_num = max(int_num)
#   → result = (min_num, max_num)
#   → return result
#   → user = input('type list of numbers: ').split()
#   → int_num = []
#   → for number in user:
#   →     int_num.append(int(number))
#   → min_num = min(int_num)
#   → max_num = max(int_num)
#   → result = (min_num, max_num)
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only find_min_max is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → find_min_max()  # jumps into find_min_max(), runs body, returns
#   → find_min_max()  # jumps into find_min_max(), runs body, returns
#   → print(find_min_max(...))  # find_min_max() runs first → value goes to print()
#   → print(find_min_max(...))  # find_min_max() runs first → value goes to print()
#   → print(find_min_max(...))  # find_min_max() runs first → value goes to print()
#   → nums = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(find_min_max(...))  # find_min_max() runs first → value goes to print()
#
# Loop: takes one item from user, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 199 :
Écrivez une fonction Python appelée find_min_max qui prend une liste de nombres en entrée et retourne un tuple contenant le minimum et maximum nombres dans la liste, dont pas call le fuction en utilisant print(find_min_max). N'utilisez pas trier().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: + > in and not in
# Fonctions intégrées : Counter, list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(lambda number: number, lst))
#   → return list(map(lambda number: number, lst))
#   → return list(map(lambda number: number, lst))
#   → return list(map(lambda number: number, lst))
#   → return list(map(lambda number: number, lst))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only common_numbers is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(common_numbers(...))  # common_numbers() runs first → value goes to print()
#   → print(common_numbers(...))  # common_numbers() runs first → value goes to print()
#   → print(common_numbers(...))  # common_numbers() runs first → value goes to print()
#   → print(common_numbers(...))  # common_numbers() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(common_numbers(...))  # common_numbers() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 200 :
Écrivez un programme Python à trouver le commun nombre dans un listes. pour cette exercise N'utilisez pas set.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: + > in
# Fonctions intégrées : Counter, list, map, set()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(lambda number: number, lst))
#   → from collections import Counter
#   → return [k for k, v in Counter(lst).items() if v > 1]
#   → from collections import Counter
#   → return [k for k, v in Counter(lst).items() if v > 1]
#   → from collections import Counter
#   → return [k for k, v in Counter(lst).items() if v > 1]
#   → from collections import Counter
#   → return [k for k, v in Counter(lst).items() if v > 1]
#   → return list(map(lambda number: number, lst))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — common_num, common_numbers are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(common_num(...))  # common_num() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → print(common_numbers(...))  # common_numbers() runs first → value goes to print()
#   → print(common_numbers(...))  # common_numbers() runs first → value goes to print()
#   → print(common_numbers(...))  # common_numbers() runs first → value goes to print()
#   → print(common_numbers(...))  # common_numbers() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(common_num(...))  # common_num() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 201 :
Écrivez un programme Python à trouver le commun nombre dans un listes. Utilisez set().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: + in
# Fonctions intégrées : Counter, dict, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only word_frequency is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → string = ...  # stored in memory
#   → print(word_frequency(...))  # word_frequency() runs first → value goes to print()
#   → print(word_frequency(...))  # word_frequency() runs first → value goes to print()
#   → print(word_frequency(...))  # word_frequency() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(word_frequency(...))  # word_frequency() runs first → value goes to print()
#
# Loop: takes one item from sort_char, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 202 :
Écrivez une fonction word_frequency qui prend une chaîne en entrée et retourne un dictionnaire où le clés sont le caractères dans la chaîne et le valeurs sont le compte de ces caractères alphabetically.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: *
# Fonctions intégrées : reduce, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return (total_numbers, multiply_numbers)
#   → return (total_numbers, multiply_numbers)
#   → return (total_numbers, multiply_numbers)
#   → return (total_numbers, multiply_numbers)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only total is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst_numbers = ...  # stored in memory
#   → print(total(...))  # total() runs first → value goes to print()
#   → print(total(...))  # total() runs first → value goes to print()
#   → print(total(...))  # total() runs first → value goes to print()
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(total(...))  # total() runs first → value goes to print()
#
# Loop: takes one item from numbers, runs body, repeats until done
"""
Problème 203 :
Définissez une fonction total() qui sums et multiplie (respectively) tous le nombres dans une liste de nombres. par exemple, sum([1, 2, 3, 4]) devrait retourner 10, et multiply([1, 2, 3, 4]) devrait retourner 24.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : len, list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(lambda word: word, lst))
#   → return list(map(lambda word: word, lst))
#   → return list(map(lambda word: word, lst))
#   → return list(map(lambda word: word, lst))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only list_integers is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(list_integers(...))  # list_integers() runs first → value goes to print()
#   → print(list_integers(...))  # list_integers() runs first → value goes to print()
#   → print(list_integers(...))  # list_integers() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(list_integers(...))  # list_integers() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
"""
Problème 204 :
Écrivez un programme qui maps une liste de mots dans une liste d'entiers representing le words avec le lengths de le correponding words.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: * /
# Fonctions intégrées : Fraction, float, len, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → from fractions import Fraction
#   → return float(Fraction(sum_lst, length))
#   → from fractions import Fraction
#   → return float(Fraction(sum_lst, length))
#   → from fractions import Fraction
#   → return float(Fraction(sum_lst, length))
#   → from fractions import Fraction
#   → return float(Fraction(sum_lst, length))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only average is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(average(...))  # average() runs first → value goes to print()
#   → print(average(...))  # average() runs first → value goes to print()
#   → print(average(...))  # average() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(average(...))  # average() runs first → value goes to print()
"""
Problème 205 :
Écrivez une fonction Python appelée `calculate_average` qui prend une liste de nombres en entrée et retourne le moyenne de ces nombres. Utilisez len() et sum().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: > !=
# Fonctions intégrées : input, int, len()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → numbers = [int(value) for value in input('Enter three numbers: ').split()]
#   → if len(numbers) != 3:
#   →     print('not enough numbers')
#   →     return
#   → largest = numbers[0]
#   → for number in numbers[1:]:
#   →     if number > largest:
#   →         largest = number
#   → print(largest)
# if ... → only one branch executes based on condition
# if ... → only one branch executes based on condition
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only max_of_three is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → max_of_three()  # jumps into max_of_three(), runs body, returns
#   → numbers = ...  # stored in memory
#   → if condition  # evaluates → runs the True branch
#   → largest = ...  # stored in memory
#   → for number in ?  # runs body once per item
#   → print(largest)
#   → numbers = ...  # stored in memory
#   → if condition  # evaluates → runs the True branch
#   → largest = ...  # stored in memory
#   → for number in ?  # runs body once per item
#   → print(largest)
#
# Loop: takes one item from ?, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 206 :
Écrivez un programme Python à trouver le maximum de trois nombres. demander le utilisateur à saisir trois nombres. N'utilisez pas max().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: > !=
# Fonctions intégrées : input, int, len, reduce, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → from functools import reduce
#   → return reduce(lambda a, b: a if a > b else b, nums)
#   → from functools import reduce
#   → return reduce(lambda a, b: a if a > b else b, nums)
#   → from functools import reduce
#   → return reduce(lambda a, b: a if a > b else b, nums)
#   → from functools import reduce
#   → return reduce(lambda a, b: a if a > b else b, nums)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only max_of_list is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → max_of_list()  # jumps into max_of_list(), runs body, returns
#   → print(max_of_list(...))  # max_of_list() runs first → value goes to print()
#   → print(max_of_list(...))  # max_of_list() runs first → value goes to print()
#   → nums = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(max_of_list(...))  # max_of_list() runs first → value goes to print()
#
# Loop: takes one item from user, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 207 :
Écrivez un programme Python à trouver le maximum de de list de nombres. demander le utilisateur à saisir trois nombres. N'utilisez pas max().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : input, int, max, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → user = input('type three numbers: ').split()
#   → int_numbers = []
#   → for number in user:
#   →     int_numbers.append(int(number))
#   → max_number = max(int_numbers)
#   → result = max_number
#   → return result
#   → user = input('type three numbers: ').split()
#   → int_numbers = []
#   → for number in user:
#   →     int_numbers.append(int(number))
#   → max_number = max(int_numbers)
#   → result = max_number
#   → return result
#   → user = input('type three numbers: ').split()
#   → int_numbers = []
#   → for number in user:
#   →     int_numbers.append(int(number))
#   → max_number = max(int_numbers)
#   → result = max_number
#   → return result
#   → user = input('type three numbers: ').split()
#   → int_numbers = []
#   → for number in user:
#   →     int_numbers.append(int(number))
#   → max_number = max(int_numbers)
#   → result = max_number
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only max_of_list is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → max_of_list()  # jumps into max_of_list(), runs body, returns
#   → print(max_of_list(...))  # max_of_list() runs first → value goes to print()
#   → print(max_of_list(...))  # max_of_list() runs first → value goes to print()
#   → nums = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(max_of_list(...))  # max_of_list() runs first → value goes to print()
#
# Loop: takes one item from user, runs body, repeats until done
"""
Problème 208 :
Écrivez un programme Python à trouver le maximum de de list de nombres. demander le utilisateur à saisir trois nombres. Utilisez max().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : len, list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(lambda word: word, lst))
#   → return list(map(lambda word: word, lst))
#   → return list(map(lambda word: word, lst))
#   → return list(map(lambda word: word, lst))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only list_words is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(list_words(...))  # list_words() runs first → value goes to print()
#   → print(list_words(...))  # list_words() runs first → value goes to print()
#   → print(list_words(...))  # list_words() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(list_words(...))  # list_words() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
"""
Problème 209 :
Écrivez un programme qui maps une liste de mots dans une liste d'entiers representing le lengths de le correponding words avec le mot par exemple ['jonathan', 8,'horse', 5,'today', 5 ].
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : enumerate, list, map, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(lambda word: word, lst))
#   → return list(map(lambda word: word, lst))
#   → return list(map(lambda word: word, lst))
#   → return list(map(lambda word: word, lst))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only list_words is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(list_words(...))  # list_words() runs first → value goes to print()
#   → print(list_words(...))  # list_words() runs first → value goes to print()
#   → print(list_words(...))  # list_words() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(list_words(...))  # list_words() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
"""
Problème 210 :
Écrivez un programme qui maps une liste de mots dans une liste d'entiers representing le lengths de le correponding words avec le mot par exemple ['jonathan', 8,'horse', 5,'today', 5 ]. N'utilisez pas len().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: +
# Fonctions intégrées : enumerate, list, map, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(lambda word: count, lst))
#   → return list(map(lambda word: count, lst))
#   → return list(map(lambda word: count, lst))
#   → return list(map(lambda word: count, lst))
#   → return list(map(lambda word: count, lst))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — len_manual, length_words are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(length_words(...))  # length_words() runs first → value goes to print()
#   → print(length_words(...))  # length_words() runs first → value goes to print()
#   → print(length_words(...))  # length_words() runs first → value goes to print()
#   → print(length_words(...))  # length_words() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(length_words(...))  # length_words() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
"""
Problème 211 :
Écrivez un programme qui maps une liste de mots dans une liste d'entiers representing le lengths de le correponding words sans en utilisant len().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: in
# Fonctions intégrées : filter, input, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → lst1 = input('type lst1: ').split()
#   → lst2 = input('type lst2: ').split()
#   → common = []
#   → for word in lst1:
#   →     if word in lst2:
#   →         common.append(word)
#   → result = common
#   → return result
#   → lst1 = input('type lst1: ').split()
#   → lst2 = input('type lst2: ').split()
#   → common = []
#   → for word in lst1:
#   →     if word in lst2:
#   →         common.append(word)
#   → result = common
#   → return result
#   → lst1 = input('type lst1: ').split()
#   → lst2 = input('type lst2: ').split()
#   → common = []
#   → for word in lst1:
#   →     if word in lst2:
#   →         common.append(word)
#   → result = common
#   → return result
#   → lst1 = input('type lst1: ').split()
#   → lst2 = input('type lst2: ').split()
#   → common = []
#   → for word in lst1:
#   →     if word in lst2:
#   →         common.append(word)
#   → result = common
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only intersection is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → intersection()  # jumps into intersection(), runs body, returns
#   → print(intersection(...))  # intersection() runs first → value goes to print()
#   → print(intersection(...))  # intersection() runs first → value goes to print()
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(intersection(...))  # intersection() runs first → value goes to print()
#
# Loop: takes one item from lst1, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 212 :
Écrivez un programme Python à trouver le l'intersection des deux listes. demander le utilisateur à saisir deux listes sans en utilisant set() et sans en utilisant l'intersection().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: *
# Fonctions intégrées : range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → for i in range(...)  # runs body once per item
#   → for i in range(...)  # runs body once per item
#   → for i in range(...)  # runs body once per item
#   → for i in range(...)  # runs body once per item
#   → for i in range(...)  # runs body once per item
#
# Loop: takes one item from range(...), runs body, repeats until done
"""
Problème 213 :
Écrivez un programme Python à print le following motif:\
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
# Keywords: for
# Operators: * +
# Fonctions intégrées : range, str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
#
# Execution starts at the top-level code (outside def/class):
#   → for i in range(...)  # runs body once per item
#   → for i in range(...)  # runs body once per item
#   → for i in range(...)  # runs body once per item
#
# Loop: takes one item from range(...), runs body, repeats until done
"""
Problème 214 :
Écrivez un programme Python à print le following nombre pyramid:\
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
# Keywords: for
# Operators: +
# Fonctions intégrées : map, range, str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
#
# Execution starts at the top-level code (outside def/class):
#   → for i in range(...)  # runs body once per item
#   → for i in range(...)  # runs body once per item
#   → for i in range(...)  # runs body once per item
#
# Loop: takes one item from range(...), runs body, repeats until done
"""
Problème 216 :
Écrivez un programme Python à print un right-angled triangle de nombres:\
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: *
# Fonctions intégrées : range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → for i in range(...)  # runs body once per item
#   → for i in range(...)  # runs body once per item
#   → for i in range(...)  # runs body once per item
#   → for i in range(...)  # runs body once per item
#   → for i in range(...)  # runs body once per item
#
# Loop: takes one item from range(...), runs body, repeats until done
"""
Problème 217 :
Écrivez un programme Python à print an inverted pyramid motif:\
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: % * + ==
# Fonctions intégrées : input, int, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → for i in range(size):
#   →     if i % 2 == 0:
#   →         print('* ' * size)
#   →     else:
#   →         print(' *' * size)
#   → for i in range(size):
#   →     if i % 2 == 0:
#   →         print('* ' * size)
#   →     else:
#   →         print(' *' * size)
#   → for i in range(size):
#   →     if i % 2 == 0:
#   →         print('* ' * size)
#   →     else:
#   →         print(' *' * size)
#   → for i in range(size):
#   →     if i % 2 == 0:
#   →         print('* ' * size)
#   →     else:
#   →         print(' *' * size)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — print_checkerboard, solve are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → size = ...  # stored in memory
#   → print_checkerboard(size)  # jumps into print_checkerboard(), runs body, returns
#   → print_checkerboard(4)  # jumps into print_checkerboard(), runs body, returns
#   → print_checkerboard(4)  # jumps into print_checkerboard(), runs body, returns
#   → size = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(print_checkerboard(...))  # print_checkerboard() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 218 :
Écrivez un programme Python à print un checkerboard motif de donné size.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | while
# Operators: + <=
# Fonctions intégrées : range, str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → num = 1
#   → for i in range(1, rows + 1):
#   →     print(' '.join((str(num + j) for j in range(i))))
#   →     num += i
#   → num = 1
#   → for i in range(1, rows + 1):
#   →     print(' '.join((str(num + j) for j in range(i))))
#   →     num += i
#   → num = 1
#   → for i in range(1, rows + 1):
#   →     print(' '.join((str(num + j) for j in range(i))))
#   →     num += i
#   → num = 1
#   → for i in range(1, rows + 1):
#   →     print(' '.join((str(num + j) for j in range(i))))
#   →     num += i
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — print_floyds_triangle, solve are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → rows = ...  # stored in memory
#   → print_floyds_triangle(rows)  # jumps into print_floyds_triangle(), runs body, returns
#   → print_floyds_triangle(4)  # jumps into print_floyds_triangle(), runs body, returns
#   → print_floyds_triangle(4)  # jumps into print_floyds_triangle(), runs body, returns
#   → rows = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(print_floyds_triangle(...))  # print_floyds_triangle() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
"""
Problème 219 :
Écrivez un programme Python à print Floyd's Triangle.\
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: +
# Fonctions intégrées : map, range, str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → for i in range(rows, 0, -1):
#   →     print(' '.join((str(j) for j in range(1, i + 1))))
#   → for i in range(rows, 0, -1):
#   →     print(' '.join((str(j) for j in range(1, i + 1))))
#   → for i in range(rows, 0, -1):
#   →     print(' '.join((str(j) for j in range(1, i + 1))))
#   → for i in range(rows, 0, -1):
#   →     print(' '.join((str(j) for j in range(1, i + 1))))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — print_reverse_pyramid, solve are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → rows = ...  # stored in memory
#   → print_reverse_pyramid(rows)  # jumps into print_reverse_pyramid(), runs body, returns
#   → print_reverse_pyramid(5)  # jumps into print_reverse_pyramid(), runs body, returns
#   → print_reverse_pyramid(5)  # jumps into print_reverse_pyramid(), runs body, returns
#   → rows = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(print_reverse_pyramid(...))  # print_reverse_pyramid() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
"""
Problème 222 :
Écrivez un programme Python à print un reverse pyramid motif de nombres:\
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: % * + - // == or and
# Fonctions intégrées : range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → for i in range(rows):
#   →     if i % 2 == 0:
#   →         print('*   ' * (rows // 2 + 1))
#   →     else:
#   →         print(' * *' * (rows // 2 + 1))
#   → for i in range(rows):
#   →     if i % 2 == 0:
#   →         print('*   ' * (rows // 2 + 1))
#   →     else:
#   →         print(' * *' * (rows // 2 + 1))
#   → for i in range(rows):
#   →     if i % 2 == 0:
#   →         print('*   ' * (rows // 2 + 1))
#   →     else:
#   →         print(' * *' * (rows // 2 + 1))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — print_zigzag, solve are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → rows = ...  # stored in memory
#   → print_zigzag(rows)  # jumps into print_zigzag(), runs body, returns
#   → print_zigzag(5)  # jumps into print_zigzag(), runs body, returns
#   → rows = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(print_zigzag(...))  # print_zigzag() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 227 :
Écrivez un programme Python à print un zigzag motif de stars pour une donnée nombre de rows.\
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: * + - // == or
# Fonctions intégrées : abs, min, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → for i in range(rows):
#   →     print(''.join(('*' if j == i or j == rows - 1 - i else ' ' for j in range(rows))))
#   → for i in range(rows):
#   →     print(''.join(('*' if j == i or j == rows - 1 - i else ' ' for j in range(rows))))
#   → for i in range(rows):
#   →     print(''.join(('*' if j == i or j == rows - 1 - i else ' ' for j in range(rows))))
#   → for i in range(rows):
#   →     print(''.join(('*' if j == i or j == rows - 1 - i else ' ' for j in range(rows))))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — print_cross, solve are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → rows = ...  # stored in memory
#   → print_cross(rows)  # jumps into print_cross(), runs body, returns
#   → print_cross(5)  # jumps into print_cross(), runs body, returns
#   → print_cross(5)  # jumps into print_cross(), runs body, returns
#   → rows = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(print_cross(...))  # print_cross() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 228 :
Écrivez un programme Python à print un cross motif de stars pour une donnée impair nombre de rows.\
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: + in
# Fonctions intégrées : Counter, dict()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#   → return result
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_occurrences is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(count_occurrences(...))  # count_occurrences() runs first → value goes to print()
#   → print(count_occurrences(...))  # count_occurrences() runs first → value goes to print()
#   → print(count_occurrences(...))  # count_occurrences() runs first → value goes to print()
#   → print(count_occurrences(...))  # count_occurrences() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_occurrences(...))  # count_occurrences() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 230 :
Écrivez une fonction Python appelée count_occurrences qui prend une liste d'éléments en entrée et retourne le nombre de fois éléments apparaît dans la liste.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: % !=
# Fonctions intégrées : filter, input, int, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → user = input('type numbers: ').split()
#   → count = 0
#   → for number in user:
#   →     number = int(number)
#   →     if number % 2 != 0:
#   →         count += number
#   → result = count
#   → return result
#   → user = input('type numbers: ').split()
#   → count = 0
#   → for number in user:
#   →     number = int(number)
#   →     if number % 2 != 0:
#   →         count += number
#   → result = count
#   → return result
#   → user = input('type numbers: ').split()
#   → count = 0
#   → for number in user:
#   →     number = int(number)
#   →     if number % 2 != 0:
#   →         count += number
#   → result = count
#   → return result
#   → user = input('type numbers: ').split()
#   → count = 0
#   → for number in user:
#   →     number = int(number)
#   →     if number % 2 != 0:
#   →         count += number
#   → result = count
#   → return result
#   → user = input('type numbers: ').split()
#   → count = 0
#   → for number in user:
#   →     number = int(number)
#   →     if number % 2 != 0:
#   →         count += number
#   → result = count
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sum_of_odd is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → sum_of_odd()  # jumps into sum_of_odd(), runs body, returns
#   → print(sum_of_odd(...))  # sum_of_odd() runs first → value goes to print()
#   → print(sum_of_odd(...))  # sum_of_odd() runs first → value goes to print()
#   → print(sum_of_odd(...))  # sum_of_odd() runs first → value goes to print()
#   → nums = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sum_of_odd(...))  # sum_of_odd() runs first → value goes to print()
#
# Loop: takes one item from user, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 231 :
Écrivez un programme Python à trouver le somme de tous les nombres impairs dans une liste. demander le utilisateur à saisir une liste de nombres. Write la fonction as trier as possible.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: not in
# Fonctions intégrées : filter, input()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → import re
#   → return re.sub('[aeiouAEIOU]', '', s)
#   → import re
#   → return re.sub('[aeiouAEIOU]', '', s)
#   → import re
#   → return re.sub('[aeiouAEIOU]', '', s)
#   → import re
#   → return re.sub('[aeiouAEIOU]', '', s)
#   → import re
#   → return re.sub('[aeiouAEIOU]', '', s)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only remove_vowels is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → remove_vowels()  # jumps into remove_vowels(), runs body, returns
#   → print(remove_vowels(...))  # remove_vowels() runs first → value goes to print()
#   → print(remove_vowels(...))  # remove_vowels() runs first → value goes to print()
#   → print(remove_vowels(...))  # remove_vowels() runs first → value goes to print()
#   → s = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(remove_vowels(...))  # remove_vowels() runs first → value goes to print()
#
# Loop: takes one item from user, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 232 :
Écrivez un programme Python à remove voyelles de une chaîne. demander le utilisateur à saisir une chaîne. N'utilisez pas append().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else | while
# Operators: <
# Fonctions intégrées : len, reduce, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return min_num
#   → return min_num
#   → return min_num
#   → return min_num
#   → return min_num
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only find_min is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(find_min(...))  # find_min() runs first → value goes to print()
#   → print(find_min(...))  # find_min() runs first → value goes to print()
#   → print(find_min(...))  # find_min() runs first → value goes to print()
#   → print(find_min(...))  # find_min() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(find_min(...))  # find_min() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 233 :
Écrivez une fonction Python appelée `find_min` qui prend une liste de nombres en entrée et retourne le minimum nombre dans la liste. N'utilisez pas min().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: while
# Operators: * <
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
# while ... → repeats as long as condition is true
#   → i = 0
#   → while i < n:
#   →     j = 0
#   →     while j < n:
#   →         print('*', end=' ')
#   →         j += 1
#   →     print()
#   →     i += 1
#   → i = 0
#   → while i < n:
#   →     j = 0
#   →     while j < n:
#   →         print('*', end=' ')
#   →         j += 1
#   →     print()
#   →     i += 1
#   → i = 0
#   → while i < n:
#   →     j = 0
#   →     while j < n:
#   →         print('*', end=' ')
#   →         j += 1
#   →     print()
#   →     i += 1
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — print_square, solve are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → i = ...  # stored in memory
#   → print_square(5)  # jumps into print_square(), runs body, returns
#   → print_square(5)  # jumps into print_square(), runs body, returns
#   → n = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(print_square(...))  # print_square() runs first → value goes to print()
#
# Loop: check condition → if True run body → check again
"""
Problème 234 :
Écrivez un programme Python à print un carré motif de stars avec une donnée side longueur. Utilisez un tandis que loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: *
# Fonctions intégrées : increasing_triangle, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → for i in range(5, 0, -1):
#   →     for j in range(i):
#   →         print('*', end=' ')
#   →     print()
#   → for i in range(5, 0, -1):
#   →     for j in range(i):
#   →         print('*', end=' ')
#   →     print()
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — decreasing_triangle, solve are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(increasing_triangle(...))
#   → decreasing_triangle()  # jumps into decreasing_triangle(), runs body, returns
#   → decreasing_triangle()  # jumps into decreasing_triangle(), runs body, returns
#   → n = ...  # stored in memory
#   → for i in range(...)  # runs body once per item
#   → n = ...  # stored in memory
#   → for i in range(...)  # runs body once per item
#
# Loop: takes one item from range(...), runs body, repeats until done
"""
Problème 236 :
Écrivez un programme Python qui affiche un decreasing triangle motif de stars.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: * + -
# Fonctions intégrées : increasing_triangle, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → n = 5
#   → for i in range(1, n + 1):
#   →     print(('* ' * i).rjust(n * 2))
#   → n = 5
#   → for i in range(1, n + 1):
#   →     print(('* ' * i).rjust(n * 2))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — left_triangle, solve are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(increasing_triangle(...))
#   → left_triangle()  # jumps into left_triangle(), runs body, returns
#   → left_triangle()  # jumps into left_triangle(), runs body, returns
#   → n = ...  # stored in memory
#   → for i in range(...)  # runs body once per item
#   → for i in range(...)  # runs body once per item
#   → n = ...  # stored in memory
#   → for i in range(...)  # runs body once per item
#   → for i in range(...)  # runs body once per item
#
# Loop: takes one item from range(...), runs body, repeats until done
"""
Problème 238 :
Écrivez un programme Python qui affiche un left triangle motif de stars.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : enumerate, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only enumerate_lst is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(enumerate_lst(...))  # enumerate_lst() runs first → value goes to print()
#   → print(enumerate_lst(...))  # enumerate_lst() runs first → value goes to print()
#   → print(enumerate_lst(...))  # enumerate_lst() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(enumerate_lst(...))  # enumerate_lst() runs first → value goes to print()
#
# Loop: takes one item from enumerate(...), runs body, repeats until done
"""
Problème 242 :
Écrivez un programme Python à créer une liste de tuples où chaque tuple contient le index et le valeur de une donnée list en utilisant `enumerate()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: ==
# Fonctions intégrées : enumerate, next()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return (word, index)
#   → return next(((v, i) for i, v in enumerate(lst) if v == target), -1)
#   → return next(((v, i) for i, v in enumerate(lst) if v == target), -1)
#   → return (word, index)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — enumerate_lst, find_first are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → target = ...  # stored in memory
#   → lst = ...  # stored in memory
#   → print(enumerate_lst(...))  # enumerate_lst() runs first → value goes to print()
#   → print(find_first(...))  # find_first() runs first → value goes to print()
#   → print(find_first(...))  # find_first() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → target = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(enumerate_lst(...))  # enumerate_lst() runs first → value goes to print()
#
# Loop: takes one item from enumerate(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 243 :
Écrivez un programme Python à trouver le index de le premier occurrence de un spécifique valeur dans une liste en utilisant `enumerate()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: +
# Fonctions intégrées : enumerate, len, range, zip()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → for i, v in zip(range(1, len(lst) + 1), lst):
#   →     print(f'Index {i}, Name {v}')
#   → for i, v in zip(range(1, len(lst) + 1), lst):
#   →     print(f'Index {i}, Name {v}')
#   → for i, v in zip(range(1, len(lst) + 1), lst):
#   →     print(f'Index {i}, Name {v}')
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — enumerate_lst, solve are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → enumerate_lst(lst)  # jumps into enumerate_lst(), runs body, returns
#   → for s in enumerate_lst(...)  # runs body once per item
#   → enumerate_lst(?)  # jumps into enumerate_lst(), runs body, returns
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(enumerate_lst(...))  # enumerate_lst() runs first → value goes to print()
#
# Loop: takes one item from enumerate_lst(...), runs body, repeats until done
"""
Problème 244 :
Écrivez un programme Python à print le index et valeur de chaque élément dans une liste starting de index 1 en utilisant `enumerate()`
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : dict, enumerate()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → result = {}
#   → for index, word in enumerate(lst):
#   →     result[index] = word
#   → result = result
#   → return result
#   → result = {}
#   → for index, word in enumerate(lst):
#   →     result[index] = word
#   → result = result
#   → return result
#   → result = {}
#   → for index, word in enumerate(lst):
#   →     result[index] = word
#   → result = result
#   → return result
#   → result = {}
#   → for index, word in enumerate(lst):
#   →     result[index] = word
#   → result = result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only enumerate_lst is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → enumerate_lst(lst)  # jumps into enumerate_lst(), runs body, returns
#   → print(enumerate_lst(...))  # enumerate_lst() runs first → value goes to print()
#   → print(enumerate_lst(...))  # enumerate_lst() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(enumerate_lst(...))  # enumerate_lst() runs first → value goes to print()
#
# Loop: takes one item from enumerate(...), runs body, repeats until done
"""
Problème 245 :
Écrivez un programme Python à créer un dictionnaire où clés sont le indexes et valeurs sont le corresponding éléments de une liste en utilisant `enumerate()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: % !=
# Fonctions intégrées : enumerate, len, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return [(i, lst[i]) for i in range(0, len(lst), 2)]
#   → return [(i, lst[i]) for i in range(0, len(lst), 2)]
#   → return [(i, lst[i]) for i in range(0, len(lst), 2)]
#   → return [(i, lst[i]) for i in range(0, len(lst), 2)]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — enumerate_lst, solve are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → enumerate_lst(lst)  # jumps into enumerate_lst(), runs body, returns
#   → enumerate_lst(?)  # jumps into enumerate_lst(), runs body, returns
#   → print(enumerate_lst(...))  # enumerate_lst() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(enumerate_lst(...))  # enumerate_lst() runs first → value goes to print()
#
# Loop: takes one item from enumerate(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 246 :
Écrivez un programme Python à filtrer et print éléments de une liste qui sont at même indexes en utilisant `enumerate()`
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : enumerate, len, list, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return lst
#   → return lst
#   → return lst
#   → return lst
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only replace_with_index is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(replace_with_index(...))  # replace_with_index() runs first → value goes to print()
#   → print(replace_with_index(...))  # replace_with_index() runs first → value goes to print()
#   → print(replace_with_index(...))  # replace_with_index() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(replace_with_index(...))  # replace_with_index() runs first → value goes to print()
#
# Loop: takes one item from enumerate(...), runs body, repeats until done
"""
Problème 248 :
Écrivez un programme Python à replace chaque élément dans une liste avec ses index en utilisant `enumerate()`
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: % !=
# Fonctions intégrées : enumerate, len, range, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return total
#   → return total
#   → return total
#   → return total
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sum_odd_indexed_elements is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sum_odd_indexed_elements(...))  # sum_odd_indexed_elements() runs first → value goes to print()
#   → print(sum_odd_indexed_elements(...))  # sum_odd_indexed_elements() runs first → value goes to print()
#   → print(sum_odd_indexed_elements(...))  # sum_odd_indexed_elements() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sum_odd_indexed_elements(...))  # sum_odd_indexed_elements() runs first → value goes to print()
#
# Loop: takes one item from enumerate(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 250 :
Écrivez un programme Python à calculate le somme d'éléments dans une liste qui sont located at impair indexes en utilisant `enumerate()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : len, list, range, zip()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return paired
#   → return paired
#   → return paired
#   → return paired
#   → return paired
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only pair_elements is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → print(pair_elements(...))  # pair_elements() runs first → value goes to print()
#   → print(pair_elements(...))  # pair_elements() runs first → value goes to print()
#   → print(pair_elements(...))  # pair_elements() runs first → value goes to print()
#   → print(pair_elements(...))  # pair_elements() runs first → value goes to print()
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(pair_elements(...))  # pair_elements() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
"""
Problème 251 :
Écrivez un programme Python à pair éléments des deux listes de equal longueur en utilisant `zip()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: +
# Fonctions intégrées : len, list, map, range, zip()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return summed_list
#   → return summed_list
#   → return summed_list
#   → return summed_list
#   → return summed_list
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sum_of_2_lst is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → print(sum_of_2_lst(...))  # sum_of_2_lst() runs first → value goes to print()
#   → print(sum_of_2_lst(...))  # sum_of_2_lst() runs first → value goes to print()
#   → print(sum_of_2_lst(...))  # sum_of_2_lst() runs first → value goes to print()
#   → print(sum_of_2_lst(...))  # sum_of_2_lst() runs first → value goes to print()
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sum_of_2_lst(...))  # sum_of_2_lst() runs first → value goes to print()
#
# Loop: takes one item from zip(...), runs body, repeats until done
"""
Problème 252 :
Écrivez un programme Python à trouver le somme de corresponding éléments des deux listes en utilisant `zip()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: + - >
# Fonctions intégrées : itemgetter, len, list, range, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sorted(tuples_list, key=lambda x: x[1])
#   → return sorted(tuples_list, key=lambda x: x[1])
#   → return sorted(tuples_list, key=lambda x: x[1])
#   → return sorted(tuples_list, key=lambda x: x[1])
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_tuples_by_second is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → tuples_list = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_tuples_by_second(...))  # sort_tuples_by_second() runs first → value goes to print()
#   → print(sort_tuples_by_second(...))  # sort_tuples_by_second() runs first → value goes to print()
#   → print(sort_tuples_by_second(...))  # sort_tuples_by_second() runs first → value goes to print()
#   → tuples_list = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_tuples_by_second(...))  # sort_tuples_by_second() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 253 :
Write un Python fonction à trier une liste de tuples by le deuxième élément dans chaque tuple en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : dict, len, range, zip()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#   → return result
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only dic_lst is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → print(dic_lst(...))  # dic_lst() runs first → value goes to print()
#   → print(dic_lst(...))  # dic_lst() runs first → value goes to print()
#   → print(dic_lst(...))  # dic_lst() runs first → value goes to print()
#   → print(dic_lst(...))  # dic_lst() runs first → value goes to print()
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(dic_lst(...))  # dic_lst() runs first → value goes to print()
#
# Loop: takes one item from zip(...), runs body, repeats until done
"""
Problème 254 :
Écrivez un programme Python à créer un dictionnaire des deux listes, l'une pour clés et l'une pour valeurs, en utilisant `zip()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : len, list, range, zip()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#   → return result
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only combine_3_lst is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → lst3 = ...  # stored in memory
#   → print(combine_3_lst(...))  # combine_3_lst() runs first → value goes to print()
#   → print(combine_3_lst(...))  # combine_3_lst() runs first → value goes to print()
#   → print(combine_3_lst(...))  # combine_3_lst() runs first → value goes to print()
#   → print(combine_3_lst(...))  # combine_3_lst() runs first → value goes to print()
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → lst3 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(combine_3_lst(...))  # combine_3_lst() runs first → value goes to print()
#
# Loop: takes one item from zip(...), runs body, repeats until done
"""
Problème 255 :
Écrivez un programme Python à combiner trois listes dans une liste de tuples en utilisant `zip()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: *
# Fonctions intégrées : len, list, range, zip()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#   → return result
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only transpose_matrix is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → matrix = ...  # stored in memory
#   → print(transpose_matrix(...))  # transpose_matrix() runs first → value goes to print()
#   → matrix = ...  # stored in memory
#   → print(transpose_matrix(...))  # transpose_matrix() runs first → value goes to print()
#   → matrix = ...  # stored in memory
#   → print(transpose_matrix(...))  # transpose_matrix() runs first → value goes to print()
#   → matrix = ...  # stored in memory
#   → print(transpose_matrix(...))  # transpose_matrix() runs first → value goes to print()
#   → matrix = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(transpose_matrix(...))  # transpose_matrix() runs first → value goes to print()
#
# Loop: takes one item from transposed, runs body, repeats until done
"""
Problème 256 :
Écrivez un programme Python à transpose un 2D matrix (list de listes) en utilisant `zip()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : enumerate, list, map, zip()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → result = [[], [], []]
#   → for t in lst:
#   →     for i, val in enumerate(t):
#   →         result[i].append(val)
#   → return result
#   → result = [[], [], []]
#   → for t in lst:
#   →     for i, val in enumerate(t):
#   →         result[i].append(val)
#   → return result
#   → result = [[], [], []]
#   → for t in lst:
#   →     for i, val in enumerate(t):
#   →         result[i].append(val)
#   → return result
#   → result = [[], [], []]
#   → for t in lst:
#   →     for i, val in enumerate(t):
#   →         result[i].append(val)
#   → return result
#   → result = [[], [], []]
#   → for t in lst:
#   →     for i, val in enumerate(t):
#   →         result[i].append(val)
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only list_tuples is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(list_tuples(...))  # list_tuples() runs first → value goes to print()
#   → print(list_tuples(...))  # list_tuples() runs first → value goes to print()
#   → print(list_tuples(...))  # list_tuples() runs first → value goes to print()
#   → print(list_tuples(...))  # list_tuples() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(list_tuples(...))  # list_tuples() runs first → value goes to print()
#
# Loop: takes one item from unzipped, runs body, repeats until done
"""
Problème 257 :
Écrivez un programme Python à unzip une liste de tuples dans individual listes en utilisant `zip()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : enumerate, len, list, map, range, zip()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#   → return result
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only individualists is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(individualists(...))  # individualists() runs first → value goes to print()
#   → print(individualists(...))  # individualists() runs first → value goes to print()
#   → print(individualists(...))  # individualists() runs first → value goes to print()
#   → print(individualists(...))  # individualists() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(individualists(...))  # individualists() runs first → value goes to print()
#
# Loop: takes one item from zip(...), runs body, repeats until done
"""
Problème 258 :
Écrivez un programme Python à unzip une liste de tuples dans individual listes en utilisant `zip()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: >
# Fonctions intégrées : len, list, map, max, range, zip()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#   → return result
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only maxium_element_wise is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → print(maxium_element_wise(...))  # maxium_element_wise() runs first → value goes to print()
#   → print(maxium_element_wise(...))  # maxium_element_wise() runs first → value goes to print()
#   → print(maxium_element_wise(...))  # maxium_element_wise() runs first → value goes to print()
#   → print(maxium_element_wise(...))  # maxium_element_wise() runs first → value goes to print()
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(maxium_element_wise(...))  # maxium_element_wise() runs first → value goes to print()
#
# Loop: takes one item from zip(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 259 :
Écrivez un programme Python à trouver le élément-wise maximum des deux listes en utilisant `zip()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: +
# Fonctions intégrées : len, list, map, range, zip()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#   → return result
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only concatenate is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → print(concatenate(...))  # concatenate() runs first → value goes to print()
#   → print(concatenate(...))  # concatenate() runs first → value goes to print()
#   → print(concatenate(...))  # concatenate() runs first → value goes to print()
#   → print(concatenate(...))  # concatenate() runs first → value goes to print()
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(concatenate(...))  # concatenate() runs first → value goes to print()
#
# Loop: takes one item from zip(...), runs body, repeats until done
"""
Problème 260 :
Écrivez un programme Python à concatenate corresponding strings des deux listes en utilisant `zip()`
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : len, list, map, range, zip()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#   → return result
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only combine_to_dict is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → print(combine_to_dict(...))  # combine_to_dict() runs first → value goes to print()
#   → print(combine_to_dict(...))  # combine_to_dict() runs first → value goes to print()
#   → print(combine_to_dict(...))  # combine_to_dict() runs first → value goes to print()
#   → print(combine_to_dict(...))  # combine_to_dict() runs first → value goes to print()
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(combine_to_dict(...))  # combine_to_dict() runs first → value goes to print()
#
# Loop: takes one item from zip(...), runs body, repeats until done
"""
Problème 261 :
Écrivez un programme Python à combiner deux listes dans une liste de dictionnaires en utilisant `zip()`. chaque dictionnaire devrait ont clés'a'et'b'.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: >
# Fonctions intégrées : filter, len, list, range, zip()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#   → return result
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only filter_pairs is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → print(filter_pairs(...))  # filter_pairs() runs first → value goes to print()
#   → print(filter_pairs(...))  # filter_pairs() runs first → value goes to print()
#   → print(filter_pairs(...))  # filter_pairs() runs first → value goes to print()
#   → print(filter_pairs(...))  # filter_pairs() runs first → value goes to print()
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(filter_pairs(...))  # filter_pairs() runs first → value goes to print()
#
# Loop: takes one item from zip(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 262 :
Écrivez un programme Python à filtrer pairs d'éléments des deux listes où le premier élément est greater que le deuxième en utilisant `zip()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: <
# Fonctions intégrées : filter, len, list, range, zip()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#   → return result
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only filter_pairs is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → print(filter_pairs(...))  # filter_pairs() runs first → value goes to print()
#   → print(filter_pairs(...))  # filter_pairs() runs first → value goes to print()
#   → print(filter_pairs(...))  # filter_pairs() runs first → value goes to print()
#   → print(filter_pairs(...))  # filter_pairs() runs first → value goes to print()
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(filter_pairs(...))  # filter_pairs() runs first → value goes to print()
#
# Loop: takes one item from zip(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 263 :
Écrivez un programme Python à filtrer pairs d'éléments des deux listes où le premier élément est lesser que le deuxième en utilisant `zip()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: +
# Fonctions intégrées : len, list, map, range, zip()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#   → return result
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only add_nested_lists is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → print(add_nested_lists(...))  # add_nested_lists() runs first → value goes to print()
#   → print(add_nested_lists(...))  # add_nested_lists() runs first → value goes to print()
#   → print(add_nested_lists(...))  # add_nested_lists() runs first → value goes to print()
#   → print(add_nested_lists(...))  # add_nested_lists() runs first → value goes to print()
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(add_nested_lists(...))  # add_nested_lists() runs first → value goes to print()
#
# Loop: takes one item from zip(...), runs body, repeats until done
"""
Problème 264 :
Écrivez un programme Python à add corresponding éléments de imbriqué listes en utilisant `zip()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: - **
# Fonctions intégrées : sum, zip()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return math.sqrt(distance_squared)
#   → return math.sqrt(distance_squared)
#   → return math.sqrt(distance_squared)
#   → return math.sqrt(distance_squared)
#   → return math.sqrt(distance_squared)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only euclidean_distance is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → point1 = ...  # stored in memory
#   → point2 = ...  # stored in memory
#   → print(euclidean_distance(...))  # euclidean_distance() runs first → value goes to print()
#   → print(euclidean_distance(...))  # euclidean_distance() runs first → value goes to print()
#   → print(euclidean_distance(...))  # euclidean_distance() runs first → value goes to print()
#   → print(euclidean_distance(...))  # euclidean_distance() runs first → value goes to print()
#   → point1 = ...  # stored in memory
#   → point2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(euclidean_distance(...))  # euclidean_distance() runs first → value goes to print()
#
# Loop: takes one item from zip(...), runs body, repeats until done
"""
Problem 265:
def euclidean_distance(point1, point2):  # defines a function with parameters point1, point2
    distance_squared = 0
    for x1, x2 in zip(point1, point2):
        distance_squared += (x1 - x2) ** 2
    return math.sqrt(distance_squared)  # return sends the result back to the caller
print(euclidean_distance(point1, point2))  # euclidean_distance() runs first, then print() outputs the result
print(euclidean_distance(?, ?))  # euclidean_distance() runs first, then print() outputs the result
print(euclidean_distance(25, 25))  # euclidean_distance() runs first, then print() outputs the result
sum(...) ** 0.5  # sum(...) → then 0.5 → then **
? ** 2  # ? → then 2 → then **
x1 - x2  # x1 → then x2 → then -
a - b  # a → then b → then -
import math
def euclidean_distance(point1, point2):  # stored in memory, not executed yet
point1 = ...  # assigns a value to the variable
point2 = ...  # assigns a value to the variable
print(euclidean_distance(...))  # euclidean_distance() runs with point1=point1, point2=point2
import math
def euclidean_distance(point1, point2):  # stored in memory, not executed yet
print(euclidean_distance(...))  # euclidean_distance() runs with point1=?, point2=?
import math
def euclidean_distance(point1, point2):  # stored in memory, not executed yet
print(euclidean_distance(...))  # euclidean_distance() runs with point1=?, point2=?
def euclidean_distance(point1, point2):  # stored in memory, not executed yet
print(euclidean_distance(...))  # euclidean_distance() runs with point1=?, point2=?
def euclidean_distance(point1, point2):  # stored in memory, not executed yet
def euclidean_distance(point1, point2):  # stored in memory, not executed yet
point1 = ...  # assigns a value to the variable
point2 = ...  # assigns a value to the variable
result = ...  # assigns a value to the variable
print(result)
print(euclidean_distance(...))  # euclidean_distance() runs with point1=25, point2=25


#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : list, sum, zip()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#   → return result
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only interleave is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → print(interleave(...))  # interleave() runs first → value goes to print()
#   → print(interleave(...))  # interleave() runs first → value goes to print()
#   → print(interleave(...))  # interleave() runs first → value goes to print()
#   → print(interleave(...))  # interleave() runs first → value goes to print()
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(interleave(...))  # interleave() runs first → value goes to print()
#
# Loop: takes one item from zip(...), runs body, repeats until done
"""
Problème 266 :
Écrivez un programme Python à interleave deux listes dans un seul list en utilisant `zip()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: *
# Fonctions intégrées : len, list, map, range, zip()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#   → return result
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only multiply_2_lst is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → print(multiply_2_lst(...))  # multiply_2_lst() runs first → value goes to print()
#   → print(multiply_2_lst(...))  # multiply_2_lst() runs first → value goes to print()
#   → print(multiply_2_lst(...))  # multiply_2_lst() runs first → value goes to print()
#   → print(multiply_2_lst(...))  # multiply_2_lst() runs first → value goes to print()
#   → lst1 = ...  # stored in memory
#   → lst2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(multiply_2_lst(...))  # multiply_2_lst() runs first → value goes to print()
#
# Loop: takes one item from zip(...), runs body, repeats until done
"""
Problème 267 :
Écrivez un programme Python à multiply corresponding éléments des deux listes en utilisant `zip()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: * +
# Fonctions intégrées : map, reduce, sum, zip()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#   → return result
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only dot_product is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → vector1 = ...  # stored in memory
#   → vector2 = ...  # stored in memory
#   → print(dot_product(...))  # dot_product() runs first → value goes to print()
#   → print(dot_product(...))  # dot_product() runs first → value goes to print()
#   → print(dot_product(...))  # dot_product() runs first → value goes to print()
#   → print(dot_product(...))  # dot_product() runs first → value goes to print()
#   → vector1 = ...  # stored in memory
#   → vector2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(dot_product(...))  # dot_product() runs first → value goes to print()
#
# Loop: takes one item from zip(...), runs body, repeats until done
"""
Problème 268 :
Écrivez un programme Python à calculate le dot produit des deux vectors represented as listes en utilisant `zip()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: % !=
# Fonctions intégrées : filter, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → result = []
#   → for x in lst:
#   →     if x % 2 != 0:
#   →         result.append(x)
#   → return result
#   → result = []
#   → for x in lst:
#   →     if x % 2 != 0:
#   →         result.append(x)
#   → return result
#   → result = []
#   → for x in lst:
#   →     if x % 2 != 0:
#   →         result.append(x)
#   → return result
#   → return x % 2 != 0
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — filter_even_numbers, is_odd are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(filter_even_numbers(...))  # filter_even_numbers() runs first → value goes to print()
#   → print(filter_even_numbers(...))  # filter_even_numbers() runs first → value goes to print()
#   → print(filter_even_numbers(...))  # filter_even_numbers() runs first → value goes to print()
#   → x = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_odd(...))  # is_odd() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 269 :
Écrivez un programme Python à filtrer out tous les nombres pairs de une liste en utilisant `filtrer()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: % ==
# Fonctions intégrées : filter, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → result = []
#   → for x in lst:
#   →     if x % 2 == 0:
#   →         result.append(x)
#   → return result
#   → result = []
#   → for x in lst:
#   →     if x % 2 == 0:
#   →         result.append(x)
#   → return result
#   → result = []
#   → for x in lst:
#   →     if x % 2 == 0:
#   →         result.append(x)
#   → return result
#   → return x % 2 == 0
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — filter_odd_numbers, is_even are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(filter_odd_numbers(...))  # filter_odd_numbers() runs first → value goes to print()
#   → print(filter_odd_numbers(...))  # filter_odd_numbers() runs first → value goes to print()
#   → print(filter_odd_numbers(...))  # filter_odd_numbers() runs first → value goes to print()
#   → x = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_even(...))  # is_even() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 270 :
Écrivez un programme Python à filtrer out tous les nombres impairs de une liste en utilisant `filtrer()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: < >=
# Fonctions intégrées : filter, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → result = []
#   → for x in lst:
#   →     if x >= 0:
#   →         result.append(x)
#   → return result
#   → result = []
#   → for x in lst:
#   →     if x >= 0:
#   →         result.append(x)
#   → return result
#   → result = []
#   → for x in lst:
#   →     if x >= 0:
#   →         result.append(x)
#   → return result
#   → return not x < 0
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — filter_negative_numbers, is_non_negative are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(filter_negative_numbers(...))  # filter_negative_numbers() runs first → value goes to print()
#   → print(filter_negative_numbers(...))  # filter_negative_numbers() runs first → value goes to print()
#   → print(filter_negative_numbers(...))  # filter_negative_numbers() runs first → value goes to print()
#   → x = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_non_negative(...))  # is_non_negative() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 272 :
Écrivez un programme Python à filtrer out tous les nombres négatifs de une liste en utilisant `filtrer()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else | while
# Operators: - < != ==
# Fonctions intégrées : filter, is_pal, len, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → def is_pal(s):
#   →     left, right = (0, len(s) - 1)
#   →     while left < right:
#   →         if s[left] != s[right]:
#   →             return False
#   →         left += 1
#   →         right -= 1
#   →     return True
#   → return [s for s in lst if is_pal(s)]
#   → def is_pal(s):
#   →     left, right = (0, len(s) - 1)
#   →     while left < right:
#   →         if s[left] != s[right]:
#   →             return False
#   →         left += 1
#   →         right -= 1
#   →     return True
#   → return [s for s in lst if is_pal(s)]
#   → def is_pal(s):
#   →     left, right = (0, len(s) - 1)
#   →     while left < right:
#   →         if s[left] != s[right]:
#   →             return False
#   →         left += 1
#   →         right -= 1
#   →     return True
#   → return [s for s in lst if is_pal(s)]
#   → return s == s[::-1]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — filter_palindromes, is_palindrome are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(filter_palindromes(...))  # filter_palindromes() runs first → value goes to print()
#   → print(filter_palindromes(...))  # filter_palindromes() runs first → value goes to print()
#   → print(filter_palindromes(...))  # filter_palindromes() runs first → value goes to print()
#   → s = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_palindrome(...))  # is_palindrome() runs first → value goes to print()
#
# Loop: check condition → if True run body → check again
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 274 :
Écrivez un programme Python à filtrer out tous palindromes de une liste de chaînes en utilisant `filtrer()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: % ==
# Fonctions intégrées : filter, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return n % divisor == 0
#   → return n % divisor == 0
#   → return n % divisor == 0
#   → return n % divisor == 0
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only filter_divisible is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → divisor = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(filter_divisible(...))  # filter_divisible() runs first → value goes to print()
#   → print(filter_divisible(...))  # filter_divisible() runs first → value goes to print()
#   → print(filter_divisible(...))  # filter_divisible() runs first → value goes to print()
#   → numbers = ...  # stored in memory
#   → divisor = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(filter_divisible(...))  # filter_divisible() runs first → value goes to print()
#
# Loop: takes one item from numbers, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 276 :
Écrivez un programme Python à filtrer out tous nombres de une liste qui sont divisible by une donnée nombre en utilisant `filtrer()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: % !=
# Fonctions intégrées : filter, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return num % divisor != 0
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only is_not_divisible is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → divisor = ...  # stored in memory
#   → filtered_numbers = ...  # stored in memory
#   → print(filtered_numbers)
#   → numbers = ...  # stored in memory
#   → divisor = ...  # stored in memory
#   → filtered_numbers = ...  # stored in memory
#   → print(filtered_numbers)
#   → numbers = ...  # stored in memory
#   → divisor = ...  # stored in memory
#   → filtered_numbers = ...  # stored in memory
#   → print(filtered_numbers)
#   → numbers = ...  # stored in memory
#   → divisor = ...  # stored in memory
#   → filtered_numbers = ...  # stored in memory
#   → for n in numbers  # runs body once per item
#   → print(filtered_numbers)
#   → num = ...  # stored in memory
#   → divisor = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_not_divisible(...))  # is_not_divisible() runs first → value goes to print()
#
# Loop: takes one item from numbers, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 277 :
Écrivez un programme Python à filtrer out tous nombres de une liste qui sont divisible by une donnée nombre en utilisant `filtrer()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: !=
# Fonctions intégrées : filter, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return s != ''
#   → return s != ''
#   → return s != ''
#   → return s != ''
#   → return s != ''
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only filter_non_empty is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → strings = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(filter_non_empty(...))  # filter_non_empty() runs first → value goes to print()
#   → print(filter_non_empty(...))  # filter_non_empty() runs first → value goes to print()
#   → print(filter_non_empty(...))  # filter_non_empty() runs first → value goes to print()
#   → print(filter_non_empty(...))  # filter_non_empty() runs first → value goes to print()
#   → strings = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(filter_non_empty(...))  # filter_non_empty() runs first → value goes to print()
#
# Loop: takes one item from strings, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 278 :
Écrivez un programme Python à filtrer out tous non vide strings de une liste en utilisant `filtrer()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: % + < > != ** == >= and
# Fonctions intégrées : all, filter, int, is_prime, list, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return False
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only filter_prime is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(filter_prime(...))  # filter_prime() runs first → value goes to print()
#
# Loop: takes one item from numbers, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 279 :
Écrivez un programme Python à filtrer out tous prime nombres de une liste en utilisant `filtrer()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Fonctions intégrées : filter, isinstance, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return not isinstance(x, float)
#   → return not isinstance(x, float)
#   → return not isinstance(x, float)
#   → return not isinstance(x, float)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only filter_floats is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → items = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(filter_floats(...))  # filter_floats() runs first → value goes to print()
#   → print(filter_floats(...))  # filter_floats() runs first → value goes to print()
#   → print(filter_floats(...))  # filter_floats() runs first → value goes to print()
#   → items = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(filter_floats(...))  # filter_floats() runs first → value goes to print()
#
# Loop: takes one item from items, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 280 :
Écrivez un programme Python à filtrer out tous floating-point nombres de une liste en utilisant `filtrer()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Fonctions intégrées : filter, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return not s.isupper()
#   → return not s.isupper()
#   → return not s.isupper()
#   → return not s.isupper()
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only filter_uppercase is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → strings = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(filter_uppercase(...))  # filter_uppercase() runs first → value goes to print()
#   → print(filter_uppercase(...))  # filter_uppercase() runs first → value goes to print()
#   → print(filter_uppercase(...))  # filter_uppercase() runs first → value goes to print()
#   → strings = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(filter_uppercase(...))  # filter_uppercase() runs first → value goes to print()
#
# Loop: takes one item from strings, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 281 :
Écrivez un programme Python à filtrer out tous uppercase strings de une liste en utilisant `filtrer()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Fonctions intégrées : filter, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return not s.isupper()
#   → return not s.isupper()
#   → return not s.isupper()
#   → return not s.isupper()
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only filter_uppercase_again is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → strings = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(filter_uppercase_again(...))  # filter_uppercase_again() runs first → value goes to print()
#   → print(filter_uppercase_again(...))  # filter_uppercase_again() runs first → value goes to print()
#   → print(filter_uppercase_again(...))  # filter_uppercase_again() runs first → value goes to print()
#   → strings = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(filter_uppercase_again(...))  # filter_uppercase_again() runs first → value goes to print()
#
# Loop: takes one item from strings, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 282 :
Écrivez un programme Python à filtrer out tous uppercase strings de une liste en utilisant `filtrer()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: is not
# Fonctions intégrées : filter, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return x is not None
#   → return x is not None
#   → return x is not None
#   → return x is not None
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only filter_non_none is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → items = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(filter_non_none(...))  # filter_non_none() runs first → value goes to print()
#   → print(filter_non_none(...))  # filter_non_none() runs first → value goes to print()
#   → print(filter_non_none(...))  # filter_non_none() runs first → value goes to print()
#   → items = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(filter_non_none(...))  # filter_non_none() runs first → value goes to print()
#
# Loop: takes one item from items, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 283 :
Écrivez un programme Python à filtrer out tous non-None valeurs de une liste en utilisant `filtrer()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: not in
# Fonctions intégrées : filter, list()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return substring not in s
#   → return substring not in s
#   → return substring not in s
#   → return substring not in s
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only filter_by_substring is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → items = ...  # stored in memory
#   → substring = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(filter_by_substring(...))  # filter_by_substring() runs first → value goes to print()
#   → print(filter_by_substring(...))  # filter_by_substring() runs first → value goes to print()
#   → print(filter_by_substring(...))  # filter_by_substring() runs first → value goes to print()
#   → items = ...  # stored in memory
#   → substring = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(filter_by_substring(...))  # filter_by_substring() runs first → value goes to print()
#
# Loop: takes one item from items, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 284 :
Écrivez un programme Python à filtrer out tous éléments de une liste qui contien un spécifique substring en utilisant `filtrer()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | while
# Operators: * + // <=
# Fonctions intégrées : range, reduce, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return total
#   → return total
#   → return total
#   → return total
# while ... → repeats as long as condition is true
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sum_first_10_natural_numbers is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sum_first_10_natural_numbers(...))  # sum_first_10_natural_numbers() runs first → value goes to print()
#   → print(sum_first_10_natural_numbers(...))  # sum_first_10_natural_numbers() runs first → value goes to print()
#   → print(sum_first_10_natural_numbers(...))  # sum_first_10_natural_numbers() runs first → value goes to print()
#   → print(sum_first_10_natural_numbers(...))  # sum_first_10_natural_numbers() runs first → value goes to print()
#   → i = ...  # stored in memory
#   → total = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → i = ...  # stored in memory
#   → total = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#
# Loop: check condition → if True run body → check again
"""
Problème 286 :
Écrivez un programme Python à trouver le somme de le premier 10 natural nombres en utilisant un `while` loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else | while
# Operators: % + > // ==
# Fonctions intégrées : abs, int, str, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return total
#   → return total
#   → return total
#   → return total
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sum_of_digits is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → number = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(?)
#   → print(sum_of_digits(...))  # sum_of_digits() runs first → value goes to print()
#   → print(sum_of_digits(...))  # sum_of_digits() runs first → value goes to print()
#   → print(sum_of_digits(...))  # sum_of_digits() runs first → value goes to print()
#   → number = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sum_of_digits(...))  # sum_of_digits() runs first → value goes to print()
#
# Loop: check condition → if True run body → check again
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 289 :
Écrivez un programme Python à trouver le somme de les chiffres de une donnée nombre en utilisant un `while` loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | while
# Operators: % * + < > //
# Fonctions intégrées : abs, input, int, reversed, str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return reversed_num
#   → return reversed_num
#   → return reversed_num
#   → return reversed_num
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only reverse_number is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → num = ...  # stored in memory
#   → print('Reversed number:', reverse_number(...))
#   → print(reverse_number(...))  # reverse_number() runs first → value goes to print()
#   → print(reverse_number(...))  # reverse_number() runs first → value goes to print()
#   → print(reverse_number(...))  # reverse_number() runs first → value goes to print()
#   → n = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(reverse_number(...))  # reverse_number() runs first → value goes to print()
#
# Loop: check condition → if True run body → check again
"""
Problème 290 :
Écrivez un programme Python à trouver le somme de les chiffres de une donnée nombre en utilisant un `while` loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else | while
# Operators: * + - > <=
# Fonctions intégrées : range, reduce()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#   → return result
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only factorial is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → number_to_calculate = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(?)
#   → test_numbers = ...  # stored in memory
#   → for num in test_numbers  # runs body once per item
#   → print(factorial(...))  # factorial() runs first → value goes to print()
#   → print(factorial(...))  # factorial() runs first → value goes to print()
#   → print(factorial(...))  # factorial() runs first → value goes to print()
#   → print(factorial(...))  # factorial() runs first → value goes to print()
#   → number = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(factorial(...))  # factorial() runs first → value goes to print()
#
# Loop: takes one item from test_numbers, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 291 :
Écrivez un programme Python à trouver la factorielle de une donnée nombre en utilisant un `while` loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else | while
# Operators: % * + < != ** <= ==
# Fonctions intégrées : all, int, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return False
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only is_prime is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → test_numbers = ...  # stored in memory
#   → print('Prime number check:')
#   → for num in test_numbers  # runs body once per item
#   → for num in [1, 2, 3, 4, 5, 10, 13, 17, 20, 23, 24, 29]  # runs body once per item
#   → for num in [1, 2, 3, 4, 5, 10, 13, 17, 20, 23, 24, 29]  # runs body once per item
#   → for num in [1, 2, 3, 4, 5, 10, 13, 17, 20, 23, 24, 29]  # runs body once per item
#   → number = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_prime(...))  # is_prime() runs first → value goes to print()
#
# Loop: takes one item from test_numbers, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 293 :
Écrivez un programme Python à vérifier si une donnée nombre est prime en utilisant un `while` loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else | while
# Operators: + < > ==
# Fonctions intégrées : abs, len, str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return count
#   → return count
#   → return count
#   → return count
#   → return count
#   → return count
#   → return count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_digits is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → test_numbers = ...  # stored in memory
#   → print('Counting digits:')
#   → for num in test_numbers  # runs body once per item
#   → print(count_digits(...))  # count_digits() runs first → value goes to print()
#   → print(count_digits(...))  # count_digits() runs first → value goes to print()
#   → print(count_digits(...))  # count_digits() runs first → value goes to print()
#   → print(count_digits(...))  # count_digits() runs first → value goes to print()
#   → print(count_digits(...))  # count_digits() runs first → value goes to print()
#   → print(count_digits(...))  # count_digits() runs first → value goes to print()
#   → number = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_digits(...))  # count_digits() runs first → value goes to print()
#
# Loop: takes one item from test_numbers, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 294 :
Écrivez un programme Python à compter le nombre de les chiffres dans une donnée nombre en utilisant un `while` loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else | while
# Operators: % > != == and
# Fonctions intégrées : abs, max()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return a
#   → return a
#   → return a
#   → return a
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only gcd is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → num1 = ...  # stored in memory
#   → num2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(?)
#   → test_cases = ...  # stored in memory
#   → print('Testing additional cases:')
#   → for case in test_cases  # runs body once per item
#   → print(gcd(...))  # gcd() runs first → value goes to print()
#   → print(gcd(...))  # gcd() runs first → value goes to print()
#   → print(gcd(...))  # gcd() runs first → value goes to print()
#   → a = ...  # stored in memory
#   → b = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(gcd(...))  # gcd() runs first → value goes to print()
#
# Loop: takes one item from test_cases, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 295 :
Écrivez un programme Python à trouver le GCD (Greatest commun Divisor) des deux nombres en utilisant un `while` loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | while
# Operators: + <
# Fonctions intégrées : len, reduce, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return total
#   → return total
#   → return total
#   → return total
#   → return total
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sum_elements is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(sum_elements(...))  # sum_elements() runs first → value goes to print()
#   → print(sum_elements(...))  # sum_elements() runs first → value goes to print()
#   → print(sum_elements(...))  # sum_elements() runs first → value goes to print()
#   → print(sum_elements(...))  # sum_elements() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sum_elements(...))  # sum_elements() runs first → value goes to print()
#
# Loop: check condition → if True run body → check again
"""
Problème 297 :
description": "Write un Python program à trouver le somme de tous éléments dans une liste en utilisant un `while` loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else | while
# Operators: < >
# Fonctions intégrées : len, max, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return max(lst, key=len)
#   → return max(lst, key=len)
#   → return sorted(numbers)[-1]
#   → return sorted(numbers)[-1]
#   → return sorted(numbers)[-1]
#   → return max(lst, key=len)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — find_largest_element, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → main(lst)  # jumps into main(), runs body, returns
#   → numbers_list = ...  # stored in memory
#   → largest_number = ...  # stored in memory
#   → print(?)
#   → additional_numbers_list = ...  # stored in memory
#   → largest_number_in_negative = ...  # stored in memory
#   → print(?)
#   → print(main(...))  # main() runs first → value goes to print()
#   → print(find_largest_element(...))  # find_largest_element() runs first → value goes to print()
#   → print(find_largest_element(...))  # find_largest_element() runs first → value goes to print()
#   → print(find_largest_element(...))  # find_largest_element() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(main(...))  # main() runs first → value goes to print()
#
# Loop: check condition → if True run body → check again
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 298 :
Écrivez un programme Python à trouver le plus grand élément dans une liste en utilisant un `while` loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else | while
# Operators: <
# Fonctions intégrées : len, min, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return None
#   → return None
#   → return None
#   → return None
#   → return None
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only smallest_element is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(smallest_element(...))  # smallest_element() runs first → value goes to print()
#   → print(smallest_element(...))  # smallest_element() runs first → value goes to print()
#   → print(smallest_element(...))  # smallest_element() runs first → value goes to print()
#   → print(smallest_element(...))  # smallest_element() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(smallest_element(...))  # smallest_element() runs first → value goes to print()
#
# Loop: check condition → if True run body → check again
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 299 :
Écrivez un programme Python à trouver le plus petit élément dans une liste en utilisant un `while` loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else | while
# Operators: > <=
# Fonctions intégrées : input, int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → user_input = input('Enter a number greater than 10: ')
#   → while int(user_input) <= 10:
#   →     user_input = input('Enter a number greater than 10: ')
#   → user_input = input('Enter a number greater than 10: ')
#   → while int(user_input) <= 10:
#   →     user_input = input('Enter a number greater than 10: ')
#   → user_input = input('Enter a number greater than 10: ')
#   → while int(user_input) <= 10:
#   →     user_input = input('Enter a number greater than 10: ')
#   → user_input = input('Enter a number greater than 10: ')
#   → while int(user_input) <= 10:
#   →     user_input = input('Enter a number greater than 10: ')
# while ... → repeats as long as condition is true
# while ... → repeats as long as condition is true
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only ask_until_condition is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → ask_until_condition()  # jumps into ask_until_condition(), runs body, returns
#   → ask_until_condition()  # jumps into ask_until_condition(), runs body, returns
#   → ask_until_condition()  # jumps into ask_until_condition(), runs body, returns
#   → ask_until_condition()  # jumps into ask_until_condition(), runs body, returns
#
# Loop: check condition → if True run body → check again
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 304 :
Écrivez un programme Python à repeatedly ask pour utilisateur entrée jusqu'à un spécifique condition est met en utilisant un `while` loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: < >
# Fonctions intégrées : input, int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → numbers = [int(value) for value in input('Enter numbers: ').split()]
#   → smallest = numbers[0]
#   → largest = numbers[0]
#   → for number in numbers[1:]:
#   →     if number < smallest:
#   →         smallest = number
#   →     if number > largest:
#   →         largest = number
#   → result = (smallest, largest)
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only find_min_max is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → find_min_max()  # jumps into find_min_max(), runs body, returns
#   → numbers = ...  # stored in memory
#   → smallest = ...  # stored in memory
#   → largest = ...  # stored in memory
#   → for number in ?  # runs body once per item
#   → print(smallest, largest)
#   → numbers = ...  # stored in memory
#   → smallest = ...  # stored in memory
#   → largest = ...  # stored in memory
#   → for number in ?  # runs body once per item
#   → print(smallest, largest)
#
# Loop: takes one item from ?, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 307 :
Écrivez une fonction Python appelée find_min_max qui prend une liste de nombres en entrée et retourne un tuple contenant le minimum et maximum nombres dans la liste, dont pas call le fuction en utilisant print(find_min_max). N'utilisez pas trier() ou max() ou min().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: not in
# Fonctions intégrées : input()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → lst = input('type word list: ').split()
#   → result = {}
#   → for word in lst:
#   →     first_letter = word[0]
#   →     if first_letter not in result:
#   →         result[first_letter] = [word]
#   →     else:
#   →         result[first_letter].append(word)
#   → result = result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only group_by_first_letter is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → group_by_first_letter()  # jumps into group_by_first_letter(), runs body, returns
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → for word in lst  # runs body once per item
#   → print(result)
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → for word in lst  # runs body once per item
#   → print(result)
#
# Loop: takes one item from lst, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 308 :
Écrivez une fonction group_by_first_letter qui prend une liste de chaînes en entrée et retourne un dictionnaire. Le dictionnaire devrait group le strings by leur premier lettre. chaque clé dans le dictionnaire devrait be un premier lettre, et le corresponding valeur devrait be une liste de chaînes qui start avec qui lettre. utilisateur devrait tapez list en entrée():
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: >
# Fonctions intégrées : len, max()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return longest_word
#   → return max(lst, key=len)
#   → return longest_word
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — find_longest_word, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(find_longest_word(...))  # find_longest_word() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → main(lst)  # jumps into main(), runs body, returns
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(find_longest_word(...))  # find_longest_word() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 310 :
Écrivez une fonction Python appelée find_longest_word qui prend une liste de mots en entrée et retourne le plus long mot dans la liste. si il y un multiple le plus long words, retourner le premier l'une encountered. N'utilisez pas trié().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: >
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return longest_word
#   → return longest_word
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only find_longest_word is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(find_longest_word(...))  # find_longest_word() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(find_longest_word(...))  # find_longest_word() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 311 :
Écrivez une fonction Python appelée find_longest_word qui prend une liste de mots en entrée et retourne le plus long mot dans la liste. si il y un multiple le plus long words, retourner le premier l'une encountered. N'utilisez pas trié()et len().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : input, list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → user = input('Type numbers separated by spaces: ').split()
#   → user_int = list(map(int, user))
#   → user_int.sort()
#   → second_largest = user_int[-2]
#   → result = second_largest
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only second_largest_number is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → second_largest_number()  # jumps into second_largest_number(), runs body, returns
#   → user = ...  # stored in memory
#   → user_int = ...  # stored in memory
#   → user_int.sort()
#   → second_largest = ...  # stored in memory
#   → print(second_largest)
#   → user = ...  # stored in memory
#   → user_int = ...  # stored in memory
#   → user_int.sort()
#   → second_largest = ...  # stored in memory
#   → print(second_largest)
"""
Problème 312 :
Écrivez un programme Python à trouver le deuxième plus grand nombre dans une liste. demander le utilisateur à saisir une liste de nombres, N'utilisez pas un pour loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: - <=
# Fonctions intégrées : chr, list, map, ord, str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return str(s).upper()
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only convert_to_uppercase is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → strings = ...  # stored in memory
#   → uppercase_strings = ...  # stored in memory
#   → print('Original list:', strings)
#   → print('Uppercase list:', uppercase_strings)
#   → strings = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(convert_to_uppercase(...))  # convert_to_uppercase() runs first → value goes to print()
"""
Problème 313 :
Écrivez un programme Python à convert une liste de chaînes à uppercase en utilisant `map()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : int, list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return int(s)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only convert_to_integers is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → string_numbers = ...  # stored in memory
#   → integer_numbers = ...  # stored in memory
#   → print('Original list of strings:', string_numbers)
#   → print('Converted list of integers:', integer_numbers)
#   → strings = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(convert_to_integers(...))  # convert_to_integers() runs first → value goes to print()
"""
Problème 314 :
Écrivez un programme Python à convert une liste de chaînes representing nombres à une liste d'entiers en utilisant `map()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: *
# Fonctions intégrées : list, map, pow, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return pow(x, x)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only square_numbers is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → original_numbers = ...  # stored in memory
#   → squared_numbers = ...  # stored in memory
#   → print('Original list of numbers:', original_numbers)
#   → print('Squared list of numbers:', squared_numbers)
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(square_numbers(...))  # square_numbers() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
"""
Problème 315 :
Écrivez un programme Python à carré chaque nombre dans une liste en utilisant `map()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : len, list, map, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sum((1 for _ in s))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only string_lengths is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → string_list = ...  # stored in memory
#   → lengths = ...  # stored in memory
#   → print('Original list of strings:', string_list)
#   → print('Lengths of each string:', lengths)
#   → strings = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(string_lengths(...))  # string_lengths() runs first → value goes to print()
#
# Loop: takes one item from s, runs body, repeats until done
"""
Problème 316 :
Écrivez un programme Python à trouver la longueur de chaque chaîne dans une liste en utilisant `map()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: * - /
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return (f - 32) * 5 / 9
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only fahrenheit_to_celsius is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → fahrenheit_temps = ...  # stored in memory
#   → celsius_temps = ...  # stored in memory
#   → print('Temperatures in Fahrenheit:', fahrenheit_temps)
#   → print('Temperatures in Celsius:', celsius_temps)
#   → temperatures = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(fahrenheit_to_celsius(...))  # fahrenheit_to_celsius() runs first → value goes to print()
"""
Problème 317 :
Écrivez un programme Python à convert une liste de temperatures de Fahrenheit à Celsius en utilisant `map()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: +
# Fonctions intégrées : list, map, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(add_five_to_number, lst))
#   → import operator
#   → return operator.add(x, 5)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — add_five, add_five_to_number are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(add_five(...))  # add_five() runs first → value goes to print()
#   → x = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(add_five_to_number(...))  # add_five_to_number() runs first → value goes to print()
"""
Problème 319 :
Écrivez un programme Python à add 5 à chaque nombre dans une liste en utilisant `map()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: **
# Fonctions intégrées : list, map, pow()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → import math
#   → return math.pow(num, 2)
#   → import math
#   → return math.pow(num, 2)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — main, square_roots are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → main(lst)  # jumps into main(), runs body, returns
#   → number_list = ...  # stored in memory
#   → roots = ...  # stored in memory
#   → print('Original numbers:', number_list)
#   → print('Square roots:', roots)
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(main(...))  # main() runs first → value goes to print()
"""
Problème 320 :
Écrivez un programme Python à compute le carré root de chaque nombre dans une liste en utilisant `map()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : len, list, map, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sum((1 for _ in s))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lengths_of_strings is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → string_list = ...  # stored in memory
#   → lengths = ...  # stored in memory
#   → print('Original strings:', string_list)
#   → print('Lengths of strings:', lengths)
#   → strings = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lengths_of_strings(...))  # lengths_of_strings() runs first → value goes to print()
#
# Loop: takes one item from s, runs body, repeats until done
"""
Problème 321 :
Écrivez un programme Python à convert une liste de chaînes à une liste de leur lengths en utilisant `map()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: - /
# Fonctions intégrées : list, map, max, min()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return (score - min_score) / (max_score - min_score)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only normalize_scores is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → score_list = ...  # stored in memory
#   → normalized_scores = ...  # stored in memory
#   → print('Original scores:', score_list)
#   → print('Normalized scores:', normalized_scores)
#   → scores = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(normalize_scores(...))  # normalize_scores() runs first → value goes to print()
"""
Problème 322 :
Écrivez un programme Python à normalize une liste de scores à un range de 0 à 1 en utilisant `map()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: +
# Fonctions intégrées : list, map, reversed()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → result = ''
#   → for char in s:
#   →     result = char + result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only reverse_strings is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → string_list = ...  # stored in memory
#   → reversed_strings = ...  # stored in memory
#   → print('Original strings:', string_list)
#   → print('Reversed strings:', reversed_strings)
#   → strings = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(reverse_strings(...))  # reverse_strings() runs first → value goes to print()
#
# Loop: takes one item from s, runs body, repeats until done
"""
Problème 323 :
Écrivez un programme Python à reverse chaque chaîne dans une liste en utilisant `map()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: *
# Fonctions intégrées : list, map, pow, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return pow(x, 2)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only double_numbers is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → number_list = ...  # stored in memory
#   → doubled_numbers = ...  # stored in memory
#   → print('Original numbers:', number_list)
#   → print('Doubled numbers:', doubled_numbers)
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(double_numbers(...))  # double_numbers() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
"""
Problème 324 :
Écrivez un programme Python à double chaque nombre dans une liste en utilisant `map()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return s.strip()
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only strip_whitespace is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → string_list = ...  # stored in memory
#   → stripped_strings = ...  # stored in memory
#   → print('Original strings:', string_list)
#   → print('Stripped strings:', stripped_strings)
#   → strings = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(strip_whitespace(...))  # strip_whitespace() runs first → value goes to print()
"""
Problème 325 :
Écrivez un programme Python à remove leading et trailing les espaces de chaque chaîne dans une liste en utilisant `map()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: *
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return (x, x * x)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only number_and_square is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers_list = ...  # stored in memory
#   → squared_tuples = ...  # stored in memory
#   → print('Numbers and their squares:', squared_tuples)
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(number_and_square(...))  # number_and_square() runs first → value goes to print()
"""
Problème 326 :
Écrivez un programme Python à créer une liste de tuples où chaque tuple contient un nombre et son carré en utilisant `map()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list, map, str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return str(s).title()
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only to_title_case is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → words = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → strings = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(to_title_case(...))  # to_title_case() runs first → value goes to print()
"""
Problème 327 :
Écrivez un programme Python à convert une liste de chaînes à title cas en utilisant `map()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: >
# Fonctions intégrées : input, int, len, list, set()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → user_input = input('Type numbers separated by spaces: ').split()
#   → user_int = []
#   → for num in user_input:
#   →     user_int.append(int(num))
#   → unique_numbers = set(user_int)
#   → unique_numbers = list(unique_numbers)
#   → unique_numbers.sort()
#   → if len(unique_numbers) > 1:
#   →     second_largest = unique_numbers[-2]
#   → else:
#   →     second_largest = 'Not enough unique numbers'
#   → result = second_largest
#   → return result
# if ... → only one branch executes based on condition
# if ... → only one branch executes based on condition
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only second_largest_number is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → second_largest_number()  # jumps into second_largest_number(), runs body, returns
#   → user_input = ...  # stored in memory
#   → user_int = ...  # stored in memory
#   → for num in user_input  # runs body once per item
#   → unique_numbers = ...  # stored in memory
#   → unique_numbers = ...  # stored in memory
#   → unique_numbers.sort()
#   → if condition  # evaluates → runs the True branch
#   → print(second_largest)
#   → user_input = ...  # stored in memory
#   → user_int = ...  # stored in memory
#   → for num in user_input  # runs body once per item
#   → unique_numbers = ...  # stored in memory
#   → unique_numbers = ...  # stored in memory
#   → unique_numbers.sort()
#   → if condition  # evaluates → runs the True branch
#   → print(second_largest)
#
# Loop: takes one item from user_input, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 328 :
Écrivez un programme Python à trouver le deuxième plus grand nombre dans une liste. demander le utilisateur à saisir une liste de nombres, N'utilisez pas un pour loop, N'utilisez pas map().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : input, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sort
#   → user = input('type number list: ').split()
#   → sort_number = sorted(user, key=int)
#   → print(sort_number)
#   → return sort
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — list_string, type_smallest_biggest are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(list_string(...))  # list_string() runs first → value goes to print()
#   → type_smallest_biggest()  # jumps into type_smallest_biggest(), runs body, returns
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(list_string(...))  # list_string() runs first → value goes to print()
"""
Problème 329 :
Écrivez une fonction où utilisateur tapez une liste de nombres dans chaîne et retourne une liste de nombres de plus petit à biggest. N'utilisez pas un pour loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : input, list, map, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sort
#   → user = input('Type numbers: ').split()
#   → int_list = list(map(int, user))
#   → sorted_list = sorted(int_list, reverse=True)
#   → print(sorted_list)
#   → return sort
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — list_of_string_numbers, type_biggest_smallest are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → print(list_of_string_numbers(...))  # list_of_string_numbers() runs first → value goes to print()
#   → type_biggest_smallest()  # jumps into type_biggest_smallest(), runs body, returns
#   → n = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(list_of_string_numbers(...))  # list_of_string_numbers() runs first → value goes to print()
"""
Problème 330 :
Écrivez une fonction où utilisateur tapez une liste de nombres dans chaîne et retourne une liste de nombres de biggest à plus petit. N'utilisez pas un pour loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : enumerate()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → for index, element in enumerate(lst):
#   →     print(f'Index: {index}, Element: {element}')
#   → for index, element in enumerate(lst):
#   →     print(f'Index: {index}, Element: {element}')
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — print_index_and_element, solve are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print_index_and_element(lst)  # jumps into print_index_and_element(), runs body, returns
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(print_index_and_element(...))  # print_index_and_element() runs first → value goes to print()
#
# Loop: takes one item from enumerate(...), runs body, repeats until done
"""
Problème 331 :
Écrivez un programme Python à print le index et élément de chaque élément dans une liste en utilisant `enumerate()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : enumerate()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only create_index_element_tuples is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(create_index_element_tuples(...))  # create_index_element_tuples() runs first → value goes to print()
#
# Loop: takes one item from enumerate(...), runs body, repeats until done
"""
Problème 332 :
Écrivez un programme Python à créer une liste de tuples où chaque tuple contient un indice et le corresponding élément de une liste en utilisant `enumerate()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : enumerate()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → for index, value in enumerate(strings):
#   →     print(index, value)
#   → for index, value in enumerate(strings):
#   →     print(index, value)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — print_with_index, solve are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → strings = ...  # stored in memory
#   → print_with_index(strings)  # jumps into print_with_index(), runs body, returns
#   → strings = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(print_with_index(...))  # print_with_index() runs first → value goes to print()
#
# Loop: takes one item from enumerate(...), runs body, repeats until done
"""
Problème 333 :
Écrivez un programme Python à print chaque élément avec ses index dans une liste de chaînes en utilisant `enumerate()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : enumerate()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only list_to_dict is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(list_to_dict(...))  # list_to_dict() runs first → value goes to print()
#
# Loop: takes one item from enumerate(...), runs body, repeats until done
"""
Problème 334 :
Écrivez un programme Python à générer un dictionnaire où clés sont indexes et valeurs sont éléments de une liste en utilisant `enumerate()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: ==
# Fonctions intégrées : enumerate()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return index
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only find_index is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → index = ...  # stored in memory
#   → print(index)
#   → lst = ...  # stored in memory
#   → element = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(find_index(...))  # find_index() runs first → value goes to print()
#
# Loop: takes one item from enumerate(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 335 :
Écrivez un programme Python à trouver le index de un spécifique élément dans une liste en utilisant `enumerate()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : enumerate()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → for index, element in enumerate(lst):
#   →     print(f'{index}: {element}')
#   → for index, element in enumerate(lst):
#   →     print(f'{index}: {element}')
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — print_index_and_element_with_colon, solve are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print_index_and_element_with_colon(lst)  # jumps into print_index_and_element_with_colon(), runs body, returns
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(print_index_and_element_with_colon(...))  # print_index_and_element_with_colon() runs first → value goes to print()
#
# Loop: takes one item from enumerate(...), runs body, repeats until done
"""
Problème 336 :
Écrivez un programme Python à print chaque élément de une liste avec ses index séparés by un colon en utilisant `enumerate()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : enumerate()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only create_indexed_strings is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → lst = ...  # stored in memory
#   → prefix = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(create_indexed_strings(...))  # create_indexed_strings() runs first → value goes to print()
#
# Loop: takes one item from enumerate(...), runs body, repeats until done
"""
Problème 337 :
Écrivez un programme Python à créer une liste de chaînes où chaque chaîne inclut ses index avec un custom prefix en utilisant `enumerate()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: % ==
# Fonctions intégrées : enumerate()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return lst
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only modify_elements is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(modify_elements(...))  # modify_elements() runs first → value goes to print()
#
# Loop: takes one item from enumerate(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 338 :
Écrivez un programme Python à modify éléments dans une liste based on leur index en utilisant `enumerate()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: % !=
# Fonctions intégrées : enumerate()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → for index, element in enumerate(lst):
#   →     if index % 2 != 0:
#   →         print(element)
#   → for index, element in enumerate(lst):
#   →     if index % 2 != 0:
#   →         print(element)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — print_odd_index_elements, solve are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print_odd_index_elements(lst)  # jumps into print_odd_index_elements(), runs body, returns
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(print_odd_index_elements(...))  # print_odd_index_elements() runs first → value goes to print()
#
# Loop: takes one item from enumerate(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 340 :
Écrivez un programme Python à print éléments de une liste qui sont located at impair indexes en utilisant `enumerate()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: in
# Fonctions intégrées : enumerate()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only index_element_if_vowel is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(index_element_if_vowel(...))  # index_element_if_vowel() runs first → value goes to print()
#
# Loop: takes one item from enumerate(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 341 :
Écrivez un programme Python à créer une liste de tuples où chaque tuple contient un indice et élément de une liste, but seulement si le élément commence par une voyelle, en utilisant `enumerate()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: >
# Fonctions intégrées : enumerate()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return (max_index, max_element)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only find_max_and_index is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → ? = ...  # stored in memory
#   → print(?)
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(find_max_and_index(...))  # find_max_and_index() runs first → value goes to print()
#
# Loop: takes one item from enumerate(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 342 :
Écrivez un programme Python à trouver le maximum élément dans une liste et ses index en utilisant `enumerate()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: >=
# Fonctions intégrées : enumerate()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only index_and_element_excluding_first_n is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → lst = ...  # stored in memory
#   → n = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(index_and_element_excluding_first_n(...))  # index_and_element_excluding_first_n() runs first → value goes to print()
#
# Loop: takes one item from enumerate(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 343 :
Écrivez un programme Python à créer une liste de tuples avec index et élément, but exclude les n premiers éléments en utilisant `enumerate()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: **
# Fonctions intégrées : enumerate()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → for index, number in enumerate(numbers):
#   →     print(f'Index: {index}, Squared: {number ** 2}')
#   → for index, number in enumerate(numbers):
#   →     print(f'Index: {index}, Squared: {number ** 2}')
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — print_index_squared, solve are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print_index_squared(lst)  # jumps into print_index_squared(), runs body, returns
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(print_index_squared(...))  # print_index_squared() runs first → value goes to print()
#
# Loop: takes one item from enumerate(...), runs body, repeats until done
"""
Problème 344 :
Écrivez un programme Python à print chaque nombre dans une liste le long de avec ses index au carré en utilisant `enumerate()`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: % ==
# Fonctions intégrées : enumerate()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return lst
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only replace_based_on_index is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(replace_based_on_index(...))  # replace_based_on_index() runs first → value goes to print()
#
# Loop: takes one item from enumerate(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 345 :
Écrivez un programme Python à replace éléments dans une liste based on leur index en utilisant `enumerate()`. par exemple, replace même indexed éléments avec'même'et impair indexed éléments avec'impair'.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: * +
# Fonctions intégrées : pow, range, square()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return pow(x, x)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sum_of_squares is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → a = ...  # stored in memory
#   → b = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sum_of_squares(...))  # sum_of_squares() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
"""
Problème 346 :
Écrivez un programme Python qui defines une fonction `sum_of_squares()` qui contient un imbriqué fonction `square()` qui squares un nombre. Le `sum_of_squares()` fonction devrait somme le squares des deux nombres.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : get_name, input()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only greet is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
"""
Problème 347 :
Écrivez un programme Python qui defines une fonction `greet()` qui contient un imbriqué fonction `get_name()` à demander le utilisateur pour leur nom. Le `greet()` fonction devrait retourner un message de salutation message en utilisant le nom.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else
# Operators: * - ==
# Fonctions intégrées : inner_factorial()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return 1
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only factorial is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → n = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(factorial(...))  # factorial() runs first → value goes to print()
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 348 :
Écrivez un programme Python qui defines une fonction `la factorielle()` qui contient un imbriqué recursive fonction `inner_factorial()` à calculate la factorielle de un nombre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: % +
# Fonctions intégrées : prefix_func()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return '%s%s' % (prefix, string)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only add_prefix is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → prefix_func = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → prefix_func = ...  # stored in memory
#   → result1 = ...  # stored in memory
#   → result2 = ...  # stored in memory
#   → result3 = ...  # stored in memory
#   → print(result1)
#   → print(result2)
#   → print(result3)
#   → prefix = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(add_prefix(...))  # add_prefix() runs first → value goes to print()
"""
Problème 349 :
Écrivez un programme Python qui defines une fonction `add_prefix()` qui contient un imbriqué fonction `prefix_string()` qui ajoute une donnée prefix à une chaîne. Le `add_prefix()` fonction devrait retourner le prefixed chaîne.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: % ==
# Fonctions intégrées : is_even()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return x % 2 == 0
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only check_even is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → num = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(check_even(...))  # check_even() runs first → value goes to print()
"""
Problème 350 :
Écrivez un programme Python qui defines une fonction `check_even()` qui contient un imbriqué fonction `is_even()` qui vérifie si un nombre est pair. Le `check_even()` fonction devrait retourner si le nombre est pair.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: **
# Fonctions intégrées : calculate_power, pow()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → import math
#   → return math.pow(b, e)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only power is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → base = ...  # stored in memory
#   → exponent = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(power(...))  # power() runs first → value goes to print()
"""
Problème 351 :
Écrivez un programme Python qui defines une fonction `power()` qui contient un imbriqué fonction `calculate_power()` qui raises un nombre à une donnée power. Le `power()` fonction devrait retourner le résultat.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: *
# Fonctions intégrées : calculate_area()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return math.pi * r * r
#   → return math.pi * r * r
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only area_circle is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(area_circle(...))  # area_circle() runs first → value goes to print()
#   → radius = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(area_circle(...))  # area_circle() runs first → value goes to print()
"""
Problème 352 :
Écrivez un programme Python qui defines une fonction `area_circle()` qui contient un imbriqué fonction `calculate_area()` qui calcule le area de un circle donné ses radius. Le `area_circle()` fonction devrait retourner le area.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : capitalize, str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return str(word).capitalize()
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only capitalize_words is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → sentence = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(capitalize_words(...))  # capitalize_words() runs first → value goes to print()
#
# Loop: takes one item from words, runs body, repeats until done
"""
Problème 353 :
Écrivez un programme Python qui defines une fonction `capitalize_words()` qui contient un imbriqué fonction `capitalize()` qui capitalizes un mot. Le `capitalize_words()` fonction devrait retourner une chaîne avec chaque mot capitalized.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: + ==
# Fonctions intégrées : reverse_string, reversed()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → result = ''
#   → for char in s:
#   →     result = char + result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only is_palindrome is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → word = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_palindrome(...))  # is_palindrome() runs first → value goes to print()
#
# Loop: takes one item from s, runs body, repeats until done
"""
Problème 354 :
Écrivez un programme Python qui defines une fonction `is_palindrome()` qui contient un imbriqué fonction `reverse_string()` qui vérifie si une chaîne est un palindrome.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: % +
# Fonctions intégrées : join_strings()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return '%s%s' % (s1, s2)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only concatenate_strings is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → str1 = ...  # stored in memory
#   → str2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(concatenate_strings(...))  # concatenate_strings() runs first → value goes to print()
"""
Problème 355 :
Écrivez un programme Python qui defines une fonction `concatenate_strings()` qui contient un imbriqué fonction `join_strings()` qui concatenates deux strings.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else
# Operators: + - <=
# Fonctions intégrées : fib, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return x
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only fibonacci is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → n = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(fibonacci(...))  # fibonacci() runs first → value goes to print()
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 356 :
Écrivez un programme Python qui defines une fonction `fibonacci()` qui contient un imbriqué recursive fonction `fib()` à générer la suite de Fibonacci up à une donnée nombre de terms.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: - <=
# Fonctions intégrées : chr, convert, ord, str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return str(s).upper()
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only to_uppercase is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(to_uppercase(...))  # to_uppercase() runs first → value goes to print()
"""
Problème 357 :
Écrivez un programme Python qui defines une fonction `to_uppercase()` qui contient un imbriqué fonction `convert()` qui convertit une chaîne à uppercase.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else
# Operators: >
# Fonctions intégrées : compare()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return x
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only find_largest is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → a = ...  # stored in memory
#   → b = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(find_largest(...))  # find_largest() runs first → value goes to print()
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 358 :
Écrivez un programme Python qui defines une fonction `find_largest()` qui contient un imbriqué fonction `compare()` qui compare deux nombres et retourne le larger l'une.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else
# Operators: * + - / != ==
# Fonctions intégrées : add, divide, multiply, subtract, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → import operator
#   → return operator.add(x, y)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only calculator is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → operation = ...  # stored in memory
#   → a = ...  # stored in memory
#   → b = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(calculator(...))  # calculator() runs first → value goes to print()
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 359 :
Écrivez un programme Python qui defines une fonction `calculator()` qui contient imbriqué fonctions pour `add()`, `subtract()`, `multiply()`, et `divide()`. Le `calculator()` fonction devrait perform le selected operation.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: % + < ** ==
# Fonctions intégrées : check_divisibility, int, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return False
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only is_prime is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → n = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_prime(...))  # is_prime() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 360 :
Écrivez un programme Python qui defines une fonction `is_prime()` qui contient un imbriqué fonction `check_divisibility()` à vérifier si un nombre est prime.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: in
# Fonctions intégrées : is_vowel, len, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return len([char for char in string if is_vowel(char)])
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_vowels is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_vowels(...))  # count_vowels() runs first → value goes to print()
#
# Loop: takes one item from string, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 361 :
Écrivez un programme Python qui defines une fonction `count_vowels()` qui contient un imbriqué fonction `is_vowel()` à compter le nombre de voyelles dans une chaîne.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: /
# Fonctions intégrées : len, sum_numbers()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return total
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only calculate_average is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(calculate_average(...))  # calculate_average() runs first → value goes to print()
#
# Loop: takes one item from nums, runs body, repeats until done
"""
Problème 362 :
Écrivez un programme Python qui defines une fonction `calculate_average()` qui contient un imbriqué fonction `sum_numbers()` à calculate le moyenne de une liste de nombres.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: +
# Fonctions intégrées : reverse, reverse_func, reversed()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → result = ''
#   → for char in s:
#   →     result = char + result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only reverse_string is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → reverse_func = ...  # stored in memory
#   → print(reverse_func(...))
#   → result = ...  # stored in memory
#   → print(result)
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(reverse_string(...))  # reverse_string() runs first → value goes to print()
#
# Loop: takes one item from s, runs body, repeats until done
"""
Problème 363 :
Écrivez un programme Python qui defines une fonction `reverse_string()` qui contient un imbriqué fonction `reverse()` qui inverse une donnée chaîne.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: + - > ==
# Fonctions intégrées : len, range, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return False
#   → return False
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — compare_elements, is_sorted are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → lst = ...  # stored in memory
#   → is_sorted()  # jumps into is_sorted(), runs body, returns
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_sorted(...))  # is_sorted() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 364 :
Écrivez un programme Python qui defines une fonction `is_sorted()` qui contient un imbriqué fonction `compare_elements()` à vérifier si une liste est trié dans l'ordre croissant.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: * +
# Fonctions intégrées : pow, range, square()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return pow(x, x)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only generate_squares is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → n = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(generate_squares(...))  # generate_squares() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
"""
Problème 365 :
Écrivez un programme Python qui defines une fonction `generate_squares()` qui contient un imbriqué fonction `square()` à générer une liste de squares de nombres de 1 à n.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: +
# Fonctions intégrées : add, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → import operator
#   → return operator.add(x, y)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sum_of_two is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → a = ...  # stored in memory
#   → b = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sum_of_two(...))  # sum_of_two() runs first → value goes to print()
"""
Problème 366 :
Écrivez un programme Python qui defines un main fonction `sum_of_two()` et un helper fonction `add(a, b)` qui ajoute deux nombres together. Le `sum_of_two()` fonction devrait call le helper fonction et retourner le résultat.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else
# Operators: % ==
# Fonctions intégrées : is_even()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return x % 2 == 0
#   → return x % 2 == 0
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only even_or_odd is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → even_or_odd(10)  # jumps into even_or_odd(), runs body, returns
#   → n = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(even_or_odd(...))  # even_or_odd() runs first → value goes to print()
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 367 :
Écrivez un programme Python qui defines un main fonction `even_or_odd()` et un imbriqué fonction `is_even(n)` qui vérifie si un nombre est pair. Le `even_or_odd()` fonction devrait Utilisez le helper fonction à print si le nombre est pair ou impair.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: * + /
# Fonctions intégrées : celsius_to_fahrenheit()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return c * 9 / 5 + 32
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only convert_temperature is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → celsius = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(convert_temperature(...))  # convert_temperature() runs first → value goes to print()
"""
Problème 368 :
Écrivez un programme Python qui defines un main fonction `convert_temperature()` et un helper fonction `celsius_to_fahrenheit(c)` qui convertit un temperature de Celsius à Fahrenheit. Le `convert_temperature()` fonction devrait Utilisez le helper fonction à retourner le converted temperature.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: *
# Fonctions intégrées : calculate_area, pow, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return pow(l, w)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only rectangle_area is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → length = ...  # stored in memory
#   → width = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(rectangle_area(...))  # rectangle_area() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
"""
Problème 369 :
Écrivez un programme Python qui defines un main fonction `rectangle_area()` et un helper fonction `calculate_area(length, width)` qui calcule le area de un rectangle. Le `rectangle_area()` fonction devrait Utilisez le helper fonction à retourner le area.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: % + < ** ==
# Fonctions intégrées : int, is_prime, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return False
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only check_prime is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → n = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(check_prime(...))  # check_prime() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 370 :
Écrivez un programme Python qui defines un main fonction `check_prime()` et un helper fonction `is_prime(n)` qui vérifie si un nombre est prime. Le `check_prime()` fonction devrait Utilisez le helper fonction à retourner si le nombre est prime.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : min, min_of_three()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return min(x, y, z)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only find_minimum is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → a = ...  # stored in memory
#   → b = ...  # stored in memory
#   → c = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(find_minimum(...))  # find_minimum() runs first → value goes to print()
"""
Problème 371 :
Écrivez un programme Python qui defines un main fonction `find_minimum()` et un helper fonction `min_of_three(a, b, c)` qui retourne le minimum de trois nombres. Le `find_minimum()` fonction devrait Utilisez le helper fonction à retourner le minimum valeur.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: + == or
# Fonctions intégrées : factorial, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return 1
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only calculate_factorial is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → n = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(calculate_factorial(...))  # calculate_factorial() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 373 :
Écrivez un programme Python qui defines un main fonction `calculate_factorial()` et un helper fonction `la factorielle(n)` qui calcule la factorielle de un nombre. Le `calculate_factorial()` fonction devrait Utilisez le helper fonction à retourner la factorielle.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: +
# Fonctions intégrées : capitalize()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return word[0].upper() + word[1:]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only capitalize_words is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → sentence = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(capitalize_words(...))  # capitalize_words() runs first → value goes to print()
#
# Loop: takes one item from words, runs body, repeats until done
"""
Problème 374 :
Écrivez un programme Python qui defines un main fonction `capitalize_words()` et un helper fonction `capitalize(word)` qui capitalizes le premier lettre de un mot. Le `capitalize_words()` fonction devrait Utilisez le helper fonction à capitalize chaque mot dans une phrase.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: >
# Fonctions intégrées : max, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → numbers = [12, 45, 7, 23, 56, 89, 34]
#   → largest = max_in_list(numbers)
#   → return largest
#   → numbers = [12, 45, 7, 23, 56, 89, 34]
#   → largest = max_in_list(numbers)
#   → return largest
#   → result = lst[0]
#   → for item in lst:
#   →     if item > result:
#   →         result = item
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — find_largest, max_in_list are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(find_largest(...))  # find_largest() runs first → value goes to print()
#   → print(find_largest(...))  # find_largest() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(max_in_list(...))  # max_in_list() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 375 :
Écrivez un programme Python qui defines un main fonction `find_largest()` et un helper fonction `max_in_list(lst)` qui retourne le plus grand nombre dans une liste. Le `find_largest()` fonction devrait Utilisez le helper fonction à trouver et retourner le plus grand nombre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: +
# Fonctions intégrées : reverse()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return reversed_str
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only reverse_string is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → s = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(reverse_string(...))  # reverse_string() runs first → value goes to print()
#
# Loop: takes one item from s, runs body, repeats until done
"""
Problème 376 :
Écrivez un programme Python qui defines un main fonction `reverse_string()` et un helper fonction `reverse(s)` qui inverse une donnée chaîne. Le `reverse_string()` fonction devrait Utilisez le helper fonction à retourner le inversé chaîne.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: /
# Fonctions intégrées : average, len()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return total / len(lst)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only calculate_average is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(calculate_average(...))  # calculate_average() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
"""
Problème 377 :
Écrivez un programme Python qui defines un main fonction `calculate_average()` et un helper fonction `moyenne(lst)` qui calcule le moyenne de une liste de nombres. Le `calculate_average()` fonction devrait Utilisez le helper fonction à retourner le moyenne.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: ==
# Fonctions intégrées : is_palindrome()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return s == s[::-1]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only check_palindrome is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → s = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(check_palindrome(...))  # check_palindrome() runs first → value goes to print()
"""
Problème 378 :
Écrivez un programme Python qui defines un main fonction `check_palindrome()` et un helper fonction `is_palindrome(s)` qui vérifie si une chaîne est un palindrome. Le `check_palindrome()` fonction devrait Utilisez le helper fonction à retourner si la chaîne est un palindrome.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: <
# Fonctions intégrées : abs()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return closest
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only closest_to_zero is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(closest_to_zero(...))  # closest_to_zero() runs first → value goes to print()
#
# Loop: takes one item from numbers, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 379 :
Écrivez un programme Python à trouver le nombre closest à zero dans une liste de nombres en utilisant le `key` paramètre dans le `min()` fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: + - >
# Fonctions intégrées : is_sorted, len, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return False
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only check_sorted is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(check_sorted(...))  # check_sorted() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 380 :
Écrivez un programme Python qui defines un main fonction `check_sorted()` et un helper fonction `is_sorted(lst)` qui vérifie si une liste est trié dans l'ordre croissant. Le `check_sorted()` fonction devrait Utilisez le helper fonction à retourner si la liste est trié.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : input, list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(int, strings))
#   → return list(map(int, strings))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only convert_to_integers is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → user = ...  # stored in memory
#   → print(list(...))
#   → numbers_in_strings = ...  # stored in memory
#   → print(convert_to_integers(...))  # convert_to_integers() runs first → value goes to print()
#   → strings = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(convert_to_integers(...))  # convert_to_integers() runs first → value goes to print()
"""
Problème 381 :
Écrivez une fonction où utilisateur tapez une liste de nombres dans chaîne et retourne une liste de nombres dans integer. N'utilisez pas un pour loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sorted_strings
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_strings_by_length is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → strings = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_strings_by_length(...))  # sort_strings_by_length() runs first → value goes to print()
"""
Problème 382 :
Écrivez un programme Python à trier une liste de chaînes by leur longueur en utilisant le `key` paramètre dans le `sorted()` fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sorted_tuples
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_tuples_by_second is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → tuples = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_tuples_by_second(...))  # sort_tuples_by_second() runs first → value goes to print()
"""
Problème 384 :
Écrivez un programme Python à trier une liste de tuples based on le deuxième élément en utilisant le `key` paramètre dans le `sorted()` fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sorted_dicts
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_dicts_by_key is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → dicts = ...  # stored in memory
#   → key_name = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_dicts_by_key(...))  # sort_dicts_by_key() runs first → value goes to print()
"""
Problème 385 :
Écrivez un programme Python à trier une liste de dictionnaires based on le valeur de un spécifique clé en utilisant le `key` paramètre dans le `sorted()` fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: >
# Fonctions intégrées : len()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return longest
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only longest_word is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → words = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(longest_word(...))  # longest_word() runs first → value goes to print()
#
# Loop: takes one item from words, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 386 :
Écrivez un programme Python à trouver le plus long mot dans une liste de mots en utilisant le `key` paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sorted_numbers
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_by_absolute_value is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_by_absolute_value(...))  # sort_by_absolute_value() runs first → value goes to print()
"""
Problème 387 :
Écrivez un programme Python à trier une liste de nombres based on leur absolute valeur en utilisant le `key` paramètre dans le `sorted()` fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → def inner(word):
#   →     return word[-1]
#   → return list(sorted(lst, key=inner))
#   → return sorted_strings
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — main, sort_strings_by_last_character are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → lst = ...  # stored in memory
#   → main(lst)  # jumps into main(), runs body, returns
#   → strings = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_strings_by_last_character(...))  # sort_strings_by_last_character() runs first → value goes to print()
"""
Problème 388 :
Écrivez un programme Python à trier une liste de chaînes by le dernier caractère de chaque chaîne en utilisant le `key` paramètre dans le `sorted()` fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: <
# Fonctions intégrées : min, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → result = dates[0]
#   → for item in dates:
#   →     if item < result:
#   →         result = item
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only earliest_date is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → dates = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(earliest_date(...))  # earliest_date() runs first → value goes to print()
#
# Loop: takes one item from dates, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 389 :
Écrivez un programme Python à trouver le earliest date dans une liste de date strings (dans'YYYY-MM-DD'format) en utilisant le `key` paramètre dans le `min()` fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return name.split()[-1]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only get_surname is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → names = ...  # stored in memory
#   → sorted_names = ...  # stored in memory
#   → print(sorted_names)
#   → name = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(get_surname(...))  # get_surname() runs first → value goes to print()
"""
Problème 390 :
Écrivez un programme Python à trier une liste de noms by surname en utilisant le `key` paramètre dans le `sorted()` fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sorted(strings, key=str.lower)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_strings_alphabetically is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → strings = ...  # stored in memory
#   → sorted_strings = ...  # stored in memory
#   → print(sorted_strings)
#   → strings = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_strings_alphabetically(...))  # sort_strings_alphabetically() runs first → value goes to print()
"""
Problème 391 :
Écrivez un programme Python à trier une liste de chaînes alphabetically, en ignorant la casse, en utilisant le `key` paramètre dans le `sorted()` fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : max()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return total_score
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — find_highest_scrabble_word, scrabble_score are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → word = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(scrabble_score(...))  # scrabble_score() runs first → value goes to print()
#
# Loop: takes one item from word.upper(...), runs body, repeats until done
"""
Problème 392 :
Écrivez un programme Python à trouver le mot avec le plus haut Scrabble score dans une liste de mots en utilisant le `key` paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: +
# Fonctions intégrées : abs, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return abs(c)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_complex_numbers is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → complex_numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_complex_numbers(...))  # sort_complex_numbers() runs first → value goes to print()
"""
Problème 393 :
Écrivez un programme Python à trier une liste de complexe nombres by leur magnitude en utilisant le `key` paramètre dans le `sorted()` fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : max()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return os.path.getsize(file_path)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only find_largest_file is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → file_paths = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(find_largest_file(...))  # find_largest_file() runs first → value goes to print()
"""
Problème 394 :
Écrivez un programme Python à trouver le file avec le plus grand size dans une liste de file paths en utilisant le `key` paramètre et `os.path.getsize`.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : Fraction, float, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return float(frac)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_fractions is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → fractions = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_fractions(...))  # sort_fractions() runs first → value goes to print()
"""
Problème 395 :
Écrivez un programme Python à trier une liste de fractions (en utilisant le `fractions.Fraction` class) by leur valeur en utilisant le `key` paramètre dans le `sorted()` fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: +
# Fonctions intégrées : list, reduce, sorted, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → def inner(tup):
#   →     return tup[0] + tup[1]
#   → return list(sorted(lst_tuples, key=inner))
#   → from functools import reduce
#   → import operator
#   → return reduce(operator.add, tup, 0)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — main, sort_tuples_by_sum are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → lst_tuples = ...  # stored in memory
#   → print(main(...))  # main() runs first → value goes to print()
#   → tuples = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_tuples_by_sum(...))  # sort_tuples_by_sum() runs first → value goes to print()
#
# Loop: takes one item from tup, runs body, repeats until done
"""
Problème 396 :
Écrivez un programme Python à trier une liste de tuples based on le somme de leur éléments en utilisant le `key` paramètre dans le `sorted()` fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : min()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return closest
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only closest_to_zero is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(closest_to_zero(...))  # closest_to_zero() runs first → value goes to print()
"""
Problème 397 :
Écrivez un programme Python à trouver le nombre closest à zero dans une liste de nombres en utilisant le `key` paramètre dans le `min()` fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: + **
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return (point[0] ** 2 + point[1] ** 2) ** 0.5
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_points_by_distance is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → points = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_points_by_distance(...))  # sort_points_by_distance() runs first → value goes to print()
"""
Problème 398 :
Écrivez un programme Python à trier une liste de 2D points (tuples) by leur distance de le origin en utilisant le `key` paramètre dans le `sorted()` fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : len, set, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return len(set(word))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_words_by_distinct_letters is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → words = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_words_by_distinct_letters(...))  # sort_words_by_distinct_letters() runs first → value goes to print()
"""
Problème 399 :
Écrivez un programme Python à trier une liste de mots by le nombre de distinct lettre dans chaque mot en utilisant le `key` paramètre dans le `sorted()` fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : max, ord()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return count
#   → return count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — ascii_value, find_highest_ascii_word, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → main(lst)  # jumps into main(), runs body, returns
#   → result = ...  # stored in memory
#   → print(result)
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(main(...))  # main() runs first → value goes to print()
#
# Loop: takes one item from word, runs body, repeats until done
"""
Problème 400 :
Écrivez un programme Python à trouver le mot avec le plus haut somme de ASCII valeurs de ses caractères dans une liste de mots en utilisant le `key` paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: in
# Fonctions intégrées : len, sorted, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return len([char for char in s if char in vowels])
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — count_vowels, sort_by_vowel_count are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → strings = ...  # stored in memory
#   → sorted_strings = ...  # stored in memory
#   → print(sorted_strings)
#   → s = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_vowels(...))  # count_vowels() runs first → value goes to print()
#
# Loop: takes one item from s, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 401 :
Écrivez un programme Python à trier une liste de chaînes by le nombre de voyelles dans chaque chaîne en utilisant le `key` paramètre dans le `sorted()` fonction."
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(str, integers))
#   → return list(map(str, integers))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only convert_to_integers is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → print(convert_to_integers(...))  # convert_to_integers() runs first → value goes to print()
#   → integers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(convert_to_integers(...))  # convert_to_integers() runs first → value goes to print()
"""
Problème 402 :
Écrivez une fonction où utilisateur transforms une liste d'entiers dans une liste de chaînes. N'utilisez pas un pour loop.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: +
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(lambda number: number + 5, lst))
#   → return list(map(lambda number: number + 5, lst))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only add_five is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(add_five(...))  # add_five() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(add_five(...))  # add_five() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
"""
Problème 403 :
Écrivez un programme Python à add 5 à chaque nombre dans une liste. N'utilisez pas map().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: <
# Fonctions intégrées : input, int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return min_num
#   → int_lst = []
#   → for num in user:
#   →     int_lst.append(int(num))
#   → min_num = int_lst[0]
#   → for num in int_lst:
#   →     if num < min_num:
#   →         min_num = num
#   → return min_num
#   → return min_num
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — find_min, main are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(find_min(...))  # find_min() runs first → value goes to print()
#   → user = ...  # stored in memory
#   → main(user)  # jumps into main(), runs body, returns
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(find_min(...))  # find_min() runs first → value goes to print()
#
# Loop: takes one item from numbers, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 404 :
Écrivez une fonction Python appelée `find_min` qui prend une liste de nombres en entrée et retourne le minimum nombre dans la liste. N'utilisez pas min().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: *
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → inch = cm * 0.39
#   → result = inch
#   → return result
#   → inch = cm * 0.39
#   → result = inch
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only converts is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → number = ...  # stored in memory
#   → print(converts(...))  # converts() runs first → value goes to print()
#   → cm = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(converts(...))  # converts() runs first → value goes to print()
"""
Problème 405 :
Écrivez une fonction qui convertit centimetets à inches. tapez un integer as argument.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return lst
#   → return lst
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only reverse is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(reverse(...))  # reverse() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(reverse(...))  # reverse() runs first → value goes to print()
"""
Problème 406 :
Écrivez un programme Python à reverse une liste Utilisez le reverse() fonction. demander le utilisateur à saisir une liste d'éléments.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: * /
# Fonctions intégrées : Fraction, float()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → from fractions import Fraction
#   → return float(Fraction(add_num, length_num))
#   → from fractions import Fraction
#   → return float(Fraction(add_num, length_num))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only calculate_average is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(calculate_average(...))  # calculate_average() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(calculate_average(...))  # calculate_average() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
"""
Problème 407 :
Écrivez une fonction Python appelée `calculate_average` qui prend une liste de nombres en entrée et retourne le moyenne de ces nombres. N'utilisez pas sum() et len().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: in
# Fonctions intégrées : list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(lambda word: word, lst))
#   → return list(map(lambda word: word, lst))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only remove_duplicates is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(remove_duplicates(...))  # remove_duplicates() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(remove_duplicates(...))  # remove_duplicates() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 408 :
Écrivez une fonction Python appelée remove_duplicates qui prend une chaîne en entrée et retourne une nouvelle chaîne avec en double caractères removed, avec maintaining le original order de caractères.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only len_words is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(len_words(...))  # len_words() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(len_words(...))  # len_words() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
"""
Problème 409 :
Écrivez un programme qui maps une liste de mots dans une liste d'entiers representing le lengths de le correponding words sans en utilisant len(). Utilisez un dictionnaire.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: ==
# Fonctions intégrées : len, list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(lambda word: word, lst))
#   → return list(map(lambda word: word, lst))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only filter_string is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(filter_string(...))  # filter_string() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(filter_string(...))  # filter_string() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 410 :
Écrivez un programme Python à determine le len de une chaîne dans une liste. N'utilisez pas filtrer(). par exemple si le len est 3 et la liste est ["jon", "chris", "tom", "Jeremy"] le résultat devrait be ["jon", "tom"].
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: +
# Fonctions intégrées : inner_sum, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → import operator
#   → return operator.add(x, y)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only calculate_sum is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → a = ...  # stored in memory
#   → b = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(calculate_sum(...))  # calculate_sum() runs first → value goes to print()
"""
Problème 411 :
Écrivez une fonction Python appelée calculate_sum qui prend deux nombres as arguments. à l'intérieur de cette fonction, define un imbriqué fonction qui retourne leur somme."
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: *
# Fonctions intégrées : pow, product, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return pow(a, b)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only calculate_product is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → a = ...  # stored in memory
#   → b = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(calculate_product(...))  # calculate_product() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
"""
Problème 412 :
Écrivez une fonction Python appelée calculate_product qui prend deux nombres as arguments. à l'intérieur de cette fonction, define un imbriqué fonction qui retourne leur produit.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: + -
# Fonctions intégrées : difference()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → import operator
#   → return operator.sub(a, b)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only calculate_difference is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → a = ...  # stored in memory
#   → b = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(calculate_difference(...))  # calculate_difference() runs first → value goes to print()
"""
Problème 413 :
Écrivez une fonction Python appelée calculate_difference qui prend deux nombres as arguments. à l'intérieur de cette fonction, define un imbriqué fonction qui retourne leur différence.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: * /
# Fonctions intégrées : Fraction, float, quotient()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → from fractions import Fraction
#   → return float(Fraction(a, b))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only calculate_quotient is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → a = ...  # stored in memory
#   → b = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(calculate_quotient(...))  # calculate_quotient() runs first → value goes to print()
"""
Problème 414 :
Écrivez une fonction Python appelée calculate_quotient qui prend deux nombres as arguments. à l'intérieur de cette fonction, define un imbriqué fonction qui retourne leur quotient.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: *
# Fonctions intégrées : area, pow, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return pow(length, width)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only area_of_rectangle is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → length = ...  # stored in memory
#   → width = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(area_of_rectangle(...))  # area_of_rectangle() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
"""
Problème 415 :
Write un Python fonction area_of_rectangle qui calcule le area de un rectangle donné ses longueur et width. Utilisez un imbriqué fonction à calculate le area.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: *
# Fonctions intégrées : perimeter, pow, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return pow(4, side_length)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only perimeter_of_square is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → side_length = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(perimeter_of_square(...))  # perimeter_of_square() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
"""
Problème 416 :
Write un Python fonction perimeter_of_square qui calcule le perimeter de un carré donné ses side longueur. Utilisez un imbriqué fonction à calculate le perimeter.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: * - /
# Fonctions intégrées : convert()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return (fahrenheit - 32) * 5 / 9
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only fahrenheit_to_celsius is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → fahrenheit = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(fahrenheit_to_celsius(...))  # fahrenheit_to_celsius() runs first → value goes to print()
"""
Problème 417 :
Écrivez une fonction Python appelée fahrenheit_to_celsius qui prend un temperature dans Fahrenheit et convertit it à Celsius. Utilisez un imbriqué fonction à do le conversion.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: * + /
# Fonctions intégrées : convert()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return celsius * 9 / 5 + 32
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only celsius_to_fahrenheit is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → celsius = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(celsius_to_fahrenheit(...))  # celsius_to_fahrenheit() runs first → value goes to print()
"""
Problème 418 :
Écrivez une fonction Python appelée celsius_to_fahrenheit qui prend un temperature dans Celsius et convertit it à Fahrenheit. Utilisez un imbriqué fonction à do le conversion.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else
# Operators: % ==
# Fonctions intégrées : check()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return 'Even'
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only even_or_odd is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → number = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(even_or_odd(...))  # even_or_odd() runs first → value goes to print()
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 419 :
Écrivez une fonction Python appelée even_or_odd qui prend un nombre et retourne si it’s même ou impair. Utilisez un imbriqué fonction à check cette condition.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: % + < ** ==
# Fonctions intégrées : check_divisibility, int, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return False
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only is_prime is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → number = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_prime(...))  # is_prime() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 420 :
Écrivez une fonction Python appelée is_prime qui vérifie si un nombre est prime. Utilisez un imbriqué fonction à iterate et check divisibility de nombres.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : add_elements()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return total
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only list_sum is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(list_sum(...))  # list_sum() runs first → value goes to print()
#
# Loop: takes one item from numbers, runs body, repeats until done
"""
Problème 421 :
Écrivez une fonction Python appelée list_sum qui prend une liste de nombres et retourne le somme. à l'intérieur de it, define un imbriqué fonction qui ajoute le éléments.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : multiply_elements()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return product
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only list_product is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(list_product(...))  # list_product() runs first → value goes to print()
#
# Loop: takes one item from numbers, runs body, repeats until done
"""
Problème 422 :
Écrivez une fonction Python appelée list_product qui prend une liste de nombres et retourne le produit de tous éléments. Utilisez un imbriqué fonction à compute le produit.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else
# Operators: > <=
# Fonctions intégrées : compare()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return not a <= b
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only greater_than is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → a = ...  # stored in memory
#   → b = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(greater_than(...))  # greater_than() runs first → value goes to print()
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 423 :
Write un Python fonction greater_than qui prend deux nombres et retourne vrai si le premier est greater que le deuxième. Utilisez un imbriqué fonction pour comparison.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : calculate_length()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return length
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only string_length is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → s = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(string_length(...))  # string_length() runs first → value goes to print()
#
# Loop: takes one item from s, runs body, repeats until done
"""
Problème 424 :
Write un Python fonction string_length qui prend une chaîne et retourne ses longueur. Utilisez un imbriqué fonction qui calcule et retourne la longueur.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else
# Operators: >
# Fonctions intégrées : get_first_last, len()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return (s[0], s[-1])
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only first_and_last is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → s = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(first_and_last(...))  # first_and_last() runs first → value goes to print()
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 425 :
Write un Python fonction first_and_last qui prend une chaîne et retourne ses premier et dernier caractères en utilisant un imbriqué fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: in
# Fonctions intégrées : is_vowel, len, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return len([char for char in s if is_vowel(char)])
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only count_vowels is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → s = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(count_vowels(...))  # count_vowels() runs first → value goes to print()
#
# Loop: takes one item from s, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 426 :
Write un Python fonction count_vowels qui prend une chaîne et compte le nombre de voyelles en utilisant un imbriqué fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: +
# Fonctions intégrées : reverse()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return reversed_s
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only reverse_string is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → s = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(reverse_string(...))  # reverse_string() runs first → value goes to print()
#
# Loop: takes one item from s, runs body, repeats until done
"""
Problème 427 :
Write un Python fonction reverse_string qui prend une chaîne et retourne ses reverse en utilisant un imbriqué fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: ==
# Fonctions intégrées : check()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return s == s[::-1]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only is_palindrome is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → s = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_palindrome(...))  # is_palindrome() runs first → value goes to print()
"""
Problème 428 :
Write un Python fonction is_palindrome qui prend une chaîne et vérifie si it’s un palindrome en utilisant un imbriqué fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: *
# Fonctions intégrées : multiply_by_3, pow, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return pow(n, x)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only multiply_by_n is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → multiply_by_3 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → n = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(multiply_by_n(...))  # multiply_by_n() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
"""
Problème 429 :
Write un Python fonction multiply_by_n qui prend un nombre n et retourne un autre fonction qui multiplie une donnée nombre by n.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: * +
# Fonctions intégrées : calculate_tax()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return price + price * tax_rate
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only add_tax is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → price = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(add_tax(...))  # add_tax() runs first → value goes to print()
"""
Problème 430 :
Write un Python fonction add_tax qui prend un price et retourne le price après applying un tax percentage en utilisant un imbriqué fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: %
# Fonctions intégrées : greeting()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return 'Hello, %s!' % name
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only greet_person is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → name = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(greet_person(...))  # greet_person() runs first → value goes to print()
"""
Problème 431 :
Write un Python fonction greet_person qui prend un nom et retourne un message de salutation en utilisant un imbriqué fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else
# Operators: * - == or
# Fonctions intégrées : calc_factorial()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return 1
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only factorial is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → n = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(factorial(...))  # factorial() runs first → value goes to print()
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 432 :
Write un Python fonction la factorielle qui calcule la factorielle de un nombre en utilisant un imbriqué recursive fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : calculate, range()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return result
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only exponent is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → base = ...  # stored in memory
#   → power = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(exponent(...))  # exponent() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
"""
Problème 433 :
Write un Python fonction exponent qui calcule le résultat de raising un nombre à un power en utilisant un imbriqué fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: while
# Operators: % !=
# Fonctions intégrées : calculate_gcd()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return x
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only gcd is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → a = ...  # stored in memory
#   → b = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(gcd(...))  # gcd() runs first → value goes to print()
#
# Loop: check condition → if True run body → check again
"""
Problème 434 :
Write un Python fonction gcd qui calcule le greatest commun divisor des deux nombres en utilisant un imbriqué fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: while
# Operators: % * != //
# Fonctions intégrées : abs, calculate_lcm, gcd()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return abs(x * y) // gcd(x, y)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only lcm is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → a = ...  # stored in memory
#   → b = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(lcm(...))  # lcm() runs first → value goes to print()
#
# Loop: check condition → if True run body → check again
"""
Problème 435 :
Write un Python fonction lcm qui calcule le moins commun multiple des deux nombres en utilisant un imbriqué fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: *
# Fonctions intégrées : pow, range, square()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return pow(n, n)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only square_of_number is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → n = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(square_of_number(...))  # square_of_number() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
"""
Problème 436 :
Write un Python fonction square_of_number qui retourne le carré de un nombre en utilisant un imbriqué fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: *
# Fonctions intégrées : cube()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return n * n * n
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only cube_of_number is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → n = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(cube_of_number(...))  # cube_of_number() runs first → value goes to print()
"""
Problème 437 :
Write un Python fonction cube_of_number qui retourne le cube de un nombre en utilisant un imbriqué fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else | while
# Operators: >
# Fonctions intégrées : list, map, sort()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(lambda item: maximum, lst))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_list_descending is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_list_descending(...))  # sort_list_descending() runs first → value goes to print()
#
# Loop: check condition → if True run body → check again
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 438 :
Write un Python fonction sort_list_descending qui prend une liste et trie it dans l'ordre décroissant en utilisant un imbriqué fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else
# Operators: >
# Fonctions intégrées : find_max()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return max_value
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only max_of_three is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → a = ...  # stored in memory
#   → b = ...  # stored in memory
#   → c = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(max_of_three(...))  # max_of_three() runs first → value goes to print()
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 439 :
Write un Python fonction max_of_three qui prend trois nombres et retourne le maximum en utilisant un imbriqué fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: / !=
# Fonctions intégrées : calculate_average()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return total / count if count != 0 else 0
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only average_of_list is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(average_of_list(...))  # average_of_list() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
"""
Problème 440 :
Write un Python fonction average_of_list qui calcule le moyenne de une liste de nombres en utilisant un imbriqué fonction. N'utilisez pas sum() et len()
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: / !=
# Fonctions intégrées : calculate_average()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return total / count if count != 0 else 0
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only average_of_list is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(average_of_list(...))  # average_of_list() runs first → value goes to print()
#
# Loop: takes one item from lst, runs body, repeats until done
"""
Problème 441 :
Write un Python fonction average_of_list qui calcule le moyenne de une liste de nombres en utilisant un imbriqué fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Fonctions intégrées : check()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return False
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only is_uppercase is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → s = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_uppercase(...))  # is_uppercase() runs first → value goes to print()
#
# Loop: takes one item from s, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 442 :
Write un Python fonction is_uppercase qui vérifie si tous caractères dans une chaîne sont uppercase en utilisant un imbriqué fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Fonctions intégrées : check()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return False
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only is_lowercase is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → result = ...  # stored in memory
#   → print(result)
#   → s = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(is_lowercase(...))  # is_lowercase() runs first → value goes to print()
#
# Loop: takes one item from s, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 443 :
Write un Python fonction is_lowercase qui vérifie si tous caractères dans une chaîne sont lowercase en utilisant un imbriqué fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Fonctions intégrées : contains_digit()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return True
#   → return True
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only string_contains_digit is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → string = ...  # stored in memory
#   → print(string_contains_digit(...))  # string_contains_digit() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(string_contains_digit(...))  # string_contains_digit() runs first → value goes to print()
#
# Loop: takes one item from x, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 444 :
Write un Python fonction string_contains_digit qui vérifie si une chaîne contient un chiffre en utilisant un imbriqué fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Fonctions intégrées : contains_letter()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return True
#   → return True
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only string_contains_letter is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → string = ...  # stored in memory
#   → print(string_contains_letter(...))  # string_contains_letter() runs first → value goes to print()
#   → string = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(string_contains_letter(...))  # string_contains_letter() runs first → value goes to print()
#
# Loop: takes one item from x, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 445 :
Write un Python fonction string_contains_letter qui vérifie si une chaîne contient une lettre en utilisant un imbriqué fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: * /
# Fonctions intégrées : Fraction, average, float, len, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → from fractions import Fraction
#   → return float(Fraction(add_num, count_len))
#   → from fractions import Fraction
#   → return float(Fraction(add_num, count_len))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only average_of_list is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(average_of_list(...))  # average_of_list() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(average_of_list(...))  # average_of_list() runs first → value goes to print()
#
# Loop: takes one item from x, runs body, repeats until done
"""
Problème 446 :
Write un Python fonction calculate_average qui prend trois nombres et retourne leur moyenne en utilisant un imbriqué fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: % ==
# Fonctions intégrées : is_multiple()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return x % y == 0
#   → return x % y == 0
#   → return x % y == 0
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only check_multiple_of_n is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(check_multiple_of_n(...))  # check_multiple_of_n() runs first → value goes to print()
#   → print(check_multiple_of_n(...))  # check_multiple_of_n() runs first → value goes to print()
#   → num1 = ...  # stored in memory
#   → num2 = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(check_multiple_of_n(...))  # check_multiple_of_n() runs first → value goes to print()
"""
Problème 447 :
Write un Python fonction check_multiple_of_n qui prend deux nombres et vérifie si le premier est un multiple de le deuxième en utilisant un imbriqué fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: >
# Fonctions intégrées : find_longest, longest, max()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return longest_word
#   → return longest_word
#   → return longest_word
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only longest_string is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(longest_string(...))  # longest_string() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → print(longest_string(...))  # longest_string() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(longest_string(...))  # longest_string() runs first → value goes to print()
#
# Loop: takes one item from x, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 448 :
Write un Python fonction longest_string qui prend une liste de chaînes et retourne le plus long l'une en utilisant un imbriqué fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : min, shortest()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return min(x, key=len)
#   → return min(x, key=len)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only shortest_string is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(shortest_string(...))  # shortest_string() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(shortest_string(...))  # shortest_string() runs first → value goes to print()
"""
Problème 449 :
Write un Python fonction shortest_string qui prend une liste de chaînes et retourne le plus court l'une en utilisant un imbriqué fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: not in
# Fonctions intégrées : duplicates_removed, list, map()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return list(map(lambda item: item, items))
#   → return list(map(lambda item: item, items))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only remove_duplicates is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(remove_duplicates(...))  # remove_duplicates() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(remove_duplicates(...))  # remove_duplicates() runs first → value goes to print()
#
# Loop: takes one item from items, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 450 :
Write un Python fonction remove_duplicates qui prend une liste et supprime les doublons en utilisant un imbriqué fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: if/else
# Operators: + - <=
# Fonctions intégrées : fib_recursive()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return n
#   → return n
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only fibonacci is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → n = ...  # stored in memory
#   → print(fibonacci(...))  # fibonacci() runs first → value goes to print()
#   → n = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(fibonacci(...))  # fibonacci() runs first → value goes to print()
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 451 :
Write un Python fonction fibonacci qui génère le nth Fibonacci nombre en utilisant un imbriqué recursive fonction.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: * +
# Fonctions intégrées : inner_mult, inner_sum, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → import operator
#   → return operator.add(x, y)
#   → import operator
#   → return operator.add(x, y)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only calculate_sum is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(calculate_sum(...))  # calculate_sum() runs first → value goes to print()
#   → a = ...  # stored in memory
#   → b = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(calculate_sum(...))  # calculate_sum() runs first → value goes to print()
"""
Problème 452 :
Écrivez une fonction Python appelée calculate_sum qui prend deux nombres as arguments. à l'intérieur de cette fonction, define un imbriqué fonction qui retourne leur somme et un autre fonction qui retourne le multiplication."
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: * + /
# Fonctions intégrées : division, pow, product, range, sum_int()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return pow(x, y)
#   → return pow(x, y)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only calculate_integers is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(calculate_integers(...))  # calculate_integers() runs first → value goes to print()
#   → a = ...  # stored in memory
#   → b = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(calculate_integers(...))  # calculate_integers() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
"""
Problème 453 :
Écrivez une fonction Python appelée calculate_integers qui prend deux nombres as arguments. à l'intérieur de cette fonction, define imbriqué fonctions qui retourne leur produit, somme et division.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: * /
# Fonctions intégrées : Fraction, average, float, len, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → from fractions import Fraction
#   → return float(Fraction(add_num, count_len))
#   → from fractions import Fraction
#   → return float(Fraction(add_num, count_len))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only average_of_list is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(average_of_list(...))  # average_of_list() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(average_of_list(...))  # average_of_list() runs first → value goes to print()
#
# Loop: takes one item from x, runs body, repeats until done
"""
Problème 455 :
Write un Python fonction average_of_list qui calcule le moyenne de une liste de nombres en utilisant un imbriqué fonction. Utilisez len() et sum().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sort
#   → return sort
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only len_lst is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(len_lst(...))  # len_lst() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(len_lst(...))  # len_lst() runs first → value goes to print()
"""
Problème 456 :
Write un Python fonction qui trie une liste de chaînes by leur longueur en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : min()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return min_string
#   → return min_string
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only min_len is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(min_len(...))  # min_len() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(min_len(...))  # min_len() runs first → value goes to print()
"""
Problème 457 :
Write un Python fonction à trouver le minimum chaîne by ses longueur en utilisant le min() fonction avec la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : max()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return word
#   → return word
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only max_string_alpha is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(max_string_alpha(...))  # max_string_alpha() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(max_string_alpha(...))  # max_string_alpha() runs first → value goes to print()
"""
Problème 458 :
Write un Python fonction à trouver le maximum chaîne alphabetically en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : itemgetter, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sorted(dict_list, key=itemgetter(sort_key))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_dicts_by_key is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dict_list = ...  # stored in memory
#   → sorted_list = ...  # stored in memory
#   → print(sorted_list)
#   → dict_list = ...  # stored in memory
#   → sort_key = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_dicts_by_key(...))  # sort_dicts_by_key() runs first → value goes to print()
"""
Problème 459 :
Write un Python fonction à trier une liste de dictionnaires by le valeur associated avec un spécifique clé en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sorted(lst, key=abs)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_by_absolute_value is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → sorted_lst = ...  # stored in memory
#   → print(sorted_lst)
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_by_absolute_value(...))  # sort_by_absolute_value() runs first → value goes to print()
"""
Problème 460 :
Write un Python fonction à trier une liste d'entiers by leur absolute valeur en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: in
# Fonctions intégrées : len, sorted, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return len([char for char in word if char in vowels])
#   → return len([char for char in word if char in vowels])
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_words_by_vowel_count is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(sort_words_by_vowel_count(...))  # sort_words_by_vowel_count() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_words_by_vowel_count(...))  # sort_words_by_vowel_count() runs first → value goes to print()
#
# Loop: takes one item from word, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 461 :
Write un Python fonction qui trie une liste de mots by le nombre de voyelles they contien en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : max()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return longest_w
#   → return longest_w
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only longest_word is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(longest_word(...))  # longest_word() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(longest_word(...))  # longest_word() runs first → value goes to print()
"""
Problème 462 :
Write un Python fonction à trouver le plus long mot dans une liste en utilisant le max() fonction avec la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sorted(lst, key=sum)
#   → return sorted(lst, key=sum)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sum_of_tuple is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(sum_of_tuple(...))  # sum_of_tuple() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sum_of_tuple(...))  # sum_of_tuple() runs first → value goes to print()
"""
Problème 463 :
Write un Python fonction à trier une liste de tuples by le somme de le éléments dans chaque tuple en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return s[-1]
#   → return s[-1]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only list_of_strings_lst is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(list_of_strings_lst(...))  # list_of_strings_lst() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(list_of_strings_lst(...))  # list_of_strings_lst() runs first → value goes to print()
"""
Problème 464 :
Write un Python fonction à trier une liste de chaînes by le dernier caractère de chaque chaîne en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Fonctions intégrées : len, sorted, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return len([char for char in x if char.isupper()])
#   → return len([char for char in x if char.isupper()])
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_number_uppercases is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(sort_number_uppercases(...))  # sort_number_uppercases() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_number_uppercases(...))  # sort_number_uppercases() runs first → value goes to print()
#
# Loop: takes one item from x, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 465 :
Write un Python fonction à trier une liste de chaînes by le nombre de uppercase lettre dans chaque chaîne en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : max()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return count
#   → return count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only tuple_largest_product is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(tuple_largest_product(...))  # tuple_largest_product() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(tuple_largest_product(...))  # tuple_largest_product() runs first → value goes to print()
#
# Loop: takes one item from x, runs body, repeats until done
"""
Problème 466 :
Write un Python fonction à trouver le tuple avec le plus grand produit de ses éléments en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sorted(numbers, key=round)
#   → return sorted(numbers, key=round)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only floating_point is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → numbers = ...  # stored in memory
#   → print(floating_point(...))  # floating_point() runs first → value goes to print()
#   → numbers = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(floating_point(...))  # floating_point() runs first → value goes to print()
"""
Problème 467 :
Write un Python fonction à trier une liste de floating-point nombres by leur rounded valeur en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return x[0]
#   → return x[0]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only first_element_decending_order is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(first_element_decending_order(...))  # first_element_decending_order() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(first_element_decending_order(...))  # first_element_decending_order() runs first → value goes to print()
"""
Problème 468 :
Write un Python fonction à trier une liste de tuples based on le premier élément dans l'ordre décroissant en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: in
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return count
#   → return count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only number_of_consonants is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(number_of_consonants(...))  # number_of_consonants() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(number_of_consonants(...))  # number_of_consonants() runs first → value goes to print()
#
# Loop: takes one item from word.lower(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 469 :
Write un Python fonction qui trie une liste de mots by le nombre de consonnes en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : min()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return min(lst, key=len)
#   → return min(lst, key=len)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only min_string is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(min_string(...))  # min_string() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(min_string(...))  # min_string() runs first → value goes to print()
"""
Problème 470 :
Write un Python fonction à trouver le plus court chaîne dans une liste en utilisant le min() fonction avec la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : len, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return len(x.get(key, ''))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only length_of_value is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → sorted_lst = ...  # stored in memory
#   → print(sorted_lst)
#   → lst = ...  # stored in memory
#   → key = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(length_of_value(...))  # length_of_value() runs first → value goes to print()
"""
Problème 471 :
Write un Python fonction à trier une liste de dictionnaires by la longueur de le valeur associated avec un spécifique clé en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : len, max()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return len(d.get(key, ''))
#   → return len(d.get(key, ''))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only find_person is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst_dict = ...  # stored in memory
#   → key = ...  # stored in memory
#   → print(find_person(...))  # find_person() runs first → value goes to print()
#   → lst_dict = ...  # stored in memory
#   → key = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(find_person(...))  # find_person() runs first → value goes to print()
"""
Problème 472 :
Write un Python fonction à trouver le personne avec le plus long nom dans une liste de dictionnaires contenant ‘nom’ as une clé en utilisant le max() fonction avec la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: % * - //
# Fonctions intégrées : divmod, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return divmod(num, divisor)[1]
#   → def key_func(x):
#   →     return remainder_key(x, divisor)
#   → return sorted(lst, key=key_func)
#   → return divmod(num, divisor)[1]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — main, remainder_key, sort_by_remainder are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → divisor = ...  # stored in memory
#   → main(lst, divisor)  # jumps into main(), runs body, returns
#   → lst = ...  # stored in memory
#   → divisor = ...  # stored in memory
#   → print(sort_by_remainder(...))  # sort_by_remainder() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → divisor = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(main(...))  # main() runs first → value goes to print()
"""
Problème 473 :
Write un Python fonction qui trie une liste d'entiers by leur reste lorsque divided by une donnée nombre en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return sorted(dates, key=year_key)
#   → return datetime.strptime(date, '%Y-%m-%d').year
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — sort_by_year, year_key are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → print(sort_by_year(...))  # sort_by_year() runs first → value goes to print()
#   → date = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(year_key(...))  # year_key() runs first → value goes to print()
"""
Problème 474 :
Write un Python fonction à trier une liste de dates by le year en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return name.lower().count('a')
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_by_a_count is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → names = ...  # stored in memory
#   → sorted_names = ...  # stored in memory
#   → print(sorted_names)
#   → names = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_by_a_count(...))  # sort_by_a_count() runs first → value goes to print()
"""
Problème 475 :
Write un Python fonction à trier une liste de noms by le nombre de fois la lettre ‘a’ apparaît dans chaque nom en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: *
# Fonctions intégrées : pow, range, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return pow(x, x)
#   → return pow(x, x)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_sqaure is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(sort_sqaure(...))  # sort_sqaure() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_sqaure(...))  # sort_sqaure() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
"""
Problème 476 :
Write un Python fonction à trier une liste de nombres by leur carré en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: -
# Fonctions intégrées : abs, min()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return abs(x - target)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only closest_to_target is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → target = ...  # stored in memory
#   → closest_value = ...  # stored in memory
#   → print(closest_value)
#   → lst = ...  # stored in memory
#   → target = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(closest_to_target(...))  # closest_to_target() runs first → value goes to print()
"""
Problème 477 :
Write un Python fonction à trouver la liste élément closest à une cible valeur en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : len, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return len(x[0])
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only length_of_first_element is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → sorted_list = ...  # stored in memory
#   → print(sorted_list)
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(length_of_first_element(...))  # length_of_first_element() runs first → value goes to print()
"""
Problème 478 :
Write un Python fonction qui trie une liste de tuples based on la longueur de le premier élément dans chaque tuple en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: ==
# Fonctions intégrées : sorted, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → count = 0
#   → for c in x:
#   →     if c == ' ':
#   →         count += 1
#   → return count
#   → count = 0
#   → for c in x:
#   →     if c == ' ':
#   →         count += 1
#   → return count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only number_of_spaces is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(number_of_spaces(...))  # number_of_spaces() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(number_of_spaces(...))  # number_of_spaces() runs first → value goes to print()
#
# Loop: takes one item from x, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 479 :
Write un Python fonction à trier une liste de chaînes by le nombre de spaces they contien en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: in
# Fonctions intégrées : len, max, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return len([char for char in word if char in vowels])
#   → return len([char for char in word if char in vowels])
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only most_vowels is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(most_vowels(...))  # most_vowels() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(most_vowels(...))  # most_vowels() runs first → value goes to print()
#
# Loop: takes one item from word, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 480 :
Write un Python fonction qui trouve le mot avec la plupart voyelles dans une liste en utilisant le max() fonction avec la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : abs, len, sorted, str()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return len(str(abs(n)))
#   → return len(str(abs(n)))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_lst_integers is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(sort_lst_integers(...))  # sort_lst_integers() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_lst_integers(...))  # sort_lst_integers() runs first → value goes to print()
"""
Problème 481 :
Write un Python fonction à trier une liste d'entiers by le nombre de les chiffres they contien en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: -
# Fonctions intégrées : abs, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return abs(tup[0] - tup[1])
#   → return abs(tup[0] - tup[1])
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_tuples_by_difference is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(sort_tuples_by_difference(...))  # sort_tuples_by_difference() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_tuples_by_difference(...))  # sort_tuples_by_difference() runs first → value goes to print()
"""
Problème 482 :
Write un Python fonction qui trie une liste de tuples by le différence entre leur éléments en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : ord, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return ord(s[0])
#   → return ord(s[0])
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_strings_by_ascii is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(sort_strings_by_ascii(...))  # sort_strings_by_ascii() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_strings_by_ascii(...))  # sort_strings_by_ascii() runs first → value goes to print()
"""
Problème 483 :
Write un Python fonction à trier une liste de chaînes by le ASCII valeur de leur premier caractère en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Fonctions intégrées : reduce, sorted, sum()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → from functools import reduce
#   → import operator
#   → return reduce(operator.add, sublist, 0)
#   → from functools import reduce
#   → import operator
#   → return reduce(operator.add, sublist, 0)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_lists_by_sum is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(sort_lists_by_sum(...))  # sort_lists_by_sum() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_lists_by_sum(...))  # sort_lists_by_sum() runs first → value goes to print()
#
# Loop: takes one item from sublist, runs body, repeats until done
"""
Problème 484 :
Write un Python fonction à trier une liste de listes by le somme de le éléments dans chaque sublist en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: in
# Fonctions intégrées : min()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return count
#   → return count
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only number_of_consonants is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(number_of_consonants(...))  # number_of_consonants() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(number_of_consonants(...))  # number_of_consonants() runs first → value goes to print()
#
# Loop: takes one item from word.lower(...), runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 485 :
Write un Python fonction à trouver le mot avec le fewest consonnes dans une liste en utilisant le min() fonction avec la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return filename.split('.')[-1]
#   → return filename.split('.')[-1]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_files_by_extension is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(sort_files_by_extension(...))  # sort_files_by_extension() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_files_by_extension(...))  # sort_files_by_extension() runs first → value goes to print()
"""
Problème 486 :
Write un Python fonction qui trie une liste de file noms by leur file extension en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for
# Operators: *
# Fonctions intégrées : pow, range, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return pow(n, n)
#   → return pow(n, n)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sqaure_numbers_lst is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(sqaure_numbers_lst(...))  # sqaure_numbers_lst() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sqaure_numbers_lst(...))  # sqaure_numbers_lst() runs first → value goes to print()
#
# Loop: takes one item from range(...), runs body, repeats until done
"""
Problème 487 :
Write un Python fonction à trier une liste de nombres by le carré root de chaque nombre en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : len, set, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return len(set(word))
#   → return len(set(word))
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_words_by_distinct_letters is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → words = ...  # stored in memory
#   → print(sort_words_by_distinct_letters(...))  # sort_words_by_distinct_letters() runs first → value goes to print()
#   → words = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_words_by_distinct_letters(...))  # sort_words_by_distinct_letters() runs first → value goes to print()
"""
Problème 488 :
Write un Python fonction à trier une liste de mots by le nombre de distinct lettre dans chaque mot en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return x[1]
#   → return x[1]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_second_letter is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(sort_second_letter(...))  # sort_second_letter() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_second_letter(...))  # sort_second_letter() runs first → value goes to print()
"""
Problème 489 :
Write un Python fonction qui trie une liste de chaînes by le deuxième lettre dans chaque chaîne en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return person['age']
#   → return person['age']
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only people_age is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → people = ...  # stored in memory
#   → print(people_age(...))  # people_age() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(people_age(...))  # people_age() runs first → value goes to print()
"""
Problème 490 :
Write un Python fonction à trier une liste de people by leur age stored dans un dictionnaire en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : bin, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return bin(x)
#   → return bin(x)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_by_binary_representation is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(sort_by_binary_representation(...))  # sort_by_binary_representation() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_by_binary_representation(...))  # sort_by_binary_representation() runs first → value goes to print()
"""
Problème 491 :
Write un Python fonction qui trie une liste de nombres by leur binary representation en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return dic[key]
#   → return dic[key]
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_keys_by_value is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dic = ...  # stored in memory
#   → print(sort_keys_by_value(...))  # sort_keys_by_value() runs first → value goes to print()
#   → dic = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_keys_by_value(...))  # sort_keys_by_value() runs first → value goes to print()
"""
Problème 492 :
Write un Python fonction à trouver le personne avec le plus court nom dans une liste de dictionnaires en utilisant le min() fonction avec la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : Fraction, float, sorted()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return float(fraction)
#   → return float(fraction)
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — only sort_fractions_by_decimal is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → fractions = ...  # stored in memory
#   → print(sort_fractions_by_decimal(...))  # sort_fractions_by_decimal() runs first → value goes to print()
#   → fractions = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(sort_fractions_by_decimal(...))  # sort_fractions_by_decimal() runs first → value goes to print()
"""
Problème 493 :
Write un Python fonction à trier une liste de fractions by leur decimal valeur en utilisant la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Keywords: for | if/else
# Operators: >
# Fonctions intégrées : len, letter_ends, max()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#   → return len(s) if s.endswith(letter) else -1
#   → return len(s) if s.endswith(letter) else -1
#   → words = string.split()
#   → def letter_ends(word):
#   →     if word.endswith(letter):
#   →         return len(word)
#   →     else:
#   →         return 0
#   → longest = None
#   → max_length = 0
#   → for word in words:
#   →     length = letter_ends(word)
#   →     if length > max_length:
#   →         max_length = length
#   →         longest = word
#   → return longest
#   → return len(s) if s.endswith(letter) else -1
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# def blocks are skipped at runtime — longest_string, longest_string_letter are stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → lst = ...  # stored in memory
#   → print(longest_string_letter(...))  # longest_string_letter() runs first → value goes to print()
#   → print(longest_string_letter(...))  # longest_string_letter() runs first → value goes to print()
#   → input_string = ...  # stored in memory
#   → letter = ...  # stored in memory
#   → print(longest_string(...))  # longest_string() runs first → value goes to print()
#   → lst = ...  # stored in memory
#   → letter = ...  # stored in memory
#   → result = ...  # stored in memory
#   → print(result)
#   → print(longest_string_letter(...))  # longest_string_letter() runs first → value goes to print()
#
# Loop: takes one item from words, runs body, repeats until done
# Branch: condition picks which block runs — the rest are skipped
"""
Problème 494 :
Write un Python fonction à trouver le plus long chaîne qui termine avec un spécifique lettre en utilisant le max() fonction avec la clé paramètre.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# Fonctions intégrées : Animal, Cat, Dog()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes Cat, Animal, Dog are defined — methods stored in memory
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → dog = ...  # stored in memory
#   → cat = ...  # stored in memory
#   → print(dog.speak(...))
#   → print(cat.speak(...))
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Animal(...))
"""
Problème 495 :
créer un base class Animal avec une méthode speak() et un derived class Dog qui overrides le speak() méthode à print “Bark”.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# Fonctions intégrées : Car, Vehicle, super()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes Car, Vehicle are defined — methods stored in memory
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → my_car = ...  # stored in memory
#   → print(?)
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Vehicle(...))
"""
Problème 496 :
créer un base class Vehicle avec attributes speed et color. créer un derived class Car qui ajoute le model attribute.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
#
# Fonctions intégrées : Person, Student, super()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes Student, Person are defined — methods stored in memory
# def blocks are skipped at runtime — only solve is stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → person = ...  # stored in memory
#   → print(person.introduce(...))
#   → student = ...  # stored in memory
#   → print(student.introduce(...))
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Person(...))
"""
Problème 497 :
créer un base class personne avec une méthode introduce(). créer un derived class Student qui overrides le introduce() méthode à inclure le student’s grade.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Operators: *
# Fonctions intégrées : Rectangle, Shape()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes Shape, Rectangle are defined — methods stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → rectangle = ...  # stored in memory
#   → print(?)
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Shape(...))
"""
Problème 498 :
créer un base class Shape avec une méthode area(). créer un derived class Rectangle qui calcule le area.
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : Appliance, WashingMachine, super()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes Appliance, WashingMachine are defined — methods stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → washing_machine = ...  # stored in memory
#   → print(washing_machine.wash_clothes(...))
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Appliance(...))
"""
Problème 499 :
créer un base class Appliance avec attributes brand et power. créer un derived class WashingMachine qui ajoute une méthode wash_clothes().
"""

#
# SYNTAX:
# Syntax describes the Python building blocks used in this code —
# the keywords, operators, and structures that make it work.
#
#
# Fonctions intégrées : Employee, Manager, super()
#
# EVALUATION ORDER:
# Evaluation Order traces how Python reads and evaluates expressions.
# Inner expressions are evaluated first, then the outer ones.
#
# (expressions evaluate left to right, inner calls first)
#
# EXECUTION ORDER:
# Execution Order shows the sequence Python follows when running
# the code. 'def' and 'class' blocks are just stored, not run yet.
#
#
# EXECUTION FLOW:
# Flux d'Exécution tracks where Python jumps during runtime — which
# blocks are skipped and which actually run.
#
# Classes Employee, Manager are defined — methods stored in memory
#
# Execution starts at the top-level code (outside def/class):
#   → manager = ...  # stored in memory
#   → print(manager.assign_task(...))
#   → obj = ...  # stored in memory
#   → print(obj)
#   → print(Employee(...))
"""
Problème 500 :
créer un base class Employee avec attributes nom et salary. créer un derived class Manager qui ajoute une méthode assign_task().
"""

