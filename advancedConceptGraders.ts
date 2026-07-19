import type { AutoGrader } from './graders';

export const ADVANCED_CONCEPT_GRADERS: Record<number, AutoGrader> = {
  "2808": {
    "functionNames": [
      "decorated_double"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 10
      },
      {
        "args": [
          -4
        ],
        "expected": -8
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2809": {
    "functionNames": [
      "decorated_triple"
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
          -4
        ],
        "expected": -12
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2810": {
    "functionNames": [
      "decorated_square"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 25
      },
      {
        "args": [
          -4
        ],
        "expected": 16
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2811": {
    "functionNames": [
      "decorated_cube"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 125
      },
      {
        "args": [
          -4
        ],
        "expected": -64
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2812": {
    "functionNames": [
      "decorated_increment"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 6
      },
      {
        "args": [
          -4
        ],
        "expected": -3
      },
      {
        "args": [
          0
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2813": {
    "functionNames": [
      "decorated_decrement"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 4
      },
      {
        "args": [
          -4
        ],
        "expected": -5
      },
      {
        "args": [
          0
        ],
        "expected": -1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2814": {
    "functionNames": [
      "decorated_negate"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": -5
      },
      {
        "args": [
          -4
        ],
        "expected": 4
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2815": {
    "functionNames": [
      "decorated_absolute"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 4
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2816": {
    "functionNames": [
      "decorated_half"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 2.5
      },
      {
        "args": [
          -4
        ],
        "expected": -2
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2817": {
    "functionNames": [
      "decorated_remainder_three"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 2
      },
      {
        "args": [
          -4
        ],
        "expected": 2
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2818": {
    "functionNames": [
      "decorated_last_digit"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 6
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2819": {
    "functionNames": [
      "decorated_distance_ten"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 14
      },
      {
        "args": [
          0
        ],
        "expected": 10
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2820": {
    "functionNames": [
      "decorated_clamp_zero"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 0
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2821": {
    "functionNames": [
      "decorated_is_even"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": false
      },
      {
        "args": [
          -4
        ],
        "expected": true
      },
      {
        "args": [
          0
        ],
        "expected": true
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2822": {
    "functionNames": [
      "decorated_is_positive"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": true
      },
      {
        "args": [
          -4
        ],
        "expected": false
      },
      {
        "args": [
          0
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2823": {
    "functionNames": [
      "decorated_sign_label"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": "positive"
      },
      {
        "args": [
          -4
        ],
        "expected": "negative"
      },
      {
        "args": [
          0
        ],
        "expected": "zero"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2824": {
    "functionNames": [
      "decorated_digit_count"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 1
      },
      {
        "args": [
          -4
        ],
        "expected": 1
      },
      {
        "args": [
          0
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2825": {
    "functionNames": [
      "decorated_digit_sum"
    ],
    "tests": [
      {
        "args": [
          52
        ],
        "expected": 7
      },
      {
        "args": [
          -407
        ],
        "expected": 11
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2826": {
    "functionNames": [
      "decorated_triangular"
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
          -4
        ],
        "expected": 10
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2827": {
    "functionNames": [
      "decorated_within_ten"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": true
      },
      {
        "args": [
          -14
        ],
        "expected": false
      },
      {
        "args": [
          10
        ],
        "expected": true
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2828": {
    "functionNames": [
      "decorated_uppercase"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "PYTHON"
      },
      {
        "args": [
          "level"
        ],
        "expected": "LEVEL"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "A B C"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2829": {
    "functionNames": [
      "decorated_lowercase"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "a b c"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2830": {
    "functionNames": [
      "decorated_reverse_text"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "nohtyP"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "c b a"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2831": {
    "functionNames": [
      "decorated_text_length"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": 6
      },
      {
        "args": [
          "level"
        ],
        "expected": 5
      },
      {
        "args": [
          "a b c"
        ],
        "expected": 5
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2832": {
    "functionNames": [
      "decorated_first_character"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "P"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      },
      {
        "args": [
          "z"
        ],
        "expected": "z"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2833": {
    "functionNames": [
      "decorated_last_character"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "n"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      },
      {
        "args": [
          "z"
        ],
        "expected": "z"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2834": {
    "functionNames": [
      "decorated_vowel_count"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": 1
      },
      {
        "args": [
          "level"
        ],
        "expected": 2
      },
      {
        "args": [
          "a b c"
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2835": {
    "functionNames": [
      "decorated_word_count"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": 1
      },
      {
        "args": [
          "level"
        ],
        "expected": 1
      },
      {
        "args": [
          "a b c"
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2836": {
    "functionNames": [
      "decorated_remove_spaces"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "Python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "abc"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2837": {
    "functionNames": [
      "decorated_hyphenate"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "Python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "a-b-c"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2838": {
    "functionNames": [
      "decorated_title_words"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "Python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "Level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "A B C"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2839": {
    "functionNames": [
      "decorated_palindrome"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": false
      },
      {
        "args": [
          "level"
        ],
        "expected": true
      },
      {
        "args": [
          "a b c"
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2840": {
    "functionNames": [
      "decorated_digit_characters"
    ],
    "tests": [
      {
        "args": [
          "a1b2"
        ],
        "expected": 2
      },
      {
        "args": [
          "2026"
        ],
        "expected": 4
      },
      {
        "args": [
          "none"
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2841": {
    "functionNames": [
      "decorated_initials"
    ],
    "tests": [
      {
        "args": [
          "python code"
        ],
        "expected": "PC"
      },
      {
        "args": [
          "Ada Lovelace"
        ],
        "expected": "AL"
      },
      {
        "args": [
          "solo"
        ],
        "expected": "S"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2842": {
    "functionNames": [
      "decorated_bracket_text"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "[Python]"
      },
      {
        "args": [
          "level"
        ],
        "expected": "[level]"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "[a b c]"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2843": {
    "functionNames": [
      "decorated_sum_items"
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
            0,
            5
          ]
        ],
        "expected": 3
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 7
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2844": {
    "functionNames": [
      "decorated_maximum_item"
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
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 5
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2845": {
    "functionNames": [
      "decorated_minimum_item"
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
        "expected": 1
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": -2
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2846": {
    "functionNames": [
      "decorated_reverse_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          5,
          0,
          -2
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          1,
          3,
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2847": {
    "functionNames": [
      "decorated_sort_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          0,
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          1,
          3,
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2848": {
    "functionNames": [
      "decorated_unique_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          0,
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2849": {
    "functionNames": [
      "decorated_even_items"
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
          2
        ]
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          0
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2850": {
    "functionNames": [
      "decorated_odd_items"
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
          3
        ]
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": [
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          3,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2851": {
    "functionNames": [
      "decorated_positive_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          3,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2852": {
    "functionNames": [
      "decorated_square_items"
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
            0,
            5
          ]
        ],
        "expected": [
          4,
          0,
          25
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          9,
          9,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2853": {
    "functionNames": [
      "decorated_item_count"
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
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 3
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2854": {
    "functionNames": [
      "decorated_average_items"
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
        "expected": 2
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 1
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 2.3333333333333335
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2855": {
    "functionNames": [
      "decorated_running_total"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          -2,
          3
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          6,
          7
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2856": {
    "functionNames": [
      "decorated_index_pairs"
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
          ]
        ]
      },
      {
        "args": [
          [
            -2,
            0,
            5
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
            5
          ]
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          [
            0,
            3
          ],
          [
            1,
            3
          ],
          [
            2,
            1
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2857": {
    "functionNames": [
      "decorated_nonzero_count"
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
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 2
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "transform_result"
    ],
    "requiredDefinedFunctions": [
      "wrapper",
      "identity"
    ]
  },
  "2858": {
    "functionNames": [
      "iterate_double"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            -4,
            0
          ]
        ],
        "expected": [
          10,
          -8,
          0
        ]
      },
      {
        "args": [
          [
            0,
            5
          ]
        ],
        "expected": [
          0,
          10
        ]
      },
      {
        "args": [
          [
            -4
          ]
        ],
        "expected": [
          -8
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2859": {
    "functionNames": [
      "iterate_triple"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            -4,
            0
          ]
        ],
        "expected": [
          15,
          -12,
          0
        ]
      },
      {
        "args": [
          [
            0,
            5
          ]
        ],
        "expected": [
          0,
          15
        ]
      },
      {
        "args": [
          [
            -4
          ]
        ],
        "expected": [
          -12
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2860": {
    "functionNames": [
      "iterate_square"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            -4,
            0
          ]
        ],
        "expected": [
          25,
          16,
          0
        ]
      },
      {
        "args": [
          [
            0,
            5
          ]
        ],
        "expected": [
          0,
          25
        ]
      },
      {
        "args": [
          [
            -4
          ]
        ],
        "expected": [
          16
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2861": {
    "functionNames": [
      "iterate_cube"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            -4,
            0
          ]
        ],
        "expected": [
          125,
          -64,
          0
        ]
      },
      {
        "args": [
          [
            0,
            5
          ]
        ],
        "expected": [
          0,
          125
        ]
      },
      {
        "args": [
          [
            -4
          ]
        ],
        "expected": [
          -64
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2862": {
    "functionNames": [
      "iterate_increment"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            -4,
            0
          ]
        ],
        "expected": [
          6,
          -3,
          1
        ]
      },
      {
        "args": [
          [
            0,
            5
          ]
        ],
        "expected": [
          1,
          6
        ]
      },
      {
        "args": [
          [
            -4
          ]
        ],
        "expected": [
          -3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2863": {
    "functionNames": [
      "iterate_decrement"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            -4,
            0
          ]
        ],
        "expected": [
          4,
          -5,
          -1
        ]
      },
      {
        "args": [
          [
            0,
            5
          ]
        ],
        "expected": [
          -1,
          4
        ]
      },
      {
        "args": [
          [
            -4
          ]
        ],
        "expected": [
          -5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2864": {
    "functionNames": [
      "iterate_negate"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            -4,
            0
          ]
        ],
        "expected": [
          -5,
          4,
          0
        ]
      },
      {
        "args": [
          [
            0,
            5
          ]
        ],
        "expected": [
          0,
          -5
        ]
      },
      {
        "args": [
          [
            -4
          ]
        ],
        "expected": [
          4
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2865": {
    "functionNames": [
      "iterate_absolute"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            -4,
            0
          ]
        ],
        "expected": [
          5,
          4,
          0
        ]
      },
      {
        "args": [
          [
            0,
            5
          ]
        ],
        "expected": [
          0,
          5
        ]
      },
      {
        "args": [
          [
            -4
          ]
        ],
        "expected": [
          4
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2866": {
    "functionNames": [
      "iterate_half"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            -4,
            0
          ]
        ],
        "expected": [
          2.5,
          -2,
          0
        ]
      },
      {
        "args": [
          [
            0,
            5
          ]
        ],
        "expected": [
          0,
          2.5
        ]
      },
      {
        "args": [
          [
            -4
          ]
        ],
        "expected": [
          -2
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2867": {
    "functionNames": [
      "iterate_remainder_three"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            -4,
            0
          ]
        ],
        "expected": [
          2,
          2,
          0
        ]
      },
      {
        "args": [
          [
            0,
            5
          ]
        ],
        "expected": [
          0,
          2
        ]
      },
      {
        "args": [
          [
            -4
          ]
        ],
        "expected": [
          2
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2868": {
    "functionNames": [
      "iterate_last_digit"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            -4,
            0
          ]
        ],
        "expected": [
          5,
          6,
          0
        ]
      },
      {
        "args": [
          [
            0,
            5
          ]
        ],
        "expected": [
          0,
          5
        ]
      },
      {
        "args": [
          [
            -4
          ]
        ],
        "expected": [
          6
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2869": {
    "functionNames": [
      "iterate_distance_ten"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            -4,
            0
          ]
        ],
        "expected": [
          5,
          14,
          10
        ]
      },
      {
        "args": [
          [
            0,
            5
          ]
        ],
        "expected": [
          10,
          5
        ]
      },
      {
        "args": [
          [
            -4
          ]
        ],
        "expected": [
          14
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2870": {
    "functionNames": [
      "iterate_clamp_zero"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            -4,
            0
          ]
        ],
        "expected": [
          5,
          0,
          0
        ]
      },
      {
        "args": [
          [
            0,
            5
          ]
        ],
        "expected": [
          0,
          5
        ]
      },
      {
        "args": [
          [
            -4
          ]
        ],
        "expected": [
          0
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2871": {
    "functionNames": [
      "iterate_is_even"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            -4,
            0
          ]
        ],
        "expected": [
          false,
          true,
          true
        ]
      },
      {
        "args": [
          [
            0,
            5
          ]
        ],
        "expected": [
          true,
          false
        ]
      },
      {
        "args": [
          [
            -4
          ]
        ],
        "expected": [
          true
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2872": {
    "functionNames": [
      "iterate_is_positive"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            -4,
            0
          ]
        ],
        "expected": [
          true,
          false,
          false
        ]
      },
      {
        "args": [
          [
            0,
            5
          ]
        ],
        "expected": [
          false,
          true
        ]
      },
      {
        "args": [
          [
            -4
          ]
        ],
        "expected": [
          false
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2873": {
    "functionNames": [
      "iterate_sign_label"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            -4,
            0
          ]
        ],
        "expected": [
          "positive",
          "negative",
          "zero"
        ]
      },
      {
        "args": [
          [
            0,
            5
          ]
        ],
        "expected": [
          "zero",
          "positive"
        ]
      },
      {
        "args": [
          [
            -4
          ]
        ],
        "expected": [
          "negative"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2874": {
    "functionNames": [
      "iterate_digit_count"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            -4,
            0
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
            0,
            5
          ]
        ],
        "expected": [
          1,
          1
        ]
      },
      {
        "args": [
          [
            -4
          ]
        ],
        "expected": [
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2875": {
    "functionNames": [
      "iterate_digit_sum"
    ],
    "tests": [
      {
        "args": [
          [
            52,
            -407,
            0
          ]
        ],
        "expected": [
          7,
          11,
          0
        ]
      },
      {
        "args": [
          [
            0,
            52
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
            -407
          ]
        ],
        "expected": [
          11
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2876": {
    "functionNames": [
      "iterate_triangular"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            -4,
            0
          ]
        ],
        "expected": [
          15,
          10,
          0
        ]
      },
      {
        "args": [
          [
            0,
            5
          ]
        ],
        "expected": [
          0,
          15
        ]
      },
      {
        "args": [
          [
            -4
          ]
        ],
        "expected": [
          10
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2877": {
    "functionNames": [
      "iterate_within_ten"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            -14,
            10
          ]
        ],
        "expected": [
          true,
          false,
          true
        ]
      },
      {
        "args": [
          [
            10,
            5
          ]
        ],
        "expected": [
          true,
          true
        ]
      },
      {
        "args": [
          [
            -14
          ]
        ],
        "expected": [
          false
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2878": {
    "functionNames": [
      "iterate_uppercase"
    ],
    "tests": [
      {
        "args": [
          [
            "Python",
            "level",
            "a b c"
          ]
        ],
        "expected": [
          "PYTHON",
          "LEVEL",
          "A B C"
        ]
      },
      {
        "args": [
          [
            "a b c",
            "Python"
          ]
        ],
        "expected": [
          "A B C",
          "PYTHON"
        ]
      },
      {
        "args": [
          [
            "level"
          ]
        ],
        "expected": [
          "LEVEL"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2879": {
    "functionNames": [
      "iterate_lowercase"
    ],
    "tests": [
      {
        "args": [
          [
            "Python",
            "level",
            "a b c"
          ]
        ],
        "expected": [
          "python",
          "level",
          "a b c"
        ]
      },
      {
        "args": [
          [
            "a b c",
            "Python"
          ]
        ],
        "expected": [
          "a b c",
          "python"
        ]
      },
      {
        "args": [
          [
            "level"
          ]
        ],
        "expected": [
          "level"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2880": {
    "functionNames": [
      "iterate_reverse_text"
    ],
    "tests": [
      {
        "args": [
          [
            "Python",
            "level",
            "a b c"
          ]
        ],
        "expected": [
          "nohtyP",
          "level",
          "c b a"
        ]
      },
      {
        "args": [
          [
            "a b c",
            "Python"
          ]
        ],
        "expected": [
          "c b a",
          "nohtyP"
        ]
      },
      {
        "args": [
          [
            "level"
          ]
        ],
        "expected": [
          "level"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2881": {
    "functionNames": [
      "iterate_text_length"
    ],
    "tests": [
      {
        "args": [
          [
            "Python",
            "level",
            "a b c"
          ]
        ],
        "expected": [
          6,
          5,
          5
        ]
      },
      {
        "args": [
          [
            "a b c",
            "Python"
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
            "level"
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2882": {
    "functionNames": [
      "iterate_first_character"
    ],
    "tests": [
      {
        "args": [
          [
            "Python",
            "",
            "z"
          ]
        ],
        "expected": [
          "P",
          "",
          "z"
        ]
      },
      {
        "args": [
          [
            "z",
            "Python"
          ]
        ],
        "expected": [
          "z",
          "P"
        ]
      },
      {
        "args": [
          [
            ""
          ]
        ],
        "expected": [
          ""
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2883": {
    "functionNames": [
      "iterate_last_character"
    ],
    "tests": [
      {
        "args": [
          [
            "Python",
            "",
            "z"
          ]
        ],
        "expected": [
          "n",
          "",
          "z"
        ]
      },
      {
        "args": [
          [
            "z",
            "Python"
          ]
        ],
        "expected": [
          "z",
          "n"
        ]
      },
      {
        "args": [
          [
            ""
          ]
        ],
        "expected": [
          ""
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2884": {
    "functionNames": [
      "iterate_vowel_count"
    ],
    "tests": [
      {
        "args": [
          [
            "Python",
            "level",
            "a b c"
          ]
        ],
        "expected": [
          1,
          2,
          1
        ]
      },
      {
        "args": [
          [
            "a b c",
            "Python"
          ]
        ],
        "expected": [
          1,
          1
        ]
      },
      {
        "args": [
          [
            "level"
          ]
        ],
        "expected": [
          2
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2885": {
    "functionNames": [
      "iterate_word_count"
    ],
    "tests": [
      {
        "args": [
          [
            "Python",
            "level",
            "a b c"
          ]
        ],
        "expected": [
          1,
          1,
          3
        ]
      },
      {
        "args": [
          [
            "a b c",
            "Python"
          ]
        ],
        "expected": [
          3,
          1
        ]
      },
      {
        "args": [
          [
            "level"
          ]
        ],
        "expected": [
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2886": {
    "functionNames": [
      "iterate_remove_spaces"
    ],
    "tests": [
      {
        "args": [
          [
            "Python",
            "level",
            "a b c"
          ]
        ],
        "expected": [
          "Python",
          "level",
          "abc"
        ]
      },
      {
        "args": [
          [
            "a b c",
            "Python"
          ]
        ],
        "expected": [
          "abc",
          "Python"
        ]
      },
      {
        "args": [
          [
            "level"
          ]
        ],
        "expected": [
          "level"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2887": {
    "functionNames": [
      "iterate_hyphenate"
    ],
    "tests": [
      {
        "args": [
          [
            "Python",
            "level",
            "a b c"
          ]
        ],
        "expected": [
          "Python",
          "level",
          "a-b-c"
        ]
      },
      {
        "args": [
          [
            "a b c",
            "Python"
          ]
        ],
        "expected": [
          "a-b-c",
          "Python"
        ]
      },
      {
        "args": [
          [
            "level"
          ]
        ],
        "expected": [
          "level"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2888": {
    "functionNames": [
      "iterate_title_words"
    ],
    "tests": [
      {
        "args": [
          [
            "Python",
            "level",
            "a b c"
          ]
        ],
        "expected": [
          "Python",
          "Level",
          "A B C"
        ]
      },
      {
        "args": [
          [
            "a b c",
            "Python"
          ]
        ],
        "expected": [
          "A B C",
          "Python"
        ]
      },
      {
        "args": [
          [
            "level"
          ]
        ],
        "expected": [
          "Level"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2889": {
    "functionNames": [
      "iterate_palindrome"
    ],
    "tests": [
      {
        "args": [
          [
            "Python",
            "level",
            "a b c"
          ]
        ],
        "expected": [
          false,
          true,
          false
        ]
      },
      {
        "args": [
          [
            "a b c",
            "Python"
          ]
        ],
        "expected": [
          false,
          false
        ]
      },
      {
        "args": [
          [
            "level"
          ]
        ],
        "expected": [
          true
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2890": {
    "functionNames": [
      "iterate_digit_characters"
    ],
    "tests": [
      {
        "args": [
          [
            "a1b2",
            "2026",
            "none"
          ]
        ],
        "expected": [
          2,
          4,
          0
        ]
      },
      {
        "args": [
          [
            "none",
            "a1b2"
          ]
        ],
        "expected": [
          0,
          2
        ]
      },
      {
        "args": [
          [
            "2026"
          ]
        ],
        "expected": [
          4
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2891": {
    "functionNames": [
      "iterate_initials"
    ],
    "tests": [
      {
        "args": [
          [
            "python code",
            "Ada Lovelace",
            "solo"
          ]
        ],
        "expected": [
          "PC",
          "AL",
          "S"
        ]
      },
      {
        "args": [
          [
            "solo",
            "python code"
          ]
        ],
        "expected": [
          "S",
          "PC"
        ]
      },
      {
        "args": [
          [
            "Ada Lovelace"
          ]
        ],
        "expected": [
          "AL"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2892": {
    "functionNames": [
      "iterate_bracket_text"
    ],
    "tests": [
      {
        "args": [
          [
            "Python",
            "level",
            "a b c"
          ]
        ],
        "expected": [
          "[Python]",
          "[level]",
          "[a b c]"
        ]
      },
      {
        "args": [
          [
            "a b c",
            "Python"
          ]
        ],
        "expected": [
          "[a b c]",
          "[Python]"
        ]
      },
      {
        "args": [
          [
            "level"
          ]
        ],
        "expected": [
          "[level]"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2893": {
    "functionNames": [
      "iterate_sum_items"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              -2,
              0,
              5
            ],
            [
              3,
              3,
              1
            ]
          ]
        ],
        "expected": [
          6,
          3,
          7
        ]
      },
      {
        "args": [
          [
            [
              3,
              3,
              1
            ],
            [
              1,
              2,
              3
            ]
          ]
        ],
        "expected": [
          7,
          6
        ]
      },
      {
        "args": [
          [
            [
              -2,
              0,
              5
            ]
          ]
        ],
        "expected": [
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2894": {
    "functionNames": [
      "iterate_maximum_item"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              -2,
              0,
              5
            ],
            [
              3,
              3,
              1
            ]
          ]
        ],
        "expected": [
          3,
          5,
          3
        ]
      },
      {
        "args": [
          [
            [
              3,
              3,
              1
            ],
            [
              1,
              2,
              3
            ]
          ]
        ],
        "expected": [
          3,
          3
        ]
      },
      {
        "args": [
          [
            [
              -2,
              0,
              5
            ]
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2895": {
    "functionNames": [
      "iterate_minimum_item"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              -2,
              0,
              5
            ],
            [
              3,
              3,
              1
            ]
          ]
        ],
        "expected": [
          1,
          -2,
          1
        ]
      },
      {
        "args": [
          [
            [
              3,
              3,
              1
            ],
            [
              1,
              2,
              3
            ]
          ]
        ],
        "expected": [
          1,
          1
        ]
      },
      {
        "args": [
          [
            [
              -2,
              0,
              5
            ]
          ]
        ],
        "expected": [
          -2
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2896": {
    "functionNames": [
      "iterate_reverse_items"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              -2,
              0,
              5
            ],
            [
              3,
              3,
              1
            ]
          ]
        ],
        "expected": [
          [
            3,
            2,
            1
          ],
          [
            5,
            0,
            -2
          ],
          [
            1,
            3,
            3
          ]
        ]
      },
      {
        "args": [
          [
            [
              3,
              3,
              1
            ],
            [
              1,
              2,
              3
            ]
          ]
        ],
        "expected": [
          [
            1,
            3,
            3
          ],
          [
            3,
            2,
            1
          ]
        ]
      },
      {
        "args": [
          [
            [
              -2,
              0,
              5
            ]
          ]
        ],
        "expected": [
          [
            5,
            0,
            -2
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2897": {
    "functionNames": [
      "iterate_sort_items"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              -2,
              0,
              5
            ],
            [
              3,
              3,
              1
            ]
          ]
        ],
        "expected": [
          [
            1,
            2,
            3
          ],
          [
            -2,
            0,
            5
          ],
          [
            1,
            3,
            3
          ]
        ]
      },
      {
        "args": [
          [
            [
              3,
              3,
              1
            ],
            [
              1,
              2,
              3
            ]
          ]
        ],
        "expected": [
          [
            1,
            3,
            3
          ],
          [
            1,
            2,
            3
          ]
        ]
      },
      {
        "args": [
          [
            [
              -2,
              0,
              5
            ]
          ]
        ],
        "expected": [
          [
            -2,
            0,
            5
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2898": {
    "functionNames": [
      "iterate_unique_items"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              -2,
              0,
              5
            ],
            [
              3,
              3,
              1
            ]
          ]
        ],
        "expected": [
          [
            1,
            2,
            3
          ],
          [
            -2,
            0,
            5
          ],
          [
            3,
            1
          ]
        ]
      },
      {
        "args": [
          [
            [
              3,
              3,
              1
            ],
            [
              1,
              2,
              3
            ]
          ]
        ],
        "expected": [
          [
            3,
            1
          ],
          [
            1,
            2,
            3
          ]
        ]
      },
      {
        "args": [
          [
            [
              -2,
              0,
              5
            ]
          ]
        ],
        "expected": [
          [
            -2,
            0,
            5
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2899": {
    "functionNames": [
      "iterate_even_items"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              -2,
              0,
              5
            ],
            [
              3,
              3,
              1
            ]
          ]
        ],
        "expected": [
          [
            2
          ],
          [
            -2,
            0
          ],
          []
        ]
      },
      {
        "args": [
          [
            [
              3,
              3,
              1
            ],
            [
              1,
              2,
              3
            ]
          ]
        ],
        "expected": [
          [],
          [
            2
          ]
        ]
      },
      {
        "args": [
          [
            [
              -2,
              0,
              5
            ]
          ]
        ],
        "expected": [
          [
            -2,
            0
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2900": {
    "functionNames": [
      "iterate_odd_items"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              -2,
              0,
              5
            ],
            [
              3,
              3,
              1
            ]
          ]
        ],
        "expected": [
          [
            1,
            3
          ],
          [
            5
          ],
          [
            3,
            3,
            1
          ]
        ]
      },
      {
        "args": [
          [
            [
              3,
              3,
              1
            ],
            [
              1,
              2,
              3
            ]
          ]
        ],
        "expected": [
          [
            3,
            3,
            1
          ],
          [
            1,
            3
          ]
        ]
      },
      {
        "args": [
          [
            [
              -2,
              0,
              5
            ]
          ]
        ],
        "expected": [
          [
            5
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2901": {
    "functionNames": [
      "iterate_positive_items"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              -2,
              0,
              5
            ],
            [
              3,
              3,
              1
            ]
          ]
        ],
        "expected": [
          [
            1,
            2,
            3
          ],
          [
            5
          ],
          [
            3,
            3,
            1
          ]
        ]
      },
      {
        "args": [
          [
            [
              3,
              3,
              1
            ],
            [
              1,
              2,
              3
            ]
          ]
        ],
        "expected": [
          [
            3,
            3,
            1
          ],
          [
            1,
            2,
            3
          ]
        ]
      },
      {
        "args": [
          [
            [
              -2,
              0,
              5
            ]
          ]
        ],
        "expected": [
          [
            5
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2902": {
    "functionNames": [
      "iterate_square_items"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              -2,
              0,
              5
            ],
            [
              3,
              3,
              1
            ]
          ]
        ],
        "expected": [
          [
            1,
            4,
            9
          ],
          [
            4,
            0,
            25
          ],
          [
            9,
            9,
            1
          ]
        ]
      },
      {
        "args": [
          [
            [
              3,
              3,
              1
            ],
            [
              1,
              2,
              3
            ]
          ]
        ],
        "expected": [
          [
            9,
            9,
            1
          ],
          [
            1,
            4,
            9
          ]
        ]
      },
      {
        "args": [
          [
            [
              -2,
              0,
              5
            ]
          ]
        ],
        "expected": [
          [
            4,
            0,
            25
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2903": {
    "functionNames": [
      "iterate_item_count"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              -2,
              0,
              5
            ],
            [
              3,
              3,
              1
            ]
          ]
        ],
        "expected": [
          3,
          3,
          3
        ]
      },
      {
        "args": [
          [
            [
              3,
              3,
              1
            ],
            [
              1,
              2,
              3
            ]
          ]
        ],
        "expected": [
          3,
          3
        ]
      },
      {
        "args": [
          [
            [
              -2,
              0,
              5
            ]
          ]
        ],
        "expected": [
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2904": {
    "functionNames": [
      "iterate_average_items"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              -2,
              0,
              5
            ],
            [
              3,
              3,
              1
            ]
          ]
        ],
        "expected": [
          2,
          1,
          2.3333333333333335
        ]
      },
      {
        "args": [
          [
            [
              3,
              3,
              1
            ],
            [
              1,
              2,
              3
            ]
          ]
        ],
        "expected": [
          2.3333333333333335,
          2
        ]
      },
      {
        "args": [
          [
            [
              -2,
              0,
              5
            ]
          ]
        ],
        "expected": [
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2905": {
    "functionNames": [
      "iterate_running_total"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              -2,
              0,
              5
            ],
            [
              3,
              3,
              1
            ]
          ]
        ],
        "expected": [
          [
            1,
            3,
            6
          ],
          [
            -2,
            -2,
            3
          ],
          [
            3,
            6,
            7
          ]
        ]
      },
      {
        "args": [
          [
            [
              3,
              3,
              1
            ],
            [
              1,
              2,
              3
            ]
          ]
        ],
        "expected": [
          [
            3,
            6,
            7
          ],
          [
            1,
            3,
            6
          ]
        ]
      },
      {
        "args": [
          [
            [
              -2,
              0,
              5
            ]
          ]
        ],
        "expected": [
          [
            -2,
            -2,
            3
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2906": {
    "functionNames": [
      "iterate_index_pairs"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              -2,
              0,
              5
            ],
            [
              3,
              3,
              1
            ]
          ]
        ],
        "expected": [
          [
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
            ]
          ],
          [
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
              5
            ]
          ],
          [
            [
              0,
              3
            ],
            [
              1,
              3
            ],
            [
              2,
              1
            ]
          ]
        ]
      },
      {
        "args": [
          [
            [
              3,
              3,
              1
            ],
            [
              1,
              2,
              3
            ]
          ]
        ],
        "expected": [
          [
            [
              0,
              3
            ],
            [
              1,
              3
            ],
            [
              2,
              1
            ]
          ],
          [
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
            ]
          ]
        ]
      },
      {
        "args": [
          [
            [
              -2,
              0,
              5
            ]
          ]
        ],
        "expected": [
          [
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
              5
            ]
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2907": {
    "functionNames": [
      "iterate_nonzero_count"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              -2,
              0,
              5
            ],
            [
              3,
              3,
              1
            ]
          ]
        ],
        "expected": [
          3,
          2,
          3
        ]
      },
      {
        "args": [
          [
            [
              3,
              3,
              1
            ],
            [
              1,
              2,
              3
            ]
          ]
        ],
        "expected": [
          3,
          3
        ]
      },
      {
        "args": [
          [
            [
              -2,
              0,
              5
            ]
          ]
        ],
        "expected": [
          2
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While"
      },
      {
        "nodeType": "Try"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ]
  },
  "2908": {
    "functionNames": [
      "managed_double"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 10
      },
      {
        "args": [
          -4
        ],
        "expected": -8
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2909": {
    "functionNames": [
      "managed_triple"
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
          -4
        ],
        "expected": -12
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2910": {
    "functionNames": [
      "managed_square"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 25
      },
      {
        "args": [
          -4
        ],
        "expected": 16
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2911": {
    "functionNames": [
      "managed_cube"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 125
      },
      {
        "args": [
          -4
        ],
        "expected": -64
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2912": {
    "functionNames": [
      "managed_increment"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 6
      },
      {
        "args": [
          -4
        ],
        "expected": -3
      },
      {
        "args": [
          0
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2913": {
    "functionNames": [
      "managed_decrement"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 4
      },
      {
        "args": [
          -4
        ],
        "expected": -5
      },
      {
        "args": [
          0
        ],
        "expected": -1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2914": {
    "functionNames": [
      "managed_negate"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": -5
      },
      {
        "args": [
          -4
        ],
        "expected": 4
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2915": {
    "functionNames": [
      "managed_absolute"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 4
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2916": {
    "functionNames": [
      "managed_half"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 2.5
      },
      {
        "args": [
          -4
        ],
        "expected": -2
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2917": {
    "functionNames": [
      "managed_remainder_three"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 2
      },
      {
        "args": [
          -4
        ],
        "expected": 2
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2918": {
    "functionNames": [
      "managed_last_digit"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 6
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2919": {
    "functionNames": [
      "managed_distance_ten"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 14
      },
      {
        "args": [
          0
        ],
        "expected": 10
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2920": {
    "functionNames": [
      "managed_clamp_zero"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 0
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2921": {
    "functionNames": [
      "managed_is_even"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": false
      },
      {
        "args": [
          -4
        ],
        "expected": true
      },
      {
        "args": [
          0
        ],
        "expected": true
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2922": {
    "functionNames": [
      "managed_is_positive"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": true
      },
      {
        "args": [
          -4
        ],
        "expected": false
      },
      {
        "args": [
          0
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2923": {
    "functionNames": [
      "managed_sign_label"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": "positive"
      },
      {
        "args": [
          -4
        ],
        "expected": "negative"
      },
      {
        "args": [
          0
        ],
        "expected": "zero"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2924": {
    "functionNames": [
      "managed_digit_count"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 1
      },
      {
        "args": [
          -4
        ],
        "expected": 1
      },
      {
        "args": [
          0
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2925": {
    "functionNames": [
      "managed_digit_sum"
    ],
    "tests": [
      {
        "args": [
          52
        ],
        "expected": 7
      },
      {
        "args": [
          -407
        ],
        "expected": 11
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2926": {
    "functionNames": [
      "managed_triangular"
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
          -4
        ],
        "expected": 10
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2927": {
    "functionNames": [
      "managed_within_ten"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": true
      },
      {
        "args": [
          -14
        ],
        "expected": false
      },
      {
        "args": [
          10
        ],
        "expected": true
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2928": {
    "functionNames": [
      "managed_uppercase"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "PYTHON"
      },
      {
        "args": [
          "level"
        ],
        "expected": "LEVEL"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "A B C"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2929": {
    "functionNames": [
      "managed_lowercase"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "a b c"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2930": {
    "functionNames": [
      "managed_reverse_text"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "nohtyP"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "c b a"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2931": {
    "functionNames": [
      "managed_text_length"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": 6
      },
      {
        "args": [
          "level"
        ],
        "expected": 5
      },
      {
        "args": [
          "a b c"
        ],
        "expected": 5
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2932": {
    "functionNames": [
      "managed_first_character"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "P"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      },
      {
        "args": [
          "z"
        ],
        "expected": "z"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2933": {
    "functionNames": [
      "managed_last_character"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "n"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      },
      {
        "args": [
          "z"
        ],
        "expected": "z"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2934": {
    "functionNames": [
      "managed_vowel_count"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": 1
      },
      {
        "args": [
          "level"
        ],
        "expected": 2
      },
      {
        "args": [
          "a b c"
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2935": {
    "functionNames": [
      "managed_word_count"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": 1
      },
      {
        "args": [
          "level"
        ],
        "expected": 1
      },
      {
        "args": [
          "a b c"
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2936": {
    "functionNames": [
      "managed_remove_spaces"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "Python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "abc"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2937": {
    "functionNames": [
      "managed_hyphenate"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "Python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "a-b-c"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2938": {
    "functionNames": [
      "managed_title_words"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "Python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "Level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "A B C"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2939": {
    "functionNames": [
      "managed_palindrome"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": false
      },
      {
        "args": [
          "level"
        ],
        "expected": true
      },
      {
        "args": [
          "a b c"
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2940": {
    "functionNames": [
      "managed_digit_characters"
    ],
    "tests": [
      {
        "args": [
          "a1b2"
        ],
        "expected": 2
      },
      {
        "args": [
          "2026"
        ],
        "expected": 4
      },
      {
        "args": [
          "none"
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2941": {
    "functionNames": [
      "managed_initials"
    ],
    "tests": [
      {
        "args": [
          "python code"
        ],
        "expected": "PC"
      },
      {
        "args": [
          "Ada Lovelace"
        ],
        "expected": "AL"
      },
      {
        "args": [
          "solo"
        ],
        "expected": "S"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2942": {
    "functionNames": [
      "managed_bracket_text"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "[Python]"
      },
      {
        "args": [
          "level"
        ],
        "expected": "[level]"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "[a b c]"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2943": {
    "functionNames": [
      "managed_sum_items"
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
            0,
            5
          ]
        ],
        "expected": 3
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 7
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2944": {
    "functionNames": [
      "managed_maximum_item"
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
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 5
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2945": {
    "functionNames": [
      "managed_minimum_item"
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
        "expected": 1
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": -2
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2946": {
    "functionNames": [
      "managed_reverse_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          5,
          0,
          -2
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          1,
          3,
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2947": {
    "functionNames": [
      "managed_sort_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          0,
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          1,
          3,
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2948": {
    "functionNames": [
      "managed_unique_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          0,
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2949": {
    "functionNames": [
      "managed_even_items"
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
          2
        ]
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          0
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2950": {
    "functionNames": [
      "managed_odd_items"
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
          3
        ]
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": [
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          3,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2951": {
    "functionNames": [
      "managed_positive_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          3,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2952": {
    "functionNames": [
      "managed_square_items"
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
            0,
            5
          ]
        ],
        "expected": [
          4,
          0,
          25
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          9,
          9,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2953": {
    "functionNames": [
      "managed_item_count"
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
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 3
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2954": {
    "functionNames": [
      "managed_average_items"
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
        "expected": 2
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 1
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 2.3333333333333335
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2955": {
    "functionNames": [
      "managed_running_total"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          -2,
          3
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          6,
          7
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2956": {
    "functionNames": [
      "managed_index_pairs"
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
          ]
        ]
      },
      {
        "args": [
          [
            -2,
            0,
            5
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
            5
          ]
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          [
            0,
            3
          ],
          [
            1,
            3
          ],
          [
            2,
            1
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2957": {
    "functionNames": [
      "managed_nonzero_count"
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
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 2
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "2958": {
    "functionNames": [
      "dataclass_double"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 10
      },
      {
        "args": [
          -4
        ],
        "expected": -8
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2959": {
    "functionNames": [
      "dataclass_triple"
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
          -4
        ],
        "expected": -12
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2960": {
    "functionNames": [
      "dataclass_square"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 25
      },
      {
        "args": [
          -4
        ],
        "expected": 16
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2961": {
    "functionNames": [
      "dataclass_cube"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 125
      },
      {
        "args": [
          -4
        ],
        "expected": -64
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2962": {
    "functionNames": [
      "dataclass_increment"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 6
      },
      {
        "args": [
          -4
        ],
        "expected": -3
      },
      {
        "args": [
          0
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2963": {
    "functionNames": [
      "dataclass_decrement"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 4
      },
      {
        "args": [
          -4
        ],
        "expected": -5
      },
      {
        "args": [
          0
        ],
        "expected": -1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2964": {
    "functionNames": [
      "dataclass_negate"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": -5
      },
      {
        "args": [
          -4
        ],
        "expected": 4
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2965": {
    "functionNames": [
      "dataclass_absolute"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 4
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2966": {
    "functionNames": [
      "dataclass_half"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 2.5
      },
      {
        "args": [
          -4
        ],
        "expected": -2
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2967": {
    "functionNames": [
      "dataclass_remainder_three"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 2
      },
      {
        "args": [
          -4
        ],
        "expected": 2
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2968": {
    "functionNames": [
      "dataclass_last_digit"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 6
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2969": {
    "functionNames": [
      "dataclass_distance_ten"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 14
      },
      {
        "args": [
          0
        ],
        "expected": 10
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2970": {
    "functionNames": [
      "dataclass_clamp_zero"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 0
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2971": {
    "functionNames": [
      "dataclass_is_even"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": false
      },
      {
        "args": [
          -4
        ],
        "expected": true
      },
      {
        "args": [
          0
        ],
        "expected": true
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2972": {
    "functionNames": [
      "dataclass_is_positive"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": true
      },
      {
        "args": [
          -4
        ],
        "expected": false
      },
      {
        "args": [
          0
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2973": {
    "functionNames": [
      "dataclass_sign_label"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": "positive"
      },
      {
        "args": [
          -4
        ],
        "expected": "negative"
      },
      {
        "args": [
          0
        ],
        "expected": "zero"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2974": {
    "functionNames": [
      "dataclass_digit_count"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 1
      },
      {
        "args": [
          -4
        ],
        "expected": 1
      },
      {
        "args": [
          0
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2975": {
    "functionNames": [
      "dataclass_digit_sum"
    ],
    "tests": [
      {
        "args": [
          52
        ],
        "expected": 7
      },
      {
        "args": [
          -407
        ],
        "expected": 11
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2976": {
    "functionNames": [
      "dataclass_triangular"
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
          -4
        ],
        "expected": 10
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2977": {
    "functionNames": [
      "dataclass_within_ten"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": true
      },
      {
        "args": [
          -14
        ],
        "expected": false
      },
      {
        "args": [
          10
        ],
        "expected": true
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2978": {
    "functionNames": [
      "dataclass_uppercase"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "PYTHON"
      },
      {
        "args": [
          "level"
        ],
        "expected": "LEVEL"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "A B C"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2979": {
    "functionNames": [
      "dataclass_lowercase"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "a b c"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2980": {
    "functionNames": [
      "dataclass_reverse_text"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "nohtyP"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "c b a"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2981": {
    "functionNames": [
      "dataclass_text_length"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": 6
      },
      {
        "args": [
          "level"
        ],
        "expected": 5
      },
      {
        "args": [
          "a b c"
        ],
        "expected": 5
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2982": {
    "functionNames": [
      "dataclass_first_character"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "P"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      },
      {
        "args": [
          "z"
        ],
        "expected": "z"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2983": {
    "functionNames": [
      "dataclass_last_character"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "n"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      },
      {
        "args": [
          "z"
        ],
        "expected": "z"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2984": {
    "functionNames": [
      "dataclass_vowel_count"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": 1
      },
      {
        "args": [
          "level"
        ],
        "expected": 2
      },
      {
        "args": [
          "a b c"
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2985": {
    "functionNames": [
      "dataclass_word_count"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": 1
      },
      {
        "args": [
          "level"
        ],
        "expected": 1
      },
      {
        "args": [
          "a b c"
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2986": {
    "functionNames": [
      "dataclass_remove_spaces"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "Python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "abc"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2987": {
    "functionNames": [
      "dataclass_hyphenate"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "Python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "a-b-c"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2988": {
    "functionNames": [
      "dataclass_title_words"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "Python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "Level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "A B C"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2989": {
    "functionNames": [
      "dataclass_palindrome"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": false
      },
      {
        "args": [
          "level"
        ],
        "expected": true
      },
      {
        "args": [
          "a b c"
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2990": {
    "functionNames": [
      "dataclass_digit_characters"
    ],
    "tests": [
      {
        "args": [
          "a1b2"
        ],
        "expected": 2
      },
      {
        "args": [
          "2026"
        ],
        "expected": 4
      },
      {
        "args": [
          "none"
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2991": {
    "functionNames": [
      "dataclass_initials"
    ],
    "tests": [
      {
        "args": [
          "python code"
        ],
        "expected": "PC"
      },
      {
        "args": [
          "Ada Lovelace"
        ],
        "expected": "AL"
      },
      {
        "args": [
          "solo"
        ],
        "expected": "S"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2992": {
    "functionNames": [
      "dataclass_bracket_text"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "[Python]"
      },
      {
        "args": [
          "level"
        ],
        "expected": "[level]"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "[a b c]"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2993": {
    "functionNames": [
      "dataclass_sum_items"
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
            0,
            5
          ]
        ],
        "expected": 3
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 7
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2994": {
    "functionNames": [
      "dataclass_maximum_item"
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
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 5
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2995": {
    "functionNames": [
      "dataclass_minimum_item"
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
        "expected": 1
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": -2
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2996": {
    "functionNames": [
      "dataclass_reverse_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          5,
          0,
          -2
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          1,
          3,
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2997": {
    "functionNames": [
      "dataclass_sort_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          0,
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          1,
          3,
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2998": {
    "functionNames": [
      "dataclass_unique_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          0,
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "2999": {
    "functionNames": [
      "dataclass_even_items"
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
          2
        ]
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          0
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "3000": {
    "functionNames": [
      "dataclass_odd_items"
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
          3
        ]
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": [
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          3,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "3001": {
    "functionNames": [
      "dataclass_positive_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          3,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "3002": {
    "functionNames": [
      "dataclass_square_items"
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
            0,
            5
          ]
        ],
        "expected": [
          4,
          0,
          25
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          9,
          9,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "3003": {
    "functionNames": [
      "dataclass_item_count"
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
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 3
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "3004": {
    "functionNames": [
      "dataclass_average_items"
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
        "expected": 2
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 1
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 2.3333333333333335
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "3005": {
    "functionNames": [
      "dataclass_running_total"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          -2,
          3
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          6,
          7
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "3006": {
    "functionNames": [
      "dataclass_index_pairs"
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
          ]
        ]
      },
      {
        "args": [
          [
            -2,
            0,
            5
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
            5
          ]
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          [
            0,
            3
          ],
          [
            1,
            3
          ],
          [
            2,
            1
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "3007": {
    "functionNames": [
      "dataclass_nonzero_count"
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
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 2
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "calculate"
    ]
  },
  "3008": {
    "functionNames": [
      "magic_string_value"
    ],
    "tests": [
      {
        "args": [
          3
        ],
        "expected": "Value(3)"
      },
      {
        "args": [
          -2
        ],
        "expected": "Value(-2)"
      },
      {
        "args": [
          0
        ],
        "expected": "Value(0)"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__str__"
    ]
  },
  "3009": {
    "functionNames": [
      "magic_string_number"
    ],
    "tests": [
      {
        "args": [
          3
        ],
        "expected": "Number(3)"
      },
      {
        "args": [
          -2
        ],
        "expected": "Number(-2)"
      },
      {
        "args": [
          0
        ],
        "expected": "Number(0)"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__str__"
    ]
  },
  "3010": {
    "functionNames": [
      "magic_string_item"
    ],
    "tests": [
      {
        "args": [
          3
        ],
        "expected": "Item(3)"
      },
      {
        "args": [
          -2
        ],
        "expected": "Item(-2)"
      },
      {
        "args": [
          0
        ],
        "expected": "Item(0)"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__str__"
    ]
  },
  "3011": {
    "functionNames": [
      "magic_string_score"
    ],
    "tests": [
      {
        "args": [
          3
        ],
        "expected": "Score(3)"
      },
      {
        "args": [
          -2
        ],
        "expected": "Score(-2)"
      },
      {
        "args": [
          0
        ],
        "expected": "Score(0)"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__str__"
    ]
  },
  "3012": {
    "functionNames": [
      "magic_string_data"
    ],
    "tests": [
      {
        "args": [
          3
        ],
        "expected": "Data(3)"
      },
      {
        "args": [
          -2
        ],
        "expected": "Data(-2)"
      },
      {
        "args": [
          0
        ],
        "expected": "Data(0)"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__str__"
    ]
  },
  "3013": {
    "functionNames": [
      "magic_representation_point"
    ],
    "tests": [
      {
        "args": [
          3
        ],
        "expected": "Point(value=3)"
      },
      {
        "args": [
          -2
        ],
        "expected": "Point(value=-2)"
      },
      {
        "args": [
          0
        ],
        "expected": "Point(value=0)"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__repr__"
    ]
  },
  "3014": {
    "functionNames": [
      "magic_representation_record"
    ],
    "tests": [
      {
        "args": [
          3
        ],
        "expected": "Record(value=3)"
      },
      {
        "args": [
          -2
        ],
        "expected": "Record(value=-2)"
      },
      {
        "args": [
          0
        ],
        "expected": "Record(value=0)"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__repr__"
    ]
  },
  "3015": {
    "functionNames": [
      "magic_representation_token"
    ],
    "tests": [
      {
        "args": [
          3
        ],
        "expected": "Token(value=3)"
      },
      {
        "args": [
          -2
        ],
        "expected": "Token(value=-2)"
      },
      {
        "args": [
          0
        ],
        "expected": "Token(value=0)"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__repr__"
    ]
  },
  "3016": {
    "functionNames": [
      "magic_representation_entry"
    ],
    "tests": [
      {
        "args": [
          3
        ],
        "expected": "Entry(value=3)"
      },
      {
        "args": [
          -2
        ],
        "expected": "Entry(value=-2)"
      },
      {
        "args": [
          0
        ],
        "expected": "Entry(value=0)"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__repr__"
    ]
  },
  "3017": {
    "functionNames": [
      "magic_representation_packet"
    ],
    "tests": [
      {
        "args": [
          3
        ],
        "expected": "Packet(value=3)"
      },
      {
        "args": [
          -2
        ],
        "expected": "Packet(value=-2)"
      },
      {
        "args": [
          0
        ],
        "expected": "Packet(value=0)"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__repr__"
    ]
  },
  "3018": {
    "functionNames": [
      "magic_length_characters"
    ],
    "tests": [
      {
        "args": [
          "python"
        ],
        "expected": 6
      },
      {
        "args": [
          ""
        ],
        "expected": 0
      },
      {
        "args": [
          "go"
        ],
        "expected": 2
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__len__"
    ]
  },
  "3019": {
    "functionNames": [
      "magic_length_items"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ]
        ],
        "expected": 2
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
            3
          ]
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__len__"
    ]
  },
  "3020": {
    "functionNames": [
      "magic_length_unique"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            1,
            2
          ]
        ],
        "expected": 2
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
            3,
            3
          ]
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__len__"
    ]
  },
  "3021": {
    "functionNames": [
      "magic_length_truthy"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1,
            2
          ]
        ],
        "expected": 2
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
            "",
            "x"
          ]
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__len__"
    ]
  },
  "3022": {
    "functionNames": [
      "magic_length_words"
    ],
    "tests": [
      {
        "args": [
          "one two"
        ],
        "expected": 2
      },
      {
        "args": [
          ""
        ],
        "expected": 0
      },
      {
        "args": [
          "three"
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__len__"
    ]
  },
  "3023": {
    "functionNames": [
      "magic_equality_exact"
    ],
    "tests": [
      {
        "args": [
          2,
          2
        ],
        "expected": true
      },
      {
        "args": [
          2,
          3
        ],
        "expected": false
      },
      {
        "args": [
          "a",
          "a"
        ],
        "expected": true
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__eq__"
    ]
  },
  "3024": {
    "functionNames": [
      "magic_equality_absolute"
    ],
    "tests": [
      {
        "args": [
          -2,
          2
        ],
        "expected": true
      },
      {
        "args": [
          3,
          -4
        ],
        "expected": false
      },
      {
        "args": [
          0,
          0
        ],
        "expected": true
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__eq__"
    ]
  },
  "3025": {
    "functionNames": [
      "magic_equality_lowercase"
    ],
    "tests": [
      {
        "args": [
          "Python",
          "python"
        ],
        "expected": true
      },
      {
        "args": [
          "A",
          "b"
        ],
        "expected": false
      },
      {
        "args": [
          "x",
          "X"
        ],
        "expected": true
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__eq__"
    ]
  },
  "3026": {
    "functionNames": [
      "magic_equality_length"
    ],
    "tests": [
      {
        "args": [
          "ab",
          "cd"
        ],
        "expected": true
      },
      {
        "args": [
          "a",
          "xyz"
        ],
        "expected": false
      },
      {
        "args": [
          [],
          []
        ],
        "expected": true
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__eq__"
    ]
  },
  "3027": {
    "functionNames": [
      "magic_equality_sorted"
    ],
    "tests": [
      {
        "args": [
          [
            2,
            1
          ],
          [
            1,
            2
          ]
        ],
        "expected": true
      },
      {
        "args": [
          [
            1
          ],
          [
            2
          ]
        ],
        "expected": false
      },
      {
        "args": [
          [
            3,
            3
          ],
          [
            3,
            3
          ]
        ],
        "expected": true
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__eq__"
    ]
  },
  "3028": {
    "functionNames": [
      "magic_ordering_numeric"
    ],
    "tests": [
      {
        "args": [
          2,
          3
        ],
        "expected": true
      },
      {
        "args": [
          4,
          1
        ],
        "expected": false
      },
      {
        "args": [
          0,
          0
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__lt__"
    ]
  },
  "3029": {
    "functionNames": [
      "magic_ordering_absolute"
    ],
    "tests": [
      {
        "args": [
          -2,
          3
        ],
        "expected": true
      },
      {
        "args": [
          4,
          -1
        ],
        "expected": false
      },
      {
        "args": [
          0,
          0
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__lt__"
    ]
  },
  "3030": {
    "functionNames": [
      "magic_ordering_text_length"
    ],
    "tests": [
      {
        "args": [
          "a",
          "abc"
        ],
        "expected": true
      },
      {
        "args": [
          "long",
          "x"
        ],
        "expected": false
      },
      {
        "args": [
          "ab",
          "cd"
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__lt__"
    ]
  },
  "3031": {
    "functionNames": [
      "magic_ordering_list_sum"
    ],
    "tests": [
      {
        "args": [
          [
            1
          ],
          [
            2
          ]
        ],
        "expected": true
      },
      {
        "args": [
          [
            5
          ],
          [
            1,
            2
          ]
        ],
        "expected": false
      },
      {
        "args": [
          [
            0
          ],
          [
            0
          ]
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__lt__"
    ]
  },
  "3032": {
    "functionNames": [
      "magic_ordering_lowercase"
    ],
    "tests": [
      {
        "args": [
          "a",
          "B"
        ],
        "expected": true
      },
      {
        "args": [
          "z",
          "a"
        ],
        "expected": false
      },
      {
        "args": [
          "x",
          "X"
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__lt__"
    ]
  },
  "3033": {
    "functionNames": [
      "magic_addition_numbers"
    ],
    "tests": [
      {
        "args": [
          2,
          3
        ],
        "expected": 5
      },
      {
        "args": [
          -1,
          4
        ],
        "expected": 3
      },
      {
        "args": [
          0,
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__add__"
    ]
  },
  "3034": {
    "functionNames": [
      "magic_addition_text"
    ],
    "tests": [
      {
        "args": [
          "py",
          "thon"
        ],
        "expected": "python"
      },
      {
        "args": [
          "a",
          ""
        ],
        "expected": "a"
      },
      {
        "args": [
          "x",
          "y"
        ],
        "expected": "xy"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__add__"
    ]
  },
  "3035": {
    "functionNames": [
      "magic_addition_lists"
    ],
    "tests": [
      {
        "args": [
          [
            1
          ],
          [
            2
          ]
        ],
        "expected": [
          1,
          2
        ]
      },
      {
        "args": [
          [
            1,
            2
          ],
          []
        ],
        "expected": [
          1,
          2
        ]
      },
      {
        "args": [
          [],
          [
            3
          ]
        ],
        "expected": [
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__add__"
    ]
  },
  "3036": {
    "functionNames": [
      "magic_addition_offset"
    ],
    "tests": [
      {
        "args": [
          2,
          3
        ],
        "expected": 6
      },
      {
        "args": [
          -1,
          4
        ],
        "expected": 4
      },
      {
        "args": [
          0,
          0
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__add__"
    ]
  },
  "3037": {
    "functionNames": [
      "magic_addition_absolute"
    ],
    "tests": [
      {
        "args": [
          -2,
          3
        ],
        "expected": 5
      },
      {
        "args": [
          -1,
          -4
        ],
        "expected": 5
      },
      {
        "args": [
          0,
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__add__"
    ]
  },
  "3038": {
    "functionNames": [
      "magic_subtraction_numbers"
    ],
    "tests": [
      {
        "args": [
          5,
          2
        ],
        "expected": 3
      },
      {
        "args": [
          -1,
          4
        ],
        "expected": -5
      },
      {
        "args": [
          0,
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__sub__"
    ]
  },
  "3039": {
    "functionNames": [
      "magic_subtraction_absolute"
    ],
    "tests": [
      {
        "args": [
          -5,
          2
        ],
        "expected": 3
      },
      {
        "args": [
          -1,
          -4
        ],
        "expected": -3
      },
      {
        "args": [
          0,
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__sub__"
    ]
  },
  "3040": {
    "functionNames": [
      "magic_subtraction_distance"
    ],
    "tests": [
      {
        "args": [
          5,
          2
        ],
        "expected": 3
      },
      {
        "args": [
          -1,
          4
        ],
        "expected": 5
      },
      {
        "args": [
          0,
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__sub__"
    ]
  },
  "3041": {
    "functionNames": [
      "magic_subtraction_floored"
    ],
    "tests": [
      {
        "args": [
          5,
          2
        ],
        "expected": 3
      },
      {
        "args": [
          1,
          4
        ],
        "expected": 0
      },
      {
        "args": [
          0,
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__sub__"
    ]
  },
  "3042": {
    "functionNames": [
      "magic_subtraction_doubled"
    ],
    "tests": [
      {
        "args": [
          5,
          2
        ],
        "expected": 1
      },
      {
        "args": [
          -1,
          4
        ],
        "expected": -9
      },
      {
        "args": [
          0,
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__sub__"
    ]
  },
  "3043": {
    "functionNames": [
      "magic_multiplication_numbers"
    ],
    "tests": [
      {
        "args": [
          3,
          2
        ],
        "expected": 6
      },
      {
        "args": [
          -2,
          4
        ],
        "expected": -8
      },
      {
        "args": [
          0,
          5
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__mul__"
    ]
  },
  "3044": {
    "functionNames": [
      "magic_multiplication_text"
    ],
    "tests": [
      {
        "args": [
          "ab",
          2
        ],
        "expected": "abab"
      },
      {
        "args": [
          "x",
          0
        ],
        "expected": ""
      },
      {
        "args": [
          "z",
          3
        ],
        "expected": "zzz"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__mul__"
    ]
  },
  "3045": {
    "functionNames": [
      "magic_multiplication_lists"
    ],
    "tests": [
      {
        "args": [
          [
            1
          ],
          2
        ],
        "expected": [
          1,
          1
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
      },
      {
        "args": [
          [
            3
          ],
          3
        ],
        "expected": [
          3,
          3,
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__mul__"
    ]
  },
  "3046": {
    "functionNames": [
      "magic_multiplication_absolute"
    ],
    "tests": [
      {
        "args": [
          -3,
          2
        ],
        "expected": 6
      },
      {
        "args": [
          -2,
          -4
        ],
        "expected": 8
      },
      {
        "args": [
          0,
          5
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__mul__"
    ]
  },
  "3047": {
    "functionNames": [
      "magic_multiplication_offset"
    ],
    "tests": [
      {
        "args": [
          3,
          2
        ],
        "expected": 7
      },
      {
        "args": [
          -2,
          4
        ],
        "expected": -7
      },
      {
        "args": [
          0,
          5
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__mul__"
    ]
  },
  "3048": {
    "functionNames": [
      "magic_contains_direct"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ],
          2
        ],
        "expected": true
      },
      {
        "args": [
          [
            1
          ],
          3
        ],
        "expected": false
      },
      {
        "args": [
          "abc",
          "b"
        ],
        "expected": true
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__contains__"
    ]
  },
  "3049": {
    "functionNames": [
      "magic_contains_casefold"
    ],
    "tests": [
      {
        "args": [
          "Python",
          "PY"
        ],
        "expected": true
      },
      {
        "args": [
          "abc",
          "Z"
        ],
        "expected": false
      },
      {
        "args": [
          "Test",
          "test"
        ],
        "expected": true
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__contains__"
    ]
  },
  "3050": {
    "functionNames": [
      "magic_contains_keys"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1
          },
          "a"
        ],
        "expected": true
      },
      {
        "args": [
          {
            "a": 1
          },
          "b"
        ],
        "expected": false
      },
      {
        "args": [
          {},
          "x"
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__contains__"
    ]
  },
  "3051": {
    "functionNames": [
      "magic_contains_absolute"
    ],
    "tests": [
      {
        "args": [
          [
            -2,
            3
          ],
          2
        ],
        "expected": true
      },
      {
        "args": [
          [
            1
          ],
          -3
        ],
        "expected": false
      },
      {
        "args": [
          [
            0
          ],
          0
        ],
        "expected": true
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__contains__"
    ]
  },
  "3052": {
    "functionNames": [
      "magic_contains_substring"
    ],
    "tests": [
      {
        "args": [
          [
            "red",
            "blue"
          ],
          "blue"
        ],
        "expected": true
      },
      {
        "args": [
          [
            "a"
          ],
          "z"
        ],
        "expected": false
      },
      {
        "args": [
          [
            "python",
            "code"
          ],
          "on"
        ],
        "expected": true
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__contains__"
    ]
  },
  "3053": {
    "functionNames": [
      "magic_truth_direct"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": false
      },
      {
        "args": [
          1
        ],
        "expected": true
      },
      {
        "args": [
          ""
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__bool__"
    ]
  },
  "3054": {
    "functionNames": [
      "magic_truth_any_items"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1
          ]
        ],
        "expected": true
      },
      {
        "args": [
          [
            0,
            0
          ]
        ],
        "expected": false
      },
      {
        "args": [
          []
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__bool__"
    ]
  },
  "3055": {
    "functionNames": [
      "magic_truth_positive"
    ],
    "tests": [
      {
        "args": [
          -1
        ],
        "expected": false
      },
      {
        "args": [
          2
        ],
        "expected": true
      },
      {
        "args": [
          0
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__bool__"
    ]
  },
  "3056": {
    "functionNames": [
      "magic_truth_longer_two"
    ],
    "tests": [
      {
        "args": [
          "abc"
        ],
        "expected": true
      },
      {
        "args": [
          "a"
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
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__bool__"
    ]
  },
  "3057": {
    "functionNames": [
      "magic_truth_all_items"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ]
        ],
        "expected": true
      },
      {
        "args": [
          [
            1,
            0
          ]
        ],
        "expected": false
      },
      {
        "args": [
          []
        ],
        "expected": true
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__bool__"
    ]
  },
  "3058": {
    "functionNames": [
      "and_mask_1_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          5
        ],
        "expected": 1
      },
      {
        "args": [
          42
        ],
        "expected": 0
      }
    ],
    "requiredAstOperators": [
      "BitAnd"
    ]
  },
  "3059": {
    "functionNames": [
      "and_mask_3_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          5
        ],
        "expected": 1
      },
      {
        "args": [
          42
        ],
        "expected": 2
      }
    ],
    "requiredAstOperators": [
      "BitAnd"
    ]
  },
  "3060": {
    "functionNames": [
      "and_mask_15_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          42
        ],
        "expected": 10
      }
    ],
    "requiredAstOperators": [
      "BitAnd"
    ]
  },
  "3061": {
    "functionNames": [
      "and_mask_85_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          42
        ],
        "expected": 0
      }
    ],
    "requiredAstOperators": [
      "BitAnd"
    ]
  },
  "3062": {
    "functionNames": [
      "and_mask_170_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          5
        ],
        "expected": 0
      },
      {
        "args": [
          42
        ],
        "expected": 42
      }
    ],
    "requiredAstOperators": [
      "BitAnd"
    ]
  },
  "3063": {
    "functionNames": [
      "or_mask_1_bitwise"
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
          5
        ],
        "expected": 5
      },
      {
        "args": [
          42
        ],
        "expected": 43
      }
    ],
    "requiredAstOperators": [
      "BitOr"
    ]
  },
  "3064": {
    "functionNames": [
      "or_mask_3_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 3
      },
      {
        "args": [
          5
        ],
        "expected": 7
      },
      {
        "args": [
          42
        ],
        "expected": 43
      }
    ],
    "requiredAstOperators": [
      "BitOr"
    ]
  },
  "3065": {
    "functionNames": [
      "or_mask_15_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 15
      },
      {
        "args": [
          5
        ],
        "expected": 15
      },
      {
        "args": [
          42
        ],
        "expected": 47
      }
    ],
    "requiredAstOperators": [
      "BitOr"
    ]
  },
  "3066": {
    "functionNames": [
      "or_mask_85_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 85
      },
      {
        "args": [
          5
        ],
        "expected": 85
      },
      {
        "args": [
          42
        ],
        "expected": 127
      }
    ],
    "requiredAstOperators": [
      "BitOr"
    ]
  },
  "3067": {
    "functionNames": [
      "or_mask_170_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 170
      },
      {
        "args": [
          5
        ],
        "expected": 175
      },
      {
        "args": [
          42
        ],
        "expected": 170
      }
    ],
    "requiredAstOperators": [
      "BitOr"
    ]
  },
  "3068": {
    "functionNames": [
      "xor_mask_1_bitwise"
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
          5
        ],
        "expected": 4
      },
      {
        "args": [
          42
        ],
        "expected": 43
      }
    ],
    "requiredAstOperators": [
      "BitXor"
    ]
  },
  "3069": {
    "functionNames": [
      "xor_mask_3_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 3
      },
      {
        "args": [
          5
        ],
        "expected": 6
      },
      {
        "args": [
          42
        ],
        "expected": 41
      }
    ],
    "requiredAstOperators": [
      "BitXor"
    ]
  },
  "3070": {
    "functionNames": [
      "xor_mask_15_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 15
      },
      {
        "args": [
          5
        ],
        "expected": 10
      },
      {
        "args": [
          42
        ],
        "expected": 37
      }
    ],
    "requiredAstOperators": [
      "BitXor"
    ]
  },
  "3071": {
    "functionNames": [
      "xor_mask_85_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 85
      },
      {
        "args": [
          5
        ],
        "expected": 80
      },
      {
        "args": [
          42
        ],
        "expected": 127
      }
    ],
    "requiredAstOperators": [
      "BitXor"
    ]
  },
  "3072": {
    "functionNames": [
      "xor_mask_170_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 170
      },
      {
        "args": [
          5
        ],
        "expected": 175
      },
      {
        "args": [
          42
        ],
        "expected": 128
      }
    ],
    "requiredAstOperators": [
      "BitXor"
    ]
  },
  "3073": {
    "functionNames": [
      "left_shift_1_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          5
        ],
        "expected": 10
      },
      {
        "args": [
          42
        ],
        "expected": 84
      }
    ],
    "requiredAstOperators": [
      "LShift"
    ]
  },
  "3074": {
    "functionNames": [
      "left_shift_2_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          5
        ],
        "expected": 20
      },
      {
        "args": [
          42
        ],
        "expected": 168
      }
    ],
    "requiredAstOperators": [
      "LShift"
    ]
  },
  "3075": {
    "functionNames": [
      "left_shift_3_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          5
        ],
        "expected": 40
      },
      {
        "args": [
          42
        ],
        "expected": 336
      }
    ],
    "requiredAstOperators": [
      "LShift"
    ]
  },
  "3076": {
    "functionNames": [
      "left_shift_4_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          5
        ],
        "expected": 80
      },
      {
        "args": [
          42
        ],
        "expected": 672
      }
    ],
    "requiredAstOperators": [
      "LShift"
    ]
  },
  "3077": {
    "functionNames": [
      "left_shift_5_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          5
        ],
        "expected": 160
      },
      {
        "args": [
          42
        ],
        "expected": 1344
      }
    ],
    "requiredAstOperators": [
      "LShift"
    ]
  },
  "3078": {
    "functionNames": [
      "right_shift_1_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          5
        ],
        "expected": 2
      },
      {
        "args": [
          42
        ],
        "expected": 21
      }
    ],
    "requiredAstOperators": [
      "RShift"
    ]
  },
  "3079": {
    "functionNames": [
      "right_shift_2_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          5
        ],
        "expected": 1
      },
      {
        "args": [
          42
        ],
        "expected": 10
      }
    ],
    "requiredAstOperators": [
      "RShift"
    ]
  },
  "3080": {
    "functionNames": [
      "right_shift_3_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          5
        ],
        "expected": 0
      },
      {
        "args": [
          42
        ],
        "expected": 5
      }
    ],
    "requiredAstOperators": [
      "RShift"
    ]
  },
  "3081": {
    "functionNames": [
      "right_shift_4_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          5
        ],
        "expected": 0
      },
      {
        "args": [
          42
        ],
        "expected": 2
      }
    ],
    "requiredAstOperators": [
      "RShift"
    ]
  },
  "3082": {
    "functionNames": [
      "right_shift_5_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          5
        ],
        "expected": 0
      },
      {
        "args": [
          42
        ],
        "expected": 1
      }
    ],
    "requiredAstOperators": [
      "RShift"
    ]
  },
  "3083": {
    "functionNames": [
      "set_bit_0_bitwise"
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
          5
        ],
        "expected": 5
      },
      {
        "args": [
          42
        ],
        "expected": 43
      }
    ],
    "requiredAstOperators": [
      "BitOr"
    ]
  },
  "3084": {
    "functionNames": [
      "set_bit_1_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 2
      },
      {
        "args": [
          5
        ],
        "expected": 7
      },
      {
        "args": [
          42
        ],
        "expected": 42
      }
    ],
    "requiredAstOperators": [
      "BitOr"
    ]
  },
  "3085": {
    "functionNames": [
      "set_bit_2_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 4
      },
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          42
        ],
        "expected": 46
      }
    ],
    "requiredAstOperators": [
      "BitOr"
    ]
  },
  "3086": {
    "functionNames": [
      "set_bit_3_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 8
      },
      {
        "args": [
          5
        ],
        "expected": 13
      },
      {
        "args": [
          42
        ],
        "expected": 42
      }
    ],
    "requiredAstOperators": [
      "BitOr"
    ]
  },
  "3087": {
    "functionNames": [
      "set_bit_4_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 16
      },
      {
        "args": [
          5
        ],
        "expected": 21
      },
      {
        "args": [
          42
        ],
        "expected": 58
      }
    ],
    "requiredAstOperators": [
      "BitOr"
    ]
  },
  "3088": {
    "functionNames": [
      "clear_bit_0_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          5
        ],
        "expected": 4
      },
      {
        "args": [
          42
        ],
        "expected": 42
      }
    ],
    "requiredAstOperators": [
      "BitAnd"
    ]
  },
  "3089": {
    "functionNames": [
      "clear_bit_1_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          42
        ],
        "expected": 40
      }
    ],
    "requiredAstOperators": [
      "BitAnd"
    ]
  },
  "3090": {
    "functionNames": [
      "clear_bit_2_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          5
        ],
        "expected": 1
      },
      {
        "args": [
          42
        ],
        "expected": 42
      }
    ],
    "requiredAstOperators": [
      "BitAnd"
    ]
  },
  "3091": {
    "functionNames": [
      "clear_bit_3_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          42
        ],
        "expected": 34
      }
    ],
    "requiredAstOperators": [
      "BitAnd"
    ]
  },
  "3092": {
    "functionNames": [
      "clear_bit_4_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          42
        ],
        "expected": 42
      }
    ],
    "requiredAstOperators": [
      "BitAnd"
    ]
  },
  "3093": {
    "functionNames": [
      "toggle_bit_0_bitwise"
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
          5
        ],
        "expected": 4
      },
      {
        "args": [
          42
        ],
        "expected": 43
      }
    ],
    "requiredAstOperators": [
      "BitXor"
    ]
  },
  "3094": {
    "functionNames": [
      "toggle_bit_1_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 2
      },
      {
        "args": [
          5
        ],
        "expected": 7
      },
      {
        "args": [
          42
        ],
        "expected": 40
      }
    ],
    "requiredAstOperators": [
      "BitXor"
    ]
  },
  "3095": {
    "functionNames": [
      "toggle_bit_2_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 4
      },
      {
        "args": [
          5
        ],
        "expected": 1
      },
      {
        "args": [
          42
        ],
        "expected": 46
      }
    ],
    "requiredAstOperators": [
      "BitXor"
    ]
  },
  "3096": {
    "functionNames": [
      "toggle_bit_3_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 8
      },
      {
        "args": [
          5
        ],
        "expected": 13
      },
      {
        "args": [
          42
        ],
        "expected": 34
      }
    ],
    "requiredAstOperators": [
      "BitXor"
    ]
  },
  "3097": {
    "functionNames": [
      "toggle_bit_4_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 16
      },
      {
        "args": [
          5
        ],
        "expected": 21
      },
      {
        "args": [
          42
        ],
        "expected": 58
      }
    ],
    "requiredAstOperators": [
      "BitXor"
    ]
  },
  "3098": {
    "functionNames": [
      "test_bit_0_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": false
      },
      {
        "args": [
          5
        ],
        "expected": true
      },
      {
        "args": [
          42
        ],
        "expected": false
      }
    ],
    "requiredAstOperators": [
      "BitAnd"
    ]
  },
  "3099": {
    "functionNames": [
      "test_bit_1_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": false
      },
      {
        "args": [
          5
        ],
        "expected": false
      },
      {
        "args": [
          42
        ],
        "expected": true
      }
    ],
    "requiredAstOperators": [
      "BitAnd"
    ]
  },
  "3100": {
    "functionNames": [
      "test_bit_2_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": false
      },
      {
        "args": [
          5
        ],
        "expected": true
      },
      {
        "args": [
          42
        ],
        "expected": false
      }
    ],
    "requiredAstOperators": [
      "BitAnd"
    ]
  },
  "3101": {
    "functionNames": [
      "test_bit_3_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": false
      },
      {
        "args": [
          5
        ],
        "expected": false
      },
      {
        "args": [
          42
        ],
        "expected": true
      }
    ],
    "requiredAstOperators": [
      "BitAnd"
    ]
  },
  "3102": {
    "functionNames": [
      "test_bit_4_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": false
      },
      {
        "args": [
          5
        ],
        "expected": false
      },
      {
        "args": [
          42
        ],
        "expected": false
      }
    ],
    "requiredAstOperators": [
      "BitAnd"
    ]
  },
  "3103": {
    "functionNames": [
      "extract_field_0_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          42
        ],
        "expected": 2
      }
    ],
    "requiredAstOperators": [
      "RShift"
    ]
  },
  "3104": {
    "functionNames": [
      "extract_field_1_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          5
        ],
        "expected": 2
      },
      {
        "args": [
          42
        ],
        "expected": 5
      }
    ],
    "requiredAstOperators": [
      "RShift"
    ]
  },
  "3105": {
    "functionNames": [
      "extract_field_2_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          5
        ],
        "expected": 1
      },
      {
        "args": [
          42
        ],
        "expected": 2
      }
    ],
    "requiredAstOperators": [
      "RShift"
    ]
  },
  "3106": {
    "functionNames": [
      "extract_field_3_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          5
        ],
        "expected": 0
      },
      {
        "args": [
          42
        ],
        "expected": 5
      }
    ],
    "requiredAstOperators": [
      "RShift"
    ]
  },
  "3107": {
    "functionNames": [
      "extract_field_4_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          5
        ],
        "expected": 0
      },
      {
        "args": [
          42
        ],
        "expected": 2
      }
    ],
    "requiredAstOperators": [
      "RShift"
    ]
  },
  "3108": {
    "functionNames": [
      "pipeline_double"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 10
      },
      {
        "args": [
          -4
        ],
        "expected": -8
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3109": {
    "functionNames": [
      "pipeline_triple"
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
          -4
        ],
        "expected": -12
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3110": {
    "functionNames": [
      "pipeline_square"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 25
      },
      {
        "args": [
          -4
        ],
        "expected": 16
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3111": {
    "functionNames": [
      "pipeline_cube"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 125
      },
      {
        "args": [
          -4
        ],
        "expected": -64
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3112": {
    "functionNames": [
      "pipeline_increment"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 6
      },
      {
        "args": [
          -4
        ],
        "expected": -3
      },
      {
        "args": [
          0
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3113": {
    "functionNames": [
      "pipeline_decrement"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 4
      },
      {
        "args": [
          -4
        ],
        "expected": -5
      },
      {
        "args": [
          0
        ],
        "expected": -1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3114": {
    "functionNames": [
      "pipeline_negate"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": -5
      },
      {
        "args": [
          -4
        ],
        "expected": 4
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3115": {
    "functionNames": [
      "pipeline_absolute"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 4
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3116": {
    "functionNames": [
      "pipeline_half"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 2.5
      },
      {
        "args": [
          -4
        ],
        "expected": -2
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3117": {
    "functionNames": [
      "pipeline_remainder_three"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 2
      },
      {
        "args": [
          -4
        ],
        "expected": 2
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3118": {
    "functionNames": [
      "pipeline_last_digit"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 6
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3119": {
    "functionNames": [
      "pipeline_distance_ten"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 14
      },
      {
        "args": [
          0
        ],
        "expected": 10
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3120": {
    "functionNames": [
      "pipeline_clamp_zero"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 0
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3121": {
    "functionNames": [
      "pipeline_is_even"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": false
      },
      {
        "args": [
          -4
        ],
        "expected": true
      },
      {
        "args": [
          0
        ],
        "expected": true
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3122": {
    "functionNames": [
      "pipeline_is_positive"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": true
      },
      {
        "args": [
          -4
        ],
        "expected": false
      },
      {
        "args": [
          0
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3123": {
    "functionNames": [
      "pipeline_sign_label"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": "positive"
      },
      {
        "args": [
          -4
        ],
        "expected": "negative"
      },
      {
        "args": [
          0
        ],
        "expected": "zero"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3124": {
    "functionNames": [
      "pipeline_digit_count"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 1
      },
      {
        "args": [
          -4
        ],
        "expected": 1
      },
      {
        "args": [
          0
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3125": {
    "functionNames": [
      "pipeline_digit_sum"
    ],
    "tests": [
      {
        "args": [
          52
        ],
        "expected": 7
      },
      {
        "args": [
          -407
        ],
        "expected": 11
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3126": {
    "functionNames": [
      "pipeline_triangular"
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
          -4
        ],
        "expected": 10
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3127": {
    "functionNames": [
      "pipeline_within_ten"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": true
      },
      {
        "args": [
          -14
        ],
        "expected": false
      },
      {
        "args": [
          10
        ],
        "expected": true
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3128": {
    "functionNames": [
      "pipeline_uppercase"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "PYTHON"
      },
      {
        "args": [
          "level"
        ],
        "expected": "LEVEL"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "A B C"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3129": {
    "functionNames": [
      "pipeline_lowercase"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "a b c"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3130": {
    "functionNames": [
      "pipeline_reverse_text"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "nohtyP"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "c b a"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3131": {
    "functionNames": [
      "pipeline_text_length"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": 6
      },
      {
        "args": [
          "level"
        ],
        "expected": 5
      },
      {
        "args": [
          "a b c"
        ],
        "expected": 5
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3132": {
    "functionNames": [
      "pipeline_first_character"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "P"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      },
      {
        "args": [
          "z"
        ],
        "expected": "z"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3133": {
    "functionNames": [
      "pipeline_last_character"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "n"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      },
      {
        "args": [
          "z"
        ],
        "expected": "z"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3134": {
    "functionNames": [
      "pipeline_vowel_count"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": 1
      },
      {
        "args": [
          "level"
        ],
        "expected": 2
      },
      {
        "args": [
          "a b c"
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3135": {
    "functionNames": [
      "pipeline_word_count"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": 1
      },
      {
        "args": [
          "level"
        ],
        "expected": 1
      },
      {
        "args": [
          "a b c"
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3136": {
    "functionNames": [
      "pipeline_remove_spaces"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "Python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "abc"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3137": {
    "functionNames": [
      "pipeline_hyphenate"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "Python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "a-b-c"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3138": {
    "functionNames": [
      "pipeline_title_words"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "Python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "Level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "A B C"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3139": {
    "functionNames": [
      "pipeline_palindrome"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": false
      },
      {
        "args": [
          "level"
        ],
        "expected": true
      },
      {
        "args": [
          "a b c"
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3140": {
    "functionNames": [
      "pipeline_digit_characters"
    ],
    "tests": [
      {
        "args": [
          "a1b2"
        ],
        "expected": 2
      },
      {
        "args": [
          "2026"
        ],
        "expected": 4
      },
      {
        "args": [
          "none"
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3141": {
    "functionNames": [
      "pipeline_initials"
    ],
    "tests": [
      {
        "args": [
          "python code"
        ],
        "expected": "PC"
      },
      {
        "args": [
          "Ada Lovelace"
        ],
        "expected": "AL"
      },
      {
        "args": [
          "solo"
        ],
        "expected": "S"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3142": {
    "functionNames": [
      "pipeline_bracket_text"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "[Python]"
      },
      {
        "args": [
          "level"
        ],
        "expected": "[level]"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "[a b c]"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3143": {
    "functionNames": [
      "pipeline_sum_items"
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
            0,
            5
          ]
        ],
        "expected": 3
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 7
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3144": {
    "functionNames": [
      "pipeline_maximum_item"
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
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 5
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3145": {
    "functionNames": [
      "pipeline_minimum_item"
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
        "expected": 1
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": -2
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3146": {
    "functionNames": [
      "pipeline_reverse_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          5,
          0,
          -2
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          1,
          3,
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3147": {
    "functionNames": [
      "pipeline_sort_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          0,
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          1,
          3,
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3148": {
    "functionNames": [
      "pipeline_unique_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          0,
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3149": {
    "functionNames": [
      "pipeline_even_items"
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
          2
        ]
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          0
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3150": {
    "functionNames": [
      "pipeline_odd_items"
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
          3
        ]
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": [
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          3,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3151": {
    "functionNames": [
      "pipeline_positive_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          3,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3152": {
    "functionNames": [
      "pipeline_square_items"
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
            0,
            5
          ]
        ],
        "expected": [
          4,
          0,
          25
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          9,
          9,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3153": {
    "functionNames": [
      "pipeline_item_count"
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
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 3
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3154": {
    "functionNames": [
      "pipeline_average_items"
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
        "expected": 2
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 1
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 2.3333333333333335
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3155": {
    "functionNames": [
      "pipeline_running_total"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          -2,
          3
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          6,
          7
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3156": {
    "functionNames": [
      "pipeline_index_pairs"
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
          ]
        ]
      },
      {
        "args": [
          [
            -2,
            0,
            5
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
            5
          ]
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          [
            0,
            3
          ],
          [
            1,
            3
          ],
          [
            2,
            1
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3157": {
    "functionNames": [
      "pipeline_nonzero_count"
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
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 2
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 3
      }
    ],
    "requiredDecorators": [
      "apply_transform"
    ],
    "requiredDefinedFunctions": [
      "wrapped",
      "preserve"
    ]
  },
  "3158": {
    "functionNames": [
      "iterator_class_double"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            -4,
            0
          ]
        ],
        "expected": [
          10,
          -8,
          0
        ]
      },
      {
        "args": [
          [
            0,
            5
          ]
        ],
        "expected": [
          0,
          10
        ]
      },
      {
        "args": [
          [
            -4
          ]
        ],
        "expected": [
          -8
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3159": {
    "functionNames": [
      "iterator_class_triple"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            -4,
            0
          ]
        ],
        "expected": [
          15,
          -12,
          0
        ]
      },
      {
        "args": [
          [
            0,
            5
          ]
        ],
        "expected": [
          0,
          15
        ]
      },
      {
        "args": [
          [
            -4
          ]
        ],
        "expected": [
          -12
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3160": {
    "functionNames": [
      "iterator_class_square"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            -4,
            0
          ]
        ],
        "expected": [
          25,
          16,
          0
        ]
      },
      {
        "args": [
          [
            0,
            5
          ]
        ],
        "expected": [
          0,
          25
        ]
      },
      {
        "args": [
          [
            -4
          ]
        ],
        "expected": [
          16
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3161": {
    "functionNames": [
      "iterator_class_cube"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            -4,
            0
          ]
        ],
        "expected": [
          125,
          -64,
          0
        ]
      },
      {
        "args": [
          [
            0,
            5
          ]
        ],
        "expected": [
          0,
          125
        ]
      },
      {
        "args": [
          [
            -4
          ]
        ],
        "expected": [
          -64
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3162": {
    "functionNames": [
      "iterator_class_increment"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            -4,
            0
          ]
        ],
        "expected": [
          6,
          -3,
          1
        ]
      },
      {
        "args": [
          [
            0,
            5
          ]
        ],
        "expected": [
          1,
          6
        ]
      },
      {
        "args": [
          [
            -4
          ]
        ],
        "expected": [
          -3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3163": {
    "functionNames": [
      "iterator_class_decrement"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            -4,
            0
          ]
        ],
        "expected": [
          4,
          -5,
          -1
        ]
      },
      {
        "args": [
          [
            0,
            5
          ]
        ],
        "expected": [
          -1,
          4
        ]
      },
      {
        "args": [
          [
            -4
          ]
        ],
        "expected": [
          -5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3164": {
    "functionNames": [
      "iterator_class_negate"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            -4,
            0
          ]
        ],
        "expected": [
          -5,
          4,
          0
        ]
      },
      {
        "args": [
          [
            0,
            5
          ]
        ],
        "expected": [
          0,
          -5
        ]
      },
      {
        "args": [
          [
            -4
          ]
        ],
        "expected": [
          4
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3165": {
    "functionNames": [
      "iterator_class_absolute"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            -4,
            0
          ]
        ],
        "expected": [
          5,
          4,
          0
        ]
      },
      {
        "args": [
          [
            0,
            5
          ]
        ],
        "expected": [
          0,
          5
        ]
      },
      {
        "args": [
          [
            -4
          ]
        ],
        "expected": [
          4
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3166": {
    "functionNames": [
      "iterator_class_half"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            -4,
            0
          ]
        ],
        "expected": [
          2.5,
          -2,
          0
        ]
      },
      {
        "args": [
          [
            0,
            5
          ]
        ],
        "expected": [
          0,
          2.5
        ]
      },
      {
        "args": [
          [
            -4
          ]
        ],
        "expected": [
          -2
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3167": {
    "functionNames": [
      "iterator_class_remainder_three"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            -4,
            0
          ]
        ],
        "expected": [
          2,
          2,
          0
        ]
      },
      {
        "args": [
          [
            0,
            5
          ]
        ],
        "expected": [
          0,
          2
        ]
      },
      {
        "args": [
          [
            -4
          ]
        ],
        "expected": [
          2
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3168": {
    "functionNames": [
      "iterator_class_last_digit"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            -4,
            0
          ]
        ],
        "expected": [
          5,
          6,
          0
        ]
      },
      {
        "args": [
          [
            0,
            5
          ]
        ],
        "expected": [
          0,
          5
        ]
      },
      {
        "args": [
          [
            -4
          ]
        ],
        "expected": [
          6
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3169": {
    "functionNames": [
      "iterator_class_distance_ten"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            -4,
            0
          ]
        ],
        "expected": [
          5,
          14,
          10
        ]
      },
      {
        "args": [
          [
            0,
            5
          ]
        ],
        "expected": [
          10,
          5
        ]
      },
      {
        "args": [
          [
            -4
          ]
        ],
        "expected": [
          14
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3170": {
    "functionNames": [
      "iterator_class_clamp_zero"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            -4,
            0
          ]
        ],
        "expected": [
          5,
          0,
          0
        ]
      },
      {
        "args": [
          [
            0,
            5
          ]
        ],
        "expected": [
          0,
          5
        ]
      },
      {
        "args": [
          [
            -4
          ]
        ],
        "expected": [
          0
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3171": {
    "functionNames": [
      "iterator_class_is_even"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            -4,
            0
          ]
        ],
        "expected": [
          false,
          true,
          true
        ]
      },
      {
        "args": [
          [
            0,
            5
          ]
        ],
        "expected": [
          true,
          false
        ]
      },
      {
        "args": [
          [
            -4
          ]
        ],
        "expected": [
          true
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3172": {
    "functionNames": [
      "iterator_class_is_positive"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            -4,
            0
          ]
        ],
        "expected": [
          true,
          false,
          false
        ]
      },
      {
        "args": [
          [
            0,
            5
          ]
        ],
        "expected": [
          false,
          true
        ]
      },
      {
        "args": [
          [
            -4
          ]
        ],
        "expected": [
          false
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3173": {
    "functionNames": [
      "iterator_class_sign_label"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            -4,
            0
          ]
        ],
        "expected": [
          "positive",
          "negative",
          "zero"
        ]
      },
      {
        "args": [
          [
            0,
            5
          ]
        ],
        "expected": [
          "zero",
          "positive"
        ]
      },
      {
        "args": [
          [
            -4
          ]
        ],
        "expected": [
          "negative"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3174": {
    "functionNames": [
      "iterator_class_digit_count"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            -4,
            0
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
            0,
            5
          ]
        ],
        "expected": [
          1,
          1
        ]
      },
      {
        "args": [
          [
            -4
          ]
        ],
        "expected": [
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3175": {
    "functionNames": [
      "iterator_class_digit_sum"
    ],
    "tests": [
      {
        "args": [
          [
            52,
            -407,
            0
          ]
        ],
        "expected": [
          7,
          11,
          0
        ]
      },
      {
        "args": [
          [
            0,
            52
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
            -407
          ]
        ],
        "expected": [
          11
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3176": {
    "functionNames": [
      "iterator_class_triangular"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            -4,
            0
          ]
        ],
        "expected": [
          15,
          10,
          0
        ]
      },
      {
        "args": [
          [
            0,
            5
          ]
        ],
        "expected": [
          0,
          15
        ]
      },
      {
        "args": [
          [
            -4
          ]
        ],
        "expected": [
          10
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3177": {
    "functionNames": [
      "iterator_class_within_ten"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            -14,
            10
          ]
        ],
        "expected": [
          true,
          false,
          true
        ]
      },
      {
        "args": [
          [
            10,
            5
          ]
        ],
        "expected": [
          true,
          true
        ]
      },
      {
        "args": [
          [
            -14
          ]
        ],
        "expected": [
          false
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3178": {
    "functionNames": [
      "iterator_class_uppercase"
    ],
    "tests": [
      {
        "args": [
          [
            "Python",
            "level",
            "a b c"
          ]
        ],
        "expected": [
          "PYTHON",
          "LEVEL",
          "A B C"
        ]
      },
      {
        "args": [
          [
            "a b c",
            "Python"
          ]
        ],
        "expected": [
          "A B C",
          "PYTHON"
        ]
      },
      {
        "args": [
          [
            "level"
          ]
        ],
        "expected": [
          "LEVEL"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3179": {
    "functionNames": [
      "iterator_class_lowercase"
    ],
    "tests": [
      {
        "args": [
          [
            "Python",
            "level",
            "a b c"
          ]
        ],
        "expected": [
          "python",
          "level",
          "a b c"
        ]
      },
      {
        "args": [
          [
            "a b c",
            "Python"
          ]
        ],
        "expected": [
          "a b c",
          "python"
        ]
      },
      {
        "args": [
          [
            "level"
          ]
        ],
        "expected": [
          "level"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3180": {
    "functionNames": [
      "iterator_class_reverse_text"
    ],
    "tests": [
      {
        "args": [
          [
            "Python",
            "level",
            "a b c"
          ]
        ],
        "expected": [
          "nohtyP",
          "level",
          "c b a"
        ]
      },
      {
        "args": [
          [
            "a b c",
            "Python"
          ]
        ],
        "expected": [
          "c b a",
          "nohtyP"
        ]
      },
      {
        "args": [
          [
            "level"
          ]
        ],
        "expected": [
          "level"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3181": {
    "functionNames": [
      "iterator_class_text_length"
    ],
    "tests": [
      {
        "args": [
          [
            "Python",
            "level",
            "a b c"
          ]
        ],
        "expected": [
          6,
          5,
          5
        ]
      },
      {
        "args": [
          [
            "a b c",
            "Python"
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
            "level"
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3182": {
    "functionNames": [
      "iterator_class_first_character"
    ],
    "tests": [
      {
        "args": [
          [
            "Python",
            "",
            "z"
          ]
        ],
        "expected": [
          "P",
          "",
          "z"
        ]
      },
      {
        "args": [
          [
            "z",
            "Python"
          ]
        ],
        "expected": [
          "z",
          "P"
        ]
      },
      {
        "args": [
          [
            ""
          ]
        ],
        "expected": [
          ""
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3183": {
    "functionNames": [
      "iterator_class_last_character"
    ],
    "tests": [
      {
        "args": [
          [
            "Python",
            "",
            "z"
          ]
        ],
        "expected": [
          "n",
          "",
          "z"
        ]
      },
      {
        "args": [
          [
            "z",
            "Python"
          ]
        ],
        "expected": [
          "z",
          "n"
        ]
      },
      {
        "args": [
          [
            ""
          ]
        ],
        "expected": [
          ""
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3184": {
    "functionNames": [
      "iterator_class_vowel_count"
    ],
    "tests": [
      {
        "args": [
          [
            "Python",
            "level",
            "a b c"
          ]
        ],
        "expected": [
          1,
          2,
          1
        ]
      },
      {
        "args": [
          [
            "a b c",
            "Python"
          ]
        ],
        "expected": [
          1,
          1
        ]
      },
      {
        "args": [
          [
            "level"
          ]
        ],
        "expected": [
          2
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3185": {
    "functionNames": [
      "iterator_class_word_count"
    ],
    "tests": [
      {
        "args": [
          [
            "Python",
            "level",
            "a b c"
          ]
        ],
        "expected": [
          1,
          1,
          3
        ]
      },
      {
        "args": [
          [
            "a b c",
            "Python"
          ]
        ],
        "expected": [
          3,
          1
        ]
      },
      {
        "args": [
          [
            "level"
          ]
        ],
        "expected": [
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3186": {
    "functionNames": [
      "iterator_class_remove_spaces"
    ],
    "tests": [
      {
        "args": [
          [
            "Python",
            "level",
            "a b c"
          ]
        ],
        "expected": [
          "Python",
          "level",
          "abc"
        ]
      },
      {
        "args": [
          [
            "a b c",
            "Python"
          ]
        ],
        "expected": [
          "abc",
          "Python"
        ]
      },
      {
        "args": [
          [
            "level"
          ]
        ],
        "expected": [
          "level"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3187": {
    "functionNames": [
      "iterator_class_hyphenate"
    ],
    "tests": [
      {
        "args": [
          [
            "Python",
            "level",
            "a b c"
          ]
        ],
        "expected": [
          "Python",
          "level",
          "a-b-c"
        ]
      },
      {
        "args": [
          [
            "a b c",
            "Python"
          ]
        ],
        "expected": [
          "a-b-c",
          "Python"
        ]
      },
      {
        "args": [
          [
            "level"
          ]
        ],
        "expected": [
          "level"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3188": {
    "functionNames": [
      "iterator_class_title_words"
    ],
    "tests": [
      {
        "args": [
          [
            "Python",
            "level",
            "a b c"
          ]
        ],
        "expected": [
          "Python",
          "Level",
          "A B C"
        ]
      },
      {
        "args": [
          [
            "a b c",
            "Python"
          ]
        ],
        "expected": [
          "A B C",
          "Python"
        ]
      },
      {
        "args": [
          [
            "level"
          ]
        ],
        "expected": [
          "Level"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3189": {
    "functionNames": [
      "iterator_class_palindrome"
    ],
    "tests": [
      {
        "args": [
          [
            "Python",
            "level",
            "a b c"
          ]
        ],
        "expected": [
          false,
          true,
          false
        ]
      },
      {
        "args": [
          [
            "a b c",
            "Python"
          ]
        ],
        "expected": [
          false,
          false
        ]
      },
      {
        "args": [
          [
            "level"
          ]
        ],
        "expected": [
          true
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3190": {
    "functionNames": [
      "iterator_class_digit_characters"
    ],
    "tests": [
      {
        "args": [
          [
            "a1b2",
            "2026",
            "none"
          ]
        ],
        "expected": [
          2,
          4,
          0
        ]
      },
      {
        "args": [
          [
            "none",
            "a1b2"
          ]
        ],
        "expected": [
          0,
          2
        ]
      },
      {
        "args": [
          [
            "2026"
          ]
        ],
        "expected": [
          4
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3191": {
    "functionNames": [
      "iterator_class_initials"
    ],
    "tests": [
      {
        "args": [
          [
            "python code",
            "Ada Lovelace",
            "solo"
          ]
        ],
        "expected": [
          "PC",
          "AL",
          "S"
        ]
      },
      {
        "args": [
          [
            "solo",
            "python code"
          ]
        ],
        "expected": [
          "S",
          "PC"
        ]
      },
      {
        "args": [
          [
            "Ada Lovelace"
          ]
        ],
        "expected": [
          "AL"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3192": {
    "functionNames": [
      "iterator_class_bracket_text"
    ],
    "tests": [
      {
        "args": [
          [
            "Python",
            "level",
            "a b c"
          ]
        ],
        "expected": [
          "[Python]",
          "[level]",
          "[a b c]"
        ]
      },
      {
        "args": [
          [
            "a b c",
            "Python"
          ]
        ],
        "expected": [
          "[a b c]",
          "[Python]"
        ]
      },
      {
        "args": [
          [
            "level"
          ]
        ],
        "expected": [
          "[level]"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3193": {
    "functionNames": [
      "iterator_class_sum_items"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              -2,
              0,
              5
            ],
            [
              3,
              3,
              1
            ]
          ]
        ],
        "expected": [
          6,
          3,
          7
        ]
      },
      {
        "args": [
          [
            [
              3,
              3,
              1
            ],
            [
              1,
              2,
              3
            ]
          ]
        ],
        "expected": [
          7,
          6
        ]
      },
      {
        "args": [
          [
            [
              -2,
              0,
              5
            ]
          ]
        ],
        "expected": [
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3194": {
    "functionNames": [
      "iterator_class_maximum_item"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              -2,
              0,
              5
            ],
            [
              3,
              3,
              1
            ]
          ]
        ],
        "expected": [
          3,
          5,
          3
        ]
      },
      {
        "args": [
          [
            [
              3,
              3,
              1
            ],
            [
              1,
              2,
              3
            ]
          ]
        ],
        "expected": [
          3,
          3
        ]
      },
      {
        "args": [
          [
            [
              -2,
              0,
              5
            ]
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3195": {
    "functionNames": [
      "iterator_class_minimum_item"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              -2,
              0,
              5
            ],
            [
              3,
              3,
              1
            ]
          ]
        ],
        "expected": [
          1,
          -2,
          1
        ]
      },
      {
        "args": [
          [
            [
              3,
              3,
              1
            ],
            [
              1,
              2,
              3
            ]
          ]
        ],
        "expected": [
          1,
          1
        ]
      },
      {
        "args": [
          [
            [
              -2,
              0,
              5
            ]
          ]
        ],
        "expected": [
          -2
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3196": {
    "functionNames": [
      "iterator_class_reverse_items"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              -2,
              0,
              5
            ],
            [
              3,
              3,
              1
            ]
          ]
        ],
        "expected": [
          [
            3,
            2,
            1
          ],
          [
            5,
            0,
            -2
          ],
          [
            1,
            3,
            3
          ]
        ]
      },
      {
        "args": [
          [
            [
              3,
              3,
              1
            ],
            [
              1,
              2,
              3
            ]
          ]
        ],
        "expected": [
          [
            1,
            3,
            3
          ],
          [
            3,
            2,
            1
          ]
        ]
      },
      {
        "args": [
          [
            [
              -2,
              0,
              5
            ]
          ]
        ],
        "expected": [
          [
            5,
            0,
            -2
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3197": {
    "functionNames": [
      "iterator_class_sort_items"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              -2,
              0,
              5
            ],
            [
              3,
              3,
              1
            ]
          ]
        ],
        "expected": [
          [
            1,
            2,
            3
          ],
          [
            -2,
            0,
            5
          ],
          [
            1,
            3,
            3
          ]
        ]
      },
      {
        "args": [
          [
            [
              3,
              3,
              1
            ],
            [
              1,
              2,
              3
            ]
          ]
        ],
        "expected": [
          [
            1,
            3,
            3
          ],
          [
            1,
            2,
            3
          ]
        ]
      },
      {
        "args": [
          [
            [
              -2,
              0,
              5
            ]
          ]
        ],
        "expected": [
          [
            -2,
            0,
            5
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3198": {
    "functionNames": [
      "iterator_class_unique_items"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              -2,
              0,
              5
            ],
            [
              3,
              3,
              1
            ]
          ]
        ],
        "expected": [
          [
            1,
            2,
            3
          ],
          [
            -2,
            0,
            5
          ],
          [
            3,
            1
          ]
        ]
      },
      {
        "args": [
          [
            [
              3,
              3,
              1
            ],
            [
              1,
              2,
              3
            ]
          ]
        ],
        "expected": [
          [
            3,
            1
          ],
          [
            1,
            2,
            3
          ]
        ]
      },
      {
        "args": [
          [
            [
              -2,
              0,
              5
            ]
          ]
        ],
        "expected": [
          [
            -2,
            0,
            5
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3199": {
    "functionNames": [
      "iterator_class_even_items"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              -2,
              0,
              5
            ],
            [
              3,
              3,
              1
            ]
          ]
        ],
        "expected": [
          [
            2
          ],
          [
            -2,
            0
          ],
          []
        ]
      },
      {
        "args": [
          [
            [
              3,
              3,
              1
            ],
            [
              1,
              2,
              3
            ]
          ]
        ],
        "expected": [
          [],
          [
            2
          ]
        ]
      },
      {
        "args": [
          [
            [
              -2,
              0,
              5
            ]
          ]
        ],
        "expected": [
          [
            -2,
            0
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3200": {
    "functionNames": [
      "iterator_class_odd_items"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              -2,
              0,
              5
            ],
            [
              3,
              3,
              1
            ]
          ]
        ],
        "expected": [
          [
            1,
            3
          ],
          [
            5
          ],
          [
            3,
            3,
            1
          ]
        ]
      },
      {
        "args": [
          [
            [
              3,
              3,
              1
            ],
            [
              1,
              2,
              3
            ]
          ]
        ],
        "expected": [
          [
            3,
            3,
            1
          ],
          [
            1,
            3
          ]
        ]
      },
      {
        "args": [
          [
            [
              -2,
              0,
              5
            ]
          ]
        ],
        "expected": [
          [
            5
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3201": {
    "functionNames": [
      "iterator_class_positive_items"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              -2,
              0,
              5
            ],
            [
              3,
              3,
              1
            ]
          ]
        ],
        "expected": [
          [
            1,
            2,
            3
          ],
          [
            5
          ],
          [
            3,
            3,
            1
          ]
        ]
      },
      {
        "args": [
          [
            [
              3,
              3,
              1
            ],
            [
              1,
              2,
              3
            ]
          ]
        ],
        "expected": [
          [
            3,
            3,
            1
          ],
          [
            1,
            2,
            3
          ]
        ]
      },
      {
        "args": [
          [
            [
              -2,
              0,
              5
            ]
          ]
        ],
        "expected": [
          [
            5
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3202": {
    "functionNames": [
      "iterator_class_square_items"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              -2,
              0,
              5
            ],
            [
              3,
              3,
              1
            ]
          ]
        ],
        "expected": [
          [
            1,
            4,
            9
          ],
          [
            4,
            0,
            25
          ],
          [
            9,
            9,
            1
          ]
        ]
      },
      {
        "args": [
          [
            [
              3,
              3,
              1
            ],
            [
              1,
              2,
              3
            ]
          ]
        ],
        "expected": [
          [
            9,
            9,
            1
          ],
          [
            1,
            4,
            9
          ]
        ]
      },
      {
        "args": [
          [
            [
              -2,
              0,
              5
            ]
          ]
        ],
        "expected": [
          [
            4,
            0,
            25
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3203": {
    "functionNames": [
      "iterator_class_item_count"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              -2,
              0,
              5
            ],
            [
              3,
              3,
              1
            ]
          ]
        ],
        "expected": [
          3,
          3,
          3
        ]
      },
      {
        "args": [
          [
            [
              3,
              3,
              1
            ],
            [
              1,
              2,
              3
            ]
          ]
        ],
        "expected": [
          3,
          3
        ]
      },
      {
        "args": [
          [
            [
              -2,
              0,
              5
            ]
          ]
        ],
        "expected": [
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3204": {
    "functionNames": [
      "iterator_class_average_items"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              -2,
              0,
              5
            ],
            [
              3,
              3,
              1
            ]
          ]
        ],
        "expected": [
          2,
          1,
          2.3333333333333335
        ]
      },
      {
        "args": [
          [
            [
              3,
              3,
              1
            ],
            [
              1,
              2,
              3
            ]
          ]
        ],
        "expected": [
          2.3333333333333335,
          2
        ]
      },
      {
        "args": [
          [
            [
              -2,
              0,
              5
            ]
          ]
        ],
        "expected": [
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3205": {
    "functionNames": [
      "iterator_class_running_total"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              -2,
              0,
              5
            ],
            [
              3,
              3,
              1
            ]
          ]
        ],
        "expected": [
          [
            1,
            3,
            6
          ],
          [
            -2,
            -2,
            3
          ],
          [
            3,
            6,
            7
          ]
        ]
      },
      {
        "args": [
          [
            [
              3,
              3,
              1
            ],
            [
              1,
              2,
              3
            ]
          ]
        ],
        "expected": [
          [
            3,
            6,
            7
          ],
          [
            1,
            3,
            6
          ]
        ]
      },
      {
        "args": [
          [
            [
              -2,
              0,
              5
            ]
          ]
        ],
        "expected": [
          [
            -2,
            -2,
            3
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3206": {
    "functionNames": [
      "iterator_class_index_pairs"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              -2,
              0,
              5
            ],
            [
              3,
              3,
              1
            ]
          ]
        ],
        "expected": [
          [
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
            ]
          ],
          [
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
              5
            ]
          ],
          [
            [
              0,
              3
            ],
            [
              1,
              3
            ],
            [
              2,
              1
            ]
          ]
        ]
      },
      {
        "args": [
          [
            [
              3,
              3,
              1
            ],
            [
              1,
              2,
              3
            ]
          ]
        ],
        "expected": [
          [
            [
              0,
              3
            ],
            [
              1,
              3
            ],
            [
              2,
              1
            ]
          ],
          [
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
            ]
          ]
        ]
      },
      {
        "args": [
          [
            [
              -2,
              0,
              5
            ]
          ]
        ],
        "expected": [
          [
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
              5
            ]
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3207": {
    "functionNames": [
      "iterator_class_nonzero_count"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              2,
              3
            ],
            [
              -2,
              0,
              5
            ],
            [
              3,
              3,
              1
            ]
          ]
        ],
        "expected": [
          3,
          2,
          3
        ]
      },
      {
        "args": [
          [
            [
              3,
              3,
              1
            ],
            [
              1,
              2,
              3
            ]
          ]
        ],
        "expected": [
          3,
          3
        ]
      },
      {
        "args": [
          [
            [
              -2,
              0,
              5
            ]
          ]
        ],
        "expected": [
          2
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 1
      },
      {
        "functionName": "next",
        "minArgs": 1
      }
    ],
    "requiredDefinedFunctions": [
      "__iter__",
      "__next__"
    ]
  },
  "3208": {
    "functionNames": [
      "resource_double"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 10
      },
      {
        "args": [
          -4
        ],
        "expected": -8
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3209": {
    "functionNames": [
      "resource_triple"
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
          -4
        ],
        "expected": -12
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3210": {
    "functionNames": [
      "resource_square"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 25
      },
      {
        "args": [
          -4
        ],
        "expected": 16
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3211": {
    "functionNames": [
      "resource_cube"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 125
      },
      {
        "args": [
          -4
        ],
        "expected": -64
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3212": {
    "functionNames": [
      "resource_increment"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 6
      },
      {
        "args": [
          -4
        ],
        "expected": -3
      },
      {
        "args": [
          0
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3213": {
    "functionNames": [
      "resource_decrement"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 4
      },
      {
        "args": [
          -4
        ],
        "expected": -5
      },
      {
        "args": [
          0
        ],
        "expected": -1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3214": {
    "functionNames": [
      "resource_negate"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": -5
      },
      {
        "args": [
          -4
        ],
        "expected": 4
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3215": {
    "functionNames": [
      "resource_absolute"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 4
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3216": {
    "functionNames": [
      "resource_half"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 2.5
      },
      {
        "args": [
          -4
        ],
        "expected": -2
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3217": {
    "functionNames": [
      "resource_remainder_three"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 2
      },
      {
        "args": [
          -4
        ],
        "expected": 2
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3218": {
    "functionNames": [
      "resource_last_digit"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 6
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3219": {
    "functionNames": [
      "resource_distance_ten"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 14
      },
      {
        "args": [
          0
        ],
        "expected": 10
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3220": {
    "functionNames": [
      "resource_clamp_zero"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 0
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3221": {
    "functionNames": [
      "resource_is_even"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": false
      },
      {
        "args": [
          -4
        ],
        "expected": true
      },
      {
        "args": [
          0
        ],
        "expected": true
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3222": {
    "functionNames": [
      "resource_is_positive"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": true
      },
      {
        "args": [
          -4
        ],
        "expected": false
      },
      {
        "args": [
          0
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3223": {
    "functionNames": [
      "resource_sign_label"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": "positive"
      },
      {
        "args": [
          -4
        ],
        "expected": "negative"
      },
      {
        "args": [
          0
        ],
        "expected": "zero"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3224": {
    "functionNames": [
      "resource_digit_count"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 1
      },
      {
        "args": [
          -4
        ],
        "expected": 1
      },
      {
        "args": [
          0
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3225": {
    "functionNames": [
      "resource_digit_sum"
    ],
    "tests": [
      {
        "args": [
          52
        ],
        "expected": 7
      },
      {
        "args": [
          -407
        ],
        "expected": 11
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3226": {
    "functionNames": [
      "resource_triangular"
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
          -4
        ],
        "expected": 10
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3227": {
    "functionNames": [
      "resource_within_ten"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": true
      },
      {
        "args": [
          -14
        ],
        "expected": false
      },
      {
        "args": [
          10
        ],
        "expected": true
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3228": {
    "functionNames": [
      "resource_uppercase"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "PYTHON"
      },
      {
        "args": [
          "level"
        ],
        "expected": "LEVEL"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "A B C"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3229": {
    "functionNames": [
      "resource_lowercase"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "a b c"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3230": {
    "functionNames": [
      "resource_reverse_text"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "nohtyP"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "c b a"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3231": {
    "functionNames": [
      "resource_text_length"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": 6
      },
      {
        "args": [
          "level"
        ],
        "expected": 5
      },
      {
        "args": [
          "a b c"
        ],
        "expected": 5
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3232": {
    "functionNames": [
      "resource_first_character"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "P"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      },
      {
        "args": [
          "z"
        ],
        "expected": "z"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3233": {
    "functionNames": [
      "resource_last_character"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "n"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      },
      {
        "args": [
          "z"
        ],
        "expected": "z"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3234": {
    "functionNames": [
      "resource_vowel_count"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": 1
      },
      {
        "args": [
          "level"
        ],
        "expected": 2
      },
      {
        "args": [
          "a b c"
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3235": {
    "functionNames": [
      "resource_word_count"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": 1
      },
      {
        "args": [
          "level"
        ],
        "expected": 1
      },
      {
        "args": [
          "a b c"
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3236": {
    "functionNames": [
      "resource_remove_spaces"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "Python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "abc"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3237": {
    "functionNames": [
      "resource_hyphenate"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "Python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "a-b-c"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3238": {
    "functionNames": [
      "resource_title_words"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "Python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "Level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "A B C"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3239": {
    "functionNames": [
      "resource_palindrome"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": false
      },
      {
        "args": [
          "level"
        ],
        "expected": true
      },
      {
        "args": [
          "a b c"
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3240": {
    "functionNames": [
      "resource_digit_characters"
    ],
    "tests": [
      {
        "args": [
          "a1b2"
        ],
        "expected": 2
      },
      {
        "args": [
          "2026"
        ],
        "expected": 4
      },
      {
        "args": [
          "none"
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3241": {
    "functionNames": [
      "resource_initials"
    ],
    "tests": [
      {
        "args": [
          "python code"
        ],
        "expected": "PC"
      },
      {
        "args": [
          "Ada Lovelace"
        ],
        "expected": "AL"
      },
      {
        "args": [
          "solo"
        ],
        "expected": "S"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3242": {
    "functionNames": [
      "resource_bracket_text"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "[Python]"
      },
      {
        "args": [
          "level"
        ],
        "expected": "[level]"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "[a b c]"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3243": {
    "functionNames": [
      "resource_sum_items"
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
            0,
            5
          ]
        ],
        "expected": 3
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 7
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3244": {
    "functionNames": [
      "resource_maximum_item"
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
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 5
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3245": {
    "functionNames": [
      "resource_minimum_item"
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
        "expected": 1
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": -2
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3246": {
    "functionNames": [
      "resource_reverse_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          5,
          0,
          -2
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          1,
          3,
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3247": {
    "functionNames": [
      "resource_sort_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          0,
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          1,
          3,
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3248": {
    "functionNames": [
      "resource_unique_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          0,
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3249": {
    "functionNames": [
      "resource_even_items"
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
          2
        ]
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          0
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3250": {
    "functionNames": [
      "resource_odd_items"
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
          3
        ]
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": [
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          3,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3251": {
    "functionNames": [
      "resource_positive_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          3,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3252": {
    "functionNames": [
      "resource_square_items"
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
            0,
            5
          ]
        ],
        "expected": [
          4,
          0,
          25
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          9,
          9,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3253": {
    "functionNames": [
      "resource_item_count"
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
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 3
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3254": {
    "functionNames": [
      "resource_average_items"
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
        "expected": 2
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 1
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 2.3333333333333335
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3255": {
    "functionNames": [
      "resource_running_total"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          -2,
          3
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          6,
          7
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3256": {
    "functionNames": [
      "resource_index_pairs"
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
          ]
        ]
      },
      {
        "args": [
          [
            -2,
            0,
            5
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
            5
          ]
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          [
            0,
            3
          ],
          [
            1,
            3
          ],
          [
            2,
            1
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3257": {
    "functionNames": [
      "resource_nonzero_count"
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
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 2
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "With"
      },
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__enter__",
      "__exit__"
    ]
  },
  "3258": {
    "functionNames": [
      "record_double"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 10
      },
      {
        "args": [
          -4
        ],
        "expected": -8
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3259": {
    "functionNames": [
      "record_triple"
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
          -4
        ],
        "expected": -12
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3260": {
    "functionNames": [
      "record_square"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 25
      },
      {
        "args": [
          -4
        ],
        "expected": 16
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3261": {
    "functionNames": [
      "record_cube"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 125
      },
      {
        "args": [
          -4
        ],
        "expected": -64
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3262": {
    "functionNames": [
      "record_increment"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 6
      },
      {
        "args": [
          -4
        ],
        "expected": -3
      },
      {
        "args": [
          0
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3263": {
    "functionNames": [
      "record_decrement"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 4
      },
      {
        "args": [
          -4
        ],
        "expected": -5
      },
      {
        "args": [
          0
        ],
        "expected": -1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3264": {
    "functionNames": [
      "record_negate"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": -5
      },
      {
        "args": [
          -4
        ],
        "expected": 4
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3265": {
    "functionNames": [
      "record_absolute"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 4
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3266": {
    "functionNames": [
      "record_half"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 2.5
      },
      {
        "args": [
          -4
        ],
        "expected": -2
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3267": {
    "functionNames": [
      "record_remainder_three"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 2
      },
      {
        "args": [
          -4
        ],
        "expected": 2
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3268": {
    "functionNames": [
      "record_last_digit"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 6
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3269": {
    "functionNames": [
      "record_distance_ten"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 14
      },
      {
        "args": [
          0
        ],
        "expected": 10
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3270": {
    "functionNames": [
      "record_clamp_zero"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 0
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3271": {
    "functionNames": [
      "record_is_even"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": false
      },
      {
        "args": [
          -4
        ],
        "expected": true
      },
      {
        "args": [
          0
        ],
        "expected": true
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3272": {
    "functionNames": [
      "record_is_positive"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": true
      },
      {
        "args": [
          -4
        ],
        "expected": false
      },
      {
        "args": [
          0
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3273": {
    "functionNames": [
      "record_sign_label"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": "positive"
      },
      {
        "args": [
          -4
        ],
        "expected": "negative"
      },
      {
        "args": [
          0
        ],
        "expected": "zero"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3274": {
    "functionNames": [
      "record_digit_count"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 1
      },
      {
        "args": [
          -4
        ],
        "expected": 1
      },
      {
        "args": [
          0
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3275": {
    "functionNames": [
      "record_digit_sum"
    ],
    "tests": [
      {
        "args": [
          52
        ],
        "expected": 7
      },
      {
        "args": [
          -407
        ],
        "expected": 11
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3276": {
    "functionNames": [
      "record_triangular"
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
          -4
        ],
        "expected": 10
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3277": {
    "functionNames": [
      "record_within_ten"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": true
      },
      {
        "args": [
          -14
        ],
        "expected": false
      },
      {
        "args": [
          10
        ],
        "expected": true
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3278": {
    "functionNames": [
      "record_uppercase"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "PYTHON"
      },
      {
        "args": [
          "level"
        ],
        "expected": "LEVEL"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "A B C"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3279": {
    "functionNames": [
      "record_lowercase"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "a b c"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3280": {
    "functionNames": [
      "record_reverse_text"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "nohtyP"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "c b a"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3281": {
    "functionNames": [
      "record_text_length"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": 6
      },
      {
        "args": [
          "level"
        ],
        "expected": 5
      },
      {
        "args": [
          "a b c"
        ],
        "expected": 5
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3282": {
    "functionNames": [
      "record_first_character"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "P"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      },
      {
        "args": [
          "z"
        ],
        "expected": "z"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3283": {
    "functionNames": [
      "record_last_character"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "n"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      },
      {
        "args": [
          "z"
        ],
        "expected": "z"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3284": {
    "functionNames": [
      "record_vowel_count"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": 1
      },
      {
        "args": [
          "level"
        ],
        "expected": 2
      },
      {
        "args": [
          "a b c"
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3285": {
    "functionNames": [
      "record_word_count"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": 1
      },
      {
        "args": [
          "level"
        ],
        "expected": 1
      },
      {
        "args": [
          "a b c"
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3286": {
    "functionNames": [
      "record_remove_spaces"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "Python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "abc"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3287": {
    "functionNames": [
      "record_hyphenate"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "Python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "a-b-c"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3288": {
    "functionNames": [
      "record_title_words"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "Python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "Level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "A B C"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3289": {
    "functionNames": [
      "record_palindrome"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": false
      },
      {
        "args": [
          "level"
        ],
        "expected": true
      },
      {
        "args": [
          "a b c"
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3290": {
    "functionNames": [
      "record_digit_characters"
    ],
    "tests": [
      {
        "args": [
          "a1b2"
        ],
        "expected": 2
      },
      {
        "args": [
          "2026"
        ],
        "expected": 4
      },
      {
        "args": [
          "none"
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3291": {
    "functionNames": [
      "record_initials"
    ],
    "tests": [
      {
        "args": [
          "python code"
        ],
        "expected": "PC"
      },
      {
        "args": [
          "Ada Lovelace"
        ],
        "expected": "AL"
      },
      {
        "args": [
          "solo"
        ],
        "expected": "S"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3292": {
    "functionNames": [
      "record_bracket_text"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "[Python]"
      },
      {
        "args": [
          "level"
        ],
        "expected": "[level]"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "[a b c]"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3293": {
    "functionNames": [
      "record_sum_items"
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
            0,
            5
          ]
        ],
        "expected": 3
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 7
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3294": {
    "functionNames": [
      "record_maximum_item"
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
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 5
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3295": {
    "functionNames": [
      "record_minimum_item"
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
        "expected": 1
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": -2
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3296": {
    "functionNames": [
      "record_reverse_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          5,
          0,
          -2
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          1,
          3,
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3297": {
    "functionNames": [
      "record_sort_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          0,
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          1,
          3,
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3298": {
    "functionNames": [
      "record_unique_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          0,
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3299": {
    "functionNames": [
      "record_even_items"
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
          2
        ]
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          0
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3300": {
    "functionNames": [
      "record_odd_items"
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
          3
        ]
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": [
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          3,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3301": {
    "functionNames": [
      "record_positive_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          3,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3302": {
    "functionNames": [
      "record_square_items"
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
            0,
            5
          ]
        ],
        "expected": [
          4,
          0,
          25
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          9,
          9,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3303": {
    "functionNames": [
      "record_item_count"
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
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 3
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3304": {
    "functionNames": [
      "record_average_items"
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
        "expected": 2
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 1
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 2.3333333333333335
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3305": {
    "functionNames": [
      "record_running_total"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          -2,
          3
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          6,
          7
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3306": {
    "functionNames": [
      "record_index_pairs"
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
          ]
        ]
      },
      {
        "args": [
          [
            -2,
            0,
            5
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
            5
          ]
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          [
            0,
            3
          ],
          [
            1,
            3
          ],
          [
            2,
            1
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3307": {
    "functionNames": [
      "record_nonzero_count"
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
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 2
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      },
      {
        "nodeType": "AnnAssign"
      }
    ],
    "requiredDecorators": [
      "dataclass"
    ],
    "requiredDefinedFunctions": [
      "result"
    ]
  },
  "3308": {
    "functionNames": [
      "callable_double"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 10
      },
      {
        "args": [
          -4
        ],
        "expected": -8
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3309": {
    "functionNames": [
      "callable_triple"
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
          -4
        ],
        "expected": -12
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3310": {
    "functionNames": [
      "callable_square"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 25
      },
      {
        "args": [
          -4
        ],
        "expected": 16
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3311": {
    "functionNames": [
      "callable_cube"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 125
      },
      {
        "args": [
          -4
        ],
        "expected": -64
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3312": {
    "functionNames": [
      "callable_increment"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 6
      },
      {
        "args": [
          -4
        ],
        "expected": -3
      },
      {
        "args": [
          0
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3313": {
    "functionNames": [
      "callable_decrement"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 4
      },
      {
        "args": [
          -4
        ],
        "expected": -5
      },
      {
        "args": [
          0
        ],
        "expected": -1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3314": {
    "functionNames": [
      "callable_negate"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": -5
      },
      {
        "args": [
          -4
        ],
        "expected": 4
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3315": {
    "functionNames": [
      "callable_absolute"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 4
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3316": {
    "functionNames": [
      "callable_half"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 2.5
      },
      {
        "args": [
          -4
        ],
        "expected": -2
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3317": {
    "functionNames": [
      "callable_remainder_three"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 2
      },
      {
        "args": [
          -4
        ],
        "expected": 2
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3318": {
    "functionNames": [
      "callable_last_digit"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 6
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3319": {
    "functionNames": [
      "callable_distance_ten"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 14
      },
      {
        "args": [
          0
        ],
        "expected": 10
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3320": {
    "functionNames": [
      "callable_clamp_zero"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 0
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3321": {
    "functionNames": [
      "callable_is_even"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": false
      },
      {
        "args": [
          -4
        ],
        "expected": true
      },
      {
        "args": [
          0
        ],
        "expected": true
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3322": {
    "functionNames": [
      "callable_is_positive"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": true
      },
      {
        "args": [
          -4
        ],
        "expected": false
      },
      {
        "args": [
          0
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3323": {
    "functionNames": [
      "callable_sign_label"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": "positive"
      },
      {
        "args": [
          -4
        ],
        "expected": "negative"
      },
      {
        "args": [
          0
        ],
        "expected": "zero"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3324": {
    "functionNames": [
      "callable_digit_count"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 1
      },
      {
        "args": [
          -4
        ],
        "expected": 1
      },
      {
        "args": [
          0
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3325": {
    "functionNames": [
      "callable_digit_sum"
    ],
    "tests": [
      {
        "args": [
          52
        ],
        "expected": 7
      },
      {
        "args": [
          -407
        ],
        "expected": 11
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3326": {
    "functionNames": [
      "callable_triangular"
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
          -4
        ],
        "expected": 10
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3327": {
    "functionNames": [
      "callable_within_ten"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": true
      },
      {
        "args": [
          -14
        ],
        "expected": false
      },
      {
        "args": [
          10
        ],
        "expected": true
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3328": {
    "functionNames": [
      "callable_uppercase"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "PYTHON"
      },
      {
        "args": [
          "level"
        ],
        "expected": "LEVEL"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "A B C"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3329": {
    "functionNames": [
      "callable_lowercase"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "a b c"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3330": {
    "functionNames": [
      "callable_reverse_text"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "nohtyP"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "c b a"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3331": {
    "functionNames": [
      "callable_text_length"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": 6
      },
      {
        "args": [
          "level"
        ],
        "expected": 5
      },
      {
        "args": [
          "a b c"
        ],
        "expected": 5
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3332": {
    "functionNames": [
      "callable_first_character"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "P"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      },
      {
        "args": [
          "z"
        ],
        "expected": "z"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3333": {
    "functionNames": [
      "callable_last_character"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "n"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      },
      {
        "args": [
          "z"
        ],
        "expected": "z"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3334": {
    "functionNames": [
      "callable_vowel_count"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": 1
      },
      {
        "args": [
          "level"
        ],
        "expected": 2
      },
      {
        "args": [
          "a b c"
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3335": {
    "functionNames": [
      "callable_word_count"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": 1
      },
      {
        "args": [
          "level"
        ],
        "expected": 1
      },
      {
        "args": [
          "a b c"
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3336": {
    "functionNames": [
      "callable_remove_spaces"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "Python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "abc"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3337": {
    "functionNames": [
      "callable_hyphenate"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "Python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "a-b-c"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3338": {
    "functionNames": [
      "callable_title_words"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "Python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "Level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "A B C"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3339": {
    "functionNames": [
      "callable_palindrome"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": false
      },
      {
        "args": [
          "level"
        ],
        "expected": true
      },
      {
        "args": [
          "a b c"
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3340": {
    "functionNames": [
      "callable_digit_characters"
    ],
    "tests": [
      {
        "args": [
          "a1b2"
        ],
        "expected": 2
      },
      {
        "args": [
          "2026"
        ],
        "expected": 4
      },
      {
        "args": [
          "none"
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3341": {
    "functionNames": [
      "callable_initials"
    ],
    "tests": [
      {
        "args": [
          "python code"
        ],
        "expected": "PC"
      },
      {
        "args": [
          "Ada Lovelace"
        ],
        "expected": "AL"
      },
      {
        "args": [
          "solo"
        ],
        "expected": "S"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3342": {
    "functionNames": [
      "callable_bracket_text"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "[Python]"
      },
      {
        "args": [
          "level"
        ],
        "expected": "[level]"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "[a b c]"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3343": {
    "functionNames": [
      "callable_sum_items"
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
            0,
            5
          ]
        ],
        "expected": 3
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 7
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3344": {
    "functionNames": [
      "callable_maximum_item"
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
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 5
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3345": {
    "functionNames": [
      "callable_minimum_item"
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
        "expected": 1
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": -2
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3346": {
    "functionNames": [
      "callable_reverse_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          5,
          0,
          -2
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          1,
          3,
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3347": {
    "functionNames": [
      "callable_sort_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          0,
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          1,
          3,
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3348": {
    "functionNames": [
      "callable_unique_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          0,
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3349": {
    "functionNames": [
      "callable_even_items"
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
          2
        ]
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          0
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3350": {
    "functionNames": [
      "callable_odd_items"
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
          3
        ]
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": [
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          3,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3351": {
    "functionNames": [
      "callable_positive_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          3,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3352": {
    "functionNames": [
      "callable_square_items"
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
            0,
            5
          ]
        ],
        "expected": [
          4,
          0,
          25
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          9,
          9,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3353": {
    "functionNames": [
      "callable_item_count"
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
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 3
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3354": {
    "functionNames": [
      "callable_average_items"
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
        "expected": 2
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 1
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 2.3333333333333335
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3355": {
    "functionNames": [
      "callable_running_total"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          -2,
          3
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          6,
          7
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3356": {
    "functionNames": [
      "callable_index_pairs"
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
          ]
        ]
      },
      {
        "args": [
          [
            -2,
            0,
            5
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
            5
          ]
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          [
            0,
            3
          ],
          [
            1,
            3
          ],
          [
            2,
            1
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3357": {
    "functionNames": [
      "callable_nonzero_count"
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
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 2
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ClassDef"
      }
    ],
    "requiredDefinedFunctions": [
      "__call__"
    ]
  },
  "3358": {
    "functionNames": [
      "advanced_and_2_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          19
        ],
        "expected": 2
      },
      {
        "args": [
          86
        ],
        "expected": 2
      }
    ],
    "requiredAstOperators": [
      "BitAnd"
    ]
  },
  "3359": {
    "functionNames": [
      "advanced_and_6_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          19
        ],
        "expected": 2
      },
      {
        "args": [
          86
        ],
        "expected": 6
      }
    ],
    "requiredAstOperators": [
      "BitAnd"
    ]
  },
  "3360": {
    "functionNames": [
      "advanced_and_12_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          19
        ],
        "expected": 0
      },
      {
        "args": [
          86
        ],
        "expected": 4
      }
    ],
    "requiredAstOperators": [
      "BitAnd"
    ]
  },
  "3361": {
    "functionNames": [
      "advanced_and_24_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          19
        ],
        "expected": 16
      },
      {
        "args": [
          86
        ],
        "expected": 16
      }
    ],
    "requiredAstOperators": [
      "BitAnd"
    ]
  },
  "3362": {
    "functionNames": [
      "advanced_and_48_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          19
        ],
        "expected": 16
      },
      {
        "args": [
          86
        ],
        "expected": 16
      }
    ],
    "requiredAstOperators": [
      "BitAnd"
    ]
  },
  "3363": {
    "functionNames": [
      "advanced_or_2_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 2
      },
      {
        "args": [
          19
        ],
        "expected": 19
      },
      {
        "args": [
          86
        ],
        "expected": 86
      }
    ],
    "requiredAstOperators": [
      "BitOr"
    ]
  },
  "3364": {
    "functionNames": [
      "advanced_or_6_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 6
      },
      {
        "args": [
          19
        ],
        "expected": 23
      },
      {
        "args": [
          86
        ],
        "expected": 86
      }
    ],
    "requiredAstOperators": [
      "BitOr"
    ]
  },
  "3365": {
    "functionNames": [
      "advanced_or_12_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 12
      },
      {
        "args": [
          19
        ],
        "expected": 31
      },
      {
        "args": [
          86
        ],
        "expected": 94
      }
    ],
    "requiredAstOperators": [
      "BitOr"
    ]
  },
  "3366": {
    "functionNames": [
      "advanced_or_24_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 24
      },
      {
        "args": [
          19
        ],
        "expected": 27
      },
      {
        "args": [
          86
        ],
        "expected": 94
      }
    ],
    "requiredAstOperators": [
      "BitOr"
    ]
  },
  "3367": {
    "functionNames": [
      "advanced_or_48_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 48
      },
      {
        "args": [
          19
        ],
        "expected": 51
      },
      {
        "args": [
          86
        ],
        "expected": 118
      }
    ],
    "requiredAstOperators": [
      "BitOr"
    ]
  },
  "3368": {
    "functionNames": [
      "advanced_xor_2_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 2
      },
      {
        "args": [
          19
        ],
        "expected": 17
      },
      {
        "args": [
          86
        ],
        "expected": 84
      }
    ],
    "requiredAstOperators": [
      "BitXor"
    ]
  },
  "3369": {
    "functionNames": [
      "advanced_xor_6_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 6
      },
      {
        "args": [
          19
        ],
        "expected": 21
      },
      {
        "args": [
          86
        ],
        "expected": 80
      }
    ],
    "requiredAstOperators": [
      "BitXor"
    ]
  },
  "3370": {
    "functionNames": [
      "advanced_xor_12_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 12
      },
      {
        "args": [
          19
        ],
        "expected": 31
      },
      {
        "args": [
          86
        ],
        "expected": 90
      }
    ],
    "requiredAstOperators": [
      "BitXor"
    ]
  },
  "3371": {
    "functionNames": [
      "advanced_xor_24_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 24
      },
      {
        "args": [
          19
        ],
        "expected": 11
      },
      {
        "args": [
          86
        ],
        "expected": 78
      }
    ],
    "requiredAstOperators": [
      "BitXor"
    ]
  },
  "3372": {
    "functionNames": [
      "advanced_xor_48_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 48
      },
      {
        "args": [
          19
        ],
        "expected": 35
      },
      {
        "args": [
          86
        ],
        "expected": 102
      }
    ],
    "requiredAstOperators": [
      "BitXor"
    ]
  },
  "3373": {
    "functionNames": [
      "scaled_left_1_bitwise"
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
          19
        ],
        "expected": 39
      },
      {
        "args": [
          86
        ],
        "expected": 173
      }
    ],
    "requiredAstOperators": [
      "LShift"
    ]
  },
  "3374": {
    "functionNames": [
      "scaled_left_2_bitwise"
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
          19
        ],
        "expected": 77
      },
      {
        "args": [
          86
        ],
        "expected": 345
      }
    ],
    "requiredAstOperators": [
      "LShift"
    ]
  },
  "3375": {
    "functionNames": [
      "scaled_left_3_bitwise"
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
          19
        ],
        "expected": 153
      },
      {
        "args": [
          86
        ],
        "expected": 689
      }
    ],
    "requiredAstOperators": [
      "LShift"
    ]
  },
  "3376": {
    "functionNames": [
      "scaled_left_4_bitwise"
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
          19
        ],
        "expected": 305
      },
      {
        "args": [
          86
        ],
        "expected": 1377
      }
    ],
    "requiredAstOperators": [
      "LShift"
    ]
  },
  "3377": {
    "functionNames": [
      "scaled_left_5_bitwise"
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
          19
        ],
        "expected": 609
      },
      {
        "args": [
          86
        ],
        "expected": 2753
      }
    ],
    "requiredAstOperators": [
      "LShift"
    ]
  },
  "3378": {
    "functionNames": [
      "scaled_right_1_bitwise"
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
          19
        ],
        "expected": 10
      },
      {
        "args": [
          86
        ],
        "expected": 44
      }
    ],
    "requiredAstOperators": [
      "RShift"
    ]
  },
  "3379": {
    "functionNames": [
      "scaled_right_2_bitwise"
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
          19
        ],
        "expected": 5
      },
      {
        "args": [
          86
        ],
        "expected": 22
      }
    ],
    "requiredAstOperators": [
      "RShift"
    ]
  },
  "3380": {
    "functionNames": [
      "scaled_right_3_bitwise"
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
          19
        ],
        "expected": 3
      },
      {
        "args": [
          86
        ],
        "expected": 11
      }
    ],
    "requiredAstOperators": [
      "RShift"
    ]
  },
  "3381": {
    "functionNames": [
      "scaled_right_4_bitwise"
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
          19
        ],
        "expected": 2
      },
      {
        "args": [
          86
        ],
        "expected": 6
      }
    ],
    "requiredAstOperators": [
      "RShift"
    ]
  },
  "3382": {
    "functionNames": [
      "scaled_right_5_bitwise"
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
          19
        ],
        "expected": 1
      },
      {
        "args": [
          86
        ],
        "expected": 3
      }
    ],
    "requiredAstOperators": [
      "RShift"
    ]
  },
  "3383": {
    "functionNames": [
      "low_mask_1_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          19
        ],
        "expected": 1
      },
      {
        "args": [
          86
        ],
        "expected": 0
      }
    ],
    "requiredAstOperators": [
      "BitAnd"
    ]
  },
  "3384": {
    "functionNames": [
      "low_mask_2_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          19
        ],
        "expected": 3
      },
      {
        "args": [
          86
        ],
        "expected": 2
      }
    ],
    "requiredAstOperators": [
      "BitAnd"
    ]
  },
  "3385": {
    "functionNames": [
      "low_mask_3_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          19
        ],
        "expected": 3
      },
      {
        "args": [
          86
        ],
        "expected": 6
      }
    ],
    "requiredAstOperators": [
      "BitAnd"
    ]
  },
  "3386": {
    "functionNames": [
      "low_mask_4_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          19
        ],
        "expected": 3
      },
      {
        "args": [
          86
        ],
        "expected": 6
      }
    ],
    "requiredAstOperators": [
      "BitAnd"
    ]
  },
  "3387": {
    "functionNames": [
      "low_mask_5_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          19
        ],
        "expected": 19
      },
      {
        "args": [
          86
        ],
        "expected": 22
      }
    ],
    "requiredAstOperators": [
      "BitAnd"
    ]
  },
  "3388": {
    "functionNames": [
      "set_pair_0_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 3
      },
      {
        "args": [
          19
        ],
        "expected": 19
      },
      {
        "args": [
          86
        ],
        "expected": 87
      }
    ],
    "requiredAstOperators": [
      "BitOr"
    ]
  },
  "3389": {
    "functionNames": [
      "set_pair_1_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 6
      },
      {
        "args": [
          19
        ],
        "expected": 23
      },
      {
        "args": [
          86
        ],
        "expected": 86
      }
    ],
    "requiredAstOperators": [
      "BitOr"
    ]
  },
  "3390": {
    "functionNames": [
      "set_pair_2_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 12
      },
      {
        "args": [
          19
        ],
        "expected": 31
      },
      {
        "args": [
          86
        ],
        "expected": 94
      }
    ],
    "requiredAstOperators": [
      "BitOr"
    ]
  },
  "3391": {
    "functionNames": [
      "set_pair_3_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 24
      },
      {
        "args": [
          19
        ],
        "expected": 27
      },
      {
        "args": [
          86
        ],
        "expected": 94
      }
    ],
    "requiredAstOperators": [
      "BitOr"
    ]
  },
  "3392": {
    "functionNames": [
      "set_pair_4_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 48
      },
      {
        "args": [
          19
        ],
        "expected": 51
      },
      {
        "args": [
          86
        ],
        "expected": 118
      }
    ],
    "requiredAstOperators": [
      "BitOr"
    ]
  },
  "3393": {
    "functionNames": [
      "clear_pair_0_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          19
        ],
        "expected": 16
      },
      {
        "args": [
          86
        ],
        "expected": 84
      }
    ],
    "requiredAstOperators": [
      "BitAnd"
    ]
  },
  "3394": {
    "functionNames": [
      "clear_pair_1_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          19
        ],
        "expected": 17
      },
      {
        "args": [
          86
        ],
        "expected": 80
      }
    ],
    "requiredAstOperators": [
      "BitAnd"
    ]
  },
  "3395": {
    "functionNames": [
      "clear_pair_2_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          19
        ],
        "expected": 19
      },
      {
        "args": [
          86
        ],
        "expected": 82
      }
    ],
    "requiredAstOperators": [
      "BitAnd"
    ]
  },
  "3396": {
    "functionNames": [
      "clear_pair_3_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          19
        ],
        "expected": 3
      },
      {
        "args": [
          86
        ],
        "expected": 70
      }
    ],
    "requiredAstOperators": [
      "BitAnd"
    ]
  },
  "3397": {
    "functionNames": [
      "clear_pair_4_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          19
        ],
        "expected": 3
      },
      {
        "args": [
          86
        ],
        "expected": 70
      }
    ],
    "requiredAstOperators": [
      "BitAnd"
    ]
  },
  "3398": {
    "functionNames": [
      "toggle_pair_0_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 3
      },
      {
        "args": [
          19
        ],
        "expected": 16
      },
      {
        "args": [
          86
        ],
        "expected": 85
      }
    ],
    "requiredAstOperators": [
      "BitXor"
    ]
  },
  "3399": {
    "functionNames": [
      "toggle_pair_1_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 6
      },
      {
        "args": [
          19
        ],
        "expected": 21
      },
      {
        "args": [
          86
        ],
        "expected": 80
      }
    ],
    "requiredAstOperators": [
      "BitXor"
    ]
  },
  "3400": {
    "functionNames": [
      "toggle_pair_2_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 12
      },
      {
        "args": [
          19
        ],
        "expected": 31
      },
      {
        "args": [
          86
        ],
        "expected": 90
      }
    ],
    "requiredAstOperators": [
      "BitXor"
    ]
  },
  "3401": {
    "functionNames": [
      "toggle_pair_3_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 24
      },
      {
        "args": [
          19
        ],
        "expected": 11
      },
      {
        "args": [
          86
        ],
        "expected": 78
      }
    ],
    "requiredAstOperators": [
      "BitXor"
    ]
  },
  "3402": {
    "functionNames": [
      "toggle_pair_4_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 48
      },
      {
        "args": [
          19
        ],
        "expected": 35
      },
      {
        "args": [
          86
        ],
        "expected": 102
      }
    ],
    "requiredAstOperators": [
      "BitXor"
    ]
  },
  "3403": {
    "functionNames": [
      "shift_mask_0_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          19
        ],
        "expected": 3
      },
      {
        "args": [
          86
        ],
        "expected": 6
      }
    ],
    "requiredAstOperators": [
      "RShift"
    ]
  },
  "3404": {
    "functionNames": [
      "shift_mask_1_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          19
        ],
        "expected": 9
      },
      {
        "args": [
          86
        ],
        "expected": 11
      }
    ],
    "requiredAstOperators": [
      "RShift"
    ]
  },
  "3405": {
    "functionNames": [
      "shift_mask_2_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          19
        ],
        "expected": 4
      },
      {
        "args": [
          86
        ],
        "expected": 5
      }
    ],
    "requiredAstOperators": [
      "RShift"
    ]
  },
  "3406": {
    "functionNames": [
      "shift_mask_3_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          19
        ],
        "expected": 2
      },
      {
        "args": [
          86
        ],
        "expected": 10
      }
    ],
    "requiredAstOperators": [
      "RShift"
    ]
  },
  "3407": {
    "functionNames": [
      "shift_mask_4_bitwise"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          19
        ],
        "expected": 1
      },
      {
        "args": [
          86
        ],
        "expected": 5
      }
    ],
    "requiredAstOperators": [
      "RShift"
    ]
  },
  "3408": {
    "functionNames": [
      "typed_double"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 10
      },
      {
        "args": [
          -4
        ],
        "expected": -8
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3409": {
    "functionNames": [
      "typed_triple"
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
          -4
        ],
        "expected": -12
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3410": {
    "functionNames": [
      "typed_square"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 25
      },
      {
        "args": [
          -4
        ],
        "expected": 16
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3411": {
    "functionNames": [
      "typed_cube"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 125
      },
      {
        "args": [
          -4
        ],
        "expected": -64
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3412": {
    "functionNames": [
      "typed_increment"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 6
      },
      {
        "args": [
          -4
        ],
        "expected": -3
      },
      {
        "args": [
          0
        ],
        "expected": 1
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3413": {
    "functionNames": [
      "typed_decrement"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 4
      },
      {
        "args": [
          -4
        ],
        "expected": -5
      },
      {
        "args": [
          0
        ],
        "expected": -1
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3414": {
    "functionNames": [
      "typed_negate"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": -5
      },
      {
        "args": [
          -4
        ],
        "expected": 4
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3415": {
    "functionNames": [
      "typed_absolute"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 4
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3416": {
    "functionNames": [
      "typed_half"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 2.5
      },
      {
        "args": [
          -4
        ],
        "expected": -2
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3417": {
    "functionNames": [
      "typed_remainder_three"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 2
      },
      {
        "args": [
          -4
        ],
        "expected": 2
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3418": {
    "functionNames": [
      "typed_last_digit"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 6
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3419": {
    "functionNames": [
      "typed_distance_ten"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 14
      },
      {
        "args": [
          0
        ],
        "expected": 10
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3420": {
    "functionNames": [
      "typed_clamp_zero"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 0
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3421": {
    "functionNames": [
      "typed_is_even"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": false
      },
      {
        "args": [
          -4
        ],
        "expected": true
      },
      {
        "args": [
          0
        ],
        "expected": true
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3422": {
    "functionNames": [
      "typed_is_positive"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": true
      },
      {
        "args": [
          -4
        ],
        "expected": false
      },
      {
        "args": [
          0
        ],
        "expected": false
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3423": {
    "functionNames": [
      "typed_sign_label"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": "positive"
      },
      {
        "args": [
          -4
        ],
        "expected": "negative"
      },
      {
        "args": [
          0
        ],
        "expected": "zero"
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3424": {
    "functionNames": [
      "typed_digit_count"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 1
      },
      {
        "args": [
          -4
        ],
        "expected": 1
      },
      {
        "args": [
          0
        ],
        "expected": 1
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3425": {
    "functionNames": [
      "typed_digit_sum"
    ],
    "tests": [
      {
        "args": [
          52
        ],
        "expected": 7
      },
      {
        "args": [
          -407
        ],
        "expected": 11
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3426": {
    "functionNames": [
      "typed_triangular"
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
          -4
        ],
        "expected": 10
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3427": {
    "functionNames": [
      "typed_within_ten"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": true
      },
      {
        "args": [
          -14
        ],
        "expected": false
      },
      {
        "args": [
          10
        ],
        "expected": true
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3428": {
    "functionNames": [
      "typed_uppercase"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "PYTHON"
      },
      {
        "args": [
          "level"
        ],
        "expected": "LEVEL"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "A B C"
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3429": {
    "functionNames": [
      "typed_lowercase"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "a b c"
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3430": {
    "functionNames": [
      "typed_reverse_text"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "nohtyP"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "c b a"
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3431": {
    "functionNames": [
      "typed_text_length"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": 6
      },
      {
        "args": [
          "level"
        ],
        "expected": 5
      },
      {
        "args": [
          "a b c"
        ],
        "expected": 5
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3432": {
    "functionNames": [
      "typed_first_character"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "P"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      },
      {
        "args": [
          "z"
        ],
        "expected": "z"
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3433": {
    "functionNames": [
      "typed_last_character"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "n"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      },
      {
        "args": [
          "z"
        ],
        "expected": "z"
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3434": {
    "functionNames": [
      "typed_vowel_count"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": 1
      },
      {
        "args": [
          "level"
        ],
        "expected": 2
      },
      {
        "args": [
          "a b c"
        ],
        "expected": 1
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3435": {
    "functionNames": [
      "typed_word_count"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": 1
      },
      {
        "args": [
          "level"
        ],
        "expected": 1
      },
      {
        "args": [
          "a b c"
        ],
        "expected": 3
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3436": {
    "functionNames": [
      "typed_remove_spaces"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "Python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "abc"
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3437": {
    "functionNames": [
      "typed_hyphenate"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "Python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "a-b-c"
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3438": {
    "functionNames": [
      "typed_title_words"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "Python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "Level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "A B C"
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3439": {
    "functionNames": [
      "typed_palindrome"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": false
      },
      {
        "args": [
          "level"
        ],
        "expected": true
      },
      {
        "args": [
          "a b c"
        ],
        "expected": false
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3440": {
    "functionNames": [
      "typed_digit_characters"
    ],
    "tests": [
      {
        "args": [
          "a1b2"
        ],
        "expected": 2
      },
      {
        "args": [
          "2026"
        ],
        "expected": 4
      },
      {
        "args": [
          "none"
        ],
        "expected": 0
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3441": {
    "functionNames": [
      "typed_initials"
    ],
    "tests": [
      {
        "args": [
          "python code"
        ],
        "expected": "PC"
      },
      {
        "args": [
          "Ada Lovelace"
        ],
        "expected": "AL"
      },
      {
        "args": [
          "solo"
        ],
        "expected": "S"
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3442": {
    "functionNames": [
      "typed_bracket_text"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "[Python]"
      },
      {
        "args": [
          "level"
        ],
        "expected": "[level]"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "[a b c]"
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3443": {
    "functionNames": [
      "typed_sum_items"
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
            0,
            5
          ]
        ],
        "expected": 3
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 7
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3444": {
    "functionNames": [
      "typed_maximum_item"
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
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 5
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 3
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3445": {
    "functionNames": [
      "typed_minimum_item"
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
        "expected": 1
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": -2
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 1
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3446": {
    "functionNames": [
      "typed_reverse_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          5,
          0,
          -2
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          1,
          3,
          3
        ]
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3447": {
    "functionNames": [
      "typed_sort_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          0,
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          1,
          3,
          3
        ]
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3448": {
    "functionNames": [
      "typed_unique_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          0,
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          1
        ]
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3449": {
    "functionNames": [
      "typed_even_items"
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
          2
        ]
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          0
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": []
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3450": {
    "functionNames": [
      "typed_odd_items"
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
          3
        ]
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": [
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          3,
          1
        ]
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3451": {
    "functionNames": [
      "typed_positive_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          3,
          1
        ]
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3452": {
    "functionNames": [
      "typed_square_items"
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
            0,
            5
          ]
        ],
        "expected": [
          4,
          0,
          25
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          9,
          9,
          1
        ]
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3453": {
    "functionNames": [
      "typed_item_count"
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
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 3
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 3
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3454": {
    "functionNames": [
      "typed_average_items"
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
        "expected": 2
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 1
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 2.3333333333333335
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3455": {
    "functionNames": [
      "typed_running_total"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          -2,
          3
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          6,
          7
        ]
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3456": {
    "functionNames": [
      "typed_index_pairs"
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
          ]
        ]
      },
      {
        "args": [
          [
            -2,
            0,
            5
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
            5
          ]
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          [
            0,
            3
          ],
          [
            1,
            3
          ],
          [
            2,
            1
          ]
        ]
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3457": {
    "functionNames": [
      "typed_nonzero_count"
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
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 2
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 3
      }
    ],
    "requiredTypeHints": {
      "minParameters": 1,
      "requireReturn": true
    }
  },
  "3458": {
    "functionNames": [
      "validated_double"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 10
      },
      {
        "args": [
          -4
        ],
        "expected": -8
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3459": {
    "functionNames": [
      "validated_triple"
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
          -4
        ],
        "expected": -12
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3460": {
    "functionNames": [
      "validated_square"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 25
      },
      {
        "args": [
          -4
        ],
        "expected": 16
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3461": {
    "functionNames": [
      "validated_cube"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 125
      },
      {
        "args": [
          -4
        ],
        "expected": -64
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3462": {
    "functionNames": [
      "validated_increment"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 6
      },
      {
        "args": [
          -4
        ],
        "expected": -3
      },
      {
        "args": [
          0
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3463": {
    "functionNames": [
      "validated_decrement"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 4
      },
      {
        "args": [
          -4
        ],
        "expected": -5
      },
      {
        "args": [
          0
        ],
        "expected": -1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3464": {
    "functionNames": [
      "validated_negate"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": -5
      },
      {
        "args": [
          -4
        ],
        "expected": 4
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3465": {
    "functionNames": [
      "validated_absolute"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 4
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3466": {
    "functionNames": [
      "validated_half"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 2.5
      },
      {
        "args": [
          -4
        ],
        "expected": -2
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3467": {
    "functionNames": [
      "validated_remainder_three"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 2
      },
      {
        "args": [
          -4
        ],
        "expected": 2
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3468": {
    "functionNames": [
      "validated_last_digit"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 6
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3469": {
    "functionNames": [
      "validated_distance_ten"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 14
      },
      {
        "args": [
          0
        ],
        "expected": 10
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3470": {
    "functionNames": [
      "validated_clamp_zero"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 0
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3471": {
    "functionNames": [
      "validated_is_even"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": false
      },
      {
        "args": [
          -4
        ],
        "expected": true
      },
      {
        "args": [
          0
        ],
        "expected": true
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3472": {
    "functionNames": [
      "validated_is_positive"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": true
      },
      {
        "args": [
          -4
        ],
        "expected": false
      },
      {
        "args": [
          0
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3473": {
    "functionNames": [
      "validated_sign_label"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": "positive"
      },
      {
        "args": [
          -4
        ],
        "expected": "negative"
      },
      {
        "args": [
          0
        ],
        "expected": "zero"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3474": {
    "functionNames": [
      "validated_digit_count"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 1
      },
      {
        "args": [
          -4
        ],
        "expected": 1
      },
      {
        "args": [
          0
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3475": {
    "functionNames": [
      "validated_digit_sum"
    ],
    "tests": [
      {
        "args": [
          52
        ],
        "expected": 7
      },
      {
        "args": [
          -407
        ],
        "expected": 11
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3476": {
    "functionNames": [
      "validated_triangular"
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
          -4
        ],
        "expected": 10
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3477": {
    "functionNames": [
      "validated_within_ten"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": true
      },
      {
        "args": [
          -14
        ],
        "expected": false
      },
      {
        "args": [
          10
        ],
        "expected": true
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3478": {
    "functionNames": [
      "validated_uppercase"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "PYTHON"
      },
      {
        "args": [
          "level"
        ],
        "expected": "LEVEL"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "A B C"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3479": {
    "functionNames": [
      "validated_lowercase"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "a b c"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3480": {
    "functionNames": [
      "validated_reverse_text"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "nohtyP"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "c b a"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3481": {
    "functionNames": [
      "validated_text_length"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": 6
      },
      {
        "args": [
          "level"
        ],
        "expected": 5
      },
      {
        "args": [
          "a b c"
        ],
        "expected": 5
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3482": {
    "functionNames": [
      "validated_first_character"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "P"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      },
      {
        "args": [
          "z"
        ],
        "expected": "z"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3483": {
    "functionNames": [
      "validated_last_character"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "n"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      },
      {
        "args": [
          "z"
        ],
        "expected": "z"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3484": {
    "functionNames": [
      "validated_vowel_count"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": 1
      },
      {
        "args": [
          "level"
        ],
        "expected": 2
      },
      {
        "args": [
          "a b c"
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3485": {
    "functionNames": [
      "validated_word_count"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": 1
      },
      {
        "args": [
          "level"
        ],
        "expected": 1
      },
      {
        "args": [
          "a b c"
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3486": {
    "functionNames": [
      "validated_remove_spaces"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "Python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "abc"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3487": {
    "functionNames": [
      "validated_hyphenate"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "Python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "a-b-c"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3488": {
    "functionNames": [
      "validated_title_words"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "Python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "Level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "A B C"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3489": {
    "functionNames": [
      "validated_palindrome"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": false
      },
      {
        "args": [
          "level"
        ],
        "expected": true
      },
      {
        "args": [
          "a b c"
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3490": {
    "functionNames": [
      "validated_digit_characters"
    ],
    "tests": [
      {
        "args": [
          "a1b2"
        ],
        "expected": 2
      },
      {
        "args": [
          "2026"
        ],
        "expected": 4
      },
      {
        "args": [
          "none"
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3491": {
    "functionNames": [
      "validated_initials"
    ],
    "tests": [
      {
        "args": [
          "python code"
        ],
        "expected": "PC"
      },
      {
        "args": [
          "Ada Lovelace"
        ],
        "expected": "AL"
      },
      {
        "args": [
          "solo"
        ],
        "expected": "S"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3492": {
    "functionNames": [
      "validated_bracket_text"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "[Python]"
      },
      {
        "args": [
          "level"
        ],
        "expected": "[level]"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "[a b c]"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3493": {
    "functionNames": [
      "validated_sum_items"
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
            0,
            5
          ]
        ],
        "expected": 3
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 7
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3494": {
    "functionNames": [
      "validated_maximum_item"
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
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 5
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3495": {
    "functionNames": [
      "validated_minimum_item"
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
        "expected": 1
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": -2
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3496": {
    "functionNames": [
      "validated_reverse_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          5,
          0,
          -2
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          1,
          3,
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3497": {
    "functionNames": [
      "validated_sort_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          0,
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          1,
          3,
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3498": {
    "functionNames": [
      "validated_unique_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          0,
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3499": {
    "functionNames": [
      "validated_even_items"
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
          2
        ]
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          0
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3500": {
    "functionNames": [
      "validated_odd_items"
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
          3
        ]
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": [
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          3,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3501": {
    "functionNames": [
      "validated_positive_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          3,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3502": {
    "functionNames": [
      "validated_square_items"
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
            0,
            5
          ]
        ],
        "expected": [
          4,
          0,
          25
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          9,
          9,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3503": {
    "functionNames": [
      "validated_item_count"
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
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 3
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3504": {
    "functionNames": [
      "validated_average_items"
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
        "expected": 2
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 1
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 2.3333333333333335
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3505": {
    "functionNames": [
      "validated_running_total"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          -2,
          3
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          6,
          7
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3506": {
    "functionNames": [
      "validated_index_pairs"
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
          ]
        ]
      },
      {
        "args": [
          [
            -2,
            0,
            5
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
            5
          ]
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          [
            0,
            3
          ],
          [
            1,
            3
          ],
          [
            2,
            1
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3507": {
    "functionNames": [
      "validated_nonzero_count"
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
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 2
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Assert"
      }
    ]
  },
  "3508": {
    "functionNames": [
      "nonlocal_double"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 10
      },
      {
        "args": [
          -4
        ],
        "expected": -8
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Nonlocal"
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ],
    "requiredDefinedFunctions": [
      "update"
    ]
  },
  "3509": {
    "functionNames": [
      "nonlocal_triple"
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
          -4
        ],
        "expected": -12
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Nonlocal"
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ],
    "requiredDefinedFunctions": [
      "update"
    ]
  },
  "3510": {
    "functionNames": [
      "nonlocal_square"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 25
      },
      {
        "args": [
          -4
        ],
        "expected": 16
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Nonlocal"
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ],
    "requiredDefinedFunctions": [
      "update"
    ]
  },
  "3511": {
    "functionNames": [
      "nonlocal_cube"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 125
      },
      {
        "args": [
          -4
        ],
        "expected": -64
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Nonlocal"
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ],
    "requiredDefinedFunctions": [
      "update"
    ]
  },
  "3512": {
    "functionNames": [
      "nonlocal_increment"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 6
      },
      {
        "args": [
          -4
        ],
        "expected": -3
      },
      {
        "args": [
          0
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Nonlocal"
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ],
    "requiredDefinedFunctions": [
      "update"
    ]
  },
  "3513": {
    "functionNames": [
      "nonlocal_decrement"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 4
      },
      {
        "args": [
          -4
        ],
        "expected": -5
      },
      {
        "args": [
          0
        ],
        "expected": -1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Nonlocal"
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ],
    "requiredDefinedFunctions": [
      "update"
    ]
  },
  "3514": {
    "functionNames": [
      "nonlocal_negate"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": -5
      },
      {
        "args": [
          -4
        ],
        "expected": 4
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Nonlocal"
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ],
    "requiredDefinedFunctions": [
      "update"
    ]
  },
  "3515": {
    "functionNames": [
      "nonlocal_absolute"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 4
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Nonlocal"
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ],
    "requiredDefinedFunctions": [
      "update"
    ]
  },
  "3516": {
    "functionNames": [
      "nonlocal_half"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 2.5
      },
      {
        "args": [
          -4
        ],
        "expected": -2
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Nonlocal"
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ],
    "requiredDefinedFunctions": [
      "update"
    ]
  },
  "3517": {
    "functionNames": [
      "nonlocal_remainder_three"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 2
      },
      {
        "args": [
          -4
        ],
        "expected": 2
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Nonlocal"
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ],
    "requiredDefinedFunctions": [
      "update"
    ]
  },
  "3518": {
    "functionNames": [
      "nonlocal_last_digit"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 6
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Nonlocal"
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ],
    "requiredDefinedFunctions": [
      "update"
    ]
  },
  "3519": {
    "functionNames": [
      "nonlocal_distance_ten"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 14
      },
      {
        "args": [
          0
        ],
        "expected": 10
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Nonlocal"
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ],
    "requiredDefinedFunctions": [
      "update"
    ]
  },
  "3520": {
    "functionNames": [
      "nonlocal_clamp_zero"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 0
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Nonlocal"
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ],
    "requiredDefinedFunctions": [
      "update"
    ]
  },
  "3521": {
    "functionNames": [
      "nonlocal_is_even"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": false
      },
      {
        "args": [
          -4
        ],
        "expected": true
      },
      {
        "args": [
          0
        ],
        "expected": true
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Nonlocal"
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ],
    "requiredDefinedFunctions": [
      "update"
    ]
  },
  "3522": {
    "functionNames": [
      "nonlocal_is_positive"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": true
      },
      {
        "args": [
          -4
        ],
        "expected": false
      },
      {
        "args": [
          0
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Nonlocal"
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ],
    "requiredDefinedFunctions": [
      "update"
    ]
  },
  "3523": {
    "functionNames": [
      "nonlocal_sign_label"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": "positive"
      },
      {
        "args": [
          -4
        ],
        "expected": "negative"
      },
      {
        "args": [
          0
        ],
        "expected": "zero"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Nonlocal"
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ],
    "requiredDefinedFunctions": [
      "update"
    ]
  },
  "3524": {
    "functionNames": [
      "nonlocal_digit_count"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 1
      },
      {
        "args": [
          -4
        ],
        "expected": 1
      },
      {
        "args": [
          0
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Nonlocal"
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ],
    "requiredDefinedFunctions": [
      "update"
    ]
  },
  "3525": {
    "functionNames": [
      "nonlocal_digit_sum"
    ],
    "tests": [
      {
        "args": [
          52
        ],
        "expected": 7
      },
      {
        "args": [
          -407
        ],
        "expected": 11
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Nonlocal"
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ],
    "requiredDefinedFunctions": [
      "update"
    ]
  },
  "3526": {
    "functionNames": [
      "nonlocal_triangular"
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
          -4
        ],
        "expected": 10
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Nonlocal"
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ],
    "requiredDefinedFunctions": [
      "update"
    ]
  },
  "3527": {
    "functionNames": [
      "nonlocal_within_ten"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": true
      },
      {
        "args": [
          -14
        ],
        "expected": false
      },
      {
        "args": [
          10
        ],
        "expected": true
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Nonlocal"
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ],
    "requiredDefinedFunctions": [
      "update"
    ]
  },
  "3528": {
    "functionNames": [
      "nonlocal_uppercase"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "PYTHON"
      },
      {
        "args": [
          "level"
        ],
        "expected": "LEVEL"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "A B C"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Nonlocal"
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ],
    "requiredDefinedFunctions": [
      "update"
    ]
  },
  "3529": {
    "functionNames": [
      "nonlocal_lowercase"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "a b c"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Nonlocal"
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ],
    "requiredDefinedFunctions": [
      "update"
    ]
  },
  "3530": {
    "functionNames": [
      "nonlocal_reverse_text"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "nohtyP"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "c b a"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Nonlocal"
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ],
    "requiredDefinedFunctions": [
      "update"
    ]
  },
  "3531": {
    "functionNames": [
      "nonlocal_text_length"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": 6
      },
      {
        "args": [
          "level"
        ],
        "expected": 5
      },
      {
        "args": [
          "a b c"
        ],
        "expected": 5
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Nonlocal"
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ],
    "requiredDefinedFunctions": [
      "update"
    ]
  },
  "3532": {
    "functionNames": [
      "nonlocal_first_character"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "P"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      },
      {
        "args": [
          "z"
        ],
        "expected": "z"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Nonlocal"
      },
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ],
    "requiredDefinedFunctions": [
      "update"
    ]
  },
  "3533": {
    "functionNames": [
      "global_last_character"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "n"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      },
      {
        "args": [
          "z"
        ],
        "expected": "z"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Global"
      }
    ]
  },
  "3534": {
    "functionNames": [
      "global_vowel_count"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": 1
      },
      {
        "args": [
          "level"
        ],
        "expected": 2
      },
      {
        "args": [
          "a b c"
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Global"
      }
    ]
  },
  "3535": {
    "functionNames": [
      "global_word_count"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": 1
      },
      {
        "args": [
          "level"
        ],
        "expected": 1
      },
      {
        "args": [
          "a b c"
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Global"
      }
    ]
  },
  "3536": {
    "functionNames": [
      "global_remove_spaces"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "Python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "abc"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Global"
      }
    ]
  },
  "3537": {
    "functionNames": [
      "global_hyphenate"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "Python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "a-b-c"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Global"
      }
    ]
  },
  "3538": {
    "functionNames": [
      "global_title_words"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "Python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "Level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "A B C"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Global"
      }
    ]
  },
  "3539": {
    "functionNames": [
      "global_palindrome"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": false
      },
      {
        "args": [
          "level"
        ],
        "expected": true
      },
      {
        "args": [
          "a b c"
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Global"
      }
    ]
  },
  "3540": {
    "functionNames": [
      "global_digit_characters"
    ],
    "tests": [
      {
        "args": [
          "a1b2"
        ],
        "expected": 2
      },
      {
        "args": [
          "2026"
        ],
        "expected": 4
      },
      {
        "args": [
          "none"
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Global"
      }
    ]
  },
  "3541": {
    "functionNames": [
      "global_initials"
    ],
    "tests": [
      {
        "args": [
          "python code"
        ],
        "expected": "PC"
      },
      {
        "args": [
          "Ada Lovelace"
        ],
        "expected": "AL"
      },
      {
        "args": [
          "solo"
        ],
        "expected": "S"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Global"
      }
    ]
  },
  "3542": {
    "functionNames": [
      "global_bracket_text"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "[Python]"
      },
      {
        "args": [
          "level"
        ],
        "expected": "[level]"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "[a b c]"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Global"
      }
    ]
  },
  "3543": {
    "functionNames": [
      "global_sum_items"
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
            0,
            5
          ]
        ],
        "expected": 3
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 7
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Global"
      }
    ]
  },
  "3544": {
    "functionNames": [
      "global_maximum_item"
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
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 5
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Global"
      }
    ]
  },
  "3545": {
    "functionNames": [
      "global_minimum_item"
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
        "expected": 1
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": -2
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Global"
      }
    ]
  },
  "3546": {
    "functionNames": [
      "global_reverse_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          5,
          0,
          -2
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          1,
          3,
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Global"
      }
    ]
  },
  "3547": {
    "functionNames": [
      "global_sort_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          0,
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          1,
          3,
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Global"
      }
    ]
  },
  "3548": {
    "functionNames": [
      "global_unique_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          0,
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Global"
      }
    ]
  },
  "3549": {
    "functionNames": [
      "global_even_items"
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
          2
        ]
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          0
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Global"
      }
    ]
  },
  "3550": {
    "functionNames": [
      "global_odd_items"
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
          3
        ]
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": [
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          3,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Global"
      }
    ]
  },
  "3551": {
    "functionNames": [
      "global_positive_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          3,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Global"
      }
    ]
  },
  "3552": {
    "functionNames": [
      "global_square_items"
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
            0,
            5
          ]
        ],
        "expected": [
          4,
          0,
          25
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          9,
          9,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Global"
      }
    ]
  },
  "3553": {
    "functionNames": [
      "global_item_count"
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
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 3
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Global"
      }
    ]
  },
  "3554": {
    "functionNames": [
      "global_average_items"
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
        "expected": 2
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 1
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 2.3333333333333335
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Global"
      }
    ]
  },
  "3555": {
    "functionNames": [
      "global_running_total"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          -2,
          3
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          6,
          7
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Global"
      }
    ]
  },
  "3556": {
    "functionNames": [
      "global_index_pairs"
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
          ]
        ]
      },
      {
        "args": [
          [
            -2,
            0,
            5
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
            5
          ]
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          [
            0,
            3
          ],
          [
            1,
            3
          ],
          [
            2,
            1
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Global"
      }
    ]
  },
  "3557": {
    "functionNames": [
      "global_nonzero_count"
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
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 2
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Global"
      }
    ]
  },
  "3558": {
    "functionNames": [
      "matched_double"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 10
      },
      {
        "args": [
          -4
        ],
        "expected": -8
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3559": {
    "functionNames": [
      "matched_triple"
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
          -4
        ],
        "expected": -12
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3560": {
    "functionNames": [
      "matched_square"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 25
      },
      {
        "args": [
          -4
        ],
        "expected": 16
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3561": {
    "functionNames": [
      "matched_cube"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 125
      },
      {
        "args": [
          -4
        ],
        "expected": -64
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3562": {
    "functionNames": [
      "matched_increment"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 6
      },
      {
        "args": [
          -4
        ],
        "expected": -3
      },
      {
        "args": [
          0
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3563": {
    "functionNames": [
      "matched_decrement"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 4
      },
      {
        "args": [
          -4
        ],
        "expected": -5
      },
      {
        "args": [
          0
        ],
        "expected": -1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3564": {
    "functionNames": [
      "matched_negate"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": -5
      },
      {
        "args": [
          -4
        ],
        "expected": 4
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3565": {
    "functionNames": [
      "matched_absolute"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 4
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3566": {
    "functionNames": [
      "matched_half"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 2.5
      },
      {
        "args": [
          -4
        ],
        "expected": -2
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3567": {
    "functionNames": [
      "matched_remainder_three"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 2
      },
      {
        "args": [
          -4
        ],
        "expected": 2
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3568": {
    "functionNames": [
      "matched_last_digit"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 6
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3569": {
    "functionNames": [
      "matched_distance_ten"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 14
      },
      {
        "args": [
          0
        ],
        "expected": 10
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3570": {
    "functionNames": [
      "matched_clamp_zero"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          -4
        ],
        "expected": 0
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3571": {
    "functionNames": [
      "matched_is_even"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": false
      },
      {
        "args": [
          -4
        ],
        "expected": true
      },
      {
        "args": [
          0
        ],
        "expected": true
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3572": {
    "functionNames": [
      "matched_is_positive"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": true
      },
      {
        "args": [
          -4
        ],
        "expected": false
      },
      {
        "args": [
          0
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3573": {
    "functionNames": [
      "matched_sign_label"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": "positive"
      },
      {
        "args": [
          -4
        ],
        "expected": "negative"
      },
      {
        "args": [
          0
        ],
        "expected": "zero"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3574": {
    "functionNames": [
      "matched_digit_count"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 1
      },
      {
        "args": [
          -4
        ],
        "expected": 1
      },
      {
        "args": [
          0
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3575": {
    "functionNames": [
      "matched_digit_sum"
    ],
    "tests": [
      {
        "args": [
          52
        ],
        "expected": 7
      },
      {
        "args": [
          -407
        ],
        "expected": 11
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3576": {
    "functionNames": [
      "matched_triangular"
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
          -4
        ],
        "expected": 10
      },
      {
        "args": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3577": {
    "functionNames": [
      "matched_within_ten"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": true
      },
      {
        "args": [
          -14
        ],
        "expected": false
      },
      {
        "args": [
          10
        ],
        "expected": true
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3578": {
    "functionNames": [
      "matched_uppercase"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "PYTHON"
      },
      {
        "args": [
          "level"
        ],
        "expected": "LEVEL"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "A B C"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3579": {
    "functionNames": [
      "matched_lowercase"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "a b c"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3580": {
    "functionNames": [
      "matched_reverse_text"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "nohtyP"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "c b a"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3581": {
    "functionNames": [
      "matched_text_length"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": 6
      },
      {
        "args": [
          "level"
        ],
        "expected": 5
      },
      {
        "args": [
          "a b c"
        ],
        "expected": 5
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3582": {
    "functionNames": [
      "matched_first_character"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "P"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      },
      {
        "args": [
          "z"
        ],
        "expected": "z"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3583": {
    "functionNames": [
      "matched_last_character"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "n"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      },
      {
        "args": [
          "z"
        ],
        "expected": "z"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3584": {
    "functionNames": [
      "matched_vowel_count"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": 1
      },
      {
        "args": [
          "level"
        ],
        "expected": 2
      },
      {
        "args": [
          "a b c"
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3585": {
    "functionNames": [
      "matched_word_count"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": 1
      },
      {
        "args": [
          "level"
        ],
        "expected": 1
      },
      {
        "args": [
          "a b c"
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3586": {
    "functionNames": [
      "matched_remove_spaces"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "Python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "abc"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3587": {
    "functionNames": [
      "matched_hyphenate"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "Python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "a-b-c"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3588": {
    "functionNames": [
      "matched_title_words"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "Python"
      },
      {
        "args": [
          "level"
        ],
        "expected": "Level"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "A B C"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3589": {
    "functionNames": [
      "matched_palindrome"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": false
      },
      {
        "args": [
          "level"
        ],
        "expected": true
      },
      {
        "args": [
          "a b c"
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3590": {
    "functionNames": [
      "matched_digit_characters"
    ],
    "tests": [
      {
        "args": [
          "a1b2"
        ],
        "expected": 2
      },
      {
        "args": [
          "2026"
        ],
        "expected": 4
      },
      {
        "args": [
          "none"
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3591": {
    "functionNames": [
      "matched_initials"
    ],
    "tests": [
      {
        "args": [
          "python code"
        ],
        "expected": "PC"
      },
      {
        "args": [
          "Ada Lovelace"
        ],
        "expected": "AL"
      },
      {
        "args": [
          "solo"
        ],
        "expected": "S"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3592": {
    "functionNames": [
      "matched_bracket_text"
    ],
    "tests": [
      {
        "args": [
          "Python"
        ],
        "expected": "[Python]"
      },
      {
        "args": [
          "level"
        ],
        "expected": "[level]"
      },
      {
        "args": [
          "a b c"
        ],
        "expected": "[a b c]"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3593": {
    "functionNames": [
      "matched_sum_items"
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
            0,
            5
          ]
        ],
        "expected": 3
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 7
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3594": {
    "functionNames": [
      "matched_maximum_item"
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
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 5
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3595": {
    "functionNames": [
      "matched_minimum_item"
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
        "expected": 1
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": -2
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3596": {
    "functionNames": [
      "matched_reverse_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          5,
          0,
          -2
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          1,
          3,
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3597": {
    "functionNames": [
      "matched_sort_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          0,
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          1,
          3,
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3598": {
    "functionNames": [
      "matched_unique_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          0,
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3599": {
    "functionNames": [
      "matched_even_items"
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
          2
        ]
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          0
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3600": {
    "functionNames": [
      "matched_odd_items"
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
          3
        ]
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": [
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          3,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3601": {
    "functionNames": [
      "matched_positive_items"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          5
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          3,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3602": {
    "functionNames": [
      "matched_square_items"
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
            0,
            5
          ]
        ],
        "expected": [
          4,
          0,
          25
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          9,
          9,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3603": {
    "functionNames": [
      "matched_item_count"
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
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 3
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3604": {
    "functionNames": [
      "matched_average_items"
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
        "expected": 2
      },
      {
        "args": [
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 1
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 2.3333333333333335
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3605": {
    "functionNames": [
      "matched_running_total"
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
            -2,
            0,
            5
          ]
        ],
        "expected": [
          -2,
          -2,
          3
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          3,
          6,
          7
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3606": {
    "functionNames": [
      "matched_index_pairs"
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
          ]
        ]
      },
      {
        "args": [
          [
            -2,
            0,
            5
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
            5
          ]
        ]
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": [
          [
            0,
            3
          ],
          [
            1,
            3
          ],
          [
            2,
            1
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3607": {
    "functionNames": [
      "matched_nonzero_count"
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
          [
            -2,
            0,
            5
          ]
        ],
        "expected": 2
      },
      {
        "args": [
          [
            3,
            3,
            1
          ]
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Match"
      },
      {
        "nodeType": "match_case"
      }
    ]
  },
  "3608": {
    "functionNames": [
      "add_1_days"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15"
        ],
        "expected": "2024-01-16"
      },
      {
        "args": [
          "2024-02-28"
        ],
        "expected": "2024-02-29"
      },
      {
        "args": [
          "2025-12-30"
        ],
        "expected": "2025-12-31"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3609": {
    "functionNames": [
      "subtract_1_days"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15"
        ],
        "expected": "2024-01-14"
      },
      {
        "args": [
          "2024-02-28"
        ],
        "expected": "2024-02-27"
      },
      {
        "args": [
          "2025-12-30"
        ],
        "expected": "2025-12-29"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3610": {
    "functionNames": [
      "weekday_after_1_days"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15"
        ],
        "expected": "Tuesday"
      },
      {
        "args": [
          "2024-02-28"
        ],
        "expected": "Thursday"
      },
      {
        "args": [
          "2025-12-30"
        ],
        "expected": "Wednesday"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3611": {
    "functionNames": [
      "day_number_after_1"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15"
        ],
        "expected": 16
      },
      {
        "args": [
          "2024-02-28"
        ],
        "expected": 60
      },
      {
        "args": [
          "2025-12-30"
        ],
        "expected": 365
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3612": {
    "functionNames": [
      "add_2_days"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15"
        ],
        "expected": "2024-01-17"
      },
      {
        "args": [
          "2024-02-28"
        ],
        "expected": "2024-03-01"
      },
      {
        "args": [
          "2025-12-30"
        ],
        "expected": "2026-01-01"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3613": {
    "functionNames": [
      "subtract_2_days"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15"
        ],
        "expected": "2024-01-13"
      },
      {
        "args": [
          "2024-02-28"
        ],
        "expected": "2024-02-26"
      },
      {
        "args": [
          "2025-12-30"
        ],
        "expected": "2025-12-28"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3614": {
    "functionNames": [
      "weekday_after_2_days"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15"
        ],
        "expected": "Wednesday"
      },
      {
        "args": [
          "2024-02-28"
        ],
        "expected": "Friday"
      },
      {
        "args": [
          "2025-12-30"
        ],
        "expected": "Thursday"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3615": {
    "functionNames": [
      "day_number_after_2"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15"
        ],
        "expected": 17
      },
      {
        "args": [
          "2024-02-28"
        ],
        "expected": 61
      },
      {
        "args": [
          "2025-12-30"
        ],
        "expected": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3616": {
    "functionNames": [
      "add_3_days"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15"
        ],
        "expected": "2024-01-18"
      },
      {
        "args": [
          "2024-02-28"
        ],
        "expected": "2024-03-02"
      },
      {
        "args": [
          "2025-12-30"
        ],
        "expected": "2026-01-02"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3617": {
    "functionNames": [
      "subtract_3_days"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15"
        ],
        "expected": "2024-01-12"
      },
      {
        "args": [
          "2024-02-28"
        ],
        "expected": "2024-02-25"
      },
      {
        "args": [
          "2025-12-30"
        ],
        "expected": "2025-12-27"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3618": {
    "functionNames": [
      "weekday_after_3_days"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15"
        ],
        "expected": "Thursday"
      },
      {
        "args": [
          "2024-02-28"
        ],
        "expected": "Saturday"
      },
      {
        "args": [
          "2025-12-30"
        ],
        "expected": "Friday"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3619": {
    "functionNames": [
      "day_number_after_3"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15"
        ],
        "expected": 18
      },
      {
        "args": [
          "2024-02-28"
        ],
        "expected": 62
      },
      {
        "args": [
          "2025-12-30"
        ],
        "expected": 2
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3620": {
    "functionNames": [
      "add_7_days"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15"
        ],
        "expected": "2024-01-22"
      },
      {
        "args": [
          "2024-02-28"
        ],
        "expected": "2024-03-06"
      },
      {
        "args": [
          "2025-12-30"
        ],
        "expected": "2026-01-06"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3621": {
    "functionNames": [
      "subtract_7_days"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15"
        ],
        "expected": "2024-01-08"
      },
      {
        "args": [
          "2024-02-28"
        ],
        "expected": "2024-02-21"
      },
      {
        "args": [
          "2025-12-30"
        ],
        "expected": "2025-12-23"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3622": {
    "functionNames": [
      "weekday_after_7_days"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15"
        ],
        "expected": "Monday"
      },
      {
        "args": [
          "2024-02-28"
        ],
        "expected": "Wednesday"
      },
      {
        "args": [
          "2025-12-30"
        ],
        "expected": "Tuesday"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3623": {
    "functionNames": [
      "day_number_after_7"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15"
        ],
        "expected": 22
      },
      {
        "args": [
          "2024-02-28"
        ],
        "expected": 66
      },
      {
        "args": [
          "2025-12-30"
        ],
        "expected": 6
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3624": {
    "functionNames": [
      "add_14_days"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15"
        ],
        "expected": "2024-01-29"
      },
      {
        "args": [
          "2024-02-28"
        ],
        "expected": "2024-03-13"
      },
      {
        "args": [
          "2025-12-30"
        ],
        "expected": "2026-01-13"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3625": {
    "functionNames": [
      "subtract_14_days"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15"
        ],
        "expected": "2024-01-01"
      },
      {
        "args": [
          "2024-02-28"
        ],
        "expected": "2024-02-14"
      },
      {
        "args": [
          "2025-12-30"
        ],
        "expected": "2025-12-16"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3626": {
    "functionNames": [
      "weekday_after_14_days"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15"
        ],
        "expected": "Monday"
      },
      {
        "args": [
          "2024-02-28"
        ],
        "expected": "Wednesday"
      },
      {
        "args": [
          "2025-12-30"
        ],
        "expected": "Tuesday"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3627": {
    "functionNames": [
      "day_number_after_14"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15"
        ],
        "expected": 29
      },
      {
        "args": [
          "2024-02-28"
        ],
        "expected": 73
      },
      {
        "args": [
          "2025-12-30"
        ],
        "expected": 13
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3628": {
    "functionNames": [
      "add_1_hours"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15T10:30"
        ],
        "expected": "2024-01-15T11:30"
      },
      {
        "args": [
          "2024-02-28T23:15"
        ],
        "expected": "2024-02-29T00:15"
      },
      {
        "args": [
          "2025-12-30T04:00"
        ],
        "expected": "2025-12-30T05:00"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3629": {
    "functionNames": [
      "subtract_1_hours"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15T10:30"
        ],
        "expected": "2024-01-15T09:30"
      },
      {
        "args": [
          "2024-02-28T23:15"
        ],
        "expected": "2024-02-28T22:15"
      },
      {
        "args": [
          "2025-12-30T04:00"
        ],
        "expected": "2025-12-30T03:00"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3630": {
    "functionNames": [
      "within_1_days"
    ],
    "tests": [
      {
        "args": [
          "2024-01-01",
          "2024-01-02"
        ],
        "expected": true
      },
      {
        "args": [
          "2024-01-01",
          "2024-01-03"
        ],
        "expected": false
      },
      {
        "args": [
          "2024-03-10",
          "2024-03-09"
        ],
        "expected": true
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3631": {
    "functionNames": [
      "days_apart_plus_1"
    ],
    "tests": [
      {
        "args": [
          "2024-01-01",
          "2024-01-10"
        ],
        "expected": 10
      },
      {
        "args": [
          "2024-02-28",
          "2024-03-01"
        ],
        "expected": 3
      },
      {
        "args": [
          "2025-12-31",
          "2025-12-30"
        ],
        "expected": 2
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3632": {
    "functionNames": [
      "year_after_1_days"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15"
        ],
        "expected": 2024
      },
      {
        "args": [
          "2024-02-28"
        ],
        "expected": 2024
      },
      {
        "args": [
          "2025-12-30"
        ],
        "expected": 2025
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3633": {
    "functionNames": [
      "month_after_1_days"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15"
        ],
        "expected": 1
      },
      {
        "args": [
          "2024-02-28"
        ],
        "expected": 2
      },
      {
        "args": [
          "2025-12-30"
        ],
        "expected": 12
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3634": {
    "functionNames": [
      "add_2_hours"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15T10:30"
        ],
        "expected": "2024-01-15T12:30"
      },
      {
        "args": [
          "2024-02-28T23:15"
        ],
        "expected": "2024-02-29T01:15"
      },
      {
        "args": [
          "2025-12-30T04:00"
        ],
        "expected": "2025-12-30T06:00"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3635": {
    "functionNames": [
      "subtract_2_hours"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15T10:30"
        ],
        "expected": "2024-01-15T08:30"
      },
      {
        "args": [
          "2024-02-28T23:15"
        ],
        "expected": "2024-02-28T21:15"
      },
      {
        "args": [
          "2025-12-30T04:00"
        ],
        "expected": "2025-12-30T02:00"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3636": {
    "functionNames": [
      "within_2_days"
    ],
    "tests": [
      {
        "args": [
          "2024-01-01",
          "2024-01-03"
        ],
        "expected": true
      },
      {
        "args": [
          "2024-01-01",
          "2024-01-04"
        ],
        "expected": false
      },
      {
        "args": [
          "2024-03-10",
          "2024-03-08"
        ],
        "expected": true
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3637": {
    "functionNames": [
      "days_apart_plus_2"
    ],
    "tests": [
      {
        "args": [
          "2024-01-01",
          "2024-01-10"
        ],
        "expected": 11
      },
      {
        "args": [
          "2024-02-28",
          "2024-03-01"
        ],
        "expected": 4
      },
      {
        "args": [
          "2025-12-31",
          "2025-12-30"
        ],
        "expected": 3
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3638": {
    "functionNames": [
      "year_after_2_days"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15"
        ],
        "expected": 2024
      },
      {
        "args": [
          "2024-02-28"
        ],
        "expected": 2024
      },
      {
        "args": [
          "2025-12-30"
        ],
        "expected": 2026
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3639": {
    "functionNames": [
      "month_after_2_days"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15"
        ],
        "expected": 1
      },
      {
        "args": [
          "2024-02-28"
        ],
        "expected": 3
      },
      {
        "args": [
          "2025-12-30"
        ],
        "expected": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3640": {
    "functionNames": [
      "add_6_hours"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15T10:30"
        ],
        "expected": "2024-01-15T16:30"
      },
      {
        "args": [
          "2024-02-28T23:15"
        ],
        "expected": "2024-02-29T05:15"
      },
      {
        "args": [
          "2025-12-30T04:00"
        ],
        "expected": "2025-12-30T10:00"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3641": {
    "functionNames": [
      "subtract_6_hours"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15T10:30"
        ],
        "expected": "2024-01-15T04:30"
      },
      {
        "args": [
          "2024-02-28T23:15"
        ],
        "expected": "2024-02-28T17:15"
      },
      {
        "args": [
          "2025-12-30T04:00"
        ],
        "expected": "2025-12-29T22:00"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3642": {
    "functionNames": [
      "within_6_days"
    ],
    "tests": [
      {
        "args": [
          "2024-01-01",
          "2024-01-07"
        ],
        "expected": true
      },
      {
        "args": [
          "2024-01-01",
          "2024-01-08"
        ],
        "expected": false
      },
      {
        "args": [
          "2024-03-10",
          "2024-03-04"
        ],
        "expected": true
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3643": {
    "functionNames": [
      "days_apart_plus_6"
    ],
    "tests": [
      {
        "args": [
          "2024-01-01",
          "2024-01-10"
        ],
        "expected": 15
      },
      {
        "args": [
          "2024-02-28",
          "2024-03-01"
        ],
        "expected": 8
      },
      {
        "args": [
          "2025-12-31",
          "2025-12-30"
        ],
        "expected": 7
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3644": {
    "functionNames": [
      "year_after_6_days"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15"
        ],
        "expected": 2024
      },
      {
        "args": [
          "2024-02-28"
        ],
        "expected": 2024
      },
      {
        "args": [
          "2025-12-30"
        ],
        "expected": 2026
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3645": {
    "functionNames": [
      "month_after_6_days"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15"
        ],
        "expected": 1
      },
      {
        "args": [
          "2024-02-28"
        ],
        "expected": 3
      },
      {
        "args": [
          "2025-12-30"
        ],
        "expected": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3646": {
    "functionNames": [
      "add_12_hours"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15T10:30"
        ],
        "expected": "2024-01-15T22:30"
      },
      {
        "args": [
          "2024-02-28T23:15"
        ],
        "expected": "2024-02-29T11:15"
      },
      {
        "args": [
          "2025-12-30T04:00"
        ],
        "expected": "2025-12-30T16:00"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3647": {
    "functionNames": [
      "subtract_12_hours"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15T10:30"
        ],
        "expected": "2024-01-14T22:30"
      },
      {
        "args": [
          "2024-02-28T23:15"
        ],
        "expected": "2024-02-28T11:15"
      },
      {
        "args": [
          "2025-12-30T04:00"
        ],
        "expected": "2025-12-29T16:00"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3648": {
    "functionNames": [
      "within_12_days"
    ],
    "tests": [
      {
        "args": [
          "2024-01-01",
          "2024-01-13"
        ],
        "expected": true
      },
      {
        "args": [
          "2024-01-01",
          "2024-01-14"
        ],
        "expected": false
      },
      {
        "args": [
          "2024-03-10",
          "2024-02-27"
        ],
        "expected": true
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3649": {
    "functionNames": [
      "days_apart_plus_12"
    ],
    "tests": [
      {
        "args": [
          "2024-01-01",
          "2024-01-10"
        ],
        "expected": 21
      },
      {
        "args": [
          "2024-02-28",
          "2024-03-01"
        ],
        "expected": 14
      },
      {
        "args": [
          "2025-12-31",
          "2025-12-30"
        ],
        "expected": 13
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3650": {
    "functionNames": [
      "year_after_12_days"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15"
        ],
        "expected": 2024
      },
      {
        "args": [
          "2024-02-28"
        ],
        "expected": 2024
      },
      {
        "args": [
          "2025-12-30"
        ],
        "expected": 2026
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3651": {
    "functionNames": [
      "month_after_12_days"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15"
        ],
        "expected": 1
      },
      {
        "args": [
          "2024-02-28"
        ],
        "expected": 3
      },
      {
        "args": [
          "2025-12-30"
        ],
        "expected": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3652": {
    "functionNames": [
      "add_24_hours"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15T10:30"
        ],
        "expected": "2024-01-16T10:30"
      },
      {
        "args": [
          "2024-02-28T23:15"
        ],
        "expected": "2024-02-29T23:15"
      },
      {
        "args": [
          "2025-12-30T04:00"
        ],
        "expected": "2025-12-31T04:00"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3653": {
    "functionNames": [
      "subtract_24_hours"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15T10:30"
        ],
        "expected": "2024-01-14T10:30"
      },
      {
        "args": [
          "2024-02-28T23:15"
        ],
        "expected": "2024-02-27T23:15"
      },
      {
        "args": [
          "2025-12-30T04:00"
        ],
        "expected": "2025-12-29T04:00"
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3654": {
    "functionNames": [
      "within_24_days"
    ],
    "tests": [
      {
        "args": [
          "2024-01-01",
          "2024-01-25"
        ],
        "expected": true
      },
      {
        "args": [
          "2024-01-01",
          "2024-01-26"
        ],
        "expected": false
      },
      {
        "args": [
          "2024-03-10",
          "2024-02-15"
        ],
        "expected": true
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3655": {
    "functionNames": [
      "days_apart_plus_24"
    ],
    "tests": [
      {
        "args": [
          "2024-01-01",
          "2024-01-10"
        ],
        "expected": 33
      },
      {
        "args": [
          "2024-02-28",
          "2024-03-01"
        ],
        "expected": 26
      },
      {
        "args": [
          "2025-12-31",
          "2025-12-30"
        ],
        "expected": 25
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3656": {
    "functionNames": [
      "year_after_24_days"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15"
        ],
        "expected": 2024
      },
      {
        "args": [
          "2024-02-28"
        ],
        "expected": 2024
      },
      {
        "args": [
          "2025-12-30"
        ],
        "expected": 2026
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  },
  "3657": {
    "functionNames": [
      "month_after_24_days"
    ],
    "tests": [
      {
        "args": [
          "2024-01-15"
        ],
        "expected": 2
      },
      {
        "args": [
          "2024-02-28"
        ],
        "expected": 3
      },
      {
        "args": [
          "2025-12-30"
        ],
        "expected": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "strptime",
        "minArgs": 1
      }
    ]
  }
};
