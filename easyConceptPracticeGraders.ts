import type { AutoGrader } from './graders';

export const EASY_CONCEPT_PRACTICE_GRADERS: Record<number, AutoGrader> = {
  "5708": {
    "functionNames": [
      "count_step_1_while"
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
          0
        ],
        "expected": 0
      },
      {
        "args": [
          17
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
  "5709": {
    "functionNames": [
      "count_step_2_while"
    ],
    "tests": [
      {
        "args": [
          10
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
          17
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
  "5710": {
    "functionNames": [
      "count_step_3_while"
    ],
    "tests": [
      {
        "args": [
          10
        ],
        "expected": 2
      },
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          17
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
  "5711": {
    "functionNames": [
      "count_step_4_while"
    ],
    "tests": [
      {
        "args": [
          10
        ],
        "expected": 2
      },
      {
        "args": [
          0
        ],
        "expected": 0
      },
      {
        "args": [
          17
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
  "5712": {
    "functionNames": [
      "count_step_5_while"
    ],
    "tests": [
      {
        "args": [
          10
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
          17
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
  "5713": {
    "functionNames": [
      "sum_step_1_while"
    ],
    "tests": [
      {
        "args": [
          12
        ],
        "expected": 42
      },
      {
        "args": [
          1
        ],
        "expected": 0
      },
      {
        "args": [
          25
        ],
        "expected": 156
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "5714": {
    "functionNames": [
      "sum_step_2_while"
    ],
    "tests": [
      {
        "args": [
          12
        ],
        "expected": 30
      },
      {
        "args": [
          1
        ],
        "expected": 0
      },
      {
        "args": [
          25
        ],
        "expected": 108
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "5715": {
    "functionNames": [
      "sum_step_3_while"
    ],
    "tests": [
      {
        "args": [
          12
        ],
        "expected": 24
      },
      {
        "args": [
          1
        ],
        "expected": 0
      },
      {
        "args": [
          25
        ],
        "expected": 84
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "5716": {
    "functionNames": [
      "sum_step_4_while"
    ],
    "tests": [
      {
        "args": [
          12
        ],
        "expected": 15
      },
      {
        "args": [
          1
        ],
        "expected": 0
      },
      {
        "args": [
          25
        ],
        "expected": 75
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "5717": {
    "functionNames": [
      "sum_step_5_while"
    ],
    "tests": [
      {
        "args": [
          12
        ],
        "expected": 18
      },
      {
        "args": [
          1
        ],
        "expected": 0
      },
      {
        "args": [
          25
        ],
        "expected": 60
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "5718": {
    "functionNames": [
      "build_sequence_1_while"
    ],
    "tests": [
      {
        "args": [
          2,
          4
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
          -3,
          3
        ],
        "expected": [
          -3,
          -2,
          -1
        ]
      },
      {
        "args": [
          8,
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
  "5719": {
    "functionNames": [
      "build_sequence_2_while"
    ],
    "tests": [
      {
        "args": [
          2,
          4
        ],
        "expected": [
          2,
          4,
          6,
          8
        ]
      },
      {
        "args": [
          -3,
          3
        ],
        "expected": [
          -3,
          -1,
          1
        ]
      },
      {
        "args": [
          8,
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
  "5720": {
    "functionNames": [
      "build_sequence_3_while"
    ],
    "tests": [
      {
        "args": [
          2,
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
          -3,
          3
        ],
        "expected": [
          -3,
          0,
          3
        ]
      },
      {
        "args": [
          8,
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
  "5721": {
    "functionNames": [
      "build_sequence_4_while"
    ],
    "tests": [
      {
        "args": [
          2,
          4
        ],
        "expected": [
          2,
          6,
          10,
          14
        ]
      },
      {
        "args": [
          -3,
          3
        ],
        "expected": [
          -3,
          1,
          5
        ]
      },
      {
        "args": [
          8,
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
  "5722": {
    "functionNames": [
      "build_sequence_5_while"
    ],
    "tests": [
      {
        "args": [
          2,
          4
        ],
        "expected": [
          2,
          7,
          12,
          17
        ]
      },
      {
        "args": [
          -3,
          3
        ],
        "expected": [
          -3,
          2,
          7
        ]
      },
      {
        "args": [
          8,
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
  "5723": {
    "functionNames": [
      "repeat_text_1_while"
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
  "5724": {
    "functionNames": [
      "repeat_text_2_while"
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
          "x"
        ],
        "expected": "xx"
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
  "5725": {
    "functionNames": [
      "repeat_text_3_while"
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
          "x"
        ],
        "expected": "xxx"
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
  "5726": {
    "functionNames": [
      "repeat_text_4_while"
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
          "x"
        ],
        "expected": "xxxx"
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
  "5727": {
    "functionNames": [
      "repeat_text_5_while"
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
          "x"
        ],
        "expected": "xxxxx"
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
  "5728": {
    "functionNames": [
      "count_above_1_while"
    ],
    "tests": [
      {
        "args": [
          [
            0,
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
  "5729": {
    "functionNames": [
      "count_above_2_while"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            2,
            5,
            9
          ]
        ],
        "expected": 2
      },
      {
        "args": [
          [
            2,
            3
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
  "5730": {
    "functionNames": [
      "count_above_3_while"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            2,
            5,
            9
          ]
        ],
        "expected": 2
      },
      {
        "args": [
          [
            3,
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
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "5731": {
    "functionNames": [
      "count_above_4_while"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            2,
            5,
            9
          ]
        ],
        "expected": 2
      },
      {
        "args": [
          [
            4,
            5
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
  "5732": {
    "functionNames": [
      "count_above_5_while"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            2,
            5,
            9
          ]
        ],
        "expected": 1
      },
      {
        "args": [
          [
            5,
            6
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
  "5733": {
    "functionNames": [
      "first_below_1_while"
    ],
    "tests": [
      {
        "args": [
          [
            9,
            0,
            8
          ]
        ],
        "expected": 1
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
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "5734": {
    "functionNames": [
      "first_below_2_while"
    ],
    "tests": [
      {
        "args": [
          [
            9,
            1,
            8
          ]
        ],
        "expected": 1
      },
      {
        "args": [
          [
            2,
            3
          ]
        ],
        "expected": -1
      },
      {
        "args": [
          [
            0
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
  "5735": {
    "functionNames": [
      "first_below_3_while"
    ],
    "tests": [
      {
        "args": [
          [
            9,
            2,
            8
          ]
        ],
        "expected": 1
      },
      {
        "args": [
          [
            3,
            4
          ]
        ],
        "expected": -1
      },
      {
        "args": [
          [
            1
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
  "5736": {
    "functionNames": [
      "first_below_4_while"
    ],
    "tests": [
      {
        "args": [
          [
            9,
            3,
            8
          ]
        ],
        "expected": 1
      },
      {
        "args": [
          [
            4,
            5
          ]
        ],
        "expected": -1
      },
      {
        "args": [
          [
            2
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
  "5737": {
    "functionNames": [
      "first_below_5_while"
    ],
    "tests": [
      {
        "args": [
          [
            9,
            4,
            8
          ]
        ],
        "expected": 1
      },
      {
        "args": [
          [
            5,
            6
          ]
        ],
        "expected": -1
      },
      {
        "args": [
          [
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
  "5738": {
    "functionNames": [
      "reach_target_1_while"
    ],
    "tests": [
      {
        "args": [
          0,
          11
        ],
        "expected": 11
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
          -2,
          7
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
  "5739": {
    "functionNames": [
      "reach_target_2_while"
    ],
    "tests": [
      {
        "args": [
          0,
          11
        ],
        "expected": 12
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
          -2,
          7
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
  "5740": {
    "functionNames": [
      "reach_target_3_while"
    ],
    "tests": [
      {
        "args": [
          0,
          11
        ],
        "expected": 12
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
          -2,
          7
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
  "5741": {
    "functionNames": [
      "reach_target_4_while"
    ],
    "tests": [
      {
        "args": [
          0,
          11
        ],
        "expected": 12
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
          -2,
          7
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
  "5742": {
    "functionNames": [
      "reach_target_5_while"
    ],
    "tests": [
      {
        "args": [
          0,
          11
        ],
        "expected": 15
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
          -2,
          7
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
  "5743": {
    "functionNames": [
      "take_prefix_1_while"
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
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "5744": {
    "functionNames": [
      "take_prefix_2_while"
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
          2
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
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "5745": {
    "functionNames": [
      "take_prefix_3_while"
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
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "5746": {
    "functionNames": [
      "take_prefix_4_while"
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
          4
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
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "5747": {
    "functionNames": [
      "take_prefix_5_while"
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
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "5748": {
    "functionNames": [
      "replace_negative_1_while"
    ],
    "tests": [
      {
        "args": [
          [
            -2,
            0,
            4,
            -1
          ]
        ],
        "expected": [
          1,
          0,
          4,
          1
        ]
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
  "5749": {
    "functionNames": [
      "replace_negative_2_while"
    ],
    "tests": [
      {
        "args": [
          [
            -2,
            0,
            4,
            -1
          ]
        ],
        "expected": [
          2,
          0,
          4,
          2
        ]
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
  "5750": {
    "functionNames": [
      "replace_negative_3_while"
    ],
    "tests": [
      {
        "args": [
          [
            -2,
            0,
            4,
            -1
          ]
        ],
        "expected": [
          3,
          0,
          4,
          3
        ]
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
  "5751": {
    "functionNames": [
      "replace_negative_4_while"
    ],
    "tests": [
      {
        "args": [
          [
            -2,
            0,
            4,
            -1
          ]
        ],
        "expected": [
          4,
          0,
          4,
          4
        ]
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
  "5752": {
    "functionNames": [
      "replace_negative_5_while"
    ],
    "tests": [
      {
        "args": [
          [
            -2,
            0,
            4,
            -1
          ]
        ],
        "expected": [
          5,
          0,
          4,
          5
        ]
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
  "5753": {
    "functionNames": [
      "running_total_1_while"
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
          7
        ]
      },
      {
        "args": [
          [
            -1,
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
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "While",
        "minCount": 1
      }
    ]
  },
  "5754": {
    "functionNames": [
      "running_total_2_while"
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
          5,
          8
        ]
      },
      {
        "args": [
          [
            -1,
            4
          ]
        ],
        "expected": [
          1,
          5
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
  "5755": {
    "functionNames": [
      "running_total_3_while"
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
          6,
          9
        ]
      },
      {
        "args": [
          [
            -1,
            4
          ]
        ],
        "expected": [
          2,
          6
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
  "5756": {
    "functionNames": [
      "running_total_4_while"
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
          7,
          10
        ]
      },
      {
        "args": [
          [
            -1,
            4
          ]
        ],
        "expected": [
          3,
          7
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
  "5757": {
    "functionNames": [
      "running_total_5_while"
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
          8,
          11
        ]
      },
      {
        "args": [
          [
            -1,
            4
          ]
        ],
        "expected": [
          4,
          8
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
  "5758": {
    "functionNames": [
      "inside_1_boolean"
    ],
    "tests": [
      {
        "args": [
          -8
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
          7
        ],
        "expected": false
      }
    ],
    "requiredBoolOps": [
      "And"
    ]
  },
  "5759": {
    "functionNames": [
      "inside_2_boolean"
    ],
    "tests": [
      {
        "args": [
          -8
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
          8
        ],
        "expected": false
      }
    ],
    "requiredBoolOps": [
      "And"
    ]
  },
  "5760": {
    "functionNames": [
      "inside_3_boolean"
    ],
    "tests": [
      {
        "args": [
          -8
        ],
        "expected": false
      },
      {
        "args": [
          3
        ],
        "expected": true
      },
      {
        "args": [
          9
        ],
        "expected": false
      }
    ],
    "requiredBoolOps": [
      "And"
    ]
  },
  "5761": {
    "functionNames": [
      "inside_4_boolean"
    ],
    "tests": [
      {
        "args": [
          -8
        ],
        "expected": false
      },
      {
        "args": [
          4
        ],
        "expected": true
      },
      {
        "args": [
          10
        ],
        "expected": false
      }
    ],
    "requiredBoolOps": [
      "And"
    ]
  },
  "5762": {
    "functionNames": [
      "inside_5_boolean"
    ],
    "tests": [
      {
        "args": [
          -8
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
          11
        ],
        "expected": false
      }
    ],
    "requiredBoolOps": [
      "And"
    ]
  },
  "5763": {
    "functionNames": [
      "outside_1_boolean"
    ],
    "tests": [
      {
        "args": [
          -8
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
          7
        ],
        "expected": true
      }
    ],
    "requiredBoolOps": [
      "Or"
    ]
  },
  "5764": {
    "functionNames": [
      "outside_2_boolean"
    ],
    "tests": [
      {
        "args": [
          -8
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
          8
        ],
        "expected": true
      }
    ],
    "requiredBoolOps": [
      "Or"
    ]
  },
  "5765": {
    "functionNames": [
      "outside_3_boolean"
    ],
    "tests": [
      {
        "args": [
          -8
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
          9
        ],
        "expected": true
      }
    ],
    "requiredBoolOps": [
      "Or"
    ]
  },
  "5766": {
    "functionNames": [
      "outside_4_boolean"
    ],
    "tests": [
      {
        "args": [
          -8
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
          10
        ],
        "expected": true
      }
    ],
    "requiredBoolOps": [
      "Or"
    ]
  },
  "5767": {
    "functionNames": [
      "outside_5_boolean"
    ],
    "tests": [
      {
        "args": [
          -8
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
          11
        ],
        "expected": true
      }
    ],
    "requiredBoolOps": [
      "Or"
    ]
  },
  "5768": {
    "functionNames": [
      "positive_even_after_1"
    ],
    "tests": [
      {
        "args": [
          1
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
          5
        ],
        "expected": false
      }
    ],
    "requiredBoolOps": [
      "And"
    ]
  },
  "5769": {
    "functionNames": [
      "positive_even_after_2"
    ],
    "tests": [
      {
        "args": [
          2
        ],
        "expected": false
      },
      {
        "args": [
          3
        ],
        "expected": false
      },
      {
        "args": [
          6
        ],
        "expected": true
      }
    ],
    "requiredBoolOps": [
      "And"
    ]
  },
  "5770": {
    "functionNames": [
      "positive_even_after_3"
    ],
    "tests": [
      {
        "args": [
          3
        ],
        "expected": false
      },
      {
        "args": [
          4
        ],
        "expected": true
      },
      {
        "args": [
          7
        ],
        "expected": false
      }
    ],
    "requiredBoolOps": [
      "And"
    ]
  },
  "5771": {
    "functionNames": [
      "positive_even_after_4"
    ],
    "tests": [
      {
        "args": [
          4
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
          8
        ],
        "expected": true
      }
    ],
    "requiredBoolOps": [
      "And"
    ]
  },
  "5772": {
    "functionNames": [
      "positive_even_after_5"
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
          6
        ],
        "expected": true
      },
      {
        "args": [
          9
        ],
        "expected": false
      }
    ],
    "requiredBoolOps": [
      "And"
    ]
  },
  "5773": {
    "functionNames": [
      "divisible_choice_1"
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
        "expected": true
      },
      {
        "args": [
          7
        ],
        "expected": false
      }
    ],
    "requiredBoolOps": [
      "Or"
    ]
  },
  "5774": {
    "functionNames": [
      "divisible_choice_2"
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
        "expected": true
      },
      {
        "args": [
          13
        ],
        "expected": false
      }
    ],
    "requiredBoolOps": [
      "Or"
    ]
  },
  "5775": {
    "functionNames": [
      "divisible_choice_3"
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
        "expected": true
      },
      {
        "args": [
          21
        ],
        "expected": false
      }
    ],
    "requiredBoolOps": [
      "Or"
    ]
  },
  "5776": {
    "functionNames": [
      "divisible_choice_4"
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
        "expected": true
      },
      {
        "args": [
          31
        ],
        "expected": false
      }
    ],
    "requiredBoolOps": [
      "Or"
    ]
  },
  "5777": {
    "functionNames": [
      "divisible_choice_5"
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
        "expected": true
      },
      {
        "args": [
          43
        ],
        "expected": false
      }
    ],
    "requiredBoolOps": [
      "Or"
    ]
  },
  "5778": {
    "functionNames": [
      "not_outside_1"
    ],
    "tests": [
      {
        "args": [
          -8
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
          7
        ],
        "expected": false
      }
    ],
    "requiredBoolOps": [
      "Or"
    ]
  },
  "5779": {
    "functionNames": [
      "not_outside_2"
    ],
    "tests": [
      {
        "args": [
          -8
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
          8
        ],
        "expected": false
      }
    ],
    "requiredBoolOps": [
      "Or"
    ]
  },
  "5780": {
    "functionNames": [
      "not_outside_3"
    ],
    "tests": [
      {
        "args": [
          -8
        ],
        "expected": false
      },
      {
        "args": [
          3
        ],
        "expected": true
      },
      {
        "args": [
          9
        ],
        "expected": false
      }
    ],
    "requiredBoolOps": [
      "Or"
    ]
  },
  "5781": {
    "functionNames": [
      "not_outside_4"
    ],
    "tests": [
      {
        "args": [
          -8
        ],
        "expected": false
      },
      {
        "args": [
          4
        ],
        "expected": true
      },
      {
        "args": [
          10
        ],
        "expected": false
      }
    ],
    "requiredBoolOps": [
      "Or"
    ]
  },
  "5782": {
    "functionNames": [
      "not_outside_5"
    ],
    "tests": [
      {
        "args": [
          -8
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
          11
        ],
        "expected": false
      }
    ],
    "requiredBoolOps": [
      "Or"
    ]
  },
  "5783": {
    "functionNames": [
      "text_starts_1_boolean"
    ],
    "tests": [
      {
        "args": [
          "1abc"
        ],
        "expected": true
      },
      {
        "args": [
          ""
        ],
        "expected": false
      },
      {
        "args": [
          "x1"
        ],
        "expected": false
      }
    ],
    "requiredBoolOps": [
      "And"
    ]
  },
  "5784": {
    "functionNames": [
      "text_starts_2_boolean"
    ],
    "tests": [
      {
        "args": [
          "2abc"
        ],
        "expected": true
      },
      {
        "args": [
          ""
        ],
        "expected": false
      },
      {
        "args": [
          "x2"
        ],
        "expected": false
      }
    ],
    "requiredBoolOps": [
      "And"
    ]
  },
  "5785": {
    "functionNames": [
      "text_starts_3_boolean"
    ],
    "tests": [
      {
        "args": [
          "3abc"
        ],
        "expected": true
      },
      {
        "args": [
          ""
        ],
        "expected": false
      },
      {
        "args": [
          "x3"
        ],
        "expected": false
      }
    ],
    "requiredBoolOps": [
      "And"
    ]
  },
  "5786": {
    "functionNames": [
      "text_starts_4_boolean"
    ],
    "tests": [
      {
        "args": [
          "4abc"
        ],
        "expected": true
      },
      {
        "args": [
          ""
        ],
        "expected": false
      },
      {
        "args": [
          "x4"
        ],
        "expected": false
      }
    ],
    "requiredBoolOps": [
      "And"
    ]
  },
  "5787": {
    "functionNames": [
      "text_starts_5_boolean"
    ],
    "tests": [
      {
        "args": [
          "5abc"
        ],
        "expected": true
      },
      {
        "args": [
          ""
        ],
        "expected": false
      },
      {
        "args": [
          "x5"
        ],
        "expected": false
      }
    ],
    "requiredBoolOps": [
      "And"
    ]
  },
  "5788": {
    "functionNames": [
      "valid_text_length_1"
    ],
    "tests": [
      {
        "args": [
          "python"
        ],
        "expected": true
      },
      {
        "args": [
          "x"
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
    "requiredBoolOps": [
      "And"
    ]
  },
  "5789": {
    "functionNames": [
      "valid_text_length_2"
    ],
    "tests": [
      {
        "args": [
          "python"
        ],
        "expected": true
      },
      {
        "args": [
          "x"
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
    "requiredBoolOps": [
      "And"
    ]
  },
  "5790": {
    "functionNames": [
      "valid_text_length_3"
    ],
    "tests": [
      {
        "args": [
          "python"
        ],
        "expected": true
      },
      {
        "args": [
          "x"
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
    "requiredBoolOps": [
      "And"
    ]
  },
  "5791": {
    "functionNames": [
      "valid_text_length_4"
    ],
    "tests": [
      {
        "args": [
          "python"
        ],
        "expected": true
      },
      {
        "args": [
          "x"
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
    "requiredBoolOps": [
      "And"
    ]
  },
  "5792": {
    "functionNames": [
      "valid_text_length_5"
    ],
    "tests": [
      {
        "args": [
          "python"
        ],
        "expected": true
      },
      {
        "args": [
          "x"
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
    "requiredBoolOps": [
      "And"
    ]
  },
  "5793": {
    "functionNames": [
      "exactly_one_above_1"
    ],
    "tests": [
      {
        "args": [
          2,
          1
        ],
        "expected": true
      },
      {
        "args": [
          3,
          4
        ],
        "expected": false
      },
      {
        "args": [
          0,
          1
        ],
        "expected": false
      }
    ]
  },
  "5794": {
    "functionNames": [
      "exactly_one_above_2"
    ],
    "tests": [
      {
        "args": [
          3,
          2
        ],
        "expected": true
      },
      {
        "args": [
          4,
          5
        ],
        "expected": false
      },
      {
        "args": [
          1,
          2
        ],
        "expected": false
      }
    ]
  },
  "5795": {
    "functionNames": [
      "exactly_one_above_3"
    ],
    "tests": [
      {
        "args": [
          4,
          3
        ],
        "expected": true
      },
      {
        "args": [
          5,
          6
        ],
        "expected": false
      },
      {
        "args": [
          2,
          3
        ],
        "expected": false
      }
    ]
  },
  "5796": {
    "functionNames": [
      "exactly_one_above_4"
    ],
    "tests": [
      {
        "args": [
          5,
          4
        ],
        "expected": true
      },
      {
        "args": [
          6,
          7
        ],
        "expected": false
      },
      {
        "args": [
          3,
          4
        ],
        "expected": false
      }
    ]
  },
  "5797": {
    "functionNames": [
      "exactly_one_above_5"
    ],
    "tests": [
      {
        "args": [
          6,
          5
        ],
        "expected": true
      },
      {
        "args": [
          7,
          8
        ],
        "expected": false
      },
      {
        "args": [
          4,
          5
        ],
        "expected": false
      }
    ]
  },
  "5798": {
    "functionNames": [
      "flags_ready_1"
    ],
    "tests": [
      {
        "args": [
          true,
          true,
          false
        ],
        "expected": true
      },
      {
        "args": [
          true,
          false,
          false
        ],
        "expected": false
      },
      {
        "args": [
          true,
          true,
          true
        ],
        "expected": false
      }
    ],
    "requiredBoolOps": [
      "And"
    ]
  },
  "5799": {
    "functionNames": [
      "flags_ready_2"
    ],
    "tests": [
      {
        "args": [
          true,
          true,
          false
        ],
        "expected": true
      },
      {
        "args": [
          true,
          false,
          false
        ],
        "expected": false
      },
      {
        "args": [
          true,
          true,
          true
        ],
        "expected": false
      }
    ],
    "requiredBoolOps": [
      "And"
    ]
  },
  "5800": {
    "functionNames": [
      "flags_ready_3"
    ],
    "tests": [
      {
        "args": [
          true,
          true,
          false
        ],
        "expected": true
      },
      {
        "args": [
          true,
          false,
          false
        ],
        "expected": false
      },
      {
        "args": [
          true,
          true,
          true
        ],
        "expected": false
      }
    ],
    "requiredBoolOps": [
      "And"
    ]
  },
  "5801": {
    "functionNames": [
      "flags_ready_4"
    ],
    "tests": [
      {
        "args": [
          true,
          true,
          false
        ],
        "expected": true
      },
      {
        "args": [
          true,
          false,
          false
        ],
        "expected": false
      },
      {
        "args": [
          true,
          true,
          true
        ],
        "expected": false
      }
    ],
    "requiredBoolOps": [
      "And"
    ]
  },
  "5802": {
    "functionNames": [
      "flags_ready_5"
    ],
    "tests": [
      {
        "args": [
          true,
          true,
          false
        ],
        "expected": true
      },
      {
        "args": [
          true,
          false,
          false
        ],
        "expected": false
      },
      {
        "args": [
          true,
          true,
          true
        ],
        "expected": false
      }
    ],
    "requiredBoolOps": [
      "And"
    ]
  },
  "5803": {
    "functionNames": [
      "score_band_1"
    ],
    "tests": [
      {
        "args": [
          10
        ],
        "expected": true
      },
      {
        "args": [
          31
        ],
        "expected": false
      },
      {
        "args": [
          20
        ],
        "expected": true
      }
    ],
    "requiredBoolOps": [
      "And"
    ]
  },
  "5804": {
    "functionNames": [
      "score_band_2"
    ],
    "tests": [
      {
        "args": [
          20
        ],
        "expected": true
      },
      {
        "args": [
          41
        ],
        "expected": false
      },
      {
        "args": [
          30
        ],
        "expected": true
      }
    ],
    "requiredBoolOps": [
      "And"
    ]
  },
  "5805": {
    "functionNames": [
      "score_band_3"
    ],
    "tests": [
      {
        "args": [
          30
        ],
        "expected": true
      },
      {
        "args": [
          51
        ],
        "expected": false
      },
      {
        "args": [
          40
        ],
        "expected": true
      }
    ],
    "requiredBoolOps": [
      "And"
    ]
  },
  "5806": {
    "functionNames": [
      "score_band_4"
    ],
    "tests": [
      {
        "args": [
          40
        ],
        "expected": true
      },
      {
        "args": [
          61
        ],
        "expected": false
      },
      {
        "args": [
          50
        ],
        "expected": true
      }
    ],
    "requiredBoolOps": [
      "And"
    ]
  },
  "5807": {
    "functionNames": [
      "score_band_5"
    ],
    "tests": [
      {
        "args": [
          50
        ],
        "expected": true
      },
      {
        "args": [
          71
        ],
        "expected": false
      },
      {
        "args": [
          60
        ],
        "expected": true
      }
    ],
    "requiredBoolOps": [
      "And"
    ]
  },
  "5808": {
    "functionNames": [
      "length_plus_1_builtin"
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
        "expected": 4
      },
      {
        "args": [
          []
        ],
        "expected": 1
      },
      {
        "args": [
          "code"
        ],
        "expected": 5
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "len",
        "minArgs": 0
      }
    ]
  },
  "5809": {
    "functionNames": [
      "length_plus_2_builtin"
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
        "expected": 5
      },
      {
        "args": [
          []
        ],
        "expected": 2
      },
      {
        "args": [
          "code"
        ],
        "expected": 6
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "len",
        "minArgs": 0
      }
    ]
  },
  "5810": {
    "functionNames": [
      "length_plus_3_builtin"
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
          []
        ],
        "expected": 3
      },
      {
        "args": [
          "code"
        ],
        "expected": 7
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "len",
        "minArgs": 0
      }
    ]
  },
  "5811": {
    "functionNames": [
      "length_plus_4_builtin"
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
        "expected": 4
      },
      {
        "args": [
          "code"
        ],
        "expected": 8
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "len",
        "minArgs": 0
      }
    ]
  },
  "5812": {
    "functionNames": [
      "length_plus_5_builtin"
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
        "expected": 5
      },
      {
        "args": [
          "code"
        ],
        "expected": 9
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "len",
        "minArgs": 0
      }
    ]
  },
  "5813": {
    "functionNames": [
      "sum_plus_1_builtin"
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
          [
            -2,
            5
          ]
        ],
        "expected": 4
      },
      {
        "args": [
          []
        ],
        "expected": 1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "sum",
        "minArgs": 0
      }
    ]
  },
  "5814": {
    "functionNames": [
      "sum_plus_2_builtin"
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
          [
            -2,
            5
          ]
        ],
        "expected": 5
      },
      {
        "args": [
          []
        ],
        "expected": 2
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "sum",
        "minArgs": 0
      }
    ]
  },
  "5815": {
    "functionNames": [
      "sum_plus_3_builtin"
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
          [
            -2,
            5
          ]
        ],
        "expected": 6
      },
      {
        "args": [
          []
        ],
        "expected": 3
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "sum",
        "minArgs": 0
      }
    ]
  },
  "5816": {
    "functionNames": [
      "sum_plus_4_builtin"
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
          [
            -2,
            5
          ]
        ],
        "expected": 7
      },
      {
        "args": [
          []
        ],
        "expected": 4
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "sum",
        "minArgs": 0
      }
    ]
  },
  "5817": {
    "functionNames": [
      "sum_plus_5_builtin"
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
          [
            -2,
            5
          ]
        ],
        "expected": 8
      },
      {
        "args": [
          []
        ],
        "expected": 5
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "sum",
        "minArgs": 0
      }
    ]
  },
  "5818": {
    "functionNames": [
      "safe_max_1_builtin"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            8,
            3
          ]
        ],
        "expected": 8
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
            -5,
            -2
          ]
        ],
        "expected": -2
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "max",
        "minArgs": 0
      }
    ]
  },
  "5819": {
    "functionNames": [
      "safe_max_2_builtin"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            8,
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
            -5,
            -2
          ]
        ],
        "expected": -2
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "max",
        "minArgs": 0
      }
    ]
  },
  "5820": {
    "functionNames": [
      "safe_max_3_builtin"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            8,
            3
          ]
        ],
        "expected": 8
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
            -5,
            -2
          ]
        ],
        "expected": -2
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "max",
        "minArgs": 0
      }
    ]
  },
  "5821": {
    "functionNames": [
      "safe_max_4_builtin"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            8,
            3
          ]
        ],
        "expected": 8
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
            -5,
            -2
          ]
        ],
        "expected": -2
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "max",
        "minArgs": 0
      }
    ]
  },
  "5822": {
    "functionNames": [
      "safe_max_5_builtin"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            8,
            3
          ]
        ],
        "expected": 8
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
            -5,
            -2
          ]
        ],
        "expected": -2
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "max",
        "minArgs": 0
      }
    ]
  },
  "5823": {
    "functionNames": [
      "safe_min_1_builtin"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            8,
            3
          ]
        ],
        "expected": 1
      },
      {
        "args": [
          []
        ],
        "expected": -1
      },
      {
        "args": [
          [
            -5,
            -2
          ]
        ],
        "expected": -5
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "min",
        "minArgs": 0
      }
    ]
  },
  "5824": {
    "functionNames": [
      "safe_min_2_builtin"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            8,
            3
          ]
        ],
        "expected": 1
      },
      {
        "args": [
          []
        ],
        "expected": -2
      },
      {
        "args": [
          [
            -5,
            -2
          ]
        ],
        "expected": -5
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "min",
        "minArgs": 0
      }
    ]
  },
  "5825": {
    "functionNames": [
      "safe_min_3_builtin"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            8,
            3
          ]
        ],
        "expected": 1
      },
      {
        "args": [
          []
        ],
        "expected": -3
      },
      {
        "args": [
          [
            -5,
            -2
          ]
        ],
        "expected": -5
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "min",
        "minArgs": 0
      }
    ]
  },
  "5826": {
    "functionNames": [
      "safe_min_4_builtin"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            8,
            3
          ]
        ],
        "expected": 1
      },
      {
        "args": [
          []
        ],
        "expected": -4
      },
      {
        "args": [
          [
            -5,
            -2
          ]
        ],
        "expected": -5
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "min",
        "minArgs": 0
      }
    ]
  },
  "5827": {
    "functionNames": [
      "safe_min_5_builtin"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            8,
            3
          ]
        ],
        "expected": 1
      },
      {
        "args": [
          []
        ],
        "expected": -5
      },
      {
        "args": [
          [
            -5,
            -2
          ]
        ],
        "expected": -5
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "min",
        "minArgs": 0
      }
    ]
  },
  "5828": {
    "functionNames": [
      "descending_marker_1_builtin"
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
          3,
          2,
          1,
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
            -1,
            4
          ]
        ],
        "expected": [
          4,
          -1,
          1
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "sorted",
        "minArgs": 0
      }
    ]
  },
  "5829": {
    "functionNames": [
      "descending_marker_2_builtin"
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
          3,
          2,
          1,
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
            -1,
            4
          ]
        ],
        "expected": [
          4,
          -1,
          2
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "sorted",
        "minArgs": 0
      }
    ]
  },
  "5830": {
    "functionNames": [
      "descending_marker_3_builtin"
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
          3,
          2,
          1,
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
            -1,
            4
          ]
        ],
        "expected": [
          4,
          -1,
          3
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "sorted",
        "minArgs": 0
      }
    ]
  },
  "5831": {
    "functionNames": [
      "descending_marker_4_builtin"
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
          3,
          2,
          1,
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
            -1,
            4
          ]
        ],
        "expected": [
          4,
          -1,
          4
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "sorted",
        "minArgs": 0
      }
    ]
  },
  "5832": {
    "functionNames": [
      "descending_marker_5_builtin"
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
          3,
          2,
          1,
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
            -1,
            4
          ]
        ],
        "expected": [
          4,
          -1,
          5
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "sorted",
        "minArgs": 0
      }
    ]
  },
  "5833": {
    "functionNames": [
      "round_to_1_builtin"
    ],
    "tests": [
      {
        "args": [
          3.1415926
        ],
        "expected": 3.1
      },
      {
        "args": [
          2.555555
        ],
        "expected": 2.6
      },
      {
        "args": [
          -1.234567
        ],
        "expected": -1.2
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "round",
        "minArgs": 0
      }
    ]
  },
  "5834": {
    "functionNames": [
      "round_to_2_builtin"
    ],
    "tests": [
      {
        "args": [
          3.1415926
        ],
        "expected": 3.14
      },
      {
        "args": [
          2.555555
        ],
        "expected": 2.56
      },
      {
        "args": [
          -1.234567
        ],
        "expected": -1.23
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "round",
        "minArgs": 0
      }
    ]
  },
  "5835": {
    "functionNames": [
      "round_to_3_builtin"
    ],
    "tests": [
      {
        "args": [
          3.1415926
        ],
        "expected": 3.142
      },
      {
        "args": [
          2.555555
        ],
        "expected": 2.556
      },
      {
        "args": [
          -1.234567
        ],
        "expected": -1.235
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "round",
        "minArgs": 0
      }
    ]
  },
  "5836": {
    "functionNames": [
      "round_to_4_builtin"
    ],
    "tests": [
      {
        "args": [
          3.1415926
        ],
        "expected": 3.1416
      },
      {
        "args": [
          2.555555
        ],
        "expected": 2.5556
      },
      {
        "args": [
          -1.234567
        ],
        "expected": -1.2346
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "round",
        "minArgs": 0
      }
    ]
  },
  "5837": {
    "functionNames": [
      "round_to_5_builtin"
    ],
    "tests": [
      {
        "args": [
          3.1415926
        ],
        "expected": 3.14159
      },
      {
        "args": [
          2.555555
        ],
        "expected": 2.55556
      },
      {
        "args": [
          -1.234567
        ],
        "expected": -1.23457
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "round",
        "minArgs": 0
      }
    ]
  },
  "5838": {
    "functionNames": [
      "distance_from_1_builtin"
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
          -3
        ],
        "expected": 4
      },
      {
        "args": [
          1
        ],
        "expected": 0
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "abs",
        "minArgs": 0
      }
    ]
  },
  "5839": {
    "functionNames": [
      "distance_from_2_builtin"
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
          -3
        ],
        "expected": 5
      },
      {
        "args": [
          2
        ],
        "expected": 0
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "abs",
        "minArgs": 0
      }
    ]
  },
  "5840": {
    "functionNames": [
      "distance_from_3_builtin"
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
          -3
        ],
        "expected": 6
      },
      {
        "args": [
          3
        ],
        "expected": 0
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "abs",
        "minArgs": 0
      }
    ]
  },
  "5841": {
    "functionNames": [
      "distance_from_4_builtin"
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
          -3
        ],
        "expected": 7
      },
      {
        "args": [
          4
        ],
        "expected": 0
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "abs",
        "minArgs": 0
      }
    ]
  },
  "5842": {
    "functionNames": [
      "distance_from_5_builtin"
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
          -3
        ],
        "expected": 8
      },
      {
        "args": [
          5
        ],
        "expected": 0
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "abs",
        "minArgs": 0
      }
    ]
  },
  "5843": {
    "functionNames": [
      "any_above_1_builtin"
    ],
    "tests": [
      {
        "args": [
          [
            0,
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
        "expected": false
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "any",
        "minArgs": 0
      }
    ]
  },
  "5844": {
    "functionNames": [
      "any_above_2_builtin"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            3
          ]
        ],
        "expected": true
      },
      {
        "args": [
          [
            2,
            1
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
    "requiredCallPatterns": [
      {
        "functionName": "any",
        "minArgs": 0
      }
    ]
  },
  "5845": {
    "functionNames": [
      "any_above_3_builtin"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            4
          ]
        ],
        "expected": true
      },
      {
        "args": [
          [
            3,
            2
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
    "requiredCallPatterns": [
      {
        "functionName": "any",
        "minArgs": 0
      }
    ]
  },
  "5846": {
    "functionNames": [
      "any_above_4_builtin"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            5
          ]
        ],
        "expected": true
      },
      {
        "args": [
          [
            4,
            3
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
    "requiredCallPatterns": [
      {
        "functionName": "any",
        "minArgs": 0
      }
    ]
  },
  "5847": {
    "functionNames": [
      "any_above_5_builtin"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            6
          ]
        ],
        "expected": true
      },
      {
        "args": [
          [
            5,
            4
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
    "requiredCallPatterns": [
      {
        "functionName": "any",
        "minArgs": 0
      }
    ]
  },
  "5848": {
    "functionNames": [
      "all_at_least_1_builtin"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            2
          ]
        ],
        "expected": true
      },
      {
        "args": [
          [
            -2,
            2
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
    "requiredCallPatterns": [
      {
        "functionName": "all",
        "minArgs": 0
      }
    ]
  },
  "5849": {
    "functionNames": [
      "all_at_least_2_builtin"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            2
          ]
        ],
        "expected": true
      },
      {
        "args": [
          [
            -3,
            2
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
    "requiredCallPatterns": [
      {
        "functionName": "all",
        "minArgs": 0
      }
    ]
  },
  "5850": {
    "functionNames": [
      "all_at_least_3_builtin"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            2
          ]
        ],
        "expected": true
      },
      {
        "args": [
          [
            -4,
            2
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
    "requiredCallPatterns": [
      {
        "functionName": "all",
        "minArgs": 0
      }
    ]
  },
  "5851": {
    "functionNames": [
      "all_at_least_4_builtin"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            2
          ]
        ],
        "expected": true
      },
      {
        "args": [
          [
            -5,
            2
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
    "requiredCallPatterns": [
      {
        "functionName": "all",
        "minArgs": 0
      }
    ]
  },
  "5852": {
    "functionNames": [
      "all_at_least_5_builtin"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            2
          ]
        ],
        "expected": true
      },
      {
        "args": [
          [
            -6,
            2
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
    "requiredCallPatterns": [
      {
        "functionName": "all",
        "minArgs": 0
      }
    ]
  },
  "5853": {
    "functionNames": [
      "zip_with_marker_1_builtin"
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
      },
      {
        "args": [
          [],
          []
        ],
        "expected": {
          "marker": 1
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "zip",
        "minArgs": 0
      }
    ]
  },
  "5854": {
    "functionNames": [
      "zip_with_marker_2_builtin"
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
      },
      {
        "args": [
          [],
          []
        ],
        "expected": {
          "marker": 2
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "zip",
        "minArgs": 0
      }
    ]
  },
  "5855": {
    "functionNames": [
      "zip_with_marker_3_builtin"
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
      },
      {
        "args": [
          [],
          []
        ],
        "expected": {
          "marker": 3
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "zip",
        "minArgs": 0
      }
    ]
  },
  "5856": {
    "functionNames": [
      "zip_with_marker_4_builtin"
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
      },
      {
        "args": [
          [],
          []
        ],
        "expected": {
          "marker": 4
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "zip",
        "minArgs": 0
      }
    ]
  },
  "5857": {
    "functionNames": [
      "zip_with_marker_5_builtin"
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
      },
      {
        "args": [
          [],
          []
        ],
        "expected": {
          "marker": 5
        }
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "zip",
        "minArgs": 0
      }
    ]
  },
  "5858": {
    "functionNames": [
      "unique_count_plus_1_set"
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
          [
            "a",
            "b",
            "a"
          ]
        ],
        "expected": 3
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5859": {
    "functionNames": [
      "unique_count_plus_2_set"
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
          [
            "a",
            "b",
            "a"
          ]
        ],
        "expected": 4
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5860": {
    "functionNames": [
      "unique_count_plus_3_set"
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
          [
            "a",
            "b",
            "a"
          ]
        ],
        "expected": 5
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5861": {
    "functionNames": [
      "unique_count_plus_4_set"
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
          [
            "a",
            "b",
            "a"
          ]
        ],
        "expected": 6
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5862": {
    "functionNames": [
      "unique_count_plus_5_set"
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
          [
            "a",
            "b",
            "a"
          ]
        ],
        "expected": 7
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5863": {
    "functionNames": [
      "union_marker_1_set"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ],
          [
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
          [],
          [
            4
          ]
        ],
        "expected": [
          1,
          4
        ]
      },
      {
        "args": [
          [
            1
          ],
          [
            1
          ]
        ],
        "expected": [
          1
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5864": {
    "functionNames": [
      "union_marker_2_set"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ],
          [
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
          [],
          [
            4
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
            2
          ],
          [
            2
          ]
        ],
        "expected": [
          2
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5865": {
    "functionNames": [
      "union_marker_3_set"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ],
          [
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
          [],
          [
            4
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
            3
          ],
          [
            3
          ]
        ],
        "expected": [
          3
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5866": {
    "functionNames": [
      "union_marker_4_set"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ],
          [
            2,
            3
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
            4
          ]
        ],
        "expected": [
          4
        ]
      },
      {
        "args": [
          [
            4
          ],
          [
            4
          ]
        ],
        "expected": [
          4
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5867": {
    "functionNames": [
      "union_marker_5_set"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ],
          [
            2,
            3
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
          [],
          [
            4
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
            5
          ],
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5868": {
    "functionNames": [
      "intersection_without_1_set"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3
          ],
          [
            2,
            3
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
          [
            1
          ]
        ],
        "expected": []
      },
      {
        "args": [
          [],
          [
            1
          ]
        ],
        "expected": []
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5869": {
    "functionNames": [
      "intersection_without_2_set"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3
          ],
          [
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
          [
            2
          ],
          [
            2
          ]
        ],
        "expected": []
      },
      {
        "args": [
          [],
          [
            1
          ]
        ],
        "expected": []
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5870": {
    "functionNames": [
      "intersection_without_3_set"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3
          ],
          [
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
            3
          ],
          [
            3
          ]
        ],
        "expected": []
      },
      {
        "args": [
          [],
          [
            1
          ]
        ],
        "expected": []
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5871": {
    "functionNames": [
      "intersection_without_4_set"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3
          ],
          [
            2,
            3
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
            4
          ],
          [
            4
          ]
        ],
        "expected": []
      },
      {
        "args": [
          [],
          [
            1
          ]
        ],
        "expected": []
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5872": {
    "functionNames": [
      "intersection_without_5_set"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3
          ],
          [
            2,
            3
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
            5
          ],
          [
            5
          ]
        ],
        "expected": []
      },
      {
        "args": [
          [],
          [
            1
          ]
        ],
        "expected": []
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5873": {
    "functionNames": [
      "difference_marker_1_set"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3
          ],
          [
            2
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
            1
          ],
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
          [],
          []
        ],
        "expected": [
          1
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5874": {
    "functionNames": [
      "difference_marker_2_set"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3
          ],
          [
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
            2
          ],
          [
            2
          ]
        ],
        "expected": [
          2
        ]
      },
      {
        "args": [
          [],
          []
        ],
        "expected": [
          2
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5875": {
    "functionNames": [
      "difference_marker_3_set"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3
          ],
          [
            2
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
            3
          ],
          [
            3
          ]
        ],
        "expected": [
          3
        ]
      },
      {
        "args": [
          [],
          []
        ],
        "expected": [
          3
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5876": {
    "functionNames": [
      "difference_marker_4_set"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3
          ],
          [
            2
          ]
        ],
        "expected": [
          1,
          3,
          4
        ]
      },
      {
        "args": [
          [
            4
          ],
          [
            4
          ]
        ],
        "expected": [
          4
        ]
      },
      {
        "args": [
          [],
          []
        ],
        "expected": [
          4
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5877": {
    "functionNames": [
      "difference_marker_5_set"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2,
            3
          ],
          [
            2
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
            5
          ],
          [
            5
          ]
        ],
        "expected": [
          5
        ]
      },
      {
        "args": [
          [],
          []
        ],
        "expected": [
          5
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5878": {
    "functionNames": [
      "symmetric_size_1_set"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ],
          [
            2,
            3
          ]
        ],
        "expected": 3
      },
      {
        "args": [
          [],
          []
        ],
        "expected": 1
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
        "expected": 3
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5879": {
    "functionNames": [
      "symmetric_size_2_set"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ],
          [
            2,
            3
          ]
        ],
        "expected": 4
      },
      {
        "args": [
          [],
          []
        ],
        "expected": 2
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
        "expected": 4
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5880": {
    "functionNames": [
      "symmetric_size_3_set"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ],
          [
            2,
            3
          ]
        ],
        "expected": 5
      },
      {
        "args": [
          [],
          []
        ],
        "expected": 3
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
        "expected": 5
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5881": {
    "functionNames": [
      "symmetric_size_4_set"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ],
          [
            2,
            3
          ]
        ],
        "expected": 6
      },
      {
        "args": [
          [],
          []
        ],
        "expected": 4
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
        "expected": 6
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5882": {
    "functionNames": [
      "symmetric_size_5_set"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ],
          [
            2,
            3
          ]
        ],
        "expected": 7
      },
      {
        "args": [
          [],
          []
        ],
        "expected": 5
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
        "expected": 7
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5883": {
    "functionNames": [
      "required_subset_1_set"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            1
          ],
          [
            1
          ]
        ],
        "expected": true
      },
      {
        "args": [
          [
            9
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
          [],
          []
        ],
        "expected": true
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5884": {
    "functionNames": [
      "required_subset_2_set"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ],
          [
            1
          ]
        ],
        "expected": true
      },
      {
        "args": [
          [
            9
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
          [],
          []
        ],
        "expected": true
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5885": {
    "functionNames": [
      "required_subset_3_set"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            3
          ],
          [
            1
          ]
        ],
        "expected": true
      },
      {
        "args": [
          [
            9
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
          [],
          []
        ],
        "expected": true
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5886": {
    "functionNames": [
      "required_subset_4_set"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            4
          ],
          [
            1
          ]
        ],
        "expected": true
      },
      {
        "args": [
          [
            9
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
          [],
          []
        ],
        "expected": true
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5887": {
    "functionNames": [
      "required_subset_5_set"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            5
          ],
          [
            1
          ]
        ],
        "expected": true
      },
      {
        "args": [
          [
            9
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
          [],
          []
        ],
        "expected": true
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5888": {
    "functionNames": [
      "disjoint_except_1_set"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            1
          ],
          [
            2,
            1
          ]
        ],
        "expected": true
      },
      {
        "args": [
          [
            1,
            2
          ],
          [
            2,
            3
          ]
        ],
        "expected": false
      },
      {
        "args": [
          [],
          [
            1
          ]
        ],
        "expected": true
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5889": {
    "functionNames": [
      "disjoint_except_2_set"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            2
          ],
          [
            2,
            2
          ]
        ],
        "expected": true
      },
      {
        "args": [
          [
            1,
            2
          ],
          [
            2,
            3
          ]
        ],
        "expected": true
      },
      {
        "args": [
          [],
          [
            2
          ]
        ],
        "expected": true
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5890": {
    "functionNames": [
      "disjoint_except_3_set"
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
            3
          ]
        ],
        "expected": true
      },
      {
        "args": [
          [
            1,
            2
          ],
          [
            2,
            3
          ]
        ],
        "expected": false
      },
      {
        "args": [
          [],
          [
            3
          ]
        ],
        "expected": true
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5891": {
    "functionNames": [
      "disjoint_except_4_set"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            4
          ],
          [
            2,
            4
          ]
        ],
        "expected": true
      },
      {
        "args": [
          [
            1,
            2
          ],
          [
            2,
            3
          ]
        ],
        "expected": false
      },
      {
        "args": [
          [],
          [
            4
          ]
        ],
        "expected": true
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5892": {
    "functionNames": [
      "disjoint_except_5_set"
    ],
    "tests": [
      {
        "args": [
          [
            1,
            5
          ],
          [
            2,
            5
          ]
        ],
        "expected": true
      },
      {
        "args": [
          [
            1,
            2
          ],
          [
            2,
            3
          ]
        ],
        "expected": false
      },
      {
        "args": [
          [],
          [
            5
          ]
        ],
        "expected": true
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5893": {
    "functionNames": [
      "unique_remainders_1_set"
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
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            -1,
            3
          ]
        ],
        "expected": [
          0,
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
  "5894": {
    "functionNames": [
      "unique_remainders_2_set"
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
          []
        ],
        "expected": []
      },
      {
        "args": [
          [
            -1,
            4
          ]
        ],
        "expected": [
          0,
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
  "5895": {
    "functionNames": [
      "unique_remainders_3_set"
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
          ]
        ],
        "expected": [
          0,
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
        "expected": []
      },
      {
        "args": [
          [
            -1,
            5
          ]
        ],
        "expected": [
          0,
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
  "5896": {
    "functionNames": [
      "unique_remainders_4_set"
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
            -1,
            6
          ]
        ],
        "expected": [
          0,
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
  "5897": {
    "functionNames": [
      "unique_remainders_5_set"
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
            -1,
            7
          ]
        ],
        "expected": [
          0,
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
  "5898": {
    "functionNames": [
      "letter_set_without_1"
    ],
    "tests": [
      {
        "args": [
          "a1ba"
        ],
        "expected": [
          "a",
          "b"
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
          "11x"
        ],
        "expected": [
          "x"
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5899": {
    "functionNames": [
      "letter_set_without_2"
    ],
    "tests": [
      {
        "args": [
          "a2ba"
        ],
        "expected": [
          "a",
          "b"
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
          "22x"
        ],
        "expected": [
          "x"
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5900": {
    "functionNames": [
      "letter_set_without_3"
    ],
    "tests": [
      {
        "args": [
          "a3ba"
        ],
        "expected": [
          "a",
          "b"
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
          "33x"
        ],
        "expected": [
          "x"
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5901": {
    "functionNames": [
      "letter_set_without_4"
    ],
    "tests": [
      {
        "args": [
          "a4ba"
        ],
        "expected": [
          "a",
          "b"
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
          "44x"
        ],
        "expected": [
          "x"
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5902": {
    "functionNames": [
      "letter_set_without_5"
    ],
    "tests": [
      {
        "args": [
          "a5ba"
        ],
        "expected": [
          "a",
          "b"
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
          "55x"
        ],
        "expected": [
          "x"
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "set",
        "minArgs": 0
      }
    ]
  },
  "5903": {
    "functionNames": [
      "set_values_at_least_1"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            1,
            2,
            1
          ]
        ],
        "expected": [
          1,
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
            -2,
            20
          ]
        ],
        "expected": [
          20
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
  "5904": {
    "functionNames": [
      "set_values_at_least_2"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            2,
            3,
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
            -2,
            20
          ]
        ],
        "expected": [
          20
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
  "5905": {
    "functionNames": [
      "set_values_at_least_3"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            3,
            4,
            3
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
            -2,
            20
          ]
        ],
        "expected": [
          20
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
  "5906": {
    "functionNames": [
      "set_values_at_least_4"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            4,
            5,
            4
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
            -2,
            20
          ]
        ],
        "expected": [
          20
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
  "5907": {
    "functionNames": [
      "set_values_at_least_5"
    ],
    "tests": [
      {
        "args": [
          [
            0,
            5,
            6,
            5
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
            -2,
            20
          ]
        ],
        "expected": [
          20
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
  "5908": {
    "functionNames": [
      "square_plus_1_comprehension"
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
          5,
          10
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
          5,
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
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "5909": {
    "functionNames": [
      "square_plus_2_comprehension"
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
          6,
          11
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
          6,
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
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "5910": {
    "functionNames": [
      "square_plus_3_comprehension"
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
          7,
          12
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
          7,
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
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "5911": {
    "functionNames": [
      "square_plus_4_comprehension"
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
          8,
          13
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
          8,
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
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "5912": {
    "functionNames": [
      "square_plus_5_comprehension"
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
          9,
          14
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
          9,
          5
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
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "5913": {
    "functionNames": [
      "divisible_1_comprehension"
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
          [
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
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "5914": {
    "functionNames": [
      "divisible_2_comprehension"
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
          [
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
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "5915": {
    "functionNames": [
      "divisible_3_comprehension"
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
          [
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
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "5916": {
    "functionNames": [
      "divisible_4_comprehension"
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
          [
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
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "5917": {
    "functionNames": [
      "divisible_5_comprehension"
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
          [
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
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "5918": {
    "functionNames": [
      "mapping_plus_1_comprehension"
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
          "2": 3
        }
      },
      {
        "args": [
          [
            -1,
            0
          ]
        ],
        "expected": {
          "0": 1,
          "-1": 0
        }
      },
      {
        "args": [
          []
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
  "5919": {
    "functionNames": [
      "mapping_plus_2_comprehension"
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
          "2": 4
        }
      },
      {
        "args": [
          [
            -1,
            0
          ]
        ],
        "expected": {
          "0": 2,
          "-1": 1
        }
      },
      {
        "args": [
          []
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
  "5920": {
    "functionNames": [
      "mapping_plus_3_comprehension"
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
          "2": 5
        }
      },
      {
        "args": [
          [
            -1,
            0
          ]
        ],
        "expected": {
          "0": 3,
          "-1": 2
        }
      },
      {
        "args": [
          []
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
  "5921": {
    "functionNames": [
      "mapping_plus_4_comprehension"
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
          "2": 6
        }
      },
      {
        "args": [
          [
            -1,
            0
          ]
        ],
        "expected": {
          "0": 4,
          "-1": 3
        }
      },
      {
        "args": [
          []
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
  "5922": {
    "functionNames": [
      "mapping_plus_5_comprehension"
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
          "2": 7
        }
      },
      {
        "args": [
          [
            -1,
            0
          ]
        ],
        "expected": {
          "0": 5,
          "-1": 4
        }
      },
      {
        "args": [
          []
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
  "5923": {
    "functionNames": [
      "remainder_1_comprehension"
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
          0,
          1,
          2
        ]
      },
      {
        "args": [
          [
            -1,
            3
          ]
        ],
        "expected": [
          0,
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
        "nodeType": "SetComp",
        "minCount": 1
      }
    ]
  },
  "5924": {
    "functionNames": [
      "remainder_2_comprehension"
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
          0,
          1,
          2,
          3
        ]
      },
      {
        "args": [
          [
            -1,
            4
          ]
        ],
        "expected": [
          0,
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
        "nodeType": "SetComp",
        "minCount": 1
      }
    ]
  },
  "5925": {
    "functionNames": [
      "remainder_3_comprehension"
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
            -1,
            5
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
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "SetComp",
        "minCount": 1
      }
    ]
  },
  "5926": {
    "functionNames": [
      "remainder_4_comprehension"
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
            -1,
            6
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
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "SetComp",
        "minCount": 1
      }
    ]
  },
  "5927": {
    "functionNames": [
      "remainder_5_comprehension"
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
            -1,
            7
          ]
        ],
        "expected": [
          0,
          6
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
        "nodeType": "SetComp",
        "minCount": 1
      }
    ]
  },
  "5928": {
    "functionNames": [
      "uppercase_long_1_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "python",
            "code"
          ]
        ],
        "expected": [
          "A",
          "PYTHON",
          "CODE"
        ]
      },
      {
        "args": [
          [
            "x"
          ]
        ],
        "expected": [
          "X"
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
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "5929": {
    "functionNames": [
      "uppercase_long_2_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "python",
            "code"
          ]
        ],
        "expected": [
          "PYTHON",
          "CODE"
        ]
      },
      {
        "args": [
          [
            "x"
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
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "5930": {
    "functionNames": [
      "uppercase_long_3_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "python",
            "code"
          ]
        ],
        "expected": [
          "PYTHON",
          "CODE"
        ]
      },
      {
        "args": [
          [
            "x"
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
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "5931": {
    "functionNames": [
      "uppercase_long_4_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "python",
            "code"
          ]
        ],
        "expected": [
          "PYTHON",
          "CODE"
        ]
      },
      {
        "args": [
          [
            "x"
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
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "5932": {
    "functionNames": [
      "uppercase_long_5_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "python",
            "code"
          ]
        ],
        "expected": [
          "PYTHON"
        ]
      },
      {
        "args": [
          [
            "x"
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
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "5933": {
    "functionNames": [
      "index_offset_1_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "b"
          ]
        ],
        "expected": {
          "1": "a",
          "2": "b"
        }
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": {
          "1": 9
        }
      },
      {
        "args": [
          []
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
  "5934": {
    "functionNames": [
      "index_offset_2_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "b"
          ]
        ],
        "expected": {
          "2": "a",
          "3": "b"
        }
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": {
          "2": 9
        }
      },
      {
        "args": [
          []
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
  "5935": {
    "functionNames": [
      "index_offset_3_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "b"
          ]
        ],
        "expected": {
          "3": "a",
          "4": "b"
        }
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": {
          "3": 9
        }
      },
      {
        "args": [
          []
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
  "5936": {
    "functionNames": [
      "index_offset_4_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "b"
          ]
        ],
        "expected": {
          "4": "a",
          "5": "b"
        }
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": {
          "4": 9
        }
      },
      {
        "args": [
          []
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
  "5937": {
    "functionNames": [
      "index_offset_5_comprehension"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "b"
          ]
        ],
        "expected": {
          "5": "a",
          "6": "b"
        }
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": {
          "5": 9
        }
      },
      {
        "args": [
          []
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
  "5938": {
    "functionNames": [
      "flatten_plus_1_comprehension"
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
          3,
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
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "5939": {
    "functionNames": [
      "flatten_plus_2_comprehension"
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
          4,
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
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "5940": {
    "functionNames": [
      "flatten_plus_3_comprehension"
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
          5,
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
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "5941": {
    "functionNames": [
      "flatten_plus_4_comprehension"
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
          6,
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
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "5942": {
    "functionNames": [
      "flatten_plus_5_comprehension"
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
          6,
          7,
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
        "nodeType": "ListComp",
        "minCount": 1
      }
    ]
  },
  "5943": {
    "functionNames": [
      "character_code_1_comprehension"
    ],
    "tests": [
      {
        "args": [
          "abc"
        ],
        "expected": [
          98,
          99,
          100
        ]
      },
      {
        "args": [
          "A"
        ],
        "expected": [
          66
        ]
      },
      {
        "args": [
          ""
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
  "5944": {
    "functionNames": [
      "character_code_2_comprehension"
    ],
    "tests": [
      {
        "args": [
          "abc"
        ],
        "expected": [
          99,
          100,
          101
        ]
      },
      {
        "args": [
          "A"
        ],
        "expected": [
          67
        ]
      },
      {
        "args": [
          ""
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
  "5945": {
    "functionNames": [
      "character_code_3_comprehension"
    ],
    "tests": [
      {
        "args": [
          "abc"
        ],
        "expected": [
          100,
          101,
          102
        ]
      },
      {
        "args": [
          "A"
        ],
        "expected": [
          68
        ]
      },
      {
        "args": [
          ""
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
  "5946": {
    "functionNames": [
      "character_code_4_comprehension"
    ],
    "tests": [
      {
        "args": [
          "abc"
        ],
        "expected": [
          101,
          102,
          103
        ]
      },
      {
        "args": [
          "A"
        ],
        "expected": [
          69
        ]
      },
      {
        "args": [
          ""
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
  "5947": {
    "functionNames": [
      "character_code_5_comprehension"
    ],
    "tests": [
      {
        "args": [
          "abc"
        ],
        "expected": [
          102,
          103,
          104
        ]
      },
      {
        "args": [
          "A"
        ],
        "expected": [
          70
        ]
      },
      {
        "args": [
          ""
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
  "5948": {
    "functionNames": [
      "pair_sum_above_1_comprehension"
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
          [
            1,
            2
          ],
          [
            1,
            4
          ],
          [
            3,
            2
          ],
          [
            3,
            4
          ]
        ]
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
        "expected": []
      },
      {
        "args": [
          [],
          [
            1
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
  "5949": {
    "functionNames": [
      "pair_sum_above_2_comprehension"
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
          [
            1,
            2
          ],
          [
            1,
            4
          ],
          [
            3,
            2
          ],
          [
            3,
            4
          ]
        ]
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
        "expected": []
      },
      {
        "args": [
          [],
          [
            1
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
  "5950": {
    "functionNames": [
      "pair_sum_above_3_comprehension"
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
          [
            1,
            4
          ],
          [
            3,
            2
          ],
          [
            3,
            4
          ]
        ]
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
        "expected": []
      },
      {
        "args": [
          [],
          [
            1
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
  "5951": {
    "functionNames": [
      "pair_sum_above_4_comprehension"
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
          [
            1,
            4
          ],
          [
            3,
            2
          ],
          [
            3,
            4
          ]
        ]
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
        "expected": []
      },
      {
        "args": [
          [],
          [
            1
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
  "5952": {
    "functionNames": [
      "pair_sum_above_5_comprehension"
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
          [
            3,
            4
          ]
        ]
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
        "expected": []
      },
      {
        "args": [
          [],
          [
            1
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
  "5953": {
    "functionNames": [
      "comparison_flags_1_comprehension"
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
          false,
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
            10
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
  "5954": {
    "functionNames": [
      "comparison_flags_2_comprehension"
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
          false,
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
            10
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
  "5955": {
    "functionNames": [
      "comparison_flags_3_comprehension"
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
          false,
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
            10
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
  "5956": {
    "functionNames": [
      "comparison_flags_4_comprehension"
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
          false,
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
            10
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
  "5957": {
    "functionNames": [
      "comparison_flags_5_comprehension"
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
          false,
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
            10
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
  "5958": {
    "functionNames": [
      "sum_plus_1_for"
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
            -2,
            5
          ]
        ],
        "expected": 4
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "5959": {
    "functionNames": [
      "sum_plus_2_for"
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
            -2,
            5
          ]
        ],
        "expected": 5
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "5960": {
    "functionNames": [
      "sum_plus_3_for"
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
            -2,
            5
          ]
        ],
        "expected": 6
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "5961": {
    "functionNames": [
      "sum_plus_4_for"
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
            -2,
            5
          ]
        ],
        "expected": 7
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "5962": {
    "functionNames": [
      "sum_plus_5_for"
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
            -2,
            5
          ]
        ],
        "expected": 8
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "5963": {
    "functionNames": [
      "count_divisible_1_for"
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
            2
          ]
        ],
        "expected": 1
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "5964": {
    "functionNames": [
      "count_divisible_2_for"
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
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "5965": {
    "functionNames": [
      "count_divisible_3_for"
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
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "5966": {
    "functionNames": [
      "count_divisible_4_for"
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
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "5967": {
    "functionNames": [
      "count_divisible_5_for"
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
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "5968": {
    "functionNames": [
      "square_offset_1_for"
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
          5,
          10
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
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "5969": {
    "functionNames": [
      "square_offset_2_for"
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
          6,
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
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "5970": {
    "functionNames": [
      "square_offset_3_for"
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
          7,
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
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "5971": {
    "functionNames": [
      "square_offset_4_for"
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
          8,
          13
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
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "5972": {
    "functionNames": [
      "square_offset_5_for"
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
          9,
          14
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
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "5973": {
    "functionNames": [
      "long_words_1_for"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "python",
            "code"
          ]
        ],
        "expected": [
          "a",
          "python",
          "code"
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
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "5974": {
    "functionNames": [
      "long_words_2_for"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "python",
            "code"
          ]
        ],
        "expected": [
          "python",
          "code"
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
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "5975": {
    "functionNames": [
      "long_words_3_for"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "python",
            "code"
          ]
        ],
        "expected": [
          "python",
          "code"
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
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "5976": {
    "functionNames": [
      "long_words_4_for"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "python",
            "code"
          ]
        ],
        "expected": [
          "python",
          "code"
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
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "5977": {
    "functionNames": [
      "long_words_5_for"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "python",
            "code"
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
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "5978": {
    "functionNames": [
      "positive_mapping_1_for"
    ],
    "tests": [
      {
        "args": [
          [
            -1,
            1,
            3
          ]
        ],
        "expected": {
          "1": 2,
          "3": 4
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
            2
          ]
        ],
        "expected": {
          "2": 3
        }
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "5979": {
    "functionNames": [
      "positive_mapping_2_for"
    ],
    "tests": [
      {
        "args": [
          [
            -1,
            1,
            3
          ]
        ],
        "expected": {
          "1": 3,
          "3": 5
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
            2
          ]
        ],
        "expected": {
          "2": 4
        }
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "5980": {
    "functionNames": [
      "positive_mapping_3_for"
    ],
    "tests": [
      {
        "args": [
          [
            -1,
            1,
            3
          ]
        ],
        "expected": {
          "1": 4,
          "3": 6
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
            2
          ]
        ],
        "expected": {
          "2": 5
        }
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "5981": {
    "functionNames": [
      "positive_mapping_4_for"
    ],
    "tests": [
      {
        "args": [
          [
            -1,
            1,
            3
          ]
        ],
        "expected": {
          "1": 5,
          "3": 7
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
            2
          ]
        ],
        "expected": {
          "2": 6
        }
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "5982": {
    "functionNames": [
      "positive_mapping_5_for"
    ],
    "tests": [
      {
        "args": [
          [
            -1,
            1,
            3
          ]
        ],
        "expected": {
          "1": 6,
          "3": 8
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
            2
          ]
        ],
        "expected": {
          "2": 7
        }
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "5983": {
    "functionNames": [
      "target_index_1_for"
    ],
    "tests": [
      {
        "args": [
          [
            4,
            7,
            7
          ],
          7
        ],
        "expected": 2
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
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "5984": {
    "functionNames": [
      "target_index_2_for"
    ],
    "tests": [
      {
        "args": [
          [
            4,
            7,
            7
          ],
          7
        ],
        "expected": 3
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
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "5985": {
    "functionNames": [
      "target_index_3_for"
    ],
    "tests": [
      {
        "args": [
          [
            4,
            7,
            7
          ],
          7
        ],
        "expected": 4
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
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "5986": {
    "functionNames": [
      "target_index_4_for"
    ],
    "tests": [
      {
        "args": [
          [
            4,
            7,
            7
          ],
          7
        ],
        "expected": 5
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
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "5987": {
    "functionNames": [
      "target_index_5_for"
    ],
    "tests": [
      {
        "args": [
          [
            4,
            7,
            7
          ],
          7
        ],
        "expected": 6
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
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "5988": {
    "functionNames": [
      "flatten_rows_1_for"
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
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "5989": {
    "functionNames": [
      "flatten_rows_2_for"
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
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "5990": {
    "functionNames": [
      "flatten_rows_3_for"
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
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "5991": {
    "functionNames": [
      "flatten_rows_4_for"
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
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "5992": {
    "functionNames": [
      "flatten_rows_5_for"
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
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "5993": {
    "functionNames": [
      "running_totals_1_for"
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
            -1,
            4
          ]
        ],
        "expected": [
          0,
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
  "5994": {
    "functionNames": [
      "running_totals_2_for"
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
            -1,
            4
          ]
        ],
        "expected": [
          1,
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
  "5995": {
    "functionNames": [
      "running_totals_3_for"
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
            -1,
            4
          ]
        ],
        "expected": [
          2,
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
  "5996": {
    "functionNames": [
      "running_totals_4_for"
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
          7,
          10
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
            -1,
            4
          ]
        ],
        "expected": [
          3,
          7
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
  "5997": {
    "functionNames": [
      "running_totals_5_for"
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
          8,
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
            -1,
            4
          ]
        ],
        "expected": [
          4,
          8
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
  "5998": {
    "functionNames": [
      "join_with_1_for"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "b"
          ]
        ],
        "expected": "a-1-b"
      },
      {
        "args": [
          [
            1
          ]
        ],
        "expected": "1"
      },
      {
        "args": [
          []
        ],
        "expected": ""
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "5999": {
    "functionNames": [
      "join_with_2_for"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "b"
          ]
        ],
        "expected": "a-2-b"
      },
      {
        "args": [
          [
            1
          ]
        ],
        "expected": "1"
      },
      {
        "args": [
          []
        ],
        "expected": ""
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "6000": {
    "functionNames": [
      "join_with_3_for"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "b"
          ]
        ],
        "expected": "a-3-b"
      },
      {
        "args": [
          [
            1
          ]
        ],
        "expected": "1"
      },
      {
        "args": [
          []
        ],
        "expected": ""
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "6001": {
    "functionNames": [
      "join_with_4_for"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "b"
          ]
        ],
        "expected": "a-4-b"
      },
      {
        "args": [
          [
            1
          ]
        ],
        "expected": "1"
      },
      {
        "args": [
          []
        ],
        "expected": ""
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "6002": {
    "functionNames": [
      "join_with_5_for"
    ],
    "tests": [
      {
        "args": [
          [
            "a",
            "b"
          ]
        ],
        "expected": "a-5-b"
      },
      {
        "args": [
          [
            1
          ]
        ],
        "expected": "1"
      },
      {
        "args": [
          []
        ],
        "expected": ""
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "6003": {
    "functionNames": [
      "count_digit_1_for"
    ],
    "tests": [
      {
        "args": [
          "1a1"
        ],
        "expected": 2
      },
      {
        "args": [
          "abc"
        ],
        "expected": 0
      },
      {
        "args": [
          ""
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "6004": {
    "functionNames": [
      "count_digit_2_for"
    ],
    "tests": [
      {
        "args": [
          "2a2"
        ],
        "expected": 2
      },
      {
        "args": [
          "abc"
        ],
        "expected": 0
      },
      {
        "args": [
          ""
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "6005": {
    "functionNames": [
      "count_digit_3_for"
    ],
    "tests": [
      {
        "args": [
          "3a3"
        ],
        "expected": 2
      },
      {
        "args": [
          "abc"
        ],
        "expected": 0
      },
      {
        "args": [
          ""
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "6006": {
    "functionNames": [
      "count_digit_4_for"
    ],
    "tests": [
      {
        "args": [
          "4a4"
        ],
        "expected": 2
      },
      {
        "args": [
          "abc"
        ],
        "expected": 0
      },
      {
        "args": [
          ""
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "6007": {
    "functionNames": [
      "count_digit_5_for"
    ],
    "tests": [
      {
        "args": [
          "5a5"
        ],
        "expected": 2
      },
      {
        "args": [
          "abc"
        ],
        "expected": 0
      },
      {
        "args": [
          ""
        ],
        "expected": 0
      }
    ],
    "requiredNodePatterns": [
      {
        "nodeType": "For",
        "minCount": 1
      }
    ]
  },
  "6008": {
    "functionNames": [
      "first_or_1_iterator"
    ],
    "tests": [
      {
        "args": [
          [
            9,
            2
          ]
        ],
        "expected": 9
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
        "expected": -1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      },
      {
        "functionName": "next",
        "minArgs": 0
      }
    ]
  },
  "6009": {
    "functionNames": [
      "first_or_2_iterator"
    ],
    "tests": [
      {
        "args": [
          [
            9,
            2
          ]
        ],
        "expected": 9
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
        "expected": -1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      },
      {
        "functionName": "next",
        "minArgs": 0
      }
    ]
  },
  "6010": {
    "functionNames": [
      "first_or_3_iterator"
    ],
    "tests": [
      {
        "args": [
          [
            9,
            2
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
        "expected": -1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      },
      {
        "functionName": "next",
        "minArgs": 0
      }
    ]
  },
  "6011": {
    "functionNames": [
      "first_or_4_iterator"
    ],
    "tests": [
      {
        "args": [
          [
            9,
            2
          ]
        ],
        "expected": 9
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
        "expected": -1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      },
      {
        "functionName": "next",
        "minArgs": 0
      }
    ]
  },
  "6012": {
    "functionNames": [
      "first_or_5_iterator"
    ],
    "tests": [
      {
        "args": [
          [
            9,
            2
          ]
        ],
        "expected": 9
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
        "expected": -1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      },
      {
        "functionName": "next",
        "minArgs": 0
      }
    ]
  },
  "6013": {
    "functionNames": [
      "second_or_1_iterator"
    ],
    "tests": [
      {
        "args": [
          [
            9,
            2,
            3
          ]
        ],
        "expected": 2
      },
      {
        "args": [
          [
            1
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
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      },
      {
        "functionName": "next",
        "minArgs": 0
      }
    ]
  },
  "6014": {
    "functionNames": [
      "second_or_2_iterator"
    ],
    "tests": [
      {
        "args": [
          [
            9,
            2,
            3
          ]
        ],
        "expected": 2
      },
      {
        "args": [
          [
            1
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
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      },
      {
        "functionName": "next",
        "minArgs": 0
      }
    ]
  },
  "6015": {
    "functionNames": [
      "second_or_3_iterator"
    ],
    "tests": [
      {
        "args": [
          [
            9,
            2,
            3
          ]
        ],
        "expected": 2
      },
      {
        "args": [
          [
            1
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
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      },
      {
        "functionName": "next",
        "minArgs": 0
      }
    ]
  },
  "6016": {
    "functionNames": [
      "second_or_4_iterator"
    ],
    "tests": [
      {
        "args": [
          [
            9,
            2,
            3
          ]
        ],
        "expected": 2
      },
      {
        "args": [
          [
            1
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
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      },
      {
        "functionName": "next",
        "minArgs": 0
      }
    ]
  },
  "6017": {
    "functionNames": [
      "second_or_5_iterator"
    ],
    "tests": [
      {
        "args": [
          [
            9,
            2,
            3
          ]
        ],
        "expected": 2
      },
      {
        "args": [
          [
            1
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
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      },
      {
        "functionName": "next",
        "minArgs": 0
      }
    ]
  },
  "6018": {
    "functionNames": [
      "take_1_iterator"
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
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      },
      {
        "functionName": "next",
        "minArgs": 0
      }
    ]
  },
  "6019": {
    "functionNames": [
      "take_2_iterator"
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
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      },
      {
        "functionName": "next",
        "minArgs": 0
      }
    ]
  },
  "6020": {
    "functionNames": [
      "take_3_iterator"
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
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      },
      {
        "functionName": "next",
        "minArgs": 0
      }
    ]
  },
  "6021": {
    "functionNames": [
      "take_4_iterator"
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
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      },
      {
        "functionName": "next",
        "minArgs": 0
      }
    ]
  },
  "6022": {
    "functionNames": [
      "take_5_iterator"
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
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      },
      {
        "functionName": "next",
        "minArgs": 0
      }
    ]
  },
  "6023": {
    "functionNames": [
      "iterator_sum_plus_1"
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
            -2,
            5
          ]
        ],
        "expected": 4
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      }
    ]
  },
  "6024": {
    "functionNames": [
      "iterator_sum_plus_2"
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
            -2,
            5
          ]
        ],
        "expected": 5
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      }
    ]
  },
  "6025": {
    "functionNames": [
      "iterator_sum_plus_3"
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
            -2,
            5
          ]
        ],
        "expected": 6
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      }
    ]
  },
  "6026": {
    "functionNames": [
      "iterator_sum_plus_4"
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
            -2,
            5
          ]
        ],
        "expected": 7
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      }
    ]
  },
  "6027": {
    "functionNames": [
      "iterator_sum_plus_5"
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
            -2,
            5
          ]
        ],
        "expected": 8
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      }
    ]
  },
  "6028": {
    "functionNames": [
      "skip_1_iterator"
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
          ],
          -1
        ],
        "expected": 2
      },
      {
        "args": [
          [
            9
          ],
          0
        ],
        "expected": 0
      },
      {
        "args": [
          [],
          7
        ],
        "expected": 7
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      },
      {
        "functionName": "next",
        "minArgs": 0
      }
    ]
  },
  "6029": {
    "functionNames": [
      "skip_2_iterator"
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
          ],
          -1
        ],
        "expected": 3
      },
      {
        "args": [
          [
            9
          ],
          0
        ],
        "expected": 0
      },
      {
        "args": [
          [],
          7
        ],
        "expected": 7
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      },
      {
        "functionName": "next",
        "minArgs": 0
      }
    ]
  },
  "6030": {
    "functionNames": [
      "skip_3_iterator"
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
          ],
          -1
        ],
        "expected": 4
      },
      {
        "args": [
          [
            9
          ],
          0
        ],
        "expected": 0
      },
      {
        "args": [
          [],
          7
        ],
        "expected": 7
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      },
      {
        "functionName": "next",
        "minArgs": 0
      }
    ]
  },
  "6031": {
    "functionNames": [
      "skip_4_iterator"
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
          ],
          -1
        ],
        "expected": 5
      },
      {
        "args": [
          [
            9
          ],
          0
        ],
        "expected": 0
      },
      {
        "args": [
          [],
          7
        ],
        "expected": 7
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      },
      {
        "functionName": "next",
        "minArgs": 0
      }
    ]
  },
  "6032": {
    "functionNames": [
      "skip_5_iterator"
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
          ],
          -1
        ],
        "expected": 6
      },
      {
        "args": [
          [
            9
          ],
          0
        ],
        "expected": 0
      },
      {
        "args": [
          [],
          7
        ],
        "expected": 7
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      },
      {
        "functionName": "next",
        "minArgs": 0
      }
    ]
  },
  "6033": {
    "functionNames": [
      "first_pair_1_iterator"
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
          9,
          1
        ]
      },
      {
        "args": [
          []
        ],
        "expected": [
          1,
          1
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      },
      {
        "functionName": "next",
        "minArgs": 0
      }
    ]
  },
  "6034": {
    "functionNames": [
      "first_pair_2_iterator"
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
          9,
          2
        ]
      },
      {
        "args": [
          []
        ],
        "expected": [
          2,
          2
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      },
      {
        "functionName": "next",
        "minArgs": 0
      }
    ]
  },
  "6035": {
    "functionNames": [
      "first_pair_3_iterator"
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
          9,
          3
        ]
      },
      {
        "args": [
          []
        ],
        "expected": [
          3,
          3
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      },
      {
        "functionName": "next",
        "minArgs": 0
      }
    ]
  },
  "6036": {
    "functionNames": [
      "first_pair_4_iterator"
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
          9,
          4
        ]
      },
      {
        "args": [
          []
        ],
        "expected": [
          4,
          4
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      },
      {
        "functionName": "next",
        "minArgs": 0
      }
    ]
  },
  "6037": {
    "functionNames": [
      "first_pair_5_iterator"
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
          9,
          5
        ]
      },
      {
        "args": [
          []
        ],
        "expected": [
          5,
          5
        ]
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      },
      {
        "functionName": "next",
        "minArgs": 0
      }
    ]
  },
  "6038": {
    "functionNames": [
      "iterator_count_plus_1"
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
        "expected": 4
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
            "a"
          ]
        ],
        "expected": 2
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      }
    ]
  },
  "6039": {
    "functionNames": [
      "iterator_count_plus_2"
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
        "expected": 5
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
            "a"
          ]
        ],
        "expected": 3
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      }
    ]
  },
  "6040": {
    "functionNames": [
      "iterator_count_plus_3"
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
          []
        ],
        "expected": 3
      },
      {
        "args": [
          [
            "a"
          ]
        ],
        "expected": 4
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      }
    ]
  },
  "6041": {
    "functionNames": [
      "iterator_count_plus_4"
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
        "expected": 4
      },
      {
        "args": [
          [
            "a"
          ]
        ],
        "expected": 5
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      }
    ]
  },
  "6042": {
    "functionNames": [
      "iterator_count_plus_5"
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
        "expected": 5
      },
      {
        "args": [
          [
            "a"
          ]
        ],
        "expected": 6
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      }
    ]
  },
  "6043": {
    "functionNames": [
      "last_or_1_iterator"
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
        "expected": 1
      },
      {
        "args": [
          [
            -1
          ]
        ],
        "expected": -1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      }
    ]
  },
  "6044": {
    "functionNames": [
      "last_or_2_iterator"
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
        "expected": 2
      },
      {
        "args": [
          [
            -1
          ]
        ],
        "expected": -1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      }
    ]
  },
  "6045": {
    "functionNames": [
      "last_or_3_iterator"
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
        "expected": 3
      },
      {
        "args": [
          [
            -1
          ]
        ],
        "expected": -1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      }
    ]
  },
  "6046": {
    "functionNames": [
      "last_or_4_iterator"
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
        "expected": 4
      },
      {
        "args": [
          [
            -1
          ]
        ],
        "expected": -1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      }
    ]
  },
  "6047": {
    "functionNames": [
      "last_or_5_iterator"
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
        "expected": 5
      },
      {
        "args": [
          [
            -1
          ]
        ],
        "expected": -1
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      }
    ]
  },
  "6048": {
    "functionNames": [
      "iterator_all_above_1"
    ],
    "tests": [
      {
        "args": [
          [
            2,
            3
          ]
        ],
        "expected": true
      },
      {
        "args": [
          [
            1,
            3
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
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      }
    ]
  },
  "6049": {
    "functionNames": [
      "iterator_all_above_2"
    ],
    "tests": [
      {
        "args": [
          [
            3,
            4
          ]
        ],
        "expected": true
      },
      {
        "args": [
          [
            2,
            4
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
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      }
    ]
  },
  "6050": {
    "functionNames": [
      "iterator_all_above_3"
    ],
    "tests": [
      {
        "args": [
          [
            4,
            5
          ]
        ],
        "expected": true
      },
      {
        "args": [
          [
            3,
            5
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
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      }
    ]
  },
  "6051": {
    "functionNames": [
      "iterator_all_above_4"
    ],
    "tests": [
      {
        "args": [
          [
            5,
            6
          ]
        ],
        "expected": true
      },
      {
        "args": [
          [
            4,
            6
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
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      }
    ]
  },
  "6052": {
    "functionNames": [
      "iterator_all_above_5"
    ],
    "tests": [
      {
        "args": [
          [
            6,
            7
          ]
        ],
        "expected": true
      },
      {
        "args": [
          [
            5,
            7
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
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      }
    ]
  },
  "6053": {
    "functionNames": [
      "indexed_from_1_iterator"
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
            1,
            "a"
          ],
          [
            2,
            "b"
          ]
        ]
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": [
          [
            1,
            9
          ]
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      }
    ]
  },
  "6054": {
    "functionNames": [
      "indexed_from_2_iterator"
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
            2,
            "a"
          ],
          [
            3,
            "b"
          ]
        ]
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": [
          [
            2,
            9
          ]
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      }
    ]
  },
  "6055": {
    "functionNames": [
      "indexed_from_3_iterator"
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
            3,
            "a"
          ],
          [
            4,
            "b"
          ]
        ]
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": [
          [
            3,
            9
          ]
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      }
    ]
  },
  "6056": {
    "functionNames": [
      "indexed_from_4_iterator"
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
            4,
            "a"
          ],
          [
            5,
            "b"
          ]
        ]
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": [
          [
            4,
            9
          ]
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      }
    ]
  },
  "6057": {
    "functionNames": [
      "indexed_from_5_iterator"
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
            5,
            "a"
          ],
          [
            6,
            "b"
          ]
        ]
      },
      {
        "args": [
          [
            9
          ]
        ],
        "expected": [
          [
            5,
            9
          ]
        ]
      },
      {
        "args": [
          []
        ],
        "expected": []
      }
    ],
    "requiredCallPatterns": [
      {
        "functionName": "iter",
        "minArgs": 0
      }
    ]
  }
};
