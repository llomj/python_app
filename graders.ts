export type CompareMode = 'exact' | 'float' | 'printedOrReturn' | 'numberRange' | 'length' | 'unorderedList' | 'unorderedWords' | 'numberList' | 'dictUnorderedLists' | 'letterCounts' | 'vowelConsonantCounts';

export interface AutoTestCase {
    args: unknown[];
    expected: unknown;
    inputValues?: string[];
    functionName?: string;
    label?: string;
}

export interface AutoGrader {
    functionNames: string[];
    compare?: CompareMode;
    tests: AutoTestCase[];
}

export const AUTO_GRADERS: Record<number, AutoGrader> = {
    1: {
        functionNames: ['add_numbers', 'add_number', 'add_num'],
        tests: [
            { args: [2, 3], expected: 5 },
            { args: [-4, 9], expected: 5 },
            { args: [1.5, 2.25], expected: 3.75 }
        ]
    },
    2: {
        functionNames: ['multiply_numbers'],
        tests: [
            { args: [4, 5], expected: 20 },
            { args: [-3, 6], expected: -18 },
            { args: [0, 99], expected: 0 }
        ]
    },
    3: {
        functionNames: ['find_max'],
        tests: [
            { args: [[2, 67, 300]], expected: 300 },
            { args: [[-9, -2, -15]], expected: -2 },
            { args: [[5]], expected: 5 }
        ]
    },
    4: {
        functionNames: ['calculate_average', 'cal_average'],
        compare: 'float',
        tests: [
            { args: [[2, 4, 6]], expected: 4 },
            { args: [[10, 15]], expected: 12.5 },
            { args: [[-3, 3, 6]], expected: 2 }
        ]
    },
    5: {
        functionNames: ['count_vowels'],
        tests: [
            { args: ['Jonathan'], expected: 3 },
            { args: ['AEIOUxyz'], expected: 5 },
            { args: ['rhythm'], expected: 0 }
        ]
    },
    6: {
        functionNames: ['reverse_string'],
        tests: [
            { args: ['Jonathan'], expected: 'nahtanoJ' },
            { args: ['abc def'], expected: 'fed cba' },
            { args: ['x'], expected: 'x' }
        ]
    },
    7: {
        functionNames: ['is_even'],
        tests: [
            { args: [10], expected: true },
            { args: [7], expected: false },
            { args: [0], expected: true }
        ]
    },
    8: {
        functionNames: ['calculate_square', 'calculate_sqaure', 'cal_square'],
        tests: [
            { args: [6], expected: 36 },
            { args: [-4], expected: 16 },
            { args: [0], expected: 0 }
        ]
    },
    9: {
        functionNames: ['greet_user'],
        compare: 'printedOrReturn',
        tests: [
            { args: ['Ada'], expected: 'Hello, Ada!' },
            { args: ['Jonathan'], expected: 'Hello, Jonathan!' }
        ]
    },
    10: {
        functionNames: ['square_list', 'square_lst'],
        tests: [
            { args: [[2, 4, 5, 6]], expected: [4, 16, 25, 36] },
            { args: [[-2, 0, 3]], expected: [4, 0, 9] }
        ]
    },
    11: {
        functionNames: ['convert_to_uppercase', 'covert_uppercase'],
        tests: [
            { args: ['Jonathan'], expected: 'JONATHAN' },
            { args: ['Hi there!'], expected: 'HI THERE!' }
        ]
    },
    12: {
        functionNames: ['calculate_sum', 'cal_sum'],
        tests: [
            { args: [[1, 56, 778]], expected: 835 },
            { args: [[-5, 5, 10]], expected: 10 },
            { args: [[]], expected: 0 }
        ]
    },
    13: {
        functionNames: ['is_odd'],
        tests: [
            { args: [10], expected: false },
            { args: [7], expected: true },
            { args: [0], expected: false }
        ]
    },
    14: {
        functionNames: ['concatenate_strings', 'concatenate_string'],
        tests: [
            { args: ['Jonathan', 'moll'], expected: 'Jonathanmoll' },
            { args: ['hello ', 'world'], expected: 'hello world' }
        ]
    },
    15: {
        functionNames: ['find_length', 'find_len'],
        tests: [
            { args: ['Jonathan'], expected: 8 },
            { args: [''], expected: 0 },
            { args: ['hi there'], expected: 8 }
        ]
    },
    16: {
        functionNames: ['is_palindrome'],
        tests: [
            { args: ['racecar'], expected: true },
            { args: ['A man a plan a canal Panama'], expected: true },
            { args: ['tom'], expected: false }
        ]
    },
    17: {
        functionNames: ['count_words'],
        tests: [
            { args: ['This is an example sentence.'], expected: 5 },
            { args: ['hello'], expected: 1 },
            { args: ['  extra   spaces here  '], expected: 3 }
        ]
    },
    18: {
        functionNames: ['find_min', 'find_minimum'],
        tests: [
            { args: [[45, 6, 1]], expected: 1 },
            { args: [[-3, -9, 2]], expected: -9 },
            { args: [[5]], expected: 5 }
        ]
    },
    19: {
        functionNames: ['is_even_index_sum'],
        tests: [
            { args: [[100, 200, 300, 400]], expected: true },
            { args: [[1, 10, 2]], expected: false },
            { args: [[2, 1, 4]], expected: true }
        ]
    },
    20: {
        functionNames: ['double_elements'],
        tests: [
            { args: [[1, 2, 3]], expected: [2, 4, 6] },
            { args: [[-1, 0, 5]], expected: [-2, 0, 10] }
        ]
    },
    21: {
        functionNames: ['is_all_positive'],
        tests: [
            { args: [[1, 6, 8]], expected: true },
            { args: [[0, 6, 8]], expected: false },
            { args: [[-1, 2]], expected: false }
        ]
    },
    22: {
        functionNames: ['find_average', 'find_average_lst'],
        compare: 'float',
        tests: [
            { args: [[4, 67, 77]], expected: 49.333333333333336 },
            { args: [[1, 56, 66]], expected: 41 },
            { args: [[-2, 2, 6]], expected: 2 }
        ]
    },
    23: {
        functionNames: ['contains_negative'],
        tests: [
            { args: [[5, -9]], expected: true },
            { args: [[0, 5, 9]], expected: false },
            { args: [[1, 2, 3]], expected: false }
        ]
    },
    24: {
        functionNames: ['find_last_element', 'find_element'],
        tests: [
            { args: [[1, 45, 66]], expected: 66 },
            { args: [['a', 'b', 'c']], expected: 'c' },
            { args: [[5]], expected: 5 }
        ]
    },
    25: {
        functionNames: ['multiply_elements'],
        tests: [
            { args: [[2, 4, 2]], expected: 16 },
            { args: [[1, 5, -3]], expected: -15 },
            { args: [[7]], expected: 7 }
        ]
    },
    26: {
        functionNames: ['has_duplicates'],
        tests: [
            { args: [[1, 2, 3, 2]], expected: true },
            { args: [['it', 'was', 'itt']], expected: false },
            { args: [[5, 5]], expected: true }
        ]
    },
    27: {
        functionNames: ['count_occurrences'],
        tests: [
            { args: [[1, 2, 2, 3, 2], 2], expected: 3 },
            { args: [['tree', 'house', 'tree'], 'tree'], expected: 2 },
            { args: [[1, 2, 3], 9], expected: 0 }
        ]
    },
    28: {
        functionNames: ['remove_vowels'],
        tests: [
            { args: ['Jonathan'], expected: 'Jnthn' },
            { args: ['AEIOUxyz'], expected: 'xyz' },
            { args: ['rhythm'], expected: 'rhythm' }
        ]
    },
    29: {
        functionNames: ['capitalize_words'],
        tests: [
            { args: ['hello world! this is a test.'], expected: 'Hello World! This Is A Test.' },
            { args: ['jonathan moll'], expected: 'Jonathan Moll' },
            { args: ['a b c'], expected: 'A B C' }
        ]
    },
    30: {
        functionNames: ['remove_spaces', 'remove_space'],
        tests: [
            { args: ['suck me duck Jonathan'], expected: 'suckmeduckJonathan' },
            { args: ['what just happened'], expected: 'whatjusthappened' },
            { args: [' no spaces '], expected: 'nospaces' }
        ]
    },
    31: {
        functionNames: ['get_initials'],
        tests: [
            { args: ['John Doe'], expected: 'J.D.' },
            { args: ['jonathan moll'], expected: 'J.M.' },
            { args: ['Ada Lovelace'], expected: 'A.L.' }
        ]
    },
    32: {
        functionNames: ['reverse_words', 'reverse_word'],
        tests: [
            { args: ['hello world'], expected: 'world hello' },
            { args: ['one two three'], expected: 'three two one' },
            { args: ['single'], expected: 'single' }
        ]
    },
    33: {
        functionNames: ['remove_duplicates'],
        tests: [
            { args: [[1, 2, 3, 1, 4, 2, 5]], expected: [1, 2, 3, 4, 5] },
            { args: [['a', 'b', 'a', 'c']], expected: ['a', 'b', 'c'] },
            { args: [[]], expected: [] }
        ]
    },
    34: {
        functionNames: ['find_longest_word'],
        tests: [
            { args: ['why dont you call Jonathan'], expected: 'Jonathan' },
            { args: ['tree cliff mountain grassy'], expected: 'mountain' },
            { args: ['same size test'], expected: 'same' }
        ]
    },
    35: {
        functionNames: ['find_vowels'],
        tests: [
            { args: ['Jonathan'], expected: ['o', 'a', 'a'] },
            { args: ['AEIOUxyz'], expected: ['A', 'E', 'I', 'O', 'U'] },
            { args: ['rhythm'], expected: [] }
        ]
    },
    36: {
        functionNames: ['reverse_number'],
        tests: [
            { args: [123], expected: 321 },
            { args: [900], expected: 9 },
            { args: [5], expected: 5 }
        ]
    },
    37: {
        functionNames: ['remove_duplicates', 'remove_duplicate'],
        tests: [
            { args: ['Jonathan'], expected: 'Jonath' },
            { args: ['banana'], expected: 'ban' },
            { args: ['abc'], expected: 'abc' }
        ]
    },
    38: {
        functionNames: ['sum_of_list'],
        tests: [
            { args: [[1, 2, 3]], expected: 6 },
            { args: [[-5, 5, 10]], expected: 10 },
            { args: [[]], expected: 0 }
        ]
    },
    39: {
        functionNames: ['sum_of_list'],
        tests: [
            { args: [[2, 2, 2]], expected: 6 },
            { args: [[-1, 1, 9]], expected: 9 },
            { args: [[]], expected: 0 }
        ]
    },
    40: {
        functionNames: ['find_min_max'],
        tests: [
            { args: [[10, 90, 45, 55, 222, 2]], expected: [2, 222] },
            { args: [[-5, -1, -9]], expected: [-9, -1] },
            { args: [[7]], expected: [7, 7] }
        ]
    },
    41: {
        functionNames: ['count_occurrences'],
        tests: [
            { args: [['Tom', 'Jerry', 'Tom'], 'Tom'], expected: 2 },
            { args: [[1, 2, 2, 2], 2], expected: 3 },
            { args: [['a', 'b'], 'z'], expected: 0 }
        ]
    },
    42: {
        functionNames: ['table'],
        compare: 'printedOrReturn',
        tests: [
            { args: [3], expected: '3 * 0 = 0\n3 * 1 = 3\n3 * 2 = 6\n3 * 3 = 9\n3 * 4 = 12\n3 * 5 = 15\n3 * 6 = 18\n3 * 7 = 21\n3 * 8 = 24\n3 * 9 = 27\n3 * 10 = 30' }
        ]
    },
    43: {
        functionNames: ['square_elements'],
        tests: [
            { args: [[2, 3, 4]], expected: [4, 9, 16] },
            { args: [[-2, 0, 5]], expected: [4, 0, 25] }
        ]
    },
    44: {
        functionNames: ['count_uppercase'],
        tests: [
            { args: ['Jonathan Moll'], expected: 2 },
            { args: ['ABC xyz!'], expected: 3 },
            { args: ['no uppercase'], expected: 0 }
        ]
    },
    45: {
        functionNames: ['remove_spaces'],
        tests: [
            { args: ['what happening boss man'], expected: 'whathappeningbossman' },
            { args: [' a b c '], expected: 'abc' },
            { args: ['none'], expected: 'none' }
        ]
    },
    46: {
        functionNames: ['merge_lists'],
        tests: [
            { args: [[1, 3, 5], [2, 4, 6]], expected: [1, 2, 3, 4, 5, 6] },
            { args: [[-3, 7], [-5, 0, 10]], expected: [-5, -3, 0, 7, 10] },
            { args: [[], [1, 2]], expected: [1, 2] }
        ]
    },
    47: {
        functionNames: ['find_index'],
        tests: [
            { args: [[10, 20, 30], 20], expected: 1 },
            { args: [[10, 20, 30], 99], expected: -1 },
            { args: [['a', 'b', 'a'], 'a'], expected: 0 }
        ]
    },
    48: {
        functionNames: ['sum_even_indices'],
        tests: [
            { args: [[10, 20, 30, 40]], expected: 40 },
            { args: [[1, 2, 3, 4, 5]], expected: 9 },
            { args: [[]], expected: 0 }
        ]
    },
    49: {
        functionNames: ['remove_duplicates_case_insensitive', 'remove_duplicates'],
        tests: [
            { args: [['Hello', 'HELLO', 'world', 'World', 'Python', 'python']], expected: ['Hello', 'world', 'Python'] },
            { args: [['not', 'not', 'hot', 'HOT', 'cold']], expected: ['not', 'hot', 'cold'] },
            { args: [[]], expected: [] }
        ]
    },
    50: {
        functionNames: ['is_palindrome'],
        tests: [
            { args: ['racecar'], expected: true },
            { args: ['hello'], expected: false },
            { args: [''], expected: true }
        ]
    },
    51: {
        functionNames: ['factorial'],
        tests: [
            { args: [0], expected: 1 },
            { args: [5], expected: 120 },
            { args: [7], expected: 5040 }
        ]
    },
    52: {
        functionNames: ['is_anagram'],
        tests: [
            { args: ['listen', 'silent'], expected: true },
            { args: ['Triangle', 'Integral'], expected: true },
            { args: ['hello', 'world'], expected: false }
        ]
    },
    53: {
        functionNames: ['count_words'],
        tests: [
            { args: ['This is this'], expected: { this: 2, is: 1 } },
            { args: ['one two one'], expected: { one: 2, two: 1 } },
            { args: ['Hello hello'], expected: { hello: 2 } }
        ]
    },
    54: {
        functionNames: ['fibonacci'],
        tests: [
            { args: [0], expected: [] },
            { args: [1], expected: [0] },
            { args: [7], expected: [0, 1, 1, 2, 3, 5, 8] }
        ]
    },
    55: {
        functionNames: ['area_rectangle'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], inputValues: ['5', '3'], expected: '15.0' },
            { args: [], inputValues: ['4', '2'], expected: '8.0' }
        ]
    },
    56: {
        functionNames: ['even_odd'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], inputValues: ['4'], expected: 'Number is even' },
            { args: [], inputValues: ['7'], expected: 'Number is odd' }
        ]
    },
    57: {
        functionNames: ['fibonacci_series'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], inputValues: ['10'], expected: '0 1 1 2 3 5 8' },
            { args: [], inputValues: ['1'], expected: '0 1' }
        ]
    },
    58: {
        functionNames: ['max_number'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], inputValues: ['10 20 15'], expected: '20' },
            { args: [], inputValues: ['-2 -9 -1'], expected: '-1' }
        ]
    },
    59: {
        functionNames: ['reverse_string'],
        compare: 'printedOrReturn',
        tests: [
            { args: ['Jonathan'], expected: 'nahtanoJ' },
            { args: ['hello'], expected: 'olleh' }
        ]
    },
    60: {
        functionNames: ['is_palindrome'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], inputValues: ['racecar'], expected: true },
            { args: [], inputValues: ['hello'], expected: false }
        ]
    },
    61: {
        functionNames: ['count_vowels'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], inputValues: ['Hello'], expected: '2' },
            { args: [], inputValues: ['rhythm'], expected: '0' }
        ]
    },
    62: {
        functionNames: ['factorial'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], inputValues: ['5'], expected: '120' },
            { args: [], inputValues: ['0'], expected: '1' }
        ]
    },
    63: {
        functionNames: ['sum_of_all_numbers'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], inputValues: ['5'], expected: '15' },
            { args: [], inputValues: ['3'], expected: '6' }
        ]
    },
    64: {
        functionNames: ['largest_element', 'find_largest'],
        tests: [
            { args: [[2, 56, 75, 4566, 3]], expected: 4566 },
            { args: [[-5, -2, -9]], expected: -2 },
            { args: [[7]], expected: 7 }
        ]
    },
    65: {
        functionNames: ['largest_elememt', 'main'],
        tests: [
            { args: [['tree', 'cliff', 'mountain', 'grassy']], expected: 'mountain' },
            { args: [['house', 'counter', 'if']], expected: 'counter' },
            { args: [['same', 'size']], expected: 'same' }
        ]
    },
    66: {
        functionNames: ['remove_duplicates'],
        tests: [
            { args: [['tree', 'kiss', 'tree']], expected: ['tree', 'kiss'] },
            { args: [[1, 2, 1, 3]], expected: [1, 2, 3] },
            { args: [[]], expected: [] }
        ]
    },
    67: {
        functionNames: ['is_leap_year'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], inputValues: ['2000'], expected: true },
            { args: [], inputValues: ['1900'], expected: false },
            { args: [], inputValues: ['2024'], expected: true }
        ]
    },
    68: {
        functionNames: ['length_string'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], inputValues: ['hello'], expected: '5' },
            { args: [], inputValues: ['hello world'], expected: '11' }
        ]
    },
    70: {
        functionNames: ['count_each_word'],
        tests: [
            { args: ['this is this'], expected: { this: 2, is: 1 } },
            { args: ['one two one'], expected: { one: 2, two: 1 } }
        ]
    },
    71: {
        functionNames: ['second_largest_number', 'sec_lar'],
        tests: [
            { args: [[10, 90, 45, 55, 222, 2]], expected: 90 },
            { args: [[5, 5, 4, 3]], expected: 4 },
            { args: [[-5, -1, -9]], expected: -5 }
        ]
    },
    72: {
        functionNames: ['is_valid_email'],
        tests: [
            { args: ['test@example.com'], expected: true },
            { args: ['bad-email'], expected: false },
            { args: ['name@site'], expected: false }
        ]
    },
    73: {
        functionNames: ['factorial'],
        tests: [
            { args: [0], expected: 1 },
            { args: [5], expected: 120 },
            { args: [6], expected: 720 }
        ]
    },
    74: {
        functionNames: ['are_anagrams', 'pal'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], inputValues: ['listen', 'silent'], expected: true },
            { args: [], inputValues: ['hello', 'world'], expected: false }
        ]
    },
    75: {
        functionNames: ['is_prime'],
        tests: [
            { args: [2], expected: true },
            { args: [17], expected: true },
            { args: [1], expected: false },
            { args: [9], expected: false }
        ]
    },
    76: {
        functionNames: ['common_elements', 'find_common_elements'],
        compare: 'unorderedList',
        tests: [
            { args: [[1, 2, 3], [2, 3, 4]], expected: [2, 3] },
            { args: [['a', 'b'], ['c', 'a']], expected: ['a'] },
            { args: [[1, 2], [3, 4]], expected: [] }
        ]
    },
    77: {
        functionNames: ['uppercase', 'count_uppercase'],
        tests: [
            { args: ['Jonathan Moll'], expected: 2 },
            { args: ['ABC xyz!'], expected: 3 },
            { args: ['no uppercase'], expected: 0 }
        ]
    },
    78: {
        functionNames: ['decimal_to_binary'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], inputValues: ['10'], expected: '1010' },
            { args: [], inputValues: ['5'], expected: '101' }
        ]
    },
    79: {
        functionNames: ['ascending_order_numbers'],
        tests: [
            { args: [[3, 1, 2]], expected: [1, 2, 3] },
            { args: [[-1, 5, 0]], expected: [-1, 0, 5] },
            { args: [[]], expected: [] }
        ]
    },
    80: {
        functionNames: ['generate_random_number'],
        compare: 'numberRange',
        tests: [
            { args: [], inputValues: ['1', '10'], expected: [1, 10] },
            { args: [], inputValues: ['20', '25'], expected: [20, 25] }
        ]
    },
    81: {
        functionNames: ['square_root'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], inputValues: ['9'], expected: '3' },
            { args: [], inputValues: ['16'], expected: '4' }
        ]
    },
    82: {
        functionNames: ['calculate_circle_area', 'circle'],
        compare: 'float',
        tests: [
            { args: [1], expected: 3.141592653589793 },
            { args: [2], expected: 12.566370614359172 }
        ]
    },
    83: {
        functionNames: ['is_palindrome'],
        tests: [
            { args: ['racecar'], expected: true },
            { args: ['hello'], expected: false },
            { args: [''], expected: true }
        ]
    },
    84: {
        functionNames: ['is_pangram', 'pangram'],
        tests: [
            { args: ['The quick brown fox jumps over the lazy dog'], expected: true },
            { args: ['hello world'], expected: false },
            { args: ['abcdefghijklmnopqrstuvwxyz'], expected: true }
        ]
    },
    85: {
        functionNames: ['gcd'],
        tests: [
            { args: [12, 18], expected: 6 },
            { args: [17, 13], expected: 1 },
            { args: [20, 5], expected: 5 }
        ]
    },
    86: {
        functionNames: ['lcm'],
        tests: [
            { args: [4, 6], expected: 12 },
            { args: [5, 7], expected: 35 },
            { args: [3, 9], expected: 9 }
        ]
    },
    87: {
        functionNames: ['reverse_list', 'reverse_lst'],
        tests: [
            { args: [[1, 2, 3]], expected: [3, 2, 1] },
            { args: [['a', 'b']], expected: ['b', 'a'] },
            { args: [[]], expected: [] }
        ]
    },
    88: {
        functionNames: ['prime_factors'],
        tests: [
            { args: [12], expected: [2, 2, 3] },
            { args: [13], expected: [13] },
            { args: [60], expected: [2, 2, 3, 5] }
        ]
    },
    89: {
        functionNames: ['generate_password'],
        compare: 'length',
        tests: [
            { args: [8], expected: 8 },
            { args: [12], expected: 12 }
        ]
    },
    90: {
        functionNames: ['count_words'],
        tests: [
            { args: ['hello world'], expected: 2 },
            { args: ['  extra   spaces here  '], expected: 3 },
            { args: ['one'], expected: 1 }
        ]
    },
    91: {
        functionNames: ['largest_smallest'],
        tests: [
            { args: [[4, 5, 100, 6, 1, 10]], expected: [1, 100] },
            { args: [[-5, -1, -9]], expected: [-9, -1] },
            { args: [[7]], expected: [7, 7] }
        ]
    },
    92: {
        functionNames: ['is_perfect_number', 'is_perfect_square'],
        tests: [
            { args: [6], expected: true },
            { args: [28], expected: true },
            { args: [12], expected: false }
        ]
    },
    93: {
        functionNames: ['factorial'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], inputValues: ['5'], expected: '120' },
            { args: [], inputValues: ['0'], expected: '1' }
        ]
    },
    94: {
        functionNames: ['is_power_of_two'],
        tests: [
            { args: [1], expected: true },
            { args: [16], expected: true },
            { args: [18], expected: false },
            { args: [0], expected: false }
        ]
    },
    95: {
        functionNames: ['find_intersection'],
        compare: 'unorderedList',
        tests: [
            { args: [[1, 2, 3], [2, 3, 4]], expected: [2, 3] },
            { args: [['a', 'b'], ['c', 'a']], expected: ['a'] },
            { args: [[1], [2]], expected: [] }
        ]
    },
    96: {
        functionNames: ['remove_vowels'],
        tests: [
            { args: ['Jonathan'], expected: 'Jnthn' },
            { args: ['AEIOUxyz'], expected: 'xyz' },
            { args: ['rhythm'], expected: 'rhythm' }
        ]
    },
    97: {
        functionNames: ['binary_to_decimal'],
        tests: [
            { args: ['1010'], expected: 10 },
            { args: ['111'], expected: 7 },
            { args: ['0'], expected: 0 }
        ]
    },
    98: {
        functionNames: ['digits_string'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], inputValues: ['2 8'], expected: '10' },
            { args: [], inputValues: ['1 2 3'], expected: '6' }
        ]
    },
    99: {
        functionNames: ['upper_lower'],
        compare: 'letterCounts',
        tests: [
            { args: ['Jonathan Moll'], expected: { upper: 2, lower: 10 } },
            { args: ['ABC xyz'], expected: { upper: 3, lower: 3 } },
            { args: ['no uppercase'], expected: { upper: 0, lower: 11 } }
        ]
    },
    100: {
        functionNames: ['sum_of_primes'],
        tests: [
            { args: [1, 10], expected: 17 },
            { args: [10, 20], expected: 60 },
            { args: [1, 2], expected: 2 }
        ]
    },
    101: {
        functionNames: ['power'],
        tests: [
            { args: [2, 3], expected: 8 },
            { args: [5, 0], expected: 1 },
            { args: [3, 4], expected: 81 }
        ]
    },
    102: {
        functionNames: ['is_anagram'],
        tests: [
            { args: ['listen', 'silent'], expected: true },
            { args: ['dormitory', 'dirty room'], expected: true },
            { args: ['hello', 'world'], expected: false }
        ]
    },
    104: {
        functionNames: ['is_perfect_square'],
        tests: [
            { args: [16], expected: true },
            { args: [14], expected: false },
            { args: [0], expected: true }
        ]
    },
    105: {
        functionNames: ['all_odd_numbers'],
        tests: [
            { args: [[1, 2, 3, 4, 5]], expected: 9 },
            { args: [[2, 4, 6]], expected: 0 },
            { args: [[-3, 5, 6]], expected: 2 }
        ]
    },
    106: {
        functionNames: ['sum_of_odd_numbers', 'sum_of_all_odd'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], inputValues: ['1 2 3 4 5'], expected: '9' },
            { args: [], inputValues: ['2 4 6'], expected: '0' },
            { args: [], inputValues: ['-3 5 6'], expected: '2' }
        ]
    },
    107: {
        functionNames: ['common_char'],
        compare: 'unorderedList',
        tests: [
            { args: ['abc', 'bcd'], expected: ['b', 'c'] },
            { args: ['hello', 'world'], expected: ['l', 'o'] },
            { args: ['abc', 'xyz'], expected: [] }
        ]
    },
    108: {
        functionNames: ['remove_duplicates'],
        compare: 'unorderedList',
        tests: [
            { args: [], inputValues: ['banana'], expected: ['b', 'a', 'n'] },
            { args: [], inputValues: ['abc'], expected: ['a', 'b', 'c'] }
        ]
    },
    109: {
        functionNames: ['is_armstrong'],
        tests: [
            { args: [153], expected: true },
            { args: [9474], expected: true },
            { args: [123], expected: false }
        ]
    },
    110: {
        functionNames: ['vowels_consonates'],
        compare: 'vowelConsonantCounts',
        tests: [
            { args: ['Hello World'], expected: { vowels: 3, consonants: 7 } },
            { args: ['AEIOU xyz'], expected: { vowels: 5, consonants: 3 } },
            { args: ['rhythm'], expected: { vowels: 0, consonants: 6 } }
        ]
    },
    111: {
        functionNames: ['second_smallest_element'],
        tests: [
            { args: [[4, 1, 3, 2]], expected: 2 },
            { args: [[5, 5, 4, 3]], expected: 4 },
            { args: [[-1, -5, 0]], expected: -1 }
        ]
    },
    112: {
        functionNames: ['generate_permutations'],
        compare: 'unorderedList',
        tests: [
            { args: ['ab'], expected: ['ab', 'ba'] },
            { args: ['abc'], expected: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'] }
        ]
    },
    114: {
        functionNames: ['max_of_three', 'main'],
        tests: [
            { args: [1, 5, 3], expected: 5 },
            { args: [-10, -2, -5], expected: -2 },
            { args: [7, 7, 1], expected: 7 }
        ]
    },
    115: {
        functionNames: ['length_string', 'length_list'],
        tests: [
            { args: ['hello'], expected: 5 },
            { args: [[1, 2, 3]], expected: 3 },
            { args: [''], expected: 0 }
        ]
    },
    117: {
        functionNames: ['translate'],
        tests: [
            { args: ['this is fun'], expected: 'tothohisos isos fofunon' },
            { args: ['abc'], expected: 'abobcoc' },
            { args: ['aeiou'], expected: 'aeiou' }
        ]
    },
    118: {
        functionNames: ['sum', 'multiply'],
        tests: [
            { functionName: 'sum', args: [[1, 2, 3, 4]], expected: 10 },
            { functionName: 'sum', args: [[-2, 5, 0]], expected: 3 },
            { functionName: 'multiply', args: [[1, 2, 3, 4]], expected: 24 },
            { functionName: 'multiply', args: [[-2, 5, 3]], expected: -30 }
        ]
    },
    119: {
        functionNames: ['reverse'],
        tests: [
            { args: ['I am testing'], expected: 'gnitset ma I' },
            { args: ['abc'], expected: 'cba' },
            { args: [''], expected: '' }
        ]
    },
    120: {
        functionNames: ['palindromes'],
        tests: [
            { args: ['radar'], expected: true },
            { args: ['hello'], expected: false },
            { args: ['level'], expected: true }
        ]
    },
    121: {
        functionNames: ['is_palindrome'],
        tests: [
            { args: ['radar'], expected: true },
            { args: ['hello'], expected: false },
            { args: ['level'], expected: true }
        ]
    },
    122: {
        functionNames: ['is_member'],
        tests: [
            { args: ['a', ['b', 'a']], expected: true },
            { args: [3, [1, 2]], expected: false },
            { args: ['x', []], expected: false }
        ]
    },
    123: {
        functionNames: ['overlapping'],
        tests: [
            { args: [[1, 2, 3], [4, 3, 5]], expected: true },
            { args: [['a', 'b'], ['c', 'd']], expected: false },
            { args: [[], [1]], expected: false }
        ]
    },
    124: {
        functionNames: ['overlapping'],
        tests: [
            { args: [[1, 2, 3], [4, 3, 5]], expected: true },
            { args: [['a', 'b'], ['c', 'd']], expected: false },
            { args: [[], [1]], expected: false }
        ]
    },
    125: {
        functionNames: ['histogram', 'histrogram'],
        compare: 'printedOrReturn',
        tests: [
            { args: [[4, 2, 1]], expected: '****\n**\n*' },
            { args: [[1, 3]], expected: '*\n***' }
        ]
    },
    126: {
        functionNames: ['map_words_to_lengths'],
        tests: [
            { args: [['apple', 'banana', 'kiwi']], expected: [5, 6, 4] },
            { args: [['a', '', 'three']], expected: [1, 0, 5] }
        ]
    },
    127: {
        functionNames: ['find_longest_word'],
        tests: [
            { args: [['jo', 'banana', 'cat']], expected: 6 },
            { args: [['a', 'abcd', 'xy']], expected: 4 },
            { args: [['same', 'size']], expected: 4 }
        ]
    },
    128: {
        functionNames: ['filter_long_words'],
        tests: [
            { args: [['one', 'three', 'seventeen', 'two'], 3], expected: ['three', 'seventeen'] },
            { args: [['a', 'ab', 'abc'], 2], expected: ['abc'] },
            { args: [['hi'], 5], expected: [] }
        ]
    },
    129: {
        functionNames: ['is_pangram'],
        tests: [
            { args: ['The quick brown fox jumps over the lazy dog'], expected: true },
            { args: ['hello world'], expected: false },
            { args: ['Sphinx of black quartz, judge my vow'], expected: true }
        ]
    },
    130: {
        functionNames: ['correct'],
        tests: [
            { args: ['This  is very funny  and cool.Indeed!'], expected: 'This is very funny and cool. Indeed!' },
            { args: ['Hello.World'], expected: 'Hello. World' },
            { args: ['Already ok. Fine'], expected: 'Already ok. Fine' }
        ]
    },
    131: {
        functionNames: ['max_func', 'max_in_list'],
        tests: [
            { functionName: 'max_func', args: [3, 5], expected: 5 },
            { functionName: 'max_func', args: [-2, -9], expected: -2 },
            { functionName: 'max_in_list', args: [[1, 5, 3, 9, 2]], expected: 9 },
            { functionName: 'max_in_list', args: [[-10, -2, -7]], expected: -2 }
        ]
    },
    134: {
        functionNames: ['sum_of_all_numbers'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], inputValues: ['1 2 3 4'], expected: '10' },
            { args: [], inputValues: ['-2 5 0'], expected: '3' }
        ]
    },
    135: {
        functionNames: ['split_number'],
        tests: [
            { args: ['123'], expected: ['1', '2', '3'] },
            { args: ['908'], expected: ['9', '0', '8'] }
        ]
    },
    136: {
        functionNames: ['alphabetically_ordered'],
        tests: [
            { args: ['hello caca face'], expected: 'caca face hello' },
            { args: ['banana apple cherry'], expected: 'apple banana cherry' }
        ]
    },
    137: {
        functionNames: ['smallest_largest'],
        tests: [
            { args: [[2, 76, 466, 3, 23]], expected: [2, 3, 23, 76, 466] },
            { args: [[5, -1, 0]], expected: [-1, 0, 5] }
        ]
    },
    138: {
        functionNames: ['largest_smallest'],
        tests: [
            { args: [[2, 76, 466, 3, 23]], expected: [466, 76, 23, 3, 2] },
            { args: [[5, -1, 0]], expected: [5, 0, -1] }
        ]
    },
    139: {
        functionNames: ['seconded_largest_number'],
        tests: [
            { args: [[2, 76, 466, 3, 23]], expected: 76 },
            { args: [[5, -1, 0]], expected: 0 },
            { args: [[7, 7, 3]], expected: 7 }
        ]
    },
    140: {
        functionNames: ['fourth_largest_number'],
        tests: [
            { args: [[2, 76, 466, 3, 23]], expected: 3 },
            { args: [[10, 9, 8, 7, 6]], expected: 7 }
        ]
    },
    141: {
        functionNames: ['smallest_and_third'],
        tests: [
            { args: [[2, 76, 466, 3, 23]], expected: [2, 23] },
            { args: [[10, 9, 8, 7, 6]], expected: [6, 8] }
        ]
    },
    142: {
        functionNames: ['largest_smallest', 'smallest_biggest'],
        tests: [
            { args: [[2, 76, 466, 3, 23]], expected: [2, 3, 23, 76, 466] },
            { args: [[5, -1, 0]], expected: [-1, 0, 5] }
        ]
    },
    143: {
        functionNames: ['int_str'],
        tests: [
            { args: [], inputValues: ['1 2 3'], expected: ['1', '2', '3'] },
            { args: [], inputValues: ['10 20'], expected: ['10', '20'] }
        ]
    },
    144: {
        functionNames: ['int_to_str_list'],
        tests: [
            { args: [123], expected: ['1', '2', '3'] },
            { args: [908], expected: ['9', '0', '8'] }
        ]
    },
    145: {
        functionNames: ['common_numbers'],
        compare: 'unorderedList',
        tests: [
            { args: [[2, 24, 23, 27, 2], [56, 2, 27, 455, 1]], expected: [2, 27] },
            { args: [[1, 2], [3, 4]], expected: [] },
            { args: [[5, 5, 6], [5, 7]], expected: [5] }
        ]
    },
    146: {
        functionNames: ['big_small'],
        tests: [
            { args: [['4', '10', '2']], expected: ['10', '4', '2'] },
            { args: [['1', '9', '3']], expected: ['9', '3', '1'] }
        ]
    },
    147: {
        functionNames: ['type_smallest_biggest', 'small_big'],
        compare: 'numberList',
        tests: [
            { args: [], inputValues: ['10 2 1'], expected: [1, 2, 10] },
            { args: [], inputValues: ['5 -1 0'], expected: [-1, 0, 5] }
        ]
    },
    148: {
        functionNames: ['double_elements'],
        tests: [
            { args: [[1, 2, 3]], expected: [1, 2, 3, 1, 2, 3] },
            { args: [['a', 'b']], expected: ['a', 'b', 'a', 'b'] }
        ]
    },
    149: {
        functionNames: ['common'],
        compare: 'unorderedList',
        tests: [
            { args: [], inputValues: ['1 2 3', '3 4 2'], expected: ['2', '3'] },
            { args: [], inputValues: ['a b', 'c d'], expected: [] }
        ]
    },
    150: {
        functionNames: ['common'],
        compare: 'unorderedList',
        tests: [
            { args: [], inputValues: ['1 2 3', '3 4 2'], expected: ['2', '3'] },
            { args: [], inputValues: ['a b', 'c d'], expected: [] }
        ]
    },
    151: {
        functionNames: ['find_longest_word'],
        tests: [
            { args: [['tree', 'mountain', 'sky']], expected: 'mountain' },
            { args: [['same', 'size', 'tiny']], expected: 'same' },
            { args: [['a']], expected: 'a' }
        ]
    },
    152: {
        functionNames: ['average', 'calculate_average'],
        compare: 'float',
        tests: [
            { args: [[4, 667, 68, 766]], expected: 376.25 },
            { args: [[2, 4, 6]], expected: 4 },
            { args: [[-2, 2, 6]], expected: 2 }
        ]
    },
    153: {
        functionNames: ['second_smallest_element'],
        tests: [
            { args: [[4, 1, 3, 2]], expected: 2 },
            { args: [[5, 5, 4, 3]], expected: 4 },
            { args: [[-1, -5, 0]], expected: -1 }
        ]
    },
    154: {
        functionNames: ['find_last_element', 'find_second_last_element'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], inputValues: ['1 2 3 4'], expected: '3' },
            { args: [], inputValues: ['apple banana cherry'], expected: 'banana' }
        ]
    },
    155: {
        functionNames: ['reverse_number'],
        tests: [
            { args: [123], expected: 321 },
            { args: [9080], expected: 809 },
            { args: [7], expected: 7 }
        ]
    },
    156: {
        functionNames: ['remove_duplicates'],
        compare: 'unorderedList',
        tests: [
            { args: ['banana'], expected: ['b', 'a', 'n'] },
            { args: ['abc'], expected: ['a', 'b', 'c'] }
        ]
    },
    157: {
        functionNames: ['remove_duplicates', 'main'],
        compare: 'unorderedWords',
        tests: [
            { args: ['and here is was and in the'], expected: ['and'] },
            { args: ['hot cold hot warm cold'], expected: ['hot', 'cold'] }
        ]
    },
    158: {
        functionNames: ['largest_element', 'main'],
        tests: [
            { args: [[2, 56, 75, 4566, 3]], expected: 4566 },
            { args: [[-5, -2, -9]], expected: -2 },
            { args: [[7]], expected: 7 }
        ]
    },
    159: {
        functionNames: ['largest_element'],
        tests: [
            { args: [[2, 56, 75, 4566, 3]], expected: 4566 },
            { args: [[-5, -2, -9]], expected: -2 },
            { args: [[7]], expected: 7 }
        ]
    },
    160: {
        functionNames: ['find_length'],
        tests: [
            { args: ['hello'], expected: 5 },
            { args: [[1, 2, 3]], expected: 3 },
            { args: [''], expected: 0 }
        ]
    },
    161: {
        functionNames: ['intersection_two_list', 'intersection'],
        compare: 'unorderedList',
        tests: [
            { args: [['tree', 'sky', 'tree'], ['sky', 'road']], expected: ['sky'] },
            { args: [[1, 2, 3], [2, 3, 4]], expected: [2, 3] },
            { args: [[1], [2]], expected: [] }
        ]
    },
    162: {
        functionNames: ['third_largest'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], inputValues: ['10 5 20 15 8'], expected: '10' },
            { args: [], inputValues: ['1 2 3 4'], expected: '2' }
        ]
    },
    163: {
        functionNames: ['count_vowels'],
        tests: [
            { args: ['JOnathAn is the best'], expected: { a: 2, e: 2, i: 1, o: 1, u: 0 } },
            { args: ['AEIOU xyz'], expected: { a: 1, e: 1, i: 1, o: 1, u: 1 } }
        ]
    },
    164: {
        functionNames: ['count_vowels'],
        tests: [
            { args: ['Jonathan is the best'], expected: { a: 2, e: 2, i: 1, o: 1, u: 0 } },
            { args: ['rhythm'], expected: { a: 0, e: 0, i: 0, o: 0, u: 0 } }
        ]
    },
    165: {
        functionNames: ['intiger_string', 'split_number_int'],
        tests: [
            { args: [123], expected: ['1', '2', '3'] },
            { args: [908], expected: ['9', '0', '8'] }
        ]
    },
    166: {
        functionNames: ['double_elements'],
        tests: [
            { args: [['tree', 'sky']], expected: ['tree', 'sky', 'tree', 'sky'] },
            { args: [['a']], expected: ['a', 'a'] },
            { args: [[]], expected: [] }
        ]
    },
    167: {
        functionNames: ['l_s', 'main'],
        tests: [
            { args: [[1, 2, 3, 4, 5]], expected: [5, 1] },
            { args: [[-5, -2, -9]], expected: [-2, -9] }
        ]
    },
    168: {
        functionNames: ['count_words'],
        tests: [
            { args: ['This is a test this test'], expected: { a: 1, is: 1, test: 2, this: 2 } },
            { args: ['Apple apple banana'], expected: { apple: 2, banana: 1 } }
        ]
    },
    169: {
        functionNames: ['merge_dictionaries'],
        tests: [
            { args: [{ a: 1, b: 2 }, { b: 9, c: 3 }], expected: { a: 1, b: 9, c: 3 } },
            { args: [{}, { x: 1 }], expected: { x: 1 } }
        ]
    },
    170: {
        functionNames: ['count_characters'],
        tests: [
            { args: ['hello'], expected: { h: 1, e: 1, l: 2, o: 1 } },
            { args: ['aba'], expected: { a: 2, b: 1 } }
        ]
    },
    171: {
        functionNames: ['invert_dictionary'],
        tests: [
            { args: [{ a: 'red', b: 'blue', c: 'red' }], expected: { red: ['a', 'c'], blue: ['b'] } },
            { args: [{ x: 'yes', y: 'yes' }], expected: { yes: ['x', 'y'] } }
        ]
    },
    172: {
        functionNames: ['filter_by_value'],
        tests: [
            { args: [{ a: 1, b: 5, c: 3 }, 2], expected: { b: 5, c: 3 } },
            { args: [{ a: 1 }, 10], expected: {} }
        ]
    },
    173: {
        functionNames: ['combine_lists_to_dict'],
        tests: [
            { args: [['a', 'b'], [1, 2]], expected: { a: 1, b: 2 } },
            { args: [['x'], ['red']], expected: { x: 'red' } }
        ]
    },
    174: {
        functionNames: ['max_value_key'],
        tests: [
            { args: [{ a: 1, b: 5, c: 3 }], expected: 'b' },
            { args: [{}], expected: null }
        ]
    },
    175: {
        functionNames: ['dict_equal'],
        tests: [
            { args: [{ a: 1, b: 2 }, { b: 2, a: 1 }], expected: true },
            { args: [{ a: 1 }, { a: 2 }], expected: false },
            { args: [{ a: 1 }, { a: 1, b: 2 }], expected: false }
        ]
    },
    176: {
        functionNames: ['word_frequency'],
        tests: [
            { args: ['gore why are you here you are gore'], expected: { gore: 2, why: 1, are: 2, you: 2, here: 1 } },
            { args: ['one two one'], expected: { one: 2, two: 1 } }
        ]
    },
    177: {
        functionNames: ['merge_list_of_dicts'],
        tests: [
            { args: [[{ a: 1, b: 2 }, { b: 3, c: 4 }, { a: 5 }]], expected: { a: 5, b: 3, c: 4 } },
            { args: [[{ x: 1 }, { y: 2 }]], expected: { x: 1, y: 2 } }
        ]
    },
    178: {
        functionNames: ['remove_duplicates_from_values'],
        compare: 'dictUnorderedLists',
        tests: [
            { args: [{ a: [1, 2, 2, 3], b: [3, 4, 4, 5], c: [1, 1] }], expected: { a: [1, 2, 3], b: [3, 4, 5], c: [1] } },
            { args: [{ x: ['a', 'a', 'b'] }], expected: { x: ['a', 'b'] } }
        ]
    },
    179: {
        functionNames: ['common_keys_max_values'],
        tests: [
            { args: [{ a: 1, b: 2, c: 3 }, { b: 3, c: 1, d: 4 }], expected: { b: 3, c: 3 } },
            { args: [{ x: 10 }, { y: 5 }], expected: {} }
        ]
    },
    180: {
        functionNames: ['average_values'],
        tests: [
            { args: [[{ a: 1, b: 2 }, { a: 3, b: 4 }, { a: 5, b: 6 }]], expected: { a: 3, b: 4 } },
            { args: [[{ a: 2 }, { a: 4, b: 10 }]], expected: { a: 3, b: 10 } }
        ]
    },
    181: {
        functionNames: ['merge_dicts_with_lists'],
        compare: 'dictUnorderedLists',
        tests: [
            { args: [[{ a: [1, 2, 3], b: [2, 3] }, { a: [3, 4], b: [4, 5], c: [6] }]], expected: { a: [1, 2, 3, 4], b: [2, 3, 4, 5], c: [6] } },
            { args: [[{ x: [1, 1] }, { x: [2] }]], expected: { x: [1, 2] } }
        ]
    },
    182: {
        functionNames: ['group_by_first_letter', 'main'],
        tests: [
            { args: [['apple', 'ant', 'banana', 'boat']], expected: { a: ['apple', 'ant'], b: ['banana', 'boat'] } },
            { args: [['cat', 'dog']], expected: { c: ['cat'], d: ['dog'] } }
        ]
    },
    183: {
        functionNames: ['is_anagram'],
        tests: [
            { args: ['listen', 'silent'], expected: true },
            { args: ['dormitory', 'dirty room'], expected: true },
            { args: ['hello', 'world'], expected: false }
        ]
    },
    184: {
        functionNames: ['int'],
        compare: 'printedOrReturn',
        tests: [
            { args: [123], expected: '2' },
            { args: [987], expected: '8' }
        ]
    },
    185: {
        functionNames: ['int'],
        tests: [
            { args: [12345678], expected: ['2', '4', '8'] },
            { args: [98765432], expected: ['8', '6', '2'] }
        ]
    },
    186: {
        functionNames: ['get_digits'],
        tests: [
            { args: [12345678910, [1, 3, 7]], expected: ['2', '4', '8'] },
            { args: [98765432, [1, 3, 7]], expected: ['8', '6', '2'] }
        ]
    },
    187: {
        functionNames: ['double_elements'],
        tests: [
            { args: [['tree', 'road', 'slow']], expected: ['tree', 'tree', 'road', 'road', 'slow', 'slow'] },
            { args: [['a', 'b']], expected: ['a', 'a', 'b', 'b'] }
        ]
    },
    188: {
        functionNames: ['get_initials'],
        tests: [
            { args: ['jonathan moll'], expected: 'joNathAn moLL' }
        ]
    },
    189: {
        functionNames: ['sum_digits', 'digits_string'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], inputValues: ['1234'], expected: '10' },
            { args: [], inputValues: ['908'], expected: '17' }
        ]
    },
    190: {
        functionNames: ['remove_duplicate'],
        tests: [
            { args: [], inputValues: ['banana'], expected: ['b', 'a', 'n'] },
            { args: [], inputValues: ['abc'], expected: ['a', 'b', 'c'] }
        ]
    },
    191: {
        functionNames: ['find_min'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], inputValues: ['5 2 9 -1'], expected: '-1' },
            { args: [], inputValues: ['10 3 7'], expected: '3' }
        ]
    },
    192: {
        functionNames: ['count_occurrences'],
        tests: [
            { args: [[1, 2, 3, 1, 1], 1], expected: 3 },
            { args: [['a', 'b', 'a'], 'a'], expected: 2 },
            { args: [[1, 2], 9], expected: 0 }
        ]
    },
    193: {
        functionNames: ['find_min_num'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], inputValues: ['5 2 9 -1'], expected: '-1' },
            { args: [], inputValues: ['10 3 7'], expected: '3' }
        ]
    },
    194: {
        functionNames: ['largest_element'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], inputValues: ['tree mountain sky'], expected: 'mountain' },
            { args: [], inputValues: ['a ab abc'], expected: 'abc' }
        ]
    },
    195: {
        functionNames: ['second_largest_element'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], inputValues: ['tree mountain sky river'], expected: 'river' },
            { args: [], inputValues: ['a ab abc abcd'], expected: 'abc' }
        ]
    },
    196: {
        functionNames: ['max_of_three'],
        tests: [
            { args: [[567, 56, 6]], expected: 567 },
            { args: [[-5, -2, -9]], expected: -2 },
            { args: [[3, 9, 1]], expected: 9 }
        ]
    },
    197: {
        functionNames: ['max_of_three'],
        tests: [
            { args: [[567, 56, 6]], expected: 567 },
            { args: [[-5, -2, -9]], expected: -2 },
            { args: [[3, 9, 1]], expected: 9 }
        ]
    },
    198: {
        functionNames: ['centimeters_inches'],
        compare: 'numberRange',
        tests: [
            { args: [], inputValues: ['10'], expected: [3.936, 3.938] },
            { args: [], inputValues: ['5'], expected: [1.967, 1.969] }
        ]
    },
    199: {
        functionNames: ['find_min_max'],
        compare: 'numberList',
        tests: [
            { args: [], inputValues: ['5 2 9 -1'], expected: [-1, 9] },
            { args: [], inputValues: ['10 3 7'], expected: [3, 10] }
        ]
    },
    200: {
        functionNames: ['common_numbers'],
        compare: 'unorderedList',
        tests: [
            { args: [[43, 2, 45, 567, 666, 2, 45]], expected: [2, 45] },
            { args: [[1, 2, 3]], expected: [] },
            { args: [[5, 5, 5]], expected: [5] }
        ]
    },
    201: {
        functionNames: ['common_num', 'common_numbers'],
        compare: 'unorderedList',
        tests: [
            { args: [[2, 5, 6, 2, 4, 5]], expected: [2, 5] },
            { args: [[43, 2, 45, 567, 666, 2, 45, 43]], expected: [2, 45, 43] },
            { args: [[1, 2, 3]], expected: [] }
        ]
    },
    202: {
        functionNames: ['word_frequency'],
        tests: [
            { args: ['banana'], expected: { a: 3, b: 1, n: 2 } },
            { args: ['a b a'], expected: { a: 2, b: 1 } }
        ]
    },
    203: {
        functionNames: ['total'],
        tests: [
            { args: [[1, 2, 3, 4]], expected: [10, 24] },
            { args: [[-2, 5, 3]], expected: [6, -30] }
        ]
    },
    204: {
        functionNames: ['list_integers'],
        tests: [
            { args: [['join', 'horse', 'today']], expected: ['join', 4, 'horse', 5, 'today', 5] },
            { args: [['a', 'abc']], expected: ['a', 1, 'abc', 3] }
        ]
    },
    205: {
        functionNames: ['average', 'calculate_average'],
        compare: 'float',
        tests: [
            { args: [[2666, 566, 6777]], expected: 3336.3333333333335 },
            { args: [[2, 4, 6]], expected: 4 }
        ]
    },
    206: {
        functionNames: ['max_of_three'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], inputValues: ['567 56 6'], expected: '567' },
            { args: [], inputValues: ['-5 -2 -9'], expected: '-2' }
        ]
    },
    207: {
        functionNames: ['max_of_list'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], inputValues: ['5 2 9'], expected: '9' },
            { args: [], inputValues: ['-5 -2 -9'], expected: '-2' }
        ]
    },
    208: {
        functionNames: ['max_of_list'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], inputValues: ['5 2 9'], expected: '9' },
            { args: [], inputValues: ['-5 -2 -9'], expected: '-2' }
        ]
    },
    209: {
        functionNames: ['list_words'],
        tests: [
            { args: [['jonathan', 'horse', 'today']], expected: ['jonathan', 8, 'horse', 5, 'today', 5] },
            { args: [['a', 'abc']], expected: ['a', 1, 'abc', 3] }
        ]
    },
    210: {
        functionNames: ['list_words'],
        tests: [
            { args: [['jonathan', 'horse', 'today']], expected: ['jonathan', 8, 'horse', 5, 'today', 5] },
            { args: [['a', 'abc']], expected: ['a', 1, 'abc', 3] }
        ]
    },
    211: {
        functionNames: ['length_words'],
        tests: [
            { args: [['jonathan', 'horse', 'today']], expected: [8, 5, 5] },
            { args: [['a', 'abc']], expected: [1, 3] }
        ]
    },
    212: {
        functionNames: ['intersection'],
        compare: 'unorderedList',
        tests: [
            { args: [], inputValues: ['1 2 3', '3 4 2'], expected: ['2', '3'] },
            { args: [], inputValues: ['a b', 'c d'], expected: [] }
        ]
    },
    215: {
        functionNames: ['square_pattern', 'print_square_pattern'],
        compare: 'printedOrReturn',
        tests: [
            { args: [3], expected: '***\n***\n***' },
            { args: [2], expected: '**\n**' }
        ]
    },
    218: {
        functionNames: ['print_checkerboard'],
        compare: 'printedOrReturn',
        tests: [
            { args: [2], expected: '*\n *' },
            { args: [3], expected: '* *\n * \n* *' }
        ]
    },
    219: {
        functionNames: ['print_floyds_triangle'],
        compare: 'printedOrReturn',
        tests: [
            { args: [4], expected: '1\n2 3\n4 5 6\n7 8 9 10' },
            { args: [2], expected: '1\n2 3' }
        ]
    },
    221: {
        functionNames: ['print_hollow_square'],
        compare: 'printedOrReturn',
        tests: [
            { args: [5], expected: '*****\n*   *\n*   *\n*   *\n*****' },
            { args: [3], expected: '***\n* *\n***' }
        ]
    },
    222: {
        functionNames: ['print_reverse_pyramid'],
        compare: 'printedOrReturn',
        tests: [
            { args: [5], expected: '1 2 3 4 5\n1 2 3 4\n1 2 3\n1 2\n1' },
            { args: [3], expected: '1 2 3\n1 2\n1' }
        ]
    },
    224: {
        functionNames: ['triangle_pattern'],
        compare: 'printedOrReturn',
        tests: [
            { args: [5], expected: 'A\nB B\nC C C\nD D D D\nE E E E E' },
            { args: [3], expected: 'A\nB B\nC C C' }
        ]
    },
    225: {
        functionNames: ['print_square_pattern'],
        compare: 'printedOrReturn',
        tests: [
            { args: [5], expected: '1 2 3 4 5\n1 2 3 4 5\n1 2 3 4 5\n1 2 3 4 5\n1 2 3 4 5' },
            { args: [3], expected: '1 2 3\n1 2 3\n1 2 3' }
        ]
    },
    226: {
        functionNames: ['print_hollow_right_triangle'],
        compare: 'printedOrReturn',
        tests: [
            { args: [5], expected: '*\n**\n* *\n*  *\n*****' },
            { args: [3], expected: '*\n**\n***' }
        ]
    },
    228: {
        functionNames: ['print_cross'],
        compare: 'printedOrReturn',
        tests: [
            { args: [5], expected: '*   *\n * * \n  *  \n * * \n*   *' },
            { args: [3], expected: '* *\n * \n* *' }
        ]
    },
    229: {
        functionNames: ['print_hourglass'],
        compare: 'printedOrReturn',
        tests: [
            { args: [5], expected: '*****\n ***\n  *\n ***\n*****' },
            { args: [3], expected: '***\n *\n***' }
        ]
    },
    230: {
        functionNames: ['count_occurrences'],
        tests: [
            { args: [['tom', 'bob', 'tom']], expected: { tom: 2, bob: 1 } },
            { args: [[1, 2, 1, 3, 2, 1]], expected: { 1: 3, 2: 2, 3: 1 } }
        ]
    },
    231: {
        functionNames: ['sum_of_odd'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], inputValues: ['1 2 3 4 5'], expected: '9' },
            { args: [], inputValues: ['2 4 6'], expected: '0' }
        ]
    },
    232: {
        functionNames: ['remove_vowels'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], inputValues: ['Jonathan'], expected: 'Jnthn' },
            { args: [], inputValues: ['AEIOUxyz'], expected: 'xyz' }
        ]
    },
    233: {
        functionNames: ['find_min'],
        tests: [
            { args: [[13, 566, 1]], expected: 1 },
            { args: [[-5, -2, -9]], expected: -9 },
            { args: [[7]], expected: 7 }
        ]
    },
    235: {
        functionNames: ['increasing_triangle'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: '*\n**\n***\n****\n*****' }
        ]
    },
    236: {
        functionNames: ['decreasing_triangle'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: '*****\n****\n***\n**\n*' }
        ]
    },
    237: {
        functionNames: ['right_triangle'],
        compare: 'printedOrReturn',
        tests: [
            { args: [5], expected: '*\n**\n***\n****\n*****' },
            { args: [3], expected: '*\n**\n***' }
        ]
    },
    238: {
        functionNames: ['left_triangle'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: '    *\n   **\n  ***\n ****\n*****' }
        ]
    },
    239: {
        functionNames: ['print_hill_pattern'],
        compare: 'printedOrReturn',
        tests: [
            { args: [5], expected: '    *\n   ***\n  *****\n *******\n*********' },
            { args: [3], expected: '  *\n ***\n*****' }
        ]
    },
    240: {
        functionNames: ['print_reverse_hill_pattern'],
        compare: 'printedOrReturn',
        tests: [
            { args: [5], expected: '*********\n *******\n  *****\n   ***\n    *' },
            { args: [3], expected: '*****\n ***\n  *' }
        ]
    },
    241: {
        functionNames: ['enumerate_lst'],
        compare: 'printedOrReturn',
        tests: [
            { args: [['Jon', 'Chris', 'Nathan']], expected: 'index 0 name Jon\nindex 1 name Chris\nindex 2 name Nathan' }
        ]
    },
    242: {
        functionNames: ['enumerate_lst'],
        tests: [
            { args: [['Jon', 'Chris', 'Nathan']], expected: [[0, 'Jon'], [1, 'Chris'], [2, 'Nathan']] },
            { args: [['a']], expected: [[0, 'a']] }
        ]
    },
    243: {
        functionNames: ['enumerate_lst'],
        tests: [
            { args: [['Jon', 'Chris', 'Nathan'], 'Chris'], expected: ['Chris', 1] },
            { args: [['a', 'b'], 'x'], expected: -1 }
        ]
    },
    244: {
        functionNames: ['enumerate_lst'],
        compare: 'printedOrReturn',
        tests: [
            { args: [['Jon', 'Chris', 'Nathan']], expected: 'Index 1, Name Jon\nIndex 2, Name Chris\nIndex 3, Name Nathan' }
        ]
    },
    245: {
        functionNames: ['enumerate_lst'],
        tests: [
            { args: [['Jon', 'Chris', 'Nathan']], expected: { 0: 'Jon', 1: 'Chris', 2: 'Nathan' } },
            { args: [['a']], expected: { 0: 'a' } }
        ]
    },
    246: {
        functionNames: ['enumerate_lst'],
        compare: 'printedOrReturn',
        tests: [
            { args: [['Jon', 'Chris', 'Nathan', 'Moll']], expected: '0 Jon\n2 Nathan' }
        ]
    },
    247: {
        functionNames: ['enumerate_lst'],
        compare: 'printedOrReturn',
        tests: [
            { args: [['Jon', 'Chris']], expected: 'index 0 name Jon\nindex 1 name Chris' }
        ]
    },
    248: {
        functionNames: ['replace_with_index'],
        tests: [
            { args: [['Jon', 'Chris', 'Nathan']], expected: [0, 1, 2] },
            { args: [['a']], expected: [0] }
        ]
    },
    249: {
        functionNames: ['enumerate_lst'],
        compare: 'printedOrReturn',
        tests: [
            { args: [['Jon', 'Chris'], ['Moll', 'Smith']], expected: 'index 0: Jon and Moll\nindex 1: Chris and Smith' }
        ]
    },
    250: {
        functionNames: ['sum_odd_indexed_elements'],
        tests: [
            { args: [[1, 2, 3, 4, 5, 6]], expected: 12 },
            { args: [[10, 20, 30]], expected: 20 }
        ]
    },
    251: {
        functionNames: ['pair_elements'],
        tests: [
            { args: [['Jon', 'Chris'], ['Moll', 'Smith']], expected: [['Jon', 'Moll'], ['Chris', 'Smith']] },
            { args: [[1, 2], ['a', 'b']], expected: [[1, 'a'], [2, 'b']] }
        ]
    },
    252: {
        functionNames: ['sum_of_2_lst'],
        tests: [
            { args: [[2, 4, 6, 8], [2, 4, 6, 8]], expected: [4, 8, 12, 16] },
            { args: [[1, -2], [3, 4]], expected: [4, 2] }
        ]
    },
    253: {
        functionNames: ['sort_tuples_by_second'],
        tests: [
            { args: [[['a', 3], ['b', 1], ['c', 2]]], expected: [['b', 1], ['c', 2], ['a', 3]] },
            { args: [[['x', -1], ['y', -3]]], expected: [['y', -3], ['x', -1]] }
        ]
    },
    254: {
        functionNames: ['dic_lst'],
        tests: [
            { args: [[1, 2, 3], ['one', 'two', 'three']], expected: { 1: 'one', 2: 'two', 3: 'three' } },
            { args: [['a', 'b'], [10, 20]], expected: { a: 10, b: 20 } }
        ]
    },
    255: {
        functionNames: ['combine_3_lst'],
        tests: [
            { args: [['Sam', 'Ron'], [1, 2], ['x', 'y']], expected: [['Sam', 1, 'x'], ['Ron', 2, 'y']] },
            { args: [[1], [2], [3]], expected: [[1, 2, 3]] }
        ]
    },
    256: {
        functionNames: ['transpose_matrix'],
        tests: [
            { args: [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]], expected: [[1, 4, 7], [2, 5, 8], [3, 6, 9]] },
            { args: [[[1, 2], [3, 4]]], expected: [[1, 3], [2, 4]] }
        ]
    },
    257: {
        functionNames: ['list_tuples'],
        tests: [
            { args: [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]], expected: [[1, 4, 7], [2, 5, 8], [3, 6, 9]] },
            { args: [[['a', 'b'], ['c', 'd']]], expected: [['a', 'c'], ['b', 'd']] }
        ]
    },
    258: {
        functionNames: ['individualists'],
        tests: [
            { args: [[[1, 2, 3], [4, 5, 6]]], expected: [[1, 4], [2, 5], [3, 6]] },
            { args: [[['a', 'b'], ['c', 'd']]], expected: [['a', 'c'], ['b', 'd']] }
        ]
    },
    259: {
        functionNames: ['maxium_element_wise', 'maximum_element_wise'],
        tests: [
            { args: [[2, 4, 6], [7, 8, 9]], expected: [7, 8, 9] },
            { args: [[10, 1], [3, 9]], expected: [10, 9] }
        ]
    },
    260: {
        functionNames: ['concatenate'],
        tests: [
            { args: [['fruit', 'blue'], ['orange', 'sky']], expected: ['fruit orange', 'blue sky'] },
            { args: [['a'], ['b']], expected: ['a b'] }
        ]
    },
    261: {
        functionNames: ['combine_to_dict'],
        tests: [
            { args: [[1, 2, 3], ['one', 'two', 'three']], expected: [{ a: 1, b: 'one' }, { a: 2, b: 'two' }, { a: 3, b: 'three' }] },
            { args: [['x'], [9]], expected: [{ a: 'x', b: 9 }] }
        ]
    },
    262: {
        functionNames: ['filter_pairs'],
        tests: [
            { args: [[5, 8, 3, 10], [4, 7, 6, 2]], expected: [[5, 4], [8, 7], [10, 2]] },
            { args: [[1, 2], [3, 1]], expected: [[2, 1]] }
        ]
    },
    263: {
        functionNames: ['filter_pairs'],
        tests: [
            { args: [[5, 8, 3, 10], [4, 7, 6, 2]], expected: [[3, 6]] },
            { args: [[1, 2], [3, 1]], expected: [[1, 3]] }
        ]
    },
    264: {
        functionNames: ['add_nested_lists'],
        tests: [
            { args: [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]], expected: [[8, 10, 12], [14, 16, 18]] },
            { args: [[[1], [2]], [[3], [4]]], expected: [[4], [6]] }
        ]
    },
    265: {
        functionNames: ['euclidean_distance'],
        compare: 'float',
        tests: [
            { args: [[3, 4], [6, 8]], expected: 5 },
            { args: [[0, 0], [3, 4]], expected: 5 }
        ]
    },
    266: {
        functionNames: ['interleave'],
        tests: [
            { args: [['a', 'b'], [1, 2]], expected: ['a', 1, 'b', 2] },
            { args: [['x'], ['y']], expected: ['x', 'y'] }
        ]
    },
    267: {
        functionNames: ['multiply_2_lst'],
        tests: [
            { args: [[2, 4, 6], [3, 6, 9]], expected: [6, 24, 54] },
            { args: [[-2, 5], [3, 0]], expected: [-6, 0] }
        ]
    },
    268: {
        functionNames: ['dot_product'],
        tests: [
            { args: [[1, 2, 3], [4, 5, 6]], expected: 32 },
            { args: [[-1, 2], [3, 4]], expected: 5 }
        ]
    },
    269: {
        functionNames: ['filter_even_numbers'],
        tests: [
            { args: [[1, 2, 3, 4, 5, 6]], expected: [1, 3, 5] },
            { args: [[2, 4]], expected: [] }
        ]
    },
    270: {
        functionNames: ['filter_odd_numbers'],
        tests: [
            { args: [[1, 2, 3, 4, 5, 6]], expected: [2, 4, 6] },
            { args: [[1, 3]], expected: [] }
        ]
    },
    271: {
        functionNames: ['filter_positive_numbers'],
        tests: [
            { args: [[-2, -1, 0, 1, 2, 3]], expected: [-2, -1, 0] },
            { args: [[1, 2]], expected: [] }
        ]
    },
    272: {
        functionNames: ['filter_negative_numbers'],
        tests: [
            { args: [[-2, -1, 0, 1, 2, 3]], expected: [0, 1, 2, 3] },
            { args: [[-1, -2]], expected: [] }
        ]
    },
    274: {
        functionNames: ['filter_palindromes'],
        tests: [
            { args: [['madam', 'hello', 'racecar', 'world', 'level']], expected: ['madam', 'racecar', 'level'] },
            { args: [['abc', 'noon']], expected: ['noon'] }
        ]
    },
    276: {
        functionNames: ['filter_divisible'],
        tests: [
            { args: [[10, 15, 20, 22], 5], expected: [10, 15, 20] },
            { args: [[1, 2, 3, 4, 5, 6], 2], expected: [2, 4, 6] }
        ]
    },
    277: {
        functionNames: ['is_not_divisible'],
        tests: [
            { args: [4, 3], expected: true },
            { args: [6, 3], expected: false },
            { args: [10, 5], expected: false }
        ]
    },
    278: {
        functionNames: ['filter_non_empty'],
        tests: [
            { args: [['apple', '', 'banana', '']], expected: ['apple', 'banana'] },
            { args: [['']], expected: [] }
        ]
    },
    279: {
        functionNames: ['filter_prime'],
        tests: [
            { args: [[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17]], expected: [2, 3, 5, 7, 11, 13, 17] },
            { args: [[1, 4, 6]], expected: [] }
        ]
    },
    280: {
        functionNames: ['filter_floats'],
        tests: [
            { args: [[1, 2.5, 'apple', 3.0]], expected: [1, 'apple'] },
            { args: [[1.1, 2.2]], expected: [] }
        ]
    },
    281: {
        functionNames: ['filter_uppercase'],
        tests: [
            { args: [['HELLO', 'world', 'PYTHON', 'code']], expected: ['world', 'code'] },
            { args: [['ABC']], expected: [] }
        ]
    },
    282: {
        functionNames: ['filter_uppercase_again'],
        tests: [
            { args: [['HELLO', 'WORLD', 'python', 'CHATGPT', 'openai']], expected: ['python', 'openai'] },
            { args: [['UP', 'DOWN']], expected: [] }
        ]
    },
    283: {
        functionNames: ['filter_non_none'],
        tests: [
            { args: [[1, null, 'x', null, 0]], expected: [1, 'x', 0] },
            { args: [[null]], expected: [] }
        ]
    },
    284: {
        functionNames: ['filter_by_substring'],
        tests: [
            { args: [['apple', 'banana', 'grape'], 'ap'], expected: ['banana'] },
            { args: [['one', 'two'], 'z'], expected: ['one', 'two'] }
        ]
    },
    285: {
        functionNames: ['print_1_to_10'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: '1\n2\n3\n4\n5\n6\n7\n8\n9\n10' }
        ]
    },
    286: {
        functionNames: ['sum_first_10_natural_numbers'],
        tests: [
            { args: [], expected: 55 }
        ]
    },
    287: {
        functionNames: ['print_even_numbers'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: '2\n4\n6\n8\n10\n12\n14\n16\n18\n20' }
        ]
    },
    288: {
        functionNames: ['print_odd_numbers'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: '1\n3\n5\n7\n9\n11\n13\n15\n17\n19' }
        ]
    },
    289: {
        functionNames: ['sum_of_digits'],
        tests: [
            { args: [12345], expected: 15 },
            { args: [908], expected: 17 }
        ]
    },
    290: {
        functionNames: ['reverse_number'],
        tests: [
            { args: [12345], expected: 54321 },
            { args: [1200], expected: 21 },
            { args: [7], expected: 7 }
        ]
    },
    291: {
        functionNames: ['factorial'],
        tests: [
            { args: [0], expected: 1 },
            { args: [5], expected: 120 },
            { args: [6], expected: 720 }
        ]
    },
    292: {
        functionNames: ['multiplication_table'],
        compare: 'printedOrReturn',
        tests: [
            { args: [5], expected: '5 x 1 = 5\n5 x 2 = 10\n5 x 3 = 15\n5 x 4 = 20\n5 x 5 = 25\n5 x 6 = 30\n5 x 7 = 35\n5 x 8 = 40\n5 x 9 = 45\n5 x 10 = 50' }
        ]
    },
    293: {
        functionNames: ['is_prime'],
        tests: [
            { args: [2], expected: true },
            { args: [17], expected: true },
            { args: [1], expected: false },
            { args: [9], expected: false }
        ]
    },
    294: {
        functionNames: ['count_digits'],
        tests: [
            { args: [12345], expected: 5 },
            { args: [7], expected: 1 },
            { args: [987654321], expected: 9 }
        ]
    },
    295: {
        functionNames: ['gcd'],
        tests: [
            { args: [48, 18], expected: 6 },
            { args: [101, 103], expected: 1 },
            { args: [56, 0], expected: 56 }
        ]
    },
    296: {
        functionNames: ['fibonacci_sequence'],
        compare: 'printedOrReturn',
        tests: [
            { args: [5], expected: '0\n1\n1\n2\n3' },
            { args: [1], expected: '0' }
        ]
    },
    297: {
        functionNames: ['sum_elements'],
        tests: [
            { args: [[1, 2, 3, 4, 5]], expected: 15 },
            { args: [[]], expected: 0 },
            { args: [[-2, 5]], expected: 3 }
        ]
    },
    298: {
        functionNames: ['find_largest_element', 'main'],
        tests: [
            { args: [[5, 9, 1]], expected: 9 },
            { args: [[-5, -2, -9]], expected: -2 }
        ]
    },
    299: {
        functionNames: ['smallest_element'],
        tests: [
            { args: [[13, 566, 1]], expected: 1 },
            { args: [[-5, -2, -9]], expected: -9 }
        ]
    },
    300: {
        functionNames: ['remove_all_occurrences'],
        tests: [
            { args: [[1, 2, 3, 3, 4], 3], expected: [1, 2, 4] },
            { args: [['apple', 'banana', 'banana'], 'banana'], expected: ['apple'] }
        ]
    }
};
