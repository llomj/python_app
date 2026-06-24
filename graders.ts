export type CompareMode = 'exact' | 'float' | 'printedOrReturn' | 'numberRange' | 'length' | 'unorderedList' | 'letterCounts' | 'vowelConsonantCounts';

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
    }
};
