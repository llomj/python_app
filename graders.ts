export type CompareMode = 'exact' | 'float' | 'printedOrReturn';

export interface AutoTestCase {
    args: unknown[];
    expected: unknown;
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
    }
};
