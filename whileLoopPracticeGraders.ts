import type { AutoGrader } from './graders';

export const WHILE_LOOP_PRACTICE_GRADERS: Record<number, AutoGrader> = {
  "2381": {
    "functionNames": [
      "count_up"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": [
          1,
          2,
          3,
          4,
          5
        ]
      },
      {
        "args": [
          1
        ],
        "expected": [
          1
        ]
      },
      {
        "args": [
          0
        ],
        "expected": []
      }
    ]
  },
  "2382": {
    "functionNames": [
      "count_down"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          3
        ],
        "expected": [
          3,
          2,
          1,
          0
        ]
      },
      {
        "args": [
          0
        ],
        "expected": [
          0
        ]
      },
      {
        "args": [
          5
        ],
        "expected": [
          5,
          4,
          3,
          2,
          1,
          0
        ]
      }
    ]
  },
  "2383": {
    "functionNames": [
      "even_numbers"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          7
        ],
        "expected": [
          0,
          2,
          4,
          6
        ]
      },
      {
        "args": [
          0
        ],
        "expected": [
          0
        ]
      },
      {
        "args": [
          10
        ],
        "expected": [
          0,
          2,
          4,
          6,
          8,
          10
        ]
      }
    ]
  },
  "2384": {
    "functionNames": [
      "odd_numbers"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          8
        ],
        "expected": [
          1,
          3,
          5,
          7
        ]
      },
      {
        "args": [
          1
        ],
        "expected": [
          1
        ]
      },
      {
        "args": [
          0
        ],
        "expected": []
      }
    ]
  },
  "2385": {
    "functionNames": [
      "multiples_up_to"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          3,
          10
        ],
        "expected": [
          3,
          6,
          9
        ]
      },
      {
        "args": [
          5,
          5
        ],
        "expected": [
          5
        ]
      },
      {
        "args": [
          4,
          3
        ],
        "expected": []
      }
    ]
  },
  "2386": {
    "functionNames": [
      "squares_to_n"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          4
        ],
        "expected": [
          1,
          4,
          9,
          16
        ]
      },
      {
        "args": [
          1
        ],
        "expected": [
          1
        ]
      },
      {
        "args": [
          0
        ],
        "expected": []
      }
    ]
  },
  "2387": {
    "functionNames": [
      "cubes_to_n"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          3
        ],
        "expected": [
          1,
          8,
          27
        ]
      },
      {
        "args": [
          1
        ],
        "expected": [
          1
        ]
      },
      {
        "args": [
          0
        ],
        "expected": []
      }
    ]
  },
  "2388": {
    "functionNames": [
      "powers_of_two"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          10
        ],
        "expected": [
          1,
          2,
          4,
          8
        ]
      },
      {
        "args": [
          1
        ],
        "expected": [
          1
        ]
      },
      {
        "args": [
          0
        ],
        "expected": []
      }
    ]
  },
  "2389": {
    "functionNames": [
      "arithmetic_sequence"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          2,
          3,
          4
        ],
        "expected": [
          2,
          5,
          8,
          11
        ]
      },
      {
        "args": [
          5,
          -2,
          3
        ],
        "expected": [
          5,
          3,
          1
        ]
      },
      {
        "args": [
          1,
          4,
          0
        ],
        "expected": []
      }
    ]
  },
  "2390": {
    "functionNames": [
      "count_down_by_step"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          10,
          3
        ],
        "expected": [
          10,
          7,
          4,
          1
        ]
      },
      {
        "args": [
          4,
          2
        ],
        "expected": [
          4,
          2,
          0
        ]
      },
      {
        "args": [
          1,
          5
        ],
        "expected": [
          1
        ]
      }
    ]
  },
  "2391": {
    "functionNames": [
      "sum_to_n"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 15
      },
      {
        "args": [
          1
        ],
        "expected": 1
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ]
  },
  "2392": {
    "functionNames": [
      "factorial_while"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 120
      },
      {
        "args": [
          0
        ],
        "expected": 1
      },
      {
        "args": [
          3
        ],
        "expected": 6
      }
    ]
  },
  "2393": {
    "functionNames": [
      "sum_squares"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          3
        ],
        "expected": 14
      },
      {
        "args": [
          1
        ],
        "expected": 1
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ]
  },
  "2394": {
    "functionNames": [
      "sum_cubes"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          3
        ],
        "expected": 36
      },
      {
        "args": [
          2
        ],
        "expected": 9
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ]
  },
  "2395": {
    "functionNames": [
      "count_multiples"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          10,
          3
        ],
        "expected": 3
      },
      {
        "args": [
          12,
          4
        ],
        "expected": 3
      },
      {
        "args": [
          2,
          5
        ],
        "expected": 0
      }
    ]
  },
  "2396": {
    "functionNames": [
      "sum_even_to_n"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          6
        ],
        "expected": 12
      },
      {
        "args": [
          1
        ],
        "expected": 0
      },
      {
        "args": [
          10
        ],
        "expected": 30
      }
    ]
  },
  "2397": {
    "functionNames": [
      "sum_odd_to_n"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          7
        ],
        "expected": 16
      },
      {
        "args": [
          1
        ],
        "expected": 1
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ]
  },
  "2398": {
    "functionNames": [
      "product_range"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          2,
          4
        ],
        "expected": 24
      },
      {
        "args": [
          5,
          5
        ],
        "expected": 5
      },
      {
        "args": [
          3,
          2
        ],
        "expected": 1
      }
    ]
  },
  "2399": {
    "functionNames": [
      "steps_to_reach"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          0,
          10,
          3
        ],
        "expected": 4
      },
      {
        "args": [
          5,
          5,
          2
        ],
        "expected": 0
      },
      {
        "args": [
          2,
          9,
          1
        ],
        "expected": 7
      }
    ]
  },
  "2400": {
    "functionNames": [
      "integer_power"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          2,
          5
        ],
        "expected": 32
      },
      {
        "args": [
          7,
          0
        ],
        "expected": 1
      },
      {
        "args": [
          -3,
          3
        ],
        "expected": -27
      }
    ]
  },
  "2401": {
    "functionNames": [
      "digit_count"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 1
      },
      {
        "args": [
          482
        ],
        "expected": 3
      },
      {
        "args": [
          10000
        ],
        "expected": 5
      }
    ]
  },
  "2402": {
    "functionNames": [
      "digit_sum"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          482
        ],
        "expected": 14
      },
      {
        "args": [
          -91
        ],
        "expected": 10
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ]
  },
  "2403": {
    "functionNames": [
      "digit_product"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          234
        ],
        "expected": 24
      },
      {
        "args": [
          105
        ],
        "expected": 0
      },
      {
        "args": [
          7
        ],
        "expected": 7
      }
    ]
  },
  "2404": {
    "functionNames": [
      "reverse_integer"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          1234
        ],
        "expected": 4321
      },
      {
        "args": [
          120
        ],
        "expected": 21
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ]
  },
  "2405": {
    "functionNames": [
      "count_zero_digits"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          1002
        ],
        "expected": 2
      },
      {
        "args": [
          7
        ],
        "expected": 0
      },
      {
        "args": [
          0
        ],
        "expected": 1
      }
    ]
  },
  "2406": {
    "functionNames": [
      "count_specific_digit"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          14424,
          4
        ],
        "expected": 3
      },
      {
        "args": [
          123,
          8
        ],
        "expected": 0
      },
      {
        "args": [
          0,
          0
        ],
        "expected": 1
      }
    ]
  },
  "2407": {
    "functionNames": [
      "largest_digit"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          5824
        ],
        "expected": 8
      },
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          111
        ],
        "expected": 1
      }
    ]
  },
  "2408": {
    "functionNames": [
      "smallest_digit"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          5824
        ],
        "expected": 2
      },
      {
        "args": [
          907
        ],
        "expected": 0
      },
      {
        "args": [
          6
        ],
        "expected": 6
      }
    ]
  },
  "2409": {
    "functionNames": [
      "digital_root"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          9875
        ],
        "expected": 2
      },
      {
        "args": [
          9
        ],
        "expected": 9
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ]
  },
  "2410": {
    "functionNames": [
      "decimal_to_binary"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          10
        ],
        "expected": "1010"
      },
      {
        "args": [
          1
        ],
        "expected": "1"
      },
      {
        "args": [
          0
        ],
        "expected": "0"
      }
    ]
  },
  "2411": {
    "functionNames": [
      "reverse_text"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          "python"
        ],
        "expected": "nohtyp"
      },
      {
        "args": [
          "a"
        ],
        "expected": "a"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      }
    ]
  },
  "2412": {
    "functionNames": [
      "count_vowels_while"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          "Hello"
        ],
        "expected": 2
      },
      {
        "args": [
          "rhythm"
        ],
        "expected": 0
      },
      {
        "args": [
          "AEIOU"
        ],
        "expected": 5
      }
    ]
  },
  "2413": {
    "functionNames": [
      "count_consonants_while"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          "Hello!"
        ],
        "expected": 3
      },
      {
        "args": [
          "AEIOU"
        ],
        "expected": 0
      },
      {
        "args": [
          "sky 2"
        ],
        "expected": 3
      }
    ]
  },
  "2414": {
    "functionNames": [
      "remove_vowels_while"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          "hello"
        ],
        "expected": "hll"
      },
      {
        "args": [
          "AEIOUxyz"
        ],
        "expected": "xyz"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      }
    ]
  },
  "2415": {
    "functionNames": [
      "remove_spaces_while"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          "a b c"
        ],
        "expected": "abc"
      },
      {
        "args": [
          " no spaces "
        ],
        "expected": "nospaces"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      }
    ]
  },
  "2416": {
    "functionNames": [
      "count_character_while"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          "banana",
          "a"
        ],
        "expected": 3
      },
      {
        "args": [
          "Mississippi",
          "s"
        ],
        "expected": 4
      },
      {
        "args": [
          "abc",
          "z"
        ],
        "expected": 0
      }
    ]
  },
  "2417": {
    "functionNames": [
      "first_character_index"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          "banana",
          "n"
        ],
        "expected": 2
      },
      {
        "args": [
          "abc",
          "z"
        ],
        "expected": -1
      },
      {
        "args": [
          "aaa",
          "a"
        ],
        "expected": 0
      }
    ]
  },
  "2418": {
    "functionNames": [
      "last_character_index"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          "banana",
          "a"
        ],
        "expected": 5
      },
      {
        "args": [
          "abc",
          "z"
        ],
        "expected": -1
      },
      {
        "args": [
          "aaa",
          "a"
        ],
        "expected": 2
      }
    ]
  },
  "2419": {
    "functionNames": [
      "is_palindrome_while"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          "level"
        ],
        "expected": true
      },
      {
        "args": [
          "python"
        ],
        "expected": false
      },
      {
        "args": [
          ""
        ],
        "expected": true
      }
    ]
  },
  "2420": {
    "functionNames": [
      "every_other_character"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          "abcdef"
        ],
        "expected": "ace"
      },
      {
        "args": [
          "python"
        ],
        "expected": "pto"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      }
    ]
  },
  "2421": {
    "functionNames": [
      "sum_list_while"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3
          ]
        ],
        "expected": 6
      },
      {
        "args": [
          [
            -2,
            5
          ]
        ],
        "expected": 3
      },
      {
        "args": [
          []
        ],
        "expected": 0
      }
    ]
  },
  "2422": {
    "functionNames": [
      "product_list_while"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            2,
            3,
            4
          ]
        ],
        "expected": 24
      },
      {
        "args": [
          [
            -2,
            5
          ]
        ],
        "expected": -10
      },
      {
        "args": [
          []
        ],
        "expected": 1
      }
    ]
  },
  "2423": {
    "functionNames": [
      "minimum_while"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            4,
            1,
            7
          ]
        ],
        "expected": 1
      },
      {
        "args": [
          [
            -3,
            -8,
            -1
          ]
        ],
        "expected": -8
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": 5
      }
    ]
  },
  "2424": {
    "functionNames": [
      "maximum_while"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            4,
            1,
            7
          ]
        ],
        "expected": 7
      },
      {
        "args": [
          [
            -3,
            -8,
            -1
          ]
        ],
        "expected": -1
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": 5
      }
    ]
  },
  "2425": {
    "functionNames": [
      "count_positive_while"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            -1,
            0,
            2,
            4
          ]
        ],
        "expected": 2
      },
      {
        "args": [
          [
            -3
          ]
        ],
        "expected": 0
      },
      {
        "args": [
          [
            1,
            2
          ]
        ],
        "expected": 2
      }
    ]
  },
  "2426": {
    "functionNames": [
      "negative_values_while"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            -1,
            0,
            2,
            -4
          ]
        ],
        "expected": [
          -1,
          -4
        ]
      },
      {
        "args": [
          [
            1,
            2
          ]
        ],
        "expected": []
      },
      {
        "args": [
          [
            -3
          ]
        ],
        "expected": [
          -3
        ]
      }
    ]
  },
  "2427": {
    "functionNames": [
      "square_values_while"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3
          ]
        ],
        "expected": [
          1,
          4,
          9
        ]
      },
      {
        "args": [
          [
            -2,
            0
          ]
        ],
        "expected": [
          4,
          0
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ]
  },
  "2428": {
    "functionNames": [
      "reverse_list_while"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3
          ]
        ],
        "expected": [
          3,
          2,
          1
        ]
      },
      {
        "args": [
          [
            "a"
          ]
        ],
        "expected": [
          "a"
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ]
  },
  "2429": {
    "functionNames": [
      "running_totals_while"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3
          ]
        ],
        "expected": [
          1,
          3,
          6
        ]
      },
      {
        "args": [
          [
            5,
            -2
          ]
        ],
        "expected": [
          5,
          3
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ]
  },
  "2430": {
    "functionNames": [
      "unique_in_order_while"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            1,
            3
          ]
        ],
        "expected": [
          1,
          2,
          3
        ]
      },
      {
        "args": [
          [
            "a",
            "a"
          ]
        ],
        "expected": [
          "a"
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ]
  },
  "2431": {
    "functionNames": [
      "first_target_index"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            3,
            8,
            8
          ],
          8
        ],
        "expected": 1
      },
      {
        "args": [
          [
            1,
            2
          ],
          9
        ],
        "expected": -1
      },
      {
        "args": [
          [],
          1
        ],
        "expected": -1
      }
    ]
  },
  "2432": {
    "functionNames": [
      "first_negative_index"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            2,
            0,
            -3,
            4
          ]
        ],
        "expected": 2
      },
      {
        "args": [
          [
            1,
            2
          ]
        ],
        "expected": -1
      },
      {
        "args": [
          [
            -1
          ]
        ],
        "expected": 0
      }
    ]
  },
  "2433": {
    "functionNames": [
      "prefix_before_marker"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            0,
            3
          ],
          0
        ],
        "expected": [
          1,
          2
        ]
      },
      {
        "args": [
          [
            "a",
            "b"
          ],
          "x"
        ],
        "expected": [
          "a",
          "b"
        ]
      },
      {
        "args": [
          [
            9
          ],
          9
        ],
        "expected": []
      }
    ]
  },
  "2434": {
    "functionNames": [
      "take_while_positive"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            2,
            3,
            0,
            4
          ]
        ],
        "expected": [
          2,
          3
        ]
      },
      {
        "args": [
          [
            -1,
            2
          ]
        ],
        "expected": []
      },
      {
        "args": [
          [
            1,
            2
          ]
        ],
        "expected": [
          1,
          2
        ]
      }
    ]
  },
  "2435": {
    "functionNames": [
      "sum_until_limit"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            2,
            3,
            5
          ],
          6
        ],
        "expected": 5
      },
      {
        "args": [
          [
            4,
            1
          ],
          3
        ],
        "expected": 0
      },
      {
        "args": [
          [
            1,
            2
          ],
          10
        ],
        "expected": 3
      }
    ]
  },
  "2436": {
    "functionNames": [
      "drop_leading_zeros"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            0,
            0,
            3,
            0
          ]
        ],
        "expected": [
          3,
          0
        ]
      },
      {
        "args": [
          [
            0,
            0
          ]
        ],
        "expected": []
      },
      {
        "args": [
          [
            2,
            0
          ]
        ],
        "expected": [
          2,
          0
        ]
      }
    ]
  },
  "2437": {
    "functionNames": [
      "common_prefix"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          "flower",
          "flow"
        ],
        "expected": "flow"
      },
      {
        "args": [
          "cat",
          "dog"
        ],
        "expected": ""
      },
      {
        "args": [
          "same",
          "same"
        ],
        "expected": "same"
      }
    ]
  },
  "2438": {
    "functionNames": [
      "count_substring"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          "aaaa",
          "aa"
        ],
        "expected": 3
      },
      {
        "args": [
          "banana",
          "ana"
        ],
        "expected": 2
      },
      {
        "args": [
          "abc",
          "z"
        ],
        "expected": 0
      }
    ]
  },
  "2439": {
    "functionNames": [
      "manual_startswith"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          "python",
          "py"
        ],
        "expected": true
      },
      {
        "args": [
          "cat",
          "car"
        ],
        "expected": false
      },
      {
        "args": [
          "a",
          ""
        ],
        "expected": true
      }
    ]
  },
  "2440": {
    "functionNames": [
      "manual_split"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          "a,b,c",
          ","
        ],
        "expected": [
          "a",
          "b",
          "c"
        ]
      },
      {
        "args": [
          "one",
          ";"
        ],
        "expected": [
          "one"
        ]
      },
      {
        "args": [
          "a::b",
          ":"
        ],
        "expected": [
          "a",
          "",
          "b"
        ]
      }
    ]
  },
  "2441": {
    "functionNames": [
      "flatten_nested"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              2
            ],
            [
              3
            ]
          ]
        ],
        "expected": [
          1,
          2,
          3
        ]
      },
      {
        "args": [
          [
            [],
            [
              4
            ]
          ]
        ],
        "expected": [
          4
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ]
  },
  "2442": {
    "functionNames": [
      "matrix_total"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              2
            ],
            [
              3,
              4
            ]
          ]
        ],
        "expected": 10
      },
      {
        "args": [
          [
            [],
            [
              5
            ]
          ]
        ],
        "expected": 5
      },
      {
        "args": [
          []
        ],
        "expected": 0
      }
    ]
  },
  "2443": {
    "functionNames": [
      "matrix_row_totals"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              2
            ],
            [
              3,
              4
            ]
          ]
        ],
        "expected": [
          3,
          7
        ]
      },
      {
        "args": [
          [
            [],
            [
              5
            ]
          ]
        ],
        "expected": [
          0,
          5
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ]
  },
  "2444": {
    "functionNames": [
      "transpose_matrix"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              2
            ],
            [
              3,
              4
            ]
          ]
        ],
        "expected": [
          [
            1,
            3
          ],
          [
            2,
            4
          ]
        ]
      },
      {
        "args": [
          [
            [
              1,
              2,
              3
            ]
          ]
        ],
        "expected": [
          [
            1
          ],
          [
            2
          ],
          [
            3
          ]
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ]
  },
  "2445": {
    "functionNames": [
      "merge_alternating"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ],
          [
            "a",
            "b"
          ]
        ],
        "expected": [
          1,
          "a",
          2,
          "b"
        ]
      },
      {
        "args": [
          [
            1,
            2,
            3
          ],
          [
            "x"
          ]
        ],
        "expected": [
          1,
          "x",
          2,
          3
        ]
      },
      {
        "args": [
          [],
          [
            4
          ]
        ],
        "expected": [
          4
        ]
      }
    ]
  },
  "2446": {
    "functionNames": [
      "chunk_list"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            4,
            5
          ],
          2
        ],
        "expected": [
          [
            1,
            2
          ],
          [
            3,
            4
          ],
          [
            5
          ]
        ]
      },
      {
        "args": [
          [
            "a",
            "b"
          ],
          3
        ],
        "expected": [
          [
            "a",
            "b"
          ]
        ]
      },
      {
        "args": [
          [],
          2
        ],
        "expected": []
      }
    ]
  },
  "2447": {
    "functionNames": [
      "rotate_left_while"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            4
          ],
          1
        ],
        "expected": [
          2,
          3,
          4,
          1
        ]
      },
      {
        "args": [
          [
            "a",
            "b",
            "c"
          ],
          4
        ],
        "expected": [
          "b",
          "c",
          "a"
        ]
      },
      {
        "args": [
          [],
          2
        ],
        "expected": []
      }
    ]
  },
  "2448": {
    "functionNames": [
      "sliding_sums"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            4
          ],
          2
        ],
        "expected": [
          3,
          5,
          7
        ]
      },
      {
        "args": [
          [
            5,
            1,
            2
          ],
          3
        ],
        "expected": [
          8
        ]
      },
      {
        "args": [
          [
            1
          ],
          2
        ],
        "expected": []
      }
    ]
  },
  "2449": {
    "functionNames": [
      "frequency_table"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            1
          ]
        ],
        "expected": {
          "1": 2,
          "2": 1
        }
      },
      {
        "args": [
          [
            "a",
            "a"
          ]
        ],
        "expected": {
          "a": 2
        }
      },
      {
        "args": [
          []
        ],
        "expected": {}
      }
    ]
  },
  "2450": {
    "functionNames": [
      "longest_word_while"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "python",
            "code"
          ]
        ],
        "expected": "python"
      },
      {
        "args": [
          [
            "same",
            "size"
          ]
        ],
        "expected": "same"
      },
      {
        "args": [
          []
        ],
        "expected": ""
      }
    ]
  },
  "2451": {
    "functionNames": [
      "gcd_while"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          48,
          18
        ],
        "expected": 6
      },
      {
        "args": [
          7,
          5
        ],
        "expected": 1
      },
      {
        "args": [
          0,
          9
        ],
        "expected": 9
      }
    ]
  },
  "2452": {
    "functionNames": [
      "lcm_while"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          4,
          6
        ],
        "expected": 12
      },
      {
        "args": [
          5,
          7
        ],
        "expected": 35
      },
      {
        "args": [
          0,
          3
        ],
        "expected": 0
      }
    ]
  },
  "2453": {
    "functionNames": [
      "is_prime_while"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          29
        ],
        "expected": true
      },
      {
        "args": [
          21
        ],
        "expected": false
      },
      {
        "args": [
          1
        ],
        "expected": false
      }
    ]
  },
  "2454": {
    "functionNames": [
      "divisors_while"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          12
        ],
        "expected": [
          1,
          2,
          3,
          4,
          6,
          12
        ]
      },
      {
        "args": [
          1
        ],
        "expected": [
          1
        ]
      },
      {
        "args": [
          7
        ],
        "expected": [
          1,
          7
        ]
      }
    ]
  },
  "2455": {
    "functionNames": [
      "prime_factors_while"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          60
        ],
        "expected": [
          2,
          2,
          3,
          5
        ]
      },
      {
        "args": [
          13
        ],
        "expected": [
          13
        ]
      },
      {
        "args": [
          1
        ],
        "expected": []
      }
    ]
  },
  "2456": {
    "functionNames": [
      "fibonacci_while"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          6
        ],
        "expected": [
          0,
          1,
          1,
          2,
          3,
          5
        ]
      },
      {
        "args": [
          1
        ],
        "expected": [
          0
        ]
      },
      {
        "args": [
          0
        ],
        "expected": []
      }
    ]
  },
  "2457": {
    "functionNames": [
      "collatz_steps"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          6
        ],
        "expected": 8
      },
      {
        "args": [
          1
        ],
        "expected": 0
      },
      {
        "args": [
          3
        ],
        "expected": 7
      }
    ]
  },
  "2458": {
    "functionNames": [
      "is_perfect_number"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          6
        ],
        "expected": true
      },
      {
        "args": [
          28
        ],
        "expected": true
      },
      {
        "args": [
          12
        ],
        "expected": false
      }
    ]
  },
  "2459": {
    "functionNames": [
      "is_armstrong_while"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          153
        ],
        "expected": true
      },
      {
        "args": [
          9474
        ],
        "expected": true
      },
      {
        "args": [
          123
        ],
        "expected": false
      }
    ]
  },
  "2460": {
    "functionNames": [
      "nth_prime_while"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          1
        ],
        "expected": 2
      },
      {
        "args": [
          5
        ],
        "expected": 11
      },
      {
        "args": [
          10
        ],
        "expected": 29
      }
    ]
  },
  "2461": {
    "functionNames": [
      "bubble_sort_while"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            3,
            1,
            2
          ]
        ],
        "expected": [
          1,
          2,
          3
        ]
      },
      {
        "args": [
          [
            -1,
            4,
            0
          ]
        ],
        "expected": [
          -1,
          0,
          4
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ]
  },
  "2462": {
    "functionNames": [
      "insertion_sort_while"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            4,
            2,
            3,
            1
          ]
        ],
        "expected": [
          1,
          2,
          3,
          4
        ]
      },
      {
        "args": [
          [
            1
          ]
        ],
        "expected": [
          1
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ]
  },
  "2463": {
    "functionNames": [
      "binary_search_while"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            1,
            3,
            5,
            7
          ],
          5
        ],
        "expected": 2
      },
      {
        "args": [
          [
            2,
            4
          ],
          3
        ],
        "expected": -1
      },
      {
        "args": [
          [
            9
          ],
          9
        ],
        "expected": 0
      }
    ]
  },
  "2464": {
    "functionNames": [
      "merge_sorted_while"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            1,
            3
          ],
          [
            2,
            4
          ]
        ],
        "expected": [
          1,
          2,
          3,
          4
        ]
      },
      {
        "args": [
          [],
          [
            1
          ]
        ],
        "expected": [
          1
        ]
      },
      {
        "args": [
          [
            2
          ],
          [
            2
          ]
        ],
        "expected": [
          2,
          2
        ]
      }
    ]
  },
  "2465": {
    "functionNames": [
      "longest_increasing_run"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            1,
            2
          ]
        ],
        "expected": 3
      },
      {
        "args": [
          [
            5,
            4
          ]
        ],
        "expected": 1
      },
      {
        "args": [
          []
        ],
        "expected": 0
      }
    ]
  },
  "2466": {
    "functionNames": [
      "run_length_encode"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          "aaabbc"
        ],
        "expected": "a3b2c1"
      },
      {
        "args": [
          "x"
        ],
        "expected": "x1"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      }
    ]
  },
  "2467": {
    "functionNames": [
      "balanced_parentheses"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          "(a(b))"
        ],
        "expected": true
      },
      {
        "args": [
          "(()"
        ],
        "expected": false
      },
      {
        "args": [
          ")("
        ],
        "expected": false
      }
    ]
  },
  "2468": {
    "functionNames": [
      "remove_adjacent_duplicates"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          "abbaca"
        ],
        "expected": "ca"
      },
      {
        "args": [
          "azxxzy"
        ],
        "expected": "ay"
      },
      {
        "args": [
          "abc"
        ],
        "expected": "abc"
      }
    ]
  },
  "2469": {
    "functionNames": [
      "convert_base"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          31,
          16
        ],
        "expected": "1F"
      },
      {
        "args": [
          10,
          2
        ],
        "expected": "1010"
      },
      {
        "args": [
          0,
          8
        ],
        "expected": "0"
      }
    ]
  },
  "2470": {
    "functionNames": [
      "modular_power"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          2,
          10,
          1000
        ],
        "expected": 24
      },
      {
        "args": [
          3,
          4,
          5
        ],
        "expected": 1
      },
      {
        "args": [
          7,
          0,
          9
        ],
        "expected": 1
      }
    ]
  },
  "2471": {
    "functionNames": [
      "sqrt_approximation"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "compare": "float",
    "tests": [
      {
        "args": [
          9,
          1e-8
        ],
        "expected": 3
      },
      {
        "args": [
          2,
          1e-8
        ],
        "expected": 1.4142135623730951
      },
      {
        "args": [
          0,
          1e-8
        ],
        "expected": 0
      }
    ]
  },
  "2472": {
    "functionNames": [
      "happy_number"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          19
        ],
        "expected": true
      },
      {
        "args": [
          2
        ],
        "expected": false
      },
      {
        "args": [
          1
        ],
        "expected": true
      }
    ]
  },
  "2473": {
    "functionNames": [
      "look_and_say"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          "1",
          4
        ],
        "expected": "111221"
      },
      {
        "args": [
          "21",
          1
        ],
        "expected": "1211"
      },
      {
        "args": [
          "3",
          0
        ],
        "expected": "3"
      }
    ]
  },
  "2474": {
    "functionNames": [
      "longest_unique_substring"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          "abcabcbb"
        ],
        "expected": 3
      },
      {
        "args": [
          "bbbbb"
        ],
        "expected": 1
      },
      {
        "args": [
          ""
        ],
        "expected": 0
      }
    ]
  },
  "2475": {
    "functionNames": [
      "lower_bound_while"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            1,
            3,
            3,
            7
          ],
          3
        ],
        "expected": 1
      },
      {
        "args": [
          [
            1,
            4
          ],
          2
        ],
        "expected": 1
      },
      {
        "args": [
          [],
          5
        ],
        "expected": 0
      }
    ]
  },
  "2476": {
    "functionNames": [
      "upper_bound_while"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            1,
            3,
            3,
            7
          ],
          3
        ],
        "expected": 3
      },
      {
        "args": [
          [
            1,
            4
          ],
          4
        ],
        "expected": 2
      },
      {
        "args": [
          [],
          5
        ],
        "expected": 0
      }
    ]
  },
  "2477": {
    "functionNames": [
      "second_largest_distinct"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            3,
            1,
            3,
            2
          ]
        ],
        "expected": 2
      },
      {
        "args": [
          [
            5,
            5
          ]
        ],
        "expected": null
      },
      {
        "args": [
          [
            -1,
            -3,
            -2
          ]
        ],
        "expected": -2
      }
    ]
  },
  "2478": {
    "functionNames": [
      "caesar_shift_while"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          "Abc!",
          2
        ],
        "expected": "Cde!"
      },
      {
        "args": [
          "xyz",
          3
        ],
        "expected": "abc"
      },
      {
        "args": [
          "Hi",
          0
        ],
        "expected": "Hi"
      }
    ]
  },
  "2479": {
    "functionNames": [
      "matrix_column_totals"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              2
            ],
            [
              3,
              4
            ]
          ]
        ],
        "expected": [
          4,
          6
        ]
      },
      {
        "args": [
          [
            [
              5,
              1,
              2
            ]
          ]
        ],
        "expected": [
          5,
          1,
          2
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ]
  },
  "2480": {
    "functionNames": [
      "run_length_decode"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          "a3b2"
        ],
        "expected": "aaabb"
      },
      {
        "args": [
          "x1"
        ],
        "expected": "x"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      }
    ]
  },
  "5658": {
    "functionNames": [
      "inclusive_range_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          2,
          5
        ],
        "expected": [
          2,
          3,
          4,
          5
        ]
      },
      {
        "args": [
          4,
          4
        ],
        "expected": [
          4
        ]
      },
      {
        "args": [
          5,
          3
        ],
        "expected": []
      }
    ]
  },
  "5659": {
    "functionNames": [
      "exclusive_range_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          2,
          5
        ],
        "expected": [
          2,
          3,
          4
        ]
      },
      {
        "args": [
          4,
          4
        ],
        "expected": []
      },
      {
        "args": [
          0,
          2
        ],
        "expected": [
          0,
          1
        ]
      }
    ]
  },
  "5660": {
    "functionNames": [
      "repeat_value_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          "a",
          3
        ],
        "expected": [
          "a",
          "a",
          "a"
        ]
      },
      {
        "args": [
          7,
          1
        ],
        "expected": [
          7
        ]
      },
      {
        "args": [
          0,
          0
        ],
        "expected": []
      }
    ]
  },
  "5661": {
    "functionNames": [
      "first_even_values_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          4
        ],
        "expected": [
          0,
          2,
          4,
          6
        ]
      },
      {
        "args": [
          1
        ],
        "expected": [
          0
        ]
      },
      {
        "args": [
          0
        ],
        "expected": []
      }
    ]
  },
  "5662": {
    "functionNames": [
      "first_odd_values_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          4
        ],
        "expected": [
          1,
          3,
          5,
          7
        ]
      },
      {
        "args": [
          1
        ],
        "expected": [
          1
        ]
      },
      {
        "args": [
          0
        ],
        "expected": []
      }
    ]
  },
  "5663": {
    "functionNames": [
      "first_multiples_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          3,
          4
        ],
        "expected": [
          3,
          6,
          9,
          12
        ]
      },
      {
        "args": [
          5,
          1
        ],
        "expected": [
          5
        ]
      },
      {
        "args": [
          2,
          0
        ],
        "expected": []
      }
    ]
  },
  "5664": {
    "functionNames": [
      "positive_countdown_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          4
        ],
        "expected": [
          4,
          3,
          2,
          1
        ]
      },
      {
        "args": [
          1
        ],
        "expected": [
          1
        ]
      },
      {
        "args": [
          0
        ],
        "expected": []
      }
    ]
  },
  "5665": {
    "functionNames": [
      "step_up_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          1,
          7,
          2
        ],
        "expected": [
          1,
          3,
          5,
          7
        ]
      },
      {
        "args": [
          3,
          3,
          4
        ],
        "expected": [
          3
        ]
      },
      {
        "args": [
          5,
          2,
          1
        ],
        "expected": []
      }
    ]
  },
  "5666": {
    "functionNames": [
      "step_down_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          8,
          3
        ],
        "expected": [
          8,
          5,
          2
        ]
      },
      {
        "args": [
          2,
          5
        ],
        "expected": [
          2
        ]
      },
      {
        "args": [
          0,
          2
        ],
        "expected": []
      }
    ]
  },
  "5667": {
    "functionNames": [
      "number_labels_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          3
        ],
        "expected": [
          "Number 1",
          "Number 2",
          "Number 3"
        ]
      },
      {
        "args": [
          1
        ],
        "expected": [
          "Number 1"
        ]
      },
      {
        "args": [
          0
        ],
        "expected": []
      }
    ]
  },
  "5668": {
    "functionNames": [
      "repeated_addition_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          4,
          3
        ],
        "expected": 12
      },
      {
        "args": [
          7,
          0
        ],
        "expected": 0
      },
      {
        "args": [
          -2,
          4
        ],
        "expected": -8
      }
    ]
  },
  "5669": {
    "functionNames": [
      "steps_by_one_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          2,
          6
        ],
        "expected": 4
      },
      {
        "args": [
          5,
          5
        ],
        "expected": 0
      },
      {
        "args": [
          8,
          3
        ],
        "expected": 0
      }
    ]
  },
  "5670": {
    "functionNames": [
      "sum_first_evens_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          4
        ],
        "expected": 12
      },
      {
        "args": [
          1
        ],
        "expected": 0
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ]
  },
  "5671": {
    "functionNames": [
      "sum_first_odds_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          4
        ],
        "expected": 16
      },
      {
        "args": [
          1
        ],
        "expected": 1
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ]
  },
  "5672": {
    "functionNames": [
      "inclusive_count_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          3,
          6
        ],
        "expected": 4
      },
      {
        "args": [
          5,
          5
        ],
        "expected": 1
      },
      {
        "args": [
          7,
          2
        ],
        "expected": 0
      }
    ]
  },
  "5673": {
    "functionNames": [
      "inclusive_sum_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          2,
          5
        ],
        "expected": 14
      },
      {
        "args": [
          4,
          4
        ],
        "expected": 4
      },
      {
        "args": [
          5,
          2
        ],
        "expected": 0
      }
    ]
  },
  "5674": {
    "functionNames": [
      "values_below_by_step_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          10,
          3
        ],
        "expected": 3
      },
      {
        "args": [
          5,
          5
        ],
        "expected": 0
      },
      {
        "args": [
          9,
          2
        ],
        "expected": 4
      }
    ]
  },
  "5675": {
    "functionNames": [
      "double_repeatedly_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          3,
          2
        ],
        "expected": 12
      },
      {
        "args": [
          5,
          0
        ],
        "expected": 5
      },
      {
        "args": [
          1,
          4
        ],
        "expected": 16
      }
    ]
  },
  "5676": {
    "functionNames": [
      "halve_until_one_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          10
        ],
        "expected": [
          10,
          5,
          2,
          1
        ]
      },
      {
        "args": [
          1
        ],
        "expected": [
          1
        ]
      },
      {
        "args": [
          0
        ],
        "expected": []
      }
    ]
  },
  "5677": {
    "functionNames": [
      "add_until_limit_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          2,
          3,
          10
        ],
        "expected": [
          2,
          5,
          8
        ]
      },
      {
        "args": [
          5,
          2,
          5
        ],
        "expected": [
          5
        ]
      },
      {
        "args": [
          7,
          1,
          3
        ],
        "expected": []
      }
    ]
  },
  "5678": {
    "functionNames": [
      "copy_text_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          "cat"
        ],
        "expected": "cat"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      },
      {
        "args": [
          "A b"
        ],
        "expected": "A b"
      }
    ]
  },
  "5679": {
    "functionNames": [
      "repeat_character_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          "x",
          4
        ],
        "expected": "xxxx"
      },
      {
        "args": [
          "a",
          1
        ],
        "expected": "a"
      },
      {
        "args": [
          "z",
          0
        ],
        "expected": ""
      }
    ]
  },
  "5680": {
    "functionNames": [
      "join_with_dashes_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          "cat"
        ],
        "expected": "c-a-t"
      },
      {
        "args": [
          "A"
        ],
        "expected": "A"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      }
    ]
  },
  "5681": {
    "functionNames": [
      "uppercase_each_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          "Hello"
        ],
        "expected": "HELLO"
      },
      {
        "args": [
          "a1"
        ],
        "expected": "A1"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      }
    ]
  },
  "5682": {
    "functionNames": [
      "lowercase_each_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          "PyTHon"
        ],
        "expected": "python"
      },
      {
        "args": [
          "A1"
        ],
        "expected": "a1"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      }
    ]
  },
  "5683": {
    "functionNames": [
      "space_count_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          "a b c"
        ],
        "expected": 2
      },
      {
        "args": [
          "none"
        ],
        "expected": 0
      },
      {
        "args": [
          "  "
        ],
        "expected": 2
      }
    ]
  },
  "5684": {
    "functionNames": [
      "text_digit_count_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          "a1b23"
        ],
        "expected": 3
      },
      {
        "args": [
          "hello"
        ],
        "expected": 0
      },
      {
        "args": [
          "007"
        ],
        "expected": 3
      }
    ]
  },
  "5685": {
    "functionNames": [
      "text_letter_count_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          "a1 B!"
        ],
        "expected": 2
      },
      {
        "args": [
          "123"
        ],
        "expected": 0
      },
      {
        "args": [
          "Python"
        ],
        "expected": 6
      }
    ]
  },
  "5686": {
    "functionNames": [
      "replace_character_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          "banana",
          "a",
          "o"
        ],
        "expected": "bonono"
      },
      {
        "args": [
          "cat",
          "x",
          "z"
        ],
        "expected": "cat"
      },
      {
        "args": [
          "",
          "a",
          "b"
        ],
        "expected": ""
      }
    ]
  },
  "5687": {
    "functionNames": [
      "first_characters_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          "python",
          3
        ],
        "expected": "pyt"
      },
      {
        "args": [
          "hi",
          5
        ],
        "expected": "hi"
      },
      {
        "args": [
          "abc",
          0
        ],
        "expected": ""
      }
    ]
  },
  "5688": {
    "functionNames": [
      "last_characters_reversed_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          "python",
          3
        ],
        "expected": "noh"
      },
      {
        "args": [
          "hi",
          5
        ],
        "expected": "ih"
      },
      {
        "args": [
          "abc",
          0
        ],
        "expected": ""
      }
    ]
  },
  "5689": {
    "functionNames": [
      "odd_index_characters_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          "abcdef"
        ],
        "expected": "bdf"
      },
      {
        "args": [
          "a"
        ],
        "expected": ""
      },
      {
        "args": [
          "python"
        ],
        "expected": "yhn"
      }
    ]
  },
  "5690": {
    "functionNames": [
      "duplicate_characters_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          "cat"
        ],
        "expected": "ccaatt"
      },
      {
        "args": [
          "A"
        ],
        "expected": "AA"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      }
    ]
  },
  "5691": {
    "functionNames": [
      "text_before_space_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          "hello world"
        ],
        "expected": "hello"
      },
      {
        "args": [
          "python"
        ],
        "expected": "python"
      },
      {
        "args": [
          " starts"
        ],
        "expected": ""
      }
    ]
  },
  "5692": {
    "functionNames": [
      "text_before_marker_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          "abc:def",
          ":"
        ],
        "expected": "abc"
      },
      {
        "args": [
          "hello",
          "x"
        ],
        "expected": "hello"
      },
      {
        "args": [
          "!wow",
          "!"
        ],
        "expected": ""
      }
    ]
  },
  "5693": {
    "functionNames": [
      "copy_list_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3
          ]
        ],
        "expected": [
          1,
          2,
          3
        ]
      },
      {
        "args": [
          [
            "a"
          ]
        ],
        "expected": [
          "a"
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ]
  },
  "5694": {
    "functionNames": [
      "first_items_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            4
          ],
          2
        ],
        "expected": [
          1,
          2
        ]
      },
      {
        "args": [
          [
            "a"
          ],
          3
        ],
        "expected": [
          "a"
        ]
      },
      {
        "args": [
          [
            1,
            2
          ],
          0
        ],
        "expected": []
      }
    ]
  },
  "5695": {
    "functionNames": [
      "last_items_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            4
          ],
          2
        ],
        "expected": [
          3,
          4
        ]
      },
      {
        "args": [
          [
            "a"
          ],
          3
        ],
        "expected": [
          "a"
        ]
      },
      {
        "args": [
          [
            1,
            2
          ],
          0
        ],
        "expected": []
      }
    ]
  },
  "5696": {
    "functionNames": [
      "item_count_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3
          ]
        ],
        "expected": 3
      },
      {
        "args": [
          []
        ],
        "expected": 0
      },
      {
        "args": [
          [
            "a"
          ]
        ],
        "expected": 1
      }
    ]
  },
  "5697": {
    "functionNames": [
      "matching_value_count_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            1,
            1
          ],
          1
        ],
        "expected": 3
      },
      {
        "args": [
          [
            "a",
            "b"
          ],
          "x"
        ],
        "expected": 0
      },
      {
        "args": [
          [],
          0
        ],
        "expected": 0
      }
    ]
  },
  "5698": {
    "functionNames": [
      "negative_to_zero_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            -2,
            3,
            -1
          ]
        ],
        "expected": [
          0,
          3,
          0
        ]
      },
      {
        "args": [
          [
            0,
            4
          ]
        ],
        "expected": [
          0,
          4
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ]
  },
  "5699": {
    "functionNames": [
      "add_one_each_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3
          ]
        ],
        "expected": [
          2,
          3,
          4
        ]
      },
      {
        "args": [
          [
            -1,
            0
          ]
        ],
        "expected": [
          0,
          1
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ]
  },
  "5700": {
    "functionNames": [
      "double_each_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3
          ]
        ],
        "expected": [
          2,
          4,
          6
        ]
      },
      {
        "args": [
          [
            -2,
            0
          ]
        ],
        "expected": [
          -4,
          0
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ]
  },
  "5701": {
    "functionNames": [
      "text_lengths_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "a",
            ""
          ]
        ],
        "expected": [
          3,
          1,
          0
        ]
      },
      {
        "args": [
          [
            "hello"
          ]
        ],
        "expected": [
          5
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ]
  },
  "5702": {
    "functionNames": [
      "nonzero_values_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            0,
            2,
            0,
            -1
          ]
        ],
        "expected": [
          2,
          -1
        ]
      },
      {
        "args": [
          [
            0,
            0
          ]
        ],
        "expected": []
      },
      {
        "args": [
          [
            3
          ]
        ],
        "expected": [
          3
        ]
      }
    ]
  },
  "5703": {
    "functionNames": [
      "append_two_lists_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ],
          [
            3,
            4
          ]
        ],
        "expected": [
          1,
          2,
          3,
          4
        ]
      },
      {
        "args": [
          [],
          [
            "a"
          ]
        ],
        "expected": [
          "a"
        ]
      },
      {
        "args": [
          [
            1
          ],
          []
        ],
        "expected": [
          1
        ]
      }
    ]
  },
  "5704": {
    "functionNames": [
      "index_item_pairs_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "b"
          ]
        ],
        "expected": [
          [
            0,
            "a"
          ],
          [
            1,
            "b"
          ]
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          [
            0,
            5
          ]
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ]
  },
  "5705": {
    "functionNames": [
      "true_value_count_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            true,
            false,
            true
          ]
        ],
        "expected": 2
      },
      {
        "args": [
          [
            1,
            true,
            0
          ]
        ],
        "expected": 1
      },
      {
        "args": [
          []
        ],
        "expected": 0
      }
    ]
  },
  "5706": {
    "functionNames": [
      "last_item_seen_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            4,
            5
          ]
        ],
        "expected": 5
      },
      {
        "args": [
          [
            "a"
          ]
        ],
        "expected": "a"
      },
      {
        "args": [
          []
        ],
        "expected": null
      }
    ]
  },
  "5707": {
    "functionNames": [
      "items_before_value_easy"
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            0,
            3
          ],
          0
        ],
        "expected": [
          1,
          2
        ]
      },
      {
        "args": [
          [
            "a",
            "b"
          ],
          "x"
        ],
        "expected": [
          "a",
          "b"
        ]
      },
      {
        "args": [
          [
            9
          ],
          9
        ],
        "expected": []
      }
    ]
  }
};
