import type { AutoGrader } from './graders';

export const CONCEPT_LEVEL_EXPANSION_GRADERS: Record<number, AutoGrader> = {
  "6058": {
    "functionNames": [
      "count_digit_1_easy_while"
    ],
    "tests": [
      {
        "args": [
          1123451
        ],
        "expected": 3
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
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6059": {
    "functionNames": [
      "count_digit_2_easy_while"
    ],
    "tests": [
      {
        "args": [
          1123451
        ],
        "expected": 1
      },
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          222
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6060": {
    "functionNames": [
      "count_digit_3_easy_while"
    ],
    "tests": [
      {
        "args": [
          1123451
        ],
        "expected": 1
      },
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          333
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6061": {
    "functionNames": [
      "count_digit_4_easy_while"
    ],
    "tests": [
      {
        "args": [
          1123451
        ],
        "expected": 1
      },
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          444
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6062": {
    "functionNames": [
      "count_digit_5_easy_while"
    ],
    "tests": [
      {
        "args": [
          1123451
        ],
        "expected": 1
      },
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          555
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6063": {
    "functionNames": [
      "sum_before_1_easy_while"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            1,
            9
          ]
        ],
        "expected": 0
      },
      {
        "args": [
          [
            1,
            5
          ]
        ],
        "expected": 0
      },
      {
        "args": [
          [
            2,
            3
          ]
        ],
        "expected": 5
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6064": {
    "functionNames": [
      "sum_before_2_easy_while"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            2,
            9
          ]
        ],
        "expected": 1
      },
      {
        "args": [
          [
            2,
            5
          ]
        ],
        "expected": 0
      },
      {
        "args": [
          [
            2,
            3
          ]
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6065": {
    "functionNames": [
      "sum_before_3_easy_while"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            9
          ]
        ],
        "expected": 3
      },
      {
        "args": [
          [
            3,
            5
          ]
        ],
        "expected": 0
      },
      {
        "args": [
          [
            2,
            3
          ]
        ],
        "expected": 2
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6066": {
    "functionNames": [
      "sum_before_4_easy_while"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            4,
            9
          ]
        ],
        "expected": 3
      },
      {
        "args": [
          [
            4,
            5
          ]
        ],
        "expected": 0
      },
      {
        "args": [
          [
            2,
            3
          ]
        ],
        "expected": 5
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6067": {
    "functionNames": [
      "sum_before_5_easy_while"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            5,
            9
          ]
        ],
        "expected": 3
      },
      {
        "args": [
          [
            5,
            5
          ]
        ],
        "expected": 0
      },
      {
        "args": [
          [
            2,
            3
          ]
        ],
        "expected": 5
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6068": {
    "functionNames": [
      "text_before_1_easy_while"
    ],
    "tests": [
      {
        "args": [
          "ab1cd"
        ],
        "expected": "ab"
      },
      {
        "args": [
          "1start"
        ],
        "expected": ""
      },
      {
        "args": [
          "plain"
        ],
        "expected": "plain"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6069": {
    "functionNames": [
      "text_before_2_easy_while"
    ],
    "tests": [
      {
        "args": [
          "ab2cd"
        ],
        "expected": "ab"
      },
      {
        "args": [
          "2start"
        ],
        "expected": ""
      },
      {
        "args": [
          "plain"
        ],
        "expected": "plain"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6070": {
    "functionNames": [
      "text_before_3_easy_while"
    ],
    "tests": [
      {
        "args": [
          "ab3cd"
        ],
        "expected": "ab"
      },
      {
        "args": [
          "3start"
        ],
        "expected": ""
      },
      {
        "args": [
          "plain"
        ],
        "expected": "plain"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6071": {
    "functionNames": [
      "text_before_4_easy_while"
    ],
    "tests": [
      {
        "args": [
          "ab4cd"
        ],
        "expected": "ab"
      },
      {
        "args": [
          "4start"
        ],
        "expected": ""
      },
      {
        "args": [
          "plain"
        ],
        "expected": "plain"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6072": {
    "functionNames": [
      "text_before_5_easy_while"
    ],
    "tests": [
      {
        "args": [
          "ab5cd"
        ],
        "expected": "ab"
      },
      {
        "args": [
          "5start"
        ],
        "expected": ""
      },
      {
        "args": [
          "plain"
        ],
        "expected": "plain"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6073": {
    "functionNames": [
      "countdown_step_1_easy_while"
    ],
    "tests": [
      {
        "args": [
          10
        ],
        "expected": [
          10,
          8,
          6,
          4,
          2
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
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6074": {
    "functionNames": [
      "countdown_step_2_easy_while"
    ],
    "tests": [
      {
        "args": [
          10
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
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6075": {
    "functionNames": [
      "countdown_step_3_easy_while"
    ],
    "tests": [
      {
        "args": [
          10
        ],
        "expected": [
          10,
          6,
          2
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
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6076": {
    "functionNames": [
      "countdown_step_4_easy_while"
    ],
    "tests": [
      {
        "args": [
          10
        ],
        "expected": [
          10,
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
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6077": {
    "functionNames": [
      "countdown_step_5_easy_while"
    ],
    "tests": [
      {
        "args": [
          10
        ],
        "expected": [
          10,
          4
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
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6078": {
    "functionNames": [
      "repeat_items_1_easy_while"
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
          "a",
          "b"
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
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6079": {
    "functionNames": [
      "repeat_items_2_easy_while"
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
          "a",
          "a",
          "b",
          "b"
        ]
      },
      {
        "args": [
          [
            1
          ]
        ],
        "expected": [
          1,
          1
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6080": {
    "functionNames": [
      "repeat_items_3_easy_while"
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
          "a",
          "a",
          "a",
          "b",
          "b",
          "b"
        ]
      },
      {
        "args": [
          [
            1
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
          []
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6081": {
    "functionNames": [
      "repeat_items_4_easy_while"
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
          "a",
          "a",
          "a",
          "a",
          "b",
          "b",
          "b",
          "b"
        ]
      },
      {
        "args": [
          [
            1
          ]
        ],
        "expected": [
          1,
          1,
          1,
          1
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6082": {
    "functionNames": [
      "repeat_items_5_easy_while"
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
          "a",
          "a",
          "a",
          "a",
          "a",
          "b",
          "b",
          "b",
          "b",
          "b"
        ]
      },
      {
        "args": [
          [
            1
          ]
        ],
        "expected": [
          1,
          1,
          1,
          1,
          1
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6083": {
    "functionNames": [
      "count_divisible_1_easy_while"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            4,
            6,
            9
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
            3
          ]
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6084": {
    "functionNames": [
      "count_divisible_2_easy_while"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            4,
            6,
            9
          ]
        ],
        "expected": 1
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
            4
          ]
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6085": {
    "functionNames": [
      "count_divisible_3_easy_while"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            4,
            6,
            9
          ]
        ],
        "expected": 0
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
            5
          ]
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6086": {
    "functionNames": [
      "count_divisible_4_easy_while"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            4,
            6,
            9
          ]
        ],
        "expected": 1
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
            6
          ]
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6087": {
    "functionNames": [
      "count_divisible_5_easy_while"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            4,
            6,
            9
          ]
        ],
        "expected": 0
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
            7
          ]
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6088": {
    "functionNames": [
      "first_greater_1_easy_while"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            9,
            2
          ]
        ],
        "expected": 1
      },
      {
        "args": [
          [
            2
          ]
        ],
        "expected": -1
      },
      {
        "args": [
          []
        ],
        "expected": -1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6089": {
    "functionNames": [
      "first_greater_2_easy_while"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            9,
            2
          ]
        ],
        "expected": 1
      },
      {
        "args": [
          [
            4
          ]
        ],
        "expected": -1
      },
      {
        "args": [
          []
        ],
        "expected": -1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6090": {
    "functionNames": [
      "first_greater_3_easy_while"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            9,
            2
          ]
        ],
        "expected": 1
      },
      {
        "args": [
          [
            6
          ]
        ],
        "expected": -1
      },
      {
        "args": [
          []
        ],
        "expected": -1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6091": {
    "functionNames": [
      "first_greater_4_easy_while"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            9,
            2
          ]
        ],
        "expected": 1
      },
      {
        "args": [
          [
            8
          ]
        ],
        "expected": -1
      },
      {
        "args": [
          []
        ],
        "expected": -1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6092": {
    "functionNames": [
      "first_greater_5_easy_while"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            9,
            2
          ]
        ],
        "expected": -1
      },
      {
        "args": [
          [
            10
          ]
        ],
        "expected": -1
      },
      {
        "args": [
          []
        ],
        "expected": -1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6093": {
    "functionNames": [
      "offset_values_1_easy_while"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
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
            -1
          ]
        ],
        "expected": [
          0
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6094": {
    "functionNames": [
      "offset_values_2_easy_while"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ]
        ],
        "expected": [
          3,
          4
        ]
      },
      {
        "args": [
          [
            -1
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
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6095": {
    "functionNames": [
      "offset_values_3_easy_while"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ]
        ],
        "expected": [
          4,
          5
        ]
      },
      {
        "args": [
          [
            -1
          ]
        ],
        "expected": [
          2
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6096": {
    "functionNames": [
      "offset_values_4_easy_while"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
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
            -1
          ]
        ],
        "expected": [
          3
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6097": {
    "functionNames": [
      "offset_values_5_easy_while"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ]
        ],
        "expected": [
          6,
          7
        ]
      },
      {
        "args": [
          [
            -1
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
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6098": {
    "functionNames": [
      "parity_characters_1_easy_while"
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
          "x"
        ],
        "expected": ""
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6099": {
    "functionNames": [
      "parity_characters_2_easy_while"
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
          "x"
        ],
        "expected": "x"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6100": {
    "functionNames": [
      "parity_characters_3_easy_while"
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
          "x"
        ],
        "expected": ""
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6101": {
    "functionNames": [
      "parity_characters_4_easy_while"
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
          "x"
        ],
        "expected": "x"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6102": {
    "functionNames": [
      "parity_characters_5_easy_while"
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
          "x"
        ],
        "expected": ""
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6103": {
    "functionNames": [
      "changes_plus_1_easy_while"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            1,
            2,
            2,
            3
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
      },
      {
        "args": [
          []
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6104": {
    "functionNames": [
      "changes_plus_2_easy_while"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            1,
            2,
            2,
            3
          ]
        ],
        "expected": 4
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": 2
      },
      {
        "args": [
          []
        ],
        "expected": 2
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6105": {
    "functionNames": [
      "changes_plus_3_easy_while"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            1,
            2,
            2,
            3
          ]
        ],
        "expected": 5
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": 3
      },
      {
        "args": [
          []
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6106": {
    "functionNames": [
      "changes_plus_4_easy_while"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            1,
            2,
            2,
            3
          ]
        ],
        "expected": 6
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": 4
      },
      {
        "args": [
          []
        ],
        "expected": 4
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6107": {
    "functionNames": [
      "changes_plus_5_easy_while"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            1,
            2,
            2,
            3
          ]
        ],
        "expected": 7
      },
      {
        "args": [
          [
            5
          ]
        ],
        "expected": 5
      },
      {
        "args": [
          []
        ],
        "expected": 5
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6108": {
    "functionNames": [
      "rotate_left_1_while"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            4
          ]
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
            9
          ]
        ],
        "expected": [
          9
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6109": {
    "functionNames": [
      "rotate_left_2_while"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            4
          ]
        ],
        "expected": [
          3,
          4,
          1,
          2
        ]
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": [
          9
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6110": {
    "functionNames": [
      "rotate_left_3_while"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            4
          ]
        ],
        "expected": [
          4,
          1,
          2,
          3
        ]
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": [
          9
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6111": {
    "functionNames": [
      "rotate_left_4_while"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
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
          [
            9
          ]
        ],
        "expected": [
          9
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6112": {
    "functionNames": [
      "rotate_left_5_while"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            4
          ]
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
            9
          ]
        ],
        "expected": [
          9
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6113": {
    "functionNames": [
      "merge_marker_1_while"
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
          4,
          1
        ]
      },
      {
        "args": [
          [],
          [
            2
          ]
        ],
        "expected": [
          2,
          1
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
          1,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6114": {
    "functionNames": [
      "merge_marker_2_while"
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
          4,
          2
        ]
      },
      {
        "args": [
          [],
          [
            2
          ]
        ],
        "expected": [
          2,
          2
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
          1,
          2
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6115": {
    "functionNames": [
      "merge_marker_3_while"
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
          4,
          3
        ]
      },
      {
        "args": [
          [],
          [
            2
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
            1
          ],
          []
        ],
        "expected": [
          1,
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6116": {
    "functionNames": [
      "merge_marker_4_while"
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
          4,
          4
        ]
      },
      {
        "args": [
          [],
          [
            2
          ]
        ],
        "expected": [
          2,
          4
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
          1,
          4
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6117": {
    "functionNames": [
      "merge_marker_5_while"
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
          4,
          5
        ]
      },
      {
        "args": [
          [],
          [
            2
          ]
        ],
        "expected": [
          2,
          5
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
          1,
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6118": {
    "functionNames": [
      "longest_run_1_while"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            1,
            0,
            1
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
        "expected": 1
      },
      {
        "args": [
          []
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6119": {
    "functionNames": [
      "longest_run_2_while"
    ],
    "tests": [
      {
        "args": [
          [
            2,
            2,
            0,
            2
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
        "expected": 1
      },
      {
        "args": [
          []
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6120": {
    "functionNames": [
      "longest_run_3_while"
    ],
    "tests": [
      {
        "args": [
          [
            3,
            3,
            0,
            3
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
        "expected": 0
      },
      {
        "args": [
          []
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6121": {
    "functionNames": [
      "longest_run_4_while"
    ],
    "tests": [
      {
        "args": [
          [
            4,
            4,
            0,
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
        "expected": 0
      },
      {
        "args": [
          []
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6122": {
    "functionNames": [
      "longest_run_5_while"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            5,
            0,
            5
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
        "expected": 0
      },
      {
        "args": [
          []
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6123": {
    "functionNames": [
      "chunk_size_1_while"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            4,
            5,
            6
          ]
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
            5,
            6
          ]
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": [
          [
            9
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6124": {
    "functionNames": [
      "chunk_size_2_while"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            4,
            5,
            6
          ]
        ],
        "expected": [
          [
            1,
            2,
            3
          ],
          [
            4,
            5,
            6
          ]
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": [
          [
            9
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6125": {
    "functionNames": [
      "chunk_size_3_while"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            4,
            5,
            6
          ]
        ],
        "expected": [
          [
            1,
            2,
            3,
            4
          ],
          [
            5,
            6
          ]
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": [
          [
            9
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6126": {
    "functionNames": [
      "chunk_size_4_while"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            4,
            5,
            6
          ]
        ],
        "expected": [
          [
            1,
            2,
            3,
            4,
            5
          ],
          [
            6
          ]
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": [
          [
            9
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6127": {
    "functionNames": [
      "chunk_size_5_while"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            4,
            5,
            6
          ]
        ],
        "expected": [
          [
            1,
            2,
            3,
            4,
            5,
            6
          ]
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": [
          [
            9
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6128": {
    "functionNames": [
      "find_pattern_from_1_while"
    ],
    "tests": [
      {
        "args": [
          "abracadabra",
          "a"
        ],
        "expected": 3
      },
      {
        "args": [
          "hello",
          "ll"
        ],
        "expected": 2
      },
      {
        "args": [
          "short",
          "xyz"
        ],
        "expected": -1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6129": {
    "functionNames": [
      "find_pattern_from_2_while"
    ],
    "tests": [
      {
        "args": [
          "abracadabra",
          "a"
        ],
        "expected": 3
      },
      {
        "args": [
          "hello",
          "ll"
        ],
        "expected": 2
      },
      {
        "args": [
          "short",
          "xyz"
        ],
        "expected": -1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6130": {
    "functionNames": [
      "find_pattern_from_3_while"
    ],
    "tests": [
      {
        "args": [
          "abracadabra",
          "a"
        ],
        "expected": 3
      },
      {
        "args": [
          "hello",
          "ll"
        ],
        "expected": -1
      },
      {
        "args": [
          "short",
          "xyz"
        ],
        "expected": -1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6131": {
    "functionNames": [
      "find_pattern_from_4_while"
    ],
    "tests": [
      {
        "args": [
          "abracadabra",
          "a"
        ],
        "expected": 5
      },
      {
        "args": [
          "hello",
          "ll"
        ],
        "expected": -1
      },
      {
        "args": [
          "short",
          "xyz"
        ],
        "expected": -1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6132": {
    "functionNames": [
      "find_pattern_from_5_while"
    ],
    "tests": [
      {
        "args": [
          "abracadabra",
          "a"
        ],
        "expected": 5
      },
      {
        "args": [
          "hello",
          "ll"
        ],
        "expected": -1
      },
      {
        "args": [
          "short",
          "xyz"
        ],
        "expected": -1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6133": {
    "functionNames": [
      "to_base_1_while"
    ],
    "tests": [
      {
        "args": [
          10
        ],
        "expected": "101"
      },
      {
        "args": [
          0
        ],
        "expected": "0"
      },
      {
        "args": [
          3
        ],
        "expected": "10"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6134": {
    "functionNames": [
      "to_base_2_while"
    ],
    "tests": [
      {
        "args": [
          10
        ],
        "expected": "22"
      },
      {
        "args": [
          0
        ],
        "expected": "0"
      },
      {
        "args": [
          4
        ],
        "expected": "10"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6135": {
    "functionNames": [
      "to_base_3_while"
    ],
    "tests": [
      {
        "args": [
          10
        ],
        "expected": "20"
      },
      {
        "args": [
          0
        ],
        "expected": "0"
      },
      {
        "args": [
          5
        ],
        "expected": "10"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6136": {
    "functionNames": [
      "to_base_4_while"
    ],
    "tests": [
      {
        "args": [
          10
        ],
        "expected": "14"
      },
      {
        "args": [
          0
        ],
        "expected": "0"
      },
      {
        "args": [
          6
        ],
        "expected": "10"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6137": {
    "functionNames": [
      "to_base_5_while"
    ],
    "tests": [
      {
        "args": [
          10
        ],
        "expected": "13"
      },
      {
        "args": [
          0
        ],
        "expected": "0"
      },
      {
        "args": [
          7
        ],
        "expected": "10"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6138": {
    "functionNames": [
      "alternating_sum_1_while"
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
          []
        ],
        "expected": 0
      },
      {
        "args": [
          [
            5,
            -1
          ]
        ],
        "expected": 6
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6139": {
    "functionNames": [
      "alternating_sum_2_while"
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
        "expected": -2
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
            5,
            -1
          ]
        ],
        "expected": -6
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6140": {
    "functionNames": [
      "alternating_sum_3_while"
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
          []
        ],
        "expected": 0
      },
      {
        "args": [
          [
            5,
            -1
          ]
        ],
        "expected": 6
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6141": {
    "functionNames": [
      "alternating_sum_4_while"
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
        "expected": -2
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
            5,
            -1
          ]
        ],
        "expected": -6
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6142": {
    "functionNames": [
      "alternating_sum_5_while"
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
          []
        ],
        "expected": 0
      },
      {
        "args": [
          [
            5,
            -1
          ]
        ],
        "expected": 6
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6143": {
    "functionNames": [
      "drop_every_1_while"
    ],
    "tests": [
      {
        "args": [
          [
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
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": [
          9
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6144": {
    "functionNames": [
      "drop_every_2_while"
    ],
    "tests": [
      {
        "args": [
          [
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
          4,
          5
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": [
          9
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6145": {
    "functionNames": [
      "drop_every_3_while"
    ],
    "tests": [
      {
        "args": [
          [
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
          5,
          6
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": [
          9
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6146": {
    "functionNames": [
      "drop_every_4_while"
    ],
    "tests": [
      {
        "args": [
          [
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
          6
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": [
          9
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6147": {
    "functionNames": [
      "drop_every_5_while"
    ],
    "tests": [
      {
        "args": [
          [
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
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": [
          9
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6148": {
    "functionNames": [
      "totals_until_1_while"
    ],
    "tests": [
      {
        "args": [
          [
            3,
            4,
            50
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
            10
          ]
        ],
        "expected": [
          10
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6149": {
    "functionNames": [
      "totals_until_2_while"
    ],
    "tests": [
      {
        "args": [
          [
            3,
            4,
            50
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
            20
          ]
        ],
        "expected": [
          20
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6150": {
    "functionNames": [
      "totals_until_3_while"
    ],
    "tests": [
      {
        "args": [
          [
            3,
            4,
            50
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
            30
          ]
        ],
        "expected": [
          30
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6151": {
    "functionNames": [
      "totals_until_4_while"
    ],
    "tests": [
      {
        "args": [
          [
            3,
            4,
            50
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
            40
          ]
        ],
        "expected": [
          40
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6152": {
    "functionNames": [
      "totals_until_5_while"
    ],
    "tests": [
      {
        "args": [
          [
            3,
            4,
            50
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
            50
          ]
        ],
        "expected": [
          50
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6153": {
    "functionNames": [
      "adjacent_sums_1_while"
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
          4,
          6
        ]
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": []
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6154": {
    "functionNames": [
      "adjacent_sums_2_while"
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
          5,
          7
        ]
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": []
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6155": {
    "functionNames": [
      "adjacent_sums_3_while"
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
          6,
          8
        ]
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": []
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6156": {
    "functionNames": [
      "adjacent_sums_4_while"
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
          7,
          9
        ]
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": []
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6157": {
    "functionNames": [
      "adjacent_sums_5_while"
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
          8,
          10
        ]
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": []
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6158": {
    "functionNames": [
      "binary_find_1_while"
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
        "expected": 3
      },
      {
        "args": [
          [
            1
          ],
          2
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
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6159": {
    "functionNames": [
      "binary_find_2_while"
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
        "expected": 4
      },
      {
        "args": [
          [
            1
          ],
          2
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
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6160": {
    "functionNames": [
      "binary_find_3_while"
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
        "expected": 5
      },
      {
        "args": [
          [
            1
          ],
          2
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
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6161": {
    "functionNames": [
      "binary_find_4_while"
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
        "expected": 6
      },
      {
        "args": [
          [
            1
          ],
          2
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
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6162": {
    "functionNames": [
      "binary_find_5_while"
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
        "expected": 7
      },
      {
        "args": [
          [
            1
          ],
          2
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
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6163": {
    "functionNames": [
      "gcd_plus_1_while"
    ],
    "tests": [
      {
        "args": [
          48,
          18
        ],
        "expected": 7
      },
      {
        "args": [
          7,
          0
        ],
        "expected": 8
      },
      {
        "args": [
          21,
          14
        ],
        "expected": 8
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6164": {
    "functionNames": [
      "gcd_plus_2_while"
    ],
    "tests": [
      {
        "args": [
          48,
          18
        ],
        "expected": 8
      },
      {
        "args": [
          7,
          0
        ],
        "expected": 9
      },
      {
        "args": [
          21,
          14
        ],
        "expected": 9
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6165": {
    "functionNames": [
      "gcd_plus_3_while"
    ],
    "tests": [
      {
        "args": [
          48,
          18
        ],
        "expected": 9
      },
      {
        "args": [
          7,
          0
        ],
        "expected": 10
      },
      {
        "args": [
          21,
          14
        ],
        "expected": 10
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6166": {
    "functionNames": [
      "gcd_plus_4_while"
    ],
    "tests": [
      {
        "args": [
          48,
          18
        ],
        "expected": 10
      },
      {
        "args": [
          7,
          0
        ],
        "expected": 11
      },
      {
        "args": [
          21,
          14
        ],
        "expected": 11
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6167": {
    "functionNames": [
      "gcd_plus_5_while"
    ],
    "tests": [
      {
        "args": [
          48,
          18
        ],
        "expected": 11
      },
      {
        "args": [
          7,
          0
        ],
        "expected": 12
      },
      {
        "args": [
          21,
          14
        ],
        "expected": 12
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6168": {
    "functionNames": [
      "encode_runs_1_while"
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
        "expected": [
          [
            1,
            3
          ],
          [
            2,
            2
          ]
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            "a",
            "a",
            "a"
          ]
        ],
        "expected": [
          [
            "a",
            4
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6169": {
    "functionNames": [
      "encode_runs_2_while"
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
        "expected": [
          [
            1,
            4
          ],
          [
            2,
            3
          ]
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            "a",
            "a",
            "a"
          ]
        ],
        "expected": [
          [
            "a",
            5
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6170": {
    "functionNames": [
      "encode_runs_3_while"
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
        "expected": [
          [
            1,
            5
          ],
          [
            2,
            4
          ]
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            "a",
            "a",
            "a"
          ]
        ],
        "expected": [
          [
            "a",
            6
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6171": {
    "functionNames": [
      "encode_runs_4_while"
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
        "expected": [
          [
            1,
            6
          ],
          [
            2,
            5
          ]
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            "a",
            "a",
            "a"
          ]
        ],
        "expected": [
          [
            "a",
            7
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6172": {
    "functionNames": [
      "encode_runs_5_while"
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
        "expected": [
          [
            1,
            7
          ],
          [
            2,
            6
          ]
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            "a",
            "a",
            "a"
          ]
        ],
        "expected": [
          [
            "a",
            8
          ]
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6173": {
    "functionNames": [
      "decode_runs_1_while"
    ],
    "tests": [
      {
        "args": [
          [
            [
              "a",
              2
            ],
            [
              "b",
              1
            ]
          ]
        ],
        "expected": [
          "a",
          "a",
          "b",
          1
        ]
      },
      {
        "args": [
          []
        ],
        "expected": [
          1
        ]
      },
      {
        "args": [
          [
            [
              9,
              1
            ]
          ]
        ],
        "expected": [
          9,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6174": {
    "functionNames": [
      "decode_runs_2_while"
    ],
    "tests": [
      {
        "args": [
          [
            [
              "a",
              2
            ],
            [
              "b",
              1
            ]
          ]
        ],
        "expected": [
          "a",
          "a",
          "b",
          2
        ]
      },
      {
        "args": [
          []
        ],
        "expected": [
          2
        ]
      },
      {
        "args": [
          [
            [
              9,
              1
            ]
          ]
        ],
        "expected": [
          9,
          2
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6175": {
    "functionNames": [
      "decode_runs_3_while"
    ],
    "tests": [
      {
        "args": [
          [
            [
              "a",
              2
            ],
            [
              "b",
              1
            ]
          ]
        ],
        "expected": [
          "a",
          "a",
          "b",
          3
        ]
      },
      {
        "args": [
          []
        ],
        "expected": [
          3
        ]
      },
      {
        "args": [
          [
            [
              9,
              1
            ]
          ]
        ],
        "expected": [
          9,
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6176": {
    "functionNames": [
      "decode_runs_4_while"
    ],
    "tests": [
      {
        "args": [
          [
            [
              "a",
              2
            ],
            [
              "b",
              1
            ]
          ]
        ],
        "expected": [
          "a",
          "a",
          "b",
          4
        ]
      },
      {
        "args": [
          []
        ],
        "expected": [
          4
        ]
      },
      {
        "args": [
          [
            [
              9,
              1
            ]
          ]
        ],
        "expected": [
          9,
          4
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6177": {
    "functionNames": [
      "decode_runs_5_while"
    ],
    "tests": [
      {
        "args": [
          [
            [
              "a",
              2
            ],
            [
              "b",
              1
            ]
          ]
        ],
        "expected": [
          "a",
          "a",
          "b",
          5
        ]
      },
      {
        "args": [
          []
        ],
        "expected": [
          5
        ]
      },
      {
        "args": [
          [
            [
              9,
              1
            ]
          ]
        ],
        "expected": [
          9,
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6178": {
    "functionNames": [
      "flatten_marker_1_while"
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
          3,
          1
        ]
      },
      {
        "args": [
          []
        ],
        "expected": [
          1
        ]
      },
      {
        "args": [
          [
            []
          ]
        ],
        "expected": [
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6179": {
    "functionNames": [
      "flatten_marker_2_while"
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
          3,
          2
        ]
      },
      {
        "args": [
          []
        ],
        "expected": [
          2
        ]
      },
      {
        "args": [
          [
            []
          ]
        ],
        "expected": [
          2
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6180": {
    "functionNames": [
      "flatten_marker_3_while"
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
          3,
          3
        ]
      },
      {
        "args": [
          []
        ],
        "expected": [
          3
        ]
      },
      {
        "args": [
          [
            []
          ]
        ],
        "expected": [
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6181": {
    "functionNames": [
      "flatten_marker_4_while"
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
          3,
          4
        ]
      },
      {
        "args": [
          []
        ],
        "expected": [
          4
        ]
      },
      {
        "args": [
          [
            []
          ]
        ],
        "expected": [
          4
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6182": {
    "functionNames": [
      "flatten_marker_5_while"
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
          3,
          5
        ]
      },
      {
        "args": [
          []
        ],
        "expected": [
          5
        ]
      },
      {
        "args": [
          [
            []
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6183": {
    "functionNames": [
      "row_max_plus_1_while"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              4
            ],
            [
              3,
              2
            ]
          ]
        ],
        "expected": [
          5,
          4
        ]
      },
      {
        "args": [
          [
            []
          ]
        ],
        "expected": []
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6184": {
    "functionNames": [
      "row_max_plus_2_while"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              4
            ],
            [
              3,
              2
            ]
          ]
        ],
        "expected": [
          6,
          5
        ]
      },
      {
        "args": [
          [
            []
          ]
        ],
        "expected": []
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6185": {
    "functionNames": [
      "row_max_plus_3_while"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              4
            ],
            [
              3,
              2
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
            []
          ]
        ],
        "expected": []
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6186": {
    "functionNames": [
      "row_max_plus_4_while"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              4
            ],
            [
              3,
              2
            ]
          ]
        ],
        "expected": [
          8,
          7
        ]
      },
      {
        "args": [
          [
            []
          ]
        ],
        "expected": []
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6187": {
    "functionNames": [
      "row_max_plus_5_while"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              4
            ],
            [
              3,
              2
            ]
          ]
        ],
        "expected": [
          9,
          8
        ]
      },
      {
        "args": [
          [
            []
          ]
        ],
        "expected": []
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6188": {
    "functionNames": [
      "depth_limit_1_while"
    ],
    "tests": [
      {
        "args": [
          "()"
        ],
        "expected": true
      },
      {
        "args": [
          "(())"
        ],
        "expected": false
      },
      {
        "args": [
          "(()"
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6189": {
    "functionNames": [
      "depth_limit_2_while"
    ],
    "tests": [
      {
        "args": [
          "()"
        ],
        "expected": true
      },
      {
        "args": [
          "(())"
        ],
        "expected": true
      },
      {
        "args": [
          "(()"
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6190": {
    "functionNames": [
      "depth_limit_3_while"
    ],
    "tests": [
      {
        "args": [
          "()"
        ],
        "expected": true
      },
      {
        "args": [
          "(())"
        ],
        "expected": true
      },
      {
        "args": [
          "(()"
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6191": {
    "functionNames": [
      "depth_limit_4_while"
    ],
    "tests": [
      {
        "args": [
          "()"
        ],
        "expected": true
      },
      {
        "args": [
          "(())"
        ],
        "expected": true
      },
      {
        "args": [
          "(()"
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6192": {
    "functionNames": [
      "depth_limit_5_while"
    ],
    "tests": [
      {
        "args": [
          "()"
        ],
        "expected": true
      },
      {
        "args": [
          "(())"
        ],
        "expected": true
      },
      {
        "args": [
          "(()"
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6193": {
    "functionNames": [
      "cycle_position_1_while"
    ],
    "tests": [
      {
        "args": [
          0,
          2,
          5
        ],
        "expected": 1
      },
      {
        "args": [
          3,
          1,
          4
        ],
        "expected": 2
      },
      {
        "args": [
          1,
          3,
          7
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6194": {
    "functionNames": [
      "cycle_position_2_while"
    ],
    "tests": [
      {
        "args": [
          0,
          2,
          5
        ],
        "expected": 2
      },
      {
        "args": [
          3,
          1,
          4
        ],
        "expected": 1
      },
      {
        "args": [
          1,
          3,
          7
        ],
        "expected": 5
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6195": {
    "functionNames": [
      "cycle_position_3_while"
    ],
    "tests": [
      {
        "args": [
          0,
          2,
          5
        ],
        "expected": 3
      },
      {
        "args": [
          3,
          1,
          4
        ],
        "expected": 0
      },
      {
        "args": [
          1,
          3,
          7
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6196": {
    "functionNames": [
      "cycle_position_4_while"
    ],
    "tests": [
      {
        "args": [
          0,
          2,
          5
        ],
        "expected": 4
      },
      {
        "args": [
          3,
          1,
          4
        ],
        "expected": 3
      },
      {
        "args": [
          1,
          3,
          7
        ],
        "expected": 2
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6197": {
    "functionNames": [
      "cycle_position_5_while"
    ],
    "tests": [
      {
        "args": [
          0,
          2,
          5
        ],
        "expected": 0
      },
      {
        "args": [
          3,
          1,
          4
        ],
        "expected": 2
      },
      {
        "args": [
          1,
          3,
          7
        ],
        "expected": 4
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6198": {
    "functionNames": [
      "integer_sqrt_plus_1_while"
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
          15
        ],
        "expected": 4
      },
      {
        "args": [
          25
        ],
        "expected": 6
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6199": {
    "functionNames": [
      "integer_sqrt_plus_2_while"
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
          15
        ],
        "expected": 5
      },
      {
        "args": [
          25
        ],
        "expected": 7
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6200": {
    "functionNames": [
      "integer_sqrt_plus_3_while"
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
          15
        ],
        "expected": 6
      },
      {
        "args": [
          25
        ],
        "expected": 8
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6201": {
    "functionNames": [
      "integer_sqrt_plus_4_while"
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
          15
        ],
        "expected": 7
      },
      {
        "args": [
          25
        ],
        "expected": 9
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6202": {
    "functionNames": [
      "integer_sqrt_plus_5_while"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 5
      },
      {
        "args": [
          15
        ],
        "expected": 8
      },
      {
        "args": [
          25
        ],
        "expected": 10
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6203": {
    "functionNames": [
      "partition_pivot_1_while"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1,
            3
          ]
        ],
        "expected": [
          [
            0
          ],
          [
            1
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
        "expected": [
          [],
          [],
          []
        ]
      },
      {
        "args": [
          [
            1,
            1
          ]
        ],
        "expected": [
          [],
          [
            1,
            1
          ],
          []
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6204": {
    "functionNames": [
      "partition_pivot_2_while"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            2,
            4
          ]
        ],
        "expected": [
          [
            0
          ],
          [
            2
          ],
          [
            4
          ]
        ]
      },
      {
        "args": [
          []
        ],
        "expected": [
          [],
          [],
          []
        ]
      },
      {
        "args": [
          [
            2,
            2
          ]
        ],
        "expected": [
          [],
          [
            2,
            2
          ],
          []
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6205": {
    "functionNames": [
      "partition_pivot_3_while"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            3,
            5
          ]
        ],
        "expected": [
          [
            0
          ],
          [
            3
          ],
          [
            5
          ]
        ]
      },
      {
        "args": [
          []
        ],
        "expected": [
          [],
          [],
          []
        ]
      },
      {
        "args": [
          [
            3,
            3
          ]
        ],
        "expected": [
          [],
          [
            3,
            3
          ],
          []
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6206": {
    "functionNames": [
      "partition_pivot_4_while"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            4,
            6
          ]
        ],
        "expected": [
          [
            0
          ],
          [
            4
          ],
          [
            6
          ]
        ]
      },
      {
        "args": [
          []
        ],
        "expected": [
          [],
          [],
          []
        ]
      },
      {
        "args": [
          [
            4,
            4
          ]
        ],
        "expected": [
          [],
          [
            4,
            4
          ],
          []
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6207": {
    "functionNames": [
      "partition_pivot_5_while"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            5,
            7
          ]
        ],
        "expected": [
          [
            0
          ],
          [
            5
          ],
          [
            7
          ]
        ]
      },
      {
        "args": [
          []
        ],
        "expected": [
          [],
          [],
          []
        ]
      },
      {
        "args": [
          [
            5,
            5
          ]
        ],
        "expected": [
          [],
          [
            5,
            5
          ],
          []
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "6208": {
    "functionNames": [
      "dict_get_1"
    ],
    "tests": [
      {
        "args": [
          {
            "k1": 1
          }
        ],
        "expected": 1
      },
      {
        "args": [
          {}
        ],
        "expected": 10
      },
      {
        "args": [
          {
            "x": 9
          }
        ],
        "expected": 10
      }
    ]
  },
  "6209": {
    "functionNames": [
      "dict_get_2"
    ],
    "tests": [
      {
        "args": [
          {
            "k2": 2
          }
        ],
        "expected": 2
      },
      {
        "args": [
          {}
        ],
        "expected": 20
      },
      {
        "args": [
          {
            "x": 9
          }
        ],
        "expected": 20
      }
    ]
  },
  "6210": {
    "functionNames": [
      "dict_get_3"
    ],
    "tests": [
      {
        "args": [
          {
            "k3": 3
          }
        ],
        "expected": 3
      },
      {
        "args": [
          {}
        ],
        "expected": 30
      },
      {
        "args": [
          {
            "x": 9
          }
        ],
        "expected": 30
      }
    ]
  },
  "6211": {
    "functionNames": [
      "dict_get_4"
    ],
    "tests": [
      {
        "args": [
          {
            "k4": 4
          }
        ],
        "expected": 4
      },
      {
        "args": [
          {}
        ],
        "expected": 40
      },
      {
        "args": [
          {
            "x": 9
          }
        ],
        "expected": 40
      }
    ]
  },
  "6212": {
    "functionNames": [
      "dict_get_5"
    ],
    "tests": [
      {
        "args": [
          {
            "k5": 5
          }
        ],
        "expected": 5
      },
      {
        "args": [
          {}
        ],
        "expected": 50
      },
      {
        "args": [
          {
            "x": 9
          }
        ],
        "expected": 50
      }
    ]
  },
  "6213": {
    "functionNames": [
      "dict_add_1"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1
          }
        ],
        "expected": {
          "a": 1,
          "k1": 1
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {
          "k1": 1
        }
      },
      {
        "args": [
          {
            "k1": 9
          }
        ],
        "expected": {
          "k1": 1
        }
      }
    ]
  },
  "6214": {
    "functionNames": [
      "dict_add_2"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1
          }
        ],
        "expected": {
          "a": 1,
          "k2": 2
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {
          "k2": 2
        }
      },
      {
        "args": [
          {
            "k2": 9
          }
        ],
        "expected": {
          "k2": 2
        }
      }
    ]
  },
  "6215": {
    "functionNames": [
      "dict_add_3"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1
          }
        ],
        "expected": {
          "a": 1,
          "k3": 3
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {
          "k3": 3
        }
      },
      {
        "args": [
          {
            "k3": 9
          }
        ],
        "expected": {
          "k3": 3
        }
      }
    ]
  },
  "6216": {
    "functionNames": [
      "dict_add_4"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1
          }
        ],
        "expected": {
          "a": 1,
          "k4": 4
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {
          "k4": 4
        }
      },
      {
        "args": [
          {
            "k4": 9
          }
        ],
        "expected": {
          "k4": 4
        }
      }
    ]
  },
  "6217": {
    "functionNames": [
      "dict_add_5"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1
          }
        ],
        "expected": {
          "a": 1,
          "k5": 5
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {
          "k5": 5
        }
      },
      {
        "args": [
          {
            "k5": 9
          }
        ],
        "expected": {
          "k5": 5
        }
      }
    ]
  },
  "6218": {
    "functionNames": [
      "dict_remove_1"
    ],
    "tests": [
      {
        "args": [
          {
            "k1": 1,
            "a": 1
          }
        ],
        "expected": {
          "a": 1
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {}
      },
      {
        "args": [
          {
            "x": 2
          }
        ],
        "expected": {
          "x": 2
        }
      }
    ]
  },
  "6219": {
    "functionNames": [
      "dict_remove_2"
    ],
    "tests": [
      {
        "args": [
          {
            "k2": 2,
            "a": 1
          }
        ],
        "expected": {
          "a": 1
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {}
      },
      {
        "args": [
          {
            "x": 2
          }
        ],
        "expected": {
          "x": 2
        }
      }
    ]
  },
  "6220": {
    "functionNames": [
      "dict_remove_3"
    ],
    "tests": [
      {
        "args": [
          {
            "k3": 3,
            "a": 1
          }
        ],
        "expected": {
          "a": 1
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {}
      },
      {
        "args": [
          {
            "x": 2
          }
        ],
        "expected": {
          "x": 2
        }
      }
    ]
  },
  "6221": {
    "functionNames": [
      "dict_remove_4"
    ],
    "tests": [
      {
        "args": [
          {
            "k4": 4,
            "a": 1
          }
        ],
        "expected": {
          "a": 1
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {}
      },
      {
        "args": [
          {
            "x": 2
          }
        ],
        "expected": {
          "x": 2
        }
      }
    ]
  },
  "6222": {
    "functionNames": [
      "dict_remove_5"
    ],
    "tests": [
      {
        "args": [
          {
            "k5": 5,
            "a": 1
          }
        ],
        "expected": {
          "a": 1
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {}
      },
      {
        "args": [
          {
            "x": 2
          }
        ],
        "expected": {
          "x": 2
        }
      }
    ]
  },
  "6223": {
    "functionNames": [
      "dict_size_plus_1"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1,
            "b": 2
          }
        ],
        "expected": 3
      },
      {
        "args": [
          {}
        ],
        "expected": 1
      },
      {
        "args": [
          {
            "x": 1
          }
        ],
        "expected": 2
      }
    ]
  },
  "6224": {
    "functionNames": [
      "dict_size_plus_2"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1,
            "b": 2
          }
        ],
        "expected": 4
      },
      {
        "args": [
          {}
        ],
        "expected": 2
      },
      {
        "args": [
          {
            "x": 1
          }
        ],
        "expected": 3
      }
    ]
  },
  "6225": {
    "functionNames": [
      "dict_size_plus_3"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1,
            "b": 2
          }
        ],
        "expected": 5
      },
      {
        "args": [
          {}
        ],
        "expected": 3
      },
      {
        "args": [
          {
            "x": 1
          }
        ],
        "expected": 4
      }
    ]
  },
  "6226": {
    "functionNames": [
      "dict_size_plus_4"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1,
            "b": 2
          }
        ],
        "expected": 6
      },
      {
        "args": [
          {}
        ],
        "expected": 4
      },
      {
        "args": [
          {
            "x": 1
          }
        ],
        "expected": 5
      }
    ]
  },
  "6227": {
    "functionNames": [
      "dict_size_plus_5"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1,
            "b": 2
          }
        ],
        "expected": 7
      },
      {
        "args": [
          {}
        ],
        "expected": 5
      },
      {
        "args": [
          {
            "x": 1
          }
        ],
        "expected": 6
      }
    ]
  },
  "6228": {
    "functionNames": [
      "dict_value_sum_1"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1,
            "b": 2
          }
        ],
        "expected": 4
      },
      {
        "args": [
          {}
        ],
        "expected": 1
      },
      {
        "args": [
          {
            "x": -2
          }
        ],
        "expected": -1
      }
    ]
  },
  "6229": {
    "functionNames": [
      "dict_value_sum_2"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1,
            "b": 2
          }
        ],
        "expected": 5
      },
      {
        "args": [
          {}
        ],
        "expected": 2
      },
      {
        "args": [
          {
            "x": -2
          }
        ],
        "expected": 0
      }
    ]
  },
  "6230": {
    "functionNames": [
      "dict_value_sum_3"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1,
            "b": 2
          }
        ],
        "expected": 6
      },
      {
        "args": [
          {}
        ],
        "expected": 3
      },
      {
        "args": [
          {
            "x": -2
          }
        ],
        "expected": 1
      }
    ]
  },
  "6231": {
    "functionNames": [
      "dict_value_sum_4"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1,
            "b": 2
          }
        ],
        "expected": 7
      },
      {
        "args": [
          {}
        ],
        "expected": 4
      },
      {
        "args": [
          {
            "x": -2
          }
        ],
        "expected": 2
      }
    ]
  },
  "6232": {
    "functionNames": [
      "dict_value_sum_5"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1,
            "b": 2
          }
        ],
        "expected": 8
      },
      {
        "args": [
          {}
        ],
        "expected": 5
      },
      {
        "args": [
          {
            "x": -2
          }
        ],
        "expected": 3
      }
    ]
  },
  "6233": {
    "functionNames": [
      "dict_sorted_keys_1"
    ],
    "tests": [
      {
        "args": [
          {
            "b": 2,
            "a": 1
          }
        ],
        "expected": [
          "a",
          "b",
          "k1"
        ]
      },
      {
        "args": [
          {}
        ],
        "expected": [
          "k1"
        ]
      },
      {
        "args": [
          {
            "x": 1
          }
        ],
        "expected": [
          "x",
          "k1"
        ]
      }
    ]
  },
  "6234": {
    "functionNames": [
      "dict_sorted_keys_2"
    ],
    "tests": [
      {
        "args": [
          {
            "b": 2,
            "a": 1
          }
        ],
        "expected": [
          "a",
          "b",
          "k2"
        ]
      },
      {
        "args": [
          {}
        ],
        "expected": [
          "k2"
        ]
      },
      {
        "args": [
          {
            "x": 1
          }
        ],
        "expected": [
          "x",
          "k2"
        ]
      }
    ]
  },
  "6235": {
    "functionNames": [
      "dict_sorted_keys_3"
    ],
    "tests": [
      {
        "args": [
          {
            "b": 2,
            "a": 1
          }
        ],
        "expected": [
          "a",
          "b",
          "k3"
        ]
      },
      {
        "args": [
          {}
        ],
        "expected": [
          "k3"
        ]
      },
      {
        "args": [
          {
            "x": 1
          }
        ],
        "expected": [
          "x",
          "k3"
        ]
      }
    ]
  },
  "6236": {
    "functionNames": [
      "dict_sorted_keys_4"
    ],
    "tests": [
      {
        "args": [
          {
            "b": 2,
            "a": 1
          }
        ],
        "expected": [
          "a",
          "b",
          "k4"
        ]
      },
      {
        "args": [
          {}
        ],
        "expected": [
          "k4"
        ]
      },
      {
        "args": [
          {
            "x": 1
          }
        ],
        "expected": [
          "x",
          "k4"
        ]
      }
    ]
  },
  "6237": {
    "functionNames": [
      "dict_sorted_keys_5"
    ],
    "tests": [
      {
        "args": [
          {
            "b": 2,
            "a": 1
          }
        ],
        "expected": [
          "a",
          "b",
          "k5"
        ]
      },
      {
        "args": [
          {}
        ],
        "expected": [
          "k5"
        ]
      },
      {
        "args": [
          {
            "x": 1
          }
        ],
        "expected": [
          "x",
          "k5"
        ]
      }
    ]
  },
  "6238": {
    "functionNames": [
      "dict_sorted_values_1"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 3,
            "b": 1
          }
        ],
        "expected": [
          1,
          3,
          1
        ]
      },
      {
        "args": [
          {}
        ],
        "expected": [
          1
        ]
      },
      {
        "args": [
          {
            "x": -1
          }
        ],
        "expected": [
          -1,
          1
        ]
      }
    ]
  },
  "6239": {
    "functionNames": [
      "dict_sorted_values_2"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 3,
            "b": 1
          }
        ],
        "expected": [
          1,
          3,
          2
        ]
      },
      {
        "args": [
          {}
        ],
        "expected": [
          2
        ]
      },
      {
        "args": [
          {
            "x": -1
          }
        ],
        "expected": [
          -1,
          2
        ]
      }
    ]
  },
  "6240": {
    "functionNames": [
      "dict_sorted_values_3"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 3,
            "b": 1
          }
        ],
        "expected": [
          1,
          3,
          3
        ]
      },
      {
        "args": [
          {}
        ],
        "expected": [
          3
        ]
      },
      {
        "args": [
          {
            "x": -1
          }
        ],
        "expected": [
          -1,
          3
        ]
      }
    ]
  },
  "6241": {
    "functionNames": [
      "dict_sorted_values_4"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 3,
            "b": 1
          }
        ],
        "expected": [
          1,
          3,
          4
        ]
      },
      {
        "args": [
          {}
        ],
        "expected": [
          4
        ]
      },
      {
        "args": [
          {
            "x": -1
          }
        ],
        "expected": [
          -1,
          4
        ]
      }
    ]
  },
  "6242": {
    "functionNames": [
      "dict_sorted_values_5"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 3,
            "b": 1
          }
        ],
        "expected": [
          1,
          3,
          5
        ]
      },
      {
        "args": [
          {}
        ],
        "expected": [
          5
        ]
      },
      {
        "args": [
          {
            "x": -1
          }
        ],
        "expected": [
          -1,
          5
        ]
      }
    ]
  },
  "6243": {
    "functionNames": [
      "dict_invert_1"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1,
            "b": 2
          }
        ],
        "expected": {
          "1": "a1",
          "2": "b1"
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {}
      },
      {
        "args": [
          {
            "x": 9
          }
        ],
        "expected": {
          "9": "x1"
        }
      }
    ]
  },
  "6244": {
    "functionNames": [
      "dict_invert_2"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1,
            "b": 2
          }
        ],
        "expected": {
          "1": "a2",
          "2": "b2"
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {}
      },
      {
        "args": [
          {
            "x": 9
          }
        ],
        "expected": {
          "9": "x2"
        }
      }
    ]
  },
  "6245": {
    "functionNames": [
      "dict_invert_3"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1,
            "b": 2
          }
        ],
        "expected": {
          "1": "a3",
          "2": "b3"
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {}
      },
      {
        "args": [
          {
            "x": 9
          }
        ],
        "expected": {
          "9": "x3"
        }
      }
    ]
  },
  "6246": {
    "functionNames": [
      "dict_invert_4"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1,
            "b": 2
          }
        ],
        "expected": {
          "1": "a4",
          "2": "b4"
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {}
      },
      {
        "args": [
          {
            "x": 9
          }
        ],
        "expected": {
          "9": "x4"
        }
      }
    ]
  },
  "6247": {
    "functionNames": [
      "dict_invert_5"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1,
            "b": 2
          }
        ],
        "expected": {
          "1": "a5",
          "2": "b5"
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {}
      },
      {
        "args": [
          {
            "x": 9
          }
        ],
        "expected": {
          "9": "x5"
        }
      }
    ]
  },
  "6248": {
    "functionNames": [
      "dict_filter_1"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 0,
            "b": 5
          }
        ],
        "expected": {
          "b": 5
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {}
      },
      {
        "args": [
          {
            "x": 1
          }
        ],
        "expected": {
          "x": 1
        }
      }
    ]
  },
  "6249": {
    "functionNames": [
      "dict_filter_2"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 0,
            "b": 5
          }
        ],
        "expected": {
          "b": 5
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {}
      },
      {
        "args": [
          {
            "x": 2
          }
        ],
        "expected": {
          "x": 2
        }
      }
    ]
  },
  "6250": {
    "functionNames": [
      "dict_filter_3"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 0,
            "b": 5
          }
        ],
        "expected": {
          "b": 5
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {}
      },
      {
        "args": [
          {
            "x": 3
          }
        ],
        "expected": {
          "x": 3
        }
      }
    ]
  },
  "6251": {
    "functionNames": [
      "dict_filter_4"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 0,
            "b": 5
          }
        ],
        "expected": {
          "b": 5
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {}
      },
      {
        "args": [
          {
            "x": 4
          }
        ],
        "expected": {
          "x": 4
        }
      }
    ]
  },
  "6252": {
    "functionNames": [
      "dict_filter_5"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 0,
            "b": 5
          }
        ],
        "expected": {
          "b": 5
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {}
      },
      {
        "args": [
          {
            "x": 5
          }
        ],
        "expected": {
          "x": 5
        }
      }
    ]
  },
  "6253": {
    "functionNames": [
      "dict_offset_1"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1,
            "b": 2
          }
        ],
        "expected": {
          "a": 2,
          "b": 3
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {}
      },
      {
        "args": [
          {
            "x": -1
          }
        ],
        "expected": {
          "x": 0
        }
      }
    ]
  },
  "6254": {
    "functionNames": [
      "dict_offset_2"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1,
            "b": 2
          }
        ],
        "expected": {
          "a": 3,
          "b": 4
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {}
      },
      {
        "args": [
          {
            "x": -1
          }
        ],
        "expected": {
          "x": 1
        }
      }
    ]
  },
  "6255": {
    "functionNames": [
      "dict_offset_3"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1,
            "b": 2
          }
        ],
        "expected": {
          "a": 4,
          "b": 5
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {}
      },
      {
        "args": [
          {
            "x": -1
          }
        ],
        "expected": {
          "x": 2
        }
      }
    ]
  },
  "6256": {
    "functionNames": [
      "dict_offset_4"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1,
            "b": 2
          }
        ],
        "expected": {
          "a": 5,
          "b": 6
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {}
      },
      {
        "args": [
          {
            "x": -1
          }
        ],
        "expected": {
          "x": 3
        }
      }
    ]
  },
  "6257": {
    "functionNames": [
      "dict_offset_5"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1,
            "b": 2
          }
        ],
        "expected": {
          "a": 6,
          "b": 7
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {}
      },
      {
        "args": [
          {
            "x": -1
          }
        ],
        "expected": {
          "x": 4
        }
      }
    ]
  },
  "6258": {
    "functionNames": [
      "dict_merge_1"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1
          },
          {
            "b": 2
          }
        ],
        "expected": {
          "a": 1,
          "b": 2,
          "marker": 1
        }
      },
      {
        "args": [
          {
            "x": 1
          },
          {
            "x": 9
          }
        ],
        "expected": {
          "x": 9,
          "marker": 1
        }
      },
      {
        "args": [
          {},
          {}
        ],
        "expected": {
          "marker": 1
        }
      }
    ]
  },
  "6259": {
    "functionNames": [
      "dict_merge_2"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1
          },
          {
            "b": 2
          }
        ],
        "expected": {
          "a": 1,
          "b": 2,
          "marker": 2
        }
      },
      {
        "args": [
          {
            "x": 1
          },
          {
            "x": 9
          }
        ],
        "expected": {
          "x": 9,
          "marker": 2
        }
      },
      {
        "args": [
          {},
          {}
        ],
        "expected": {
          "marker": 2
        }
      }
    ]
  },
  "6260": {
    "functionNames": [
      "dict_merge_3"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1
          },
          {
            "b": 2
          }
        ],
        "expected": {
          "a": 1,
          "b": 2,
          "marker": 3
        }
      },
      {
        "args": [
          {
            "x": 1
          },
          {
            "x": 9
          }
        ],
        "expected": {
          "x": 9,
          "marker": 3
        }
      },
      {
        "args": [
          {},
          {}
        ],
        "expected": {
          "marker": 3
        }
      }
    ]
  },
  "6261": {
    "functionNames": [
      "dict_merge_4"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1
          },
          {
            "b": 2
          }
        ],
        "expected": {
          "a": 1,
          "b": 2,
          "marker": 4
        }
      },
      {
        "args": [
          {
            "x": 1
          },
          {
            "x": 9
          }
        ],
        "expected": {
          "x": 9,
          "marker": 4
        }
      },
      {
        "args": [
          {},
          {}
        ],
        "expected": {
          "marker": 4
        }
      }
    ]
  },
  "6262": {
    "functionNames": [
      "dict_merge_5"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1
          },
          {
            "b": 2
          }
        ],
        "expected": {
          "a": 1,
          "b": 2,
          "marker": 5
        }
      },
      {
        "args": [
          {
            "x": 1
          },
          {
            "x": 9
          }
        ],
        "expected": {
          "x": 9,
          "marker": 5
        }
      },
      {
        "args": [
          {},
          {}
        ],
        "expected": {
          "marker": 5
        }
      }
    ]
  },
  "6263": {
    "functionNames": [
      "dict_frequency_1"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "a",
            "b"
          ]
        ],
        "expected": {
          "a": 3,
          "b": 2
        }
      },
      {
        "args": [
          []
        ],
        "expected": {}
      },
      {
        "args": [
          [
            "x"
          ]
        ],
        "expected": {
          "x": 2
        }
      }
    ]
  },
  "6264": {
    "functionNames": [
      "dict_frequency_2"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "a",
            "b"
          ]
        ],
        "expected": {
          "a": 4,
          "b": 3
        }
      },
      {
        "args": [
          []
        ],
        "expected": {}
      },
      {
        "args": [
          [
            "x"
          ]
        ],
        "expected": {
          "x": 3
        }
      }
    ]
  },
  "6265": {
    "functionNames": [
      "dict_frequency_3"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "a",
            "b"
          ]
        ],
        "expected": {
          "a": 5,
          "b": 4
        }
      },
      {
        "args": [
          []
        ],
        "expected": {}
      },
      {
        "args": [
          [
            "x"
          ]
        ],
        "expected": {
          "x": 4
        }
      }
    ]
  },
  "6266": {
    "functionNames": [
      "dict_frequency_4"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "a",
            "b"
          ]
        ],
        "expected": {
          "a": 6,
          "b": 5
        }
      },
      {
        "args": [
          []
        ],
        "expected": {}
      },
      {
        "args": [
          [
            "x"
          ]
        ],
        "expected": {
          "x": 5
        }
      }
    ]
  },
  "6267": {
    "functionNames": [
      "dict_frequency_5"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "a",
            "b"
          ]
        ],
        "expected": {
          "a": 7,
          "b": 6
        }
      },
      {
        "args": [
          []
        ],
        "expected": {}
      },
      {
        "args": [
          [
            "x"
          ]
        ],
        "expected": {
          "x": 6
        }
      }
    ]
  },
  "6268": {
    "functionNames": [
      "dict_word_lengths_1"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "code"
          ]
        ],
        "expected": {
          "a": 2,
          "code": 5
        }
      },
      {
        "args": [
          []
        ],
        "expected": {}
      },
      {
        "args": [
          [
            "xy"
          ]
        ],
        "expected": {
          "xy": 3
        }
      }
    ]
  },
  "6269": {
    "functionNames": [
      "dict_word_lengths_2"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "code"
          ]
        ],
        "expected": {
          "a": 3,
          "code": 6
        }
      },
      {
        "args": [
          []
        ],
        "expected": {}
      },
      {
        "args": [
          [
            "xy"
          ]
        ],
        "expected": {
          "xy": 4
        }
      }
    ]
  },
  "6270": {
    "functionNames": [
      "dict_word_lengths_3"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "code"
          ]
        ],
        "expected": {
          "a": 4,
          "code": 7
        }
      },
      {
        "args": [
          []
        ],
        "expected": {}
      },
      {
        "args": [
          [
            "xy"
          ]
        ],
        "expected": {
          "xy": 5
        }
      }
    ]
  },
  "6271": {
    "functionNames": [
      "dict_word_lengths_4"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "code"
          ]
        ],
        "expected": {
          "a": 5,
          "code": 8
        }
      },
      {
        "args": [
          []
        ],
        "expected": {}
      },
      {
        "args": [
          [
            "xy"
          ]
        ],
        "expected": {
          "xy": 6
        }
      }
    ]
  },
  "6272": {
    "functionNames": [
      "dict_word_lengths_5"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "code"
          ]
        ],
        "expected": {
          "a": 6,
          "code": 9
        }
      },
      {
        "args": [
          []
        ],
        "expected": {}
      },
      {
        "args": [
          [
            "xy"
          ]
        ],
        "expected": {
          "xy": 7
        }
      }
    ]
  },
  "6273": {
    "functionNames": [
      "dict_has_1"
    ],
    "tests": [
      {
        "args": [
          {
            "k1": 1
          }
        ],
        "expected": true
      },
      {
        "args": [
          {}
        ],
        "expected": false
      },
      {
        "args": [
          {
            "x": 1
          }
        ],
        "expected": false
      }
    ]
  },
  "6274": {
    "functionNames": [
      "dict_has_2"
    ],
    "tests": [
      {
        "args": [
          {
            "k2": 1
          }
        ],
        "expected": true
      },
      {
        "args": [
          {}
        ],
        "expected": false
      },
      {
        "args": [
          {
            "x": 1
          }
        ],
        "expected": false
      }
    ]
  },
  "6275": {
    "functionNames": [
      "dict_has_3"
    ],
    "tests": [
      {
        "args": [
          {
            "k3": 1
          }
        ],
        "expected": true
      },
      {
        "args": [
          {}
        ],
        "expected": false
      },
      {
        "args": [
          {
            "x": 1
          }
        ],
        "expected": false
      }
    ]
  },
  "6276": {
    "functionNames": [
      "dict_has_4"
    ],
    "tests": [
      {
        "args": [
          {
            "k4": 1
          }
        ],
        "expected": true
      },
      {
        "args": [
          {}
        ],
        "expected": false
      },
      {
        "args": [
          {
            "x": 1
          }
        ],
        "expected": false
      }
    ]
  },
  "6277": {
    "functionNames": [
      "dict_has_5"
    ],
    "tests": [
      {
        "args": [
          {
            "k5": 1
          }
        ],
        "expected": true
      },
      {
        "args": [
          {}
        ],
        "expected": false
      },
      {
        "args": [
          {
            "x": 1
          }
        ],
        "expected": false
      }
    ]
  },
  "6278": {
    "functionNames": [
      "dict_missing_1"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1
          },
          [
            "a",
            "b"
          ]
        ],
        "expected": [
          "b",
          "k1"
        ]
      },
      {
        "args": [
          {},
          []
        ],
        "expected": [
          "k1"
        ]
      },
      {
        "args": [
          {
            "x": 1
          },
          [
            "y"
          ]
        ],
        "expected": [
          "y",
          "k1"
        ]
      }
    ]
  },
  "6279": {
    "functionNames": [
      "dict_missing_2"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1
          },
          [
            "a",
            "b"
          ]
        ],
        "expected": [
          "b",
          "k2"
        ]
      },
      {
        "args": [
          {},
          []
        ],
        "expected": [
          "k2"
        ]
      },
      {
        "args": [
          {
            "x": 1
          },
          [
            "y"
          ]
        ],
        "expected": [
          "y",
          "k2"
        ]
      }
    ]
  },
  "6280": {
    "functionNames": [
      "dict_missing_3"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1
          },
          [
            "a",
            "b"
          ]
        ],
        "expected": [
          "b",
          "k3"
        ]
      },
      {
        "args": [
          {},
          []
        ],
        "expected": [
          "k3"
        ]
      },
      {
        "args": [
          {
            "x": 1
          },
          [
            "y"
          ]
        ],
        "expected": [
          "y",
          "k3"
        ]
      }
    ]
  },
  "6281": {
    "functionNames": [
      "dict_missing_4"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1
          },
          [
            "a",
            "b"
          ]
        ],
        "expected": [
          "b",
          "k4"
        ]
      },
      {
        "args": [
          {},
          []
        ],
        "expected": [
          "k4"
        ]
      },
      {
        "args": [
          {
            "x": 1
          },
          [
            "y"
          ]
        ],
        "expected": [
          "y",
          "k4"
        ]
      }
    ]
  },
  "6282": {
    "functionNames": [
      "dict_missing_5"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1
          },
          [
            "a",
            "b"
          ]
        ],
        "expected": [
          "b",
          "k5"
        ]
      },
      {
        "args": [
          {},
          []
        ],
        "expected": [
          "k5"
        ]
      },
      {
        "args": [
          {
            "x": 1
          },
          [
            "y"
          ]
        ],
        "expected": [
          "y",
          "k5"
        ]
      }
    ]
  },
  "6283": {
    "functionNames": [
      "dict_prefix_1"
    ],
    "tests": [
      {
        "args": [
          {
            "1a": 1,
            "b": 2
          }
        ],
        "expected": {
          "1a": 1
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {}
      },
      {
        "args": [
          {
            "1x": 9
          }
        ],
        "expected": {
          "1x": 9
        }
      }
    ]
  },
  "6284": {
    "functionNames": [
      "dict_prefix_2"
    ],
    "tests": [
      {
        "args": [
          {
            "2a": 1,
            "b": 2
          }
        ],
        "expected": {
          "2a": 1
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {}
      },
      {
        "args": [
          {
            "2x": 9
          }
        ],
        "expected": {
          "2x": 9
        }
      }
    ]
  },
  "6285": {
    "functionNames": [
      "dict_prefix_3"
    ],
    "tests": [
      {
        "args": [
          {
            "3a": 1,
            "b": 2
          }
        ],
        "expected": {
          "3a": 1
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {}
      },
      {
        "args": [
          {
            "3x": 9
          }
        ],
        "expected": {
          "3x": 9
        }
      }
    ]
  },
  "6286": {
    "functionNames": [
      "dict_prefix_4"
    ],
    "tests": [
      {
        "args": [
          {
            "4a": 1,
            "b": 2
          }
        ],
        "expected": {
          "4a": 1
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {}
      },
      {
        "args": [
          {
            "4x": 9
          }
        ],
        "expected": {
          "4x": 9
        }
      }
    ]
  },
  "6287": {
    "functionNames": [
      "dict_prefix_5"
    ],
    "tests": [
      {
        "args": [
          {
            "5a": 1,
            "b": 2
          }
        ],
        "expected": {
          "5a": 1
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {}
      },
      {
        "args": [
          {
            "5x": 9
          }
        ],
        "expected": {
          "5x": 9
        }
      }
    ]
  },
  "6288": {
    "functionNames": [
      "dict_group_parity_1"
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
        "expected": {
          "even": [
            3
          ],
          "odd": [
            2,
            4
          ]
        }
      },
      {
        "args": [
          []
        ],
        "expected": {
          "even": [],
          "odd": []
        }
      },
      {
        "args": [
          [
            4
          ]
        ],
        "expected": {
          "even": [
            5
          ],
          "odd": []
        }
      }
    ]
  },
  "6289": {
    "functionNames": [
      "dict_group_parity_2"
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
        "expected": {
          "even": [
            4
          ],
          "odd": [
            3,
            5
          ]
        }
      },
      {
        "args": [
          []
        ],
        "expected": {
          "even": [],
          "odd": []
        }
      },
      {
        "args": [
          [
            4
          ]
        ],
        "expected": {
          "even": [
            6
          ],
          "odd": []
        }
      }
    ]
  },
  "6290": {
    "functionNames": [
      "dict_group_parity_3"
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
        "expected": {
          "even": [
            5
          ],
          "odd": [
            4,
            6
          ]
        }
      },
      {
        "args": [
          []
        ],
        "expected": {
          "even": [],
          "odd": []
        }
      },
      {
        "args": [
          [
            4
          ]
        ],
        "expected": {
          "even": [
            7
          ],
          "odd": []
        }
      }
    ]
  },
  "6291": {
    "functionNames": [
      "dict_group_parity_4"
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
        "expected": {
          "even": [
            6
          ],
          "odd": [
            5,
            7
          ]
        }
      },
      {
        "args": [
          []
        ],
        "expected": {
          "even": [],
          "odd": []
        }
      },
      {
        "args": [
          [
            4
          ]
        ],
        "expected": {
          "even": [
            8
          ],
          "odd": []
        }
      }
    ]
  },
  "6292": {
    "functionNames": [
      "dict_group_parity_5"
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
        "expected": {
          "even": [
            7
          ],
          "odd": [
            6,
            8
          ]
        }
      },
      {
        "args": [
          []
        ],
        "expected": {
          "even": [],
          "odd": []
        }
      },
      {
        "args": [
          [
            4
          ]
        ],
        "expected": {
          "even": [
            9
          ],
          "odd": []
        }
      }
    ]
  },
  "6293": {
    "functionNames": [
      "dict_from_pairs_1"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "b"
          ],
          [
            1,
            2
          ]
        ],
        "expected": {
          "a": 1,
          "b": 2,
          "marker": 1
        }
      },
      {
        "args": [
          [],
          []
        ],
        "expected": {
          "marker": 1
        }
      },
      {
        "args": [
          [
            "x"
          ],
          [
            9
          ]
        ],
        "expected": {
          "x": 9,
          "marker": 1
        }
      }
    ]
  },
  "6294": {
    "functionNames": [
      "dict_from_pairs_2"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "b"
          ],
          [
            1,
            2
          ]
        ],
        "expected": {
          "a": 1,
          "b": 2,
          "marker": 2
        }
      },
      {
        "args": [
          [],
          []
        ],
        "expected": {
          "marker": 2
        }
      },
      {
        "args": [
          [
            "x"
          ],
          [
            9
          ]
        ],
        "expected": {
          "x": 9,
          "marker": 2
        }
      }
    ]
  },
  "6295": {
    "functionNames": [
      "dict_from_pairs_3"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "b"
          ],
          [
            1,
            2
          ]
        ],
        "expected": {
          "a": 1,
          "b": 2,
          "marker": 3
        }
      },
      {
        "args": [
          [],
          []
        ],
        "expected": {
          "marker": 3
        }
      },
      {
        "args": [
          [
            "x"
          ],
          [
            9
          ]
        ],
        "expected": {
          "x": 9,
          "marker": 3
        }
      }
    ]
  },
  "6296": {
    "functionNames": [
      "dict_from_pairs_4"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "b"
          ],
          [
            1,
            2
          ]
        ],
        "expected": {
          "a": 1,
          "b": 2,
          "marker": 4
        }
      },
      {
        "args": [
          [],
          []
        ],
        "expected": {
          "marker": 4
        }
      },
      {
        "args": [
          [
            "x"
          ],
          [
            9
          ]
        ],
        "expected": {
          "x": 9,
          "marker": 4
        }
      }
    ]
  },
  "6297": {
    "functionNames": [
      "dict_from_pairs_5"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "b"
          ],
          [
            1,
            2
          ]
        ],
        "expected": {
          "a": 1,
          "b": 2,
          "marker": 5
        }
      },
      {
        "args": [
          [],
          []
        ],
        "expected": {
          "marker": 5
        }
      },
      {
        "args": [
          [
            "x"
          ],
          [
            9
          ]
        ],
        "expected": {
          "x": 9,
          "marker": 5
        }
      }
    ]
  },
  "6298": {
    "functionNames": [
      "dict_best_key_1"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1,
            "b": 5
          }
        ],
        "expected": "b"
      },
      {
        "args": [
          {}
        ],
        "expected": "k1"
      },
      {
        "args": [
          {
            "x": -1
          }
        ],
        "expected": "x"
      }
    ]
  },
  "6299": {
    "functionNames": [
      "dict_best_key_2"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1,
            "b": 5
          }
        ],
        "expected": "b"
      },
      {
        "args": [
          {}
        ],
        "expected": "k2"
      },
      {
        "args": [
          {
            "x": -1
          }
        ],
        "expected": "x"
      }
    ]
  },
  "6300": {
    "functionNames": [
      "dict_best_key_3"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1,
            "b": 5
          }
        ],
        "expected": "b"
      },
      {
        "args": [
          {}
        ],
        "expected": "k3"
      },
      {
        "args": [
          {
            "x": -1
          }
        ],
        "expected": "x"
      }
    ]
  },
  "6301": {
    "functionNames": [
      "dict_best_key_4"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1,
            "b": 5
          }
        ],
        "expected": "b"
      },
      {
        "args": [
          {}
        ],
        "expected": "k4"
      },
      {
        "args": [
          {
            "x": -1
          }
        ],
        "expected": "x"
      }
    ]
  },
  "6302": {
    "functionNames": [
      "dict_best_key_5"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1,
            "b": 5
          }
        ],
        "expected": "b"
      },
      {
        "args": [
          {}
        ],
        "expected": "k5"
      },
      {
        "args": [
          {
            "x": -1
          }
        ],
        "expected": "x"
      }
    ]
  },
  "6303": {
    "functionNames": [
      "dict_nested_1"
    ],
    "tests": [
      {
        "args": [
          {
            "a": {
              "k1": 9
            }
          },
          "a"
        ],
        "expected": 9
      },
      {
        "args": [
          {},
          "x"
        ],
        "expected": 1
      },
      {
        "args": [
          {
            "a": {}
          },
          "a"
        ],
        "expected": 1
      }
    ]
  },
  "6304": {
    "functionNames": [
      "dict_nested_2"
    ],
    "tests": [
      {
        "args": [
          {
            "a": {
              "k2": 9
            }
          },
          "a"
        ],
        "expected": 9
      },
      {
        "args": [
          {},
          "x"
        ],
        "expected": 2
      },
      {
        "args": [
          {
            "a": {}
          },
          "a"
        ],
        "expected": 2
      }
    ]
  },
  "6305": {
    "functionNames": [
      "dict_nested_3"
    ],
    "tests": [
      {
        "args": [
          {
            "a": {
              "k3": 9
            }
          },
          "a"
        ],
        "expected": 9
      },
      {
        "args": [
          {},
          "x"
        ],
        "expected": 3
      },
      {
        "args": [
          {
            "a": {}
          },
          "a"
        ],
        "expected": 3
      }
    ]
  },
  "6306": {
    "functionNames": [
      "dict_nested_4"
    ],
    "tests": [
      {
        "args": [
          {
            "a": {
              "k4": 9
            }
          },
          "a"
        ],
        "expected": 9
      },
      {
        "args": [
          {},
          "x"
        ],
        "expected": 4
      },
      {
        "args": [
          {
            "a": {}
          },
          "a"
        ],
        "expected": 4
      }
    ]
  },
  "6307": {
    "functionNames": [
      "dict_nested_5"
    ],
    "tests": [
      {
        "args": [
          {
            "a": {
              "k5": 9
            }
          },
          "a"
        ],
        "expected": 9
      },
      {
        "args": [
          {},
          "x"
        ],
        "expected": 5
      },
      {
        "args": [
          {
            "a": {}
          },
          "a"
        ],
        "expected": 5
      }
    ]
  },
  "6308": {
    "functionNames": [
      "comp_add_1"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ]
        ],
        "expected": [
          2,
          3
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            -1
          ]
        ],
        "expected": [
          0
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
  "6309": {
    "functionNames": [
      "comp_add_2"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ]
        ],
        "expected": [
          3,
          4
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            -1
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
  "6310": {
    "functionNames": [
      "comp_add_3"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ]
        ],
        "expected": [
          4,
          5
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            -1
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
  "6311": {
    "functionNames": [
      "comp_add_4"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ]
        ],
        "expected": [
          5,
          6
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            -1
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
  "6312": {
    "functionNames": [
      "comp_add_5"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ]
        ],
        "expected": [
          6,
          7
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            -1
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
  "6313": {
    "functionNames": [
      "comp_even_1"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            4,
            6
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
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            2
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
  "6314": {
    "functionNames": [
      "comp_even_2"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            4,
            6
          ]
        ],
        "expected": [
          3,
          6
        ]
      },
      {
        "args": [
          []
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
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "6315": {
    "functionNames": [
      "comp_even_3"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            4,
            6
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
      },
      {
        "args": [
          [
            4
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
  "6316": {
    "functionNames": [
      "comp_even_4"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            4,
            6
          ]
        ],
        "expected": []
      },
      {
        "args": [
          []
        ],
        "expected": []
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
  "6317": {
    "functionNames": [
      "comp_even_5"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            4,
            6
          ]
        ],
        "expected": [
          6
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            6
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
  "6318": {
    "functionNames": [
      "comp_text_1"
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
          "a1",
          "b1"
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            "x"
          ]
        ],
        "expected": [
          "x1"
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
  "6319": {
    "functionNames": [
      "comp_text_2"
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
          "a2",
          "b2"
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            "x"
          ]
        ],
        "expected": [
          "x2"
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
  "6320": {
    "functionNames": [
      "comp_text_3"
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
          "a3",
          "b3"
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            "x"
          ]
        ],
        "expected": [
          "x3"
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
  "6321": {
    "functionNames": [
      "comp_text_4"
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
          "a4",
          "b4"
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            "x"
          ]
        ],
        "expected": [
          "x4"
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
  "6322": {
    "functionNames": [
      "comp_text_5"
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
          "a5",
          "b5"
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            "x"
          ]
        ],
        "expected": [
          "x5"
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
  "6323": {
    "functionNames": [
      "comp_lengths_1"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "code"
          ]
        ],
        "expected": [
          2,
          5
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            "xy"
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
  "6324": {
    "functionNames": [
      "comp_lengths_2"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "code"
          ]
        ],
        "expected": [
          3,
          6
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            "xy"
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
  "6325": {
    "functionNames": [
      "comp_lengths_3"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "code"
          ]
        ],
        "expected": [
          4,
          7
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            "xy"
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
  "6326": {
    "functionNames": [
      "comp_lengths_4"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "code"
          ]
        ],
        "expected": [
          5,
          8
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            "xy"
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
  "6327": {
    "functionNames": [
      "comp_lengths_5"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "code"
          ]
        ],
        "expected": [
          6,
          9
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            "xy"
          ]
        ],
        "expected": [
          7
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
  "6328": {
    "functionNames": [
      "comp_dict_1"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ]
        ],
        "expected": {
          "1": 2,
          "2": 5
        }
      },
      {
        "args": [
          []
        ],
        "expected": {}
      },
      {
        "args": [
          [
            -1
          ]
        ],
        "expected": {
          "-1": 2
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
  "6329": {
    "functionNames": [
      "comp_dict_2"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ]
        ],
        "expected": {
          "1": 3,
          "2": 6
        }
      },
      {
        "args": [
          []
        ],
        "expected": {}
      },
      {
        "args": [
          [
            -1
          ]
        ],
        "expected": {
          "-1": 3
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
  "6330": {
    "functionNames": [
      "comp_dict_3"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ]
        ],
        "expected": {
          "1": 4,
          "2": 7
        }
      },
      {
        "args": [
          []
        ],
        "expected": {}
      },
      {
        "args": [
          [
            -1
          ]
        ],
        "expected": {
          "-1": 4
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
  "6331": {
    "functionNames": [
      "comp_dict_4"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ]
        ],
        "expected": {
          "1": 5,
          "2": 8
        }
      },
      {
        "args": [
          []
        ],
        "expected": {}
      },
      {
        "args": [
          [
            -1
          ]
        ],
        "expected": {
          "-1": 5
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
  "6332": {
    "functionNames": [
      "comp_dict_5"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ]
        ],
        "expected": {
          "1": 6,
          "2": 9
        }
      },
      {
        "args": [
          []
        ],
        "expected": {}
      },
      {
        "args": [
          [
            -1
          ]
        ],
        "expected": {
          "-1": 6
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
  "6333": {
    "functionNames": [
      "comp_set_1"
    ],
    "tests": [
      {
        "args": [
          [
            -1,
            1,
            2
          ]
        ],
        "expected": [
          2,
          3
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            0
          ]
        ],
        "expected": [
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "SetComp",
        "minCount": 1
      }
    ]
  },
  "6334": {
    "functionNames": [
      "comp_set_2"
    ],
    "tests": [
      {
        "args": [
          [
            -1,
            1,
            2
          ]
        ],
        "expected": [
          3,
          4
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            0
          ]
        ],
        "expected": [
          2
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "SetComp",
        "minCount": 1
      }
    ]
  },
  "6335": {
    "functionNames": [
      "comp_set_3"
    ],
    "tests": [
      {
        "args": [
          [
            -1,
            1,
            2
          ]
        ],
        "expected": [
          4,
          5
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            0
          ]
        ],
        "expected": [
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "SetComp",
        "minCount": 1
      }
    ]
  },
  "6336": {
    "functionNames": [
      "comp_set_4"
    ],
    "tests": [
      {
        "args": [
          [
            -1,
            1,
            2
          ]
        ],
        "expected": [
          5,
          6
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            0
          ]
        ],
        "expected": [
          4
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "SetComp",
        "minCount": 1
      }
    ]
  },
  "6337": {
    "functionNames": [
      "comp_set_5"
    ],
    "tests": [
      {
        "args": [
          [
            -1,
            1,
            2
          ]
        ],
        "expected": [
          6,
          7
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            0
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "SetComp",
        "minCount": 1
      }
    ]
  },
  "6338": {
    "functionNames": [
      "comp_indexes_1"
    ],
    "tests": [
      {
        "args": [
          "a1b1"
        ],
        "expected": [
          2,
          4
        ]
      },
      {
        "args": [
          ""
        ],
        "expected": []
      },
      {
        "args": [
          "abc"
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
  "6339": {
    "functionNames": [
      "comp_indexes_2"
    ],
    "tests": [
      {
        "args": [
          "a2b2"
        ],
        "expected": [
          3,
          5
        ]
      },
      {
        "args": [
          ""
        ],
        "expected": []
      },
      {
        "args": [
          "abc"
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
  "6340": {
    "functionNames": [
      "comp_indexes_3"
    ],
    "tests": [
      {
        "args": [
          "a3b3"
        ],
        "expected": [
          4,
          6
        ]
      },
      {
        "args": [
          ""
        ],
        "expected": []
      },
      {
        "args": [
          "abc"
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
  "6341": {
    "functionNames": [
      "comp_indexes_4"
    ],
    "tests": [
      {
        "args": [
          "a4b4"
        ],
        "expected": [
          5,
          7
        ]
      },
      {
        "args": [
          ""
        ],
        "expected": []
      },
      {
        "args": [
          "abc"
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
  "6342": {
    "functionNames": [
      "comp_indexes_5"
    ],
    "tests": [
      {
        "args": [
          "a5b5"
        ],
        "expected": [
          6,
          8
        ]
      },
      {
        "args": [
          ""
        ],
        "expected": []
      },
      {
        "args": [
          "abc"
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
  "6343": {
    "functionNames": [
      "comp_flat_1"
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
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            []
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
  "6344": {
    "functionNames": [
      "comp_flat_2"
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
          2,
          4,
          6
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            []
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
  "6345": {
    "functionNames": [
      "comp_flat_3"
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
          3,
          6,
          9
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            []
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
  "6346": {
    "functionNames": [
      "comp_flat_4"
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
          4,
          8,
          12
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            []
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
  "6347": {
    "functionNames": [
      "comp_flat_5"
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
          5,
          10,
          15
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            []
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
  "6348": {
    "functionNames": [
      "comp_flags_1"
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
        "expected": [
          false,
          true,
          true
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": [
          true
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
  "6349": {
    "functionNames": [
      "comp_flags_2"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            2,
            3
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
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": [
          true
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
  "6350": {
    "functionNames": [
      "comp_flags_3"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            3,
            4
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
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": [
          true
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
  "6351": {
    "functionNames": [
      "comp_flags_4"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            4,
            5
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
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": [
          true
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
  "6352": {
    "functionNames": [
      "comp_flags_5"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            5,
            6
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
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": [
          true
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
  "6353": {
    "functionNames": [
      "comp_pairs_1"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ]
        ],
        "expected": [
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
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            -1
          ]
        ],
        "expected": [
          [
            -1,
            0
          ]
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
  "6354": {
    "functionNames": [
      "comp_pairs_2"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
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
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            -1
          ]
        ],
        "expected": [
          [
            -1,
            1
          ]
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
  "6355": {
    "functionNames": [
      "comp_pairs_3"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ]
        ],
        "expected": [
          [
            1,
            4
          ],
          [
            2,
            5
          ]
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            -1
          ]
        ],
        "expected": [
          [
            -1,
            2
          ]
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
  "6356": {
    "functionNames": [
      "comp_pairs_4"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ]
        ],
        "expected": [
          [
            1,
            5
          ],
          [
            2,
            6
          ]
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            -1
          ]
        ],
        "expected": [
          [
            -1,
            3
          ]
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
  "6357": {
    "functionNames": [
      "comp_pairs_5"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ]
        ],
        "expected": [
          [
            1,
            6
          ],
          [
            2,
            7
          ]
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            -1
          ]
        ],
        "expected": [
          [
            -1,
            4
          ]
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
  "6358": {
    "functionNames": [
      "comp_nested_filter_1"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              5
            ],
            [
              0,
              9
            ]
          ]
        ],
        "expected": [
          5,
          9
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            []
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
  "6359": {
    "functionNames": [
      "comp_nested_filter_2"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              5
            ],
            [
              0,
              9
            ]
          ]
        ],
        "expected": [
          5,
          9
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            []
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
  "6360": {
    "functionNames": [
      "comp_nested_filter_3"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              5
            ],
            [
              0,
              9
            ]
          ]
        ],
        "expected": [
          5,
          9
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            []
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
  "6361": {
    "functionNames": [
      "comp_nested_filter_4"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              5
            ],
            [
              0,
              9
            ]
          ]
        ],
        "expected": [
          5,
          9
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            []
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
  "6362": {
    "functionNames": [
      "comp_nested_filter_5"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              5
            ],
            [
              0,
              9
            ]
          ]
        ],
        "expected": [
          9
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            []
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
  "6363": {
    "functionNames": [
      "comp_coordinate_1"
    ],
    "tests": [
      {
        "args": [
          [
            [
              1,
              0
            ],
            [
              0,
              1
            ]
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
          ]
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            [
              1
            ]
          ]
        ],
        "expected": [
          [
            0,
            0
          ]
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
  "6364": {
    "functionNames": [
      "comp_coordinate_2"
    ],
    "tests": [
      {
        "args": [
          [
            [
              2,
              0
            ],
            [
              0,
              2
            ]
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
          ]
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            [
              1
            ]
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
  "6365": {
    "functionNames": [
      "comp_coordinate_3"
    ],
    "tests": [
      {
        "args": [
          [
            [
              3,
              0
            ],
            [
              0,
              3
            ]
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
          ]
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            [
              1
            ]
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
  "6366": {
    "functionNames": [
      "comp_coordinate_4"
    ],
    "tests": [
      {
        "args": [
          [
            [
              4,
              0
            ],
            [
              0,
              4
            ]
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
          ]
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            [
              1
            ]
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
  "6367": {
    "functionNames": [
      "comp_coordinate_5"
    ],
    "tests": [
      {
        "args": [
          [
            [
              5,
              0
            ],
            [
              0,
              5
            ]
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
          ]
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            [
              1
            ]
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
  "6368": {
    "functionNames": [
      "comp_group_1"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            4
          ]
        ],
        "expected": {
          "0": [
            3
          ],
          "1": [
            1,
            4
          ],
          "2": [
            2
          ]
        }
      },
      {
        "args": [
          []
        ],
        "expected": {
          "0": [],
          "1": [],
          "2": []
        }
      },
      {
        "args": [
          [
            0
          ]
        ],
        "expected": {
          "0": [
            0
          ],
          "1": [],
          "2": []
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
  "6369": {
    "functionNames": [
      "comp_group_2"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            4
          ]
        ],
        "expected": {
          "0": [
            4
          ],
          "1": [
            1
          ],
          "2": [
            2
          ],
          "3": [
            3
          ]
        }
      },
      {
        "args": [
          []
        ],
        "expected": {
          "0": [],
          "1": [],
          "2": [],
          "3": []
        }
      },
      {
        "args": [
          [
            0
          ]
        ],
        "expected": {
          "0": [
            0
          ],
          "1": [],
          "2": [],
          "3": []
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
  "6370": {
    "functionNames": [
      "comp_group_3"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            4
          ]
        ],
        "expected": {
          "0": [],
          "1": [
            1
          ],
          "2": [
            2
          ],
          "3": [
            3
          ],
          "4": [
            4
          ]
        }
      },
      {
        "args": [
          []
        ],
        "expected": {
          "0": [],
          "1": [],
          "2": [],
          "3": [],
          "4": []
        }
      },
      {
        "args": [
          [
            0
          ]
        ],
        "expected": {
          "0": [
            0
          ],
          "1": [],
          "2": [],
          "3": [],
          "4": []
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
  "6371": {
    "functionNames": [
      "comp_group_4"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            4
          ]
        ],
        "expected": {
          "0": [],
          "1": [
            1
          ],
          "2": [
            2
          ],
          "3": [
            3
          ],
          "4": [
            4
          ],
          "5": []
        }
      },
      {
        "args": [
          []
        ],
        "expected": {
          "0": [],
          "1": [],
          "2": [],
          "3": [],
          "4": [],
          "5": []
        }
      },
      {
        "args": [
          [
            0
          ]
        ],
        "expected": {
          "0": [
            0
          ],
          "1": [],
          "2": [],
          "3": [],
          "4": [],
          "5": []
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
  "6372": {
    "functionNames": [
      "comp_group_5"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            4
          ]
        ],
        "expected": {
          "0": [],
          "1": [
            1
          ],
          "2": [
            2
          ],
          "3": [
            3
          ],
          "4": [
            4
          ],
          "5": [],
          "6": []
        }
      },
      {
        "args": [
          []
        ],
        "expected": {
          "0": [],
          "1": [],
          "2": [],
          "3": [],
          "4": [],
          "5": [],
          "6": []
        }
      },
      {
        "args": [
          [
            0
          ]
        ],
        "expected": {
          "0": [
            0
          ],
          "1": [],
          "2": [],
          "3": [],
          "4": [],
          "5": [],
          "6": []
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
  "6373": {
    "functionNames": [
      "comp_transpose_1"
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
            2,
            4
          ],
          [
            3,
            5
          ]
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            [
              5
            ]
          ]
        ],
        "expected": [
          [
            6
          ]
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
  "6374": {
    "functionNames": [
      "comp_transpose_2"
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
            3,
            5
          ],
          [
            4,
            6
          ]
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            [
              5
            ]
          ]
        ],
        "expected": [
          [
            7
          ]
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
  "6375": {
    "functionNames": [
      "comp_transpose_3"
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
            4,
            6
          ],
          [
            5,
            7
          ]
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            [
              5
            ]
          ]
        ],
        "expected": [
          [
            8
          ]
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
  "6376": {
    "functionNames": [
      "comp_transpose_4"
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
            5,
            7
          ],
          [
            6,
            8
          ]
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            [
              5
            ]
          ]
        ],
        "expected": [
          [
            9
          ]
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
  "6377": {
    "functionNames": [
      "comp_transpose_5"
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
            6,
            8
          ],
          [
            7,
            9
          ]
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            [
              5
            ]
          ]
        ],
        "expected": [
          [
            10
          ]
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
  "6378": {
    "functionNames": [
      "comp_word_map_1"
    ],
    "tests": [
      {
        "args": [
          [
            "A",
            "code"
          ]
        ],
        "expected": {
          "a": "A",
          "code": "CODE"
        }
      },
      {
        "args": [
          []
        ],
        "expected": {}
      },
      {
        "args": [
          [
            "Python"
          ]
        ],
        "expected": {
          "python": "PYTHON"
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
  "6379": {
    "functionNames": [
      "comp_word_map_2"
    ],
    "tests": [
      {
        "args": [
          [
            "A",
            "code"
          ]
        ],
        "expected": {
          "code": "CODE"
        }
      },
      {
        "args": [
          []
        ],
        "expected": {}
      },
      {
        "args": [
          [
            "Python"
          ]
        ],
        "expected": {
          "python": "PYTHON"
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
  "6380": {
    "functionNames": [
      "comp_word_map_3"
    ],
    "tests": [
      {
        "args": [
          [
            "A",
            "code"
          ]
        ],
        "expected": {
          "code": "CODE"
        }
      },
      {
        "args": [
          []
        ],
        "expected": {}
      },
      {
        "args": [
          [
            "Python"
          ]
        ],
        "expected": {
          "python": "PYTHON"
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
  "6381": {
    "functionNames": [
      "comp_word_map_4"
    ],
    "tests": [
      {
        "args": [
          [
            "A",
            "code"
          ]
        ],
        "expected": {
          "code": "CODE"
        }
      },
      {
        "args": [
          []
        ],
        "expected": {}
      },
      {
        "args": [
          [
            "Python"
          ]
        ],
        "expected": {
          "python": "PYTHON"
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
  "6382": {
    "functionNames": [
      "comp_word_map_5"
    ],
    "tests": [
      {
        "args": [
          [
            "A",
            "code"
          ]
        ],
        "expected": {}
      },
      {
        "args": [
          []
        ],
        "expected": {}
      },
      {
        "args": [
          [
            "Python"
          ]
        ],
        "expected": {
          "python": "PYTHON"
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
  "6383": {
    "functionNames": [
      "comp_products_1"
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
          3,
          4,
          6,
          8
        ]
      },
      {
        "args": [
          [],
          [
            1
          ]
        ],
        "expected": []
      },
      {
        "args": [
          [
            2
          ],
          [
            1
          ]
        ],
        "expected": [
          2
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "SetComp",
        "minCount": 1
      }
    ]
  },
  "6384": {
    "functionNames": [
      "comp_products_2"
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
          3,
          4,
          6,
          8
        ]
      },
      {
        "args": [
          [],
          [
            1
          ]
        ],
        "expected": []
      },
      {
        "args": [
          [
            3
          ],
          [
            1
          ]
        ],
        "expected": [
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "SetComp",
        "minCount": 1
      }
    ]
  },
  "6385": {
    "functionNames": [
      "comp_products_3"
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
          4,
          6,
          8
        ]
      },
      {
        "args": [
          [],
          [
            1
          ]
        ],
        "expected": []
      },
      {
        "args": [
          [
            4
          ],
          [
            1
          ]
        ],
        "expected": [
          4
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "SetComp",
        "minCount": 1
      }
    ]
  },
  "6386": {
    "functionNames": [
      "comp_products_4"
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
          6,
          8
        ]
      },
      {
        "args": [
          [],
          [
            1
          ]
        ],
        "expected": []
      },
      {
        "args": [
          [
            5
          ],
          [
            1
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "SetComp",
        "minCount": 1
      }
    ]
  },
  "6387": {
    "functionNames": [
      "comp_products_5"
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
          6,
          8
        ]
      },
      {
        "args": [
          [],
          [
            1
          ]
        ],
        "expected": []
      },
      {
        "args": [
          [
            6
          ],
          [
            1
          ]
        ],
        "expected": [
          6
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "SetComp",
        "minCount": 1
      }
    ]
  },
  "6388": {
    "functionNames": [
      "comp_running_windows_1"
    ],
    "tests": [
      {
        "args": [
          [
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
          5,
          7,
          9,
          11
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            9
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
  "6389": {
    "functionNames": [
      "comp_running_windows_2"
    ],
    "tests": [
      {
        "args": [
          [
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
          9,
          12,
          15
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            9
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
  "6390": {
    "functionNames": [
      "comp_running_windows_3"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            4,
            5,
            6
          ]
        ],
        "expected": [
          10,
          14,
          18
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            9
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
  "6391": {
    "functionNames": [
      "comp_running_windows_4"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            4,
            5,
            6
          ]
        ],
        "expected": [
          15,
          20
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            9
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
  "6392": {
    "functionNames": [
      "comp_running_windows_5"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3,
            4,
            5,
            6
          ]
        ],
        "expected": [
          21
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            9
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
  "6393": {
    "functionNames": [
      "comp_invert_groups_1"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1,
            "b": 2
          }
        ],
        "expected": {
          "1": "a1",
          "2": "b1"
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {}
      },
      {
        "args": [
          {
            "x": 9
          }
        ],
        "expected": {
          "9": "x1"
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
  "6394": {
    "functionNames": [
      "comp_invert_groups_2"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1,
            "b": 2
          }
        ],
        "expected": {
          "1": "a2",
          "2": "b2"
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {}
      },
      {
        "args": [
          {
            "x": 9
          }
        ],
        "expected": {
          "9": "x2"
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
  "6395": {
    "functionNames": [
      "comp_invert_groups_3"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1,
            "b": 2
          }
        ],
        "expected": {
          "1": "a3",
          "2": "b3"
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {}
      },
      {
        "args": [
          {
            "x": 9
          }
        ],
        "expected": {
          "9": "x3"
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
  "6396": {
    "functionNames": [
      "comp_invert_groups_4"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1,
            "b": 2
          }
        ],
        "expected": {
          "1": "a4",
          "2": "b4"
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {}
      },
      {
        "args": [
          {
            "x": 9
          }
        ],
        "expected": {
          "9": "x4"
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
  "6397": {
    "functionNames": [
      "comp_invert_groups_5"
    ],
    "tests": [
      {
        "args": [
          {
            "a": 1,
            "b": 2
          }
        ],
        "expected": {
          "1": "a5",
          "2": "b5"
        }
      },
      {
        "args": [
          {}
        ],
        "expected": {}
      },
      {
        "args": [
          {
            "x": 9
          }
        ],
        "expected": {
          "9": "x5"
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
  "6398": {
    "functionNames": [
      "comp_diagonal_1"
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
          2,
          5
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            [
              5
            ]
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
  "6399": {
    "functionNames": [
      "comp_diagonal_2"
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
          6
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            [
              5
            ]
          ]
        ],
        "expected": [
          7
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
  "6400": {
    "functionNames": [
      "comp_diagonal_3"
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
          7
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            [
              5
            ]
          ]
        ],
        "expected": [
          8
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
  "6401": {
    "functionNames": [
      "comp_diagonal_4"
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
          5,
          8
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            [
              5
            ]
          ]
        ],
        "expected": [
          9
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
  "6402": {
    "functionNames": [
      "comp_diagonal_5"
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
          6,
          9
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            [
              5
            ]
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
  "6403": {
    "functionNames": [
      "comp_conditional_1"
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
        "expected": [
          0,
          -1,
          4
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            -2
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
  "6404": {
    "functionNames": [
      "comp_conditional_2"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            2,
            3
          ]
        ],
        "expected": [
          0,
          -2,
          9
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            -2
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
  "6405": {
    "functionNames": [
      "comp_conditional_3"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            3,
            4
          ]
        ],
        "expected": [
          0,
          -3,
          16
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            -2
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
  "6406": {
    "functionNames": [
      "comp_conditional_4"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            4,
            5
          ]
        ],
        "expected": [
          0,
          -4,
          25
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            -2
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
  "6407": {
    "functionNames": [
      "comp_conditional_5"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            5,
            6
          ]
        ],
        "expected": [
          0,
          -5,
          36
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            -2
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
  "6408": {
    "functionNames": [
      "closure_add_1"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          5
        ],
        "expected": 6
      },
      {
        "args": [],
        "callReturnedWith": [
          -1
        ],
        "expected": 0
      },
      {
        "args": [],
        "callReturnedWith": [
          0
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
  "6409": {
    "functionNames": [
      "closure_add_2"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          5
        ],
        "expected": 7
      },
      {
        "args": [],
        "callReturnedWith": [
          -1
        ],
        "expected": 1
      },
      {
        "args": [],
        "callReturnedWith": [
          0
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
  "6410": {
    "functionNames": [
      "closure_add_3"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          5
        ],
        "expected": 8
      },
      {
        "args": [],
        "callReturnedWith": [
          -1
        ],
        "expected": 2
      },
      {
        "args": [],
        "callReturnedWith": [
          0
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "6411": {
    "functionNames": [
      "closure_add_4"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          5
        ],
        "expected": 9
      },
      {
        "args": [],
        "callReturnedWith": [
          -1
        ],
        "expected": 3
      },
      {
        "args": [],
        "callReturnedWith": [
          0
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
  "6412": {
    "functionNames": [
      "closure_add_5"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          5
        ],
        "expected": 10
      },
      {
        "args": [],
        "callReturnedWith": [
          -1
        ],
        "expected": 4
      },
      {
        "args": [],
        "callReturnedWith": [
          0
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
  "6413": {
    "functionNames": [
      "closure_multiply_1"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          5
        ],
        "expected": 5
      },
      {
        "args": [],
        "callReturnedWith": [
          -1
        ],
        "expected": -1
      },
      {
        "args": [],
        "callReturnedWith": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "6414": {
    "functionNames": [
      "closure_multiply_2"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          5
        ],
        "expected": 10
      },
      {
        "args": [],
        "callReturnedWith": [
          -1
        ],
        "expected": -2
      },
      {
        "args": [],
        "callReturnedWith": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "6415": {
    "functionNames": [
      "closure_multiply_3"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          5
        ],
        "expected": 15
      },
      {
        "args": [],
        "callReturnedWith": [
          -1
        ],
        "expected": -3
      },
      {
        "args": [],
        "callReturnedWith": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "6416": {
    "functionNames": [
      "closure_multiply_4"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          5
        ],
        "expected": 20
      },
      {
        "args": [],
        "callReturnedWith": [
          -1
        ],
        "expected": -4
      },
      {
        "args": [],
        "callReturnedWith": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "6417": {
    "functionNames": [
      "closure_multiply_5"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          5
        ],
        "expected": 25
      },
      {
        "args": [],
        "callReturnedWith": [
          -1
        ],
        "expected": -5
      },
      {
        "args": [],
        "callReturnedWith": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "6418": {
    "functionNames": [
      "closure_prefix_1"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          "code"
        ],
        "expected": "1:code"
      },
      {
        "args": [],
        "callReturnedWith": [
          ""
        ],
        "expected": "1:"
      },
      {
        "args": [],
        "callReturnedWith": [
          "x"
        ],
        "expected": "1:x"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "6419": {
    "functionNames": [
      "closure_prefix_2"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          "code"
        ],
        "expected": "2:code"
      },
      {
        "args": [],
        "callReturnedWith": [
          ""
        ],
        "expected": "2:"
      },
      {
        "args": [],
        "callReturnedWith": [
          "x"
        ],
        "expected": "2:x"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "6420": {
    "functionNames": [
      "closure_prefix_3"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          "code"
        ],
        "expected": "3:code"
      },
      {
        "args": [],
        "callReturnedWith": [
          ""
        ],
        "expected": "3:"
      },
      {
        "args": [],
        "callReturnedWith": [
          "x"
        ],
        "expected": "3:x"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "6421": {
    "functionNames": [
      "closure_prefix_4"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          "code"
        ],
        "expected": "4:code"
      },
      {
        "args": [],
        "callReturnedWith": [
          ""
        ],
        "expected": "4:"
      },
      {
        "args": [],
        "callReturnedWith": [
          "x"
        ],
        "expected": "4:x"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "6422": {
    "functionNames": [
      "closure_prefix_5"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          "code"
        ],
        "expected": "5:code"
      },
      {
        "args": [],
        "callReturnedWith": [
          ""
        ],
        "expected": "5:"
      },
      {
        "args": [],
        "callReturnedWith": [
          "x"
        ],
        "expected": "5:x"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "6423": {
    "functionNames": [
      "closure_suffix_1"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          "code"
        ],
        "expected": "code:1"
      },
      {
        "args": [],
        "callReturnedWith": [
          ""
        ],
        "expected": ":1"
      },
      {
        "args": [],
        "callReturnedWith": [
          "x"
        ],
        "expected": "x:1"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "6424": {
    "functionNames": [
      "closure_suffix_2"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          "code"
        ],
        "expected": "code:2"
      },
      {
        "args": [],
        "callReturnedWith": [
          ""
        ],
        "expected": ":2"
      },
      {
        "args": [],
        "callReturnedWith": [
          "x"
        ],
        "expected": "x:2"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "6425": {
    "functionNames": [
      "closure_suffix_3"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          "code"
        ],
        "expected": "code:3"
      },
      {
        "args": [],
        "callReturnedWith": [
          ""
        ],
        "expected": ":3"
      },
      {
        "args": [],
        "callReturnedWith": [
          "x"
        ],
        "expected": "x:3"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "6426": {
    "functionNames": [
      "closure_suffix_4"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          "code"
        ],
        "expected": "code:4"
      },
      {
        "args": [],
        "callReturnedWith": [
          ""
        ],
        "expected": ":4"
      },
      {
        "args": [],
        "callReturnedWith": [
          "x"
        ],
        "expected": "x:4"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "6427": {
    "functionNames": [
      "closure_suffix_5"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          "code"
        ],
        "expected": "code:5"
      },
      {
        "args": [],
        "callReturnedWith": [
          ""
        ],
        "expected": ":5"
      },
      {
        "args": [],
        "callReturnedWith": [
          "x"
        ],
        "expected": "x:5"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "6428": {
    "functionNames": [
      "closure_power_1"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          2
        ],
        "expected": 4
      },
      {
        "args": [],
        "callReturnedWith": [
          1
        ],
        "expected": 1
      },
      {
        "args": [],
        "callReturnedWith": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "6429": {
    "functionNames": [
      "closure_power_2"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          2
        ],
        "expected": 8
      },
      {
        "args": [],
        "callReturnedWith": [
          1
        ],
        "expected": 1
      },
      {
        "args": [],
        "callReturnedWith": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "6430": {
    "functionNames": [
      "closure_power_3"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          2
        ],
        "expected": 16
      },
      {
        "args": [],
        "callReturnedWith": [
          1
        ],
        "expected": 1
      },
      {
        "args": [],
        "callReturnedWith": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "6431": {
    "functionNames": [
      "closure_power_4"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          2
        ],
        "expected": 32
      },
      {
        "args": [],
        "callReturnedWith": [
          1
        ],
        "expected": 1
      },
      {
        "args": [],
        "callReturnedWith": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "6432": {
    "functionNames": [
      "closure_power_5"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          2
        ],
        "expected": 64
      },
      {
        "args": [],
        "callReturnedWith": [
          1
        ],
        "expected": 1
      },
      {
        "args": [],
        "callReturnedWith": [
          0
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "6433": {
    "functionNames": [
      "closure_minimum_1"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          0
        ],
        "expected": 1
      },
      {
        "args": [],
        "callReturnedWith": [
          3
        ],
        "expected": 3
      },
      {
        "args": [],
        "callReturnedWith": [
          1
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
  "6434": {
    "functionNames": [
      "closure_minimum_2"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          0
        ],
        "expected": 2
      },
      {
        "args": [],
        "callReturnedWith": [
          4
        ],
        "expected": 4
      },
      {
        "args": [],
        "callReturnedWith": [
          2
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
  "6435": {
    "functionNames": [
      "closure_minimum_3"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          0
        ],
        "expected": 3
      },
      {
        "args": [],
        "callReturnedWith": [
          5
        ],
        "expected": 5
      },
      {
        "args": [],
        "callReturnedWith": [
          3
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "6436": {
    "functionNames": [
      "closure_minimum_4"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          0
        ],
        "expected": 4
      },
      {
        "args": [],
        "callReturnedWith": [
          6
        ],
        "expected": 6
      },
      {
        "args": [],
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
  "6437": {
    "functionNames": [
      "closure_minimum_5"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          0
        ],
        "expected": 5
      },
      {
        "args": [],
        "callReturnedWith": [
          7
        ],
        "expected": 7
      },
      {
        "args": [],
        "callReturnedWith": [
          5
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
  "6438": {
    "functionNames": [
      "closure_member_1"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          1
        ],
        "expected": true
      },
      {
        "args": [],
        "callReturnedWith": [
          3
        ],
        "expected": false
      },
      {
        "args": [],
        "callReturnedWith": [
          2
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
  "6439": {
    "functionNames": [
      "closure_member_2"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          2
        ],
        "expected": true
      },
      {
        "args": [],
        "callReturnedWith": [
          4
        ],
        "expected": false
      },
      {
        "args": [],
        "callReturnedWith": [
          3
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
  "6440": {
    "functionNames": [
      "closure_member_3"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          3
        ],
        "expected": true
      },
      {
        "args": [],
        "callReturnedWith": [
          5
        ],
        "expected": false
      },
      {
        "args": [],
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
  "6441": {
    "functionNames": [
      "closure_member_4"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          4
        ],
        "expected": true
      },
      {
        "args": [],
        "callReturnedWith": [
          6
        ],
        "expected": false
      },
      {
        "args": [],
        "callReturnedWith": [
          5
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
  "6442": {
    "functionNames": [
      "closure_member_5"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          5
        ],
        "expected": true
      },
      {
        "args": [],
        "callReturnedWith": [
          7
        ],
        "expected": false
      },
      {
        "args": [],
        "callReturnedWith": [
          6
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
  "6443": {
    "functionNames": [
      "closure_above_1"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          2
        ],
        "expected": true
      },
      {
        "args": [],
        "callReturnedWith": [
          1
        ],
        "expected": false
      },
      {
        "args": [],
        "callReturnedWith": [
          0
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
  "6444": {
    "functionNames": [
      "closure_above_2"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          3
        ],
        "expected": true
      },
      {
        "args": [],
        "callReturnedWith": [
          2
        ],
        "expected": false
      },
      {
        "args": [],
        "callReturnedWith": [
          0
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
  "6445": {
    "functionNames": [
      "closure_above_3"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          4
        ],
        "expected": true
      },
      {
        "args": [],
        "callReturnedWith": [
          3
        ],
        "expected": false
      },
      {
        "args": [],
        "callReturnedWith": [
          0
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
  "6446": {
    "functionNames": [
      "closure_above_4"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          5
        ],
        "expected": true
      },
      {
        "args": [],
        "callReturnedWith": [
          4
        ],
        "expected": false
      },
      {
        "args": [],
        "callReturnedWith": [
          0
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
  "6447": {
    "functionNames": [
      "closure_above_5"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          6
        ],
        "expected": true
      },
      {
        "args": [],
        "callReturnedWith": [
          5
        ],
        "expected": false
      },
      {
        "args": [],
        "callReturnedWith": [
          0
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
  "6448": {
    "functionNames": [
      "closure_label_1"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          "Ana"
        ],
        "expected": "L1=Ana"
      },
      {
        "args": [],
        "callReturnedWith": [
          ""
        ],
        "expected": "L1="
      },
      {
        "args": [],
        "callReturnedWith": [
          "X"
        ],
        "expected": "L1=X"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "6449": {
    "functionNames": [
      "closure_label_2"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          "Ana"
        ],
        "expected": "L2=Ana"
      },
      {
        "args": [],
        "callReturnedWith": [
          ""
        ],
        "expected": "L2="
      },
      {
        "args": [],
        "callReturnedWith": [
          "X"
        ],
        "expected": "L2=X"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "6450": {
    "functionNames": [
      "closure_label_3"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          "Ana"
        ],
        "expected": "L3=Ana"
      },
      {
        "args": [],
        "callReturnedWith": [
          ""
        ],
        "expected": "L3="
      },
      {
        "args": [],
        "callReturnedWith": [
          "X"
        ],
        "expected": "L3=X"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "6451": {
    "functionNames": [
      "closure_label_4"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          "Ana"
        ],
        "expected": "L4=Ana"
      },
      {
        "args": [],
        "callReturnedWith": [
          ""
        ],
        "expected": "L4="
      },
      {
        "args": [],
        "callReturnedWith": [
          "X"
        ],
        "expected": "L4=X"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "6452": {
    "functionNames": [
      "closure_label_5"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          "Ana"
        ],
        "expected": "L5=Ana"
      },
      {
        "args": [],
        "callReturnedWith": [
          ""
        ],
        "expected": "L5="
      },
      {
        "args": [],
        "callReturnedWith": [
          "X"
        ],
        "expected": "L5=X"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "6453": {
    "functionNames": [
      "closure_offset_length_1"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          [
            1,
            2
          ]
        ],
        "expected": 3
      },
      {
        "args": [],
        "callReturnedWith": [
          "abc"
        ],
        "expected": 4
      },
      {
        "args": [],
        "callReturnedWith": [
          []
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
  "6454": {
    "functionNames": [
      "closure_offset_length_2"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          [
            1,
            2
          ]
        ],
        "expected": 4
      },
      {
        "args": [],
        "callReturnedWith": [
          "abc"
        ],
        "expected": 5
      },
      {
        "args": [],
        "callReturnedWith": [
          []
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
  "6455": {
    "functionNames": [
      "closure_offset_length_3"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          [
            1,
            2
          ]
        ],
        "expected": 5
      },
      {
        "args": [],
        "callReturnedWith": [
          "abc"
        ],
        "expected": 6
      },
      {
        "args": [],
        "callReturnedWith": [
          []
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "FunctionDef",
        "minCount": 2
      }
    ]
  },
  "6456": {
    "functionNames": [
      "closure_offset_length_4"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          [
            1,
            2
          ]
        ],
        "expected": 6
      },
      {
        "args": [],
        "callReturnedWith": [
          "abc"
        ],
        "expected": 7
      },
      {
        "args": [],
        "callReturnedWith": [
          []
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
  "6457": {
    "functionNames": [
      "closure_offset_length_5"
    ],
    "tests": [
      {
        "args": [],
        "callReturnedWith": [
          [
            1,
            2
          ]
        ],
        "expected": 7
      },
      {
        "args": [],
        "callReturnedWith": [
          "abc"
        ],
        "expected": 8
      },
      {
        "args": [],
        "callReturnedWith": [
          []
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
  "6458": {
    "functionNames": [
      "lambda_add_1"
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
          -1
        ],
        "expected": 0
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
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6459": {
    "functionNames": [
      "lambda_add_2"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 7
      },
      {
        "args": [
          -1
        ],
        "expected": 1
      },
      {
        "args": [
          0
        ],
        "expected": 2
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6460": {
    "functionNames": [
      "lambda_add_3"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 8
      },
      {
        "args": [
          -1
        ],
        "expected": 2
      },
      {
        "args": [
          0
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6461": {
    "functionNames": [
      "lambda_add_4"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 9
      },
      {
        "args": [
          -1
        ],
        "expected": 3
      },
      {
        "args": [
          0
        ],
        "expected": 4
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6462": {
    "functionNames": [
      "lambda_add_5"
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
          -1
        ],
        "expected": 4
      },
      {
        "args": [
          0
        ],
        "expected": 5
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6463": {
    "functionNames": [
      "lambda_multiply_1"
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
          -1
        ],
        "expected": -1
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
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6464": {
    "functionNames": [
      "lambda_multiply_2"
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
          -1
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
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6465": {
    "functionNames": [
      "lambda_multiply_3"
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
          -1
        ],
        "expected": -3
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
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6466": {
    "functionNames": [
      "lambda_multiply_4"
    ],
    "tests": [
      {
        "args": [
          5
        ],
        "expected": 20
      },
      {
        "args": [
          -1
        ],
        "expected": -4
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
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6467": {
    "functionNames": [
      "lambda_multiply_5"
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
          -1
        ],
        "expected": -5
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
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6468": {
    "functionNames": [
      "lambda_square_1"
    ],
    "tests": [
      {
        "args": [
          3
        ],
        "expected": 10
      },
      {
        "args": [
          -2
        ],
        "expected": 5
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
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6469": {
    "functionNames": [
      "lambda_square_2"
    ],
    "tests": [
      {
        "args": [
          3
        ],
        "expected": 11
      },
      {
        "args": [
          -2
        ],
        "expected": 6
      },
      {
        "args": [
          0
        ],
        "expected": 2
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6470": {
    "functionNames": [
      "lambda_square_3"
    ],
    "tests": [
      {
        "args": [
          3
        ],
        "expected": 12
      },
      {
        "args": [
          -2
        ],
        "expected": 7
      },
      {
        "args": [
          0
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6471": {
    "functionNames": [
      "lambda_square_4"
    ],
    "tests": [
      {
        "args": [
          3
        ],
        "expected": 13
      },
      {
        "args": [
          -2
        ],
        "expected": 8
      },
      {
        "args": [
          0
        ],
        "expected": 4
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6472": {
    "functionNames": [
      "lambda_square_5"
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
          -2
        ],
        "expected": 9
      },
      {
        "args": [
          0
        ],
        "expected": 5
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6473": {
    "functionNames": [
      "lambda_distance_1"
    ],
    "tests": [
      {
        "args": [
          10
        ],
        "expected": 9
      },
      {
        "args": [
          -1
        ],
        "expected": 2
      },
      {
        "args": [
          1
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6474": {
    "functionNames": [
      "lambda_distance_2"
    ],
    "tests": [
      {
        "args": [
          10
        ],
        "expected": 8
      },
      {
        "args": [
          -1
        ],
        "expected": 3
      },
      {
        "args": [
          2
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6475": {
    "functionNames": [
      "lambda_distance_3"
    ],
    "tests": [
      {
        "args": [
          10
        ],
        "expected": 7
      },
      {
        "args": [
          -1
        ],
        "expected": 4
      },
      {
        "args": [
          3
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6476": {
    "functionNames": [
      "lambda_distance_4"
    ],
    "tests": [
      {
        "args": [
          10
        ],
        "expected": 6
      },
      {
        "args": [
          -1
        ],
        "expected": 5
      },
      {
        "args": [
          4
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6477": {
    "functionNames": [
      "lambda_distance_5"
    ],
    "tests": [
      {
        "args": [
          10
        ],
        "expected": 5
      },
      {
        "args": [
          -1
        ],
        "expected": 6
      },
      {
        "args": [
          5
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6478": {
    "functionNames": [
      "lambda_divisible_1"
    ],
    "tests": [
      {
        "args": [
          2
        ],
        "expected": true
      },
      {
        "args": [
          3
        ],
        "expected": false
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
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6479": {
    "functionNames": [
      "lambda_divisible_2"
    ],
    "tests": [
      {
        "args": [
          3
        ],
        "expected": true
      },
      {
        "args": [
          4
        ],
        "expected": false
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
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6480": {
    "functionNames": [
      "lambda_divisible_3"
    ],
    "tests": [
      {
        "args": [
          4
        ],
        "expected": true
      },
      {
        "args": [
          5
        ],
        "expected": false
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
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6481": {
    "functionNames": [
      "lambda_divisible_4"
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
          6
        ],
        "expected": false
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
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6482": {
    "functionNames": [
      "lambda_divisible_5"
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
          7
        ],
        "expected": false
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
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6483": {
    "functionNames": [
      "lambda_suffix_1"
    ],
    "tests": [
      {
        "args": [
          "code"
        ],
        "expected": "code1"
      },
      {
        "args": [
          ""
        ],
        "expected": "1"
      },
      {
        "args": [
          "x"
        ],
        "expected": "x1"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6484": {
    "functionNames": [
      "lambda_suffix_2"
    ],
    "tests": [
      {
        "args": [
          "code"
        ],
        "expected": "code2"
      },
      {
        "args": [
          ""
        ],
        "expected": "2"
      },
      {
        "args": [
          "x"
        ],
        "expected": "x2"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6485": {
    "functionNames": [
      "lambda_suffix_3"
    ],
    "tests": [
      {
        "args": [
          "code"
        ],
        "expected": "code3"
      },
      {
        "args": [
          ""
        ],
        "expected": "3"
      },
      {
        "args": [
          "x"
        ],
        "expected": "x3"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6486": {
    "functionNames": [
      "lambda_suffix_4"
    ],
    "tests": [
      {
        "args": [
          "code"
        ],
        "expected": "code4"
      },
      {
        "args": [
          ""
        ],
        "expected": "4"
      },
      {
        "args": [
          "x"
        ],
        "expected": "x4"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6487": {
    "functionNames": [
      "lambda_suffix_5"
    ],
    "tests": [
      {
        "args": [
          "code"
        ],
        "expected": "code5"
      },
      {
        "args": [
          ""
        ],
        "expected": "5"
      },
      {
        "args": [
          "x"
        ],
        "expected": "x5"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6488": {
    "functionNames": [
      "lambda_first_1"
    ],
    "tests": [
      {
        "args": [
          "abc"
        ],
        "expected": "a"
      },
      {
        "args": [
          ""
        ],
        "expected": "1"
      },
      {
        "args": [
          "x"
        ],
        "expected": "x"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6489": {
    "functionNames": [
      "lambda_first_2"
    ],
    "tests": [
      {
        "args": [
          "abc"
        ],
        "expected": "a"
      },
      {
        "args": [
          ""
        ],
        "expected": "2"
      },
      {
        "args": [
          "x"
        ],
        "expected": "x"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6490": {
    "functionNames": [
      "lambda_first_3"
    ],
    "tests": [
      {
        "args": [
          "abc"
        ],
        "expected": "a"
      },
      {
        "args": [
          ""
        ],
        "expected": "3"
      },
      {
        "args": [
          "x"
        ],
        "expected": "x"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6491": {
    "functionNames": [
      "lambda_first_4"
    ],
    "tests": [
      {
        "args": [
          "abc"
        ],
        "expected": "a"
      },
      {
        "args": [
          ""
        ],
        "expected": "4"
      },
      {
        "args": [
          "x"
        ],
        "expected": "x"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6492": {
    "functionNames": [
      "lambda_first_5"
    ],
    "tests": [
      {
        "args": [
          "abc"
        ],
        "expected": "a"
      },
      {
        "args": [
          ""
        ],
        "expected": "5"
      },
      {
        "args": [
          "x"
        ],
        "expected": "x"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6493": {
    "functionNames": [
      "lambda_length_1"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ]
        ],
        "expected": 3
      },
      {
        "args": [
          []
        ],
        "expected": 1
      },
      {
        "args": [
          "abc"
        ],
        "expected": 4
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6494": {
    "functionNames": [
      "lambda_length_2"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ]
        ],
        "expected": 4
      },
      {
        "args": [
          []
        ],
        "expected": 2
      },
      {
        "args": [
          "abc"
        ],
        "expected": 5
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6495": {
    "functionNames": [
      "lambda_length_3"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ]
        ],
        "expected": 5
      },
      {
        "args": [
          []
        ],
        "expected": 3
      },
      {
        "args": [
          "abc"
        ],
        "expected": 6
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6496": {
    "functionNames": [
      "lambda_length_4"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ]
        ],
        "expected": 6
      },
      {
        "args": [
          []
        ],
        "expected": 4
      },
      {
        "args": [
          "abc"
        ],
        "expected": 7
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6497": {
    "functionNames": [
      "lambda_length_5"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ]
        ],
        "expected": 7
      },
      {
        "args": [
          []
        ],
        "expected": 5
      },
      {
        "args": [
          "abc"
        ],
        "expected": 8
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6498": {
    "functionNames": [
      "lambda_pair_1"
    ],
    "tests": [
      {
        "args": [
          1
        ],
        "expected": [
          1,
          2
        ]
      },
      {
        "args": [
          -1
        ],
        "expected": [
          -1,
          0
        ]
      },
      {
        "args": [
          0
        ],
        "expected": [
          0,
          1
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6499": {
    "functionNames": [
      "lambda_pair_2"
    ],
    "tests": [
      {
        "args": [
          1
        ],
        "expected": [
          1,
          3
        ]
      },
      {
        "args": [
          -1
        ],
        "expected": [
          -1,
          1
        ]
      },
      {
        "args": [
          0
        ],
        "expected": [
          0,
          2
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6500": {
    "functionNames": [
      "lambda_pair_3"
    ],
    "tests": [
      {
        "args": [
          1
        ],
        "expected": [
          1,
          4
        ]
      },
      {
        "args": [
          -1
        ],
        "expected": [
          -1,
          2
        ]
      },
      {
        "args": [
          0
        ],
        "expected": [
          0,
          3
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6501": {
    "functionNames": [
      "lambda_pair_4"
    ],
    "tests": [
      {
        "args": [
          1
        ],
        "expected": [
          1,
          5
        ]
      },
      {
        "args": [
          -1
        ],
        "expected": [
          -1,
          3
        ]
      },
      {
        "args": [
          0
        ],
        "expected": [
          0,
          4
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6502": {
    "functionNames": [
      "lambda_pair_5"
    ],
    "tests": [
      {
        "args": [
          1
        ],
        "expected": [
          1,
          6
        ]
      },
      {
        "args": [
          -1
        ],
        "expected": [
          -1,
          4
        ]
      },
      {
        "args": [
          0
        ],
        "expected": [
          0,
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6503": {
    "functionNames": [
      "lambda_default_1"
    ],
    "tests": [
      {
        "args": [
          {
            "k1": 9
          }
        ],
        "expected": 9
      },
      {
        "args": [
          {}
        ],
        "expected": 1
      },
      {
        "args": [
          {
            "x": 1
          }
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6504": {
    "functionNames": [
      "lambda_default_2"
    ],
    "tests": [
      {
        "args": [
          {
            "k2": 9
          }
        ],
        "expected": 9
      },
      {
        "args": [
          {}
        ],
        "expected": 2
      },
      {
        "args": [
          {
            "x": 1
          }
        ],
        "expected": 2
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6505": {
    "functionNames": [
      "lambda_default_3"
    ],
    "tests": [
      {
        "args": [
          {
            "k3": 9
          }
        ],
        "expected": 9
      },
      {
        "args": [
          {}
        ],
        "expected": 3
      },
      {
        "args": [
          {
            "x": 1
          }
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6506": {
    "functionNames": [
      "lambda_default_4"
    ],
    "tests": [
      {
        "args": [
          {
            "k4": 9
          }
        ],
        "expected": 9
      },
      {
        "args": [
          {}
        ],
        "expected": 4
      },
      {
        "args": [
          {
            "x": 1
          }
        ],
        "expected": 4
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6507": {
    "functionNames": [
      "lambda_default_5"
    ],
    "tests": [
      {
        "args": [
          {
            "k5": 9
          }
        ],
        "expected": 9
      },
      {
        "args": [
          {}
        ],
        "expected": 5
      },
      {
        "args": [
          {
            "x": 1
          }
        ],
        "expected": 5
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6508": {
    "functionNames": [
      "lambda_max_1"
    ],
    "tests": [
      {
        "args": [
          1,
          5
        ],
        "expected": 6
      },
      {
        "args": [
          -1,
          -2
        ],
        "expected": 0
      },
      {
        "args": [
          3,
          3
        ],
        "expected": 4
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6509": {
    "functionNames": [
      "lambda_max_2"
    ],
    "tests": [
      {
        "args": [
          1,
          5
        ],
        "expected": 7
      },
      {
        "args": [
          -1,
          -2
        ],
        "expected": 1
      },
      {
        "args": [
          3,
          3
        ],
        "expected": 5
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6510": {
    "functionNames": [
      "lambda_max_3"
    ],
    "tests": [
      {
        "args": [
          1,
          5
        ],
        "expected": 8
      },
      {
        "args": [
          -1,
          -2
        ],
        "expected": 2
      },
      {
        "args": [
          3,
          3
        ],
        "expected": 6
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6511": {
    "functionNames": [
      "lambda_max_4"
    ],
    "tests": [
      {
        "args": [
          1,
          5
        ],
        "expected": 9
      },
      {
        "args": [
          -1,
          -2
        ],
        "expected": 3
      },
      {
        "args": [
          3,
          3
        ],
        "expected": 7
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6512": {
    "functionNames": [
      "lambda_max_5"
    ],
    "tests": [
      {
        "args": [
          1,
          5
        ],
        "expected": 10
      },
      {
        "args": [
          -1,
          -2
        ],
        "expected": 4
      },
      {
        "args": [
          3,
          3
        ],
        "expected": 8
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6513": {
    "functionNames": [
      "lambda_min_1"
    ],
    "tests": [
      {
        "args": [
          1,
          5
        ],
        "expected": 0
      },
      {
        "args": [
          -1,
          -2
        ],
        "expected": -3
      },
      {
        "args": [
          3,
          3
        ],
        "expected": 2
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6514": {
    "functionNames": [
      "lambda_min_2"
    ],
    "tests": [
      {
        "args": [
          1,
          5
        ],
        "expected": -1
      },
      {
        "args": [
          -1,
          -2
        ],
        "expected": -4
      },
      {
        "args": [
          3,
          3
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6515": {
    "functionNames": [
      "lambda_min_3"
    ],
    "tests": [
      {
        "args": [
          1,
          5
        ],
        "expected": -2
      },
      {
        "args": [
          -1,
          -2
        ],
        "expected": -5
      },
      {
        "args": [
          3,
          3
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6516": {
    "functionNames": [
      "lambda_min_4"
    ],
    "tests": [
      {
        "args": [
          1,
          5
        ],
        "expected": -3
      },
      {
        "args": [
          -1,
          -2
        ],
        "expected": -6
      },
      {
        "args": [
          3,
          3
        ],
        "expected": -1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6517": {
    "functionNames": [
      "lambda_min_5"
    ],
    "tests": [
      {
        "args": [
          1,
          5
        ],
        "expected": -4
      },
      {
        "args": [
          -1,
          -2
        ],
        "expected": -7
      },
      {
        "args": [
          3,
          3
        ],
        "expected": -2
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6518": {
    "functionNames": [
      "lambda_above_1"
    ],
    "tests": [
      {
        "args": [
          2
        ],
        "expected": true
      },
      {
        "args": [
          1
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
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6519": {
    "functionNames": [
      "lambda_above_2"
    ],
    "tests": [
      {
        "args": [
          3
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
          0
        ],
        "expected": false
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6520": {
    "functionNames": [
      "lambda_above_3"
    ],
    "tests": [
      {
        "args": [
          4
        ],
        "expected": true
      },
      {
        "args": [
          3
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
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6521": {
    "functionNames": [
      "lambda_above_4"
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
          4
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
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6522": {
    "functionNames": [
      "lambda_above_5"
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
          5
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
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6523": {
    "functionNames": [
      "lambda_sign_1"
    ],
    "tests": [
      {
        "args": [
          1
        ],
        "expected": "positive1"
      },
      {
        "args": [
          0
        ],
        "expected": "other1"
      },
      {
        "args": [
          -1
        ],
        "expected": "other1"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6524": {
    "functionNames": [
      "lambda_sign_2"
    ],
    "tests": [
      {
        "args": [
          1
        ],
        "expected": "positive2"
      },
      {
        "args": [
          0
        ],
        "expected": "other2"
      },
      {
        "args": [
          -1
        ],
        "expected": "other2"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6525": {
    "functionNames": [
      "lambda_sign_3"
    ],
    "tests": [
      {
        "args": [
          1
        ],
        "expected": "positive3"
      },
      {
        "args": [
          0
        ],
        "expected": "other3"
      },
      {
        "args": [
          -1
        ],
        "expected": "other3"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6526": {
    "functionNames": [
      "lambda_sign_4"
    ],
    "tests": [
      {
        "args": [
          1
        ],
        "expected": "positive4"
      },
      {
        "args": [
          0
        ],
        "expected": "other4"
      },
      {
        "args": [
          -1
        ],
        "expected": "other4"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6527": {
    "functionNames": [
      "lambda_sign_5"
    ],
    "tests": [
      {
        "args": [
          1
        ],
        "expected": "positive5"
      },
      {
        "args": [
          0
        ],
        "expected": "other5"
      },
      {
        "args": [
          -1
        ],
        "expected": "other5"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6528": {
    "functionNames": [
      "lambda_upper_1"
    ],
    "tests": [
      {
        "args": [
          "code"
        ],
        "expected": "CODE1"
      },
      {
        "args": [
          ""
        ],
        "expected": "1"
      },
      {
        "args": [
          "Py"
        ],
        "expected": "PY1"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6529": {
    "functionNames": [
      "lambda_upper_2"
    ],
    "tests": [
      {
        "args": [
          "code"
        ],
        "expected": "CODE2"
      },
      {
        "args": [
          ""
        ],
        "expected": "2"
      },
      {
        "args": [
          "Py"
        ],
        "expected": "PY2"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6530": {
    "functionNames": [
      "lambda_upper_3"
    ],
    "tests": [
      {
        "args": [
          "code"
        ],
        "expected": "CODE3"
      },
      {
        "args": [
          ""
        ],
        "expected": "3"
      },
      {
        "args": [
          "Py"
        ],
        "expected": "PY3"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6531": {
    "functionNames": [
      "lambda_upper_4"
    ],
    "tests": [
      {
        "args": [
          "code"
        ],
        "expected": "CODE4"
      },
      {
        "args": [
          ""
        ],
        "expected": "4"
      },
      {
        "args": [
          "Py"
        ],
        "expected": "PY4"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6532": {
    "functionNames": [
      "lambda_upper_5"
    ],
    "tests": [
      {
        "args": [
          "code"
        ],
        "expected": "CODE5"
      },
      {
        "args": [
          ""
        ],
        "expected": "5"
      },
      {
        "args": [
          "Py"
        ],
        "expected": "PY5"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6533": {
    "functionNames": [
      "lambda_last_1"
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
        "expected": 1
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": 9
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6534": {
    "functionNames": [
      "lambda_last_2"
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
        "expected": 2
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": 9
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6535": {
    "functionNames": [
      "lambda_last_3"
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
        "expected": 3
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": 9
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6536": {
    "functionNames": [
      "lambda_last_4"
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
        "expected": 4
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": 9
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6537": {
    "functionNames": [
      "lambda_last_5"
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
        "expected": 5
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": 9
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6538": {
    "functionNames": [
      "lambda_sum_1"
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
        "expected": 7
      },
      {
        "args": [
          []
        ],
        "expected": 1
      },
      {
        "args": [
          [
            -1
          ]
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6539": {
    "functionNames": [
      "lambda_sum_2"
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
        "expected": 8
      },
      {
        "args": [
          []
        ],
        "expected": 2
      },
      {
        "args": [
          [
            -1
          ]
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6540": {
    "functionNames": [
      "lambda_sum_3"
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
        "expected": 9
      },
      {
        "args": [
          []
        ],
        "expected": 3
      },
      {
        "args": [
          [
            -1
          ]
        ],
        "expected": 2
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6541": {
    "functionNames": [
      "lambda_sum_4"
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
        "expected": 10
      },
      {
        "args": [
          []
        ],
        "expected": 4
      },
      {
        "args": [
          [
            -1
          ]
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6542": {
    "functionNames": [
      "lambda_sum_5"
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
        "expected": 11
      },
      {
        "args": [
          []
        ],
        "expected": 5
      },
      {
        "args": [
          [
            -1
          ]
        ],
        "expected": 4
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6543": {
    "functionNames": [
      "lambda_reverse_1"
    ],
    "tests": [
      {
        "args": [
          "abc"
        ],
        "expected": "cba1"
      },
      {
        "args": [
          ""
        ],
        "expected": "1"
      },
      {
        "args": [
          "x"
        ],
        "expected": "x1"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6544": {
    "functionNames": [
      "lambda_reverse_2"
    ],
    "tests": [
      {
        "args": [
          "abc"
        ],
        "expected": "cba2"
      },
      {
        "args": [
          ""
        ],
        "expected": "2"
      },
      {
        "args": [
          "x"
        ],
        "expected": "x2"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6545": {
    "functionNames": [
      "lambda_reverse_3"
    ],
    "tests": [
      {
        "args": [
          "abc"
        ],
        "expected": "cba3"
      },
      {
        "args": [
          ""
        ],
        "expected": "3"
      },
      {
        "args": [
          "x"
        ],
        "expected": "x3"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6546": {
    "functionNames": [
      "lambda_reverse_4"
    ],
    "tests": [
      {
        "args": [
          "abc"
        ],
        "expected": "cba4"
      },
      {
        "args": [
          ""
        ],
        "expected": "4"
      },
      {
        "args": [
          "x"
        ],
        "expected": "x4"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6547": {
    "functionNames": [
      "lambda_reverse_5"
    ],
    "tests": [
      {
        "args": [
          "abc"
        ],
        "expected": "cba5"
      },
      {
        "args": [
          ""
        ],
        "expected": "5"
      },
      {
        "args": [
          "x"
        ],
        "expected": "x5"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6548": {
    "functionNames": [
      "lambda_clamp_1"
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
          1
        ],
        "expected": 1
      },
      {
        "args": [
          3
        ],
        "expected": 3
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6549": {
    "functionNames": [
      "lambda_clamp_2"
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
          2
        ],
        "expected": 2
      },
      {
        "args": [
          4
        ],
        "expected": 4
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6550": {
    "functionNames": [
      "lambda_clamp_3"
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
          3
        ],
        "expected": 3
      },
      {
        "args": [
          5
        ],
        "expected": 5
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6551": {
    "functionNames": [
      "lambda_clamp_4"
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
          4
        ],
        "expected": 4
      },
      {
        "args": [
          6
        ],
        "expected": 6
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6552": {
    "functionNames": [
      "lambda_clamp_5"
    ],
    "tests": [
      {
        "args": [
          0
        ],
        "expected": 5
      },
      {
        "args": [
          5
        ],
        "expected": 5
      },
      {
        "args": [
          7
        ],
        "expected": 7
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6553": {
    "functionNames": [
      "lambda_repeat_1"
    ],
    "tests": [
      {
        "args": [
          "ab"
        ],
        "expected": "ab"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      },
      {
        "args": [
          "x"
        ],
        "expected": "x"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6554": {
    "functionNames": [
      "lambda_repeat_2"
    ],
    "tests": [
      {
        "args": [
          "ab"
        ],
        "expected": "abab"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      },
      {
        "args": [
          "x"
        ],
        "expected": "xx"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6555": {
    "functionNames": [
      "lambda_repeat_3"
    ],
    "tests": [
      {
        "args": [
          "ab"
        ],
        "expected": "ababab"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      },
      {
        "args": [
          "x"
        ],
        "expected": "xxx"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6556": {
    "functionNames": [
      "lambda_repeat_4"
    ],
    "tests": [
      {
        "args": [
          "ab"
        ],
        "expected": "abababab"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      },
      {
        "args": [
          "x"
        ],
        "expected": "xxxx"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6557": {
    "functionNames": [
      "lambda_repeat_5"
    ],
    "tests": [
      {
        "args": [
          "ab"
        ],
        "expected": "ababababab"
      },
      {
        "args": [
          ""
        ],
        "expected": ""
      },
      {
        "args": [
          "x"
        ],
        "expected": "xxxxx"
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6558": {
    "functionNames": [
      "lambda_sort_length_1"
    ],
    "tests": [
      {
        "args": [
          [
            "bbb",
            "a",
            "cc"
          ]
        ],
        "expected": [
          "a",
          "cc",
          "bbb",
          "1"
        ]
      },
      {
        "args": [
          []
        ],
        "expected": [
          "1"
        ]
      },
      {
        "args": [
          [
            "x"
          ]
        ],
        "expected": [
          "x",
          "1"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6559": {
    "functionNames": [
      "lambda_sort_length_2"
    ],
    "tests": [
      {
        "args": [
          [
            "bbb",
            "a",
            "cc"
          ]
        ],
        "expected": [
          "a",
          "cc",
          "bbb",
          "2"
        ]
      },
      {
        "args": [
          []
        ],
        "expected": [
          "2"
        ]
      },
      {
        "args": [
          [
            "x"
          ]
        ],
        "expected": [
          "x",
          "2"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6560": {
    "functionNames": [
      "lambda_sort_length_3"
    ],
    "tests": [
      {
        "args": [
          [
            "bbb",
            "a",
            "cc"
          ]
        ],
        "expected": [
          "a",
          "cc",
          "bbb",
          "3"
        ]
      },
      {
        "args": [
          []
        ],
        "expected": [
          "3"
        ]
      },
      {
        "args": [
          [
            "x"
          ]
        ],
        "expected": [
          "x",
          "3"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6561": {
    "functionNames": [
      "lambda_sort_length_4"
    ],
    "tests": [
      {
        "args": [
          [
            "bbb",
            "a",
            "cc"
          ]
        ],
        "expected": [
          "a",
          "cc",
          "bbb",
          "4"
        ]
      },
      {
        "args": [
          []
        ],
        "expected": [
          "4"
        ]
      },
      {
        "args": [
          [
            "x"
          ]
        ],
        "expected": [
          "x",
          "4"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6562": {
    "functionNames": [
      "lambda_sort_length_5"
    ],
    "tests": [
      {
        "args": [
          [
            "bbb",
            "a",
            "cc"
          ]
        ],
        "expected": [
          "a",
          "cc",
          "bbb",
          "5"
        ]
      },
      {
        "args": [
          []
        ],
        "expected": [
          "5"
        ]
      },
      {
        "args": [
          [
            "x"
          ]
        ],
        "expected": [
          "x",
          "5"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6563": {
    "functionNames": [
      "lambda_map_offset_1"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ]
        ],
        "expected": [
          2,
          5
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            -2
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6564": {
    "functionNames": [
      "lambda_map_offset_2"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ]
        ],
        "expected": [
          3,
          6
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            -2
          ]
        ],
        "expected": [
          6
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6565": {
    "functionNames": [
      "lambda_map_offset_3"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ]
        ],
        "expected": [
          4,
          7
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            -2
          ]
        ],
        "expected": [
          7
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6566": {
    "functionNames": [
      "lambda_map_offset_4"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ]
        ],
        "expected": [
          5,
          8
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            -2
          ]
        ],
        "expected": [
          8
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6567": {
    "functionNames": [
      "lambda_map_offset_5"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ]
        ],
        "expected": [
          6,
          9
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            -2
          ]
        ],
        "expected": [
          9
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6568": {
    "functionNames": [
      "lambda_filter_1"
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
        "expected": [
          2
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": [
          9
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6569": {
    "functionNames": [
      "lambda_filter_2"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            2,
            3
          ]
        ],
        "expected": [
          3
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": [
          9
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6570": {
    "functionNames": [
      "lambda_filter_3"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            3,
            4
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
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": [
          9
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6571": {
    "functionNames": [
      "lambda_filter_4"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            4,
            5
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
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": [
          9
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6572": {
    "functionNames": [
      "lambda_filter_5"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            5,
            6
          ]
        ],
        "expected": [
          6
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": [
          9
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6573": {
    "functionNames": [
      "lambda_sort_dict_1"
    ],
    "tests": [
      {
        "args": [
          [
            {
              "name": "B",
              "score": 1
            },
            {
              "name": "A",
              "score": 2
            }
          ]
        ],
        "expected": [
          {
            "name": "A",
            "score": 2
          },
          {
            "name": "B",
            "score": 1
          },
          {
            "marker": 1
          }
        ]
      },
      {
        "args": [
          []
        ],
        "expected": [
          {
            "marker": 1
          }
        ]
      },
      {
        "args": [
          [
            {
              "name": "X",
              "score": 0
            }
          ]
        ],
        "expected": [
          {
            "name": "X",
            "score": 0
          },
          {
            "marker": 1
          }
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6574": {
    "functionNames": [
      "lambda_sort_dict_2"
    ],
    "tests": [
      {
        "args": [
          [
            {
              "name": "B",
              "score": 1
            },
            {
              "name": "A",
              "score": 2
            }
          ]
        ],
        "expected": [
          {
            "name": "A",
            "score": 2
          },
          {
            "name": "B",
            "score": 1
          },
          {
            "marker": 2
          }
        ]
      },
      {
        "args": [
          []
        ],
        "expected": [
          {
            "marker": 2
          }
        ]
      },
      {
        "args": [
          [
            {
              "name": "X",
              "score": 0
            }
          ]
        ],
        "expected": [
          {
            "name": "X",
            "score": 0
          },
          {
            "marker": 2
          }
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6575": {
    "functionNames": [
      "lambda_sort_dict_3"
    ],
    "tests": [
      {
        "args": [
          [
            {
              "name": "B",
              "score": 1
            },
            {
              "name": "A",
              "score": 2
            }
          ]
        ],
        "expected": [
          {
            "name": "A",
            "score": 2
          },
          {
            "name": "B",
            "score": 1
          },
          {
            "marker": 3
          }
        ]
      },
      {
        "args": [
          []
        ],
        "expected": [
          {
            "marker": 3
          }
        ]
      },
      {
        "args": [
          [
            {
              "name": "X",
              "score": 0
            }
          ]
        ],
        "expected": [
          {
            "name": "X",
            "score": 0
          },
          {
            "marker": 3
          }
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6576": {
    "functionNames": [
      "lambda_sort_dict_4"
    ],
    "tests": [
      {
        "args": [
          [
            {
              "name": "B",
              "score": 1
            },
            {
              "name": "A",
              "score": 2
            }
          ]
        ],
        "expected": [
          {
            "name": "A",
            "score": 2
          },
          {
            "name": "B",
            "score": 1
          },
          {
            "marker": 4
          }
        ]
      },
      {
        "args": [
          []
        ],
        "expected": [
          {
            "marker": 4
          }
        ]
      },
      {
        "args": [
          [
            {
              "name": "X",
              "score": 0
            }
          ]
        ],
        "expected": [
          {
            "name": "X",
            "score": 0
          },
          {
            "marker": 4
          }
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6577": {
    "functionNames": [
      "lambda_sort_dict_5"
    ],
    "tests": [
      {
        "args": [
          [
            {
              "name": "B",
              "score": 1
            },
            {
              "name": "A",
              "score": 2
            }
          ]
        ],
        "expected": [
          {
            "name": "A",
            "score": 2
          },
          {
            "name": "B",
            "score": 1
          },
          {
            "marker": 5
          }
        ]
      },
      {
        "args": [
          []
        ],
        "expected": [
          {
            "marker": 5
          }
        ]
      },
      {
        "args": [
          [
            {
              "name": "X",
              "score": 0
            }
          ]
        ],
        "expected": [
          {
            "name": "X",
            "score": 0
          },
          {
            "marker": 5
          }
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6578": {
    "functionNames": [
      "lambda_pairs_1"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            3,
            9
          ]
        ],
        "expected": [
          0,
          3,
          9
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
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
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6579": {
    "functionNames": [
      "lambda_pairs_2"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            3,
            9
          ]
        ],
        "expected": [
          3,
          0,
          9
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            2
          ]
        ],
        "expected": [
          2
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6580": {
    "functionNames": [
      "lambda_pairs_3"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            3,
            9
          ]
        ],
        "expected": [
          3,
          0,
          9
        ]
      },
      {
        "args": [
          []
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
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6581": {
    "functionNames": [
      "lambda_pairs_4"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            3,
            9
          ]
        ],
        "expected": [
          3,
          0,
          9
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            4
          ]
        ],
        "expected": [
          4
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6582": {
    "functionNames": [
      "lambda_pairs_5"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            3,
            9
          ]
        ],
        "expected": [
          3,
          9,
          0
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
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
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6583": {
    "functionNames": [
      "lambda_dict_values_1"
    ],
    "tests": [
      {
        "args": [
          {
            "b": 1,
            "a": 2
          }
        ],
        "expected": [
          "b",
          "a"
        ]
      },
      {
        "args": [
          {}
        ],
        "expected": []
      },
      {
        "args": [
          {
            "x": 0
          }
        ],
        "expected": [
          "x"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6584": {
    "functionNames": [
      "lambda_dict_values_2"
    ],
    "tests": [
      {
        "args": [
          {
            "b": 1,
            "a": 2
          }
        ],
        "expected": [
          "b",
          "a"
        ]
      },
      {
        "args": [
          {}
        ],
        "expected": []
      },
      {
        "args": [
          {
            "x": 0
          }
        ],
        "expected": [
          "x"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6585": {
    "functionNames": [
      "lambda_dict_values_3"
    ],
    "tests": [
      {
        "args": [
          {
            "b": 1,
            "a": 2
          }
        ],
        "expected": [
          "b",
          "a"
        ]
      },
      {
        "args": [
          {}
        ],
        "expected": []
      },
      {
        "args": [
          {
            "x": 0
          }
        ],
        "expected": [
          "x"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6586": {
    "functionNames": [
      "lambda_dict_values_4"
    ],
    "tests": [
      {
        "args": [
          {
            "b": 1,
            "a": 2
          }
        ],
        "expected": [
          "b",
          "a"
        ]
      },
      {
        "args": [
          {}
        ],
        "expected": []
      },
      {
        "args": [
          {
            "x": 0
          }
        ],
        "expected": [
          "x"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6587": {
    "functionNames": [
      "lambda_dict_values_5"
    ],
    "tests": [
      {
        "args": [
          {
            "b": 1,
            "a": 2
          }
        ],
        "expected": [
          "b",
          "a"
        ]
      },
      {
        "args": [
          {}
        ],
        "expected": []
      },
      {
        "args": [
          {
            "x": 0
          }
        ],
        "expected": [
          "x"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6588": {
    "functionNames": [
      "lambda_nested_1"
    ],
    "tests": [
      {
        "args": [
          [
            [
              3
            ],
            [
              1,
              1
            ],
            [
              0
            ]
          ]
        ],
        "expected": [
          [
            0
          ],
          [
            1,
            1
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
      },
      {
        "args": [
          [
            []
          ]
        ],
        "expected": [
          []
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6589": {
    "functionNames": [
      "lambda_nested_2"
    ],
    "tests": [
      {
        "args": [
          [
            [
              3
            ],
            [
              1,
              1
            ],
            [
              0
            ]
          ]
        ],
        "expected": [
          [
            0
          ],
          [
            1,
            1
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
      },
      {
        "args": [
          [
            []
          ]
        ],
        "expected": [
          []
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6590": {
    "functionNames": [
      "lambda_nested_3"
    ],
    "tests": [
      {
        "args": [
          [
            [
              3
            ],
            [
              1,
              1
            ],
            [
              0
            ]
          ]
        ],
        "expected": [
          [
            0
          ],
          [
            1,
            1
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
      },
      {
        "args": [
          [
            []
          ]
        ],
        "expected": [
          []
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6591": {
    "functionNames": [
      "lambda_nested_4"
    ],
    "tests": [
      {
        "args": [
          [
            [
              3
            ],
            [
              1,
              1
            ],
            [
              0
            ]
          ]
        ],
        "expected": [
          [
            0
          ],
          [
            1,
            1
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
      },
      {
        "args": [
          [
            []
          ]
        ],
        "expected": [
          []
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6592": {
    "functionNames": [
      "lambda_nested_5"
    ],
    "tests": [
      {
        "args": [
          [
            [
              3
            ],
            [
              1,
              1
            ],
            [
              0
            ]
          ]
        ],
        "expected": [
          [
            0
          ],
          [
            1,
            1
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
      },
      {
        "args": [
          [
            []
          ]
        ],
        "expected": [
          []
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6593": {
    "functionNames": [
      "lambda_transform_words_1"
    ],
    "tests": [
      {
        "args": [
          [
            "A",
            "Py"
          ]
        ],
        "expected": [
          "a1",
          "py1"
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            "X"
          ]
        ],
        "expected": [
          "x1"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6594": {
    "functionNames": [
      "lambda_transform_words_2"
    ],
    "tests": [
      {
        "args": [
          [
            "A",
            "Py"
          ]
        ],
        "expected": [
          "a2",
          "py2"
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            "X"
          ]
        ],
        "expected": [
          "x2"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6595": {
    "functionNames": [
      "lambda_transform_words_3"
    ],
    "tests": [
      {
        "args": [
          [
            "A",
            "Py"
          ]
        ],
        "expected": [
          "a3",
          "py3"
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            "X"
          ]
        ],
        "expected": [
          "x3"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6596": {
    "functionNames": [
      "lambda_transform_words_4"
    ],
    "tests": [
      {
        "args": [
          [
            "A",
            "Py"
          ]
        ],
        "expected": [
          "a4",
          "py4"
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            "X"
          ]
        ],
        "expected": [
          "x4"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6597": {
    "functionNames": [
      "lambda_transform_words_5"
    ],
    "tests": [
      {
        "args": [
          [
            "A",
            "Py"
          ]
        ],
        "expected": [
          "a5",
          "py5"
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            "X"
          ]
        ],
        "expected": [
          "x5"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6598": {
    "functionNames": [
      "lambda_filter_length_1"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "code",
            "python"
          ]
        ],
        "expected": [
          "a",
          "code",
          "python"
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            "x"
          ]
        ],
        "expected": [
          "x"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6599": {
    "functionNames": [
      "lambda_filter_length_2"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "code",
            "python"
          ]
        ],
        "expected": [
          "code",
          "python"
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            "xx"
          ]
        ],
        "expected": [
          "xx"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6600": {
    "functionNames": [
      "lambda_filter_length_3"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "code",
            "python"
          ]
        ],
        "expected": [
          "code",
          "python"
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            "xxx"
          ]
        ],
        "expected": [
          "xxx"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6601": {
    "functionNames": [
      "lambda_filter_length_4"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "code",
            "python"
          ]
        ],
        "expected": [
          "code",
          "python"
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            "xxxx"
          ]
        ],
        "expected": [
          "xxxx"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6602": {
    "functionNames": [
      "lambda_filter_length_5"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "code",
            "python"
          ]
        ],
        "expected": [
          "python"
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            "xxxxx"
          ]
        ],
        "expected": [
          "xxxxx"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6603": {
    "functionNames": [
      "lambda_sort_last_1"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "bee",
            ""
          ]
        ],
        "expected": [
          "",
          "bee",
          "cat"
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            "a",
            "b"
          ]
        ],
        "expected": [
          "a",
          "b"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6604": {
    "functionNames": [
      "lambda_sort_last_2"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "bee",
            ""
          ]
        ],
        "expected": [
          "",
          "bee",
          "cat"
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            "a",
            "b"
          ]
        ],
        "expected": [
          "a",
          "b"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6605": {
    "functionNames": [
      "lambda_sort_last_3"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "bee",
            ""
          ]
        ],
        "expected": [
          "",
          "bee",
          "cat"
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            "a",
            "b"
          ]
        ],
        "expected": [
          "a",
          "b"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6606": {
    "functionNames": [
      "lambda_sort_last_4"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "bee",
            ""
          ]
        ],
        "expected": [
          "",
          "bee",
          "cat"
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            "a",
            "b"
          ]
        ],
        "expected": [
          "a",
          "b"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  },
  "6607": {
    "functionNames": [
      "lambda_sort_last_5"
    ],
    "tests": [
      {
        "args": [
          [
            "cat",
            "bee",
            ""
          ]
        ],
        "expected": [
          "",
          "bee",
          "cat"
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            "a",
            "b"
          ]
        ],
        "expected": [
          "a",
          "b"
        ]
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "Lambda",
        "minCount": 1
      }
    ]
  }
};
