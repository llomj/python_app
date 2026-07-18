import type { AutoGrader } from './graders';

export const CONCEPT_EXPANSION_GRADERS: Record<number, AutoGrader> = {
  "2481": {
    "functionNames": [
      "square_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          4,
          9,
          100
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          16,
          0,
          49,
          144
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          25
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2482": {
    "functionNames": [
      "cube_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          8,
          27,
          1000
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -64,
          0,
          343,
          1728
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          125
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2483": {
    "functionNames": [
      "double_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          2,
          4,
          6,
          20
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -8,
          0,
          14,
          24
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          10
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2484": {
    "functionNames": [
      "triple_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          3,
          6,
          9,
          30
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -12,
          0,
          21,
          36
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          15
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2485": {
    "functionNames": [
      "negate_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          -1,
          -2,
          -3,
          -10
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          4,
          0,
          -7,
          -12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          -5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2486": {
    "functionNames": [
      "absolute_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          2,
          3,
          10
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          4,
          0,
          7,
          12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2487": {
    "functionNames": [
      "increment_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          2,
          3,
          4,
          11
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -3,
          1,
          8,
          13
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          6
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2488": {
    "functionNames": [
      "decrement_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          0,
          1,
          2,
          9
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -5,
          -1,
          6,
          11
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          4
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2489": {
    "functionNames": [
      "half_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          0.5,
          1,
          1.5,
          5
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -2,
          0,
          3.5,
          6
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          2.5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2490": {
    "functionNames": [
      "last_digit_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          2,
          3,
          0
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          6,
          0,
          7,
          2
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2491": {
    "functionNames": [
      "distance_from_ten_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          9,
          8,
          7,
          0
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          14,
          10,
          3,
          2
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2492": {
    "functionNames": [
      "percent_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          100,
          200,
          300,
          1000
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -400,
          0,
          700,
          1200
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          500
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2493": {
    "functionNames": [
      "remainder_three_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          2,
          0,
          1
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          2,
          0,
          1,
          0
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          2
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2494": {
    "functionNames": [
      "weighted_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          4,
          9,
          40
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4,
          0,
          21,
          48
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2495": {
    "functionNames": [
      "offset_index_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          3,
          5,
          13
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4,
          1,
          9,
          15
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2496": {
    "functionNames": [
      "even_filter_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          2,
          10
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4,
          0,
          12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2497": {
    "functionNames": [
      "odd_filter_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          3
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          7
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2498": {
    "functionNames": [
      "positive_filter_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          2,
          3,
          10
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          7,
          12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2499": {
    "functionNames": [
      "negative_filter_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": []
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2500": {
    "functionNames": [
      "nonzero_filter_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          2,
          3,
          10
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4,
          7,
          12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2501": {
    "functionNames": [
      "at_least_five_filter_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          10
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          7,
          12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2502": {
    "functionNames": [
      "below_ten_filter_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
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
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4,
          0,
          7
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2503": {
    "functionNames": [
      "multiple_three_filter_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          3
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          0,
          12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2504": {
    "functionNames": [
      "single_digit_filter_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
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
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          0,
          7
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2505": {
    "functionNames": [
      "outside_unit_filter_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          2,
          3,
          10
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4,
          7,
          12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2506": {
    "functionNames": [
      "even_index_filter_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          3
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4,
          7
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2507": {
    "functionNames": [
      "odd_index_filter_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          2,
          10
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          0,
          12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2508": {
    "functionNames": [
      "greater_index_filter_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          2,
          3,
          10
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          7,
          12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2509": {
    "functionNames": [
      "matching_parity_filter_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": []
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2510": {
    "functionNames": [
      "square_below_fifty_filter_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
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
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4,
          0,
          7
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2511": {
    "functionNames": [
      "uppercase_word_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          "CAT",
          "PYTHON",
          "GO"
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          "A",
          "LEVEL",
          "CODE"
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          "SUN"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2512": {
    "functionNames": [
      "lowercase_word_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          "cat",
          "python",
          "go"
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          "a",
          "level",
          "code"
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          "sun"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2513": {
    "functionNames": [
      "lengths_word_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          3,
          6,
          2
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          1,
          5,
          4
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2514": {
    "functionNames": [
      "first_chars_word_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          "c",
          "P",
          "g"
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          "A",
          "l",
          "C"
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          "s"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2515": {
    "functionNames": [
      "last_chars_word_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          "t",
          "n",
          "o"
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          "A",
          "l",
          "e"
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          "n"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2516": {
    "functionNames": [
      "reverse_words_word_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          "tac",
          "nohtyP",
          "og"
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          "A",
          "level",
          "edoC"
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          "nus"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2517": {
    "functionNames": [
      "wrap_words_word_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          "[cat]",
          "[Python]",
          "[go]"
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          "[A]",
          "[level]",
          "[Code]"
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          "[sun]"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2518": {
    "functionNames": [
      "double_words_word_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          "catcat",
          "PythonPython",
          "gogo"
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          "AA",
          "levellevel",
          "CodeCode"
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          "sunsun"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2519": {
    "functionNames": [
      "initial_pairs_word_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          "ct",
          "Pn",
          "go"
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          "AA",
          "ll",
          "Ce"
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          "sn"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2520": {
    "functionNames": [
      "vowel_counts_word_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          1,
          1,
          1
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          1,
          2,
          2
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "2521": {
    "functionNames": [
      "square_index_dictionary"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": {
          "0": 1,
          "1": 4,
          "2": 9,
          "3": 100
        }
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": {
          "0": 16,
          "1": 0,
          "2": 49,
          "3": 144
        }
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": {
          "0": 25
        }
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "DictComp",
        "minCount": 1
      }
    ]
  },
  "2522": {
    "functionNames": [
      "cube_index_dictionary"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": {
          "0": 1,
          "1": 8,
          "2": 27,
          "3": 1000
        }
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": {
          "0": -64,
          "1": 0,
          "2": 343,
          "3": 1728
        }
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": {
          "0": 125
        }
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "DictComp",
        "minCount": 1
      }
    ]
  },
  "2523": {
    "functionNames": [
      "double_index_dictionary"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": {
          "0": 2,
          "1": 4,
          "2": 6,
          "3": 20
        }
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": {
          "0": -8,
          "1": 0,
          "2": 14,
          "3": 24
        }
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": {
          "0": 10
        }
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "DictComp",
        "minCount": 1
      }
    ]
  },
  "2524": {
    "functionNames": [
      "triple_index_dictionary"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": {
          "0": 3,
          "1": 6,
          "2": 9,
          "3": 30
        }
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": {
          "0": -12,
          "1": 0,
          "2": 21,
          "3": 36
        }
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": {
          "0": 15
        }
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "DictComp",
        "minCount": 1
      }
    ]
  },
  "2525": {
    "functionNames": [
      "negate_index_dictionary"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": {
          "0": -1,
          "1": -2,
          "2": -3,
          "3": -10
        }
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": {
          "0": 4,
          "1": 0,
          "2": -7,
          "3": -12
        }
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": {
          "0": -5
        }
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "DictComp",
        "minCount": 1
      }
    ]
  },
  "2526": {
    "functionNames": [
      "absolute_index_dictionary"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": {
          "0": 1,
          "1": 2,
          "2": 3,
          "3": 10
        }
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": {
          "0": 4,
          "1": 0,
          "2": 7,
          "3": 12
        }
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": {
          "0": 5
        }
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "DictComp",
        "minCount": 1
      }
    ]
  },
  "2527": {
    "functionNames": [
      "increment_index_dictionary"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": {
          "0": 2,
          "1": 3,
          "2": 4,
          "3": 11
        }
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": {
          "0": -3,
          "1": 1,
          "2": 8,
          "3": 13
        }
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": {
          "0": 6
        }
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "DictComp",
        "minCount": 1
      }
    ]
  },
  "2528": {
    "functionNames": [
      "decrement_index_dictionary"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": {
          "0": 0,
          "1": 1,
          "2": 2,
          "3": 9
        }
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": {
          "0": -5,
          "1": -1,
          "2": 6,
          "3": 11
        }
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": {
          "0": 4
        }
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "DictComp",
        "minCount": 1
      }
    ]
  },
  "2529": {
    "functionNames": [
      "half_index_dictionary"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": {
          "0": 0.5,
          "1": 1,
          "2": 1.5,
          "3": 5
        }
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": {
          "0": -2,
          "1": 0,
          "2": 3.5,
          "3": 6
        }
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": {
          "0": 2.5
        }
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "DictComp",
        "minCount": 1
      }
    ]
  },
  "2530": {
    "functionNames": [
      "last_digit_index_dictionary"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": {
          "0": 1,
          "1": 2,
          "2": 3,
          "3": 0
        }
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": {
          "0": 6,
          "1": 0,
          "2": 7,
          "3": 2
        }
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": {
          "0": 5
        }
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "DictComp",
        "minCount": 1
      }
    ]
  },
  "2531": {
    "functionNames": [
      "even_index_dictionary_filter"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": {
          "1": 2,
          "3": 10
        }
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": {
          "0": -4,
          "1": 0,
          "3": 12
        }
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": {}
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "DictComp",
        "minCount": 1
      }
    ]
  },
  "2532": {
    "functionNames": [
      "odd_index_dictionary_filter"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": {
          "0": 1,
          "2": 3
        }
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": {
          "2": 7
        }
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": {
          "0": 5
        }
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "DictComp",
        "minCount": 1
      }
    ]
  },
  "2533": {
    "functionNames": [
      "positive_index_dictionary_filter"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": {
          "0": 1,
          "1": 2,
          "2": 3,
          "3": 10
        }
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": {
          "2": 7,
          "3": 12
        }
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": {
          "0": 5
        }
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "DictComp",
        "minCount": 1
      }
    ]
  },
  "2534": {
    "functionNames": [
      "negative_index_dictionary_filter"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": {}
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": {
          "0": -4
        }
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": {}
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "DictComp",
        "minCount": 1
      }
    ]
  },
  "2535": {
    "functionNames": [
      "nonzero_index_dictionary_filter"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": {
          "0": 1,
          "1": 2,
          "2": 3,
          "3": 10
        }
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": {
          "0": -4,
          "2": 7,
          "3": 12
        }
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": {
          "0": 5
        }
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "DictComp",
        "minCount": 1
      }
    ]
  },
  "2536": {
    "functionNames": [
      "at_least_five_index_dictionary_filter"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": {
          "3": 10
        }
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": {
          "2": 7,
          "3": 12
        }
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": {
          "0": 5
        }
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "DictComp",
        "minCount": 1
      }
    ]
  },
  "2537": {
    "functionNames": [
      "below_ten_index_dictionary_filter"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": {
          "0": 1,
          "1": 2,
          "2": 3
        }
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": {
          "0": -4,
          "1": 0,
          "2": 7
        }
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": {
          "0": 5
        }
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "DictComp",
        "minCount": 1
      }
    ]
  },
  "2538": {
    "functionNames": [
      "multiple_three_index_dictionary_filter"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": {
          "2": 3
        }
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": {
          "1": 0,
          "3": 12
        }
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": {}
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "DictComp",
        "minCount": 1
      }
    ]
  },
  "2539": {
    "functionNames": [
      "single_digit_index_dictionary_filter"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": {
          "0": 1,
          "1": 2,
          "2": 3
        }
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": {
          "1": 0,
          "2": 7
        }
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": {
          "0": 5
        }
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "DictComp",
        "minCount": 1
      }
    ]
  },
  "2540": {
    "functionNames": [
      "outside_unit_index_dictionary_filter"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": {
          "1": 2,
          "2": 3,
          "3": 10
        }
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": {
          "0": -4,
          "2": 7,
          "3": 12
        }
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": {
          "0": 5
        }
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "DictComp",
        "minCount": 1
      }
    ]
  },
  "2541": {
    "functionNames": [
      "square_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          4,
          9,
          100
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          16,
          0,
          49,
          144
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          25
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2542": {
    "functionNames": [
      "cube_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          8,
          27,
          1000
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -64,
          0,
          343,
          1728
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          125
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2543": {
    "functionNames": [
      "double_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          2,
          4,
          6,
          20
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -8,
          0,
          14,
          24
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          10
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2544": {
    "functionNames": [
      "triple_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          3,
          6,
          9,
          30
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -12,
          0,
          21,
          36
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          15
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2545": {
    "functionNames": [
      "negate_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          -1,
          -2,
          -3,
          -10
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          4,
          0,
          -7,
          -12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          -5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2546": {
    "functionNames": [
      "absolute_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          2,
          3,
          10
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          4,
          0,
          7,
          12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2547": {
    "functionNames": [
      "increment_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          2,
          3,
          4,
          11
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -3,
          1,
          8,
          13
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          6
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2548": {
    "functionNames": [
      "decrement_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          0,
          1,
          2,
          9
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -5,
          -1,
          6,
          11
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          4
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2549": {
    "functionNames": [
      "half_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          0.5,
          1,
          1.5,
          5
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -2,
          0,
          3.5,
          6
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          2.5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2550": {
    "functionNames": [
      "last_digit_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          2,
          3,
          0
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          6,
          0,
          7,
          2
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2551": {
    "functionNames": [
      "distance_from_ten_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          9,
          8,
          7,
          0
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          14,
          10,
          3,
          2
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2552": {
    "functionNames": [
      "percent_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          100,
          200,
          300,
          1000
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -400,
          0,
          700,
          1200
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          500
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2553": {
    "functionNames": [
      "remainder_three_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          2,
          0,
          1
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          2,
          0,
          1,
          0
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          2
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2554": {
    "functionNames": [
      "weighted_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          4,
          9,
          40
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4,
          0,
          21,
          48
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2555": {
    "functionNames": [
      "offset_index_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          3,
          5,
          13
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4,
          1,
          9,
          15
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2556": {
    "functionNames": [
      "even_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          2,
          10
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4,
          0,
          12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2557": {
    "functionNames": [
      "odd_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          3
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          7
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2558": {
    "functionNames": [
      "positive_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          2,
          3,
          10
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          7,
          12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2559": {
    "functionNames": [
      "negative_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": []
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2560": {
    "functionNames": [
      "nonzero_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          2,
          3,
          10
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4,
          7,
          12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2561": {
    "functionNames": [
      "at_least_five_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          10
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          7,
          12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2562": {
    "functionNames": [
      "below_ten_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
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
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4,
          0,
          7
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2563": {
    "functionNames": [
      "multiple_three_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          3
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          0,
          12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2564": {
    "functionNames": [
      "single_digit_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
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
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          0,
          7
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2565": {
    "functionNames": [
      "outside_unit_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          2,
          3,
          10
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4,
          7,
          12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2566": {
    "functionNames": [
      "even_index_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          3
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4,
          7
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2567": {
    "functionNames": [
      "odd_index_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          2,
          10
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          0,
          12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2568": {
    "functionNames": [
      "greater_index_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          2,
          3,
          10
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          7,
          12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2569": {
    "functionNames": [
      "matching_parity_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": []
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2570": {
    "functionNames": [
      "square_below_fifty_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
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
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4,
          0,
          7
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2571": {
    "functionNames": [
      "uppercase_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          "CAT",
          "PYTHON",
          "GO"
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          "A",
          "LEVEL",
          "CODE"
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          "SUN"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2572": {
    "functionNames": [
      "lowercase_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          "cat",
          "python",
          "go"
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          "a",
          "level",
          "code"
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          "sun"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2573": {
    "functionNames": [
      "lengths_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          3,
          6,
          2
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          1,
          5,
          4
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2574": {
    "functionNames": [
      "first_chars_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          "c",
          "P",
          "g"
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          "A",
          "l",
          "C"
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          "s"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2575": {
    "functionNames": [
      "last_chars_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          "t",
          "n",
          "o"
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          "A",
          "l",
          "e"
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          "n"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2576": {
    "functionNames": [
      "reverse_words_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          "tac",
          "nohtyP",
          "og"
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          "A",
          "level",
          "edoC"
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          "nus"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2577": {
    "functionNames": [
      "wrap_words_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          "[cat]",
          "[Python]",
          "[go]"
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          "[A]",
          "[level]",
          "[Code]"
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          "[sun]"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2578": {
    "functionNames": [
      "double_words_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          "catcat",
          "PythonPython",
          "gogo"
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          "AA",
          "levellevel",
          "CodeCode"
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          "sunsun"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2579": {
    "functionNames": [
      "initial_pairs_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          "ct",
          "Pn",
          "go"
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          "AA",
          "ll",
          "Ce"
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          "sn"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2580": {
    "functionNames": [
      "vowel_counts_explicit_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          1,
          1,
          1
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          1,
          2,
          2
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2581": {
    "functionNames": [
      "square_running_total_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          5,
          14,
          114
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          16,
          16,
          65,
          209
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          25
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2582": {
    "functionNames": [
      "cube_running_total_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          9,
          36,
          1036
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -64,
          -64,
          279,
          2007
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          125
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2583": {
    "functionNames": [
      "double_running_total_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          2,
          6,
          12,
          32
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -8,
          -8,
          6,
          30
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          10
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2584": {
    "functionNames": [
      "triple_running_total_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          3,
          9,
          18,
          48
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -12,
          -12,
          9,
          45
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          15
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2585": {
    "functionNames": [
      "negate_running_total_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          -1,
          -3,
          -6,
          -16
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          4,
          4,
          -3,
          -15
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          -5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2586": {
    "functionNames": [
      "absolute_running_total_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          3,
          6,
          16
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          4,
          4,
          11,
          23
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2587": {
    "functionNames": [
      "increment_running_total_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          2,
          5,
          9,
          20
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -3,
          -2,
          6,
          19
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          6
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2588": {
    "functionNames": [
      "decrement_running_total_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          0,
          1,
          3,
          12
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -5,
          -6,
          0,
          11
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          4
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2589": {
    "functionNames": [
      "half_running_total_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          0.5,
          1.5,
          3,
          8
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -2,
          -2,
          1.5,
          7.5
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          2.5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2590": {
    "functionNames": [
      "last_digit_running_total_for_loop"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          3,
          6,
          6
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          6,
          6,
          13,
          15
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "2591": {
    "functionNames": [
      "square_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          4,
          9,
          100
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          16,
          0,
          49,
          144
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          25
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2592": {
    "functionNames": [
      "cube_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          8,
          27,
          1000
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -64,
          0,
          343,
          1728
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          125
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2593": {
    "functionNames": [
      "double_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          2,
          4,
          6,
          20
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -8,
          0,
          14,
          24
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          10
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2594": {
    "functionNames": [
      "triple_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          3,
          6,
          9,
          30
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -12,
          0,
          21,
          36
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          15
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2595": {
    "functionNames": [
      "negate_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          -1,
          -2,
          -3,
          -10
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          4,
          0,
          -7,
          -12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          -5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2596": {
    "functionNames": [
      "absolute_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          2,
          3,
          10
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          4,
          0,
          7,
          12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2597": {
    "functionNames": [
      "increment_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          2,
          3,
          4,
          11
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -3,
          1,
          8,
          13
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          6
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2598": {
    "functionNames": [
      "decrement_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          0,
          1,
          2,
          9
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -5,
          -1,
          6,
          11
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          4
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2599": {
    "functionNames": [
      "half_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          0.5,
          1,
          1.5,
          5
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -2,
          0,
          3.5,
          6
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          2.5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2600": {
    "functionNames": [
      "last_digit_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          2,
          3,
          0
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          6,
          0,
          7,
          2
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2601": {
    "functionNames": [
      "distance_from_ten_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          9,
          8,
          7,
          0
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          14,
          10,
          3,
          2
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2602": {
    "functionNames": [
      "percent_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          100,
          200,
          300,
          1000
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -400,
          0,
          700,
          1200
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          500
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2603": {
    "functionNames": [
      "remainder_three_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          2,
          0,
          1
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          2,
          0,
          1,
          0
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          2
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2604": {
    "functionNames": [
      "weighted_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          4,
          9,
          40
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4,
          0,
          21,
          48
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2605": {
    "functionNames": [
      "offset_index_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          3,
          5,
          13
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4,
          1,
          9,
          15
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2606": {
    "functionNames": [
      "even_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          2,
          10
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4,
          0,
          12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2607": {
    "functionNames": [
      "odd_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          3
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          7
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2608": {
    "functionNames": [
      "positive_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          2,
          3,
          10
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          7,
          12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2609": {
    "functionNames": [
      "negative_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": []
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2610": {
    "functionNames": [
      "nonzero_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          2,
          3,
          10
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4,
          7,
          12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2611": {
    "functionNames": [
      "at_least_five_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          10
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          7,
          12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2612": {
    "functionNames": [
      "below_ten_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
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
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4,
          0,
          7
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2613": {
    "functionNames": [
      "multiple_three_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          3
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          0,
          12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2614": {
    "functionNames": [
      "single_digit_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
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
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          0,
          7
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2615": {
    "functionNames": [
      "outside_unit_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          2,
          3,
          10
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4,
          7,
          12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2616": {
    "functionNames": [
      "even_index_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          3
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4,
          7
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2617": {
    "functionNames": [
      "odd_index_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          2,
          10
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          0,
          12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2618": {
    "functionNames": [
      "greater_index_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          2,
          3,
          10
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          7,
          12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2619": {
    "functionNames": [
      "matching_parity_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": []
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2620": {
    "functionNames": [
      "square_below_fifty_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
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
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4,
          0,
          7
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2621": {
    "functionNames": [
      "uppercase_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          "CAT",
          "PYTHON",
          "GO"
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          "A",
          "LEVEL",
          "CODE"
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          "SUN"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2622": {
    "functionNames": [
      "lowercase_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          "cat",
          "python",
          "go"
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          "a",
          "level",
          "code"
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          "sun"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2623": {
    "functionNames": [
      "lengths_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          3,
          6,
          2
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          1,
          5,
          4
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2624": {
    "functionNames": [
      "first_chars_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          "c",
          "P",
          "g"
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          "A",
          "l",
          "C"
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          "s"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2625": {
    "functionNames": [
      "last_chars_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          "t",
          "n",
          "o"
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          "A",
          "l",
          "e"
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          "n"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2626": {
    "functionNames": [
      "reverse_words_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          "tac",
          "nohtyP",
          "og"
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          "A",
          "level",
          "edoC"
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          "nus"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2627": {
    "functionNames": [
      "wrap_words_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          "[cat]",
          "[Python]",
          "[go]"
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          "[A]",
          "[level]",
          "[Code]"
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          "[sun]"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2628": {
    "functionNames": [
      "double_words_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          "catcat",
          "PythonPython",
          "gogo"
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          "AA",
          "levellevel",
          "CodeCode"
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          "sunsun"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2629": {
    "functionNames": [
      "initial_pairs_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          "ct",
          "Pn",
          "go"
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          "AA",
          "ll",
          "Ce"
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          "sn"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2630": {
    "functionNames": [
      "vowel_counts_yield_generator"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          1,
          1,
          1
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          1,
          2,
          2
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2631": {
    "functionNames": [
      "square_enumerated_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          [
            0,
            1
          ],
          [
            1,
            4
          ],
          [
            2,
            9
          ],
          [
            3,
            100
          ]
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          [
            0,
            16
          ],
          [
            1,
            0
          ],
          [
            2,
            49
          ],
          [
            3,
            144
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
            25
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2632": {
    "functionNames": [
      "cube_enumerated_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          [
            0,
            1
          ],
          [
            1,
            8
          ],
          [
            2,
            27
          ],
          [
            3,
            1000
          ]
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          [
            0,
            -64
          ],
          [
            1,
            0
          ],
          [
            2,
            343
          ],
          [
            3,
            1728
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
            125
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2633": {
    "functionNames": [
      "double_enumerated_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          [
            0,
            2
          ],
          [
            1,
            4
          ],
          [
            2,
            6
          ],
          [
            3,
            20
          ]
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          [
            0,
            -8
          ],
          [
            1,
            0
          ],
          [
            2,
            14
          ],
          [
            3,
            24
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
            10
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2634": {
    "functionNames": [
      "triple_enumerated_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          [
            0,
            3
          ],
          [
            1,
            6
          ],
          [
            2,
            9
          ],
          [
            3,
            30
          ]
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          [
            0,
            -12
          ],
          [
            1,
            0
          ],
          [
            2,
            21
          ],
          [
            3,
            36
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
            15
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2635": {
    "functionNames": [
      "negate_enumerated_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          [
            0,
            -1
          ],
          [
            1,
            -2
          ],
          [
            2,
            -3
          ],
          [
            3,
            -10
          ]
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          [
            0,
            4
          ],
          [
            1,
            0
          ],
          [
            2,
            -7
          ],
          [
            3,
            -12
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
            -5
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2636": {
    "functionNames": [
      "absolute_enumerated_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          [
            0,
            1
          ],
          [
            1,
            2
          ],
          [
            2,
            3
          ],
          [
            3,
            10
          ]
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          [
            0,
            4
          ],
          [
            1,
            0
          ],
          [
            2,
            7
          ],
          [
            3,
            12
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
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2637": {
    "functionNames": [
      "increment_enumerated_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          [
            0,
            2
          ],
          [
            1,
            3
          ],
          [
            2,
            4
          ],
          [
            3,
            11
          ]
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          [
            0,
            -3
          ],
          [
            1,
            1
          ],
          [
            2,
            8
          ],
          [
            3,
            13
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
            6
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2638": {
    "functionNames": [
      "decrement_enumerated_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          [
            0,
            0
          ],
          [
            1,
            1
          ],
          [
            2,
            2
          ],
          [
            3,
            9
          ]
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          [
            0,
            -5
          ],
          [
            1,
            -1
          ],
          [
            2,
            6
          ],
          [
            3,
            11
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
            4
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2639": {
    "functionNames": [
      "half_enumerated_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          [
            0,
            0.5
          ],
          [
            1,
            1
          ],
          [
            2,
            1.5
          ],
          [
            3,
            5
          ]
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          [
            0,
            -2
          ],
          [
            1,
            0
          ],
          [
            2,
            3.5
          ],
          [
            3,
            6
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
            2.5
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2640": {
    "functionNames": [
      "last_digit_enumerated_generator"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          [
            0,
            1
          ],
          [
            1,
            2
          ],
          [
            2,
            3
          ],
          [
            3,
            0
          ]
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          [
            0,
            6
          ],
          [
            1,
            0
          ],
          [
            2,
            7
          ],
          [
            3,
            2
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
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Yield",
        "minCount": 1
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 1
      }
    ]
  },
  "2641": {
    "functionNames": [
      "recursive_square_values"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          4,
          9,
          100
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          16,
          0,
          49,
          144
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          25
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_square_values",
        "minArgs": 1
      }
    ]
  },
  "2642": {
    "functionNames": [
      "recursive_cube_values"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          8,
          27,
          1000
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -64,
          0,
          343,
          1728
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          125
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_cube_values",
        "minArgs": 1
      }
    ]
  },
  "2643": {
    "functionNames": [
      "recursive_double_values"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          2,
          4,
          6,
          20
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -8,
          0,
          14,
          24
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          10
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_double_values",
        "minArgs": 1
      }
    ]
  },
  "2644": {
    "functionNames": [
      "recursive_triple_values"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          3,
          6,
          9,
          30
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -12,
          0,
          21,
          36
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          15
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_triple_values",
        "minArgs": 1
      }
    ]
  },
  "2645": {
    "functionNames": [
      "recursive_negate_values"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          -1,
          -2,
          -3,
          -10
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          4,
          0,
          -7,
          -12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          -5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_negate_values",
        "minArgs": 1
      }
    ]
  },
  "2646": {
    "functionNames": [
      "recursive_absolute_values"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          2,
          3,
          10
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          4,
          0,
          7,
          12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_absolute_values",
        "minArgs": 1
      }
    ]
  },
  "2647": {
    "functionNames": [
      "recursive_increment_values"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          2,
          3,
          4,
          11
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -3,
          1,
          8,
          13
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          6
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_increment_values",
        "minArgs": 1
      }
    ]
  },
  "2648": {
    "functionNames": [
      "recursive_decrement_values"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          0,
          1,
          2,
          9
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -5,
          -1,
          6,
          11
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          4
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_decrement_values",
        "minArgs": 1
      }
    ]
  },
  "2649": {
    "functionNames": [
      "recursive_half_values"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          0.5,
          1,
          1.5,
          5
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -2,
          0,
          3.5,
          6
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          2.5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_half_values",
        "minArgs": 1
      }
    ]
  },
  "2650": {
    "functionNames": [
      "recursive_last_digit_values"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          2,
          3,
          0
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          6,
          0,
          7,
          2
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_last_digit_values",
        "minArgs": 1
      }
    ]
  },
  "2651": {
    "functionNames": [
      "recursive_distance_from_ten_values"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          9,
          8,
          7,
          0
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          14,
          10,
          3,
          2
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_distance_from_ten_values",
        "minArgs": 1
      }
    ]
  },
  "2652": {
    "functionNames": [
      "recursive_percent_values"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          100,
          200,
          300,
          1000
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -400,
          0,
          700,
          1200
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          500
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_percent_values",
        "minArgs": 1
      }
    ]
  },
  "2653": {
    "functionNames": [
      "recursive_remainder_three_values"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          2,
          0,
          1
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          2,
          0,
          1,
          0
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          2
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_remainder_three_values",
        "minArgs": 1
      }
    ]
  },
  "2654": {
    "functionNames": [
      "recursive_weighted_values"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          4,
          9,
          40
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4,
          0,
          21,
          48
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_weighted_values",
        "minArgs": 1
      }
    ]
  },
  "2655": {
    "functionNames": [
      "recursive_offset_index_values"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          3,
          5,
          13
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4,
          1,
          9,
          15
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_offset_index_values",
        "minArgs": 1
      }
    ]
  },
  "2656": {
    "functionNames": [
      "recursive_keep_even"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          2,
          10
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4,
          0,
          12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_keep_even",
        "minArgs": 1
      }
    ]
  },
  "2657": {
    "functionNames": [
      "recursive_keep_odd"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          3
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          7
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_keep_odd",
        "minArgs": 1
      }
    ]
  },
  "2658": {
    "functionNames": [
      "recursive_keep_positive"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          2,
          3,
          10
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          7,
          12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_keep_positive",
        "minArgs": 1
      }
    ]
  },
  "2659": {
    "functionNames": [
      "recursive_keep_negative"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": []
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_keep_negative",
        "minArgs": 1
      }
    ]
  },
  "2660": {
    "functionNames": [
      "recursive_keep_nonzero"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          2,
          3,
          10
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4,
          7,
          12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_keep_nonzero",
        "minArgs": 1
      }
    ]
  },
  "2661": {
    "functionNames": [
      "recursive_keep_at_least_five"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          10
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          7,
          12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_keep_at_least_five",
        "minArgs": 1
      }
    ]
  },
  "2662": {
    "functionNames": [
      "recursive_keep_below_ten"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
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
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4,
          0,
          7
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_keep_below_ten",
        "minArgs": 1
      }
    ]
  },
  "2663": {
    "functionNames": [
      "recursive_keep_multiple_three"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          3
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          0,
          12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_keep_multiple_three",
        "minArgs": 1
      }
    ]
  },
  "2664": {
    "functionNames": [
      "recursive_keep_single_digit"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
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
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          0,
          7
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_keep_single_digit",
        "minArgs": 1
      }
    ]
  },
  "2665": {
    "functionNames": [
      "recursive_keep_outside_unit"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          2,
          3,
          10
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4,
          7,
          12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_keep_outside_unit",
        "minArgs": 1
      }
    ]
  },
  "2666": {
    "functionNames": [
      "recursive_keep_even_index"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          3
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4,
          7
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_keep_even_index",
        "minArgs": 1
      }
    ]
  },
  "2667": {
    "functionNames": [
      "recursive_keep_odd_index"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          2,
          10
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          0,
          12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_keep_odd_index",
        "minArgs": 1
      }
    ]
  },
  "2668": {
    "functionNames": [
      "recursive_keep_greater_index"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": [
          1,
          2,
          3,
          10
        ]
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          7,
          12
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_keep_greater_index",
        "minArgs": 1
      }
    ]
  },
  "2669": {
    "functionNames": [
      "recursive_keep_matching_parity"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": []
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_keep_matching_parity",
        "minArgs": 1
      }
    ]
  },
  "2670": {
    "functionNames": [
      "recursive_keep_square_below_fifty"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
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
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": [
          -4,
          0,
          7
        ]
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_keep_square_below_fifty",
        "minArgs": 1
      }
    ]
  },
  "2671": {
    "functionNames": [
      "recursive_total_square"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": 114
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": 209
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": 25
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_total_square",
        "minArgs": 1
      }
    ]
  },
  "2672": {
    "functionNames": [
      "recursive_total_cube"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": 1036
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": 2007
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": 125
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_total_cube",
        "minArgs": 1
      }
    ]
  },
  "2673": {
    "functionNames": [
      "recursive_total_double"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": 32
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": 30
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": 10
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_total_double",
        "minArgs": 1
      }
    ]
  },
  "2674": {
    "functionNames": [
      "recursive_total_triple"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": 48
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": 45
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": 15
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_total_triple",
        "minArgs": 1
      }
    ]
  },
  "2675": {
    "functionNames": [
      "recursive_total_negate"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": -16
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": -15
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": -5
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_total_negate",
        "minArgs": 1
      }
    ]
  },
  "2676": {
    "functionNames": [
      "recursive_total_absolute"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": 16
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": 23
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": 5
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_total_absolute",
        "minArgs": 1
      }
    ]
  },
  "2677": {
    "functionNames": [
      "recursive_total_increment"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": 20
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": 19
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": 6
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_total_increment",
        "minArgs": 1
      }
    ]
  },
  "2678": {
    "functionNames": [
      "recursive_total_decrement"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": 12
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": 11
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": 4
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_total_decrement",
        "minArgs": 1
      }
    ]
  },
  "2679": {
    "functionNames": [
      "recursive_total_half"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": 8
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": 7.5
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": 2.5
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_total_half",
        "minArgs": 1
      }
    ]
  },
  "2680": {
    "functionNames": [
      "recursive_total_last_digit"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": 6
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": 15
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": 5
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_total_last_digit",
        "minArgs": 1
      }
    ]
  },
  "2681": {
    "functionNames": [
      "recursive_total_distance_from_ten"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": 24
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": 29
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": 5
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_total_distance_from_ten",
        "minArgs": 1
      }
    ]
  },
  "2682": {
    "functionNames": [
      "recursive_total_percent"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": 1600
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": 1500
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": 500
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_total_percent",
        "minArgs": 1
      }
    ]
  },
  "2683": {
    "functionNames": [
      "recursive_total_remainder_three"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": 4
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": 3
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": 2
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_total_remainder_three",
        "minArgs": 1
      }
    ]
  },
  "2684": {
    "functionNames": [
      "recursive_total_weighted"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": 54
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": 65
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": 5
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_total_weighted",
        "minArgs": 1
      }
    ]
  },
  "2685": {
    "functionNames": [
      "recursive_total_offset_index"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": 22
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": 21
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": 5
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_total_offset_index",
        "minArgs": 1
      }
    ]
  },
  "2686": {
    "functionNames": [
      "recursive_uppercase_words"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          "CAT",
          "PYTHON",
          "GO"
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          "A",
          "LEVEL",
          "CODE"
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          "SUN"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_uppercase_words",
        "minArgs": 1
      }
    ]
  },
  "2687": {
    "functionNames": [
      "recursive_lowercase_words"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          "cat",
          "python",
          "go"
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          "a",
          "level",
          "code"
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          "sun"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_lowercase_words",
        "minArgs": 1
      }
    ]
  },
  "2688": {
    "functionNames": [
      "recursive_lengths_words"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          3,
          6,
          2
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          1,
          5,
          4
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_lengths_words",
        "minArgs": 1
      }
    ]
  },
  "2689": {
    "functionNames": [
      "recursive_first_chars_words"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          "c",
          "P",
          "g"
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          "A",
          "l",
          "C"
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          "s"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_first_chars_words",
        "minArgs": 1
      }
    ]
  },
  "2690": {
    "functionNames": [
      "recursive_last_chars_words"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          "t",
          "n",
          "o"
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          "A",
          "l",
          "e"
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          "n"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_last_chars_words",
        "minArgs": 1
      }
    ]
  },
  "2691": {
    "functionNames": [
      "recursive_reverse_words_words"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          "tac",
          "nohtyP",
          "og"
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          "A",
          "level",
          "edoC"
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          "nus"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_reverse_words_words",
        "minArgs": 1
      }
    ]
  },
  "2692": {
    "functionNames": [
      "recursive_wrap_words_words"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          "[cat]",
          "[Python]",
          "[go]"
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          "[A]",
          "[level]",
          "[Code]"
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          "[sun]"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_wrap_words_words",
        "minArgs": 1
      }
    ]
  },
  "2693": {
    "functionNames": [
      "recursive_double_words_words"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          "catcat",
          "PythonPython",
          "gogo"
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          "AA",
          "levellevel",
          "CodeCode"
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          "sunsun"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_double_words_words",
        "minArgs": 1
      }
    ]
  },
  "2694": {
    "functionNames": [
      "recursive_initial_pairs_words"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          "ct",
          "Pn",
          "go"
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          "AA",
          "ll",
          "Ce"
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          "sn"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_initial_pairs_words",
        "minArgs": 1
      }
    ]
  },
  "2695": {
    "functionNames": [
      "recursive_vowel_counts_words"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "Python",
            "go"
          ]
        ],
        "expected": [
          1,
          1,
          1
        ]
      },
      {
        "args": [
          [
            "A",
            "level",
            "Code"
          ]
        ],
        "expected": [
          1,
          2,
          2
        ]
      },
      {
        "args": [
          [
            "sun"
          ]
        ],
        "expected": [
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_vowel_counts_words",
        "minArgs": 1
      }
    ]
  },
  "2696": {
    "functionNames": [
      "recursive_count_even"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": 2
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": 3
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_count_even",
        "minArgs": 1
      }
    ]
  },
  "2697": {
    "functionNames": [
      "recursive_count_odd"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": 2
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": 1
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_count_odd",
        "minArgs": 1
      }
    ]
  },
  "2698": {
    "functionNames": [
      "recursive_count_positive"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": 4
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": 2
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_count_positive",
        "minArgs": 1
      }
    ]
  },
  "2699": {
    "functionNames": [
      "recursive_count_negative"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": 0
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": 1
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_count_negative",
        "minArgs": 1
      }
    ]
  },
  "2700": {
    "functionNames": [
      "recursive_count_nonzero"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            10
          ]
        ],
        "expected": 4
      },
      {
        "args": [
          [
            -4,
            0,
            7,
            12
          ]
        ],
        "expected": 3
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "If",
        "minCount": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "recursive_count_nonzero",
        "minArgs": 1
      }
    ]
  },
  "2701": {
    "functionNames": [
      "make_adder_closure"
    ],
    "tests": [
      {
        "args": [
          2
        ],
        "callReturnedWith": [
          5
        ],
        "expected": 7
      },
      {
        "args": [
          3
        ],
        "callReturnedWith": [
          -2
        ],
        "expected": 1
      },
      {
        "args": [
          10
        ],
        "callReturnedWith": [
          4
        ],
        "expected": 14
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2702": {
    "functionNames": [
      "make_multiplier_closure"
    ],
    "tests": [
      {
        "args": [
          2
        ],
        "callReturnedWith": [
          5
        ],
        "expected": 10
      },
      {
        "args": [
          3
        ],
        "callReturnedWith": [
          -2
        ],
        "expected": -6
      },
      {
        "args": [
          10
        ],
        "callReturnedWith": [
          4
        ],
        "expected": 40
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2703": {
    "functionNames": [
      "make_power_closure"
    ],
    "tests": [
      {
        "args": [
          2
        ],
        "callReturnedWith": [
          5
        ],
        "expected": 25
      },
      {
        "args": [
          3
        ],
        "callReturnedWith": [
          -2
        ],
        "expected": -8
      },
      {
        "args": [
          10
        ],
        "callReturnedWith": [
          4
        ],
        "expected": 1048576
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2704": {
    "functionNames": [
      "make_minimum_closure"
    ],
    "tests": [
      {
        "args": [
          2
        ],
        "callReturnedWith": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          3
        ],
        "callReturnedWith": [
          -2
        ],
        "expected": 3
      },
      {
        "args": [
          10
        ],
        "callReturnedWith": [
          4
        ],
        "expected": 10
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2705": {
    "functionNames": [
      "make_maximum_closure"
    ],
    "tests": [
      {
        "args": [
          2
        ],
        "callReturnedWith": [
          5
        ],
        "expected": 2
      },
      {
        "args": [
          3
        ],
        "callReturnedWith": [
          -2
        ],
        "expected": -2
      },
      {
        "args": [
          10
        ],
        "callReturnedWith": [
          4
        ],
        "expected": 4
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2706": {
    "functionNames": [
      "make_remainder_closure"
    ],
    "tests": [
      {
        "args": [
          2
        ],
        "callReturnedWith": [
          5
        ],
        "expected": 1
      },
      {
        "args": [
          3
        ],
        "callReturnedWith": [
          -2
        ],
        "expected": 1
      },
      {
        "args": [
          10
        ],
        "callReturnedWith": [
          4
        ],
        "expected": 4
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2707": {
    "functionNames": [
      "make_distance_closure"
    ],
    "tests": [
      {
        "args": [
          2
        ],
        "callReturnedWith": [
          5
        ],
        "expected": 3
      },
      {
        "args": [
          3
        ],
        "callReturnedWith": [
          -2
        ],
        "expected": 5
      },
      {
        "args": [
          10
        ],
        "callReturnedWith": [
          4
        ],
        "expected": 6
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2708": {
    "functionNames": [
      "make_percentage_closure"
    ],
    "tests": [
      {
        "args": [
          2
        ],
        "callReturnedWith": [
          5
        ],
        "expected": 0.1
      },
      {
        "args": [
          3
        ],
        "callReturnedWith": [
          -2
        ],
        "expected": -0.06
      },
      {
        "args": [
          10
        ],
        "callReturnedWith": [
          4
        ],
        "expected": 0.4
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2709": {
    "functionNames": [
      "make_offset_square_closure"
    ],
    "tests": [
      {
        "args": [
          2
        ],
        "callReturnedWith": [
          5
        ],
        "expected": 49
      },
      {
        "args": [
          3
        ],
        "callReturnedWith": [
          -2
        ],
        "expected": 1
      },
      {
        "args": [
          10
        ],
        "callReturnedWith": [
          4
        ],
        "expected": 196
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2710": {
    "functionNames": [
      "make_scale_then_add_closure"
    ],
    "tests": [
      {
        "args": [
          2
        ],
        "callReturnedWith": [
          5
        ],
        "expected": 11
      },
      {
        "args": [
          3
        ],
        "callReturnedWith": [
          -2
        ],
        "expected": -5
      },
      {
        "args": [
          10
        ],
        "callReturnedWith": [
          4
        ],
        "expected": 41
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2711": {
    "functionNames": [
      "make_subtract_from_closure"
    ],
    "tests": [
      {
        "args": [
          2
        ],
        "callReturnedWith": [
          5
        ],
        "expected": -3
      },
      {
        "args": [
          3
        ],
        "callReturnedWith": [
          -2
        ],
        "expected": 5
      },
      {
        "args": [
          10
        ],
        "callReturnedWith": [
          4
        ],
        "expected": 6
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2712": {
    "functionNames": [
      "make_multiple_check_closure"
    ],
    "tests": [
      {
        "args": [
          2
        ],
        "callReturnedWith": [
          5
        ],
        "expected": false
      },
      {
        "args": [
          3
        ],
        "callReturnedWith": [
          -2
        ],
        "expected": false
      },
      {
        "args": [
          10
        ],
        "callReturnedWith": [
          4
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2713": {
    "functionNames": [
      "make_greater_check_closure"
    ],
    "tests": [
      {
        "args": [
          2
        ],
        "callReturnedWith": [
          5
        ],
        "expected": true
      },
      {
        "args": [
          3
        ],
        "callReturnedWith": [
          -2
        ],
        "expected": false
      },
      {
        "args": [
          10
        ],
        "callReturnedWith": [
          4
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2714": {
    "functionNames": [
      "make_range_check_closure"
    ],
    "tests": [
      {
        "args": [
          2
        ],
        "callReturnedWith": [
          5
        ],
        "expected": false
      },
      {
        "args": [
          3
        ],
        "callReturnedWith": [
          -2
        ],
        "expected": false
      },
      {
        "args": [
          10
        ],
        "callReturnedWith": [
          4
        ],
        "expected": true
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2715": {
    "functionNames": [
      "make_prefix_text_closure"
    ],
    "tests": [
      {
        "args": [
          "-"
        ],
        "callReturnedWith": [
          "code"
        ],
        "expected": "-code"
      },
      {
        "args": [
          "x"
        ],
        "callReturnedWith": [
          "example"
        ],
        "expected": "xexample"
      },
      {
        "args": [
          "go"
        ],
        "callReturnedWith": [
          "gopher"
        ],
        "expected": "gogopher"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2716": {
    "functionNames": [
      "make_suffix_text_closure"
    ],
    "tests": [
      {
        "args": [
          "-"
        ],
        "callReturnedWith": [
          "code"
        ],
        "expected": "code-"
      },
      {
        "args": [
          "x"
        ],
        "callReturnedWith": [
          "example"
        ],
        "expected": "examplex"
      },
      {
        "args": [
          "go"
        ],
        "callReturnedWith": [
          "gopher"
        ],
        "expected": "gophergo"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2717": {
    "functionNames": [
      "make_wrapper_text_closure"
    ],
    "tests": [
      {
        "args": [
          "-"
        ],
        "callReturnedWith": [
          "code"
        ],
        "expected": "-code-"
      },
      {
        "args": [
          "x"
        ],
        "callReturnedWith": [
          "example"
        ],
        "expected": "xexamplex"
      },
      {
        "args": [
          "go"
        ],
        "callReturnedWith": [
          "gopher"
        ],
        "expected": "gogophergo"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2718": {
    "functionNames": [
      "make_separator_text_closure"
    ],
    "tests": [
      {
        "args": [
          "-"
        ],
        "callReturnedWith": [
          "code"
        ],
        "expected": "c-o-d-e"
      },
      {
        "args": [
          "x"
        ],
        "callReturnedWith": [
          "example"
        ],
        "expected": "exxxaxmxpxlxe"
      },
      {
        "args": [
          "go"
        ],
        "callReturnedWith": [
          "gopher"
        ],
        "expected": "ggoogopgohgoegor"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2719": {
    "functionNames": [
      "make_repeater_text_closure"
    ],
    "tests": [
      {
        "args": [
          3
        ],
        "callReturnedWith": [
          "go"
        ],
        "expected": "gogogo"
      },
      {
        "args": [
          2
        ],
        "callReturnedWith": [
          "example"
        ],
        "expected": "exampleexample"
      },
      {
        "args": [
          5
        ],
        "callReturnedWith": [
          "python"
        ],
        "expected": "pythonpythonpythonpythonpython"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2720": {
    "functionNames": [
      "make_truncator_text_closure"
    ],
    "tests": [
      {
        "args": [
          3
        ],
        "callReturnedWith": [
          "go"
        ],
        "expected": "go"
      },
      {
        "args": [
          2
        ],
        "callReturnedWith": [
          "example"
        ],
        "expected": "ex"
      },
      {
        "args": [
          5
        ],
        "callReturnedWith": [
          "python"
        ],
        "expected": "pytho"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2721": {
    "functionNames": [
      "make_contains_text_closure"
    ],
    "tests": [
      {
        "args": [
          "-"
        ],
        "callReturnedWith": [
          "code"
        ],
        "expected": false
      },
      {
        "args": [
          "x"
        ],
        "callReturnedWith": [
          "example"
        ],
        "expected": true
      },
      {
        "args": [
          "go"
        ],
        "callReturnedWith": [
          "gopher"
        ],
        "expected": true
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2722": {
    "functionNames": [
      "make_starts_text_closure"
    ],
    "tests": [
      {
        "args": [
          "-"
        ],
        "callReturnedWith": [
          "code"
        ],
        "expected": false
      },
      {
        "args": [
          "x"
        ],
        "callReturnedWith": [
          "example"
        ],
        "expected": false
      },
      {
        "args": [
          "go"
        ],
        "callReturnedWith": [
          "gopher"
        ],
        "expected": true
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2723": {
    "functionNames": [
      "make_ends_text_closure"
    ],
    "tests": [
      {
        "args": [
          "-"
        ],
        "callReturnedWith": [
          "code"
        ],
        "expected": false
      },
      {
        "args": [
          "x"
        ],
        "callReturnedWith": [
          "example"
        ],
        "expected": false
      },
      {
        "args": [
          "go"
        ],
        "callReturnedWith": [
          "gopher"
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2724": {
    "functionNames": [
      "make_replacement_text_closure"
    ],
    "tests": [
      {
        "args": [
          "-"
        ],
        "callReturnedWith": [
          "code"
        ],
        "expected": "code"
      },
      {
        "args": [
          "x"
        ],
        "callReturnedWith": [
          "example"
        ],
        "expected": "e_ample"
      },
      {
        "args": [
          "go"
        ],
        "callReturnedWith": [
          "gopher"
        ],
        "expected": "_pher"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2725": {
    "functionNames": [
      "make_padding_text_closure"
    ],
    "tests": [
      {
        "args": [
          3
        ],
        "callReturnedWith": [
          "go"
        ],
        "expected": "0go"
      },
      {
        "args": [
          2
        ],
        "callReturnedWith": [
          "example"
        ],
        "expected": "example"
      },
      {
        "args": [
          5
        ],
        "callReturnedWith": [
          "python"
        ],
        "expected": "python"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2726": {
    "functionNames": [
      "make_case_prefix_text_closure"
    ],
    "tests": [
      {
        "args": [
          "-"
        ],
        "callReturnedWith": [
          "code"
        ],
        "expected": "-code"
      },
      {
        "args": [
          "x"
        ],
        "callReturnedWith": [
          "example"
        ],
        "expected": "Xexample"
      },
      {
        "args": [
          "go"
        ],
        "callReturnedWith": [
          "gopher"
        ],
        "expected": "GOgopher"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2727": {
    "functionNames": [
      "make_label_text_closure"
    ],
    "tests": [
      {
        "args": [
          "-"
        ],
        "callReturnedWith": [
          "code"
        ],
        "expected": "-: code"
      },
      {
        "args": [
          "x"
        ],
        "callReturnedWith": [
          "example"
        ],
        "expected": "x: example"
      },
      {
        "args": [
          "go"
        ],
        "callReturnedWith": [
          "gopher"
        ],
        "expected": "go: gopher"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2728": {
    "functionNames": [
      "make_remove_text_closure"
    ],
    "tests": [
      {
        "args": [
          "-"
        ],
        "callReturnedWith": [
          "code"
        ],
        "expected": "code"
      },
      {
        "args": [
          "x"
        ],
        "callReturnedWith": [
          "example"
        ],
        "expected": "eample"
      },
      {
        "args": [
          "go"
        ],
        "callReturnedWith": [
          "gopher"
        ],
        "expected": "pher"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2729": {
    "functionNames": [
      "build_adder_pipeline_closure"
    ],
    "tests": [
      {
        "args": [
          4
        ],
        "callReturnedWith": [
          2
        ],
        "expected": 6
      },
      {
        "args": [
          5
        ],
        "callReturnedWith": [
          7
        ],
        "expected": 12
      },
      {
        "args": [
          2
        ],
        "callReturnedWith": [
          -3
        ],
        "expected": -1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2730": {
    "functionNames": [
      "build_multiplier_pipeline_closure"
    ],
    "tests": [
      {
        "args": [
          4
        ],
        "callReturnedWith": [
          2
        ],
        "expected": 8
      },
      {
        "args": [
          5
        ],
        "callReturnedWith": [
          7
        ],
        "expected": 35
      },
      {
        "args": [
          2
        ],
        "callReturnedWith": [
          -3
        ],
        "expected": -6
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2731": {
    "functionNames": [
      "build_power_pipeline_closure"
    ],
    "tests": [
      {
        "args": [
          4
        ],
        "callReturnedWith": [
          2
        ],
        "expected": 16
      },
      {
        "args": [
          5
        ],
        "callReturnedWith": [
          7
        ],
        "expected": 16807
      },
      {
        "args": [
          2
        ],
        "callReturnedWith": [
          -3
        ],
        "expected": 9
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2732": {
    "functionNames": [
      "build_minimum_pipeline_closure"
    ],
    "tests": [
      {
        "args": [
          4
        ],
        "callReturnedWith": [
          2
        ],
        "expected": 4
      },
      {
        "args": [
          5
        ],
        "callReturnedWith": [
          7
        ],
        "expected": 7
      },
      {
        "args": [
          2
        ],
        "callReturnedWith": [
          -3
        ],
        "expected": 2
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2733": {
    "functionNames": [
      "build_maximum_pipeline_closure"
    ],
    "tests": [
      {
        "args": [
          4
        ],
        "callReturnedWith": [
          2
        ],
        "expected": 2
      },
      {
        "args": [
          5
        ],
        "callReturnedWith": [
          7
        ],
        "expected": 5
      },
      {
        "args": [
          2
        ],
        "callReturnedWith": [
          -3
        ],
        "expected": -3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2734": {
    "functionNames": [
      "build_remainder_pipeline_closure"
    ],
    "tests": [
      {
        "args": [
          4
        ],
        "callReturnedWith": [
          2
        ],
        "expected": 2
      },
      {
        "args": [
          5
        ],
        "callReturnedWith": [
          7
        ],
        "expected": 2
      },
      {
        "args": [
          2
        ],
        "callReturnedWith": [
          -3
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2735": {
    "functionNames": [
      "build_distance_pipeline_closure"
    ],
    "tests": [
      {
        "args": [
          4
        ],
        "callReturnedWith": [
          2
        ],
        "expected": 2
      },
      {
        "args": [
          5
        ],
        "callReturnedWith": [
          7
        ],
        "expected": 2
      },
      {
        "args": [
          2
        ],
        "callReturnedWith": [
          -3
        ],
        "expected": 5
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2736": {
    "functionNames": [
      "build_percentage_pipeline_closure"
    ],
    "tests": [
      {
        "args": [
          4
        ],
        "callReturnedWith": [
          2
        ],
        "expected": 0.08
      },
      {
        "args": [
          5
        ],
        "callReturnedWith": [
          7
        ],
        "expected": 0.35
      },
      {
        "args": [
          2
        ],
        "callReturnedWith": [
          -3
        ],
        "expected": -0.06
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2737": {
    "functionNames": [
      "build_offset_square_pipeline_closure"
    ],
    "tests": [
      {
        "args": [
          4
        ],
        "callReturnedWith": [
          2
        ],
        "expected": 36
      },
      {
        "args": [
          5
        ],
        "callReturnedWith": [
          7
        ],
        "expected": 144
      },
      {
        "args": [
          2
        ],
        "callReturnedWith": [
          -3
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2738": {
    "functionNames": [
      "build_scale_then_add_pipeline_closure"
    ],
    "tests": [
      {
        "args": [
          4
        ],
        "callReturnedWith": [
          2
        ],
        "expected": 9
      },
      {
        "args": [
          5
        ],
        "callReturnedWith": [
          7
        ],
        "expected": 36
      },
      {
        "args": [
          2
        ],
        "callReturnedWith": [
          -3
        ],
        "expected": -5
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2739": {
    "functionNames": [
      "build_subtract_from_pipeline_closure"
    ],
    "tests": [
      {
        "args": [
          4
        ],
        "callReturnedWith": [
          2
        ],
        "expected": 2
      },
      {
        "args": [
          5
        ],
        "callReturnedWith": [
          7
        ],
        "expected": -2
      },
      {
        "args": [
          2
        ],
        "callReturnedWith": [
          -3
        ],
        "expected": 5
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2740": {
    "functionNames": [
      "build_multiple_check_pipeline_closure"
    ],
    "tests": [
      {
        "args": [
          4
        ],
        "callReturnedWith": [
          2
        ],
        "expected": false
      },
      {
        "args": [
          5
        ],
        "callReturnedWith": [
          7
        ],
        "expected": false
      },
      {
        "args": [
          2
        ],
        "callReturnedWith": [
          -3
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2741": {
    "functionNames": [
      "build_greater_check_pipeline_closure"
    ],
    "tests": [
      {
        "args": [
          4
        ],
        "callReturnedWith": [
          2
        ],
        "expected": false
      },
      {
        "args": [
          5
        ],
        "callReturnedWith": [
          7
        ],
        "expected": true
      },
      {
        "args": [
          2
        ],
        "callReturnedWith": [
          -3
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2742": {
    "functionNames": [
      "build_range_check_pipeline_closure"
    ],
    "tests": [
      {
        "args": [
          4
        ],
        "callReturnedWith": [
          2
        ],
        "expected": true
      },
      {
        "args": [
          5
        ],
        "callReturnedWith": [
          7
        ],
        "expected": false
      },
      {
        "args": [
          2
        ],
        "callReturnedWith": [
          -3
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "2743": {
    "functionNames": [
      "first_two_list_slice"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1,
            2,
            3,
            4,
            5,
            6
          ]
        ],
        "expected": [
          0,
          1
        ]
      },
      {
        "args": [
          [
            "a",
            "b",
            "c",
            "d"
          ]
        ],
        "expected": [
          "a",
          "b"
        ]
      },
      {
        "args": [
          [
            9,
            8,
            7,
            6,
            5
          ]
        ],
        "expected": [
          9,
          8
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2744": {
    "functionNames": [
      "last_two_list_slice"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1,
            2,
            3,
            4,
            5,
            6
          ]
        ],
        "expected": [
          5,
          6
        ]
      },
      {
        "args": [
          [
            "a",
            "b",
            "c",
            "d"
          ]
        ],
        "expected": [
          "c",
          "d"
        ]
      },
      {
        "args": [
          [
            9,
            8,
            7,
            6,
            5
          ]
        ],
        "expected": [
          6,
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2745": {
    "functionNames": [
      "drop_first_list_slice"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1,
            2,
            3,
            4,
            5,
            6
          ]
        ],
        "expected": [
          1,
          2,
          3,
          4,
          5,
          6
        ]
      },
      {
        "args": [
          [
            "a",
            "b",
            "c",
            "d"
          ]
        ],
        "expected": [
          "b",
          "c",
          "d"
        ]
      },
      {
        "args": [
          [
            9,
            8,
            7,
            6,
            5
          ]
        ],
        "expected": [
          8,
          7,
          6,
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2746": {
    "functionNames": [
      "drop_last_list_slice"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1,
            2,
            3,
            4,
            5,
            6
          ]
        ],
        "expected": [
          0,
          1,
          2,
          3,
          4,
          5
        ]
      },
      {
        "args": [
          [
            "a",
            "b",
            "c",
            "d"
          ]
        ],
        "expected": [
          "a",
          "b",
          "c"
        ]
      },
      {
        "args": [
          [
            9,
            8,
            7,
            6,
            5
          ]
        ],
        "expected": [
          9,
          8,
          7,
          6
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2747": {
    "functionNames": [
      "reverse_list_slice"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1,
            2,
            3,
            4,
            5,
            6
          ]
        ],
        "expected": [
          6,
          5,
          4,
          3,
          2,
          1,
          0
        ]
      },
      {
        "args": [
          [
            "a",
            "b",
            "c",
            "d"
          ]
        ],
        "expected": [
          "d",
          "c",
          "b",
          "a"
        ]
      },
      {
        "args": [
          [
            9,
            8,
            7,
            6,
            5
          ]
        ],
        "expected": [
          5,
          6,
          7,
          8,
          9
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2748": {
    "functionNames": [
      "even_positions_list_slice"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1,
            2,
            3,
            4,
            5,
            6
          ]
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
          [
            "a",
            "b",
            "c",
            "d"
          ]
        ],
        "expected": [
          "a",
          "c"
        ]
      },
      {
        "args": [
          [
            9,
            8,
            7,
            6,
            5
          ]
        ],
        "expected": [
          9,
          7,
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2749": {
    "functionNames": [
      "odd_positions_list_slice"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1,
            2,
            3,
            4,
            5,
            6
          ]
        ],
        "expected": [
          1,
          3,
          5
        ]
      },
      {
        "args": [
          [
            "a",
            "b",
            "c",
            "d"
          ]
        ],
        "expected": [
          "b",
          "d"
        ]
      },
      {
        "args": [
          [
            9,
            8,
            7,
            6,
            5
          ]
        ],
        "expected": [
          8,
          6
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2750": {
    "functionNames": [
      "middle_list_slice"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1,
            2,
            3,
            4,
            5,
            6
          ]
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
          [
            "a",
            "b",
            "c",
            "d"
          ]
        ],
        "expected": [
          "b",
          "c"
        ]
      },
      {
        "args": [
          [
            9,
            8,
            7,
            6,
            5
          ]
        ],
        "expected": [
          8,
          7,
          6
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2751": {
    "functionNames": [
      "first_half_list_slice"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1,
            2,
            3,
            4,
            5,
            6
          ]
        ],
        "expected": [
          0,
          1,
          2
        ]
      },
      {
        "args": [
          [
            "a",
            "b",
            "c",
            "d"
          ]
        ],
        "expected": [
          "a",
          "b"
        ]
      },
      {
        "args": [
          [
            9,
            8,
            7,
            6,
            5
          ]
        ],
        "expected": [
          9,
          8
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2752": {
    "functionNames": [
      "second_half_list_slice"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1,
            2,
            3,
            4,
            5,
            6
          ]
        ],
        "expected": [
          3,
          4,
          5,
          6
        ]
      },
      {
        "args": [
          [
            "a",
            "b",
            "c",
            "d"
          ]
        ],
        "expected": [
          "c",
          "d"
        ]
      },
      {
        "args": [
          [
            9,
            8,
            7,
            6,
            5
          ]
        ],
        "expected": [
          7,
          6,
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2753": {
    "functionNames": [
      "every_third_list_slice"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1,
            2,
            3,
            4,
            5,
            6
          ]
        ],
        "expected": [
          0,
          3,
          6
        ]
      },
      {
        "args": [
          [
            "a",
            "b",
            "c",
            "d"
          ]
        ],
        "expected": [
          "a",
          "d"
        ]
      },
      {
        "args": [
          [
            9,
            8,
            7,
            6,
            5
          ]
        ],
        "expected": [
          9,
          6
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2754": {
    "functionNames": [
      "reverse_every_second_list_slice"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1,
            2,
            3,
            4,
            5,
            6
          ]
        ],
        "expected": [
          6,
          4,
          2,
          0
        ]
      },
      {
        "args": [
          [
            "a",
            "b",
            "c",
            "d"
          ]
        ],
        "expected": [
          "d",
          "b"
        ]
      },
      {
        "args": [
          [
            9,
            8,
            7,
            6,
            5
          ]
        ],
        "expected": [
          5,
          7,
          9
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2755": {
    "functionNames": [
      "without_edges_two_list_slice"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1,
            2,
            3,
            4,
            5,
            6
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
            "a",
            "b",
            "c",
            "d"
          ]
        ],
        "expected": []
      },
      {
        "args": [
          [
            9,
            8,
            7,
            6,
            5
          ]
        ],
        "expected": [
          7
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2756": {
    "functionNames": [
      "first_three_reverse_list_slice"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1,
            2,
            3,
            4,
            5,
            6
          ]
        ],
        "expected": [
          2,
          1,
          0
        ]
      },
      {
        "args": [
          [
            "a",
            "b",
            "c",
            "d"
          ]
        ],
        "expected": [
          "c",
          "b",
          "a"
        ]
      },
      {
        "args": [
          [
            9,
            8,
            7,
            6,
            5
          ]
        ],
        "expected": [
          7,
          8,
          9
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2757": {
    "functionNames": [
      "last_three_reverse_list_slice"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1,
            2,
            3,
            4,
            5,
            6
          ]
        ],
        "expected": [
          6,
          5,
          4
        ]
      },
      {
        "args": [
          [
            "a",
            "b",
            "c",
            "d"
          ]
        ],
        "expected": [
          "d",
          "c",
          "b"
        ]
      },
      {
        "args": [
          [
            9,
            8,
            7,
            6,
            5
          ]
        ],
        "expected": [
          5,
          6,
          7
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2758": {
    "functionNames": [
      "copy_list_slice"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1,
            2,
            3,
            4,
            5,
            6
          ]
        ],
        "expected": [
          0,
          1,
          2,
          3,
          4,
          5,
          6
        ]
      },
      {
        "args": [
          [
            "a",
            "b",
            "c",
            "d"
          ]
        ],
        "expected": [
          "a",
          "b",
          "c",
          "d"
        ]
      },
      {
        "args": [
          [
            9,
            8,
            7,
            6,
            5
          ]
        ],
        "expected": [
          9,
          8,
          7,
          6,
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2759": {
    "functionNames": [
      "quarter_start_list_slice"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1,
            2,
            3,
            4,
            5,
            6
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
            "b",
            "c",
            "d"
          ]
        ],
        "expected": [
          "b",
          "c",
          "d"
        ]
      },
      {
        "args": [
          [
            9,
            8,
            7,
            6,
            5
          ]
        ],
        "expected": [
          8,
          7,
          6
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2760": {
    "functionNames": [
      "bounded_step_list_slice"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1,
            2,
            3,
            4,
            5,
            6
          ]
        ],
        "expected": [
          1,
          3,
          5
        ]
      },
      {
        "args": [
          [
            "a",
            "b",
            "c",
            "d"
          ]
        ],
        "expected": [
          "b",
          "d"
        ]
      },
      {
        "args": [
          [
            9,
            8,
            7,
            6,
            5
          ]
        ],
        "expected": [
          8,
          6
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2761": {
    "functionNames": [
      "reverse_middle_list_slice"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1,
            2,
            3,
            4,
            5,
            6
          ]
        ],
        "expected": [
          5,
          4,
          3,
          2,
          1
        ]
      },
      {
        "args": [
          [
            "a",
            "b",
            "c",
            "d"
          ]
        ],
        "expected": [
          "c",
          "b"
        ]
      },
      {
        "args": [
          [
            9,
            8,
            7,
            6,
            5
          ]
        ],
        "expected": [
          6,
          7,
          8
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2762": {
    "functionNames": [
      "first_from_reverse_list_slice"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1,
            2,
            3,
            4,
            5,
            6
          ]
        ],
        "expected": [
          6,
          5,
          4,
          3,
          2,
          1
        ]
      },
      {
        "args": [
          [
            "a",
            "b",
            "c",
            "d"
          ]
        ],
        "expected": [
          "d",
          "c",
          "b"
        ]
      },
      {
        "args": [
          [
            9,
            8,
            7,
            6,
            5
          ]
        ],
        "expected": [
          5,
          6,
          7,
          8
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2763": {
    "functionNames": [
      "up_to_four_list_slice"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1,
            2,
            3,
            4,
            5,
            6
          ]
        ],
        "expected": [
          0,
          1,
          2,
          3
        ]
      },
      {
        "args": [
          [
            "a",
            "b",
            "c",
            "d"
          ]
        ],
        "expected": [
          "a",
          "b",
          "c",
          "d"
        ]
      },
      {
        "args": [
          [
            9,
            8,
            7,
            6,
            5
          ]
        ],
        "expected": [
          9,
          8,
          7,
          6
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2764": {
    "functionNames": [
      "from_third_list_slice"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1,
            2,
            3,
            4,
            5,
            6
          ]
        ],
        "expected": [
          2,
          3,
          4,
          5,
          6
        ]
      },
      {
        "args": [
          [
            "a",
            "b",
            "c",
            "d"
          ]
        ],
        "expected": [
          "c",
          "d"
        ]
      },
      {
        "args": [
          [
            9,
            8,
            7,
            6,
            5
          ]
        ],
        "expected": [
          7,
          6,
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2765": {
    "functionNames": [
      "exclude_last_three_list_slice"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1,
            2,
            3,
            4,
            5,
            6
          ]
        ],
        "expected": [
          0,
          1,
          2,
          3
        ]
      },
      {
        "args": [
          [
            "a",
            "b",
            "c",
            "d"
          ]
        ],
        "expected": [
          "a"
        ]
      },
      {
        "args": [
          [
            9,
            8,
            7,
            6,
            5
          ]
        ],
        "expected": [
          9,
          8
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2766": {
    "functionNames": [
      "last_four_step_two_list_slice"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1,
            2,
            3,
            4,
            5,
            6
          ]
        ],
        "expected": [
          3,
          5
        ]
      },
      {
        "args": [
          [
            "a",
            "b",
            "c",
            "d"
          ]
        ],
        "expected": [
          "a",
          "c"
        ]
      },
      {
        "args": [
          [
            9,
            8,
            7,
            6,
            5
          ]
        ],
        "expected": [
          8,
          6
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2767": {
    "functionNames": [
      "double_reverse_copy_list_slice"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1,
            2,
            3,
            4,
            5,
            6
          ]
        ],
        "expected": [
          0,
          1,
          2,
          3,
          4,
          5,
          6
        ]
      },
      {
        "args": [
          [
            "a",
            "b",
            "c",
            "d"
          ]
        ],
        "expected": [
          "a",
          "b",
          "c",
          "d"
        ]
      },
      {
        "args": [
          [
            9,
            8,
            7,
            6,
            5
          ]
        ],
        "expected": [
          9,
          8,
          7,
          6,
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2768": {
    "functionNames": [
      "first_two_text_slice"
    ],
    "tests": [
      {
        "args": [
          "abcdefgh"
        ],
        "expected": "ab"
      },
      {
        "args": [
          "Python"
        ],
        "expected": "Py"
      },
      {
        "args": [
          "12345"
        ],
        "expected": "12"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2769": {
    "functionNames": [
      "last_two_text_slice"
    ],
    "tests": [
      {
        "args": [
          "abcdefgh"
        ],
        "expected": "gh"
      },
      {
        "args": [
          "Python"
        ],
        "expected": "on"
      },
      {
        "args": [
          "12345"
        ],
        "expected": "45"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2770": {
    "functionNames": [
      "drop_first_text_slice"
    ],
    "tests": [
      {
        "args": [
          "abcdefgh"
        ],
        "expected": "bcdefgh"
      },
      {
        "args": [
          "Python"
        ],
        "expected": "ython"
      },
      {
        "args": [
          "12345"
        ],
        "expected": "2345"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2771": {
    "functionNames": [
      "drop_last_text_slice"
    ],
    "tests": [
      {
        "args": [
          "abcdefgh"
        ],
        "expected": "abcdefg"
      },
      {
        "args": [
          "Python"
        ],
        "expected": "Pytho"
      },
      {
        "args": [
          "12345"
        ],
        "expected": "1234"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2772": {
    "functionNames": [
      "reverse_text_slice"
    ],
    "tests": [
      {
        "args": [
          "abcdefgh"
        ],
        "expected": "hgfedcba"
      },
      {
        "args": [
          "Python"
        ],
        "expected": "nohtyP"
      },
      {
        "args": [
          "12345"
        ],
        "expected": "54321"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2773": {
    "functionNames": [
      "even_positions_text_slice"
    ],
    "tests": [
      {
        "args": [
          "abcdefgh"
        ],
        "expected": "aceg"
      },
      {
        "args": [
          "Python"
        ],
        "expected": "Pto"
      },
      {
        "args": [
          "12345"
        ],
        "expected": "135"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2774": {
    "functionNames": [
      "odd_positions_text_slice"
    ],
    "tests": [
      {
        "args": [
          "abcdefgh"
        ],
        "expected": "bdfh"
      },
      {
        "args": [
          "Python"
        ],
        "expected": "yhn"
      },
      {
        "args": [
          "12345"
        ],
        "expected": "24"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2775": {
    "functionNames": [
      "middle_text_slice"
    ],
    "tests": [
      {
        "args": [
          "abcdefgh"
        ],
        "expected": "bcdefg"
      },
      {
        "args": [
          "Python"
        ],
        "expected": "ytho"
      },
      {
        "args": [
          "12345"
        ],
        "expected": "234"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2776": {
    "functionNames": [
      "first_half_text_slice"
    ],
    "tests": [
      {
        "args": [
          "abcdefgh"
        ],
        "expected": "abcd"
      },
      {
        "args": [
          "Python"
        ],
        "expected": "Pyt"
      },
      {
        "args": [
          "12345"
        ],
        "expected": "12"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2777": {
    "functionNames": [
      "second_half_text_slice"
    ],
    "tests": [
      {
        "args": [
          "abcdefgh"
        ],
        "expected": "efgh"
      },
      {
        "args": [
          "Python"
        ],
        "expected": "hon"
      },
      {
        "args": [
          "12345"
        ],
        "expected": "345"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2778": {
    "functionNames": [
      "every_third_text_slice"
    ],
    "tests": [
      {
        "args": [
          "abcdefgh"
        ],
        "expected": "adg"
      },
      {
        "args": [
          "Python"
        ],
        "expected": "Ph"
      },
      {
        "args": [
          "12345"
        ],
        "expected": "14"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2779": {
    "functionNames": [
      "reverse_every_second_text_slice"
    ],
    "tests": [
      {
        "args": [
          "abcdefgh"
        ],
        "expected": "hfdb"
      },
      {
        "args": [
          "Python"
        ],
        "expected": "nhy"
      },
      {
        "args": [
          "12345"
        ],
        "expected": "531"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2780": {
    "functionNames": [
      "without_edges_two_text_slice"
    ],
    "tests": [
      {
        "args": [
          "abcdefgh"
        ],
        "expected": "cdef"
      },
      {
        "args": [
          "Python"
        ],
        "expected": "th"
      },
      {
        "args": [
          "12345"
        ],
        "expected": "3"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2781": {
    "functionNames": [
      "first_three_reverse_text_slice"
    ],
    "tests": [
      {
        "args": [
          "abcdefgh"
        ],
        "expected": "cba"
      },
      {
        "args": [
          "Python"
        ],
        "expected": "tyP"
      },
      {
        "args": [
          "12345"
        ],
        "expected": "321"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2782": {
    "functionNames": [
      "last_three_reverse_text_slice"
    ],
    "tests": [
      {
        "args": [
          "abcdefgh"
        ],
        "expected": "hgf"
      },
      {
        "args": [
          "Python"
        ],
        "expected": "noh"
      },
      {
        "args": [
          "12345"
        ],
        "expected": "543"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2783": {
    "functionNames": [
      "copy_text_slice"
    ],
    "tests": [
      {
        "args": [
          "abcdefgh"
        ],
        "expected": "abcdefgh"
      },
      {
        "args": [
          "Python"
        ],
        "expected": "Python"
      },
      {
        "args": [
          "12345"
        ],
        "expected": "12345"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2784": {
    "functionNames": [
      "quarter_start_text_slice"
    ],
    "tests": [
      {
        "args": [
          "abcdefgh"
        ],
        "expected": "bcd"
      },
      {
        "args": [
          "Python"
        ],
        "expected": "yth"
      },
      {
        "args": [
          "12345"
        ],
        "expected": "234"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2785": {
    "functionNames": [
      "bounded_step_text_slice"
    ],
    "tests": [
      {
        "args": [
          "abcdefgh"
        ],
        "expected": "bdf"
      },
      {
        "args": [
          "Python"
        ],
        "expected": "yhn"
      },
      {
        "args": [
          "12345"
        ],
        "expected": "24"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2786": {
    "functionNames": [
      "reverse_middle_text_slice"
    ],
    "tests": [
      {
        "args": [
          "abcdefgh"
        ],
        "expected": "gfedcb"
      },
      {
        "args": [
          "Python"
        ],
        "expected": "ohty"
      },
      {
        "args": [
          "12345"
        ],
        "expected": "432"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2787": {
    "functionNames": [
      "first_from_reverse_text_slice"
    ],
    "tests": [
      {
        "args": [
          "abcdefgh"
        ],
        "expected": "hgfedcb"
      },
      {
        "args": [
          "Python"
        ],
        "expected": "nohty"
      },
      {
        "args": [
          "12345"
        ],
        "expected": "5432"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2788": {
    "functionNames": [
      "up_to_four_text_slice"
    ],
    "tests": [
      {
        "args": [
          "abcdefgh"
        ],
        "expected": "abcd"
      },
      {
        "args": [
          "Python"
        ],
        "expected": "Pyth"
      },
      {
        "args": [
          "12345"
        ],
        "expected": "1234"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2789": {
    "functionNames": [
      "from_third_text_slice"
    ],
    "tests": [
      {
        "args": [
          "abcdefgh"
        ],
        "expected": "cdefgh"
      },
      {
        "args": [
          "Python"
        ],
        "expected": "thon"
      },
      {
        "args": [
          "12345"
        ],
        "expected": "345"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2790": {
    "functionNames": [
      "exclude_last_three_text_slice"
    ],
    "tests": [
      {
        "args": [
          "abcdefgh"
        ],
        "expected": "abcde"
      },
      {
        "args": [
          "Python"
        ],
        "expected": "Pyt"
      },
      {
        "args": [
          "12345"
        ],
        "expected": "12"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2791": {
    "functionNames": [
      "last_four_step_two_text_slice"
    ],
    "tests": [
      {
        "args": [
          "abcdefgh"
        ],
        "expected": "eg"
      },
      {
        "args": [
          "Python"
        ],
        "expected": "to"
      },
      {
        "args": [
          "12345"
        ],
        "expected": "24"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2792": {
    "functionNames": [
      "double_reverse_copy_text_slice"
    ],
    "tests": [
      {
        "args": [
          "abcdefgh"
        ],
        "expected": "abcdefgh"
      },
      {
        "args": [
          "Python"
        ],
        "expected": "Python"
      },
      {
        "args": [
          "12345"
        ],
        "expected": "12345"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Slice",
        "minCount": 1
      }
    ]
  },
  "2793": {
    "functionNames": [
      "extract_signed_integers_regex"
    ],
    "tests": [
      {
        "args": [
          "x=-12 y=+7 z=4"
        ],
        "expected": [
          "-12",
          "+7",
          "4"
        ]
      },
      {
        "args": [
          "none"
        ],
        "expected": []
      },
      {
        "args": [
          "0 -3"
        ],
        "expected": [
          "0",
          "-3"
        ]
      }
    ],
    "requiredAnyCallPatterns": [
      {
        "functionName": "findall",
        "minArgs": 1
      }
    ]
  },
  "2794": {
    "functionNames": [
      "validate_simple_slug_regex"
    ],
    "tests": [
      {
        "args": [
          "hello-world"
        ],
        "expected": true
      },
      {
        "args": [
          "Hello-world"
        ],
        "expected": false
      },
      {
        "args": [
          "one--two"
        ],
        "expected": false
      }
    ],
    "requiredAnyCallPatterns": [
      {
        "functionName": "fullmatch",
        "minArgs": 1
      }
    ]
  },
  "2795": {
    "functionNames": [
      "extract_named_groups_regex"
    ],
    "tests": [
      {
        "args": [
          "Smith, Ada; Jones, Bob"
        ],
        "expected": [
          [
            "Smith",
            "Ada"
          ],
          [
            "Jones",
            "Bob"
          ]
        ]
      },
      {
        "args": [
          "none"
        ],
        "expected": []
      },
      {
        "args": [
          "Lee, Kim"
        ],
        "expected": [
          [
            "Lee",
            "Kim"
          ]
        ]
      }
    ],
    "requiredAnyCallPatterns": [
      {
        "functionName": "findall",
        "minArgs": 1
      }
    ]
  },
  "2796": {
    "functionNames": [
      "normalize_dashes_regex"
    ],
    "tests": [
      {
        "args": [
          "a__b---c"
        ],
        "expected": "a-b-c"
      },
      {
        "args": [
          "clean"
        ],
        "expected": "clean"
      },
      {
        "args": [
          "_x_"
        ],
        "expected": "-x-"
      }
    ],
    "requiredAnyCallPatterns": [
      {
        "functionName": "sub",
        "minArgs": 1
      }
    ]
  },
  "2797": {
    "functionNames": [
      "split_pipe_fields_regex"
    ],
    "tests": [
      {
        "args": [
          "a | b|c"
        ],
        "expected": [
          "a",
          "b",
          "c"
        ]
      },
      {
        "args": [
          "one"
        ],
        "expected": [
          "one"
        ]
      },
      {
        "args": [
          "x  |  y"
        ],
        "expected": [
          "x",
          "y"
        ]
      }
    ],
    "requiredAnyCallPatterns": [
      {
        "functionName": "split",
        "minArgs": 1
      }
    ]
  },
  "2798": {
    "functionNames": [
      "extract_html_attributes_regex"
    ],
    "tests": [
      {
        "args": [
          "id=\"main\" class=\"box\""
        ],
        "expected": [
          [
            "id",
            "main"
          ],
          [
            "class",
            "box"
          ]
        ]
      },
      {
        "args": [
          "disabled"
        ],
        "expected": []
      },
      {
        "args": [
          "x=\"1\""
        ],
        "expected": [
          [
            "x",
            "1"
          ]
        ]
      }
    ],
    "requiredAnyCallPatterns": [
      {
        "functionName": "findall",
        "minArgs": 1
      }
    ]
  },
  "2799": {
    "functionNames": [
      "validate_binary_text_regex"
    ],
    "tests": [
      {
        "args": [
          "10101"
        ],
        "expected": true
      },
      {
        "args": [
          "102"
        ],
        "expected": false
      },
      {
        "args": [
          ""
        ],
        "expected": false
      }
    ],
    "requiredAnyCallPatterns": [
      {
        "functionName": "fullmatch",
        "minArgs": 1
      }
    ]
  },
  "2800": {
    "functionNames": [
      "mask_card_groups_regex"
    ],
    "tests": [
      {
        "args": [
          "1234 5678"
        ],
        "expected": "**** ****"
      },
      {
        "args": [
          "id 12"
        ],
        "expected": "id 12"
      },
      {
        "args": [
          "0000"
        ],
        "expected": "****"
      }
    ],
    "requiredAnyCallPatterns": [
      {
        "functionName": "sub",
        "minArgs": 1
      }
    ]
  },
  "2801": {
    "functionNames": [
      "extract_markdown_links_regex"
    ],
    "tests": [
      {
        "args": [
          "See [Docs](https://x.dev)"
        ],
        "expected": [
          [
            "Docs",
            "https://x.dev"
          ]
        ]
      },
      {
        "args": [
          "none"
        ],
        "expected": []
      },
      {
        "args": [
          "[A](a) [B](b)"
        ],
        "expected": [
          [
            "A",
            "a"
          ],
          [
            "B",
            "b"
          ]
        ]
      }
    ],
    "requiredAnyCallPatterns": [
      {
        "functionName": "findall",
        "minArgs": 1
      }
    ]
  },
  "2802": {
    "functionNames": [
      "count_sentence_endings_regex"
    ],
    "tests": [
      {
        "args": [
          "Hi! How are you? Fine."
        ],
        "expected": 3
      },
      {
        "args": [
          "none"
        ],
        "expected": 0
      },
      {
        "args": [
          "Wow!!!"
        ],
        "expected": 1
      }
    ],
    "requiredAnyCallPatterns": [
      {
        "functionName": "findall",
        "minArgs": 1
      }
    ]
  },
  "2803": {
    "functionNames": [
      "extract_python_identifiers_regex"
    ],
    "tests": [
      {
        "args": [
          "x1 = _value + 2"
        ],
        "expected": [
          "x1",
          "_value"
        ]
      },
      {
        "args": [
          "123"
        ],
        "expected": []
      },
      {
        "args": [
          "hello world"
        ],
        "expected": [
          "hello",
          "world"
        ]
      }
    ],
    "requiredAnyCallPatterns": [
      {
        "functionName": "findall",
        "minArgs": 1
      }
    ]
  },
  "2804": {
    "functionNames": [
      "remove_duplicate_spaces_lines_regex"
    ],
    "tests": [
      {
        "args": [
          "a   b\nc  d"
        ],
        "expected": "a b\nc d"
      },
      {
        "args": [
          "x"
        ],
        "expected": "x"
      },
      {
        "args": [
          "  hi  "
        ],
        "expected": " hi "
      }
    ],
    "requiredAnyCallPatterns": [
      {
        "functionName": "sub",
        "minArgs": 1
      }
    ]
  },
  "2805": {
    "functionNames": [
      "validate_decimal_number_regex"
    ],
    "tests": [
      {
        "args": [
          "-12.5"
        ],
        "expected": true
      },
      {
        "args": [
          ".75"
        ],
        "expected": true
      },
      {
        "args": [
          "1.2.3"
        ],
        "expected": false
      }
    ],
    "requiredAnyCallPatterns": [
      {
        "functionName": "fullmatch",
        "minArgs": 1
      }
    ]
  },
  "2806": {
    "functionNames": [
      "extract_log_levels_regex"
    ],
    "tests": [
      {
        "args": [
          "INFO start ERROR stop"
        ],
        "expected": [
          "INFO",
          "ERROR"
        ]
      },
      {
        "args": [
          "info"
        ],
        "expected": []
      },
      {
        "args": [
          "WARNING"
        ],
        "expected": [
          "WARNING"
        ]
      }
    ],
    "requiredAnyCallPatterns": [
      {
        "functionName": "findall",
        "minArgs": 1
      }
    ]
  },
  "2807": {
    "functionNames": [
      "camel_to_words_regex"
    ],
    "tests": [
      {
        "args": [
          "camelCaseWord"
        ],
        "expected": "camel case word"
      },
      {
        "args": [
          "Python"
        ],
        "expected": "python"
      },
      {
        "args": [
          "already"
        ],
        "expected": "already"
      }
    ],
    "requiredAnyCallPatterns": [
      {
        "functionName": "sub",
        "minArgs": 1
      }
    ]
  }
};
