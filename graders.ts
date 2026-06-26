export type CompareMode = 'exact' | 'float' | 'printedOrReturn' | 'numberRange' | 'setPop' | 'length' | 'typeName' | 'unorderedList' | 'unorderedWords' | 'numberList' | 'dictUnorderedLists' | 'letterCounts' | 'vowelConsonantCounts';

export interface AutoTestCase {
    args: unknown[];
    kwargs?: Record<string, unknown>;
    expected: unknown;
    inputValues?: string[];
    setupRemove?: string[];
    setupDirs?: string[];
    setupFiles?: Record<string, string>;
    permissionDeniedPaths?: string[];
    getFiles?: string[];
    randomValues?: number[];
    randomFloatValues?: number[];
    randomChoiceValues?: unknown[];
    randomSampleValues?: unknown[][];
    randomShuffleValues?: unknown[][];
    callReturnedWith?: unknown[];
    callMethod?: string;
    callMethodArgs?: unknown[];
    callMethodArgExpressions?: string[];
    getAttrs?: string[];
    setAttrs?: Record<string, unknown>;
    deleteAttrs?: string[];
    setItems?: Array<{ key: unknown; value: unknown }>;
    deleteItems?: unknown[];
    argExpressions?: string[];
    argFunctionNames?: string[];
    functionListArgNames?: string[];
    functionName?: string;
    expectedException?: string;
    label?: string;
}

export interface AutoGrader {
    functionNames: string[];
    mode?: 'function' | 'script';
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
        functionNames: ['calculate_square', 'cal_square'],
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
            { args: ['Jonathan', 'noll'], expected: 'Jonathannoll' },
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
            { args: ['jonathan noll'], expected: 'Jonathan Noll' },
            { args: ['a b c'], expected: 'A B C' }
        ]
    },
    30: {
        functionNames: ['remove_spaces', 'remove_space'],
        tests: [
            { args: ['remove spaces sample Jonathan'], expected: 'removespacessampleJonathan' },
            { args: ['what just happened'], expected: 'whatjusthappened' },
            { args: [' no spaces '], expected: 'nospaces' }
        ]
    },
    31: {
        functionNames: ['get_initials'],
        tests: [
            { args: ['John Doe'], expected: 'J.D.' },
            { args: ['jonathan noll'], expected: 'J.N.' },
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
            { args: [3], expected: '3 * 0 = 0\n3 * 1 = 3\n3 * 2 = 6\n3 * 3 = 9\n3 * 4 = 12\n3 * 5 = 15\n3 * 6 = 18\n3 * 7 = 21\n3 * 8 = 24\n3 * 9 = 27\n3 * 10 = 30' },
            { args: [5], expected: '5 * 0 = 0\n5 * 1 = 5\n5 * 2 = 10\n5 * 3 = 15\n5 * 4 = 20\n5 * 5 = 25\n5 * 6 = 30\n5 * 7 = 35\n5 * 8 = 40\n5 * 9 = 45\n5 * 10 = 50' }
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
            { args: ['Jonathan Noll'], expected: 2 },
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
            { args: ['Jonathan Noll'], expected: 2 },
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
            { args: ['Jonathan Noll'], expected: { upper: 2, lower: 10 } },
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
  133: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [{ args: [], expected: '1 x 1 = 1\n1 x 2 = 2\n1 x 3 = 3\n1 x 4 = 4\n1 x 5 = 5\n1 x 6 = 6\n1 x 7 = 7\n1 x 8 = 8\n1 x 9 = 9\n1 x 10 = 10\n2 x 1 = 2\n2 x 2 = 4\n2 x 3 = 6\n2 x 4 = 8\n2 x 5 = 10\n2 x 6 = 12\n2 x 7 = 14\n2 x 8 = 16\n2 x 9 = 18\n2 x 10 = 20\n3 x 1 = 3\n3 x 2 = 6\n3 x 3 = 9\n3 x 4 = 12\n3 x 5 = 15\n3 x 6 = 18\n3 x 7 = 21\n3 x 8 = 24\n3 x 9 = 27\n3 x 10 = 30\n4 x 1 = 4\n4 x 2 = 8\n4 x 3 = 12\n4 x 4 = 16\n4 x 5 = 20\n4 x 6 = 24\n4 x 7 = 28\n4 x 8 = 32\n4 x 9 = 36\n4 x 10 = 40\n5 x 1 = 5\n5 x 2 = 10\n5 x 3 = 15\n5 x 4 = 20\n5 x 5 = 25\n5 x 6 = 30\n5 x 7 = 35\n5 x 8 = 40\n5 x 9 = 45\n5 x 10 = 50\n6 x 1 = 6\n6 x 2 = 12\n6 x 3 = 18\n6 x 4 = 24\n6 x 5 = 30\n6 x 6 = 36\n6 x 7 = 42\n6 x 8 = 48\n6 x 9 = 54\n6 x 10 = 60\n7 x 1 = 7\n7 x 2 = 14\n7 x 3 = 21\n7 x 4 = 28\n7 x 5 = 35\n7 x 6 = 42\n7 x 7 = 49\n7 x 8 = 56\n7 x 9 = 63\n7 x 10 = 70\n8 x 1 = 8\n8 x 2 = 16\n8 x 3 = 24\n8 x 4 = 32\n8 x 5 = 40\n8 x 6 = 48\n8 x 7 = 56\n8 x 8 = 64\n8 x 9 = 72\n8 x 10 = 80\n9 x 1 = 9\n9 x 2 = 18\n9 x 3 = 27\n9 x 4 = 36\n9 x 5 = 45\n9 x 6 = 54\n9 x 7 = 63\n9 x 8 = 72\n9 x 9 = 81\n9 x 10 = 90\n10 x 1 = 10\n10 x 2 = 20\n10 x 3 = 30\n10 x 4 = 40\n10 x 5 = 50\n10 x 6 = 60\n10 x 7 = 70\n10 x 8 = 80\n10 x 9 = 90\n10 x 10 = 100' }]
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
            { args: ['jonathan noll'], expected: 'joNathAn noLL' }
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
  213: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [{ args: [], expected: '*\n* *\n* * *\n* * * *\n* * * * *' }]
  },
  214: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [{ args: [], expected: '1\n2 2\n3 3 3\n4 4 4 4\n5 5 5 5 5' }]
  },
    215: {
        functionNames: ['square_pattern', 'print_square_pattern'],
        compare: 'printedOrReturn',
        tests: [
            { args: [3], expected: '***\n***\n***' },
            { args: [2], expected: '**\n**' }
        ]
    },
  216: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [{ args: [], expected: '1\n1 2\n1 2 3\n1 2 3 4\n1 2 3 4 5' }]
  },
  217: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [{ args: [], expected: '* * * * *\n* * * *\n* * *\n* *\n*' }]
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
  227: {
    functionNames: ["print_zigzag"],
    compare: 'printedOrReturn',
    tests: [{
      args: [5],
      expected: "*       * \n  *       \n*       * \n  *       \n*       *"
    }]
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
  234: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [{ args: [], expected: '* * * * *\n* * * * *\n* * * * *\n* * * * *\n* * * * *' }]
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
            { args: [['Jon', 'Chris', 'Nathan']], expected: 'index 0 name Jon\nindex 1 name Chris\nindex 2 name Nathan' },
            { args: [['A', 'B']], expected: 'index 0 name A\nindex 1 name B' }
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
            { args: [['Jon', 'Chris', 'Nathan']], expected: 'Index 1, Name Jon\nIndex 2, Name Chris\nIndex 3, Name Nathan' },
            { args: [['A', 'B']], expected: 'Index 1, Name A\nIndex 2, Name B' }
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
            { args: [['Jon', 'Chris', 'Nathan', 'Noll']], expected: '0 Jon\n2 Nathan' },
            { args: [['a', 'b', 'c', 'd', 'e']], expected: '0 a\n2 c\n4 e' }
        ]
    },
    247: {
        functionNames: ['enumerate_lst'],
        compare: 'printedOrReturn',
        tests: [
            { args: [['Jon', 'Chris']], expected: 'index 0 name Jon\nindex 1 name Chris' },
            { args: [['A', 'B', 'C']], expected: 'index 0 name A\nindex 1 name B\nindex 2 name C' }
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
            { args: [['Jon', 'Chris'], ['Noll', 'Smith']], expected: 'index 0: Jon and Noll\nindex 1: Chris and Smith' },
            { args: [['A', 'B', 'C'], ['x', 'y', 'z']], expected: 'index 0: A and x\nindex 1: B and y\nindex 2: C and z' }
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
            { args: [['Jon', 'Chris'], ['Noll', 'Smith']], expected: [['Jon', 'Noll'], ['Chris', 'Smith']] },
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
            { args: [[1, 2.5, 'apple', 3]], expected: [1, 'apple', 3] },
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
            { args: [5], expected: '5 x 1 = 5\n5 x 2 = 10\n5 x 3 = 15\n5 x 4 = 20\n5 x 5 = 25\n5 x 6 = 30\n5 x 7 = 35\n5 x 8 = 40\n5 x 9 = 45\n5 x 10 = 50' },
            { args: [3], expected: '3 x 1 = 3\n3 x 2 = 6\n3 x 3 = 9\n3 x 4 = 12\n3 x 5 = 15\n3 x 6 = 18\n3 x 7 = 21\n3 x 8 = 24\n3 x 9 = 27\n3 x 10 = 30' }
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
    },
  301: {
        functionNames: ['is_palindrome'],
        tests: [
            { args: ['radar'], expected: true },
            { args: ['hello'], expected: false },
            { args: ['level'], expected: true }
        ]
    },
  302: {
        functionNames: ['count_vowels'],
        tests: [
            { args: ['Hello, World!'], expected: 3 },
            { args: ['Python programming'], expected: 4 },
            { args: ['AEIOU'], expected: 5 }
        ]
    },
  303: {
        functionNames: ['print_each_character'],
        compare: 'printedOrReturn',
        tests: [
            { args: ['abc'], expected: 'a\nb\nc' },
            { args: ['Hi'], expected: 'H\ni' }
        ]
    },
  304: {
        functionNames: ['ask_until_condition'],
        tests: [
            { args: [], inputValues: ['11'], expected: null },
            { args: [], inputValues: ['5', '12'], expected: null }
        ]
    },
  307: {
        functionNames: ['find_min_max'],
        compare: 'numberList',
        tests: [
            { args: [], inputValues: ['10 2 7'], expected: [2, 10] },
            { args: [], inputValues: ['-5 3 9'], expected: [-5, 9] }
        ]
    },
  308: {
        functionNames: ['group_by_first_letter'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], inputValues: ['apple ape bat'], expected: "{'a': ['apple', 'ape'], 'b': ['bat']}" },
            { args: [], inputValues: ['cat cow dog'], expected: "{'c': ['cat', 'cow'], 'd': ['dog']}" }
        ]
    },
  310: {
        functionNames: ['find_longest_word', 'main'],
        tests: [
            { args: [['Jonathan', 'noll', 'it']], expected: 'Jonathan' },
            { args: [['a', 'abc', 'def']], expected: 'abc' }
        ]
    },
  311: {
        functionNames: ['find_longest_word'],
        tests: [
            { args: [['Jonathan', 'noll', 'it']], expected: 'Jonathan' },
            { args: [['a', 'ab', 'abc']], expected: 'abc' }
        ]
    },
  312: {
        functionNames: ['second_largest_number'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], inputValues: ['5 2 9 1'], expected: '5' },
            { args: [], inputValues: ['10 7 3'], expected: '7' }
        ]
    },
  313: {
        functionNames: ['convert_to_uppercase'],
        tests: [
            { args: [['hello', 'world', 'python']], expected: ['HELLO', 'WORLD', 'PYTHON'] },
            { args: [['a', 'b']], expected: ['A', 'B'] }
        ]
    },
  314: {
        functionNames: ['convert_to_integers'],
        tests: [
            { args: [['1', '2', '3', '4', '5']], expected: [1, 2, 3, 4, 5] },
            { args: [['10', '20']], expected: [10, 20] }
        ]
    },
  315: {
        functionNames: ['square_numbers'],
        tests: [
            { args: [[1, 2, 3, 4, 5]], expected: [1, 4, 9, 16, 25] },
            { args: [[-2, 3]], expected: [4, 9] }
        ]
    },
  316: {
        functionNames: ['string_lengths'],
        tests: [
            { args: [['apple', 'banana', 'cherry', 'date']], expected: [5, 6, 6, 4] },
            { args: [['a', 'ab', 'abc']], expected: [1, 2, 3] }
        ]
    },
  317: {
        functionNames: ['fahrenheit_to_celsius'],
        tests: [
            { args: [[32, 68, 100, 212]], expected: [0, 20, 37.77777777777778, 100] },
            { args: [[-40]], expected: [-40] }
        ]
    },
  319: {
        functionNames: ['add_five', 'add_five_to_number'],
        tests: [
            { args: [[1, 2, 3, 4]], expected: [6, 7, 8, 9] },
            { args: [[0, -5]], expected: [5, 0] }
        ]
    },
  320: {
        functionNames: ['square_roots', 'main'],
        tests: [
            { args: [[4, 9, 16]], expected: [2, 3, 4] },
            { args: [[1, 25]], expected: [1, 5] }
        ]
  },
  321: {
        functionNames: ['lengths_of_strings'],
        tests: [
            { args: [['apple', 'banana', 'cherry', 'date']], expected: [5, 6, 6, 4] },
            { args: [['hi', 'hello', 'hey']], expected: [2, 5, 3] }
        ]
    },
  322: {
        functionNames: ['normalize_scores'],
        tests: [
            { args: [[50, 60, 70, 80, 90]], expected: [0, 0.25, 0.5, 0.75, 1] },
            { args: [[10, 20, 30]], expected: [0, 0.5, 1] }
        ]
    },
  323: {
        functionNames: ['reverse_strings'],
        tests: [
            { args: [['hello', 'world', 'python']], expected: ['olleh', 'dlrow', 'nohtyp'] },
            { args: [['a', 'ab']], expected: ['a', 'ba'] }
        ]
    },
  324: {
        functionNames: ['double_numbers'],
        tests: [
            { args: [[1, 2, 3, 4, 5]], expected: [2, 4, 6, 8, 10] },
            { args: [[0, -3, 10]], expected: [0, -6, 20] }
        ]
    },
  325: {
        functionNames: ['strip_whitespace'],
        tests: [
            { args: [['  Hello  ', '  World  ', '  Python  ']], expected: ['Hello', 'World', 'Python'] },
            { args: [['  a', 'b  ']], expected: ['a', 'b'] }
        ]
    },
  326: {
        functionNames: ['number_and_square'],
        tests: [
            { args: [[1, 2, 3]], expected: [[1, 1], [2, 4], [3, 9]] },
            { args: [[0, -2]], expected: [[0, 0], [-2, 4]] }
        ]
    },
  327: {
        functionNames: ['to_title_case'],
        tests: [
            { args: [['hello world', 'python programming']], expected: ['Hello World', 'Python Programming'] },
            { args: [['a b c']], expected: ['A B C'] }
        ]
    },
  328: {
        functionNames: ['second_largest_number'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], inputValues: ["1 5 3 2"], expected: "3" },
            { args: [], inputValues: ["7 7 7"], expected: "Not enough unique numbers" },
        ]
    },
  329: {
        functionNames: ['list_string', 'type_smallest_biggest'],
        tests: [
            { args: [['377', '55', '44']], expected: ['44', '55', '377'] },
            { args: [['3', '1', '2']], expected: ['1', '2', '3'] }
        ]
    },
  330: {
        functionNames: ['list_of_string_numbers', 'type_biggest_smallest'],
        tests: [
            { args: [['44', '66', '3', '477']], expected: ['477', '66', '44', '3'] },
            { args: [['1', '3', '2']], expected: ['3', '2', '1'] }
        ]
    },
  331: {
        functionNames: ['print_index_and_element'],
        compare: 'printedOrReturn',
        tests: [
            { args: [['apple', 'banana']], expected: 'Index: 0, Element: apple\nIndex: 1, Element: banana' },
            { args: [['x', 'y', 'z']], expected: 'Index: 0, Element: x\nIndex: 1, Element: y\nIndex: 2, Element: z' }
        ]
    },
  332: {
        functionNames: ['create_index_element_tuples'],
        tests: [
            { args: [['apple', 'banana', 'cherry']], expected: [[0, 'apple'], [1, 'banana'], [2, 'cherry']] },
            { args: [['x', 'y']], expected: [[0, 'x'], [1, 'y']] }
        ]
    },
  333: {
        functionNames: ['print_with_index'],
        compare: 'printedOrReturn',
        tests: [
            { args: [['apple', 'banana']], expected: '0 apple\n1 banana' },
            { args: [['x']], expected: '0 x' }
        ]
  },
  334: {
        functionNames: ['list_to_dict'],
        tests: [
            { args: [['apple', 'banana', 'cherry']], expected: {0: 'apple', 1: 'banana', 2: 'cherry'} },
            { args: [['a']], expected: {0: 'a'} }
        ]
    },
  335: {
        functionNames: ['find_index'],
        tests: [
            { args: [['apple', 'banana', 'cherry'], 'banana'], expected: 1 },
            { args: [['a', 'b', 'c'], 'z'], expected: -1 }
        ]
    },
  336: {
        functionNames: ['print_index_and_element_with_colon'],
        compare: 'printedOrReturn',
        tests: [
            { args: [['apple', 'banana']], expected: '0: apple\n1: banana' },
            { args: [['x', 'y', 'z']], expected: '0: x\n1: y\n2: z' }
        ]
    },
  337: {
        functionNames: ['create_indexed_strings'],
        tests: [
            { args: [['apple', 'banana', 'cherry'], 'Item '], expected: ['Item 0: apple', 'Item 1: banana', 'Item 2: cherry'] },
            { args: [['a', 'b'], 'idx'], expected: ['idx0: a', 'idx1: b'] }
        ]
    },
  338: {
        functionNames: ['modify_elements'],
        tests: [
            { args: [['apple', 'banana', 'cherry', 'date']], expected: ['APPLE', 'banana', 'CHERRY', 'date'] },
            { args: [['a', 'b', 'c']], expected: ['A', 'b', 'C'] }
        ]
    },
  340: {
        functionNames: ['print_odd_index_elements'],
        compare: 'printedOrReturn',
        tests: [
            { args: [['apple', 'banana', 'cherry', 'date']], expected: 'banana\ndate' },
            { args: [['x', 'y']], expected: 'y' }
        ]
    },
  341: {
        functionNames: ['index_element_if_vowel'],
        tests: [
            { args: [['apple', 'banana', 'orange', 'grape']], expected: [[0, 'apple'], [2, 'orange']] },
            { args: [['egg', 'fish']], expected: [[0, 'egg']] }
        ]
    },
  342: {
        functionNames: ['find_max_and_index'],
        tests: [
            { args: [[10, 20, 30, 25]], expected: [2, 30] },
            { args: [[5, 3, 9]], expected: [2, 9] }
        ]
    },
  343: {
        functionNames: ['index_and_element_excluding_first_n'],
        tests: [
            { args: [['apple', 'banana', 'cherry', 'date', 'elderberry'], 2], expected: [[2, 'cherry'], [3, 'date'], [4, 'elderberry']] },
            { args: [['a', 'b', 'c'], 1], expected: [[1, 'b'], [2, 'c']] }
        ]
    },
  344: {
        functionNames: ['print_index_squared'],
        compare: 'printedOrReturn',
        tests: [
            { args: [[1, 2, 3]], expected: 'Index: 0, Squared: 1\nIndex: 1, Squared: 4\nIndex: 2, Squared: 9' },
            { args: [[0, -2]], expected: 'Index: 0, Squared: 0\nIndex: 1, Squared: 4' }
        ]
    },
  345: {
        functionNames: ['replace_based_on_index'],
        tests: [
            { args: [['a', 'b', 'c', 'd', 'e']], expected: ['Even', 'Odd', 'Even', 'Odd', 'Even'] },
            { args: [[1, 2]], expected: ['Even', 'Odd'] }
        ]
    },
  346: {
        functionNames: ['sum_of_squares'],
        tests: [
            { args: [3, 4], expected: 25 },
            { args: [1, 2], expected: 5 }
        ]
    },
  347: {
        functionNames: ['greet'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], inputValues: ['Ada'], expected: 'Hello, Ada!' },
            { args: [], inputValues: ['Jonathan'], expected: 'Hello, Jonathan!' }
        ]
    },
  348: {
        functionNames: ['factorial'],
        tests: [
            { args: [5], expected: 120 },
            { args: [0], expected: 1 },
            { args: [3], expected: 6 }
        ]
    },
  349: {
        functionNames: ['add_prefix'],
        tests: [
            { args: ['pre-'], callReturnedWith: ['fix'], expected: 'pre-fix' },
            { args: ['un'], callReturnedWith: ['known'], expected: 'unknown' }
        ]
    },
  350: {
        functionNames: ['check_even'],
        tests: [
            { args: [10], expected: true },
            { args: [7], expected: false },
            { args: [0], expected: true }
        ]
    },
  351: {
        functionNames: ['power'],
        tests: [
            { args: [2, 3], expected: 8 },
            { args: [5, 0], expected: 1 },
            { args: [3, 2], expected: 9 }
        ]
    },
  352: {
    functionNames: ["area_circle","calculate_area","inner"],
    compare: 'float',
    tests: [
      { args: [5], expected: 78.53981633974483 },
      { args: [1], expected: 3.141592653589793 }
    ]
  },
  353: {
        functionNames: ['capitalize_words'],
        tests: [
            { args: ['hello world from python'], expected: 'Hello World From Python' },
            { args: ['a b c'], expected: 'A B C' }
        ]
    },
  354: {
        functionNames: ['is_palindrome'],
        tests: [
            { args: ['radar'], expected: true },
            { args: ['hello'], expected: false },
            { args: ['racecar'], expected: true }
        ]
    },
  355: {
        functionNames: ['concatenate_strings'],
        tests: [
            { args: ['Hello, ', 'world!'], expected: 'Hello, world!' },
            { args: ['a', 'b'], expected: 'ab' }
        ]
    },
  356: {
        functionNames: ['fibonacci'],
        tests: [
            { args: [5], expected: [0, 1, 1, 2, 3] },
            { args: [10], expected: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] },
            { args: [1], expected: [0] }
        ]
    },
  357: {
        functionNames: ['to_uppercase'],
        tests: [
            { args: ['hello world'], expected: 'HELLO WORLD' },
            { args: ['abc'], expected: 'ABC' }
        ]
    },
  358: {
        functionNames: ['find_largest'],
        tests: [
            { args: [10, 20], expected: 20 },
            { args: [30, 5], expected: 30 },
            { args: [7, 7], expected: 7 }
        ]
    },
  359: {
        functionNames: ['calculator'],
        tests: [
            { args: ['add', 5, 3], expected: 8 },
            { args: ['multiply', 4, 2], expected: 8 },
            { args: ['subtract', 10, 3], expected: 7 }
        ]
    },
  360: {
        functionNames: ['is_prime'],
        tests: [
            { args: [7], expected: true },
            { args: [4], expected: false },
            { args: [1], expected: false },
            { args: [11], expected: true }
        ]
    },
  361: {
        functionNames: ['count_vowels'],
        tests: [
            { args: ['Hello World'], expected: 3 },
            { args: ['Python'], expected: 1 }
        ]
    },
  362: {
        functionNames: ['calculate_average'],
        compare: 'float',
        tests: [
            { args: [[1, 2, 3, 4, 5]], expected: 3 },
            { args: [[10, 20, 30]], expected: 20 }
        ]
    },
  363: {
        functionNames: ['reverse_string'],
        tests: [
            { args: ['Hello, World!'], expected: '!dlroW ,olleH' },
            { args: ['abc'], expected: 'cba' }
        ]
    },
  364: {
        functionNames: ['is_sorted', 'compare_elements'],
        tests: [
            { args: [[1, 2, 3, 4, 5]], expected: true },
            { args: [[1, 3, 2, 4]], expected: false }
        ]
    },
  365: {
        functionNames: ['generate_squares'],
        tests: [
            { args: [5], expected: [1, 4, 9, 16, 25] },
            { args: [3], expected: [1, 4, 9] }
        ]
    },
  366: {
        functionNames: ['sum_of_two'],
        tests: [
            { args: [3, 5], expected: 8 },
            { args: [10, 20], expected: 30 }
        ]
    },
  367: {
        functionNames: ['even_or_odd'],
        compare: 'printedOrReturn',
        tests: [
            { args: [10], expected: '10 is even' },
            { args: [7], expected: '7 is odd' }
        ]
    },
  368: {
        functionNames: ['convert_temperature'],
        compare: 'float',
        tests: [
            { args: [25], expected: 77 },
            { args: [0], expected: 32 },
            { args: [100], expected: 212 }
        ]
    },
  369: {
        functionNames: ['rectangle_area'],
        tests: [
            { args: [5, 10], expected: 50 },
            { args: [3, 7], expected: 21 }
        ]
    },
  370: {
        functionNames: ['check_prime'],
        tests: [
            { args: [11], expected: true },
            { args: [4], expected: false },
            { args: [2], expected: true }
        ]
    },
  371: {
        functionNames: ['find_minimum'],
        tests: [
            { args: [5, 3, 8], expected: 3 },
            { args: [10, 20, 5], expected: 5 }
        ]
    },
  373: {
        functionNames: ['calculate_factorial'],
        tests: [
            { args: [5], expected: 120 },
            { args: [3], expected: 6 },
            { args: [0], expected: 1 }
        ]
    },
  374: {
        functionNames: ['capitalize_words'],
        tests: [
            { args: ['hello world from python'], expected: 'Hello World From Python' },
            { args: ['a b c'], expected: 'A B C' }
        ]
    },
  375: {
        functionNames: ['max_in_list', 'find_largest'],
        tests: [
            { args: [[12, 45, 7, 23, 56, 89, 34]], expected: 89 },
            { args: [[1, 2, 3]], expected: 3 }
        ]
    },
  376: {
        functionNames: ['reverse_string'],
        tests: [
            { args: ['hello'], expected: 'olleh' },
            { args: ['abc'], expected: 'cba' }
        ]
    },
  377: {
        functionNames: ['calculate_average'],
        compare: 'float',
        tests: [
            { args: [[10, 20, 30, 40]], expected: 25 },
            { args: [[1, 2, 3, 4, 5]], expected: 3 }
        ]
    },
  378: {
        functionNames: ['check_palindrome'],
        tests: [
            { args: ['racecar'], expected: true },
            { args: ['hello'], expected: false },
            { args: ['radar'], expected: true }
        ]
    },
  379: {
        functionNames: ['closest_to_zero'],
        tests: [
            { args: [[-5, 2, 3, -1, 0, -7]], expected: 0 },
            { args: [[-5, 2, 3]], expected: 2 }
        ]
    },
  380: {
        functionNames: ['check_sorted'],
        tests: [
            { args: [[1, 2, 3, 4]], expected: true },
            { args: [[1, 3, 2]], expected: false }
        ]
    },
  381: {
        functionNames: ['convert_to_integers'],
        tests: [
            { args: [['10', '20', '30', '40']], expected: [10, 20, 30, 40] },
            { args: [['1', '2']], expected: [1, 2] }
        ]
    },
  382: {
        functionNames: ['sort_strings_by_length'],
        tests: [
            { args: [['apple', 'fig', 'banana', 'kiwi']], expected: ['fig', 'kiwi', 'apple', 'banana'] },
            { args: [['a', 'abc', 'ab']], expected: ['a', 'ab', 'abc'] }
        ]
    },
  384: {
        functionNames: ['sort_tuples_by_second'],
        tests: [
            { args: [[[1, 3], [2, 1], [3, 2]]], expected: [[2, 1], [3, 2], [1, 3]] },
            { args: [[[1, 5], [2, 2]]], expected: [[2, 2], [1, 5]] }
        ]
    },
  385: {
        functionNames: ['sort_dicts_by_key'],
        tests: [
            { args: [[{name: 'Alice', age: 30}, {name: 'Bob', age: 25}], 'age'], expected: [{name: 'Bob', age: 25}, {name: 'Alice', age: 30}] },
            { args: [[{v: 3}, {v: 1}], 'v'], expected: [{v: 1}, {v: 3}] }
        ]
    },
  386: {
        functionNames: ['longest_word'],
        tests: [
            { args: [['apple', 'banana', 'cherry', 'date']], expected: 'banana' },
            { args: [['a', 'ab', 'abc']], expected: 'abc' }
        ]
    },
  387: {
        functionNames: ['sort_by_absolute_value'],
        tests: [
            { args: [[-2, -3, 1, 5, -4]], expected: [1, -2, -3, -4, 5] },
            { args: [[-1, 0, 1]], expected: [0, -1, 1] }
        ]
    },
  388: {
        functionNames: ['sort_strings_by_last_character', 'main'],
        tests: [
            { args: [['banana', 'apple', 'grape', 'kiwi']], expected: ['banana', 'apple', 'grape', 'kiwi'] },
            { args: [['treez', 'cliff', 'grassya']], expected: ['grassya', 'cliff', 'treez'] }
        ]
  },
  389: {
        functionNames: ['earliest_date'],
        tests: [
            { args: [['2023-10-01', '2024-01-15', '2022-12-31']], expected: '2022-12-31' },
            { args: [['2025-01-01', '2024-01-01']], expected: '2024-01-01' }
        ]
    },
  390: {
        functionNames: ['get_surname'],
        tests: [
            { args: ['John Doe'], expected: 'Doe' },
            { args: ['Jane Smith'], expected: 'Smith' }
        ]
    },
  391: {
        functionNames: ['sort_strings_alphabetically'],
        tests: [
            { args: [['banana', 'Apple', 'cherry', 'Date']], expected: ['Apple', 'banana', 'cherry', 'Date'] },
            { args: [['b', 'A']], expected: ['A', 'b'] }
        ]
    },
  392: {
        functionNames: ['find_highest_scrabble_word'],
        tests: [
            { args: [['hello', 'world', 'python', 'scrabble']], expected: 'python' },
            { args: [['a', 'zzzz']], expected: 'zzzz' }
        ]
    },
  393: {
        functionNames: ['sort_complex_numbers'],
        tests: [
            { args: [[3, 1, 2]], expected: [1, 2, 3] },
            { args: [[5, -1, 0]], expected: [0, -1, 5] }
        ]
    },
  394: {
        functionNames: ['find_largest_file'],
        tests: [
            { args: [["small.txt", "large.txt"]], setupFiles: { "small.txt": "small", "large.txt": "this is larger" }, expected: "large.txt" },
        ]
    },
  395: {
        functionNames: ['sort_fractions'],
        tests: [
            { args: [[0.5, 0.3333333333333333, 0.6666666666666666, 0.25]], expected: [0.25, 0.3333333333333333, 0.5, 0.6666666666666666] },
            { args: [[0.75, 0.125]], expected: [0.125, 0.75] }
        ]
    },
  396: {
        functionNames: ['sort_tuples_by_sum', 'main'],
        tests: [
            { args: [[[1, 2], [3, 4], [1, 1], [2, 2]]], expected: [[1, 1], [1, 2], [2, 2], [3, 4]] },
            { args: [[[1, 64], [7, 3], [2, 9]]], expected: [[7, 3], [2, 9], [1, 64]] }
        ]
    },
  397: {
        functionNames: ['closest_to_zero'],
        tests: [
            { args: [[-5, 2, 3, -1, 0, -7]], expected: 0 },
            { args: [[-3, 3, 1]], expected: 1 }
        ]
    },
  398: {
        functionNames: ['sort_points_by_distance'],
        tests: [
            { args: [[[3, 4], [1, 1], [0, 2], [5, 0]]], expected: [[1, 1], [0, 2], [3, 4], [5, 0]] },
            { args: [[[1, 1], [0, 0]]], expected: [[0, 0], [1, 1]] }
        ]
    },
  399: {
        functionNames: ['sort_words_by_distinct_letters'],
        tests: [
            { args: [['apple', 'banana', 'cherry', 'date']], expected: ['banana', 'apple', 'date', 'cherry'] },
            { args: [['a', 'ab', 'abc']], expected: ['a', 'ab', 'abc'] }
        ]
    },
  400: {
        functionNames: ['find_highest_ascii_word', 'main'],
        tests: [
            { args: [['hello', 'world', 'python', 'scrabble']], expected: 'scrabble' },
            { args: [['aa', 'bb', 'cc', 'uu']], expected: 'uu' }
        ]
    },
  401: {
        functionNames: ['sort_by_vowel_count'],
        tests: [
            { args: [['apple', 'banana', 'cherry', 'date', 'fig', 'grape']], expected: ['cherry', 'fig', 'apple', 'date', 'grape', 'banana'] },
            { args: [['a', 'e', 'i']], expected: ['a', 'e', 'i'] }
        ]
    },
  402: {
        functionNames: ['convert_to_integers'],
        tests: [
            { args: [[4, 24, 66, 25]], expected: ['4', '24', '66', '25'] },
            { args: [[1, 2]], expected: ['1', '2'] }
        ]
    },
  403: {
        functionNames: ['add_five'],
        tests: [
            { args: [[1, 2, 3, 4, 5]], expected: [6, 7, 8, 9, 10] },
            { args: [[0, -5]], expected: [5, 0] }
        ]
    },
  404: {
        functionNames: ['find_min', 'main'],
        tests: [
            { args: [[2, 6, 1, 189]], expected: 1 },
            { args: [[5, -3, 10]], expected: -3 }
        ]
    },
  405: {
        functionNames: ['converts'],
        compare: 'float',
        tests: [
            { args: [5], expected: 1.95 },
            { args: [0], expected: 0 }
        ]
    },
  406: {
        functionNames: ['reverse'],
        tests: [
            { args: [[1, 2, 3, 4]], expected: [4, 3, 2, 1] },
            { args: [['a', 'b', 'c']], expected: ['c', 'b', 'a'] }
        ]
    },
  407: {
        functionNames: ['calculate_average'],
        compare: 'float',
        tests: [
            { args: [[23, 56, 33]], expected: 37.333333333333336 },
            { args: [[10, 20]], expected: 15 }
        ]
    },
  408: {
        functionNames: ['remove_duplicates'],
        tests: [
            { args: ['what is you is going is to do'], expected: ['what', 'is', 'you', 'going', 'to', 'do'] },
            { args: ['a b a c'], expected: ['a', 'b', 'c'] }
        ]
    },
  409: {
        functionNames: ['len_words'],
        tests: [
            { args: [['Jonathan', 'Chris', 'Jeremy']], expected: {Jonathan: 8, Chris: 5, Jeremy: 6} },
            { args: [['a', 'ab']], expected: {a: 1, ab: 2} }
        ]
    },
  410: {
        functionNames: ['filter_string'],
        tests: [
            { args: [['jon', 'chris', 'tom', 'Jeremy']], expected: ['jon', 'tom'] },
            { args: [['a', 'ab', 'abc']], expected: ['abc'] }
        ]
    },
  411: {
        functionNames: ['calculate_sum'],
        tests: [
            { args: [7, 3], expected: 10 },
            { args: [5, 5], expected: 10 }
        ]
    },
  412: {
        functionNames: ['calculate_product'],
        tests: [
            { args: [3, 5], expected: 15 },
            { args: [10, 2], expected: 20 }
        ]
    },
  413: {
        functionNames: ['calculate_difference'],
        tests: [
            { args: [10, 3], expected: 7 },
            { args: [5, 8], expected: -3 }
        ]
    },
  414: {
        functionNames: ['calculate_quotient'],
        compare: 'float',
        tests: [
            { args: [10, 2], expected: 5 },
            { args: [9, 2], expected: 4.5 }
        ]
    },
  415: {
        functionNames: ['area_of_rectangle'],
        tests: [
            { args: [5, 4], expected: 20 },
            { args: [3, 7], expected: 21 }
        ]
    },
  416: {
        functionNames: ['perimeter_of_square'],
        tests: [
            { args: [5], expected: 20 },
            { args: [10], expected: 40 }
        ]
    },
  417: {
        functionNames: ['fahrenheit_to_celsius'],
        compare: 'float',
        tests: [
            { args: [68], expected: 20 },
            { args: [32], expected: 0 },
            { args: [212], expected: 100 }
        ]
    },
  418: {
        functionNames: ['celsius_to_fahrenheit'],
        compare: 'float',
        tests: [
            { args: [20], expected: 68 },
            { args: [0], expected: 32 },
            { args: [100], expected: 212 }
        ]
    },
  419: {
        functionNames: ['even_or_odd'],
        tests: [
            { args: [7], expected: 'Odd' },
            { args: [10], expected: 'Even' },
            { args: [0], expected: 'Even' }
        ]
    },
  420: {
        functionNames: ['is_prime'],
        tests: [
            { args: [29], expected: true },
            { args: [1], expected: false },
            { args: [4], expected: false }
        ]
    },
  421: {
        functionNames: ['list_sum'],
        tests: [
            { args: [[1, 2, 3, 4]], expected: 10 },
            { args: [[5, 10, 15]], expected: 30 }
        ]
    },
  422: {
        functionNames: ['list_product'],
        tests: [
            { args: [[1, 2, 3, 4]], expected: 24 },
            { args: [[2, 3, 5]], expected: 30 }
        ]
    },
  423: {
        functionNames: ['greater_than'],
        tests: [
            { args: [10, 5], expected: true },
            { args: [3, 7], expected: false },
            { args: [5, 5], expected: false }
        ]
    },
  424: {
        functionNames: ['string_length'],
        tests: [
            { args: ['Hello, World!'], expected: 13 },
            { args: ['abc'], expected: 3 }
        ]
    },
  425: {
        functionNames: ['first_and_last'],
        tests: [
            { args: ['Hello'], expected: ['H', 'o'] },
            { args: ['a'], expected: ['a', 'a'] }
        ]
    },
  426: {
        functionNames: ['count_vowels'],
        tests: [
            { args: ['Hello, World!'], expected: 3 },
            { args: ['Python'], expected: 1 }
        ]
    },
  427: {
        functionNames: ['reverse_string'],
        tests: [
            { args: ['Hello'], expected: 'olleH' },
            { args: ['abc'], expected: 'cba' }
        ]
    },
  428: {
        functionNames: ['is_palindrome'],
        tests: [
            { args: ['racecar'], expected: true },
            { args: ['hello'], expected: false }
        ]
    },
  429: {
        functionNames: ['multiply_by_n'],
        tests: [
            { args: [3], callReturnedWith: [5], expected: 15 },
            { args: [10], callReturnedWith: [2], expected: 20 }
        ]
    },
  430: {
        functionNames: ['add_tax'],
        compare: 'float',
        tests: [
            { args: [100], expected: 115 },
            { args: [200], expected: 230 }
        ]
    },
  431: {
        functionNames: ['greet_person'],
        tests: [
            { args: ['Alice'], expected: 'Hello, Alice!' },
            { args: ['Bob'], expected: 'Hello, Bob!' }
        ]
    },
  432: {
        functionNames: ['factorial'],
        tests: [
            { args: [5], expected: 120 },
            { args: [3], expected: 6 },
            { args: [0], expected: 1 }
        ]
    },
  433: {
        functionNames: ['exponent'],
        tests: [
            { args: [2, 3], expected: 8 },
            { args: [5, 0], expected: 1 }
        ]
    },
  434: {
        functionNames: ['gcd'],
        tests: [
            { args: [48, 18], expected: 6 },
            { args: [12, 8], expected: 4 }
        ]
    },
  435: {
        functionNames: ['lcm'],
        tests: [
            { args: [4, 5], expected: 20 },
            { args: [6, 8], expected: 24 }
        ]
    },
  436: {
        functionNames: ['square_of_number'],
        tests: [
            { args: [5], expected: 25 },
            { args: [0], expected: 0 },
            { args: [-3], expected: 9 }
        ]
    },
  437: {
        functionNames: ['cube_of_number'],
        tests: [
            { args: [3], expected: 27 },
            { args: [0], expected: 0 },
            { args: [-2], expected: -8 }
        ]
    },
  438: {
        functionNames: ['sort_list_descending'],
        tests: [
            { args: [[4, 1, 3, 2]], expected: [4, 3, 2, 1] },
            { args: [[1, 2, 3]], expected: [3, 2, 1] }
        ]
    },
  439: {
        functionNames: ['max_of_three'],
        tests: [
            { args: [10, 20, 15], expected: 20 },
            { args: [5, 3, 8], expected: 8 }
        ]
    },
  440: {
        functionNames: ['average_of_list'],
        compare: 'float',
        tests: [
            { args: [[10, 20, 30, 40]], expected: 25 },
            { args: [[1, 2, 3, 4, 5]], expected: 3 }
        ]
    },
  441: {
        functionNames: ['average_of_list'],
        compare: 'float',
        tests: [
            { args: [[5, 15, 25]], expected: 15 },
            { args: [[10, 20]], expected: 15 }
        ]
    },
  442: {
        functionNames: ['is_uppercase'],
        tests: [
            { args: ['HELLO'], expected: true },
            { args: ['Hello'], expected: false }
        ]
    },
  443: {
        functionNames: ['is_lowercase'],
        tests: [
            { args: ['hello'], expected: true },
            { args: ['Hello'], expected: false }
        ]
    },
  444: {
        functionNames: ['string_contains_digit'],
        tests: [
            { args: ['jonathan5'], expected: true },
            { args: ['hello'], expected: false }
        ]
    },
  445: {
        functionNames: ['string_contains_letter'],
        tests: [
            { args: ['123455g'], expected: true },
            { args: ['12345'], expected: false }
        ]
    },
  446: {
        functionNames: ['average_of_list'],
        compare: 'float',
        tests: [
            { args: [[1, 2, 3, 4, 5]], expected: 3 },
            { args: [[10, 20, 30]], expected: 20 }
        ]
    },
  447: {
        functionNames: ['check_multiple_of_n'],
        tests: [
            { args: [10, 5], expected: true },
            { args: [10, 3], expected: false }
        ]
    },
  448: {
        functionNames: ['longest_string'],
        tests: [
            { args: [['a', 'bb', 'ccc']], expected: 'ccc' },
            { args: [['hi', 'hello', 'hey']], expected: 'hello' }
        ]
    },
  449: {
        functionNames: ['shortest_string'],
        tests: [
            { args: [['a', 'bb', 'ccc']], expected: 'a' },
            { args: [['hi', 'hello', 'hey']], expected: 'hi' }
        ]
    },
  450: {
        functionNames: ['remove_duplicates'],
        tests: [
            { args: [[1, 2, 2, 3, 3, 4]], expected: [1, 2, 3, 4] },
            { args: [['a', 'b', 'a']], expected: ['a', 'b'] }
        ]
    },
  451: {
        functionNames: ['fibonacci'],
        tests: [
            { args: [5], expected: 5 },
            { args: [10], expected: 55 }
        ]
    },
  452: {
        functionNames: ['calculate_sum'],
        tests: [
            { args: [3, 5], expected: 8 },
            { args: [10, 20], expected: 30 }
        ]
    },
  453: {
        functionNames: ['calculate_integers'],
        tests: [
            { args: [10, 5], expected: [50, 15, 2] },
            { args: [6, 3], expected: [18, 9, 2] }
        ]
    },
  455: {
        functionNames: ['average_of_list'],
        compare: 'float',
        tests: [
            { args: [[10, 20, 30]], expected: 20 },
            { args: [[1, 2, 3, 4]], expected: 2.5 }
        ]
    },
  456: {
        functionNames: ['len_lst'],
        tests: [
            { args: [['apple', 'fig', 'banana', 'kiwi']], expected: ['fig', 'kiwi', 'apple', 'banana'] },
            { args: [['aa', 'b', 'cccc']], expected: ['b', 'aa', 'cccc'] }
        ]
    },
  457: {
        functionNames: ['min_len'],
        tests: [
            { args: [['apple', 'fig', 'banana']], expected: 'fig' },
            { args: [['long', 'to', 'a']], expected: 'a' }
        ]
    },
  458: {
        functionNames: ['max_string_alpha'],
        tests: [
            { args: [['apple', 'banana', 'cherry']], expected: 'cherry' },
            { args: [['zebra', 'yak', 'ant']], expected: 'zebra' }
        ]
    },
  459: {
        functionNames: ['sort_dicts_by_key'],
        tests: [
            { args: [[{name: 'Alice', age: 30}, {name: 'Bob', age: 25}], 'age'], expected: [{name: 'Bob', age: 25}, {name: 'Alice', age: 30}] },
            { args: [[{name: 'Charlie', age: 20}, {name: 'Alice', age: 30}], 'name'], expected: [{name: 'Alice', age: 30}, {name: 'Charlie', age: 20}] }
        ]
    },
  460: {
        functionNames: ['sort_by_absolute_value'],
        tests: [
            { args: [[-2, -3, 1, 5, -4]], expected: [1, -2, -3, -4, 5] },
            { args: [[10, -1, -7, 3]], expected: [-1, 3, -7, 10] }
        ]
    },
  461: {
        functionNames: ['sort_words_by_vowel_count'],
        tests: [
            { args: [['apple', 'banana', 'cherry', 'date']], expected: ['cherry', 'apple', 'date', 'banana'] },
            { args: [['sky', 'tree', 'audio']], expected: ['sky', 'tree', 'audio'] }
        ]
    },
  462: {
        functionNames: ['longest_word'],
        tests: [
            { args: [['apple', 'banana', 'cherry']], expected: 'banana' },
            { args: [['a', 'alphabet', 'tool']], expected: 'alphabet' }
        ]
    },
  463: {
        functionNames: ['sum_of_tuple'],
        tests: [
            { args: [[[1, 2], [3, 4], [1, 1], [2, 2]]], expected: [[1, 1], [1, 2], [2, 2], [3, 4]] },
            { args: [[[5, 5], [1, 1], [3, 0]]], expected: [[1, 1], [3, 0], [5, 5]] }
        ]
    },
  464: {
        functionNames: ['list_of_strings_lst'],
        tests: [
            { args: [['banana', 'apple', 'grape', 'kiwi']], expected: ['banana', 'apple', 'grape', 'kiwi'] },
            { args: [['ab', 'aa', 'ac']], expected: ['aa', 'ab', 'ac'] }
        ]
    },
  465: {
        functionNames: ['sort_number_uppercases'],
        tests: [
            { args: [['Hello', 'World', 'PYTHON', 'code']], expected: ['code', 'Hello', 'World', 'PYTHON'] },
            { args: [['ABC', 'aB', 'plain']], expected: ['plain', 'aB', 'ABC'] }
        ]
    },
  466: {
        functionNames: ['tuple_largest_product'],
        tests: [
            { args: [[[1, 2], [3, 4], [5, 6]]], expected: [5, 6] },
            { args: [[[2, 2, 2], [3, 3], [1, 10]]], expected: [1, 10] }
        ]
    },
  467: {
        functionNames: ['floating_point'],
        tests: [
            { args: [[3.5, 2.1, 4.8, 1.3]], expected: [1.3, 2.1, 3.5, 4.8] },
            { args: [[2.6, 1.2, 3.8]], expected: [1.2, 2.6, 3.8] }
        ]
    },
  468: {
        functionNames: ['first_element_decending_order'],
        tests: [
            { args: [[[3, 1], [1, 2], [2, 3]]], expected: [[3, 1], [2, 3], [1, 2]] },
            { args: [[[10, 'a'], [5, 'b'], [20, 'c']]], expected: [[20, 'c'], [10, 'a'], [5, 'b']] }
        ]
    },
  469: {
        functionNames: ['number_of_consonants'],
        tests: [
            { args: [['hello', 'world', 'python']], expected: ['hello', 'world', 'python'] },
            { args: [['ai', 'cat', 'strength']], expected: ['ai', 'cat', 'strength'] }
        ]
    },
  470: {
        functionNames: ['min_string'],
        tests: [
            { args: [['apple', 'fig', 'banana']], expected: 'fig' }
        ]
    },
  471: {
        functionNames: ['length_of_value'],
        tests: [
            { args: [[{name: 'Alice'}, {name: 'Bob'}, {name: 'Jonathan'}], 'name'], expected: [{name: 'Bob'}, {name: 'Alice'}, {name: 'Jonathan'}] }
        ]
    },
  472: {
        functionNames: ['find_person'],
        tests: [
            { args: [[{name: 'Beth'}, {name: 'Brett'}, {name: 'Jhonivan'}, {name: 'Jonathan'}], 'name'], expected: {name: 'Jhonivan'} },
            { args: [[{name: 'Ann'}, {name: 'Christopher'}], 'name'], expected: {name: 'Christopher'} }
        ]
    },
  473: {
    functionNames: ["main"],
    tests: [{
      args: [[1, 2, 3, 4, 5], 2],
      expected: [2, 4, 1, 3, 5]
    }]
  },
  474: {
        functionNames: ['sort_by_year'],
        tests: [
            { args: [['2023-10-01', '2020-01-15', '2025-12-31']], expected: ['2020-01-15', '2023-10-01', '2025-12-31'] }
        ]
    },
  475: {
        functionNames: ['sort_by_a_count'],
        tests: [
            { args: [['apple', 'banana', 'cherry', 'date']], expected: ['cherry', 'apple', 'date', 'banana'] }
        ]
    },
  476: {
        functionNames: ['sort_sqaure'],
        tests: [
            { args: [[-2, 3, -1, 2]], expected: [-1, -2, 2, 3] }
        ]
    },
  477: {
        functionNames: ['closest_to_target'],
        tests: [
            { args: [[10, 20, 30, 40], 25], expected: 20 },
            { args: [[1, 5, 10], 6], expected: 5 }
        ]
    },
  478: {
        functionNames: ['length_of_first_element'],
        tests: [
            { args: [[['apple', 1], ['banana', 2], ['fig', 3]]], expected: [['fig', 3], ['apple', 1], ['banana', 2]] }
        ]
    },
  479: {
        functionNames: ['number_of_spaces'],
        tests: [
            { args: [['hello world', 'a b c', 'nospace']], expected: ['nospace', 'hello world', 'a b c'] }
        ]
    },
  480: {
        functionNames: ['most_vowels'],
        tests: [
            { args: [['apple', 'banana', 'cherry', 'date']], expected: 'banana' }
        ]
    },
  481: {
        functionNames: ['sort_lst_integers'],
        tests: [
            { args: [[100, 5, 50, 2, 1000]], expected: [5, 2, 50, 100, 1000] }
        ]
    },
  482: {
        functionNames: ['sort_tuples_by_difference'],
        tests: [
            { args: [[[1, 5], [3, 4], [10, 2]]], expected: [[3, 4], [1, 5], [10, 2]] }
        ]
    },
  483: {
        functionNames: ['sort_strings_by_ascii'],
        tests: [
            { args: [['banana', 'Apple', 'cherry']], expected: ['Apple', 'banana', 'cherry'] }
        ]
    },
  484: {
        functionNames: ['sort_lists_by_sum'],
        tests: [
            { args: [[[1, 2], [3, 4], [1, 1]]], expected: [[1, 1], [1, 2], [3, 4]] }
        ]
    },
  485: {
        functionNames: ['number_of_consonants'],
        tests: [
            { args: [['apple', 'banana', 'cherry', 'date']], expected: 'date' }
        ]
    },
  486: {
        functionNames: ['sort_files_by_extension'],
        tests: [
            { args: [['file.txt', 'image.jpg', 'doc.pdf', 'script.py']], expected: ['image.jpg', 'doc.pdf', 'script.py', 'file.txt'] }
        ]
    },
  487: {
        functionNames: ['sqaure_numbers_lst'],
        tests: [
            { args: [[4, 9, 1, 16]], expected: [1, 4, 9, 16] }
        ]
    },
  488: {
        functionNames: ['sort_words_by_distinct_letters'],
        tests: [
            { args: [['apple', 'banana', 'cherry', 'date']], expected: ['banana', 'apple', 'date', 'cherry'] }
        ]
    },
  489: {
        functionNames: ['sort_second_letter'],
        tests: [
            { args: [['banana', 'apple', 'cherry', 'date']], expected: ['banana', 'date', 'cherry', 'apple'] }
        ]
    },
  490: {
        functionNames: ['people_age'],
        tests: [
            { args: [[{name: 'Alice', age: 30}, {name: 'Bob', age: 25}, {name: 'Charlie', age: 35}]], expected: [{name: 'Bob', age: 25}, {name: 'Alice', age: 30}, {name: 'Charlie', age: 35}] }
        ]
    },
  491: {
        functionNames: ['sort_by_binary_representation'],
        tests: [
            { args: [[3, 2, 1, 4]], expected: [1, 2, 4, 3] }
        ]
    },
  492: {
        functionNames: ['sort_keys_by_value'],
        tests: [
            { args: [{Sam: 27, Tommy: 56, Chantelle: 18}], expected: ['Chantelle', 'Sam', 'Tommy'] },
            { args: [{a: 3, b: 1, c: 2}], expected: ['b', 'c', 'a'] }
        ]
    },
  493: {
        functionNames: ['sort_fractions_by_decimal'],
        tests: [
            { args: [[3, 7, 1, 5]], expected: [1, 3, 5, 7] }
        ]
    },
  494: {
        functionNames: ['longest_string_letter'],
        tests: [
            { args: [['apple', 'grape', 'date', 'cherry'], 'e'], expected: 'apple' }
        ]
    },
  495: {
        functionNames: ['Dog', 'Cat'],
        tests: [
            { args: [], functionName: 'Dog', callMethod: 'speak', expected: 'Bark' },
            { args: [], functionName: 'Cat', callMethod: 'speak', expected: 'Meow' }
        ]
    },
  496: {
        functionNames: ['Car'],
        tests: [
            { args: [120, 'Red', 'Toyota'], getAttrs: ['speed', 'color', 'model'], expected: {speed: 120, color: 'Red', model: 'Toyota'} },
            { args: [80, 'Blue', 'Honda'], getAttrs: ['speed', 'color', 'model'], expected: {speed: 80, color: 'Blue', model: 'Honda'} }
        ]
    },
  497: {
        functionNames: ['Person', 'Student'],
        tests: [
            { args: ['Alice'], functionName: 'Person', callMethod: 'introduce', expected: 'Hello, my name is Alice.' },
            { args: ['Bob', 10], functionName: 'Student', callMethod: 'introduce', expected: 'Hello, my name is Bob and I am in grade 10.' }
        ]
    },
  498: {
        functionNames: ['Rectangle'],
        tests: [
            { args: [5, 3], callMethod: 'area', expected: 15 },
            { args: [4, 7], callMethod: 'area', expected: 28 }
        ]
    },
  499: {
        functionNames: ['WashingMachine'],
        tests: [
            { args: ['LG', 1500], callMethod: 'wash_clothes', expected: 'The LG washing machine is washing clothes with 1500 watts of power.' },
            { args: ['Samsung', 1200], callMethod: 'wash_clothes', expected: 'The Samsung washing machine is washing clothes with 1200 watts of power.' }
        ]
    },
  500: {
        functionNames: ['Manager'],
        tests: [
            { args: ['John Doe', 75000], callMethod: 'assign_task', callMethodArgs: ['Prepare a project report'], expected: 'Manager John Doe has assigned the task: Prepare a project report.' },
            { args: ['Ada', 90000], callMethod: 'assign_task', callMethodArgs: ['Review code'], expected: 'Manager Ada has assigned the task: Review code.' }
        ]
    },
  501: {
        functionNames: ['Penguin', 'Bird'],
        tests: [
            { args: [], functionName: 'Penguin', callMethod: 'fly', expected: 'Cannot fly' },
            { args: [], functionName: 'Bird', callMethod: 'fly', expected: 'I can fly!' }
        ]
    },
  502: {
        functionNames: ['EBook'],
        tests: [
            { args: ['Python Programming', 'John Doe', 2.5], getAttrs: ['title', 'author', 'file_size'], expected: {title: 'Python Programming', author: 'John Doe', file_size: 2.5} }
        ]
    },
  503: {
        functionNames: ['Guitar', 'Instrument'],
        tests: [
            { args: [], functionName: 'Guitar', callMethod: 'play', expected: 'Strum' },
            { args: [], functionName: 'Instrument', callMethod: 'play', expected: 'Playing an instrument.' }
        ]
    },
  504: {
        functionNames: ['Chess', 'Game'],
        tests: [
            { args: [], functionName: 'Chess', callMethod: 'start', expected: 'Start Chess' },
            { args: [], functionName: 'Game', callMethod: 'start', expected: 'Starting the game.' }
        ]
    },
  505: {
        functionNames: ['Bicycle'],
        tests: [
            { args: [], callMethod: 'drive', expected: 'Pedal' }
        ]
    },
  506: {
        functionNames: ['Laptop'],
        tests: [
            { args: ['Dell', 'Intel i7', 2.3], getAttrs: ['brand', 'processor', 'weight'], expected: {brand: 'Dell', processor: 'Intel i7', weight: 2.3} }
        ]
    },
  507: {
        functionNames: ['Smartphone'],
        tests: [
            { args: [['WhatsApp', 'Instagram']], callMethod: 'turn_on', expected: 'Device is now on.' },
            { args: [['WhatsApp', 'Instagram']], getAttrs: ['apps'], expected: {apps: ['WhatsApp', 'Instagram']} }
        ]
    },
  508: {
        functionNames: ['Child', 'Parent'],
        tests: [
            { args: [], functionName: 'Child', callMethod: 'display', expected: 'This is a child' },
            { args: [], functionName: 'Parent', callMethod: 'display', expected: 'This is the parent.' }
        ]
    },
  509: {
        functionNames: ['Skyscraper'],
        tests: [
            { args: [50, '123 High Street', 200], getAttrs: ['floors', 'address', 'height'], expected: {floors: 50, address: '123 High Street', height: 200} }
        ]
    },
  510: {
        functionNames: ['Flower', 'Plant'],
        tests: [
            { args: [], functionName: 'Flower', callMethod: 'grow', expected: 'Bloom' },
            { args: [], functionName: 'Plant', callMethod: 'grow', expected: 'The plant is growing.' }
        ]
    },
  511: {
        functionNames: ['MathTeacher'],
        tests: [
            { args: ['Alice Smith'], getAttrs: ['name', 'subject'], expected: {name: 'Alice Smith', subject: 'Math'} },
            { args: ['Alice Smith'], callMethod: 'teach_math', expected: 'Teaching math concepts.' }
        ]
    },
  512: {
        functionNames: ['Poet'],
        tests: [
            { args: ['William Wordsworth'], getAttrs: ['name', 'genre'], expected: {name: 'William Wordsworth', genre: 'Poetry'} }
        ]
    },
  513: {
        functionNames: ['Oven', 'Appliance'],
        tests: [
            { args: [], functionName: 'Oven', callMethod: 'use', expected: 'Bake' },
            { args: [], functionName: 'Appliance', callMethod: 'use', expected: 'Using the appliance.' }
        ]
    },
  514: {
        functionNames: ['Painter'],
        tests: [
            { args: ['Vincent van Gogh', 'Oil Paint'], callMethod: 'paint', expected: 'Painting with Oil Paint' }
        ]
    },
  515: {
        functionNames: ['Electrician'],
        tests: [
            { args: [], callMethod: 'work', expected: 'Fix wires' }
        ]
    },
  516: {
        functionNames: ['Lion'],
        tests: [
            { args: [], callMethod: 'eat', expected: 'Eat meat' }
        ]
    },
  517: {
        functionNames: ['Fan'],
        tests: [
            { args: [], callMethod: 'run', expected: 'Spin blades' }
        ]
    },
  518: {
        functionNames: ['Intern', 'Employee'],
        tests: [
            { args: [], functionName: 'Intern', callMethod: 'get_salary', expected: 2000 },
            { args: [], functionName: 'Employee', callMethod: 'get_salary', expected: 5000 }
        ]
    },
  519: {
        functionNames: ['Motorcycle'],
        tests: [
            { args: [], getAttrs: ['wheels'], expected: {wheels: 2} }
        ]
    },
  520: {
        functionNames: ['Hammer'],
        tests: [
            { args: [], callMethod: 'use', expected: 'Hammer nails' }
        ]
    },
  521: {
        functionNames: ['SavingsAccount'],
        tests: [
            { args: [1500, 'Bob', 2.5], getAttrs: ['balance', 'owner', 'interest_rate'], expected: {balance: 1500, owner: 'Bob', interest_rate: 2.5} }
        ]
    },
  522: {
        functionNames: ['Sword'],
        tests: [
            { args: [], callMethod: 'attack', expected: 'Slash' }
        ]
    },
  523: {
        functionNames: ['Microwave'],
        tests: [
            { args: [1200], getAttrs: ['power'], expected: {power: 1200} },
            { args: [1200], callMethod: 'heat_food', expected: 'Heating food' }
        ]
    },
  524: {
        functionNames: ['ElectricCar'],
        tests: [
            { args: [], callMethod: 'start', expected: 'Silent start' }
        ]
    },
  525: {
        functionNames: ['Cat'],
        tests: [
            { args: [], callMethod: 'make_sound', expected: 'Meow' }
        ]
    },
  526: {
        functionNames: ['PastryChef'],
        tests: [
            { args: [], callMethod: 'cook', expected: 'Bake cake' }
        ]
    },
  527: {
        functionNames: ['create_chair'],
        tests: [
            { args: ['wood', 'brown', 4], getAttrs: ['material', 'color', 'legs'], expected: {material: 'wood', color: 'brown', legs: 4} }
        ]
    },
  528: {
        functionNames: ['Soccer'],
        tests: [
            { args: [], getAttrs: ['players'], expected: {players: 22} }
        ]
    },
  529: {
        functionNames: ['Pianist'],
        tests: [
            { args: [], callMethod: 'play_instrument', expected: 'Play piano' }
        ]
    },
  530: {
        functionNames: ['TechCompany'],
        tests: [
            { args: ['Tech Innovators', 'San Francisco', ['Smartphone', 'Laptop']], getAttrs: ['name', 'location', 'products'], expected: {name: 'Tech Innovators', location: 'San Francisco', products: ['Smartphone', 'Laptop']} }
        ]
    },
  531: {
        functionNames: ['Smartwatch'],
        tests: [
            { args: [true], callMethod: 'operate', expected: 'Operate gadget' },
            { args: [true], getAttrs: ['heart_rate_monitor'], expected: {heart_rate_monitor: true} }
        ]
    },
  532: {
        functionNames: ['FitnessTrainer'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], callMethod: 'train', expected: 'Train body' }
        ]
    },
  533: {
        functionNames: ['ComicBook'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], callMethod: 'read', expected: 'Read with pictures' }
        ]
    },
  534: {
        functionNames: ['GameSoftware'],
        tests: [
            { args: ['EpicQuest', '2.5', 'RPG'], getAttrs: ['name', 'version', 'genre'], expected: {name: 'EpicQuest', version: '2.5', genre: 'RPG'} }
        ]
    },
  535: {
        functionNames: ['count_letter'],
        tests: [
            { args: ['banana'], expected: 3 },
            { args: ['apple'], expected: 1 }
        ]
    },
  536: {
        functionNames: ['count_number'],
        tests: [
            { args: [[1, 5, 2, 5, 3, 5]], expected: 3 },
            { args: [[1, 2, 3]], expected: 0 }
        ]
    },
  537: {
        functionNames: ['count_hello'],
        tests: [
            { args: ['hello world hello hello'], expected: 3 },
            { args: ['hello'], expected: 1 }
        ]
    },
  538: {
        functionNames: ['count'],
        tests: [
            { args: ['a#b#c#d'], expected: 3 },
            { args: ['abc'], expected: 0 }
        ]
    },
  539: {
        functionNames: ['count_substring'],
        tests: [
            { args: ['the cat sat on the mat cat'], expected: 2 },
            { args: ['dog dog dog'], expected: 0 }
        ]
    },
  540: {
        functionNames: ['count_number'],
        tests: [
            { args: [[0, 1, 0, 2, 0]], expected: 3 },
            { args: [[1, 2, 3]], expected: 0 }
        ]
    },
  541: {
        functionNames: ['count_spaces'],
        tests: [
            { args: ['hello world python'], expected: 2 },
            { args: ['nospaces'], expected: 0 }
        ]
    },
  542: {
        functionNames: ['count_occurrences'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], inputValues: ["banana", "a"], expected: "The character 'a' occurs 3 times." },
            { args: [], inputValues: ["banana", "aa"], expected: "Please enter exactly one character." },
        ]
    },
  543: {
        functionNames: ['count_word_in_file'],
        tests: [
            { args: ['test.txt', 'python'], expected: 0 }
        ]
    },
  544: {
        functionNames: ['count_letters'],
        tests: [
            { args: [['hello', 'world', 'python']], expected: 1 }
        ]
    },
  545: {
        functionNames: ['count_elements_in_lst'],
        tests: [
            { args: [[1, 'a', 2, 'a', 3], 'a'], expected: 2 }
        ]
    },
  546: {
        functionNames: ['count_test_occurrences'],
        tests: [
            { args: ['test test test testing'], expected: 4 }
        ]
    },
  547: {
        functionNames: ['count_floating_numbers'],
        tests: [
            { args: [[1.5, 2.0, 1.5, 3.5], 1.5], expected: 2 }
        ]
    },
  548: {
        functionNames: ['count_floating_numbers'],
        tests: [
            { args: [[2.3, 5.0, 6.3, 78.0, 0.6, 5.0], 5.0], expected: 2 }
        ]
    },
  549: {
        functionNames: ['count_uppercase'],
        tests: [
            { args: ['Hello World PYTHON'], expected: 8 }
        ]
    },
  550: {
        functionNames: ['count_digit'],
        tests: [
            { args: [12345, 3], expected: 1 },
            { args: [11111, 1], expected: 5 }
        ]
    },
  551: {
        functionNames: ['count_letters'],
        tests: [
            { args: ['banana'], expected: {b: 1, a: 3, n: 2} },
            { args: ['AaB'], expected: {a: 2, b: 1} }
        ]
    },
  552: {
        functionNames: ['count_text'],
        tests: [
            { args: ['Python is great. Python is fun.'], expected: 2 }
        ]
    },
  553: {
        functionNames: ['count_item_in_dict_list'],
        tests: [
            { args: [[{a: 1}, {a: 2}, {a: 1}], {a: 1}], expected: 2 }
        ]
    },
  554: {
        functionNames: ['count_letters'],
        tests: [
            { args: [['zebra', 'pizza', 'hello']], expected: 3 }
        ]
    },
  555: {
        functionNames: ['count_asterisks'],
        tests: [
            { args: ['a*b*c*d'], expected: 3 },
            { args: ['hello'], expected: 0 }
        ]
    },
  556: {
        functionNames: ['count_substring'],
        tests: [
            { args: ['123 456 123 789', '123'], expected: 2 }
        ]
    },
  557: {
        functionNames: ['count_lines_with_word'],
        tests: [
            { args: ['test.txt', 'error'], setupFiles: { 'test.txt': 'ok\nerror one\nERROR two\nfine' }, expected: 2 }
        ]
    },
  558: {
        functionNames: ['count_email_domain'],
        tests: [
            { args: [['a@gmail.com', 'b@yahoo.com', 'c@gmail.com'], 'gmail.com'], expected: 2 }
        ]
    },
  559: {
        functionNames: ['count_word'],
        tests: [
            { args: [['I am happy', 'happy birthday', 'sad day']], expected: 2 }
        ]
    },
  560: {
        functionNames: ['count_exclamations'],
        tests: [
            { args: [['hello!', 'world!!', 'python']], expected: 3 }
        ]
    },
  561: {
        functionNames: ['count_phrase_occurrences'],
        tests: [
            { args: ['the cat and the dog and the bird', 'the'], expected: 3 }
        ]
    },
  562: {
        functionNames: ['count_word_occurrences'],
        tests: [
            { args: [['the', 'cat', 'the', 'dog'], 'the'], expected: 2 }
        ]
    },
  563: {
        functionNames: ['count_x_in_mixed_list'],
        tests: [
            { args: [[1, 'x', 2, 'x', 3]], expected: 2 }
        ]
    },
  564: {
        functionNames: ['count_letter_occurrences'],
        tests: [
            { args: ['hello', 'l'], expected: "The letter 'l' appears 2 times in the given string." }
        ]
    },
  565: {
        functionNames: ['square_lst'],
        tests: [
            { args: [[1, 2, 3, 4, 5]], expected: [1, 4, 9, 16, 25] }
        ]
    },
  566: {
        functionNames: ['filter_odd_numbers'],
        tests: [
            { args: [[1, 2, 3, 4, 5, 6]], expected: [1, 3, 5] }
        ]
    },
  567: {
        functionNames: ['filters_even_numbers'],
        tests: [
            { args: [[1, 2, 3, 4, 5, 6]], expected: [2, 4, 6] }
        ]
    },
  568: {
        functionNames: ['convert_to_uppercase'],
        tests: [
            { args: [['hello', 'world']], expected: ['HELLO', 'WORLD'] }
        ]
    },
  569: {
        functionNames: ['empty_strings'],
        tests: [
            { args: [['a', '', 'b', '', 'c']], expected: ['a', 'b', 'c'] }
        ]
    },
  570: {
        functionNames: ['multiply_lst'],
        tests: [
            { args: [[1, 2, 3]], expected: [5, 10, 15] }
        ]
    },
  571: {
        functionNames: ['lst_of_string'],
        tests: [
            { args: [['hi', 'hello', 'hey']], expected: [2, 5, 3] }
        ]
    },
  572: {
        functionNames: ['palindromes'],
        tests: [
            { args: [['radar', 'hello', 'level', 'world']], expected: ['radar', 'level'] }
        ]
    },
  573: {
        functionNames: ['sum_of_lst'],
        tests: [
            { args: [[1, 2, 3, 4, 5]], expected: 15 }
        ]
    },
  574: {
        functionNames: ['sum_of_lst'],
        tests: [
            { args: [[1, 2, 3, 4]], expected: 24 }
        ]
    },
  575: {
        functionNames: ['capitalize_string'],
        tests: [
            { args: [['hello', 'world']], expected: ['Hello', 'World'] }
        ]
    },
  576: {
        functionNames: ['number_lst', 'min_number'],
        tests: [
            { args: [[3, 1, 4, 1, 5]], expected: 1 }
        ]
    },
  577: {
        functionNames: ['find_max'],
        tests: [
            { args: [[3, 1, 4, 1, 5]], expected: 5 }
        ]
    },
  578: {
        functionNames: ['list_words'],
        tests: [
            { args: [['a', 'ab', 'abc', 'abcd', 'abcde']], expected: ['abcd', 'abcde'] }
        ]
    },
  579: {
        functionNames: ['lst_strings'],
        tests: [
            { args: [['hello', ' ', 'world']], expected: 'hello world' }
        ]
    },
  580: {
        functionNames: ['num_lst'],
        tests: [
            { args: [[-1, 0, 1, -2, 2]], expected: [1, 2] }
        ]
    },
  581: {
        functionNames: ['num_lst'],
        tests: [
            { args: [[1, 2, 3]], expected: [1, 8, 27] }
        ]
    },
  582: {
        functionNames: ['lst_numbers'],
        tests: [
            { args: [[1, 2, 3]], expected: 14 }
        ]
    },
  583: {
        functionNames: ['lst_2'],
        tests: [
            { args: [['John', 'Jane'], ['Doe', 'Smith']], expected: ['John Doe', 'Jane Smith'] }
        ]
    },
  584: {
        functionNames: ['non_alphabetical_string'],
        tests: [
            { args: [['hello', 'world', 'abc123', 'python']], expected: ['hello', 'world', 'python'] }
        ]
    },
  585: {
        functionNames: ['lst_words'],
        tests: [
            { args: [['a', 'b', 'a', 'c', 'b', 'a']], expected: {a: 3, b: 2, c: 1} }
        ]
    },
  586: {
        functionNames: ['unique_words'],
        tests: [
            { args: [['a', 'b', 'a', 'c', 'b']], expected: ['a', 'b', 'c'] }
        ]
    },
  587: {
        functionNames: ['word_lst'],
        tests: [
            { args: [['a', 'ab', 'abc', 'abcd'], 3], expected: ['abcd'] }
        ]
    },
  588: {
        functionNames: ['apply_lsts'],
        tests: [
            { args: [[1, 2, 3, 4, 5]], expected: [1, 9, 25] }
        ]
    },
  589: {
        functionNames: ['sum_nested_list'],
        tests: [
            { args: [[[1, 2], [3, 4], [5]]], expected: 15 }
        ]
    },
  590: {
        functionNames: ['fibonacci_n_numbers'],
        tests: [
            { args: [6], expected: [0, 1, 1, 2, 3, 5] }
        ]
    },
  591: {
        functionNames: ['lst_string'],
        tests: [
            { args: [['hello', 'world', 'python']], expected: [2, 1, 1] }
        ]
    },
  592: {
        functionNames: ['sum_even_numbers'],
        tests: [
            { args: [[1, 2, 3, 4, 5, 6]], expected: 12 }
        ]
    },
  593: {
        functionNames: ['lst_string'],
        tests: [
            { args: [['a', 'ab', 'abc']], expected: 'abc' }
        ]
    },
  594: {
        functionNames: ['lst_num'],
        tests: [
            { args: [[1, 2, 3, 4]], expected: [1, 3, 6, 10] }
        ]
    },
  595: {
        functionNames: ['flatten'],
        tests: [
            { args: [[[1, 2], [3, 4], [5]]], expected: [1, 2, 3, 4, 5] }
        ]
    },
  596: {
        functionNames: ['lst_words'],
        tests: [
            { args: [['a', 'b', 'a', 'c']], expected: {a: 2, b: 1, c: 1} }
        ]
    },
  597: {
        functionNames: ['lst_words'],
        tests: [
            { args: [['listen', 'silent', 'hello', 'world'], 'listen'], expected: ['hello', 'world'] }
        ]
    },
  598: {
        functionNames: ['compose'],
        tests: [
            { args: [], argFunctionNames: ['add_one', 'multiply_by_two'], callReturnedWith: [5], expected: 12 },
            { args: [], argFunctionNames: ['multiply_by_two', 'add_one'], callReturnedWith: [5], expected: 11 }
        ]
    },
  599: {
        functionNames: ['word_string'],
        tests: [
            { args: [['a', 'bb', 'ccc', 'dd']], expected: {1: ['a'], 2: ['bb', 'dd'], 3: ['ccc']} }
        ]
    },
  600: {
        functionNames: ['filter_primes'],
        tests: [
            { args: [[1, 2, 3, 4, 5, 6, 7]], expected: [2, 3, 5, 7] },
            { args: [[8, 9, 10, 11, 12, 13]], expected: [11, 13] }
        ]
    },
  601: {
        functionNames: ['map_with_index'],
        tests: [
            { args: [[10, 20, 30, 40]], argFunctionNames: ['example_func'], expected: [0, 20, 60, 120] }
        ]
    },
  602: {
        functionNames: ['intersection'],
        tests: [
            { args: [[1, 2, 3, 4], [3, 4, 5, 6]], expected: [3, 4] }
        ]
    },
  603: {
        functionNames: ['average'],
        compare: 'float',
        tests: [
            { args: [[1, 2, 3, 4, 5]], expected: 3 },
            { args: [[]], expected: 0 }
        ]
    },
  604: {
        functionNames: ['compose_functions'],
        tests: [
            { args: [5], functionListArgNames: ['add_one', 'multiply_by_two', 'add_one'], expected: 13 },
            { args: [3], functionListArgNames: ['multiply_by_two', 'add_one'], expected: 7 }
        ]
    },
  605: {
        functionNames: ['get_keys'],
        tests: [
            { args: [{a: 1, b: 2, c: 3}], expected: ['a', 'b', 'c'] }
        ]
    },
  606: {
        functionNames: ['sort_string_len'],
        tests: [
            { args: [['apple', 'fig', 'banana', 'kiwi']], expected: ['fig', 'kiwi', 'apple', 'banana'] }
        ]
    },
  607: {
        functionNames: ['lst_tuples_second'],
        tests: [
            { args: [[[1, 3], [2, 1], [3, 2]]], expected: [[2, 1], [3, 2], [1, 3]] }
        ]
    },
  608: {
        functionNames: ['sort_dicts_by_key'],
        tests: [
            { args: [[{name: 'Alice', age: 30}, {name: 'Bob', age: 25}], 'age'], expected: [{name: 'Bob', age: 25}, {name: 'Alice', age: 30}] }
        ]
    },
  609: {
        functionNames: ['sort_last_names'],
        tests: [
            { args: [['John Doe', 'Jane Smith', 'Alice Johnson']], expected: ['John Doe', 'Alice Johnson', 'Jane Smith'] }
        ]
    },
  610: {
        functionNames: ['sort_ignore_case'],
        tests: [
            { args: [['banana', 'Apple', 'cherry', 'Date']], expected: ['Apple', 'banana', 'cherry', 'Date'] }
        ]
    },
  611: {
        functionNames: ['list_floats'],
        tests: [
            { args: [[3.5, 1.2, 2.8, 4.1]], expected: [4.1, 3.5, 2.8, 1.2] }
        ]
    },
  612: {
        functionNames: ['lst_words'],
        tests: [
            { args: [['apple', 'banana', 'cherry', 'date']], expected: ['cherry', 'apple', 'date', 'banana'] }
        ]
    },
  613: {
        functionNames: ['sort_people_by_age'],
        tests: [
            { args: [[{name: 'Alice', age: 30}, {name: 'Bob', age: 25}]], expected: [{name: 'Bob', age: 25}, {name: 'Alice', age: 30}] }
        ]
    },
  614: {
        functionNames: ['lst_integers'],
        tests: [
            { args: [[123, 45, 7, 89, 100]], expected: [100, 123, 7, 45, 89] },
            { args: [[5666, 566, 56, 6]], expected: [6, 56, 566, 5666] }
        ]
    },
  615: {
        functionNames: ['lst_products'],
        tests: [
            { args: [[{name: 'A', price: 10}, {name: 'B', price: 5}]], expected: [{name: 'B', price: 5}, {name: 'A', price: 10}] }
        ]
    },
  616: {
        functionNames: ['sort_dates'],
        tests: [
            { args: [['2023-01-01', '2021-01-01', '2022-01-01']], expected: ['2021-01-01', '2022-01-01', '2023-01-01'] }
        ]
    },
  617: {
        functionNames: ['lst_tuples'],
        tests: [
            { args: [[[1, 3], [1, 2], [2, 1]]], expected: [[1, 2], [1, 3], [2, 1]] }
        ]
    },
  618: {
        functionNames: ['lst_names'],
        tests: [
            { args: [['Alice', 'Bob', 'Jonathan']], expected: ['Bob', 'Alice', 'Jonathan'] }
        ]
    },
  619: {
        functionNames: ['sort_by_hire_date'],
        tests: [
            { args: [[['Alice', '2020-05-15'], ['Bob', '2019-03-22'], ['Charlie', '2021-07-30']]], expected: [['Bob', '2019-03-22'], ['Alice', '2020-05-15'], ['Charlie', '2021-07-30']] }
        ]
    },
  620: {
        functionNames: ['lst_of_sentences'],
        tests: [
            { args: [['a b c', 'a b', 'a']], expected: ['a', 'a b', 'a b c'] }
        ]
    },
  621: {
        functionNames: ['frequency_first_letter'],
        tests: [
            { args: [['apple', 'banana', 'avocado', 'cherry']], expected: ['banana', 'cherry', 'apple', 'avocado'] }
        ]
    },
  622: {
        functionNames: ['lst_of_tuples'],
        tests: [
            { args: [[[-3, 1], [1, 2], [-2, 3]]], expected: [[1, 2], [-2, 3], [-3, 1]] }
        ]
    },
  623: {
        functionNames: ['reverse_order'],
        tests: [
            { args: [['cat', 'dog', 'bird']], expected: ['dog', 'cat', 'bird'] }
        ]
    },
  624: {
        functionNames: ['temperture'],
        tests: [
            { args: [[0, 100, 50, 20]], expected: [0, 20, 50, 100] }
        ]
    },
  625: {
        functionNames: ['sort_scores'],
        tests: [
            { args: [[10, -5, 0, 3, -2]], expected: [-5, -2, 0, 3, 10] }
        ]
    },
  626: {
        functionNames: ['sort_emails'],
        tests: [
            { args: [['b@yahoo.com', 'a@gmail.com', 'c@outlook.com']], expected: ['a@gmail.com', 'c@outlook.com', 'b@yahoo.com'] }
        ]
    },
  627: {
        functionNames: ['sort_cities_by_population'],
        tests: [
            { args: [[['A', 100], ['B', 50]]], expected: [['B', 50], ['A', 100]] }
        ]
    },
  628: {
        functionNames: ['last_letter'],
        tests: [
            { args: [['banana', 'apple', 'grape', 'kiwi']], expected: ['banana', 'apple', 'grape', 'kiwi'] }
        ]
    },
  629: {
        functionNames: ['lst_of_numbers'],
        tests: [
            { args: [[1, 1, 2, 3, 3, 3]], expected: [2, 1, 1, 3, 3, 3] }
        ]
    },
  630: {
        functionNames: ['sort_students_by_grades'],
        tests: [
            { args: [[['A', 90], ['B', 80]]], expected: [['B', 80], ['A', 90]] }
        ]
    },
  631: {
        functionNames: ['sort_books_by_year'],
        tests: [
            { args: [[['A', 2000], ['B', 1990]]], expected: [['B', 1990], ['A', 2000]] }
        ]
    },
  632: {
        functionNames: ['sort_files_by_extension'],
        tests: [
            { args: [['file.txt', 'image.jpg', 'doc.pdf']], expected: ['image.jpg', 'doc.pdf', 'file.txt'] }
        ]
    },
  633: {
        functionNames: ['sort_movies_by_release_date'],
        tests: [
            { args: [[{title: 'A', release_date: '2001'}, {title: 'B', release_date: '1999'}, {title: 'C', release_date: '2005'}]], expected: [{title: 'B', release_date: '1999'}, {title: 'A', release_date: '2001'}, {title: 'C', release_date: '2005'}] }
        ]
    },
  634: {
        functionNames: ['sort_sentences_by_unique_words'],
        tests: [
            { args: [['a a', 'a b c', 'a b']], expected: ['a a', 'a b', 'a b c'] }
        ]
    },
  635: {
        functionNames: ['get_keys_from_dictionary'],
        tests: [
            { args: [{a: 1, b: 2}], expected: ['a', 'b'] }
        ]
    },
  636: {
        functionNames: ['dic_keys'],
        tests: [
            { args: [{a: 5, b: 15, c: 20, d: 3}], expected: ['b', 'c'] }
        ]
    },
  637: {
        functionNames: ['print_fruit_keys'],
        tests: [
            { args: [{apple: 1.2, banana: 0.5, orange: 0.75}], expected: ['apple', 'banana', 'orange'] }
        ]
    },
  638: {
        functionNames: ['max_key'],
        tests: [
            { args: [{1: 'a', 5: 'b', 3: 'c'}], expected: '5' }
        ]
    },
  639: {
        functionNames: ['name_age'],
        tests: [
            { args: [{Natty: 78, Bob: 45}], expected: ['Bob', 'Natty'] }
        ]
    },
  640: {
        functionNames: ['concatenate_keys'],
        tests: [
            { args: [{1: 456, 2: 5566, 3: 566}], expected: '123' }
        ]
    },
  641: {
    functionNames: ["print_countries_and_capitals"],
    compare: 'printedOrReturn',
    tests: [{
      args: [{"a": 1, "b": 2}],
      expected: "a: 1\nb: 2"
    }]
  },
  642: {
        functionNames: ['count_key'],
        tests: [
            { args: [{a: 1, b: 2, c: 3}], expected: 3 }
        ]
    },
  643: {
        functionNames: ['count_key'],
        tests: [
            { args: [{apple: 1, banana: 2, apricot: 3, berry: 4}, 'a'], expected: ['apple', 'apricot'] }
        ]
    },
  644: {
        functionNames: ['sorted_students_grades'],
        tests: [
            { args: [{Alice: 90, Bob: 85, Charlie: 95}], expected: ['Alice', 'Bob', 'Charlie'] }
        ]
    },
  645: {
        functionNames: ['list_dictionary'],
        tests: [
            { args: [[1, 2, 3], ['a', 'b', 'c']], expected: {1: 'a', 2: 'b', 3: 'c'} }
        ]
    },
  646: {
        functionNames: ['reverse_keys'],
        tests: [
            { args: [{a: 1, b: 2, c: 3}], expected: ['c', 'b', 'a'] }
        ]
    },
  647: {
        functionNames: ['first_key'],
        tests: [
            { args: [{apple: 1, banana: 2, cherry: 3}], expected: 'apple' }
        ]
    },
  648: {
        functionNames: ['shopping_cart_items'],
        compare: 'printedOrReturn',
        tests: [
            { args: [{apple: 3, banana: 6, orange: 4, milk: 1}], expected: 'apple\nbanana\norange\nmilk' }
        ]
    },
  649: {
        functionNames: ['check_key_exists'],
        tests: [
            { args: [{a: 1, b: 2, c: 3}, 'b'], expected: true },
            { args: [{a: 1, b: 2, c: 3}, 'z'], expected: false }
        ]
    },
  650: {
        functionNames: ['print_keys_greater_than_five'],
        compare: 'printedOrReturn',
        tests: [
            { args: [{apple: 3, banana: 6, orange: 4, milk: 8, bread: 2, eggs: 12}], expected: 'banana\nmilk\neggs' }
        ]
    },
  651: {
        functionNames: ['returns_strings'],
        tests: [
            { args: [{a: 1, 42: 'answer', c: 3}], expected: ['42', 'a', 'c'] }
        ]
    },
  652: {
        functionNames: ['sports_by_popularity'],
        tests: [
            { args: [{Soccer: 1, Cricket: 2, Basketball: 3}], expected: ['Soccer', 'Cricket', 'Basketball'] }
        ]
    },
  653: {
        functionNames: ['main'],
        tests: [
            { args: [], argExpressions: ["{2: 1, 'orange': 33, 'mango': 5}"], expected: [2] }
        ]
    },
  654: {
    functionNames: ["books_authors"],
    compare: 'printedOrReturn',
    tests: [{
      args: [{"a": 1, "b": 2}],
      expected: "1. a\n2. b"
    }]
  },
  655: {
        functionNames: ['palindromic_keys'],
        tests: [
            { args: [{racecar: 1, hello: 2, level: 3}], expected: ['racecar', 'level'] }
        ]
    },
  656: {
        functionNames: ['pet_owners'],
        tests: [
            { args: [{Boudy: 'Alice', Charlie: 'Bob', Monty: 'Catherine', Bella: 'Eva'}], expected: ['Boudy', 'Monty'] }
        ]
    },
  657: {
        functionNames: ['count_tuple_keys'],
        tests: [
            { args: [{a: 1, b: 2, c: 3}], expected: 0 }
        ]
    },
  658: {
        functionNames: ['movies'],
        tests: [
            { args: [{Inception: 2010, 'The Matrix': 1999, Gladiator: 2000}], expected: ['Gladiator', 'Inception', 'The Matrix'] }
        ]
    },
  659: {
        functionNames: ['keys_with_list_values'],
        tests: [
            { args: [{ fruits: ["apple"], vegetable: "carrot", numbers: [1, 2, 3] }], expected: ["fruits", "numbers"] },
            { args: [{ a: 1, b: 2 }], expected: [] },
        ]
    },
  660: {
    functionNames: ["print_car_brands"],
    compare: 'printedOrReturn',
    tests: [{
      args: [{"a": 1, "b": 2}],
      expected: "Car Brands:\n1. a\n2. b"
    }]
  },
  661: {
        functionNames: ['second_key'],
        tests: [
            { args: [{a: 1, b: 2, c: 3}], expected: 'b' }
        ]
    },
  662: {
        functionNames: ['temperature'],
        tests: [
            { args: [{Celsius: [0, 20], Fahrenheit: [32, 68]}], expected: ['CELSIUS', 'FAHRENHEIT'] }
        ]
    },
  663: {
        functionNames: ['keys_in_list'],
        tests: [
            { args: [{a: 1, b: 2, c: 3}, ['b', 'd']], expected: ['b'] }
        ]
    },
  664: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "Headphones\nKeyboard\nMouse\nCharger" },
        ]
    },
  665: {
        functionNames: ['keys_with_values_greater_than_10', 'get_dict_keys'],
        tests: [
            { args: [{Sam: 5, Chris: 34, Simon: 12, Anna: 9}], expected: ['Chris', 'Simon'] }
        ]
    },
  666: {
        functionNames: ['print_fruit_keys'],
        compare: 'printedOrReturn',
        tests: [
            { args: [{Apple: 3, Banana: 1, Mango: 2, Orange: 4}], expected: 'Apple\nBanana\nMango\nOrange' }
        ]
    },
  667: {
        functionNames: ['name_age'],
        tests: [
            { args: [{Tom: 15, Lucka: 66, Bob: 8}], expected: ['Bob', 'Tom', 'Lucka'] }
        ]
    },
  668: {
        functionNames: ['concatenate'],
        tests: [
            { args: [{1: 'one', 2: 'two', 3: 'three'}], expected: '123' }
        ]
    },
  669: {
    functionNames: ["countries_capitals"],
    compare: 'printedOrReturn',
    tests: [{
      args: [{"a": 1, "b": 2}],
      expected: "a: 1\nb: 2\n"
    }]
  },
  670: {
        functionNames: ['count_keys'],
        tests: [
            { args: [{a: 1, b: 2, c: 3, d: 4, e: 5}], expected: 5 }
        ]
    },
  671: {
        functionNames: ['keys_starting_with'],
        tests: [
            { args: [{apple: 1, banana: 2, apricot: 3, berry: 4}, 'a'], expected: ['apple', 'apricot'] }
        ]
    },
  672: {
    functionNames: ["students_grades"],
    compare: 'printedOrReturn',
    tests: [{
      args: [{"a": 1, "b": 2}],
      expected: "a\nb"
    }]
  },
  673: {
        functionNames: ['two_lst'],
        tests: [
            { args: [[1, 2, 3], ['a', 'b', 'c']], expected: {1: 'a', 2: 'b', 3: 'c'} }
        ]
    },
  674: {
        functionNames: ['colors_hex'],
        tests: [
            { args: [{a: 1, b: 2, c: 3}], expected: ['c', 'b', 'a'] }
        ]
    },
  675: {
        functionNames: ['first_key'],
        tests: [
            { args: [{apple: 1, banana: 2, cherry: 3}], expected: 'apple' }
        ]
    },
  676: {
        functionNames: ['print_cart_items'],
        compare: 'printedOrReturn',
        tests: [
            { args: [{apple: 3, banana: 2, bread: 1, milk: 2}], expected: 'apple\nbanana\nbread\nmilk' }
        ]
    },
  677: {
        functionNames: ['check_key_exists'],
        tests: [
            { args: [{a: 1, b: 2, c: 3}, 'b'], expected: true },
            { args: [{a: 1, b: 2, c: 3}, 'z'], expected: false }
        ]
    },
  678: {
        functionNames: ['items_with_high_quantity'],
        tests: [
            { args: [{apple: 3, banana: 6, orange: 2, milk: 8}], expected: ['banana', 'milk'] }
        ]
    },
  679: {
        functionNames: ['string_keys'],
        tests: [
            { args: [{a: 1, 42: 'answer', c: 3}], expected: ['42', 'a', 'c'] }
        ]
    },
  680: {
        functionNames: ['sports_by_popularity'],
        tests: [
            { args: [{Soccer: 1, Cricket: 2, Basketball: 3}], expected: ['Soccer', 'Cricket', 'Basketball'] }
        ]
    },
  681: {
        functionNames: ['retrieve_integer_keys'],
        tests: [
            { args: [], argExpressions: ["{1: 'one', 'two': 2, 3: 'three'}"], expected: [1, 3] }
        ]
    },
  682: {
    functionNames: ["print_numbered_books"],
    compare: 'printedOrReturn',
    tests: [{
      args: [{"a": 1, "b": 2}],
      expected: "1. a\n2. b"
    }]
  },
  683: {
        functionNames: ['palindrome_keys'],
        tests: [
            { args: [{racecar: 1, hello: 2, level: 3, world: 4}], expected: ['racecar', 'level'] }
        ]
    },
  684: {
        functionNames: ['pets_with_o'],
        tests: [
            { args: [{Boudy: 'Alice', Charlie: 'Bob', Monty: 'Catherine'}], expected: ['Boudy', 'Monty'] }
        ]
    },
  685: {
        functionNames: ['count_list_keys'],
        tests: [
            { args: [{a: 1, b: 2, c: 3}], expected: 0 }
        ]
    },
  686: {
        functionNames: ['sorted_movie_titles'],
        tests: [
            { args: [{Inception: 2010, 'The Matrix': 1999}], expected: ['Inception', 'The Matrix'] }
        ]
    },
  687: {
        functionNames: ['keys_with_list_values'],
        tests: [
            { args: [{a: [1, 2], b: 'carrot', c: [3]}], expected: ['a', 'c'] }
        ]
    },
  688: {
    functionNames: ["print_car_brands"],
    compare: 'printedOrReturn',
    tests: [{
      args: [{"a": 1, "b": 2}],
      expected: "Brand: a\nBrand: b"
    }]
  },
  689: {
        functionNames: ['second_key'],
        tests: [
            { args: [{a: 1, b: 2, c: 3}], expected: 'b' }
        ]
    },
  690: {
        functionNames: ['uppercase_keys'],
        tests: [
            { args: [{Celsius: [0, 20], Fahrenheit: [32, 68]}], expected: ['CELSIUS', 'FAHRENHEIT'] }
        ]
    },
  691: {
        functionNames: ['key_max'],
        tests: [
            { args: [{a: 1, c: 3, b: 2}], expected: 'c' }
        ]
    },
  692: {
        functionNames: ['square_numbers'],
        tests: [
            { args: [[1, 2, 3, 4, 5]], expected: [1, 4, 9, 16, 25] }
        ]
    },
  693: {
        functionNames: ['string_lengths'],
        tests: [
            { args: [['hello', 'world', 'python']], expected: [5, 5, 6] }
        ]
    },
  694: {
        functionNames: ['lst_words'],
        tests: [
            { args: [['monkey', 'lizard', 'hippopotamus']], expected: ['MONKEY', 'LIZARD', 'HIPPOPOTAMUS'] }
        ]
    },
  695: {
        functionNames: ['lst_numbers'],
        tests: [
            { args: [[2.6666, 4.7777, 7.5666]], expected: [2.67, 4.78, 7.57] }
        ]
    },
  696: {
        functionNames: ['celsius_to_fahrenheit'],
        tests: [
            { args: [[0, 20, 37, 100]], expected: [32.0, 68.0, 98.6, 212.0] }
        ]
    },
  697: {
        functionNames: ['numbers_to_ascii'],
        tests: [
            { args: [[65, 66, 67]], expected: ['A', 'B', 'C'] }
        ]
    },
  698: {
        functionNames: ['lst_words'],
        tests: [
            { args: [['monkey', 'lizard']], expected: ['yeknom', 'drazil'] }
        ]
    },
  700: {
        functionNames: ['lst_integers'],
        tests: [
            { args: [[1, 2, 3]], expected: [2, 4, 6] }
        ]
    },
  701: {
        functionNames: ['lst_words'],
        tests: [
            { args: [['monkey', 'lizard']], expected: ['m', 'l'] }
        ]
    },
  702: {
        functionNames: ['lst_words'],
        tests: [
            { args: [['101', '110', '1001']], expected: [5, 6, 9] }
        ]
    },
  703: {
        functionNames: ['lst_mixed_case'],
        tests: [
            { args: [['LIZARD', 'hiPpopotamus', 'FroG']], expected: ['lizard', 'hippopotamus', 'frog'] }
        ]
    },
  704: {
        functionNames: ['lst_integers'],
        tests: [
            { args: [[6, 12, 23, 68], [1, 2, 3, 4]], expected: [6, 24, 69, 272] }
        ]
    },
  705: {
        functionNames: ['euclidean_distances'],
        tests: [
            { args: [[[3, 4], [1, 1], [0, 0], [6, 8]]], expected: [5.0, 1.4142135623730951, 0.0, 10.0] }
        ]
    },
  706: {
        functionNames: ['lst_emails'],
        tests: [
            { args: [['user@example.com', 'admin@domain.org']], expected: ['example.com', 'domain.org'] }
        ]
    },
  707: {
        functionNames: ['lst_integers'],
        tests: [
            { args: [[1, 2, 3]], expected: ['Odd', 'Even', 'Odd'] }
        ]
    },
  708: {
        functionNames: ['negate_bool'],
        tests: [
            { args: [true], expected: false },
            { args: [false], expected: true }
        ]
    },
  709: {
        functionNames: ['negate_bool'],
        tests: [
            { args: [[true, false, true, false]], expected: [false, true, false, true] }
        ]
    },
  710: {
        functionNames: ['negate_booleans'],
        tests: [
            { args: [[true, false, true, false]], expected: [false, true, false, true] }
        ]
    },
  711: {
        functionNames: ['lst_sentence'],
        tests: [
            { args: [['hello world', 'python is fun', 'test']], expected: [2, 3, 1] }
        ]
    },
  712: {
        functionNames: ['lst_sentence'],
        tests: [
            { args: [['hello', 'world', 'python']], expected: ['Hello', 'World', 'Python'] }
        ]
    },
  713: {
        functionNames: ['lst_sentence'],
        tests: [
            { args: [['hello world', 'foo bar']], expected: ['helloworld', 'foobar'] }
        ]
    },
  714: {
        functionNames: ['lst_of_tuples'],
        tests: [
            { args: [[[3, 4], [5, 6]]], expected: [12, 30] }
        ]
    },
  715: {
        functionNames: ['extract_domain'],
        tests: [
            { args: [['https://example.com/page', 'https://domain.org']], expected: ['example.com', 'domain.org'] }
        ]
    },
  716: {
        functionNames: ['pair_elements'],
        tests: [
            { args: [[1, 2, 3], ['a', 'b', 'c']], expected: [[1, 'a'], [2, 'b'], [3, 'c']] }
        ]
    },
  717: {
        functionNames: ['lowercase_to_uppercase'],
        tests: [
            { args: [['a', 'b', 'c']], expected: ['A', 'B', 'C'] }
        ]
    },
  718: {
        functionNames: ['factorial_lst'],
        tests: [
            { args: [[1, 2, 3, 4, 5]], expected: [1, 2, 6, 24, 120] }
        ]
    },
  719: {
        functionNames: ['reverse_words_in_sentences'],
        tests: [
            { args: [['hello world', 'abc def']], expected: ['olleh dlrow', 'cba fed'] }
        ]
    },
  720: {
        functionNames: ['lst_strings'],
        tests: [
            { args: [['hello', 'world123']], expected: [true, false] }
        ]
    },
  721: {
        functionNames: ['square_floats'],
        tests: [
            { args: [[2.5, 3.0, 4.0]], expected: [6.25, 9.0, 16.0] }
        ]
    },
  722: {
        functionNames: ['format_phone_numbers'],
        tests: [
            { args: [['1234567890', '9876543210']], expected: ['+1-1234567890', '+1-9876543210'] }
        ]
    },
  723: {
        functionNames: ['absolute_values'],
        tests: [
            { args: [[-1, 2, -3, 4]], expected: [1, 2, 3, 4] }
        ]
    },
  724: {
        functionNames: ['pair_lists'],
        tests: [
            { args: [[1, 2, 3], [4, 5, 6]], expected: [[1, 4], [2, 5], [3, 6]] }
        ]
    },
  725: {
        functionNames: ['cartesian_to_polar'],
        tests: [
            { args: [[[3, 4], [1, 1]]], expected: [[5.0, 0.9272952180016122], [1.4142135623730951, 0.7853981633974483]] }
        ]
    },
  726: {
        functionNames: ['lst_cubes'],
        tests: [
            { args: [[1, 2, 3, 4, 5]], expected: [1, 8, 27, 64, 125] }
        ]
    },
  727: {
        functionNames: ['lst_squares_and_cubes'],
        tests: [
            { args: [[1, 2, 3]], expected: [[1, 1], [4, 8], [9, 27]] }
        ]
    },
  728: {
        functionNames: ['rgb_to_hex'],
        tests: [
            { args: [[[255, 0, 0], [0, 255, 0]]], expected: ['#ff0000', '#00ff00'] }
        ]
    },
  729: {
        functionNames: ['mixed_case_string'],
        tests: [
            { args: [['first', 'second', 'third', 'fourth']], expected: ['fIrst', 'sEcond', 'tHird', 'fOurth'] }
        ]
    },
  730: {
        functionNames: ['convert_dates'],
        tests: [
            { args: [['2024-01-01', '2023-12-25']], expected: ['2024-01-01T00:00:00', '2023-12-25T00:00:00'] }
        ]
    },
  731: {
        functionNames: ['calculate_square_roots'],
        tests: [
            { args: [[1, 4, 9, 16]], expected: [1.0, 2.0, 3.0, 4.0] }
        ]
    },
  732: {
        functionNames: ['calculate_percentage'],
        tests: [
            { args: [[50, 75, 100], 100], expected: [50.0, 75.0, 100.0] }
        ]
    },
  733: {
    functionNames: ["sum_list", "add"],
    tests: [
      { functionName: "sum_list", args: [[1, 2, 3, 4, 5]], expected: 15 },
      { functionName: "add", args: [7, 8], expected: 15 }
    ]
  },
  734: {
    functionNames: ["is_even","filter_even_numbers"],
    tests: [
      { functionName: "filter_even_numbers", args: [[1, 2, 3, 4, 5, 6]], expected: [2, 4, 6] },
      { functionName: "is_even", args: [5], expected: false }
    ]
  },
  735: {
    functionNames: ["word_list", "capitalize_first_letter"],
    tests: [
      { functionName: "word_list", args: [["first", "letter", "word"]], expected: ["First", "Letter", "Word"] },
      { functionName: "capitalize_first_letter", args: ["hello"], expected: "Hello" }
    ]
  },
  736: {
    functionNames: ["lst_numbers", "find_max"],
    tests: [
      { functionName: "lst_numbers", args: [[2, 4, 6, 1]], expected: 6 },
      { functionName: "find_max", args: [[-5, -2, -9]], expected: -2 }
    ]
  },
  737: {
    functionNames: ["lst_tempertures", "convert_to_celsius"],
    tests: [
      { functionName: "lst_tempertures", args: [[32, 50, 68]], expected: [0, 10, 20] },
      { functionName: "convert_to_celsius", args: [212], expected: 100 }
    ]
  },
  738: {
    functionNames: ["string_lst", "reverse_string"],
    tests: [
      { functionName: "string_lst", args: [["hello", "twice"]], expected: ["olleh", "eciwt"] },
      { functionName: "reverse_string", args: ["python"], expected: "nohtyp" }
    ]
  },
  739: {
    functionNames: ["lst_words", "count_vowels"],
    tests: [
      { functionName: "lst_words", args: [["word", "eerie", "education"]], expected: "education" },
      { functionName: "count_vowels", args: ["Queue"], expected: 4 }
    ]
  },
  740: {
    functionNames: ["lst_of_word", "is_palindrome"],
    tests: [
      { functionName: "lst_of_word", args: [["radar", "words", "level", "deed"]], expected: ["radar", "level", "deed"] },
      { functionName: "is_palindrome", args: ["python"], expected: false }
    ]
  },
  741: {
    functionNames: ["lst_of_radii", "calculate_area"],
    tests: [
      { functionName: "lst_of_radii", args: [[1, 2, 3]], expected: [3.14159, 12.56636, 28.27431] },
      { functionName: "calculate_area", args: [4], expected: 50.26544 }
    ]
  },
  742: {
    functionNames: ["lst_numbers", "sqaure_number"],
    tests: [
      { functionName: "lst_numbers", args: [[2, 5, 7]], expected: [4, 25, 49] },
      { functionName: "sqaure_number", args: [9], expected: 81 }
    ]
  },
  743: {
    functionNames: ["get_first_n_elements"],
    tests: [
      { args: [[1, 2, 3, 4, 5], 3], expected: [1, 2, 3] },
      { args: [[1, 2, 3, 4, 5], 5], expected: [1, 2, 3, 4, 5] }
    ]
  },
  744: {
    functionNames: ["merge_dicts","combine_dicts"],
    tests: [
      { functionName: "merge_dicts", args: [{"a":1},{"b":2}], expected: {"a":1,"b":2} },
      { functionName: "combine_dicts", args: [[{"a":1},{"b":2},{"a":3}]], expected: {"a":3,"b":2} }
    ]
  },
  745: {
    functionNames: ["format_name", "format_names"],
    tests: [
      { functionName: "format_name", args: ["John", "Doe"], expected: "John Doe" },
      { functionName: "format_names", args: [[["Jane", "Smith"], ["Alice", "Johnson"]]], expected: ["Jane Smith", "Alice Johnson"] }
    ]
  },
  746: {
    functionNames: ["find_gcd","gcd_of_pairs","gcd_pair"],
    tests: [
      { functionName: "find_gcd", args: [48, 18], expected: 6 },
      { functionName: "gcd_of_pairs", args: [[[48, 18], [56, 98], [100, 10]]], expected: [6, 14, 10] }
    ]
  },
  747: {
    functionNames: ["lst_elements", "count_occurrences"],
    tests: [
      { functionName: "lst_elements", args: [["tree", "tree", "tree", "sand"]], expected: 3 },
      { functionName: "count_occurrences", args: [["a", "b", "a"], "a"], expected: 2 }
    ]
  },
  748: {
    functionNames: ["lst_words", "sort_lst"],
    tests: [
      { functionName: "lst_words", args: [["zebra", "frog", "anaconda"], ["ktm", "Honda", "Suzuki"]], expected: [["anaconda", "frog", "zebra"], ["Honda", "Suzuki", "ktm"]] },
      { functionName: "sort_lst", args: [[3, 1, 2]], expected: [1, 2, 3] }
    ]
  },
  749: {
    functionNames: ["domain_names", "extract_URL"],
    tests: [
      { functionName: "domain_names", args: [["http://google.com", "http://github.com"]], expected: ["google.com", "github.com"] },
      { functionName: "extract_URL", args: ["http://stackoverflow.com"], expected: "stackoverflow.com" }
    ]
  },
  750: {
    functionNames: ["lst_sites", "remove_duplicates"],
    compare: "unorderedList",
    tests: [
      { functionName: "lst_sites", args: [["google", "twitter", "google", "apple"]], expected: ["google", "twitter", "apple"] },
      { functionName: "remove_duplicates", args: [[1, 2, 1, 3]], expected: [1, 2, 3] }
    ]
  },
  751: {
    functionNames: ["main", "lst_of_lists", "flatten_list"],
    tests: [
      { functionName: "flatten_list", args: [[[1, 2], [3], [4, 5]]], expected: [1, 2, 3, 4, 5] },
      { functionName: "lst_of_lists", args: [[["a"], ["b", "c"]]], expected: ["a", "b", "c"] }
    ]
  },
  752: {
    functionNames: ["filter_primes", "is_prime"],
    tests: [
      { functionName: "filter_primes", args: [[1, 2, 3, 4, 5, 9, 11]], expected: [2, 3, 5, 11] },
      { functionName: "is_prime", args: [9], expected: false }
    ]
  },
  753: {
    functionNames: ["main", "lst_of_numbers", "calculate_factorial"],
    tests: [
      { functionName: "lst_of_numbers", args: [[2, 4, 5]], expected: [2, 24, 120] },
      { functionName: "calculate_factorial", args: [6], expected: 720 }
    ]
  },
  754: {
    functionNames: ["main", "sort_dict_by_value", "get_value"],
    tests: [
      { functionName: "sort_dict_by_value", args: [{"name": 2, "age": 5, "city": 1}], expected: {"city": 1, "name": 2, "age": 5} },
      { functionName: "get_value", args: [["key", 9]], expected: 9 }
    ]
  },
  755: {
    functionNames: ["main", "get_unique_elements"],
    compare: "unorderedList",
    tests: [
      { functionName: "get_unique_elements", args: [["apple", "banana", "apple", "kiwi"]], expected: ["apple", "banana", "kiwi"] }
    ]
  },
  756: {
    functionNames: ["main", "check_anagram"],
    tests: [
      { functionName: "check_anagram", args: ["evil", "vile"], expected: true },
      { functionName: "main", args: ["hello", "world"], expected: false }
    ]
  },
  757: {
    functionNames: ["find_index", "main"],
    tests: [
      { functionName: "find_index", args: [["apple", "banana", "date"], "date"], expected: 2 },
      { functionName: "find_index", args: [[10, 20, 30], 20], expected: 1 }
    ]
  },
  758: {
    functionNames: ["main", "generate_fibonacci"],
    tests: [
      { functionName: "generate_fibonacci", args: [7], expected: [0, 1, 1, 2, 3, 5, 8] },
      { functionName: "main", args: [3], expected: [0, 1, 1] }
    ]
  },
  759: {
    functionNames: ["main", "calculate_average"],
    tests: [
      { functionName: "calculate_average", args: [[10, 20, 30]], expected: 20 },
      { functionName: "main", args: [[10, 20], [2, 4, 6]], expected: [15, 4] }
    ]
  },
  760: {
    functionNames: ["main", "convert_to_kilometers"],
    tests: [
      { functionName: "convert_to_kilometers", args: [10], expected: 16.0934 },
      { functionName: "main", args: [[1, 2]], expected: [1.60934, 3.21868] }
    ]
  },
  761: {
    functionNames: ["main", "get_last_n_elements"],
    tests: [
      { functionName: "get_last_n_elements", args: [[1, 2, 3, 4, 5], 3], expected: [1, 2, 3] },
      { functionName: "main", args: [["a", "b", "c"], 2], expected: ["a", "b"] }
    ]
  },
  762: {
    functionNames: ["main", "remove_whitespace"],
    tests: [
      { functionName: "remove_whitespace", args: ["hello world"], expected: "helloworld" },
      { functionName: "main", args: ["a b c"], expected: "abc" }
    ]
  },
  763: {
    functionNames: ["main", "get_positive_numbers"],
    tests: [
      { functionName: "main", args: [[1, -2, 2, -3, 3]], expected: [1, 2, 3] },
      { functionName: "get_positive_numbers", args: [-1], expected: false }
    ]
  },
  764: {
    functionNames: ["get_common_elements", "main"],
    tests: [
      { functionName: "get_common_elements", args: [["tree", "boat", "sea"], ["boat", "cat", "sea"]], expected: ["boat", "sea"] },
      { functionName: "main", args: [[1, 2, 2, 3], [2, 3]], expected: [2, 3] }
    ]
  },
  765: {
    functionNames: ["main", "check_even_odd"],
    tests: [
      { functionName: "main", args: [[45, 7, 2, 3]], expected: ["Odd", "Odd", "Even", "Odd"] },
      { functionName: "check_even_odd", args: [8], expected: "Even" }
    ]
  },
  766: {
    functionNames: ["main", "convert_to_uppercase"],
    tests: [
      { functionName: "main", args: [["hello", "world"]], expected: ["HELLO", "WORLD"] },
      { functionName: "convert_to_uppercase", args: ["python"], expected: "PYTHON" }
    ]
  },
  767: {
    functionNames: ["main", "count_characters"],
    tests: [
      { functionName: "main", args: [["eorl", "sitting", "mountain"]], expected: [4, 7, 8] },
      { functionName: "count_characters", args: ["hello"], expected: 5 }
    ]
  },
  768: {
    functionNames: ["main", "remove_special_characters"],
    tests: [
      { functionName: "main", args: [["eor?@l", "s@itting?", "@mountain?"]], expected: ["eorl", "sitting", "mountain"] },
      { functionName: "remove_special_characters", args: ["a?@b"], expected: "ab" }
    ]
  },
  769: {
    functionNames: ["main", "is_substring"],
    tests: [
      { functionName: "main", args: [[["apple", "pineapple"], ["cat", "dog"]]], expected: [true, false] },
      { functionName: "is_substring", args: ["dog", "doghouse"], expected: true }
    ]
  },
  770: {
    functionNames: ["main", "sum_of_list"],
    tests: [
      { functionName: "main", args: [[2, 2, 2, 2, 2]], expected: 10 }
    ]
  },
  771: {
    functionNames: ["main", "get_even_numbers"],
    tests: [
      { functionName: "main", args: [[46, 22, 7, 4, 8, 13]], expected: [46, 22, 4, 8] },
      { functionName: "get_even_numbers", args: [7], expected: false }
    ]
  },
  772: {
    functionNames: ["main", "merge_sorted_lists"],
    compare: "unorderedList",
    tests: [
      { functionName: "merge_sorted_lists", args: [[3, 1], [2, 4]], expected: [1, 2, 3, 4] },
      { functionName: "main", args: [[1, 33, 8], [9, 2, 7]], expected: [1, 2, 7, 8, 9, 33] }
    ]
  },
  773: {
    functionNames: ["lst_to_dic"],
    tests: [
      { args: [[1, 2, 3], ["start", "middle", "end"]], expected: {"1": "start", "2": "middle", "3": "end"} }
    ]
  },
  774: {
    functionNames: ["main", "value_of_specific_key"],
    tests: [
      { functionName: "main", args: [{"name": 777, "job": 1}, "job"], expected: 1 },
      { functionName: "value_of_specific_key", args: [{"age": 30}, "age"], expected: 30 }
    ]
  },
  775: {
    functionNames: ["main", "merge_dicts"],
    tests: [
      { functionName: "merge_dicts", args: [{"a": 1}, {"b": 2}], expected: {"a": 1, "b": 2} },
      { functionName: "main", args: [{"a": 1}, {"b": 3}], expected: {"a": 1, "b": 3} }
    ]
  },
  776: {
    functionNames: ["remove_key", "main"],
    tests: [
      { functionName: "remove_key", args: [{"a": 1, "b": 2}, "a"], expected: {"b": 2} },
      { functionName: "main", args: [{"x": 1, "y": 2}, "z"], expected: {"x": 1, "y": 2} }
    ]
  },
  777: {
    functionNames: ["print_dict_items", "main"],
    compare: "printedOrReturn",
    tests: [
      { functionName: "print_dict_items", args: [{"a": 1, "b": 2}], expected: "a: 1\nb: 2" }
    ]
  },
  778: {
    functionNames: ["main", "does_key_exist"],
    tests: [
      { functionName: "does_key_exist", args: [{"name": "Steven", "age": 56}, "name"], expected: "key exists" },
      { functionName: "does_key_exist", args: [{"name": "Steven", "age": 56}, "job"], expected: "key does not exist" }
    ]
  },
  779: {
    functionNames: ["sort_dic"],
    tests: [
      { args: [{"b": 2, "a": 1}], expected: {"a": 1, "b": 2} }
    ]
  },
  780: {
    functionNames: ["main", "sort_values", "sort_key"],
    tests: [
      { functionName: "main", args: [{"name": 777, "age": 56, "city": 34, "job": 1}], expected: {"job": 1, "city": 34, "age": 56, "name": 777} },
      { functionName: "sort_key", args: [["cat", 34]], expected: 34 }
    ]
  },
  781: {
    functionNames: ["frequency_elements"],
    tests: [
      { args: [["tree", "tree", "flower", "flower", "tree"]], expected: {"tree": 3, "flower": 2} }
    ]
  },
  782: {
    functionNames: ["square_dic"],
    tests: [
      { args: [], expected: {"1": 1, "2": 4, "3": 9, "4": 16, "5": 25} }
    ]
  },
  783: {
    functionNames: ["main", "update_value"],
    tests: [
      { functionName: "main", args: [{"name": 777, "city": 34}, ["city", 78]], expected: {"name": 777, "city": 78} },
      { functionName: "update_value", args: [{"age": 30}, "age", 60], expected: {"age": 60} }
    ]
  },
  784: {
    functionNames: ["get_keys"],
    compare: "unorderedList",
    tests: [
      { args: [{"name": "Steven", "age": 56}], expected: ["name", "age"] }
    ]
  },
  785: {
    functionNames: ["get_keys"],
    tests: [
      { args: [{"name": "Steven", "age": 56}], expected: ["Steven", 56] }
    ]
  },
  786: {
    functionNames: ["get_keys"],
    compare: "unorderedList",
    tests: [
      { args: [{"city": "New York", "job": "Engineer"}], expected: ["New York", "Engineer"] }
    ]
  },
  787: {
    functionNames: ["largest_value"],
    tests: [
      { args: [{"name": 777, "age": 56, "city": 34}], expected: 777 }
    ]
  },
  788: {
    functionNames: ["largest_value"],
    tests: [
      { args: [{"name": 777, "age": 56, "city": 34}], expected: 34 }
    ]
  },
  789: {
    functionNames: ["lst_dic"],
    tests: [
      { args: [[1, 2, 3], ["sand", "rock", "beach", "sea"]], expected: {"1": "sand", "2": "rock", "3": "beach"} }
    ]
  },
  790: {
    functionNames: ["combine_dictionaries"],
    tests: [
      { args: [{"a": 1, "b": 2, "c": 3}, {"b": 3, "c": 4, "d": 5}], expected: {"a": 1, "b": 5, "c": 7, "d": 5} }
    ]
  },
  791: {
    functionNames: ["invert_dictionary"],
    tests: [
      { args: [{"name": "Alice", "age": 30}], expected: {"Alice": "name", "30": "age"} }
    ]
  },
  792: {
    functionNames: ["remove_duplicates_values"],
    tests: [
      { args: [{"name": "Alice", "age": 30, "nickname": "Alice"}], expected: {"name": "Alice", "age": 30} }
    ]
  },
  793: {
    functionNames: ["same_keys"],
    tests: [
      { args: [{"name": "Alice", "age": 30}, {"age": 40, "name": "Bob"}], expected: true },
      { args: [{"name": "Alice"}, {"age": 30}], expected: false }
    ]
  },
  794: {
    functionNames: ["multiply_by2"],
    tests: [
      { args: [{"a": 2, "b": 8}], expected: {"a": 4, "b": 16} }
    ]
  },
  795: {
    functionNames: ["len_key_value_pair"],
    tests: [
      { args: [{"name": "Alice", "age": 30, "job": "Engineer"}], expected: 3 }
    ]
  },
  796: {
    functionNames: ["map_lst_string_dic", "len_dic"],
    tests: [
      { functionName: "map_lst_string_dic", args: [["it", "shop", "jonny"]], expected: {"it": 2, "shop": 4, "jonny": 5} },
      { functionName: "len_dic", args: [["not", "house"]], expected: {"not": 3, "house": 5} }
    ]
  },
  797: {
    functionNames: ["add_key_value_pair"],
    tests: [
      { args: [{"name": "Alice"}], expected: {"name": "Alice", "new_key": "new_value"} }
    ]
  },
  798: {
    functionNames: ["value_cubes"],
    tests: [
      { args: [], expected: {"1": 1, "2": 8, "3": 27, "4": 64, "5": 125} }
    ]
  },
  799: {
    functionNames: ["check_if_empty"],
    tests: [
      { args: [{}], expected: "Dictionary is empty" },
      { args: [{"name": "Alice"}], expected: "Dictionary is not empty" }
    ]
  },
  800: {
    functionNames: ["remove_set_keys"],
    tests: [
      { args: [{"name": "Alice", "age": 30, "city": "New York", "job": "Engineer"}, ["age", "city"]], expected: {"name": "Alice", "job": "Engineer"} }
    ]
  },
  801: {
    functionNames: ["dic_lst_tuples"],
    tests: [
      { args: [{"a": 1, "b": 2}], expected: [["a", 1], ["b", 2]] }
    ]
  },
  802: {
    functionNames: ["main", "map_value"],
    tests: [
      { functionName: "main", args: [{"name": 1, "age": 56, "job": 1}], expected: ["name", "job"] },
      { functionName: "map_value", args: [{"name": "Alice", "age": 30, "nickname": "Alice"}, "Alice"], expected: {"name": "Alice", "nickname": "Alice"} }
    ]
  },
  803: {
    functionNames: ["replace_value"],
    tests: [
      { args: [{"a": 1, "b": [2]}, [1, 2, 3]], expected: {"a": [1, 2, 3], "b": [2]} }
    ]
  },
  804: {
    functionNames: ["nested_dic"],
    tests: [
      { args: [], expected: {"1": {"square": 1, "cube": 1}, "2": {"square": 4, "cube": 8}, "3": {"square": 9, "cube": 27}, "4": {"square": 16, "cube": 64}, "5": {"square": 25, "cube": 125}} }
    ]
  },
  805: {
    functionNames: ["string_dic"],
    tests: [
      { args: ["hello"], expected: {"h": 1, "e": 1, "l": 2, "o": 1} },
      { args: ["banana"], expected: {"b": 1, "a": 3, "n": 2} }
    ]
  },
  806: {
    functionNames: ["sort_dic"],
    tests: [
      { args: [{"a": 1, "b": 2, "c": 0}], expected: {"b": 2, "a": 1, "c": 0} }
    ]
  },
  807: {
    functionNames: ["lst_tuples"],
    tests: [
      { args: [[["a", 1], ["b", 2], ["c", 3]]], expected: {"a": 1, "b": 2, "c": 3} }
    ]
  },
  808: {
    functionNames: ["less_then_10"],
    tests: [
      { args: [{"low": 1, "ten": 10, "high": 12}], expected: {"ten": 10, "high": 12} }
    ]
  },
  809: {
    functionNames: ["print_readable"],
    compare: "printedOrReturn",
    tests: [
      { args: [{"a": 1, "b": 2}], expected: "a: 1\nb: 2" }
    ]
  },
  810: {
    functionNames: ["students_grades"],
    tests: [
      { args: [{"Bob": 50, "Alex": 72, "Fred": 87, "Liz": 90}], expected: ["Alex", "Fred", "Liz"] }
    ]
  },
  811: {
    functionNames: ["word_len"],
    tests: [
      { args: ["today we code"], expected: {"today": 5, "we": 2, "code": 4} }
    ]
  },
  812: {
    functionNames: ["word_len"],
    tests: [
      { args: ["python is fun"], expected: {"python": 6, "is": 2, "fun": 3} }
    ]
  },
  813: {
    functionNames: ["starting_letter", "main"],
    tests: [
      { functionName: "starting_letter", args: [{"Bob": 50, "Alex": 72, "Fred": 87, "Ben": 90}], expected: {"B": ["Bob", "Ben"], "A": ["Alex"], "F": ["Fred"]} },
      { functionName: "main", args: [{"name": 777, "age": 56}], expected: {"n": "name", "a": "age"} }
    ]
  },
  814: {
    functionNames: ["upper_keys"],
    tests: [
      { args: [{"a": 1, "b": 2}], expected: {"A": 1, "B": 2} }
    ]
  },
  815: {
    functionNames: ["intersection"],
    tests: [
      { args: [{"Bob": 500, "Alex": 72, "Liz": 90}, {"Bob": 50, "Liz": 90}], expected: {"Bob": 500, "Liz": 90} }
    ]
  },
  816: {
    functionNames: ["count_vowels"],
    tests: [
      { args: ["hello"], expected: {"a": 0, "e": 1, "i": 0, "o": 1, "u": 0} }
    ]
  },
  817: {
    functionNames: ["remove_value_is_none"],
    tests: [
      { args: [{"Bob": null, "Fred": 89, "Liz": 90}], expected: {"Fred": 89, "Liz": 90} }
    ]
  },
  818: {
    functionNames: ["check_key_value"],
    tests: [
      { args: [{"Bob": 500, "Liz": 90}, {"Liz": 90}], expected: true },
      { args: [{"Bob": 500, "Liz": 90}, {"Liz": 91}], expected: false }
    ]
  },
  819: {
    functionNames: ["dict_to_json"],
    tests: [
      { args: [{"Bob": 500, "Alex": 72}], expected: "{\"Bob\": 500, \"Alex\": 72}" }
    ]
  },
  820: {
    functionNames: ["merge_dicts"],
    tests: [
      { args: [{"name": "Steven"}, {"named": "Alice"}], expected: {"name": "Steven", "named": "Alice"} }
    ]
  },
  821: {
    functionNames: ["product_values"],
    tests: [
      { args: [{"a": 2, "b": 3, "c": 4}], expected: 24 }
    ]
  },
  822: {
    functionNames: ["average_values"],
    tests: [
      { args: [{"a": 10, "b": 20, "c": 30}], expected: 20 }
    ]
  },
  823: {
    functionNames: ["swap_values"],
    tests: [
      { args: [{"a": 1, "b": 2, "c": 3}, "a", "c"], expected: {"a": 3, "b": 2, "c": 1} }
    ]
  },
  824: {
    functionNames: ["largest_value"],
    tests: [
      { args: [{"name": 777, "age": 56, "city": 34}], expected: "name" }
    ]
  },
  825: {
    functionNames: ["smallest_value"],
    tests: [
      { args: [{"name": 777, "age": 56, "city": 34}], expected: "city" }
    ]
  },
  826: {
    functionNames: ["main", "add_multiple_pairs"],
    tests: [
      { functionName: "main", args: [{"a": 1}], expected: {"a": 1, "first": 1, "second": 2} },
      { functionName: "add_multiple_pairs", args: [{"name": 777}, {"status": "unemployed", "country": "USA"}], expected: {"name": 777, "status": "unemployed", "country": "USA"} }
    ]
  },
  827: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "1\n2\n3\n4\n5\n6\n7\n8\n9\n10" }
    ]
  },
  828: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "2\n4\n6\n8\n10\n12\n14\n16\n18\n20" }
    ]
  },
  829: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "10\n9\n8\n7\n6\n5\n4\n3\n2\n1" }
    ]
  },
  830: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], inputValues: ["3"], expected: "Hello\nHello\nHello" },
      { args: [], inputValues: ["1"], expected: "Hello" }
    ]
  },
  831: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], inputValues: ["hello", "again", "exit"], expected: "" }
    ]
  },
  832: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "1\n2\n4\n8\n16\n32\n64\n128\n256\n512" }
    ]
  },
  833: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "5\n10\n15\n20\n25\n30\n35\n40\n45\n50" }
    ]
  },
  834: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], inputValues: ["20", "15", "18"], expected: "53" },
      { args: [], inputValues: ["51"], expected: "51" }
    ]
  },
  835: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], inputValues: ["3", "5", "8"], expected: "" }
    ]
  },
  836: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], inputValues: ["5", "7", "0"], expected: "12" },
      { args: [], inputValues: ["0"], expected: "0" }
    ]
  },
  837: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "0\n1\n1\n2\n3\n5\n8\n13\n21\n34" }
    ]
  },
  838: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], inputValues: ["1", "9", "7"], expected: "" }
    ]
  },
  839: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], inputValues: ["Education"], expected: "5" },
      { args: [], inputValues: ["rhythm"], expected: "0" }
    ]
  },
  840: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], inputValues: ["code"], expected: "code\ncod\nco\nc" }
    ]
  },
  841: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], inputValues: ["4"], expected: "4\n3\n2\n1\n0" }
    ]
  },
  842: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], inputValues: ["4", "6", "2", "-1"], expected: "12" },
      { args: [], inputValues: ["-5"], expected: "0" }
    ]
  },
  843: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], inputValues: ["3", "9", "4", "stop"], expected: "9" },
      { args: [], inputValues: ["-2", "-5", "stop"], expected: "-2" }
    ]
  },
  844: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], inputValues: ["wrong", "python"], expected: "" }
    ]
  },
  845: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "2\n4\n16\n256" }
    ]
  },
  846: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], inputValues: ["12345"], expected: "54321" },
      { args: [], inputValues: ["900"], expected: "9" }
    ]
  },
  847: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], inputValues: ["10", "20", "30", "done"], expected: "20.0" },
      { args: [], inputValues: ["5", "done"], expected: "5.0" }
    ]
  },
  848: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], inputValues: ["4"], expected: "4\n3\n2\n1" }
    ]
  },
  849: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], randomValues: [5, 8, 14], expected: "5\n8" },
      { args: [], randomValues: [21], expected: "" }
    ]
  },
  850: {
    functionNames: ["is_prime"],
    tests: [
      { args: [2], expected: true },
      { args: [9], expected: false },
      { args: [17], expected: true }
    ]
  },
  851: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], inputValues: ["Education"], expected: "dctn" },
      { args: [], inputValues: ["rhythm"], expected: "rhythm" }
    ]
  },
  852: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], inputValues: ["12345"], expected: "5" },
      { args: [], inputValues: ["7"], expected: "1" }
    ]
  },
  853: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], inputValues: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], expected: "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]" }
    ]
  },
  854: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], inputValues: ["8"], expected: "8\n4.0\n2.0\n1.0" },
      { args: [], inputValues: ["1"], expected: "1" }
    ]
  },
  855: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], inputValues: ["red", "blue", "stop"], expected: "['red', 'blue']" },
      { args: [], inputValues: ["stop"], expected: "[]" }
    ]
  },
  856: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], inputValues: ["30"], expected: "900\n961" },
      { args: [], inputValues: ["32"], expected: "" }
    ]
  },
  857: {
    functionNames: [],
    mode: 'script',
    compare: 'numberList',
    tests: [
      { args: [], expected: [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26, 28, 29, 31, 32, 34, 35, 37, 38, 40, 41, 43, 44, 46, 47, 49, 50] }
    ]
  },
  858: {
    functionNames: [],
    mode: 'script',
    compare: 'numberList',
    tests: [
      { args: [], expected: [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100] }
    ]
  },
  859: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "1\n2\n3\n4\n5" }
    ]
  },
  860: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "2500" }
    ]
  },
  861: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "9" }
    ]
  },
  862: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], inputValues: ["121", "quit", "121", "12", "quit"], expected: "121 is a palindrome\n12 is not a palindrome" }
    ]
  },
  863: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "10\n9\n8\n7\n6\n5\n4\n3\n2\n1\nLift off!" }
    ]
  },
  864: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], inputValues: ["hello", "Python", "exit"], expected: "5\n6" },
      { args: [], inputValues: ["exit"], expected: "" }
    ]
  },
  865: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], inputValues: ["1", "2", "3", "4", "5"], expected: "120" },
      { args: [], inputValues: ["2", "3", "4", "5", "6"], expected: "720" }
    ]
  },
  866: {
    functionNames: ["main"],
    tests: [
      { args: [[1, 3, 8], ["9", "2", "7"]], expected: {"1": "9", "3": "2", "8": "7"} },
      { args: [["a", "b"], [10, 20]], expected: {"a": 10, "b": 20} }
    ]
  },
  867: {
    functionNames: ["create_dictionary"],
    tests: [
      { args: [["apple", "banana", "cherry"], [1, 2, 3]], expected: {"apple": 1, "banana": 2, "cherry": 3} },
      { args: [[1, 2], ["one", "two"]], expected: {"1": "one", "2": "two"} }
    ]
  },
  868: {
    functionNames: ["capitalize_words","capitalize"],
    tests: [
      { args: [["jonathan", "sam", "mimi"]], expected: ["Jonathan", "Sam", "Mimi"] },
      { args: [["python", "code"]], expected: ["Python", "Code"] }
    ]
  },
  869: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "1 2 3" }
    ]
  },
  870: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "10 [20, 30, 40] 50" }
    ]
  },
  871: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "10 5" }
    ]
  },
  872: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "('name', 'age', 'city') ('Alice', 25, 'New York')" }
    ]
  },
  873: {
    functionNames: ["get_coordinates"],
    tests: [{
      args: [],
      expected: [5, 10]
    }]
  },
  874: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "P y thon" }
    ]
  },
  875: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "100 500" }
    ]
  },
  876: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "1 2 3 4" }
    ]
  },
  877: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "0 1 2" }
    ]
  },
  878: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "John Doe" }
    ]
  },
  879: {
    functionNames: ["greet"],
    compare: "printedOrReturn",
    tests: [
      { args: ["Alice", 30], expected: "Hello, Alice. You are 30 years old." },
      { args: ["Bob", 41], expected: "Hello, Bob. You are 41 years old." }
    ]
  },
  880: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[1, 2, 3, 4, 5, 6]" }
    ]
  },
  881: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "{'a': 1, 'b': 2, 'c': 3, 'd': 4}" }
    ]
  },
  882: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "1 3 5" }
    ]
  },
  883: {
    functionNames: ["add"],
    tests: [{
      args: [1, 2, 3],
      expected: 6
    }]
  },
  884: {
    functionNames: ["describe"],
    tests: [{
      args: ["Emma", 28, "London"],
      expected: "Emma is 28 years old and lives in London."
    }]
  },
  885: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "A B C" }
    ]
  },
  886: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "1 [2, 3, 4, 5, 6, 7, 8] 9" }
    ]
  },
  887: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "1 a\n2 b\n3 c" }
    ]
  },
  888: {
    functionNames: ["get_user"],
    tests: [{
      args: [],
      expected: ["Alice", 25]
    }]
  },
  889: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[12, 15, 18]" }
    ]
  },
  890: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['name: Alice', 'age: 25', 'city: New York']" }
    ]
  },
  891: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Python ['is', 'a', 'powerful', 'programming'] language" }
    ]
  },
  892: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['u', 'a', 'i']" }
    ]
  },
  893: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Alice 30 5.8 True" }
    ]
  },
  894: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[(4, 1), (2, 2), (1, 3)]" }
    ]
  },
  895: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[2, 4, 6]" }
    ]
  },
  896: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "3 1 2" }
    ]
  },
  897: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "0 1 [2, 3, 4, 5, 6, 7, 8, 9]" }
    ]
  },
  898: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "15" }
    ]
  },
  899: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['5', '4', '3', '2', '1']\n['6', '5', '4', '3', '2', '1']" }
    ]
  },
  900: {
    functionNames: ["min_max"],
    tests: [{
      args: [[1, 2, 3, 4, 5]],
      expected: [1, 5]
    }]
  },
  901: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[10, 20, 30]" }
    ]
  },
  902: {
    functionNames: ["main"],
    tests: [
      { args: [[{"name": "jon", "age": 55}, {"name": "sam", "age": 8}]], expected: [55, 8] },
      { args: [[{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]], expected: [25, 30] }
    ]
  },
  903: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "3 + 5 - 2 * 4" }
    ]
  },
  904: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "30 10 20" }
    ]
  },
  905: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "john.doe example.com" }
    ]
  },
  906: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "1 2 3\n4 5 6" }
    ]
  },
  907: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "3 2" }
    ]
  },
  908: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], randomValues: [42], expected: "42" }
    ]
  },
  909: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], randomFloatValues: [0.25], expected: "0.25" }
    ]
  },
  910: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], randomValues: [24], expected: "24" }
    ]
  },
  911: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], randomChoiceValues: ["green"], expected: "green" }
    ]
  },
  912: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], randomShuffleValues: [[5, 4, 3, 2, 1]], expected: "[5, 4, 3, 2, 1]" }
    ]
  },
  913: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], randomSampleValues: [[3, 7, 11]], expected: "[3, 7, 11]" }
    ]
  },
  914: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], randomFloatValues: [7.5], expected: "7.5" }
    ]
  },
  915: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], randomChoiceValues: ["Q"], expected: "Q" }
    ]
  },
  916: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], randomValues: [6], expected: "6" }
    ]
  },
  917: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], randomChoiceValues: ["Heads"], expected: "Heads" }
    ]
  },
  918: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], randomChoiceValues: ["Alice", "Brown"], expected: "Alice Brown" }
    ]
  },
  919: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], randomSampleValues: [["A", "b", "3", "!", "Z", "9", "?", "q"]], expected: "Ab3!Z9?q" }
    ]
  },
  920: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], randomChoiceValues: [true], expected: "True" }
    ]
  },
  921: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], randomValues: [4, 8, 15, 16, 23], expected: "[4, 8, 15, 16, 23]" }
    ]
  },
  922: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], randomSampleValues: [[2, 4, 6, 8]], expected: "[2, 4, 6, 8]" }
    ]
  },
  923: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], randomValues: [31], expected: "2023-02-01" }
    ]
  },
  924: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], randomChoiceValues: ["banana"], expected: "banana" }
    ]
  },
  925: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], randomValues: [654321], expected: "654321" }
    ]
  },
  926: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], randomValues: [11259375], expected: "#abcdef" }
    ]
  },
  927: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], randomValues: [123, 456, 7890], expected: "(123) 456-7890" }
    ]
  },
  928: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], randomValues: [2468], expected: "2468" }
    ]
  },
  929: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], randomValues: [2, 5], expected: "2 5" }
    ]
  },
  930: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], randomValues: [192, 168, 1, 10], expected: "192.168.1.10" }
    ]
  },
  931: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], randomChoiceValues: ["A", "b", "3", "!", "Z", "9", "?", "q", "R", "7", "$", "m"], expected: "Ab3!Z9?qR7$m" }
    ]
  },
  932: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], randomChoiceValues: ["elephant"], expected: "elephant" }
    ]
  },
  933: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Cannot divide by zero" }
    ]
  },
  934: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Index out of range" }
    ]
  },
  935: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Key not found" }
    ]
  },
  936: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Invalid integer conversion" }
    ]
  },
  937: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Type mismatch error" }
    ]
  },
  938: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "File not found" }
    ]
  },
  939: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Attribute not found" }
    ]
  },
  940: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Variable not defined" }
    ]
  },
  941: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], permissionDeniedPaths: ["/root/protected.txt"], expected: "Permission denied" }
    ]
  },
  942: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Division successful: 5.0" }
    ]
  },
  943: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Execution completed\nCannot divide by zero" }
    ]
  },
  944: {
    functionNames: ["check_number"],
    tests: [
      { args: [5], expected: null },
      { args: [-5], expected: null, expectedException: "NegativeNumberError" }
    ]
  },
  945: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "An error occurred" }
    ]
  },
  946: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Negative number not allowed" }
    ]
  },
  947: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Memory limit exceeded" }
    ]
  },
  948: {
    functionNames: ["infinite_recursion"],
    tests: [
      { args: [], expected: null, expectedException: "RecursionError" }
    ]
  },
  949: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Module not found" }
    ]
  },
  950: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Error reading file" }
    ]
  },
  951: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Process interrupted by user" }
    ]
  },
  952: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "HELLO WORLD" }
    ]
  },
  953: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "3" }
    ]
  },
  954: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  955: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "I love apples. Bananas are delicious." }
    ]
  },
  956: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['Python', 'is', 'amazing']" }
    ]
  },
  957: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Python is fun" }
    ]
  },
  958: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "hello world" }
    ]
  },
  959: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "2" }
    ]
  },
  960: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[1, 2, 3, 5, 8]" }
    ]
  },
  961: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[5, 4, 3, 2, 1]" }
    ]
  },
  962: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[1, 2, 3, 4]" }
    ]
  },
  963: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[10, 20]\n30" }
    ]
  },
  964: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[5, 15, 20]" }
    ]
  },
  965: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['name', 'age', 'city']" }
    ]
  },
  966: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['Alice', 25, 'New York']" }
    ]
  },
  967: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "{'a': 1, 'b': 2, 'c': 3, 'd': 4}" }
    ]
  },
  968: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "{'name': 'Alice', 'city': 'New York'}" }
    ]
  },
  969: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  970: {
    functionNames: [],
    mode: 'script',
    compare: 'setPop',
    tests: [
      { args: [], expected: [10, 20, 30, 40] }
    ]
  },
  971: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[]" }
    ]
  },
  972: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "42" }
    ]
  },
  973: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "3.14" }
    ]
  },
  974: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  975: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[10, 20, 30, 40]" }
    ]
  },
  976: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "2024-03-22 00:00:00" }
    ]
  },
  977: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['12345', '67890']" }
    ]
  },
  978: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "{'name': 'Alice', 'age': 25, 'city': 'New York'}" }
    ]
  },
  979: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "{\"name\": \"Bob\", \"age\": 30, \"city\": \"London\"}" }
    ]
  },
  980: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Charlie" }
    ]
  },
  981: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "{'name': ['David'], 'age': ['35'], 'city': ['Paris']}" }
    ]
  },
  982: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[['name', 'age', 'city'], ['Alice', '25', 'New York'], ['Bob', '30', 'London']]" }
    ]
  },
  983: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['https://example.com', 'https://google.com']" }
    ]
  },
  984: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "14:30:45" }
    ]
  },
  985: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "26" }
    ]
  },
  986: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "10" }
    ]
  },
  987: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "35000.0" }
    ]
  },
  988: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "admin" }
    ]
  },
  989: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['Hello World']" }
    ]
  },
  990: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "{'name': 'Alice', 'age': 25, 'city': 'New York'}" }
    ]
  },
  991: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[1, 2, 3, 4, 5]" }
    ]
  },
  992: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "123.45" }
    ]
  },
  993: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Alice" }
    ]
  },
  994: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Hello" }
    ]
  },
  995: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "ming" }
    ]
  },
  996: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[30, 40, 50]" }
    ]
  },
  997: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[4, 5, 6]" }
    ]
  },
  998: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "PtoSiig" }
    ]
  },
  999: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "yhnlcn" }
    ]
  },
  1000: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "fedcba" }
    ]
  },
  1001: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[5, 4, 3, 2, 1]" }
    ]
  },
  1002: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[10, 40, 70]" }
    ]
  },
  1003: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "jhfdb" }
    ]
  },
  1004: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "cde" }
    ]
  },
  1005: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "ytho" }
    ]
  },
  1006: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "abcd" }
    ]
  },
  1007: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "efgh" }
    ]
  },
  1008: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "cd" }
    ]
  },
  1009: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[4, 5, 6]" }
    ]
  },
  1010: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "(10, 20, 30)" }
    ]
  },
  1011: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[1, 3, 5, 7]" }
    ]
  },
  1012: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "honPr" }
    ]
  },
  1013: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "(300, 400, 500, 600)" }
    ]
  },
  1014: {
        functionNames: ['is_palindrome'],
        tests: [
            { args: ["madam"], expected: true },
            { args: ["hello"], expected: false },
            { args: ["level"], expected: true },
        ]
    },
  1015: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "ing" }
    ]
  },
  1016: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[10, 20, 30, 40, 50]" }
    ]
  },
  1017: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "(5, 10, 15, 20)" }
    ]
  },
  1018: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "lloWor" }
    ]
  },
  1019: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]" }
    ]
  },
  1020: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]" }
    ]
  },
  1021: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]" }
    ]
  },
  1022: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['P', 'i', 'a', 'p', 'p', 'l']" }
    ]
  },
  1023: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['bright', 'today']" }
    ]
  },
  1024: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81), (10, 100)]" }
    ]
  },
  1025: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[6, 10, 14, 18]" }
    ]
  },
  1026: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[3, 6, 7, 9, 12, 14, 15, 18, 21, 24, 27, 28, 30, 33, 35, 36, 39, 42, 45, 48, 49, 51, 54, 56, 57, 60, 63, 66, 69, 70, 72, 75, 77, 78, 81, 84, 87, 90, 91, 93, 96, 98, 99]" }
    ]
  },
  1027: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['HELLO', 'WORLD', 'PYTHON']" }
    ]
  },
  1028: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[1, 2, 3, 4, 5, 6, 7, 8, 9]" }
    ]
  },
  1029: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['i', 'o', 'e', 'e', 'i', 'o', 'i', 'o', 'e', 'u']" }
    ]
  },
  1030: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[10, 15.5, 30]" }
    ]
  },
  1031: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]" }
    ]
  },
  1032: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]" }
    ]
  },
  1033: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['The', 'apple', 'the', 'tree']" }
    ]
  },
  1034: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['y', 't', 'h', 'o', 'n', 'i', 's', 't', 'o', 'm', 'p', 'r', 'e', 'h', 'e', 'n', 's', 'i', 'o', 'n']" }
    ]
  },
  1035: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[('List', 4), ('comprehension', 13), ('makes', 5), ('Python', 6), ('concise', 7)]" }
    ]
  },
  1036: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[1, 2, 3, 4, 5]" }
    ]
  },
  1037: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['apple', 'grape', 'peach']" }
    ]
  },
  1038: {
        functionNames: ['factorial'],
        tests: [
            { args: [0], expected: 1 },
            { args: [5], expected: 120 },
        ]
    },
  1039: {
        functionNames: ['sum_n'],
        tests: [
            { args: [5], expected: 15 },
            { args: [10], expected: 55 },
        ]
    },
  1040: {
        functionNames: ['fibonacci'],
        tests: [
            { args: [0], expected: 0 },
            { args: [6], expected: 8 },
            { args: [7], expected: 13 },
        ]
    },
  1041: {
        functionNames: ['reverse_string'],
        tests: [
            { args: ["hello"], expected: "olleh" },
            { args: ["python"], expected: "nohtyp" },
        ]
    },
  1042: {
        functionNames: ['count_digits'],
        tests: [
            { args: [7], expected: 1 },
            { args: [12345], expected: 5 },
        ]
    },
  1043: {
        functionNames: ['gcd'],
        tests: [
            { args: [12, 8], expected: 4 },
            { args: [48, 18], expected: 6 },
        ]
    },
  1044: {
        functionNames: ['list_sum'],
        tests: [
            { args: [[]], expected: 0 },
            { args: [[1,2,3,4,5]], expected: 15 },
        ]
    },
  1045: {
        functionNames: ['is_palindrome'],
        tests: [
            { args: [121], expected: true },
            { args: [123], expected: false },
            { args: [1221], expected: true },
        ]
    },
  1046: {
        functionNames: ['power'],
        tests: [
            { args: [5, 0], expected: 1 },
            { args: [2,3], expected: 8 },
        ]
    },
  1047: {
        functionNames: ['multiply'],
        tests: [
            { args: [5, 0], expected: 0 },
            { args: [4,5], expected: 20 },
        ]
    },
  1048: {
    functionNames: ["print_numbers"],
    compare: 'printedOrReturn',
    tests: [{
      args: [5],
      expected: "1\n2\n3\n4\n5"
    }]
  },
  1049: {
    functionNames: ["print_reverse"],
    compare: 'printedOrReturn',
    tests: [{
      args: [5],
      expected: "5\n4\n3\n2\n1"
    }]
  },
  1050: {
        functionNames: ['is_sorted'],
        tests: [
            { args: [[1,2,3,4,5]], expected: true },
            { args: [[1,3,2,4,5]], expected: false },
            { args: [[]], expected: true },
        ]
    },
  1051: {
        functionNames: ['char_count'],
        tests: [
            { args: ["hello","l"], expected: 2 },
            { args: ["banana", "a"], expected: 3 },
        ]
    },
  1052: {
    functionNames: ["binary_strings"],
    compare: "printedOrReturn",
    tests: [
      { args: [2], expected: "00\n01\n10\n11" }
    ]
  },
  1053: {
        functionNames: ['sum_of_digits'],
        tests: [
            { args: [123], expected: 6 },
            { args: [1244], expected: 11 },
        ]
    },
  1054: {
        functionNames: ['triangular_number'],
        tests: [
            { args: [5], expected: 15 },
        ]
    },
  1055: {
        functionNames: ['remove_duplicates'],
        tests: [
            { args: ["banana"], expected: "ban" },
            { args: ["mississippi"], expected: "misp" },
        ]
    },
  1056: {
    functionNames: ["permutations"],
    compare: "printedOrReturn",
    tests: [
      { args: ["ab"], expected: "ab\nba" }
    ]
  },
  1057: {
        functionNames: ['longest_string'],
        tests: [
            { args: [["a","abc","ab"]], expected: "abc" },
        ]
    },
  1058: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1059: {
        functionNames: ['square_roots'],
        tests: [
            { args: [[1,4,9]], expected: [1,2,3] },
        ]
    },
  1060: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1061: {
        functionNames: ['sort_by_first_element_desc'],
        tests: [
            { args: [[[3,1],[1,2],[2,3]]], expected: [[3,1],[2,3],[1,2]] },
        ]
    },
  1062: {
        functionNames: ['filter_short_words'],
        tests: [
            { args: [["a","abc","abcd","ab"],3], expected: ["abc","abcd"] },
        ]
    },
  1063: {
        functionNames: ['double_elements'],
        tests: [
            { args: [[1,2,3,4]], expected: [2,4,6,8] },
        ]
    },
  1064: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1065: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "40" }
    ]
  },
  1066: {
        functionNames: ['cube_elements'],
        tests: [
            { args: [[1,2,3,4]], expected: [1,8,27,64] },
        ]
    },
  1067: {
        functionNames: ['sort_by_length'],
        tests: [
            { args: [["abc","a","ab"]], expected: ["a","ab","abc"] },
        ]
    },
  1068: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1069: {
        functionNames: ['sum_of_elements'],
        tests: [
            { args: [[1,2,3,4,5]], expected: 15 },
        ]
    },
  1070: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1071: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "The smallest number in the list is: 7" }
    ]
  },
  1072: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1073: {
        functionNames: ['convert_to_strings'],
        tests: [
            { args: [[1,2,3]], expected: ["1","2","3"] },
        ]
    },
  1074: {
        functionNames: ['sum_of_even'],
        tests: [
            { args: [[1,2,3,4,5,6]], expected: 12 },
        ]
    },
  1075: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "helloworld" }
    ]
  },
  1076: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "3" }
    ]
  },
  1077: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "15" }
    ]
  },
  1078: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1079: {
        functionNames: ['create_square_root_tuples'],
        tests: [
            { args: [[1,4,9]], expected: [[1,1],[4,2],[9,3]] },
        ]
    },
  1080: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1081: {
        functionNames: ['average_of_odds'],
        tests: [
            { args: [[1,2,3,4,5]], expected: 3 },
        ]
    },
  1082: {
        functionNames: ['square_odd_numbers'],
        tests: [
            { args: [[1,2,3,4,5]], expected: [1,9,25] },
        ]
    },
  1083: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1084: {
        functionNames: ['create_cube_tuples'],
        tests: [
            { args: [[1,2,3]], expected: [[1,1],[2,8],[3,27]] },
        ]
    },
  1085: {
        functionNames: ['filter_greater_than'],
        tests: [
            { args: [[1,5,3,8,2],3], expected: [1,3,2] },
        ]
    },
  1086: {
        functionNames: ['convert_to_lengths'],
        tests: [
            { args: [["hi","hello","a"]], expected: [2,5,1] },
        ]
    },
  1087: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1088: {
        functionNames: ['sum_of_cubes'],
        tests: [
            { args: [[1,2,3]], expected: 36 },
        ]
    },
  1089: {
        functionNames: ['remove_elements_greater_than'],
        tests: [
            { args: [[1,5,3,8,2],4], expected: [1,3,2] },
        ]
    },
  1090: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1091: {
    functionNames: ["square_generator"],
    tests: [
      { args: [5], expected: [0, 1, 4, 9, 16] }
    ]
  },
  1092: {
    functionNames: ["fibonacci_generator"],
    tests: [
      { args: [20], expected: [0, 1, 1, 2, 3, 5, 8, 13] }
    ]
  },
  1093: {
    functionNames: ["char_generator"],
    tests: [
      { args: ["hello"], expected: ["h", "e", "l", "l", "o"] }
    ]
  },
  1094: {
    functionNames: ["step_generator"],
    tests: [
      { args: [10], expected: [1, 3, 5, 7, 9] }
    ]
  },
  1095: {
    functionNames: ["even_number_generator"],
    tests: [
      { args: [10], expected: [2, 4, 6, 8, 10] }
    ]
  },
  1096: {
    functionNames: ["square_even_generator"],
    tests: [
      { args: [10], expected: [4, 16, 36, 64, 100] }
    ]
  },
  1097: {
    functionNames: ["prime_generator"],
    tests: [
      { args: [5], expected: [2, 3, 5, 7, 11] }
    ]
  },
  1098: {
    functionNames: ["consecutive_pair_sum"],
    tests: [
      { args: [[1, 2, 3, 4, 5]], expected: [3, 5, 7, 9] }
    ]
  },
  1099: {
    functionNames: ["factorial_generator"],
    tests: [
      { args: [5], expected: [1, 2, 6, 24, 120] }
    ]
  },
  1100: {
    functionNames: ["divisible_by_3_and_5_generator"],
    tests: [
      { args: [50], expected: [15, 30, 45] }
    ]
  },
  1101: {
    functionNames: ["odd_filter_generator"],
    tests: [
      { args: [[1, 2, 3, 4, 5, 6]], expected: [2, 4, 6] },
      { args: [[7, 9, 10]], expected: [10] }
    ]
  },
  1102: {
    functionNames: ["cumulative_sum_generator"],
    tests: [
      { args: [[1, 2, 3, 4, 5]], expected: [1, 3, 6, 10, 15] },
      { args: [[10, -2, 5]], expected: [10, 8, 13] }
    ]
  },
  1103: {
    functionNames: ["power_generator"],
    tests: [
      { args: [5, 3], expected: [1, 8, 27, 64, 125] },
      { args: [4, 2], expected: [1, 4, 9, 16] }
    ]
  },
  1104: {
    functionNames: ["word_generator"],
    tests: [
      { args: ["This is a test sentence"], expected: ["This", "is", "a", "test", "sentence"] },
      { args: ["hello world"], expected: ["hello", "world"] }
    ]
  },
  1105: {
    functionNames: ["square_number_generator"],
    tests: [
      { args: [5], expected: [1, 4, 9, 16, 25] },
      { args: [3], expected: [1, 4, 9] }
    ]
  },
  1106: {
    functionNames: ["main", "square_odd_number_generator"],
    tests: [
      { functionName: "main", args: [10], expected: [1, 9, 25, 49, 81] },
      { functionName: "square_odd_number_generator", args: [7], expected: [1, 9, 25, 49] }
    ]
  },
  1107: {
    functionNames: ["reverse_list_generator"],
    tests: [
      { args: [[1, 2, 3, 4, 5]], expected: [5, 4, 3, 2, 1] },
      { args: [["a", "b"]], expected: ["b", "a"] }
    ]
  },
  1108: {
    functionNames: ["multiple_generator"],
    tests: [
      { args: [20, 3], expected: [3, 6, 9, 12, 15, 18] },
      { args: [10, 5], expected: [5, 10] }
    ]
  },
  1109: {
    functionNames: ["uppercase_generator"],
    tests: [
      { args: ["Hello World"], expected: ["H", "W"] },
      { args: ["ABCdef"], expected: ["A", "B", "C"] }
    ]
  },
  1110: {
    functionNames: ["consecutive_diff_generator"],
    tests: [
      { args: [[1, 3, 6, 10]], expected: [2, 3, 4] },
      { args: [[10, 7, 2]], expected: [-3, -5] }
    ]
  },
  1111: {
    functionNames: ["greater_than_generator"],
    tests: [
      { args: [[1, 2, 3, 4, 5, 6], 3], expected: [4, 5, 6] },
      { args: [[10, 1, 11], 10], expected: [11] }
    ]
  },
  1112: {
    functionNames: ["sum_with_index_generator"],
    tests: [
      { args: [[10, 20, 30, 40]], expected: [10, 21, 32, 43] },
      { args: [[1, 1, 1]], expected: [1, 2, 3] }
    ]
  },
  1113: {
    functionNames: ["palindrome_generator"],
    tests: [
      { args: [["madam", "apple", "racecar", "banana"]], expected: ["madam", "racecar"] },
      { args: [["noon", "cat", "level"]], expected: ["noon", "level"] }
    ]
  },
  1114: {
    functionNames: ["pair_product_generator"],
    tests: [
      { args: [[1, 2, 3, 4]], expected: [2, 6, 12] },
      { args: [[2, 5]], expected: [10] }
    ]
  },
  1115: {
    functionNames: ["greater_than_previous_generator"],
    tests: [
      { args: [[1, 2, 1, 4, 3]], expected: [2, 4] },
      { args: [[5, 6, 7]], expected: [6, 7] }
    ]
  },
  1116: {
    functionNames: ["divisible_by_generator"],
    tests: [
      { args: [[10, 15, 20, 25, 30], 5], expected: [10, 15, 20, 25, 30] },
      { args: [[2, 3, 4, 6], 2], expected: [2, 4, 6] }
    ]
  },
  1117: {
    functionNames: ["even_fibonacci_generator"],
    tests: [
      { args: [5], expected: [0, 2, 8, 34, 144] },
      { args: [3], expected: [0, 2, 8] }
    ]
  },
  1118: {
    functionNames: ["even_index_generator"],
    tests: [
      { args: [[1, 2, 3, 4, 5, 6]], expected: [1, 3, 5] },
      { args: [["a", "b", "c"]], expected: ["a", "c"] }
    ]
  },
  1119: {
    functionNames: ["even_length_word_generator"],
    tests: [
      { args: ["This is a simple test sentence"], expected: ["This", "is", "simple", "test", "sentence"] },
      { args: ["odd even four"], expected: ["even", "four"] }
    ]
  },
  1120: {
    functionNames: ["check_number"],
    tests: [{
      args: [5],
      expected: "Positive"
    }]
  },
  1121: {
    functionNames: ["largest_of_three"],
    tests: [{
      args: [1, 2, 3],
      expected: 3
    }]
  },
  1122: {
        functionNames: ['is_leap_year'],
        tests: [
            { args: [2020], expected: true },
            { args: [2021], expected: false },
        ]
    },
  1123: {
        functionNames: ['check_even_odd'],
        tests: [
            { args: [4], expected: 'Even' },
            { args: [7], expected: 'Odd' },
        ]
    },
  1124: {
        functionNames: ['divisible_by_3_and_5'],
        tests: [
            { args: [15], expected: true },
            { args: [10], expected: false },
        ]
    },
  1125: {
        functionNames: ['divisible_by_7'],
        compare: 'printedOrReturn',
        tests: [
            { args: [14], expected: '7\n14' },
            { args: [10], expected: '7' },
        ]
    },
  1126: {
        functionNames: ['is_prime'],
        tests: [
            { args: [7], expected: true },
            { args: [4], expected: false },
        ]
    },
  1127: {
        functionNames: ['factorial'],
        tests: [
            { args: [5], expected: 120 },
        ]
    },
  1128: {
        functionNames: ['is_palindrome'],
        tests: [
            { args: ["radar"], expected: true },
            { args: ["hello"], expected: false },
        ]
    },
  1129: {
    functionNames: ["count_vowels"],
    tests: [
      { args: ["hello"], expected: 2 }
    ]
  },
  1130: {
        functionNames: ['is_perfect_number'],
        tests: [
            { args: [6], expected: true },
            { args: [10], expected: false },
        ]
    },
  1131: {
        functionNames: ['is_armstrong'],
        tests: [
            { args: [153], expected: true },
            { args: [123], expected: false },
        ]
    },
  1132: {
    functionNames: ["prime_numbers_up_to_n"],
    tests: [{
      args: [5],
      expected: [2, 3, 5]
    }]
  },
  1133: {
    functionNames: ["even_and_greater_than_10"],
    tests: [{
      args: [5],
      expected: false
    }]
  },
  1134: {
    functionNames: ["find_divisors"],
    tests: [{
      args: [5],
      expected: [1, 5]
    }]
  },
  1135: {
    functionNames: ["multiplication_table"],
    compare: 'printedOrReturn',
    tests: [
      { args: [5], expected: "5 x 1 = 5\n5 x 2 = 10\n5 x 3 = 15\n5 x 4 = 20\n5 x 5 = 25\n5 x 6 = 30\n5 x 7 = 35\n5 x 8 = 40\n5 x 9 = 45\n5 x 10 = 50" }
    ]
  },
  1136: {
        functionNames: ['is_perfect_square'],
        tests: [
            { args: [16], expected: true },
            { args: [10], expected: false },
        ]
    },
  1137: {
        functionNames: ['is_power_of_2'],
        tests: [
            { args: [8], expected: true },
            { args: [10], expected: false },
        ]
    },
  1138: {
    functionNames: ["second_largest"],
    tests: [
      { args: [[3,7,2,9,5]], expected: 7 }
    ]
  },
  1139: {
        functionNames: ['is_power_of_3'],
        tests: [
            { args: [9], expected: true },
            { args: [10], expected: false },
        ]
    },
  1140: {
    functionNames: ["fibonacci_up_to_n"],
    compare: 'printedOrReturn',
    tests: [
      { args: [20], expected: "0 1 1 2 3 5 8 13" },
      { args: [5], expected: "0 1 1 2 3 5" }
    ]
  },
  1141: {
    functionNames: ["count_occurrences"],
    tests: [
      { args: [[1,2,2,3],2], expected: 2 }
    ]
  },
  1142: {
    functionNames: ["is_perfect_square_and_armstrong"],
    tests: [
      { args: [1], expected: true },
      { args: [153], expected: false },
      { args: [16], expected: false }
    ]
  },
  1143: {
    functionNames: ["divisible_by_7_and_11"],
    tests: [{
      args: [1, 5],
      expected: []
    }]
  },
  1144: {
    functionNames: ["factorial_while"],
    tests: [{
      args: [5],
      expected: 120
    }]
  },
  1145: {
        functionNames: ['reverse_list'],
        tests: [
            { args: [[1,2,3,4]], expected: [4,3,2,1] },
        ]
    },
  1146: {
        functionNames: ['divisible_by_5_or_10'],
        tests: [
            { args: [10], expected: true },
            { args: [7], expected: false },
        ]
    },
  1147: {
    functionNames: ["divisible_by_any_number"],
    tests: [{
      args: [5, [1, 2, 3, 4, 5]],
      expected: true
    }]
  },
  1148: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "10" }
    ]
  },
  1149: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Local variable: 10\nGlobal variable: 20" }
    ]
  },
  1150: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "30" }
    ]
  },
  1151: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "20" }
    ]
  },
  1152: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Local x: 50\nGlobal x: 100" }
    ]
  },
  1153: {
    functionNames: ["example_function"],
    compare: 'printedOrReturn',
    tests: [{
      args: [1, 2],
      expected: "The sum of 1 and 2 is 3"
    }]
  },
  1154: {
        functionNames: ['greet'],
        tests: [
            { args: ["Alice"], expected: "Hello, Alice!" },
        ]
    },
  1155: {
    functionNames: ["modify_list"],
    compare: 'printedOrReturn',
    tests: [{
      args: [[1, 2, 3, 4, 5]],
      expected: "Modified list: [1, 2, 3, 4, 5, 4]"
    }]
  },
  1156: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Inside loop: 0\nInside loop: 1\nInside loop: 2\nOutside loop: 2" }
    ]
  },
  1157: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "x is not defined" }
    ]
  },
  1158: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Inner function: x = 10, y = 20\nOuter function: x = 10" }
    ]
  },
  1159: {
        functionNames: ['add_numbers'],
        tests: [
            { args: [2,3], expected: 5 },
        ]
    },
  1160: {
    functionNames: ["append_to_list"],
    tests: [{
      args: [5, [1, 2, 3, 4, 5]],
      expected: [1, 2, 3, 4, 5, 5]
    }]
  },
  1161: {
    functionNames: ["square_numbers"],
    tests: [{
      args: [[1, 2, 3, 4, 5]],
      expected: [1, 4, 9, 16, 25]
    }]
  },
  1162: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "New value of x: 10" }
    ]
  },
  1163: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Function One: 50\nFunction Two: 40" }
    ]
  },
  1164: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Global variable x: 12" }
    ]
  },
  1165: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Inner function: x = 25\nOuter function: x = 25" }
    ]
  },
  1166: {
    functionNames: ["print_arguments"],
    compare: 'printedOrReturn',
    tests: [{
      args: ["{1, 2, 3}"],
      expected: "{1, 2, 3}"
    }]
  },
  1167: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "In the loop: y = 0\nIn the loop: y = 1\nIn the loop: y = 2\nAfter the loop: y = 2" }
    ]
  },
  1168: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Global variable x inside function: 10" }
    ]
  },
  1169: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Mutable variable: [100, 2, 3]\nImmutable variable: 20" }
    ]
  },
  1170: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "List comprehension result: [0, 1, 4, 9, 16]" }
    ]
  },
  1171: {
    functionNames: ["print_variable_in_function"],
    compare: 'printedOrReturn',
    tests: [{
      args: [5],
      expected: "Function variable y: 10"
    }]
  },
  1172: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "In the loop: x = 0\nIn the loop: x = 1\nIn the loop: x = 2\nOutside the loop: x = 2" }
    ]
  },
  1173: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Global x after modification: 50" }
    ]
  },
  1174: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Inner function: x = 5, y = 10, z = 15" }
    ]
  },
  1175: {
    functionNames: ["print_global_variable"],
    compare: 'printedOrReturn',
    tests: [{
      args: [5],
      expected: "Global x inside function: 5"
    }]
  },
  1176: {
        functionNames: ['factorial_recursive'],
        tests: [
            { args: [5], expected: 120 },
        ]
    },
  1177: {
        functionNames: ['calculate_square_root'],
        tests: [
            { args: [16], expected: 4 },
        ]
    },
  1178: {
        functionNames: ['generate_random_number'],
        compare: 'numberRange',
        tests: [
            { args: [], expected: [1, 100] },
        ]
    },
  1179: {
        functionNames: ['current_datetime'],
        compare: 'typeName',
        tests: [
            { args: [], expected: "datetime" },
        ]
    },
  1180: {
        functionNames: ['current_working_directory'],
        compare: 'typeName',
        tests: [
            { args: [], expected: "str" },
        ]
    },
  1181: {
        functionNames: ['python_version'],
        compare: 'typeName',
        tests: [
            { args: [], expected: "str" },
        ]
    },
  1182: {
    functionNames: ["dict_to_json"],
    tests: [{
      args: [],
      expected: "{\"name\": \"Alice\", \"age\": 30}"
    }]
  },
  1183: {
        functionNames: ['contains_number'],
        tests: [
            { args: ["abc123"], expected: true },
            { args: ["abc"], expected: false },
        ]
    },
  1184: {
        functionNames: ['list_files'],
        compare: 'unorderedList',
        tests: [
            { args: ["grader_files"], setupRemove: ["grader_files"], setupFiles: { "grader_files/a.txt": "a", "grader_files/b.txt": "b" }, expected: ["a.txt", "b.txt"] },
        ]
    },
  1185: {
        functionNames: ['calculate_factorial'],
        tests: [
            { args: [5], expected: 120 },
        ]
    },
  1186: {
    functionNames: ["measure_time"],
    compare: 'numberRange',
    tests: [{
      args: [],
      expected: [0, 5]
    }]
  },
  1187: {
        functionNames: ['is_leap_year'],
        tests: [
            { args: [2020], expected: true },
            { args: [2021], expected: false },
        ]
    },
  1188: {
        functionNames: ['get_pi_value'],
        compare: 'float',
        tests: [
            { args: [], expected: 3.141592653589793 },
        ]
    },
  1189: {
        functionNames: ['shuffle_list'],
        compare: 'unorderedList',
        tests: [
            { args: [[1, 2, 3, 4, 5]], expected: [1, 2, 3, 4, 5] },
        ]
    },
  1190: {
    functionNames: ["count_occurrences"],
    tests: [
      { args: [[1,2,2,3]], expected: {"1": 1, "2": 2, "3": 1} }
    ]
  },
  1191: {
        functionNames: ['calculate_gcd'],
        tests: [
            { args: [12,8], expected: 4 },
        ]
    },
  1192: {
        functionNames: ['rename_file'],
        tests: [
            { args: ["old_file.txt", "new_file.txt"], setupRemove: ["new_file.txt"], setupFiles: { "old_file.txt": "renamed content" }, getFiles: ["new_file.txt", "old_file.txt"], expected: { "new_file.txt": "renamed content", "old_file.txt": null } },
        ]
    },
  1193: {
        functionNames: ['format_current_date'],
        compare: 'length',
        tests: [
            { args: [], expected: 10 },
        ]
    },
  1194: {
    functionNames: ["json_to_dict"],
    tests: [
      { args: ['{"name": "Bob", "age": 25}'], expected: { name: "Bob", age: 25 } },
      { args: ['{"ok": true, "count": 3}'], expected: { ok: true, count: 3 } }
    ]
  },
  1195: {
        functionNames: ['select_random_element'],
        tests: [
            { args: [[7]], expected: 7 },
        ]
    },
  1196: {
        functionNames: ['round_number'],
        tests: [
            { args: [3.14159], expected: 3 },
        ]
    },
  1197: {
        functionNames: ['access_value'],
        tests: [
            { args: [], expected: 'Alice' },
        ]
    },
  1198: {
        functionNames: ['add_key_value'],
        tests: [
            { args: [], expected: {"name": "Alice", "age": 30, "city": "New York"} },
        ]
    },
  1199: {
        functionNames: ['remove_key'],
        tests: [
            { args: [], expected: {"name": "Alice", "age": 30} },
        ]
    },
  1200: {
    functionNames: ["get_keys"],
    tests: [{
      args: [],
      expected: ['name', 'age', 'city']
    }]
  },
  1201: {
    functionNames: ["get_values"],
    tests: [{
      args: [],
      expected: ['Alice', 30, 'New York']
    }]
  },
  1202: {
        functionNames: ['check_key'],
        tests: [
            { args: [], expected: true },
        ]
    },
  1203: {
        functionNames: ['get_value'],
        tests: [
            { args: [{"a":1,"b":2},"a"], expected: 1 },
        ]
    },
  1204: {
        functionNames: ['clear_dict'],
        tests: [
            { args: [], expected: {} },
        ]
    },
  1205: {
        functionNames: ['copy_dict'],
        tests: [
            { args: [], expected: {"name": "Alice", "age": 30} },
        ]
    },
  1206: {
        functionNames: ['merge_dicts'],
        tests: [
            { args: [], expected: {"name": "Alice", "age": 30, "city": "New York", "job": "Engineer"} },
        ]
    },
  1207: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "name: Alice\nage: 30\ncity: New York" }
    ]
  },
  1208: {
        functionNames: ['dict_length'],
        tests: [
            { args: [], expected: 3 },
        ]
    },
  1209: {
        functionNames: ['reverse_dict'],
        tests: [
            { args: [], expected: {"Alice": "name", "30": "age", "New York": "city"} },
        ]
    },
  1210: {
        functionNames: ['create_dict_from_lists'],
        tests: [
            { args: [], expected: {"name": "Alice", "age": 30, "city": "New York"} },
        ]
    },
  1211: {
        functionNames: ['sum_values'],
        tests: [
            { args: [], expected: 60 },
        ]
    },
  1212: {
    functionNames: ["filter_dict"],
    tests: [{
      args: [],
      expected: {"name": "Alice", "city": "New York"}
    }]
  },
  1213: {
        functionNames: ['max_value'],
        tests: [
            { args: [], expected: 30 },
        ]
    },
  1214: {
        functionNames: ['is_dict_empty'],
        tests: [
            { args: [], expected: true },
        ]
    },
  1215: {
    functionNames: ["remove_value"],
    tests: [{
      args: [],
      expected: {"b": 20}
    }]
  },
  1216: {
    functionNames: ["find_key_by_value"],
    tests: [{
      args: [],
      expected: ["b"]
    }]
  },
  1217: {
    functionNames: ["create_defaultdict"],
    tests: [{
      args: [],
      expected: {"a": 1, "b": 2}
    }]
  },
  1218: {
        functionNames: ['first_key_value'],
        tests: [
            { args: [], expected: ["a", 10] },
        ]
    },
  1219: {
        functionNames: ['merge_multiple_dicts'],
        tests: [
            { args: [], expected: {"a": 10, "b": 20, "c": 30, "d": 40, "e": 50} },
        ]
    },
  1220: {
    functionNames: ["list_to_dict"],
    tests: [{
      args: [],
      expected: {"a": 1, "b": 2, "c": 3}
    }]
  },
  1221: {
    functionNames: ["create_path"],
    tests: [{
      args: [],
      expected: "example_directory"
    }]
  },
  1222: {
    functionNames: ["check_path_exists"],
    tests: [{
      args: [],
      expected: false
    }]
  },
  1223: {
    functionNames: ["check_if_file"],
    tests: [{
      args: [],
      expected: false
    }]
  },
  1224: {
    functionNames: ["check_if_directory"],
    tests: [{
      args: [],
      expected: false
    }]
  },
  1225: {
    functionNames: ["get_file_name"],
    tests: [{
      args: [],
      expected: "example_file.txt"
    }]
  },
  1226: {
    functionNames: ["get_parent_directory"],
    tests: [{
      args: [],
      expected: "example_directory"
    }]
  },
  1227: {
    functionNames: ["join_paths"],
    tests: [{
      args: [],
      expected: "example_directory/example_file.txt"
    }]
  },
  1228: {
    functionNames: ["get_file_extension"],
    tests: [{
      args: [],
      expected: ".txt"
    }]
  },
  1229: {
        functionNames: ['get_file_size'],
        tests: [
            { args: [], setupFiles: { "example_file.txt": "hello" }, expected: 5 },
        ]
    },
  1230: {
        functionNames: ['rename_file'],
        tests: [
            { args: [], setupRemove: ["new_file.txt"], setupFiles: { "old_file.txt": "renamed content" }, getFiles: ["new_file.txt", "old_file.txt"], expected: { "new_file.txt": "renamed content", "old_file.txt": null } },
        ]
    },
  1231: {
    functionNames: ["create_directory"],
    tests: [{
      args: [],
      expected: "new_directory"
    }]
  },
  1232: {
    functionNames: ["remove_directory"],
    tests: [{
      args: [],
      setupRemove: ["new_directory"],
      setupDirs: ["new_directory"],
      expected: "Directory new_directory removed"
    }]
  },
  1233: {
        functionNames: ['remove_file'],
        tests: [
            { args: [], setupFiles: { "example_file.txt": "remove me" }, getFiles: ["example_file.txt"], expected: { "example_file.txt": null } },
        ]
    },
  1234: {
    functionNames: ["get_absolute_path"],
    compare: 'printedOrReturn',
    tests: [{
      args: [],
      expected: "example_file.txt"
    }]
  },
  1235: {
    functionNames: ["check_if_symlink"],
    tests: [{
      args: [],
      expected: false
    }]
  },
  1236: {
        functionNames: ['create_symlink'],
        tests: [
            { args: [], setupRemove: ["example_symlink"], setupFiles: { "example_file.txt": "target" }, callMethod: "is_symlink", expected: true },
        ]
    },
  1237: {
    functionNames: ["check_directory_and_files"],
    tests: [{
      args: [],
      expected: []
    }]
  },
  1238: {
        functionNames: ['get_last_modified_time'],
        compare: 'length',
        tests: [
            { args: [], setupFiles: { "example_file.txt": "timestamp" }, expected: 24 },
        ]
    },
  1239: {
    functionNames: ["get_directory_name"],
    tests: [{
      args: [],
      expected: "example_directory"
    }]
  },
  1240: {
        functionNames: ['check_if_empty'],
        tests: [
            { args: [], setupRemove: ["example_directory"], setupDirs: ["example_directory"], expected: true },
        ]
    },
  1241: {
        functionNames: ['iterate_files'],
        compare: 'unorderedList',
        tests: [
            { args: [], setupRemove: ["example_directory"], setupFiles: { "example_directory/a.txt": "a", "example_directory/b.txt": "b" }, expected: ["a.txt", "b.txt"] },
        ]
    },
  1242: {
    functionNames: ["get_parent_directory"],
    tests: [{
      args: [],
      expected: "."
    }]
  },
  1243: {
    functionNames: ["check_file_extension"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1244: {
        functionNames: ['get_human_readable_size'],
        tests: [
            { args: [], setupFiles: { "example_file.txt": "x".repeat(2048) }, expected: "2.00 KB" },
        ]
    },
  1245: {
        functionNames: ['change_working_directory'],
        tests: [
            { args: [], setupRemove: ["example_directory"], setupDirs: ["example_directory"], expected: "Changed working directory to: example_directory" },
        ]
    },
  1246: {
    functionNames: ["check_conditions"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1247: {
    functionNames: ["check_range"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1248: {
    functionNames: ["check_string"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1249: {
    functionNames: ["main"],
    tests: [{
      args: [5],
      expected: false
    }]
  },
  1250: {
    functionNames: ["check_list"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1251: {
    functionNames: ["check_leap_year"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1252: {
    functionNames: ["check_number"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1253: {
    functionNames: ["check_list_conditions"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1254: {
    functionNames: ["check_string_conditions"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1255: {
    functionNames: ["check_range_conditions"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1256: {
    functionNames: ["check_multiples"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1257: {
    functionNames: ["check_voting_eligibility"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1258: {
    functionNames: ["check_divisibility_all"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1259: {
    functionNames: ["check_dict_conditions"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1260: {
    functionNames: ["check_string_length"],
    tests: [{
      args: [],
      expected: false
    }]
  },
  1261: {
    functionNames: ["check_range_inclusive"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1262: {
    functionNames: ["check_divisible_by_2_and_7"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1263: {
    functionNames: ["check_negative_and_divisible"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1264: {
    functionNames: ["check_digit_string"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1265: {
    functionNames: ["check_prime_and_greater_than_10"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1266: {
    functionNames: ["check_odd_and_positive"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1267: {
    functionNames: ["check_file_exists_and_size"],
    tests: [{
      args: [],
      expected: false
    }]
  },
  1268: {
    functionNames: ["check_list_length_and_last_element"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1269: {
    functionNames: ["check_range_and_odd"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1270: {
    functionNames: ["check_conditions"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1271: {
    functionNames: ["check_range"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1272: {
    functionNames: ["check_string"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1273: {
    functionNames: ["check_divisibility"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1274: {
    functionNames: ["check_list"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1275: {
    functionNames: ["check_leap_year"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1276: {
    functionNames: ["check_number"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1277: {
    functionNames: ["check_string_conditions"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1278: {
    functionNames: ["check_conditions"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1279: {
    functionNames: ["check_multiples"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1280: {
    functionNames: ["check_voting_eligibility"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1281: {
    functionNames: ["check_divisibility_all"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1282: {
    functionNames: ["check_dict_conditions"],
    tests: [{
      args: [],
      expected: false
    }]
  },
  1283: {
    functionNames: ["check_string_empty_or_number"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1284: {
    functionNames: ["check_negative_or_divisible_by_3"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1285: {
    functionNames: ["check_list_conditions"],
    tests: [{
      args: [],
      expected: false
    }]
  },
  1286: {
    functionNames: ["check_perfect_square_or_cube"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1287: {
    functionNames: ["check_string_type"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1288: {
    functionNames: ["check_list_conditions"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1289: {
    functionNames: ["check_divisible_by_2_or_5"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1290: {
    functionNames: ["check_file_conditions"],
    tests: [{
      args: [],
      expected: false
    }]
  },
  1291: {
    functionNames: ["check_number"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1292: {
    functionNames: ["check_string_conditions"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1293: {
    functionNames: ["check_list_conditions"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1294: {
    functionNames: ["check_even_or_divisible_by_3"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1295: {
    functionNames: ["check_string"],
    tests: [{
      args: [],
      expected: true
    }]
  },
  1296: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['Hello', 'World', 'Python']" }
    ]
  },
  1297: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['apple', 'banana', 'cherry', 'grape']" }
    ]
  },
  1298: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1299: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['alice@example.com', 'bob99@domain.co.uk']" }
    ]
  },
  1300: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['#Python', '#coding']" }
    ]
  },
  1301: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['example.com', 'test.org']" }
    ]
  },
  1302: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1303: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Hello world Python is great" }
    ]
  },
  1304: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1328: {
    functionNames: [],
    mode: 'script',
    compare: 'unorderedList',
    tests: [
      { args: [], expected: ["r", "g", "m"] }
    ]
  },
  1305: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['2024-06-01', '2025-07-04']" }
    ]
  },
  1306: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1307: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['running', 'jumping', 'singing']" }
    ]
  },
  1308: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "pdf" }
    ]
  },
  1309: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['is', 'test']" }
    ]
  },
  1310: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['Alice', 'Bob', 'New', 'York', 'City', 'Monday']" }
    ]
  },
  1311: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1312: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['21.5', '60', '0.25']" }
    ]
  },
  1313: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "192.168.1.1" }
    ]
  },
  1314: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1315: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['with content', 'another one']" }
    ]
  },
  1316: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['<div>', '<p>', '</p>', '</div>']" }
    ]
  },
  1317: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1318: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['U.S.A.', 'E.U.']" }
    ]
  },
  1319: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "3" }
    ]
  },
  1320: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "This is a spaced sentence." }
    ]
  },
  1321: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1322: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "john.doe" }
    ]
  },
  1323: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "1,000,000" }
    ]
  },
  1324: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['@python', '@realpython', '@openai']" }
    ]
  },
  1325: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1326: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['02:30 PM', '07:45 AM']" }
    ]
  },
  1327: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['$20.99', '$3.50', '$100']" }
    ]
  },
  1329: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1330: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['Hello', 'How are you?']" }
    ]
  },
  1331: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1332: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1333: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1334: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1335: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1336: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1337: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1338: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[1, 4]" }
    ]
  },
  1339: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['apple', 'banana']" }
    ]
  },
  1340: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1341: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1342: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1343: {
        functionNames: ['greet'],
        tests: [
            { args: ["Alice"], expected: "Hello, Alice!" },
        ]
    },
  1344: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1345: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[1, 2, 3]\n['one', 'two', 'three']" }
    ]
  },
  1346: {
        functionNames: ['multiply'],
        tests: [
            { args: [4,5], expected: 20 },
        ]
    },
  1347: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1348: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1349: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1350: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1351: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "{'a': 1, 'c': 3}" }
    ]
  },
  1352: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "10" }
    ]
  },
  1353: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[1, 2, 3]" }
    ]
  },
  1354: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[10, 30, 40]" }
    ]
  },
  1355: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "7" }
    ]
  },
  1356: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "3\n2\n1" }
    ]
  },
  1357: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "List is empty" }
    ]
  },
  1358: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Not Found" }
    ]
  },
  1359: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Key not found" }
    ]
  },
  1360: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "('k2', 2)\n('k1', 1)" }
    ]
  },
  1361: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "3" }
    ]
  },
  1362: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "10" }
    ]
  },
  1363: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "6" }
    ]
  },
  1364: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Alice" }
    ]
  },
  1365: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[1, 2]" }
    ]
  },
  1366: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "500" }
    ]
  },
  1367: {
        functionNames: ['remove_key'],
        tests: [
            { args: [{"a":1,"b":2},"a"], expected: 1 },
            { args: [{"a":1},"missing"], expected: null },
        ]
    },
  1368: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[7]" }
    ]
  },
  1369: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "save" }
    ]
  },
  1370: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[5, 6]" }
    ]
  },
  1371: {
    functionNames: ['print_kwargs'],
    compare: 'printedOrReturn',
    tests: [
      { args: [], kwargs: { a: 1, b: 2 }, expected: "{'a': 1, 'b': 2}" }
    ]
  },
  1372: {
    functionNames: ['display_kwargs'],
    compare: 'printedOrReturn',
    tests: [
      { args: [], kwargs: { name: 'Alice', age: 30 }, expected: "name: Alice\nage: 30" }
    ]
  },
  1373: {
    functionNames: ['count_kwargs'],
    compare: 'printedOrReturn',
    tests: [
      { args: [], kwargs: { a: 1, b: 2, c: 3 }, expected: "3" }
    ]
  },
  1374: {
    functionNames: ['kwargs_keys'],
    tests: [
      { args: [], kwargs: { x: 10, y: 20 }, expected: ['x', 'y'] }
    ]
  },
  1375: {
    functionNames: ['kwargs_values'],
    tests: [
      { args: [], kwargs: { x: 10, y: 20 }, expected: [10, 20] }
    ]
  },
  1376: {
    functionNames: ['has_id'],
    tests: [
      { args: [], kwargs: { name: 'A', id: 123 }, expected: true },
      { args: [], kwargs: { name: 'A' }, expected: false }
    ]
  },
  1377: {
    functionNames: ['get_name'],
    tests: [
      { args: [], kwargs: { age: 22 }, expected: 'Unknown' },
      { args: [], kwargs: { name: 'Dana' }, expected: 'Dana' }
    ]
  },
  1378: {
    functionNames: ['sum_kwargs'],
    compare: 'float',
    tests: [
      { args: [], kwargs: { a: 10, b: 5.5, c: 'x' }, expected: 15.5 }
    ]
  },
  1379: {
    functionNames: ['string_kwargs'],
    tests: [
      { args: [], kwargs: { a: 'hi', b: 2, c: 'hello' }, expected: { a: 'hi', c: 'hello' } }
    ]
  },
  1380: {
        functionNames: ['greet'],
        compare: 'printedOrReturn',
        tests: [
            { args: [], kwargs: { name: 'Bob', age: 40 }, expected: "Hello Bob, age 40" },
        ]
    },
  1381: {
    functionNames: ['update_dict'],
    tests: [
      { args: [{ x: 1 }], kwargs: { y: 2, z: 3 }, expected: { x: 1, y: 2, z: 3 } }
    ]
  },
  1382: {
        functionNames: ['merge_dicts'],
        tests: [
            { args: [{ a: 1 }], kwargs: { b: 2 }, expected: { a: 1, b: 2 } },
        ]
    },
  1383: {
    functionNames: ['even_kwargs'],
    compare: 'printedOrReturn',
    tests: [
      { args: [], kwargs: { a: 1, b: 2, c: 4 }, expected: "b: 2\nc: 4" }
    ]
  },
  1384: {
    functionNames: ['sorted_kwargs'],
    compare: 'printedOrReturn',
    tests: [
      { args: [], kwargs: { z: 9, a: 1, m: 5 }, expected: "a: 1\nm: 5\nz: 9" }
    ]
  },
  1385: {
    functionNames: ['count_strings'],
    compare: 'printedOrReturn',
    tests: [
      { args: [], kwargs: { a: 'one', b: 2, c: 'three' }, expected: "2" }
    ]
  },
  1386: {
    functionNames: ['check_truthy'],
    compare: 'printedOrReturn',
    tests: [
      { args: [], kwargs: { a: 0, b: 'hello', c: [] }, expected: "a: Falsy\nb: Truthy\nc: Falsy" }
    ]
  },
  1387: {
    functionNames: ['starts_with_a'],
    compare: 'printedOrReturn',
    tests: [
      { args: [], kwargs: { apple: 1, banana: 2, ant: 3 }, expected: "apple: 1\nant: 3" }
    ]
  },
  1388: {
    functionNames: ['reverse_kwargs'],
    tests: [
      { args: [], kwargs: { a: 1, b: 2 }, expected: { 1: 'a', 2: 'b' } }
    ]
  },
  1389: {
    functionNames: ['longest_key'],
    tests: [
      { args: [], kwargs: { short: 1, muchlonger: 2 }, expected: 'muchlonger' }
    ]
  },
  1390: {
    functionNames: ['stringify_kwargs'],
    tests: [
      { args: [], kwargs: { x: 10, y: 20 }, expected: 'x=10, y=20' }
    ]
  },
  1391: {
    functionNames: ['all_ints'],
    tests: [
      { args: [], kwargs: { a: 1, b: 2 }, expected: true },
      { args: [], kwargs: { a: 1, b: '2' }, expected: false }
    ]
  },
  1392: {
    functionNames: ['max_numeric'],
    compare: 'float',
    tests: [
      { args: [], kwargs: { a: 1, b: 3.5, c: 'x' }, expected: 3.5 }
    ]
  },
  1393: {
    functionNames: ['count_none'],
    tests: [
      { args: [], kwargs: { a: null, b: 1, c: null }, expected: 2 }
    ]
  },
  1394: {
    functionNames: ['print_types'],
    compare: 'printedOrReturn',
    tests: [
      { args: [], kwargs: { a: 1, b: 'str', c: 3.14 }, expected: "a: int\nb: str\nc: float" }
    ]
  },
  1395: {
    functionNames: ['kv_pairs'],
    tests: [
      { args: [], kwargs: { a: 1, b: 2 }, expected: [['a', 1], ['b', 2]] }
    ]
  },
  1396: {
    functionNames: ['remove_falsy'],
    tests: [
      { args: [], kwargs: { a: 0, b: 1, c: '' }, expected: { b: 1 } }
    ]
  },
  1397: {
    functionNames: ['has_list'],
    tests: [
      { args: [], kwargs: { a: [1, 2], b: 'x' }, expected: true },
      { args: [], kwargs: { a: 1, b: 'x' }, expected: false }
    ]
  },
  1398: {
    functionNames: ['even_or_odd_kwargs'],
    compare: 'printedOrReturn',
    tests: [
      { args: [], kwargs: { a: 1, b: 2, c: 3 }, expected: "Odd" },
      { args: [], kwargs: { a: 1, b: 2 }, expected: "Even" }
    ]
  },
  1399: {
    functionNames: ['clean_temp_keys'],
    tests: [
      { args: [], kwargs: { temp_x: 1, y: 2 }, expected: { x: 1, y: 2 } }
    ]
  },
  1400: {
    functionNames: ['uppercase_keys_only'],
    tests: [
      { args: [], kwargs: { AGE: 30, name: 'Ann' }, expected: { AGE: 30 } }
    ]
  },
  1402: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "0: apple\n1: banana\n2: cherry" }
    ]
  },
  1403: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[('Alice', 25), ('Bob', 30), ('Charlie', 35)]" }
    ]
  },
  1404: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "{1: 'a', 2: 'b', 3: 'c'}" }
    ]
  },
  1405: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1406: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[1, 2, 3, 4, 5, 6, 7, 8, 9]" }
    ]
  },
  1407: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['HELLO', 'WORLD', 'PYTHON']" }
    ]
  },
  1408: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[2, 4, 6, 8, 10]" }
    ]
  },
  1409: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[1, 2, 3, 4, 5]" }
    ]
  },
  1410: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Python is great" }
    ]
  },
  1411: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "nohtyP" }
    ]
  },
  1412: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})" }
    ]
  },
  1413: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[1, 2, 3, 4, 5, 6, 7, 8, 9]" }
    ]
  },
  1414: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Hello World Python" }
    ]
  },
  1415: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[(1, 4, 7), (2, 5, 8), (3, 6, 9)]" }
    ]
  },
  1416: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Alice Unknown" }
    ]
  },
  1417: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "{'fruit': ['apple', 'banana', 'cherry'], 'vegetable': ['carrot']}" }
    ]
  },
  1418: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "{1: [1, 1, 1], 2: [2, 2], 3: [3, 3, 3, 3], 4: [4]}" }
    ]
  },
  1419: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "he112 w2r1d" }
    ]
  },
  1420: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "first" }
    ]
  },
  1421: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')]" }
    ]
  },
  1422: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "1 [2, 3]" }
    ]
  },
  1423: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "hello world:python" }
    ]
  },
  1424: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]" }
    ]
  },
  1425: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Continues after exception" }
    ]
  },
  1426: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1427: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "14" }
    ]
  },
  1428: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "{2, 3}" }
    ]
  },
  1429: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "{1, 2, 3, 4}" }
    ]
  },
  1430: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1431: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[3, 2, 1]" }
    ]
  },
  1432: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[('a', 1), ('b', 2)]" }
    ]
  },
  1433: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "1" }
    ]
  },
  1434: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "{2: ['hi', 'no'], 5: ['hello'], 3: ['yes']}" }
    ]
  },
  1435: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[(2, 1), (4, 2), (1, 3)]" }
    ]
  },
  1436: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Hello" }
    ]
  },
  1437: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "5" }
    ]
  },
  1438: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "1 2 3" }
    ]
  },
  1439: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "{'a': 1, 'b': 2}" }
    ]
  },
  1440: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "{'a': 1}" }
    ]
  },
  1441: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1442: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Key not found" }
    ]
  },
  1443: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "1 2" }
    ]
  },
  1444: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1445: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Counter({'a': 3, 'n': 2, 'b': 1})" }
    ]
  },
  1446: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[1, 3]" }
    ]
  },
  1447: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1448: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "1" }
    ]
  },
  1449: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "{'b': 15}" }
    ]
  },
  1450: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "{1: 'a', 2: 'b'}" }
    ]
  },
  1451: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1452: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1453: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1454: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1455: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1456: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1457: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1458: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1459: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1460: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1461: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1462: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1463: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1464: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1465: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1466: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1467: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1469: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1470: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1471: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1472: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1473: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1474: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1475: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1476: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1477: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1478: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1480: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1481: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1482: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1483: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Assertion passed" }
    ]
  },
  1484: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1486: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1487: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "False" }
    ]
  },
  1488: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1489: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True" }
    ]
  },
  1490: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "True\nFalse" }
    ]
  },
  1491: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "0" }
    ]
  },
  1492: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "-1" }
    ]
  },
  1493: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "None" }
    ]
  },
  1494: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "-1" }
    ]
  },
  1495: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "No item" }
    ]
  },
  1496: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "None" }
    ]
  },
  1497: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "-1" }
    ]
  },
  1498: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Not found" }
    ]
  },
  1499: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "empty" }
    ]
  },
  1500: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Empty" }
    ]
  },
  1501: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "0" }
    ]
  },
  1502: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Missing" }
    ]
  },
  1503: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "No scores" }
    ]
  },
  1504: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Not found" }
    ]
  },
  1505: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "None" }
    ]
  },
  1506: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "No match" }
    ]
  },
  1507: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "-99" }
    ]
  },
  1508: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "No data" }
    ]
  },
  1509: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Nothing" }
    ]
  },
  1510: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "N/A" }
    ]
  },
  1511: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[]" }
    ]
  },
  1512: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "{'age': 20}" }
    ]
  },
  1513: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "python" }
    ]
  },
  1514: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Alice Unknown" }
    ]
  },
  1515: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "{'apple': 3, 'banana': 2, 'cherry': 1}" }
    ]
  },
  1516: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "{'items': ['apple', 'banana']}" }
    ]
  },
  1517: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "8" }
    ]
  },
  1518: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "{'fruit': ['apple', 'banana'], 'vegetable': ['carrot']}" }
    ]
  },
  1519: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Alice" }
    ]
  },
  1520: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "hi" }
    ]
  },
  1521: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "{'user': {'profile': {'name': 'Alice'}}}" }
    ]
  },
  1522: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "(2, 8)" }
    ]
  },
  1523: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "{'a': [1, 2], 'b': [1, 3]}" }
    ]
  },
  1524: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "100" }
    ]
  },
  1525: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "-1" }
    ]
  },
  1526: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['apple', 'banana']" }
    ]
  },
  1527: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "25" }
    ]
  },
  1528: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "{'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}" }
    ]
  },
  1529: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['apple', 'banana'] []" }
    ]
  },
  1530: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "python" }
    ]
  },
  1531: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "{'count': 1}" }
    ]
  },
  1533: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "{'h': 1, 'e': 1, 'l': 2, 'o': 1}" }
    ]
  },
  1534: {
    functionNames: [],
    mode: 'script',
    tests: [
      { args: [], expected: {'a': 1, 'b': 5, 'c': 4} }
    ]
  },
  1535: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "85.5" }
    ]
  },
  1536: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "{'fruits': ['apple', 'banana'], 'vegetables': ['carrot']}" }
    ]
  },
  1537: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "999" }
    ]
  },
  1538: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "{'a': {'x': 2, 'y': 1}, 'b': {'x': 1}}" }
    ]
  },
  1539: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Alice Smith" }
    ]
  },
  1540: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "7" }
    ]
  },
  1541: {
    functionNames: [],
    mode: 'script',
    compare: 'dictUnorderedLists',
    tests: [
      { args: [], expected: { tags: ["python", "programming"] } }
    ]
  },
  1542: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "{'name': 'Bob', 'age': 25}" }
    ]
  },
  1543: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "{'category': 'apple banana', 'type': 'fruit'}" }
    ]
  },
  1544: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[1, 2, 3, 4, 5]" }
    ]
  },
  1545: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "2023-03-01 00:00:00" }
    ]
  },
  1546: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "{'users': {'alice': {'age': 30}, 'bob': {'age': 25}}}" }
    ]
  },
  1547: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "1 END" }
    ]
  },
  1548: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "{'item1': {'count': 1, 'total': 10}, 'item2': {'count': 1, 'total': 20}}" }
    ]
  },
  1550: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "120" }
    ]
  },
  1551: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "50" }
    ]
  },
  1553: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]" }
    ]
  },
  1554: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]" }
    ]
  },
  1555: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['red', 'green', 'blue', 'red', 'green']" }
    ]
  },
  1556: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "['hello', 'hello', 'hello']" }
    ]
  },
  1557: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[0, 1, 2, 3, 4]" }
    ]
  },
  1558: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[1, 2, 3, 4, 5] [1, 2, 3, 4, 5]" }
    ]
  },
  1559: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "[1, 3, 6, 10, 15]" }
    ]
  },
  1560: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Person(name='Alice', age=30)" }
    ]
  },
  1561: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Student(name='Bob', age=18, grades=[])" }
    ]
  },
  1562: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "Point(x=3, y=4)" }
    ]
  },
  1468: {
        functionNames: ['is_prime'],
        tests: [
            { args: [7], expected: true },
            { args: [4], expected: false },
        ]
    },
  1479: {
        functionNames: ['identity'],
        tests: [
            { args: [5], expected: 5 },
        ]
    },
  1485: {
        functionNames: ['greet'],
        tests: [
            { args: ["Alice"], expected: "Hello, Alice!" },
        ]
    },
  1532: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [
      { args: [], expected: "11" }
    ]
  },
  1549: {
    functionNames: [],
    mode: 'script',
    compare: 'printedOrReturn',
    tests: [{
      args: [],
      expected: "{'items': ['apple']}"
    }]
  },
  1552: {
        functionNames: ['fibonacci'],
        tests: [
            { args: [7], expected: 13 },
        ]
    },
  1563: {
        functionNames: ['sum_numbers'],
        tests: [
            { args: [[1, 2]], expected: 3 },
        ]
    },
  1564: {
        functionNames: ['greet'],
        tests: [
            { args: ["Alice"], expected: "Hello, Alice!" },
        ]
    },
  1565: {
        functionNames: ['process_value'],
        tests: [
            { args: [42], expected: "42" },
            { args: ["hello"], expected: "hello" },
        ]
    },
  1566: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "Remaining: 5\nRemaining: 4\nRemaining: 3\nRemaining: 2\nRemaining: 1" },
        ]
    },
  1567: {
    functionNames: ["expensive_function"],
    tests: [{
      args: [5],
      expected: 10
    }]
  },
  1568: {
    functionNames: ["handle_command"],
    tests: [{
      args: [1],
      expected: "Unknown command"
    }]
  },
  1569: {
        functionNames: ['process_point'],
        tests: [
            { args: [[0, 0]], expected: "Origin" },
            { args: [[3, 0]], expected: "On x-axis at 3" },
            { args: [[0, 4]], expected: "On y-axis at 4" },
            { args: [[3, 4]], expected: "Point at (3, 4)" },
        ]
    },
  1570: {
        functionNames: ['Circle'],
        tests: [
            { args: [5], getAttrs: ['area'], expected: { area: 78.53975 } },
        ]
    },
  1571: {
        functionNames: ['Temperature'],
        tests: [
            { args: [], setAttrs: { celsius: 25 }, getAttrs: ['celsius'], expected: { celsius: 25 } },
            { args: [], setAttrs: { celsius: -274 }, expected: null, expectedException: "ValueError" },
        ]
    },
  1572: {
        functionNames: ['Book'],
        tests: [
            { args: ["Python Guide", "John Doe"], callMethod: "__str__", expected: "Python Guide by John Doe" },
        ]
    },
  1573: {
        functionNames: ['Point'],
        tests: [
            { args: [3, 4], callMethod: "__repr__", expected: "Point(x=3, y=4)" },
        ]
    },
  1574: {
        functionNames: ['Person'],
        tests: [
            { args: ["Alice", 30], callMethod: "__eq__", callMethodArgExpressions: ["Person('Alice', 30)"], expected: true },
            { args: ["Alice", 30], callMethod: "__eq__", callMethodArgExpressions: ["Person('Bob', 30)"], expected: false },
        ]
    },
  1575: {
        functionNames: ['Point'],
        compare: 'typeName',
        tests: [
            { args: [3, 4], callMethod: "__hash__", expected: "int" },
        ]
    },
  1576: {
        functionNames: ['Stack'],
        tests: [
            { args: [], callMethod: "__len__", expected: 0 },
        ]
    },
  1577: {
        functionNames: ['MyList'],
        tests: [
            { args: [[10, 20, 30, 40]], callMethod: "__getitem__", callMethodArgs: [2], expected: 30 },
        ]
    },
  1578: {
        functionNames: ['Timer'],
        compare: 'typeName',
        tests: [
            { args: [], callMethod: "__enter__", expected: "Timer" },
        ]
    },
  1579: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "Entering resource\nEntering resource\nUsing resources\nExiting resource\nExiting resource" },
        ]
    },
  1580: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], setupFiles: { "example.txt": "exists" }, expected: "File exists: True" },
        ]
    },
  1581: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "/home/user/documents" },
        ]
    },
  1582: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "/home/user/documents/file.txt" },
        ]
    },
  1583: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "{\"name\": \"Alice\", \"age\": 30, \"city\": \"New York\"}" },
        ]
    },
  1584: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "{'name': 'Alice', 'age': 30}" },
        ]
    },
  1585: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "The dog sat on the mat" },
        ]
    },
  1586: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "[('The', 0), ('cat', 4), ('and', 8), ('the', 12), ('hat', 16)]" },
        ]
    },
  1587: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "John Doe 30" },
        ]
    },
  1588: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "['first', 'second', 'third']" },
        ]
    },
  1589: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "{'c': 3, 'd': 4, 'a': 1, 'b': 2}" },
        ]
    },
  1590: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "3 4" },
        ]
    },
  1591: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "[[1, 2, 3], [2, 4, 6], [3, 6, 9]]" },
        ]
    },
  1592: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "[0, 6, 12, 18]" },
        ]
    },
  1593: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "['Bob', 'Alice', 'Charlie']" },
        ]
    },
  1594: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "['Hello', 'Hello', 'Hello']" },
        ]
    },
  1595: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "World" },
        ]
    },
  1596: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "Hello" },
        ]
    },
  1597: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "['one.two', 'three', 'four']" },
        ]
    },
  1598: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "[1, 2, [3, 4]] [10, 2, [3, 4]]" },
        ]
    },
  1599: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "[]" },
        ]
    },
  1600: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "('c', 3) {'a': 1, 'b': 2}" },
        ]
    },
  1601: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "{'a': 1, 'b': 2, 'c': 3, 'd': 4}" },
        ]
    },
  1602: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "['a', 'b', 'c']" },
        ]
    },
  1603: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "[1, 2, 3]" },
        ]
    },
  1604: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "[('a', 1), ('b', 2), ('c', 3)]" },
        ]
    },
  1605: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "Caught: This is a custom error" },
        ]
    },
  1606: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "Error: Conversion failed, caused by: invalid literal for int() with base 10: 'not a number'" },
        ]
    },
  1607: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "Captured: Hello, World!\nPython is great!" },
        ]
    },
  1608: {
    functionNames: ["my_decorator"],
    tests: [{
      args: [],
      argExpressions: ["lambda: 'Hello'"],
      getAttrs: ["__name__"],
      expected: { "__name__": "<lambda>" }
    }]
  },
  1609: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "[2, 6, 24, 120]" },
        ]
    },
  1610: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "[('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'b'), ('b', 'c'), ('c', 'c')]" },
        ]
    },
  1611: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "[5, 6, 7, 8]" },
        ]
    },
  1612: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "[1, 2, 3, 4]" },
        ]
    },
  1613: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "[6, 20, 42]" },
        ]
    },
  1614: {
        functionNames: ['compare'],
        tests: [
            { args: [5,3], expected: -2 },
            { args: [2,5], expected: 3 },
            { args: [4,4], expected: 0 },
        ]
    },
  1615: {
    functionNames: ["process"],
    tests: [{
      args: [1],
      expected: "Unknown type: int"
    }]
  },
  1616: {
        functionNames: ['process_scores'],
        tests: [
            { args: [{ Alice: 85, Bob: 90 }], expected: 175 },
            { args: [{ A: 1, B: 2, C: 3 }], expected: 6 },
        ]
    },
  1617: {
    functionNames: ["get_name_age"],
    tests: [{
      args: [],
      expected: ["Alice", 30]
    }]
  },
  1618: {
        functionNames: ['apply_operation'],
        tests: [
            { args: [5, 3], argExpressions: ["lambda a, b: a * b"], expected: 15 },
            { args: [5, 3], argExpressions: ["lambda a, b: a + b"], expected: 8 },
        ]
    },
  1619: {
    functionNames: ["categorize"],
    tests: [{
      args: [1],
      expected: "Positive"
    }]
  },
  1620: {
    functionNames: ["handle_status"],
    tests: [{
      args: [1],
      expected: "Unknown Status"
    }]
  },
  1621: {
        functionNames: ['Person'],
        tests: [
            { args: ["Alice"], deleteAttrs: ["name"], getAttrs: ['name'], expected: { name: null } },
        ]
    },
  1622: {
        functionNames: ['MyDict'],
        tests: [
            { args: [], setItems: [{ key: "key", value: "value" }], callMethod: "__getitem__", callMethodArgs: ["key"], expected: "value" },
        ]
    },
  1623: {
        functionNames: ['MyList'],
        tests: [
            { args: [[1, 2, 3, 4, 5]], deleteItems: [2], getAttrs: ['items'], expected: { items: [1, 2, 4, 5] } },
        ]
    },
  1624: {
        functionNames: ['MyContainer'],
        tests: [
            { args: [[1, 2, 3, 4, 5]], callMethod: "__contains__", callMethodArgs: [3], expected: true },
            { args: [[1, 2, 3, 4, 5]], callMethod: "__contains__", callMethodArgs: [9], expected: false },
        ]
    },
  1625: {
        functionNames: ['CountDown'],
        tests: [
            { args: [5], callMethod: "__next__", expected: 5 },
            { args: [1], callMethod: "__next__", expected: 1 },
        ]
    },
  1626: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "Entering context\nInside context: context value\nExiting context" },
        ]
    },
  1627: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "Demonstration: Path('file.txt').read_text() reads file content" },
        ]
    },
  1628: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "Demonstration: Path('file.txt').write_text('Hello, World!') writes to file" },
        ]
    },
  1629: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "Demonstration: Path('.').glob('*.py') finds all .py files" },
        ]
    },
  1630: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "Demonstration: json.dump(data, open('data.json', 'w')) writes JSON to file" },
        ]
    },
  1631: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "Demonstration: json.load(open('data.json')) reads and parses JSON file" },
        ]
    },
  1632: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "['3', '2']" },
        ]
    },
  1633: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "['apple', 'banana', 'cherry', 'date']" },
        ]
    },
  1634: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "['b', 'c', 'a']" },
        ]
    },
  1635: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "{'a': 1, 'b': 2, 'c': 3}" },
        ]
    },
  1636: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "Point(x=3, y=4) Point(x=10, y=4)" },
        ]
    },
  1637: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "{'1x1': 1, '1x2': 2, '1x3': 3, '2x1': 2, '2x2': 4, '2x3': 6, '3x1': 3, '3x2': 6, '3x3': 9}" },
        ]
    },
  1638: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "['d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y']" },
        ]
    },
  1639: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "15" },
        ]
    },
  1640: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "24" },
        ]
    },
  1641: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "True" },
        ]
    },
  1642: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "b'Hello, World!'" },
        ]
    },
  1643: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "Hello, World!" },
        ]
    },
  1644: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "[1, 2, 3, 4, 5, 6]" },
        ]
    },
  1645: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "1" },
        ]
    },
  1646: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "{'a': 0, 'b': 0, 'c': 0}" },
        ]
    },
  1647: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "Result: 5.0" },
        ]
    },
  1648: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "Caught division by zero\nThis always executes" },
        ]
    },
  1649: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "Continues after suppressed exception" },
        ]
    },
  1650: {
        functionNames: ['subtract_numbers'],
        tests: [
            { args: [5,3], expected: 2 },
        ]
    },
  1651: {
        functionNames: ['divide_numbers'],
        tests: [
            { args: [6,2], expected: 3 },
        ]
    },
  1652: {
        functionNames: ['calculate_remainder'],
        tests: [
            { args: [7,3], expected: 1 },
        ]
    },
  1653: {
        functionNames: ['calculate_power'],
        tests: [
            { args: [2,3], expected: 8 },
        ]
    },
  1654: {
    functionNames: ["calculate_circle_area"],
    tests: [{
      args: [1],
      expected: 3.14
    }]
  },
  1655: {
        functionNames: ['calculate_rectangle_area'],
        tests: [
            { args: [4,5], expected: 20 },
        ]
    },
  1656: {
        functionNames: ['calculate_triangle_area'],
        tests: [
            { args: [4,5], expected: 10 },
        ]
    },
  1657: {
        functionNames: ['convert_celsius_to_fahrenheit'],
        tests: [
            { args: [0], expected: 32 },
            { args: [100], expected: 212 },
        ]
    },
  1658: {
        functionNames: ['convert_fahrenheit_to_celsius'],
        tests: [
            { args: [32], expected: 0 },
            { args: [212], expected: 100 },
        ]
    },
  1659: {
        functionNames: ['is_positive'],
        tests: [
            { args: [5], expected: true },
            { args: [-3], expected: false },
        ]
    },
  1660: {
        functionNames: ['is_negative'],
        tests: [
            { args: [-5], expected: true },
            { args: [3], expected: false },
        ]
    },
  1661: {
        functionNames: ['get_first_char'],
        tests: [
            { args: ["hello"], expected: "h" },
        ]
    },
  1662: {
        functionNames: ['get_last_char'],
        tests: [
            { args: ["hello"], expected: "o" },
        ]
    },
  1663: {
        functionNames: ['get_middle_char'],
        tests: [
            { args: ["hello"], expected: "l" },
        ]
    },
  1664: {
        functionNames: ['repeat_string'],
        tests: [
            { args: ["ab",3], expected: "ababab" },
        ]
    },
  1665: {
        functionNames: ['swap_first_last'],
        tests: [
            { args: ["hello"], expected: "oellh" },
        ]
    },
  1666: {
        functionNames: ['remove_first_char'],
        tests: [
            { args: ["hello"], expected: "ello" },
        ]
    },
  1667: {
        functionNames: ['remove_last_char'],
        tests: [
            { args: ["hello"], expected: "hell" },
        ]
    },
  1668: {
        functionNames: ['get_first_word'],
        tests: [
            { args: ["hello world"], expected: "hello" },
        ]
    },
  1669: {
        functionNames: ['get_last_word'],
        tests: [
            { args: ["hello world"], expected: "world" },
        ]
    },
  1670: {
        functionNames: ['count_characters'],
        tests: [
            { args: ["hello"], expected: 5 },
        ]
    },
  1671: {
        functionNames: ['add_to_list'],
        tests: [
            { args: [[1,2],3], expected: [1,2,3] },
        ]
    },
  1672: {
        functionNames: ['get_first_element'],
        tests: [
            { args: [[1,2,3]], expected: 1 },
        ]
    },
  1673: {
        functionNames: ['get_last_element'],
        tests: [
            { args: [[1,2,3]], expected: 3 },
        ]
    },
  1674: {
        functionNames: ['get_middle_element'],
        tests: [
            { args: [[1,2,3]], expected: 2 },
        ]
    },
  1675: {
        functionNames: ['remove_first_element'],
        tests: [
            { args: [[1,2,3]], expected: [2,3] },
        ]
    },
  1676: {
        functionNames: ['remove_last_element'],
        tests: [
            { args: [[1,2,3]], expected: [1,2] },
        ]
    },
  1677: {
        functionNames: ['get_list_slice'],
        tests: [
            { args: [[1,2,3,4,5],1,3], expected: [2,3] },
        ]
    },
  1678: {
        functionNames: ['combine_lists'],
        tests: [
            { args: [[1,2],[3,4]], expected: [1,2,3,4] },
        ]
    },
  1679: {
        functionNames: ['multiply_list'],
        tests: [
            { args: [[1,2,3]], expected: [2,4,6] },
        ]
    },
  1680: {
        functionNames: ['add_one_to_all'],
        tests: [
            { args: [[1,2,3]], expected: [2,3,4] },
        ]
    },
  1681: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "1\n2\n3\n4\n5\n6\n7\n8\n9\n10" },
        ]
    },
  1682: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "2\n4\n6\n8\n10\n12\n14\n16\n18\n20" },
        ]
    },
  1683: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "1\n3\n5\n7\n9\n11\n13\n15\n17\n19" },
        ]
    },
  1684: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "5 x 1 = 5\n5 x 2 = 10\n5 x 3 = 15\n5 x 4 = 20\n5 x 5 = 25\n5 x 6 = 30\n5 x 7 = 35\n5 x 8 = 40\n5 x 9 = 45\n5 x 10 = 50" },
        ]
    },
  1685: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "H\ne\nl\nl\no" },
        ]
    },
  1686: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "10\n20\n30" },
        ]
    },
  1687: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "55" },
        ]
    },
  1688: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "120" },
        ]
    },
  1689: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "10\n9\n8\n7\n6\n5\n4\n3\n2\n1" },
        ]
    },
  1690: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "0\n3\n6\n9\n12\n15\n18" },
        ]
    },
  1691: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "1\n2\n3\n4\n5" },
        ]
    },
  1692: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "55" },
        ]
    },
  1693: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "2\n4\n6\n8\n10\n12\n14\n16\n18\n20" },
        ]
    },
  1694: {
        functionNames: [],
        mode: 'script',
        compare: 'printedOrReturn',
        tests: [
            { args: [], expected: "10\n9\n8\n7\n6\n5\n4\n3\n2\n1" },
        ]
    },
  1695: {
        functionNames: ['check_greater'],
        tests: [
            { args: [5,3], expected: true },
            { args: [2,5], expected: false },
        ]
    },
  1696: {
        functionNames: ['check_less'],
        tests: [
            { args: [2,5], expected: true },
            { args: [5,3], expected: false },
        ]
    },
  1697: {
        functionNames: ['check_equal'],
        tests: [
            { args: [3,3], expected: true },
            { args: [3,4], expected: false },
        ]
    },
  1698: {
        functionNames: ['check_not_equal'],
        tests: [
            { args: [3,4], expected: true },
            { args: [3,3], expected: false },
        ]
    },
  1699: {
        functionNames: ['check_greater_equal'],
        tests: [
            { args: [5,3], expected: true },
            { args: [3,5], expected: false },
        ]
    },
  1700: {
        functionNames: ['check_less_equal'],
        tests: [
            { args: [3,5], expected: true },
            { args: [5,3], expected: false },
        ]
    },
  1701: {
        functionNames: ['get_absolute_value'],
        tests: [
            { args: [-5], expected: 5 },
            { args: [3], expected: 3 },
        ]
    },
  1702: {
        functionNames: ['round_number'],
        tests: [
            { args: [3.14159], expected: 3 },
        ]
    },
  1703: {
        functionNames: ['get_maximum'],
        tests: [
            { args: [3,7,5], expected: 7 },
        ]
    },
  1704: {
        functionNames: ['get_minimum'],
        tests: [
            { args: [3,7,5], expected: 3 },
        ]
    },
  1705: {
        functionNames: ['check_divisible'],
        tests: [
            { args: [10,5], expected: true },
            { args: [10,3], expected: false },
        ]
    },
  1706: {
        functionNames: ['convert_to_string'],
        tests: [
            { args: [123], expected: "123" },
        ]
    },
  1707: {
        functionNames: ['convert_to_integer'],
        tests: [
            { args: ["123"], expected: 123 },
        ]
    },
  1708: {
        functionNames: ['convert_to_float'],
        compare: 'float',
        tests: [
            { args: ["3.14"], expected: 3.14 },
        ]
    },
  1709: {
    functionNames: ["get_type"],
    tests: [{
      args: [1],
      expected: "int"
    }]
  },
  1710: {
        functionNames: ['check_is_integer'],
        tests: [
            { args: [5], expected: true },
        ]
    },
  1711: {
        functionNames: ['check_is_string'],
        tests: [
            { args: ["hello"], expected: true },
        ]
    },
  1712: {
        functionNames: ['check_is_list'],
        tests: [
            { args: [[1,2]], expected: true },
        ]
    },
  1713: {
        functionNames: ['format_greeting'],
        tests: [
            { args: ["Alice"], expected: "Hello, Alice!" },
        ]
    },
  1714: {
        functionNames: ['format_age_message'],
        tests: [
            { args: ["Bob", 25], expected: "Bob is 25 years old." },
        ]
    },
  1715: {
        functionNames: ['format_calculation'],
        tests: [
            { args: [5,3], expected: "5 + 3 = 8" },
        ]
    },
  1716: {
        functionNames: ['calculate_perimeter_rectangle'],
        tests: [
            { args: [4,5], expected: 18 },
        ]
    },
  1717: {
        functionNames: ['calculate_perimeter_square'],
        tests: [
            { args: [4], expected: 16 },
        ]
    },
  1718: {
    functionNames: ["calculate_circle_circumference"],
    tests: [{
      args: [1],
      expected: 6.28
    }]
  },
  1719: {
    functionNames: ["convert_km_to_miles"],
    tests: [{
      args: [1],
      expected: 0.621371
    }]
  },
  1720: {
    functionNames: ["convert_miles_to_km"],
    tests: [{
      args: [1],
      expected: 1.6093444978925633
    }]
  },
  1721: {
    functionNames: ["convert_kg_to_pounds"],
    tests: [{
      args: [1],
      expected: 2.20462
    }]
  },
  1722: {
    functionNames: ["convert_pounds_to_kg"],
    tests: [{
      args: [5],
      expected: 2.267964547178199
    }]
  },
  1723: {
        functionNames: ['check_vowel'],
        tests: [
            { args: ["a"], expected: true },
            { args: ["b"], expected: false },
        ]
    },
  1724: {
        functionNames: ['check_consonant'],
        tests: [
            { args: ["b"], expected: true },
            { args: ["a"], expected: false },
        ]
    },
  1725: {
        functionNames: ['check_digit'],
        tests: [
            { args: ["5"], expected: true },
            { args: ["a"], expected: false },
        ]
    },
  1726: {
        functionNames: ['check_letter'],
        tests: [
            { args: ["a"], expected: true },
            { args: ["1"], expected: false },
        ]
    },
  1727: {
        functionNames: ['check_uppercase'],
        tests: [
            { args: ["A"], expected: true },
            { args: ["a"], expected: false },
        ]
    },
  1728: {
        functionNames: ['check_lowercase'],
        tests: [
            { args: ["a"], expected: true },
            { args: ["A"], expected: false },
        ]
    },
  1729: {
        functionNames: ['find_char_index'],
        tests: [
            { args: ["hello","l"], expected: 2 },
        ]
    },
  1730: {
        functionNames: ['count_char_in_string'],
        tests: [
            { args: ["hello","l"], expected: 2 },
        ]
    },
  1731: {
        functionNames: ['check_starts_with'],
        tests: [
            { args: ["hello","he"], expected: true },
            { args: ["hello","el"], expected: false },
        ]
    },
  1732: {
        functionNames: ['check_ends_with'],
        tests: [
            { args: ["hello","lo"], expected: true },
            { args: ["hello","el"], expected: false },
        ]
    },
  1733: {
        functionNames: ['replace_char'],
        tests: [
            { args: ["hello","l","x"], expected: "hexxo" },
        ]
    },
  1734: {
        functionNames: ['remove_char'],
        tests: [
            { args: ["hello","l"], expected: "heo" },
        ]
    },
  1735: {
        functionNames: ['get_substring'],
        tests: [
            { args: ["hello",1,3], expected: "el" },
        ]
    },
  1736: {
        functionNames: ['reverse_list'],
        tests: [
            { args: [[1,2,3,4]], expected: [4,3,2,1] },
        ]
    },
  1737: {
        functionNames: ['get_list_length'],
        tests: [
            { args: [[1,2,3]], expected: 3 },
        ]
    },
  1738: {
        functionNames: ['check_element_in_list'],
        tests: [
            { args: [[1,2,3],2], expected: true },
        ]
    },
  1739: {
        functionNames: ['get_element_count'],
        tests: [
            { args: [[1,2,2,3],2], expected: 2 },
        ]
    },
  1740: {
        functionNames: ['get_element_index'],
        tests: [
            { args: [[1,2,3],2], expected: 1 },
        ]
    },
  1741: {
        functionNames: ['get_even_numbers'],
        tests: [
            { args: [[1,2,3,4,5,6]], expected: [2,4,6] },
        ]
    },
  1742: {
        functionNames: ['get_odd_numbers'],
        tests: [
            { args: [[1,2,3,4,5,6]], expected: [1,3,5] },
        ]
    },
  1743: {
        functionNames: ['get_positive_numbers'],
        tests: [
            { args: [[-1,0,1,2]], expected: [1,2] },
        ]
    },
  1744: {
        functionNames: ['get_negative_numbers'],
        tests: [
            { args: [[-1,0,1,-2]], expected: [-1,-2] },
        ]
    },
  1745: {
        functionNames: ['get_numbers_greater_than'],
        tests: [
            { args: [[1,5,3,8],3], expected: [5,8] },
        ]
    },
  1746: {
        functionNames: ['get_numbers_less_than'],
        tests: [
            { args: [[1,5,3,8],5], expected: [1,3] },
        ]
    },
  1747: {
        functionNames: ['calculate_sum_of_list'],
        tests: [
            { args: [[1,2,3]], expected: 6 },
        ]
    },
  1748: {
        functionNames: ['calculate_product_of_list'],
        tests: [
            { args: [[2,3,4]], expected: 24 },
        ]
    },
  1749: {
        functionNames: ['get_average_of_list'],
        compare: 'float',
        tests: [
            { args: [[1,2,3,4]], expected: 2.5 },
        ]
    },
  1750: {
        functionNames: ['create_dictionary'],
        tests: [
            { args: [["a","b"],[1,2]], expected: {"a":1,"b":2} },
        ]
    },
  1751: {
        functionNames: ['get_dictionary_value'],
        tests: [
            { args: [{"a":1,"b":2},"a"], expected: 1 },
        ]
    },
  1752: {
        functionNames: ['get_dictionary_keys'],
        tests: [
            { args: [{"a":1,"b":2}], expected: ["a","b"] },
        ]
    },
  1753: {
        functionNames: ['get_dictionary_values'],
        tests: [
            { args: [{"a":1,"b":2}], expected: [1,2] },
        ]
    },
  1754: {
        functionNames: ['check_key_in_dictionary'],
        tests: [
            { args: [{"a":1},"a"], expected: true },
        ]
    },
  1755: {
        functionNames: ['add_to_dictionary'],
        tests: [
            { args: [{"a":1},"b",2], expected: {"a":1,"b":2} },
        ]
    },
  1756: {
        functionNames: ['create_tuple'],
        tests: [
            { args: [1,2,3], expected: [1,2,3] },
        ]
    },
  1757: {
        functionNames: ['get_tuple_element'],
        tests: [
            { args: [[1,2,3],1], expected: 2 },
        ]
    },
  1758: {
        functionNames: ['unpack_tuple'],
        tests: [
            { args: [[1,2]], expected: [1,2] },
        ]
    },
  1759: {
        functionNames: ['create_set'],
        tests: [
            { args: [[1,2,2,3]], expected: [1,2,3] },
        ]
    },
  1760: {
        functionNames: ['check_element_in_set'],
        tests: [
            { args: [[1,2,3],2], expected: true },
        ]
    },
  1761: {
        functionNames: ['union_sets'],
        tests: [
            { args: [], argExpressions: ["{1, 2}", "{2, 3}"], expected: [1,2,3] },
        ]
    },
  1762: {
        functionNames: ['intersection_sets'],
        tests: [
            { args: [], argExpressions: ["{1, 2, 3}", "{2, 3, 4}"], expected: [2,3] },
        ]
    },
  1763: {
        functionNames: ['difference_sets'],
        tests: [
            { args: [], argExpressions: ["{1, 2, 3}", "{2, 3}"], expected: [1] },
        ]
    },
  1764: {
        functionNames: ['read_file_content'],
        tests: [
            { args: ["example.txt"], setupFiles: { "example.txt": "Hello file" }, expected: "Hello file" },
        ]
    },
  1765: {
        functionNames: ['write_to_file'],
        tests: [
            { args: ["output.txt", "Hello, World!"], getFiles: ["output.txt"], expected: { "output.txt": "Hello, World!" } },
        ]
    },
  1766: {
        functionNames: ['append_to_file'],
        tests: [
            { args: ["append.txt", " plus more"], setupFiles: { "append.txt": "start" }, getFiles: ["append.txt"], expected: { "append.txt": "start plus more" } },
        ]
    },
  1767: {
        functionNames: ['safe_divide'],
        tests: [
            { args: [6,3], expected: 2 },
        ]
    },
  1768: {
        functionNames: ['safe_convert_to_int'],
        tests: [
            { args: ["123"], expected: 123 },
        ]
    },
  1769: {
        functionNames: ['safe_get_list_element'],
        tests: [
            { args: [[1,2,3],1], expected: 2 },
        ]
    },
  1770: {
        functionNames: ['join_strings'],
        tests: [
            { args: [["a","b","c"], ""], expected: "abc" },
        ]
    },
  1771: {
        functionNames: ['split_string'],
        tests: [
            { args: ["a,b,c",","], expected: ["a","b","c"] },
        ]
    },
  1772: {
        functionNames: ['strip_whitespace'],
        tests: [
            { args: ["  hello  "], expected: "hello" },
        ]
    },
  1773: {
        functionNames: ['capitalize_first_letter'],
        tests: [
            { args: ["hello"], expected: "Hello" },
        ]
    },
  1774: {
        functionNames: ['swap_case'],
        tests: [
            { args: ["Hello"], expected: "hELLO" },
        ]
    },
  1775: {
        functionNames: ['check_all_digits'],
        tests: [
            { args: ["123"], expected: true },
            { args: ["12a"], expected: false },
        ]
    },
  1776: {
        functionNames: ['check_all_letters'],
        tests: [
            { args: ["abc"], expected: true },
            { args: ["ab1"], expected: false },
        ]
    },
  1777: {
        functionNames: ['check_all_alphanumeric'],
        tests: [
            { args: ["abc123"], expected: true },
            { args: ["abc 123"], expected: false },
        ]
    },
  1778: {
        functionNames: ['get_squared_numbers'],
        tests: [
            { args: [[1,2,3]], expected: [1,4,9] },
        ]
    },
  1779: {
        functionNames: ['get_doubled_numbers'],
        tests: [
            { args: [[1,2,3]], expected: [2,4,6] },
        ]
    },
  1780: {
        functionNames: ['get_even_numbers_comprehension'],
        tests: [
            { args: [[1,2,3,4,5,6]], expected: [2,4,6] },
        ]
    },
  1781: {
        functionNames: ['get_uppercase_strings'],
        tests: [
            { args: [["a","b","c"]], expected: ["A","B","C"] },
        ]
    },
  1782: {
        functionNames: ['get_string_lengths'],
        tests: [
            { args: [["hi","hello","a"]], expected: [2,5,1] },
        ]
    },
  1783: {
    functionNames: ["print_number_pattern"],
    compare: 'printedOrReturn',
    tests: [{
      args: [5],
      expected: "1 \n1 2 \n1 2 3 \n1 2 3 4 \n1 2 3 4 5"
    }]
  },
  1784: {
    functionNames: ["print_star_pattern"],
    compare: 'printedOrReturn',
    tests: [{
      args: [5],
      expected: "*\n**\n***\n****\n*****"
    }]
  },
  1785: {
    functionNames: ["print_reverse_star_pattern"],
    compare: 'printedOrReturn',
    tests: [{
      args: [5],
      expected: "*****\n****\n***\n**\n*"
    }]
  },
  1786: {
    functionNames: ["print_number_square"],
    compare: 'printedOrReturn',
    tests: [{
      args: [5],
      expected: "1 2 3 4 5\n6 7 8 9 10\n11 12 13 14 15\n16 17 18 19 20\n21 22 23 24 25"
    }]
  },
  1787: {
        functionNames: ['calculate_factorial'],
        tests: [
            { args: [5], expected: 120 },
        ]
    },
  1788: {
    functionNames: ["calculate_sum_range"],
    tests: [{
      args: [1, 5],
      expected: 15
    }]
  },
  1789: {
    functionNames: ["calculate_product_range"],
    tests: [{
      args: [1, 5],
      expected: 120
    }]
  },
  1790: {
    functionNames: ["get_fibonacci_sequence"],
    tests: [{
      args: [5],
      expected: [0, 1, 1, 2, 3]
    }]
  },
  1791: {
        functionNames: ['check_palindrome_number'],
        tests: [
            { args: [121], expected: true },
            { args: [123], expected: false },
        ]
    },
  1792: {
        functionNames: ['sum_of_digits'],
        tests: [
            { args: [123], expected: 6 },
        ]
    },
  1793: {
        functionNames: ['product_of_digits'],
        tests: [
            { args: [123], expected: 6 },
        ]
    },
  1794: {
        functionNames: ['count_digits'],
        tests: [
            { args: [12345], expected: 5 },
        ]
    },
  1795: {
        functionNames: ['reverse_number'],
        tests: [
            { args: [123], expected: 321 },
        ]
    },
  1796: {
        functionNames: ['get_first_n_elements'],
        tests: [
            { args: [[1,2,3,4,5],3], expected: [1,2,3] },
        ]
    },
  1797: {
        functionNames: ['get_last_n_elements'],
        tests: [
            { args: [[1,2,3,4,5],3], expected: [3,4,5] },
        ]
    },
  1798: {
        functionNames: ['remove_duplicates_from_list'],
        tests: [
            { args: [[1,2,2,3,3,4]], expected: [1,2,3,4] },
        ]
    },
  1799: {
        functionNames: ['merge_two_lists'],
        tests: [
            { args: [[1,2],[3,4]], expected: [1,3,2,4] },
        ]
    },
  1800: {
        functionNames: ['get_common_elements'],
        tests: [
            { args: [[1,2,3],[2,3,4]], expected: [2,3] },
        ]
    },
  1801: {
        functionNames: ['get_unique_elements'],
        tests: [
            { args: [[1,2,3,4], [3,4,5,6]], expected: [1,2,5,6] },
        ]
    },
  1802: {
        functionNames: ['sort_list_ascending'],
        tests: [
            { args: [[3,1,4,1,5]], expected: [1,1,3,4,5] },
        ]
    },
  1803: {
        functionNames: ['sort_list_descending'],
        tests: [
            { args: [[3,1,4,1,5]], expected: [5,4,3,1,1] },
        ]
    },
  1804: {
        functionNames: ['get_second_largest'],
        tests: [
            { args: [[1,5,3,8,2]], expected: 5 },
        ]
    },
  1805: {
        functionNames: ['get_second_smallest'],
        tests: [
            { args: [[1,5,3,8,2]], expected: 2 },
        ]
    },
  1806: {
        functionNames: ['check_sorted'],
        tests: [
            { args: [[1,2,3]], expected: true },
            { args: [[3,1,2]], expected: false },
        ]
    },
  1807: {
        functionNames: ['count_occurrences_in_list'],
        tests: [
            { args: [[1,2,2,3,2]], expected: {"1": 1, "2": 3, "3": 1} },
        ]
    },
  1808: {
        functionNames: ['get_most_frequent'],
        tests: [
            { args: [[1,2,2,3,3,3]], expected: 3 },
        ]
    },
  1809: {
        functionNames: ['get_least_frequent'],
        tests: [
            { args: [[1,2,2,3]], expected: 1 },
        ]
    },
  1810: {
        functionNames: ['flatten_nested_list'],
        tests: [
            { args: [[[1,2],[3,4],[5]]], expected: [1,2,3,4,5] },
        ]
    },
  1811: {
        functionNames: ['group_by_length'],
        tests: [
            { args: [["a","ab","abc","ab"]], expected: {"1":["a"],"2":["ab","ab"],"3":["abc"]} },
        ]
    },
  1812: {
        functionNames: ['filter_by_length'],
        tests: [
            { args: [["a","ab","abc","abcd"],3], expected: ["abc","abcd"] },
        ]
    },
  1813: {
        functionNames: ['get_longest_string'],
        tests: [
            { args: [["a","abc","ab"]], expected: "abc" },
        ]
    },
  1814: {
        functionNames: ['get_shortest_string'],
        tests: [
            { args: [["a","abc","ab"]], expected: "a" },
        ]
    },
  1815: {
        functionNames: ['capitalize_all_words'],
        tests: [
            { args: ["hello world"], expected: "Hello World" },
        ]
    },
  1816: {
        functionNames: ['reverse_words'],
        tests: [
            { args: ["hello world"], expected: "world hello" },
        ]
    },
  1817: {
        functionNames: ['count_words'],
        tests: [
            { args: ["hello world"], expected: 2 },
        ]
    },
  1818: {
        functionNames: ['get_longest_word'],
        tests: [
            { args: ["hello world python"], expected: "python" },
        ]
    },
  1819: {
        functionNames: ['get_shortest_word'],
        tests: [
            { args: ["hello world a"], expected: "a" },
        ]
    },
  1820: {
        functionNames: ['remove_vowels_from_string'],
        tests: [
            { args: ["hello"], expected: "hll" },
        ]
    },
  1821: {
        functionNames: ['remove_consonants_from_string'],
        tests: [
            { args: ["hello"], expected: "eo" },
        ]
    },
  1822: {
        functionNames: ['count_vowels_in_string'],
        tests: [
            { args: ["hello"], expected: 2 },
        ]
    },
  1823: {
        functionNames: ['count_consonants_in_string'],
        tests: [
            { args: ["hello"], expected: 3 },
        ]
    },
  1824: {
        functionNames: ['swap_first_last_words'],
        tests: [
            { args: ["hello world python"], expected: "python world hello" },
        ]
    },
  1825: {
        functionNames: ['get_middle_word'],
        tests: [
            { args: ["hello world python"], expected: "world" },
        ]
    },
  1826: {
        functionNames: ['check_all_same'],
        tests: [
            { args: [[1,1,1]], expected: true },
            { args: [[1,2,1]], expected: false },
        ]
    },
  1827: {
        functionNames: ['check_all_different'],
        tests: [
            { args: [[1,2,3]], expected: true },
            { args: [[1,2,1]], expected: false },
        ]
    },
  1828: {
        functionNames: ['get_range_list'],
        tests: [
            { args: [1,5], expected: [1,2,3,4,5] },
        ]
    },
  1829: {
        functionNames: ['get_even_range'],
        tests: [
            { args: [1,10], expected: [2,4,6,8,10] },
        ]
    },
  1830: {
        functionNames: ['get_odd_range'],
        tests: [
            { args: [1,10], expected: [1,3,5,7,9] },
        ]
    },
  1831: {
        functionNames: ['multiply_lists'],
        tests: [
            { args: [[1,2,3],[4,5,6]], expected: [4,10,18] },
        ]
    },
  1832: {
        functionNames: ['add_lists'],
        tests: [
            { args: [[1,2,3],[4,5,6]], expected: [5,7,9] },
        ]
    },
  1833: {
        functionNames: ['subtract_lists'],
        tests: [
            { args: [[5,3,7],[1,2,4]], expected: [4,1,3] },
        ]
    },
  1834: {
        functionNames: ['get_index_of_max'],
        tests: [
            { args: [[1,5,3,8,2]], expected: 3 },
        ]
    },
  1835: {
        functionNames: ['get_index_of_min'],
        tests: [
            { args: [[1,5,3,8,2]], expected: 0 },
        ]
    },
  1836: {
        functionNames: ['rotate_list_left'],
        tests: [
            { args: [[1,2,3,4,5],2], expected: [3,4,5,1,2] },
        ]
    },
  1837: {
        functionNames: ['rotate_list_right'],
        tests: [
            { args: [[1,2,3,4,5],2], expected: [4,5,1,2,3] },
        ]
    },
  1838: {
        functionNames: ['chunk_list'],
        tests: [
            { args: [[1,2,3,4,5,6],2], expected: [[1,2],[3,4],[5,6]] },
        ]
    },
  1839: {
        functionNames: ['interleave_lists'],
        tests: [
            { args: [[1,2,3],["a","b","c"]], expected: [1,"a",2,"b",3,"c"] },
        ]
    },
  1840: {
        functionNames: ['zip_lists'],
        tests: [
            { args: [[1,2],["a","b"]], expected: [[1,"a"],[2,"b"]] },
        ]
    },
  1841: {
        functionNames: ['unzip_list'],
        tests: [
            { args: [[[1,"a"],[2,"b"]]], expected: [[1,2],["a","b"]] },
        ]
    },
  1842: {
        functionNames: ['count_uppercase_letters'],
        tests: [
            { args: ["Hello WORLD"], expected: 6 },
        ]
    },
  1843: {
        functionNames: ['count_lowercase_letters'],
        tests: [
            { args: ["Hello WORLD"], expected: 4 },
        ]
    },
  1844: {
        functionNames: ['swap_uppercase_lowercase'],
        tests: [
            { args: ["Hello"], expected: "hELLO" },
        ]
    },
  1845: {
        functionNames: ['remove_numbers_from_string'],
        tests: [
            { args: ["ab12cd34"], expected: "abcd" },
        ]
    },
  1846: {
        functionNames: ['remove_letters_from_string'],
        tests: [
            { args: ["ab12cd34"], expected: "1234" },
        ]
    },
  1847: {
        functionNames: ['extract_numbers_from_string'],
        tests: [
            { args: ["ab12cd34"], expected: ["1","2","3","4"] },
        ]
    },
  1848: {
        functionNames: ['extract_letters_from_string'],
        tests: [
            { args: ["ab12cd34"], expected: ["a","b","c","d"] },
        ]
    },
  1849: {
        functionNames: ['format_phone_number'],
        tests: [
            { args: ["1234567890"], expected: "(123) 456-7890" },
        ]
    },
  1850: {
        functionNames: ['calculate_volume_box'],
        tests: [
            { args: [3,4,5], expected: 60 },
        ]
    },
  1851: {
        functionNames: ['check_triangle_valid'],
        tests: [
            { args: [3,4,5], expected: true },
            { args: [1,1,3], expected: false },
        ]
    },
  1852: {
        functionNames: ['find_grade'],
        tests: [
            { args: [85], expected: "B" },
        ]
    },
  1853: {
        functionNames: ['get_season'],
        tests: [
            { args: [3], expected: "Spring" },
        ]
    },
  1854: {
        functionNames: ['calculate_discount'],
        tests: [
            { args: [100,20], expected: 80 },
        ]
    },
  1855: {
        functionNames: ['calculate_tip'],
        tests: [
            { args: [50,15], expected: [7.5,57.5] },
        ]
    },
  1856: {
        functionNames: ['swap_two_elements'],
        tests: [
            { args: [[1,2,3,4],1,3], expected: [1,4,3,2] },
        ]
    },
  1857: {
        functionNames: ['insert_at_index'],
        tests: [
            { args: [[1,2,4],2,3], expected: [1,2,3,4] },
        ]
    },
  1858: {
        functionNames: ['remove_at_index'],
        tests: [
            { args: [[1,2,3,4],2], expected: [1,2,4] },
        ]
    },
  1859: {
        functionNames: ['count_vowels_and_consonants'],
        tests: [
            { args: ["hello"], expected: [2,3] },
        ]
    },
  1860: {
        functionNames: ['get_min_max'],
        tests: [
            { args: [[1,5,3,8,2]], expected: [1,8] },
        ]
    },
  1861: {
        functionNames: ['check_all_conditions'],
        tests: [
            { args: [6], expected: true },
        ]
    },
  1862: {
        functionNames: ['format_full_name'],
        tests: [
            { args: ["John","Michael","Doe"], expected: "John Michael Doe" },
        ]
    },
  1863: {
        functionNames: ['calculate_bmi'],
        compare: 'float',
        tests: [
            { args: [70,1.75], expected: 22.9 },
        ]
    },
  1864: {
        functionNames: ['check_bmi_category'],
        tests: [
            { args: [70,1.75], expected: "Normal" },
        ]
    },
  1865: {
        functionNames: ['find_common_elements_three'],
        tests: [
            { args: [[1,2,3],[2,3,4],[2,3,5]], expected: [2,3] },
        ]
    },
  1866: {
        functionNames: ['merge_three_lists'],
        tests: [
            { args: [[1],[2],[3]], expected: [1,2,3] },
        ]
    },
  1867: {
        functionNames: ['get_elements_at_indices'],
        tests: [
            { args: [[10,20,30,40],[0,2]], expected: [10,30] },
        ]
    },
  1868: {
        functionNames: ['replace_multiple_chars'],
        tests: [
            { args: ["hello",{"l":"x"}], expected: "hexxo" },
        ]
    },
  1869: {
        functionNames: ['count_words_by_length'],
        tests: [
            { args: ["a ab abc ab"], expected: {"1":1,"2":2,"3":1} },
        ]
    },
  1870: {
        functionNames: ['filter_and_transform'],
        tests: [
            { args: [[1,2,3,4,5]], expected: [4,8] },
        ]
    },
  1871: {
        functionNames: ['get_strings_starting_with'],
        tests: [
            { args: [["apple","banana","apricot"],"a"], expected: ["apple","apricot"] },
        ]
    },
  1872: {
        functionNames: ['get_strings_ending_with'],
        tests: [
            { args: [["apple","banana","orange"],"e"], expected: ["apple","orange"] },
        ]
    },
  1873: {
        functionNames: ['calculate_total_cost'],
        tests: [
            { args: [[10,20,30],10], expected: 66 },
        ]
    },
  1874: {
        functionNames: ['find_all_indices'],
        tests: [
            { args: [[1,2,3,2,4],2], expected: [1,3] },
        ]
    },
  1875: {
        functionNames: ['split_into_chunks'],
        tests: [
            { args: [[1,2,3,4,5,6],2], expected: [[1,2],[3,4],[5,6]] },
        ]
    },
  1876: {
        functionNames: ['remove_multiple_elements'],
        tests: [
            { args: [[1,2,3,4,5],[1,3]], expected: [2,4,5] },
        ]
    },
  1877: {
        functionNames: ['count_occurrences_multiple'],
        tests: [
            { args: [[1,2,2,3,2,3],[2,3]], expected: {"2":3,"3":2} },
        ]
    },
  1878: {
        functionNames: ['get_unique_elements_three'],
        tests: [
            { args: [[1,2,3],[2,3,4],[3,4,5]], expected: [1,5] },
        ]
    },
  1879: {
        functionNames: ['sort_by_multiple_criteria'],
        tests: [
            { args: [[["Bob",25,90],["Alice",25,85],["Charlie",30,80]]], expected: [["Alice",25,85],["Bob",25,90],["Charlie",30,80]] },
        ]
    },
  1880: {
    functionNames: ["calculate_statistics"],
    tests: [{
      args: [[1, 2, 3, 4, 5]],
      expected: {"sum": 15, "average": 3, "min": 1, "max": 5}
    }]
  },
  1881: {
        functionNames: ['extract_numbers_from_string'],
        tests: [
            { args: ["ab12cd34"], expected: [12,34] },
        ]
    },
  1882: {
        functionNames: ['format_address'],
        tests: [
            { args: ["123 Main St","New York","NY","10001"], expected: "123 Main St\nNew York, NY 10001" },
        ]
    },
  1883: {
        functionNames: ['check_password_strength'],
        tests: [
            { args: ["Abc123!@"], expected: true },
        ]
    },
  1884: {
        functionNames: ['get_words_by_length_range'],
        tests: [
            { args: ["a ab abc abcd abcde",2,4], expected: ["ab","abc","abcd"] },
        ]
    },
  1885: {
        functionNames: ['calculate_compound_interest'],
        compare: 'float',
        tests: [
            { args: [1000,5,2,12], expected: 1104.941335558327 },
        ]
    },
  1886: {
        functionNames: ['find_duplicate_elements'],
        tests: [
            { args: [[1,2,2,3,3,3]], expected: [2,3] },
        ]
    },
  1887: {
        functionNames: ['group_by_first_letter'],
        tests: [
            { args: [["apple","banana","apricot"]], expected: {"a":["apple","apricot"],"b":["banana"]} },
        ]
    },
  1888: {
        functionNames: ['calculate_distance'],
        tests: [
            { args: [0,0,3,4], expected: 5 },
        ]
    },
  1889: {
        functionNames: ['check_in_range'],
        tests: [
            { args: [5,1,10], expected: true },
            { args: [15,1,10], expected: false },
        ]
    },
  1890: {
        functionNames: ['get_divisors'],
        tests: [
            { args: [12], expected: [1,2,3,4,6,12] },
        ]
    },
  1891: {
        functionNames: ['check_perfect_square'],
        tests: [
            { args: [16], expected: true },
            { args: [15], expected: false },
            { args: [0], expected: true },
        ]
    },
  1892: {
        functionNames: ['format_time'],
        tests: [
            { args: [1,0,0], expected: "01:00:00" },
        ]
    },
  1893: {
    functionNames: ["calculate_age"],
    tests: [{
      args: [1, 5, 3],
      expected: 2022
    }]
  },
  1894: {
        functionNames: ['get_middle_elements'],
        tests: [
            { args: [[1,2,3,4]], expected: [2,3] },
        ]
    },
  1895: {
        functionNames: ['swap_adjacent_elements'],
        tests: [
            { args: [[1,2,3,4]], expected: [2,1,4,3] },
        ]
    },
  1896: {
        functionNames: ['get_every_nth_element'],
        tests: [
            { args: [[1,2,3,4,5,6],2], expected: [1,3,5] },
        ]
    },
  1897: {
        functionNames: ['count_uppercase_lowercase'],
        tests: [
            { args: ["Hello WORLD"], expected: {"uppercase":6,"lowercase":4} },
        ]
    },
  1898: {
        functionNames: ['remove_duplicates_preserve_order'],
        tests: [
            { args: [[3,1,2,1,3,2]], expected: [3,1,2] },
        ]
    },
  1899: {
        functionNames: ['get_intersection_three_lists'],
        tests: [
            { args: [[1,2,3],[2,3,4],[2,3,5]], expected: [2,3] },
        ]
    },
  1900: {
        functionNames: ['calculate_percentage'],
        tests: [
            { args: [25,100], expected: 25 },
        ]
    },
  1901: {
        functionNames: ['find_largest_three'],
        tests: [
            { args: [[1,8,3,9,5,2]], expected: [9,8,5] },
        ]
    },
  1902: {
        functionNames: ['find_smallest_three'],
        tests: [
            { args: [[1,8,3,9,5,2]], expected: [1,2,3] },
        ]
    },
  1903: {
        functionNames: ['check_palindrome_and_length'],
        tests: [
            { args: ["radar"], expected: [true,5] },
            { args: ["hello"], expected: [false,5] },
        ]
    },
  1904: {
        functionNames: ['get_words_starting_with_vowel'],
        tests: [
            { args: ["apple banana orange"], expected: ["apple","orange"] },
        ]
    },
  1905: {
        functionNames: ['get_words_ending_with_consonant'],
        tests: [
            { args: ["apple banana world"], expected: ["world"] },
        ]
    },
  1906: {
        functionNames: ['calculate_area_perimeter'],
        tests: [
            { args: [4,5], expected: [20,18] },
        ]
    },
  1907: {
        functionNames: ['format_currency'],
        tests: [
            { args: [1234.5], expected: "$1234.50" },
        ]
    },
  1908: {
        functionNames: ['get_even_indices'],
        tests: [
            { args: [[10,20,30,40,50]], expected: [10,30,50] },
        ]
    },
  1909: {
        functionNames: ['get_odd_indices'],
        tests: [
            { args: [[10,20,30,40,50]], expected: [20,40] },
        ]
    },
  1910: {
        functionNames: ['multiply_corresponding'],
        tests: [
            { args: [[1,2,3],[4,5,6]], expected: [4,10,18] },
        ]
    },
  1911: {
        functionNames: ['divide_corresponding'],
        tests: [
            { args: [[10,20,30],[2,4,5]], expected: [5,5,6] },
        ]
    },
  1912: {
        functionNames: ['get_strings_containing'],
        tests: [
            { args: [["hello","world","help"],"el"], expected: ["hello","help"] },
        ]
    },
  1913: {
    functionNames: ["count_characters_by_type"],
    tests: [{
      args: ["hello"],
      expected: {"letters": 5, "digits": 0, "others": 0}
    }]
  },
  1914: {
        functionNames: ['get_range_between'],
        tests: [
            { args: [[1,3,5,7,9],3,7], expected: [3,5,7] },
        ]
    },
  1915: {
        functionNames: ['format_date'],
        tests: [
            { args: [2023,12,25], expected: "2023-12-25" },
        ]
    },
  1916: {
        functionNames: ['calculate_simple_interest'],
        tests: [
            { args: [1000,5,2], expected: 100 },
        ]
    },
  1917: {
        functionNames: ['get_unique_characters'],
        tests: [
            { args: ["hello"], expected: ["h","e","l","o"] },
        ]
    },
  1918: {
        functionNames: ['count_words_ending_with'],
        tests: [
            { args: ["running walking jumped","ing"], expected: 2 },
        ]
    },
  1919: {
        functionNames: ['get_numbers_in_range'],
        tests: [
            { args: [[1,5,10,15],5,15], expected: [5,10,15] },
        ]
    },
  1920: {
        functionNames: ['format_name_age_city'],
        tests: [
            { args: ["Alice",25,"NYC"], expected: "Name: Alice, Age: 25, City: NYC" },
        ]
    },
  1921: {
        functionNames: ['check_multiple_of'],
        tests: [
            { args: [10,[2,5]], expected: true },
            { args: [10,[2,3]], expected: false },
        ]
    },
  1922: {
        functionNames: ['get_sum_of_squares'],
        tests: [
            { args: [[1,2,3]], expected: 14 },
        ]
    },
  1923: {
        functionNames: ['get_product_of_even'],
        tests: [
            { args: [[1,2,3,4,5]], expected: 8 },
        ]
    },
  1924: {
        functionNames: ['get_sum_of_odd'],
        tests: [
            { args: [[1,2,3,4,5]], expected: 9 },
        ]
    },
  1925: {
        functionNames: ['find_second_occurrence'],
        tests: [
            { args: [[1,2,3,2,4],2], expected: 3 },
        ]
    },
  1926: {
        functionNames: ['get_elements_greater_than_average'],
        tests: [
            { args: [[1,2,3,4,5]], expected: [4,5] },
        ]
    },
  1927: {
        functionNames: ['get_elements_less_than_average'],
        tests: [
            { args: [[1,2,3,4,5]], expected: [1,2] },
        ]
    },
  1928: {
        functionNames: ['count_digits_letters'],
        tests: [
            { args: ["abc123"], expected: [3,3] },
        ]
    },
  1929: {
        functionNames: ['get_words_with_length'],
        tests: [
            { args: ["a ab abc abcd",3], expected: ["abc"] },
        ]
    },
  1930: {
    functionNames: ["format_full_address"],
    tests: [{
      args: ["hello", "hello", 3, 4, 5],
      expected: "hello hello, 3, 4 5"
    }]
  },
  1931: {
        functionNames: ['calculate_total_with_discount'],
        tests: [
            { args: [[100],20,0], expected: 80 },
        ]
    },
  1932: {
        functionNames: ['get_common_prefix'],
        tests: [
            { args: ["flower","flow"], expected: "flow" },
        ]
    },
  1933: {
        functionNames: ['get_common_suffix'],
        tests: [
            { args: ["running","walking"], expected: "ing" },
        ]
    },
  1934: {
        functionNames: ['check_all_uppercase_words'],
        tests: [
            { args: ["HELLO WORLD"], expected: true },
            { args: ["hello WORLD"], expected: false },
        ]
    },
  1935: {
        functionNames: ['get_strings_with_length_range'],
        tests: [
            { args: [["a","ab","abc","abcd"],2,3], expected: ["ab","abc"] },
        ]
    },
  1936: {
        functionNames: ['calculate_median'],
        tests: [
            { args: [[1,3,5,7,9]], expected: 5 },
        ]
    },
  1937: {
        functionNames: ['get_mode'],
        tests: [
            { args: [[1,2,2,3,3,3]], expected: 3 },
        ]
    },
  1938: {
    functionNames: ["format_multiline_string"],
    compare: 'printedOrReturn',
    tests: [{
      args: ["hello", 2, 3],
      expected: "Name: hello\nAge: 2\nEmail: 3"
    }]
  },
  1939: {
        functionNames: ['get_numbers_divisible_by_all'],
        tests: [
            { args: [[2,4,6,8,10],[2,4]], expected: [4,8] },
        ]
    },
  1940: {
        functionNames: ['count_vowels_per_word'],
        tests: [
            { args: ["hello world ai"], expected: {"hello":2,"world":1,"ai":2} },
        ]
    },
  1941: {
        functionNames: ['get_words_with_vowel_count'],
        tests: [
            { args: ["hello ai world",2], expected: ["hello","ai"] },
        ]
    },
  1942: {
    functionNames: ["format_table_row"],
    tests: [{
      args: [1, 2, 3],
      expected: "1 | 2 | 3"
    }]
  },
  1943: {
        functionNames: ['get_elements_not_in_both'],
        tests: [
            { args: [[1,2,3],[2,3,4]], expected: [1,4] },
        ]
    },
  1944: {
        functionNames: ['calculate_weighted_average'],
        tests: [
            { args: [[70,80,90],[1,2,1]], expected: 80 },
        ]
    },
  1945: {
        functionNames: ['get_strings_sorted_by_length'],
        tests: [
            { args: [["abc","a","ab"]], expected: ["a","ab","abc"] },
        ]
    },
  1946: {
    functionNames: ["format_percentage_list"],
    tests: [{
      args: [[1, 2, 3, 4, 5]],
      expected: ["1%", "2%", "3%", "4%", "5%"]
    }]
  },
  1947: {
        functionNames: ['get_pairs_summing_to'],
        tests: [
            { args: [[1,2,3,4,5],5], expected: [[1,4],[2,3]] },
        ]
    },
  1948: {
    functionNames: ["count_character_types"],
    tests: [{
      args: ["hello"],
      expected: {"vowels": 2, "consonants": 3, "digits": 0, "spaces": 0}
    }]
  },
  1949: {
        functionNames: ['get_words_by_vowel_count'],
        tests: [
            { args: ["hello ai world ae"], expected: {"1":["world"],"2":["hello","ai","ae"]} },
        ]
    },
  1950: {
        functionNames: ['format_name_with_title'],
        tests: [
            { args: ["John","Doe","Dr"], expected: "Dr. John Doe" },
        ]
    },
  1951: {
    functionNames: ["calculate_area_circle_sector"],
    tests: [{
      args: [1, 5],
      expected: 0.04363323129985824
    }]
  },
  1952: {
        functionNames: ['get_elements_at_multiple_indices'],
        tests: [
            { args: [[10,20,30,40],[0,2]], expected: {"0":10,"2":30} },
        ]
    },
  1953: {
    functionNames: ["check_string_properties"],
    tests: [{
      args: ["hello"],
      expected: {"has_uppercase": false, "has_lowercase": true, "has_digit": false, "has_special": false}
    }]
  },
  1954: {
    functionNames: ["get_numbers_summing_to_range"],
    tests: [{
      args: [[1, 2, 3, 4, 5], 5, 5],
      expected: [[1, 4], [2, 3]]
    }]
  },
  1955: {
    functionNames: ["format_phone_with_country"],
    tests: [{
      args: [5, 2, 5],
      expected: "+5 (2) 5"
    }]
  },
  1956: {
        functionNames: ['get_consecutive_elements'],
        tests: [
            { args: [[1,2,3,4,5],2], expected: [[1,2],[2,3],[3,4],[4,5]] },
        ]
    },
  1957: {
        functionNames: ['calculate_gcd'],
        tests: [
            { args: [12,8], expected: 4 },
        ]
    },
  1958: {
        functionNames: ['calculate_lcm'],
        tests: [
            { args: [12,18], expected: 36 },
        ]
    },
  1959: {
        functionNames: ['get_frequency_dict'],
        tests: [
            { args: [[1,2,2,3]], expected: {"1":1,"2":2,"3":1} },
        ]
    },
  1960: {
        functionNames: ['format_number_with_commas'],
        tests: [
            { args: [1234567], expected: "1,234,567" },
        ]
    },
  1961: {
        functionNames: ['get_words_with_same_length'],
        tests: [
            { args: [["a","ab","a","abc","ab"]], expected: {"1":["a","a"],"2":["ab","ab"],"3":["abc"]} },
        ]
    },
  1962: {
        functionNames: ['check_anagram_pair'],
        tests: [
            { args: ["listen","silent"], expected: true },
            { args: ["hello","world"], expected: false },
        ]
    },
  1963: {
        functionNames: ['get_sublist_sum'],
        tests: [
            { args: [[1,2,3,4,5],1,3], expected: 5 },
        ]
    },
  1964: {
        functionNames: ['format_time_12hour'],
        tests: [
            { args: [14], expected: "2 PM" },
        ]
    },
  1965: {
        functionNames: ['get_elements_between_values'],
        tests: [
            { args: [[1,5,10,15,20],5,15], expected: [10] },
        ]
    },
  1966: {
        functionNames: ['count_substring_occurrences'],
        tests: [
            { args: ["abababa","aba"], expected: 3 },
        ]
    },
  1967: {
        functionNames: ['format_list_as_string'],
        tests: [
            { args: [[1,2,3],", "], expected: "[1, 2, 3]" },
        ]
    },
  1968: {
    functionNames: ["get_unique_combinations"],
    tests: [{
      args: [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]],
      expected: [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5]]
    }]
  },
  1969: {
        functionNames: ['calculate_quadratic_roots'],
        tests: [
            { args: [1, -5, 6], expected: [3, 2] },
            { args: [1, 0, 1], expected: null },
        ]
    },
  1970: {
        functionNames: ['get_strings_matching_pattern'],
        tests: [
            { args: [["hello", "lollipop", "world"], "l"], expected: ["hello", "lollipop"] },
            { args: [["aaaa", "aa", "abc"], "aa"], expected: ["aaaa"] },
        ]
    },
  1971: {
        functionNames: ['format_name_initials'],
        tests: [
            { args: ["John","F","Kennedy"], expected: "J.F.K." },
        ]
    },
  1972: {
        functionNames: ['get_elements_with_condition'],
        tests: [
            { args: [[1, 2, 3, 4, 5, 6]], argExpressions: ["lambda x: x > 3"], expected: [4, 5, 6] },
            { args: [[1, 2, 3, 4, 5, 6]], argExpressions: ["lambda x: x % 2 == 0"], expected: [2, 4, 6] },
        ]
    },
  1973: {
        functionNames: ['calculate_total_area'],
        compare: 'float',
        tests: [
            { args: [[['rectangle', [5, 3]], ['circle', [2]]]], expected: 27.566370614359172 },
        ]
    },
  1974: {
        functionNames: ['get_words_with_repeated_chars'],
        tests: [
            { args: ["hello world aabb"], expected: ["hello","aabb"] },
        ]
    },
  1975: {
    functionNames: ["format_multi_value_string"],
    tests: [{
      args: ["hello", [1, 2, 3]],
      expected: "Name: hello, Scores: 1, 2, 3"
    }]
  },
  1976: {
        functionNames: ['get_symmetric_difference'],
        tests: [
            { args: [[1,2,3],[2,3,4]], expected: [1,4] },
        ]
    },
  1977: {
        functionNames: ['count_words_by_first_letter'],
        tests: [
            { args: ["apple banana apricot"], expected: {"a":2,"b":1} },
        ]
    },
  1978: {
        functionNames: ['format_decimal_places'],
        tests: [
            { args: [3.14159,2], expected: "3.14" },
        ]
    },
  1979: {
        functionNames: ['get_elements_satisfying_all'],
        tests: [
            { args: [[1, 2, 3, 4, 5, 6]], argExpressions: ["lambda x: x > 2", "lambda x: x < 6"], expected: [3, 4, 5] },
            { args: [[1, 2, 3, 4, 5, 6]], argExpressions: ["lambda x: x % 2 == 0", "lambda x: x > 3"], expected: [4, 6] },
        ]
    },
  1980: {
        functionNames: ['calculate_net_price'],
        tests: [
            { args: [100,20,0], expected: 80 },
        ]
    },
  1981: {
        functionNames: ['get_strings_with_all_vowels'],
        tests: [
            { args: [["education","hello","aerious"]], expected: ["education","aerious"] },
        ]
    },
  1982: {
    functionNames: ["format_currency_multiple"],
    tests: [{
      args: [[1, 2, 3, 4, 5]],
      expected: ["$1.00", "$2.00", "$3.00", "$4.00", "$5.00"]
    }]
  },
  1983: {
        functionNames: ['get_consecutive_pairs'],
        tests: [
            { args: [[1,2,3,4]], expected: [[1,2],[2,3],[3,4]] },
        ]
    },
  1984: {
        functionNames: ['calculate_geometric_mean'],
        tests: [
            { args: [[2,8]], expected: 4 },
        ]
    },
  1985: {
        functionNames: ['get_words_sorted_by_vowels'],
        tests: [
            { args: ["hello ai world"], expected: ["world","hello","ai"] },
        ]
    },
  1986: {
        functionNames: ['format_name_age_grade'],
        tests: [
            { args: ["Alice",15,"A"], expected: "Alice (Age: 15) - Grade: A" },
        ]
    },
  1987: {
        functionNames: ['get_elements_with_max_frequency'],
        tests: [
            { args: [[1,2,2,3,3,3]], expected: [3] },
        ]
    },
  1988: {
    functionNames: ["calculate_harmonic_mean"],
    tests: [{
      args: [[1, 2, 3, 4, 5]],
      expected: 2.18978102189781
    }]
  },
  1989: {
    functionNames: ["format_list_items"],
    tests: [{
      args: [[1, 2, 3, 4, 5]],
      expected: "Item 1: 1, Item 2: 2, Item 3: 3, Item 4: 4, Item 5: 5"
    }]
  },
  1990: {
        functionNames: ['get_strings_with_pattern_count'],
        tests: [
            { args: [["hello", "lollipop", "world"], "l", 2], expected: ["hello"] },
            { args: [["aaa", "aa", "a"], "a", 1], expected: ["a"] },
        ]
    },
  1991: {
    functionNames: ["calculate_compound_growth"],
    tests: [{
      args: [5, 2, 3],
      expected: 5.306040000000001
    }]
  },
  1992: {
    functionNames: ["get_elements_by_frequency_range"],
    tests: [{
      args: [[1, 2, 3, 4, 5], 5, 5],
      expected: []
    }]
  },
  1993: {
        functionNames: ['format_table_data'],
        tests: [
            { args: [[["Alice", 85], ["Bob", 90], ["Charlie", 75]]], expected: "Alice      | 85\nBob        | 90\nCharlie    | 75" },
        ]
    },
  1994: {
        functionNames: ['get_words_with_unique_chars'],
        tests: [
            { args: ["hello world abc"], expected: ["world","abc"] },
        ]
    },
  1995: {
        functionNames: ['calculate_total_with_multiple_discounts'],
        compare: 'float',
        tests: [
            { args: [100, [10, 20]], expected: 72 },
            { args: [200, [50, 10]], expected: 90 },
        ]
    },
  1996: {
    functionNames: ["format_multi_line_address"],
    compare: 'printedOrReturn',
    tests: [{
      args: ["hello", "hello", 3, "{1, 2, 3}", {"a": 1, "b": 2}],
      expected: "hello\nhello\n3, {1, 2, 3} {'a': 1, 'b': 2}"
    }]
  },
  1997: {
        functionNames: ['get_elements_matching_multiple_patterns'],
        tests: [
            { args: [["hello", "world", "python", "programming"], "o", "r"], expected: ["world", "programming"] },
            { args: [["abc", "abd", "bcd"], "a", "b"], expected: ["abc", "abd"] },
        ]
    },
  1998: {
    functionNames: ["calculate_statistical_summary"],
    tests: [{
      args: [[1, 2, 3, 4, 5]],
      expected: {"mean": 3, "median": 3, "min": 1, "max": 5, "range": 4}
    }]
  },
  1999: {
    functionNames: ["format_contact_info"],
    compare: 'printedOrReturn',
    tests: [{
      args: ["hello", 5, 3, {"a": 1, "b": 2}],
      expected: "Name: hello\nPhone: 5\nEmail: 3\nAddress: {'a': 1, 'b': 2}"
    }]
  },
  2000: {
    functionNames: ["get_comprehensive_statistics"],
    tests: [{
      args: [[1, 2, 3, 4, 5]],
      expected: {"sum": 15, "average": 3, "min": 1, "max": 5, "count": 5, "standard_deviation": 1.4142135623730951}
    }]
  }

};
